#!/usr/bin/env python3
"""Resumable scraper for EuroQol project publications.

Stages, each independently rerunnable:

    discover  network only  -- fill the HTTP cache, record attempts in the ledger
    match     offline       -- replay the cache, link projects to works
    enrich    network only  -- OA status and free full-text location per DOI
    harvest   network only  -- pull Europe PMC full text for the whole work pool
    mine      offline       -- read grant ids out of that text
    fulltext  network only  -- download openly licensed full texts
    export    offline       -- write publications.json into each project directory
    report    offline       -- coverage gap report
    status    offline       -- what the ledger currently knows

`all` runs discover -> match -> enrich -> match -> export -> report.

Interrupting is safe: settled tasks are skipped on the next run. Use --retry-failed
to re-attempt transient failures, and --force to bypass the HTTP cache entirely.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scrape import discover, fulltext, match, mine, report  # noqa: E402
from scrape.db import connect  # noqa: E402
from scrape.http import Fetcher  # noqa: E402


def cmd_discover(conn, args) -> None:
    fetcher = Fetcher(conn, force=args.force)
    projects = match.load_projects()
    if args.limit:
        projects = projects[: args.limit]
    print(f"corpus sweeps over {len(projects)} projects")
    run_corpus = not args.projects_only
    if run_corpus:
        discover.run_corpus(conn, fetcher, args.retry_failed)
    discover.run_projects(conn, fetcher, projects, args.retry_failed)
    print(f"cache: {fetcher.stats}")


def cmd_match(conn, args) -> None:
    match.run(conn)


def cmd_enrich(conn, args) -> None:
    fetcher = Fetcher(conn, force=args.force)
    stats = discover.run_enrichment(conn, fetcher, args.retry_failed, args.min_score)
    print(f"enrichment: {stats}")


def cmd_harvest(conn, args) -> None:
    fetcher = Fetcher(conn, force=args.force)
    mine.harvest(conn, fetcher, args.retry_failed)


def cmd_mine(conn, args) -> None:
    mine.mine(conn)


def cmd_fulltext(conn, args) -> None:
    fetcher = Fetcher(conn, force=args.force)
    fulltext.run(conn, fetcher, args.retry_failed, args.min_fulltext_score)


def cmd_export(conn, args) -> None:
    report.export(conn)


def cmd_report(conn, args) -> None:
    report.no_publication_report(conn)
    report.gap_report(conn)


def cmd_status(conn, args) -> None:
    rows = conn.execute(
        "SELECT source, op, status, COUNT(*) n FROM task GROUP BY source, op, status "
        "ORDER BY source, op, status"
    ).fetchall()
    if not rows:
        print("ledger empty - run `discover` first")
        return
    print(f"{'source':<12} {'op':<22} {'status':<10} {'count':>7}")
    for row in rows:
        print(f"{row['source']:<12} {row['op']:<22} {row['status']:<10} {row['n']:>7}")
    for label, query in (
        ("works", "SELECT COUNT(*) FROM work"),
        ("candidates", "SELECT COUNT(*) FROM candidate"),
        ("curated decisions", "SELECT COUNT(*) FROM decision"),
        ("cached responses", "SELECT COUNT(*) FROM fetch"),
    ):
        print(f"{label:<24} {conn.execute(query).fetchone()[0]:>7}")


def cmd_all(conn, args) -> None:
    cmd_discover(conn, args)
    cmd_match(conn, args)
    cmd_enrich(conn, args)
    cmd_harvest(conn, args)
    cmd_mine(conn, args)
    cmd_match(conn, args)  # re-link with enriched OA fields and mined grant ids
    cmd_export(conn, args)
    cmd_fulltext(conn, args)
    cmd_report(conn, args)


COMMANDS = {
    "discover": cmd_discover, "match": cmd_match, "enrich": cmd_enrich,
    "harvest": cmd_harvest, "mine": cmd_mine,
    "fulltext": cmd_fulltext, "export": cmd_export, "report": cmd_report,
    "status": cmd_status, "all": cmd_all,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=sorted(COMMANDS))
    parser.add_argument("--limit", type=int, help="only the first N projects (smoke tests)")
    parser.add_argument("--retry-failed", action="store_true",
                        help="re-attempt tasks left in the failed state")
    parser.add_argument("--force", action="store_true",
                        help="bypass the HTTP cache and re-fetch")
    parser.add_argument("--projects-only", action="store_true",
                        help="skip the corpus-wide sweeps")
    parser.add_argument("--min-fulltext-score", type=float, default=0.85,
                        help="minimum score to download full text (default: 0.85)")
    parser.add_argument("--min-score", type=float, default=0.45,
                        help="minimum candidate score to enrich (default: 0.45)")
    args = parser.parse_args()

    conn = connect()
    try:
        COMMANDS[args.command](conn, args)
    finally:
        conn.commit()
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
