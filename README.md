# eq-graph

A research knowledge graph of the EuroQol Research Foundation's funded projects and the publications they produced.

EuroQol has funded over a thousand research projects, producing a large body of literature on EQ-5D and related instruments.
That literature holds detailed evidence on how the instruments perform across populations, countries, clinical areas and methods —
but it is distributed across individual papers and is not searchable or aggregable at the portfolio level.
This project extracts that evidence into a graph and makes it queryable.

Funded as EuroQol seed grant **2582-SG** (1.3 Seed grant), €28,404, running **2026-07-01 to 2026-12-31**.
The submitted proposal is in [`docs/submitted-proposal.pdf`](docs/submitted-proposal.pdf) and is the authoritative statement of scope;
this README summarises it and records how far the work has got.

Team: Paul Schneider (PI, paul@shoulde.rs), Sofia Fabishevskaya (co-I), Kazik Pogoda (advisor).
Executed by [Shoulders](https://shoulde.rs).

## Scope

The proposal defines three stages.

| # | Stage | Status |
| --- | --- | --- |
| 1 | **Corpus assembly** — resolve every funded project to its publications, retrieve full texts | largely done, see below |
| 2 | **Schema + LLM extraction pipeline** — extract structured data from full text, refine the schema iteratively | graph model designed, extraction not started |
| 3 | **Graph database + web application** — Neo4j, visual summaries, structured search, natural-language queries | schema DDL written, nothing loaded |

Deliverables promised to EuroQol:

1. Populated knowledge graph of the funded projects
2. Web application with AI-assisted search and visualisation (12 months hosting)
3. Open-source code repository
4. Plenary presentation with live demonstration (2027)
5. Final report

### What gets extracted (stage 2)

Per paper: study design;
sample characteristics (size, age range, sex distribution, clinical condition, severity, recruitment setting);
instrument versions and administration modes;
statistical methods and models;
comparator instruments used alongside EQ-5D;
key findings (value set coefficients, measurement properties, population norms).

Initial entity types: Study, Instrument (version-specific — EQ-5D-3L, EQ-5D-5L, EQ-5D-Y, EQ-HWB), Population, Method, Country, Author, Institution, Working Group, Value Set, Outcome.
The schema is expected to **grow from the data**: the pipeline flags what does not fit the current categories, and a researcher decides whether to widen the schema.

Accuracy is to be assessed against ~50 papers hand-coded by a research assistant, reporting per-field extraction accuracy.

### Explicitly out of scope for the seed grant

The broader EQ-5D literature (17,000+ PubMed publications) is a possible follow-on, not part of this grant.
The seed grant covers the *funded portfolio* and produces the evidence needed to judge whether the wider expansion is warranted.

A prior demonstration built from 944 project abstracts alone (2,116 nodes, 8,213 edges) is at <https://shoulde.rs/eq-graph>.
It is not in this repository; this work supersedes it by going to full text.

## Where things stand

Stage 1 is implemented as a resumable scraping pipeline.
From the current run over all 1024 projects:

- **209 projects (20.4%)** have a publication linked at accepted confidence; 243 have no candidate at all; the remaining 572 sit in review or name-only bands.
- **2603 works** in the pool, 305 linked at accepted confidence.
- **287 full texts on disk** (114 MB), mostly Europe PMC JATS XML.

Read [`reports/coverage.md`](reports/coverage.md) before drawing conclusions from those numbers,
and [`reports/no-publications.md`](reports/no-publications.md) for the caveat that matters most:
a project drops off the "no publications" list as soon as the *weakest* rule fires, so absence from it is not resolution.

The hard ceiling on stage 1 is stated in [`scripts/README.md`](scripts/README.md#evidence-and-scoring):
344 PIs hold 1024 grants, so name-and-date evidence identifies *a* paper by that PI, never *which grant* funded it.
That band is a review pool by construction and cannot be promoted by tuning.

## Repository map

| Path | What it holds |
| --- | --- |
| [`input/`](input/README.md) | The immutable record of what was collected — the source CSV and its documented schema |
| [`input/projects/`](input/projects/README.md) | One directory per funded project: `project.json`, `abstract.txt`, `publications.json`, `papers/` |
| [`scripts/`](scripts/README.md) | The scraping pipeline and the CSV splitter |
| [`graph/`](graph/) | Neo4j schema DDL — constraints, indexes, and the declarative `GRAPH TYPE` equivalent |
| [`reports/`](reports/) | Generated coverage and gap reports |
| [`docs/`](docs/) | The submitted proposal and [the graph model](docs/graph-model.md) |
| `cache/`, `state/` | Gitignored: raw HTTP responses and the SQLite ledger |

Derived graph artefacts do not belong under `input/` — that tree stays the record of what was collected, not of what was inferred from it.

## Running it

```sh
python3 scripts/split_projects.py    # CSV -> input/projects/*
python3 scripts/scrape.py all        # discover -> match -> enrich -> harvest -> mine -> export -> fulltext -> report
python3 scripts/scrape.py status     # what the ledger currently knows
```

Python 3 with `requests` as the only third-party dependency.
Europe PMC, Crossref and Unpaywall need no key;
the CORE harvest stage skips itself unless `CORE_API_KEY` is set (free).
Every source in use is free — OpenAlex is deliberately *not* used, being metered at a rate a single funders query exhausts.

Interrupting is safe — settled tasks are skipped on the next run.
Only `discover`, `enrich`, `harvest` and `fulltext` touch the network;
everything else replays the cache, so refining the matcher costs nothing.
[`scripts/README.md`](scripts/README.md) explains the three layers, the evidence weights, and the curation table that overrides the matcher permanently.

Set `SCRAPE_CONTACT_EMAIL` to change the address sent in the User-Agent.

## Conventions and constraints

- **This repository is private.**
  Downloaded full texts are committed on that basis;
  two of them carry publisher TDM licences that permit mining but not redistribution, so making the repository public means revisiting those first.
  The open-source deliverable is the code, not the corpus.
- No paywall circumvention.
  A publisher refusal is recorded with its reason, never worked around.
- No personal data is collected.
  Everything in the graph comes from published papers and the public project listing.
- [`CLAUDE.md`](CLAUDE.md) collects the gotchas that cost time and are not visible in the source —
  publisher fetch behaviour, index coverage limits, paging traps, determinism requirements.
  Read it before touching the pipeline, and add to it when something surprises you.

## Known discrepancy

The proposal describes a portfolio of 944 projects.
The CSV exported on 2026-07-28 lists **1024**; the extra rows are later awards.
Where a number in the proposal and a number in this repository disagree, the repository is current.