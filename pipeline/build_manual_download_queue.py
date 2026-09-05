#!/usr/bin/env python3
"""Build the manual full-text download queue with links and citations."""

from __future__ import annotations

import argparse
import csv
import json
import urllib.parse
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
MANUAL_QUEUE = ROOT / "scale/protocol-2.0/fulltext-retrieval-v2/MANUAL_QUEUE.tsv"
RETRIEVAL_QUEUE = ROOT / "scale/protocol-2.0/fulltext-retrieval-v2/QUEUE.tsv"
OPENALEX = ROOT / "scale/protocol-2.0/openalex-discovery.jsonl"
OUTPUT = ROOT / "scale/protocol-2.0/fulltext-retrieval-v2/MANUAL_DOWNLOAD_QUEUE.csv"
CITATION_SNAPSHOT_DATE = "2026-08-04"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_openalex(path: Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_id: dict[str, dict[str, Any]] = {}
    by_doi: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            value = json.loads(line)
            by_id[value["openalex_id"]] = value
            doi = str(value.get("doi") or "").casefold()
            if doi:
                by_doi[doi] = value
    return by_id, by_doi


def scholar_url(doi: str, title: str) -> str:
    query = f'"{doi}"' if doi else f'"{title}"'
    return "https://scholar.google.com/scholar?q=" + urllib.parse.quote_plus(query)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manual-queue", type=Path, default=MANUAL_QUEUE)
    parser.add_argument("--retrieval-queue", type=Path, default=RETRIEVAL_QUEUE)
    parser.add_argument("--openalex", type=Path, default=OPENALEX)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--citation-snapshot-date", default=CITATION_SNAPSHOT_DATE)
    args = parser.parse_args()

    manual_rows = read_tsv(args.manual_queue)
    queue = {row["record_id"]: row for row in read_tsv(args.retrieval_queue)}
    by_openalex_id, by_doi = read_openalex(args.openalex)
    output_rows: list[dict[str, str | int]] = []

    for row in manual_rows:
        record_id = row["record_id"]
        queued = queue[record_id]
        openalex_ids = [value for value in queued["openalex_ids"].split(";") if value]
        matches = [by_openalex_id[value] for value in openalex_ids if value in by_openalex_id]
        doi = row["doi"].casefold()
        if not matches and doi in by_doi:
            matches = [by_doi[doi]]
        citation_status = "EXACT_OPENALEX_MATCH" if matches else "MANUAL_LOOKUP"
        if len(matches) > 1:
            exact = [value for value in matches if str(value.get("doi") or "").casefold() == doi]
            if exact:
                matches = exact
            if len(matches) > 1 and not doi:
                raise ValueError(f"Ambiguous OpenAlex match for {record_id}")
            matches.sort(
                key=lambda value: (int(value.get("cited_by_count") or 0), value["openalex_id"]),
                reverse=True,
            )
            citation_status = "DUPLICATE_OPENALEX_RECORDS_MAX"
        openalex = matches[0] if matches else None
        openalex_id = str(openalex.get("openalex_id") or "") if openalex else ""
        citation_count = openalex.get("cited_by_count") if openalex else ""
        publisher_url = str(openalex.get("primary_landing_page_url") or "") if openalex else ""
        if not publisher_url:
            publisher_url = row["landing_url"]
        pmid = queued["pmid"]
        output_rows.append(
            {
                "record_id": record_id,
                "title": row["title"],
                "year": row["year"],
                "doi": row["doi"],
                "doi_url": row["doi_url"],
                "publisher_url": publisher_url,
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                "openalex_url": f"https://openalex.org/{openalex_id}" if openalex_id else "",
                "openalex_citation_count": citation_count,
                "citation_snapshot_date": args.citation_snapshot_date if openalex else "",
                "citation_status": citation_status,
                "google_scholar_url": scholar_url(row["doi"], row["title"]),
                "expected_filename": f"{record_id}.pdf",
            }
        )

    if not output_rows:
        raise ValueError("The manual queue is empty")
    ids = [str(row["record_id"]) for row in output_rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate record ID in manual queue")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]))
        writer.writeheader()
        writer.writerows(output_rows)

    matched = sum(row["citation_status"] != "MANUAL_LOOKUP" for row in output_rows)
    print(f"records={len(output_rows)}")
    print(f"citations={matched}")
    print(f"manual_citation_lookup={len(output_rows) - matched}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
