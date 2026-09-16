from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
TABLES = ANALYSIS / "decoded_tables"
OUT_JSON = ANALYSIS / "data" / "sjw_point_progression.json"
OUT_CSV = ANALYSIS / "csv" / "sjw_point_progression.csv"
OUT_MD = ANALYSIS / "reports" / "SJW_POINT_PROGRESSION.md"
TALENT_TREE = ANALYSIS / "data" / "sjw_talent_tree.json"

POINT_FIELDS = ["SkillPoint", "WeaponPoint", "SpecialPoint", "IdentityPoint"]


def load_table(name: str) -> list[dict]:
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


def as_int(value, default=0) -> int:
    if value in (None, ""):
        return default
    return int(value)


def numeric_cost(value):
    if value in (None, ""):
        return None
    try:
        parsed = int(str(value))
    except ValueError:
        return None
    return parsed


def load_sysconst() -> dict:
    rows = load_table("SysConst")
    return rows[0] if rows else {}


def build_level_rows(chsjwlv: list[dict]) -> tuple[list[dict], dict[str, list[int]], dict[str, int]]:
    rows = []
    cumulative = {field: 0 for field in POINT_FIELDS}
    gain_levels = {field: [] for field in POINT_FIELDS}
    for row in sorted(chsjwlv, key=lambda item: as_int(item["Level"])):
        level = as_int(row["Level"])
        output = {
            "id": as_int(row["ID"]),
            "level": level,
            "totalExpRaw": row.get("TotalExp"),
            "maxAP": as_int(row.get("MaxAP")),
            "provideSkillSet": as_int(row.get("ProvideSkillSet")),
            "gains": {},
            "cumulative": {},
            "confidence": "CONFIRMÉ PAR LES GAMEDATA",
        }
        for field in POINT_FIELDS:
            gain = as_int(row.get(field))
            cumulative[field] += gain
            output["gains"][field] = gain
            output["cumulative"][field] = cumulative[field]
            if gain:
                gain_levels[field].append(level)
        rows.append(output)
    return rows, gain_levels, cumulative


def point_source_summary(rows: list[dict], gain_levels: dict[str, list[int]], totals: dict[str, int]) -> dict:
    summary = {}
    for field in POINT_FIELDS:
        levels = gain_levels[field]
        gains = sorted({row["gains"][field] for row in rows if row["gains"][field]})
        if levels:
            confidence = "CONFIRMÉ PAR LES GAMEDATA"
            note = "Gain par niveau trouvé dans ChSJWLv."
        else:
            confidence = "CONFIRMÉ POUR LE LEVEL-UP; SOURCE D'ACQUISITION NON DÉTERMINÉE"
            note = "ChSJWLv ne donne aucun gain par niveau pour cette monnaie."
        summary[field] = {
            "sourceTable": "ChSJWLv",
            "sourceField": field,
            "gainValues": gains,
            "gainLevels": levels,
            "totalAtMaxLevel": totals[field],
            "confidence": confidence,
            "wip": field == "IdentityPoint",
            "note": note,
        }
    return summary


def demand_from_talent_tree() -> dict:
    model = json.loads(TALENT_TREE.read_text(encoding="utf-8"))
    demand = defaultdict(
        lambda: {
            "knownCostTotal": 0,
            "knownRankCount": 0,
            "unknownRankCount": 0,
            "nodeIdsWithUnknownCost": [],
            "source": "analysis/data/sjw_talent_tree.json",
            "confidence": "CALCULÉ À PARTIR DES GAMEDATA",
            "note": "Somme brute des coûts connus sur tous les rangs présents; ce n'est pas un coût de route.",
        }
    )
    for tree in model.get("trees", []):
        for node in tree.get("nodes", []):
            for rank in node.get("ranks", []):
                currency = rank.get("pointCurrency") or "UNKNOWN"
                bucket = demand[currency]
                cost = numeric_cost(rank.get("cost"))
                if rank.get("costConfidence") == "NON DÉTERMINÉ" or cost is None:
                    bucket["unknownRankCount"] += 1
                    node_id = node.get("nodeId")
                    if node_id not in bucket["nodeIdsWithUnknownCost"]:
                        bucket["nodeIdsWithUnknownCost"].append(node_id)
                    continue
                bucket["knownCostTotal"] += cost
                bucket["knownRankCount"] += 1
    return {currency: demand[currency] for currency in sorted(demand)}


