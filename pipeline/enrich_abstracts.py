#!/usr/bin/env python3
"""Make the pilot corpus screening-ready: eligible article + real abstract.

Existing abstracts are preserved. Missing abstracts are sought in Europe PMC,
Crossref, and OpenAlex using DOI/PMID first and a strict title/year match only
when no identifier is available. Records are never deleted.
"""

import csv
import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
WORKS = PILOT / "derived" / "works.json"
OUT = PILOT / "derived" / "abstract-enrichment.json"
RAW = PILOT / "raw" / "abstract-enrichment"
INVALID_ABSTRACTS = PILOT / "abstract-invalid.csv"
USER_AGENT = "eq-graph-protocol-2.0/0.2 (abstract audit; mailto:research@example.invalid)"
TODAY = dt.date.today().isoformat()

sys.path.insert(0, str(ROOT / "pipeline"))
import pilot_2_0 as pilot  # noqa: E402


def get_json(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return json.loads(path.read_text())
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = json.loads(response.read())
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            time.sleep(0.1)
            return data
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def clean_abstract(value):
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", html.unescape(value))
    value = " ".join(value.split())
    if len(value) < 80:
        return ""
    return value


def title_key(value):
    for character in "‐‑‒–—−":
        value = (value or "").replace(character, " ")
    return pilot.norm_title(value)


def title_matches(left, right):
    left_key, right_key = title_key(left), title_key(right)
    if not left_key or not right_key:
        return False
    if left_key == right_key:
        return True
    left_truncated = (left or "").strip().endswith(("…", "..."))
    right_truncated = (right or "").strip().endswith(("…", "..."))
    return (
        left_truncated and right_key.startswith(left_key)
    ) or (
        right_truncated and left_key.startswith(right_key)
    )


def year_matches(record, candidate_year):
    if not record.get("year") or not candidate_year:
        return False
    try:
        return int(record["year"]) == int(candidate_year)
    except (TypeError, ValueError):
        return False


def select_candidate(record, candidates, doi_key="doi", title_key="title", year_key="year"):
    doi = pilot.norm_doi(record.get("doi", ""))
    if doi:
        exact = [x for x in candidates if pilot.norm_doi(x.get(doi_key, "")) == doi]
        if exact:
            return exact[0], "doi"
    exact = [
        candidate for candidate in candidates
        if title_matches(record["title"], candidate.get(title_key, ""))
        and year_matches(record, candidate.get(year_key))
    ]
    if len(exact) == 1:
        return exact[0], "title_year"
    return None, ""


def europe_pmc(record):
    if record.get("doi"):
        query = f'DOI:"{record["doi"]}"'
    elif record.get("pmid"):
        query = f'EXT_ID:{record["pmid"]} AND SRC:MED'
    else:
        query = f'TITLE:"{record["title"]}"'
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": query, "format": "json", "resultType": "core", "pageSize": 10,
    })
    data = get_json(url, RAW / "europe-pmc" / f"{record['record_id']}.json")
    candidates = data.get("resultList", {}).get("result", [])
    candidate, match = select_candidate(record, candidates, year_key="pubYear")
    if not candidate:
        return None
    return {
        "source": "europe_pmc", "match": match,
        "abstract": clean_abstract(candidate.get("abstractText", "")),
        "doi": pilot.norm_doi(candidate.get("doi", "")),
        "pmid": candidate.get("pmid", ""), "pmcid": candidate.get("pmcid", ""),
        "matched_title": candidate.get("title", ""),
    }


def crossref(record):
    if record.get("doi"):
        url = "https://api.crossref.org/works/" + urllib.parse.quote(record["doi"], safe="")
        data = get_json(url, RAW / "crossref" / f"{record['record_id']}.json")
        candidates = [data.get("message", {})]
    else:
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.bibliographic": record["title"], "rows": 5,
            "select": "DOI,title,type,abstract,published,published-print,published-online",
        })
        data = get_json(url, RAW / "crossref" / f"{record['record_id']}.json")
        candidates = data.get("message", {}).get("items", [])
    normalized = []
    for item in candidates:
        dates = (
            item.get("published", {}).get("date-parts")
            or item.get("published-print", {}).get("date-parts")
            or item.get("published-online", {}).get("date-parts") or []
        )
        normalized.append({
            "raw": item, "doi": item.get("DOI", ""),
            "title": " ".join(item.get("title", [])),
            "year": dates[0][0] if dates and dates[0] else None,
        })
    candidate, match = select_candidate(record, normalized)
    if not candidate:
        return None
    item = candidate["raw"]
    return {
        "source": "crossref", "match": match,
        "abstract": clean_abstract(item.get("abstract", "")),
        "doi": pilot.norm_doi(item.get("DOI", "")), "pmid": "", "pmcid": "",
        "matched_title": candidate["title"], "crossref_type": item.get("type", ""),
    }


