from __future__ import annotations

import ast
import csv
import importlib.util
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
OUT = WORK / "analysis"
TABLES = OUT / "decoded_tables"
CSV_OUT = OUT / "csv" / "sjw_talent_tier_scaling.csv"
REPORT_OUT = OUT / "reports" / "SJW_TALENT_TREE_TIER_SCALING.md"

MAIN = Path("/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/GameData")
CODEC_PATH = Path("/home/cryptologiq/SoloLevelingAR-SaveGameEditor/tools/gamedata_codec.py")

CSV_COLUMNS = [
    "TalentFamily",
    "TalentName",
    "NodeID",
    "ProgressionDepth",
    "VisualRow",
    "Rank",
    "Cost",
    "RequiredPathCost",
    "EffectType",
    "RawValue",
    "DisplayedValue",
    "MarginalGain",
    "GainPerPoint",
    "ParentNodeID",
    "BuffID",
    "PatternType",
    "Confidence",
]

STAT_LABELS = {
    "AttFR": "Attaque",
    "ArmFR": "Défense",
    "CriticalP": "Taux critique",
    "CriDamP": "Dégâts critiques",
    "ArmPen": "Pénétration de défense",
    "ArmPenP": "Pénétration de défense %",
    "PrecisionP": "Précision",
    "DamP": "Hausse des dégâts",
    "DamReduP": "Réduction des dégâts",
    "AddMMP": "PM max",
    "IncreaseMHP": "PV",
    "IncreaseDamageByTargetBuff": "Hausse des dégâts conditionnelle",
    "IncreaseDamageByTargetSpecialState": "Hausse des dégâts conditionnelle",
}

PERCENT_EFFECTS = {
    "AttFR",
    "ArmFR",
    "CriticalP",
    "CriDamP",
    "ArmPenP",
    "PrecisionP",
    "DamP",
    "DamReduP",
    "AddMMP",
    "IncreaseMHP",
    "IncreaseDamageByTargetBuff",
    "IncreaseDamageByTargetSpecialState",
}


def load_json(name: str):
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


