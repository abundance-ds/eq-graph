#!/usr/bin/env python3
"""Prepare a deterministic sample of unseen repository JATS articles."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import sys
from collections import defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SQLITE_DIR = SCRIPT_DIR.parent / "sqlite"
sys.path.append(str(SQLITE_DIR))

from jats_metadata import parse_jats  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def project_candidate(project_id: str) -> dict[str, object]:
    folder = REPO_ROOT / "input" / "projects" / project_id
    project_path = folder / "project.json"
    if not project_path.is_file():
        return {"project_id": project_id, "metadata_available": False}
    source = json.loads(project_path.read_text(encoding="utf-8"))
    abstract_path = folder / "abstract.txt"
    return {
        "project_id": project_id,
        "title": source.get("title"),
        "principal_investigator": source.get("pi_name_raw"),
        "grant_type": source.get("grant_type"),
        "working_groups": source.get("working_groups"),
        "status": source.get("status"),
        "start_year": source.get("start_year"),
        "end_year": source.get("end_year"),
        "abstract": abstract_path.read_text(encoding="utf-8").strip()
        if abstract_path.is_file()
        else None,
    }


def slim_metadata(parsed: dict) -> dict:
    return {
        "publication": parsed["publication"],
        "dates": parsed["dates"],
        "authors": parsed["authors"],
        "affiliations": parsed["affiliations"],
        "funding": parsed["funding"],
        "keywords": parsed["keywords"],
        "categories": parsed["categories"],
        "correspondence": parsed["correspondence"],
    }


def discover() -> dict[str, list[dict[str, object]]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    pattern = REPO_ROOT / "input" / "projects"
    for xml_path in sorted(pattern.glob("*/papers/*.xml")):
        project_id = xml_path.parents[1].name
        article_path = REPO_ROOT / "corpus" / project_id / f"{xml_path.stem}.md"
        if not article_path.is_file():
            continue
        parsed = parse_jats(xml_path)
        doi = parsed["publication"].get("doi")
        if not doi:
            continue
        groups[doi].append(
            {
                "project_id": project_id,
                "xml_path": xml_path,
                "article_path": article_path,
                "parsed": parsed,
            }
        )
    return groups


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=50)
    parser.add_argument("--seed", type=int, default=20260817)
    parser.add_argument("--name", default="production-50")
    parser.add_argument(
        "--exclude-manifest",
        action="append",
        default=["MANIFEST.tsv"],
        help="manifest path inside this directory; can be used more than once",
    )
    args = parser.parse_args()
    if not 1 <= args.size <= 200:
        raise ValueError("size must be from 1 to 200")
    if Path(args.name).name != args.name:
        raise ValueError("name must not contain a path")

    excluded: set[str] = set()
    for value in args.exclude_manifest:
        path = (SCRIPT_DIR / value).resolve()
        if SCRIPT_DIR.resolve() not in path.parents:
            raise ValueError("exclude manifest must be inside the calibration directory")
        excluded.update(row["doi"].casefold() for row in read_tsv(path))
    groups = discover()
    eligible = sorted(doi for doi in groups if doi.casefold() not in excluded)
    if args.size > len(eligible):
        raise ValueError(f"requested {args.size} records from {len(eligible)} eligible DOI records")
    selected_dois = sorted(random.Random(args.seed).sample(eligible, args.size))

    output_root = SCRIPT_DIR / args.name
    input_dir = output_root / "inputs"
    metadata_dir = output_root / "metadata"
    input_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)
    graph_path = SCRIPT_DIR / "ONTOLOGY_GRAPH.md"
    task_path = SCRIPT_DIR / "EXTRACTION_TASK_V3.md"
    addon_path = SCRIPT_DIR / "INDEX_TASK.md"
    graph = graph_path.read_text(encoding="utf-8").rstrip()
    task = task_path.read_text(encoding="utf-8").rstrip()
    addon = addon_path.read_text(encoding="utf-8").rstrip()
    instructions = "\n\n".join([graph, task, addon])

    rows: list[dict[str, object]] = []
    for number, doi in enumerate(selected_dois, 1):
        record_id = f"P{number:03d}"
        copies = groups[doi]
        canonical = sorted(copies, key=lambda item: str(item["xml_path"]))[0]
        project_ids = sorted({str(item["project_id"]) for item in copies})
        article_path = canonical["article_path"]
        xml_path = canonical["xml_path"]
        metadata = slim_metadata(canonical["parsed"])
        metadata_path = metadata_dir / f"{record_id}.json"
        metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        candidates = [project_candidate(project_id) for project_id in project_ids]
        prompt = "\n\n".join(
            [
                instructions,
                "# Production-pilot item\n\n"
                f"- Record ID: `{record_id}`\n"
                f"- DOI: `{doi}`\n"
                "- The candidate projects below are context, not proof.",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(metadata, ensure_ascii=False, indent=2)
                + "\n```",
                "## Candidate EuroQol projects\n\n```json\n"
                + json.dumps(candidates, ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + article_path.read_text(encoding="utf-8").rstrip(),
            ]
        ) + "\n"
        input_path = input_dir / f"{record_id}.md"
        input_path.write_text(prompt, encoding="utf-8")
        rows.append(
            {
                "record_id": record_id,
                "doi": doi,
                "article_path": str(article_path.relative_to(REPO_ROOT)),
                "article_sha256": digest(article_path),
                "article_bytes": article_path.stat().st_size,
                "xml_path": str(xml_path.relative_to(REPO_ROOT)),
                "xml_sha256": digest(xml_path),
                "xml_bytes": xml_path.stat().st_size,
                "candidate_project_ids": ";".join(project_ids),
                "metadata_path": str(metadata_path.relative_to(REPO_ROOT)),
                "metadata_sha256": digest(metadata_path),
                "input_path": str(input_path.relative_to(REPO_ROOT)),
                "input_sha256": digest(input_path),
                "input_bytes": input_path.stat().st_size,
                "graph_sha256": digest(graph_path),
                "task_sha256": digest(task_path),
                "addon_sha256": digest(addon_path),
            }
        )

    manifest_path = output_root / "MANIFEST.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"eligible_unique_dois={len(eligible)}")
    print(f"excluded_unique_dois={len(excluded)}")
    print(f"selected={len(rows)}")
    print(f"seed={args.seed}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")


if __name__ == "__main__":
    main()