def openalex(record):
    fields = "id,title,doi,publication_year,abstract_inverted_index,type"
    if record.get("doi"):
        work_id = "https://doi.org/" + record["doi"]
        url = "https://api.openalex.org/works/" + urllib.parse.quote(work_id, safe="") + "?" + urllib.parse.urlencode({"select": fields})
        data = get_json(url, RAW / "openalex" / f"{record['record_id']}.json")
        candidates = [data]
    else:
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
            "search": record["title"], "per-page": 5, "select": fields,
        })
        data = get_json(url, RAW / "openalex" / f"{record['record_id']}.json")
        candidates = data.get("results", [])
    normalized = [{
        "raw": item, "doi": item.get("doi", ""), "title": item.get("title", ""),
        "year": item.get("publication_year"),
    } for item in candidates]
    candidate, match = select_candidate(record, normalized)
    if not candidate:
        return None
    item = candidate["raw"]
    inverted = item.get("abstract_inverted_index") or {}
    tokens = sorted(
        ((position, token) for token, positions in inverted.items() for position in positions),
        key=lambda pair: pair[0],
    )
    return {
        "source": "openalex", "match": match,
        "abstract": clean_abstract(" ".join(token for _, token in tokens)),
        "doi": pilot.norm_doi(item.get("doi", "")), "pmid": "", "pmcid": "",
        "matched_title": item.get("title", ""), "openalex_type": item.get("type", ""),
    }


def resolve_missing_abstract(record):
    attempts = []
    for resolver in (europe_pmc, crossref, openalex):
        try:
            result = resolver(record)
            attempts.append({
                "source": resolver.__name__, "matched": bool(result),
                "has_abstract": bool(result and result.get("abstract")),
            })
            if result and result.get("abstract"):
                return result, attempts
        except Exception as exc:
            attempts.append({"source": resolver.__name__, "error": type(exc).__name__})
    return None, attempts


def merge_identifier_duplicates(works):
    parent = {record["record_id"]: record["record_id"] for record in works}

    def find(record_id):
        while parent[record_id] != record_id:
            parent[record_id] = parent[parent[record_id]]
            record_id = parent[record_id]
        return record_id

    def union(left, right):
        left, right = find(left), find(right)
        if left != right:
            parent[right] = left

    for field in ("doi", "pmid"):
        seen = {}
        for record in works:
            value = record.get(field, "")
            if not value:
                continue
            if value in seen:
                union(seen[value], record["record_id"])
            else:
                seen[value] = record["record_id"]

    groups = {}
    by_id = {record["record_id"]: record for record in works}
    for record_id in parent:
        groups.setdefault(find(record_id), []).append(record_id)
    lineage, removed = [], set()
    for record_ids in groups.values():
        if len(record_ids) == 1:
            continue
        records = [by_id[record_id] for record_id in record_ids]
        records.sort(key=lambda record: (-len(record.get("sources", [])), record["record_id"]))
        target = records[0]
        for source in records[1:]:
            for author in source.get("authors", []):
                if author not in target["authors"]:
                    target["authors"].append(author)
            source_keys = {
                (item.get("author"), item.get("source"), item.get("source_id"))
                for item in target.get("sources", [])
            }
            target["sources"].extend(
                item for item in source.get("sources", [])
                if (item.get("author"), item.get("source"), item.get("source_id")) not in source_keys
            )
            target["profile_flags"] = sorted(set(target.get("profile_flags", []) + source.get("profile_flags", [])))
            if len(source.get("abstract", "")) > len(target.get("abstract", "")):
                for field in ("abstract", "abstract_status", "abstract_source", "abstract_retrieval_method", "abstract_retrieved"):
                    if field in source:
                        target[field] = source[field]
            for field in ("doi", "pmid", "pmcid"):
                if not target.get(field) and source.get(field):
                    target[field] = source[field]
            target["screening_ready"] = bool(target.get("screening_ready") or source.get("screening_ready"))
            removed.add(source["record_id"])
            lineage.append({"removed_record_id": source["record_id"], "retained_record_id": target["record_id"]})
    return [record for record in works if record["record_id"] not in removed], lineage


