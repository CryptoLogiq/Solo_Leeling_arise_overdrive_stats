from __future__ import annotations

import csv
import json
import subprocess
from collections import defaultdict
from pathlib import Path

from analyze_sjw_talent_human import clean_name, effect_summary, maybe_list


WORK = Path(__file__).resolve().parents[1]
TABLES = WORK / "analysis" / "decoded_tables"
FULL_CSV = WORK / "analysis" / "csv" / "sjw_talent_tree.csv"
OUT = WORK / "analysis" / "reports" / "SJW_ASSASSIN_TALENT_GRAPH.md"

EXPECTED_UI_EDGES = {
    "Attaque sournoise": {
        ("111101", "111201"),
        ("111101", "111202"),
        ("111201", "111301"),
        ("111202", "111301"),
        ("111301", "111401"),
        ("111202", "111402"),
        ("111401", "111501"),
        ("111501", "111601"),
        ("111501", "111701"),
        ("111402", "111602"),
    },
    "Frappe vitale": {
        ("112102", "112201"),
        ("112201", "112301"),
        ("112201", "112302"),
        ("112201", "112303"),
        ("112302", "112401"),
        ("112301", "112501"),
        ("112401", "112502"),
        ("112303", "112502"),
        ("112401", "112601"),
        ("112501", "112701"),
    },
}

EXPECTED_PROGRESSION_DEPTHS = {
    "Attaque sournoise": {
        "111101": 0,
        "111201": 1,
        "111202": 1,
        "111301": 2,
        "111401": 3,
        "111402": 2,
        "111501": 4,
        "111601": 5,
        "111602": 3,
        "111701": 5,
    },
    "Frappe vitale": {
        "112102": 0,
        "112201": 1,
        "112301": 2,
        "112302": 2,
        "112303": 2,
        "112401": 3,
        "112501": 3,
        "112502": 4,
        "112601": 4,
        "112701": 4,
    },
}

AMBUSH_NODE_IDS = ["111201", "111202", "111402", "111602"]


def load_json(name: str):
    payload = json.loads((TABLES / f"{name}.json").read_text(encoding="utf-8"))
    return payload.get("records", payload)


def ensure_source_csv():
    if not FULL_CSV.exists():
        subprocess.run(["python", "tools/analyze_sjw_talent_tree.py"], cwd=WORK, check=True)


def read_rows():
    ensure_source_csv()
    with FULL_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def natural_node_key(item):
    return (item["progression_depth"], item["visual_row"], item["x"], int(item["node_id"]))


def position_label(item):
    if item.get("node_type") == "Identity":
        return "centre de classe"
    x = item["x"]
    labels = {2: "gauche", 3: "centre", 4: "droite"}
    return labels.get(x, f"position {x}")


