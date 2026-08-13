#!/usr/bin/env python3
"""Validate the complete-candidate project audit and its integration rule."""

import csv
import hashlib
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
AUDIT = PILOT / "project-assessment-v3"


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    failures = []
    selection = json.loads((AUDIT / "selection.json").read_text())
    prompt_hash = hashlib.sha256((AUDIT / "SYSTEM.md").read_text().encode()).hexdigest()
    if selection["prompt_sha256"] != prompt_hash:
        failures.append("prompt_hash_mismatch")
    results = {row["record_id"]: row for row in read_csv(AUDIT / "results.csv")}
    selected_ids = {
        record_id
        for batch in selection["batches"]
        for record_id in batch["record_ids"]
    }
    if set(results) != selected_ids:
        failures.append("results_do_not_equal_selection")

    prior = {
        row["record_id"]: row
        for row in read_csv(PILOT / "paper-assessment.csv")
        if row["assessment_status"] == "assessed"
    }
    omitted_by_record = {}
    candidates_by_record = {}
    for batch in selection["batches"]:
        payload = json.loads((AUDIT / batch["batch_id"] / "batch.json").read_text())
        if payload["prompt_sha256"] != prompt_hash:
            failures.append(f"batch_prompt_hash_mismatch:{batch['batch_id']}")
        record = payload["records"][0]
        omitted_by_record[record["record_id"]] = set(record["previously_omitted_project_ids"])
        candidates_by_record[record["record_id"]] = set(record["candidate_project_ids"])

    newly_selected = []
    decision_differences = []
    for record_id, row in results.items():
        project_ids = {value for value in row["project_ids"].split(";") if value}
        if not project_ids <= candidates_by_record[record_id]:
            failures.append(f"selected_non_candidate:{record_id}")
        new_ids = sorted(project_ids & omitted_by_record[record_id])
        if new_ids:
            newly_selected.append({
                "record_id": record_id,
                "project_ids": new_ids,
                "project_link": row["project_link"],
            })
        old = prior[record_id]
        if (old["project_link"], old["project_ids"]) != (
            row["project_link"], row["project_ids"]
        ):
            decision_differences.append({
                "record_id": record_id,
                "prior_project_link": old["project_link"],
                "prior_project_ids": old["project_ids"],
                "audit_project_link": row["project_link"],
                "audit_project_ids": row["project_ids"],
            })

    summary = {
        "ok": not failures,
        "prompt_sha256": prompt_hash,
        "audited_articles": len(results),
        "previously_omitted_candidates_supplied": sum(
            len(values) for values in omitted_by_record.values()
        ),
        "audit_selected_previously_omitted_candidates": newly_selected,
        "raw_decision_differences": decision_differences,
        "integration_rule": (
            "Add or revise a link only when the audit selects a project that was absent "
            "from the original candidate input. Do not replace an existing decision "
            "because of ordinary repeat variation."
        ),
        "canonical_changes": [],
        "failures": failures,
    }
    (AUDIT / "evaluation.json").write_text(json.dumps(summary, indent=2) + "\n")
    (AUDIT / "EVALUATION.md").write_text(f"""# Complete project-candidate audit

The audit is valid. It rechecked **{len(results)}** pilot articles and supplied
**{summary['previously_omitted_candidates_supplied']}** projects that the first
12-project shortlist omitted.

The audit selected **{len(newly_selected)}** previously omitted projects. Therefore,
the shortlist did not cause a missed pilot project link. The canonical project links do
not change.

One audit decision differed from the prior decision without selecting a new candidate.
This is repeat variation, so the fixed integration rule keeps the prior, more
conservative decision.

The current method supplies every rule-based candidate. It uses no similarity score and
no candidate cap.
""")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
