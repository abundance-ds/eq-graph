#!/usr/bin/env python3
"""Validate the final title and abstract screen and export the retained set."""

import csv
import hashlib
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
SCREEN = PILOT / "screening-final"
CODE_PATTERN = re.compile(r"^\[(R1|R2|RU|E1|E2|E3|E4|E5)\]")
RETAIN_CODES = {"R1", "R2", "RU"}
EXCLUDE_CODES = {"E1", "E2", "E3", "E4", "E5"}


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    works = json.loads((PILOT / "derived" / "works.json").read_text())
    ready = {work["record_id"]: work for work in works if work.get("screening_ready")}
    selection = json.loads((SCREEN / "selection.json").read_text())
    results = read_csv(SCREEN / "results.csv")
    selected = [
        record_id
        for batch in selection["batches"]
        for record_id in batch["record_ids"]
    ]
    failures = []
    if len(selected) != len(set(selected)):
        failures.append("duplicate_selected_record")
    if set(selected) != set(ready):
        failures.append("selection_does_not_equal_screening_ready_corpus")
    if len(results) != len({row["record_id"] for row in results}):
        failures.append("duplicate_result_record")
    if {row["record_id"] for row in results} != set(selected):
        failures.append("results_do_not_equal_selection")
    system = (PILOT / "screening-v3" / "SYSTEM.md").read_text()
    prompt_hash = hashlib.sha256(system.encode()).hexdigest()
    if selection["prompt_sha256"] != prompt_hash:
        failures.append("prompt_hash_mismatch")

    code_counts = {code: 0 for code in sorted(RETAIN_CODES | EXCLUDE_CODES)}
    retained = []
    for row in results:
        match = CODE_PATTERN.match(row["reason"])
        if not match:
            failures.append(f"missing_code:{row['record_id']}")
            continue
        code = match.group(1)
        code_counts[code] += 1
        if row["outcome"] == "retain" and code not in RETAIN_CODES:
            failures.append(f"retain_code_mismatch:{row['record_id']}")
        if row["outcome"] == "exclude" and code not in EXCLUDE_CODES:
            failures.append(f"exclude_code_mismatch:{row['record_id']}")
        if len(row["reason"]) > 240:
            failures.append(f"long_reason:{row['record_id']}")
        if row["outcome"] == "retain":
            work = ready[row["record_id"]]
            retained.append({
                "record_id": row["record_id"],
                "screen_code": code,
                "screen_reason": row["reason"],
                "title": work["title"],
                "year": work.get("year") or "",
                "doi": work.get("doi", ""),
                "pmid": work.get("pmid", ""),
                "pmcid": work.get("pmcid", ""),
                "linked_people": "; ".join(work["authors"]),
            })

    calibration = []
    for folder in ["screening-v3", "screening-v3-boundary"]:
        calibration.extend(read_csv(PILOT / folder / "results.csv"))
    final_by_id = {row["record_id"]: row for row in results}
    repeated_outcome_disagreements = [
        row["record_id"] for row in calibration
        if final_by_id[row["record_id"]]["outcome"] != row["outcome"]
    ]
    if repeated_outcome_disagreements:
        failures.append("calibration_repeatability")

    fields = [
        "record_id", "screen_code", "screen_reason", "title", "year",
        "doi", "pmid", "pmcid", "linked_people",
    ]
    with (SCREEN / "retained.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(retained)

    summary = {
        "ok": not failures,
        "prompt_sha256": prompt_hash,
        "screening_ready_records": len(ready),
        "decisions": len(results),
        "retained": len(retained),
        "excluded": sum(row["outcome"] == "exclude" for row in results),
        "code_counts": code_counts,
        "calibration_records_repeated": len(calibration),
        "calibration_outcome_disagreements": repeated_outcome_disagreements,
        "abstract_quality_exclusions": selection.get("abstract_quality_exclusions", []),
        "failures": failures,
    }
    (SCREEN / "validation.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["ok"] else 1)


if __name__ == "__main__":
    main()
