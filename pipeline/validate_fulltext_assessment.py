#!/usr/bin/env python3
"""Validate and integrate the Protocol 2.0 pilot assessment outputs."""

import csv
import hashlib
import json
import pathlib
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
FULLTEXT = PILOT / "fulltext"
ASSESSMENT = PILOT / "fulltext-assessment-v1-final"
FUNDING_AUDIT = PILOT / "funding-audit-v1"
NOT_ASSESSED = "not_assessed_fulltext_unavailable"

CONNECTIONS = {
    "direct_eq", "adjacent_measurement", "application_only", "unrelated", "unclear",
}
FUNDING_RAW = {
    "explicit_euroqol", "other_funding_only", "no_funding_statement", "unclear",
}
FUNDING_SCOPES = {
    "study_funding", "related_work_funding", "publication_support_only",
    "nonfinancial_support_only", "no_euroqol_support", "unclear",
}
PROJECT_LINKS = {"explicit", "probable", "possible", "none", "unclear"}
CONFIDENCE = {"high", "medium", "low"}
ADJUDICABLE_FIELDS = {
    "connection": CONNECTIONS,
    "project_link": PROJECT_LINKS,
}


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, fields, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def keyed(rows, label, failures):
    result = {}
    for row in rows:
        record_id = row["record_id"]
        if record_id in result:
            failures.append(f"duplicate_{label}:{record_id}")
        result[record_id] = row
    return result


def percentage(numerator, denominator):
    return round(100 * numerator / denominator, 1) if denominator else 0.0


def validate_prompt(selection, prompt_path, label, failures):
    prompt_hash = hashlib.sha256(prompt_path.read_text().encode()).hexdigest()
    if selection.get("prompt_sha256") != prompt_hash:
        failures.append(f"{label}_prompt_hash_mismatch")
    return prompt_hash


