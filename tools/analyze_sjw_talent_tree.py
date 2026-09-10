from __future__ import annotations

import ast
import csv
import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
OUT = WORK / "analysis"
TABLES = OUT / "decoded_tables"
CSV_OUT = OUT / "csv" / "sjw_talent_tree.csv"
REPORT_OUT = OUT / "reports" / "SJW_TALENT_TREE.md"
EFF_OUT = OUT / "reports" / "SJW_TALENT_TREE_COST_EFFICIENCY.md"

MAIN = Path("/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/GameData")
CODEC_PATH = Path("/home/cryptologiq/SoloLevelingAR-SaveGameEditor/tools/gamedata_codec.py")

CSV_COLUMNS = [
    "MainTab",
    "SubTab",
    "Branch",
    "TalentName",
    "LogicalTalentID",
    "LogicalTalentName",
    "LogicalRank",
    "LogicalGroupingEvidence",
    "NodeID",
    "Rank",
    "MaxRank",
    "Cost",
    "RequiredLevel",
    "ParentNodeID",
    "ProgressionDepth",
    "VisualRow",
    "EffectType",
    "RawValue",
    "DisplayedValue",
    "MarginalGain",
    "CumulativeGain",
    "Unit",
    "BuffID",
    "AbilityID",
    "Confidence",
]

STAT_LABELS = {
    "AttFR": "Attaque",
    "ArmFR": "Défense",
    "CriticalP": "Taux de coup critique",
    "CriDamP": "Dégâts de coup critique",
    "ArmPen": "Pénétration de défense",
    "ArmPenP": "Pénétration de défense",
    "DamP": "Dégâts infligés",
    "PrecisionP": "Précision",
    "DamReduP": "Réduction des dégâts",
    "AddMMP": "PM max",
    "MPR": "PM",
    "AddMP": "PM",
}

SPECIAL_LABELS = {
    "IncreaseMHP": "PV",
    "SkillTreeMpCost": "Coût MP",
    "SkillTreeEnhance": "Dégâts de compétence",
    "ChangeDamageOnElementType": "Dégâts élémentaires",
    "IncreaseDamageByTargetSpecialState": "Dégâts conditionnels",
    "IncreaseDamageByTargetBuff": "Dégâts conditionnels",
}

PERCENT_STATS = {
    "AttFR",
    "ArmFR",
    "CriticalP",
    "CriDamP",
    "ArmPenP",
    "DamP",
    "PrecisionP",
    "DamReduP",
}
RAW_STATS = {"ArmPen"}


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
    try:
        parsed = ast.literal_eval(str(value))
    except (SyntaxError, ValueError):
        raw = str(value).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            if not inner:
                return []
            return [part.strip() for part in inner.split(",")]
        return [value]
    return parsed if isinstance(parsed, list) else [parsed]


def loc(value, text):
    if not isinstance(value, str) or value == "":
        return value or ""
    if value in text:
        return text[value]
    return value


