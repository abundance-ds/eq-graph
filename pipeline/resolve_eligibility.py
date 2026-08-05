#!/usr/bin/env python3
"""Resolve missing publication types in the Protocol 2.0 pilot."""

import difflib
import csv
import json
import pathlib
import time
import urllib.parse
import urllib.request

import pilot_2_0 as pilot


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
RAW = PILOT / "raw" / "eligibility"
OUT = PILOT / "derived" / "eligibility-resolution.json"
WORKS = PILOT / "derived" / "works.json"
USER_AGENT = "eq-graph-protocol-2.0/0.1 (research pilot)"


def get_json(url, path, accept="application/json"):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return json.loads(path.read_text())
    request = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                data = json.loads(response.read())
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            time.sleep(0.12)
            return data
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


def get_text(url, path, accept):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_text()
    request = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        text = response.read().decode("utf-8")
    path.write_text(text)
    time.sleep(0.12)
    return text


def orcid_items(data):
    items = []
    for group in data.get("group", []):
        for work in group.get("work-summary", []):
            title = (((work.get("title") or {}).get("title") or {}).get("value") or "")
            external = (work.get("external-ids") or {}).get("external-id", [])
            dois = [
                x.get("external-id-value", "") for x in external
                if x.get("external-id-type", "").lower() == "doi"
            ]
            items.append({
                "title": title,
                "doi": pilot.norm_doi(dois[0]) if dois else "",
                "type": work.get("type") or "",
                "put_code": work.get("put-code"),
            })
    return items


def close_title(query, candidate):
    left, right = pilot.norm_title(query), pilot.norm_title(candidate)
    if not left or not right:
        return 0.0
    if min(len(left), len(right)) >= 40 and (left.startswith(right) or right.startswith(left)):
        return 1.0
    return difflib.SequenceMatcher(None, left, right).ratio()


def classify(kind, source_type="", venue=""):
    kind = (kind or "").lower()
    source_type = (source_type or "").lower()
    venue = (venue or "").lower()
    if (
        (kind in {"journal-article", "article", "review"} or "journal article" in kind)
        and (source_type in {"", "journal"} or venue == "pubmed")
    ):
        return "candidate_full_journal_article"
    if kind in {
        "conference-abstract", "conference-paper", "proceedings-article", "proceedings",
        "book", "book-chapter", "book-section", "dissertation", "posted-content", "preprint",
        "report", "dataset", "data-set", "editorial", "letter", "peer-review", "paratext", "other",
        "edited-book", "working-paper", "clinical-guideline",
    }:
        return "exclude_non_journal"
    return "uncertain"


def crossref(record):
    rid = record["record_id"]
    if record.get("doi"):
        url = "https://api.crossref.org/works/" + urllib.parse.quote(record["doi"], safe="")
        data = get_json(url, RAW / "crossref" / f"{rid}.json")
        candidates = [data.get("message", {})]
        method = "crossref_doi"
    else:
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.title": record["title"], "rows": 5,
            "select": "DOI,title,type,container-title,published,page,volume,issue",
        })
        data = get_json(url, RAW / "crossref" / f"{rid}.json")
        candidates = data.get("message", {}).get("items", [])
        method = "crossref_title"
    ranked = sorted(
        ((close_title(record["title"], " ".join(x.get("title", []))), x) for x in candidates),
        reverse=True, key=lambda pair: pair[0],
    )
    if not ranked or ranked[0][0] < 0.94:
        return None
    score, item = ranked[0]
    return {
        "method": method, "match_score": round(score, 3), "matched_title": " ".join(item.get("title", [])),
        "matched_id": pilot.norm_doi(item.get("DOI", "")), "source_type": item.get("type", ""),
        "venue": " ".join(item.get("container-title", [])),
        "status": classify(item.get("type", "")),
    }


