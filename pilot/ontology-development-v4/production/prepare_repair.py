#!/usr/bin/env python3
"""Prepare full-record repair prompts from reviewed feedback."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--feedback", type=Path, required=True)
    parser.add_argument("--base-run", type=Path, required=True)
    parser.add_argument(
        "--fallback-run",
        type=Path,
        action="append",
        default=[],
        help="use a record from this run when the base run has no record",
    )
    parser.add_argument("--prepared", type=Path, default=HERE / "prepared")
    parser.add_argument("--output", type=Path, default=HERE / "prepared-repair")
    args = parser.parse_args()
    base_run = args.base_run.resolve()
    fallback_runs = [path.resolve() for path in args.fallback_run]
    prepared = args.prepared.resolve()
    output = args.output.resolve()

    feedback_rows = read_tsv(args.feedback)
    feedback = {row["record_id"]: row["feedback"] for row in feedback_rows}
    if len(feedback) != len(feedback_rows):
        raise ValueError("repair feedback has duplicate record IDs")
    source_rows = {
        row["record_id"]: row for row in read_tsv(prepared / "MANIFEST.tsv")
    }
    unknown = sorted(set(feedback) - set(source_rows))
    if unknown:
        raise ValueError(f"unknown repair record IDs: {unknown}")

    inputs_dir = output / "inputs"
    inputs_dir.mkdir(parents=True, exist_ok=True)
    output_rows: list[dict[str, str]] = []
    for record_id, note in feedback.items():
        row = source_rows[record_id]
        base_input = REPO / row["input_path"]
        prior_record = next(
            (
                path
                for run in (base_run, *fallback_runs)
                if (path := run / "records" / f"{record_id}.json").is_file()
            ),
            None,
        )
        if not base_input.is_file() or prior_record is None:
            raise ValueError(f"missing repair input for {record_id}")
        prompt = (
            base_input.read_text(encoding="utf-8").rstrip()
            + "\n\n# Repair task\n\n"
            + "Return a complete corrected record, not a patch. The source article is "
            + "authoritative. Preserve supported details from the prior record. Correct "
            + "the reviewed defects below and follow the current ontology and schema.\n\n"
            + note.strip()
            + "\n\n## Prior record\n\n```json\n"
            + prior_record.read_text(encoding="utf-8").rstrip()
            + "\n```\n"
        )
        input_path = inputs_dir / f"{record_id}.md"
        input_path.write_text(prompt, encoding="utf-8")
        output_rows.append(
            {
                **row,
                "input_path": str(input_path.relative_to(REPO)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                "repair_base_record": str(prior_record.relative_to(REPO)),
                "repair_base_sha256": digest(prior_record),
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
