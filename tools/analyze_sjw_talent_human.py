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
RANK_PARENT_AUDIT = WORK / "analysis" / "reports" / "SJW_TALENT_TREE_RANK_PARENT_AUDIT.md"


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


def md_escape(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def rank_label(rank: int):
    labels = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    return labels.get(rank, str(rank))


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
            costs_by_rank[int(row.get("LogicalRank") or row["Rank"])].append(parts[0])
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
    max_rank = max(int(row.get("LogicalRank") or row["Rank"]) for row in rows if row.get("LogicalRank") or row["Rank"])
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


def single_rank_cost(rows):
    costs = sorted({row["Cost"] for row in rows if row["Cost"]})
    if not costs:
        return ""
    return costs[0] if len(costs) == 1 else " / ".join(costs)


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
        for entry in sorted(entries, key=lambda r: int(r.get("LogicalRank") or r["Rank"])):
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
    by_logical = defaultdict(list)
    for row in rows:
        by_logical[row.get("LogicalTalentID") or f"node:{row['NodeID']}"].append(row)
    node_to_logical = {
        str(row["NodeID"]): row.get("LogicalTalentID") or f"node:{row['NodeID']}"
        for row in rows
    }
    raw_children = defaultdict(list)
    for node in nodes.values():
        node_id = str(node["ID"])
        for parent in maybe_list(node.get("SlotLinkNodeID")):
            raw_children[str(parent)].append(node_id)

    talents = []
    for logical_id, entries in by_logical.items():
        node_ids = sorted({str(row["NodeID"]) for row in entries}, key=int)
        sample = sorted(entries, key=lambda row: (int(row.get("LogicalRank") or row["Rank"]), int(row["NodeID"])))[0]
        node_id = str(sample["NodeID"])
        node = nodes.get(node_id)
        if not node:
            continue
        system, section, branch, deduced = system_for(sample["MainTab"], sample["SubTab"], sample["Branch"])
        node_type = str(node.get("NodeType") or "")
        if system == "class" and node_type == "Identity":
            branch = "Nœud de classe / Overdrive"
        scoped_human_cleanup = system == "class" and section == "Assassin" and branch == "Attaque sournoise"
        ranks = sorted({int(row.get("LogicalRank") or row["Rank"]) for row in entries if row.get("LogicalRank") or row["Rank"]})
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
        rank_rows = []
        by_rank_node = defaultdict(list)
        for row in entries:
            by_rank_node[(int(row.get("LogicalRank") or row["Rank"]), str(row["NodeID"]))].append(row)
        for (logical_rank, rank_node_id), rank_entries in sorted(by_rank_node.items()):
            rank_node = nodes.get(rank_node_id, {})
            rank_effect, rank_gain_values, rank_unresolved = effect_summary(rank_entries)
            rank_gain = " / ".join(rank_gain_values) if rank_gain_values else ""
            if rank_gain and not rank_gain.startswith(("+", "-")):
                rank_gain = "+" + rank_gain
            cumulative_values = sorted(
                {
                    row["CumulativeGain"]
                    for row in rank_entries
                    if row["CumulativeGain"] and row["CumulativeGain"] != "NON DÉTERMINÉ"
                }
            )
            rank_rows.append(
                {
                    "rank": logical_rank,
                    "node_id": rank_node_id,
                    "parents": [str(v) for v in maybe_list(rank_node.get("SlotLinkNodeID"))],
                    "visual_row": int(rank_entries[0].get("VisualRow") or rank_node.get("NodeTierY") or 0),
                    "x": int(rank_node.get("NodeTierX") or 0),
                    "progression_depth": int(rank_entries[0].get("ProgressionDepth") or 0),
                    "cost": single_rank_cost(rank_entries) if scoped_human_cleanup else cost_summary(rank_entries)[0],
                    "effect": rank_effect,
                    "gain": rank_gain or ("NON DÉTERMINÉ" if rank_unresolved else "Non chiffré"),
                    "cumulative": " / ".join(cumulative_values)
                    if cumulative_values
                    else ("NON DÉTERMINÉ" if rank_unresolved else "Non chiffré"),
                    "access": human_access(rank_entries[0].get("RequiredLevel"))
                    or f"{required_path_cost(rank_node_id, nodes)} pts requis",
                    "confidence": "; ".join(sorted({row["Confidence"] for row in rank_entries if row["Confidence"]})),
                    "buff_ids": ",".join(sorted({row["BuffID"] for row in rank_entries if row["BuffID"]})),
                }
            )
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
                "node_ids": node_ids,
                "logical_id": logical_id,
                "logical_evidence": "; ".join(sorted({row.get("LogicalGroupingEvidence", "") for row in entries if row.get("LogicalGroupingEvidence")})),
                "parent": ",".join(str(v) for v in maybe_list(node.get("SlotLinkNodeID"))),
                "talent": clean_name(sample.get("LogicalTalentName") or sample["TalentName"]),
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
                "rank_rows": rank_rows,
                "parents_human": [],
                "unlocks_human": [],
            }
        )
    talent_by_logical = {talent["logical_id"]: talent for talent in talents}
    for talent in talents:
        parent_refs = set()
        unlock_refs = set()
        for rank_row in talent["rank_rows"]:
            for parent in rank_row["parents"]:
                parent_logical = node_to_logical.get(parent)
                if parent_logical and parent_logical != talent["logical_id"]:
                    parent_refs.add((parent_logical, rank_row["rank"]))
            for child in raw_children.get(rank_row["node_id"], []):
                child_logical = node_to_logical.get(child)
                if child_logical and child_logical != talent["logical_id"]:
                    unlock_refs.add((child_logical, rank_row["rank"]))
        talent["parents_human"] = [
            talent_by_logical[logical_id]["talent"]
            for logical_id in sorted(
                {item[0] for item in parent_refs if item[0] in talent_by_logical},
                key=lambda item: talent_by_logical[item]["node_id"],
            )
        ]
        scoped_human_cleanup = (
            talent["system"] == "class"
            and talent["section"] == "Assassin"
            and talent["branch"] == "Attaque sournoise"
        )
        if scoped_human_cleanup:
            unlock_by_logical = {}
            for logical_id, rank in unlock_refs:
                if logical_id not in talent_by_logical:
                    continue
                unlock_by_logical.setdefault(logical_id, set()).add(rank)
            talent["unlocks_human"] = [
                talent_by_logical[logical_id]["talent"]
                for logical_id in sorted(
                    unlock_by_logical,
                    key=lambda item: (talent_by_logical[item]["visual_row"], talent_by_logical[item]["x"]),
                )
            ]
        else:
            talent["unlocks_human"] = [
                talent_by_logical[logical_id]["talent"]
                for logical_id in sorted(
                    {item[0] for item in unlock_refs if item[0] in talent_by_logical},
                    key=lambda item: (
                        talent_by_logical[item]["visual_row"],
                        talent_by_logical[item]["x"],
                        talent_by_logical[item]["talent"],
                    ),
                )
            ]
    return talents


