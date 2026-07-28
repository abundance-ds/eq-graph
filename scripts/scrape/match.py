"""Match stage: replay cached responses and link projects to works.

This stage is a pure function of the HTTP cache — it runs the fetcher in offline
mode, so refining the heuristics below costs no network requests. Bump
EXTRACTOR_VERSION whenever the scoring changes; rows from older versions are dropped
on the next run. The `decision` table is read-only here.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path

from . import sources
from .db import now
from .http import FetchError, Fetcher

REPO = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO / "input" / "projects"

# Stamped on every candidate row so exported links say which matcher produced them.
# Bump on any scoring change; `run()` rebuilds the candidate table wholesale.
EXTRACTOR_VERSION = 3

# Score at or above which a link is treated as established rather than a suggestion.
ACCEPT_THRESHOLD = 0.85
# Must sit strictly above the weakest rule's weight, or the weak band is unreachable
# and name-only guesses get exported as review candidates.
REVIEW_THRESHOLD = 0.60

WEIGHTS = {
    "grant_id_acknowledged": 1.00,  # the paper's own text names this project id
    "grant_id_structured": 1.00,  # the id is in the indexed grant metadata
    "grant_id_fulltext": 0.90,    # the id appears in the article text/acknowledgement
    "title_exact": 0.95,
    "title_strong": 0.80,         # >=0.95 similarity
    "title_fuzzy": 0.65,          # >=0.88 similarity AND a PI surname among the authors
    "ack_pi_year": 0.45,          # EuroQol-acknowledged, PI is an author, plausible year
}

TITLES_RE = re.compile(
    r"\b(prof(essor)?|dr|phd|ph\.d|md|m\.d|msc|m\.sc|bsc|mph|rn|mbbs|dphil)\b\.?",
    re.IGNORECASE,
)
SPLIT_RE = re.compile(r"\s*(?:;|&|/|\band\b|,\s*(?=[A-Z][a-z]+\s+[A-Z]))\s*")
STOPWORDS = {
    "a", "an", "and", "the", "of", "in", "for", "on", "to", "with", "by", "from",
    "using", "study", "based", "into", "at", "as", "its", "via",
}


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def title_tokens(title: str) -> frozenset[str]:
    return frozenset(t for t in normalize_title(title).split() if t not in STOPWORDS and len(t) > 2)


def parse_pi_names(raw: str) -> list[tuple[str, frozenset[str]]]:
    """Split the free-text PI cell into (surname, given-name initials) pairs.

    Surname alone is far too weak: matching every name token made common surnames
    collide with authors' *first* names and produced ~79 spurious links per project.
    Initials are a set rather than one letter because "A. Simon Pickard" is bylined
    "Pickard AS" by Europe PMC -- comparing only the first given name would miss it.
    """
    cleaned = TITLES_RE.sub("", raw or "")
    names: list[tuple[str, frozenset[str]]] = []
    for part in SPLIT_RE.split(cleaned):
        tokens = [t.strip(".") for t in part.replace(",", " ").split()]
        tokens = [t for t in tokens if t and t.isalpha()]
        if len(tokens) < 2:
            continue
        surname = tokens[-1].lower()
        initials = frozenset(t[0].lower() for t in tokens[:-1])
        if len(surname) > 2 and initials:
            names.append((surname, initials))
    return list(dict.fromkeys(names))


@dataclass
class Project:
    project_id: str
    title: str
    pi_raw: str
    start_year: int | None
    end_year: int | None
    surnames: list[str] = field(default_factory=list)
    tokens: frozenset[str] = frozenset()

    @classmethod
    def load(cls, path: Path) -> "Project":
        data = json.loads(path.read_text(encoding="utf-8"))
        project = cls(
            project_id=data["project_id"],
            title=data["title"],
            pi_raw=data["pi_name_raw"],
            start_year=data["start_year"],
            end_year=data["end_year"],
        )
        project.surnames = parse_pi_names(project.pi_raw)
        project.tokens = title_tokens(project.title)
        return project


def load_projects() -> list[Project]:
    return [
        Project.load(d / "project.json")
        for d in sorted(PROJECTS_DIR.iterdir())
        if d.is_dir() and (d / "project.json").exists()
    ]


def plausible_year(project: Project, year: int | None) -> bool:
    """Publications trail the grant; allow a wide but not unlimited window."""
    if year is None or project.start_year is None:
        return False
    end = project.end_year or project.start_year + 4
    return project.start_year - 1 <= year <= end + 6


def author_names(work: dict) -> list[tuple[str, frozenset[str]]]:
    """(surname, initials) per author, in byline order."""
    parsed: list[tuple[str, frozenset[str]]] = []
    for author in work.get("authors") or []:
        last = (author.get("last_name") or "").strip().lower()
        full = (author.get("full_name") or "").strip().lower()
        if not last and full:
            last = full.split()[-1]
        tokens = [t.strip(".") for t in full.split() if t.strip(".")]
        initials: set[str] = set()
        if tokens:
            # Europe PMC bylines are "Surname AB"; Crossref gives "Given Surname".
            if tokens[0] == last:
                initials = {c for token in tokens[1:] for c in token if c.isalpha()}
            else:
                initials = {t[0] for t in tokens[:-1] if t}
        parsed.append((last, frozenset(initials)))
    return parsed


def pi_is_lead_author(project: "Project", work: dict) -> bool:
    """True when a PI appears as first or last author -- the usual place for one."""
    authors = author_names(work)
    if not authors:
        return False
    for position in {0, len(authors) - 1}:
        surname, initials = authors[position]
        for pi_surname, pi_initials in project.surnames:
            if surname != pi_surname:
                continue
            if not initials or not pi_initials or (initials & pi_initials):
                return True
    return False


def grant_ids(work: dict) -> set[str]:
    return {
        str(g.get("grant_id")).strip().lower()
        for g in work.get("grants") or []
        if g.get("grant_id")
    }


class WorkPool:
    """Accumulates works from every replayed response, merging duplicates."""

    def __init__(self):
        self.works: dict[str, dict] = {}
        self.hits: dict[str, set[tuple[str, str]]] = {}  # work_id -> {(project_id, kind)}
        self.corpus_ids: set[str] = set()  # seen in a funder-wide sweep

    def add(self, work: dict, origin: tuple[str, str] | None = None,
            corpus: bool = False) -> str:
        work_id = work["work_id"]
        existing = self.works.get(work_id)
        if existing:
            for key, value in work.items():
                if not existing.get(key) and value:
                    existing[key] = value
            existing.setdefault("sources", set())
            existing["sources"].add(work["source"])
        else:
            work = dict(work)
            work["sources"] = {work["source"]}
            self.works[work_id] = work
        if origin:
            self.hits.setdefault(work_id, set()).add(origin)
        if corpus:
            self.corpus_ids.add(work_id)
        return work_id


def replay(fetcher: Fetcher, projects: list[Project], log=print) -> WorkPool:
    """Rebuild the work pool from cached responses only."""
    pool = WorkPool()

    def collect(origin: tuple[str, str] | None, adapter, iterator,
                corpus: bool = False) -> int:
        try:
            count = 0
            for item in iterator:
                work = adapter(item)
                if work:
                    pool.add(work, origin, corpus=corpus)
                    count += 1
            return count
        except (FetchError, RuntimeError):
            return 0  # not cached: this query was never fetched, nothing to replay

    collect(None, sources.crossref_to_work, sources.crossref_funder_works(fetcher),
            corpus=True)
    collect(None, sources.epmc_to_work,
            sources.epmc_search(fetcher, sources.epmc_ack_query()), corpus=True)
    collect(None, sources.epmc_to_work,
            sources.epmc_search(fetcher, sources.epmc_phrase_query()), corpus=True)
    log(f"corpus sweeps: {len(pool.works)} works")

    for project in projects:
        for kind, query in sources.epmc_grant_queries(project.project_id):
            collect((project.project_id, kind), sources.epmc_to_work,
                    sources.epmc_search(fetcher, query, max_pages=3))
        title_query = sources.epmc_title_query(project.title, project.surnames)
        if title_query:
            collect((project.project_id, "title_query"), sources.epmc_to_work,
                    sources.epmc_search(fetcher, title_query, max_pages=2))

    log(f"after per-project replay: {len(pool.works)} works")
    return pool


def load_mentions(conn) -> dict[str, set[str]]:
    """project_id -> {work_id} mined from full text (see mine.py)."""
    out: dict[str, set[str]] = {}
    for row in conn.execute("SELECT project_id, work_id FROM fulltext_mention"):
        out.setdefault(row["project_id"], set()).add(row["work_id"])
    return out


def score_project(project: Project, pool: WorkPool, token_index: dict,
                  mentions: dict[str, set[str]] | None = None) -> dict[str, dict]:
    """Return {work_id: {"score": float, "evidence": [...]}} for one project."""
    found: dict[str, list[dict]] = {}
    pid_lower = project.project_id.lower()

    def add(work_id: str, kind: str, detail: str) -> None:
        found.setdefault(work_id, []).append(
            {"kind": kind, "detail": detail, "weight": WEIGHTS[kind]}
        )

    # 0. The work's own full text names this project id near a EuroQol mention.
    for work_id in sorted((mentions or {}).get(project.project_id, ())):
        if work_id in pool.works:
            add(work_id, "grant_id_acknowledged",
                "project id printed in the article's own acknowledgement/funding text")

    # 1. Targeted grant-id queries that returned this work. A GRANT_ID hit only counts
    #    once the agency confirms EuroQol -- grant numbers are reused across funders.
    # Sets are iterated in sorted order throughout: their natural order varies with
    # Python's per-process string hash seed, which would make the exported evidence
    # text and row order differ between identical runs.
    for work_id, origins in pool.hits.items():
        work = pool.works[work_id]
        for origin_pid, kind in sorted(origins):
            if origin_pid != project.project_id or kind not in WEIGHTS:
                continue
            if kind == "grant_id_structured" and not sources.is_euroqol_grant(
                work, project.project_id
            ):
                continue
            add(work_id, kind, f"returned by {kind} query for {project.project_id}")

    # 2. The same confirmed grant credit, found anywhere else in the pool.
    for work_id, work in pool.works.items():
        if pid_lower in grant_ids(work) and sources.is_euroqol_grant(work, project.project_id):
            add(work_id, "grant_id_structured",
                f"grant id {project.project_id} credited to EuroQol in metadata")

    # 3. Title agreement, restricted to works sharing enough rare tokens.
    if project.tokens:
        counts: dict[str, int] = {}
        for token in project.tokens:
            for work_id in token_index.get(token, ()):
                counts[work_id] = counts.get(work_id, 0) + 1
        norm_project = normalize_title(project.title)
        for work_id, shared in counts.items():
            work = pool.works[work_id]
            work_tokens = title_tokens(work.get("title") or "")
            if not work_tokens or shared / max(len(project.tokens), 1) < 0.5:
                continue
            norm_work = normalize_title(work.get("title") or "")
            if norm_work == norm_project:
                add(work_id, "title_exact", "normalized titles identical")
                continue
            similarity = SequenceMatcher(None, norm_project, norm_work).ratio()
            if similarity >= 0.95:
                add(work_id, "title_strong", f"title similarity {similarity:.2f}")
            elif similarity >= 0.88 and pi_is_lead_author(project, work):
                add(work_id, "title_fuzzy",
                    f"title similarity {similarity:.2f} + PI as lead author")

    # 4. Weak fallback, and only within the funder-acknowledged corpus: the work
    #    credits EuroQol, the PI is an author, and the year fits the grant window.
    for work_id in sorted(pool.corpus_ids):
        work = pool.works[work_id]
        if work_id in found or not project.surnames:
            continue
        if pi_is_lead_author(project, work) and plausible_year(project, work.get("year")):
            add(work_id, "ack_pi_year",
                "EuroQol-acknowledged work with the PI as lead author, in window")

    def dedupe(evidence: list[dict]) -> list[dict]:
        """One entry per kind -- the targeted query and the pool scan often agree."""
        best: dict[str, dict] = {}
        for item in evidence:
            best.setdefault(item["kind"], item)
        return sorted(best.values(), key=lambda e: -e["weight"])

    return {
        work_id: {
            "score": max(e["weight"] for e in evidence),
            "evidence": dedupe(evidence),
        }
        for work_id, evidence in found.items()
    }


def build_token_index(pool: WorkPool) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for work_id, work in pool.works.items():
        for token in title_tokens(work.get("title") or ""):
            index.setdefault(token, []).append(work_id)
    return index


def run(conn, log=print) -> dict:
    fetcher = Fetcher(conn, offline=True)
    projects = load_projects()
    pool = replay(fetcher, projects, log=log)
    token_index = build_token_index(pool)
    mentions = load_mentions(conn)
    if mentions:
        log(f"full-text grant mentions: {sum(len(v) for v in mentions.values())} "
            f"across {len(mentions)} projects")

    stamp = now()
    for work_id, work in pool.works.items():
        conn.execute(
            """INSERT INTO work(work_id, doi, pmid, pmcid, title, journal, year, authors,
                                is_oa, oa_url, licence, pdf_url, sources, raw_ref, updated_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(work_id) DO UPDATE SET
                 doi=COALESCE(work.doi, excluded.doi),
                 pmid=COALESCE(work.pmid, excluded.pmid),
                 pmcid=COALESCE(work.pmcid, excluded.pmcid),
                 title=excluded.title, journal=excluded.journal, year=excluded.year,
                 authors=excluded.authors, is_oa=MAX(work.is_oa, excluded.is_oa),
                 oa_url=COALESCE(excluded.oa_url, work.oa_url),
                 licence=COALESCE(excluded.licence, work.licence),
                 pdf_url=COALESCE(excluded.pdf_url, work.pdf_url),
                 sources=excluded.sources, raw_ref=excluded.raw_ref,
                 updated_at=excluded.updated_at""",
            (
                work_id, work.get("doi"), work.get("pmid"), work.get("pmcid"),
                work.get("title"), work.get("journal"), work.get("year"),
                sources.dumps(work.get("authors")), work.get("is_oa"),
                work.get("oa_url"), work.get("licence"), work.get("pdf_url"),
                sources.dumps(sorted(work.get("sources", []))),
                sources.dumps(work.get("grants")), stamp,
            ),
        )

    conn.execute("DELETE FROM candidate")
    total = 0
    for project in projects:
        for work_id, result in sorted(
            score_project(project, pool, token_index, mentions).items(),
            key=lambda item: (-item[1]["score"], item[0]),
        ):
            conn.execute(
                """INSERT INTO candidate(project_id, work_id, score, evidence,
                                         extractor_version, updated_at)
                   VALUES (?,?,?,?,?,?)""",
                (project.project_id, work_id, result["score"],
                 sources.dumps(result["evidence"]), EXTRACTOR_VERSION, stamp),
            )
            total += 1
    conn.commit()
    log(f"{total} candidate links across {len(projects)} projects")
    return {"works": len(pool.works), "candidates": total, "projects": len(projects)}
