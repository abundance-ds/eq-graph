#!/usr/bin/env python3
"""Retrieve open full text for articles retained by the pilot screen."""

import csv
import datetime as dt
import hashlib
import json
import os
import pathlib
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
SCREEN = PILOT / "screening-final"
OUT = PILOT / "fulltext"
RECORDS = OUT / "records"
RAW = OUT / "raw"
API = OUT / "api"
TEXT = OUT / "text"
USER_AGENT = "eq-graph-protocol-2.0/0.3 (full-text audit; mailto:paul@priorb.com)"
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "paul@priorb.com")
TODAY = dt.date.today().isoformat()


def ensure_dirs():
    for path in [RECORDS, RAW / "europe-pmc", RAW / "pdf", API / "europe-pmc", API / "openalex", API / "unpaywall", TEXT]:
        path.mkdir(parents=True, exist_ok=True)


def get_bytes(url, path, accept="application/json", retries=3):
    if path.exists():
        return path.read_bytes()
    request = urllib.request.Request(
        url,
        headers={"Accept": accept, "User-Agent": USER_AGENT},
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            return body
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)


def get_json(url, path):
    return json.loads(get_bytes(url, path))


def norm_doi(value):
    value = value or ""
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if value.casefold().startswith(prefix):
            value = value[len(prefix):]
    return value.strip().casefold()


def epmc_result(record):
    if record.get("pmcid"):
        return {"pmcid": record["pmcid"], "match": "existing_pmcid"}
    query = f'DOI:"{record["doi"]}"' if record.get("doi") else f'EXT_ID:{record["pmid"]} AND SRC:MED'
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": query,
        "format": "json",
        "resultType": "core",
        "pageSize": 10,
    })
    data = get_json(url, API / "europe-pmc" / f"{record['record_id']}.json")
    for item in data.get("resultList", {}).get("result", []):
        doi_match = record.get("doi") and norm_doi(item.get("doi")) == norm_doi(record["doi"])
        pmid_match = record.get("pmid") and item.get("pmid") == record["pmid"]
        if doi_match or pmid_match:
            return {
                "pmcid": item.get("pmcid", ""),
                "match": "doi" if doi_match else "pmid",
                "full_text_urls": item.get("fullTextUrlList", {}).get("fullTextUrl", []),
            }
    return {}


def xml_text(path):
    root = ET.fromstring(path.read_bytes())

    def node_text(node):
        return " ".join("".join(node.itertext()).split()) if node is not None else ""

    parts = []
    for xpath in [".//article-title", ".//abstract", ".//body"]:
        value = node_text(root.find(xpath))
        if value:
            parts.append(value)
    for xpath in [".//ack", ".//funding-group"]:
        for node in root.findall(xpath):
            value = node_text(node)
            if value and value not in parts:
                parts.append(value)
    return "\n\n".join(parts)


def find_existing_epmc_xml(record_id, pmcid):
    candidates = [
        PILOT / "raw" / "europe-pmc" / f"{record_id}-{pmcid}.xml",
        RAW / "europe-pmc" / f"{record_id}-{pmcid}.xml",
    ]
    return next((path for path in candidates if path.exists()), None)


def openalex_locations(record):
    source_ids = [
        item["source_id"] for item in record.get("sources", [])
        if item.get("source") == "openalex" and item.get("source_id", "").startswith("W")
    ]
    work_id = source_ids[0] if source_ids else "https://doi.org/" + record["doi"]
    url = "https://api.openalex.org/works/" + urllib.parse.quote(work_id, safe="") + "?" + urllib.parse.urlencode({
        "select": "id,doi,open_access,best_oa_location,locations",
        "mailto": UNPAYWALL_EMAIL,
    })
    data = get_json(url, API / "openalex" / f"{record['record_id']}.json")
    locations = []
    if data.get("best_oa_location"):
        locations.append(data["best_oa_location"])
    locations.extend(data.get("locations") or [])
    return [{
        "source": "openalex",
        "pdf_url": item.get("pdf_url") or "",
        "landing_url": item.get("landing_page_url") or "",
    } for item in locations if item]


def unpaywall_locations(record):
    url = "https://api.unpaywall.org/v2/" + urllib.parse.quote(record["doi"], safe="") + "?" + urllib.parse.urlencode({
        "email": UNPAYWALL_EMAIL,
    })
    data = get_json(url, API / "unpaywall" / f"{record['record_id']}.json")
    locations = []
    if data.get("best_oa_location"):
        locations.append(data["best_oa_location"])
    locations.extend(data.get("oa_locations") or [])
    return [{
        "source": "unpaywall",
        "pdf_url": item.get("url_for_pdf") or "",
        "landing_url": item.get("url_for_landing_page") or "",
    } for item in locations if item]


def unique_locations(locations):
    seen = set()
    output = []
    for item in locations:
        key = item.get("pdf_url") or item.get("landing_url")
        if not key or key in seen:
            continue
        seen.add(key)
        output.append(item)
    return output


def download_pdf(url, path):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/pdf",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        body = response.read(100 * 1024 * 1024 + 1)
        final_url = response.geturl()
        content_type = response.headers.get("Content-Type", "")
    if len(body) > 100 * 1024 * 1024:
        raise ValueError("PDF exceeds 100 MB limit")
    if not body.startswith(b"%PDF-"):
        raise ValueError(f"response is not PDF: {content_type}")
    path.write_bytes(body)
    return final_url


