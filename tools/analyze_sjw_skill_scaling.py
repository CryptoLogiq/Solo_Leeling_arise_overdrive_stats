from __future__ import annotations

import ast
import csv
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
OUT_CSV = ANALYSIS / "csv" / "sjw_skill_level_scaling.csv"
OUT_MD = ANALYSIS / "reports" / "SJW_SKILL_LEVEL_SCALING.md"

ROMAN = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
}

FIELDS = [
    "TotalDamage",
    "DamAttCoeff",
    "DamArmCoeff",
    "DamMHPCoeff",
    "Cooldown",
    "MPCon",
    "MPGain",
]


def load_table(name: str) -> list[dict]:
    return json.loads((ANALYSIS / "decoded_tables" / f"{name}.json").read_text(encoding="utf-8"))[
        "records"
    ]


def parse_list(value):
    if value in (None, "", "[]", "[0]"):
        return []
    if isinstance(value, list):
        return value
    try:
        parsed = ast.literal_eval(str(value))
    except (SyntaxError, ValueError):
        return [value]
    if parsed in (0, "0", None):
        return []
    return parsed if isinstance(parsed, list) else [parsed]


def numeric(value):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fmt(value):
    if value is None:
        return ""
    if isinstance(value, float):
        if math.isclose(value, round(value), abs_tol=1e-9):
            return str(int(round(value)))
        return f"{value:.6g}"
    return str(value)


def pct_delta(current, previous):
    current = numeric(current)
    previous = numeric(previous)
    if current is None or previous is None or math.isclose(previous, 0.0, abs_tol=1e-12):
        return ""
    return (current - previous) / previous * 100.0


def abs_delta(current, previous):
    current = numeric(current)
    previous = numeric(previous)
    if current is None or previous is None:
        return ""
    return current - previous


def rank_from_name(name: str):
    if not name:
        return None
    match = re.search(r"(?:\s|\u00a0)(I|II|III|IV|V|VI|VII|VIII|IX|X)$", name)
    if match:
        return ROMAN[match.group(1)]
    return None


def base_name(name: str):
    return re.sub(r"(?:\s|\u00a0)(I|II|III|IV|V|VI|VII|VIII|IX|X)$", "", name or "").strip()


def buff_ids_from_info(info: dict) -> list[int]:
    ids = []
    for key in ("BuffSet1", "BuffSet2", "BuffSet3", "BuffSet4", "BuffSet5", "BoundBuffID", "PassiveBuffID"):
        for item in parse_list(info.get(key)):
            try:
                item = int(item)
            except (TypeError, ValueError):
                continue
            if item and item not in ids:
                ids.append(item)
    return ids


def buff_summary(buff: dict) -> str:
    parts = [f"{buff.get('ID')}"]
    name = buff.get("BuffName_fra") or buff.get("BuffName_eng") or buff.get("BuffName")
    if name:
        parts.append(name.replace("\n", " / "))
    stats = []
    for i in (1, 2, 3):
        st = buff.get(f"AddedStatType{i}")
        val = buff.get(f"AddedStatValue{i}")
        std = buff.get(f"AddedStatStandard{i}")
        if st:
            stats.append(f"{st}={val}" + (f"({std})" if std else ""))
    states = []
    for i in (1, 2, 3):
        state = buff.get(f"SpecialState{i}")
        if state:
            states.append(
                f"{state}({buff.get(f'SpecialState{i}OptionValue1')},"
                f"{buff.get(f'SpecialState{i}OptionValue2')},"
                f"{buff.get(f'SpecialState{i}OptionValue3')})"
            )
    desc = buff.get("SkillDescBuff_fra") or buff.get("SkillDescBuff_eng")
    if stats:
        parts.append("stats " + ", ".join(stats))
    if states:
        parts.append("states " + ", ".join(states))
    if desc:
        parts.append(desc.replace("\n", " "))
    return " | ".join(parts)


def row_signature(row: dict):
    changed = []
    for field in FIELDS:
        delta = row.get(f"Delta {field}")
        if delta not in ("", None) and not math.isclose(float(delta), 0.0, abs_tol=1e-9):
            changed.append(field)
    if row.get("Buffs appliqués") != row.get("Buffs rang précédent", ""):
        changed.append("Buffs")
    if not changed:
        return "aucun changement numérique explicite"
    return "+".join(changed)


def classify_group(rows: list[dict]) -> str:
    deltas = []
    pct_values = []
    for row in rows[1:]:
        changed = []
        for field in FIELDS:
            delta = row.get(f"Delta {field}")
            pct = row.get(f"Variation {field} %")
            if delta not in ("", None) and not math.isclose(float(delta), 0.0, abs_tol=1e-9):
                changed.append(field)
                if pct not in ("", None):
                    pct_values.append(round(float(pct), 4))
        if changed:
            deltas.append(tuple(changed))
    if not deltas:
        return "aucun changement numérique explicite"
    if len(set(deltas)) > 1:
        return "courbe mixte selon le rang"
    if len(set(pct_values)) == 1 and pct_values:
        return f"même pourcentage sur {','.join(deltas[0])}"
    if len(set(pct_values)) > 1:
        return f"pourcentages variables sur {','.join(deltas[0])}"
    return f"gain fixe sur {','.join(deltas[0])}"


