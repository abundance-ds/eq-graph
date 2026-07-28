"""Discovery stage: the only code allowed to touch the network.

Its sole job is to make every response we might need present in the cache, and to
record in the ledger what was attempted. It deliberately does no matching — that is
the match stage's business, and keeping them apart is what makes refinement free.
"""

from __future__ import annotations

from . import sources
from .db import is_settled, set_task, task_row
from .http import FetchError, Fetcher

CORPUS = "__corpus__"

CORPUS_OPS = [
    ("europepmc", "ack_sweep"),
    ("crossref", "funder_sweep"),
]


def _drain(iterator) -> int:
    return sum(1 for _ in iterator)


def run_corpus(conn, fetcher: Fetcher, retry_failed: bool, log=print) -> None:
    for source, op in CORPUS_OPS:
        # The descriptor is what the ledger compares against, so encoding the paging
        # mode here means changing it re-runs the sweep instead of trusting old rows.
        query = (sources.epmc_ack_query() if op == "ack_sweep"
                 else f"crossref funder:{sources.CROSSREF_FUNDER_ID} offset-paged")
        if is_settled(task_row(conn, CORPUS, source, op), retry_failed, query):
            log(f"  {source}/{op}: settled, skipping")
            continue
        try:
            if op == "ack_sweep":
                count = _drain(sources.epmc_search(fetcher, query, strict=True))
            else:
                count = _drain(sources.crossref_funder_works(fetcher))
        except (FetchError, RuntimeError) as exc:
            set_task(conn, CORPUS, source, op, "failed", query=query,
                     http_status=getattr(exc, "status", None), error=str(exc)[:500])
            log(f"  {source}/{op}: FAILED {exc}")
        else:
            set_task(conn, CORPUS, source, op, "ok" if count else "empty",
                     result_count=count, query=query)
            log(f"  {source}/{op}: {count} results")
        conn.commit()


def run_projects(conn, fetcher: Fetcher, projects, retry_failed: bool, log=print) -> dict:
    stats = {"ok": 0, "empty": 0, "failed": 0, "skipped": 0, "settled": 0}
    total = len(projects)

    for index, project in enumerate(projects, 1):
        jobs: list[tuple[str, str | None]] = [
            (kind, query) for kind, query in sources.epmc_grant_queries(project.project_id)
        ]
        jobs.append(("title", sources.epmc_title_query(project.title, project.surnames)))

        for op, query in jobs:
            if is_settled(task_row(conn, project.project_id, "europepmc", op),
                          retry_failed, query):
                stats["settled"] += 1
                continue
            if query is None:
                set_task(conn, project.project_id, "europepmc", op, "skipped",
                         error="no usable query for this id scheme or title")
                stats["skipped"] += 1
                continue
            pages = 3 if op != "title" else 2
            try:
                count = _drain(sources.epmc_search(fetcher, query, max_pages=pages))
            except FetchError as exc:
                set_task(conn, project.project_id, "europepmc", op, "failed", query=query,
                         http_status=exc.status, error=str(exc)[:500])
                stats["failed"] += 1
            else:
                set_task(conn, project.project_id, "europepmc", op,
                         "ok" if count else "empty", result_count=count, query=query)
                stats["ok" if count else "empty"] += 1
        conn.commit()

        if index % 50 == 0 or index == total:
            log(f"  {index}/{total} projects | {stats} | cache {fetcher.stats}")
    return stats


def run_enrichment(conn, fetcher: Fetcher, retry_failed: bool, min_score: float,
                   log=print) -> dict:
    """Resolve OA status and a free full-text location for every plausible work."""
    rows = conn.execute(
        """SELECT DISTINCT w.doi FROM work w
           JOIN candidate c ON c.work_id = w.work_id
           WHERE w.doi IS NOT NULL AND c.score >= ?""",
        (min_score,),
    ).fetchall()
    stats = {"oa": 0, "closed": 0, "unknown": 0, "failed": 0, "settled": 0}

    for index, row in enumerate(rows, 1):
        doi = row["doi"]
        if is_settled(task_row(conn, doi, "unpaywall", "oa"), retry_failed):
            stats["settled"] += 1
            continue
        try:
            info = sources.unpaywall_lookup(fetcher, doi)
        except FetchError as exc:
            set_task(conn, doi, "unpaywall", "oa", "failed",
                     http_status=exc.status, error=str(exc)[:500])
            stats["failed"] += 1
        else:
            if info is None:
                set_task(conn, doi, "unpaywall", "oa", "empty")
                stats["unknown"] += 1
            else:
                conn.execute(
                    """UPDATE work SET
                         is_oa   = MAX(COALESCE(is_oa,0), ?),
                         oa_url  = COALESCE(?, oa_url),
                         pdf_url = COALESCE(?, pdf_url),
                         licence = COALESCE(licence, ?)
                       WHERE doi = ?""",
                    (info["is_oa"], info["oa_url"], info["pdf_url"], info["licence"], doi),
                )
                set_task(conn, doi, "unpaywall", "oa", "ok", result_count=info["is_oa"])
                stats["oa" if info["is_oa"] else "closed"] += 1
        if index % 100 == 0 or index == len(rows):
            conn.commit()
            log(f"  {index}/{len(rows)} DOIs | {stats}")
    conn.commit()
    return stats
