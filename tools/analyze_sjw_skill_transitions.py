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
OUT_MD = ANALYSIS / "reports" / "SJW_SKILL_TRANSITION_CARDS.md"
OUT_CSV = ANALYSIS / "csv" / "sjw_skill_transition_cards.csv"

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
RANK_LABEL = {v: k for k, v in ROMAN.items()}

NUMERIC_FIELDS = [
    ("TotalDamage", "Dégâts directs", ""),
    ("DamAttCoeff", "ATK coeff", ""),
    ("DamArmCoeff", "DEF coeff", ""),
    ("DamMHPCoeff", "HP coeff", ""),
    ("Cooldown", "Cooldown", " s"),
    ("MPCon", "MP", ""),
    ("MPGain", "Gain MP", ""),
]

RECURSIVE_STATES = {"SkillChange", "SkillCast"}
CONDITIONAL_DAMAGE_STATES = {
    "IncreaseDamageByTargetBuff",
    "IncreaseDamageByTargetSpecialState",
    "SkillDamageIncreaseOnBuffedTarget",
    "EnhanceBackDamage",
    "ChangeDamageOnElementType",
}
UTILITY_STATES = {
    "BodyStop",
    "ReactionImmune",
    "ForceBackAttack",
    "SkillChange",
    "SkillCast",
    "PeriodGiveBuff",
    "AddBuffInRange",
}
DEFENSIVE_STATES = {"Invincible", "ReactionImmune"}


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


def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def num(value):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fmt_num(value):
    value = num(value)
    if value is None:
        return ""
    if math.isclose(value, round(value), abs_tol=1e-9):
        return str(int(round(value)))
    return f"{value:.6g}"


def fmt_change(before, after, suffix=""):
    b = num(before)
    a = num(after)
    if b is None or a is None:
        return f"{before} → {after}"
    if math.isclose(b, a, abs_tol=1e-9):
        return "inchangés"
    return f"{fmt_num(b)}{suffix} → {fmt_num(a)}{suffix}"


def pct_change(before, after):
    b = num(before)
    a = num(after)
    if b is None or a is None or math.isclose(b, 0.0, abs_tol=1e-12):
        return ""
    return (a - b) / b * 100.0


def rank_from_name(name: str):
    match = re.search(r"(?:\s|\u00a0)(I|II|III|IV|V|VI|VII|VIII|IX|X)$", name or "")
    return ROMAN[match.group(1)] if match else None


def base_name(name: str):
    return re.sub(r"(?:\s|\u00a0)(I|II|III|IV|V|VI|VII|VIII|IX|X)$", "", name or "").strip()


def clean_text(text: str) -> str:
    text = (text or "").replace("\\n", "\n")
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\u00a0", " ")
    return text.strip()


def stat_value_text(stat_type, value):
    if not stat_type:
        return ""
    if stat_type.endswith("P") or stat_type.endswith("R") or stat_type in {"DamP", "ArmPenP", "CriDamP", "PrecisionP", "AttFR"}:
        return f"{stat_type}: {value / 100:.3g}% (FORTEMENT PROBABLE; valeur interne {fmt_num(value)})"
    return f"{stat_type}: {fmt_num(value)} (CONFIRMÉ interne)"