def load_codec():
    spec = importlib.util.spec_from_file_location("gamedata_codec", CODEC_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {CODEC_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_table(table: str):
    codec = load_codec()
    cols, count, _ = codec.parse_file(MAIN / f"{table}.byte")
    return [{column: values[i] for column, values in cols.items()} for i in range(count)]


def load_text():
    rows = parse_table("TextData")
    return {
        row["StringID"]: row.get("Value_fra") or row.get("Value_eng") or row.get("Value") or row["StringID"]
        for row in rows
    }


def maybe_list(value):
    if value in ("", None):
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (int, float)):
        return [value]
    raw = str(value).strip()
    try:
        parsed = ast.literal_eval(raw)
    except (SyntaxError, ValueError):
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            return [] if not inner else [part.strip() for part in inner.split(",")]
        return [value]
    return parsed if isinstance(parsed, list) else [parsed]


def loc(value, text):
    if isinstance(value, str) and value in text:
        return text[value]
    return value or ""


def fmt_num(value):
    if value == "":
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def normalized_name(name: str) -> str:
    name = re.sub(r"\s+\d+$", "", name or "").strip()
    return name.replace("\xa0", " ")


def display_value(effect_type: str, raw):
    if raw == "":
        return "", None, "NON DÉTERMINÉ"
    if effect_type in PERCENT_EFFECTS:
        value = raw * 0.01
        return f"{fmt_num(value)}%", value, "FORTEMENT PROBABLE"
    return fmt_num(raw), None, "CONFIRMÉ PAR LES GAMEDATA; unité NON DÉTERMINÉE"


def effect_label(effect_type: str) -> str:
    return STAT_LABELS.get(effect_type, effect_type)


def first_numeric(options):
    for option in options:
        if option not in ("", None, 0):
            return option
    return 0


def node_effects(buff):
    effects = []
    for index in range(1, 4):
        etype = buff.get(f"AddedStatType{index}") or ""
        raw = buff.get(f"AddedStatValue{index}", 0)
        if etype and raw != 0:
            effects.append((etype, raw))
    for index in range(1, 4):
        state = buff.get(f"SpecialState{index}") or ""
        if not state:
            continue
        if state == "IncreaseMHP":
            raw = buff.get(f"SpecialState{index}OptionValue2", 0)
        elif state in {"IncreaseDamageByTargetBuff", "IncreaseDamageByTargetSpecialState"}:
            raw = buff.get(f"SpecialState{index}OptionValue3", 0)
        else:
            raw = first_numeric(
                [
                    buff.get(f"SpecialState{index}OptionValue2", 0),
                    buff.get(f"SpecialState{index}OptionValue1", 0),
                    buff.get(f"SpecialState{index}OptionValue3", 0),
                ]
            )
        if state in STAT_LABELS or raw != 0:
            effects.append((state, raw))
    return effects


def cost_for_rank(costs, rank):
    if not costs:
        return None
    if len(costs) == 1:
        return costs[0]
    if rank - 1 < len(costs):
        return costs[rank - 1]
    return None


def cost_confidence(costs, max_rank):
    if max_rank <= 1 or len(costs) == max_rank:
        return "CONFIRMÉ PAR LES GAMEDATA"
    if len(costs) == 1:
        return "FORTEMENT PROBABLE"
    return "NON DÉTERMINÉ"


def build_tab_maps(subtabs, mains, text):
    main_by_id = {}
    for row in mains:
        title = loc(row.get("SkillTreeTitle"), text)
        if isinstance(title, str) and title.startswith("ESkillTreeTab."):
            title = row.get("SkillTreeMainType", title)
        main_by_id[row["ID"]] = title

    group_to_tab = {}
    for sub in subtabs:
        groups = maybe_list(sub.get("NodeGroup"))
        titles = maybe_list(sub.get("NodeGroupTitle"))
        sub_title = sub.get("SubTabTitle_fra") or loc(sub.get("SubTabTitle"), text)
        main_title = main_by_id.get(sub.get("LinkSkillTreeMain"), str(sub.get("LinkSkillTreeMain")))
        for index, group in enumerate(groups):
            title_key = str(titles[index]) if index < len(titles) else ""
            group_to_tab[int(group)] = {
                "main": main_title,
                "sub": sub_title,
                "branch": loc(title_key, text) if title_key else f"Groupe {group}",
            }
    return group_to_tab


def compute_progression_depths(nodes):
    node_by_id = {str(node["ID"]): node for node in nodes if str(node.get("NodeDisplay")) == "True"}
    parent_map = {
        node_id: [str(parent) for parent in maybe_list(node.get("SlotLinkNodeID")) if str(parent)]
        for node_id, node in node_by_id.items()
    }
    missing = sorted({parent for parents in parent_map.values() for parent in parents if parent not in node_by_id})
    if missing:
        raise SystemExit("Parents inexistants dans CharPCSkillTreeNode: " + ", ".join(missing))

    depths = {}
    visiting = set()

    def depth(node_id):
        if node_id in depths:
            return depths[node_id]
        if node_id in visiting:
            raise SystemExit(f"Cycle détecté dans l'arbre de talents autour du NodeID {node_id}")
        visiting.add(node_id)
        parents = parent_map[node_id]
        value = 0 if not parents else 1 + max(depth(parent) for parent in parents)
        visiting.remove(node_id)
        depths[node_id] = value
        return value

    for node_id in node_by_id:
        depth(node_id)
    return depths


def path_cost(node_id, node_by_id, first_cost_by_id, visiting=None):
    if visiting is None:
        visiting = set()
    if node_id in visiting:
        return 0
    visiting.add(node_id)
    node = node_by_id.get(node_id)
    if not node:
        return 0
    total = 0
    for parent in maybe_list(node.get("SlotLinkNodeID")):
        try:
            parent_id = int(parent)
        except (TypeError, ValueError):
            continue
        total += first_cost_by_id.get(parent_id, 0)
        total += path_cost(parent_id, node_by_id, first_cost_by_id, visiting)
    return total


def classify_series(entries):
    node_entries = {}
    for entry in entries:
        if entry["Rank"] == 1:
            node_entries[entry["NodeID"]] = entry
    series = sorted(node_entries.values(), key=lambda row: (row["VisualRow"], row["NodeID"]))
    if len(series) < 2:
        return "NON DÉTERMINÉ", "une seule occurrence"
    if len({row["EffectType"] for row in series}) > 1:
        return "D. EFFETS NON COMPARABLES", "type d'effet variable"
    values = [row["_gain_numeric"] for row in series]
    costs = [row["_cost_numeric"] for row in series]
    visual_rows = [row["VisualRow"] for row in series]
    if any(value is None for value in values) or any(cost in (None, 0) for cost in costs):
        return "NON DÉTERMINÉ", "gain ou coût absent"
    ratios = [value / cost for value, cost in zip(values, costs)]
    ratio_constant = max(ratios) - min(ratios) < 1e-9
    gain_constant = max(values) - min(values) < 1e-9
    cost_constant = max(costs) - min(costs) < 1e-9
    gain_visual_linear = all(math.isclose(values[i] / visual_rows[i], values[0] / visual_rows[0]) for i in range(len(series)) if visual_rows[i])
    cost_visual_linear = all(math.isclose(costs[i] / visual_rows[i], costs[0] / visual_rows[0]) for i in range(len(series)) if visual_rows[i])
    increasing = all(ratios[i] <= ratios[i + 1] for i in range(len(ratios) - 1)) and any(
        ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1)
    )
    decreasing = all(ratios[i] >= ratios[i + 1] for i in range(len(ratios) - 1)) and any(
        ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1)
    )

    if ratio_constant and gain_visual_linear and cost_visual_linear:
        return "A. LISSAGE VISUEL / RENDEMENT CONSTANT", "bonus et coût proportionnels à la rangée visuelle"
    if ratio_constant and gain_constant and cost_constant:
        return "A. RENDEMENT CONSTANT, GAIN ET COÛT FIXES", "même bonus et même coût à chaque occurrence"
    if ratio_constant:
        return "A. RENDEMENT CONSTANT PARTIEL", "gain/coût constant sans proportion stricte à la rangée visuelle"
    if decreasing:
        return "B. RENDEMENT DÉCROISSANT", "gain par point décroissant"
    if increasing:
        return "C. RENDEMENT CROISSANT", "gain par point croissant"
    return "D. NON COMPARABLE / IRRÉGULIER", "rendement non monotone ou série irrégulière"


