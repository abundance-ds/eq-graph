#!/usr/bin/env python3
"""Run one read-only aggregate-validity review through Claude Code."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CODEX_HOME = Path.home() / ".codex-profiles" / "eq-extraction-2"
CODEX_BIN = Path.home() / ".bun" / "bin" / "codex"
VERDICTS = ("PASS", "PARTIAL", "FAIL", "NOT TESTABLE")
CAUSES = ("NONE", "QUERY", "DATA", "STRUCTURE", "MISSING_INPUT", "UNSAFE")
REVIEW_IDS = {
    "A": [f"Q{number}" for number in range(1, 51)],
    "B": [f"Q{number}" for number in range(51, 101)],
    "C": [f"Q{number}" for number in range(1, 101)],
    "D": [
        "Q16", "Q17", "Q18", "Q20", "Q21", "Q22", "Q24", "Q26", "Q27",
        "Q28", "Q32", "Q38", "Q44", "Q47", "Q62", "Q89", "Q98",
    ],
}


def output_schema(item_count: int) -> dict:
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "evaluations": {
                "type": "array",
                "minItems": item_count,
                "maxItems": item_count,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string", "pattern": "^Q[1-9][0-9]*$"},
                        "verdict": {"type": "string", "enum": list(VERDICTS)},
                        "defect_class": {"type": "string", "enum": list(CAUSES)},
                        "result": {"type": "string", "minLength": 1},
                        "cause": {"type": "string", "minLength": 1},
                    },
                    "required": ["id", "verdict", "defect_class", "result", "cause"],
                },
            }
        },
        "required": ["evaluations"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reviewer", choices=tuple(REVIEW_IDS))
    parser.add_argument("--provider", choices=("claude", "codex"), default="claude")
    parser.add_argument("--model")
    args = parser.parse_args()
    model = args.model or (
        "claude-opus-5" if args.provider == "claude" else "gpt-5.6-sol"
    )

    expected = REVIEW_IDS[args.reviewer]
    count = len(expected)
    prompt_path = HERE / f"PROMPT_{args.reviewer}.txt"
    output_path = HERE / f"REVIEW_{args.reviewer}.json"
    traces = HERE / "traces"
    traces.mkdir(exist_ok=True)

    environment = os.environ.copy()
    api_key_removed = bool(
        environment.pop(
            "ANTHROPIC_API_KEY" if args.provider == "claude" else "OPENAI_API_KEY",
            None,
        )
    )
    final_path = traces / f"review-{args.reviewer}.final.json"
    if args.provider == "claude":
        command = [
            "claude",
            "-p",
            "--safe-mode",
            "--model",
            model,
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
            json.dumps(output_schema(count), separators=(",", ":")),
            "--system-prompt",
            (
                "Act as an independent scientific data auditor. Follow the task. "
                "Use only repository files and read-only SQLite queries."
            ),
        ]
    else:
        schema_path = traces / f"review-{args.reviewer}.schema.json"
        schema_path.write_text(
            json.dumps(output_schema(count), separators=(",", ":")), encoding="utf-8"
        )
        environment["CODEX_HOME"] = str(CODEX_HOME)
        command = [
            str(CODEX_BIN),
            "exec",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--ignore-user-config",
            "--disable",
            "multi_agent",
            "--json",
            "-m",
            model,
            "-c",
            'model_reasoning_effort="high"',
            "--output-schema",
            str(schema_path),
            "-o",
            str(final_path),
            "-",
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
    (traces / f"review-{args.reviewer}.json").write_text(
        result.stdout, encoding="utf-8"
    )
    (traces / f"review-{args.reviewer}.stderr.txt").write_text(
        result.stderr, encoding="utf-8"
    )
    if result.returncode:
        raise SystemExit(f"Reviewer {args.reviewer} failed: {result.returncode}")

    if args.provider == "claude":
        envelope = json.loads(result.stdout)
        review = envelope.get("structured_output")
        if not isinstance(review, dict):
            review = json.loads(envelope["result"])
    else:
        review = json.loads(final_path.read_text(encoding="utf-8"))
    ids = [row["id"] for row in review["evaluations"]]
    if ids != expected:
        raise ValueError(f"Reviewer {args.reviewer} returned invalid IDs")
    review["run"] = {
        "provider": args.provider,
        "model": model,
        "effort": "high",
        "api_key_removed": api_key_removed,
        "database": "web/server/data/serving.sqlite",
        "publication_count": 797,
    }
    output_path.write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    totals = {verdict: 0 for verdict in VERDICTS}
    causes = {cause: 0 for cause in CAUSES}
    for row in review["evaluations"]:
        totals[row["verdict"]] += 1
        causes[row["defect_class"]] += 1
    print(json.dumps({"reviewer": args.reviewer, "totals": totals, "causes": causes}))


if __name__ == "__main__":
    main()
