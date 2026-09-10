from __future__ import annotations

import ast
import csv
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
TABLES = WORK / "analysis" / "decoded_tables"
FULL_CSV = WORK / "analysis" / "csv" / "sjw_talent_tree.csv"
DETAILED_CSV = WORK / "analysis" / "csv" / "sjw_talent_tree_detailed.csv"
HUMAN = WORK / "analysis" / "reports" / "SJW_TALENT_TREE_HUMAN.md"
TECH = WORK / "analysis" / "reports" / "SJW_TALENT_TREE_TECHNICAL.md"


CLASS_ORDER = ["Assassin", "Duelliste", "Magicien élémentaire", "Souverain"]
WEAPON_ORDER = ["Épée", "Dague", "Arc", "Arme à feu", "Focalisateur", "Arme d'hast", "Arme à deux mains"]
JINWOO_ORDER = ["Physique", "Éveil du monarque"]

EFFECT_LABELS = {
    "ActiveSkillReference": "Compétence active",
    "TriggeredBuff": "Effet déclenché",
    "PassiveNoNumericEffect": "Passif / Overdrive",
    "AttFR": "Attaque",
    "ArmFR": "Défense",
    "IncreaseMHP": "PV",
    "CriticalP": "Taux critique",
    "CriDamP": "Dégâts critiques",
    "ArmPen": "Pénétration",
    "ArmPenP": "Pénétration",
    "PrecisionP": "Précision",
    "DamP": "Dégâts infligés",
    "DamReduP": "Réduction des dégâts subis",
    "AddMMP": "PM max",
    "MPCostReduP": "Réduction coût MP",
    "EnhanceBackDamage": "Dégâts dans le dos",
    "EnhanceSkillDamage": "Dégâts de compétence",
    "BreakModifier": "Déséquilibre / Break",
    "SkillChange": "Modification de compétence",
    "ElementCumulativeDam": "Accumulation élémentaire",
    "IncreaseDamageByTargetBuff": "Dégâts contre cible affectée",
    "IncreaseDamageByTargetSpecialState": "Dégâts contre état spécial",
    "DamageOnReaction": "Dégâts contre réaction",
    "IncreaseDamageByEquipGs": "Dégâts de compétence d'arme",
    "BaseStatConversionOnSkillDamage": "Conversion stat -> dégâts",
    "DamageByDistance": "Dégâts selon distance",
    "WeaknessElementDamage": "Dégâts de faiblesse élémentaire",
    "EnhanceElementValue": "Valeur élémentaire",
    "EXGainRateAdd": "Gain de jauge",
    "PeriodGiveBuff": "Buff périodique",
    "SkillTreeMpCost": "Coût MP",
    "SkillTreeEnhance": "Amélioration de compétence",
}

OFFENSIVE_EFFECTS = {
    "AttFR",
    "CriticalP",
    "CriDamP",
    "ArmPen",
    "ArmPenP",
    "PrecisionP",
    "DamP",
    "EnhanceBackDamage",
    "EnhanceSkillDamage",
    "BreakModifier",
    "IncreaseDamageByEquipGs",
    "IncreaseDamageByTargetBuff",
    "IncreaseDamageByTargetSpecialState",
    "DamageOnReaction",
    "WeaknessElementDamage",
}

NUMERIC_GAIN_EFFECTS = {
    "AttFR",
    "ArmFR",
    "IncreaseMHP",
    "CriticalP",
    "CriDamP",
    "ArmPen",
    "ArmPenP",
    "PrecisionP",
    "DamP",
    "DamReduP",
    "AddMMP",
    "MPCostReduP",
    "EnhanceBackDamage",
    "EnhanceSkillDamage",
    "BreakModifier",
    "ElementCumulativeDam",
    "IncreaseDamageByTargetBuff",
    "IncreaseDamageByTargetSpecialState",
    "DamageOnReaction",
    "IncreaseDamageByEquipGs",
    "BaseStatConversionOnSkillDamage",
    "DamageByDistance",
    "WeaknessElementDamage",
    "EnhanceElementValue",
    "EXGainRateAdd",
    "SkillTreeMpCost",
    "SkillTreeEnhance",
}


def load_json(name: str):
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


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


def first_number(text: str):
    if not text:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(match.group(0)) if match else None


def fmt_number(value):
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def fr_text(value):
    text = str(value)
    text = re.sub(r"([+-]?\d+)\.(\d+)%", r"\1,\2 %", text)
    text = re.sub(r"([+-]?\d+)%", r"\1 %", text)
    text = re.sub(r"([+-]?\d+)\.(\d+) %/", r"\1,\2 %/", text)
    return text


