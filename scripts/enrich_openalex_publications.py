#!/usr/bin/env python3
"""Fetch DOI-matched OpenAlex citation and authorship data for publications."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


OPENALEX_WORKS = "https://api.openalex.org/works"
CONTACT = "pschneider@abundanceds.com"
SELECT = ",".join(
    (
        "id",
        "doi",
        "title",
        "publication_year",
        "cited_by_count",
        "counts_by_year",
        "updated_date",
        "authorships",
        "abstract_inverted_index",
        "biblio",
        "language",
        "primary_location",
        "type_crossref",
    )
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--database", type=Path)
    source.add_argument(
        "--manifest",
        type=Path,
        help="prepared manifest with a verified metadata_path for each publication",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review-output", type=Path, required=True)
    parser.add_argument("--summary-output", type=Path, required=True)
    parser.add_argument("--delay", type=float, default=0.15)
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reconstruct_abstract(index: dict[str, list[int]] | None) -> str | None:
    if not index:
        return None
    positions = [
        (position, word)
        for word, values in index.items()
        for position in values
    ]
    if not positions:
        return None
    return " ".join(word for _, word in sorted(positions))


def publications_from_manifest(path: Path) -> list[tuple[str, str | None, str, int | None]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    publications: list[tuple[str, str | None, str, int | None]] = []
    for row in rows:
        metadata_path = Path(row["metadata_path"])
        if not metadata_path.is_absolute():
            metadata_path = Path.cwd() / metadata_path
        if digest(metadata_path) != row["metadata_sha256"]:
            raise ValueError(f"metadata hash mismatch: {row['record_id']}")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        publication = metadata["publication"]
        years = [
            int(match.group())
            for value in (item.get("value", "") for item in metadata.get("dates", []))
            if (match := re.search(r"(?:19|20)\d{2}", value))
        ]
        publications.append(
            (
                publication["publication_id"],
                publication.get("doi"),
                publication["title"],
                min(years) if years else None,
            )
        )
    return publications


def normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    text = value.strip().casefold()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    return text.rstrip(". ,;") or None


def normalize_title(value: str | None) -> str:
    text = (value or "").casefold()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def request_work(doi: str, api_key: str | None) -> tuple[int, dict[str, Any] | None]:
    work_id = urllib.parse.quote(f"doi:{doi}", safe=":")
    query = urllib.parse.urlencode({"select": SELECT, "mailto": CONTACT})
    request = urllib.request.Request(f"{OPENALEX_WORKS}/{work_id}?{query}")
    if api_key:
        request.add_header("Authorization", f"Bearer {api_key}")
    for attempt in range(7):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return error.code, None
            if error.code not in {429, 500, 502, 503, 504}:
                raise
        except (TimeoutError, urllib.error.URLError):
            pass
        time.sleep(min(60, 2**attempt))
    raise RuntimeError(f"OpenAlex request failed after retries: {doi}")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        with temporary.open("w", encoding="utf-8") as output:
            for row in rows:
                output.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    args = parse_args()
    if args.database:
        source = sqlite3.connect(f"file:{args.database.resolve()}?mode=ro", uri=True)
        publications = source.execute(
            """
            SELECT publication_id, doi, title, publication_year
            FROM publication
            ORDER BY publication_id
            """
        ).fetchall()
        source.close()
    else:
        publications = publications_from_manifest(args.manifest.resolve())
    if not publications:
        raise SystemExit("No publications found")

    api_key = os.environ.get("OPENALEX_API_KEY") or None
    retrieved_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    output_rows: list[dict[str, Any]] = []
    status_counts: dict[str, int] = {}
    for index, (publication_id, doi, title, year) in enumerate(publications, 1):
        if not doi:
            scholar_url = "https://scholar.google.com/scholar?" + urllib.parse.urlencode(
                {"q": f'"{title}"'}
            )
            row = {
                "publication_id": publication_id,
                "requested_doi": None,
                "source_title": title,
                "source_year": year,
                "match_status": "NO_DOI",
                "retrieved_at": retrieved_at,
                "google_scholar_url": scholar_url,
            }
        else:
            status, payload = request_work(doi, api_key)
            scholar_url = "https://scholar.google.com/scholar?" + urllib.parse.urlencode(
                {"q": f'"{doi}"'}
            )
            if status == 404 or payload is None:
                row = {
                    "publication_id": publication_id,
                    "requested_doi": doi,
                    "source_title": title,
                    "source_year": year,
                    "match_status": "NOT_FOUND",
                    "retrieved_at": retrieved_at,
                    "google_scholar_url": scholar_url,
                }
            else:
                returned_doi = normalize_doi(payload.get("doi"))
                title_similarity = SequenceMatcher(
                    None, normalize_title(title), normalize_title(payload.get("title"))
                ).ratio()
                returned_year = payload.get("publication_year")
                year_difference = (
                    abs(int(year) - int(returned_year))
                    if year is not None and returned_year is not None
                    else None
                )
                exact = (
                    returned_doi == normalize_doi(doi)
                    and title_similarity >= 0.80
                    and (year_difference is None or year_difference <= 1)
                )
                row = {
                    "publication_id": publication_id,
                    "requested_doi": doi,
                    "source_title": title,
                    "source_year": year,
                    "match_status": "EXACT" if exact else "REVIEW",
                    "openalex_id": (payload.get("id") or "").rsplit("/", 1)[-1] or None,
                    "openalex_doi": returned_doi,
                    "openalex_title": payload.get("title"),
                    "openalex_year": returned_year,
                    "title_similarity": round(title_similarity, 6),
                    "year_difference": year_difference,
                    "cited_by_count": payload.get("cited_by_count"),
                    "counts_by_year": payload.get("counts_by_year") or [],
                    "openalex_updated_date": payload.get("updated_date"),
                    "authorships": payload.get("authorships") or [],
                    "abstract": reconstruct_abstract(payload.get("abstract_inverted_index")),
                    "biblio": payload.get("biblio") or {},
                    "language": payload.get("language"),
                    "primary_location": payload.get("primary_location") or {},
                    "type_crossref": payload.get("type_crossref"),
                    "retrieved_at": retrieved_at,
                    "google_scholar_url": scholar_url,
                }
        output_rows.append(row)
        status_counts[row["match_status"]] = status_counts.get(row["match_status"], 0) + 1
        if index % 25 == 0 or index == len(publications):
            print(f"{index}/{len(publications)} OpenAlex records", flush=True)
        time.sleep(args.delay)

    write_jsonl(args.output, output_rows)
    review_rows = [row for row in output_rows if row["match_status"] != "EXACT"]
    args.review_output.parent.mkdir(parents=True, exist_ok=True)
    fields = (
        "publication_id",
        "requested_doi",
        "source_title",
        "source_year",
        "match_status",
        "openalex_id",
        "openalex_doi",
        "openalex_title",
        "openalex_year",
        "title_similarity",
        "year_difference",
        "google_scholar_url",
    )
    with args.review_output.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(review_rows)
    summary = {
        "publications": len(publications),
        "retrieved_at": retrieved_at,
        "status_counts": dict(sorted(status_counts.items())),
        "review_rows": len(review_rows),
        "api_key_used": bool(api_key),
    }
    args.summary_output.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
