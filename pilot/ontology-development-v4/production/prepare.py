#!/usr/bin/env python3
"""Verify calibration sources and prepare one self-contained prompt per paper."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SQLITE_CODE = HERE.parent.parent / "ontology-development-v3" / "sqlite"
sys.path.insert(0, str(SQLITE_CODE))

from jats_metadata import parse_jats  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def slim_metadata(parsed: dict[str, Any]) -> dict[str, Any]:
    return {
        "publication": parsed["publication"],
        "dates": parsed["dates"],
        "authors": parsed["authors"],
        "affiliations": parsed["affiliations"],
        "funding": parsed["funding"],
        "keywords": parsed["keywords"],
        "categories": parsed["categories"],
        "correspondence": parsed["correspondence"],
    }


def verify(path: Path, expected_hash: str, expected_bytes: str) -> None:
    if not path.is_file():
        raise ValueError(f"missing source: {path}")
    if path.stat().st_size != int(expected_bytes):
        raise ValueError(f"byte mismatch: {path}")
    actual = digest(path)
    if actual != expected_hash:
        raise ValueError(f"SHA-256 mismatch: {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=HERE / "CALIBRATION.tsv")
    parser.add_argument("--output", type=Path, default=HERE / "prepared")
    args = parser.parse_args()
    output = args.output.resolve()
    task_path = HERE / "TASK.md"
    ontology_path = HERE.parent / "ONTOLOGY.md"
    vocabulary_path = HERE.parent / "VOCABULARY.tsv"
    registry_path = HERE / "REGISTRY.tsv"
    aliases_path = HERE / "REGISTRY_ALIASES.tsv"
    control_paths = (task_path, ontology_path, vocabulary_path)
    control = {
        "task_sha256": digest(task_path),
        "ontology_sha256": digest(ontology_path),
        "vocabulary_sha256": digest(vocabulary_path),
        "normalization_registry_sha256": digest(registry_path),
        "normalization_aliases_sha256": digest(aliases_path),
    }
    inputs_dir = output / "inputs"
    metadata_dir = output / "metadata"
    inputs_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)
    task = task_path.read_text(encoding="utf-8").rstrip()
    ontology = ontology_path.read_text(encoding="utf-8").rstrip()
    vocabulary = vocabulary_path.read_text(encoding="utf-8").rstrip()
    output_rows: list[dict[str, str]] = []
    for row in read_tsv(args.manifest.resolve()):
        article_path = REPO / row["article_path"]
        xml_path = REPO / row["xml_path"]
        verify(article_path, row["article_sha256"], row["article_bytes"])
        verify(xml_path, row["xml_sha256"], row["xml_bytes"])
        parsed = parse_jats(xml_path)
        metadata = slim_metadata(parsed)
        parsed_doi = str(parsed["publication"]["doi"]).casefold()
        if parsed_doi != row["paper_id"].casefold():
            raise ValueError(
                f"DOI mismatch for {row['record_id']}: {parsed_doi} != {row['paper_id']}"
            )
        metadata_path = metadata_dir / f"{row['record_id']}.json"
        metadata_path.write_text(
            json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        prompt = "\n\n".join(
            (
                task,
                "# Ontology reference\n\n" + ontology,
                "# Controlled vocabulary\n\n```tsv\n" + vocabulary + "\n```",
                "# Calibration item\n\n"
                f"- Record ID: `{row['record_id']}`\n"
                f"- DOI: `{row['paper_id']}`\n"
                f"- Article SHA-256: `{row['article_sha256']}`",
                "## Deterministic publication metadata\n\n```json\n"
                + json.dumps(metadata, ensure_ascii=False, indent=2)
                + "\n```",
                "## Full article\n\n" + article_path.read_text(encoding="utf-8").rstrip(),
            )
        ) + "\n"
        input_path = inputs_dir / f"{row['record_id']}.md"
        input_path.write_text(prompt, encoding="utf-8")
        output_rows.append(
            {
                **row,
                "metadata_path": str(metadata_path.relative_to(REPO)),
                "metadata_sha256": digest(metadata_path),
                "input_path": str(input_path.relative_to(REPO)),
                "input_sha256": digest(input_path),
                "input_bytes": str(input_path.stat().st_size),
                **control,
            }
        )
    manifest_path = output / "MANIFEST.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(output_rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"records={len(output_rows)}")
    print(f"manifest={manifest_path}")
    print(f"manifest_sha256={digest(manifest_path)}")
    for path in control_paths:
        print(f"control={path.relative_to(REPO)}\t{digest(path)}")


if __name__ == "__main__":
    main()
