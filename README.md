# eq-graph

A research knowledge graph of the EuroQol Research Foundation's funded projects, their publications, and the evidence reported in those publications.

EuroQol has funded more than one thousand research projects.
The related literature contains evidence about EQ-5D and other instruments across populations, countries, clinical areas, and methods.
This project finds that literature, assesses it, extracts structured evidence, loads the evidence into a graph, and makes the graph available through a web application.

The project is funded as EuroQol seed grant **2582-SG** (1.3 Seed grant), with a budget of €28,404 and a term from **2026-07-01 to 2026-12-31**.
The submitted proposal is in [`docs/submitted-proposal.pdf`](docs/submitted-proposal.pdf).

Team: Paul Schneider (PI), Sofia Fabishevskaya (co-I), and Kazik Pogoda (advisor).
Executed by [Shoulders](https://shoulde.rs).

## Project flow

```text
project-first route                         literature-first route
1,024 projects                             author and funder searches
  -> strong project-work matches             -> 28,600 distinct records
  -> 287 held full texts                      -> 18,348 screened abstracts
  -> 209 unique JATS papers                   -> 3,148 retained records
  -> 207 audited studies                      -> full-text retrieval pending
                    \                       /
                     -> graph -> application
```

These routes are separate. The 305 project-first works passed an automated
link threshold; they did not pass the later full-text assessment. The 3,148
literature-first records passed title-and-abstract screening, but their full
texts have not been retrieved. See the concise
[`pipeline recap`](docs/PIPELINE_RECAP.md).

The ontology and graph schema develop with the extraction stage.
Extraction can identify concepts that the schema does not yet represent, and the schema controls how accepted evidence enters the graph.

## Current status

### Portfolio and publication discovery

- The canonical public export contains **1,024 projects**.
- The project-first pipeline has **305 distinct works** above its automated
  project-link threshold and **287 full texts** on disk. This is discovery
  evidence, not a completed full-text assessment.
  The corpus contains Markdown for all 220 JATS XML files and the 7 PDF files used in the ontology pilot.
  The converter supports the remaining PDFs, but they have not been converted in bulk.
- The author and funding routes produced a deduplicated union of **28,600 records**, including **23,175 articles or reviews**.
- Binary identity QA accepted **222 profiles** for the current author route.
- A total of **94 people** and **76 additional profile suggestions** remain in a separate identity queue.

### Protocol 2.0 screening

The frozen title-and-abstract screen is complete and validated:

- Input: **18,348 records** with usable abstracts.
- Complete batches: **918/918**.
- Retained: **3,148**.
- Excluded: **15,200**.
- Collector failures: **0**.
- Two nonoverlapping 100-record exclusion audits found no confirmed false exclusion after adjudication.
- Scale full texts downloaded: **0**.

The project is paused before scale full-text retrieval.
Independent human screening validation and the held identity queue remain as gates.
Do not rerun or replace the completed screen.
See [`scale/protocol-2.0/PAUSE_2026-08-05.md`](scale/protocol-2.0/PAUSE_2026-08-05.md).

### Audited research graph

- The current audited SQLite graph covers **209 local JATS publications** and
  **207 included studies**. It contains **17,650 nodes**, **26,143 typed
  relationships**, **871 principal findings**, **602 limitations**, and **191
  source conflicts**.
- An independent full-source audit checked all 207 included records. It passed
  121 unchanged, corrected 86, and left no unresolved material issue. A strong
  source-verification pass is now mandatory after the low-cost draft pass.
- The project-link audit checked 260 paper-project pairs. The final graph has
  **242 accepted links** and keeps **14 possible links** as reviewable
  assessments without trusted support or output edges.
- The former Aura load is a historical small pilot. It is not the current data
  foundation. The closed Aura model under [`graph/`](graph/) is a baseline.
- The version-3 work tested exact EuroQol domain facts against 100 competency
  questions, 100 design papers, three independent proposals, and a source-checked
  holdout. One paper call combines full-text assessment and conditional draft
  extraction; deterministic code then normalizes and loads source-verified
  facts. The final database passes structure, exact-domain, linkage, integrity,
  and foreign-key checks. See
  [`pilot/ontology-development-v3/production-calibration/DECISION.md`](pilot/ontology-development-v3/production-calibration/DECISION.md).

### Application delivery

Application design is not part of the research method. The Nuxt application
reads a deterministic, sanitized SQLite derivative of the audited graph through
a read-only query tool. Full text, local paths, unresolved citations, possible
links, and audit reasoning stay outside the public database. See
[`web/README.md`](web/README.md) for implementation status.

## Repository map

| Path | Contents |
| --- | --- |
| [`input/`](input/README.md) | Canonical project export and project-first publication records |
| [`scripts/`](scripts/README.md) | Existing project-first discovery, matching, retrieval, and report pipeline |
| [`pipeline/`](pipeline/) | Protocol 2.0 author discovery, screening, assessment, validation, and preparation stages |
| [`data/`](data/) | Legacy graph inputs, extractions, and a compatibility link to the canonical project export |
| [`artefacts/`](artefacts/) | Compact identity checkpoint and a manifest of the larger local artefact tree |
| [`pilot/protocol-2.0/`](pilot/protocol-2.0/) | Compact pilot result and a manifest of the complete local pilot tree |
| [`pilot/ontology-development-v3/`](pilot/ontology-development-v3/README.md) | Exact-domain ontology experiment, source validation, and JATS production pipeline |
| [`scale/protocol-2.0/`](scale/protocol-2.0/) | Validated scale checkpoint, compact results, and a manifest of the complete local scale tree |
| [`corpus/`](corpus/README.md) | Retrieved full text converted to Markdown for extraction |
| [`graph/`](graph/) | Historical Neo4j pilot ontology, schema, constraints, and indexes |
| [`web/`](web/) | Nuxt server, narrative, AI chat, chart templates, and read-only SQLite adapter |
| [`docs/`](docs/) | Method, provenance, graph design, work plan, decisions, and proposal |

See [`docs/repository-layout.md`](docs/repository-layout.md) for the integration boundary between tracked source, compact evidence, and local working data.

## Governing method and provenance

- [`protocol-2.0.md`](protocol-2.0.md) is the canonical Protocol 2.0 method and status record.
- [`docs/METHOD_SIMPLE.md`](docs/METHOD_SIMPLE.md) is the short governing method.
- [`docs/PROVENANCE.md`](docs/PROVENANCE.md) identifies the source-to-result evidence trail.
- [`docs/PIPELINE_RECAP.md`](docs/PIPELINE_RECAP.md) separates the two discovery routes and records the current model and audit boundary.
- [`docs/WORKPLAN.md`](docs/WORKPLAN.md) states the current work-package status,
  ordered next work, and open decision gates.
- [`LOG.md`](LOG.md) is the chronological build log.
- [`scale/protocol-2.0/SCALE_STATUS.md`](scale/protocol-2.0/SCALE_STATUS.md) records the current scale funnel and work queue.
- [`docs/COMPETENCY_QUESTIONS.md`](docs/COMPETENCY_QUESTIONS.md) defines 100 broad graph and application questions plus 20 negative tests.
- [`pilot/ontology-development-v2/USER_QUESTIONS.md`](pilot/ontology-development-v2/USER_QUESTIONS.md) defines the focused paper-ontology requirements.

`docs/METHOD.md` is a historical design document.
`docs/graph-model.md` is the historical Neo4j pilot model.
`pilot/ontology-development-v3/SCALE_UP_DECISION.md` is a completed historical
gate; the production-calibration decision now governs.
`FRIEND_REPO_EMPIRICAL_FINDINGS.md` is a historical assessment of the project-first pipeline at commit `68ebeab`.

## Running the project

The project-first pipeline uses Python and `requests`:

```sh
python3 scripts/split_projects.py
python3 scripts/scrape.py all
python3 scripts/scrape.py status
python3 scripts/to_markdown.py
```

`to_markdown.py` needs Pandoc for JATS XML and Poppler for PDF files.
It is offline and makes no network request.

The Protocol 2.0 reproduction commands are in [`pilot/protocol-2.0/REPRODUCE.md`](pilot/protocol-2.0/REPRODUCE.md).
Network steps and large working outputs use ignored local directories.
Do not run the completed scale-screen preparation or submission commands against `scale/protocol-2.0/screening-v1`.

The Nuxt application uses pnpm:

```sh
cd web
pnpm install --frozen-lockfile
pnpm dev
```

Interface work can use `pnpm dev:remote` to run the frontend locally against
the shared preview API. Fixed chat states are available at `/chat-lab`. See
[`web/README.md`](web/README.md) for the designer workflow.

Shared interface preview: [eq-graph.shoulde.rs](https://eq-graph.shoulde.rs)

The narrative and chat use the same generated serving database. The AI chat
also needs the Anthropic key in `web/.env`. See [`DESIGN.md`](DESIGN.md) for
the interface system and [`docs/APP_DATA_ADAPTER.md`](docs/APP_DATA_ADAPTER.md)
for the data boundary.

## Data and repository rules

- `input/` is the immutable record of the public project export and collected project-first results.
- Active runs, caches, dependencies, and generated build output do not enter Git.
- Compact validated results can enter Git when they include their method and provenance records.
- `WORKSPACE_MANIFEST.tsv` files preserve file names, byte counts, and SHA-256 digests for larger local evidence trees that do not enter Git.
- An accepted project-publication link and a Protocol 2.0 relevance decision are separate facts.
- Full text must confirm funding scope; funding metadata is a discovery signal, not final proof.

This repository is private because some downloaded full texts cannot be redistributed.
The open-source deliverable is the code, not the restricted corpus.
Do not make the repository public until restricted content has a separate release path.
Do not circumvent paywalls.

OpenAlex is metered.
Run OpenAlex network stages only with a deliberate budget and the required local credentials.
No credential belongs in Git.

## Next gates

1. Process the 60 local PDF-only papers with a validated general paper parser
   and the same source-verification gate.
2. Complete an independent human sample check of retained and excluded screening decisions.
3. Resolve the held identity queue and create an additive tranche for newly accepted profiles.
4. Confirm the final retained set without replacing the completed 918-batch screen.
5. Retrieve lawful scale full text and keep unavailable papers unassessed.
6. Repeat extraction, source audit, serving-database build, and project linkage
   for each new full-text tranche.