def clean_markup(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    return text.replace("\\n", " ").replace("\n", " ").strip()


def fmt_num(value):
    if value == "":
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def scaled_percent(raw):
    return raw * 0.01


def display_for_effect(effect_type: str, raw_value):
    if raw_value == "":
        return "", "", "NON DÉTERMINÉ"
    if effect_type in PERCENT_STATS:
        return f"{fmt_num(scaled_percent(raw_value))}%", "%", "FORTEMENT PROBABLE"
    if effect_type in RAW_STATS:
        return fmt_num(raw_value), "valeur brute", "CONFIRMÉ PAR LES GAMEDATA"
    if effect_type == "IncreaseMHP":
        return f"{fmt_num(scaled_percent(raw_value))}%", "%", "FORTEMENT PROBABLE"
    if effect_type in {"IncreaseDamageByTargetSpecialState", "IncreaseDamageByTargetBuff"}:
        return f"{fmt_num(scaled_percent(raw_value))}%", "%", "FORTEMENT PROBABLE"
    return fmt_num(raw_value), "valeur brute", "CONFIRMÉ PAR LES GAMEDATA"


def progress_for_effect(effect_type: str, raw_value, rank: int):
    display, unit, _ = display_for_effect(effect_type, raw_value)
    if unit != "%" or not isinstance(raw_value, (int, float)):
        return display, unit, "NON DÉTERMINÉ", "NON DÉTERMINÉ"
    marginal_display, _, _ = display_for_effect(effect_type, raw_value)
    cumulative_display, _, _ = display_for_effect(effect_type, raw_value * rank)
    return display, unit, marginal_display, cumulative_display


def cost_for_rank(cost_values, rank):
    if not cost_values:
        return ""
    if len(cost_values) == 1:
        return cost_values[0]
    if rank - 1 < len(cost_values):
        return cost_values[rank - 1]
    return ""


def cost_confidence(cost_values, max_rank):
    if max_rank <= 1 or len(cost_values) == max_rank:
        return "CONFIRMÉ PAR LES GAMEDATA"
    if len(cost_values) == 1:
        return "FORTEMENT PROBABLE"
    return "NON DÉTERMINÉ"


def build_tab_maps(subtabs, mains, text):
    main_by_id = {}
    for row in mains:
        title = loc(row.get("SkillTreeTitle"), text)
        if title.startswith("ESkillTreeTab."):
            title = row.get("SkillTreeMainType", title)
        main_by_id[row["ID"]] = title

    group_to_tab = {}
    for sub in subtabs:
        groups = maybe_list(sub.get("NodeGroup"))
        titles = maybe_list(sub.get("NodeGroupTitle"))
        sub_title = sub.get("SubTabTitle_fra") or loc(sub.get("SubTabTitle"), text)
        main_title = main_by_id.get(sub.get("LinkSkillTreeMain"), str(sub.get("LinkSkillTreeMain")))
        for index, group in enumerate(groups):
            key = titles[index] if index < len(titles) else ""
            group_to_tab[int(group)] = {
                "main": main_title,
                "sub": sub_title,
                "branch": loc(str(key), text) if key else f"Groupe {group}",
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


def node_effects(buff):
    effects = []
    if not buff:
        return effects
    for i in range(1, 4):
        etype = buff.get(f"AddedStatType{i}") or ""
        raw = buff.get(f"AddedStatValue{i}", 0)
        if etype and raw != 0:
            effects.append((etype, raw))
    for i in range(1, 4):
        state = buff.get(f"SpecialState{i}") or ""
        if not state:
            continue
        if state == "IncreaseMHP":
            raw = buff.get(f"SpecialState{i}OptionValue2", 0)
        elif state in {"IncreaseDamageByTargetSpecialState", "IncreaseDamageByTargetBuff"}:
            raw = buff.get(f"SpecialState{i}OptionValue3", 0)
        else:
            raw = buff.get(f"SpecialState{i}OptionValue2", 0) or buff.get(
                f"SpecialState{i}OptionValue1", 0
            )
        effects.append((state, raw))
    if not effects and buff.get("TriggeredBuffID"):
        effects.append(("TriggeredBuff", buff.get("TriggeredBuffID")))
    return effects


def label_for(effect_type):
    return STAT_LABELS.get(effect_type) or SPECIAL_LABELS.get(effect_type) or effect_type


def logical_talent_for_node(node, base_name: str, rank: int):
    node_id = str(node["ID"])
    return {
        "LogicalTalentID": f"node:{node_id}",
        "LogicalTalentName": base_name,
        "LogicalRank": rank,
        "LogicalGroupingEvidence": "RAW_NODE_ONLY",
    }


def validate_logical_rows(rows):
    node_to_logical = defaultdict(set)
    logical_rank_nodes = defaultdict(set)
    for row in rows:
        node_to_logical[str(row["NodeID"])].add(row["LogicalTalentID"])
        logical_rank_nodes[(row["LogicalTalentID"], str(row["LogicalRank"]))].add(str(row["NodeID"]))
    duplicated_nodes = sorted(node_id for node_id, logical_ids in node_to_logical.items() if len(logical_ids) > 1)
    if duplicated_nodes:
        raise SystemExit("NodeID associé à plusieurs talents logiques: " + ", ".join(duplicated_nodes))
    ambiguous_ranks = sorted(
        f"{logical_id} rang {rank}: {', '.join(sorted(node_ids))}"
        for (logical_id, rank), node_ids in logical_rank_nodes.items()
        if len(node_ids) > 1
    )
    if ambiguous_ranks:
        raise SystemExit("Rang logique associé à plusieurs NodeID sans validation: " + "; ".join(ambiguous_ranks))


def make_rows():
    nodes = load_json("CharPCSkillTreeNode")
    buffs = {row["ID"]: row for row in load_json("ChComBuff")}
    subtabs = load_json("CharPCSkillTreelSubTab")
    mains = load_json("CharPCSkillTreelMainTab")
    skill_rows = load_json("ChPCSkill")
    stat_desc = {row["EStatType"]: row for row in load_json("ChComStatDesc")}
    contents = {row["ID"]: row for row in parse_table("ContentsUnlock")}
    text = load_text()

    tabs = build_tab_maps(subtabs, mains, text)
    progression_depths = compute_progression_depths(nodes)
    skill_by_group = {}
    for row in skill_rows:
        skill_by_group.setdefault(row.get("SkillGroupID"), row)

    rows = []
    for node in sorted(nodes, key=lambda r: (r["SkillTreelNodeGroup"], r["NodeTierY"], r["NodeTierX"], r["ID"])):
        if str(node.get("NodeDisplay")) != "True":
            continue
        group = int(node["SkillTreelNodeGroup"])
        tab = tabs.get(group, {"main": f"Groupe {group}", "sub": "", "branch": f"Groupe {group}"})
        max_rank = int(node.get("NodeMaxLevel") or 1)
        costs = maybe_list(node.get("LevelUpCostValue"))
        cost_kind = node.get("LevelUpCost") or ""
        cost_note = cost_confidence(costs, max_rank)
        parent = ",".join(str(x) for x in maybe_list(node.get("SlotLinkNodeID")))
        unlock_id = node.get("NodeContentsUnlock") or 0
        required = ""
        if unlock_id:
            unlock = contents.get(unlock_id, {})
            required = f"{unlock.get('UnlockType','')}:{unlock.get('Value','')}".strip(":")

        node_type = node.get("NodeType")
        buff = buffs.get(node.get("NodeValue"))
        skill = skill_by_group.get(node.get("NodeValue"))
        ability_id = ""
        base_name = ""
        if buff:
            base_name = buff.get("BuffName_fra") or loc(buff.get("BuffName"), text)
            desc = clean_markup(buff.get("SkillDescBuff_fra") or loc(buff.get("SkillDescBuff"), text))
            effects = node_effects(buff)
            buff_id = buff["ID"]
        elif skill:
            base_name = loc(skill.get("SkillName"), text)
            desc = f"Référence compétence active: {node.get('NodeValue')}"
            effects = [("ActiveSkillReference", node.get("NodeValue"))]
            buff_id = ""
            ability_id = node.get("NodeValue")
        else:
            base_name = f"{node_type} {node.get('NodeValue')}"
            desc = ""
            effects = [(node_type, node.get("NodeValue"))]
            buff_id = ""
            ability_id = node.get("NodeValue")

        if not effects:
            effects = [("PassiveNoNumericEffect", "")]

        for rank in range(1, max_rank + 1):
            logical = logical_talent_for_node(node, base_name, rank)
            rank_cost = cost_for_rank(costs, rank)
            if rank_cost != "" and cost_kind:
                rank_cost = f"{rank_cost} {cost_kind}"
            rank_suffix = f" {rank}/{max_rank}" if max_rank > 1 else ""
            for effect_type, raw in effects:
                display, unit, effect_conf = display_for_effect(effect_type, raw)
                display, unit, marginal_display, cumulative_display = progress_for_effect(effect_type, raw, rank)
                confidence = effect_conf
                if cost_note != "CONFIRMÉ PAR LES GAMEDATA":
                    confidence = f"{confidence}; coût {cost_note}"
                if effect_type in stat_desc and unit == "%":
                    confidence = confidence.replace("FORTEMENT PROBABLE", "FORTEMENT PROBABLE")
                rows.append(
                    {
                        "MainTab": tab["main"],
                        "SubTab": tab["sub"],
                        "Branch": tab["branch"],
                        "TalentName": f"{base_name}{rank_suffix}",
                        **logical,
                        "NodeID": node["ID"],
                        "Rank": rank,
                        "MaxRank": max_rank,
                        "Cost": rank_cost,
                        "RequiredLevel": required,
                        "ParentNodeID": parent,
                        "ProgressionDepth": progression_depths[str(node["ID"])],
                        "VisualRow": node["NodeTierY"],
                        "EffectType": effect_type,
                        "RawValue": fmt_num(raw),
                        "DisplayedValue": display,
                        "MarginalGain": marginal_display,
                        "CumulativeGain": cumulative_display,
                        "Unit": unit,
                        "BuffID": buff_id,
                        "AbilityID": ability_id,
                        "Confidence": confidence,
                        "_desc": desc,
                        "_node_type": node_type,
                    }
                )
    return rows


def write_csv(rows):
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in CSV_COLUMNS})