def main():
    works = json.loads(WORKS.read_text())
    invalid_abstracts = {
        row["record_id"]: row
        for row in csv.DictReader(INVALID_ABSTRACTS.open())
    } if INVALID_ABSTRACTS.exists() else {}
    previous_data, previous_audit, previous_lineage = {}, {}, []
    if OUT.exists():
        previous_data = json.loads(OUT.read_text())
        previous_audit = {
            item["record_id"]: item
            for item in previous_data.get("records", [])
        }
        previous_lineage = previous_data.get("duplicate_lineage", [])
    candidates = [
        x for x in works
        if x.get("eligibility_status") in {"candidate_full_journal_article", "exclude_abstract_unavailable"}
    ]
    audit, missing = [], []
    enriched = 0
    for record in candidates:
        if record["record_id"] in invalid_abstracts:
            issue = invalid_abstracts[record["record_id"]]
            record["abstract_status"] = "invalid"
            record["screening_ready"] = False
            record["eligibility_status"] = "exclude_abstract_unavailable"
            record["eligibility_reason"] = "stored abstract is not a usable article abstract"
            audit.append({
                "record_id": record["record_id"],
                "title": record["title"],
                "doi": record.get("doi", ""),
                "outcome": "invalid",
                "abstract_source": record.get("abstract_source", ""),
                "attempts": [],
                "reason": issue["reason"],
                "detected_in": issue["detected_in"],
            })
            continue
        existing = clean_abstract(record.get("abstract", ""))
        if existing:
            record["abstract"] = existing
            record["abstract_status"] = "available"
            record["abstract_source"] = record.get("abstract_source") or "source_union"
            record["screening_ready"] = True
            continue
        if record.get("abstract_status") == "unavailable" and record["record_id"] in previous_audit:
            record["screening_ready"] = False
            record["eligibility_status"] = "exclude_abstract_unavailable"
            continue
        missing.append(record)

    with ThreadPoolExecutor(max_workers=6) as executor:
        jobs = {executor.submit(resolve_missing_abstract, record): record for record in missing}
        for index, future in enumerate(as_completed(jobs), 1):
            record = jobs[future]
            found, attempts = future.result()
            if found:
                record["abstract"] = found["abstract"]
                record["abstract_status"] = "available"
                record["abstract_source"] = found["source"]
                record["abstract_retrieval_method"] = found["match"]
                record["abstract_retrieved"] = TODAY
                record["screening_ready"] = True
                for field in ("doi", "pmid", "pmcid"):
                    if not record.get(field) and found.get(field):
                        record[field] = found[field]
                enriched += 1
            else:
                record["abstract_status"] = "unavailable"
                record["abstract_source"] = ""
                record["screening_ready"] = False
                record["eligibility_status"] = "exclude_abstract_unavailable"
                record["eligibility_reason"] = "no abstract after bibliographic enrichment"
            audit.append({
                "record_id": record["record_id"], "title": record["title"],
                "doi": record.get("doi", ""), "outcome": record["abstract_status"],
                "abstract_source": record.get("abstract_source", ""), "attempts": attempts,
            })
            if index % 50 == 0:
                print(f"processed={index}/{len(missing)} enriched={enriched}", flush=True)

    previous_audit.update({item["record_id"]: item for item in audit})
    audit = sorted(previous_audit.values(), key=lambda item: item["record_id"])

    works, new_duplicate_lineage = merge_identifier_duplicates(works)
    duplicate_lineage = previous_lineage + [
        item for item in new_duplicate_lineage if item not in previous_lineage
    ]

    WORKS.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n")
    final_candidates = [
        x for x in works
        if x.get("eligibility_status") in {"candidate_full_journal_article", "exclude_abstract_unavailable"}
    ]
    summary = {
        "retrieved": TODAY,
        "journal_article_candidates_before_abstract_gate": len(final_candidates),
        "abstract_available_before_enrichment": sum(
            x.get("abstract_source") == "source_union" and x.get("abstract_status") == "available"
            for x in final_candidates
        ),
        "abstract_enriched": sum(
            x.get("abstract_source") in {"europe_pmc", "crossref", "openalex"}
            and x.get("abstract_status") == "available" for x in final_candidates
        ),
        "abstract_unavailable_excluded": sum(
            x.get("eligibility_status") == "exclude_abstract_unavailable"
            for x in final_candidates
        ),
        "screening_ready": sum(bool(x.get("screening_ready")) for x in works),
        "duplicates_merged_after_abstract_enrichment": len(duplicate_lineage),
        "deduplicated_works_after_abstract_enrichment": len(works),
    }
    OUT.write_text(json.dumps({
        "summary": summary, "duplicate_lineage": duplicate_lineage, "records": audit,
    }, ensure_ascii=False, indent=2) + "\n")

    aggregate_path = PILOT / "derived" / "aggregate_counts.json"
    aggregate = json.loads(aggregate_path.read_text())
    for stale_key in ("new_duplicate_identifier_flags", "deduplicated_works_after_abstract_enrichment"):
        aggregate.pop(stale_key, None)
    aggregate["deduplicated_works"] = len(works)
    aggregate["full_journal_article_candidates"] = len(final_candidates)
    aggregate.update(summary)
    aggregate_path.write_text(json.dumps(aggregate, indent=2) + "\n")

    with (PILOT / "abstract-unavailable.csv").open("w", newline="") as handle:
        fields = ["record_id", "title", "doi", "outcome", "abstract_source"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(
            {key: item.get(key, "") for key in fields}
            for item in audit if item["outcome"] in {"unavailable", "invalid"}
        )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
