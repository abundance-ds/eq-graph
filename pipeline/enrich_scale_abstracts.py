#!/usr/bin/env python3
"""Enrich missing scale abstracts with exact DOI or PMID matches from Europe PMC."""

import csv
import hashlib
import html
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

import pilot_2_0 as pilot


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
SOURCE = SCALE / "source-union.jsonl"
OUT = SCALE / "article-corpus.jsonl"
SUMMARY = SCALE / "abstract-enrichment-summary.json"
SELECTION = SCALE / "abstract-enrichment-selection.json"
RAW = SCALE / "raw" / "abstract-enrichment" / "europe-pmc"
USER_AGENT = "eq-graph-protocol-2.0/0.2 (research; contact: paul@abundanceds.com)"
BATCH_SIZE = 20
MIN_ABSTRACT_LENGTH = 80


def clean_abstract(value):
    text = re.sub(r"<[^>]+>", " ", html.unescape(value or ""))
    return " ".join(text.split())


def query_terms(record):
    dois = [record["doi"], *(record.get("alternate_dois") or [])]
    dois = sorted({pilot.norm_doi(value) for value in dois if pilot.norm_doi(value)})
    if dois:
        return [f'DOI:"{value}"' for value in dois]
    pmids = [record["pmid"], *(record.get("alternate_pmids") or [])]
    pmids = sorted({str(value).strip() for value in pmids if str(value).strip()})
    return [f"(EXT_ID:{value} AND SRC:MED)" for value in pmids]


def make_selection(records):
    eligible = [
        record for record in records
        if len(record["abstract"].strip()) < MIN_ABSTRACT_LENGTH
        and query_terms(record)
    ]
    batches = []
    for index in range(0, len(eligible), BATCH_SIZE):
        batch_records = eligible[index:index + BATCH_SIZE]
        query = " OR ".join(
            f"({term})"
            for record in batch_records
            for term in query_terms(record)
        )
        batch_id = f"batch-{index // BATCH_SIZE + 1:04d}"
        batches.append({
            "batch_id": batch_id,
            "record_ids": [record["record_id"] for record in batch_records],
            "query": query,
            "query_sha256": hashlib.sha256(query.encode()).hexdigest(),
        })
    return {
        "source": "Europe PMC REST search",
        "match_rule": "exact normalized DOI, otherwise exact PMID",
        "batch_size": BATCH_SIZE,
        "records": len(eligible),
        "batches": batches,
    }


def retrieve(batch):
    path = RAW / f"{batch['batch_id']}.json"
    if path.exists():
        return batch, json.loads(path.read_text()), False
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": batch["query"],
        "format": "json",
        "resultType": "core",
        "pageSize": 1000,
    })
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read())
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False) + "\n")
            time.sleep(0.1)
            return batch, payload, True
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def result_indexes(payloads):
    by_doi = {}
    by_pmid = {}
    for payload in payloads:
        for result in (payload.get("resultList") or {}).get("result") or []:
            abstract = clean_abstract(result.get("abstractText") or "")
            if len(abstract) < MIN_ABSTRACT_LENGTH:
                continue
            doi = pilot.norm_doi(result.get("doi") or "")
            pmid = str(result.get("pmid") or "").strip()
            item = {
                "abstract": abstract,
                "doi": doi,
                "pmid": pmid,
                "pmcid": result.get("pmcid") or "",
                "title": result.get("title") or "",
            }
            if doi and len(abstract) > len(by_doi.get(doi, {}).get("abstract", "")):
                by_doi[doi] = item
            if pmid and len(abstract) > len(by_pmid.get(pmid, {}).get("abstract", "")):
                by_pmid[pmid] = item
    return by_doi, by_pmid


def exact_match(record, by_doi, by_pmid):
    for value in [record["doi"], *(record.get("alternate_dois") or [])]:
        doi = pilot.norm_doi(value)
        if doi and doi in by_doi:
            return by_doi[doi], "doi"
    for value in [record["pmid"], *(record.get("alternate_pmids") or [])]:
        pmid = str(value).strip()
        if pmid and pmid in by_pmid:
            return by_pmid[pmid], "pmid"
    return None, ""


