#!/usr/bin/env python3
"""Run the funded-project abstract screen through a Codex subscription."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import signal
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_gemini_abstract_screen import (
    CANONICAL_METADATA,
    CORPUS,
    OUTPUT_SCHEMA,
    PAPER_FIELDS,
    PROJECTS,
    PROJECT_YEAR_LOWER_BOUNDS,
    PROMPT,
    YEAR_OVERRIDES,
    digest,
    load_canonical_metadata,
    load_papers,
    load_projects,
    load_year_overrides,
    paper_for_prompt,
    project_can_precede_paper,
    project_for_prompt,
)


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "scale/protocol-2.0/abstract-screen-v2-codex-r5"
MODEL = "gpt-5.6-terra"
TASK_PREFIX = "Do not use tools. Return only the required JSON object.\n\n"
STOP_EVENT = threading.Event()
ACTIVE_LOCK = threading.Lock()
ACTIVE_PROCESSES: set[subprocess.Popen[str]] = set()


class UsageLimitError(RuntimeError):
    """Report a Codex account limit that requires a later resume."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument("--canonical-metadata", type=Path, default=CANONICAL_METADATA)
    parser.add_argument("--projects", type=Path, default=PROJECTS)
    parser.add_argument("--prompt", type=Path, default=PROMPT)
    parser.add_argument("--year-overrides", type=Path, default=YEAR_OVERRIDES)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--max-attempts", type=int, default=5)
    parser.add_argument("--max-errors", type=int, default=5)
    parser.add_argument("--timeout", type=float, default=240.0)
    parser.add_argument("--warm-delay", type=float, default=2.0)
    parser.add_argument("--project-abstract-chars", type=int, default=300)
    parser.add_argument(
        "--project-lookback-years",
        type=int,
        help=(
            "Only supply projects that started no more than this many years before "
            "the publication. Completed records remain unchanged on resume."
        ),
    )
    parser.add_argument("--limit", type=int)
    parser.add_argument("--year", type=int, action="append", dest="years")
    parser.add_argument("--record-id", action="append", dest="record_ids")
    parser.add_argument("--record-id-file", type=Path)
    parser.add_argument(
        "--errors-only",
        action="store_true",
        help="Retry only records that have a current error file.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Call Codex. Without this flag, prepare artifacts and report status.",
    )
    return parser.parse_args()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def record_path(output_dir: Path, paper: dict[str, Any]) -> Path:
    return output_dir / "records" / str(paper["year"]) / f"{paper['record_id']}.json"


def error_path(output_dir: Path, paper: dict[str, Any]) -> Path:
    return output_dir / "errors" / str(paper["year"]) / f"{paper['record_id']}.json"


def run_root(output_dir: Path, paper: dict[str, Any]) -> Path:
    return output_dir / "runs" / str(paper["year"]) / paper["record_id"]