def main():
    pc = load_table("ChPCSkill")
    info = {r["ID"]: r for r in load_table("ChPCSkillInfo")}
    buffs = {r["ID"]: r for r in load_table("ChComBuff")}
    nodes = load_table("CharPCSkillTreeNode")

    node_costs = defaultdict(list)
    for node in nodes:
        value = node.get("NodeValue")
        if value:
            node_costs[int(value)].append(node)

    pairs = []
    for skill in pc:
        gid = int(skill.get("SkillGroupID", 0))
        sid = int(skill.get("ID", 0))
        if not str(gid).startswith("100") or not str(sid).startswith("100"):
            continue
        if skill.get("UIDisplay") != "True":
            continue
        skill_info = info.get(skill.get("BaseSkillInfoKey"))
        if not skill_info:
            continue
        name = skill.get("SkillName_fra") or skill.get("SkillName_eng") or skill.get("SkillName")
        rank = rank_from_name(name)
        if rank is None:
            continue
        pairs.append((base_name(name), gid // 10000, rank, skill, skill_info))

    grouped = defaultdict(list)
    for name, base_group, rank, skill, skill_info in pairs:
        grouped[(name, base_group)].append((rank, skill, skill_info))

    selected_groups = []
    for key, values in grouped.items():
        unique_ranks = sorted({rank for rank, _, _ in values})
        if len(unique_ranks) >= 2:
            selected_groups.append((key, values))
    selected_groups.sort(key=lambda item: (-len({v[0] for v in item[1]}), item[0][1], item[0][0]))

    all_rows = []
    group_rows = {}
    for (name, base_group), values in selected_groups:
        values.sort(key=lambda item: (item[0], int(item[1]["SkillGroupID"]), int(item[1]["ID"])))
        rows = []
        previous = None
        previous_buffs = ""
        for rank, skill, skill_info in values:
            buff_ids = buff_ids_from_info(skill_info)
            buff_texts = [buff_summary(buffs[i]) if i in buffs else str(i) for i in buff_ids]
            tree_cost = []
            for node in node_costs.get(int(skill["SkillGroupID"]), []):
                tree_cost.append(
                    f"node {node.get('ID')} {node.get('LevelUpCost')} {node.get('LevelUpCostValue')}"
                )
            upgrade_cost = ""
            if parse_list(skill.get("CostItemId01")) or numeric(skill.get("GoldValue")):
                upgrade_cost = (
                    f"items {skill.get('CostItemId01')} x {skill.get('CostItemValue01')}; "
                    f"gold {skill.get('GoldValue')}"
                )
            cost = "; ".join(x for x in [upgrade_cost, " | ".join(tree_cost)] if x)
            desc = (
                skill_info.get("SkillDescDetail_fra")
                or skill_info.get("SkillDescDefalut_fra")
                or skill_info.get("SkillDescDetail_eng")
                or skill_info.get("SkillDescDefalut_eng")
                or ""
            )
            row = {
                "Compétence": name,
                "Nom rang": skill.get("SkillName_fra") or skill.get("SkillName_eng") or "",
                "ID interne": skill.get("ID"),
                "SkillGroupID": skill.get("SkillGroupID"),
                "BaseSkillInfoKey": skill.get("BaseSkillInfoKey"),
                "Niveau": skill.get("SkillLevel"),
                "Rang": rank,
                "SkillType": skill.get("SkillType"),
                "TotalDamage": skill_info.get("TotalDamage"),
                "DamAttCoeff": skill_info.get("DamAttCoeff"),
                "DamArmCoeff": skill_info.get("DamArmCoeff"),
                "DamMHPCoeff": skill_info.get("DamMHPCoeff"),
                "Cooldown": skill_info.get("Cooldown"),
                "Coût MP": skill_info.get("MPCon"),
                "Gain MP": skill_info.get("MPGain"),
                "Buff IDs": ",".join(map(str, buff_ids)),
                "Buffs appliqués": " || ".join(buff_texts),
                "Description localisée": desc.replace("\n", "\\n"),
                "Coût d'amélioration explicite": cost,
            }
            for field, label in [
                ("TotalDamage", "TotalDamage"),
                ("DamAttCoeff", "ATK"),
                ("DamArmCoeff", "DEF"),
                ("DamMHPCoeff", "HP"),
                ("Cooldown", "cooldown"),
                ("MPCon", "coût MP"),
                ("MPGain", "gain MP"),
            ]:
                current_value = skill_info.get(field)
                previous_value = previous.get(field) if previous else None
                row[f"Delta {field}"] = fmt(abs_delta(current_value, previous_value)) if previous else ""
                row[f"Variation {field} %"] = fmt(pct_delta(current_value, previous_value)) if previous else ""
            real_gain_parts = []
            if previous:
                for field in FIELDS:
                    delta = row[f"Delta {field}"]
                    pct = row[f"Variation {field} %"]
                    if delta and not math.isclose(float(delta), 0.0, abs_tol=1e-9):
                        real_gain_parts.append(f"{field}: {delta}" + (f" ({pct}%)" if pct else ""))
                if row["Buffs appliqués"] != previous_buffs:
                    real_gain_parts.append("buffs modifiés")
            row["Gain réel par rapport au rang précédent"] = (
                "; ".join(real_gain_parts) if previous else ""
            )
            row["Buffs rang précédent"] = previous_buffs
            rows.append(row)
            all_rows.append(row)
            previous = skill_info
            previous_buffs = row["Buffs appliqués"]
        group_rows[(name, base_group)] = rows

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [k for k in all_rows[0] if k != "Buffs rang précédent"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    pattern_counter = Counter(classify_group(rows) for rows in group_rows.values())
    signature_counter = Counter(row_signature(row) for row in all_rows if row["Rang"] != 1)

    report_groups = list(group_rows.items())[:10]
    top_group_patterns = pattern_counter.most_common(5)
    top_transition_patterns = signature_counter.most_common(5)

    lines = [
        "# Sung Jinwoo - Skill Level/Rank Scaling",
        "",
        "Source tables: `ChPCSkill`, `ChPCSkillInfo`, `ChComBuff`, `CharPCSkillTreeNode`, `TextData.byte`.",
        "",
        "Scope: rows where `ID` and `SkillGroupID` start with `100`, `UIDisplay=True`, and the French skill name contains an explicit Roman rank suffix. This avoids mixing Hunter rows from the same tables.",
        "",
        f"CSV: `analysis/csv/sjw_skill_level_scaling.csv`",
        "",
        f"Detected ranked SJW skill groups: {len(group_rows)}.",
        f"Exported ranked rows: {len(all_rows)}.",
        "",
        "## Five Most Frequent Improvement Patterns",
        "",
    ]
    for pattern, count in top_transition_patterns:
        lines.append(f"- {pattern}: {count} rank transitions")
    lines.extend(["", "## Group-level Curve Families", ""])
    for pattern, count in top_group_patterns:
        lines.append(f"- {pattern}: {count} skill groups")

    lines.extend(
        [
            "",
            "## Selected Skills",
            "",
            "The following 10 skills are the first 10 ranked SJW groups by rank count and internal group order. Empty delta cells mean no previous rank or no explicit numeric value to compare.",
            "",
        ]
    )
    for (name, base_group), rows in report_groups:
        lines.extend([f"### {name}", "", f"- Base group: `{base_group}`", f"- Pattern: {classify_group(rows)}", ""])
        lines.append(
            "| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |"
        )
        lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|")
        for row in rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        fmt(row["Rang"]),
                        str(row["Nom rang"]).replace("|", "/"),
                        fmt(row["ID interne"]),
                        fmt(row["TotalDamage"]),
                        fmt(row["DamAttCoeff"]),
                        fmt(row["DamArmCoeff"]),
                        fmt(row["DamMHPCoeff"]),
                        fmt(row["Cooldown"]),
                        f"{fmt(row['Coût MP'])}/{fmt(row['Gain MP'])}",
                        (row["Gain réel par rapport au rang précédent"] or "").replace("|", "/"),
                        (row["Coût d'amélioration explicite"] or "").replace("|", "/"),
                    ]
                )
                + " |"
            )
        lines.extend(["", "**Buffs et description localisée**", ""])
        for row in rows:
            lines.append(f"- Rang {row['Rang']} `{row['ID interne']}`: {row['Description localisée'] or '(aucune description explicite)'}")
            if row["Buffs appliqués"]:
                lines.append(f"  Buffs: {row['Buffs appliqués']}")
        lines.append("")

    lines.extend(
        [
            "## Interpretation",
            "",
            "- Les améliorations ne suivent pas une courbe unique dans les données exportées.",
            "- Beaucoup de rangs modifient seulement les textes/buffs ou des propriétés non listées, sans changer les coefficients numériques explicites.",
            "- Quand les coefficients changent, les gains peuvent être fixes sur certains pas, absents sur d'autres, ou concentrés sur un rang précis.",
            "- Les coûts d'amélioration directs de `ChPCSkill` sont souvent vides/0 pour ces rangs SJW; les coûts disponibles proviennent surtout des nœuds `CharPCSkillTreeNode` qui déverrouillent un `SkillGroupID`.",
            "- Aucun ordre d'application des buffs n'est déduit ici; le CSV liste uniquement les buffs explicitement référencés.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
