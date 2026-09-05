# Method

Ontology 0.13.
Stage results: [RESULTS.md](RESULTS.md).
Release record: [DATA_RELEASE.md](DATA_RELEASE.md).

## Scope

Include a publication only when its verified full text confirms one of these conditions:

- EuroQol supported the paper, study, data, research component, or an author's work on the paper.
- The paper is an output of a funded EuroQol project.

The following do not establish eligibility: EQ instrument use, EQ topic, generic HRQoL content, EuroQol membership, or authorship alone.
Include explicit EuroQol support even when the paper has no EQ instrument focus.

The abstract screen routes a paper to full-text assessment or excludes it from that next step.
Routing is not eligibility; the full-text assessment decides.

## Steps

1. **Portfolio.**
Public EuroQol export, normalized to `data/funded-projects-canonical.csv`.

2. **People.**
297 project leaders and 125 current members (overlap 106), deduplicated to `artefacts/01_people.csv`.

3. **Profile QA.**
Each profile receives a binary accept or hold decision based on name, affiliation, field, coauthors, and works.
Only accepted profiles enter the author discovery route.

4. **Discovery.**
Use accepted OpenAlex and ORCID IDs plus explicit EuroQol funder metadata.
PubMed adds a paper only through an exact accepted ORCID ID.
No name-only PubMed discovery at scale.

5. **Bibliographic dedup.**
Merge by DOI, then PMID, then normalized title and year.

6. **Article gate.**
Keep journal articles and reviews with at least 80 abstract characters.
Exclude conference abstracts and proceedings, books and chapters, theses, preprints, blogs, editorials, commentaries, letters, corrections, and retractions.

7. **Abstract screen.**
`gpt-5.6-terra` receives one publication and the time-eligible project rows.
It returns `RETRIEVE_FULL_TEXT` or `EXCLUDE`, nominated project IDs, and a reason.
The last records screened used a 10-year lookback window; no completed record was rerun.

8. **Retrieval.**
Europe PMC JATS XML first, then repository or publisher PDF.
Code verifies file type, checksum, and paper identity against DOI, PMID, or title, authors, and year.
If identity remains unclear, a small AI check ("Luna": `gpt-5.6-luna`, a Codex model) reviews the expected metadata and the first page; unresolved cases go to human review.
An operator scope screen, applied once by title to the manual queue, removed records the abstract screen had routed on author or PI-name plausibility alone ([RESULTS.md](RESULTS.md#operator-scope-screen)).
Unretrieved records get a recorded disposition and stay unassessed.

9. **Preparation.**
JATS metadata parsed deterministically.
PDF body converted to Markdown with font-map repair; Poppler fallback marks unreadable glyphs instead of guessing.
References stay outside the AI reading text.
One paper package per paper with the abstract-screen result and only the nominated project rows.

10. **Assessment and extraction.**
One Opus or Sol ("Sol": `gpt-5.6-sol`, a Codex model) call receives an isolated SQLite workspace and three tools: `sql`, `submit`, and `reject`.
It confirms eligibility and, for an eligible paper, writes typed evidence rows.
`submit` validates the complete workspace and returns specific errors to the same call until the record is valid.
Labels resolve against the identity registry; the model may add a genuinely new identity.

11. **Load.**
Complete evidence and audit data load into the private SQLite database.
A separate sanitized public copy is built and checked.
Release checks run before freeze.

## Fixed rules

- Project start year after publication year is a hard no-link rule.
- Authorship is evidence for the model, not a deterministic link rule.
- Exact structured EuroQol funding metadata can establish support; ambiguous funder names or award identifiers require confirmation from the paper.
- No full text means no final funding or project-link decision.
- A possible link remains a review item and does not enter the trusted graph.
- AI must cite brief record-specific evidence.
- The abstract screen can nominate project IDs; full text must confirm the link.
- Funding scope is classified directly: publication fees, related-work funding, and nonfinancial support are not study funding.
- A longer field that is not a usable article abstract is excluded as E5 during AI screening; do not decide relevance from the title.
- The semantic extraction call does not reconstruct structured JATS metadata or a PDF bibliography.
- Competency questions test the graph; they do not dictate its shape.
- Every prompt, per-record decision, and compiled count is retained.

## Known limits

- The repository has no Git history before the completed scale-screen checkpoint. Earlier work has file-level and run-level records only.
- The pilot and first scale checks used operator reference labels, not an independent human validation.
- Two blinded 100-record AI exclusion audits cover the superseded 2026-08-05 topic screen. The current funded-project screen has only a 10-record stratified random check.
- Records without a usable abstract were never screened.
- 94 people and 76 profile suggestions remain outside the author route pending identity review.
- Not-retrieved full texts stay unassessed. The revisit list is [`data/fulltext-not-retrieved.csv`](../data/fulltext-not-retrieved.csv).
- Abstract-screen records with a hedged reason or no nominated project have not been reviewed as a population.
- Five duplicate title pairs found during the manual retrieval push await a corpus decision.
- Unresolved authorships receive no forced person links.
- PDF reference lists are not parsed. Dated citation counts are present; outgoing bibliography edges are not.

Counts for each limit are in [RESULTS.md](RESULTS.md) and [DATA_RELEASE.md](DATA_RELEASE.md).

## Key files

| Stage | Code | Result |
|---|---|---|
| Portfolio | `data/funded-projects-canonical.csv` | — |
| People | `artefacts/01_people.csv` | — |
| Abstract screen | `pipeline/run_codex_abstract_screen.py`, `pipeline/prompts/abstract_screen_v2.md` | [RESULTS.md](RESULTS.md) |
| Retrieval | `pipeline/run_scale_fulltext_retrieval.py` | [RESULTS.md](RESULTS.md) |
| Manual queue | `pipeline/build_manual_download_queue.py` | [MANUAL_FULLTEXT_DOWNLOAD.md](../pipeline/MANUAL_FULLTEXT_DOWNLOAD.md) |
| Preparation | `pipeline/prepare_scale_fulltexts.py`, `pipeline/build_fulltext_paper_packages.py` | [PDF_PARSING.md](../pipeline/PDF_PARSING.md) |
| Extraction workspace | `pipeline/fulltext_sql_workspace.py` | — |
| Extraction (Opus) | `pipeline/run_fulltext_sql_claude_pilot.py` | [RESULTS.md](RESULTS.md) |
| Extraction (Sol) | `pipeline/run_fulltext_sql_pilot.py` | [RESULTS.md](RESULTS.md) |
| Release prep | `scripts/prepare_fulltext_release.py` | — |
| Load | `pilot/ontology-development-v4/production/load_research_v2.py`, `scripts/build_serving_database_v2.py` | — |
| Release check | `scripts/check_serving_database_v2.py` | [DATA_RELEASE.md](DATA_RELEASE.md) |
| Ontology | `pilot/ontology-development-v4/ONTOLOGY.md`, `pilot/ontology-development-v4/VOCABULARY.tsv` | — |
