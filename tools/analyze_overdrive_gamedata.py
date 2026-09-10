from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import math
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
MAIN = Path("/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/GameData")
STREAMING = Path(
    "/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/"
    "Solo_Leveling_ARISE_OVERDRIVE_Data/StreamingAssets/GameData"
)
CODEC_PATH = Path("/home/cryptologiq/SoloLevelingAR-SaveGameEditor/tools/gamedata_codec.py")
OUT = WORK / "analysis"

KEYWORDS = (
    "Stat",
    "Skill",
    "Level",
    "Penalty",
    "Boss",
    "Monster",
    "Battle",
    "Power",
    "Buff",
    "Dam",
    "Coeff",
    "Cooldown",
    "Critical",
    "Precision",
    "Armor",
    "Arm",
    "MHP",
    "Attack",
    "Correction",
    "Calibrated",
    "Target",
    "Tree",
)

EXPORT_TABLES = [
    "BattlePowerCorretCondition",
    "CHObjSkill",
    "ChComBuff",
    "ChComInfo",
    "ChComStatDesc",
    "ChHunt",
    "ChHuntGrade",
    "ChMon",
    "ChMonSkill",
    "ChPCBStat",
    "ChPCSkill",
    "ChPCSkillInfo",
    "ChSJWBStat",
    "ChSJWLv",
    "ChShadSkill",
    "ChStat",
    "CharAbilityCorrection",
    "CharCalibratedStat",
    "CharCommonLevelStat",
    "CharHunterAbility",
    "CharHunterSkillCategoryLevel",
    "CharPCSkillTreeNode",
    "CharPCSkillTreelMainTab",
    "CharPCSkillTreelSubTab",
    "CharPCStatAbility",
    "CharPetSkill",
    "CharRaidReplicaSkill",
    "CharSJWStartPreset",
    "DimensionSkillTree",
    "DimensionStageLevel",
    "GateDungeonLevelGroup",
    "GroupStat",
    "ItemArtifactSubStat",
    "ItemCardCollectionStat",
    "ItemCoreLevel",
    "ItemCoreLevelOption",
    "Penalty",
    "PenaltyFix",
    "PenaltyGroup",
    "PenaltyLevel",
    "SJWP",
    "SJWSPrest",
    "SJWSkSet",
    "SkillPreview",
    "SysConst",
    "SysConstStr",
    "SystemHunterGrowth",
    "WorldBossAdvent",
    "WorldContents",
]