def clean_name(name: str):
    name = (name or "").replace("\\n", " - ").replace("\n", " - ").replace("\xa0", " ").strip()
    name = re.sub(r"\s+[123456]\s*/\s*3$", "", name)
    return name


def ensure_source_csv():
    if not FULL_CSV.exists():
        subprocess.run(["python", "tools/analyze_sjw_talent_tree.py"], cwd=WORK, check=True)


def read_full_rows():
    ensure_source_csv()
    with FULL_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def system_for(main, sub, branch):
    if main == "SJWSkillTree":
        return "class", sub, branch, False
    if main == "GSSkillTree":
        return "weapon", sub, branch, False
    if main == "LordSkillTree":
        return "jinwoo", sub, branch, False
    if main == "Groupe 9":
        return "unattached", "Stats principales", "Stats principales", True
    if main == "Groupe 10":
        return "unattached", "Critique et pénétration", "Critique et pénétration", True
    return "unattached", "Structure non rattachée", branch or "Talents", True


def cost_summary(rows):
    costs_by_rank = defaultdict(list)
    units = []
    confidences = []
    for row in rows:
        if row["Cost"]:
            parts = row["Cost"].split()
            costs_by_rank[int(row["Rank"])].append(parts[0])
            units.append(" ".join(parts[1:]))
        confidences.append(row["Confidence"])
    unit = next((unit for unit in units if unit), "")
    ranks = sorted(costs_by_rank)
    costs = []
    for rank in ranks:
        values = sorted(set(costs_by_rank[rank]))
        costs.append(values[0] if len(values) == 1 else "/".join(values))
    if not costs:
        return "", None, False
    ambiguous = any("coût FORTEMENT PROBABLE" in conf or "coût NON" in conf for conf in confidences)
    max_rank = max(int(row["Rank"]) for row in rows if row["Rank"])
    if len(set(costs)) == 1:
        suffix = "/rang" if max_rank > 1 else ""
        label = f"{costs[0]} {unit}{suffix}".strip()
    else:
        label = " / ".join(costs) + (f" {unit}" if unit else "")
        ambiguous = True
    if ambiguous and len(set(costs)) > 1:
        label += " - interprétation NON DÉTERMINÉE"
    elif ambiguous:
        label += " - par rang probable"
    total = None if ambiguous and len(set(costs)) > 1 else sum(float(cost) for cost in costs if re.match(r"^-?\d+(\.\d+)?$", cost))
    return label, total, ambiguous


def cost_unit(rows):
    for row in rows:
        if row["Cost"]:
            parts = row["Cost"].split()
            if len(parts) > 1:
                return " ".join(parts[1:])
    return "pt"


def has_interpretable_gain(entry):
    return entry.get("Unit") == "%" and (entry.get("DisplayedValue") or "").endswith("%")


def effect_summary(rows):
    by_effect = defaultdict(list)
    for row in rows:
        by_effect[row["EffectType"]].append(row)
    chunks = []
    gain_values = []
    unresolved_numeric = False
    for effect_type, entries in sorted(by_effect.items()):
        label = EFFECT_LABELS.get(effect_type, effect_type)
        if effect_type not in NUMERIC_GAIN_EFFECTS:
            chunks.append(label)
            continue
        displays = []
        for entry in sorted(entries, key=lambda r: int(r["Rank"])):
            value = entry["DisplayedValue"] or entry["MarginalGain"] or entry["RawValue"]
            if value and value not in displays:
                displays.append(value)
        if displays:
            chunks.append(f"{label}: {' / '.join(displays)}")
        else:
            chunks.append(label)
        if len(displays) == 1 and all(has_interpretable_gain(entry) for entry in entries):
            gain_values.append(displays[0])
        elif displays:
            unresolved_numeric = True
    return "; ".join(chunks), gain_values, unresolved_numeric


