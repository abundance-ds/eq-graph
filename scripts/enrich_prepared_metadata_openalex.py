#!/usr/bin/env python3
"""Add exact OpenAlex metadata to prepared publication records."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--openalex", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(value: str | None) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).split())


def normalized_orcid(value: str | None) -> str | None:
    text = (value or "").strip().casefold().replace("https://orcid.org/", "")
    return text or None


def author_order_is_safe(
    source_authors: list[dict[str, Any]],
    openalex_authors: list[dict[str, Any]],
) -> bool:
    if len(source_authors) != len(openalex_authors):
        return False
    for source, authorship in zip(source_authors, openalex_authors, strict=True):
        family = normalize(source.get("family_name"))
        author = authorship.get("author") or {}
        candidate = normalize(author.get("display_name") or authorship.get("raw_author_name"))
        if family and family not in candidate:
            return False
    return True


def affiliation_id(institution: dict[str, Any]) -> str:
    openalex_id = (institution.get("id") or "").rsplit("/", 1)[-1]
    if openalex_id:
        return f"aff:openalex:{openalex_id}"
    key = normalize(institution.get("display_name"))
    return "aff:local:" + hashlib.sha256(key.encode()).hexdigest()[:16]


def enrich(metadata: dict[str, Any], row: dict[str, Any]) -> tuple[dict[str, Any], str]:
    publication = metadata["publication"]
    source_path = Path(publication.get("source_path") or "")
    if source_path.is_absolute() and source_path.is_relative_to(Path.cwd()):
        publication["source_path"] = str(source_path.relative_to(Path.cwd()))
    if row.get("match_status") != "EXACT":
        return metadata, "NO_EXACT_OPENALEX_MATCH"

    publication["abstract"] = publication.get("abstract") or row.get("abstract")
    publication["language"] = publication.get("language") or row.get("language")
    publication["article_type"] = publication.get("article_type") or row.get("type_crossref")
    biblio = row.get("biblio") or {}
    publication["volume"] = publication.get("volume") or biblio.get("volume")
    publication["issue"] = publication.get("issue") or biblio.get("issue")
    location = row.get("primary_location") or {}
    source = location.get("source") or {}
    publication["journal"] = publication.get("journal") or source.get("display_name")
    publication["openalex_id"] = row.get("openalex_id")
    publication["metadata_status"] = "project-discovery-plus-openalex-exact"
    publication["openalex_retrieved_at"] = row.get("retrieved_at")

    urls = {(item["type"], item["url"]) for item in metadata.get("urls", [])}
    for url_type, url in (
        ("landing", location.get("landing_page_url")),
        ("full-text-pdf", location.get("pdf_url")),
    ):
        if url and (url_type, url) not in urls:
            metadata.setdefault("urls", []).append({"type": url_type, "url": url})
            urls.add((url_type, url))

    source_authors = metadata.get("authors", [])
    openalex_authors = row.get("authorships") or []
    if not author_order_is_safe(source_authors, openalex_authors):
        publication["author_enrichment_status"] = "REVIEW"
        return metadata, "AUTHOR_ORDER_REVIEW"

    affiliations = {item["id"]: item for item in metadata.get("affiliations", [])}
    for source_author, authorship in zip(source_authors, openalex_authors, strict=True):
        author = authorship.get("author") or {}
        openalex_name = author.get("display_name") or authorship.get("raw_author_name")
        if not source_author.get("display_name") and openalex_name:
            source_author["display_name"] = openalex_name
            source_author["family_name"] = None
            source_author["given_names"] = openalex_name
        source_author["openalex_id"] = (author.get("id") or "").rsplit("/", 1)[-1] or None
        source_author["openalex_name"] = openalex_name
        source_author["orcid"] = source_author.get("orcid") or normalized_orcid(author.get("orcid"))
        linked_affiliations: list[str] = []
        for institution in authorship.get("institutions") or []:
            item_id = affiliation_id(institution)
            affiliations.setdefault(
                item_id,
                {
                    "id": item_id,
                    "name": institution.get("display_name"),
                    "ror": institution.get("ror"),
                    "country_code": institution.get("country_code"),
                    "source": "OpenAlex exact DOI match",
                },
            )
            linked_affiliations.append(item_id)
        if linked_affiliations:
            source_author["affiliation_ids"] = linked_affiliations
    metadata["affiliations"] = list(affiliations.values())
    publication["author_enrichment_status"] = "EXACT_ORDER_AND_SURNAME"
    return metadata, "ENRICHED"


def main() -> None:
    args = parse_args()
    output = args.output_directory.resolve()
    metadata_output = output / "metadata"
    metadata_output.mkdir(parents=True, exist_ok=True)

    openalex = {
        row["publication_id"]: row
        for row in (
            json.loads(line)
            for line in args.openalex.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }
    with args.manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    output_rows: list[dict[str, str]] = []
    status_counts: dict[str, int] = {}
    for row in rows:
        source_path = Path(row["metadata_path"])
        if not source_path.is_absolute():
            source_path = Path.cwd() / source_path
        if digest(source_path) != row["metadata_sha256"]:
            raise ValueError(f"metadata hash mismatch: {row['record_id']}")
        metadata = json.loads(source_path.read_text(encoding="utf-8"))
        publication_id = metadata["publication"]["publication_id"]
        metadata, status = enrich(metadata, openalex.get(publication_id, {}))
        status_counts[status] = status_counts.get(status, 0) + 1
        target = metadata_output / f"{row['record_id']}.json"
        target.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        output_rows.append(
            {
                **row,
                "metadata_path": str(target.relative_to(Path.cwd())),
                "metadata_sha256": digest(target),
                "metadata_enrichment": status,
            }
        )

    manifest = output / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(output_rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(output_rows)
    summary = {
        "records": len(output_rows),
        "status_counts": dict(sorted(status_counts.items())),
        "manifest_sha256": digest(manifest),
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
