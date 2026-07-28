"""Mine grant ids out of full text.

Europe PMC's `GRANT_ID` and `ACK_FUND` indexes capture EuroQol awards only
patchily, but the project id is almost always printed in the article's own
acknowledgement or funding statement. Reading the text therefore recovers
attributions no index query can reach -- and it is the strongest evidence there is,
because the paper itself names the grant.

Two stages, kept apart like the rest of the pipeline:

    harvest  network  -- pull Europe PMC JATS XML for every pooled work with a PMCID
    mine     offline  -- scan the harvested text and record project id mentions
"""

from __future__ import annotations

import json
import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from .db import is_settled, now, set_task, task_row
from .http import CACHE_DIR, FetchError, Fetcher

REPO = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO / "input" / "projects"
STORE = CACHE_DIR / "fulltext"

EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"

# Both id schemes. Bounded so "20180340" matches but a 12-digit accession does not.
ID_TOKEN = re.compile(r"\b\d{2,5}-[A-Z]{2,4}\b|\b\d{7,8}(?:R\d)?\b")

# A bare number is not evidence: grant ids are reused across funders, so the id must
# sit near a EuroQol mention to count. 300 chars comfortably spans a funding sentence.
PROXIMITY = 300
EUROQOL_RE = re.compile(r"euroqol", re.IGNORECASE)


def store_path(pmcid: str) -> Path:
    return STORE / f"{pmcid}.xml"


def harvest(conn, fetcher: Fetcher, retry_failed: bool = False, log=print) -> dict:
    """Fetch Europe PMC full text for every pooled work that has a PMCID."""
    rows = conn.execute(
        "SELECT work_id, pmcid FROM work WHERE pmcid IS NOT NULL ORDER BY work_id"
    ).fetchall()
    STORE.mkdir(parents=True, exist_ok=True)
    stats = {"fetched": 0, "adopted": 0, "settled": 0, "absent": 0, "failed": 0}

    # Anything already downloaded into a project directory is byte-identical to what
    # the endpoint would return; adopt it rather than asking for it again.
    existing = {p.name: p for p in PROJECTS_DIR.glob("*/papers/*.xml")}

    for index, row in enumerate(rows, 1):
        pmcid, work_id = row["pmcid"], row["work_id"]
        dest = store_path(pmcid)
        url = EPMC_FULLTEXT.format(pmcid=pmcid)
        prior = task_row(conn, work_id, "europepmc", "harvest")

        if dest.exists() and is_settled(prior, retry_failed, url):
            stats["settled"] += 1
            continue
        if is_settled(prior, retry_failed, url) and prior["status"] in ("empty", "skipped"):
            stats["settled"] += 1
            continue

        twin = existing.get(f"{re.sub(r'[^A-Za-z0-9._-]+', '_', work_id)}.xml")
        if twin and twin.exists():
            shutil.copyfile(twin, dest)
            set_task(conn, work_id, "europepmc", "harvest", "ok",
                     query=url, result_count=dest.stat().st_size)
            stats["adopted"] += 1
            continue

        try:
            data = fetcher.get_bytes(url, max_bytes=40 * 1024 * 1024)
        except FetchError as exc:
            status = getattr(exc, "status", None)
            set_task(conn, work_id, "europepmc", "harvest",
                     "empty" if status in (404, 403) else "failed",
                     query=url, http_status=status, error=str(exc)[:300])
            stats["absent" if status in (404, 403) else "failed"] += 1
            continue

        dest.write_bytes(data)
        set_task(conn, work_id, "europepmc", "harvest", "ok",
                 query=url, result_count=len(data))
        stats["fetched"] += 1

        if index % 100 == 0:
            conn.commit()
            log(f"  {index}/{len(rows)} | {stats}")
    conn.commit()
    log(f"harvest: {stats}")
    return stats


def core_store_path(doi: str) -> Path:
    return STORE / ("doi_" + re.sub(r"[^A-Za-z0-9._-]+", "_", doi) + ".txt")