def main():
    all_records = [json.loads(line) for line in SOURCE.open()]
    records = [
        record for record in all_records
        if record["document_gate"] == "candidate_article"
    ]
    selection = make_selection(records)
    if SELECTION.exists():
        frozen = json.loads(SELECTION.read_text())
        if frozen != selection:
            raise SystemExit("abstract enrichment selection changed; use a new version")
    else:
        SELECTION.write_text(json.dumps(selection, indent=2) + "\n")

    payloads = []
    failures = []
    network_requests = 0
    with ThreadPoolExecutor(max_workers=4) as executor:
        jobs = {executor.submit(retrieve, batch): batch for batch in selection["batches"]}
        for index, future in enumerate(as_completed(jobs), 1):
            batch = jobs[future]
            try:
                _, payload, retrieved = future.result()
                payloads.append(payload)
                network_requests += int(retrieved)
            except Exception as error:
                failures.append({"batch_id": batch["batch_id"], "error": str(error)})
            if index % 50 == 0:
                print(f"batches={index}/{len(jobs)} failures={len(failures)}", flush=True)
    if failures:
        result = {"ok": False, "failures": failures}
        SUMMARY.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        raise SystemExit(1)

    by_doi, by_pmid = result_indexes(payloads)
    available_before = sum(
        len(record["abstract"].strip()) >= MIN_ABSTRACT_LENGTH for record in records
    )
    enriched = 0
    for record in records:
        record["abstract_source"] = (
            "source_union" if len(record["abstract"].strip()) >= MIN_ABSTRACT_LENGTH else ""
        )
        record["abstract_match"] = ""
        if not record["abstract_source"]:
            match, method = exact_match(record, by_doi, by_pmid)
            if match:
                record["abstract"] = match["abstract"]
                record["abstract_source"] = "europe_pmc"
                record["abstract_match"] = method
                if not record["pmid"] and match["pmid"]:
                    record["pmid"] = match["pmid"]
                enriched += 1
        record["abstract_length_gate"] = (
            len(record["abstract"].strip()) >= MIN_ABSTRACT_LENGTH
        )

    with OUT.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    with (SCALE / "abstract-unavailable-or-short.csv").open("w", newline="") as handle:
        fields = ["record_id", "title", "year", "doi", "pmid", "abstract_length"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({
            "record_id": record["record_id"],
            "title": record["title"],
            "year": record["year"] or "",
            "doi": record["doi"],
            "pmid": record["pmid"],
            "abstract_length": len(record["abstract"].strip()),
        } for record in records if not record["abstract_length_gate"])

    result = {
        "ok": True,
        "candidate_articles_and_reviews": len(records),
        "abstract_length_gate": MIN_ABSTRACT_LENGTH,
        "abstracts_available_before_enrichment": available_before,
        "records_queried_by_exact_identifier": selection["records"],
        "europe_pmc_batches": len(selection["batches"]),
        "network_requests_this_run": network_requests,
        "abstracts_enriched": enriched,
        "abstracts_passing_length_gate": sum(
            record["abstract_length_gate"] for record in records
        ),
        "abstracts_unavailable_or_short": sum(
            not record["abstract_length_gate"] for record in records
        ),
        "records_without_doi_or_pmid_not_queried": sum(
            not query_terms(record)
            and len(record["abstract"].strip()) < MIN_ABSTRACT_LENGTH
            for record in records
        ),
        "rule": (
            "Preserve source abstracts. For missing or short text, accept a Europe PMC "
            "abstract only on exact normalized DOI or exact PMID. Do not use fuzzy matching."
        ),
        "quality_status": (
            "Length gate only. A separate abstract-quality check is required before screening."
        ),
        "failures": [],
    }
    SUMMARY.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