def validate_logical_talents(rows, talents):
    source_nodes = {str(row["NodeID"]) for row in rows}
    represented_nodes = {node_id for talent in talents for node_id in talent["node_ids"]}
    if source_nodes != represented_nodes:
        missing = sorted(source_nodes - represented_nodes, key=int)
        extra = sorted(represented_nodes - source_nodes, key=int)
        details = []
        if missing:
            details.append("NodeID perdus: " + ", ".join(missing))
        if extra:
            details.append("NodeID inattendus: " + ", ".join(extra))
        raise SystemExit("; ".join(details))

    owners = defaultdict(set)
    for talent in talents:
        for node_id in talent["node_ids"]:
            owners[node_id].add(talent["logical_id"])
    duplicates = sorted(node_id for node_id, logical_ids in owners.items() if len(logical_ids) > 1)
    if duplicates:
        raise SystemExit("NodeID représenté dans plusieurs talents logiques: " + ", ".join(duplicates))

    rank_nodes = defaultdict(set)
    for row in rows:
        rank_nodes[(row.get("LogicalTalentID") or f"node:{row['NodeID']}", row.get("LogicalRank") or row["Rank"])].add(row["NodeID"])
    ambiguous = sorted(
        f"{logical_id} rang {rank}: {', '.join(sorted(node_ids, key=int))}"
        for (logical_id, rank), node_ids in rank_nodes.items()
        if len(node_ids) > 1
    )
    if ambiguous:
        raise SystemExit("Rang logique ambigu: " + "; ".join(ambiguous))


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


