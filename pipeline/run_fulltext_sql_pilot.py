#!/usr/bin/env python3
"""Run resumable Codex full-text extraction with the flat SQL tools."""

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


ROOT = Path(__file__).resolve().parent.parent
WORKSPACE_TOOL = ROOT / "pipeline" / "fulltext_sql_workspace.py"
TOOL_ADAPTER = ROOT / "pipeline" / "fulltext_sql_mcp.py"
BACKEND_TOOL = ROOT / "pipeline" / "fulltext_ingest_tool.py"
DDL = ROOT / "pilot" / "ontology-development-v4" / "production" / "sql-agent-pilot" / "WORKSPACE_SCHEMA.sql"
PRODUCTION = ROOT / "pilot" / "ontology-development-v4" / "production"
ONTOLOGY = PRODUCTION.parent
DEFAULT_CODEX_HOME = Path.home() / ".codex-profiles" / "eq-extraction-2"
DEFAULT_CODEX = Path.home() / ".bun" / "bin" / "codex"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tool_digest() -> str:
    value = hashlib.sha256()
    for path in (
        WORKSPACE_TOOL,
        TOOL_ADAPTER,
        BACKEND_TOOL,
        DDL,
        PRODUCTION / "schema.py",
        PRODUCTION / "validate.py",
        PRODUCTION / "normalize_registry.py",
        PRODUCTION / "REGISTRY.tsv",
        PRODUCTION / "REGISTRY_ALIASES.tsv",
        PRODUCTION / "CONCEPT_MAP.tsv",
        ONTOLOGY / "VOCABULARY.tsv",
    ):
        value.update(path.read_bytes())
    return value.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def prepare_context(source: Path, run_dir: Path, record_id: str) -> Path:
    value = read_json(source)
    value.update(
        {
            "accepted_record_path": str(run_dir / "records" / f"{record_id}.json"),
            "extension_log_path": str(run_dir / "extensions.jsonl"),
            "workspace_path": str(run_dir / "workspaces" / f"{record_id}.sqlite"),
        }
    )
    target = run_dir / "contexts" / f"{record_id}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target


def trace_metrics(path: Path) -> dict[str, Any]:
    metrics: dict[str, Any] = {"tool_calls": 0, "tool_errors": 0}
    if not path.is_file():
        return metrics
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "mcp_tool_call":
            metrics["tool_calls"] += 1
            if item.get("status") == "failed" or item.get("error"):
                metrics["tool_errors"] += 1
        usage = event.get("usage")
        if isinstance(usage, dict):
            metrics["usage"] = usage
    return metrics


def usage_limit_reached(stderr_text: str, trace_path: Path) -> bool:
    """Return true only for a Codex subscription usage-limit error."""
    marker = "you've hit your usage limit"
    if marker in stderr_text.casefold():
        return True
    if not trace_path.is_file():
        return False
    for line in trace_path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") not in {"error", "turn.failed"}:
            continue
        message = event.get("message")
        if not isinstance(message, str):
            error = event.get("error")
            message = error.get("message", "") if isinstance(error, dict) else ""
        if marker in message.casefold():
            return True
    return False


