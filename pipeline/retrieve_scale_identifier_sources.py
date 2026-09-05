#!/usr/bin/env python3
"""Retrieve ORCID works and exact-ORCID PubMed records for accepted profiles."""

import csv
import datetime as dt
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

import pilot_2_0 as pilot


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
ACCEPTED = SCALE / "profile-qa-v1" / "accepted.csv"
RAW = SCALE / "raw" / "identifier-sources"
OUT = SCALE / "identifier-sources"
MANIFEST = SCALE / "identifier-source-summary.json"
USER_AGENT = "eq-graph-protocol-2.0/0.2 (research; contact: paul@abundanceds.com)"
PUBMED_CHUNK = 200


def fetch(url, path, accept, pause=0.0):
    """Return cached bytes or retrieve and cache the response."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_bytes(), False
    request = urllib.request.Request(
        url,
        headers={"Accept": accept, "User-Agent": USER_AGENT},
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
            path.write_bytes(body)
            if pause:
                time.sleep(pause)
            return body, True
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def value(item):
    return (item or {}).get("value") or ""


def external_ids(*containers):
    values = {}
    for container in containers:
        for item in (container or {}).get("external-id", []):
            kind = (item.get("external-id-type") or "").casefold()
            identifier = (item.get("external-id-value") or "").strip()
            if kind and identifier and kind not in values:
                values[kind] = identifier
    return values


def orcid_works(payload):
    """Return one normalized record for each ORCID work group."""
    records = []
    for group in payload.get("group", []):
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        work = summaries[0]
        title = value(((work.get("title") or {}).get("title")))
        if not title:
            continue
        identifiers = external_ids(group.get("external-ids"), work.get("external-ids"))
        date = work.get("publication-date") or {}
        year = value(date.get("year"))
        records.append({
            "source_id": str(work.get("put-code") or ""),
            "doi": pilot.norm_doi(identifiers.get("doi", "")),
            "pmid": identifiers.get("pmid", ""),
            "title": title,
            "year": int(year) if year.isdigit() else None,
            "document_type": work.get("type") or "",
            "venue": value(work.get("journal-title")),
            "url": value(work.get("url")),
            "abstract": "",
        })
    return records


def retrieve_orcid(orcid):
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    body, retrieved = fetch(
        url,
        RAW / "orcid" / f"{orcid}.json",
        "application/json",
        pause=0.1,
    )
    return orcid_works(json.loads(body)), retrieved


def retrieve_pubmed(orcid):
    term = f"{orcid}[AUID]"
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed",
        "term": term,
        "retmode": "json",
        "retmax": 10000,
    })
    body, search_retrieved = fetch(
        search_url,
        RAW / "pubmed" / f"{orcid}-search.json",
        "application/json",
        pause=0.36,
    )
    search = json.loads(body).get("esearchresult", {})
    pmids = search.get("idlist") or []
    expected = int(search.get("count") or 0)
    if expected != len(pmids):
        raise RuntimeError(f"PubMed result limit reached for {orcid}: {len(pmids)}/{expected}")
    if expected and "Author - Identifier" not in (search.get("querytranslation") or ""):
        raise RuntimeError(f"PubMed did not apply the AUID field for {orcid}")

    records = []
    network_requests = int(search_retrieved)
    for index in range(0, len(pmids), PUBMED_CHUNK):
        chunk = pmids[index:index + PUBMED_CHUNK]
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode({
            "db": "pubmed",
            "id": ",".join(chunk),
            "retmode": "xml",
        })
        xml, retrieved = fetch(
            fetch_url,
            RAW / "pubmed" / f"{orcid}-records-{index // PUBMED_CHUNK + 1:03d}.xml",
            "application/xml",
            pause=0.36,
        )
        network_requests += int(retrieved)
        records.extend(pilot.parse_pubmed(xml))
    if len(records) != len(pmids):
        raise RuntimeError(f"PubMed parse count differs for {orcid}: {len(records)}/{len(pmids)}")
    return records, network_requests, {
        "term": term,
        "query_translation": search.get("querytranslation") or "",
        "count": expected,
    }


def main():
    accepted = list(csv.DictReader(ACCEPTED.open(newline="")))
    OUT.mkdir(parents=True, exist_ok=True)
    failures = []
    source_files = []
    orcid_records = 0
    pubmed_records = 0
    profiles_with_orcid = 0
    network_requests = 0

    for index, profile in enumerate(accepted, 1):
        author_id = profile["openalex_id"]
        output = OUT / f"{author_id}.json"
        if output.exists():
            payload = json.loads(output.read_text())
            source_files.append(output)
            orcid_records += len(payload.get("orcid_works") or [])
            pubmed_records += len(payload.get("pubmed_records") or [])
            profiles_with_orcid += int(bool(profile["orcid"]))
            continue

        payload = {
            "name": profile["name"],
            "openalex_id": author_id,
            "orcid": profile["orcid"],
            "retrieval_date": dt.date.today().isoformat(),
            "discovery_rule": "accepted ORCID record or exact PubMed AUID match",
            "orcid_works": [],
            "pubmed_query": {},
            "pubmed_records": [],
        }
        if profile["orcid"]:
            profiles_with_orcid += 1
            try:
                payload["orcid_works"], retrieved = retrieve_orcid(profile["orcid"])
                network_requests += int(retrieved)
                (
                    payload["pubmed_records"],
                    pubmed_network_requests,
                    payload["pubmed_query"],
                ) = retrieve_pubmed(profile["orcid"])
                network_requests += pubmed_network_requests
            except Exception as error:
                failures.append({
                    "name": profile["name"],
                    "openalex_id": author_id,
                    "orcid": profile["orcid"],
                    "error": str(error),
                })
                print(f"FAIL {index}/{len(accepted)} {profile['name']}: {error}", flush=True)
                continue
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        source_files.append(output)
        orcid_records += len(payload["orcid_works"])
        pubmed_records += len(payload["pubmed_records"])
        print(
            f"{index}/{len(accepted)} {profile['name']}: "
            f"ORCID {len(payload['orcid_works'])}, PubMed {len(payload['pubmed_records'])}",
            flush=True,
        )

    summary = {
        "ok": not failures and len(source_files) == len(accepted),
        "accepted_profiles": len(accepted),
        "profiles_with_orcid": profiles_with_orcid,
        "profiles_without_orcid": len(accepted) - profiles_with_orcid,
        "source_files": len(source_files),
        "orcid_work_records": orcid_records,
        "pubmed_exact_orcid_records": pubmed_records,
        "network_requests_this_run": network_requests,
        "rule": (
            "ORCID and PubMed records can add papers only through an ORCID identifier "
            "from a profile accepted by binary identity QA. Name-only PubMed search is not used."
        ),
        "failures": failures,
    }
    MANIFEST.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