def aggregate_nodes(rows):
    nodes = {str(row["ID"]): row for row in load_json("CharPCSkillTreeNode")}
    by_node = defaultdict(list)
    for row in rows:
        by_node[row["NodeID"]].append(row)

    talents = []
    for node_id, entries in by_node.items():
        node = nodes.get(node_id)
        if not node:
            continue
        sample = entries[0]
        system, section, branch, deduced = system_for(sample["MainTab"], sample["SubTab"], sample["Branch"])
        node_type = str(node.get("NodeType") or "")
        if system == "class" and node_type == "Identity":
            branch = "Nœud de classe / Overdrive"
        ranks = sorted({int(row["Rank"]) for row in entries if row["Rank"]})
        max_rank = max(ranks) if ranks else int(sample["MaxRank"] or 1)
        cost, total_cost, cost_ambiguous = cost_summary(entries)
        unit_cost = cost_unit(entries)
        effect, gain_values, unresolved_numeric = effect_summary(entries)
        gain = " / ".join(gain_values) if gain_values else ""
        if gain and not gain.startswith(("+", "-")):
            gain = "+" + gain
        numeric_gain = first_number(gain_values[0]) if len(set(gain_values)) == 1 and gain_values else None
        total_gain = ""
        gain_per_point = ""
        if numeric_gain is not None and max_rank:
            suffix = "%" if "%" in gain_values[0] else ""
            total_gain_num = numeric_gain * max_rank
            total_gain = f"+{fmt_number(total_gain_num)}{suffix}"
            if total_cost and not cost_ambiguous:
                gain_per_point = f"{fmt_number(total_gain_num / total_cost)}{suffix}/{unit_cost}"
            elif cost_ambiguous:
                gain_per_point = "NON DÉTERMINÉ"
        else:
            total_gain = gain or ("NON DÉTERMINÉ" if unresolved_numeric else "Non chiffré")
            gain_per_point = "NON DÉTERMINÉ"
        talents.append(
            {
                "system": system,
                "section": section,
                "branch": branch,
                "deduced": deduced,
                "node_type": node_type,
                "progression_depth": int(sample.get("ProgressionDepth") or 0),
                "visual_row": int(sample.get("VisualRow") or node.get("NodeTierY") or 0),
                "x": int(node.get("NodeTierX") or 0),
                "node_id": node_id,
                "parent": ",".join(str(v) for v in maybe_list(node.get("SlotLinkNodeID"))),
                "talent": clean_name(sample["TalentName"]),
                "effect": effect,
                "ranks": max_rank,
                "cost": cost,
                "gain": gain or ("NON DÉTERMINÉ" if unresolved_numeric else "Non chiffré"),
                "bonus_max": total_gain,
                "yield": gain_per_point,
                "access": human_access(sample.get("RequiredLevel")) or f"{required_path_cost(node_id, nodes)} pts requis",
                "buff_ids": ",".join(sorted({row["BuffID"] for row in entries if row["BuffID"]})),
                "effect_types": ",".join(sorted({row["EffectType"] for row in entries})),
                "confidence": "; ".join(sorted({row["Confidence"] for row in entries if row["Confidence"]})),
            }
        )
    return talents


def human_access(value):
    if not value:
        return ""
    if value.startswith("MainQuestChapter:"):
        return "Chapitre principal " + value.split(":", 1)[1]
    return value


def required_path_cost(node_id, nodes):
    seen = set()

    def walk(nid):
        if nid in seen:
            return 0
        seen.add(nid)
        node = nodes.get(str(nid))
        if not node:
            return 0
        total = 0
        for parent in maybe_list(node.get("SlotLinkNodeID")):
            parent = str(parent)
            parent_node = nodes.get(parent)
            if not parent_node:
                continue
            costs = maybe_list(parent_node.get("LevelUpCostValue"))
            try:
                total += float(costs[0]) if costs else 0
            except (TypeError, ValueError):
                pass
            total += walk(parent)
        return total

    value = walk(node_id)
    return fmt_number(value)


def write_detailed(talents):
    DETAILED_CSV.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(FULL_CSV, DETAILED_CSV)


def table(lines, talents):
    lines.extend(
        [
            "| Talent | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |",
            "|---|---|---:|---|---|---|---|---|",
        ]
    )
    for talent in sorted(talents, key=lambda t: (t["visual_row"], t["x"], t["node_id"])):
        lines.append(
            f"| {talent['talent']} | {fr_text(talent['effect'])} | {talent['ranks']} | {talent['cost']} | "
            f"{fr_text(talent['gain'])} | {fr_text(talent['bonus_max'])} | {fr_text(talent['yield'])} | {talent['access']} |"
        )
    lines.append("")


