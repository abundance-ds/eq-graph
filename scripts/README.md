# Scraping pipeline

Resolves each EuroQol funded project to the publications it produced, and records
where the full text can be obtained.

```sh
python3 scripts/scrape.py all        # discover -> match -> enrich -> export -> report
python3 scripts/scrape.py status     # what the ledger currently knows
```

## Three layers

The design exists to make one thing cheap: **changing your mind about how matching
works, without re-crawling.**

| Layer | Where | Rebuilt from |
| --- | --- | --- |
| Raw responses | `cache/` (gitignored) | the network |
| State ledger | `state/scrape.db` (gitignored) | the cache + your curation |
| Derived output | `input/projects/*/publications.json`, `reports/` | the ledger |

Only `discover` and `enrich` touch the network. `match` runs the same HTTP client in
offline mode, so it reads exclusively from `cache/` — replaying all 1024 projects
takes about a second and costs nothing. Refining a heuristic means editing
`match.py` and rerunning `match`, never re-fetching.

## Stages

| Stage | Network | What it does |
| --- | --- | --- |
| `discover` | yes | Issues corpus sweeps and per-project queries; fills the cache; records every attempt |
| `match` | no | Replays the cache, scores project↔work links, writes `work` and `candidate` |
| `enrich` | yes | Unpaywall lookup per DOI for OA status and a free full-text location |
| `fulltext` | yes | Downloads openly licensed full texts into each project's `papers/` |
| `export` | no | Writes `publications.json` into each project directory |
| `report` | no | Coverage gap report in `reports/` |

## Resuming and refining

Interrupting at any point is safe. A task is *settled* when its status is `ok`,
`empty`, or `skipped`; settled tasks are skipped on the next run.

- `empty` means the source genuinely returned nothing. It is deliberately distinct
  from `failed`, so the ~hundreds of projects no source can resolve are not retried
  forever.
- `--retry-failed` re-attempts transient failures.
- `--force` bypasses the cache and re-fetches.
- Each task stores the exact query that produced it. **Change a query in
  `sources.py` and the affected tasks un-settle themselves** — no manual
  invalidation, no stale results silently surviving a refinement.
- `match` rebuilds the candidate table wholesale, so a scoring change needs no
  invalidation; `match.EXTRACTOR_VERSION` stamps each row with the matcher that
  produced it.

## Evidence and scoring

A link carries the evidence that produced it, not just a number:

| Kind | Weight | Meaning |
| --- | ---: | --- |
| `grant_id_structured` | 1.00 | Indexed grant metadata credits this id **to EuroQol** |
| `title_exact` | 0.95 | Normalized project and article titles identical |
| `grant_id_fulltext` | 0.90 | Id appears in the text of a EuroQol-acknowledged article |
| `title_strong` | 0.80 | ≥0.95 title similarity |
| `title_fuzzy` | 0.65 | ≥0.88 title similarity and the PI is first or last author |
| `ack_pi_year` | 0.45 | EuroQol-acknowledged, PI is lead author, year fits the window |

`>= 0.85` is exported as `accepted`, `>= 0.45` as `review`, the rest as `weak`.

The bottom rule cannot be promoted by tuning: 344 PIs hold 1024 grants, so name and
date evidence identifies *a* paper by that PI, never *which grant* funded it. That
band is a review pool. It is capped at 15 entries per project in the export, with
`weak_omitted` recording what was dropped.

## Curation

`decision` is the one table the automated stages never write. Rows there override the
matcher permanently — `reject` removes a link from the export, `accept` promotes it
regardless of score — and survive every rerun, including a full re-match.

```sql
INSERT INTO decision(project_id, work_id, verdict, note, decided_by, decided_at)
VALUES ('1489-RA', 'doi:10.1007/s11136-025-03930-1', 'accept', 'checked ack section',
        'kazik', datetime('now'));
```

## Sources

Europe PMC (search + acknowledgement index), Crossref (funder `501100006419`) and
Unpaywall — all free, no API key, contacted with an identifying User-Agent and
per-host throttling. Set `SCRAPE_CONTACT_EMAIL` to change the contact address.

OpenAlex is **not** used: it is now metered, and its free daily allowance is a
fraction of a cent. `reports/coverage.md` quantifies what it would add.

## Full-text policy

Only openly licensed copies are downloaded, in this order of preference:

1. **Europe PMC JATS XML** for anything with a PMCID. Europe PMC serves `fullTextXML`
   only for its open-access subset, so a 200 *is* the licence check — and the result
   is structured text rather than a PDF to re-parse later. This covers the large
   majority (171 of 177 files).
2. **Repository-hosted PDFs** (green OA) as recorded by Unpaywall.
3. **Publisher PDFs only under an explicit Creative Commons licence.** An Elsevier
   "TDM user licence" is not a redistribution licence and does not qualify.

Everything else is skipped with a recorded reason and its DOI landing page. Downloads
are checked for magic bytes, so a paywall interstitial cannot be stored as a PDF.

A publisher answering 401/403 is recorded as `skipped`, not `failed`: it is a
deliberate refusal, so retrying cannot succeed and re-hammering the endpoint would be
rude. `--retry-failed` therefore never touches them.

Downloaded files under `papers/` are committed, alongside a `papers/manifest.json`
recording the source URL, licence, byte count and SHA-256 of each one — and the
reason for every publication deliberately *not* fetched.

This is safe because the repository is **private**. Two repository-hosted PDFs carry
an Elsevier "TDM user licence", which permits text and data mining but not
redistribution; making this repository public would mean revisiting those. The rest
are Europe PMC's open-access subset or explicitly Creative Commons.
