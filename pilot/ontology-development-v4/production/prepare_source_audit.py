#!/usr/bin/env python3
"""Prepare compact full-source audit batches for validated extraction records."""

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


def chunks(values: list[dict[str, str]], size: int) -> list[list[dict[str, str]]]:
    return [values[index : index + size] for index in range(0, len(values), size)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--fallback-run", type=Path, action="append", default=[])
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--ids", help="comma-separated record IDs; default is all")
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 5:
        raise ValueError("batch size must be from 1 to 5")

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
    task = (HERE / "SOURCE_AUDIT_TASK.md").read_text(encoding="utf-8").rstrip()
    ontology = (HERE.parent / "ONTOLOGY.md").read_text(encoding="utf-8").rstrip()
    vocabulary = (HERE.parent / "VOCABULARY.tsv").read_text(encoding="utf-8").rstrip()
    task_sha = digest(HERE / "SOURCE_AUDIT_TASK.md")
    output_rows: list[dict[str, str]] = []

    for batch_number, batch_rows in enumerate(chunks(rows, args.batch_size), 1):
        batch_id = f"A{batch_number:03d}"
        sections = [
            task,
            "# Ontology reference\n\n" + ontology,
            "# Controlled vocabulary\n\n```tsv\n" + vocabulary + "\n```",
            f"# Batch\n\nReturn `batch_id` as `{batch_id}` and one audit for each assigned record.",
        ]
        source_runs: list[str] = []
        for row in batch_rows:
            resolved = resolve_record_path(row["record_id"], run, fallback_runs)
            if resolved is None:
                raise ValueError(f"missing record: {row['record_id']}")
            record_path, source_run = resolved
            record = json.loads(record_path.read_text(encoding="utf-8"))
            validation_errors, validation_warnings = validate_record(
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
                if key not in {"source_path"}
            }
            sections.append(
                "\n\n".join(
                    (
                        f"# {row['record_id']} — {row['paper_id']}",
                        "## Deterministic metadata\n\n```json\n"
                        + json.dumps(safe_metadata, ensure_ascii=False, indent=2)
                        + "\n```",
                        "## Full article\n\n" + article_path.read_text(encoding="utf-8").rstrip(),
                        "## Extraction record\n\n```json\n"
                        + json.dumps(record, ensure_ascii=False, indent=2)
                        + "\n```",
                        "## Deterministic validation\n\n```json\n"
                        + json.dumps(
                            {
                                "errors": validation_errors,
                                "warning_count": len(validation_warnings),
                            },
                            ensure_ascii=False,
                            indent=2,
                        )
                        + "\n```",
                    )
                )
            )
            source_runs.append(
                str(source_run.relative_to(REPO))
                if source_run.is_relative_to(REPO)
                else str(source_run)
            )
        input_path = inputs / f"{batch_id}.md"
        input_path.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
        output_rows.append(
            {
                "batch_id": batch_id,
                "record_ids": ",".join(row["record_id"] for row in batch_rows),
                "paper_ids": ",".join(row["paper_id"] for row in batch_rows),
                "source_runs": ",".join(source_runs),
                "input_path": str(input_path.relative_to(REPO)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "task_sha256": task_sha,
            }
        )
    manifest = output / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(output_rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"records={len(rows)}")
    print(f"batches={len(output_rows)}")
    print(f"manifest={manifest}")
    print(f"manifest_sha256={digest(manifest)}")


if __name__ == "__main__":
    main()
