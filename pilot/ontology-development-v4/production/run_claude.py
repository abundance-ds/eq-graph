#!/usr/bin/env python3
"""Run isolated Claude Code calls that return schema-valid JSON."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from audit_schema import build_audit_schema
from review_schema import build_review_schema
from schema import build_schema


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def extract_structured_output(trace_path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        envelope = json.loads(trace_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        return None, str(error)
    value = envelope.get("structured_output")
    if value is None and isinstance(envelope.get("result"), str):
        try:
            value = json.loads(envelope["result"])
        except json.JSONDecodeError as error:
            return None, str(error)
    if not isinstance(value, dict):
        return None, "Claude response has no structured object"
    return value, None


def usage_from_trace(trace_path: Path) -> dict[str, Any]:
    try:
        envelope = json.loads(trace_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    usage = envelope.get("usage")
    return usage if isinstance(usage, dict) else {}


def limit_from_trace(trace_path: Path) -> bool:
    try:
        envelope = json.loads(trace_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    result = str(envelope.get("result", "")).casefold()
    return envelope.get("api_error_status") == 429 or "session limit" in result


def run_one(
    row: dict[str, str],
    id_key: str,
    run_dir: Path,
    schema_path: Path,
    model: str,
    effort: str,
    timeout_seconds: int,
    kind: str,
    force: bool,
    stop_event: threading.Event,
) -> dict[str, Any]:
    item_id = row[id_key]
    records_dir = run_dir / "records"
    traces_dir = run_dir / "traces"
    work_dir = run_dir / "work" / item_id
    for path in (records_dir, traces_dir, work_dir):
        path.mkdir(parents=True, exist_ok=True)

    output_path = records_dir / f"{item_id}.json"
    result_path = traces_dir / f"{item_id}.run.json"
    schema_sha256 = digest(schema_path)
    if output_path.is_file() and result_path.is_file() and not force:
        prior = json.loads(result_path.read_text(encoding="utf-8"))
        if (
            prior.get("returncode") == 0
            and prior.get("json_valid")
            and prior.get("input_sha256") == row["input_sha256"]
            and prior.get("schema_sha256") == schema_sha256
            and prior.get("model") == model
            and prior.get("effort") == effort
            and prior.get("engine") == "claude-code"
            and prior.get("kind") == kind
        ):
            return {"item_id": item_id, "status": "skipped", **prior}

    if stop_event.is_set():
        return {"item_id": item_id, "status": "deferred"}

    input_path = REPO / row["input_path"]
    if digest(input_path) != row["input_sha256"]:
        raise ValueError(f"input hash mismatch: {item_id}")

    trace_path = traces_dir / f"{item_id}.json"
    stderr_path = traces_dir / f"{item_id}.stderr.txt"
    claude_schema = json.loads(schema_path.read_text(encoding="utf-8"))
    claude_schema.pop("$schema", None)
    compact_schema = json.dumps(
        claude_schema,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    command = [
        "claude",
        "-p",
        "--safe-mode",
        "--model",
        model,
        "--effort",
        effort,
        "--tools",
        "",
        "--no-session-persistence",
        "--output-format",
        "json",
        "--json-schema",
        compact_schema,
        "--system-prompt",
        (
            "Follow the supplied extraction, review, or audit task exactly. "
            "Use only the supplied source text. Return only the requested structured object."
        ),
    ]
    started = time.time()
    returncode = -1
    timed_out = False
    claude_env = os.environ.copy()
    claude_env.pop("ANTHROPIC_API_KEY", None)
    with input_path.open("r", encoding="utf-8") as stdin, trace_path.open(
        "w", encoding="utf-8"
    ) as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        try:
            result = subprocess.run(
                command,
                cwd=work_dir,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr,
                text=True,
                timeout=timeout_seconds,
                env=claude_env,
            )
            returncode = result.returncode
        except subprocess.TimeoutExpired:
            timed_out = True

    record, json_error = extract_structured_output(trace_path)
    rate_limited = limit_from_trace(trace_path)
    if rate_limited:
        stop_event.set()
    json_valid = returncode == 0 and record is not None
    review_path: Path | None = None
    output_record = record
    if kind == "review" and record is not None:
        output_record = record.get("record")
        json_valid = json_valid and isinstance(output_record, dict)
        review_path = run_dir / "reviews" / f"{item_id}.json"
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_value = {key: value for key, value in record.items() if key != "record"}
        review_path.write_text(
            json.dumps(review_value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if isinstance(output_record, dict):
        output_path.write_text(
            json.dumps(output_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    elapsed = round(time.time() - started, 3)
    run_result = {
        "item_id": item_id,
        "engine": "claude-code",
        "model": model,
        "effort": effort,
        "kind": kind,
        "returncode": returncode,
        "timed_out": timed_out,
        "rate_limited": rate_limited,
        "json_valid": json_valid,
        "json_error": json_error,
        "elapsed_seconds": elapsed,
        "input_path": row["input_path"],
        "input_sha256": row["input_sha256"],
        "schema_sha256": schema_sha256,
        "output_path": str(output_path.relative_to(REPO)) if output_path.is_file() else None,
        "output_sha256": digest(output_path) if output_path.is_file() else None,
        "trace_path": str(trace_path.relative_to(REPO)),
        "review_path": str(review_path.relative_to(REPO)) if review_path else None,
        "usage": usage_from_trace(trace_path),
    }
    result_path.write_text(json.dumps(run_result, indent=2) + "\n", encoding="utf-8")
    status = "ok" if json_valid else "rate_limited" if rate_limited else "failed"
    return {"status": status, **run_result}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("extraction", "audit", "review"), required=True)
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--model", default="claude-opus-5")
    parser.add_argument("--effort", default="high", choices=("low", "medium", "high", "xhigh", "max"))
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--ids", help="comma-separated extraction record IDs")
    parser.add_argument("--exclude-ids", help="comma-separated extraction record IDs to omit")
    args = parser.parse_args()
    if not 1 <= args.workers <= 24:
        raise ValueError("workers must be from 1 to 24")
    if args.kind == "audit" and (args.ids or args.exclude_ids):
        raise ValueError("ID filters do not apply to audit runs")

    run_dir = HERE / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    if args.kind == "extraction":
        id_key = "record_id"
        schema_path = run_dir / "record.schema.json"
        schema = build_schema()
    elif args.kind == "audit":
        id_key = "batch_id"
        schema_path = run_dir / "audit.schema.json"
        schema = build_audit_schema()
    else:
        id_key = "record_id"
        schema_path = run_dir / "review.schema.json"
        schema = build_review_schema()
    schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest_path = args.prepared.resolve() / "MANIFEST.tsv"
    rows = read_tsv(manifest_path)
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        rows = [row for row in rows if row[id_key] in wanted]
        found = {row[id_key] for row in rows}
        if found != wanted:
            raise ValueError(f"unknown record IDs: {sorted(wanted - found)}")
    if args.exclude_ids:
        excluded = {value.strip() for value in args.exclude_ids.split(",") if value.strip()}
        known = {row[id_key] for row in rows}
        if not excluded <= known:
            raise ValueError(f"unknown excluded record IDs: {sorted(excluded - known)}")
        rows = [row for row in rows if row[id_key] not in excluded]

    results: list[dict[str, Any]] = []
    stop_event = threading.Event()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                run_one,
                row,
                id_key,
                run_dir,
                schema_path,
                args.model,
                args.effort,
                args.timeout_seconds,
                args.kind,
                args.force,
                stop_event,
            ): row[id_key]
            for row in rows
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"{result['item_id']}\t{result['status']}\t{result.get('elapsed_seconds', 0):.1f}s",
                flush=True,
            )

    results.sort(key=lambda value: value["item_id"])
    summary = {
        "run": args.run,
        "kind": args.kind,
        "engine": "claude-code",
        "model": args.model,
        "effort": args.effort,
        "workers": args.workers,
        "manifest": str(manifest_path.relative_to(REPO)),
        "manifest_sha256": digest(manifest_path),
        "schema_sha256": digest(schema_path),
        "items": len(results),
        "successful": sum(value["status"] in {"ok", "skipped"} for value in results),
        "failed": sum(value["status"] == "failed" for value in results),
        "rate_limited": sum(value["status"] == "rate_limited" for value in results),
        "deferred": sum(value["status"] == "deferred" for value in results),
        "elapsed_agent_seconds": round(
            sum(float(value.get("elapsed_seconds", 0)) for value in results), 3
        ),
        "usage": {
            key: sum(int(value.get("usage", {}).get(key, 0)) for value in results)
            for key in (
                "input_tokens",
                "cache_creation_input_tokens",
                "cache_read_input_tokens",
                "output_tokens",
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
    if summary["rate_limited"]:
        raise SystemExit(75)


if __name__ == "__main__":
    main()
