#!/usr/bin/env python3
"""Evaluate OpenAlex EuroQol funding metadata against pilot full-text evidence."""

import csv
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
PILOT = ROOT / "pilot" / "protocol-2.0"


def normalize_doi(value):
    value = (value or "").strip().casefold()
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def percentage(numerator, denominator):
    return round(100 * numerator / denominator, 1) if denominator else 0.0


def main():
    metadata = read_csv(SCALE / "funding-metadata-discovery.csv")
    papers = read_csv(PILOT / "paper-assessment.csv")
    metadata_by_doi = {}
    for row in metadata:
        doi = normalize_doi(row["doi"])
        if doi:
            metadata_by_doi.setdefault(doi, []).append(row)

    output_rows = []
    for paper in papers:
        doi = normalize_doi(paper["doi"])
        matches = metadata_by_doi.get(doi, []) if doi else []
        output_rows.append({
            "record_id": paper["record_id"],
            "doi": doi,
            "title": paper["title"],
            "metadata_match": "1" if matches else "0",
            "openalex_ids": "; ".join(sorted({row["openalex_id"] for row in matches})),
            "euroqol_award_ids": "; ".join(sorted({
                award_id
                for row in matches
                for award_id in row["euroqol_award_ids"].split("; ")
                if award_id
            })),
            "assessment_status": paper["assessment_status"],
            "funding_raw": paper["funding_raw"],
            "funding_scope": paper["funding_scope"],
            "project_link": paper["project_link"],
        })

    fields = [
        "record_id", "doi", "title", "metadata_match", "openalex_ids",
        "euroqol_award_ids", "assessment_status", "funding_raw", "funding_scope",
        "project_link",
    ]
    with (SCALE / "funding-metadata-pilot-evaluation.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)

    assessed = [row for row in output_rows if row["assessment_status"] == "assessed"]
    matched = [row for row in output_rows if row["metadata_match"] == "1"]
    assessed_matched = [row for row in matched if row["assessment_status"] == "assessed"]
    study_funded = [row for row in assessed if row["funding_scope"] == "study_funding"]
    explicit_support = [row for row in assessed if row["funding_raw"] == "explicit_euroqol"]
    matched_study = [row for row in assessed_matched if row["funding_scope"] == "study_funding"]
    matched_explicit = [
        row for row in assessed_matched if row["funding_raw"] == "explicit_euroqol"
    ]
    metadata_work_matches = sum(
        len(metadata_by_doi.get(normalize_doi(row["doi"]), []))
        for row in papers if row["doi"]
    )
    summary = {
        "pilot_retained_articles": len(papers),
        "metadata_matched_retained_articles": len(matched),
        "metadata_work_matches": metadata_work_matches,
        "metadata_matched_assessed_articles": len(assessed_matched),
        "metadata_matched_unavailable_articles": len(matched) - len(assessed_matched),
        "current_study_funding": {
            "metadata_true_positives": len(matched_study),
            "metadata_matches_assessed": len(assessed_matched),
            "positive_predictive_value_percent": percentage(
                len(matched_study), len(assessed_matched)
            ),
            "fulltext_positive_articles": len(study_funded),
            "metadata_detected_fulltext_positives": len(matched_study),
            "sensitivity_percent": percentage(len(matched_study), len(study_funded)),
        },
        "any_explicit_euroqol_support": {
            "metadata_true_positives": len(matched_explicit),
            "metadata_matches_assessed": len(assessed_matched),
            "positive_predictive_value_percent": percentage(
                len(matched_explicit), len(assessed_matched)
            ),
            "fulltext_positive_articles": len(explicit_support),
            "metadata_detected_fulltext_positives": len(matched_explicit),
            "sensitivity_percent": percentage(len(matched_explicit), len(explicit_support)),
        },
        "interpretation": [
            "Use the metadata route for discovery, not final funding classification.",
            "A full-text funding-scope assessment is still required.",
            "Do not calculate funding accuracy for unavailable full texts.",
        ],
    }
    (SCALE / "funding-metadata-pilot-evaluation.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