def parse_cost(cost):
    if not cost:
        return None
    try:
        return float(str(cost).split()[0])
    except (ValueError, IndexError):
        return None


def cost_unit(cost):
    if not cost:
        return ""
    parts = str(cost).split()
    return " ".join(parts[1:])


def parse_display_percent(value):
    if not value or not str(value).endswith("%"):
        return None
    try:
        return float(str(value).rstrip("%"))
    except ValueError:
        return None


def stat_rows(rows):
    return [
        row
        for row in rows
        if row["EffectType"] in STAT_LABELS
        or row["EffectType"] in SPECIAL_LABELS
        or row["EffectType"] == "IncreaseMHP"
    ]


def attack_answer(rows):
    attack = [
        row
        for row in rows
        if row["NodeID"] == 31100102 and row["EffectType"] == "AttFR"
    ]
    if not attack:
        attack = [
            row
            for row in rows
            if row["EffectType"] == "AttFR" and row["MaxRank"] == 3
        ][:3]
    lines = [
        "## Réponse immédiate: Attaque 1/3 -> 3/3",
        "",
    ]
    for row in attack:
        lines.append(
            f"- Rang {row['Rank']}/{row['MaxRank']}: gain marginal {row['MarginalGain']}, "
            f"cumul {row['CumulativeGain']}, coût {row['Cost'] or 'non renseigné'}, "
            f"buff `{row['BuffID']}`."
        )
    lines.extend(
        [
            "",
            "Lecture: le nœud `31100102` applique le buff `200000086`, `AttFR=100`, "
            "`NodeMaxLevel=3`. La conversion d'affichage `0.01` est fortement appuyée "
            "par les textes de buffs du jeu: `100` correspond à `1%`. Le rang 3/3 donne "
            "donc `3%` cumulés si le moteur applique une instance/stack par rang.",
            "",
            "Statut: **FORTEMENT PROBABLE** pour `+1% par rang / +3% au rang 3`; "
            "**NON DÉTERMINÉ** pour l'ordre d'application runtime, l'additivité exacte "
            "entre sources différentes et la base exacte d'attaque affectée.",
            "",
        ]
    )
    return lines


