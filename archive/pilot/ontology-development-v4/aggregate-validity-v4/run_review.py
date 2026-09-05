#!/usr/bin/env python3
"""Run one read-only Claude aggregate-validity review."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
VERDICTS = ("PASS", "PARTIAL", "FAIL", "NOT TESTABLE")


def schema(item_count: int) -> dict:
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "evaluations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string", "pattern": "^Q[1-9][0-9]*$"},
                        "verdict": {"type": "string", "enum": list(VERDICTS)},
                        "current_result": {"type": "string", "minLength": 1},
                        "main_cause": {"type": "string", "minLength": 1},
                    },
                    "required": ["id", "verdict", "current_result", "main_cause"],
                },
                "minItems": item_count,
                "maxItems": item_count,
            }
        },
        "required": ["evaluations"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reviewer", choices=("A", "B", "C"))
    parser.add_argument("--model", default="claude-opus-5")
    args = parser.parse_args()

    start = 1 if args.reviewer in ("A", "C") else 51
    count = 100 if args.reviewer == "C" else 50
    expected = [f"Q{number}" for number in range(start, start + count)]
    prompt_path = HERE / f"PROMPT_{args.reviewer}.txt"
    output_path = HERE / f"REVIEW_{args.reviewer}.json"
    traces = HERE / "traces"
    traces.mkdir(exist_ok=True)
    trace_path = traces / f"review-{args.reviewer}.json"
    error_path = traces / f"review-{args.reviewer}.stderr.txt"

    environment = os.environ.copy()
    api_key_removed = bool(environment.pop("ANTHROPIC_API_KEY", None))
    command = [
        "claude",
        "-p",
        "--safe-mode",
        "--model",
        args.model,
        "--effort",
        "high",
        "--tools",
        "Read,Bash",
        "--permission-mode",
        "bypassPermissions",
        "--no-session-persistence",
        "--output-format",
        "json",
        "--json-schema",
        json.dumps(schema(count), separators=(",", ":")),
        "--system-prompt",
        (
            "Act as an independent scientific data auditor. Follow the supplied "
            "task exactly. Use only repository files and read-only SQLite queries."
        ),
    ]
    result = subprocess.run(
        command,
        cwd=REPO,
        input=prompt_path.read_text(encoding="utf-8"),
        capture_output=True,
        text=True,
        env=environment,
        timeout=3600,
    )
    trace_path.write_text(result.stdout, encoding="utf-8")
    error_path.write_text(result.stderr, encoding="utf-8")
    if result.returncode:
        raise SystemExit(f"Reviewer {args.reviewer} failed: {result.returncode}")

    envelope = json.loads(result.stdout)
    review = envelope.get("structured_output")
    if not isinstance(review, dict):
        review = json.loads(envelope["result"])
    ids = [row["id"] for row in review["evaluations"]]
    if ids != expected:
        raise ValueError(f"Reviewer {args.reviewer} returned invalid IDs")
    review["run"] = {
        "model": args.model,
        "effort": "high",
        "api_key_removed": api_key_removed,
        "database": "web/server/data/serving.sqlite",
        "publication_count": 273,
    }
    output_path.write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totals = {verdict: 0 for verdict in VERDICTS}
    for row in review["evaluations"]:
        totals[row["verdict"]] += 1
    print(json.dumps({"reviewer": args.reviewer, "totals": totals}, indent=2))


if __name__ == "__main__":
    main()
