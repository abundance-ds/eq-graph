#!/usr/bin/env python3
"""Run one fresh structured extraction call for each calibration paper."""

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

from schema import build_schema


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_manifest(path: Path) -> list[dict[str, str]]:
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
            usage = {
                key: int(value)
                for key, value in event["usage"].items()
                if isinstance(value, int)
            }
    return usage


def run_one(
    row: dict[str, str],
    run_dir: Path,
    schema_path: Path,
    model: str,
    reasoning_effort: str,
    force: bool,
) -> dict[str, Any]:
    record_id = row["record_id"]
    records_dir = run_dir / "records"
    traces_dir = run_dir / "traces"
    work_dir = run_dir / "work" / record_id
    for path in (records_dir, traces_dir, work_dir):
        path.mkdir(parents=True, exist_ok=True)
    output_path = records_dir / f"{record_id}.json"
    result_path = traces_dir / f"{record_id}.run.json"
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
            return {"record_id": record_id, "status": "skipped", **prior}

    input_path = REPO / row["input_path"]
    if digest(input_path) != row["input_sha256"]:
        raise ValueError(f"input hash mismatch: {record_id}")
    trace_path = traces_dir / f"{record_id}.jsonl"
    stderr_path = traces_dir / f"{record_id}.stderr.txt"
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
        str(work_dir),
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
            record = json.loads(output_path.read_text(encoding="utf-8"))
            output_path.write_text(
                json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            json_valid = True
        except json.JSONDecodeError as error:
            json_error = str(error)
    finished = time.time()
    run_result = {
        "record_id": record_id,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "returncode": result.returncode,
        "json_valid": json_valid,
        "json_error": json_error,
        "started_unix": started,
        "finished_unix": finished,
        "elapsed_seconds": round(finished - started, 3),
        "input_path": row["input_path"],
        "input_sha256": row["input_sha256"],
        "schema_sha256": digest(schema_path),
        "output_path": str(output_path.relative_to(REPO)),
        "output_sha256": digest(output_path) if output_path.is_file() else None,
        "trace_path": str(trace_path.relative_to(REPO)),
        "usage": read_usage(trace_path),
    }
    result_path.write_text(json.dumps(run_result, indent=2) + "\n", encoding="utf-8")
    status = "ok" if result.returncode == 0 and json_valid else "failed"
    return {"status": status, **run_result}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", type=Path, default=HERE / "prepared")
    parser.add_argument("--run", default="run-01")
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument(
        "--reasoning-effort",
        default="high",
        choices=("low", "medium", "high", "xhigh", "max", "ultra"),
    )
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--ids", help="comma-separated record IDs; default is all")
    args = parser.parse_args()
    if not 1 <= args.workers <= 12:
        raise ValueError("workers must be from 1 to 12")
    run_dir = HERE / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    schema_path = run_dir / "record.schema.json"
    schema_path.write_text(
        json.dumps(build_schema(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest_path = args.prepared.resolve() / "MANIFEST.tsv"
    manifest = read_manifest(manifest_path)
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        manifest = [row for row in manifest if row["record_id"] in wanted]
        found = {row["record_id"] for row in manifest}
        if found != wanted:
            raise ValueError(f"unknown record IDs: {sorted(wanted - found)}")
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
            ): row["record_id"]
            for row in manifest
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"{result['record_id']}\t{result['status']}\t"
                f"{result.get('elapsed_seconds', 0):.1f}s",
                flush=True,
            )
    results.sort(key=lambda item: item["record_id"])
    summary = {
        "run": args.run,
        "model": args.model,
        "workers": args.workers,
        "reasoning_effort": args.reasoning_effort,
        "manifest": str(manifest_path.relative_to(REPO)),
        "manifest_sha256": digest(manifest_path),
        "schema_sha256": digest(schema_path),
        "records": len(results),
        "successful": sum(item["status"] in {"ok", "skipped"} for item in results),
        "failed": sum(item["status"] == "failed" for item in results),
        "elapsed_agent_seconds": round(
            sum(float(item.get("elapsed_seconds", 0)) for item in results), 3
        ),
        "usage": {
            key: sum(int(item.get("usage", {}).get(key, 0)) for item in results)
            for key in (
                "input_tokens",
                "cached_input_tokens",
                "output_tokens",
                "reasoning_output_tokens",
            )
        },
        "results": results,
    }
    (run_dir / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: value for key, value in summary.items() if key != "results"}))
    if summary["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