def harvest_core(conn, fetcher, retry_failed: bool = False, log=print) -> dict:
    """Fetch full text from CORE for pooled works Europe PMC cannot serve.

    Only works with a DOI and no PMCID: those have no Europe PMC full text at all,
    so CORE's repository deposit is the only text available to mine.
    """
    from . import sources
    if not sources.CORE_API_KEY:
        log("  core: skipped, CORE_API_KEY not set")
        return {"skipped": True}

    rows = conn.execute(
        "SELECT work_id, doi FROM work WHERE pmcid IS NULL AND doi IS NOT NULL "
        "ORDER BY work_id"
    ).fetchall()
    STORE.mkdir(parents=True, exist_ok=True)
    stats = {"fetched": 0, "no_text": 0, "absent": 0, "settled": 0, "failed": 0}

    for index, row in enumerate(rows, 1):
        work_id, doi = row["work_id"], row["doi"]
        dest = core_store_path(doi)
        key = f"core:{doi}"
        prior = task_row(conn, work_id, "core", "harvest")
        if is_settled(prior, retry_failed, key) and (
            prior["status"] != "ok" or dest.exists()
        ):
            stats["settled"] += 1
            continue
        try:
            record = sources.core_by_doi(fetcher, doi)
        except FetchError as exc:
            set_task(conn, work_id, "core", "harvest", "failed", query=key,
                     http_status=getattr(exc, "status", None), error=str(exc)[:300])
            stats["failed"] += 1
            continue
        text = (record or {}).get("fullText") or ""
        if not record:
            set_task(conn, work_id, "core", "harvest", "empty", query=key,
                     error="not in CORE")
            stats["absent"] += 1
        elif not text:
            set_task(conn, work_id, "core", "harvest", "empty", query=key,
                     error="in CORE but no full text deposited")
            stats["no_text"] += 1
        else:
            dest.write_text(text, encoding="utf-8")
            set_task(conn, work_id, "core", "harvest", "ok", query=key,
                     result_count=len(text))
            stats["fetched"] += 1
        if index % 50 == 0:
            conn.commit()
            log(f"  core {index}/{len(rows)} | {stats}")
    conn.commit()
    log(f"core harvest: {stats}")
    return stats


def project_ids(conn) -> set[str]:
    return {
        json.loads(p.read_text(encoding="utf-8"))["project_id"]
        for p in PROJECTS_DIR.glob("*/project.json")
    }


def mentions_in(text: str, known: set[str]) -> dict[str, str]:
    """Project ids appearing within PROXIMITY characters of a EuroQol mention."""
    zones = [
        (max(0, m.start() - PROXIMITY), m.end() + PROXIMITY)
        for m in EUROQOL_RE.finditer(text)
    ]
    if not zones:
        return {}
    found: dict[str, str] = {}
    for match in ID_TOKEN.finditer(text):
        token = match.group()
        if token not in known or token in found:
            continue
        if any(start <= match.start() <= end for start, end in zones):
            lo = max(0, match.start() - 120)
            found[token] = " ".join(text[lo:match.end() + 120].split())
    return found


def mine(conn, log=print) -> dict:
    """Offline: scan harvested text and record which projects each work names."""
    known = project_ids(conn)
    work_by_pmcid = {
        row["pmcid"]: row["work_id"]
        for row in conn.execute("SELECT work_id, pmcid FROM work WHERE pmcid IS NOT NULL")
    }
    work_by_corefile = {
        core_store_path(row["doi"]).name: row["work_id"]
        for row in conn.execute("SELECT work_id, doi FROM work WHERE doi IS NOT NULL")
    }
    conn.execute("DELETE FROM fulltext_mention")
    stamp = now()
    scanned = linked = 0

    for path in sorted(list(STORE.glob("*.xml")) + list(STORE.glob("*.txt"))):
        if path.suffix == ".xml":
            work_id = work_by_pmcid.get(path.stem)
            if not work_id:
                continue
            try:
                text = " ".join(t for t in ET.parse(path).getroot().itertext())
            except ET.ParseError:
                continue
        else:
            work_id = work_by_corefile.get(path.name)
            if not work_id:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
        scanned += 1
        for project_id, snippet in mentions_in(text, known).items():
            conn.execute(
                """INSERT OR REPLACE INTO fulltext_mention
                   (work_id, project_id, snippet, updated_at) VALUES (?,?,?,?)""",
                (work_id, project_id, snippet[:400], stamp),
            )
            linked += 1
    conn.commit()
    projects = conn.execute(
        "SELECT COUNT(DISTINCT project_id) FROM fulltext_mention"
    ).fetchone()[0]
    log(f"mined {scanned} full texts: {linked} mentions across {projects} projects")
    return {"scanned": scanned, "mentions": linked, "projects": projects}
