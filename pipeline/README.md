# Pipeline

Discovery, screening, retrieval, preparation, and extraction scripts for the release.
Prefixes indicate the role: `prepare_` builds inputs, `run_` executes a batch, `submit_` saves one result, `validate_` checks outputs, `evaluate_` scores or audits.

## Discovery and people

| Script | Purpose |
|---|---|
| `01_authors.py` | Canonical PI-name CSV |
| `01b_people.py` | Merge project leaders and EuroQol members |
| `02_resolve.py` | Resolve PI names to OpenAlex author IDs |
| `02b_review.py` | Human-review sheet for identity links |
| `03_works.py` | Fetch works for resolved authors |
| `prepare_scale_discovery.py` | Build OpenAlex discovery corpus |
| `prepare_scale_source_union.py` | Merge OpenAlex, ORCID, PubMed, and funding |
| `validate_scale_source_union.py` | Validate the source union |
| `retrieve_scale_profiles.py` | Retrieve missing OpenAlex works |
| `retrieve_scale_identifier_sources.py` | Retrieve ORCID and PubMed |
| `name_utils.py` | Name normalization (imported by `01_authors`, `01b_people`) |
| `oa.py` | OpenAlex helpers (imported by `02_resolve`, `03_works`, `retrieve_scale_profiles`) |
| `pilot_2_0.py` | Protocol 2.0 paths/loaders (imported by four scale scripts) |

## Abstract screen

| Script | Purpose |
|---|---|
| `prepare_scale_inputs.py` | Prepare profile and funding inputs |
| `run_codex_abstract_screen.py` | Run abstract screen through Codex |
| `enrich_scale_abstracts.py` | Enrich missing abstracts by DOI or PMID |
| `validate_scale_abstract_enrichment.py` | Validate abstract enrichment |
| `run_gemini_abstract_screen.py` | Gemini Flash runner (imported by `run_codex_abstract_screen`) |
| `scale_publication_metadata.py` | Canonical metadata loader (imported by three retrieval/prep scripts) |

## Retrieval

| Script | Purpose |
|---|---|
| `run_scale_fulltext_retrieval.py` | Build and run the retrieval queue |
| `build_fulltext_paper_packages.py` | Build paper packages from screen |
| `build_manual_download_queue.py` | Build the manual download queue |

See [MANUAL_FULLTEXT_DOWNLOAD.md](MANUAL_FULLTEXT_DOWNLOAD.md) for per-publisher routes.

## Preparation

| Script | Purpose |
|---|---|
| `prepare_scale_fulltexts.py` | Prepare verified full texts |
| `prepare_fulltext_sql_pilot.py` | Prepare SQL workspaces |
| `prepare_fulltext_single_agent_pilot.py` | Single-agent prep (imported by `prepare_fulltext_sql_pilot`) |

See [PDF_PARSING.md](PDF_PARSING.md) for the converter and repair rules.

## Extraction

| Script | Purpose |
|---|---|
| `fulltext_sql_workspace.py` | Paper-scoped SQL workspace |
| `run_fulltext_sql_pilot.py` | Codex extraction with SQL tools |
| `run_fulltext_sql_claude_pilot.py` | Claude extraction with SQL tools |
| `fulltext_ingest_tool.py` | Validate and save one extraction (imported by `fulltext_sql_workspace`) |
| `fulltext_sql_mcp.py` | SQL workspace as native tools (imported by `run_fulltext_sql_pilot`) |

## Audits

| Script | Purpose |
|---|---|
| `prepare_profile_qa.py` | Prepare QA batches for author profiles |
| `run_profile_qa.py` | Run and aggregate profile-QA batches |
| `submit_profile_qa.py` | Save one profile-QA batch |
| `evaluate_profile_qa.py` | Validate and export accepted sets |

## Utilities

| File | Purpose |
|---|---|
| `data/project-year-lower-bounds.tsv` | Manual lower bounds on project start years |
| `data/publication_year_overrides.tsv` | Manual overrides for publication years |
| `data/source_record_exclusions.tsv` | Records excluded from source union |
| `prompts/abstract_screen_v2.md` | Frozen abstract-screen prompt |

## Reproduce the release

Run from the repository root.
Discovery requires `OPENALEX_API_KEY` when profiles are missing.
Preparation commands stop if versioned output exists; use a new version name for a new run.
The discovery, profile QA, and abstract-screen commands are the sequence recorded for the scale run. The retrieval, preparation, and extraction commands follow the stage order in [docs/METHOD.md](../docs/METHOD.md); their run records are local and each script documents its own arguments.

```sh
python pipeline/01_authors.py
python pipeline/01b_people.py
python pipeline/02_resolve.py
python pipeline/02b_review.py
python pipeline/03_works.py
python pipeline/prepare_scale_inputs.py
python pipeline/retrieve_scale_profiles.py
python pipeline/prepare_scale_inputs.py
python pipeline/prepare_profile_qa.py
python pipeline/run_profile_qa.py
python pipeline/evaluate_profile_qa.py
python pipeline/prepare_scale_discovery.py
python pipeline/retrieve_scale_identifier_sources.py
python pipeline/prepare_scale_source_union.py
python pipeline/validate_scale_source_union.py
python pipeline/enrich_scale_abstracts.py
python pipeline/validate_scale_abstract_enrichment.py
python pipeline/run_codex_abstract_screen.py
python pipeline/run_scale_fulltext_retrieval.py
python pipeline/build_manual_download_queue.py
python pipeline/prepare_scale_fulltexts.py
python pipeline/build_fulltext_paper_packages.py
python pipeline/prepare_fulltext_sql_pilot.py
python pipeline/run_fulltext_sql_pilot.py
python pipeline/run_fulltext_sql_claude_pilot.py
```

The release build (typed database, serving database, checks) continues in [scripts/README.md](../scripts/README.md).

## Superseded scripts

18 superseded scripts are under [`archive/pipeline/`](../archive/pipeline/); 30 more were removed on 2026-09-03 and are in Git history.
The topic screen, the 10-person pilot, and the two-agent full-text pilot are indexed in [archive/README.md](../archive/README.md).

## Source and conversion notes

- Crossref: use `offset` paging. Cursor paging returns the same `next-cursor` token on every page, and a URL-keyed cache then replays one page forever.
- Grant numbers are not unique across funders. Confirm the funder agency before a grant-id match counts as evidence.
- Europe PMC indexes only the funding statements it could parse (`ACK_FUND:"EuroQol"` finds 626 works; the phrase "EuroQol Research Foundation" finds 1,147). The grant id in the acknowledgement text is the most reliable attribution route.
- Publishers answer 403 to scripted PDF requests even for CC-licensed articles; treat 401 and 403 as terminal. An empty Unpaywall location list does not mean that no free copy exists. Per-publisher routes: [MANUAL_FULLTEXT_DOWNLOAD.md](MANUAL_FULLTEXT_DOWNLOAD.md).
- Pandoc's JATS reader drops the reference text and files the abstract under metadata. Read references from the XML and do not use `--citeproc`. PDF font-map repair: [PDF_PARSING.md](PDF_PARSING.md).
- Output that lands in Git must iterate sets in sorted order; Python randomizes string hashing per process.
