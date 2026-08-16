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
project and member records
  -> author and paper discovery
  -> title-and-abstract screening
  -> full-text retrieval
  -> full-text assessment and evidence extraction
  -> graph loading
  -> Nuxt application
```

The ontology and graph schema develop with the extraction stage.
Extraction can identify concepts that the schema does not yet represent, and the schema controls how accepted evidence enters the graph.

## Current status

### Portfolio and publication discovery

- The canonical public export contains **1,024 projects**.
- The project-first pipeline has **305 distinct works** linked at accepted confidence and **287 full texts** on disk.
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

### Graph and application

- A real ontology pilot is online in Neo4j Aura. On 2026-08-05 it contains
  **5,137 nodes**, **8,661 relationships**, **20 projects**, **174 works**,
  **30 accepted project-work attributions**, and **178 extracted findings**.
- This Aura load is a small pilot. It is not the complete 1,024-project
  portfolio or the completed Protocol 2.0 screen. Its record counts will grow.
- The full closed graph model and Aura DDL are under [`graph/`](graph/).
- The Nuxt application under [`web/`](web/) reads the Aura graph through Nitro.
  Its status line reads current counts from Neo4j instead of hard-coding them.
- The application agent knows all three graph layers and can resolve projects,
  people, works, instruments, concepts, methods, conditions, properties,
  countries, working groups, journals, and value sets.

## Repository map

| Path | Contents |
| --- | --- |
| [`input/`](input/README.md) | Canonical project export and project-first publication records |
| [`scripts/`](scripts/README.md) | Existing project-first discovery, matching, retrieval, and report pipeline |
| [`pipeline/`](pipeline/) | Protocol 2.0 author discovery, screening, assessment, validation, and preparation stages |
| [`data/`](data/) | Legacy graph inputs, extractions, and a compatibility link to the canonical project export |
| [`artefacts/`](artefacts/) | Compact identity checkpoint and a manifest of the larger local artefact tree |
| [`pilot/protocol-2.0/`](pilot/protocol-2.0/) | Compact pilot result and a manifest of the complete local pilot tree |
| [`scale/protocol-2.0/`](scale/protocol-2.0/) | Validated scale checkpoint, compact results, and a manifest of the complete local scale tree |
| [`corpus/`](corpus/README.md) | Retrieved full text converted to Markdown for extraction |
| [`graph/`](graph/) | Neo4j ontology, schema, constraints, and indexes |
| [`web/`](web/) | Nuxt server, chat, graph tools, migrations, and visual output |
| [`docs/`](docs/) | Method, provenance, graph design, work plan, decisions, and proposal |

See [`docs/repository-layout.md`](docs/repository-layout.md) for the integration boundary between tracked source, compact evidence, and local working data.

## Governing method and provenance

- [`protocol-2.0.md`](protocol-2.0.md) is the canonical Protocol 2.0 method and status record.
- [`docs/METHOD_SIMPLE.md`](docs/METHOD_SIMPLE.md) is the short governing method.
- [`docs/PROVENANCE.md`](docs/PROVENANCE.md) identifies the source-to-result evidence trail.
- [`LOG.md`](LOG.md) is the chronological build log.
- [`scale/protocol-2.0/SCALE_STATUS.md`](scale/protocol-2.0/SCALE_STATUS.md) records the current scale funnel and work queue.
- [`docs/COMPETENCY_QUESTIONS.md`](docs/COMPETENCY_QUESTIONS.md) defines graph and application evaluation questions.

`docs/METHOD.md` is a historical design document.
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
cp .env.example .env
# Add the Anthropic and Neo4j Aura values to .env.
pnpm db:check
pnpm dev
```

See [`web/README.md`](web/README.md) for the live Aura setup, checks, and the
separate local demo database.

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

1. Complete an independent human sample check of retained and excluded screening decisions.
2. Resolve the held identity queue and create an additive tranche for newly accepted profiles.
3. Confirm the final retained set without replacing the completed 918-batch screen.
4. Retrieve lawful scale full text and keep unavailable papers unassessed.
5. Assess EuroQol connection, funding scope, project links, and graph evidence.
6. Expand the Aura pilot with accepted evidence and evaluate the graph and application.