def load_wanted(args: argparse.Namespace) -> set[str]:
    wanted = set(args.record_ids or [])
    if args.record_id_file:
        wanted.update(
            line.strip()
            for line in args.record_id_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    return wanted


def task_text(prompt_path: Path) -> str:
    return TASK_PREFIX + prompt_path.read_text(encoding="utf-8")


def build_year_prefix(
    task: str,
    projects: list[dict[str, Any]],
    abstract_chars: int,
) -> str:
    project_text = "\n".join(
        json.dumps(
            project_for_prompt(project, abstract_chars),
            ensure_ascii=False,
            separators=(",", ":"),
        )
        for project in projects
    )
    return (
        f"{task.rstrip()}\n\n"
        f"# Time-eligible EuroQol projects ({len(projects)})\n\n{project_text}\n"
        "\n# Publication\n\n"
    )


def build_record_prompt(prefix: str, paper: dict[str, Any]) -> str:
    paper_text = json.dumps(
        paper_for_prompt(paper),
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return prefix + paper_text + "\n"


def project_is_in_window(
    project: dict[str, Any],
    paper_year: int,
    lookback_years: int | None,
) -> bool:
    """Keep a time-eligible project within an optional lookback window."""

    if not project_can_precede_paper(project, paper_year):
        return False
    if lookback_years is None:
        return True
    earliest = project["start_year"] or project["not_before_year"]
    return earliest is not None and earliest >= paper_year - lookback_years


def expected_manifest(
    args: argparse.Namespace,
    task: str,
    papers: list[dict[str, Any]],
    codex_version: str,
) -> dict[str, Any]:
    counts = Counter(paper["year"] for paper in papers)
    return {
        "screen_version": "2.0-codex",
        "scope": "abstract routing only; full text confirms funded-project eligibility",
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "project_abstract_chars": args.project_abstract_chars,
        "records": len(papers),
        "records_by_year": {str(year): counts[year] for year in sorted(counts)},
        "prompt_path": str(args.prompt.relative_to(ROOT)),
        "prompt_sha256": sha256_text(task),
        "output_schema_sha256": sha256_text(
            json.dumps(OUTPUT_SCHEMA, sort_keys=True, separators=(",", ":"))
        ),
        "corpus_path": str(args.corpus.relative_to(ROOT)),
        "corpus_sha256": digest(args.corpus),
        "canonical_metadata_path": str(args.canonical_metadata.relative_to(ROOT)),
        "canonical_metadata_sha256": digest(args.canonical_metadata),
        "projects_path": str(args.projects.relative_to(ROOT)),
        "projects_sha256": digest(args.projects),
        "project_year_lower_bounds_path": str(PROJECT_YEAR_LOWER_BOUNDS.relative_to(ROOT)),
        "project_year_lower_bounds_sha256": digest(PROJECT_YEAR_LOWER_BOUNDS),
        "year_overrides_path": str(args.year_overrides.relative_to(ROOT)),
        "year_overrides_sha256": digest(args.year_overrides),
        "codex_version_at_preparation": codex_version,
        "authentication": "Codex CLI ChatGPT subscription; OPENAI_API_KEY removed",
        "unit": "one publication per Codex call",
        "paper_packet_version": "2.0-no-raw-funder-ids",
        "cache_strategy": "group by publication year; stable instructions and project list before publication",
    }


def prepare_output(
    args: argparse.Namespace,
    task: str,
    papers: list[dict[str, Any]],
    codex_version: str,
) -> dict[str, Any]:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    expected = expected_manifest(args, task, papers, codex_version)
    manifest_path = args.output_dir / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        stable_keys = set(expected) - {"codex_version_at_preparation"}
        mismatches = [key for key in stable_keys if existing.get(key) != expected.get(key)]
        if mismatches:
            raise RuntimeError(
                "Output directory belongs to a different run: " + ", ".join(sorted(mismatches))
            )
        manifest = existing
    else:
        atomic_json(manifest_path, expected)
        manifest = expected
        selection_path = args.output_dir / "selection.jsonl"
        with selection_path.open("w", encoding="utf-8") as handle:
            for paper in sorted(papers, key=lambda item: (item["year"], item["record_id"])):
                value = {
                    "record_id": paper["record_id"],
                    "doi": paper.get("doi") or "",
                    "title": paper.get("title") or "",
                    "year": paper["year"],
                    "abstract_sha256": sha256_text((paper.get("abstract") or "").strip()),
                }
                handle.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")
        (args.output_dir / "PROMPT.md").write_text(task, encoding="utf-8")
        (args.output_dir / "output.schema.json").write_text(
            json.dumps(OUTPUT_SCHEMA, indent=2) + "\n",
            encoding="utf-8",
        )
        (args.output_dir / "README.md").write_text(
            "# Corrected abstract screen\n\n"
            "Each publication is routed to full-text assessment or excluded. A retrieval "
            "decision is not final eligibility. Records are atomic, grouped by year for "
            "prompt caching, validated against the supplied project list, and safe to resume.\n\n"
            "Run or resume:\n\n"
            "```sh\n"
            "python3 pipeline/run_codex_abstract_screen.py --execute --workers 6 "
            "--project-lookback-years 10\n"
            "```\n\n"
            "Retry only current errors with `--errors-only`. Limit work with `--year`, "
            "`--record-id`, `--record-id-file`, or `--limit`. A normal rerun skips all "
            "valid completed records. Omit `--project-lookback-years` only when every "
            "past project must remain in the prompt.\n",
            encoding="utf-8",
        )
    return manifest


def codex_status() -> tuple[str, str]:
    version = subprocess.run(
        ["codex", "--version"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    login = subprocess.run(
        ["codex", "login", "status"],
        capture_output=True,
        text=True,
        check=True,
    )
    status = (login.stdout + login.stderr).strip()
    if "ChatGPT" not in status:
        raise RuntimeError(f"Codex is not using a ChatGPT subscription: {status}")
    return version, status


def validate_decision(value: Any, eligible_ids: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("Output is not one JSON object.")
    if set(value) != {"decision", "project_ids", "reason"}:
        raise ValueError(f"Output keys are invalid: {sorted(value)}")
    if value["decision"] not in {"RETRIEVE_FULL_TEXT", "EXCLUDE"}:
        raise ValueError(f"Invalid decision: {value['decision']}")
    project_ids = value["project_ids"]
    if not isinstance(project_ids, list) or any(not isinstance(item, str) for item in project_ids):
        raise ValueError("Project IDs must be a string array.")
    if len(project_ids) != len(set(project_ids)):
        raise ValueError("Project IDs contain duplicates.")
    invalid = sorted(set(project_ids) - eligible_ids)
    if invalid:
        raise ValueError("Project IDs were not in the time-eligible prompt: " + ", ".join(invalid))
    if value["decision"] == "EXCLUDE" and project_ids:
        raise ValueError("An EXCLUDE decision must have no project IDs.")
    reason = value["reason"]
    if not isinstance(reason, str) or not reason.strip() or len(reason.split()) > 35:
        raise ValueError("Reason must contain 1–35 words.")
    return {
        "decision": value["decision"],
        "project_ids": project_ids,
        "reason": reason.strip(),
    }


def trace_usage(path: Path) -> tuple[dict[str, Any], list[str]]:
    usage: dict[str, Any] | None = None
    tool_types: list[str] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            event = json.loads(line)
            if event.get("type") == "turn.completed":
                usage = event.get("usage") or {}
            if event.get("type") == "item.completed":
                item_type = (event.get("item") or {}).get("type")
                if item_type and item_type != "agent_message":
                    tool_types.append(item_type)
    if usage is None:
        raise ValueError("Codex trace has no completed-turn usage.")
    return usage, tool_types


def next_attempt(folder: Path) -> int:
    if not folder.exists():
        return 1
    numbers = []
    for child in folder.iterdir():
        if child.is_dir() and child.name.startswith("attempt-"):
            try:
                numbers.append(int(child.name.removeprefix("attempt-")))
            except ValueError:
                continue
    return max(numbers, default=0) + 1


def limit_error(stderr: str, stdout: str) -> bool:
    text = (stderr + "\n" + stdout).lower()
    phrases = (
        "usage limit",
        "weekly limit",
        "rate limit exceeded",
        "you've hit your limit",
        "you have hit your limit",
        "resets at",
    )
    return any(phrase in text for phrase in phrases)


def terminate_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return


def terminate_all() -> None:
    with ACTIVE_LOCK:
        processes = list(ACTIVE_PROCESSES)
    for process in processes:
        terminate_process(process)


def run_codex_attempt(
    args: argparse.Namespace,
    paper: dict[str, Any],
    prompt: str,
    attempt: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    attempt_dir = run_root(args.output_dir, paper) / f"attempt-{attempt:03d}"
    attempt_dir.mkdir(parents=True, exist_ok=False)
    final_path = attempt_dir / "final.json"
    trace_path = attempt_dir / "trace.jsonl"
    stderr_path = attempt_dir / "stderr.txt"
    command = [
        "codex",
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--ignore-rules",
        "--ignore-user-config",
        "--json",
        "-c",
        'web_search="disabled"',
        "-c",
        f'model_reasoning_effort="{args.reasoning_effort}"',
        "-m",
        args.model,
        "--output-schema",
        str((args.output_dir / "output.schema.json").resolve()),
        "-o",
        str(final_path.resolve()),
        "-",
    ]
    environment = os.environ.copy()
    environment.pop("OPENAI_API_KEY", None)
    runtime_dir = args.output_dir / "runtime"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    with trace_path.open("w", encoding="utf-8") as trace, stderr_path.open(
        "w", encoding="utf-8"
    ) as stderr:
        process = subprocess.Popen(
            command,
            cwd=runtime_dir,
            stdin=subprocess.PIPE,
            stdout=trace,
            stderr=stderr,
            text=True,
            env=environment,
            start_new_session=True,
        )
        with ACTIVE_LOCK:
            ACTIVE_PROCESSES.add(process)
        try:
            process.communicate(prompt, timeout=args.timeout)
        except subprocess.TimeoutExpired as error:
            terminate_process(process)
            process.wait(timeout=15)
            raise RuntimeError(f"Codex timed out after {args.timeout:g} seconds.") from error
        finally:
            with ACTIVE_LOCK:
                ACTIVE_PROCESSES.discard(process)
    elapsed = time.perf_counter() - started
    stderr_text = stderr_path.read_text(encoding="utf-8")
    trace_text = trace_path.read_text(encoding="utf-8")
    if process.returncode:
        if limit_error(stderr_text, trace_text):
            raise UsageLimitError(stderr_text.strip() or trace_text[-1000:])
        raise RuntimeError(f"Codex returned {process.returncode}: {stderr_text[-1000:]}")
    if not final_path.exists():
        raise RuntimeError("Codex did not write the final JSON output.")
    decision = json.loads(final_path.read_text(encoding="utf-8"))
    usage, tool_types = trace_usage(trace_path)
    if tool_types:
        raise ValueError("Codex used prohibited tools: " + ", ".join(sorted(set(tool_types))))
    return decision, {"usage": usage, "elapsed_seconds": round(elapsed, 3)}


def run_record(
    args: argparse.Namespace,
    paper: dict[str, Any],
    prefix: str,
    eligible_ids: set[str],
    manifest: dict[str, Any],
    codex_version: str,
) -> tuple[str, dict[str, Any] | None]:
    if STOP_EVENT.is_set():
        return "stopped", None
    destination = record_path(args.output_dir, paper)
    if destination.exists():
        return "skipped", json.loads(destination.read_text(encoding="utf-8"))
    prompt = build_record_prompt(prefix, paper)
    attempt_prompt = prompt
    folder = run_root(args.output_dir, paper)
    first_attempt = next_attempt(folder)
    last_error: Exception | None = None
    attempt_runs: list[dict[str, Any]] = []
    attempts_made = 0
    for offset in range(args.max_attempts):
        if STOP_EVENT.is_set():
            return "stopped", None
        attempt = first_attempt + offset
        attempts_made += 1
        raw: Any = None
        try:
            raw, run = run_codex_attempt(args, paper, attempt_prompt, attempt)
            attempt_runs.append(run)
            decision = validate_decision(raw, eligible_ids)
            usage_keys = {
                key
                for item in attempt_runs
                for key in (item.get("usage") or {})
                if isinstance((item.get("usage") or {}).get(key), (int, float))
            }
            combined_usage = {
                key: sum((item.get("usage") or {}).get(key, 0) or 0 for item in attempt_runs)
                for key in sorted(usage_keys)
            }
            value = {
                "screen_version": "2.0-codex",
                "screened_at": datetime.now(timezone.utc).isoformat(),
                "record_id": paper["record_id"],
                "doi": paper.get("doi") or "",
                "title": paper.get("title") or "",
                "year": paper["year"],
                "model": args.model,
                "reasoning_effort": args.reasoning_effort,
                "codex_version": codex_version,
                "prompt_sha256": manifest["prompt_sha256"],
                "projects_sha256": manifest["projects_sha256"],
                "decision": decision["decision"],
                "project_ids": decision["project_ids"],
                "reason": decision["reason"],
                "eligible_project_count": len(eligible_ids),
                "project_lookback_years": args.project_lookback_years,
                "attempt": attempt,
                "attempts_used": attempts_made,
                "elapsed_seconds": round(
                    sum(item["elapsed_seconds"] for item in attempt_runs),
                    3,
                ),
                "usage": combined_usage,
            }
            atomic_json(destination, value)
            current_error = error_path(args.output_dir, paper)
            if current_error.exists():
                current_error.unlink()
            return "completed", value
        except UsageLimitError as error:
            STOP_EVENT.set()
            last_error = error
            break
        except ValueError as error:
            last_error = error
            if raw is not None:
                attempt_prompt = (
                    prompt
                    + "\n# Correct a rejected output\n\n"
                    + "Your previous JSON was rejected by deterministic validation. "
                    + "Return a corrected complete JSON object. Do not explain the correction.\n\n"
                    + f"Previous JSON: {json.dumps(raw, ensure_ascii=False, separators=(',', ':'))}\n"
                    + f"Validation error: {error}\n"
                )
        except Exception as error:  # noqa: BLE001
            last_error = error
    error = {
        "record_id": paper["record_id"],
        "year": paper["year"],
        "model": args.model,
        "failed_at": datetime.now(timezone.utc).isoformat(),
        "attempts_in_invocation": attempts_made,
        "error_type": type(last_error).__name__ if last_error else "Stopped",
        "error": str(last_error)[:2000] if last_error else "Run stopped.",
    }
    atomic_json(error_path(args.output_dir, paper), error)
    return "error", error


def valid_completion(
    path: Path,
    paper: dict[str, Any],
    manifest: dict[str, Any],
) -> bool:
    if not path.exists():
        return False
    value = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "record_id": paper["record_id"],
        "year": paper["year"],
        "model": manifest["model"],
        "reasoning_effort": manifest["reasoning_effort"],
        "prompt_sha256": manifest["prompt_sha256"],
        "projects_sha256": manifest["projects_sha256"],
    }
    mismatches = [key for key, expected in required.items() if value.get(key) != expected]
    if mismatches:
        raise RuntimeError(f"Stale completed record {paper['record_id']}: {', '.join(mismatches)}")
    return True


def parallel_group(
    args: argparse.Namespace,
    papers: list[dict[str, Any]],
    prefix: str,
    eligible_ids: set[str],
    manifest: dict[str, Any],
    codex_version: str,
) -> Counter[str]:
    counts: Counter[str] = Counter()
    if not papers or STOP_EVENT.is_set():
        return counts
    iterator = iter(papers)
    futures: dict[Future[tuple[str, dict[str, Any] | None]], dict[str, Any]] = {}
    errors = 0
    executor = ThreadPoolExecutor(max_workers=args.workers)
    try:
        for _ in range(min(args.workers, len(papers))):
            paper = next(iterator)
            future = executor.submit(
                run_record,
                args,
                paper,
                prefix,
                eligible_ids,
                manifest,
                codex_version,
            )
            futures[future] = paper
        while futures:
            done, _ = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                paper = futures.pop(future)
                status, value = future.result()
                counts[status] += 1
                if status == "completed" and value:
                    print(
                        f"{paper['record_id']}\t{value['decision']}\t"
                        f"{value['elapsed_seconds']:.1f}s",
                        flush=True,
                    )
                elif status == "error":
                    errors += 1
                    print(f"ERROR\t{paper['record_id']}\t{value['error'][:200]}", flush=True)
                if errors >= args.max_errors:
                    STOP_EVENT.set()
                if not STOP_EVENT.is_set():
                    try:
                        next_paper = next(iterator)
                    except StopIteration:
                        continue
                    next_future = executor.submit(
                        run_record,
                        args,
                        next_paper,
                        prefix,
                        eligible_ids,
                        manifest,
                        codex_version,
                    )
                    futures[next_future] = next_paper
    finally:
        if STOP_EVENT.is_set():
            terminate_all()
        executor.shutdown(wait=True, cancel_futures=True)
    return counts


def compile_progress(
    args: argparse.Namespace,
    papers: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> dict[str, Any]:
    values = []
    errors = []
    by_year: dict[int, dict[str, int]] = defaultdict(
        lambda: {"expected": 0, "completed": 0, "errors": 0}
    )
    for paper in papers:
        year = paper["year"]
        by_year[year]["expected"] += 1
        completed = record_path(args.output_dir, paper)
        failed = error_path(args.output_dir, paper)
        if completed.exists():
            valid_completion(completed, paper, manifest)
            values.append(json.loads(completed.read_text(encoding="utf-8")))
            by_year[year]["completed"] += 1
        elif failed.exists():
            errors.append(json.loads(failed.read_text(encoding="utf-8")))
            by_year[year]["errors"] += 1
    values.sort(key=lambda item: (item["year"], item["record_id"]))
    results_path = args.output_dir / "results.jsonl"
    temporary = results_path.with_name(f".{results_path.name}.{os.getpid()}.tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        for value in values:
            handle.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")
    os.replace(temporary, results_path)
    usage_fields = (
        "input_tokens",
        "cached_input_tokens",
        "cache_write_input_tokens",
        "output_tokens",
        "reasoning_output_tokens",
    )
    usage = {
        key: sum((value.get("usage") or {}).get(key, 0) or 0 for value in values)
        for key in usage_fields
    }
    summary = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "model": manifest["model"],
        "expected_records": len(papers),
        "completed_records": len(values),
        "remaining_records": len(papers) - len(values),
        "current_errors": len(errors),
        "decisions": {
            decision: sum(value["decision"] == decision for value in values)
            for decision in ("RETRIEVE_FULL_TEXT", "EXCLUDE")
        },
        "usage": usage,
        "years": {str(year): by_year[year] for year in sorted(by_year)},
        "stopped": STOP_EVENT.is_set(),
    }
    atomic_json(args.output_dir / "progress.json", summary)
    return summary


def select_papers(
    args: argparse.Namespace,
    papers: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> list[dict[str, Any]]:
    wanted = load_wanted(args)
    known = {paper["record_id"] for paper in papers}
    if wanted - known:
        raise ValueError("Unknown or unready record IDs: " + ", ".join(sorted(wanted - known)))
    selected = papers
    if wanted:
        selected = [paper for paper in selected if paper["record_id"] in wanted]
    if args.years:
        selected = [paper for paper in selected if paper["year"] in set(args.years)]
    if args.errors_only:
        selected = [paper for paper in selected if error_path(args.output_dir, paper).exists()]
    selected = [
        paper
        for paper in selected
        if not valid_completion(record_path(args.output_dir, paper), paper, manifest)
    ]
    selected.sort(key=lambda paper: (paper["year"], paper["record_id"]))
    if args.limit is not None:
        selected = selected[: args.limit]
    return selected


def install_signal_handlers() -> None:
    def stop(signum: int, frame: Any) -> None:  # noqa: ARG001
        STOP_EVENT.set()
        terminate_all()

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.max_attempts < 1 or args.max_errors < 1:
        raise ValueError("workers, max-attempts, and max-errors must be at least 1")
    STOP_EVENT.clear()
    install_signal_handlers()
    codex_version, login_status = codex_status()
    task = task_text(args.prompt)
    year_overrides = load_year_overrides(args.year_overrides)
    canonical = load_canonical_metadata(args.canonical_metadata)
    papers, missing_year = load_papers(args.corpus, canonical, year_overrides)
    if missing_year:
        raise RuntimeError(
            "Resolve missing publication years before screening: "
            + ", ".join(paper["record_id"] for paper in missing_year)
        )
    papers.sort(key=lambda paper: (paper["year"], paper["record_id"]))
    projects, _ = load_projects(args.projects)
    manifest = prepare_output(args, task, papers, codex_version)
    summary = compile_progress(args, papers, manifest)
    selected = select_papers(args, papers, manifest)
    readiness = {
        "codex_version": codex_version,
        "login": login_status,
        "model": args.model,
        "workers": args.workers,
        "selected_pending_records": len(selected),
        "selected_years": sorted({paper["year"] for paper in selected}),
        "progress": summary,
        "network_calls_enabled": args.execute,
    }
    if not args.execute:
        print(json.dumps(readiness, indent=2))
        return 0
    if not selected:
        print(json.dumps(readiness, indent=2))
        return 0

    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for paper in selected:
        grouped[paper["year"]].append(paper)
    invocation_counts: Counter[str] = Counter()
    try:
        for year in sorted(grouped):
            if STOP_EVENT.is_set():
                break
            eligible = [
                project
                for project in projects
                if project_is_in_window(project, year, args.project_lookback_years)
            ]
            eligible_ids = {project["project_id"] for project in eligible}
            prefix = build_year_prefix(task, eligible, args.project_abstract_chars)
            year_papers = grouped[year]
            warm = year_papers[0]
            print(
                f"YEAR\t{year}\trecords={len(year_papers)}\tprojects={len(eligible)}\t"
                f"warm={warm['record_id']}",
                flush=True,
            )
            status, value = run_record(
                args,
                warm,
                prefix,
                eligible_ids,
                manifest,
                codex_version,
            )
            invocation_counts[status] += 1
            if status == "completed" and value:
                print(
                    f"{warm['record_id']}\t{value['decision']}\t"
                    f"{value['elapsed_seconds']:.1f}s\tWARM",
                    flush=True,
                )
            elif status == "error":
                print(f"ERROR\t{warm['record_id']}\t{value['error'][:200]}", flush=True)
                STOP_EVENT.set()
                break
            if len(year_papers) > 1 and args.warm_delay:
                time.sleep(args.warm_delay)
            invocation_counts.update(
                parallel_group(
                    args,
                    year_papers[1:],
                    prefix,
                    eligible_ids,
                    manifest,
                    codex_version,
                )
            )
    finally:
        terminate_all()
        summary = compile_progress(args, papers, manifest)
    print(
        json.dumps(
            {
                "invocation": dict(invocation_counts),
                "progress": summary,
                "resume_command": (
                    "python3 pipeline/run_codex_abstract_screen.py --execute "
                    f"--workers {args.workers}"
                    + (
                        f" --project-lookback-years {args.project_lookback_years}"
                        if args.project_lookback_years is not None
                        else ""
                    )
                ),
            },
            indent=2,
        )
    )
    return 75 if STOP_EVENT.is_set() else 0


if __name__ == "__main__":
    raise SystemExit(main())
