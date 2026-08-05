#!/usr/bin/env python3
"""Validate the hand-off from bibliographic retrieval to AI screening."""

import csv
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
WORKS = PILOT / "derived" / "works.json"
OUT = PILOT / "screening-corpus-validation.json"


def duplicate_values(records, field):
    seen, duplicates = {}, []
    for record in records:
        value = record.get(field, "")
        if not value:
            continue
        if value in seen:
            duplicates.append({field: value, "record_ids": [seen[value], record["record_id"]]})
        else:
            seen[value] = record["record_id"]
    return duplicates


def main():
    works = json.loads(WORKS.read_text())
    ready = [record for record in works if record.get("screening_ready")]
    unavailable = [
        record for record in works
        if record.get("eligibility_status") == "exclude_abstract_unavailable"
    ]
    article_records = [
        record for record in works
        if record.get("eligibility_status") in {
            "candidate_full_journal_article", "exclude_abstract_unavailable",
        }
    ]
    unavailable_csv = list(csv.DictReader(open(PILOT / "abstract-unavailable.csv")))
    failures = []
    failures.extend(
        f"ready_without_abstract:{record['record_id']}"
        for record in ready if len((record.get("abstract") or "").strip()) < 80
    )
    failures.extend(
        f"ready_wrong_status:{record['record_id']}"
        for record in ready
        if record.get("eligibility_status") != "candidate_full_journal_article"
    )
    failures.extend(
        f"candidate_not_ready:{record['record_id']}"
        for record in works
        if record.get("eligibility_status") == "candidate_full_journal_article"
        and not record.get("screening_ready")
    )
    duplicate_identifiers = duplicate_values(works, "doi") + duplicate_values(works, "pmid")
    if duplicate_identifiers:
        failures.append("duplicate_identifiers")
    if len(unavailable_csv) != len(unavailable):
        failures.append("abstract_unavailable_csv_count")
    if len(article_records) != len(ready) + len(unavailable):
        failures.append("abstract_gate_partition")

    result = {
        "ok": not failures,
        "deduplicated_records": len(works),
        "article_records_before_abstract_gate": len(article_records),
        "screening_ready": len(ready),
        "abstract_unavailable_excluded": len(unavailable),
        "duplicate_identifier_groups": len(duplicate_identifiers),
        "failures": failures,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
