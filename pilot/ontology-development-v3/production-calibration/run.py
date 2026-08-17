#!/usr/bin/env python3
"""Run one fresh Codex extraction pass for each calibration paper."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]


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


def run_one(row: dict[str, str], run_dir: Path, model: str, force: bool) -> dict:
    record_id = row["record_id"]
    output_dir = run_dir / "records"
    trace_dir = run_dir / "traces"
    work_dir = run_dir / "work" / record_id
    for path in (output_dir, trace_dir, work_dir):
        path.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{record_id}.md"
    result_path = trace_dir / f"{record_id}.run.json"
    if output_path.is_file() and result_path.is_file() and not force:
        prior = json.loads(result_path.read_text(encoding="utf-8"))
        if prior.get("returncode") == 0:
            return {"record_id": record_id, "status": "skipped", **prior}

    input_path = REPO_ROOT / row["input_path"]
    trace_path = trace_dir / f"{record_id}.jsonl"
    stderr_path = trace_dir / f"{record_id}.stderr.txt"
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
        "-m",
        model,
        "-C",
        str(work_dir),
        "-o",
        str(output_path),
        "-",
    ]
    started = time.time()
    with input_path.open("r", encoding="utf-8") as stdin, trace_path.open(
        "w", encoding="utf-8"
    ) as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, stdin=stdin, stdout=stdout, stderr=stderr, text=True)
    if result.returncode == 0 and output_path.is_file():
        output = output_path.read_text(encoding="utf-8")
        if output and not output.endswith("\n"):
            output_path.write_text(output + "\n", encoding="utf-8")
    finished = time.time()
    run_result = {
        "record_id": record_id,
        "model": model,
        "returncode": result.returncode,
        "started_unix": started,
        "finished_unix": finished,
        "elapsed_seconds": round(finished - started, 3),
        "input_path": row["input_path"],
        "output_path": str(output_path.relative_to(REPO_ROOT)),
        "trace_path": str(trace_path.relative_to(REPO_ROOT)),
        "usage": read_usage(trace_path),
    }
    result_path.write_text(json.dumps(run_result, indent=2) + "\n", encoding="utf-8")
    return {"status": "ok" if result.returncode == 0 else "failed", **run_result}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", default="run-01")
    parser.add_argument("--model", default="gpt-5.6-terra")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--ids", help="comma-separated record IDs; default is all")
    parser.add_argument("--manifest", default="MANIFEST.tsv")
    args = parser.parse_args()
    if not 1 <= args.workers <= 4:
        raise ValueError("workers must be between 1 and 4")
    run_dir = SCRIPT_DIR / args.run
    manifest_path = (SCRIPT_DIR / args.manifest).resolve()
    if SCRIPT_DIR.resolve() not in manifest_path.parents:
        raise ValueError("manifest must be inside the calibration directory")
    manifest = read_manifest(manifest_path)
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        manifest = [row for row in manifest if row["record_id"] in wanted]
        found = {row["record_id"] for row in manifest}
        if found != wanted:
            raise ValueError(f"Unknown record IDs: {sorted(wanted - found)}")
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(run_one, row, run_dir, args.model, args.force): row["record_id"]
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
        "manifest": args.manifest,
        "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "records": len(results),
        "successful": sum(item.get("returncode") == 0 for item in results),
        "failed": sum(item.get("returncode") != 0 for item in results),
        "elapsed_agent_seconds": round(sum(item.get("elapsed_seconds", 0) for item in results), 3),
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
