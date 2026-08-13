#!/usr/bin/env python3
"""Compare AI screening decisions with an independent reference screen."""

import argparse
import csv
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
CODES = {"R1", "R2", "RU", "E1", "E2", "E3", "E4", "E5"}
CODE_PATTERN = re.compile(r"^\[(R1|R2|RU|E1|E2|E3|E4|E5)\]")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v3")
    parser.add_argument("--screen-dir")
    return parser.parse_args()


def load_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    args = parse_args()
    screen = pathlib.Path(args.screen_dir).resolve() if args.screen_dir else PILOT / f"screening-{args.version}"
    reference = load_csv(screen / "reference.csv")
    results = load_csv(screen / "results.csv")
    selection = json.loads((screen / "selection.json").read_text())
    expected = {
        record_id
        for batch in selection["batches"]
        for record_id in batch["record_ids"]
    }
    reference_by_id = {row["record_id"]: row for row in reference}
    results_by_id = {row["record_id"]: row for row in results}
    if set(reference_by_id) != expected:
        raise SystemExit("reference.csv does not contain exactly the selected records")
    if set(results_by_id) != expected:
        raise SystemExit("results.csv does not contain exactly the selected records")

    rows = []
    failures = []
    for record_id in sorted(expected):
        human = reference_by_id[record_id]
        ai = results_by_id[record_id]
        human_code = human["human_code"]
        code_match = CODE_PATTERN.match(ai["reason"])
        ai_code = code_match.group(1) if code_match else ""
        if human["human_outcome"] not in {"retain", "exclude"}:
            failures.append(f"invalid_human_outcome:{record_id}")
        if human_code not in CODES:
            failures.append(f"invalid_human_code:{record_id}")
        if not ai_code:
            failures.append(f"missing_ai_code:{record_id}")
        if human["human_outcome"] == ai["outcome"]:
            error_type = "correct"
        elif human["human_outcome"] == "retain":
            error_type = "false_exclusion"
        else:
            error_type = "false_inclusion"
        rows.append({
            "batch_id": ai["batch_id"],
            "record_id": record_id,
            "human_outcome": human["human_outcome"],
            "human_code": human_code,
            "human_reason": human["human_reason"],
            "ai_outcome": ai["outcome"],
            "ai_code": ai_code,
            "ai_reason": ai["reason"],
            "error_type": error_type,
            "notes": human.get("notes", ""),
            "title": ai["title"],
        })

    fields = list(rows[0])
    with (screen / "evaluation.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    batch_ids = [batch["batch_id"] for batch in selection["batches"]]
    by_batch = {}
    for batch_id in batch_ids:
        subset = [row for row in rows if row["batch_id"] == batch_id]
        by_batch[batch_id] = {
            "records": len(subset),
            "human_retained": sum(row["human_outcome"] == "retain" for row in subset),
            "ai_retained": sum(row["ai_outcome"] == "retain" for row in subset),
            "false_exclusions": sum(row["error_type"] == "false_exclusion" for row in subset),
            "false_inclusions": sum(row["error_type"] == "false_inclusion" for row in subset),
            "agreement": sum(row["error_type"] == "correct" for row in subset) / len(subset),
        }
    false_exclusions = sum(row["error_type"] == "false_exclusion" for row in rows)
    false_inclusions = sum(row["error_type"] == "false_inclusion" for row in rows)
    summary = {
        "version": args.version,
        "prompt_sha256": selection["prompt_sha256"],
        "records": len(rows),
        "human_retained": sum(row["human_outcome"] == "retain" for row in rows),
        "ai_retained": sum(row["ai_outcome"] == "retain" for row in rows),
        "false_exclusions": false_exclusions,
        "false_inclusions": false_inclusions,
        "agreement": sum(row["error_type"] == "correct" for row in rows) / len(rows),
        "batches": by_batch,
        "pilot_gate": {
            "rule": "At least three batches; zero false exclusions and at most two false inclusions in each batch.",
            "passed": len(by_batch) >= 3 and all(
                item["false_exclusions"] == 0 and item["false_inclusions"] <= 2
                for item in by_batch.values()
            ),
        },
        "validation_failures": failures,
    }
    (screen / "evaluation.json").write_text(json.dumps(summary, indent=2) + "\n")

    lines = [
        f"# Screening {args.version} evaluation", "",
        f"- Records: {summary['records']}",
        f"- Human retained: {summary['human_retained']}",
        f"- AI retained: {summary['ai_retained']}",
        f"- False exclusions: {false_exclusions}",
        f"- False inclusions: {false_inclusions}",
        f"- Agreement: {summary['agreement']:.1%}",
        f"- Pilot gate passed: {'yes' if summary['pilot_gate']['passed'] else 'no'}", "",
        "## Errors", "",
    ]
    errors = [row for row in rows if row["error_type"] != "correct"]
    if errors:
        for row in errors:
            lines.append(
                f"- {row['record_id']} — {row['error_type']}: "
                f"human {row['human_outcome']} {row['human_code']}; "
                f"AI {row['ai_outcome']} {row['ai_code']}. {row['title']}"
            )
    else:
        lines.append("- None.")
    (screen / "EVALUATION.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