def load_codec():
    spec = importlib.util.spec_from_file_location("gamedata_codec", CODEC_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {CODEC_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


codec = load_codec()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_table(game_data: Path, table: str):
    columns, row_count, name = codec.parse_file(game_data / f"{table}.byte")
    records = [
        {column: values[i] for column, values in columns.items()} for i in range(row_count)
    ]
    return columns, records, name


def translations(game_data: Path):
    cols, row_count, _ = codec.parse_file(game_data / "TextData.byte")
    result = {}
    for i in range(row_count):
        key = cols["StringID"][i]
        result[key] = {
            "fra": cols.get("Value_fra", [""] * row_count)[i],
            "eng": cols.get("Value_eng", [""] * row_count)[i],
            "raw": cols.get("Value", [""] * row_count)[i],
        }
    return result


def loc(value, text):
    if not isinstance(value, str) or value == "":
        return value
    hit = text.get(value)
    if not hit:
        return value
    return hit.get("fra") or hit.get("eng") or hit.get("raw") or value


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")


def compare_dirs():
    main = {p.name: {"size": p.stat().st_size, "sha256": sha256(p)} for p in MAIN.glob("*.byte")}
    streaming = {
        p.name: {"size": p.stat().st_size, "sha256": sha256(p)} for p in STREAMING.glob("*.byte")
    }
    names = sorted(set(main) | set(streaming))
    rows = []
    for name in names:
        a = main.get(name)
        b = streaming.get(name)
        if a and b:
            status = "same" if a["sha256"] == b["sha256"] else "different"
        elif a:
            status = "main_only"
        else:
            status = "streaming_only"
        rows.append({"file": name, "status": status, "main": a, "streaming": b})
    summary = {}
    for row in rows:
        summary[row["status"]] = summary.get(row["status"], 0) + 1
    write_json(OUT / "gamedata_compare_main_vs_streaming.json", {"summary": summary, "files": rows})


def candidate_inventory(text):
    files = []
    for path in sorted(MAIN.glob("*.byte")):
        columns, row_count, table_name = codec.parse_file(path)
        column_names = list(columns)
        hay = " ".join([table_name, *column_names])
        score = sum(1 for kw in KEYWORDS if kw.lower() in hay.lower())
        if score:
            files.append(
                {
                    "table": table_name,
                    "rows": row_count,
                    "columns": column_names,
                    "score": score,
                }
            )
    files.sort(key=lambda r: (-r["score"], r["table"]))
    write_json(OUT / "candidate_tables_by_columns.json", files)

    with (OUT / "candidate_tables_by_columns.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["table", "rows", "score", "columns"])
        for row in files:
            writer.writerow([row["table"], row["rows"], row["score"], "|".join(row["columns"])])


def export_tables(text):
    exports = OUT / "decoded_tables"
    exports.mkdir(parents=True, exist_ok=True)
    for table in EXPORT_TABLES:
        path = MAIN / f"{table}.byte"
        if not path.exists():
            continue
        columns, records, table_name = parse_table(MAIN, table)
        for record in records:
            for key, value in list(record.items()):
                if isinstance(value, str) and (
                    key.lower().endswith(("name", "desc", "text", "title"))
                    or "string" in key.lower()
                    or "skill" in key.lower()
                    or value.startswith(("SysConstStr.", "ChPCSkill.", "Skill.", "Buff"))
                ):
                    record[f"{key}_fra"] = loc(value, text)
                    record[f"{key}_eng"] = text.get(value, {}).get("eng", value)
        write_json(
            exports / f"{table}.json",
            {"table": table_name, "row_count": len(records), "columns": list(columns), "records": records},
        )


def conversion_probe(text):
    _, records, _ = parse_table(MAIN, "ChComStatDesc")
    stats = {r["EStatType"]: r for r in records}
    _, sys_records, _ = parse_table(MAIN, "SysConst")
    sys_const = sys_records[0]
    examples = {
        "Precision": (117, 60.64),
        "Arm": (497, 35.42),
        "Critical": (157, 8.04),
        "CriDam": (140, 55.45),
        "ArmPen": (167, 7.71),
        "Dam": (74, 3.57),
    }
    probes = []
    for stat, (rating, shown) in examples.items():
        r = stats[stat]
        base = float(r["BaseValue"])
        const = float(r["ConstValue"])
        level_cond = float(r["ConstLevelCondition"])
        level_val = float(r["ConstLevelValue"])
        min_v = float(r["Min"])
        max_v = float(r["Max"])

        base_percent = base / 100.0
        extra_percent = shown - base_percent
        inferred_k = None
        if extra_percent > 0:
            inferred_k = rating * (100.0 / extra_percent - 1.0)

        fixed_constants = {
            "table_ConstValue": const,
            "BattleConfig.PrecisionLevelConstValue": sys_const.get(
                "BattleConfig.PrecisionLevelConstValue"
            ),
            "BattleConfig.DefRefConstant": sys_const.get("BattleConfig.DefRefConstant"),
            "BattleConfig.BaseCriChanceWeight": sys_const.get("BattleConfig.BaseCriChanceWeight"),
            "BattleConfig.BaseCriDamP": sys_const.get("BattleConfig.BaseCriDamP"),
        }
        fixed_tests = []
        for name, k in fixed_constants.items():
            if not k:
                continue
            pct = base_percent + rating / (rating + float(k)) * 100.0
            if min_v:
                pct = max(min_v / 100.0, pct)
            if max_v > -1:
                pct = min(max_v / 100.0, pct)
            fixed_tests.append(
                {
                    "constant": name,
                    "K": k,
                    "percent": round(pct, 4),
                    "abs_error": round(abs(pct - shown), 6),
                }
            )

        level_k_matches = []
        if level_val:
            for level in range(1, 201):
                k = max(0.0, level - level_cond) * level_val
                if not k:
                    continue
                pct = base_percent + rating / (rating + k) * 100.0
                if min_v:
                    pct = max(min_v / 100.0, pct)
                if max_v > -1:
                    pct = min(max_v / 100.0, pct)
                level_k_matches.append((abs(pct - shown), level, pct, k))
            level_k_matches.sort(key=lambda x: x[0])

        # Linear candidate kept as a negative control:
        # displayed basis-points = base + rating * const / (const + max(0, level-level_cond)*level_val)
        candidates = []
        for level in range(1, 201):
            denom = const + max(0.0, level - level_cond) * level_val
            if denom == 0:
                continue
            bp = base + rating * const / denom
            if min_v:
                bp = max(min_v, bp)
            if max_v > -1:
                bp = min(max_v, bp)
            pct = bp / 100.0
            candidates.append((abs(pct - shown), level, pct, denom))
        candidates.sort(key=lambda x: x[0])
        best = candidates[:10]
        probes.append(
            {
                "stat": stat,
                "rating": rating,
                "shown_percent": shown,
                "constants": {
                    "BaseValue": r["BaseValue"],
                    "ConstValue": r["ConstValue"],
                    "ConstLevelCondition": r["ConstLevelCondition"],
                    "ConstLevelValue": r["ConstLevelValue"],
                    "Min": r["Min"],
                    "Max": r["Max"],
                    "tooltip_fra": loc(r["ToolTipText"], text),
                    "tooltip_eng": text.get(r["ToolTipText"], {}).get("eng", ""),
                },
                "inferred_K_for_base_plus_rating_over_rating_plus_K": (
                    round(inferred_k, 6) if inferred_k is not None else None
                ),
                "fixed_constant_tests_base_plus_rating_over_rating_plus_K": fixed_tests,
                "best_level_K_matches_with_K_eq_max_0_level_minus_condition_times_level_value": [
                    {
                        "level": level,
                        "K": round(k, 6),
                        "percent": round(pct, 4),
                        "abs_error": round(err, 6),
                    }
                    for err, level, pct, k in level_k_matches[:10]
                ],
                "negative_control_linear_candidate": [
                    {
                        "level": level,
                        "percent": round(pct, 4),
                        "abs_error": round(err, 6),
                        "denominator": denom,
                    }
                    for err, level, pct, denom in best
                ],
            }
        )
    write_json(OUT / "stat_conversion_probe.json", probes)


def skill_summaries(text):
    skill_tables = ["ChPCSkillInfo", "ChPCSkill", "CHObjSkill", "ChMonSkill", "ChShadSkill"]
    rows = []
    for table in skill_tables:
        _, records, _ = parse_table(MAIN, table)
        for r in records:
            row = {
                "table": table,
                "ID": r.get("ID"),
                "SkillGroupID": r.get("SkillGroupID"),
                "SkillLevel": r.get("SkillLevel"),
                "SkillType": r.get("SkillType"),
                "SkillName": loc(r.get("SkillName"), text),
                "Cooldown": r.get("Cooldown"),
                "MPCon": r.get("MPCon"),
                "TotalDamage": r.get("TotalDamage"),
                "DamAttCoeff": r.get("DamAttCoeff"),
                "DamArmCoeff": r.get("DamArmCoeff"),
                "DamMHPCoeff": r.get("DamMHPCoeff"),
                "DamTargetMHPCoeff": r.get("DamTargetMHPCoeff"),
                "DamTargetHPCoeff": r.get("DamTargetHPCoeff"),
                "BuffSet1": r.get("BuffSet1"),
                "BuffSet2": r.get("BuffSet2"),
                "BuffSet3": r.get("BuffSet3"),
                "SkillDesc": loc(r.get("SkillDescDetail") or r.get("SkillDescDefalut"), text),
            }
            rows.append(row)
    with (OUT / "skill_summary.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = translations(MAIN)
    compare_dirs()
    candidate_inventory(text)
    export_tables(text)
    conversion_probe(text)
    skill_summaries(text)


if __name__ == "__main__":
    main()
