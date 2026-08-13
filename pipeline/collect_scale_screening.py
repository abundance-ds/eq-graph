#!/usr/bin/env python3
"""Collect and validate cumulative scale screening decisions."""

import csv
import json
import pathlib
import re
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCREEN = ROOT / "scale" / "protocol-2.0" / "screening-v1"
CODE = re.compile(r"^\[(R1|R2|RU|E1|E2|E3|E4|E5)\]")
RETAIN = {"R1", "R2", "RU"}
EXCLUDE = {"E1", "E2", "E3", "E4", "E5"}


def main():
    selection = json.loads((SCREEN / "selection.json").read_text())
    metadata = {}
    rows = []
    complete_batches = []
    failures = []
    selected_ids = []
    for batch in selection["batches"]:
        batch_id = batch["batch_id"]
        folder = SCREEN / batch_id
        manifest = json.loads((folder / "batch.json").read_text())
        expected = {row["record_id"] for row in manifest["records"]}
        selected_ids.extend(batch["record_ids"])
        if expected != set(batch["record_ids"]):
            failures.append(f"manifest_selection_mismatch:{batch_id}")
        if manifest.get("prompt_sha256") != selection["prompt_sha256"]:
            failures.append(f"batch_prompt_hash_mismatch:{batch_id}")
        metadata.update({row["record_id"]: row for row in manifest["records"]})
        path = folder / "decisions.jsonl"
        if not path.exists():
            continue
        decisions = [json.loads(line) for line in path.open() if line.strip()]
        received = {row["record_id"] for row in decisions}
        if len(decisions) != len(received):
            failures.append(f"duplicate_submission:{batch_id}")
        if received - expected:
            failures.append(f"unknown_submission:{batch_id}")
        if received == expected and len(decisions) == len(expected):
            complete_batches.append(batch_id)
        for decision in decisions:
            match = CODE.match(decision["reason"])
            code = match.group(1) if match else ""
            if decision["outcome"] not in {"retain", "exclude"}:
                failures.append(f"invalid_outcome:{decision['record_id']}")
            if not code:
                failures.append(f"invalid_code:{decision['record_id']}")
            if decision["outcome"] == "retain" and code not in RETAIN:
                failures.append(f"retain_code_mismatch:{decision['record_id']}")
            if decision["outcome"] == "exclude" and code not in EXCLUDE:
                failures.append(f"exclude_code_mismatch:{decision['record_id']}")
            rows.append({
                "batch_id": batch_id,
                **metadata[decision["record_id"]],
                **decision,
                "code": code,
            })

    if len(selected_ids) != selection["records"]:
        failures.append("selection_record_count_mismatch")
    if len(selected_ids) != len(set(selected_ids)):
        failures.append("duplicate_selection_record")
    submitted_ids = [row["record_id"] for row in rows]
    if len(submitted_ids) != len(set(submitted_ids)):
        failures.append("duplicate_cross_batch_submission")

    rows.sort(key=lambda row: (row["batch_id"], row["record_id"]))
    fields = [
        "batch_id", "record_id", "outcome", "code", "reason",
        "year", "linked_people", "title",
    ]
    with (SCREEN / "results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["linked_people"] = "; ".join(output["linked_people"])
            writer.writerow({field: output[field] for field in fields})
    for outcome, filename in [("retain", "retained.csv"), ("exclude", "excluded.csv")]:
        with (SCREEN / filename).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for row in rows:
                if row["outcome"] != outcome:
                    continue
                output = dict(row)
                output["linked_people"] = "; ".join(output["linked_people"])
                writer.writerow({field: output[field] for field in fields})

    code_counts = Counter(row["code"] for row in rows)
    result = {
        "ok": not failures,
        "prompt_sha256": selection["prompt_sha256"],
        "expected_batches": len(selection["batches"]),
        "complete_batches": len(complete_batches),
        "remaining_batches": len(selection["batches"]) - len(complete_batches),
        "expected_records": selection["records"],
        "submitted_records": len(rows),
        "retained": sum(row["outcome"] == "retain" for row in rows),
        "excluded": sum(row["outcome"] == "exclude" for row in rows),
        "code_counts": dict(sorted(code_counts.items())),
        "submission_complete": len(rows) == selection["records"],
        "failures": failures,
    }
    (SCREEN / "progress.json").write_text(json.dumps(result, indent=2) + "\n")
    (SCREEN / "results-summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
