#!/usr/bin/env python3
"""Build the accepted-profile OpenAlex discovery corpus for scale-up."""

import csv
import json
import pathlib
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
PROFILE_WORKS = ROOT / "artefacts" / "03_works"
FUNDER_WORKS = ROOT / "artefacts" / "03_funder_works.json"
EUROQOL_FUNDER = "F4320323856"
ELIGIBLE_TYPES = {"article", "review"}


def suffix(value):
    return (value or "").rsplit("/", 1)[-1]


def normalize_doi(value):
    value = (value or "").strip().casefold()
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value


def abstract_text(inverted_index):
    if not inverted_index:
        return ""
    positions = [
        (position, word)
        for word, word_positions in inverted_index.items()
        for position in word_positions
    ]
    return " ".join(word for _, word in sorted(positions))


def normalized(work):
    authors = []
    for authorship in work.get("authorships") or []:
        author = authorship.get("author") or {}
        if not author.get("id") and not author.get("display_name"):
            continue
        authors.append({
            "openalex_id": suffix(author.get("id")),
            "name": author.get("display_name") or "",
            "orcid": suffix(author.get("orcid")),
        })
    funders = sorted({
        suffix(funder.get("id"))
        for funder in work.get("funders") or []
        if funder.get("id")
    })
    euroqol_awards = sorted({
        (award.get("funder_award_id") or "").strip()
        for award in work.get("awards") or []
        if suffix(award.get("funder_id")) == EUROQOL_FUNDER
        and (award.get("funder_award_id") or "").strip()
    })
    location = work.get("primary_location") or {}
    source = location.get("source") or {}
    abstract = abstract_text(work.get("abstract_inverted_index"))
    return {
        "openalex_id": suffix(work.get("id")),
        "doi": normalize_doi(work.get("doi")),
        "title": work.get("title") or "",
        "year": work.get("publication_year"),
        "publication_date": work.get("publication_date") or "",
        "document_type": work.get("type") or "unknown",
        "venue": source.get("display_name") or "",
        "authors": authors,
        "abstract": abstract,
        "abstract_status": "available" if abstract else "unavailable",
        "cited_by_count": work.get("cited_by_count") or 0,
        "primary_landing_page_url": location.get("landing_page_url") or "",
        "primary_pdf_url": location.get("pdf_url") or "",
        "topics": [topic.get("display_name") or "" for topic in (work.get("topics") or [])[:3]],
        "funders": funders,
        "euroqol_award_ids": euroqol_awards,
        "linked_people": [],
        "discovery_routes": [],
    }


def main():
    failures = []
    qa_path = SCALE / "profile-qa-v1" / "results.csv"
    if not qa_path.exists():
        raise SystemExit("profile QA results not found")
    accepted_names = {
        row["name"]
        for row in csv.DictReader(qa_path.open(newline=""))
        if row["decision"] == "accept"
    }
    ready_by_author = {}
    held_split_assignments = []
    with (SCALE / "profile-scale-readiness.csv").open(newline="") as handle:
        for row in csv.DictReader(handle):
            if row["scale_status"] == "ready" and row["name"] in accepted_names:
                ready_by_author.setdefault(row["chosen_id"], []).append(row["name"])
                held_split_assignments.extend(
                    value for value in row["additional_profile_ids_held"].split(";") if value
                )

    records = {}
    author_source_links = 0
    for author_id, people in sorted(ready_by_author.items()):
        path = PROFILE_WORKS / f"{author_id}.json"
        if not path.exists():
            failures.append(f"missing_profile_file:{author_id}")
            continue
        payload = json.loads(path.read_text())
        if payload.get("author_id") != author_id:
            failures.append(f"profile_file_id_mismatch:{author_id}")
        for work in payload["works"]:
            work_id = suffix(work.get("id"))
            if not work_id:
                failures.append(f"missing_work_id:{author_id}")
                continue
            row = records.setdefault(work_id, normalized(work))
            if "accepted_openalex_profile" not in row["discovery_routes"]:
                row["discovery_routes"].append("accepted_openalex_profile")
            for person in people:
                if person not in row["linked_people"]:
                    row["linked_people"].append(person)
                    author_source_links += 1

    author_work_ids = set(records)
    funder_payload = json.loads(FUNDER_WORKS.read_text())
    for work in funder_payload:
        work_id = suffix(work.get("id"))
        row = records.setdefault(work_id, normalized(work))
        if EUROQOL_FUNDER not in row["funders"]:
            failures.append(f"funding_route_missing_funder:{work_id}")
        if "euroqol_funding_metadata" not in row["discovery_routes"]:
            row["discovery_routes"].append("euroqol_funding_metadata")

    for row in records.values():
        row["linked_people"].sort()
        row["discovery_routes"].sort()
        row["euroqol_funding_metadata"] = EUROQOL_FUNDER in row["funders"]
        row["document_gate"] = (
            "candidate_article" if row["document_type"] in ELIGIBLE_TYPES else "exclude_format"
        )

    ordered = sorted(records.values(), key=lambda row: (-(row["year"] or 0), row["openalex_id"]))
    with (SCALE / "openalex-discovery.jsonl").open("w") as handle:
        for row in ordered:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    doi_counts = Counter(row["doi"] for row in ordered if row["doi"])
    type_counts = Counter(row["document_type"] for row in ordered)
    candidates = [row for row in ordered if row["document_gate"] == "candidate_article"]
    summary = {
        "ok": not failures,
        "people_total": 316,
        "people_in_accepted_author_route": sum(len(names) for names in ready_by_author.values()),
        "people_held_for_review": 316 - sum(len(names) for names in ready_by_author.values()),
        "profiles_held_by_binary_qa": 271 - sum(
            len(names) for names in ready_by_author.values()
        ),
        "profiles_accepted_by_binary_qa": len(ready_by_author),
        "additional_profile_assignments_for_accepted_people_held": len(held_split_assignments),
        "distinct_additional_profile_ids_for_accepted_people_held": len(set(held_split_assignments)),
        "unique_author_route_works": len(author_work_ids),
        "author_person_work_links": author_source_links,
        "funding_metadata_works": len(funder_payload),
        "funding_only_works": len({suffix(work.get('id')) for work in funder_payload} - author_work_ids),
        "union_works": len(ordered),
        "document_type_counts": dict(sorted(type_counts.items())),
        "candidate_articles_and_reviews": len(candidates),
        "candidate_articles_with_abstract": sum(
            row["abstract_status"] == "available" for row in candidates
        ),
        "candidate_articles_without_abstract": sum(
            row["abstract_status"] == "unavailable" for row in candidates
        ),
        "duplicate_doi_groups_before_bibliographic_qa": sum(count > 1 for count in doi_counts.values()),
        "rule": (
            "The author route contains only profiles accepted by binary identity QA. "
            "The independent EuroQol funding-metadata route remains available. Held "
            "and additional profile IDs are excluded. Each available abstract is "
            "included in full."
        ),
        "failures": failures,
    }
    (SCALE / "openalex-discovery-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