def run_one(
    row: dict[str, str],
    run_dir: Path,
    model: str,
    effort: str,
    timeout_seconds: int,
    force: bool,
    codex_home: Path,
    stop_event: threading.Event,
) -> dict[str, Any]:
    record_id = row["record_id"]
    record_path = run_dir / "records" / f"{record_id}.json"
    workspace_path = run_dir / "workspaces" / f"{record_id}.sqlite"
    trace_path = run_dir / "traces" / f"{record_id}.jsonl"
    stderr_path = run_dir / "traces" / f"{record_id}.stderr.txt"
    final_path = run_dir / "traces" / f"{record_id}.final.txt"
    result_path = run_dir / "traces" / f"{record_id}.run.json"
    work_dir = run_dir / "work" / record_id
    for path in (record_path.parent, workspace_path.parent, trace_path.parent, work_dir):
        path.mkdir(parents=True, exist_ok=True)

    prior = read_json(result_path)
    if (
        not force
        and record_path.is_file()
        and prior.get("input_sha256") == row["input_sha256"]
        and prior.get("context_sha256") == row["context_sha256"]
        and prior.get("tool_sha256") == tool_digest()
    ):
        return {**prior, "record_id": record_id, "status": "skipped"}
    if stop_event.is_set():
        return {"record_id": record_id, "status": "deferred"}

    input_path = ROOT / row["input_path"]
    source_context = ROOT / row["context_path"]
    if digest(input_path) != row["input_sha256"]:
        raise ValueError(f"input hash mismatch: {record_id}")
    if digest(source_context) != row["context_sha256"]:
        raise ValueError(f"context hash mismatch: {record_id}")
    context_path = prepare_context(source_context, run_dir, record_id)
    record_path.unlink(missing_ok=True)
    workspace_path.unlink(missing_ok=True)

    python = ROOT / ".venv" / "bin" / "python"
    if not python.is_file():
        python = Path("python3")
    codex = Path(os.environ.get("CODEX_BIN", str(DEFAULT_CODEX)))
    adapter_args = json.dumps(
        [str(TOOL_ADAPTER), "--context", str(context_path)],
        ensure_ascii=False,
        separators=(",", ":"),
    )
    command = [
        str(codex),
        "exec",
        "--ephemeral",
        "--dangerously-bypass-approvals-and-sandbox",
        "--skip-git-repo-check",
        "--ignore-user-config",
        "--disable",
        "shell_tool",
        "--disable",
        "unified_exec",
        "--disable",
        "multi_agent",
        "--json",
        "-m",
        model,
        "-c",
        f'model_reasoning_effort="{effort}"',
        "-c",
        "tools.web_search=false",
        "-c",
        f'mcp_servers.eq_sql.command={json.dumps(str(python))}',
        "-c",
        f"mcp_servers.eq_sql.args={adapter_args}",
        "-o",
        str(final_path),
        "-",
    ]
    environment = os.environ.copy()
    environment.pop("OPENAI_API_KEY", None)
    environment["CODEX_HOME"] = str(codex_home)
    started = time.time()
    returncode = -1
    timed_out = False
    with input_path.open(encoding="utf-8") as stdin, trace_path.open(
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
                env=environment,
            )
            returncode = result.returncode
        except subprocess.TimeoutExpired:
            timed_out = True

    stderr_text = stderr_path.read_text(encoding="utf-8", errors="replace")
    rate_limited = usage_limit_reached(stderr_text, trace_path)
    if rate_limited:
        stop_event.set()
    saved = record_path.is_file()
    status = "ok" if saved else "rate_limited" if rate_limited else "failed"
    result_value = {
        "record_id": record_id,
        "status": status,
        "model": model,
        "effort": effort,
        "returncode": returncode,
        "timed_out": timed_out,
        "saved": saved,
        "elapsed_seconds": round(time.time() - started, 3),
        "input_sha256": row["input_sha256"],
        "context_sha256": row["context_sha256"],
        "tool_sha256": tool_digest(),
        **trace_metrics(trace_path),
    }
    result_path.write_text(json.dumps(result_value, indent=2) + "\n", encoding="utf-8")
    return result_value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--effort", default="high")
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    parser.add_argument("--ids", help="comma-separated record IDs")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 20:
        raise ValueError("workers must be from 1 to 20")
    if not args.codex_home.joinpath("auth.json").is_file():
        raise ValueError(f"Codex profile is not authenticated: {args.codex_home}")

    prepared = args.prepared.resolve()
    run_dir = args.run.resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    rows = read_tsv(prepared / "MANIFEST.tsv")
    if args.ids:
        wanted = {value.strip() for value in args.ids.split(",") if value.strip()}
        rows = [row for row in rows if row["record_id"] in wanted]
        found = {row["record_id"] for row in rows}
        if found != wanted:
            raise ValueError(f"unknown record IDs: {sorted(wanted - found)}")
    if args.offset < 0:
        raise ValueError("offset must not be negative")
    rows = rows[args.offset :]
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("limit must be positive")
        rows = rows[: args.limit]
    stop_event = threading.Event()
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(
                run_one,
                row,
                run_dir,
                args.model,
                args.effort,
                args.timeout_seconds,
                args.force,
                args.codex_home.resolve(),
                stop_event,
            )
            for row in rows
        ]
        for future in as_completed(futures):
            value = future.result()
            results.append(value)
            print(
                f"{value['record_id']}\t{value['status']}\t{value.get('elapsed_seconds', 0):.1f}s",
                flush=True,
            )

    results.sort(key=lambda value: value["record_id"])
    summary = {
        "model": args.model,
        "effort": args.effort,
        "workers": args.workers,
        "records": len(results),
        "successful": sum(value["status"] in {"ok", "skipped"} for value in results),
        "failed": sum(value["status"] == "failed" for value in results),
        "rate_limited": sum(value["status"] == "rate_limited" for value in results),
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
