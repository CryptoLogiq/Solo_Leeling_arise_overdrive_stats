from __future__ import annotations

import ast
import json
import re
from collections import deque
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
TABLES = WORK / "analysis" / "decoded_tables"
CANONICAL = WORK / "analysis" / "data" / "sjw_talent_tree.json"
OUT = WORK / "analysis" / "data" / "sjw_effect_database.json"

STAT_LABELS = {
    "AttFR": "Attaque",
    "ArmFR": "Défense",
    "CriticalP": "Taux critique",
    "CriDamP": "Dégâts critiques",
    "ArmPen": "Pénétration défense",
    "ArmPenP": "Pénétration défense",
    "DamP": "Dégâts infligés",
    "PrecisionP": "Précision",
    "DamReduP": "Réduction des dégâts",
    "AddMMP": "PM max",
    "MPR": "PM",
    "AddMP": "PM",
}

SPECIAL_LABELS = {
    "EnhanceBackDamage": "Dégâts dans le dos",
    "IncreaseMHP": "PV",
    "SkillTreeMpCost": "Coût MP",
    "SkillTreeEnhance": "Dégâts de compétence",
    "ChangeDamageOnElementType": "Dégâts élémentaires",
    "IncreaseDamageByTargetSpecialState": "Dégâts conditionnels",
    "IncreaseDamageByTargetBuff": "Dégâts conditionnels",
}

SKILL_NUMERIC_FIELDS = [
    ("MPCon", "Consommation PM"),
    ("MPGain", "Gain PM"),
    ("MMPRCon", "Consommation PM max"),
    ("MHPRCon", "Consommation PV max"),
    ("PGCon", "Consommation jauge"),
    ("PGGain", "Gain jauge"),
    ("UsePGGain", "Gain jauge à l'utilisation"),
    ("CGGain", "Gain CG"),
    ("EXGain", "Gain EX"),
    ("Cooldown", "Cooldown"),
    ("ElementValue", "Valeur élément"),
    ("CrashDam", "Crash / break"),
    ("DamAttCoeff", "Coeff. attaque"),
    ("DamArmCoeff", "Coeff. défense"),
    ("DamMHPCoeff", "Coeff. PV max"),
    ("HealAttCoeff", "Soin coeff. attaque"),
    ("HealArmCoeff", "Soin coeff. défense"),
    ("HealMHPCoeff", "Soin coeff. PV max"),
    ("GSAttack", "Attaque arme"),
    ("ControlDuration", "Duree controle"),
    ("MagazineCount", "Charges"),
    ("SkillRange", "Portée"),
    ("SkillMinRange", "Portée min"),
    ("SkillImpactMaxCount", "Impacts max"),
]

SKILL_BUFF_FIELDS = ["BuffSet1", "BuffSet2", "BuffSet3", "BuffSet4", "BuffSet5", "BoundBuffID", "PassiveBuffID"]


def load_table(name: str):
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


def parse_list(value):
    if value in ("", None, "[]"):
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (int, float)):
        return [] if value == 0 else [value]
    text = str(value).strip()
    if not text or text == "0":
        return []
    try:
        parsed = ast.literal_eval(text)
    except (SyntaxError, ValueError):
        if text.startswith("[") and text.endswith("]"):
            inner = text[1:-1].strip()
            return [part.strip() for part in inner.split(",") if part.strip()]
        return [text]
    return parsed if isinstance(parsed, list) else [parsed]


def str_id(value):
    if value in ("", None, 0, "0"):
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def ids_from(value):
    return [str_id(item) for item in parse_list(value) if str_id(item)]


def clean_markup(value):
    text = re.sub(r"<[^>]+>", "", str(value or ""))
    return text.replace("\\n", " ").replace("\n", " ").strip()


def meaningful(value):
    return value not in ("", None, 0, 0.0, "0", "[]")


def numeric_stat(field, label, value):
    return {
        "field": field,
        "label": label,
        "rawValue": value,
        "display": f"{value}",
        "confidence": "CONFIRMÉ PAR LES GAMEDATA",
        "wip": True,
        "wipReason": "Conversion gameplay exacte et ordre d'application runtime non déterminés.",
    }


def added_stats(row):
    stats = []
    for index in range(1, 4):
        stat_type = row.get(f"AddedStatType{index}") or ""
        raw_value = row.get(f"AddedStatValue{index}", 0)
        standard = row.get(f"AddedStatStandard{index}") or ""
        if not stat_type and not meaningful(raw_value) and not standard:
            continue
        label = STAT_LABELS.get(stat_type, stat_type or f"AddedStat{index}")
        stats.append(
            {
                "slot": index,
                "type": stat_type,
                "label": label,
                "rawValue": raw_value,
                "standard": standard,
                "display": f"{label} +{raw_value} raw" if meaningful(raw_value) else label,
                "confidence": "CONFIRMÉ PAR LES GAMEDATA",
                "wip": True,
                "wipReason": "Valeur brute conservée; conversion finale non validée pour le planner.",
            }
        )
    return stats


