#!/usr/bin/env python3
"""Validate source-audit coverage and collect repair instructions."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from audit_schema import build_audit_schema


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def path_text(error: Any) -> str:
    location = ".".join(str(value) for value in error.absolute_path)
    return f"{location}: {error.message}" if location else error.message


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    args = parser.parse_args()
    manifest = read_tsv(args.prepared.resolve() / "MANIFEST.tsv")
    run = args.run.resolve()
    validator = Draft202012Validator(build_audit_schema())
    results: list[dict[str, Any]] = []
    collected: list[dict[str, str]] = []
    seen_records: set[str] = set()
    for row in manifest:
        batch_id = row["batch_id"]
        expected = [value for value in row["record_ids"].split(",") if value]
        output = run / "records" / f"{batch_id}.json"
        errors: list[str] = []
        if not output.is_file():
            errors.append("missing output")
            value: dict[str, Any] | None = None
        else:
            try:
                value = json.loads(output.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                value = None
                errors.append(f"invalid JSON: {error}")
        if value is not None:
            errors.extend(path_text(error) for error in validator.iter_errors(value))
            if value.get("batch_id") != batch_id:
                errors.append(f"batch_id is {value.get('batch_id')}; expected {batch_id}")
            audits = value.get("audits", [])
            actual = [audit.get("record_id") for audit in audits]
            if len(actual) != len(set(actual)):
                errors.append("duplicate record ID")
            if set(actual) != set(expected):
                errors.append(f"record IDs are {sorted(actual)}; expected {sorted(expected)}")
            for audit in audits:
                record_id = audit.get("record_id")
                if record_id in seen_records:
                    errors.append(f"record appears in more than one batch: {record_id}")
                seen_records.add(record_id)
                verdict = audit.get("verdict")
                repair = audit.get("repair")
                if verdict == "PASS" and repair not in (None, ""):
                    errors.append(f"{record_id}: PASS has repair instructions")
                if verdict in {"MINOR", "MAJOR"} and not repair:
                    errors.append(f"{record_id}: {verdict} lacks repair instructions")
                collected.append(
                    {
                        "batch_id": batch_id,
                        "record_id": str(record_id),
                        "verdict": str(verdict),
                        "source_locations": " | ".join(audit.get("source_locations", [])),
                        "repair": repair or "",
                        "ontology_gap": audit.get("ontology_gap") or "",
                    }
                )
        results.append({"batch_id": batch_id, "errors": errors})
    expected_all = {
        record_id
        for row in manifest
        for record_id in row["record_ids"].split(",")
        if record_id
    }
    if seen_records != expected_all:
        results.append(
            {
                "batch_id": "ALL",
                "errors": [
                    f"coverage differs: missing={sorted(expected_all-seen_records)}, extra={sorted(seen_records-expected_all)}"
                ],
            }
        )
    collected.sort(key=lambda row: row["record_id"])
    summary = {
        "batches": len(manifest),
        "records": len(collected),
        "verdicts": dict(Counter(row["verdict"] for row in collected)),
        "errors": sum(len(row["errors"]) for row in results),
    }
    (run / "VALIDATION.json").write_text(
        json.dumps({"summary": summary, "batches": results}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    columns = ["batch_id", "record_id", "verdict", "source_locations", "repair", "ontology_gap"]
    write_tsv(run / "AUDIT_RESULTS.tsv", collected, columns)
    repairs = [
        {"record_id": row["record_id"], "feedback": row["repair"]}
        for row in collected
        if row["verdict"] in {"MINOR", "MAJOR"}
    ]
    write_tsv(run / "REPAIRS.tsv", repairs, ["record_id", "feedback"])
    print(json.dumps(summary, indent=2))
    if summary["errors"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
