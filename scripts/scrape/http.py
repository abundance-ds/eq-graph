"""Polite, caching HTTP layer.

Every response is written to a content-addressed cache keyed by the canonical URL.
Nothing downstream is allowed to touch the network: the match stage reads only from
this cache, so improving a matcher costs zero requests.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

import requests

from .db import DB_PATH, now

REPO = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO / "cache"

CONTACT_EMAIL = os.environ.get("SCRAPE_CONTACT_EMAIL", "morisil@xemantic.com")
USER_AGENT = f"eq-graph/0.1 (research knowledge graph; mailto:{CONTACT_EMAIL})"

# Minimum seconds between requests to the same host. Europe PMC and Crossref both
# publish generous limits; this keeps us well inside them without parallelism.
HOST_DELAY = {
    "www.ebi.ac.uk": 0.34,
    "api.crossref.org": 0.34,
    "api.unpaywall.org": 0.12,
    "api.openalex.org": 0.34,
}
DEFAULT_DELAY = 0.5

RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 4


class FetchError(RuntimeError):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


@dataclass
class Response:
    url: str
    status: int
    body: str
    fetched_at: str
    from_cache: bool

    def json(self):
        return json.loads(self.body)


def canonical_url(url: str, params: dict | None = None) -> str:
    """Stable URL form so the same logical request always hits the same cache key."""
    if params:
        query = urllib.parse.urlencode(sorted(params.items()), doseq=True)
        url = f"{url}?{query}"
    return url


def cache_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def cache_path(key: str) -> Path:
    return CACHE_DIR / key[:2] / f"{key}.json"


class Fetcher:
    """Cache-first HTTP client with per-host throttling and bounded retries."""

    def __init__(self, conn, offline: bool = False, force: bool = False):
        self.conn = conn
        self.offline = offline
        self.force = force
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
        self._last_request: dict[str, float] = {}
        self.stats = {"hits": 0, "misses": 0, "errors": 0}

    def _throttle(self, host: str) -> None:
        delay = HOST_DELAY.get(host, DEFAULT_DELAY)
        elapsed = time.monotonic() - self._last_request.get(host, 0.0)
        if elapsed < delay:
            time.sleep(delay - elapsed)
        self._last_request[host] = time.monotonic()

    def get(self, url: str, params: dict | None = None,
            headers: dict | None = None) -> Response:
        full = canonical_url(url, params)
        key = cache_key(full)
        path = cache_path(key)

        if path.exists() and not self.force:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.stats["hits"] += 1
            cached = Response(full, payload["status"], payload["body"],
                              payload["fetched_at"], from_cache=True)
            # 4xx other than 404 were transient-ish (auth/limits); let them re-fetch.
            if cached.status < 400 or cached.status == 404:
                if cached.status >= 400:
                    raise FetchError(f"cached HTTP {cached.status} for {full}", cached.status)
                return cached

        if self.offline:
            raise FetchError(f"offline and not cached: {full}", None)

        host = urllib.parse.urlparse(full).netloc
        last_error: Exception | None = None

        for attempt in range(1, MAX_ATTEMPTS + 1):
            self._throttle(host)
            try:
                resp = self.session.get(full, timeout=60, headers=headers or {})
            except requests.RequestException as exc:
                last_error = exc
                time.sleep(min(2**attempt, 30))
                continue

            if resp.status_code in RETRY_STATUS and attempt < MAX_ATTEMPTS:
                wait = resp.headers.get("Retry-After")
                time.sleep(float(wait) if wait and wait.isdigit() else min(2**attempt, 30))
                last_error = FetchError(f"HTTP {resp.status_code}", resp.status_code)
                continue

            self._store(full, key, path, resp.status_code, resp.text)
            self.stats["misses"] += 1
            if resp.status_code >= 400:
                self.stats["errors"] += 1
                raise FetchError(f"HTTP {resp.status_code} for {full}", resp.status_code)
            return Response(full, resp.status_code, resp.text, now(), from_cache=False)

        self.stats["errors"] += 1
        status = getattr(last_error, "status", None)
        raise FetchError(f"giving up on {full}: {last_error}", status)

    def get_bytes(self, url: str, max_bytes: int = 80 * 1024 * 1024) -> bytes:
        """Fetch a binary document.

        Deliberately not routed through the JSON cache -- the downloaded file on disk
        *is* the cache, and the caller skips this call when it already exists.
        """
        if self.offline:
            raise FetchError(f"offline, cannot download: {url}", None)
        host = urllib.parse.urlparse(url).netloc
        last_error: Exception | None = None

        for attempt in range(1, MAX_ATTEMPTS + 1):
            self._throttle(host)
            try:
                resp = self.session.get(url, timeout=120, stream=True,
                                        headers={"Accept": "*/*"})
            except requests.RequestException as exc:
                last_error = exc
                time.sleep(min(2**attempt, 30))
                continue

            if resp.status_code in RETRY_STATUS and attempt < MAX_ATTEMPTS:
                time.sleep(min(2**attempt, 30))
                last_error = FetchError(f"HTTP {resp.status_code}", resp.status_code)
                continue
            if resp.status_code >= 400:
                self.stats["errors"] += 1
                raise FetchError(f"HTTP {resp.status_code} for {url}", resp.status_code)

            chunks, total = [], 0
            for chunk in resp.iter_content(65536):
                total += len(chunk)
                if total > max_bytes:
                    raise FetchError(f"exceeds {max_bytes} bytes: {url}", resp.status_code)
                chunks.append(chunk)
            self.stats["misses"] += 1
            data = b"".join(chunks)
            self.conn.execute(
                """INSERT INTO fetch(url, cache_key, http_status, bytes, fetched_at)
                   VALUES (?,?,?,?,?)
                   ON CONFLICT(url) DO UPDATE SET http_status=excluded.http_status,
                     bytes=excluded.bytes, fetched_at=excluded.fetched_at""",
                (url, hashlib.sha256(data).hexdigest(), resp.status_code, len(data), now()),
            )
            return data

        self.stats["errors"] += 1
        raise FetchError(f"giving up on {url}: {last_error}",
                         getattr(last_error, "status", None))

    def _store(self, url: str, key: str, path: Path, status: int, body: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        stamp = now()
        path.write_text(
            json.dumps({"url": url, "status": status, "fetched_at": stamp, "body": body},
                       ensure_ascii=False),
            encoding="utf-8",
        )
        self.conn.execute(
            """INSERT INTO fetch(url, cache_key, http_status, bytes, fetched_at)
               VALUES (?,?,?,?,?)
               ON CONFLICT(url) DO UPDATE SET
                 cache_key=excluded.cache_key, http_status=excluded.http_status,
                 bytes=excluded.bytes, fetched_at=excluded.fetched_at""",
            (url, key, status, len(body.encode("utf-8")), stamp),
        )
        self.conn.commit()