def pubmed(record):
    rid = record["record_id"]
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "term": f"{record['title']}[Title]", "retmode": "json", "retmax": 5,
    })
    search = get_json(search_url, RAW / "pubmed" / f"{rid}-search.json")
    pmids = search.get("esearchresult", {}).get("idlist", [])
    if not pmids:
        return None
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids), "retmode": "xml",
    })
    records = pilot.parse_pubmed(get_text(
        fetch_url, RAW / "pubmed" / f"{rid}-records.xml", "application/xml"
    ))
    ranked = sorted(
        ((close_title(record["title"], x.get("title", "")), x) for x in records),
        reverse=True, key=lambda pair: pair[0],
    )
    if not ranked or ranked[0][0] < 0.94:
        return None
    score, item = ranked[0]
    return {
        "method": "pubmed_title", "match_score": round(score, 3),
        "matched_title": item.get("title", ""), "matched_id": item.get("pmid", ""),
        "source_type": item.get("document_type", ""), "venue": "PubMed",
        "status": classify(item.get("document_type", ""), "", "PubMed"),
    }


def openalex(record):
    rid = record["record_id"]
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": record["title"], "per-page": 5,
        "select": "id,title,doi,type,publication_year,primary_location,biblio",
    })
    data = get_json(url, RAW / "openalex" / f"{rid}.json")
    ranked = sorted(
        ((close_title(record["title"], x.get("title", "")), x) for x in data.get("results", [])),
        reverse=True, key=lambda pair: pair[0],
    )
    if not ranked or ranked[0][0] < 0.94:
        return None
    score, item = ranked[0]
    location = item.get("primary_location") or {}
    source = location.get("source") or {}
    return {
        "method": "openalex_title", "match_score": round(score, 3), "matched_title": item.get("title", ""),
        "matched_id": item.get("id", ""), "source_type": item.get("type", ""),
        "venue": source.get("display_name", ""),
        "status": classify(item.get("type", ""), source.get("type", ""), source.get("display_name", "")),
    }


