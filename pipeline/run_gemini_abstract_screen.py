#!/usr/bin/env python3
"""Run the funded-project abstract screen with Gemini Flash."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
MODEL = "gemini-3.7-flash"
CORPUS = ROOT / "scale/protocol-2.0/article-corpus.jsonl"
CANONICAL_METADATA = ROOT / "scale/protocol-2.0/source-union.jsonl"
PROJECTS = ROOT / "data/funded-projects-canonical.csv"
PROJECT_YEAR_LOWER_BOUNDS = ROOT / "pipeline/data/project-year-lower-bounds.tsv"
PROMPT = ROOT / "pipeline/prompts/abstract_screen_v2.md"
YEAR_OVERRIDES = ROOT / "pipeline/data/publication_year_overrides.tsv"
OUTPUT = ROOT / "scale/protocol-2.0/abstract-screen-v2/results.jsonl"
SUMMARY = ROOT / "scale/protocol-2.0/abstract-screen-v2/summary.json"
EUROQOL_FUNDER_ID = "F4320323856"

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": ["RETRIEVE_FULL_TEXT", "EXCLUDE"]},
        "project_ids": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
    },
    "required": ["decision", "project_ids", "reason"],
    "additionalProperties": False,
}

PAPER_FIELDS = (
    "record_id",
    "doi",
    "pmid",
    "title",
    "year",
    "year_source",
    "document_types",
    "venue",
    "authors",
    "abstract",
    "abstract_source",
    "linked_people",
    "discovery_routes",
    "sources",
    "openalex_ids",
    "funders",
    "euroqol_award_ids",
)

CANONICAL_FIELDS = tuple(field for field in PAPER_FIELDS if field not in {"abstract", "abstract_source"})


class RateLimitError(RuntimeError):
    """Report a rate limit and its requested wait."""

    def __init__(self, message: str, retry_after: float = 60.0) -> None:
        super().__init__(message)
        self.retry_after = retry_after


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument("--canonical-metadata", type=Path, default=CANONICAL_METADATA)
    parser.add_argument("--projects", type=Path, default=PROJECTS)
    parser.add_argument("--prompt", type=Path, default=PROMPT)
    parser.add_argument("--year-overrides", type=Path, default=YEAR_OVERRIDES)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--summary", type=Path, default=SUMMARY)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--workers", type=int, default=50)
    parser.add_argument("--minimum-workers", type=int, default=10)
    parser.add_argument("--worker-step", type=int, default=10)
    parser.add_argument("--thinking-level", default="high")
    parser.add_argument("--project-abstract-chars", type=int, default=300)
    parser.add_argument(
        "--shared-project-prefix",
        action="store_true",
        help=(
            "Give every request the full project register before the publication. "
            "This improves shared-prefix caching; year validity remains deterministic."
        ),
    )
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--record-id", action="append", dest="record_ids")
    parser.add_argument(
        "--record-id-file",
        type=Path,
        help="Read one record ID per line and run only those records.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Call Gemini. Without this flag, print a readiness report only.",
    )
    return parser.parse_args()


def load_year_overrides(path: Path) -> dict[str, int]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["record_id"]: int(row["year"]) for row in csv.DictReader(handle, delimiter="\t")}


def load_papers(
    path: Path,
    canonical_metadata: dict[str, dict[str, Any]],
    year_overrides: dict[str, int],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ready: list[dict[str, Any]] = []
    missing_year: list[dict[str, Any]] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            paper = json.loads(line)
            canonical = canonical_metadata.get(paper["record_id"])
            if canonical:
                for field in CANONICAL_FIELDS:
                    paper[field] = canonical.get(field)
            abstract_ready = paper.get("abstract_length_gate")
            if abstract_ready is None:
                abstract_ready = len((paper.get("abstract") or "").strip()) >= 80
            if not abstract_ready:
                continue
            record_id = paper["record_id"]
            if record_id in seen:
                raise ValueError(f"Duplicate record ID: {record_id}")
            seen.add(record_id)
            if not isinstance(paper.get("year"), int) and record_id in year_overrides:
                paper["year"] = year_overrides[record_id]
                paper["year_source"] = "reviewed_override"
            if not isinstance(paper.get("year"), int):
                missing_year.append(paper)
            else:
                ready.append(paper)
    return ready, missing_year


def load_canonical_metadata(path: Path) -> dict[str, dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return {
            record["record_id"]: record
            for line in handle
            if line.strip()
            for record in [json.loads(line)]
        }


def parse_year(value: str) -> int | None:
    value = value.strip()
    return int(value) if value.isdigit() else None


def load_project_year_lower_bounds(
    path: Path = PROJECT_YEAR_LOWER_BOUNDS,
) -> dict[str, int]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {
            row["project_id"]: int(row["not_before_year"])
            for row in csv.DictReader(handle, delimiter="\t")
        }


def load_projects(
    path: Path,
    lower_bounds_path: Path = PROJECT_YEAR_LOWER_BOUNDS,
) -> tuple[list[dict[str, Any]], list[str]]:
    projects: list[dict[str, Any]] = []
    undated: list[str] = []
    lower_bounds = load_project_year_lower_bounds(lower_bounds_path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            start_year = parse_year(row["Start Year"])
            not_before_year = lower_bounds.get(row["Project Id"])
            if start_year is None and not_before_year is None:
                undated.append(row["Project Id"])
            projects.append(
                {
                    "project_id": row["Project Id"],
                    "title": row["Title"],
                    "abstract": row["Abstract"],
                    "principal_investigator": row["Project PI / Applicant Name"],
                    "working_group": row["Working Group"],
                    "start_year": start_year,
                    "not_before_year": not_before_year,
                    "end_year": parse_year(row["End Year"]),
                }
            )
    projects.sort(
        key=lambda item: (
            (item["start_year"] or item["not_before_year"]) is None,
            item["start_year"] or item["not_before_year"] or 0,
            item["project_id"],
        )
    )
    return projects, undated


def project_can_precede_paper(project: dict[str, Any], paper_year: int) -> bool:
    """Keep projects unless a known start year is later than the paper."""

    earliest = project["start_year"] or project["not_before_year"]
    return earliest is None or earliest <= paper_year


def project_for_prompt(project: dict[str, Any], abstract_chars: int) -> dict[str, Any]:
    value = {
        key: project[key]
        for key in project
        if key != "abstract" and project[key] is not None
    }
    abstract = project["abstract"] or ""
    if abstract_chars < 0:
        value["abstract"] = abstract
    elif abstract_chars:
        value["abstract_prefix"] = abstract[:abstract_chars]
        value["abstract_was_truncated"] = len(abstract) > abstract_chars
    return value


def paper_for_prompt(paper: dict[str, Any]) -> dict[str, Any]:
    value = {field: paper.get(field) for field in PAPER_FIELDS}
    funders = value.get("funders") or []
    # Raw OpenAlex funder IDs have no labels and can be mistaken for EuroQol.
    # Give the model only the exact EuroQol signal derived from that list.
    value.pop("funders", None)
    value["openalex_euroqol_funder"] = (
        {"id": EUROQOL_FUNDER_ID, "label": "EuroQol Research Foundation"}
        if EUROQOL_FUNDER_ID in funders
        else None
    )
    return value


def build_prompt(
    task: str,
    paper: dict[str, Any],
    projects: list[dict[str, Any]],
    abstract_chars: int,
) -> str:
    paper_text = json.dumps(paper_for_prompt(paper), ensure_ascii=False, separators=(",", ":"))
    project_text = "\n".join(
        json.dumps(project_for_prompt(project, abstract_chars), ensure_ascii=False, separators=(",", ":"))
        for project in projects
    )
    return (
        f"{task.rstrip()}\n\n"
        f"# Time-eligible EuroQol projects ({len(projects)})\n\n{project_text}\n"
        f"\n# Publication\n\n{paper_text}\n"
    )


def request_body(prompt: str, thinking_level: str) -> bytes:
    value = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0,
            "responseMimeType": "application/json",
            "responseJsonSchema": OUTPUT_SCHEMA,
            "thinkingConfig": {"thinkingLevel": thinking_level},
        },
    }
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def call_gemini(
    api_key: str,
    model: str,
    body: bytes,
    timeout: float,
    retries: int,
) -> tuple[dict[str, Any], float]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
        method="POST",
    )
    for attempt in range(retries + 1):
        started = time.perf_counter()
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.load(response), time.perf_counter() - started
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            retry_match = re.search(r"retry in ([0-9.]+)s", detail, flags=re.IGNORECASE)
            retry_after = float(retry_match.group(1)) if retry_match else 60.0
            if error.code == 429:
                raise RateLimitError(detail[:1000], retry_after) from error
            if error.code not in {500, 502, 503, 504} or attempt == retries:
                raise RuntimeError(f"Gemini HTTP {error.code}: {detail[:1000]}") from error
        except urllib.error.URLError as error:
            if attempt == retries:
                raise RuntimeError(f"Gemini request failed: {error}") from error
        time.sleep(min(2**attempt, 8))
    raise AssertionError("Unreachable")


def response_value(payload: dict[str, Any], eligible_ids: set[str]) -> dict[str, Any]:
    candidates = payload.get("candidates") or []
    if not candidates:
        raise ValueError("Gemini returned no candidate.")
    parts = candidates[0].get("content", {}).get("parts", [])
    text = "".join(part["text"] for part in parts if "text" in part)
    value = json.loads(text)
    if value.get("decision") not in {"RETRIEVE_FULL_TEXT", "EXCLUDE"}:
        raise ValueError(f"Invalid decision: {value}")
    project_ids = value.get("project_ids")
    if not isinstance(project_ids, list) or any(not isinstance(item, str) for item in project_ids):
        raise ValueError(f"Invalid project IDs: {value}")
    invalid = sorted(set(project_ids) - eligible_ids)
    if invalid:
        raise ValueError(f"Project IDs were not supplied: {', '.join(invalid)}")
    if value["decision"] == "EXCLUDE" and project_ids:
        raise ValueError("An EXCLUDE decision must have no project IDs.")
    if not isinstance(value.get("reason"), str) or len(value["reason"].split()) > 35:
        raise ValueError(f"Invalid reason: {value}")
    return value


def completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    values: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record_id = json.loads(line)["record_id"]
                if record_id in values:
                    raise ValueError(f"Duplicate completed record: {record_id}")
                values.add(record_id)
    return values


def write_summary(
    path: Path,
    values: list[dict[str, Any]],
    prompt_path: Path,
    corpus_path: Path,
    projects_path: Path,
    year_overrides_path: Path,
    model: str,
    workers: int,
    missing_year: list[dict[str, Any]],
) -> None:
    summary = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "initial_workers": workers,
        "records": len(values),
        "decisions": {
            key: sum(value["decision"] == key for value in values)
            for key in ("RETRIEVE_FULL_TEXT", "EXCLUDE")
        },
        "missing_year_records": [paper["record_id"] for paper in missing_year],
        "prompt_path": str(prompt_path.relative_to(ROOT)),
        "prompt_sha256": digest(prompt_path),
        "corpus_sha256": digest(corpus_path),
        "projects_sha256": digest(projects_path),
        "year_overrides_sha256": digest(year_overrides_path),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if args.minimum_workers < 1 or args.workers < args.minimum_workers:
        raise ValueError("workers must be greater than or equal to minimum-workers")
    if args.worker_step < 1:
        raise ValueError("worker-step must be at least 1")
    year_overrides = load_year_overrides(args.year_overrides)
    canonical_metadata = load_canonical_metadata(args.canonical_metadata)
    papers, missing_year = load_papers(args.corpus, canonical_metadata, year_overrides)
    projects, undated_projects = load_projects(args.projects)
    task = args.prompt.read_text(encoding="utf-8")
    wanted = set(args.record_ids or [])
    if args.record_id_file:
        wanted.update(
            line.strip()
            for line in args.record_id_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    if wanted:
        papers = [paper for paper in papers if paper["record_id"] in wanted]
        found = {paper["record_id"] for paper in papers}
        if found != wanted:
            raise ValueError(f"Unknown or unready records: {sorted(wanted - found)}")
    if args.limit is not None:
        papers = papers[: args.limit]
    papers.sort(key=lambda paper: (paper["year"], paper["record_id"]))

    project_counts = [
        sum(project_can_precede_paper(project, paper["year"]) for project in projects)
        for paper in papers
    ]
    context_chars: dict[int, int] = {}
    for year in {paper["year"] for paper in papers}:
        eligible = [project for project in projects if project_can_precede_paper(project, year)]
        project_text = "\n".join(
            json.dumps(
                project_for_prompt(project, args.project_abstract_chars),
                ensure_ascii=False,
                separators=(",", ":"),
            )
            for project in eligible
        )
        context_chars[year] = len(task) + len(project_text) + 100
    approximate_input_tokens = sum(
        (context_chars[paper["year"]] + len(json.dumps(paper_for_prompt(paper), ensure_ascii=False))) // 4
        for paper in papers
    )
    report = {
        "usable_abstract_records": len(papers) + len(missing_year),
        "ready_records": len(papers),
        "missing_year_records": len(missing_year),
        "missing_year_ids": [paper["record_id"] for paper in missing_year],
        "undated_projects_included": len(undated_projects),
        "model": args.model,
        "initial_workers": args.workers,
        "minimum_workers": args.minimum_workers,
        "projects_per_request_min": min(project_counts, default=0),
        "projects_per_request_max": max(project_counts, default=0),
        "approximate_uncached_input_tokens": approximate_input_tokens,
        "approximate_uncached_input_cost_usd_at_0_75_per_million": round(
            approximate_input_tokens * 0.75 / 1_000_000,
            2,
        ),
        "cost_note": "Planning estimate only. Actual tokenization, output, and caching change the charge.",
        "prompt_sha256": digest(args.prompt),
        "year_overrides_sha256": digest(args.year_overrides),
        "network_calls_enabled": args.execute,
    }
    if not args.execute:
        print(json.dumps(report, indent=2))
        return 0
    if missing_year and not wanted and args.limit is None:
        raise RuntimeError("Resolve all missing publication years before the complete run.")

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print("Set GEMINI_API_KEY in the process environment.", file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    done = completed_ids(args.output)
    pending = [paper for paper in papers if paper["record_id"] not in done]
    attempts = {paper["record_id"]: 0 for paper in pending}
    workers = args.workers
    results: list[dict[str, Any]] = []

    while pending:
        wave = pending[:workers]
        pending = pending[workers:]

        def run_one(paper: dict[str, Any]) -> dict[str, Any]:
            eligible = [
                project
                for project in projects
                if project_can_precede_paper(project, paper["year"])
            ]
            prompt_projects = projects if args.shared_project_prefix else eligible
            prompt = build_prompt(
                task,
                paper,
                prompt_projects,
                args.project_abstract_chars,
            )
            payload, elapsed = call_gemini(
                api_key,
                args.model,
                request_body(prompt, args.thinking_level),
                args.timeout,
                args.retries,
            )
            decision = response_value(payload, {project["project_id"] for project in eligible})
            return {
                "screen_version": "2.0",
                "screened_at": datetime.now(timezone.utc).isoformat(),
                "record_id": paper["record_id"],
                "doi": paper.get("doi") or "",
                "title": paper.get("title") or "",
                "year": paper["year"],
                "model": args.model,
                "model_version": payload.get("modelVersion"),
                "thinking_level": args.thinking_level,
                "prompt_sha256": digest(args.prompt),
                "decision": decision["decision"],
                "project_ids": decision["project_ids"],
                "reason": decision["reason"],
                "eligible_project_count": len(eligible),
                "elapsed_seconds": round(elapsed, 3),
                "usage": payload.get("usageMetadata", {}),
                "response_id": payload.get("responseId"),
            }

        rate_limited: list[tuple[dict[str, Any], RateLimitError]] = []
        failed: list[tuple[dict[str, Any], Exception]] = []
        with ThreadPoolExecutor(max_workers=len(wave)) as executor:
            futures = {executor.submit(run_one, paper): paper for paper in wave}
            for future in as_completed(futures):
                paper = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    with args.output.open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
                    print(f"{result['record_id']}\t{result['decision']}\t{result['elapsed_seconds']:.1f}s", flush=True)
                except RateLimitError as error:
                    rate_limited.append((paper, error))
                except Exception as error:  # noqa: BLE001
                    failed.append((paper, error))

        for paper, error in failed:
            attempts[paper["record_id"]] += 1
            if attempts[paper["record_id"]] > args.retries:
                raise RuntimeError(f"Repeated failure for {paper['record_id']}: {error}") from error
            pending.append(paper)
        if rate_limited:
            for paper, _ in rate_limited:
                pending.insert(0, paper)
            old_workers = workers
            workers = max(args.minimum_workers, workers - args.worker_step)
            wait_seconds = max(error.retry_after for _, error in rate_limited)
            print(f"rate_limit workers={old_workers}->{workers} wait={wait_seconds:.1f}s", flush=True)
            time.sleep(wait_seconds + 1)

    all_values = [json.loads(line) for line in args.output.read_text(encoding="utf-8").splitlines() if line]
    write_summary(
        args.summary,
        all_values,
        args.prompt,
        args.corpus,
        args.projects,
        args.year_overrides,
        args.model,
        args.workers,
        missing_year,
    )
    print(json.dumps({**report, "completed": len(all_values)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