def make_rows():
    nodes = load_json("CharPCSkillTreeNode")
    buffs = {row["ID"]: row for row in load_json("ChComBuff")}
    subtabs = load_json("CharPCSkillTreelSubTab")
    mains = load_json("CharPCSkillTreelMainTab")
    contents = {row["ID"]: row for row in parse_table("ContentsUnlock")}
    text = load_text()
    tabs = build_tab_maps(subtabs, mains, text)
    progression_depths = compute_progression_depths(nodes)
    node_by_id = {row["ID"]: row for row in nodes}
    first_cost_by_id = {}
    for node in nodes:
        costs = maybe_list(node.get("LevelUpCostValue"))
        first = cost_for_rank(costs, 1)
        first_cost_by_id[node["ID"]] = first or 0

    rows = []
    for node in sorted(nodes, key=lambda r: (r["SkillTreelNodeGroup"], r["NodeTierY"], r["NodeTierX"], r["ID"])):
        if str(node.get("NodeDisplay")) != "True":
            continue
        buff = buffs.get(node.get("NodeValue"))
        if not buff:
            continue
        effects = node_effects(buff)
        if not effects:
            continue

        tab = tabs.get(
            int(node["SkillTreelNodeGroup"]),
            {"main": f"Groupe {node['SkillTreelNodeGroup']}", "sub": "", "branch": f"Groupe {node['SkillTreelNodeGroup']}"},
        )
        max_rank = int(node.get("NodeMaxLevel") or 1)
        costs = maybe_list(node.get("LevelUpCostValue"))
        cost_kind = node.get("LevelUpCost") or ""
        parent_ids = ",".join(str(parent) for parent in maybe_list(node.get("SlotLinkNodeID")))
        required_path = path_cost(node["ID"], node_by_id, first_cost_by_id)
        unlock_id = node.get("NodeContentsUnlock") or 0
        unlock = contents.get(unlock_id, {})
        required = ""
        if unlock:
            required = f"; prérequis {unlock.get('UnlockType')}:{unlock.get('Value')}"
        cost_note = cost_confidence(costs, max_rank)

        name = buff.get("BuffName_fra") or loc(buff.get("BuffName"), text)
        base_name = normalized_name(name)
        for effect_type, raw in effects:
            family = " / ".join(
                part
                for part in [
                    str(tab["main"]),
                    str(tab["sub"]),
                    str(tab["branch"]),
                    effect_label(effect_type),
                    normalized_name(base_name),
                ]
                if part
            )
            displayed, gain_number, effect_conf = display_value(effect_type, raw)
            for rank in range(1, max_rank + 1):
                direct_cost = cost_for_rank(costs, rank)
                cost_label = "" if direct_cost is None else f"{direct_cost} {cost_kind}".strip()
                gain_per_point = "NON DÉTERMINÉ"
                if direct_cost not in (None, 0) and gain_number is not None:
                    gain_per_point = fmt_num(gain_number / direct_cost)
                if max_rank > 1:
                    talent_name = f"{name} {rank}/{max_rank}"
                else:
                    talent_name = name
                confidence = effect_conf
                if cost_note != "CONFIRMÉ PAR LES GAMEDATA":
                    confidence = f"{confidence}; coût {cost_note}"
                rows.append(
                    {
                        "TalentFamily": family,
                        "TalentName": talent_name,
                        "NodeID": node["ID"],
                        "ProgressionDepth": progression_depths[str(node["ID"])],
                        "VisualRow": node["NodeTierY"],
                        "Rank": rank,
                        "Cost": cost_label,
                        "RequiredPathCost": required_path,
                        "EffectType": effect_type,
                        "RawValue": fmt_num(raw),
                        "DisplayedValue": displayed,
                        "MarginalGain": displayed,
                        "GainPerPoint": gain_per_point,
                        "ParentNodeID": parent_ids,
                        "BuffID": buff["ID"],
                        "PatternType": "",
                        "Confidence": confidence + required,
                        "_main": tab["main"],
                        "_sub": tab["sub"],
                        "_branch": tab["branch"],
                        "_x": node["NodeTierX"],
                        "_max_rank": max_rank,
                        "_gain_numeric": gain_number,
                        "_cost_numeric": direct_cost,
                    }
                )

    by_family = defaultdict(list)
    for row in rows:
        by_family[row["TalentFamily"]].append(row)
    family_notes = {}
    for family, entries in by_family.items():
        pattern, note = classify_series(entries)
        family_notes[family] = note
        for entry in entries:
            entry["PatternType"] = pattern
    return rows, family_notes