def branch_section(lines, branch_name, talents, number=None, deduced=False):
    suffix = " - nom déduit" if deduced else ""
    if number is None:
        title = f"### {branch_name}{suffix}"
    else:
        title = f"### Branche {number} — {branch_name}{suffix}"
    lines.extend([title, ""])
    by_depth = defaultdict(list)
    for talent in talents:
        by_depth[talent["progression_depth"]].append(talent)
    if not by_depth:
        lines.extend(["Aucun nœud identifié.", ""])
        return
    for depth in range(0, max(by_depth) + 1):
        lines.extend([f"#### Niveau de progression {depth + 1}", ""])
        if depth not in by_depth:
            lines.extend(["Aucun nœud identifié à ce niveau de progression.", ""])
            continue
        table(lines, by_depth[depth])


def render_system(lines, title, talents, order):
    lines.extend([f"# {title}", ""])
    by_section = defaultdict(list)
    for talent in talents:
        by_section[talent["section"]].append(talent)
    section_names = [name for name in order if name in by_section]
    section_names += sorted(name for name in by_section if name not in section_names)
    for section in section_names:
        lines.extend([f"## {section.upper()}", ""])
        by_branch = defaultdict(list)
        for talent in by_section[section]:
            by_branch[talent["branch"]].append(talent)
        sorted_branches = sorted(
            by_branch.items(),
            key=lambda kv: min(t["progression_depth"] * 100 + t["visual_row"] * 10 + t["x"] for t in kv[1]),
        )
        numbered_index = 1
        for branch, items in sorted_branches:
            if branch == "Nœud de classe / Overdrive":
                branch_section(lines, branch, items, None, any(t["deduced"] for t in items))
                continue
            branch_section(lines, branch, items, numbered_index, any(t["deduced"] for t in items))
            numbered_index += 1


def summary_by_system(talents):
    lines = [
        "# Résumé de l'arbre",
        "",
        "Ce rapport HUMAN présente les arbres de talents de Sung Jinwoo sous une forme lisible sur GitHub: topologie par système, branches, niveaux de progression, coûts, rangs, gains interprétés et rendements seulement lorsqu'ils sont démontrés.",
        "",
        "Validation: nœuds, parents, coûts, rangs, BuffID/SkillID et valeurs raw proviennent des GameData décodés. `ProgressionDepth` est calculé depuis les parents; `VisualRow` conserve la rangée UI `NodeTierY`. Les valeurs affichées en pourcentage restent marquées selon leur niveau de confiance; les valeurs brutes sans unité démontrée conservent un gain/rendement `NON DÉTERMINÉ`.",
        "",
        "Reste non déterminé: conversion runtime de certaines valeurs raw, ordre d'application des buffs, additivité exacte entre sources différentes et exclusivité éventuelle de certaines branches/classes/armes.",
        "",
        "## Sommaire",
        "",
    ]
    for system_key, title, order in [
        ("class", "Arbres de classe", CLASS_ORDER),
        ("weapon", "Arbres d'armes", WEAPON_ORDER),
        ("jinwoo", "Améliorations de Jinwoo", JINWOO_ORDER),
        ("unattached", "Structures non rattachées", []),
    ]:
        subset = [t for t in talents if t["system"] == system_key]
        if not subset:
            continue
        lines.append(f"{title}:")
        by_section = defaultdict(set)
        for talent in subset:
            by_section[talent["section"]].add(talent["branch"])
        names = [name for name in order if name in by_section]
        names += sorted(name for name in by_section if name not in names)
        for name in names:
            branches = " / ".join(sorted(by_section[name]))
            lines.append(f"- {name}: {branches}")
        lines.append("")
    return lines


def stat_index(lines, talents):
    lines.extend(["# Annexe - Index par statistique", ""])
    by_effect = defaultdict(list)
    for talent in talents:
        for effect in talent["effect_types"].split(","):
            if effect in OFFENSIVE_EFFECTS:
                by_effect[EFFECT_LABELS.get(effect, effect)].append(talent)
    for effect in sorted(by_effect):
        lines.extend([f"## {effect}", ""])
        for talent in sorted(by_effect[effect], key=lambda t: (t["system"], t["section"], t["branch"], t["progression_depth"], t["visual_row"], t["x"])):
            lines.append(
                f"- {talent['section']} / {talent['branch']} / Niveau {talent['progression_depth'] + 1}: "
                f"{talent['talent']} ({fr_text(talent['gain'])}, {fr_text(talent['yield'])})"
            )
        lines.append("")


def technical_reference(lines, talents):
    lines.extend(
        [
            "# Annexe - Traçabilité technique",
            "",
            f"- Talents représentés dans la vue principale: {len(talents)}.",
            "- Détails techniques complets: `SJW_TALENT_TREE_TECHNICAL.md`.",
            "- Données sources normalisées: `analysis/csv/sjw_talent_tree.csv` et `analysis/csv/sjw_talent_tree_detailed.csv`.",
            "",
        ]
    )


