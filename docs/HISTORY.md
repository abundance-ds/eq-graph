# History

How the release was reached, on one page.
Superseded records are in [`archive/`](../archive/README.md); the day-by-day build log is [`archive/LOG.md`](../archive/LOG.md).

## Timeline

| Date | What happened | What it replaced or produced |
|---|---|---|
| 2026-07-28 | Started a literature-first pipeline: resolve every principal investigator to an OpenAlex identity and harvest their works, against a 944-project CSV. | First discovery corpus |
| 2026-07-29 | Assessed an independent grant-mining pipeline (`abundance-ds/eq-graph`): 318 accepted project links from grant IDs read out of full text. | [`2026-07-29-grant-mining-pipeline-assessment.md`](../archive/docs/2026-07-29-grant-mining-pipeline-assessment.md), [`2026-07-29-scrape-pipeline.md`](../archive/docs/2026-07-29-scrape-pipeline.md) |
| 2026-07-30 | Drafted a joint method: two pipelines, a two-axis inclusion rule (EuroQol-funded OR EQ-instrument-focused), weighted link evidence, Neo4j as target store. Adopted the 1,024-project public export as the canonical portfolio. | The 944-project CSV. Draft: [`2026-07-30-method-draft.md`](../archive/docs/2026-07-30-method-draft.md) |
| 2026-08-05 | Completed the topic-based abstract screen: 18,348 records, 3,148 retained, 15,200 excluded. Connected a Neo4j Aura pilot graph to the Nuxt app. Paused before full-text retrieval. | [`2026-08-05-topic-screen-and-pilot-results.md`](../archive/docs/2026-08-05-topic-screen-and-pilot-results.md), [`PAUSE_2026-08-05.md`](../archive/scale/protocol-2.0/PAUSE_2026-08-05.md) |
| 2026-08-16 | Merged both pipelines into one repository and one Nuxt 4 application. Dropped the separate Kotlin/Neo4j backend. Ran ontology experiments version 1 and version 2 with isolated agent lineages. | Neo4j graph model: [`neo4j-pilot/`](../archive/docs/neo4j-pilot) |
| 2026-08-17 to 08-21 | Completed ontology version 3 (analytical model, 209-paper JATS calibration, project linkage), then replaced it with the typed version-4 rebuild, versions 0.5 to 0.9. | Versions 1 to 3: [`pilot/README.md`](../pilot/README.md) |
| 2026-08-22 | Built an interim project-first graph of 273 publications (271 studies) and ran the 100 competency questions against it: 32 pass. Built a 40-paper two-agent full-text pilot. | [`2026-08-27-pipeline-recap.md`](../archive/docs/2026-08-27-pipeline-recap.md) |
| 2026-08-23 to 08-24 | Corrected the scope: the full text decides eligibility, and EQ-instrument use alone does not qualify. Reran the abstract screen with `gpt-5.6-terra` under the funded-project rule: 1,679 routed to retrieval, 16,669 excluded. | The topic screen of 2026-08-05. Plan: [`2026-08-24-scope-repair-plan.md`](../archive/docs/2026-08-24-scope-repair-plan.md) |
| 2026-08-26 | Closed retrieval at 1,607 verified full texts and 72 not retrieved, after a manual retrieval push and an operator scope screen that removed 36 off-scope records. Replaced the two-call extraction with one Opus call and native tools. | The 40-paper two-agent pilot. Record: [`SCOPE_SCREEN_RESULT.md`](../archive/docs/results/SCOPE_SCREEN_RESULT.md) |
| 2026-08-27 | Chose the flat SQL extraction interface after a five-paper Opus and Sol pilot. Processed all 1,607 papers: 797 included, 810 excluded. Loaded the graph, deployed the release, scored 54 pass, 36 partial, 6 fail, 4 not testable on the 100 questions. | Nested-JSON submission. Stage records: [`results/`](../archive/docs/results) |
| 2026-08-29 | Froze ontology 0.13 and the data release `beta-2026-08-29`. | [DATA_RELEASE.md](DATA_RELEASE.md) |
| 2026-08-31 to 09-02 | Moved all charts into the chat, published the public data release with codebook and `/data` page, added private analytics. | The separate chart gallery |
| 2026-09-03 | Restructured the repository around one entry point (README.md). Moved superseded design drafts, stage results, and pilots to `archive/`. Deleted Gradle scaffolding, the 944-row funded-projects CSV, the corpus directory, the scrape pipeline, dead pipeline scripts, and iteration snapshots of the interim 273-publication database. Moved COMPETENCY_QUESTIONS.md next to its test result and operator runbooks to `pipeline/`. | 20 files in `docs/`, four method documents, the vendored Neo4j skills |
