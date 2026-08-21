#!/usr/bin/env python3
"""Prepare one source-review and correction prompt per extraction record."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from validate import resolve_record_path, validate_record


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--fallback-run", type=Path, action="append", default=[])
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ids", help="comma-separated record IDs; default is all")
    args = parser.parse_args()

    run = args.run.resolve()
    fallback_runs = [path.resolve() for path in args.fallback_run]
    prepared = args.prepared.resolve()
    output = args.output.resolve()
    inputs = output / "inputs"
    inputs.mkdir(parents=True, exist_ok=True)

    rows = read_tsv(prepared / "MANIFEST.tsv")
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        rows = [row for row in rows if row["record_id"] in wanted]
        found = {row["record_id"] for row in rows}
        if found != wanted:
            raise ValueError(f"unknown record IDs: {sorted(wanted - found)}")

    task_path = HERE / "REVIEW_AND_CORRECT_TASK.md"
    ontology_path = HERE.parent / "ONTOLOGY.md"
    vocabulary_path = HERE.parent / "VOCABULARY.tsv"
    task = task_path.read_text(encoding="utf-8").rstrip()
    ontology = ontology_path.read_text(encoding="utf-8").rstrip()
    vocabulary = vocabulary_path.read_text(encoding="utf-8").rstrip()
    output_rows: list[dict[str, str]] = []

    for row in rows:
        resolved = resolve_record_path(row["record_id"], run, fallback_runs)
        if resolved is None:
            raise ValueError(f"missing draft record: {row['record_id']}")
        record_path, source_run = resolved
        record = json.loads(record_path.read_text(encoding="utf-8"))
        errors, warnings = validate_record(
            record,
            row["record_id"],
            require_null_registry=True,
        )
        article_path = REPO / row["article_path"]
        if digest(article_path) != row["article_sha256"]:
            raise ValueError(f"article hash mismatch: {row['record_id']}")
        metadata = json.loads((REPO / row["metadata_path"]).read_text(encoding="utf-8"))
        safe_metadata = {
            key: metadata[key]
            for key in (
                "publication",
                "dates",
                "authors",
                "affiliations",
                "funding",
                "keywords",
                "categories",
                "correspondence",
            )
        }
        safe_metadata["publication"] = {
            key: value
            for key, value in safe_metadata["publication"].items()
            if key != "source_path"
        }
        prompt = "\n\n".join(
            (
                task,
                "# Ontology reference\n\n" + ontology,
                "# Controlled vocabulary\n\n```tsv\n" + vocabulary + "\n```",
                "# Paper\n\n"
                f"- Record ID: `{row['record_id']}`\n"
                f"- DOI: `{row['paper_id']}`\n"
                f"- Article SHA-256: `{row['article_sha256']}`",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(safe_metadata, ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + article_path.read_text(encoding="utf-8").rstrip(),
                "## Draft extraction record\n\n```json\n"
                + json.dumps(record, ensure_ascii=False, indent=2)
                + "\n```",
                "## Deterministic validation of the draft\n\n```json\n"
                + json.dumps(
                    {"errors": errors, "warning_count": len(warnings)},
                    ensure_ascii=False,
                    indent=2,
                )
                + "\n```",
            )
        ) + "\n"
        input_path = inputs / f"{row['record_id']}.md"
        input_path.write_text(prompt, encoding="utf-8")
        output_rows.append(
            {
                **row,
                "input_path": str(input_path.relative_to(REPO)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "draft_record": str(record_path.relative_to(REPO)),
                "draft_sha256": digest(record_path),
                "draft_source_run": str(source_run.relative_to(REPO)),
                "review_task_sha256": digest(task_path),
            }
        )

    manifest_path = output / "MANIFEST.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(output_rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"records={len(output_rows)}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")


if __name__ == "__main__":
    main()