def main():
    authors = json.loads((PILOT / "derived" / "authors.json").read_text())["authors"]
    author_by_name = {x["name"]: x for x in authors}
    orcid_by_author = {}
    for author in authors:
        if not author.get("orcid"):
            continue
        url = f"https://pub.orcid.org/v3.0/{author['orcid']}/works"
        data = get_json(url, RAW / "orcid" / f"{pilot.slug(author['name'])}.json")
        orcid_by_author[author["name"]] = orcid_items(data)

    works = json.loads(WORKS.read_text())
    override_path = PILOT / "eligibility-manual-review.csv"
    overrides = {}
    if override_path.exists():
        with override_path.open(newline="") as handle:
            overrides = {row["record_id"]: row for row in csv.DictReader(handle)}
    decisions = []
    for record in works:
        if record.get("eligibility_status") != "uncertain":
            continue
        decision = None
        for source in record["sources"]:
            if source["source"] != "orcid":
                continue
            for item in orcid_by_author.get(source["author"], []):
                doi_match = record.get("doi") and item["doi"] == record["doi"]
                title_score = close_title(record["title"], item["title"])
                if doi_match or title_score >= 0.98:
                    decision = {
                        "method": "orcid", "match_score": round(title_score, 3),
                        "matched_title": item["title"], "matched_id": str(item["put_code"]),
                        "source_type": item["type"], "venue": "", "status": classify(item["type"]),
                    }
                    break
            if decision:
                break
        if not decision:
            try:
                decision = crossref(record)
            except Exception:
                decision = None
        if not decision:
            try:
                decision = pubmed(record)
            except Exception:
                decision = None
        if not decision:
            try:
                decision = openalex(record)
            except Exception:
                decision = None
        if not decision:
            decision = {
                "method": "unresolved", "match_score": 0, "matched_title": "", "matched_id": "",
                "source_type": "", "venue": "", "status": "uncertain",
            }
        if decision["status"] == "uncertain" and record["record_id"] in overrides:
            override = overrides[record["record_id"]]
            decision = {
                "method": "manual_source_type_review", "match_score": 1,
                "matched_title": record["title"], "matched_id": "",
                "source_type": override["evidence"], "venue": override["evidence"],
                "status": override["status"],
            }
        decision.update({"record_id": record["record_id"], "title": record["title"]})
        decisions.append(decision)

    by_id = {x["record_id"]: x for x in decisions}
    for record in works:
        if record["record_id"] not in by_id:
            continue
        decision = by_id[record["record_id"]]
        record["eligibility_status"] = decision["status"]
        record["eligibility_reason"] = (
            f"{decision['method']}: {decision['source_type'] or 'type unresolved'}"
        )

    work_by_id = {x["record_id"]: x for x in works}
    doi_to_id = {x["doi"]: x["record_id"] for x in works if x.get("doi")}
    pmid_to_id = {x["pmid"]: x["record_id"] for x in works if x.get("pmid")}
    openalex_to_id = {
        source["source_id"]: work["record_id"]
        for work in works for source in work["sources"] if source["source"] == "openalex"
    }
    merge_links = {}
    for decision in decisions:
        source_id = decision["record_id"]
        target_id = overrides.get(source_id, {}).get("merge_into_record_id", "")
        if decision["method"].startswith("crossref"):
            target_id = target_id or doi_to_id.get(decision["matched_id"], "")
        elif decision["method"] == "pubmed_title":
            target_id = target_id or pmid_to_id.get(decision["matched_id"], "")
        elif decision["method"] == "openalex_title":
            target_id = target_id or openalex_to_id.get(decision["matched_id"].rsplit("/", 1)[-1], "")
        if target_id and target_id != source_id and target_id in work_by_id:
            merge_links[source_id] = target_id
            decision["merge_into_record_id"] = target_id

    for source_id, target_id in merge_links.items():
        source, target = work_by_id[source_id], work_by_id[target_id]
        for author in source["authors"]:
            if author not in target["authors"]:
                target["authors"].append(author)
        existing_sources = {
            (x["author"], x["source"], x["source_id"]) for x in target["sources"]
        }
        target["sources"].extend(
            x for x in source["sources"]
            if (x["author"], x["source"], x["source_id"]) not in existing_sources
        )
        target["profile_flags"] = sorted(set(target["profile_flags"] + source["profile_flags"]))
        target["positive_signal"] = target["positive_signal"] or source["positive_signal"]
        if source["eligibility_status"] == "candidate_full_journal_article":
            target["eligibility_status"] = "candidate_full_journal_article"
    works = [x for x in works if x["record_id"] not in merge_links]
    WORKS.write_text(json.dumps(works, ensure_ascii=False, indent=2))
    summary = {
        status: sum(x["status"] == status for x in decisions)
        for status in ["candidate_full_journal_article", "exclude_non_journal", "uncertain"]
    }
    OUT.write_text(json.dumps({
        "summary": summary, "duplicates_merged": len(merge_links), "decisions": decisions,
    }, ensure_ascii=False, indent=2))
    aggregate_path = PILOT / "derived" / "aggregate_counts.json"
    aggregate = json.loads(aggregate_path.read_text())
    aggregate.update({
        "deduplicated_works": len(works),
        "document_excluded": sum(x["eligibility_status"] == "exclude_document" for x in works),
        "non_journal_excluded": sum(x["eligibility_status"] == "exclude_non_journal" for x in works),
        "publication_type_uncertain": sum(x["eligibility_status"] == "uncertain" for x in works),
        "full_journal_article_candidates": sum(
            x["eligibility_status"] == "candidate_full_journal_article" for x in works
        ),
    })
    aggregate_path.write_text(json.dumps(aggregate, indent=2) + "\n")
    with (PILOT / "eligibility-unresolved.csv").open("w", newline="") as handle:
        fields = ["record_id", "title", "method", "source_type", "venue"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: x.get(field, "") for field in fields} for x in decisions if x["status"] == "uncertain")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