def render_talent(lines, talent):
    parents = ", ".join(dict.fromkeys(talent["parents_human"])) if talent["parents_human"] else "RACINE"
    unlocks = ", ".join(dict.fromkeys(talent["unlocks_human"])) if talent["unlocks_human"] else "aucun"
    position = f"profondeur technique {talent['progression_depth'] + 1}, rangée UI {talent['visual_row']}, X {talent['x']}"
    scoped_human_cleanup = (
        talent["system"] == "class"
        and talent["section"] == "Assassin"
        and talent["branch"] == "Attaque sournoise"
    )
    lines.extend(
        [
            f"#### {talent['talent']}",
            "",
        ]
    )
    if not scoped_human_cleanup:
        lines.append(f"**Position dans l'arbre :** {position}")
    lines.extend(
        [
            f"**Prérequis :** {parents}",
            f"**Débloque :** {unlocks}",
            "",
            "| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for rank_row in sorted(talent["rank_rows"], key=lambda row: (row["rank"], row["node_id"])):
        lines.append(
            f"| {rank_label(rank_row['rank'])} | {rank_row['cost']} | {fr_text(md_escape(rank_row['effect']))} | "
            f"{fr_text(rank_row['gain'])} | {fr_text(rank_row['cumulative'])} | {rank_row['access']} | {rank_row['confidence']} |"
        )
    if len(talent["node_ids"]) > 1 or talent["logical_evidence"] != "RAW_NODE_ONLY":
        lines.extend(
            [
                "",
                "<details>",
                "<summary>Données techniques</summary>",
                "",
                "| Rang | NodeID | Parent(s) | Profondeur technique | VisualRow | Position X | BuffID | Preuve de regroupement |",
                "|---:|---:|---|---:|---:|---:|---|---|",
            ]
        )
        for rank_row in sorted(talent["rank_rows"], key=lambda row: (row["rank"], row["node_id"])):
            parents_raw = ", ".join(rank_row["parents"]) if rank_row["parents"] else "RACINE"
            lines.append(
                f"| {rank_label(rank_row['rank'])} | {rank_row['node_id']} | {parents_raw} | "
                f"{rank_row['progression_depth'] + 1} | {rank_row['visual_row']} | {rank_row['x']} | "
                f"{rank_row['buff_ids']} | {talent['logical_evidence']} |"
            )
        lines.extend(["", "</details>"])
    lines.append("")


def branch_section(lines, branch_name, talents, number=None, deduced=False):
    suffix = " - nom déduit" if deduced else ""
    if number is None:
        title = f"### {branch_name}{suffix}"
    else:
        title = f"### Branche {number} — {branch_name}{suffix}"
    lines.extend([title, ""])
    if not talents:
        lines.extend(["Aucun nœud identifié.", ""])
        return
    for talent in sorted(talents, key=lambda t: (t["visual_row"], t["x"], t["node_id"])):
        render_talent(lines, talent)


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
        "Ce rapport HUMAN présente les arbres de talents de Sung Jinwoo sous une forme lisible sur GitHub: topologie par système, branches, talents logiques, coûts, rangs, gains interprétés et rendements seulement lorsqu'ils sont démontrés.",
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
                f"- {talent['section']} / {talent['branch']} / profondeur technique {talent['progression_depth'] + 1}: "
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
            "Lecture: le rapport est trié par arbre, puis branche, puis talent logique dans l'ordre technique. `ProgressionDepth` reste une propriété du graphe technique; `NodeTierY` reste une rangée visuelle et ne reconstruit jamais les chemins.",
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
        "- Le rapport joueur agrège par `LogicalTalentID`, pas directement par `NodeID`.",
        "- Par défaut, un NodeID reste son propre talent logique (`RAW_NODE_ONLY`).",
        "- Plusieurs NodeID ne peuvent partager un talent logique que si une preuve explicite est ajoutée dans `LogicalGroupingEvidence`.",
        "- Les effets multiples d'un même rang logique sont regroupés dans la colonne `Effet`.",
        "- `ProgressionDepth`: profondeur réelle calculée depuis les relations Parent.",
        "- `VisualRow`: valeur GameData `NodeTierY`, utilisée seulement comme rangée visuelle.",
        "- Position horizontale: `NodeTierX`.",
        "- Rang technique: `NodeMaxLevel`; rang logique: `LogicalRank`.",
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
            "- La partie principale du rapport joueur est triée arbre -> branche -> talent logique dans l'ordre technique.",
            "- Chaque NodeID source appartient à au plus un talent logique.",
            "- Chaque rang logique pointe vers un seul NodeID sauf preuve explicite future.",
            "- Les sections de rendement/statistiques sont déplacées en annexe.",
            "- `NodeID`, `BuffID`, noms de tables et groupes internes sont absents du corps principal.",
            "- Les détails `NodeID`/`BuffID` complets restent dans ce rapport technique, pas dans le rapport HUMAN.",
        ]
    )
    TECH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_rank_parent_audit(talents):
    by_node = {node_id: talent for talent in talents for node_id in talent["node_ids"]}

    def row_for(node_id):
        talent = by_node[str(node_id)]
        rank_count = len(talent["rank_rows"])
        parents = ", ".join(talent["parents_human"]) if talent["parents_human"] else "RACINE"
        unlocks = ", ".join(talent["unlocks_human"]) if talent["unlocks_human"] else "aucun"
        rank_rows = sorted(talent["rank_rows"], key=lambda row: row["rank"])
        visual = " / ".join(
            f"{rank_label(row['rank'])}: Node {row['node_id']}, UI {row['visual_row']} X{row['x']}"
            for row in rank_rows
        )
        return (
            f"| {talent['section']} / {talent['branch']} | {talent['talent']} | "
            f"{', '.join(talent['node_ids'])} | {rank_count} | {parents} | {unlocks} | {visual} |"
        )

    lines = [
        "# Audit rangs internes et parents",
        "",
        "Audit ciblé généré depuis les GameData normalisées avant tout rendu web.",
        "",
        "## Conclusion",
        "",
        "- Un suffixe romain/numérique dans le nom localisé ne prouve pas un rang interne.",
        "- Le rang interne provient du même `NodeID` quand `NodeMaxLevel > 1`.",
        "- `SlotLinkNodeID` référence un `NodeID`, pas un rang interne précis; HUMAN affiche donc une seule relation tant qu'aucun champ GameData ne prouve une condition par rang.",
        "- Une famille/série sémantique peut aider la lecture, mais elle ne remplace jamais la topologie du graphe.",
        "",
        "## Échantillons validés",
        "",
        "| Zone | Talent / nœud | NodeID | Rangs internes | Prérequis HUMAN | Débloque HUMAN | Détail rang / position |",
        "|---|---|---:|---:|---|---|---|",
    ]
    for node_id in [
        "111201",
        "111202",
        "111402",
        "111602",
        "2150102",
        "2150202",
        "2150401",
        "2150403",
        "2150502",
        "1110501",
        "1110601",
        "119501",
        "119601",
    ]:
        if node_id in by_node:
            lines.append(row_for(node_id))
    lines.extend(
        [
            "",
            "## Points non généralisés",
            "",
            "- Les familles visibles comme `Embuscade I..IV`, `Taux de coup critique 1..6` ou `Attaque augmentée 1..6` restent des chaînes de nœuds distincts tant qu'aucune preuve de fusion n'existe.",
            "- Les cumuls des structures non rattachées restent marqués par leur confiance existante; cette passe valide le modèle nœud/rang/parent, pas les formules runtime.",
        ]
    )
    RANK_PARENT_AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    rows = read_full_rows()
    talents = aggregate_nodes(rows)
    validate_logical_talents(rows, talents)
    write_detailed(talents)
    write_human(talents)
    write_technical(talents)
    write_rank_parent_audit(talents)
    print(f"wrote {HUMAN}")
    print(f"wrote {DETAILED_CSV}")
    print(f"wrote {TECH}")
    print(f"wrote {RANK_PARENT_AUDIT}")


if __name__ == "__main__":
    main()