def pdf_text(pdf_path, text_path):
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), str(text_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "pdftotext failed")
    value = text_path.read_text(errors="replace")
    if len(value.strip()) < 500:
        raise ValueError("PDF text is too short")
    return value


def process_record(record):
    record_path = RECORDS / f"{record['record_id']}.json"
    if record_path.exists():
        return json.loads(record_path.read_text())
    result = {
        "record_id": record["record_id"],
        "title": record["title"],
        "doi": record.get("doi", ""),
        "pmid": record.get("pmid", ""),
        "pmcid": record.get("pmcid", ""),
        "screen_code": record["screen_code"],
        "status": "unavailable",
        "source": "",
        "raw_path": "",
        "text_path": "",
        "text_chars": 0,
        "url": "",
        "landing_url": "",
        "retrieved": TODAY,
        "attempts": [],
    }

    try:
        epmc = epmc_result(record)
        result["attempts"].append({"source": "europe_pmc", "pmcid": epmc.get("pmcid", "")})
        pmcid = epmc.get("pmcid", "")
        if pmcid:
            result["pmcid"] = pmcid
            xml_path = find_existing_epmc_xml(record["record_id"], pmcid)
            if not xml_path:
                xml_path = RAW / "europe-pmc" / f"{record['record_id']}-{pmcid}.xml"
                url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
                get_bytes(url, xml_path, accept="application/xml")
            value = xml_text(xml_path)
            if len(value.strip()) >= 500:
                text_path = TEXT / f"{record['record_id']}.txt"
                text_path.write_text(value + "\n")
                result.update({
                    "status": "available",
                    "source": "europe_pmc_xml",
                    "raw_path": str(xml_path.relative_to(ROOT)),
                    "text_path": str(text_path.relative_to(ROOT)),
                    "text_chars": len(value),
                    "url": f"https://europepmc.org/articles/{pmcid}",
                })
                record_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
                return result
    except Exception as exc:
        result["attempts"].append({"source": "europe_pmc_error", "error": type(exc).__name__})

    locations = []
    try:
        locations.extend(openalex_locations(record))
    except Exception as exc:
        result["attempts"].append({"source": "openalex_error", "error": type(exc).__name__})
    try:
        locations.extend(unpaywall_locations(record))
    except Exception as exc:
        result["attempts"].append({"source": "unpaywall_error", "error": type(exc).__name__})

    for index, location in enumerate(unique_locations(locations), 1):
        pdf_url = location.get("pdf_url", "")
        result["attempts"].append({
            "source": location["source"],
            "pdf_url": pdf_url,
            "landing_url": location.get("landing_url", ""),
        })
        if not pdf_url:
            if not result["landing_url"]:
                result["landing_url"] = location.get("landing_url", "")
            continue
        pdf_path = RAW / "pdf" / f"{record['record_id']}.pdf"
        text_path = TEXT / f"{record['record_id']}.txt"
        try:
            final_url = download_pdf(pdf_url, pdf_path)
            value = pdf_text(pdf_path, text_path)
            result.update({
                "status": "available",
                "source": location["source"] + "_pdf",
                "raw_path": str(pdf_path.relative_to(ROOT)),
                "text_path": str(text_path.relative_to(ROOT)),
                "text_chars": len(value),
                "url": final_url,
                "landing_url": location.get("landing_url", ""),
            })
            break
        except Exception as exc:
            result["attempts"][-1]["error"] = type(exc).__name__
            if pdf_path.exists() and not pdf_path.read_bytes().startswith(b"%PDF-"):
                pdf_path.unlink()

    record_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return result


def main():
    ensure_dirs()
    retained = list(csv.DictReader((SCREEN / "retained.csv").open(newline="")))
    works = {
        work["record_id"]: work
        for work in json.loads((PILOT / "derived" / "works.json").read_text())
    }
    records = []
    for item in retained:
        record = dict(works[item["record_id"]])
        record["screen_code"] = item["screen_code"]
        records.append(record)

    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        jobs = {executor.submit(process_record, record): record for record in records}
        for index, future in enumerate(as_completed(jobs), 1):
            results.append(future.result())
            if index % 20 == 0:
                available = sum(item["status"] == "available" for item in results)
                print(f"processed={index}/{len(records)} available={available}", flush=True)

    results.sort(key=lambda item: item["record_id"])
    fields = [
        "record_id", "status", "source", "title", "doi", "pmid", "pmcid",
        "screen_code", "raw_path", "text_path", "text_chars", "url", "landing_url",
        "retrieved",
    ]
    with (OUT / "manifest.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: item.get(field, "") for field in fields} for item in results)
    summary = {
        "retained": len(results),
        "full_text_available": sum(item["status"] == "available" for item in results),
        "full_text_unavailable": sum(item["status"] != "available" for item in results),
        "sources": {},
        "retrieved": TODAY,
    }
    for source in sorted({item["source"] or "unavailable" for item in results}):
        summary["sources"][source] = sum((item["source"] or "unavailable") == source for item in results)
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
