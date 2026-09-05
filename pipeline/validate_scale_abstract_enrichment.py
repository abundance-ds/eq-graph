#!/usr/bin/env python3
"""Validate exact-identifier abstract enrichment for the scale corpus."""

import csv
import json
import pathlib
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
CORPUS = SCALE / "article-corpus.jsonl"
SUMMARY = SCALE / "abstract-enrichment-summary.json"
UNAVAILABLE = SCALE / "abstract-unavailable-or-short.csv"


def main():
    summary = json.loads(SUMMARY.read_text())
    records = [json.loads(line) for line in CORPUS.open()]
    unavailable = list(csv.DictReader(UNAVAILABLE.open(newline="")))
    failures = list(summary.get("failures") or [])
    ids = Counter(record["record_id"] for record in records)

    if len(records) != summary["candidate_articles_and_reviews"]:
        failures.append("candidate_count_differs")
    if any(count > 1 for count in ids.values()):
        failures.append("duplicate_record_id")
    if any(record["document_gate"] != "candidate_article" for record in records):
        failures.append("noncandidate_in_article_corpus")
    if any(
        record["abstract_length_gate"] != (len(record["abstract"].strip()) >= 80)
        for record in records
    ):
        failures.append("abstract_length_gate_differs")
    if any(
        record["abstract_source"] == "europe_pmc"
        and record["abstract_match"] not in {"doi", "pmid"}
        for record in records
    ):
        failures.append("enriched_record_without_exact_match")
    if len(unavailable) != sum(not record["abstract_length_gate"] for record in records):
        failures.append("unavailable_queue_count_differs")

    result = {
        "ok": not failures,
        "records": len(records),
        "abstracts_passing_length_gate": sum(
            record["abstract_length_gate"] for record in records
        ),
        "abstracts_unavailable_or_short": len(unavailable),
        "europe_pmc_exact_identifier_enrichments": sum(
            record["abstract_source"] == "europe_pmc" for record in records
        ),
        "duplicate_record_ids": sum(count > 1 for count in ids.values()),
        "failures": failures,
    }
    (SCALE / "abstract-enrichment-validation.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