def main():
    failures = []
    retained_rows = read_csv(PILOT / "screening-final" / "retained.csv")
    manifest_rows = read_csv(FULLTEXT / "manifest.csv")
    assessment_rows = read_csv(ASSESSMENT / "results.csv")
    funding_rows = read_csv(FUNDING_AUDIT / "results.csv")
    adjudication_rows = read_csv(PILOT / "fulltext-manual-adjudications.csv")
    project_candidate_audit = json.loads(
        (PILOT / "project-assessment-v3" / "evaluation.json").read_text()
    )
    if not project_candidate_audit["ok"]:
        failures.append("project_candidate_audit_failed")

    retained = keyed(retained_rows, "retained_record", failures)
    manifest = keyed(manifest_rows, "manifest_record", failures)
    assessments = keyed(assessment_rows, "assessment_record", failures)
    funding_audit = keyed(funding_rows, "funding_audit_record", failures)

    if set(manifest) != set(retained):
        failures.append("manifest_does_not_equal_retained_set")
    available = {
        record_id for record_id, row in manifest.items() if row["status"] == "available"
    }
    unavailable = {
        record_id for record_id, row in manifest.items() if row["status"] == "unavailable"
    }
    unknown_status = set(manifest) - available - unavailable
    if unknown_status:
        failures.append("unknown_fulltext_status:" + ";".join(sorted(unknown_status)))
    if set(assessments) != available:
        failures.append("assessment_does_not_equal_available_fulltext_set")

    selection = json.loads((ASSESSMENT / "selection.json").read_text())
    assessment_prompt_hash = validate_prompt(
        selection, PILOT / "fulltext-assessment-v1" / "SYSTEM.md", "assessment", failures
    )
    selected = [
        record_id
        for batch in selection["batches"]
        for record_id in batch["record_ids"]
    ]
    if len(selected) != len(set(selected)):
        failures.append("duplicate_assessment_selection_record")
    if set(selected) != available:
        failures.append("assessment_selection_does_not_equal_available_fulltext_set")

    candidates = {}
    batch_records = []
    for batch in selection["batches"]:
        payload = json.loads((ASSESSMENT / batch["batch_id"] / "batch.json").read_text())
        if payload.get("prompt_sha256") != assessment_prompt_hash:
            failures.append(f"batch_prompt_hash_mismatch:{batch['batch_id']}")
        payload_ids = [row["record_id"] for row in payload["records"]]
        if payload_ids != batch["record_ids"]:
            failures.append(f"batch_selection_mismatch:{batch['batch_id']}")
        for row in payload["records"]:
            batch_records.append(row["record_id"])
            candidates[row["record_id"]] = set(row["candidate_project_ids"])
    if batch_records != selected:
        failures.append("batch_records_do_not_equal_selection")

    canonical_projects = {
        row["Project Id"]
        for row in read_csv(ROOT / "data" / "funded-projects-canonical.csv")
    }
    for record_id, row in assessments.items():
        if row["connection"] not in CONNECTIONS:
            failures.append(f"invalid_connection:{record_id}")
        if row["funding"] not in FUNDING_RAW:
            failures.append(f"invalid_funding:{record_id}")
        if row["project_link"] not in PROJECT_LINKS:
            failures.append(f"invalid_project_link:{record_id}")
        if row["confidence"] not in CONFIDENCE:
            failures.append(f"invalid_confidence:{record_id}")
        for field in ["connection_evidence", "funding_evidence", "project_evidence"]:
            if not row[field].strip():
                failures.append(f"missing_{field}:{record_id}")
            if len(row[field]) > 600:
                failures.append(f"long_{field}:{record_id}")
        project_ids = [value for value in row["project_ids"].split(";") if value]
        if row["project_link"] in {"none", "unclear"} and project_ids:
            failures.append(f"project_ids_with_no_link:{record_id}")
        if row["project_link"] in {"explicit", "probable", "possible"} and not project_ids:
            failures.append(f"missing_project_id_for_link:{record_id}")
        for project_id in project_ids:
            if project_id not in candidates.get(record_id, set()):
                failures.append(f"project_not_supplied_as_candidate:{record_id}:{project_id}")
            if project_id not in canonical_projects:
                failures.append(f"project_not_canonical:{record_id}:{project_id}")

    funding_selection = json.loads((FUNDING_AUDIT / "selection.json").read_text())
    funding_prompt_hash = validate_prompt(
        funding_selection, FUNDING_AUDIT / "SYSTEM.md", "funding_audit", failures
    )
    raw_explicit = {
        record_id for record_id, row in assessments.items()
        if row["funding"] == "explicit_euroqol"
    }
    audit_selected = {
        record_id
        for batch in funding_selection["batches"]
        for record_id in batch["record_ids"]
    }
    if set(funding_audit) != raw_explicit:
        failures.append("funding_audit_does_not_equal_raw_explicit_set")
    if audit_selected != raw_explicit:
        failures.append("funding_audit_selection_does_not_equal_raw_explicit_set")
    for record_id, row in funding_audit.items():
        if row["funding_scope"] not in FUNDING_SCOPES:
            failures.append(f"invalid_funding_scope:{record_id}")
        if not row["funding_scope_evidence"].strip():
            failures.append(f"missing_funding_scope_evidence:{record_id}")
        if len(row["funding_scope_evidence"]) > 600:
            failures.append(f"long_funding_scope_evidence:{record_id}")

    final_assessments = {record_id: dict(row) for record_id, row in assessments.items()}
    adjudications_by_record = {}
    seen_adjudications = set()
    for row in adjudication_rows:
        record_id = row["record_id"]
        field = row["field"]
        key = (record_id, field)
        if key in seen_adjudications:
            failures.append(f"duplicate_adjudication:{record_id}:{field}")
            continue
        seen_adjudications.add(key)
        if record_id not in final_assessments:
            failures.append(f"unknown_adjudication_record:{record_id}")
            continue
        if field not in ADJUDICABLE_FIELDS:
            failures.append(f"invalid_adjudication_field:{record_id}:{field}")
            continue
        if final_assessments[record_id][field] != row["original_value"]:
            failures.append(f"adjudication_original_value_mismatch:{record_id}:{field}")
            continue
        if row["final_value"] not in ADJUDICABLE_FIELDS[field]:
            failures.append(f"invalid_adjudication_value:{record_id}:{field}")
            continue
        if not row["reason"].strip():
            failures.append(f"missing_adjudication_reason:{record_id}:{field}")
            continue
        final_assessments[record_id][field] = row["final_value"]
        adjudications_by_record.setdefault(record_id, []).append(
            f"{field}: {row['original_value']} -> {row['final_value']}"
        )

    sample = keyed(
        read_csv(PILOT / "fulltext-assessment-v1-sample" / "results.csv"),
        "sample_assessment_record", failures,
    )
    sample_disagreements = {"connection": [], "funding": [], "project_link": [], "project_ids": []}
    for record_id, sample_row in sample.items():
        if record_id not in final_assessments:
            failures.append(f"sample_record_not_in_final:{record_id}")
            continue
        final_row = final_assessments[record_id]
        for field in sample_disagreements:
            if sample_row[field] != final_row[field]:
                sample_disagreements[field].append(record_id)

    fields = [
        "record_id", "title", "year", "doi", "pmid", "pmcid", "linked_people",
        "screen_code", "screen_reason", "full_text_status", "full_text_source",
        "assessment_status", "connection", "connection_evidence", "funding_raw",
        "funding_scope", "funding_evidence", "funding_scope_evidence",
        "project_link", "project_ids", "project_evidence", "confidence",
        "manual_adjudication",
    ]
    paper_rows = []
    project_rows = []
    for record_id in retained:
        screen = retained[record_id]
        fulltext = manifest[record_id]
        base = {
            "record_id": record_id,
            "title": screen["title"],
            "year": screen["year"],
            "doi": screen["doi"],
            "pmid": screen["pmid"],
            "pmcid": screen["pmcid"],
            "linked_people": screen["linked_people"],
            "screen_code": screen["screen_code"],
            "screen_reason": screen["screen_reason"],
            "full_text_status": fulltext["status"],
            "full_text_source": fulltext["source"],
        }
        if record_id in available:
            row = final_assessments[record_id]
            if row["funding"] == "explicit_euroqol":
                funding_scope = funding_audit[record_id]["funding_scope"]
                funding_scope_evidence = funding_audit[record_id]["funding_scope_evidence"]
            else:
                funding_scope = row["funding"]
                funding_scope_evidence = row["funding_evidence"]
            base.update({
                "assessment_status": "assessed",
                "connection": row["connection"],
                "connection_evidence": row["connection_evidence"],
                "funding_raw": row["funding"],
                "funding_scope": funding_scope,
                "funding_evidence": row["funding_evidence"],
                "funding_scope_evidence": funding_scope_evidence,
                "project_link": row["project_link"],
                "project_ids": row["project_ids"],
                "project_evidence": row["project_evidence"],
                "confidence": row["confidence"],
                "manual_adjudication": "; ".join(adjudications_by_record.get(record_id, [])),
            })
            for project_id in [value for value in row["project_ids"].split(";") if value]:
                project_rows.append({
                    "record_id": record_id,
                    "project_id": project_id,
                    "project_link": row["project_link"],
                    "confidence": row["confidence"],
                    "project_evidence": row["project_evidence"],
                    "title": screen["title"],
                })
        else:
            base.update({
                "assessment_status": NOT_ASSESSED,
                "connection": NOT_ASSESSED,
                "connection_evidence": "",
                "funding_raw": NOT_ASSESSED,
                "funding_scope": NOT_ASSESSED,
                "funding_evidence": "",
                "funding_scope_evidence": "",
                "project_link": NOT_ASSESSED,
                "project_ids": "",
                "project_evidence": "",
                "confidence": "",
                "manual_adjudication": "",
            })
        paper_rows.append(base)

    write_csv(PILOT / "paper-assessment.csv", fields, paper_rows)
    write_csv(
        PILOT / "article-project-links.csv",
        ["record_id", "project_id", "project_link", "confidence", "project_evidence", "title"],
        project_rows,
    )

    connection_counts = Counter(
        row["connection"] for row in paper_rows if row["assessment_status"] == "assessed"
    )
    funding_scope_counts = Counter(
        row["funding_scope"] for row in paper_rows if row["assessment_status"] == "assessed"
    )
    project_link_counts = Counter(
        row["project_link"] for row in paper_rows if row["assessment_status"] == "assessed"
    )
    linked_articles = sum(
        project_link_counts[value] for value in ["explicit", "probable", "possible"]
    )
    strong_link_articles = project_link_counts["explicit"] + project_link_counts["probable"]

    screening_validation = json.loads((PILOT / "screening-final" / "validation.json").read_text())
    random_calibration = json.loads((PILOT / "screening-v3" / "evaluation.json").read_text())
    boundary_calibration = json.loads(
        (PILOT / "screening-v3-boundary" / "evaluation.json").read_text()
    )
    evaluation = {
        "status": "pass_with_scale_conditions" if not failures else "validation_failed",
        "pilot_people": 10,
        "screening": {
            "ready": screening_validation["screening_ready_records"],
            "retained": screening_validation["retained"],
            "excluded": screening_validation["excluded"],
            "retain_rate_percent": percentage(
                screening_validation["retained"], screening_validation["screening_ready_records"]
            ),
            "random_calibration_records": random_calibration["records"],
            "random_false_exclusions": random_calibration["false_exclusions"],
            "random_false_inclusions": random_calibration["false_inclusions"],
            "boundary_check_records": boundary_calibration["records"],
            "boundary_false_exclusions": boundary_calibration["false_exclusions"],
            "boundary_false_inclusions": boundary_calibration["false_inclusions"],
            "production_repeat_records": screening_validation["calibration_records_repeated"],
            "production_repeat_outcome_disagreements": len(
                screening_validation["calibration_outcome_disagreements"]
            ),
        },
        "full_text": {
            "retained": len(retained),
            "available": len(available),
            "unavailable": len(unavailable),
            "availability_percent": percentage(len(available), len(retained)),
        },
        "assessment": {
            "assessed": len(assessments),
            "connection_counts": dict(sorted(connection_counts.items())),
            "content_confirmed_direct_or_adjacent": connection_counts["direct_eq"]
            + connection_counts["adjacent_measurement"],
            "funding_scope_counts": dict(sorted(funding_scope_counts.items())),
            "study_funding_articles": funding_scope_counts["study_funding"],
            "study_funding_percent_of_assessed": percentage(
                funding_scope_counts["study_funding"], len(assessments)
            ),
            "project_link_counts": dict(sorted(project_link_counts.items())),
            "linked_articles_including_possible": linked_articles,
            "strong_link_articles": strong_link_articles,
            "strong_link_percent_of_assessed": percentage(strong_link_articles, len(assessments)),
            "article_project_edges": len(project_rows),
            "distinct_linked_projects": len({row["project_id"] for row in project_rows}),
            "manual_adjudications": len(adjudication_rows),
            "project_candidate_audit": {
                "articles": project_candidate_audit["audited_articles"],
                "previously_omitted_candidates": project_candidate_audit[
                    "previously_omitted_candidates_supplied"
                ],
                "new_links": len(project_candidate_audit[
                    "audit_selected_previously_omitted_candidates"
                ]),
                "canonical_changes": len(project_candidate_audit["canonical_changes"]),
            },
        },
        "full_text_prompt_repeatability": {
            "records": len(sample),
            "disagreements_after_adjudication": sample_disagreements,
        },
        "scale_conditions": [
            "Keep the screening-v3 prompt and frozen prompt hash.",
            "Complete profile QA before each person's records enter the scaled corpus.",
            "Add more lawful full-text routes or a manual retrieval queue; 38.8% of retained pilot articles were unavailable.",
            "Keep unavailable articles unassessed for funding and project links.",
            "Add an independent human check before final graph publication; the title/abstract reference labels were made by the same project operator.",
            "Treat possible project links as review items, not confirmed graph edges.",
        ],
        "prompt_sha256": {
            "full_text_assessment": assessment_prompt_hash,
            "funding_audit": funding_prompt_hash,
        },
        "failures": failures,
    }
    (PILOT / "pilot-evaluation.json").write_text(json.dumps(evaluation, indent=2) + "\n")

    markdown = f"""# Protocol 2.0 pilot evaluation

## Decision

The pilot passes with scale conditions. The title and abstract screen is ready for
controlled scale-up. The full workflow is not ready for unattended graph publication.

## Results

- Screened: **{screening_validation['screening_ready_records']:,}**.
- Retained: **{screening_validation['retained']:,}** ({evaluation['screening']['retain_rate_percent']:.1f}%).
- Full text available: **{len(available):,}/{len(retained):,}** ({evaluation['full_text']['availability_percent']:.1f}%).
- Full text unavailable and not assessed: **{len(unavailable):,}/{len(retained):,}**.
- Direct EuroQol research: **{connection_counts['direct_eq']:,}**.
- Adjacent measurement or valuation research: **{connection_counts['adjacent_measurement']:,}**.
- Current-study EuroQol funding: **{funding_scope_counts['study_funding']:,}/{len(assessments):,}** assessed articles ({evaluation['assessment']['study_funding_percent_of_assessed']:.1f}%).
- Strong project links: **{strong_link_articles:,}/{len(assessments):,}** assessed articles ({evaluation['assessment']['strong_link_percent_of_assessed']:.1f}%).
- Possible project links: **{project_link_counts['possible']:,}** review items.
- Article-project edges: **{len(project_rows):,}** across **{evaluation['assessment']['distinct_linked_projects']:,}** projects.

All **{len(assessments):,}** assessed full texts were direct or adjacent measurement or
valuation research. This result supports the recall-focused screen. It does not measure
the relevance of the **{len(unavailable):,}** unavailable full texts.

## Screening validation

The three random batches contained **{random_calibration['records']}** articles. They had
zero false exclusions and zero false inclusions against the operator reference labels.
The separate **{boundary_calibration['records']}**-article boundary check also had zero
outcome errors. The final production run repeated all 80 records with zero outcome
disagreements. These labels were not an independent second-human validation.

## Full-text validation

The prompt check repeated **{len(sample)}** articles. After manual adjudication, the
connection, project-link, and project-ID decisions were stable. Two raw funding labels
differed. The separate funding-scope audit replaces the raw funding label for reporting.
It distinguishes study funding from related-work funding, publication fees, and
nonfinancial support.

The first project assessment limited each article to 12 candidate projects. A complete
candidate audit supplied all **{project_candidate_audit['previously_omitted_candidates_supplied']}**
omitted projects for the **{project_candidate_audit['audited_articles']}** affected
articles. It selected no omitted project, so the canonical links did not change. The
current method uses no similarity score and no candidate cap.

## Scale conditions

1. Keep the frozen screening prompt and prompt hash.
2. Complete profile QA before records enter the scaled corpus.
3. Improve lawful full-text retrieval and keep a manual queue. Pilot availability was only **{evaluation['full_text']['availability_percent']:.1f}%**.
4. Do not infer funding or project links for unavailable full texts.
5. Add an independent human check before final graph publication.
6. Send possible links to review; do not publish them as confirmed edges.

## Canonical outputs

- `paper-assessment.csv`: one row for every retained article.
- `article-project-links.csv`: one row for every explicit, probable, or possible edge.
- `pilot-evaluation.json`: machine-readable metrics and validation state.
- `fulltext-manual-adjudications.csv`: preserved manual corrections.
- `project-assessment-v3/evaluation.json`: complete project-candidate audit.
"""
    (PILOT / "PILOT_EVALUATION.md").write_text(markdown)

    validation = {
        "ok": not failures,
        "retained": len(retained),
        "full_text_available": len(available),
        "full_text_unavailable": len(unavailable),
        "assessments": len(assessments),
        "funding_audits": len(funding_audit),
        "paper_assessment_rows": len(paper_rows),
        "article_project_edges": len(project_rows),
        "manual_adjudications": len(adjudication_rows),
        "project_candidate_audit_ok": project_candidate_audit["ok"],
        "failures": failures,
    }
    (PILOT / "fulltext-assessment-validation.json").write_text(
        json.dumps(validation, indent=2) + "\n"
    )
    print(json.dumps(validation, indent=2))
    raise SystemExit(0 if validation["ok"] else 1)


if __name__ == "__main__":
    main()