def write_report(rows):
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    stats = stat_rows(rows)
    by_main = Counter(row["MainTab"] for row in rows)
    by_effect = Counter(row["EffectType"] for row in stats)
    max_nodes = len({row["NodeID"] for row in rows})
    numeric_nodes = len({row["NodeID"] for row in stats})
    node_rank_patterns = Counter()
    seen_nodes = {}
    for row in rows:
        seen_nodes.setdefault(row["NodeID"], []).append(row)
    for node_id, node_rows in seen_nodes.items():
        sample = node_rows[0]
        max_rank = int(sample["MaxRank"])
        sample_effect = sample["EffectType"]
        costs = [r["Cost"] for r in node_rows if r["EffectType"] == sample_effect]
        gains = [r["MarginalGain"] for r in node_rows if r["EffectType"] == sample_effect]
        if max_rank == 1 and sample["MarginalGain"]:
            node_rank_patterns["passif à rang unique avec gain numérique"] += 1
        elif max_rank == 1 and sample_effect == "ActiveSkillReference":
            node_rank_patterns["rang unique qui déverrouille/référence une compétence active"] += 1
        elif max_rank == 1 and sample_effect == "TriggeredBuff":
            node_rank_patterns["rang unique avec buff déclenché non chiffré directement"] += 1
        elif max_rank == 1:
            node_rank_patterns["rang unique sans gain numérique direct"] += 1
        elif len(set(gains)) == 1 and gains[0]:
            if len(set(costs)) == 1:
                node_rank_patterns["3 rangs, gain marginal fixe, coût plat"] += 1
            else:
                node_rank_patterns["3 rangs, gain marginal fixe, coût croissant"] += 1
        elif max_rank > 1:
            node_rank_patterns["plusieurs rangs, gain non numérique ou mixte"] += 1

    lines = [
        "# Sung Jinwoo - Talent Tree / Skill Tree",
        "",
        "Sources: `CharPCSkillTreeNode`, `CharPCSkillTreelMainTab`, "
        "`CharPCSkillTreelSubTab`, `CharPCStatAbility`, `ChComBuff`, "
        "`ChComStatDesc`, `TextData.byte`, `SysConst`.",
        "",
        f"CSV: `analysis/csv/sjw_talent_tree.csv`",
        "",
        f"Nœuds affichés reconstruits: {max_nodes}.",
        f"Nœuds avec effet numérique/stat lisible: {numeric_nodes}.",
        "",
        "Progression: `ProgressionDepth` est calculé depuis les relations Parent. `VisualRow` conserve la valeur GameData `NodeTierY` et décrit seulement la rangée dans l'interface.",
        "Talent logique: `LogicalTalentID` ajoute une couche au-dessus des NodeID. Par défaut, chaque NodeID reste son propre talent logique; un regroupement multi-NodeID exige une preuve explicite dans `LogicalGroupingEvidence`.",
        "",
    ]
    lines.extend(attack_answer(rows))
    lines.extend(
        [
            "## Structure globale",
            "",
            "| Arbre principal | Lignes exportées |",
            "|---|---:|",
        ]
    )
    for main, count in by_main.most_common():
        lines.append(f"| {main} | {count} |")
    lines.extend(["", "## 5 patterns d'amélioration les plus fréquents", ""])
    for pattern, count in node_rank_patterns.most_common(5):
        lines.append(f"- {pattern}: {count} nœuds")
    lines.extend(["", "## Effets de stat détectés", "", "| Effet | Lignes |", "|---|---:|"])
    for effect, count in by_effect.most_common():
        lines.append(f"| {label_for(effect)} (`{effect}`) | {count} |")

    lines.extend(
        [
            "",
            "## Talents de stats principaux",
            "",
            "| Arbre | Sous-onglet | Branche | Talent | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Effet | Gain marginal | Cumul | Confiance |",
            "|---|---|---|---|---:|---:|---:|---:|---|---|---:|---:|---|",
        ]
    )
    for row in stats:
        lines.append(
            f"| {row['MainTab']} | {row['SubTab']} | {row['Branch']} | "
            f"{row['TalentName']} | {row['NodeID']} | {row['ProgressionDepth']} | {row['VisualRow']} | {row['Rank']}/{row['MaxRank']} | "
            f"{row['Cost']} | {label_for(row['EffectType'])} | {row['MarginalGain']} | "
            f"{row['CumulativeGain']} | {row['Confidence']} |"
        )

    lines.extend(
        [
            "",
            "## Ce que les données confirment",
            "",
            "- **CONFIRMÉ PAR LES GAMEDATA**: `NodeValue` référence un buff ou une compétence; pour les talents de stat, le buff contient le type d'effet et la valeur brute.",
            "- **FORTEMENT PROBABLE**: pour les stats `AttFR`, `ArmFR`, `CriticalP`, `CriDamP`, `DamP`, `PrecisionP` et `IncreaseMHP`, la valeur affichée utilise `raw * 0.01%`, car de nombreux textes de buffs utilisent explicitement `{...,0.01}%`.",
            "- **FORTEMENT PROBABLE**: quand `NodeMaxLevel=3` et que le buff a une seule valeur brute, chaque rang réapplique le même gain marginal; le cumul est donc `raw * rang`.",
            "- **NON DÉTERMINÉ**: les données GameData seules ne prouvent pas si plusieurs sources de même stat sont additionnées avant ou après d'autres multiplicateurs runtime.",
            "- **NON DÉTERMINÉ**: la base exacte affectée par `AttFR` est nommée comme Attaque finale/ratio dans les tables (`FR`), mais l'ordre exact par rapport à attaque de base, arme, artefacts ou buffs temporaires n'est pas prouvé ici.",
            "- Les colonnes `LogicalTalentID`, `LogicalTalentName`, `LogicalRank` et `LogicalGroupingEvidence` séparent nœud GameData, talent logique et rang logique sans fusionner par nom.",
            "- Quand deux lignes CSV ont le même `NodeID`, le même rang et le même effet, cela correspond à plusieurs slots de buff/special state dans `ChComBuff`; les colonnes demandées ne prévoient pas de champ slot/cible séparé.",
            "- Les groupes `9` et `10` existent dans `CharPCSkillTreeNode`, mais aucun sous-onglet de `CharPCSkillTreelSubTab` ne les référence explicitement; ils restent donc libellés `Groupe 9/10` au lieu d'être rattachés artificiellement.",
            "",
            "## CharPCStatAbility",
            "",
            "`CharPCStatAbility` contient des courbes liées aux attributs de Jinwoo (`StrAbilityRate`, `VitAbilityRate`, etc.). Aucune liaison directe `NodeID -> CharPCStatAbility.ID` n'est présente dans `CharPCSkillTreeNode`; elle est donc référencée comme contexte, pas utilisée pour inventer des valeurs de talent.",
        ]
    )
    REPORT_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_efficiency(rows):
    EFF_OUT.parent.mkdir(parents=True, exist_ok=True)
    candidates = []
    for row in stat_rows(rows):
        cost = parse_cost(row["Cost"])
        if cost in (None, 0):
            continue
        if row.get("Unit") != "%":
            continue
        display_score = parse_display_percent(row["MarginalGain"])
        if display_score is None:
            continue
        display = row["MarginalGain"]
        score = display_score / cost
        candidates.append((score, row, display))

    by_effect = defaultdict(list)
    for score, row, display in candidates:
        by_effect[row["EffectType"]].append((score, row, display))

    lines = [
        "# Sung Jinwoo - Talent Tree Cost Efficiency",
        "",
        "Efficacité calculée uniquement quand coût et unité du gain marginal sont démontrés.",
        "Les valeurs brutes sans conversion validée restent exclues du classement.",
        "",
        "## Meilleurs gains par coût",
    ]
    by_currency = defaultdict(list)
    for score, row, display in candidates:
        by_currency[cost_unit(row["Cost"])].append((score, row, display))
    for currency in sorted(by_currency):
        lines.extend(
            [
                "",
                f"### {currency}",
                "",
                "| Effet | Talent | NodeID | Rang | Coût | Gain marginal | Score %/point | Confiance |",
                "|---|---|---:|---:|---|---:|---:|---|",
            ]
        )
        for score, row, display in sorted(by_currency[currency], key=lambda item: item[0], reverse=True)[:30]:
            lines.append(
                f"| {label_for(row['EffectType'])} | {row['TalentName']} | {row['NodeID']} | "
                f"{row['Rank']}/{row['MaxRank']} | {row['Cost']} | {display} | "
                f"{score:.4f} | {row['Confidence']} |"
            )

    lines.extend(["", "## Résumé par effet et monnaie", "", "| Monnaie | Effet | Lignes | Score %/point moyen |", "|---|---|---:|---:|"])
    by_currency_effect = defaultdict(list)
    for score, row, display in candidates:
        by_currency_effect[(cost_unit(row["Cost"]), row["EffectType"])].append((score, row, display))
    for (currency, effect), items in sorted(
        by_currency_effect.items(),
        key=lambda kv: (kv[0][0], -(sum(x[0] for x in kv[1]) / len(kv[1])), kv[0][1]),
    ):
        avg = sum(score for score, _, _ in items) / len(items)
        lines.append(f"| {currency} | {label_for(effect)} (`{effect}`) | {len(items)} | {avg:.4f} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Les nœuds avec `LevelUpCostValue=[1]` et `NodeMaxLevel=3` sont traités comme coût identique par rang: **FORTEMENT PROBABLE**, pas confirmé par une liste à trois valeurs.",
            "- Les monnaies de coût sont séparées: `SkillPoint`, `WeaponPoint`, `SpecialPoint` et `IdentityPoint` ne sont pas comparées entre elles.",
            "- L'efficacité ne compare pas les dégâts réels en combat: elle compare seulement les gains en pourcentage dont l'unité est interprétée.",
        ]
    )
    EFF_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    rows = make_rows()
    validate_logical_rows(rows)
    write_csv(rows)
    write_report(rows)
    write_efficiency(rows)
    print(f"wrote {CSV_OUT} ({len(rows)} rows)")
    print(f"wrote {REPORT_OUT}")
    print(f"wrote {EFF_OUT}")


if __name__ == "__main__":
    main()
