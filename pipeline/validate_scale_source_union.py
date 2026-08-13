#!/usr/bin/env python3
"""Validate the Protocol 2.0 scale source union."""

import json
import pathlib
from collections import Counter

import pilot_2_0 as pilot


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
UNION = SCALE / "source-union.jsonl"
SUMMARY = SCALE / "source-union-summary.json"


def main():
    summary = json.loads(SUMMARY.read_text())
    records = [json.loads(line) for line in UNION.open()]
    failures = list(summary.get("failures") or [])

    record_ids = Counter(row["record_id"] for row in records)
    dois = Counter(row["doi"] for row in records if row["doi"])
    pmids = Counter(row["pmid"] for row in records if row["pmid"])
    title_years = Counter()
    for row in records:
        title = pilot.norm_title(row["title"])
        if title and row["year"]:
            title_years[f"{title}:{row['year']}"] += 1
    unexpected_title_duplicates = sorted(
        key for key, count in title_years.items()
        if count > 1
    )

    if len(records) != summary["deduplicated_records"]:
        failures.append("summary_record_count_differs")
    if any(count > 1 for count in record_ids.values()):
        failures.append("duplicate_record_id")
    if any(count > 1 for count in dois.values()):
        failures.append("duplicate_doi")
    if any(count > 1 for count in pmids.values()):
        failures.append("duplicate_pmid")
    if unexpected_title_duplicates:
        failures.append("unexpected_duplicate_title_year")
    if any(row["abstract_status"] == "available" and not row["abstract"].strip() for row in records):
        failures.append("available_abstract_is_empty")
    if any(row["abstract_status"] == "unavailable" and row["abstract"].strip() for row in records):
        failures.append("unavailable_abstract_has_text")
    if any(not row["discovery_routes"] for row in records):
        failures.append("record_without_discovery_route")

    result = {
        "ok": not failures,
        "records": len(records),
        "candidate_articles_and_reviews": sum(
            row["document_gate"] == "candidate_article" for row in records
        ),
        "duplicate_record_ids": sum(count > 1 for count in record_ids.values()),
        "duplicate_dois": sum(count > 1 for count in dois.values()),
        "duplicate_pmids": sum(count > 1 for count in pmids.values()),
        "title_year_identifier_variant_groups_merged": summary[
            "title_year_identifier_variant_groups_merged"
        ],
        "unexpected_duplicate_title_years": unexpected_title_duplicates,
        "failures": failures,
    }
    (SCALE / "source-union-validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
