#!/usr/bin/env python3
"""Build the version-2 extraction manifest from the frozen 209-paper corpus."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
DEFAULT_SOURCE = (
    REPO
    / "pilot"
    / "ontology-development-v3"
    / "production-calibration"
    / "graph-neutral-209-pre-conflict-rule"
    / "MANIFEST.tsv"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=HERE / "REBUILD_V2.tsv")
    args = parser.parse_args()

    source_rows = read_tsv(args.source.resolve())
    if len(source_rows) != 209:
        raise ValueError(f"expected 209 source rows; found {len(source_rows)}")

    rows: list[dict[str, str]] = []
    seen_dois: set[str] = set()
    seen_articles: set[str] = set()
    for index, source in enumerate(source_rows, 1):
        article_rel = Path(source["article_path"])
        article = REPO / article_rel
        project_id = article_rel.parent.name
        xml_rel = Path("input") / "projects" / project_id / "papers" / (
            article_rel.name.removesuffix(".md") + ".xml"
        )
        xml = REPO / xml_rel
        if not article.is_file() or not xml.is_file():
            raise ValueError(f"missing source pair for {source['record_id']}")
        article_hash = digest(article)
        if article_hash != source["article_sha256"]:
            raise ValueError(f"article hash mismatch for {source['record_id']}")
        doi = source["doi"].strip().casefold()
        if doi in seen_dois:
            raise ValueError(f"duplicate DOI: {doi}")
        if str(article_rel) in seen_articles:
            raise ValueError(f"duplicate article path: {article_rel}")
        seen_dois.add(doi)
        seen_articles.add(str(article_rel))
        rows.append(
            {
                "record_id": f"V2-P{index:03d}",
                "source_record_id": source["record_id"],
                "paper_id": doi,
                "article_path": str(article_rel),
                "article_sha256": article_hash,
                "article_bytes": str(article.stat().st_size),
                "xml_path": str(xml_rel),
                "xml_sha256": digest(xml),
                "xml_bytes": str(xml.stat().st_size),
                "coverage_reason": "frozen 209-paper JATS corpus",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"records={len(rows)}")
    print(f"manifest={args.output}")
    print(f"manifest_sha256={digest(args.output)}")


if __name__ == "__main__":
    main()
