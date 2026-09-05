#!/usr/bin/env python3
"""Build external co-authorship files from the resolved publication authors."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sqlite3
import xml.etree.ElementTree as ET
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args()


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def graphml(nodes: list[dict[str, object]], edges: list[dict[str, object]]) -> ET.ElementTree:
    namespace = "http://graphml.graphdrawing.org/xmlns"
    ET.register_namespace("", namespace)
    root = ET.Element(f"{{{namespace}}}graphml")
    keys = (
        ("name", "node", "name", "string"),
        ("paper_count", "node", "paper_count", "int"),
        ("project_count", "node", "project_count", "int"),
        ("euroqol_member", "node", "euroqol_member", "boolean"),
        ("project_leader", "node", "project_leader", "boolean"),
        ("weight", "edge", "weight", "int"),
        ("distance", "edge", "distance", "double"),
    )
    for key_id, target, name, value_type in keys:
        ET.SubElement(
            root,
            f"{{{namespace}}}key",
            {"id": key_id, "for": target, "attr.name": name, "attr.type": value_type},
        )
    graph = ET.SubElement(root, f"{{{namespace}}}graph", {"edgedefault": "undirected"})
    for row in nodes:
        element = ET.SubElement(graph, f"{{{namespace}}}node", {"id": str(row["person_id"])})
        for key in ("name", "paper_count", "project_count", "euroqol_member", "project_leader"):
            value = row[key]
            if isinstance(value, bool):
                value = str(value).lower()
            ET.SubElement(element, f"{{{namespace}}}data", {"key": key}).text = str(value)
    for index, row in enumerate(edges, 1):
        element = ET.SubElement(
            graph,
            f"{{{namespace}}}edge",
            {"id": f"e{index}", "source": str(row["source"]), "target": str(row["target"])},
        )
        ET.SubElement(element, f"{{{namespace}}}data", {"key": "weight"}).text = str(
            row["coauthored_paper_count"]
        )
        ET.SubElement(element, f"{{{namespace}}}data", {"key": "distance"}).text = str(
            row["layout_distance"]
        )
    return ET.ElementTree(root)


def main() -> None:
    args = parse_args()
    output = args.output_directory
    output.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(f"file:{args.database.resolve()}?mode=ro", uri=True)
    people = {
        row[0]: {
            "person_id": row[0],
            "name": row[1],
            "orcid": row[2] or "",
            "openalex_id": row[3] or "",
        }
        for row in connection.execute(
            "SELECT person_id, display_name, orcid, openalex_id FROM person WHERE entity_kind='PERSON'"
        )
    }
    memberships = {
        row[0] for row in connection.execute("SELECT person_id FROM euroqol_membership")
    }
    leaders = {
        row[0]
        for row in connection.execute(
            "SELECT DISTINCT person_id FROM project_person WHERE role='PRINCIPAL_INVESTIGATOR'"
        )
    }
    project_counts = dict(
        connection.execute(
            "SELECT person_id, COUNT(DISTINCT project_id) FROM project_person GROUP BY person_id"
        )
    )
    publication_metadata = {
        row[0]: {"doi": row[1] or "", "title": row[2]}
        for row in connection.execute(
            """
            SELECT publication_id, doi, title FROM publication AS p
            WHERE EXISTS (SELECT 1 FROM study AS s WHERE s.publication_id=p.publication_id)
            """
        )
    }
    by_publication: dict[str, list[str]] = defaultdict(list)
    for publication_id, person_id in connection.execute(
        """
        SELECT pa.publication_id, pa.person_id
        FROM publication_author AS pa
        JOIN person AS p USING (person_id)
        WHERE p.entity_kind='PERSON'
          AND EXISTS (
            SELECT 1 FROM study AS s WHERE s.publication_id=pa.publication_id
          )
        ORDER BY pa.publication_id, pa.author_order
        """
    ):
        by_publication[publication_id].append(person_id)
    connection.close()

    person_papers: dict[str, set[str]] = defaultdict(set)
    pair_papers: dict[tuple[str, str], set[str]] = defaultdict(set)
    for publication_id, person_ids in by_publication.items():
        unique_ids = list(dict.fromkeys(person_ids))
        for person_id in unique_ids:
            person_papers[person_id].add(publication_id)
        for source, target in combinations(sorted(unique_ids), 2):
            pair_papers[(source, target)].add(publication_id)

    nodes = []
    for person_id, papers in person_papers.items():
        person = people[person_id]
        nodes.append(
            {
                **person,
                "paper_count": len(papers),
                "project_count": project_counts.get(person_id, 0),
                "euroqol_member": person_id in memberships,
                "project_leader": person_id in leaders,
                "publication_ids": ";".join(sorted(papers)),
            }
        )
    nodes.sort(key=lambda row: (-int(row["paper_count"]), str(row["name"]), str(row["person_id"])))
    edges = []
    for (source, target), papers in pair_papers.items():
        count = len(papers)
        edges.append(
            {
                "source": source,
                "target": target,
                "coauthored_paper_count": count,
                "layout_distance": round(1 / math.sqrt(count), 6),
                "publication_ids": ";".join(sorted(papers)),
                "dois": ";".join(
                    publication_metadata[publication_id]["doi"] for publication_id in sorted(papers)
                ),
            }
        )
    edges.sort(
        key=lambda row: (
            -int(row["coauthored_paper_count"]), str(row["source"]), str(row["target"])
        )
    )

    write_csv(
        output / "nodes.csv",
        (
            "person_id", "name", "paper_count", "project_count", "euroqol_member",
            "project_leader", "orcid", "openalex_id", "publication_ids",
        ),
        nodes,
    )
    write_csv(
        output / "edges.csv",
        (
            "source", "target", "coauthored_paper_count", "layout_distance",
            "publication_ids", "dois",
        ),
        edges,
    )
    (output / "network.json").write_text(
        json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    graphml(nodes, edges).write(output / "network.graphml", encoding="utf-8", xml_declaration=True)
    summary = {
        "scope": "external co-authorship analysis; no co-author edges are loaded into the research database",
        "publications": len(by_publication),
        "person_nodes": len(nodes),
        "coauthor_edges": len(edges),
        "people_with_multiple_papers": sum(int(row["paper_count"]) > 1 for row in nodes),
        "maximum_paper_count": max((int(row["paper_count"]) for row in nodes), default=0),
        "maximum_pair_count": max((int(row["coauthored_paper_count"]) for row in edges), default=0),
        "node_size_field": "paper_count",
        "layout_edge_weight_field": "coauthored_paper_count",
        "layout_distance_field": "layout_distance",
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
