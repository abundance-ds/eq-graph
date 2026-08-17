#!/usr/bin/env python3
"""Rebuild selected production prompts with the current compact instructions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from prepare_corpus import project_candidate


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-manifest", required=True)
    parser.add_argument("--ids", required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    base_path = (SCRIPT_DIR / args.base_manifest).resolve()
    if SCRIPT_DIR.resolve() not in base_path.parents:
        raise ValueError("base manifest must be inside the calibration directory")
    wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
    selected = [row for row in read_tsv(base_path) if row["record_id"] in wanted]
    found = {row["record_id"] for row in selected}
    if found != wanted:
        raise ValueError(f"Unknown record IDs: {sorted(wanted - found)}")

    output_root = SCRIPT_DIR / args.name
    input_dir = output_root / "inputs"
    input_dir.mkdir(parents=True, exist_ok=True)
    graph_path = SCRIPT_DIR / "ONTOLOGY_GRAPH.md"
    task_path = SCRIPT_DIR / "EXTRACTION_TASK_V3.md"
    addon_path = SCRIPT_DIR / "INDEX_TASK.md"
    instructions = "\n\n".join(
        path.read_text(encoding="utf-8").rstrip()
        for path in (graph_path, task_path, addon_path)
    )

    output: list[dict[str, str]] = []
    for item in selected:
        metadata = json.loads((REPO_ROOT / item["metadata_path"]).read_text(encoding="utf-8"))
        project_ids = [value for value in item["candidate_project_ids"].split(";") if value]
        candidates = [project_candidate(project_id) for project_id in project_ids]
        article_path = REPO_ROOT / item["article_path"]
        prompt = "\n\n".join(
            [
                instructions,
                "# Targeted-repair item\n\n"
                f"- Record ID: `{item['record_id']}`\n"
                f"- DOI: `{item['doi']}`\n"
                "- The candidate projects below are context, not proof.\n"
                "- Produce the complete record again. This is not an edit of an earlier output.",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(metadata, ensure_ascii=False, indent=2)
                + "\n```",
                "## Candidate EuroQol projects\n\n```json\n"
                + json.dumps(candidates, ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + article_path.read_text(encoding="utf-8").rstrip(),
            ]
        ) + "\n"
        input_path = input_dir / f"{item['record_id']}.md"
        input_path.write_text(prompt, encoding="utf-8")
        revised = dict(item)
        revised.update(
            {
                "input_path": str(input_path.relative_to(REPO_ROOT)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "graph_sha256": digest(graph_path),
                "task_sha256": digest(task_path),
                "addon_sha256": digest(addon_path),
            }
        )
        output.append(revised)

    manifest_path = output_root / "MANIFEST.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(output[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(output)
    print(f"selected={len(output)}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")


if __name__ == "__main__":
    main()
