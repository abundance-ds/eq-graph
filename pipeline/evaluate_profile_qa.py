#!/usr/bin/env python3
"""Validate profile QA and export accepted, held, and inspection sets."""

import csv
import hashlib
import json
import pathlib
import random


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
QA = SCALE / "profile-qa-v1"
SEED = 20260804


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, fields, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    failures = []
    selection = json.loads((QA / "selection.json").read_text())
    prompt_hash = hashlib.sha256((QA / "SYSTEM.md").read_text().encode()).hexdigest()
    if selection["prompt_sha256"] != prompt_hash:
        failures.append("prompt_hash_mismatch")
    results = read_csv(QA / "results.csv")
    if len(results) != len({row["name"] for row in results}):
        failures.append("duplicate_result_name")
    expected = {
        name for batch in selection["batches"] for name in batch["names"]
    }
    if {row["name"] for row in results} != expected:
        failures.append("results_do_not_equal_selection")
    for row in results:
        if row["decision"] not in {"accept", "hold"}:
            failures.append(f"invalid_decision:{row['name']}")
        if not row["reason"].strip() or len(row["reason"]) > 400:
            failures.append(f"invalid_reason:{row['name']}")

    readiness = {
        row["name"]: row
        for row in read_csv(SCALE / "profile-scale-readiness.csv")
    }
    fields = [
        "name", "openalex_id", "decision", "reason", "chosen_name", "orcid",
        "affiliation", "member_affiliation", "total_works", "project_ids",
    ]
    enriched = []
    for row in results:
        source = readiness[row["name"]]
        enriched.append({
            **row,
            "chosen_name": source["chosen_name"],
            "orcid": source["orcid"],
            "affiliation": source["affiliation"],
            "member_affiliation": source["member_affiliation"],
            "total_works": source["total_works"],
            "project_ids": source["project_ids"],
        })
    accepted = [row for row in enriched if row["decision"] == "accept"]
    held = [row for row in enriched if row["decision"] == "hold"]
    write_csv(QA / "accepted.csv", fields, accepted)
    write_csv(QA / "held.csv", fields, held)

    decision_by_name = {row["name"]: row for row in enriched}
    final_review = []
    for name, source in readiness.items():
        scopes = []
        qa_row = decision_by_name.get(name)
        if source["scale_status"] == "needs_review":
            scopes.append("primary_original")
        if qa_row and qa_row["decision"] == "hold":
            scopes.append("primary_binary_qa")
        if source["additional_profile_ids_held"]:
            scopes.append("additional_profile_ids")
        if scopes:
            final_review.append({
                "review_scope": ";".join(scopes),
                "name": name,
                "chosen_id": source["chosen_id"],
                "chosen_name": source["chosen_name"],
                "orcid": source["orcid"],
                "affiliation": source["affiliation"],
                "member_affiliation": source["member_affiliation"],
                "qa_decision": qa_row["decision"] if qa_row else "not_assessed",
                "qa_reason": qa_row["reason"] if qa_row else "",
                "additional_profile_ids_held": source["additional_profile_ids_held"],
                "alternatives": source["alternatives"],
                "project_ids": source["project_ids"],
            })
    review_fields = [
        "review_scope", "name", "chosen_id", "chosen_name", "orcid", "affiliation",
        "member_affiliation", "qa_decision", "qa_reason",
        "additional_profile_ids_held", "alternatives", "project_ids",
    ]
    write_csv(SCALE / "profile-review-queue-final.csv", review_fields, final_review)

    largest = sorted(
        accepted, key=lambda row: -int(row["total_works"] or 0)
    )[:25]
    rng = random.Random(SEED)
    random_sample = rng.sample(accepted, min(20, len(accepted)))
    scope = {}
    for row in held:
        scope.setdefault(row["name"], []).append("all_held")
    for row in largest:
        scope.setdefault(row["name"], []).append("largest_accepted")
    for row in random_sample:
        scope.setdefault(row["name"], []).append("random_accepted")
    by_name = {row["name"]: row for row in enriched}
    inspection = [{
        "inspection_scope": ";".join(scope[name]),
        **{field: by_name[name][field] for field in fields},
    } for name in sorted(scope, key=str.casefold)]
    write_csv(QA / "inspection-set.csv", ["inspection_scope", *fields], inspection)

    summary = {
        "ok": not failures,
        "prompt_sha256": prompt_hash,
        "profiles_assessed": len(results),
        "accepted": len(accepted),
        "held": len(held),
        "inspection_set": {
            "all_held": len(held),
            "largest_accepted": len(largest),
            "random_accepted": len(random_sample),
            "unique_people": len(inspection),
            "seed": SEED,
            "status": "Inspected by the project operator; not independently validated.",
        },
        "people_in_final_review_queue": len(final_review),
        "rule": "Only accept enters the author discovery route. Hold requires review.",
        "failures": failures,
    }
    (QA / "evaluation.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