def md_escape(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def mermaid_id(node_id):
    return f"N{node_id}"


def mermaid_label(node):
    name = clean_name(node["talent"])
    return f"{node['node_id']}<br/>{name}<br/>N{node['progression_depth'] + 1} / UI {node['visual_row']} X{node['x']}"


def graph_stats(items, children, missing_parents):
    roots = [item for item in items if not item["parents"]]
    leaves = [item for item in items if not children[item["node_id"]]]
    bifurcations = [item for item in items if len(children[item["node_id"]]) > 1]
    convergences = [item for item in items if len(item["parents"]) > 1]
    edge_count = sum(len(item["parents"]) for item in items)
    return {
        "nodes": len(items),
        "edges": edge_count,
        "roots": roots,
        "leaves": leaves,
        "bifurcations": bifurcations,
        "convergences": convergences,
        "missing_parents": missing_parents,
    }


def edge_set(items):
    return {(parent, item["node_id"]) for item in items for parent in item["parents"]}


def validate_against_ui(branch, items):
    expected = EXPECTED_UI_EDGES.get(branch)
    if expected is None:
        return "NON TESTÉ", [], []
    actual = edge_set(items)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        details = []
        if missing:
            details.append("arêtes attendues absentes: " + ", ".join(f"{a}→{b}" for a, b in missing))
        if extra:
            details.append("arêtes non attendues: " + ", ".join(f"{a}→{b}" for a, b in extra))
        raise SystemExit(f"Graphe Assassin non conforme pour {branch}: {'; '.join(details)}")
    return "CONFORME à la validation UI fournie", [], []


def validate_depths(branch, items):
    expected = EXPECTED_PROGRESSION_DEPTHS.get(branch)
    if expected is None:
        return "NON TESTÉ"
    actual = {item["node_id"]: item["progression_depth"] for item in items}
    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        mismatched = sorted(
            node_id for node_id in set(expected) & set(actual) if expected[node_id] != actual[node_id]
        )
        details = []
        if missing:
            details.append("nœuds attendus absents: " + ", ".join(missing))
        if extra:
            details.append("nœuds inattendus: " + ", ".join(extra))
        if mismatched:
            details.append(
                "profondeurs différentes: "
                + ", ".join(f"{node_id} attendu {expected[node_id]}, obtenu {actual[node_id]}" for node_id in mismatched)
            )
        raise SystemExit(f"Profondeur Assassin non conforme pour {branch}: {'; '.join(details)}")
    return "CONFORME aux profondeurs attendues"


def render_mermaid(lines, items, children):
    lines.extend(["```mermaid", "flowchart TD"])
    for item in sorted(items, key=natural_node_key):
        lines.append(f'  {mermaid_id(item["node_id"])}["{mermaid_label(item)}"]')
    for item in sorted(items, key=natural_node_key):
        for child_id in children[item["node_id"]]:
            lines.append(f"  {mermaid_id(item['node_id'])} --> {mermaid_id(child_id)}")
    lines.extend(["```", ""])


def render_ascii(lines, items, children):
    by_id = {item["node_id"]: item for item in items}
    roots = sorted([item for item in items if not item["parents"]], key=natural_node_key)
    emitted = set()

    def node_line(item):
        markers = []
        if len(item["parents"]) > 1:
            markers.append("convergence")
        if len(children[item["node_id"]]) > 1:
            markers.append("bifurcation")
        suffix = f" ({', '.join(markers)})" if markers else ""
        return f"{item['node_id']} - {clean_name(item['talent'])}{suffix}"

    def walk(item, prefix="", connector=""):
        repeated = item["node_id"] in emitted
        lines.append(prefix + connector + node_line(item) + (" [déjà relié plus haut]" if repeated else ""))
        if repeated:
            return
        emitted.add(item["node_id"])
        child_prefix = prefix
        if connector:
            child_prefix += "    " if connector == "└── " else "│   "
        child_ids = children[item["node_id"]]
        for index, child_id in enumerate(child_ids):
            connector = "└── " if index == len(child_ids) - 1 else "├── "
            walk(by_id[child_id], child_prefix, connector)

    lines.append("```text")
    for root in roots:
        walk(root)
    lines.extend(["```", ""])


def render_validation(lines, stats):
    missing = stats["missing_parents"]
    lines.extend(
        [
            "### Contrôles du graphe",
            "",
            f"- Nombre de nœuds: {stats['nodes']}",
            f"- Nombre d'arêtes Parent → Enfant: {stats['edges']}",
            f"- Nombre de racines: {len(stats['roots'])}",
            f"- Nombre de feuilles: {len(stats['leaves'])}",
            f"- Nombre de bifurcations: {len(stats['bifurcations'])}",
            f"- Nombre de convergences: {len(stats['convergences'])}",
            f"- Parents référencés manquants: {', '.join(missing) if missing else 'aucun'}",
            "",
            f"- Racines: {', '.join(item['node_id'] for item in stats['roots']) or 'aucune'}",
            f"- Feuilles: {', '.join(item['node_id'] for item in stats['leaves']) or 'aucune'}",
            f"- Bifurcations: {', '.join(item['node_id'] for item in stats['bifurcations']) or 'aucune'}",
            f"- Convergences: {', '.join(item['node_id'] for item in stats['convergences']) or 'aucune'}",
            "",
        ]
    )


def node_ref(node_id, by_id):
    item = by_id.get(node_id)
    if not item:
        return f"`{node_id}`"
    return f"{clean_name(item['talent'])} (`{node_id}`)"


def refs(node_ids, by_id, empty):
    if not node_ids:
        return empty
    return ", ".join(node_ref(node_id, by_id) for node_id in node_ids)


def render_node_inventory(lines, items, children):
    lines.extend(
        [
            "### Inventaire des nœuds",
            "",
            "| NodeID | Talent | Profondeur de progression | Rangée visuelle | Position X/Y | Parent(s) | Enfant(s) |",
            "|---:|---|---:|---:|---|---|---|",
        ]
    )
    for item in sorted(items, key=natural_node_key):
        parents = ", ".join(item["parents"]) if item["parents"] else "RACINE"
        child_ids = ", ".join(children[item["node_id"]]) if children[item["node_id"]] else "FEUILLE"
        lines.append(
            f"| {item['node_id']} | {md_escape(clean_name(item['talent']))} | {item['progression_depth']} | "
            f"{item['visual_row']} | "
            f"{item['x']} / {item['y']} (offset {md_escape(item['offset'])}) | {parents} | {child_ids} |"
        )
    lines.append("")


def render_depth_detail(lines, items, children):
    by_depth = defaultdict(list)
    by_id = {item["node_id"]: item for item in items}
    for item in items:
        by_depth[item["progression_depth"]].append(item)
    lines.extend(["### Détail par profondeur de progression", ""])
    for depth in sorted(by_depth):
        lines.extend([f"#### Niveau de progression {depth + 1}", ""])
        for item in sorted(by_depth[depth], key=natural_node_key):
            parents = refs(item["parents"], by_id, "RACINE")
            child_ids = refs(children[item["node_id"]], by_id, "aucun")
            lines.extend(
                [
                    f"##### {clean_name(item['talent'])}",
                    "",
                    f"- NodeID: `{item['node_id']}`",
                    f"- position UI: {position_label(item)}",
                    f"- effet: {item['effect'] or 'Non chiffré'}",
                    f"- coût: {item['cost'] or 'Non explicite'}",
                    f"- rangs: {item['ranks']}",
                    f"- parent(s): {parents}",
                    f"- débloque: {child_ids}",
                    f"- profondeur de progression: {item['progression_depth']}",
                    f"- rangée visuelle / NodeTierY: {item['visual_row']}",
                    f"- position UI: X {item['x']}, Y {item['y']}, offset {item['offset']}",
                    f"- gain/rendement: {item['gain']} / {item['yield']}",
                    "",
                ]
            )


def render_ambush_logical_check(lines, items, children):
    by_id = {item["node_id"]: item for item in items}
    raw_nodes = {str(row["ID"]): row for row in load_json("CharPCSkillTreeNode")}
    buffs = {str(row["ID"]): row for row in load_json("ChComBuff")}
    lines.extend(
        [
            "### Contrôle talent logique / rang - Embuscade",
            "",
            "Décision HUMAN: **FUSIONNÉ** en un talent logique `Embuscade` à 4 rangs. Les NodeID restent distincts dans ce graphe technique.",
            "",
            "Preuves contrôlées:",
            "",
            "- `NodeMaxLevel=1` pour chaque NodeID Embuscade.",
            "- `BuffLevel=1` pour chaque BuffID direct.",
            "- `BuffGroupID` diffère entre les BuffID directs.",
            "- `NodeValue`, `TriggeredBuffID`, descriptions et effets déclenchés diffèrent.",
            "- La fusion ne repose pas sur un regex de nom: elle est limitée aux NodeID explicites `111201`, `111202`, `111402`, `111602`, validés pour Assassin / Attaque sournoise.",
            "- Les signaux retenus ensemble sont la même branche GameData, la suite UI `st_ambushed_1..4`, les libellés localisés I..IV et le contrôle utilisateur.",
            "",
            "| Libellé | NodeID | NodeValue / BuffID | NodeMaxLevel | BuffGroupID | BuffLevel | Parent(s) | Enfant(s) |",
            "|---|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for node_id in AMBUSH_NODE_IDS:
        item = by_id[node_id]
        node = raw_nodes[node_id]
        buff = buffs.get(str(node.get("NodeValue")), {})
        parents = ", ".join(item["parents"]) if item["parents"] else "RACINE"
        child_ids = ", ".join(children[item["node_id"]]) if children[item["node_id"]] else "FEUILLE"
        lines.append(
            f"| {md_escape(clean_name(item['talent']))} | {node_id} | {node.get('NodeValue')} | "
            f"{node.get('NodeMaxLevel')} | {buff.get('BuffGroupID', '')} | {buff.get('BuffLevel', '')} | "
            f"{parents} | {child_ids} |"
        )
    lines.extend(
        [
            "",
            "Conséquence HUMAN: `Embuscade` apparaît une seule fois avec les rangs I à IV; les parents, enfants, VisualRow et positions restent dans les données techniques.",
            "",
        ]
    )


def build_assassin():
    rows = read_rows()
    raw_nodes = {str(row["ID"]): row for row in load_json("CharPCSkillTreeNode")}
    by_node = defaultdict(list)
    for row in rows:
        if row["MainTab"] == "SJWSkillTree" and row["SubTab"] == "Assassin":
            by_node[str(row["NodeID"])].append(row)
    assassin = []
    for node_id, entries in by_node.items():
        sample = entries[0]
        effect, gain_values, _ = effect_summary(entries)
        gain = " / ".join(gain_values) if gain_values else "Non chiffré"
        assassin.append(
            {
                "system": "class",
                "section": "Assassin",
                "branch": sample["Branch"],
                "node_id": node_id,
                "talent": clean_name(sample["TalentName"]),
                "effect": effect,
                "cost": sample["Cost"],
                "ranks": sample["MaxRank"],
                "gain": gain,
                "yield": "NON DÉTERMINÉ",
                "progression_depth": int(sample["ProgressionDepth"]),
                "visual_row": int(sample["VisualRow"]),
                "x": int(raw_nodes[node_id].get("NodeTierX") or 0),
            }
        )
    for item in assassin:
        node = raw_nodes[item["node_id"]]
        item["node_group"] = int(node["SkillTreelNodeGroup"])
        item["parents"] = [str(v) for v in maybe_list(node.get("SlotLinkNodeID"))]
        item["y"] = item["visual_row"]
        item["offset"] = str(node.get("NodeOffset") or "")
        item["node_type"] = str(node.get("NodeType") or "")
    by_section = defaultdict(list)
    class_nodes = []
    for item in assassin:
        if item["node_type"] == "Identity":
            class_nodes.append(item)
        else:
            by_section[(item["node_group"], item["branch"])].append(item)
    return class_nodes, by_section


def write_report():
    class_nodes, by_section = build_assassin()
    lines = [
        "# Assassin - Graphe orienté de l'arbre de talents",
        "",
        "Source primaire: `CharPCSkillTreeNode` pour les nœuds, parents, rangées visuelles et positions; `sjw_talent_tree.csv` pour les noms, coûts, rangs techniques, talents logiques, effets et profondeurs de progression.",
        "",
        "Règle de reconstruction: la progression réelle vient uniquement des relations Parent/Enfant (`SlotLinkNodeID`). `NodeTierY` est conservé comme rangée visuelle (`VisualRow`) et ne crée aucune connexion.",
        "",
        "Structure UI validée: Assassin contient deux sections de progression et un nœud central de classe / Overdrive séparé. Total: 21 nœuds.",
        "",
        "## Sections / NodeGroups",
        "",
    ]
    if class_nodes:
        lines.append(f"- Nœud de classe / Overdrive: {len(class_nodes)} nœud")
    for (node_group, branch), items in sorted(by_section.items()):
        lines.append(f"- NodeGroup `{node_group}` — {branch}: {len(items)} nœuds")
    lines.append("")

    if class_nodes:
        children = {item["node_id"]: [] for item in class_nodes}
        stats = graph_stats(class_nodes, children, [])
        lines.extend(["## Nœud de classe / Overdrive", ""])
        render_validation(lines, stats)
        render_node_inventory(lines, class_nodes, children)
        render_depth_detail(lines, class_nodes, children)

    for (node_group, branch), items in sorted(by_section.items()):
        node_ids = {item["node_id"] for item in items}
        children = {item["node_id"]: [] for item in items}
        missing_parents = []
        for item in items:
            for parent in item["parents"]:
                if parent in node_ids:
                    children[parent].append(item["node_id"])
                else:
                    missing_parents.append(f"{item['node_id']}→{parent}")
        for node_id in children:
            children[node_id].sort(key=lambda child_id: natural_node_key(next(i for i in items if i["node_id"] == child_id)))
        stats = graph_stats(items, children, sorted(set(missing_parents)))
        ui_status, _, _ = validate_against_ui(branch, items)
        depth_status = validate_depths(branch, items)

        lines.extend([f"## {branch}", "", f"NodeGroup: `{node_group}`", ""])
        lines.extend([f"Validation contre les arêtes UI fournies: **{ui_status}**", ""])
        lines.extend([f"Validation des profondeurs de progression: **{depth_status}**", ""])
        render_validation(lines, stats)
        render_node_inventory(lines, items, children)
        if branch == "Attaque sournoise":
            render_ambush_logical_check(lines, items, children)
        lines.extend(["### Vue de progression", "", "Version Mermaid complète:", ""])
        render_mermaid(lines, items, children)
        lines.extend(["Version ASCII de lecture:", ""])
        render_ascii(lines, items, children)
        render_depth_detail(lines, items, children)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    write_report()
    print(OUT)


if __name__ == "__main__":
    main()
