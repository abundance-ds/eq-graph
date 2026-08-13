#!/usr/bin/env python3
"""Prepare safe profile and funding-metadata inputs for Protocol 2.0 scale-up."""

import csv
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone


ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "scale" / "protocol-2.0"
FUNDER_INPUT = ROOT / "artefacts" / "03_funder_works.json"
REVIEW_INPUT = ROOT / "artefacts" / "02_review.csv"
PILOT = ROOT / "pilot" / "protocol-2.0"
EUROQOL_FUNDER = "F4320323856"
ELIGIBLE_TYPES = {"article", "review"}


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, fields, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    failures = []

    review_rows = read_csv(REVIEW_INPUT)
    author_resolution = json.loads((ROOT / "artefacts" / "02_author_ids.json").read_text())
    if len(review_rows) != len({row["name"] for row in review_rows}):
        failures.append("duplicate_profile_review_name")
    profile_rows = []
    for row in review_rows:
        ready = (
            row["review_required"] == "0"
            and row["status"] in {"ok", "ok_via_works"}
            and bool(row["chosen_id"])
        )
        cached_path = ROOT / "artefacts" / "03_works" / f"{row['chosen_id']}.json"
        if ready and not cached_path.exists():
            failures.append(f"missing_cached_profile:{row['name']}:{row['chosen_id']}")
        if ready:
            next_action = "use_cached_profile"
        elif row["status"] in {"unresolved", "not_found"}:
            next_action = "find_and_verify_profile"
        else:
            next_action = "manually_verify_profile"
        profile_rows.append({
            "name": row["name"],
            "scale_status": "ready" if ready else "needs_review",
            "next_action": next_action,
            "review_reason": row["review_reason"],
            "resolution_status": row["status"],
            "chosen_id": row["chosen_id"],
            "additional_profile_ids_held": ";".join(
                author_resolution[row["name"]].get("also_plausible") or []
            ) if ready else "",
            "chosen_name": row["chosen_name"],
            "orcid": row["orcid"],
            "affiliation": row["openalex_affiliation"],
            "member_affiliation": row["member_affiliation"],
            "total_works": row["total_works"],
            "eq_works": row["eq_works"],
            "alternatives": row["alternatives"],
            "project_ids": row["project_ids"],
            "is_member": row["is_member"],
            "cached_profile_path": (
                str(cached_path.relative_to(ROOT)) if cached_path.exists() else ""
            ),
        })
    profile_fields = [
        "name", "scale_status", "next_action", "review_reason", "resolution_status",
        "chosen_id", "additional_profile_ids_held", "chosen_name", "orcid", "affiliation",
        "member_affiliation", "total_works", "eq_works", "alternatives", "project_ids",
        "is_member", "cached_profile_path",
    ]
    write_csv(OUT / "profile-scale-readiness.csv", profile_fields, profile_rows)
    review_queue = []
    for row in profile_rows:
        scopes = []
        if row["scale_status"] == "needs_review":
            scopes.append("primary_profile")
        if row["additional_profile_ids_held"]:
            scopes.append("additional_profile_ids")
        if scopes:
            review_queue.append({"review_scope": ";".join(scopes), **row})
    write_csv(
        OUT / "profile-review-queue.csv",
        ["review_scope", *profile_fields],
        review_queue,
    )

    funder_works = json.loads(FUNDER_INPUT.read_text())
    if len(funder_works) != len({row["id"] for row in funder_works}):
        failures.append("duplicate_funding_metadata_work")
    pilot_works = json.loads((PILOT / "derived" / "works.json").read_text())
    pilot_dois = {normalize_doi(row.get("doi")) for row in pilot_works if row.get("doi")}
    retained = read_csv(PILOT / "screening-final" / "retained.csv")
    retained_dois = {normalize_doi(row["doi"]) for row in retained if row["doi"]}

    funding_rows = []
    for work in funder_works:
        funders = [
            {
                "id": suffix(funder.get("id")),
                "name": funder.get("display_name") or "",
            }
            for funder in work.get("funders") or []
            if funder.get("id")
        ]
        if EUROQOL_FUNDER not in {funder["id"] for funder in funders}:
            failures.append(f"missing_euroqol_funder:{suffix(work.get('id'))}")
        euroqol_awards = sorted({
            (award.get("funder_award_id") or "").strip()
            for award in work.get("awards") or []
            if suffix(award.get("funder_id")) == EUROQOL_FUNDER
            and (award.get("funder_award_id") or "").strip()
        })
        authors = []
        for authorship in work.get("authorships") or []:
            author = authorship.get("author") or {}
            if author.get("display_name"):
                authors.append(author["display_name"])
        abstract = abstract_text(work.get("abstract_inverted_index"))
        location = work.get("primary_location") or {}
        source = location.get("source") or {}
        doi = normalize_doi(work.get("doi"))
        document_type = work.get("type") or "unknown"
        funding_rows.append({
            "openalex_id": suffix(work.get("id")),
            "title": work.get("title") or "",
            "year": work.get("publication_year") or "",
            "publication_date": work.get("publication_date") or "",
            "document_type": document_type,
            "document_gate": "candidate_article" if document_type in ELIGIBLE_TYPES else "exclude_format",
            "doi": doi,
            "venue": source.get("display_name") or "",
            "authors": "; ".join(authors),
            "abstract_status": "available" if abstract else "unavailable",
            "abstract": abstract,
            "funder_id": EUROQOL_FUNDER,
            "funder_name": "EuroQol Research Foundation",
            "euroqol_award_ids": "; ".join(euroqol_awards),
            "funding_metadata_signal": "openalex_funder_relation",
            "requires_fulltext_confirmation": "1",
            "in_pilot_discovery_by_doi": "1" if doi and doi in pilot_dois else "0",
            "in_pilot_retained_by_doi": "1" if doi and doi in retained_dois else "0",
        })
    funding_fields = [
        "openalex_id", "title", "year", "publication_date", "document_type",
        "document_gate", "doi", "venue", "authors", "abstract_status", "abstract",
        "funder_id", "funder_name", "euroqol_award_ids", "funding_metadata_signal",
        "requires_fulltext_confirmation", "in_pilot_discovery_by_doi",
        "in_pilot_retained_by_doi",
    ]
    write_csv(OUT / "funding-metadata-discovery.csv", funding_fields, funding_rows)

    ready_profiles = sum(row["scale_status"] == "ready" for row in profile_rows)
    held_split_assignments = [
        profile_id
        for row in profile_rows
        for profile_id in row["additional_profile_ids_held"].split(";")
        if profile_id
    ]
    eligible_funding = [row for row in funding_rows if row["document_gate"] == "candidate_article"]
    source_timestamp = datetime.fromtimestamp(
        FUNDER_INPUT.stat().st_mtime, tz=timezone.utc
    ).isoformat()
    summary = {
        "ok": not failures,
        "people": len(profile_rows),
        "profiles_ready": ready_profiles,
        "profiles_needing_review": len(profile_rows) - ready_profiles,
        "people_in_profile_review_queue": len(review_queue),
        "ready_people_with_additional_profile_ids_held": sum(
            bool(row["additional_profile_ids_held"]) for row in profile_rows
        ),
        "additional_profile_assignments_held": len(held_split_assignments),
        "distinct_additional_profile_ids_held": len(set(held_split_assignments)),
        "profile_resolution_status": dict(sorted(Counter(
            row["resolution_status"] for row in profile_rows
        ).items())),
        "funding_metadata_works": len(funding_rows),
        "funding_metadata_candidate_articles": len(eligible_funding),
        "funding_metadata_excluded_formats": len(funding_rows) - len(eligible_funding),
        "candidate_articles_with_abstract": sum(
            row["abstract_status"] == "available" for row in eligible_funding
        ),
        "candidate_articles_without_abstract": sum(
            row["abstract_status"] == "unavailable" for row in eligible_funding
        ),
        "works_with_euroqol_award_id": sum(bool(row["euroqol_award_ids"]) for row in funding_rows),
        "pilot_discovery_overlap_by_doi": sum(
            row["in_pilot_discovery_by_doi"] == "1" for row in funding_rows
        ),
        "pilot_retained_overlap_by_doi": sum(
            row["in_pilot_retained_by_doi"] == "1" for row in funding_rows
        ),
        "input_file": str(FUNDER_INPUT.relative_to(ROOT)),
        "input_file_mtime_utc": source_timestamp,
        "rule": (
            "OpenAlex funding metadata is a discovery signal. Full text must confirm "
            "the funding scope before publication."
        ),
        "failures": failures,
    }
    (OUT / "scale-input-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
