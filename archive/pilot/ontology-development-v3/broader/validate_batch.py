#!/usr/bin/env python3
"""Validate the broader ontology test batch and its extraction records."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SQLITE_DIR = SCRIPT_DIR.parent / "sqlite"
sys.path.append(str(SQLITE_DIR))

from jats_metadata import parse_jats  # noqa: E402


HEADINGS = [
    "Identity and study type",
    "Population and samples",
    "Concepts and themes",
    "Instruments and administration",
    "Methods, protocol, and task design",
    "Analysis and statistical models",
    "Products",
    "Outcomes or measurement properties",
    "Principal findings and interpretation",
    "Limitations and source issues",
    "High-value exact terms",
    "Extraction fit",
]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_dois(path: Path, field: str) -> set[str]:
    return {item[field].strip().lower() for item in rows(path)}


def main() -> None:
    batch = rows(SCRIPT_DIR / "BATCH.tsv")
    if len(batch) != 20:
        raise ValueError(f"Expected 20 batch rows; found {len(batch)}")
    record_ids = [item["record_id"] for item in batch]
    if record_ids != [f"B{number:02d}" for number in range(1, 21)]:
        raise ValueError("Record IDs or order are incorrect")

    batch_dois = {item["doi"].lower() for item in batch}
    if len(batch_dois) != 20:
        raise ValueError("The batch contains a duplicate DOI")
    design_dois = selected_dois(SCRIPT_DIR.parent / "papers.tsv", "paper_id")
    holdout_dois = selected_dois(SCRIPT_DIR.parent / "validation" / "holdout.tsv", "doi")
    overlap = batch_dois & (design_dois | holdout_dois)
    if overlap:
        raise ValueError(f"Broader batch overlaps prior evaluation data: {sorted(overlap)}")

    for item in batch:
        record_id = item["record_id"]
        for prefix in ("article", "xml"):
            path = REPO_ROOT / item[f"{prefix}_path"]
            if not path.is_file():
                raise FileNotFoundError(f"{record_id}: missing {prefix}: {path}")
            if path.stat().st_size != int(item[f"{prefix}_bytes"]):
                raise ValueError(f"{record_id}: {prefix} byte-count mismatch")
            if sha256(path) != item[f"{prefix}_sha256"]:
                raise ValueError(f"{record_id}: {prefix} SHA-256 mismatch")

        parsed = parse_jats(REPO_ROOT / item["xml_path"])
        if parsed["publication"]["doi"] != item["doi"].lower():
            raise ValueError(f"{record_id}: JATS DOI mismatch")

        record_path = SCRIPT_DIR / "records" / f"{record_id}.md"
        text = record_path.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
        if headings != HEADINGS:
            raise ValueError(f"{record_id}: record headings differ from the extraction task")
        if re.search(r"[ \t]+$", text, flags=re.MULTILINE):
            raise ValueError(f"{record_id}: trailing whitespace")
        if not text.endswith("\n"):
            raise ValueError(f"{record_id}: missing final newline")
        if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text, flags=re.IGNORECASE):
            raise ValueError(f"{record_id}: unresolved placeholder")
        if f"doi: `{item['doi'].lower()}`." not in text.lower():
            raise ValueError(f"{record_id}: DOI is absent or differs")

    unexpected = sorted(
        path.name
        for path in (SCRIPT_DIR / "records").glob("*.md")
        if path.stem not in set(record_ids)
    )
    if unexpected:
        raise ValueError(f"Unexpected record files: {unexpected}")

    print("Broader batch validation: PASS")
    print("Manifest rows: 20")
    print("Prior-set overlap: 0")
    print("Article and JATS hashes: 40/40")
    print("JATS DOI matches: 20/20")
    print("Extraction records: 20/20")
    print("Required headings: 240/240")


if __name__ == "__main__":
    main()
