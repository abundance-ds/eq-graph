#!/usr/bin/env python3
"""Run strong structured source-audit batches."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from audit_schema import build_audit_schema


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_usage(path: Path) -> dict[str, int]:
    usage: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            usage = {key: int(value) for key, value in event["usage"].items() if isinstance(value, int)}
    return usage


def run_one(
    row: dict[str, str],
    run_dir: Path,
    schema_path: Path,
    model: str,
    reasoning_effort: str,
    force: bool,
) -> dict[str, Any]:
    batch_id = row["batch_id"]
    records = run_dir / "records"
    traces = run_dir / "traces"
    work = run_dir / "work" / batch_id
    for path in (records, traces, work):
        path.mkdir(parents=True, exist_ok=True)
    output_path = records / f"{batch_id}.json"
    result_path = traces / f"{batch_id}.run.json"
    if output_path.is_file() and result_path.is_file() and not force:
        prior = json.loads(result_path.read_text(encoding="utf-8"))
        if (
            prior.get("returncode") == 0
            and prior.get("json_valid")
            and prior.get("input_sha256") == row["input_sha256"]
            and prior.get("schema_sha256") == digest(schema_path)
            and prior.get("model") == model
            and prior.get("reasoning_effort") == reasoning_effort
        ):
            return {"batch_id": batch_id, "status": "skipped", **prior}
    input_path = REPO / row["input_path"]
    if digest(input_path) != row["input_sha256"]:
        raise ValueError(f"input hash mismatch: {batch_id}")
    trace_path = traces / f"{batch_id}.jsonl"
    stderr_path = traces / f"{batch_id}.stderr.txt"
    command = [
        "codex",
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--ignore-user-config",
        "--ignore-rules",
        "--json",
        "-c",
        'web_search="disabled"',
        "-c",
        f'model_reasoning_effort="{reasoning_effort}"',
        "-m",
        model,
        "-C",
        str(work),
        "--output-schema",
        str(schema_path),
        "-o",
        str(output_path),
        "-",
    ]
    started = time.time()
    with input_path.open("r", encoding="utf-8") as stdin, trace_path.open(
        "w", encoding="utf-8"
    ) as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, stdin=stdin, stdout=stdout, stderr=stderr, text=True)
    json_valid = False
    json_error: str | None = None
    if result.returncode == 0 and output_path.is_file():
        try:
            value = json.loads(output_path.read_text(encoding="utf-8"))
            output_path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            json_valid = True
        except json.JSONDecodeError as error:
            json_error = str(error)
    elapsed = round(time.time() - started, 3)
    run_result = {
        "batch_id": batch_id,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "returncode": result.returncode,
        "json_valid": json_valid,
        "json_error": json_error,
        "elapsed_seconds": elapsed,
        "input_path": row["input_path"],
        "input_sha256": row["input_sha256"],
        "schema_sha256": digest(schema_path),
        "output_path": str(output_path.relative_to(REPO)),
        "output_sha256": digest(output_path) if output_path.is_file() else None,
        "trace_path": str(trace_path.relative_to(REPO)),
        "usage": read_usage(trace_path),
    }
    result_path.write_text(json.dumps(run_result, indent=2) + "\n", encoding="utf-8")
    return {
        "status": "ok" if result.returncode == 0 and json_valid else "failed",
        **run_result,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 12:
        raise ValueError("workers must be from 1 to 12")
    run_dir = HERE / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    schema_path = run_dir / "audit.schema.json"
    schema_path.write_text(json.dumps(build_audit_schema(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path = args.prepared.resolve() / "MANIFEST.tsv"
    rows = read_tsv(manifest_path)
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                run_one,
                row,
                run_dir,
                schema_path,
                args.model,
                args.reasoning_effort,
                args.force,
            ): row["batch_id"]
            for row in rows
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"{result['batch_id']}\t{result['status']}\t{result.get('elapsed_seconds', 0):.1f}s", flush=True)
    results.sort(key=lambda value: value["batch_id"])
    summary = {
        "run": args.run,
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "batches": len(results),
        "successful": sum(value["status"] in {"ok", "skipped"} for value in results),
        "failed": sum(value["status"] == "failed" for value in results),
        "manifest_sha256": digest(manifest_path),
        "schema_sha256": digest(schema_path),
        "usage": {
            key: sum(int(value.get("usage", {}).get(key, 0)) for value in results)
            for key in ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
        },
        "results": results,
    }
    (run_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in summary.items() if key != "results"}))
    if summary["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
