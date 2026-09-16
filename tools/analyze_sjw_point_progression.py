from __future__ import annotations

import csv
import importlib.util
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
TABLES = ANALYSIS / "decoded_tables"
OUT_JSON = ANALYSIS / "data" / "sjw_point_progression.json"
OUT_CSV = ANALYSIS / "csv" / "sjw_point_progression.csv"
OUT_MD = ANALYSIS / "reports" / "SJW_POINT_PROGRESSION.md"
TALENT_TREE = ANALYSIS / "data" / "sjw_talent_tree.json"
MAIN = Path("/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/GameData")
CODEC_PATH = Path("/home/cryptologiq/SoloLevelingAR-SaveGameEditor/tools/gamedata_codec.py")

POINT_FIELDS = ["SkillPoint", "WeaponPoint", "SpecialPoint", "IdentityPoint"]


def load_table(name: str) -> list[dict]:
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


def load_codec():
    spec = importlib.util.spec_from_file_location("gamedata_codec", CODEC_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {CODEC_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_table(name: str) -> list[dict]:
    codec = load_codec()
    cols, count, _ = codec.parse_file(MAIN / f"{name}.byte")
    return [{column: values[i] for column, values in cols.items()} for i in range(count)]


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


def load_text() -> dict:
    rows = parse_table("TextData")
    return {
        row["StringID"]: row.get("Value_fra") or row.get("Value_eng") or row.get("Value") or row["StringID"]
        for row in rows
    }


def clean_markup(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value or "")
    return value.replace("\\n", " ").replace("\n", " ").strip()


def loc(value, text: dict) -> str:
    if not isinstance(value, str) or not value:
        return value or ""
    return text.get(value, value)


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


def identity_overdrive_details() -> dict:
    model = json.loads(TALENT_TREE.read_text(encoding="utf-8"))
    text = load_text()
    unlocks = {row["ID"]: row for row in parse_table("ContentsUnlock")}
    chapters = {row["ID"]: row for row in parse_table("MainQuestChapter")}
    buffs = {str(row["ID"]): row for row in load_table("ChComBuff")}
    raw_nodes = {str(row["ID"]): row for row in load_table("CharPCSkillTreeNode")}
    missions_by_chapter = defaultdict(list)
    for row in parse_table("MainQuestMission"):
        missions_by_chapter[row["ChapterID"]].append(row)

    nodes = []
    for tree in model.get("trees", []):
        for node in tree.get("nodes", []):
            if node.get("nodeType") != "Identity":
                continue
            rank = node["ranks"][0]
            raw_node = raw_nodes.get(str(node["nodeId"]), {})
            unlock_id = as_int(raw_node.get("NodeContentsUnlock"))
            access = rank.get("accessCondition") or ""
            unlock = unlocks.get(unlock_id)
            chapter = None
            if unlock and unlock.get("UnlockType") == "MainQuestChapter":
                chapter = chapters.get(as_int(unlock.get("Value")))
            elif access.startswith("MainQuestChapter:"):
                chapter = chapters.get(as_int(access.split(":", 1)[1]))

            chapter_id = as_int(chapter.get("ID")) if chapter else None
            mission_rows = sorted(missions_by_chapter.get(chapter_id, []), key=lambda row: row.get("SortOrder", 0))
            buff_id = str(node.get("nodeValue") or "")
            buff = buffs.get(buff_id, {})
            node_name_key = f"NodeName.{buff_id}"
            desc_key = f"SkillDescBuff.{buff_id}"
            description = buff.get("SkillDescBuff_fra") or buff.get("SkillDescBuff_eng") or loc(desc_key, text)
            nodes.append(
                {
                    "nodeId": node["nodeId"],
                    "classSection": tree.get("section"),
                    "nodeValue": buff_id,
                    "overdriveName": loc(node_name_key, text),
                    "cost": as_int(rank.get("cost")),
                    "currency": rank.get("pointCurrency"),
                    "accessCondition": access,
                    "contentsUnlockId": unlock_id or None,
                    "contentsType": unlock.get("ContentsType") if unlock else "",
                    "unlockType": unlock.get("UnlockType") if unlock else "",
                    "unlockValue": unlock.get("Value") if unlock else None,
                    "chapterTitle": loc(chapter.get("Title"), text) if chapter else "",
                    "chapterSortOrder": chapter.get("SortOrder") if chapter else None,
                    "missionTitles": [loc(row.get("Title"), text) for row in mission_rows],
                    "descriptionSummary": clean_markup(description),
                    "confidence": "CONFIRMÉ PAR LES GAMEDATA",
                }
            )

    unlock_ids = sorted({node["contentsUnlockId"] for node in nodes if node["contentsUnlockId"] is not None})
    return {
        "interpretation": "IdentityPoint est utilisé par les nœuds de classe / Overdrive, pas gagné par le level-up dans ChSJWLv.",
        "identityPointLevelUpTotal": 0,
        "knownOverdriveNodeCount": len(nodes),
        "knownOverdriveKnownCostTotal": sum(node["cost"] for node in nodes),
        "contentsUnlockIds": unlock_ids,
        "exclusiveSelection": {
            "status": "FORTEMENT PROBABLE",
            "note": "Les quatre nœuds sont isolés, coûtent chacun 1 IdentityPoint et représentent les OverDrive de classe. Aucun champ GameData décodé ici ne démontre encore explicitement la règle runtime 'un seul actif'.",
        },
        "nodes": nodes,
        "confidence": "CONFIRMÉ PAR LES GAMEDATA POUR LES NŒUDS, COÛTS ET PRÉREQUIS; EXCLUSIVITÉ RUNTIME À CONFIRMER",
    }


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
    identity = payload["identityOverdrive"]
    level30 = summary["snapshots"].get("30", {})
    max_level = summary["maxLevel"]
    max_snapshot = summary["snapshots"].get(str(max_level), {})

    lines = [
        "# Sung Jinwoo - Point Progression",
        "",
        "Sources primaires: `ChSJWLv` pour les gains par niveau, `SysConst` pour la limite de niveau, `CharPCSkillTreeNode` / `ContentsUnlock` / `MainQuestChapter` pour les nœuds OverDrive, `sjw_talent_tree.json` pour les coûts de talents.",
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
            "## IdentityPoint / OverDrive",
            "",
            "`IdentityPoint` ne se comporte pas comme les autres points de talent dans les données observées: `ChSJWLv.IdentityPoint` reste à 0 sur tous les niveaux, tandis que quatre nœuds `NodeType=Identity` consomment chacun 1 `IdentityPoint`.",
            "",
            "| Classe | NodeID | OverDrive | Coût | Prérequis | Confiance |",
            "|---|---:|---|---:|---|---|",
        ]
    )
    for node in identity["nodes"]:
        prereq = f"{node['chapterTitle']} (`{node['unlockType']}:{node['unlockValue']}`)"
        lines.append(
            f"| {node['classSection']} | `{node['nodeId']}` | {node['overdriveName']} (`{node['nodeValue']}`) | {node['cost']} | {prereq} | {node['confidence']} |"
        )

    lines.extend(
        [
            "",
            f"Exclusivité d'activation: {identity['exclusiveSelection']['status']}. {identity['exclusiveSelection']['note']}",
            "",
            "## Points non résolus",
            "",
            "- `IdentityPoint`: la source level-up est confirmée à 0. Les prérequis des nœuds OverDrive viennent de `ContentsUnlock` et pointent vers des chapitres de quête principale, mais la règle runtime exacte du budget/slot d'activation reste à vérifier en jeu.",
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
            "sourceTables": [
                "ChSJWLv",
                "SysConst",
                "CharPCSkillTreeNode",
                "ContentsUnlock",
                "MainQuestChapter",
                "MainQuestMission",
                "TextData",
                "ChComBuff",
                "analysis/data/sjw_talent_tree.json",
            ],
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
        "identityOverdrive": identity_overdrive_details(),
        "levels": rows,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(csv_rows(rows))
    write_report(payload)


if __name__ == "__main__":
    main()
