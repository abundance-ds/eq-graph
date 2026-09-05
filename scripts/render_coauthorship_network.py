#!/usr/bin/env python3
"""Render a standalone co-authorship network from the analysis JSON file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATE_PATH = Path(__file__).with_name("templates") / "coauthorship-network.html"
DATA_MARKER = "__COAUTHORSHIP_DATA__"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--minimum-papers",
        type=int,
        default=2,
        help="Show authors with at least this many papers. Default: 2.",
    )
    return parser.parse_args()


def build_payload(source: dict[str, object], minimum_papers: int) -> dict[str, object]:
    if minimum_papers < 1:
        raise ValueError("--minimum-papers must be at least 1")

    source_nodes = source.get("nodes")
    source_edges = source.get("edges")
    if not isinstance(source_nodes, list) or not isinstance(source_edges, list):
        raise ValueError("The input must contain node and edge lists")

    selected = sorted(
        (node for node in source_nodes if int(node["paper_count"]) >= minimum_papers),
        key=lambda node: (
            -int(node["paper_count"]),
            str(node["name"]).casefold(),
            str(node["person_id"]),
        ),
    )
    id_map = {str(node["person_id"]): index for index, node in enumerate(selected)}
    nodes = [
        {
            "id": id_map[str(node["person_id"])],
            "n": str(node["name"]),
            "p": int(node["paper_count"]),
            "m": bool(node.get("euroqol_member")),
            "l": bool(node.get("project_leader")),
        }
        for node in selected
    ]
    links = [
        {
            "source": id_map[str(edge["source"])],
            "target": id_map[str(edge["target"])],
            "w": int(edge["coauthored_paper_count"]),
        }
        for edge in source_edges
        if str(edge["source"]) in id_map and str(edge["target"]) in id_map
    ]
    publication_ids = {
        publication_id
        for node in selected
        for publication_id in str(node.get("publication_ids", "")).split(";")
        if publication_id
    }
    return {
        "meta": {
            "minimum_papers": minimum_papers,
            "authors": len(nodes),
            "links": len(links),
            "publications": len(publication_ids),
        },
        "nodes": nodes,
        "links": links,
    }


def main() -> None:
    args = parse_args()
    source = json.loads(args.network_json.read_text(encoding="utf-8"))
    payload = build_payload(source, args.minimum_papers)
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if template.count(DATA_MARKER) != 1:
        raise ValueError(f"Expected one {DATA_MARKER} marker in {TEMPLATE_PATH}")

    rendered = template.replace(
        DATA_MARKER,
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(
        f"Wrote {args.output}: {payload['meta']['authors']} authors, "
        f"{payload['meta']['links']} links, {payload['meta']['publications']} papers"
    )


if __name__ == "__main__":
    main()