def write_human(talents):
    HUMAN.parent.mkdir(parents=True, exist_ok=True)
    lines = summary_by_system(talents)
    lines.extend(
        [
            "Lecture: le rapport est trié par arbre, puis branche, puis profondeur de progression calculée depuis les parents. La rangée visuelle `NodeTierY` n'est pas utilisée pour reconstruire les chemins.",
            "",
        ]
    )
    for system_key, title, order in [
        ("class", "ARBRES DE CLASSE", CLASS_ORDER),
        ("weapon", "ARBRES D'ARMES", WEAPON_ORDER),
        ("jinwoo", "AMÉLIORATIONS DE JINWOO", JINWOO_ORDER),
        ("unattached", "STRUCTURES NON RATTACHÉES", []),
    ]:
        subset = [t for t in talents if t["system"] == system_key]
        if subset:
            render_system(lines, title, subset, order)
    stat_index(lines, talents)
    technical_reference(lines, talents)
    HUMAN.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_technical(talents):
    TECH.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter(t["system"] for t in talents)
    lines = [
        "# SJW Talent Tree Technical",
        "",
        "Ce rapport justifie la reconstruction lisible de `SJW_TALENT_TREE_HUMAN.md`.",
        "",
        "## Sources externes secondaires",
        "",
        "- Backdash, `Solo Leveling Arise Overdrive Classes and Skill Trees guide`: https://thebackdash.com/gaming/solo-leveling-arise-overdrive-classes-and-skill-trees-guide/",
        "- GuideDragon, `Solo Leveling: Arise Overdrive - Classes & Builds explained`: https://guidedragon.de/en/guides-en/solo-leveling-arise-overdrive-classes-builds-explained-which-class-is-the-best/",
        "- AlcastHQ, `Best Sung Jinwoo Duelist Build Guide`: https://alcasthq.com/slao-duelist-build/",
        "- HaploGamingChef, `Top 5 Game-Changing Updates in Solo Leveling: ARISE Overdrive`: https://haplogamingchef.blogspot.com/2025/06/Top%205%20Game-Changing%20Updates%20in%20Solo%20Leveling%20ARISE%20Overdrive.html",
        "",
        "Ces sources ne sont utilisées que pour corroborer la structure visuelle. Les coûts, rangs, effets et valeurs viennent des GameData.",
        "",
        "## Modèle",
        "",
        "- Le rapport joueur agrège par `NodeID`: un nœud visuel = une ligne de talent.",
        "- Les effets multiples d'un même `NodeID`/`BuffID` sont regroupés dans la colonne `Effet`.",
        "- `ProgressionDepth`: profondeur réelle calculée depuis les relations Parent.",
        "- `VisualRow`: valeur GameData `NodeTierY`, utilisée seulement comme rangée visuelle.",
        "- Position horizontale: `NodeTierX`.",
        "- Rang: `NodeMaxLevel`, affiché comme nombre de rangs du talent.",
        "- Les groupes 9/10 ne sont pas forcés dans les classes; ils deviennent des structures non rattachées avec noms déduits.",
        "- Données détaillées vérifiables: `analysis/csv/sjw_talent_tree.csv` et `analysis/csv/sjw_talent_tree_detailed.csv`.",
        "",
        "## Talents agrégés",
        "",
        "| Système | Talents |",
        "|---|---:|",
    ]
    for system, count in counts.most_common():
        lines.append(f"| {system} | {count} |")
    lines.extend(
        [
            "",
            "## Contrôle qualité",
            "",
            "- La partie principale du rapport joueur est triée arbre -> branche -> profondeur de progression -> rangée visuelle -> position.",
            "- Les sections de rendement/statistiques sont déplacées en annexe.",
            "- `NodeID`, `BuffID`, noms de tables et groupes internes sont absents du corps principal.",
            "- Les détails `NodeID`/`BuffID` complets restent dans ce rapport technique, pas dans le rapport HUMAN.",
        ]
    )
    TECH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    rows = read_full_rows()
    talents = aggregate_nodes(rows)
    write_detailed(talents)
    write_human(talents)
    write_technical(talents)
    print(f"wrote {HUMAN}")
    print(f"wrote {DETAILED_CSV}")
    print(f"wrote {TECH}")


if __name__ == "__main__":
    main()
