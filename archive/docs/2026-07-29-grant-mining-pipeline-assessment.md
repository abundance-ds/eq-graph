# Empirical findings from `abundance-ds/eq-graph`

Repository assessed: `git@github.com:abundance-ds/eq-graph.git`

- Branch: `main`
- Commit: `68ebeab6b6a55d8123e104f92f73eaf1ad1698ac`
- Commit date: 2026-07-29 01:35:39 +02:00
- Commit message: `Retrieve the 15 papers publishers refuse to serve to scripts`
- Assessment date: 2026-07-29

## Project-data comparison

The local project file contains 944 projects. The assessed repository contains a
public EuroQol export with 1,024 projects, downloaded on 2026-07-28.

| Comparison | Projects |
| --- | ---: |
| Local dataset | 944 |
| Assessed repository | 1,024 |
| Project IDs present in both | 942 |
| Present only in assessed repository | 82 |
| Present only in local dataset | 2 |

The two local-only project IDs are:

- `2015080`
- `2016400`

Among the 942 shared projects:

- Project ID, title, PI/applicant name, and working group agree.
- 82 abstracts differ.

The assessed repository's CSV has four fields absent from the local CSV:

- `Approved Budget (EUR)`
- `Status`
- `Start Year`
- `End Year`

Among the 82 projects present only in the assessed repository:

| Status | Projects |
| --- | ---: |
| Ongoing | 69 |
| Completed | 12 |
| Closed | 1 |

Their recorded start years are:

| Start year | Projects |
| --- | ---: |
| Missing | 1 |
| 2021 | 3 |
| 2022 | 2 |
| 2023 | 2 |
| 2024 | 1 |
| 2025 | 7 |
| 2026 | 64 |
| 2027 | 2 |

## Input portfolio characteristics

The assessed repository documents the following properties of its 1,024-row CSV:

- 1,024 unique project IDs.
- 344 distinct raw PI/applicant values.
- 20 projects have no abstract.
- Status counts: 711 completed, 312 ongoing, and 1 closed.
- Start years range from 2012 to 2027; 5 are missing.
- End years range from 2013 to 2030; 190 are missing.
- Total approved budget is approximately EUR 51.1 million.
- 354 project IDs use the older suffix-less numbering scheme.
- 670 use a sequence/grant-type suffix scheme.

Each CSV row is split into:

```text
input/projects/<Project Id>/project.json
input/projects/<Project Id>/abstract.txt
```

The abstract file is omitted when the CSV abstract is empty.

## Implemented pipeline

The pipeline is implemented as these stages:

```text
discover -> match -> enrich -> harvest -> mine -> match
         -> export -> fulltext -> report
```

### Discovery

Corpus-wide discovery performs:

- Europe PMC funding-index search for EuroQol.
- Europe PMC free-text search for `"EuroQol Research Foundation"`.
- Crossref funder sweep using funder ID `501100006419`.
- OpenAlex funder sweep using funder ID `F4320323856` when an API key is
  available.

Per-project discovery performs:

- A Europe PMC structured `GRANT_ID` query for every project ID.
- For seven- or eight-digit project IDs, an additional query combining the
  project ID with EuroQol acknowledgement metadata.
- A Europe PMC title query.

The committed publication records include `openalex` in their source lists, and
the committed coverage report contains an `openalex/funder_sweep` task marked
`ok`.

### Cache and state

Network responses are stored in a URL-keyed cache. Operational state is stored in
SQLite tables for:

- Tasks and their status.
- Fetched URLs.
- Normalized works.
- Automated project-publication candidates.
- Project IDs found in full text.
- Human accept/reject decisions.

Task statuses are `pending`, `ok`, `empty`, `failed`, and `skipped`. A stored task
is rerun if the exact query string changes.

Both `cache/` and `state/` are excluded by `.gitignore`. In a fresh clone,
`python3 scripts/scrape.py status` creates an empty ledger and reports:

