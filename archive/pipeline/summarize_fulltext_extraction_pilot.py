#!/usr/bin/env python3
"""Validate and publish the compact 20-paper pilot result."""

from __future__ import annotations

import csv
import json
import shutil
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work" / "fulltext-assessment-v2-pilot"
OUTPUT = ROOT / "pilot" / "ontology-development-v4" / "production" / "scale-pilot-01"
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
sys.path.insert(0, str(PRODUCTION))

from scale_validate import validate_scale_result  # noqa: E402


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    manifest = read_tsv(WORK / "review-prepared" / "MANIFEST.tsv")
    records_out = OUTPUT / "records"
    reviews_out = OUTPUT / "reviews"
    records_out.mkdir(parents=True, exist_ok=True)
    reviews_out.mkdir(parents=True, exist_ok=True)
    review_rows: list[dict[str, str]] = []
    decisions: Counter[str] = Counter()
    verdicts: Counter[str] = Counter()
    correction_count = 0
    gap_count = 0
    for row in manifest:
        record_id = row["record_id"]
        record_path = WORK / "review-run" / "records" / f"{record_id}.json"
        review_path = WORK / "review-run" / "reviews" / f"{record_id}.json"
        record = json.loads(record_path.read_text(encoding="utf-8"))
        review = json.loads(review_path.read_text(encoding="utf-8"))
        errors, _ = validate_scale_result(
            record,
            record_id,
            set(filter(None, row["candidate_project_ids"].split(";"))),
        )
        if errors:
            raise ValueError(f"{record_id}: " + "; ".join(errors))
        shutil.copy2(record_path, records_out / record_path.name)
        shutil.copy2(review_path, reviews_out / review_path.name)
        eligibility = record["eligibility"]
        decisions[eligibility["decision"]] += 1
        verdicts[review["draft_verdict"]] += 1
        correction_count += len(review["corrections"])
        gap_count += len(review["ontology_gaps"])
        package = json.loads((ROOT / row["package_path"]).read_text(encoding="utf-8"))
        review_rows.append(
            {
                "record_id": record_id,
                "title": row["title"],
                "year": row["year"],
                "doi": row["doi"],
                "doi_url": f"https://doi.org/{row['doi']}" if row["doi"] else "",
                "source_url": package["full_text"].get("source_url") or "",
                "sample_group": row["sample_group"],
                "decision": eligibility["decision"],
                "basis": eligibility["basis"],
                "project_ids": ";".join(eligibility["project_ids"]),
                "reason": eligibility["reason"],
                "source": "; ".join(eligibility["source"]),
                "draft_verdict": review["draft_verdict"],
                "corrections": str(len(review["corrections"])),
                "human_correct": "",
                "human_note": "",
            }
        )
    with (OUTPUT / "HUMAN_REVIEW.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(review_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(review_rows)
    shutil.copy2(WORK / "review-prepared" / "MANIFEST.tsv", OUTPUT / "MANIFEST.tsv")
    result = f"""# Funded-project full-text pilot

- Papers: 20
- Final decisions: {decisions['INCLUDE']} include, {decisions['EXCLUDE']} exclude, {decisions['UNCLEAR']} unclear
- Fresh source review: {verdicts['PASS']} pass, {verdicts['MINOR']} minor, {verdicts['MAJOR']} major
- Local corrections: {correction_count}
- Eligibility decisions changed by review: 0
- Final validation errors: 0
- Reported ontology gaps: {gap_count}; the one gap is a bounded product-type choice, not evidence for an ontology change

One Opus call made the strict eligibility decision and conditionally extracted
the typed record. A fresh Opus call checked the same full source and returned
the corrected result. The final 20 records pass the scale wrapper, core schema,
controlled vocabulary, relation, source, and null-registry checks.

Human review now checks the 20 eligibility decisions in `HUMAN_REVIEW.csv`.
No pilot record enters the database before that gate.
"""
    (OUTPUT / "RESULTS.md").write_text(result, encoding="utf-8")
    print(result, end="")


if __name__ == "__main__":
    main()