def special_states(row):
    states = []
    for index in range(1, 4):
        state = row.get(f"SpecialState{index}") or ""
        values = [
            row.get(f"SpecialState{index}OptionValue1", 0),
            row.get(f"SpecialState{index}OptionValue2", 0),
            row.get(f"SpecialState{index}OptionValue3", 0),
        ]
        string_value = row.get(f"SpecialState{index}StringValue1_fra") or row.get(f"SpecialState{index}StringValue1") or ""
        if not state and not any(meaningful(value) for value in values) and not string_value:
            continue
        states.append(
            {
                "slot": index,
                "type": state,
                "label": SPECIAL_LABELS.get(state, state or f"SpecialState{index}"),
                "optionValues": values,
                "stringValue": clean_markup(string_value),
                "display": f"{SPECIAL_LABELS.get(state, state)} raw {values}",
                "confidence": "CONFIRMÉ PAR LES GAMEDATA",
                "wip": True,
                "wipReason": "SpecialState identifié; sémantique exacte à valider en runtime.",
            }
        )
    return states


def trigger_info(row):
    triggered_ids = ids_from(row.get("TriggeredBuffID"))
    if not triggered_ids and not row.get("TriggeredBuffCondition"):
        return None
    return {
        "condition": row.get("TriggeredBuffCondition") or "",
        "target": row.get("TriggeredBuffTarget") or "",
        "buffIds": triggered_ids,
        "ratioRaw": row.get("TriggeredBuffRatio", 0),
        "coolTimeRaw": row.get("TriggeredBuffCoolTime", 0),
        "executeDelayRaw": row.get("TriggeredBuffExecuteDelay", 0),
        "triggerString": clean_markup(row.get("TriggerStringValue_fra") or row.get("TriggerStringValue") or ""),
        "optionValues": [
            row.get("TriggerOptionValue1", 0),
            row.get("TriggerOptionValue2", 0),
            row.get("TriggerOptionValue3", 0),
            row.get("TriggerOptionValue4", 0),
            row.get("TriggerOptionValue5", 0),
        ],
        "confidence": "CONFIRMÉ PAR LES GAMEDATA",
        "wip": True,
        "wipReason": "Condition et valeurs raw conservées; probabilité/unité runtime à valider.",
    }


def compact_buff(row):
    trigger = trigger_info(row)
    return {
        "id": str_id(row.get("ID")),
        "groupId": str_id(row.get("BuffGroupID")),
        "level": row.get("BuffLevel"),
        "name": clean_markup(row.get("BuffName_fra") or row.get("BuffName_eng") or row.get("BuffName") or ""),
        "description": clean_markup(row.get("SkillDescBuff_fra") or row.get("SkillDescBuff_eng") or row.get("SkillDescBuff") or row.get("RefDesc_fra") or row.get("RefDesc") or ""),
        "largeType": row.get("BuffLargeType") or "",
        "teamBuff": row.get("TeamBuff") or "",
        "applyType": row.get("BuffApplyType"),
        "dispelable": row.get("Dispelable"),
        "stackMaxCount": row.get("StackMaxCount"),
        "durationRaw": row.get("Duration"),
        "applyCondition": row.get("ApplyCondition"),
        "addedStats": added_stats(row),
        "specialStates": special_states(row),
        "trigger": trigger,
        "rawIds": {
            "BuffID": str_id(row.get("ID")),
            "BuffGroupID": str_id(row.get("BuffGroupID")),
        },
        "confidence": "CONFIRMÉ PAR LES GAMEDATA",
        "wip": bool(trigger or added_stats(row) or special_states(row)),
        "wipReason": "Effet brut affiché; conversion exacte et application runtime à compléter.",
    }


def skill_stats(info):
    stats = []
    for field, label in SKILL_NUMERIC_FIELDS:
        value = info.get(field)
        if meaningful(value):
            stats.append(numeric_stat(field, label, value))
    return stats