```text
ledger empty - run `discover` first
```

The committed per-project results therefore exist without the HTTP cache and
SQLite state used to produce them.

### Matching

Works are normalized around DOI, PMID, or PMCID identifiers. Duplicate records
with the same normalized work ID are merged.

The matcher assigns the maximum individual evidence weight; evidence weights are
not summed.

| Evidence | Weight |
| --- | ---: |
| Project ID found in article text near a EuroQol mention | 1.00 |
| Structured grant metadata credits the project ID to EuroQol | 1.00 |
| Normalized project and publication titles are identical | 0.95 |
| Project ID returned by the Europe PMC acknowledgement/full-text query | 0.90 |
| Title similarity at least 0.95 | 0.80 |
| Title similarity at least 0.88 plus PI as lead author | 0.65 |
| EuroQol corpus work, PI as lead author, and plausible year | 0.45 |

The thresholds in code are:

- `accepted`: score greater than or equal to 0.85.
- `review`: score greater than or equal to 0.60 and below 0.85.
- `weak`: score below 0.60.

The pipeline documentation states that scores greater than or equal to 0.45 are
review-band, which differs from the implemented 0.60 threshold.

The PI fallback checks whether a parsed PI surname and compatible initial appear
as the first or last publication author. Project abstracts are not used by the
matcher.

### Full-text mining

The harvest stage obtains:

- Europe PMC JATS XML for pooled works with a PMCID.
- CORE full text for works with a DOI but no PMCID, when a CORE API key is
  available.

The mining stage:

- Extracts text from the harvested XML or text files.
- Searches for project-ID-shaped tokens.
- Requires the ID to be a known project ID.
- Requires the ID to occur within 300 characters of a case-insensitive
  `EuroQol` mention.
- Stores the project, work, and a surrounding snippet in
  `fulltext_mention`.

The matcher is rerun after mining so that these mentions can create or strengthen
project-publication links.

### Open-access enrichment and retrieval

Unpaywall is queried for candidate works with a DOI. The full-text stage considers:

1. Europe PMC XML.
2. Repository PDFs reported by Unpaywall.
3. Publisher PDFs with a licence matched as Creative Commons.
4. PDF locations already present in work metadata.

Downloaded files are checked for expected PDF or XML content. Each
`papers/manifest.json` records the method, source URL, licence, byte count, and
SHA-256 digest, or a reason the file was skipped.

The latest commit also contains 15 files recorded with retrieval method
`manual_browser`.

## Project-level funnel

The committed `publications.json` files produce these mutually exclusive outcomes,
based on each project's strongest candidate:

| Outcome | Projects | Share |
| --- | ---: | ---: |
| At least one accepted candidate | 209 | 20.4% |
| Best candidate is review-band | 9 | 0.9% |
| Only weak candidates | 563 | 55.0% |
| No candidate | 243 | 23.7% |
| **Total** | **1,024** | **100%** |

Consequently, 815 projects have no accepted candidate.

There are 781 projects with a `publications.json` file and 243 without one.

## Publication-link counts

Across the committed per-project exports:

| Band | Exported links | Distinct works |
| --- | ---: | ---: |
| Accepted | 318 | 305 |
| Review | 9 | 9 |
| Weak | 5,148 | 659 |

An additional 1,647 weak links were omitted from the JSON files because the export
caps weak entries at 15 per project. The omitted counts are retained in each
project's `weak_omitted` field.

Of the 305 distinct accepted works:

- 292 are accepted for one project.
- 13 are accepted for two projects.

Accepted-link score distribution:

| Score | Links |
| --- | ---: |
| 1.00 | 311 |
| 0.95 | 4 |
| 0.90 | 3 |

The 318 accepted links contain the following evidence counts. A link can contain
more than one kind of evidence.