def snapshots_for(rows: list[dict], levels: list[int]) -> dict[str, dict[str, int]]:
    by_level = {row["level"]: row for row in rows}
    snapshots = {}
    for level in levels:
        row = by_level.get(level)
        if row:
            snapshots[str(level)] = dict(row["cumulative"])
    return snapshots


def csv_rows(rows: list[dict]) -> list[dict]:
    output = []
    for row in rows:
        output.append(
            {
                "Level": row["level"],
                "TotalExpRaw": row["totalExpRaw"],
                "MaxAP": row["maxAP"],
                "ProvideSkillSet": row["provideSkillSet"],
                "SkillPointGain": row["gains"]["SkillPoint"],
                "SkillPointTotal": row["cumulative"]["SkillPoint"],
                "WeaponPointGain": row["gains"]["WeaponPoint"],
                "WeaponPointTotal": row["cumulative"]["WeaponPoint"],
                "SpecialPointGain": row["gains"]["SpecialPoint"],
                "SpecialPointTotal": row["cumulative"]["SpecialPoint"],
                "IdentityPointGain": row["gains"]["IdentityPoint"],
                "IdentityPointTotal": row["cumulative"]["IdentityPoint"],
                "Confidence": row["confidence"],
            }
        )
    return output


def write_csv(rows: list[dict]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "Level",
        "TotalExpRaw",
        "MaxAP",
        "ProvideSkillSet",
        "SkillPointGain",
        "SkillPointTotal",
        "WeaponPointGain",
        "WeaponPointTotal",
        "SpecialPointGain",
        "SpecialPointTotal",
        "IdentityPointGain",
        "IdentityPointTotal",
        "Confidence",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def compact_levels(levels: list[int]) -> str:
    if not levels:
        return "aucun niveau"
    if len(levels) > 8:
        return f"{', '.join(str(level) for level in levels[:6])}, ... {levels[-2]}, {levels[-1]}"
    return ", ".join(str(level) for level in levels)


def write_report(payload: dict) -> None:
    summary = payload["summary"]
    sources = payload["pointSources"]
    demand = payload["talentDemandByCurrency"]
    level30 = summary["snapshots"].get("30", {})
    max_level = summary["maxLevel"]
    max_snapshot = summary["snapshots"].get(str(max_level), {})

    lines = [
        "# Sung Jinwoo - Point Progression",
        "",
        "Sources primaires: `ChSJWLv` pour les gains par niveau, `SysConst` pour la limite de niveau, `sjw_talent_tree.json` pour les coûts de talents.",
        "",
        "## Résumé",
        "",
        f"- Niveau max SJW: `{max_level}` (`ChSJWLv.Level` max, recoupé avec `SysConst.Common.SungjinwooMaxLevel`).",
        f"- Niveau de départ SJW: `{summary['startLevel']}` (`SysConst.BeginSetting.SJWLevel`).",
        f"- Exemple demandé niveau 30: Skill `{level30.get('SkillPoint', 0)}`, Weapon `{level30.get('WeaponPoint', 0)}`, Special `{level30.get('SpecialPoint', 0)}`, Identity `{level30.get('IdentityPoint', 0)}`.",
        f"- Maximum niveau {max_level}: Skill `{max_snapshot.get('SkillPoint', 0)}`, Weapon `{max_snapshot.get('WeaponPoint', 0)}`, Special `{max_snapshot.get('SpecialPoint', 0)}`, Identity `{max_snapshot.get('IdentityPoint', 0)}`.",
        "",
        "Les valeurs de `ChSJWLv` sont traitées comme des gains marginaux par niveau; les totaux ci-dessous sont calculés par cumul.",
        "",
        "## Sources par monnaie",
        "",
        "| Monnaie | Source gain niveau | Pattern | Total max | Confiance | WIP |",
        "|---|---|---|---:|---|---|",
    ]
    for field in POINT_FIELDS:
        source = sources[field]
        gains = ", ".join(str(value) for value in source["gainValues"]) or "0"
        if source["gainLevels"]:
            pattern = f"+{gains} aux niveaux {compact_levels(source['gainLevels'])}"
        else:
            pattern = "aucun gain par niveau trouvé"
        lines.append(
            f"| `{field}` | `{source['sourceTable']}.{source['sourceField']}` | {pattern} | {source['totalAtMaxLevel']} | {source['confidence']} | {'oui' if source['wip'] else 'non'} |"
        )

    lines.extend(
        [
            "",
            "## Paliers utiles",
            "",
            "| Niveau | SkillPoint | WeaponPoint | SpecialPoint | IdentityPoint |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for level, values in summary["snapshots"].items():
        lines.append(
            f"| {level} | {values['SkillPoint']} | {values['WeaponPoint']} | {values['SpecialPoint']} | {values['IdentityPoint']} |"
        )

    lines.extend(
        [
            "",
            "## Demande brute des talents",
            "",
            "Cette table additionne les coûts connus de tous les rangs de talents présents dans le modèle canonique. Elle sert à comparer un budget maximum à une demande brute, pas à valider une route optimale.",
            "",
            "| Monnaie | Coût connu total | Rangs connus | Rangs coût WIP | Confiance |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for currency in sorted(demand):
        item = demand[currency]
        confidence = item["confidence"]
        if item["unknownRankCount"]:
            confidence = "CALCULÉ SUR COÛTS CONNUS; COÛTS PARTIELLEMENT NON DÉTERMINÉS"
        lines.append(
            f"| `{currency}` | {item['knownCostTotal']} | {item['knownRankCount']} | {item['unknownRankCount']} | {confidence} |"
        )

    lines.extend(
        [
            "",
            "## Points non résolus",
            "",
            "- `IdentityPoint`: 4 nœuds de talent consomment chacun 1 point, mais `ChSJWLv.IdentityPoint` reste à 0 du niveau 1 au niveau 75. La source d'acquisition n'est donc pas le level-up dans cette table et reste WIP.",
            "- `TotalExp`: le champ existe dans `ChSJWLv`, mais le décodage actuel produit des flottants extrêmement petits. Ne pas utiliser cette courbe XP pour planifier tant qu'elle n'est pas vérifiée.",
            "- `ProvideSkillSet`: présent dans `ChSJWLv`, mais vaut 0 sur les lignes décodées actuelles.",
            "",
            f"CSV complet: `{OUT_CSV.relative_to(ROOT)}`",
            f"JSON planner: `{OUT_JSON.relative_to(ROOT)}`",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    chsjwlv = load_table("ChSJWLv")
    sysconst = load_sysconst()
    rows, gain_levels, totals = build_level_rows(chsjwlv)
    max_level = max(row["level"] for row in rows)
    snapshot_levels = [1, 30, max_level]
    payload = {
        "metadata": {
            "game": "Solo Leveling: ARISE OVERDRIVE",
            "generatedBy": "tools/analyze_sjw_point_progression.py",
            "sourceTables": ["ChSJWLv", "SysConst", "analysis/data/sjw_talent_tree.json"],
            "confidence": "CALCULÉ À PARTIR DES GAMEDATA",
            "notes": [
                "Les champs SkillPoint/WeaponPoint/SpecialPoint/IdentityPoint de ChSJWLv sont conservés comme gains bruts par niveau.",
                "Les cumuls sont calculés à partir des gains bruts, sans conversion ni hypothèse de route.",
                "TotalExp est conservé en raw mais non interprété.",
            ],
        },
        "summary": {
            "startLevel": as_int(sysconst.get("BeginSetting.SJWLevel")),
            "maxLevel": max_level,
            "maxLevelFromSysConst": as_int(sysconst.get("Common.SungjinwooMaxLevel")),
            "accountMaxLevelFromSysConst": as_int(sysconst.get("Common.AccountMaxLevel")),
            "levelCount": len(rows),
            "snapshots": snapshots_for(rows, snapshot_levels),
            "maxTotals": totals,
        },
        "pointSources": point_source_summary(rows, gain_levels, totals),
        "talentDemandByCurrency": demand_from_talent_tree(),
        "levels": rows,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(csv_rows(rows))
    write_report(payload)


if __name__ == "__main__":
    main()