def compact_skill(skill, info):
    related_buff_ids = []
    if info:
        for field in SKILL_BUFF_FIELDS:
            related_buff_ids.extend(ids_from(info.get(field)))
    return {
        "id": str_id(skill.get("ID")),
        "groupId": str_id(skill.get("SkillGroupID")),
        "level": skill.get("SkillLevel"),
        "name": clean_markup(skill.get("SkillName_fra") or skill.get("SkillName_eng") or skill.get("SkillName") or ""),
        "type": skill.get("SkillType") or "",
        "upgradable": skill.get("Upgradable") or "",
        "baseSkillInfoKey": str_id(skill.get("BaseSkillInfoKey")),
        "description": clean_markup((info or {}).get("SkillDescDefalut_fra") or (info or {}).get("SkillDescDefalut_eng") or ""),
        "prefab": (info or {}).get("SkillPrefab") or "",
        "resourceName": (info or {}).get("ResourceName") or "",
        "stats": skill_stats(info or {}),
        "relatedBuffIds": sorted(set(related_buff_ids), key=int),
        "descEnums": ids_from((info or {}).get("SkillDescEnums")),
        "rawIds": {
            "SkillID": str_id(skill.get("ID")),
            "SkillGroupID": str_id(skill.get("SkillGroupID")),
            "BaseSkillInfoKey": str_id(skill.get("BaseSkillInfoKey")),
        },
        "confidence": "CONFIRMÉ PAR LES GAMEDATA",
        "wip": True,
        "wipReason": "Stats de skill brutes; formule finale et scaling runtime à valider.",
    }


def collect_references(model):
    buff_ids = set()
    skill_group_ids = set()
    for tree in model.get("trees", []):
        for node in tree.get("nodes", []):
            for rank in node.get("ranks", []):
                for effect in rank.get("effects", []):
                    buff_id = str_id(effect.get("buffId"))
                    ability_id = str_id(effect.get("abilityId"))
                    if buff_id:
                        buff_ids.add(buff_id)
                    if ability_id:
                        skill_group_ids.add(ability_id)
                    if effect.get("effectType") == "TriggeredBuff":
                        buff_ids.update(ids_from(effect.get("rawValue")))
    return buff_ids, skill_group_ids


def main():
    model = json.loads(CANONICAL.read_text(encoding="utf-8"))
    buff_rows = {str_id(row.get("ID")): row for row in load_table("ChComBuff")}
    skill_rows = load_table("ChPCSkill")
    skill_info_rows = {str_id(row.get("ID")): row for row in load_table("ChPCSkillInfo")}
    skills_by_group = {}
    for row in skill_rows:
        group_id = str_id(row.get("SkillGroupID"))
        if group_id:
            skills_by_group.setdefault(group_id, []).append(row)

    buff_ids, skill_group_ids = collect_references(model)
    skill_groups = {}
    skill_ids = set()
    queue = deque(sorted(buff_ids, key=int))

    for group_id in sorted(skill_group_ids, key=int):
        rows = sorted(skills_by_group.get(group_id, []), key=lambda row: (row.get("SkillLevel") or 0, row.get("ID") or 0))
        entries = []
        for skill in rows:
            info = skill_info_rows.get(str_id(skill.get("BaseSkillInfoKey")))
            entries.append(compact_skill(skill, info))
            skill_ids.add(str_id(skill.get("ID")))
            if info:
                for field in SKILL_BUFF_FIELDS:
                    for buff_id in ids_from(info.get(field)):
                        if buff_id not in buff_ids:
                            buff_ids.add(buff_id)
                            queue.append(buff_id)
        if entries:
            skill_groups[group_id] = {
                "groupId": group_id,
                "name": entries[0].get("name", ""),
                "skills": entries,
                "confidence": "CONFIRMÉ PAR LES GAMEDATA",
                "wip": True,
                "wipReason": "Référence de compétence résolue; formules runtime à compléter.",
            }

    while queue:
        buff_id = queue.popleft()
        row = buff_rows.get(buff_id)
        if not row:
            continue
        trigger = trigger_info(row)
        if not trigger:
            continue
        for child_id in trigger["buffIds"]:
            if child_id not in buff_ids:
                buff_ids.add(child_id)
                queue.append(child_id)

    buffs = {}
    missing_buffs = []
    for buff_id in sorted(buff_ids, key=int):
        row = buff_rows.get(buff_id)
        if row:
            buffs[buff_id] = compact_buff(row)
        else:
            missing_buffs.append(buff_id)

    payload = {
        "meta": {
            "generatedBy": "tools/build_sjw_effect_database.py",
            "source": [
                "analysis/data/sjw_talent_tree.json",
                "analysis/decoded_tables/ChComBuff.json",
                "analysis/decoded_tables/ChPCSkill.json",
                "analysis/decoded_tables/ChPCSkillInfo.json",
            ],
            "scope": "References used by the SJW talent planner plus linked skill/buff chains.",
            "wipPolicy": "Raw values are shown even when exact gameplay conversion is not determined.",
        },
        "effectTypeLabels": {**STAT_LABELS, **SPECIAL_LABELS},
        "skillsByGroupId": skill_groups,
        "buffsById": buffs,
        "missing": {
            "buffIds": missing_buffs,
            "skillGroupIds": [group_id for group_id in sorted(skill_group_ids, key=int) if group_id not in skill_groups],
            "skillIds": sorted(skill_ids, key=int),
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
