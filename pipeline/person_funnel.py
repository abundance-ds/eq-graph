#!/usr/bin/env python3
"""Create the per-person paper funnel for the Protocol 2.0 pilot."""

import csv
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
OUT = PILOT / "person-funnel.csv"
CHECK = PILOT / "person-funnel-validation.json"
sys.path.insert(0, str(ROOT / "pipeline"))
import pilot_2_0 as pilot  # noqa: E402


FIELDS = [
    "person", "names_linked", "projects_as_pi",
    "orcid_listed_works_n", "openalex_profile_works_n", "pubmed_v2_topic_hits_n",
    "google_scholar_first_page_n", "google_scholar_count_status",
    "profile_statuses",
    "source_records_total_n", "source_records_from_rejected_profiles_n",
    "source_records_accepted_n", "dedup_n", "excluded_document_junk_n",
    "excluded_non_journal_output_n", "publication_type_uncertain_n",
    "journal_article_before_abstract_gate_n", "abstract_from_source_union_n",
    "abstract_enriched_n", "abstract_unavailable_excluded_n",
    "for_title_abstract_screen_n", "ai_screened_n", "ai_excluded_n",
    "for_full_text_n", "status",
]


def main():
    _, authors = pilot.sample_authors()
    people = {r["name"]: r for r in csv.DictReader(open(ROOT / "artefacts" / "01_people.csv"))}
    profile = pilot.profile_statuses()
    works = json.load(open(PILOT / "derived" / "works.json"))

    rows = []
    for author in sorted(authors, key=lambda x: x["name"]):
        name = author["name"]
        sources = pilot.source_records(author)
        counts = {source: len(records) for source, records in sources.items()}
        rejected = sum(counts[source] for source in sources
                       if profile.get((name, source), {}).get("status") == "reject")
        person_works = [x for x in works if name in x["authors"]]
        article_records = [
            x for x in person_works
            if x.get("eligibility_status") in {
                "candidate_full_journal_article", "exclude_abstract_unavailable",
            }
        ]
        rows.append({
            "person": name,
            "names_linked": people[name]["raw_names"],
            "projects_as_pi": people[name]["project_ids"],
            "orcid_listed_works_n": counts["orcid"],
            "openalex_profile_works_n": counts["openalex"],
            "pubmed_v2_topic_hits_n": counts["pubmed"],
            "google_scholar_first_page_n": counts["scholar"],
            "google_scholar_count_status": (
                "AT_LEAST_100_FIRST_PAGE_ONLY" if counts["scholar"] == 100
                else "NO_VERIFIED_PROFILE" if not author["scholar_id"]
                else "FIRST_PAGE_COUNT"
            ),
            "profile_statuses": ";".join(
                f"{source}={profile.get((name, source), {}).get('status', 'not_available')}"
                for source in ["orcid", "openalex", "pubmed", "scholar"]
            ),
            "source_records_total_n": sum(counts.values()),
            "source_records_from_rejected_profiles_n": rejected,
            "source_records_accepted_n": sum(counts.values()) - rejected,
            "dedup_n": len(person_works),
            "excluded_document_junk_n": sum(
                x.get("eligibility_status") == "exclude_document" for x in person_works
            ),
            "excluded_non_journal_output_n": sum(
                x.get("eligibility_status") == "exclude_non_journal" for x in person_works
            ),
            "publication_type_uncertain_n": sum(
                x.get("eligibility_status") == "uncertain" for x in person_works
            ),
            "journal_article_before_abstract_gate_n": len(article_records),
            "abstract_from_source_union_n": sum(
                x.get("abstract_status") == "available" and x.get("abstract_source") == "source_union"
                for x in article_records
            ),
            "abstract_enriched_n": sum(
                x.get("abstract_status") == "available" and x.get("abstract_source") in {
                    "europe_pmc", "crossref", "openalex",
                } for x in article_records
            ),
            "abstract_unavailable_excluded_n": sum(
                x.get("eligibility_status") == "exclude_abstract_unavailable" for x in article_records
            ),
            "for_title_abstract_screen_n": sum(bool(x.get("screening_ready")) for x in article_records),
            "ai_screened_n": 0,
            "ai_excluded_n": "",
            "for_full_text_n": "",
            "status": "READY_FOR_TITLE_ABSTRACT_SCREEN",
        })

    with open(OUT, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    source_total = sum(x["source_records_total_n"] for x in rows)
    accepted_total = sum(x["source_records_accepted_n"] for x in rows)
    validation = {
        "ok": len(rows) == 10 and accepted_total <= source_total and all(
            int(x["dedup_n"]) == sum(int(x[field]) for field in [
                "excluded_document_junk_n", "excluded_non_journal_output_n",
                "publication_type_uncertain_n", "journal_article_before_abstract_gate_n",
            ]) for x in rows
        ),
        "pubmed_query_version": pilot.PUBMED_QUERY_VERSION,
        "persons": len(rows),
        "raw_source_records": source_total,
        "accepted_source_records": accepted_total,
        "unique_deduplicated_papers": len(works),
        "unique_screening_ready_papers": sum(bool(x.get("screening_ready")) for x in works),
        "abstract_rule": "A title/abstract screening record must be an eligible article with a real abstract.",
        "note": "Per-person dedup counts overlap when a paper belongs to multiple sampled people.",
    }
    CHECK.write_text(json.dumps(validation, indent=2) + "\n")
    print(OUT)
    print(json.dumps(validation, indent=2))
    raise SystemExit(0 if validation["ok"] else 1)


if __name__ == "__main__":
    main()