def write_csv(rows):
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in CSV_COLUMNS})


def stat_rows(rows, effects):
    return [row for row in rows if row["EffectType"] in effects and row["Rank"] == 1]


def family_table(lines, title, rows, limit=None):
    lines.extend(["", f"# {title}", "", "| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |", "|---|---:|---:|---:|---:|---|---:|---:|---:|---|"])
    count = 0
    for row in rows:
        if limit is not None and count >= limit:
            break
        lines.append(
            f"| {row['TalentFamily']} | {row['NodeID']} | {row['ProgressionDepth']} | {row['VisualRow']} | {row['Rank']} | "
            f"{row['Cost']} | {row['RequiredPathCost']} | {row['MarginalGain']} | "
            f"{row['GainPerPoint']} | {row['PatternType']} |"
        )
        count += 1


def write_report(rows, family_notes):
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    rank1 = [row for row in rows if row["Rank"] == 1]
    by_pattern = Counter()
    repeated_stats = Counter()
    family_rank1 = defaultdict(list)
    for row in rank1:
        family_rank1[row["TalentFamily"]].append(row)
    seen_families = set()
    for row in rank1:
        if row["TalentFamily"] in seen_families:
            continue
        seen_families.add(row["TalentFamily"])
        by_pattern[row["PatternType"]] += 1
    for family, entries in family_rank1.items():
        if len({row["NodeID"] for row in entries}) < 2:
            continue
        repeated_stats["Familles répétées analysées"] += 1
        pattern = entries[0]["PatternType"]
        costs = [row["_cost_numeric"] for row in entries if row["_cost_numeric"] not in (None, 0)]
        gains = [row["_gain_numeric"] for row in entries if row["_gain_numeric"] is not None]
        if len({row["EffectType"] for row in entries}) > 1:
            repeated_stats["effet différent selon la rangée visuelle"] += 1
        elif pattern == "A. LISSAGE VISUEL / RENDEMENT CONSTANT":
            repeated_stats["coût et gain proportionnels"] += 1
        elif pattern == "A. RENDEMENT CONSTANT, GAIN ET COÛT FIXES":
            repeated_stats["coût fixe et gain fixe"] += 1
        elif pattern.startswith("A."):
            repeated_stats["rendement constant partiel"] += 1
        elif pattern.startswith("B."):
            repeated_stats["coût croissant, gain moins rapide"] += 1
        elif pattern.startswith("C."):
            repeated_stats["coût croissant, gain plus rapide"] += 1
        elif len(costs) >= 2 and max(costs) == min(costs):
            repeated_stats["coût fixe, gain variable"] += 1
        elif len(gains) >= 2 and max(gains) == min(gains):
            repeated_stats["gain fixe, coût variable"] += 1
        else:
            repeated_stats["non comparables directement"] += 1
    attack = stat_rows(rows, {"AttFR"})
    crit = stat_rows(rows, {"CriticalP", "CriDamP"})
    pen = stat_rows(rows, {"ArmPen", "ArmPenP"})
    precision = stat_rows(rows, {"PrecisionP"})
    defense = stat_rows(rows, {"ArmFR"})
    hp = stat_rows(rows, {"IncreaseMHP"})
    other = [
        row
        for row in rank1
        if row["EffectType"] not in {"AttFR", "CriticalP", "CriDamP", "ArmPen", "ArmPenP", "PrecisionP", "ArmFR", "IncreaseMHP"}
    ]

    lines = [
        "# Résumé",
        "",
        "Cette passe sépare explicitement la **profondeur de progression** calculée depuis les parents, la **rangée visuelle** (`NodeTierY`) et le **rang réel** (`NodeMaxLevel`). "
        "Les familles sont regroupées par arbre/sous-onglet/branche/stat/nom normalisé, puis comparées sur les nœuds distincts au rang 1.",
        "",
        f"CSV: `analysis/csv/sjw_talent_tier_scaling.csv`",
        f"Lignes numériques exportées: {len(rows)}.",
        f"Familles analysées: {len(seen_families)}.",
        "",
        "# Profondeur, rangée visuelle et rang",
        "",
        "- Profondeur de progression: profondeur réelle du nœud dans le graphe Parent/Enfant.",
        "- Rangée visuelle: position verticale réelle du nœud dans `CharPCSkillTreeNode.NodeTierY`.",
        "- Rang: niveau interne d'un même nœud via `NodeMaxLevel`; il est exporté séparément dans la colonne `Rank`.",
        "- Deux nœuds avec la même stat à deux rangées visuelles différentes sont traités comme des talents distincts, même si leur nom se ressemble.",
        "",
        "# Vérification de l'hypothèse de lissage",
        "",
        "| Classification | Familles |",
        "|---|---:|",
    ]
    for pattern, count in by_pattern.most_common():
        lines.append(f"| {pattern} | {count} |")
    lines.extend(
        [
            "",
            "## Statistiques globales sur familles répétées",
            "",
            "| Mesure | Nombre |",
            "|---|---:|",
        ]
    )
    for label in [
        "Familles répétées analysées",
        "coût et gain proportionnels",
        "rendement constant partiel",
        "coût fixe et gain fixe",
        "coût fixe, gain variable",
        "gain fixe, coût variable",
        "coût croissant, gain moins rapide",
        "coût croissant, gain plus rapide",
        "effet différent selon la rangée visuelle",
        "non comparables directement",
    ]:
        lines.append(f"| {label} | {repeated_stats.get(label, 0)} |")
    lines.extend(
        [
            "",
            "Conclusion globale: l'observation est **vraie seulement pour certains nœuds**. "
            "Plusieurs familles en pourcentage gardent un rendement direct constant, mais les principales séries `+1/+2/+3...` observées ici deviennent irrégulières quand on vérifie toutes leurs rangées visuelles. Les valeurs brutes sans unité démontrée restent non comparables.",
            "",
            "# Attaque",
            "",
            "## Vérification de l'hypothèse Attaque",
            "",
            "| NodeID | Profondeur | Rangée visuelle | Position | Coût | Chemin requis | RawValue | DisplayValue | Gain/point | Parent | BuffID | Stat type | Pattern | Conclusion |",
            "|---:|---:|---:|---:|---|---:|---:|---:|---:|---|---:|---|---|---|",
        ]
    )
    for row in attack:
        conclusion = "talent distinct" if row["PatternType"] != "NON DÉTERMINÉ" else "isolé/non comparable"
        lines.append(
            f"| {row['NodeID']} | {row['ProgressionDepth']} | {row['VisualRow']} | {row['_x']} | {row['Cost']} | "
            f"{row['RequiredPathCost']} | {row['RawValue']} | {row['DisplayedValue']} | "
            f"{row['GainPerPoint']} | {row['ParentNodeID']} | {row['BuffID']} | "
            f"{row['EffectType']} | {row['PatternType']} | {conclusion} |"
        )
    lines.extend(
        [
            "",
            "Conclusion Attaque: **Observation vraie seulement pour certains nœuds**. "
            "Les nœuds `119101` à `119601` sont des talents distincts par rangée visuelle avec valeurs +1% à +6%, mais leur coût de rang 1 n'est pas toujours proportionnel à cette rangée. "
            "Les nœuds `31100102`, `31100302` et `31100502` répètent au contraire le même +1% pour 1 point à différentes profondeurs de progression.",
        ]
    )

    family_table(lines, "Critique", crit)
    family_table(lines, "Pénétration", pen)
    family_table(lines, "Précision", precision)
    family_table(lines, "Défense", defense)
    family_table(lines, "PV", hp)
    family_table(lines, "Autres stats", other, limit=80)

    for title, predicate in [
        ("Familles à rendement constant", lambda p: p.startswith("A.")),
        ("Familles à rendement décroissant", lambda p: p.startswith("B.")),
        ("Familles à rendement croissant", lambda p: p.startswith("C.")),
        ("Talents non comparables", lambda p: p.startswith("D.") or p == "NON DÉTERMINÉ"),
    ]:
        lines.extend(["", f"# {title}", ""])
        families = sorted({row["TalentFamily"] for row in rank1 if predicate(row["PatternType"])})
        for family in families:
            pattern = next(row["PatternType"] for row in rank1 if row["TalentFamily"] == family)
            note = family_notes.get(family, "")
            lines.append(f"- {family}: {pattern} ({note})")

    lines.extend(
        [
            "",
            "# Conséquences pour le build EXP",
            "",
            "- La priorité directe peut utiliser `GainPerPoint` uniquement quand l'unité du gain est démontrée, pas sur les valeurs brutes.",
            "- Deux nœuds donnant le même gain par point ont la même rentabilité directe; une rangée visuelle plus basse n'est pas automatiquement meilleure.",
            "- `RequiredPathCost` sépare le coût d'accès du coût direct. Il indique les points minimums explicitement reliés par les parents, mais ces prérequis donnent eux-mêmes des bonus et ne doivent pas être considérés comme perdus.",
            "- Les familles à rendement constant sont de bons candidats de remplissage stable pour leveling; les familles à rendement croissant peuvent devenir intéressantes une fois le chemin déjà ouvert.",
            "- Les effets conditionnels, bruts ou non comparables doivent être évalués selon le style de jeu et les conditions d'activation, pas uniquement par une formule gain/coût.",
        ]
    )
    REPORT_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    rows, family_notes = make_rows()
    write_csv(rows)
    write_report(rows, family_notes)
    print(f"wrote {CSV_OUT} ({len(rows)} rows)")
    print(f"wrote {REPORT_OUT}")


if __name__ == "__main__":
    main()
