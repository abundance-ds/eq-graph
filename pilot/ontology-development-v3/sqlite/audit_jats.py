#!/usr/bin/env python3
"""Audit deterministic JATS metadata extraction across the local corpus."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

from jats_metadata import parse_jats


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]


def main() -> None:
    paths = sorted((REPO_ROOT / "input" / "projects").glob("*/papers/*.xml"))
    if len(paths) != 220:
        raise SystemExit(f"Expected 220 JATS files; found {len(paths)}")

    records = []
    failures: list[str] = []
    nondeterministic: list[str] = []
    for path in paths:
        try:
            first = parse_jats(path)
            second = parse_jats(path)
            first_bytes = json.dumps(first, ensure_ascii=False, sort_keys=True).encode("utf-8")
            second_bytes = json.dumps(second, ensure_ascii=False, sort_keys=True).encode("utf-8")
            if hashlib.sha256(first_bytes).digest() != hashlib.sha256(second_bytes).digest():
                nondeterministic.append(str(path.relative_to(REPO_ROOT)))
            records.append(first)
        except Exception as error:
            failures.append(f"{path.relative_to(REPO_ROOT)}: {error}")

    if failures or nondeterministic:
        for failure in failures:
            print(f"FAIL\t{failure}")
        for path in nondeterministic:
            print(f"FAIL\tnondeterministic\t{path}")
        raise SystemExit(1)

    publications = [record["publication"] for record in records]
    doi_counts = Counter(item["doi"] for item in publications)
    metrics = {
        "files": len(records),
        "unique_dois": len(doi_counts),
        "duplicate_file_copies": sum(value - 1 for value in doi_counts.values()),
        "doi": sum(bool(item["doi"]) for item in publications),
        "pmid": sum(bool(item["pmid"]) for item in publications),
        "pmcid": sum(bool(item["pmcid"]) for item in publications),
        "title": sum(bool(item["title"]) for item in publications),
        "journal": sum(bool(item["journal"]) for item in publications),
        "publisher": sum(bool(item["publisher"]) for item in publications),
        "abstract": sum(bool(item["abstract"]) for item in publications),
        "licence_url": sum(bool(item["licence_url"]) for item in publications),
        "authors": sum(len(record["authors"]) for record in records),
        "files_with_orcid": sum(any(author["orcid"] for author in record["authors"]) for record in records),
        "files_with_corresponding_email": sum(any(author["email"] for author in record["authors"]) for record in records),
        "author_role_values": sum(len(author["roles"]) for record in records for author in record["authors"]),
        "affiliations": sum(len(record["affiliations"]) for record in records),
        "correspondence_records": sum(len(record["correspondence"]) for record in records),
        "files_with_correspondence": sum(bool(record["correspondence"]) for record in records),
        "keywords": sum(len(record["keywords"]) for record in records),
        "files_with_keywords": sum(bool(record["keywords"]) for record in records),
        "category_values": sum(len(record["categories"]) for record in records),
        "files_with_categories": sum(bool(record["categories"]) for record in records),
        "funding_records": sum(len(record["funding"]) for record in records),
        "files_with_funding": sum(bool(record["funding"]) for record in records),
        "date_records": sum(len(record["dates"]) for record in records),
        "files_with_multiple_dates": sum(len(record["dates"]) > 1 for record in records),
        "references": sum(len(record["references"]) for record in records),
        "reference_dois": sum(bool(reference["doi"]) for record in records for reference in record["references"]),
        "reference_pmids": sum(bool(reference["pmid"]) for record in records for reference in record["references"]),
    }
    expected_core = {
        "files": 220,
        "unique_dois": 209,
        "duplicate_file_copies": 11,
        "doi": 220,
        "pmid": 220,
        "pmcid": 220,
        "title": 220,
        "journal": 220,
        "publisher": 80,
        "abstract": 219,
        "authors": 1337,
        "author_role_values": 233,
        "affiliations": 1053,
        "licence_url": 211,
        "references": 9890,
        "reference_dois": 8242,
        "reference_pmids": 4411,
    }
    problems = []
    for name, expected in expected_core.items():
        if metrics[name] != expected:
            problems.append(f"{name}: expected {expected}, got {metrics[name]}")

    for name, value in metrics.items():
        print(f"{name}\t{value}")
    print(f"parse_failures\t{len(failures)}")
    print(f"nondeterministic_outputs\t{len(nondeterministic)}")
    if problems:
        for problem in problems:
            print(f"FAIL\t{problem}")
        raise SystemExit(1)
    print("SUMMARY\tPASS")


if __name__ == "__main__":
    main()
