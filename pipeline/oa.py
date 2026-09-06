"""Shared OpenAlex helpers: disk-cached HTTP, polite pool, replayable.

Cache key excludes credentials, so cache survives key changes. Set
OPENALEX_API_KEY to use a paid key (bills ~$0.001/request against a daily
budget, resets midnight UTC); default is the free polite pool.
"""
import hashlib
import json
import os
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "http"
MAILTO = "pschneider@abundanceds.com"
API_KEY = os.environ.get("OPENALEX_API_KEY", "")
EUROQOL_FUNDER = "F4320323856"
EQ_SEARCH = 'EQ-5D OR EuroQol OR EQ-HWB OR "health-related quality of life"'


def get(url: str, cache_key: str | None = None) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / (hashlib.sha1((cache_key or url).encode()).hexdigest() + ".json")
    if p.exists():
        return json.loads(p.read_text())
    for attempt in range(8):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.loads(r.read())
            p.write_text(json.dumps(data))
            time.sleep(0.12)  # stay well under 10 req/s
            return data
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503):
                time.sleep(min(60, 2 ** attempt))  # transient throttle windows can last ~1 min
                continue
            raise
        except Exception:
            time.sleep(min(60, 2 ** attempt))
    raise RuntimeError(f"failed after retries: {url}")


def api(path: str, **params) -> dict:
    key = f"https://api.openalex.org/{path}?{urllib.parse.urlencode(params)}"
    params["mailto"] = MAILTO
    if API_KEY:
        params["api_key"] = API_KEY
    url = f"https://api.openalex.org/{path}?{urllib.parse.urlencode(params)}"
    return get(url, cache_key=key)


def api_all(path: str, **params) -> list:
    """Cursor-paginate through all results. Replayable: each page is one
    cached request (cursor value is part of the URL/cache key)."""
    results = []
    cursor = "*"
    while cursor:
        d = api(path, **params, **{"per-page": 200, "cursor": cursor})
        results.extend(d["results"])
        cursor = d["meta"].get("next_cursor")
    return results