| Evidence kind | Accepted links containing it |
| --- | ---: |
| Project ID found near EuroQol in harvested text | 223 |
| Structured EuroQol grant ID | 217 |
| Europe PMC acknowledgement/full-text query | 98 |
| Exact title | 11 |
| Strong title similarity | 4 |
| Fuzzy title plus lead PI | 2 |

At project level:

- 205 accepted projects have at least one accepted link containing grant-ID
  evidence.
- 4 accepted projects rely only on an exact title match.

The four title-only accepted links are:

| Project | Publication |
| --- | --- |
| `169-RA` | Value Sets for EQ-5D-5L: A Compendium, Comparative Review & User Guide |
| `20170230` | Estimating the EQ-5D-5L value set for the Philippines |
| `214-RA` | Measurement Properties of the EQ-5D-Y: A Systematic Review |
| `229-RA` | Examining the psychometric properties of a split version of the EQ-5D-5L anxiety/depression dimension in patients with anxiety and/or depression |

All 5,148 exported weak links have only `ack_pi_year` evidence and a score of 0.45.

All exported records have `curated: null`; no human accept/reject decision is
represented in the committed publication exports.

## Full-text funnel

The committed manifests cover all 318 accepted project-publication links:

| Manifest status | Links |
| --- | ---: |
| Full text on disk | 257 |
| Skipped | 61 |
| **Total** | **318** |

Retrieval methods are:

| Method | Links |
| --- | ---: |
| Europe PMC XML | 220 |
| Repository PDF | 17 |
| Manual browser retrieval | 15 |
| Indexed PDF | 3 |
| Publisher PDF | 2 |
| Skipped without a file | 61 |

The 257 stored link files occupy approximately 74.7 MB according to their manifest
byte counts. Because 13 accepted works belong to two projects, the same work can be
stored in two project directories.

The checked-in `reports/coverage.md` states that 242 accepted links have full text.
The current manifests contain 257. The difference is the 15 manual-browser files
added by the latest commit.

## Comparison with the local pipeline artifacts

Current local artifacts contain:

- 46,620 distinct publication records.
- 46,400 publications with at least one resolved PI author.
- 739 publications marked as EuroQol-funded.
- 166,556 project-publication candidate pairs.

Local candidate tiers are:

| Tier | Candidate pairs |
| --- | ---: |
| Award ID | 209 |
| PI | 166,027 |
| Funder without resolved PI | 320 |

Local score counts at selected thresholds are:

| Threshold | Links | Projects |
| --- | ---: | ---: |
| 1.00 | 209 | 133 |
| 0.85 | 224 | 147 |
| 0.65 | 296 | 207 |
| 0.45 | 985 | 459 |
| 0.30 | 11,530 | 805 |

The local publication records include OpenAlex author IDs, references, citation
counts, and reconstructed abstracts. The assessed repository's output does not
contain citation or reference edges.

## Repository and validation observations

- Root working-tree size after cloning: approximately 139 MB.
- Git pack size: approximately 43 MB.
- Tracked files: 3,297.
- Project directories: 1,024.
- Per-project publication files: 781.
- Per-project paper manifests: 209.
- Stored article files: 220 XML and 37 PDF.
- Python source files compile successfully with `python3 -m compileall`.
- Rerunning `scripts/split_projects.py` reported 1,024 projects and zero changed
  files.
- All 1,805 checked per-project JSON files parsed successfully.
- All 257 manifest entries marked `ok` had an existing file with the recorded byte
  count and SHA-256 digest.
- `git fsck --full` reported no repository-integrity errors.
- No test directory or automated test suite is present.
- No `requirements.txt`, `pyproject.toml`, lock file, or other dependency declaration
  is present.
- The scripts import the third-party `requests` package.
- The Semantic Scholar adapter is defined but is not called by a pipeline stage.
- The root `README.md` contains only the heading `# eq-graph`; operational
  documentation is in `input/README.md`, `input/projects/README.md`, and
  `scripts/README.md`.
