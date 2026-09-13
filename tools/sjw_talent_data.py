from __future__ import annotations

import json
import subprocess
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
CANONICAL_JSON = WORK / "analysis" / "data" / "sjw_talent_tree.json"


def ensure_canonical_tree():
    if not CANONICAL_JSON.exists():
        subprocess.run(["python", "tools/analyze_sjw_talent_tree.py"], cwd=WORK, check=True)


def load_canonical_tree():
    ensure_canonical_tree()
    return json.loads(CANONICAL_JSON.read_text(encoding="utf-8"))


def iter_sections(model):
    yield from model.get("trees", [])


def iter_nodes(model):
    for section in iter_sections(model):
        for node in section.get("nodes", []):
            yield section, node


def nodes_by_id(model):
    return {node["nodeId"]: node for _, node in iter_nodes(model)}


def node_display_name(node, rank):
    if node["nodeMaxLevel"] > 1:
        return f"{node['name']} {rank}/{node['nodeMaxLevel']}"
    return node["name"]


def flatten_effect_rows(model):
    rows = []
    for section, node in iter_nodes(model):
        for rank in node["ranks"]:
            cost = str(rank.get("cost") or "")
            currency = rank.get("pointCurrency") or ""
            cost_label = f"{cost} {currency}".strip()
            for effect in rank.get("effects", []):
                rows.append(
                    {
                        "MainTab": section["mainTab"],
                        "System": section["system"],
                        "SubTab": section["section"],
                        "Branch": section["branch"],
                        "DeducedSection": str(section.get("deduced", False)),
                        "TalentName": node_display_name(node, rank["rank"]),
                        "LogicalTalentID": node["logicalTalentId"],
                        "LogicalTalentName": node["name"],
                        "LogicalRank": str(rank["rank"]),
                        "LogicalGroupingEvidence": node["logicalGroupingEvidence"],
                        "NodeID": node["nodeId"],
                        "Rank": str(rank["rank"]),
                        "MaxRank": str(node["nodeMaxLevel"]),
                        "Cost": cost_label,
                        "RequiredLevel": rank.get("accessCondition") or "",
                        "ParentNodeID": ",".join(node["parents"]),
                        "RelationScope": "NODE",
                        "ProgressionDepth": str(node["progressionDepth"]),
                        "VisualRow": str(node["visual"]["row"]),
                        "VisualColumn": str(node["visual"]["column"]),
                        "NodeOffset": str(node["visual"]["offset"]),
                        "EffectType": effect["effectType"],
                        "RawValue": effect["rawValue"],
                        "DisplayedValue": effect["displayedValue"],
                        "MarginalGain": effect["marginalGain"],
                        "CumulativeGain": effect["cumulativeGain"],
                        "Unit": effect["unit"],
                        "BuffID": effect["buffId"],
                        "AbilityID": effect["abilityId"],
                        "Confidence": effect["confidence"],
                    }
                )
    return rows
