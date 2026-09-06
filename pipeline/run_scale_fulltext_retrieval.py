#!/usr/bin/env python3
"""Build and run the Protocol 2.0 full-text retrieval queue."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import signal
import subprocess
import tempfile
import threading
import time
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import requests

from scale_publication_metadata import load_publications


ROOT = Path(__file__).resolve().parent.parent
SCREEN = ROOT / "scale/protocol-2.0/abstract-screen-v2-codex-r5/results.jsonl"
CORPUS = ROOT / "scale/protocol-2.0/article-corpus.jsonl"
CANONICAL_METADATA = ROOT / "scale/protocol-2.0/source-union.jsonl"
OUTPUT = ROOT / "scale/protocol-2.0/fulltext-retrieval-v2"
OLD_AVAILABILITY = ROOT / "scale/protocol-2.0/fulltext-pilot-v1/AVAILABILITY.tsv"
OLD_RETRIEVAL = ROOT / "scale/protocol-2.0/fulltext-pilot-v1/MANIFEST.tsv"
AUDITED_JATS = (
    ROOT / "pilot/ontology-development-v4/production/release-inputs-v2/MANIFEST.tsv"
)
AUDITED_PDF = (
    ROOT
    / "pilot/ontology-development-v4/production/release-inputs-v2/ADDED_MANIFEST.tsv"
)
EUROPE_PMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
EUROPE_PMC_XML = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
OPENALEX_WORK = "https://api.openalex.org/works/{work_id}"
UNPAYWALL = "https://api.unpaywall.org/v2/{doi}"
CONTACT = "pschneider@abundanceds.com"
USER_AGENT = f"eq-graph-scale-fulltext/2.0 (mailto:{CONTACT})"
MODEL = "gpt-5.6-luna"
MAX_BYTES = 80 * 1024 * 1024
STOP = threading.Event()
AI_LIMIT = threading.Semaphore(2)


IDENTITY_SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": ["MATCH", "NOT_MATCH", "UNCLEAR"]},
        "reason": {"type": "string"},
    },
    "required": ["decision", "reason"],
    "additionalProperties": False,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screen", type=Path, default=SCREEN)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument(
        "--canonical-metadata", type=Path, default=CANONICAL_METADATA
    )
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--record-id", action="append", dest="record_ids")
    parser.add_argument("--retry", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--no-identity-ai", action="store_true")
    parser.add_argument("--identity-model", default=MODEL)
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp"
    )
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalized_doi(value: str | None) -> str:
    text = (value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", text)


def normalized_title(value: str | None) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", (value or "").casefold()))


def title_similarity(expected: str, observed: str) -> float:
    left = normalized_title(expected)
    right = normalized_title(observed)
    if not left or not right:
        return 0.0
    return SequenceMatcher(None, left, right).ratio()


def title_token_coverage(expected: str, text: str) -> float:
    stop = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with"}
    wanted = {
        token for token in normalized_title(expected).split() if token not in stop
    }
    found = set(normalized_title(text).split())
    return len(wanted & found) / len(wanted) if wanted else 0.0


def unique_sources(values: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    output: list[dict[str, str]] = []
    for value in values:
        url = value.get("url") or ""
        if url and url not in seen:
            seen.add(url)
            output.append(value)
    return output


def queue_rows(
    screen_path: Path,
    corpus_path: Path,
    canonical_path: Path,
) -> list[dict[str, Any]]:
    papers = load_publications(corpus_path, canonical_path)
    decisions = [
        row
        for row in load_jsonl(screen_path)
        if row["decision"] == "RETRIEVE_FULL_TEXT"
    ]
    if screen_path.resolve() == SCREEN.resolve() and len(decisions) != 1679:
        raise ValueError(f"Expected 1,679 routed papers, found {len(decisions)}.")
    old = {row["record_id"]: row for row in read_tsv(OLD_AVAILABILITY)}
    rows: list[dict[str, Any]] = []
    for decision in decisions:
        record_id = decision["record_id"]
        paper = papers[record_id]
        prior = old.get(record_id, {})
        candidates: list[dict[str, str]] = []
        if prior.get("candidate_urls_json"):
            candidates.extend(json.loads(prior["candidate_urls_json"]))
        if paper.get("primary_pdf_url"):
            candidates.append(
                {
                    "url": paper["primary_pdf_url"],
                    "origin": "screening_metadata",
                    "license": "",
                    "version": "",
                    "host_type": "",
                }
            )
        candidates = unique_sources(candidates)
        doi = normalized_doi(paper.get("doi"))
        landing = (
            paper.get("primary_landing_page_url")
            or prior.get("landing_url")
            or (f"https://doi.org/{doi}" if doi else "")
        )
        rows.append(
            {
                "record_id": record_id,
                "title": paper.get("title") or "",
                "year": int(paper["year"]),
                "authors": paper.get("authors") or [],
                "doi": doi,
                "pmid": str(paper.get("pmid") or ""),
                "openalex_ids": paper.get("openalex_ids") or [],
                "doi_url": f"https://doi.org/{doi}" if doi else "",
                "landing_url": landing,
                "pmcid": prior.get("pmcid") or "",
                "candidate_urls": candidates,
                "project_ids": decision.get("project_ids") or [],
                "screen_reason": decision.get("reason") or "",
            }
        )
    rows.sort(key=lambda row: (row["year"], row["record_id"]))
    ids = [row["record_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("The queue contains a duplicate record ID.")
    for field in ("doi", "pmid"):
        values = [row[field].casefold() for row in rows if row[field]]
        if len(values) != len(set(values)):
            raise ValueError(f"The queue contains a duplicate {field}.")
    return rows


def write_queue(output: Path, rows: list[dict[str, Any]]) -> tuple[Path, str]:
    output.mkdir(parents=True, exist_ok=True)
    path = output / ".QUEUE.tsv.next"
    fields = [
        "record_id",
        "title",
        "year",
        "doi",
        "pmid",
        "doi_url",
        "landing_url",
        "openalex_ids",
        "project_ids",
        "candidate_urls_json",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    **{field: row.get(field, "") for field in fields},
                    "openalex_ids": ";".join(row["openalex_ids"]),
                    "project_ids": ";".join(row["project_ids"]),
                    "candidate_urls_json": json.dumps(
                        row["candidate_urls"],
                        ensure_ascii=False,
                        separators=(",", ":"),
                    ),
                }
            )
    return path, digest(path)


def load_audited_sources() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    by_doi: dict[str, dict[str, str]] = {}
    by_record: dict[str, dict[str, str]] = {}
    for row in read_tsv(AUDITED_JATS):
        doi = normalized_doi(row.get("paper_id"))
        if doi:
            by_doi[doi] = {
                "path": row["xml_path"],
                "sha256": row["xml_sha256"],
                "format": "xml",
                "method": "audited_local_source",
            }
    for row in read_tsv(AUDITED_PDF):
        doi = normalized_doi(row.get("paper_id"))
        if doi:
            by_doi[doi] = {
                "path": row["pdf_path"],
                "sha256": row["pdf_sha256"],
                "format": "pdf",
                "method": "audited_local_source",
            }
    for row in read_tsv(OLD_RETRIEVAL):
        by_record[row["record_id"]] = {
            "path": row["raw_path"],
            "sha256": row["sha256"],
            "format": row["format"],
            "method": "verified_pilot_source",
        }
    return by_doi, by_record


def jats_identity(data: bytes, row: dict[str, Any]) -> tuple[str, str, str]:
    root = ET.fromstring(data)
    if root.tag.rsplit("}", 1)[-1] != "article":
        return "NOT_MATCH", "The XML root is not an article.", ""
    ids: dict[str, str] = {}
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] != "article-id":
            continue
        kind = node.attrib.get("pub-id-type", "").casefold()
        if node.text:
            ids[kind] = node.text.strip()
    title = ""
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] == "article-title":
            title = " ".join("".join(node.itertext()).split())
            break
    expected_doi = row["doi"]
    expected_pmid = row["pmid"]
    if expected_doi and normalized_doi(ids.get("doi")) == expected_doi:
        return "MATCH", "The JATS DOI matches.", title
    if expected_pmid and ids.get("pmid", "") == expected_pmid:
        return "MATCH", "The JATS PMID matches.", title
    if ids.get("doi") and expected_doi:
        return "NOT_MATCH", f"The JATS DOI is {ids['doi']}.", title
    similarity = title_similarity(row["title"], title)
    if similarity >= 0.92:
        return "MATCH", f"The JATS title matches ({similarity:.2f}).", title
    return "UNCLEAR", f"No exact identifier; title similarity is {similarity:.2f}.", title


def pdf_preview(path: Path) -> str:
    with tempfile.TemporaryDirectory() as temporary:
        target = Path(temporary) / "first-pages.txt"
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "2", "-layout", str(path), str(target)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode or not target.exists():
            return ""
        return target.read_text(encoding="utf-8", errors="replace")[:12000]


def pdf_full_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout[:4_000_000] if result.returncode == 0 else ""


def title_is_ordered_in_text(title: str, text: str) -> bool:
    wanted = normalized_title(title).split()
    if len(wanted) < 6:
        return False
    lines = text.splitlines()
    for index in range(len(lines)):
        available = normalized_title(" ".join(lines[index : index + 5])).split()
        position = 0
        for token in available:
            if position < len(wanted) and token == wanted[position]:
                position += 1
        if position == len(wanted):
            return True
    return False


def author_match(authors: list[str], text: str) -> bool:
    normalized = normalized_title(text)
    for author in authors[:6]:
        parts = normalized_title(author).split()
        if parts and len(parts[-1]) >= 4 and parts[-1] in normalized:
            return True
    return False


def pdf_identity(path: Path, row: dict[str, Any]) -> tuple[str, str, str]:
    preview = pdf_preview(path)
    if len(preview.strip()) < 200:
        return "UNCLEAR", "The PDF has no usable first-page text.", preview
    doi = row["doi"]
    compact_preview = re.sub(r"[\s\u00ad]+", "", preview.casefold())
    if doi and doi.casefold() in compact_preview:
        return "MATCH", "The DOI appears on the first pages.", preview
    coverage = title_token_coverage(row["title"], preview[:5000])
    has_author = author_match(row["authors"], preview[:5000])
    if coverage >= 0.88 and has_author:
        return "MATCH", f"The title and an author match ({coverage:.2f}).", preview
    full_text = pdf_full_text(path)
    if title_is_ordered_in_text(row["title"], full_text):
        return "MATCH", "The complete PDF contains the expected title.", preview
    return (
        "UNCLEAR",
        f"No exact identifier; title coverage is {coverage:.2f} and author match is {has_author}.",
        preview,
    )


def luna_identity(
    args: argparse.Namespace,
    row: dict[str, Any],
    preview: str,
    source_key: str,
) -> tuple[str, str]:
    if args.no_identity_ai:
        return "UNCLEAR", "AI identity review is disabled."
    folder = args.output / "identity-ai" / row["record_id"] / source_key
    final_path = folder / "final.json"
    if final_path.exists():
        value = json.loads(final_path.read_text(encoding="utf-8"))
        return value["decision"], value["reason"]
    folder.mkdir(parents=True, exist_ok=True)
    prompt = (
        "Decide whether the downloaded paper is the expected paper. Minor title or "
        "author formatting differences are acceptable. Return MATCH only when the "
        "identity is clear, NOT_MATCH when it is a different paper, and UNCLEAR "
        "otherwise. Use only the supplied data.\n\n"
        + json.dumps(
            {
                "expected": {
                    "title": row["title"],
                    "authors": row["authors"],
                    "year": row["year"],
                    "doi": row["doi"],
                    "pmid": row["pmid"],
                },
                "downloaded_first_pages": preview[:8000],
            },
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n"
    )
    command = [
        "codex",
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--ignore-rules",
        "--ignore-user-config",
        "-c",
        'web_search="disabled"',
        "-c",
        'model_reasoning_effort="medium"',
        "-m",
        args.identity_model,
        "--output-schema",
        str((args.output / "IDENTITY_SCHEMA.json").resolve()),
        "-o",
        str(final_path.resolve()),
        "-",
    ]
    environment = os.environ.copy()
    environment.pop("OPENAI_API_KEY", None)
    with AI_LIMIT:
        result = subprocess.run(
            command,
            cwd=args.output,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=180,
            env=environment,
        )
    (folder / "stderr.txt").write_text(result.stderr, encoding="utf-8")
    if result.returncode or not final_path.exists():
        return "UNCLEAR", "Luna identity review failed."
    value = json.loads(final_path.read_text(encoding="utf-8"))
    if value.get("decision") not in {"MATCH", "NOT_MATCH", "UNCLEAR"}:
        return "UNCLEAR", "Luna returned an invalid decision."
    return value["decision"], str(value.get("reason") or "")[:400]


def verify_candidate(
    args: argparse.Namespace,
    row: dict[str, Any],
    path: Path,
    format_name: str,
    source_key: str,
) -> tuple[str, str, str]:
    data = path.read_bytes()
    if len(data) < 500:
        return "NOT_MATCH", "The file is shorter than 500 bytes.", ""
    if format_name == "xml":
        decision, reason, preview = jats_identity(data, row)
    elif format_name == "pdf":
        if not data.lstrip().startswith(b"%PDF-"):
            return "NOT_MATCH", "The response is not a PDF.", ""
        decision, reason, preview = pdf_identity(path, row)
    else:
        return "NOT_MATCH", "The file format is unsupported.", ""
    if decision != "UNCLEAR":
        return decision, reason, preview
    ai_decision, ai_reason = luna_identity(args, row, preview, source_key)
    return ai_decision, ai_reason or reason, preview


def request(
    session: requests.Session,
    url: str,
    *,
    params: dict[str, str] | None = None,
    accept: str,
) -> requests.Response:
    last: Exception | None = None
    for attempt in range(4):
        if STOP.is_set():
            raise RuntimeError("Retrieval stopped.")
        try:
            response = session.get(
                url,
                params=params,
                headers={"Accept": accept},
                timeout=90,
                stream=accept != "application/json",
            )
            if response.status_code == 429 or response.status_code >= 500:
                delay = float(response.headers.get("Retry-After") or 2**attempt)
                time.sleep(min(delay, 20))
                continue
            response.raise_for_status()
            return response
        except (requests.RequestException, TimeoutError) as error:
            last = error
            if attempt < 3:
                time.sleep(2**attempt)
    raise RuntimeError(str(last or "Request failed after retries."))


def cached_json(
    session: requests.Session,
    path: Path,
    url: str,
    params: dict[str, str],
) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    response = request(session, url, params=params, accept="application/json")
    value = response.json()
    atomic_json(path, value)
    return value


def epmc_record(session: requests.Session, args: argparse.Namespace, row: dict[str, Any]) -> dict[str, Any]:
    cache = args.output / "api/europe-pmc" / f"{row['record_id']}.json"
    terms = []
    if row["doi"]:
        terms.append(f'DOI:"{row["doi"]}"')
    if row["pmid"]:
        terms.append(f'(EXT_ID:{row["pmid"]} AND SRC:MED)')
    if not terms:
        return {}
    value = cached_json(
        session,
        cache,
        EUROPE_PMC_SEARCH,
        {
            "query": " OR ".join(terms),
            "format": "json",
            "resultType": "core",
            "pageSize": "10",
        },
    )
    matches = []
    for item in value.get("resultList", {}).get("result", []):
        if (
            row["doi"]
            and normalized_doi(item.get("doi")) == row["doi"]
        ) or (row["pmid"] and str(item.get("pmid") or "") == row["pmid"]):
            matches.append(item)
    return max(matches, key=lambda item: bool(item.get("pmcid")), default={})


def network_json_sources(
    session: requests.Session,
    args: argparse.Namespace,
    row: dict[str, Any],
    attempts: list[dict[str, str]],
) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    if row["openalex_ids"]:
        work_id = row["openalex_ids"][0]
        try:
            value = cached_json(
                session,
                args.output / "api/openalex" / f"{row['record_id']}.json",
                OPENALEX_WORK.format(work_id=urllib.parse.quote(work_id, safe="")),
                {"select": "id,doi,best_oa_location,locations", "mailto": CONTACT},
            )
            locations = []
            if value.get("best_oa_location"):
                locations.append(value["best_oa_location"])
            locations.extend(value.get("locations") or [])
            for item in locations:
                if item.get("pdf_url"):
                    sources.append(
                        {
                            "url": item["pdf_url"],
                            "origin": "openalex",
                            "license": item.get("license") or "",
                            "version": item.get("version") or "",
                        }
                    )
        except Exception as error:
            attempts.append(
                {
                    "method": "openalex_lookup",
                    "url": OPENALEX_WORK.format(work_id=work_id),
                    "result": "ERROR",
                    "error": f"{type(error).__name__}: {str(error)[:240]}",
                }
            )
    if row["doi"]:
        try:
            value = cached_json(
                session,
                args.output / "api/unpaywall" / f"{row['record_id']}.json",
                UNPAYWALL.format(doi=urllib.parse.quote(row["doi"], safe="")),
                {"email": CONTACT},
            )
            locations = []
            if value.get("best_oa_location"):
                locations.append(value["best_oa_location"])
            locations.extend(value.get("oa_locations") or [])
            for item in locations:
                if item.get("url_for_pdf"):
                    sources.append(
                        {
                            "url": item["url_for_pdf"],
                            "origin": "unpaywall",
                            "license": item.get("license") or "",
                            "version": item.get("version") or "",
                        }
                    )
        except Exception as error:
            attempts.append(
                {
                    "method": "unpaywall_lookup",
                    "url": UNPAYWALL.format(doi=row["doi"]),
                    "result": "ERROR",
                    "error": f"{type(error).__name__}: {str(error)[:240]}",
                }
            )
    return sources


def download(
    session: requests.Session, url: str, path: Path, accept: str
) -> tuple[str, int]:
    response = request(session, url, accept=accept)
    size = 0
    with path.open("wb") as handle:
        for chunk in response.iter_content(65536):
            size += len(chunk)
            if size > MAX_BYTES:
                raise ValueError(f"The source exceeds {MAX_BYTES} bytes.")
            handle.write(chunk)
    return response.url, size


def record_path(output: Path, row: dict[str, Any]) -> Path:
    return output / "records" / str(row["year"]) / f"{row['record_id']}.json"


def verified_result(
    row: dict[str, Any],
    queue_sha256: str,
    *,
    source_method: str,
    source_url: str,
    final_url: str,
    license_value: str,
    version: str,
    path: Path,
    format_name: str,
    identity_method: str,
    identity_reason: str,
    attempts: list[dict[str, str]],
) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "record_id": row["record_id"],
        "status": "VERIFIED",
        "title": row["title"],
        "year": row["year"],
        "doi": row["doi"],
        "pmid": row["pmid"],
        "doi_url": row["doi_url"],
        "landing_url": row["landing_url"],
        "source_method": source_method,
        "source_url": source_url,
        "final_url": final_url,
        "license": license_value,
        "version": version,
        "format": format_name,
        "source_path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "identity_method": identity_method,
        "identity_reason": identity_reason,
        "project_ids": row["project_ids"],
        "queue_sha256": queue_sha256,
        "attempts": attempts,
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def process_record(
    args: argparse.Namespace,
    row: dict[str, Any],
    queue_sha256: str,
    local_doi: dict[str, dict[str, str]],
    local_record: dict[str, dict[str, str]],
) -> dict[str, Any]:
    target = record_path(args.output, row)
    if target.exists():
        existing = json.loads(target.read_text(encoding="utf-8"))
        if existing.get("queue_sha256") == queue_sha256:
            if existing.get("status") == "VERIFIED" or not args.retry:
                return existing
    attempts: list[dict[str, str]] = []
    local = local_record.get(row["record_id"]) or local_doi.get(row["doi"])
    if local:
        path = ROOT / local["path"]
        if path.is_file() and digest(path) == local["sha256"]:
            result = verified_result(
                row,
                queue_sha256,
                source_method=local["method"],
                source_url="",
                final_url="",
                license_value="",
                version="",
                path=path,
                format_name=local["format"],
                identity_method="audited_manifest",
                identity_reason="The source and DOI were verified in the audited local corpus.",
                attempts=attempts,
            )
            atomic_json(target, result)
            return result
    held_review = args.output / "identity-review" / f"{row['record_id']}.pdf"
    if held_review.is_file():
        decision, reason, _ = verify_candidate(
            args, row, held_review, "pdf", "held-review"
        )
        attempts.append(
            {
                "method": "held_identity_review",
                "url": "",
                "result": decision,
                "error": "",
            }
        )
        if decision == "MATCH":
            destination = args.output / "documents" / f"{row['record_id']}.pdf"
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(held_review, destination)
            result = verified_result(
                row,
                queue_sha256,
                source_method="held_identity_review",
                source_url="",
                final_url="",
                license_value="",
                version="",
                path=destination,
                format_name="pdf",
                identity_method="full_pdf_title",
                identity_reason=reason,
                attempts=attempts,
            )
            atomic_json(target, result)
            return result
    manual = next(
        (
            path
            for suffix in ("xml", "pdf")
            if (path := args.output / "manual" / f"{row['record_id']}.{suffix}").is_file()
        ),
        None,
    )
    if manual:
        format_name = manual.suffix.lstrip(".")
        decision, reason, _ = verify_candidate(
            args, row, manual, format_name, "manual"
        )
        attempts.append({"method": "manual", "url": "", "result": decision, "error": ""})
        if decision == "MATCH":
            result = verified_result(
                row,
                queue_sha256,
                source_method="manual_import",
                source_url=row["landing_url"],
                final_url="",
                license_value="",
                version="",
                path=manual,
                format_name=format_name,
                identity_method="luna_or_metadata",
                identity_reason=reason,
                attempts=attempts,
            )
            atomic_json(target, result)
            return result
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    documents = args.output / "documents"
    documents.mkdir(parents=True, exist_ok=True)
    review_candidate: dict[str, str] | None = None
    with tempfile.TemporaryDirectory(dir=args.output) as temporary:
        temp = Path(temporary)
        try:
            epmc = epmc_record(session, args, row)
        except Exception as error:  # The attempt log preserves the failure.
            epmc = {}
            attempts.append(
                {
                    "method": "europe_pmc_lookup",
                    "url": EUROPE_PMC_SEARCH,
                    "result": "ERROR",
                    "error": f"{type(error).__name__}: {str(error)[:240]}",
                }
            )
        pmcid = str(epmc.get("pmcid") or row.get("pmcid") or "")
        if pmcid:
            url = EUROPE_PMC_XML.format(pmcid=pmcid)
            source = temp / f"{row['record_id']}.xml"
            try:
                final_url, _ = download(session, url, source, "application/xml")
                decision, reason, _ = verify_candidate(
                    args, row, source, "xml", f"epmc-{pmcid}"
                )
                attempts.append(
                    {"method": "europe_pmc_jats", "url": url, "result": decision, "error": ""}
                )
                if decision == "MATCH":
                    destination = documents / f"{row['record_id']}.xml"
                    os.replace(source, destination)
                    result = verified_result(
                        row,
                        queue_sha256,
                        source_method="europe_pmc_jats",
                        source_url=url,
                        final_url=final_url,
                        license_value=str(epmc.get("license") or ""),
                        version="publishedVersion",
                        path=destination,
                        format_name="xml",
                        identity_method="jats_metadata_or_luna",
                        identity_reason=reason,
                        attempts=attempts,
                    )
                    atomic_json(target, result)
                    return result
            except Exception as error:
                attempts.append(
                    {
                        "method": "europe_pmc_jats",
                        "url": url,
                        "result": "ERROR",
                        "error": f"{type(error).__name__}: {str(error)[:240]}",
                    }
                )
        candidates = list(row["candidate_urls"])
        candidates.extend(network_json_sources(session, args, row, attempts))
        candidates = unique_sources(candidates)[:12]
        for index, candidate in enumerate(candidates, 1):
            url = candidate["url"]
            source = temp / f"{row['record_id']}-{index}.pdf"
            try:
                final_url, _ = download(session, url, source, "application/pdf")
                decision, reason, _ = verify_candidate(
                    args,
                    row,
                    source,
                    "pdf",
                    hashlib.sha256(url.encode("utf-8")).hexdigest()[:12],
                )
                attempts.append(
                    {
                        "method": f"{candidate.get('origin') or 'indexed'}_pdf",
                        "url": url,
                        "result": decision,
                        "error": "",
                    }
                )
                if decision == "MATCH":
                    destination = documents / f"{row['record_id']}.pdf"
                    os.replace(source, destination)
                    result = verified_result(
                        row,
                        queue_sha256,
                        source_method=f"{candidate.get('origin') or 'indexed'}_pdf",
                        source_url=url,
                        final_url=final_url,
                        license_value=candidate.get("license") or "",
                        version=candidate.get("version") or "",
                        path=destination,
                        format_name="pdf",
                        identity_method="pdf_metadata_or_luna",
                        identity_reason=reason,
                        attempts=attempts,
                    )
                    atomic_json(target, result)
                    return result
                if decision == "UNCLEAR" and review_candidate is None:
                    review = args.output / "identity-review" / f"{row['record_id']}.pdf"
                    review.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(source, review)
                    review_candidate = {
                        "path": str(review.relative_to(ROOT)),
                        "url": url,
                        "reason": reason,
                    }
            except Exception as error:
                attempts.append(
                    {
                        "method": f"{candidate.get('origin') or 'indexed'}_pdf",
                        "url": url,
                        "result": "ERROR",
                        "error": f"{type(error).__name__}: {str(error)[:240]}",
                    }
                )
    status = "IDENTITY_REVIEW" if review_candidate else "MANUAL_REQUIRED"
    result = {
        "record_id": row["record_id"],
        "status": status,
        "title": row["title"],
        "year": row["year"],
        "doi": row["doi"],
        "pmid": row["pmid"],
        "doi_url": row["doi_url"],
        "landing_url": row["landing_url"],
        "project_ids": row["project_ids"],
        "queue_sha256": queue_sha256,
        "review_candidate": review_candidate,
        "attempts": attempts,
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    atomic_json(target, result)
    return result


def compile_results(output: Path, rows: list[dict[str, Any]], queue_sha256: str) -> dict[str, Any]:
    values = []
    for row in rows:
        path = record_path(output, row)
        if not path.exists():
            continue
        value = json.loads(path.read_text(encoding="utf-8"))
        if value.get("queue_sha256") != queue_sha256:
            raise ValueError(f"Stale retrieval result: {path}")
        if value.get("status") == "VERIFIED":
            source = ROOT / value["source_path"]
            if not source.is_file():
                raise ValueError(f"Missing verified source: {source}")
            data = source.read_bytes()
            if len(data) != value["bytes"] or hashlib.sha256(data).hexdigest() != value["sha256"]:
                raise ValueError(f"Verified source changed: {source}")
            if value["format"] == "pdf" and not data.lstrip().startswith(b"%PDF-"):
                raise ValueError(f"Invalid verified PDF: {source}")
            if value["format"] == "xml":
                try:
                    if ET.fromstring(data).tag.rsplit("}", 1)[-1] != "article":
                        raise ValueError(f"Invalid verified JATS root: {source}")
                except ET.ParseError as error:
                    raise ValueError(f"Invalid verified XML: {source}") from error
        elif value.get("status") == "IDENTITY_REVIEW":
            candidate = value.get("review_candidate") or {}
            review_path = ROOT / str(candidate.get("path") or "")
            if not review_path.is_file():
                raise ValueError(f"Missing identity-review source: {review_path}")
        values.append(value)
    values.sort(key=lambda value: (value["year"], value["record_id"]))
    fields = [
        "record_id",
        "status",
        "title",
        "year",
        "doi",
        "pmid",
        "doi_url",
        "landing_url",
        "source_method",
        "source_url",
        "source_path",
        "format",
        "bytes",
        "sha256",
        "identity_method",
        "identity_reason",
    ]
    with (output / "RESULTS.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows({field: value.get(field, "") for field in fields} for value in values)
    for status, name in (
        ("MANUAL_REQUIRED", "MANUAL_QUEUE.tsv"),
        ("IDENTITY_REVIEW", "IDENTITY_REVIEW.tsv"),
    ):
        selected = [value for value in values if value["status"] == status]
        with (output / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["record_id", "title", "year", "doi", "doi_url", "landing_url"],
                delimiter="\t",
            )
            writer.writeheader()
            writer.writerows(
                {key: value.get(key, "") for key in writer.fieldnames}
                for value in selected
            )
    counts = Counter(value["status"] for value in values)
    summary = {
        "queue": len(rows),
        "completed": len(values),
        "remaining": len(rows) - len(values),
        "status": dict(sorted(counts.items())),
        "verified_formats": dict(
            sorted(
                Counter(
                    value["format"]
                    for value in values
                    if value["status"] == "VERIFIED"
                ).items()
            )
        ),
        "queue_sha256": queue_sha256,
        "results_sha256": digest(output / "RESULTS.tsv"),
    }
    atomic_json(output / "SUMMARY.json", summary)
    return summary


def main() -> int:
    args = parse_args()
    if args.workers < 1:
        raise ValueError("workers must be positive")
    rows = queue_rows(args.screen, args.corpus, args.canonical_metadata)
    staged_queue, queue_sha256 = write_queue(args.output, rows)
    queue_path = args.output / "QUEUE.tsv"
    atomic_json(args.output / "IDENTITY_SCHEMA.json", IDENTITY_SCHEMA)
    manifest = {
        "version": "2.0",
        "records": len(rows),
        "screen_path": str(args.screen),
        "screen_sha256": digest(args.screen),
        "corpus_path": str(args.corpus),
        "corpus_sha256": digest(args.corpus),
        "canonical_metadata_path": str(args.canonical_metadata),
        "canonical_metadata_sha256": digest(args.canonical_metadata),
        "queue_path": str(queue_path),
        "queue_sha256": queue_sha256,
        "identity_model": args.identity_model,
        "identity_ai_authentication": "Codex ChatGPT subscription; OPENAI_API_KEY removed",
        "runner_sha256": digest(Path(__file__)),
    }
    manifest_path = args.output / "MANIFEST.json"
    if manifest_path.exists() and any((args.output / "records").rglob("*.json")):
        prior = json.loads(manifest_path.read_text(encoding="utf-8"))
        if prior.get("queue_sha256") != queue_sha256:
            staged_queue.unlink(missing_ok=True)
            raise ValueError(
                "The frozen queue changed after retrieval began. Use a new output directory."
            )
    os.replace(staged_queue, queue_path)
    atomic_json(manifest_path, manifest)
    summary = compile_results(args.output, rows, queue_sha256)
    if not args.execute:
        print(json.dumps(summary, indent=2))
        return 0
    selected = rows
    if args.record_ids:
        wanted = set(args.record_ids)
        if wanted - {row["record_id"] for row in rows}:
            raise ValueError("A requested record is outside the queue.")
        selected = [row for row in rows if row["record_id"] in wanted]
    if args.limit is not None:
        selected = sorted(
            selected,
            key=lambda row: hashlib.sha256(row["record_id"].encode("utf-8")).hexdigest(),
        )[: args.limit]
    local_doi, local_record = load_audited_sources()
    counts: Counter[str] = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                process_record,
                args,
                row,
                queue_sha256,
                local_doi,
                local_record,
            ): row
            for row in selected
        }
        for index, future in enumerate(as_completed(futures), 1):
            value = future.result()
            counts[value["status"]] += 1
            if index % 10 == 0 or index == len(futures):
                print(
                    f"processed={index}/{len(futures)} status={dict(counts)}",
                    flush=True,
                )
    summary = compile_results(args.output, rows, queue_sha256)
    print(json.dumps(summary, indent=2))
    return 0


def stop(signum: int, frame: Any) -> None:  # noqa: ARG001
    STOP.set()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    raise SystemExit(main())
