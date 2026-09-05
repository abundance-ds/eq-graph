#!/usr/bin/env python3
"""Merge accepted OpenAlex, ORCID, PubMed, and funding discovery records."""

import csv
import difflib
import hashlib
import json
import pathlib
from collections import Counter, defaultdict

import pilot_2_0 as pilot


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
OPENALEX = SCALE / "openalex-discovery.jsonl"
IDENTIFIERS = SCALE / "identifier-sources"
ACCEPTED = SCALE / "profile-qa-v1" / "accepted.csv"
OUTPUT = SCALE / "source-union.jsonl"
SUMMARY = SCALE / "source-union-summary.json"
SOURCE_EXCLUSIONS = ROOT / "pipeline/data/source_record_exclusions.tsv"


def normalize_record(raw, source, person=""):
    """Return common fields for one source record."""
    title = raw.get("title") or ""
    year = raw.get("year")
    if isinstance(year, str) and year.isdigit():
        year = int(year)
    doi = pilot.norm_doi(raw.get("doi") or "")
    pmid = str(raw.get("pmid") or "").strip()
    normalized_title = pilot.norm_title(title)
    title_year = f"{normalized_title}:{year}" if normalized_title and year else ""
    if source == "openalex":
        authors = [item.get("name") or "" for item in raw.get("authors") or []]
        linked_people = list(raw.get("linked_people") or [])
        routes = list(raw.get("discovery_routes") or [])
        source_id = raw.get("openalex_id") or ""
        venue = raw.get("venue") or ""
        document_type = raw.get("document_type") or ""
    else:
        authors = list(raw.get("authors") or [])
        linked_people = [person] if person else []
        routes = ["accepted_orcid_profile" if source == "orcid" else "pubmed_exact_orcid"]
        source_id = str(raw.get("source_id") or "")
        venue = raw.get("venue") or ("PubMed" if source == "pubmed" else "")
        document_type = raw.get("document_type") or ""
    return {
        "source": source,
        "source_id": source_id,
        "doi": doi,
        "pmid": pmid,
        "title": title,
        "normalized_title_year": title_year,
        "year": year,
        "document_type": document_type,
        "venue": venue,
        "authors": [name for name in authors if name],
        "abstract": raw.get("abstract") or "",
        "linked_people": linked_people,
        "discovery_routes": routes,
        "openalex_id": (raw.get("openalex_id") or "") if source == "openalex" else "",
        "funders": list(raw.get("funders") or []),
        "euroqol_award_ids": list(raw.get("euroqol_award_ids") or []),
        "primary_landing_page_url": raw.get("primary_landing_page_url") or "",
        "primary_pdf_url": raw.get("primary_pdf_url") or "",
    }


class Components:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, item):
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left, right):
        left, right = self.find(left), self.find(right)
        if left != right:
            self.parent[right] = left


def union_exact(records, components, field):
    first = {}
    for index, record in enumerate(records):
        token = record[field]
        if not token:
            continue
        if token in first:
            components.union(first[token], index)
        else:
            first[token] = index


def validate_identifier_coherence(records, field):
    """Stop when one exact identifier joins incompatible publications."""
    groups = defaultdict(list)
    for record in records:
        if record[field]:
            groups[record[field]].append(record)
    conflicts = []
    for token, group in groups.items():
        for left_index, left in enumerate(group):
            for right in group[left_index + 1:]:
                titles = (pilot.norm_title(left["title"]), pilot.norm_title(right["title"]))
                title_ratio = difflib.SequenceMatcher(None, *titles).ratio() if all(titles) else 1.0
                years = (left["year"], right["year"])
                year_gap = abs(years[0] - years[1]) if all(isinstance(year, int) for year in years) else 0
                if title_ratio < 0.20 and year_gap > 10:
                    conflicts.append(
                        f"{field}:{token}:{left['source']}:{left['source_id']}:"
                        f"{right['source']}:{right['source_id']}"
                    )
    if conflicts:
        raise ValueError("Incompatible exact identifiers: " + ", ".join(conflicts[:20]))


