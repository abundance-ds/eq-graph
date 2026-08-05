#!/usr/bin/env python3
"""Validate PubMed v2 retrieval and the rebuilt 10-person funnel."""

import csv
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
OUT = PILOT / "PUBMED_V2_VALIDATION.json"


def main():
    manifest = json.loads((PILOT / "derived" / "pubmed-v2-queries.json").read_text())
    authors = manifest["authors"]
    decisions = json.loads(
        (PILOT / "ai" / "outputs" / "pubmed-v2-profile-verification.json").read_text()
    )["decisions"]
    with (PILOT / "person-funnel.csv").open(newline="") as handle:
        funnel = list(csv.DictReader(handle))
    aggregate = json.loads((PILOT / "derived" / "aggregate_counts.json").read_text())

    required_columns = {
        "orcid_listed_works_n",
        "openalex_profile_works_n",
        "pubmed_v2_topic_hits_n",
        "google_scholar_first_page_n",
        "google_scholar_count_status",
        "journal_article_before_abstract_gate_n",
        "abstract_unavailable_excluded_n",
        "for_title_abstract_screen_n",
    }
    checks = {
        "ten_people": len(authors) == len(decisions) == len(funnel) == 10,
        "all_pubmed_records_parsed": all(x["esearch_n"] == x["parsed_n"] for x in authors),
        "all_raw_files_saved": all(
            (ROOT / x["raw_search"]).exists() and (ROOT / x["raw_records"]).exists()
            for x in authors
        ),
        "all_derived_files_saved": all((ROOT / x["derived"]).exists() for x in authors),
        "unquoted_author_terms": all('\"[Author]' not in x["query"] for x in authors),
        "orcid_identifier_terms": all("[Author Identifier]" in x["query"] for x in authors),
        "funnel_columns_present": required_columns.issubset(funnel[0]),
        "scholar_caps_labelled": all(
            row["google_scholar_first_page_n"] != "100"
            or row["google_scholar_count_status"] == "AT_LEAST_100_FIRST_PAGE_ONLY"
            for row in funnel
        ),
        "eligibility_partition_complete": all(
            int(row["dedup_n"]) == sum(int(row[field]) for field in [
                "excluded_document_junk_n",
                "excluded_non_journal_output_n",
                "publication_type_uncertain_n",
                "journal_article_before_abstract_gate_n",
            ])
            for row in funnel
        ),
        "abstract_partition_complete": all(
            int(row["journal_article_before_abstract_gate_n"])
            == int(row["abstract_unavailable_excluded_n"])
            + int(row["for_title_abstract_screen_n"])
            for row in funnel
        ),
    }
    result = {
        "ok": all(checks.values()),
        "checks": checks,
        "pubmed_v1_records": 262,
        "pubmed_v2_records": sum(x["parsed_n"] for x in authors),
        "known_v1_misses_audited": 69,
        "known_v1_misses_recovered_v2": 65,
        "profile_decisions": {
            status: sum(x["status"] == status for x in decisions)
            for status in ["accept", "caution", "reject"]
        },
        "aggregate_after_profile_check": aggregate,
        "scope": "PubMed v2 retrieval, profile decisions, and pre-screen funnel",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
