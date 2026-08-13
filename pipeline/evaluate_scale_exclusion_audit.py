#!/usr/bin/env python3
"""Compare the blinded exclusion audit with current production decisions."""

import argparse
import csv
import json
import pathlib
import re
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
SCREEN = SCALE / "screening-v1"
CODE = re.compile(r"^\[(R1|R2|RU|E1|E2|E3|E4|E5)\]")
RETAIN = {"R1", "R2", "RU"}
EXCLUDE = {"E1", "E2", "E3", "E4", "E5"}


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    audit = SCALE / f"exclusion-audit-{args.version}"
    selection = json.loads((audit / "selection.json").read_text())
    production = {row["record_id"]: row for row in read_csv(SCREEN / "results.csv")}
    rows = []
    failures = []
    expected = []

    for batch in selection["batches"]:
        batch_id = batch["batch_id"]
        expected.extend(batch["record_ids"])
        path = audit / batch_id / "decisions.jsonl"
        if not path.exists():
            failures.append(f"missing_decisions:{batch_id}")
            continue
        decisions = [json.loads(line) for line in path.open() if line.strip()]
        if len(decisions) != len(batch["record_ids"]):
            failures.append(f"incomplete_batch:{batch_id}")
        if {row["record_id"] for row in decisions} != set(batch["record_ids"]):
            failures.append(f"batch_id_mismatch:{batch_id}")
        for decision in decisions:
            record_id = decision["record_id"]
            match = CODE.match(decision["reason"])
            audit_code = match.group(1) if match else ""
            if not audit_code:
                failures.append(f"invalid_audit_code:{record_id}")
            if decision["outcome"] == "retain" and audit_code not in RETAIN:
                failures.append(f"audit_retain_code_mismatch:{record_id}")
            if decision["outcome"] == "exclude" and audit_code not in EXCLUDE:
                failures.append(f"audit_exclude_code_mismatch:{record_id}")
            original = production.get(record_id)
            if not original:
                failures.append(f"missing_production_record:{record_id}")
                continue
            if original["outcome"] != "exclude":
                failures.append(f"sample_contains_non_exclusion:{record_id}")
            rows.append({
                "record_id": record_id,
                "title": original["title"],
                "production_batch": original["batch_id"],
                "production_outcome": original["outcome"],
                "production_code": original["code"],
                "production_reason": original["reason"],
                "audit_batch": batch_id,
                "audit_outcome": decision["outcome"],
                "audit_code": audit_code,
                "audit_reason": decision["reason"],
                "outcome_agreement": str(decision["outcome"] == original["outcome"]).lower(),
            })

    if len(expected) != len(set(expected)):
        failures.append("duplicate_selection_record")
    if {row["record_id"] for row in rows} != set(expected):
        failures.append("audit_does_not_cover_selection")

    fields = [
        "record_id", "title", "production_batch", "production_outcome",
        "production_code", "production_reason", "audit_batch", "audit_outcome",
        "audit_code", "audit_reason", "outcome_agreement",
    ]
    with (audit / "comparison.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    audit_retains = [row for row in rows if row["audit_outcome"] == "retain"]
    (audit / "disagreements.json").write_text(
        json.dumps(audit_retains, ensure_ascii=False, indent=2) + "\n"
    )
    adjudication_path = audit / "primary-agent-adjudication.csv"
    adjudications = read_csv(adjudication_path) if adjudication_path.exists() else []
    adjudication_by_id = {row["record_id"]: row for row in adjudications}
    if len(adjudication_by_id) != len(adjudications):
        failures.append("duplicate_adjudication_record")
    if adjudication_path.exists() and set(adjudication_by_id) != {
        row["record_id"] for row in audit_retains
    }:
        failures.append("adjudication_does_not_cover_disagreements")
    for record_id, row in adjudication_by_id.items():
        if row["audit_outcome"] != "retain":
            failures.append(f"invalid_adjudication_audit_outcome:{record_id}")
        if row["final_outcome"] not in {"retain", "exclude"}:
            failures.append(f"invalid_adjudication_final_outcome:{record_id}")
        if row["final_outcome"] == "retain" and row["final_code"] not in RETAIN:
            failures.append(f"adjudication_retain_code_mismatch:{record_id}")
        if row["final_outcome"] == "exclude" and row["final_code"] not in EXCLUDE:
            failures.append(f"adjudication_exclude_code_mismatch:{record_id}")
        if not row["rationale"].strip():
            failures.append(f"missing_adjudication_rationale:{record_id}")
    confirmed_false_exclusions = sorted(
        record_id for record_id, row in adjudication_by_id.items()
        if row["final_outcome"] == "retain"
    )
    result = {
        "ok": not failures,
        "reviewer": "Separate AI subagent; production outcomes, codes, and reasons withheld",
        "sample_method": selection["method"],
        "seed": selection["seed"],
        "sampling_frame_exclusions": selection["sampling_frame_exclusions"],
        "sample_size": len(rows),
        "outcome_agreements": sum(row["outcome_agreement"] == "true" for row in rows),
        "audit_exclusions": len(rows) - len(audit_retains),
        "audit_retains_for_adjudication": len(audit_retains),
        "audit_retain_record_ids": [row["record_id"] for row in audit_retains],
        "adjudications_complete": bool(adjudication_path.exists()) and not failures,
        "confirmed_true_negatives": (
            len(rows) - len(confirmed_false_exclusions)
            if adjudication_path.exists() else None
        ),
        "confirmed_false_exclusions": confirmed_false_exclusions,
        "continue_frozen_prompt": (
            bool(adjudication_path.exists()) and not failures
            and not confirmed_false_exclusions
        ),
        "production_code_counts": dict(sorted(Counter(row["production_code"] for row in rows).items())),
        "audit_code_counts": dict(sorted(Counter(row["audit_code"] for row in rows).items())),
        "interpretation_rule": (
            "An audit retain is a disagreement for operator adjudication, not an automatic "
            "false exclusion. Continue the frozen screen unchanged only if adjudication "
            "finds no substantive false exclusion or systematic scope problem."
        ),
        "limitations": [
            "This is an AI consistency and error-finding check, not independent human validation.",
            "The primary-agent adjudication is also AI review, not human adjudication.",
            "A random sample can miss rare or systematic false exclusions.",
        ],
        "failures": failures,
    }
    (audit / "evaluation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