def union_title_year(records, components):
    """Merge exact title-year groups and return their identifier variants."""
    root_members = defaultdict(list)
    for index in range(len(records)):
        root_members[components.find(index)].append(index)
    candidates = defaultdict(set)
    for index, record in enumerate(records):
        if record["normalized_title_year"]:
            candidates[record["normalized_title_year"]].add(components.find(index))
    variants = []
    for title_year, roots in candidates.items():
        if len(roots) < 2:
            continue
        members = [index for root in roots for index in root_members[root]]
        dois = {records[index]["doi"] for index in members if records[index]["doi"]}
        pmids = {records[index]["pmid"] for index in members if records[index]["pmid"]}
        if len(dois) > 1 or len(pmids) > 1:
            variants.append({
                "normalized_title_year": title_year,
                "dois": ";".join(sorted(dois)),
                "pmids": ";".join(sorted(pmids)),
            })
        anchor = min(roots)
        for root in roots:
            components.union(anchor, root)
    return variants


def is_eligible(record):
    kind = record["document_type"].casefold()
    if record["source"] == "openalex":
        return kind in {"article", "review"}
    if record["source"] == "orcid":
        return kind in {"journal-article", "journal article", "review"}
    return "journal article" in kind or "review" in kind


def merged_record(group):
    source_order = {"pubmed": 0, "openalex": 1, "orcid": 2}
    ordered = sorted(group, key=lambda row: (source_order[row["source"]], row["source_id"]))
    dois = sorted({row["doi"] for row in group if row["doi"]})
    pmids = sorted({row["pmid"] for row in group if row["pmid"]})
    title_years = sorted({row["normalized_title_year"] for row in group if row["normalized_title_year"]})
    if dois:
        stable_key = f"doi:{dois[0]}"
    elif pmids:
        stable_key = f"pmid:{pmids[0]}"
    elif title_years:
        stable_key = f"title:{title_years[0]}"
    else:
        first = ordered[0]
        stable_key = (
            f"source:{first['source']}:{first['source_id']}:"
            f"{pilot.norm_title(first['title'])}"
        )
    title = next((row["title"] for row in ordered if row["title"]), "")
    year = next((row["year"] for row in ordered if row["year"]), None)
    abstract = max((row["abstract"] for row in group), key=len, default="")
    document_types = sorted({row["document_type"] for row in group if row["document_type"]})
    routes = sorted({route for row in group for route in row["discovery_routes"]})
    sources = sorted({row["source"] for row in group})
    authors = []
    for row in ordered:
        if row["authors"]:
            authors = row["authors"]
            break
    linked_people = sorted({person for row in group for person in row["linked_people"]})
    openalex_ids = sorted({row["openalex_id"] for row in group if row["openalex_id"]})
    funders = sorted({funder for row in group for funder in row["funders"]})
    awards = sorted({award for row in group for award in row["euroqol_award_ids"]})
    eligible = any(is_eligible(row) for row in group)
    junk = bool(pilot.JUNK.search(title))
    return {
        "record_id": "P" + hashlib.sha1(stable_key.encode()).hexdigest()[:12],
        "doi": dois[0] if dois else "",
        "alternate_dois": dois[1:],
        "pmid": pmids[0] if pmids else "",
        "alternate_pmids": pmids[1:],
        "title": title,
        "year": year,
        "document_types": document_types,
        "venue": next((row["venue"] for row in ordered if row["venue"]), ""),
        "authors": authors,
        "abstract": abstract,
        "abstract_status": "available" if abstract.strip() else "unavailable",
        "linked_people": linked_people,
        "discovery_routes": routes,
        "sources": sources,
        "source_records": sorted(
            {
                (row["source"], row["source_id"])
                for row in group if row["source_id"]
            }
        ),
        "openalex_ids": openalex_ids,
        "funders": funders,
        "euroqol_award_ids": awards,
        "primary_landing_page_url": next(
            (row["primary_landing_page_url"] for row in ordered if row["primary_landing_page_url"]),
            "",
        ),
        "primary_pdf_url": next(
            (row["primary_pdf_url"] for row in ordered if row["primary_pdf_url"]),
            "",
        ),
        "document_gate": (
            "exclude_document_junk" if junk else
            "candidate_article" if eligible else
            "exclude_format"
        ),
        "source_record_count": len(group),
        "identifier_variants": len(dois) > 1 or len(pmids) > 1,
    }


