#!/usr/bin/env python3
"""Retrieve and verify the full-text eligibility pilot sample."""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parent.parent
PILOT = ROOT / "scale" / "protocol-2.0" / "fulltext-pilot-v1"
DOCUMENTS = PILOT / "documents"
MAX_BYTES = 80 * 1024 * 1024
MAX_WORKERS = 4
USER_AGENT = "eq-graph-fulltext-pilot/1.0 (mailto:pschneider@abundanceds.com)"
EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
EPMC_XML = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"


def read_queue() -> list[dict[str, str]]:
    with (PILOT / "CANDIDATE_QUEUE.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize_doi(value: str | None) -> str:
    value = (value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", value)


def verify_document(data: bytes, expected: str) -> str:
    if len(data) < 500:
        raise ValueError("document is shorter than 500 bytes")
    if expected == "pdf":
        if not data.lstrip().startswith(b"%PDF-"):
            raise ValueError("response is not a PDF")
        return "pdf"
    root = ET.fromstring(data)
    if root.tag.rsplit("}", 1)[-1] != "article":
        raise ValueError("XML root is not a JATS article")
    return "xml"


def fetch_bytes(session: requests.Session, url: str, expected: str) -> tuple[bytes, str]:
    response = session.get(
        url,
        headers={"Accept": "application/pdf" if expected == "pdf" else "application/xml"},
        timeout=120,
        stream=True,
    )
    response.raise_for_status()
    chunks: list[bytes] = []
    size = 0
    for chunk in response.iter_content(65536):
        size += len(chunk)
        if size > MAX_BYTES:
            raise ValueError(f"document exceeds {MAX_BYTES} bytes")
        chunks.append(chunk)
    data = b"".join(chunks)
    verify_document(data, expected)
    return data, response.url


def exact_epmc_match(session: requests.Session, row: dict[str, str]) -> dict:
    doi = normalize_doi(row["doi"])
    pmid = row["pmid"]
    if not doi and not pmid:
        return {}
    terms = []
    if doi:
        terms.append(f'DOI:"{doi}"')
    if pmid:
        terms.append(f"(EXT_ID:{pmid} AND SRC:MED)")
    query = " OR ".join(terms)
    response = session.get(
        EPMC_SEARCH,
        params={"query": query, "format": "json", "resultType": "core", "pageSize": 10},
        timeout=60,
    )
    response.raise_for_status()
    matches = []
    for item in response.json().get("resultList", {}).get("result", []):
        doi_match = doi and normalize_doi(item.get("doi")) == doi
        pmid_match = pmid and str(item.get("pmid") or "") == pmid
        if doi_match or pmid_match:
            matches.append(item)
    return max(matches, key=lambda item: bool(item.get("pmcid")), default={})


def ordered_pdf_sources(row: dict[str, str]) -> list[dict[str, str]]:
    locations = json.loads(row["candidate_urls_json"] or "[]")
    order = {"repository": 0, "journal": 1}
    locations.sort(
        key=lambda item: (
            order.get(item.get("host_type") or "", 2),
            item.get("origin") or "",
            item.get("url") or "",
        )
    )
    output = []
    seen = set()
    for item in locations:
        url = item.get("url") or ""
        if url and url not in seen:
            seen.add(url)
            output.append(item)
    return output


def prior_result(record_id: str) -> dict | None:
    path = DOCUMENTS / f"{record_id}.source.json"
    if not path.exists():
        return None
    result = json.loads(path.read_text(encoding="utf-8"))
    document = ROOT / result["raw_path"]
    if not document.exists():
        return None
    data = document.read_bytes()
    verify_document(data, result["format"])
    if hashlib.sha256(data).hexdigest() != result["sha256"]:
        raise ValueError(f"Stored hash mismatch for {record_id}.")
    result["status"] = "REUSED"
    return result


def process(row: dict[str, str]) -> dict:
    record_id = row["record_id"]
    existing = prior_result(record_id)
    if existing:
        return {**row, **existing}

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    attempts: list[dict[str, str]] = []
    result = {
        **row,
        "status": "FAILED",
        "format": "",
        "source_method": "",
        "source_url": "",
        "final_url": "",
        "license": "",
        "raw_path": "",
        "bytes": "",
        "sha256": "",
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "attempts_json": "[]",
    }

    sources = ordered_pdf_sources(row)
    for source in sources:
        url = source["url"]
        attempt = {"method": "pdf", "url": url, "error": ""}
        try:
            data, final_url = fetch_bytes(session, url, "pdf")
        except Exception as exc:  # The ledger must retain each failed source.
            attempt["error"] = f"{type(exc).__name__}: {str(exc)[:240]}"
            attempts.append(attempt)
            continue
        path = DOCUMENTS / f"{record_id}.pdf"
        path.write_bytes(data)
        result.update(
            {
                "status": "DOWNLOADED",
                "format": "pdf",
                "source_method": f"{source.get('origin') or 'indexed'}_pdf",
                "source_url": url,
                "final_url": final_url,
                "license": source.get("license") or "",
                "raw_path": str(path.relative_to(ROOT)),
                "bytes": str(len(data)),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
        attempts.append(attempt)
        break

    if result["status"] == "FAILED":
        pmcid = row["pmcid"]
        epmc = {}
        if not pmcid:
            try:
                epmc = exact_epmc_match(session, row)
                pmcid = str(epmc.get("pmcid") or "")
            except Exception as exc:
                attempts.append(
                    {
                        "method": "europe_pmc_lookup",
                        "url": EPMC_SEARCH,
                        "error": f"{type(exc).__name__}: {str(exc)[:240]}",
                    }
                )
        if pmcid:
            url = EPMC_XML.format(pmcid=pmcid)
            attempt = {"method": "jats", "url": url, "error": ""}
            try:
                data, final_url = fetch_bytes(session, url, "xml")
                path = DOCUMENTS / f"{record_id}.xml"
                path.write_bytes(data)
                result.update(
                    {
                        "status": "DOWNLOADED",
                        "format": "xml",
                        "source_method": "europe_pmc_jats",
                        "source_url": url,
                        "final_url": final_url,
                        "license": str(epmc.get("license") or ""),
                        "raw_path": str(path.relative_to(ROOT)),
                        "bytes": str(len(data)),
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "pmcid": pmcid,
                    }
                )
            except Exception as exc:
                attempt["error"] = f"{type(exc).__name__}: {str(exc)[:240]}"
            attempts.append(attempt)

    result["attempts_json"] = json.dumps(
        attempts, ensure_ascii=False, separators=(",", ":")
    )
    if result["status"] == "DOWNLOADED":
        provenance = {
            key: result[key]
            for key in (
                "record_id",
                "status",
                "format",
                "source_method",
                "source_url",
                "final_url",
                "license",
                "raw_path",
                "bytes",
                "sha256",
                "retrieved_at",
                "attempts_json",
            )
        }
        (DOCUMENTS / f"{record_id}.source.json").write_text(
            json.dumps(provenance, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return result


def run_group(
    rows: list[dict[str, str]], quota: int, parser_failures: set[str]
) -> list[dict]:
    results: list[dict] = []
    for start in range(0, len(rows), MAX_WORKERS):
        batch = rows[start : start + MAX_WORKERS]
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            jobs = {executor.submit(process, row): row for row in batch}
            for future in as_completed(jobs):
                results.append(future.result())
        successes = sorted(
            (
                row
                for row in results
                if row["status"] in {"DOWNLOADED", "REUSED"}
                and row["record_id"] not in parser_failures
            ),
            key=lambda row: int(row["reserve_rank"]),
        )
        print(
            f"{rows[0]['sample_group']}: tried={len(results)} available={len(successes)}/{quota}",
            flush=True,
        )
        if len(successes) >= quota:
            break
    return results


def main() -> None:
    DOCUMENTS.mkdir(parents=True, exist_ok=True)
    queue = read_queue()
    parser_failure_file = PILOT / "PARSER_FAILURES.tsv"
    source_exclusion_file = PILOT / "SOURCE_EXCLUSIONS.tsv"
    parser_failures = set()
    if parser_failure_file.exists():
        with parser_failure_file.open(encoding="utf-8", newline="") as handle:
            parser_failures = {
                row["record_id"]
                for row in csv.DictReader(handle, delimiter="\t")
            }
    source_exclusions = set()
    if source_exclusion_file.exists():
        with source_exclusion_file.open(encoding="utf-8", newline="") as handle:
            source_exclusions = {
                row["record_id"]
                for row in csv.DictReader(handle, delimiter="\t")
            }
    disqualified = parser_failures | source_exclusions
    groups = []
    for name in dict.fromkeys(row["sample_group"] for row in queue):
        rows = [row for row in queue if row["sample_group"] == name]
        rows.sort(key=lambda row: int(row["reserve_rank"]))
        groups.append((name, rows, int(rows[0]["final_quota"])))

    attempted: list[dict] = []
    selected: list[dict] = []
    for _, rows, quota in groups:
        results = run_group(rows, quota, disqualified)
        attempted.extend(results)
        available = sorted(
            (
                row
                for row in results
                if row["status"] in {"DOWNLOADED", "REUSED"}
                and row["record_id"] not in disqualified
            ),
            key=lambda row: int(row["reserve_rank"]),
        )
        selected.extend(available[:quota])

    for row in attempted:
        if row["record_id"] in parser_failures:
            row["status"] = "PARSER_FAILED"
        elif row["record_id"] in source_exclusions:
            row["status"] = "SOURCE_EXCLUDED"

    attempted_ids = {row["record_id"] for row in attempted}
    for row in queue:
        if row["record_id"] not in attempted_ids:
            attempted.append(
                {
                    **row,
                    "status": "NOT_NEEDED",
                    "format": "",
                    "source_method": "",
                    "source_url": "",
                    "final_url": "",
                    "license": "",
                    "raw_path": "",
                    "bytes": "",
                    "sha256": "",
                    "retrieved_at": "",
                    "attempts_json": "[]",
                }
            )
    attempted.sort(key=lambda row: (row["sample_group"], int(row["reserve_rank"])))
    selected.sort(key=lambda row: (row["sample_group"], int(row["reserve_rank"])))

    ledger_fields = list(attempted[0])
    with (PILOT / "RETRIEVAL.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=ledger_fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(attempted)
    manifest_fields = list(selected[0])
    manifest = PILOT / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(selected)

    group_counts = {
        name: sum(row["sample_group"] == name for row in selected)
        for name, _, _ in groups
    }
    target_counts = {name: quota for name, _, quota in groups}
    summary = {
        "target": sum(target_counts.values()),
        "available": len(selected),
        "groups": group_counts,
        "targets": target_counts,
        "formats": {
            kind: sum(row["format"] == kind for row in selected)
            for kind in ("pdf", "xml")
        },
        "attempted": sum(row["status"] != "NOT_NEEDED" for row in attempted),
        "failed": sum(row["status"] == "FAILED" for row in attempted),
        "parser_failed": sorted(parser_failures),
        "source_excluded": sorted(source_exclusions),
        "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
        "policy": (
            "Prefer a verified PDF for this parser-stress pilot. Use Europe PMC JATS "
            "only when PDF retrieval fails. Do not bypass access controls."
        ),
    }
    (PILOT / "RETRIEVAL_SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    if group_counts != target_counts:
        raise SystemExit("The retrieved sample does not meet all quotas.")


if __name__ == "__main__":
    main()
