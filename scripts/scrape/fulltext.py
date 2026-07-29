"""Full-text acquisition for the private analysis corpus.

Policy, in order of preference:

1. **Europe PMC full-text XML** for anything with a PMCID. Europe PMC only serves
   `fullTextXML` for its open-access subset, and the result is structured text
   rather than a PDF to re-parse later.
2. **Repository-hosted PDFs** (green OA: PMC mirrors, institutional repositories)
   as recorded by Unpaywall.
3. **Publisher PDFs at any licence**, for every free location Unpaywall records.

Every free location is tried regardless of licence: the corpus is held privately for
analysis, so redistribution terms do not gate acquisition, and an Elsevier "TDM user
licence" article is one we may read. What is *not* done here is circumventing a
paywall -- no credential sharing, no scraper evasion. A work with no free location
is skipped with its landing page recorded, for retrieval through institutional
access instead.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from . import sources
from .db import is_settled, set_task, task_row
from .http import FetchError, Fetcher
from .match import ACCEPT_THRESHOLD

REPO = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO / "input" / "projects"

EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"

OPEN_HOST_TYPES = {"repository"}

# Ledger note that marks a copy fetched by hand in a desktop browser, for the
# publishers that answer 403 to every automated request. See `is_manual`.
MANUAL_NOTE_PREFIX = "retrieved manually"

# Signatures used to reject an HTML interstitial saved under a .pdf name.
PDF_MAGIC = b"%PDF"
MAX_BYTES = 80 * 1024 * 1024
# A landing page is HTML; anything this large is not the page we asked for.
MAX_LANDING_BYTES = 4 * 1024 * 1024

CITATION_PDF_RE = re.compile(
    rb"""<meta[^>]*\bname=["']citation_pdf_url["'][^>]*\bcontent=["']([^"']+)["']"""
    rb"""|<meta[^>]*\bcontent=["']([^"']+)["'][^>]*\bname=["']citation_pdf_url["']""",
    re.IGNORECASE,
)


def safe_name(work_id: str) -> str:
    """Filesystem-safe stem derived from the work id (DOIs contain slashes)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", work_id)


def held_copy(papers_dir: Path, work_id: str) -> Path | None:
    """The document we already hold for this work, in whichever form it arrived."""
    for suffix in (".pdf", ".xml"):
        path = papers_dir / f"{safe_name(work_id)}{suffix}"
        if path.exists():
            return path
    return None


def is_manual(prior) -> bool:
    """Was this row filed by hand rather than by a run of this stage?

    Hand retrieval is recorded in the ledger exactly like any other success, so the
    note is the only thing distinguishing it -- and it matters, because the URL that
    worked in a browser is not one this stage can reach.
    """
    return (prior["last_error"] or "").startswith(MANUAL_NOTE_PREFIX)


def recorded_entries(project_id: str) -> dict[str, dict]:
    """What the project's manifest already says, keyed by work id.

    The ledger's `query` is a settle key -- the whole candidate list -- not a record
    of where a file came from. For anything already on disk the manifest is the only
    place that provenance lives, so it is read back rather than re-derived.
    """
    path = PROJECTS_DIR / project_id / "papers" / "manifest.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {e["work_id"]: e for e in payload.get("entries", []) if e.get("work_id")}


PROVENANCE_FIELDS = ("method", "source_url", "alternates", "attempts_failed")


def unpaywall_from_cache(fetcher: Fetcher, doi: str) -> list[dict]:
    """Every free location Unpaywall knows for a DOI, not just the best one.

    `best_oa_location` is Unpaywall's single pick and is frequently the publisher's
    own copy -- exactly the one that answers 403. The `oa_locations` array usually
    also lists a repository deposit of the same article, which is both openly
    licensed and happy to be fetched.
    """
    try:
        payload = fetcher.get(
            f"{sources.UNPAYWALL}{doi}", {"email": sources.CONTACT_EMAIL}
        ).json()
    except FetchError:
        return []
    locations = list(payload.get("oa_locations") or [])
    best = payload.get("best_oa_location")
    if best and best not in locations:
        locations.insert(0, best)
    return [loc for loc in locations if loc]


def resolve_landing_pdf(fetcher: Fetcher, url: str) -> str | None:
    """The PDF file a repository landing page advertises, one fetch behind the record.

    Unpaywall lists many green deposits with a landing page and no `url_for_pdf`, so
    the file looks absent when it is merely one hop away. Only the Highwire
    `citation_pdf_url` meta tag is trusted: a landing page also links the PDFs of
    everything the article cites, and matching bare `.pdf` hrefs picks up the wrong
    paper (see the ScienceDirect note in CLAUDE.md).
    """
    try:
        payload = fetcher.get_bytes(url, max_bytes=MAX_LANDING_BYTES)
    except FetchError:
        return None
    match = CITATION_PDF_RE.search(payload)
    if not match:
        return None
    found = match.group(1) or match.group(2)
    return found.decode("utf-8", "replace").strip() or None


def enrich_locations(fetcher: Fetcher, locations: list[dict]) -> list[dict]:
    """Fill in `url_for_pdf` for repository records that only carry a landing page."""
    for loc in locations:
        if loc.get("url_for_pdf") or loc.get("host_type") not in OPEN_HOST_TYPES:
            continue
        landing = loc.get("url_for_landing_page")
        if landing:
            loc["url_for_pdf"] = resolve_landing_pdf(fetcher, landing)
    return locations


def candidate_sources(work, locations: list[dict]) -> list[tuple[str, str, str]]:
    """Ordered (method, url, reason) candidates to try for one work.

    Repositories come before publishers: a green-OA deposit rarely blocks automated
    fetching, whereas the publisher copy frequently answers 403 to anything that is
    not a browser. Within each tier, order is stable so the ledger key is
    deterministic.
    """
    out: list[tuple[str, str, str]] = []
    if work["pmcid"]:
        out.append(("epmc_xml", EPMC_FULLTEXT.format(pmcid=work["pmcid"]), "PMCID present"))

    tiers: dict[str, list[tuple[str, str, str]]] = {"repo": [], "publisher": []}
    for loc in locations:
        url = loc.get("url_for_pdf")
        if not url:
            continue
        licence = loc.get("license") or ""
        host = loc.get("host_type")
        tier, method = (
            ("repo", "repository_pdf") if host in OPEN_HOST_TYPES
            else ("publisher", "publisher_pdf")
        )
        tiers[tier].append((method, url, f"{tier} copy, licence {licence or 'unstated'}"))

    seen: set[str] = set()
    for tier in ("repo", "publisher"):
        for method, url, reason in tiers[tier]:
            if url not in seen:
                seen.add(url)
                out.append((method, url, reason))

    # Last resort: a pointer recorded on the work itself, from OpenAlex or Europe PMC.
    # These mostly duplicate Unpaywall, but a handful of locations are known only to
    # those sources -- including for works Unpaywall reports as having no location.
    own = work["pdf_url"]
    if own and own not in seen:
        out.append((
            "indexed_pdf", own,
            f"location from work metadata, licence {work['licence'] or 'unstated'}",
        ))
    return out


def skip_reason(work, locations: list[dict]) -> str:
    # Reached only when no candidate url exists at all: every location that records a
    # `url_for_pdf` now becomes a candidate, whatever its licence says.
    if work["is_oa"]:
        return "flagged OA but no free location records a pdf url; use the landing page"
    return "no free copy located; use the landing page"


def verify(method: str, data: bytes) -> str | None:
    """Reject responses that are not actually the document we asked for."""
    if not data:
        return "empty response"
    head = data.lstrip()[:512].lower()
    if method.endswith("pdf"):
        if not data.lstrip().startswith(PDF_MAGIC):
            return "response is not a PDF (likely an HTML interstitial)"
    elif b"<html" in head and b"<article" not in head:
        return "response is HTML, not full-text XML"
    return None


def run(conn, fetcher: Fetcher, retry_failed: bool = False,
        min_score: float = ACCEPT_THRESHOLD, log=print) -> dict:
    offline = Fetcher(conn, offline=True)
    rows = conn.execute(
        """SELECT DISTINCT c.project_id, w.work_id, w.doi, w.pmcid, w.title,
                  w.is_oa, w.licence, w.pdf_url, w.oa_url, c.score
           FROM candidate c JOIN work w USING (work_id)
           LEFT JOIN decision d
                  ON d.project_id = c.project_id AND d.work_id = c.work_id
           WHERE (c.score >= ? OR d.verdict = 'accept')
             AND COALESCE(d.verdict, '') != 'reject'
           ORDER BY c.project_id, c.score DESC""",
        (min_score,),
    ).fetchall()

    stats = {"downloaded": 0, "reused": 0, "skipped": 0, "failed": 0, "settled": 0}
    manifests: dict[str, list[dict]] = {}
    # Manifests as they stand before this run, read once per project.
    recorded: dict[str, dict[str, dict]] = {}
    # A work linked to several projects is fetched once and copied.
    blobs: dict[str, Path] = {}

    for row in rows:
        project_id, work_id = row["project_id"], row["work_id"]
        locations = unpaywall_from_cache(offline, row["doi"]) if row["doi"] else []
        candidates = candidate_sources(row, locations)
        # Only when there is nothing to try at all is it worth spending a request on
        # resolving landing pages -- otherwise every settled work would re-fetch one.
        if not candidates:
            candidates = candidate_sources(row, enrich_locations(fetcher, locations))
        entry = {
            "work_id": work_id,
            "doi": row["doi"],
            "title": row["title"],
            "licence": next((loc.get("license") for loc in locations if loc.get("license")),
                            row["licence"]),
            "landing_page": f"https://doi.org/{row['doi']}" if row["doi"] else row["oa_url"],
        }

        papers_dir = PROJECTS_DIR / project_id / "papers"
        ledger_key = f"{project_id}|{work_id}"

        prior = task_row(conn, ledger_key, "fulltext", "download")
        held = held_copy(papers_dir, work_id)

        # Whatever the candidate list says now, a copy we already hold and recorded as
        # ok is the answer. Both halves of that matter: a hand-retrieved article has no
        # candidate at all to rediscover, and one retrieved as a PDF is invisible to a
        # candidate list that has since started proposing Europe PMC's XML instead.
        if prior is not None and prior["status"] == "ok" and held is not None:
            was = recorded.setdefault(project_id, recorded_entries(project_id)).get(work_id, {})
            if was.get("status") == "ok" and was.get("method"):
                entry.update({k: was[k] for k in PROVENANCE_FIELDS if k in was})
            elif is_manual(prior):
                entry.update(method="manual_browser", source_url=prior["query"])
            else:
                # Describe the file we hold, not the candidate currently ranked first:
                # once Europe PMC starts serving XML for a work whose PDF we already
                # took, candidates[0] no longer names what is on disk.
                method, url, _reason = next(
                    (c for c in candidates
                     if (".xml" if c[0] == "epmc_xml" else ".pdf") == held.suffix),
                    candidates[0])
                entry.update(method=method, source_url=url,
                             alternates=max(0, len(candidates) - 1))
            entry.update(status="ok", file=str(held.relative_to(REPO)),
                         bytes=held.stat().st_size,
                         sha256=hashlib.sha256(held.read_bytes()).hexdigest())
            manifests.setdefault(project_id, []).append(entry)
            stats["settled"] += 1
            continue

        if not candidates:
            entry.update(method="skip", source_url=None, status="skipped",
                         reason=skip_reason(row, locations))
            manifests.setdefault(project_id, []).append(entry)
            stats["skipped"] += 1
            continue

        method, url, reason = candidates[0]
        entry.update(method=method, source_url=url,
                     alternates=max(0, len(candidates) - 1))

        suffix = ".xml" if method == "epmc_xml" else ".pdf"
        dest = papers_dir / f"{safe_name(work_id)}{suffix}"

        # Key the ledger on the whole candidate list: if a new alternate location
        # appears, the task un-settles and the extra copy gets tried.
        url = "|".join(c[1] for c in candidates)

        # A settled *failure* leaves no file behind, so the ledger alone decides;
        # requiring a held file here would silently re-attempt it on every run.
        if is_settled(prior, retry_failed, url) and (
            prior["status"] != "ok" or dest.exists()
        ):
            stats["settled"] += 1
            if prior["status"] == "ok":
                entry.update(status="ok", file=str(dest.relative_to(REPO)),
                             bytes=dest.stat().st_size,
                             sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
            else:
                entry.update(status="unavailable", reason=prior["last_error"])
            manifests.setdefault(project_id, []).append(entry)
            continue

        papers_dir.mkdir(parents=True, exist_ok=True)
        data = None
        attempts: list[str] = []

        if work_id in blobs:
            data = blobs[work_id].read_bytes()
            stats["reused"] += 1
        else:
            # Walk the candidates: a publisher 403 is terminal for *that URL*, not for
            # the article, so fall through to the repository deposit behind it.
            for cand_method, cand_url, _reason in candidates:
                try:
                    payload = fetcher.get_bytes(cand_url, max_bytes=MAX_BYTES)
                    problem = verify(cand_method, payload)
                    if problem:
                        raise FetchError(problem)
                except FetchError as exc:
                    code = getattr(exc, "status", None)
                    attempts.append(f"{cand_url} -> {code or str(exc)[:60]}")
                    continue
                data = payload
                method, dest = cand_method, papers_dir / (
                    safe_name(work_id) + (".xml" if cand_method == "epmc_xml" else ".pdf")
                )
                entry["method"] = cand_method
                entry["source_url"] = cand_url
                stats["downloaded"] += 1
                break

        if data is None:
            blocked = any("403" in a or "401" in a for a in attempts)
            reason = (
                f"no candidate location yielded the document ({len(candidates)} tried); "
                + ("publisher refuses automated download" if blocked else "see attempts")
            )
            set_task(conn, ledger_key, "fulltext", "download",
                     "skipped" if blocked else "failed",
                     query=url, error=reason + " :: " + "; ".join(attempts)[:300])
            entry.update(status="unavailable", reason=reason, attempts=attempts)
            manifests.setdefault(project_id, []).append(entry)
            stats["skipped" if blocked else "failed"] += 1
            continue

        if entry.get("attempts_failed") is None and attempts:
            entry["attempts_failed"] = attempts

        dest.write_bytes(data)
        blobs.setdefault(work_id, dest)
        digest = hashlib.sha256(data).hexdigest()
        set_task(conn, ledger_key, "fulltext", "download", "ok",
                 query=url, result_count=len(data))
        entry.update(status="ok", file=str(dest.relative_to(REPO)),
                     bytes=len(data), sha256=digest)
        manifests.setdefault(project_id, []).append(entry)

        if (stats["downloaded"] + stats["reused"]) % 25 == 0:
            conn.commit()
            log(f"  {stats}")

    conn.commit()
    for project_id, entries in manifests.items():
        path = PROJECTS_DIR / project_id / "papers" / "manifest.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "project_id": project_id,
            "policy": "every free location, any licence; see scripts/scrape/fulltext.py",
            "entries": sorted(entries, key=lambda e: e["work_id"]),
        }
        # No timestamp in the payload: it would churn every run for no information
        # the ledger does not already hold.
        content = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
    log(f"full text: {stats} across {len(manifests)} projects")
    return stats
