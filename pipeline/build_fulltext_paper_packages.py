#!/usr/bin/env python3
"""Build full-text paper packages from accepted abstract-screen results."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

from scale_publication_metadata import load_publications


ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "scale/protocol-2.0/article-corpus.jsonl"
CANONICAL_METADATA = ROOT / "scale/protocol-2.0/source-union.jsonl"
PROJECTS = ROOT / "data/funded-projects-canonical.csv"
SCREEN = ROOT / "scale/protocol-2.0/abstract-screen-v2-codex-r5/results.jsonl"
YEAR_OVERRIDES = ROOT / "pipeline/data/publication_year_overrides.tsv"

PUBLICATION_FIELDS = (
    "record_id",
    "doi",
    "pmid",
    "title",
    "year",
    "year_source",
    "document_types",
    "venue",
    "authors",
    "abstract",
    "abstract_source",
    "linked_people",
    "discovery_routes",
    "sources",
    "openalex_ids",
    "funders",
    "euroqol_award_ids",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screen", type=Path, default=SCREEN)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument(
        "--canonical-metadata", type=Path, default=CANONICAL_METADATA
    )
    parser.add_argument("--projects", type=Path, default=PROJECTS)
    parser.add_argument("--year-overrides", type=Path, default=YEAR_OVERRIDES)
    parser.add_argument("--fulltext-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def read_jsonl(path: Path, key: str) -> dict[str, dict[str, Any]]:
    values: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            value = json.loads(line)
            item_id = value[key]
            if item_id in values:
                raise ValueError(f"Duplicate {key}: {item_id}")
            values[item_id] = value
    return values


def read_manifest(path: Path) -> list[dict[str, str]]:
    delimiter = "\t" if path.suffix.casefold() == ".tsv" else ","
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter=delimiter))
    if not rows or "record_id" not in rows[0]:
        raise ValueError("The full-text manifest must contain record_id.")
    return rows


def read_projects(path: Path) -> dict[str, dict[str, Any]]:
    values: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            project_id = row["Project Id"]
            values[project_id] = {
                "project_id": project_id,
                "title": row["Title"],
                "abstract": row["Abstract"],
                "principal_investigator": row["Project PI / Applicant Name"],
                "working_group": row["Working Group"],
                "start_year": int(row["Start Year"]) if row["Start Year"].isdigit() else None,
                "end_year": int(row["End Year"]) if row["End Year"].isdigit() else None,
                "status": row["Status"],
            }
    return values


def apply_year_overrides(
    corpus: dict[str, dict[str, Any]],
    path: Path,
) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            record_id = row["record_id"]
            if record_id in corpus and not isinstance(corpus[record_id].get("year"), int):
                corpus[record_id]["year"] = int(row["year"])
                corpus[record_id]["year_source"] = "reviewed_override"


def text_reference(row: dict[str, str]) -> tuple[Path, str, str]:
    text_value = row.get("text_path") or row.get("markdown_path") or row.get("source_path")
    if not text_value:
        raise ValueError(f"No text path for {row['record_id']}.")
    path = Path(text_value)
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file():
        raise ValueError(f"Missing text for {row['record_id']}: {path}")
    expected = row.get("text_sha256") or row.get("markdown_sha256") or row.get("source_sha256")
    actual = digest(path)
    if expected and expected != actual:
        raise ValueError(f"Text hash mismatch for {row['record_id']}.")
    source_format = row.get("source_format") or row.get("format") or path.suffix.lstrip(".")
    return path, actual, source_format


def metadata_reference(
    row: dict[str, str], publication: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    value = row.get("metadata_path")
    if not value:
        return {"publication": publication}, {"path": None, "sha256": None}
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file():
        raise ValueError(f"Missing deterministic metadata for {row['record_id']}: {path}")
    actual = digest(path)
    expected = row.get("metadata_sha256")
    if expected and expected != actual:
        raise ValueError(f"Metadata hash mismatch for {row['record_id']}.")
    parsed = json.loads(path.read_text(encoding="utf-8"))
    reference = {
        "path": str(path.relative_to(ROOT)),
        "sha256": actual,
        "structured_reference_count": len(parsed.get("references", [])),
    }
    return {key: value for key, value in parsed.items() if key != "references"}, reference


def main() -> None:
    args = parse_args()
    args.output = args.output.resolve()
    screen = read_jsonl(args.screen, "record_id")
    corpus = load_publications(args.corpus, args.canonical_metadata)
    apply_year_overrides(corpus, args.year_overrides)
    projects = read_projects(args.projects)
    manifest = read_manifest(args.fulltext_manifest)
    packages = args.output / "packages"
    packages.mkdir(parents=True, exist_ok=True)
    output_rows: list[dict[str, str]] = []

    for row in manifest:
        record_id = row["record_id"]
        if record_id not in screen:
            raise ValueError(f"No abstract-screen result for {record_id}.")
        result = screen[record_id]
        if result["decision"] in {"NO", "EXCLUDE"}:
            continue
        if result["decision"] not in {"YES", "UNCERTAIN", "RETRIEVE_FULL_TEXT"}:
            raise ValueError(f"Invalid screen decision for {record_id}.")
        if record_id not in corpus:
            raise ValueError(f"No publication metadata for {record_id}.")
        publication = corpus[record_id]
        candidate_projects: list[dict[str, Any]] = []
        for project_id in result["project_ids"]:
            if project_id not in projects:
                raise ValueError(f"Unknown project {project_id} for {record_id}.")
            project = projects[project_id]
            if project["start_year"] is not None and project["start_year"] > publication["year"]:
                raise ValueError(f"Project {project_id} starts after {record_id}.")
            candidate_projects.append(project)
        path, text_sha256, source_format = text_reference(row)
        deterministic_metadata, metadata_file = metadata_reference(row, publication)
        package = {
            "package_version": "2.0",
            "record_id": record_id,
            "publication": {field: publication.get(field) for field in PUBLICATION_FIELDS},
            "abstract_screen": result,
            "candidate_projects": candidate_projects,
            "deterministic_metadata": deterministic_metadata,
            "metadata_file": metadata_file,
            "full_text": {
                "path": str(path.relative_to(ROOT)),
                "sha256": text_sha256,
                "format": source_format,
                "source_path": row.get("source_path"),
                "source_sha256": row.get("source_sha256"),
                "source_method": row.get("source_method"),
                "source_url": row.get("source_url"),
            },
        }
        package_path = packages / f"{record_id}.json"
        package_path.write_text(
            json.dumps(package, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        output_rows.append(
            {
                "record_id": record_id,
                "screen_decision": result["decision"],
                "candidate_project_ids": ";".join(result["project_ids"]),
                "package_path": str(package_path.relative_to(ROOT)),
                "package_sha256": digest(package_path),
                "text_path": str(path.relative_to(ROOT)),
                "text_sha256": text_sha256,
                "metadata_path": metadata_file["path"] or "",
                "metadata_sha256": metadata_file["sha256"] or "",
            }
        )

    output_manifest = args.output / "MANIFEST.tsv"
    if output_rows:
        with output_manifest.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=list(output_rows[0]),
                delimiter="\t",
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(output_rows)
    summary = {
        "package_version": "2.0",
        "fulltext_manifest_records": len(manifest),
        "packages": len(output_rows),
        "excluded_screen_records": len(manifest) - len(output_rows),
        "packages_with_candidate_projects": sum(
            bool(row["candidate_project_ids"]) for row in output_rows
        ),
        "manifest_sha256": digest(output_manifest),
        "output": str(args.output),
    }
    (args.output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(summary, indent=2)
    )


if __name__ == "__main__":
    main()
