#!/usr/bin/env python3
"""Prepare paper-scoped prompts and SQL workspaces for full-text extraction."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from prepare_fulltext_single_agent_pilot import publication_form


ROOT = Path(__file__).resolve().parent.parent
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
PILOT = PRODUCTION / "sql-agent-pilot"
PACKAGES = ROOT / "scale" / "protocol-2.0" / "fulltext-paper-packages-v2" / "packages"
DEFAULT_MANIFEST = ROOT / "scale" / "protocol-2.0" / "fulltext-single-agent-v1" / "prepared" / "MANIFEST.tsv"
VOCABULARY = PRODUCTION.parent / "VOCABULARY.tsv"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, values: list[dict[str, str]]) -> None:
    if not values:
        raise ValueError("no records selected")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(values[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(values)


def replace_once(text: str, marker: str, value: str) -> str:
    if text.count(marker) != 1:
        raise ValueError(f"expected one prompt marker: {marker}")
    return text.replace(marker, value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--ids", help="comma-separated record IDs")
    parser.add_argument(
        "--exclude-records-dir",
        type=Path,
        help="exclude record IDs that already have a saved JSON record",
    )
    args = parser.parse_args()

    output = args.output.resolve()
    inputs = output / "inputs"
    contexts = output / "contexts"
    inputs.mkdir(parents=True, exist_ok=True)
    contexts.mkdir(parents=True, exist_ok=True)

    template = (PILOT / "PROMPT_TEMPLATE.md").read_text(encoding="utf-8")
    template = replace_once(
        template,
        "[INSERT THE COMPLETE SQL WORKSPACE SCHEMA.]",
        (PILOT / "WORKSPACE_SCHEMA.sql").read_text(encoding="utf-8").rstrip(),
    )
    controlled = (
        "The values `UNMAPPED_VALUE`, `UNCERTAIN_MAPPING`, and `NOT_REPORTED` "
        "are also valid for controlled fields when applicable.\n\n```tsv\n"
        + VOCABULARY.read_text(encoding="utf-8").rstrip()
        + "\n```"
    )
    template = replace_once(
        template,
        "[INSERT THE COMPLETE CONTROLLED VOCABULARY.]",
        controlled,
    )

    source_rows = read_tsv(args.manifest.resolve())
    if args.exclude_records_dir:
        completed = {
            path.stem for path in args.exclude_records_dir.resolve().glob("*.json")
        }
        source_rows = [row for row in source_rows if row["record_id"] not in completed]
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        source_rows = [row for row in source_rows if row["record_id"] in wanted]
        found = {row["record_id"] for row in source_rows}
        if found != wanted:
            raise ValueError(f"unknown record IDs: {sorted(wanted - found)}")

    prepared_rows: list[dict[str, str]] = []
    for source_row in source_rows:
        record_id = source_row["record_id"]
        package_value = source_row.get("package_path")
        if not package_value:
            package_path = PACKAGES / f"{record_id}.json"
        else:
            package_path = Path(package_value)
            if not package_path.is_absolute():
                package_path = ROOT / package_path
        if source_row.get("package_sha256") and digest(package_path) != source_row["package_sha256"]:
            raise ValueError(f"package hash mismatch: {record_id}")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        source_path = ROOT / package["full_text"]["path"]
        if digest(source_path) != package["full_text"]["sha256"]:
            raise ValueError(f"source hash mismatch: {record_id}")

        candidates = package["candidate_projects"]
        candidates_text = (
            json.dumps(candidates, ensure_ascii=False, indent=2)
            if candidates
            else "No candidate projects found."
        )
        metadata = {
            "publication": package["publication"],
            "deterministic_metadata": package["deterministic_metadata"],
            "abstract_screen": {
                "decision": package["abstract_screen"].get("decision"),
                "project_ids": package["abstract_screen"].get("project_ids", []),
                "reason": package["abstract_screen"].get("reason"),
            },
        }
        prompt = replace_once(
            template,
            '[INSERT THE CANDIDATE PROJECTS, OR "No candidate projects found."]',
            candidates_text,
        )
        prompt = replace_once(
            prompt,
            "[INSERT THE DETERMINISTICALLY EXTRACTED METADATA.]",
            "```json\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n```",
        )
        prompt = replace_once(
            prompt,
            "[INSERT THE FULL PAPER TEXT.]",
            source_path.read_text(encoding="utf-8").rstrip(),
        )
        input_path = inputs / f"{record_id}.md"
        input_path.write_text(prompt + "\n", encoding="utf-8")

        form = publication_form(package)
        context_path = contexts / f"{record_id}.json"
        context_path.write_text(
            json.dumps(
                {
                    "record_id": record_id,
                    "candidate_project_ids": [row["project_id"] for row in candidates],
                    "candidate_projects": candidates,
                    "publication_form": form,
                    "source_marker": package["full_text"]["path"],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        prepared_rows.append(
            {
                **source_row,
                "input_path": str(input_path.relative_to(ROOT)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "context_path": str(context_path.relative_to(ROOT)),
                "context_sha256": digest(context_path),
                "publication_form": form,
            }
        )

    manifest_path = output / "MANIFEST.tsv"
    write_tsv(manifest_path, prepared_rows)
    print(f"records={len(prepared_rows)}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")


if __name__ == "__main__":
    main()