def state_value_text(name, values, string_value=""):
    v1, v2, v3 = values
    if name in {"IncreaseDamageByTargetSpecialState", "IncreaseDamageByTargetBuff"}:
        return (
            f"{name}: +{v3 / 100:.3g}% dégâts conditionnels "
            f"(FORTEMENT PROBABLE; bonus interne {fmt_num(v3)}, cible {fmt_num(v1)}/{fmt_num(v2)} {string_value})"
        )
    if name == "SkillDamageIncreaseOnBuffedTarget":
        return (
            f"{name}: +{v3 / 100:.3g}% dégâts contre cible avec buff "
            f"(FORTEMENT PROBABLE; bonus interne {fmt_num(v3)}, paramètres {fmt_num(v1)}/{fmt_num(v2)})"
        )
    if name == "ChangeDamageOnElementType":
        return (
            f"{name}: +{v2 / 100:.3g}% dégâts élémentaires conditionnels "
            f"(FORTEMENT PROBABLE; bonus interne {fmt_num(v2)}, élément/type {fmt_num(v1)})"
        )
    if name == "EnhanceBackDamage":
        return (
            f"{name}: +{v2 / 100:.3g}% attaque de dos "
            f"(FORTEMENT PROBABLE; bonus interne {fmt_num(v2)}, hit/skill {fmt_num(v1)})"
        )
    if name in {"CriticalRate", "IncreaseHitCriRate", "IncreaseHitCriDam"}:
        return f"{name}: +{v1 / 100:.3g}% (CONFIRMÉ par placeholders 0.01 quand présents; interne {fmt_num(v1)})"
    if name == "SkillTreeEnhance":
        return f"{name}: +{v2 / 100:.3g}% dégâts de compétence (FORTEMENT PROBABLE; interne {fmt_num(v2)})"
    if name == "SkillTreeMpCost":
        return f"{name}: {v2 / 100:.3g}% coût MP (FORTEMENT PROBABLE; interne {fmt_num(v2)})"
    if name == "BodyStop":
        return f"Paralysie/immobilisation {v1 / 1000:.3g} s (FORTEMENT PROBABLE; interne {fmt_num(v1)})"
    if name == "ReactionImmune":
        return "Super armure / immunité aux réactions (CONFIRMÉ par description)"
    if name == "Invincible":
        return f"Immunité aux dégâts (HYPOTHÈSE durée/valeur interne {fmt_num(v1)})"
    if name == "ForceBackAttack":
        return f"attaque de dos garantie pour référence {fmt_num(v1)} (CONFIRMÉ par description si présente)"
    if name == "SkillChange":
        return f"SkillChange: remplace/cible skill group {fmt_num(v1)} -> {fmt_num(v2)}"
    if name == "SkillCast":
        return f"SkillCast: lance skill group {fmt_num(v1)}"
    return f"{name}: paramètres internes {fmt_num(v1)}, {fmt_num(v2)}, {fmt_num(v3)}"


