#!/usr/bin/env python3
"""Prepare a stable, diverse queue for the full-text eligibility pilot."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCALE = ROOT / "scale" / "protocol-2.0"
PILOT = SCALE / "fulltext-pilot-v1"
BOUNDARY_TERMS = (
    "review",
    "clinical",
    "outcome",
    "application",
    "secondary",
    "population",
    "routine",
    "implementation",
)
QUEUE_TARGETS = {
    "boundary-retained": 40,
    "clear-retained": 20,
    "excluded-e1": 6,
    "excluded-e2": 6,
    "excluded-e3": 4,
    "excluded-e4": 4,
}
FINAL_QUOTAS = {
    "boundary-retained": 20,
    "clear-retained": 10,
    "excluded-e1": 3,
    "excluded-e2": 3,
    "excluded-e3": 2,
    "excluded-e4": 2,
}


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def normalize_doi(value: str | None) -> str:
    value = (value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", value)


def normalize_title(value: str | None) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", (value or "").casefold()))


def stable_rank(record_id: str) -> str:
    return hashlib.sha256(record_id.encode("utf-8")).hexdigest()


def current_identities() -> tuple[set[str], set[str], set[tuple[str, int]]]:
    database = ROOT / "web" / "server" / "data" / "serving.sqlite"
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    rows = connection.execute(
        "SELECT doi, pmid, title, publication_year FROM publications"
    ).fetchall()
    connection.close()
    dois = {normalize_doi(row[0]) for row in rows if normalize_doi(row[0])}
    pmids = {str(row[1]) for row in rows if row[1]}
    titles = {
        (normalize_title(row[2]), int(row[3]))
        for row in rows
        if normalize_title(row[2]) and row[3] is not None
    }
    return dois, pmids, titles


def is_current(work: dict, identities: tuple[set, set, set]) -> bool:
    dois, pmids, titles = identities
    doi = normalize_doi(work.get("doi"))
    pmid = str(work.get("pmid") or "")
    title_year = (
        normalize_title(work.get("title")),
        int(work.get("year") or 0),
    )
    return bool(
        (doi and doi in dois)
        or (pmid and pmid in pmids)
        or (title_year[0] and title_year in titles)
    )


def take_balanced(rows: list[dict], count: int) -> list[dict]:
    """Select stable rows while spreading boundary terms and screen codes."""
    selected: list[dict] = []
    unused = sorted(rows, key=lambda row: stable_rank(row["record_id"]))
    dimensions = [
        (code, term)
        for term in BOUNDARY_TERMS
        for code in ("R1", "R2")
    ]
    for code, term in dimensions:
        match = next(
            (
                row
                for row in unused
                if row["screen_code"] == code
                and term in row["screen_reason"].casefold()
            ),
            None,
        )
        if match:
            selected.append(match)
            unused.remove(match)
        if len(selected) == count:
            return selected
    selected.extend(unused[: count - len(selected)])
    return selected


def main() -> None:
    PILOT.mkdir(parents=True, exist_ok=True)
    inventory = read_csv(PILOT / "AVAILABILITY.tsv", "\t")
    corpus = {
        row["record_id"]: row
        for row in map(json.loads, (SCALE / "article-corpus.jsonl").open())
    }
    excluded = read_csv(SCALE / "screening-v1" / "excluded.csv")
    identities = current_identities()

    usable = [
        row
        for row in inventory
        if row["current_graph_overlap"] == "0"
        and not row["identity_issue"]
        and (
            row["pmcid"]
            or json.loads(row["candidate_urls_json"])
        )
    ]
    boundary_pool = [
        row
        for row in usable
        if row["screen_code"] == "RU"
        or any(term in row["screen_reason"].casefold() for term in BOUNDARY_TERMS)
    ]
    ru = sorted(
        (row for row in boundary_pool if row["screen_code"] == "RU"),
        key=lambda row: stable_rank(row["record_id"]),
    )
    other_boundary = [row for row in boundary_pool if row["screen_code"] != "RU"]
    boundary = ru + take_balanced(
        other_boundary,
        QUEUE_TARGETS["boundary-retained"] - len(ru),
    )
    boundary_ids = {row["record_id"] for row in boundary}

    clear_pool = [
        row
        for row in usable
        if row["screen_code"] == "R1"
        and row["record_id"] not in boundary_ids
        and not any(
            term in row["screen_reason"].casefold() for term in BOUNDARY_TERMS
        )
    ]
    clear = sorted(clear_pool, key=lambda row: stable_rank(row["record_id"]))[
        : QUEUE_TARGETS["clear-retained"]
    ]

    queue: list[dict[str, str]] = []

    def add_retained(group: str, rows: list[dict]) -> None:
        for rank, row in enumerate(rows, 1):
            queue.append(
                {
                    "sample_group": group,
                    "final_quota": str(FINAL_QUOTAS[group]),
                    "reserve_rank": str(rank),
                    **row,
                }
            )

    add_retained("boundary-retained", boundary)
    add_retained("clear-retained", clear)

    for code in ("E1", "E2", "E3", "E4"):
        group = f"excluded-{code.casefold()}"
        pool = []
        for screen in excluded:
            if screen["code"] != code:
                continue
            work = corpus[screen["record_id"]]
            if is_current(work, identities) or not work.get("primary_pdf_url"):
                continue
            pool.append((screen, work))
        pool.sort(key=lambda item: stable_rank(item[0]["record_id"]))
        for rank, (screen, work) in enumerate(pool[: QUEUE_TARGETS[group]], 1):
            location = {
                "url": work["primary_pdf_url"],
                "host_type": "",
                "license": "",
                "version": "",
                "origin": "screening_metadata",
            }
            queue.append(
                {
                    "sample_group": group,
                    "final_quota": str(FINAL_QUOTAS[group]),
                    "reserve_rank": str(rank),
                    "record_id": screen["record_id"],
                    "screen_code": screen["code"],
                    "screen_reason": screen["reason"],
                    "title": work.get("title") or "",
                    "year": str(work.get("year") or ""),
                    "doi": normalize_doi(work.get("doi")),
                    "pmid": str(work.get("pmid") or ""),
                    "pmcid": "",
                    "openalex_ids": ";".join(work.get("openalex_ids", [])),
                    "linked_people": "; ".join(work.get("linked_people", [])),
                    "availability_class": "PDF_CANDIDATE",
                    "oa_status": "",
                    "landing_url": work.get("primary_landing_page_url") or "",
                    "candidate_urls_json": json.dumps(
                        [location], ensure_ascii=False, separators=(",", ":")
                    ),
                    "current_graph_overlap": "0",
                    "overlap_method": "",
                    "identity_issue": "",
                }
            )

    expected = sum(QUEUE_TARGETS.values())
    if len(queue) != expected:
        raise SystemExit(f"Expected {expected} queue rows, found {len(queue)}.")
    if len({row["record_id"] for row in queue}) != len(queue):
        raise SystemExit("The candidate queue contains a duplicate record ID.")

    fields = list(queue[0])
    output = PILOT / "CANDIDATE_QUEUE.tsv"
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(queue)
    summary = {
        "queue_records": len(queue),
        "queue_groups": dict(sorted(Counter(row["sample_group"] for row in queue).items())),
        "final_target": sum(FINAL_QUOTAS.values()),
        "final_quotas": FINAL_QUOTAS,
        "already_assessed_excluded": sum(
            row["current_graph_overlap"] == "1" for row in inventory
        ),
        "selection_rule": (
            "Use the explicit RU code and pre-registered boundary terms. Do not "
            "calculate an ambiguity score. Use stable record hashes within strata."
        ),
        "queue_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
    }
    (PILOT / "CANDIDATE_QUEUE_SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
