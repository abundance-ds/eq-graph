#!/usr/bin/env python3
"""Load enriched abstracts with current canonical publication metadata."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ABSTRACT_FIELDS = (
    "abstract",
    "abstract_source",
    "abstract_match",
    "abstract_length_gate",
)


def normalized_doi(value: str | None) -> str:
    text = (value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", text)


def read_jsonl(path: Path) -> dict[str, dict[str, Any]]:
    values: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            value = json.loads(line)
            record_id = value["record_id"]
            if record_id in values:
                raise ValueError(f"Duplicate record ID: {record_id}")
            values[record_id] = value
    return values


def load_publications(
    corpus_path: Path,
    canonical_path: Path,
) -> dict[str, dict[str, Any]]:
    """Return canonical identities with the exact-identifier abstract enrichment."""

    enriched = read_jsonl(corpus_path)
    canonical = read_jsonl(canonical_path)
    publications: dict[str, dict[str, Any]] = {}
    for record_id, source in canonical.items():
        if source.get("document_gate") != "candidate_article":
            continue
        value = dict(source)
        prior = enriched.get(record_id)
        if prior:
            for field in ABSTRACT_FIELDS:
                if field in prior:
                    value[field] = prior[field]
            if (
                not value.get("pmid")
                and prior.get("pmid")
                and normalized_doi(value.get("doi"))
                and normalized_doi(value.get("doi")) == normalized_doi(prior.get("doi"))
            ):
                value["pmid"] = str(prior["pmid"])
        publications[record_id] = value
    return publications