class Analyzer:
    def __init__(self):
        self.pc = load_table("ChPCSkill")
        self.info = {int(r["ID"]): r for r in load_table("ChPCSkillInfo")}
        self.buffs = {int(r["ID"]): r for r in load_table("ChComBuff")}
        self.pc_by_group = defaultdict(list)
        self.info_by_group = defaultdict(list)
        for row in self.pc:
            self.pc_by_group[int(row["SkillGroupID"])].append(row)
        for row in self.info.values():
            self.info_by_group[int(row["ID"]) // 10000 * 10000].append(row)

    def resolve_skill_infos(self, ref, depth=0, seen=None):
        if seen is None:
            seen = set()
        if depth > 5:
            return []
        ref = to_int(ref)
        if not ref or ref in seen:
            return []
        seen.add(ref)
        out = []
        for candidate in (ref, ref + 1):
            if candidate in self.info:
                out.append(self.info[candidate])
        for skill in self.pc_by_group.get(ref, []):
            info = self.info.get(int(skill.get("BaseSkillInfoKey", 0)))
            if info:
                out.append(info)
        for info in self.info_by_group.get(ref, []):
            out.append(info)
        unique = []
        got = set()
        for info in out:
            if int(info["ID"]) not in got:
                unique.append(info)
                got.add(int(info["ID"]))
        return unique

    def direct_buff_ids(self, info):
        ids = []
        for key in ("BuffSet1", "BuffSet2", "BuffSet3", "BuffSet4", "BuffSet5", "BoundBuffID", "PassiveBuffID"):
            for item in parse_list(info.get(key)):
                iid = to_int(item)
                if iid and iid not in ids:
                    ids.append(iid)
        return ids

    def effects_for_info(self, info, depth=0, seen_buffs=None, seen_infos=None):
        if seen_buffs is None:
            seen_buffs = set()
        if seen_infos is None:
            seen_infos = set()
        iid = int(info["ID"])
        if iid in seen_infos or depth > 5:
            return []
        seen_infos.add(iid)
        effects = []
        for buff_id in self.direct_buff_ids(info):
            buff = self.buffs.get(buff_id)
            if not buff or buff_id in seen_buffs:
                continue
            seen_buffs.add(buff_id)
            effects.extend(self.effects_for_buff(buff, depth, seen_buffs, seen_infos))
        return effects

    def effects_for_buff(self, buff, depth, seen_buffs, seen_infos):
        effects = []
        bid = int(buff["ID"])
        bname = buff.get("BuffName_fra") or buff.get("BuffName_eng") or ""
        bdesc = buff.get("SkillDescBuff_fra") or buff.get("SkillDescBuff_eng") or ""
        for idx in (1, 2, 3):
            st = buff.get(f"AddedStatType{idx}")
            val = num(buff.get(f"AddedStatValue{idx}"))
            if st and val is not None:
                effects.append(
                    {
                        "kind": "stat",
                        "key": f"stat:{st}",
                        "category": "défensif" if st in {"DamReduP", "Arm", "ArmR"} else "conditionnel",
                        "buff_id": bid,
                        "summary": stat_value_text(st, val),
                        "raw": {"stat": st, "value": val},
                    }
                )
        for idx in (1, 2, 3):
            state = buff.get(f"SpecialState{idx}")
            if not state:
                continue
            vals = [
                num(buff.get(f"SpecialState{idx}OptionValue1")) or 0,
                num(buff.get(f"SpecialState{idx}OptionValue2")) or 0,
                num(buff.get(f"SpecialState{idx}OptionValue3")) or 0,
            ]
            string_value = buff.get(f"SpecialState{idx}StringValue1") or ""
            category = "mécanique"
            if state in CONDITIONAL_DAMAGE_STATES:
                category = "conditionnel"
            elif state in DEFENSIVE_STATES:
                category = "défensif"
            elif state in UTILITY_STATES:
                category = "utilitaire"
            summary = state_value_text(state, vals, string_value)
            effects.append(
                {
                    "kind": "state",
                    "key": f"state:{state}:{fmt_num(vals[0])}:{fmt_num(vals[1])}:{string_value}",
                    "category": category,
                    "buff_id": bid,
                    "summary": summary,
                    "raw": {"state": state, "values": vals, "string": string_value},
                }
            )
            if state in RECURSIVE_STATES:
                refs = [vals[0]]
                if state == "SkillChange":
                    refs.append(vals[1])
                for ref in refs:
                    for nested in self.resolve_skill_infos(ref, depth + 1, seen_infos):
                        effects.append(
                            {
                                "kind": "payload",
                                "key": f"payload:{nested['ID']}",
                                "category": "mécanique",
                                "buff_id": bid,
                                "summary": (
                                    f"payload référencé {nested['ID']}: ATK {fmt_num(nested.get('DamAttCoeff'))}, "
                                    f"DEF {fmt_num(nested.get('DamArmCoeff'))}, HP {fmt_num(nested.get('DamMHPCoeff'))}, "
                                    f"CD {fmt_num(nested.get('Cooldown'))} s, MP {fmt_num(nested.get('MPCon'))}"
                                ),
                                "raw": {"info_id": nested["ID"]},
                            }
                        )
                        effects.extend(self.effects_for_info(nested, depth + 1, seen_buffs, seen_infos))
        if bname or bdesc:
            effects.append(
                {
                    "kind": "description",
                    "key": f"desc:{bid}",
                    "category": "mécanique",
                    "buff_id": bid,
                    "summary": clean_text(bname or bdesc),
                    "raw": {},
                }
            )
        return effects

    def ranked_groups(self):
        rows = []
        for skill in self.pc:
            gid = int(skill.get("SkillGroupID", 0))
            sid = int(skill.get("ID", 0))
            if not str(gid).startswith("100") or not str(sid).startswith("100"):
                continue
            if skill.get("UIDisplay") != "True":
                continue
            info = self.info.get(int(skill.get("BaseSkillInfoKey", 0)))
            if not info:
                continue
            name = skill.get("SkillName_fra") or skill.get("SkillName_eng") or ""
            rank = rank_from_name(name)
            if rank is None:
                continue
            rows.append((base_name(name), gid // 10000, rank, skill, info))
        grouped = defaultdict(list)
        for item in rows:
            grouped[(item[0], item[1])].append(item)
        groups = []
        for key, values in grouped.items():
            ranks = sorted({v[2] for v in values})
            if len(ranks) >= 2:
                values.sort(key=lambda x: (x[2], int(x[3]["SkillGroupID"]), int(x[3]["ID"])))
                # Keep first row for duplicate same rank inside one base group.
                dedup = []
                seen = set()
                for value in values:
                    if value[2] in seen:
                        continue
                    seen.add(value[2])
                    dedup.append(value)
                groups.append((key, dedup))
        return sorted(groups, key=lambda x: (-len(x[1]), x[0][1], x[0][0]))

    def transition(self, before, after):
        _, _, rb, sb, ib = before
        name, _, ra, sa, ia = after
        eb = self.effects_for_info(ib)
        ea = self.effects_for_info(ia)
        mb = {e["key"]: e for e in eb}
        ma = {e["key"]: e for e in ea}
        added = [ma[k] for k in ma.keys() - mb.keys()]
        removed = [mb[k] for k in mb.keys() - ma.keys()]
        modified = []
        # Same effect family with changed value, useful for stat and state names.
        fam_b = defaultdict(list)
        fam_a = defaultdict(list)
        for e in eb:
            fam_b[e["key"].split(":")[0:2][1] if ":" in e["key"] else e["key"]].append(e)
        for e in ea:
            fam_a[e["key"].split(":")[0:2][1] if ":" in e["key"] else e["key"]].append(e)
        for fam in sorted(set(fam_b) & set(fam_a)):
            if {e["summary"] for e in fam_b[fam]} != {e["summary"] for e in fam_a[fam]}:
                modified.append((fam_b[fam], fam_a[fam]))
        return {
            "skill": name,
            "before_rank": rb,
            "after_rank": ra,
            "before_skill": sb,
            "after_skill": sa,
            "before_info": ib,
            "after_info": ia,
            "added": added,
            "removed": removed,
            "modified": modified,
        }


def gain_lines(t):
    ib, ia = t["before_info"], t["after_info"]
    direct = []
    conditional = []
    utility = []
    defensive = []
    mechanics = []
    for field, label, _suffix in NUMERIC_FIELDS[:4]:
        pc = pct_change(ib.get(field), ia.get(field))
        delta = (num(ia.get(field)) or 0) - (num(ib.get(field)) or 0)
        if pc != "" and not math.isclose(delta, 0.0, abs_tol=1e-9):
            direct.append(f"{label}: {delta:+.6g} ({pc:+.3g}%)")
    for field, label, suffix in NUMERIC_FIELDS[4:]:
        delta = (num(ia.get(field)) or 0) - (num(ib.get(field)) or 0)
        if not math.isclose(delta, 0.0, abs_tol=1e-9):
            utility.append(f"{label}: {fmt_num(ib.get(field))}{suffix} -> {fmt_num(ia.get(field))}{suffix}")
    for e in t["added"]:
        if e["category"] == "conditionnel":
            conditional.append(e["summary"])
        elif e["category"] == "utilitaire":
            utility.append(e["summary"])
        elif e["category"] == "défensif":
            defensive.append(e["summary"])
        else:
            mechanics.append(e["summary"])
    out = []
    out.append("Gain direct :")
    out.extend([f"- {x}" for x in direct] or ["- 0 % dégâts directs explicites"])
    if conditional:
        out.append("Gain conditionnel :")
        out.extend(f"- {x}" for x in conditional)
    if defensive:
        out.append("Gain défensif :")
        out.extend(f"- {x}" for x in defensive)
    if utility:
        out.append("Utilitaire :")
        out.extend(f"- {x}" for x in utility)
    if mechanics:
        out.append("Changement de mécanique :")
        out.extend(f"- {x}" for x in mechanics)
    return out


def skill_desc(info):
    return clean_text(
        info.get("SkillDescDetail_fra")
        or info.get("SkillDescDefalut_fra")
        or info.get("SkillDescDetail_eng")
        or info.get("SkillDescDefalut_eng")
        or ""
    )


def main():
    analyzer = Analyzer()
    transitions = []
    for _key, rows in analyzer.ranked_groups():
        by_rank = {r[2]: r for r in rows}
        for before_rank in (1, 2, 3, 4):
            if before_rank in by_rank and before_rank + 1 in by_rank:
                transitions.append(analyzer.transition(by_rank[before_rank], by_rank[before_rank + 1]))

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    csv_rows = []
    pattern_counter = Counter()
    lines = [
        "# Sung Jinwoo - Fiches de transitions de rang",
        "",
        "Source tables: `ChPCSkill`, `ChPCSkillInfo`, `ChComBuff`, `CharPCSkillTreeNode`, `TextData.byte` via exports JSON existants.",
        "",
        "Les conversions numériques des buffs sont indiquées avec un niveau de confiance. `CONFIRMÉ` signifie que la description localisée ou un placeholder indique l'unité; `FORTEMENT PROBABLE` signifie cohérent avec les conventions répétées des tables, mais pas prouvé par cette ligne seule; `HYPOTHÈSE` reste brut.",
        "",
        f"Transitions exportées: {len(transitions)}.",
        "",
    ]

    for t in transitions:
        ib, ia = t["before_info"], t["after_info"]
        sb, sa = t["before_skill"], t["after_skill"]
        title = f"{t['skill']} {RANK_LABEL[t['before_rank']]} → {RANK_LABEL[t['after_rank']]}"
        lines.extend([f"# {title}", ""])
        for field, label, suffix in NUMERIC_FIELDS:
            lines.append(f"{label:<22}: {fmt_change(ib.get(field), ia.get(field), suffix)}")
        lines.append("")
        before_desc = skill_desc(ib)
        after_desc = skill_desc(ia)
        if before_desc != after_desc and after_desc:
            lines.append("DESCRIPTION MODIFIÉE")
            lines.append(after_desc)
            lines.append("")
        if t["added"]:
            lines.append("NOUVEL EFFET")
            for e in t["added"]:
                lines.append(f"- {e['summary']}")
            lines.append("")
        if t["modified"]:
            lines.append("EFFET MODIFIÉ")
            for before, after in t["modified"]:
                lines.append(f"- {', '.join(e['summary'] for e in before)} -> {', '.join(e['summary'] for e in after)}")
            lines.append("")
        if t["removed"]:
            lines.append("EFFET SUPPRIMÉ")
            for e in t["removed"]:
                lines.append(f"- {e['summary']}")
            lines.append("")
        lines.append("Gain réel :")
        glines = gain_lines(t)
        lines.extend(glines)
        lines.append("")
        lines.append("Données sources :")
        lines.append(f"- SkillGroupID avant/après: `{sb['SkillGroupID']}` → `{sa['SkillGroupID']}`")
        lines.append(f"- ID avant/après: `{sb['ID']}` → `{sa['ID']}`")
        lines.append(f"- BaseSkillInfoKey avant/après: `{sb['BaseSkillInfoKey']}` → `{sa['BaseSkillInfoKey']}`")
        lines.append(f"- Buff IDs avant: `{','.join(map(str, analyzer.direct_buff_ids(ib)))}`")
        lines.append(f"- Buff IDs après: `{','.join(map(str, analyzer.direct_buff_ids(ia)))}`")
        recursive_ids = [e["raw"].get("info_id") for e in t["added"] + t["removed"] if e["kind"] == "payload"]
        recursive_refs = []
        for e in t["added"] + t["removed"]:
            if e["kind"] == "state" and e["raw"].get("state") in RECURSIVE_STATES:
                recursive_refs.extend(int(v) for v in e["raw"].get("values", [])[:2] if v)
        lines.append(f"- SkillChange/SkillCast payload IDs suivis: `{','.join(map(str, recursive_ids))}`")
        lines.append(f"- SkillChange/SkillCast refs brutes: `{','.join(map(str, recursive_refs))}`")
        lines.append("")

        sig_parts = []
        if any(pct_change(ib.get(f), ia.get(f)) != "" and not math.isclose((num(ia.get(f)) or 0) - (num(ib.get(f)) or 0), 0, abs_tol=1e-9) for f, _, _ in NUMERIC_FIELDS[:4]):
            sig_parts.append("direct")
        cats = {e["category"] for e in t["added"]}
        sig_parts.extend(sorted(cats))
        if not sig_parts:
            sig_parts.append("aucun changement explicite")
        pattern_counter["+".join(sig_parts)] += 1
        csv_rows.append(
            {
                "transition": title,
                "skill": t["skill"],
                "from_rank": t["before_rank"],
                "to_rank": t["after_rank"],
                "from_id": sb["ID"],
                "to_id": sa["ID"],
                "from_skill_group": sb["SkillGroupID"],
                "to_skill_group": sa["SkillGroupID"],
                "direct_gain": " | ".join(x for x in glines if x.startswith("-")),
                "new_effects": " || ".join(e["summary"] for e in t["added"]),
                "removed_effects": " || ".join(e["summary"] for e in t["removed"]),
                "source_buff_ids_before": ",".join(map(str, analyzer.direct_buff_ids(ib))),
                "source_buff_ids_after": ",".join(map(str, analyzer.direct_buff_ids(ia))),
            }
        )

    lines.extend(["# Synthèse - 5 patterns les plus fréquents", ""])
    for pattern, count in pattern_counter.most_common(5):
        lines.append(f"- {pattern}: {count} transitions")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)


if __name__ == "__main__":
    main()
