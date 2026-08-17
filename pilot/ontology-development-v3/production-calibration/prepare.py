#!/usr/bin/env python3
"""Prepare the frozen 30-paper one-pass calibration inputs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SQLITE_DIR = SCRIPT_DIR.parent / "sqlite"
sys.path.append(str(SQLITE_DIR))

from jats_metadata import parse_jats  # noqa: E402


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def records() -> list[dict[str, str]]:
    pilot_rows = {
        row["record_id"]: row
        for row in read_tsv(SCRIPT_DIR.parent / "sqlite" / "PILOT_SET.tsv")
    }
    holdout_rows = {
        row["holdout_id"]: row
        for row in read_tsv(SCRIPT_DIR.parent / "validation" / "holdout.tsv")
    }
    output: list[dict[str, str]] = []
    for number in range(1, 11):
        record_id = f"H{number:02d}"
        pilot = pilot_rows[record_id]
        holdout = holdout_rows[record_id]
        candidate_ids = pilot["project_id"]
        if record_id == "H09":
            candidate_ids = "341-RA;357-RA"
        output.append(
            {
                "record_id": record_id,
                "doi": pilot["doi"],
                "article_path": pilot["article_path"],
                "article_sha256": holdout["source_sha256"],
                "article_bytes": holdout["bytes"],
                "xml_path": pilot["xml_path"],
                "xml_sha256": pilot["xml_sha256"],
                "candidate_project_ids": candidate_ids,
                "reference_path": pilot["record_path"],
            }
        )
    for row in read_tsv(SCRIPT_DIR.parent / "broader" / "BATCH.tsv"):
        output.append(
            {
                "record_id": row["record_id"],
                "doi": row["doi"],
                "article_path": row["article_path"],
                "article_sha256": row["article_sha256"],
                "article_bytes": row["article_bytes"],
                "xml_path": row["xml_path"],
                "xml_sha256": row["xml_sha256"],
                "candidate_project_ids": row["project_id"],
                "reference_path": f"pilot/ontology-development-v3/broader/records/{row['record_id']}.md",
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="EXTRACTION_TASK.md")
    parser.add_argument("--input-set", default="inputs")
    parser.add_argument("--metadata-set", default="metadata")
    parser.add_argument("--manifest", default="MANIFEST.tsv")
    parser.add_argument("--ids", help="comma-separated record IDs; default is all")
    parser.add_argument("--addon", help="optional instruction file appended to the task")
    args = parser.parse_args()
    for value in (args.task, args.input_set, args.metadata_set, args.manifest, args.addon):
        if value is None:
            continue
        if Path(value).name != value:
            raise ValueError("Preparation file and directory names must not contain a path")

    input_dir = SCRIPT_DIR / args.input_set
    metadata_dir = SCRIPT_DIR / args.metadata_set
    input_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)
    graph = (SCRIPT_DIR / "ONTOLOGY_GRAPH.md").read_text(encoding="utf-8")
    task = (SCRIPT_DIR / args.task).read_text(encoding="utf-8")
    if args.addon:
        task = task.rstrip() + "\n\n" + (SCRIPT_DIR / args.addon).read_text(encoding="utf-8")

    selected = records()
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        selected = [item for item in selected if item["record_id"] in wanted]
        found = {item["record_id"] for item in selected}
        if found != wanted:
            raise ValueError(f"Unknown record IDs: {sorted(wanted - found)}")

    manifest_rows: list[dict[str, str | int]] = []
    for item in selected:
        article_path = REPO_ROOT / item["article_path"]
        xml_path = REPO_ROOT / item["xml_path"]
        reference_path = REPO_ROOT / item["reference_path"]
        for path in (article_path, xml_path, reference_path):
            if not path.is_file():
                raise FileNotFoundError(path)
        if article_path.stat().st_size != int(item["article_bytes"]):
            raise ValueError(f"{item['record_id']}: article byte-count mismatch")
        if digest(article_path) != item["article_sha256"]:
            raise ValueError(f"{item['record_id']}: article SHA-256 mismatch")
        if digest(xml_path) != item["xml_sha256"]:
            raise ValueError(f"{item['record_id']}: JATS SHA-256 mismatch")

        parsed = parse_jats(xml_path)
        if parsed["publication"]["doi"] != item["doi"].lower():
            raise ValueError(f"{item['record_id']}: JATS DOI mismatch")
        metadata = slim_metadata(parsed)
        metadata_path = metadata_dir / f"{item['record_id']}.json"
        metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        candidate_ids = [value for value in item["candidate_project_ids"].split(";") if value]
        candidates = [project_candidate(value) for value in candidate_ids]
        article = article_path.read_text(encoding="utf-8")
        prompt = "\n\n".join(
            [
                graph.rstrip(),
                task.rstrip(),
                "# Calibration item\n\n"
                f"- Record ID: `{item['record_id']}`\n"
                f"- DOI: `{item['doi']}`\n"
                "- The candidate projects below are context, not proof.",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(metadata, ensure_ascii=False, indent=2)
                + "\n```",
                "## Candidate EuroQol projects\n\n```json\n"
                + json.dumps(candidates, ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + article.rstrip(),
            ]
        ) + "\n"
        input_path = input_dir / f"{item['record_id']}.md"
        input_path.write_text(prompt, encoding="utf-8")
        manifest_rows.append(
            {
                **item,
                "xml_bytes": xml_path.stat().st_size,
                "metadata_path": str(metadata_path.relative_to(REPO_ROOT)),
                "metadata_sha256": digest(metadata_path),
                "input_path": str(input_path.relative_to(REPO_ROOT)),
                "input_sha256": digest(input_path),
                "input_bytes": input_path.stat().st_size,
                "reference_sha256": digest(reference_path),
            }
        )

    manifest_path = SCRIPT_DIR / args.manifest
    fields = list(manifest_rows[0])
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest_rows)
    print(f"Prepared {len(manifest_rows)} one-pass inputs")
    print(f"Manifest: {manifest_path}")
    print(f"Manifest SHA-256: {digest(manifest_path)}")


if __name__ == "__main__":
    main()