def main():
    accepted = list(csv.DictReader(ACCEPTED.open(newline="")))
    with SOURCE_EXCLUSIONS.open(encoding="utf-8", newline="") as handle:
        source_exclusions = {
            (row["source"], row["source_id"])
            for row in csv.DictReader(handle, delimiter="\t")
        }
    records = []
    with OPENALEX.open() as handle:
        for line in handle:
            record = normalize_record(json.loads(line), "openalex")
            if (record["source"], record["source_id"]) not in source_exclusions:
                records.append(record)

    missing_identifier_files = []
    for profile in accepted:
        path = IDENTIFIERS / f"{profile['openalex_id']}.json"
        if not path.exists():
            missing_identifier_files.append(profile["openalex_id"])
            continue
        payload = json.loads(path.read_text())
        for row in payload.get("orcid_works") or []:
            record = normalize_record(row, "orcid", profile["name"])
            if (record["source"], record["source_id"]) not in source_exclusions:
                records.append(record)
        for row in payload.get("pubmed_records") or []:
            record = normalize_record(row, "pubmed", profile["name"])
            if (record["source"], record["source_id"]) not in source_exclusions:
                records.append(record)
    if missing_identifier_files:
        raise SystemExit(
            "identifier source files missing: " + ", ".join(missing_identifier_files)
        )

    components = Components(len(records))
    validate_identifier_coherence(records, "doi")
    validate_identifier_coherence(records, "pmid")
    union_exact(records, components, "doi")
    union_exact(records, components, "pmid")
    title_year_variants = union_title_year(records, components)
    groups = defaultdict(list)
    for index, record in enumerate(records):
        groups[components.find(index)].append(record)
    merged = [merged_record(group) for group in groups.values()]
    merged.sort(key=lambda row: (-(row["year"] or 0), row["record_id"]))

    with OUTPUT.open("w") as handle:
        for row in merged:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    with (SCALE / "source-union-title-year-identifier-variants.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["normalized_title_year", "dois", "pmids"],
        )
        writer.writeheader()
        writer.writerows(sorted(
            title_year_variants,
            key=lambda row: row["normalized_title_year"],
        ))

    candidates = [row for row in merged if row["document_gate"] == "candidate_article"]
    routes = Counter(route for row in merged for route in row["discovery_routes"])
    summary = {
        "ok": True,
        "accepted_profiles": len(accepted),
        "source_records": len(records),
        "source_record_counts": dict(sorted(Counter(row["source"] for row in records).items())),
        "deduplicated_records": len(merged),
        "records_removed_as_duplicates": len(records) - len(merged),
        "discovery_route_record_counts_after_deduplication": dict(sorted(routes.items())),
        "candidate_articles_and_reviews": len(candidates),
        "candidate_articles_with_abstract": sum(
            row["abstract_status"] == "available" for row in candidates
        ),
        "candidate_articles_without_abstract": sum(
            row["abstract_status"] == "unavailable" for row in candidates
        ),
        "document_junk_excluded": sum(
            row["document_gate"] == "exclude_document_junk" for row in merged
        ),
        "other_formats_excluded": sum(
            row["document_gate"] == "exclude_format" for row in merged
        ),
        "records_with_identifier_variants": sum(
            row["identifier_variants"] for row in merged
        ),
        "title_year_identifier_variant_groups_merged": len(title_year_variants),
        "rule": (
            "Merge exact DOI, then exact PMID, then exact normalized title and year. "
            "Retain alternate DOI and PMID values in the merged record and audit table."
        ),
        "failures": [],
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
