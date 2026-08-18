# Build log

Chronological record of what was done, what broke, and how it was fixed.
Stable knowledge lives in README.md; this file is the narrative.

## 2026-08-18

- Replaced the research dot clouds in the landing story with corpus-level
  science-communication views. The new sequence shows study-family shape,
  instrument co-use, DCE/cTTO bundles, method profiles, geography,
  cross-cutting concepts, research outputs, and instrument coverage. Counts,
  denominators, overlaps, and limits are stated on the chart or in the copy.
  Population-gap and time-trend views remain out until those fields support
  reliable comparisons.
- Expanded the landing narrative from six to twelve views. The first six keep
  the funded-project visuals with shorter subject-focused text. The next six
  show study types, instruments, methods, populations and countries, research
  products, findings, limitations, and gaps. The globe now counts studies by
  country. The chat examples now use researcher questions.
- Corrected the interpretation of the Asian DCE comparison paper. Its eleven
  project links comprise ten country-data projects and one comparative-study
  project; they are not eleven country-project outputs. The AI guidance now
  distinguishes data support, study support, and project-output status.
- Replaced the interface fixtures with a deterministic 6.2 MB SQLite serving
  database built from the audited graph. It exposes 1,024 projects, 209
  publications, 207 studies, 242 accepted project links, 871 findings, and 602
  limitations through simple research tables.
- Kept full text, local paths, unresolved and external citations, possible
  project links, and project-link audit reasoning out of the serving database.
  The integrity, fixed-count, foreign-key, path-leak, and repeat-build checks
  pass. Two builds from the same input have the same SHA-256.
- Connected the landing narrative, project-country layout, graph-status route,
  and AI SQL tool to the serving database. Added `/api/story` and `/api/graph`;
  the old mock routes remain temporary aliases for designer branches.
- Corrected the narrative boundary: 1,024 items are funded projects, while
  209 publications contain 207 studies. The project map follows project
  support; the study map and globe follow all named study countries.

- Added a short pipeline recap after the project-first and literature-first
  routes became easy to confuse. The 305 automated project matches are not the
  3,148 retained abstract-screen records, and neither count is a completed
  full-text assessment.
- Confirmed that the Nuxt application type check and production build pass.
  The landing page, chat lab, chart gallery, story API, graph API, and SQLite
  status route respond successfully.
- Added a short PDF-parser handoff that asks for an established library, not a
  new custom parser, and separates bibliography parsing from semantic extraction.
- Hardened citation ingestion. DOI and PMID references can resolve to shared
  publication nodes; unidentified references remain paper-scoped. Added an
  explicit corpus-publication view so cited works cannot inflate corpus counts.
- Reframed the ontology around exact EuroQol research hits: study type,
  instrument and version, valuation and research method, statistical model,
  population, product, concept, finding, limitation, and source conflict.
- Completed version-3 ontology development with 100 competency questions, 100
  design papers, three independent Markdown proposals, synthesis, and an
  unchanged ten-paper holdout.
- Implemented a typed SQLite graph. Shared nodes hold exact query values;
  paper-specific use nodes hold roles, language, administration, perspective,
  inputs, and qualifiers. Findings contain aggregate results only.
- Parsed JATS metadata, authors, affiliations, funding, dates, URLs, and
  references with deterministic code before semantic extraction.
- Processed all 209 unique local JATS papers. The final set contains 207
  included studies, one excluded paper, and one correction notice.
- Completed an independent full-source audit of all 207 included records with
  a strong high-reasoning model. A total of 121 passed unchanged and 86 needed
  at least one material correction. Corrected all 86 and left no unresolved
  issue. The low-cost pass is now a draft stage, not a publication gate.
- Compared each paper with all date-eligible projects. Independently audited
  260 candidate pairs, retained 242 accepted links, and kept 14 possible links
  as non-materialized assessments. Corrected one false person-support link
  after final source adjudication.
- Kept support scope separate from project-output status. The trusted graph has
  185 study-support, 34 dataset-support, 18 person-support, 3
  publication-support, and 209 project-output edges.
- Tested `pdf-inspector` 1.15.0 on exactly six papers. Rejected it as the
  default because it silently corrupted 304 meaningful minus or inequality
  signs in five papers. Kept the current converter.
- Built the final local JATS database with 17,650 nodes, 26,143 relationships,
  7,030 semantic facts, 871 findings, 602 limitations, and 191 source
  conflicts. Structure, exact-domain, linkage, integrity, and foreign-key
  checks pass.
- Verified the Moroccan value-set path through valuation study, EQ-5D-5L, EQ
  VAS, cTTO, DCE, conditional logit, heteroskedastic Tobit, hybrid model, and
  Moroccan value-set and scoring-algorithm products.
- Moved stale development databases to Trash. They remain recoverable. The
  audited database is local and is not added to Git.

## 2026-08-17

- Added a shared designer preview workflow. `pnpm dev:remote` keeps the Nuxt
  frontend local and proxies API calls to `eq-graph.shoulde.rs`. `pnpm
  dev:local` keeps all fixture and SQLite work local.
- Extracted the production chat surface into one reusable workbench. Added
  `/chat-lab` with fixed empty, working, answer, chart, table, and error states.
  The lab and live agent now use the same components.
- Added the exact Node version, design branch instructions, preview routes, and
  data replacement seams to the repository documentation.
- Fixed server rendering for the working activity state and stopped accessible
  chart tables from changing the mobile page height.
- Deployed the preview to `eq-graph.shoulde.rs` as an isolated Node 24 service
  behind Caddy. Verified HTTPS, the live AI path, remote local development, all
  chat-lab states, the chart gallery, and desktop and mobile layouts.
- Replaced the designer chat landing surface with a full-height research
  workbench based on the original Nuxt 4 chat architecture. Restored the
  persistent header, internal transcript scroll, fixed composer, inline tool
  trail, ordered response parts, and visible follow-up questions.
- Moved the transcript scroll layer to the full cockpit width. The scroll rail
  now stays at the window edge while messages stay in the centered reading
  column.
- Added a real story-to-chat mode boundary. Completing the handover or using
  “Skip story” removes the narrative from the scroll range. “Back to story”
  restores the exact settled story position and keyboard focus.
- Limited categorical runtime charts to 12 marks and added rich-result scroll
  anchoring so a streamed answer cannot push a new chart above the viewport.
- Made categorical charts detect and correct reversed category and value
  fields from model specifications.
- Fixed italic Markdown inside answer tables and removed the obsolete designer
  chat CSS and its unused component rules.
- Rebuilt the scroll story as a hold-first timeline. Each scene now stays fully
  settled for about 78% of its range and changes during the remaining 22%.
  Added direct scene buttons, reduced-motion snapping, explicit scroll state,
  and a separate final handover range so the sixth scene has full reading time.
- Connected the redesigned chat surface to the existing Nuxt 4 AI SDK stream.
  Removed the unused canned chat endpoint.
- Replaced the unavailable Aura runtime path with the intended interim design:
  one model-written `query_sql` tool over a small SQLite database built from the
  temporary reference JSON. Query-only mode and the SQLite authorizer reject
  writes, schema changes, and PRAGMA actions.
- Let the same SQL call request a stat, bar, line, donut, or table. The answer
  uses the shared `GraphWidget` renderer and keeps the 11-template Observable
  Plot gallery at `/widgets`.
- Added safe streamed-answer formatting for prose, lists, links, and tables.
  Added chart-mark follow-up actions and a query disclosure in the activity row.
- Corrected the narrative and mock adapter so that only the 30 accepted
  project-publication links appear as confirmed. The 170 weak matches no longer
  inflate the linked-publication claims.
- Tested all six settled story states and the transition range on desktop and
  mobile. Tested the final story hold, chat handover, live model-to-SQL-to-chart
  path, stat and bar responses, chart selection, write rejection, keyboard
  targets, overflow, console errors, type checking, and the production build.
- Completed the version-3 ontology experiment: 100 papers, 100 competency
  questions, three independent ontology proposals, primary synthesis, and a
  ten-paper source-checked holdout.
- Human review approved the exact EuroQol domain direction and added a flexible
  concepts-and-themes layer. Removed fixed finding counts and made limitations,
  data-quality caveats, scope limits, gaps, and source conflicts explicit.
- Confirmed that JATS publication metadata is deterministic table stakes and is
  not an AI extraction task.
- Audited no-EQ papers for direct EuroQol support. Kept verified study, data,
  researcher, travel, and publication support types distinct. Reclassified the
  H09 project link as unverified because its article lists EuroQol grants only
  in one author's competing-interest statement.
- Paused the small relational pilot for final human confirmation.
- Completed the exact-domain ontology process with 100 design papers and 100
  competency questions. Replaced the long ontology description in the runtime
  task with a one-page domain graph and a flat typed search index.
- Approved one AI pass per paper for full-text assessment and conditional
  extraction. JATS metadata preparation, validation, normalization, and SQLite
  loading remain deterministic. A second AI call is only for a failed record.
- Tested 30 source-checked papers and corrected one corpus-boundary failure with
  two short rules. A seven-paper hard-case test supports `gpt-5.6-luna` as the
  first-pass model.
- Completed an unseen random 50-paper JATS production sample. All 50 calls
  completed. Three records needed a formatting repair; the final 50/50 records
  pass decision, structure, heading, and flat-index checks.
- Loaded 50 publications, 1,156 normalized terms, 1,474 record-term links, and
  4,174 fact bullets into SQLite. All nine integrity and search tests pass.
- Kept the production-calibration records local. No new full-text retrieval was
  started, and the completed Protocol 2.0 screen did not change.
- Completed the remaining 129 local JATS papers with the final task. Three
  structural repairs and a focused connection-label audit produced 129/129
  clean records. No sampled substantive fact needed correction.
- Reran the final task on the 30 source-checked calibration papers. After two
  targeted repairs, the result passed 30/30 expected decisions, 30/30 record
  checks, and 22/22 critical safety checks.
- Combined all 209 unique local JATS papers in SQLite: 206 included studies,
  two exclusions, one correction notice, 3,731 normalized terms, 5,786
  record-term links, and 16,471 fact bullets. All nine database and search
  checks pass.
- Recorded the complete local JATS result and moved the next gate to PDF input
  calibration. The abstract screen and retrieval state did not change.

## 2026-08-16

- Merged the approved designer surface into the current Nuxt 4 application.
  Ported the official logo, orthographic globe, 760-vh six-step narrative,
  scroll motion, story copy, and chat visual system. The separate Nuxt 3 shell
  and Cloudflare target did not enter the application.
- Added two temporary JSON reference fixtures and three Nitro endpoints. The
  narrative and chat now use the same reference records. Marked the adapter for
  replacement when the new ontology and SQLite schema are ready.
- Retained the Observable Plot gallery at `/widgets`, applied the paper and EuroQol
  green theme, and expanded the shared chat renderer with a donut mark.
- Added `DESIGN.md`. The production build, Nuxt type check, eight desktop story
  comparisons, mobile story review, mock chat flow, globe drag, source disclosure,
  and chart gallery checks pass.
- Integrated the useful parts of collaborator PR #2 while preserving its Git history.
  Kept the PDF converter and seven pilot PDF texts in `corpus/`.
  Excluded the separate Kotlin/Neo4j backend, duplicate derived files under `input/`, and the reduced duplicate pilot CSV.
- Confirmed that the corpus now has 227 converted documents: all 220 JATS XML files and seven pilot PDFs.
  The 60 other PDF files remain unconverted.
- Started a new ontology-development pilot.
  It uses three isolated lineages, the same frozen paper batches, fresh agents and flexible Markdown output.
  It does not prescribe ontology classes or a JSON output schema.
- Audited all 220 JATS files.
  Core bibliographic metadata is almost complete, and the XML has rich structured funding, affiliation, reference, section and table data that Markdown does not preserve fully.
  Raw JATS is now the canonical structured source; deterministic parsing precedes semantic AI work.
- Added the concise protocol, common agent task and XML audit under `pilot/ontology-development/`.
- Froze 30 unique development papers in three ordered batches of ten and a separate ten-paper holdout.
  The agent manifests contain only identity, format, path, hash and byte count; prior ontology labels remain outside the agent context.
- Completed round one in three isolated branches with fresh agent contexts.
  Each lineage verified the ten source hashes, applied its ontology to all ten papers, and recorded its decisions and open cases.
  The round-one commits are `92f51c8` (A), `b6b6cd8` (B) and `8fba6e8` (C).
  No semantic comparison occurred before the next round started.
- Completed round two with three new agent contexts and the same isolation controls.
  Each lineage covered all ten new papers and retained its earlier research record.
  The round-two commits are `e3e440c` (A), `e33c618` (B) and `7f50cfd` (C).
  No semantic comparison occurred before round three started.
- Completed round three and froze all three 30-paper lineage states.
  The round-three commits are `53a1f79` (A), `cbad9d1` (B) and `d5ef649` (C).
  All nine runs passed source identity, paper coverage and lineage-scope checks.
- Started a separate anonymous semantic comparison.
  A recorded seed randomized the candidate order, and the comparison workspace does not contain holdout papers.
  The comparison cannot rank candidates, choose a winner or propose a harmonized ontology.
- Completed the anonymous comparison and retained its exact inputs, task and run record.
  The lineages converge on a stable semantic core, including contribution, focal object, people and perspective, property-specific evaluation, derivation, output maturity, evidence dependence and scoped uncertainty.
  They differ materially in the main architecture and in boundaries for study components, comparisons, data quality, transparency and inferential terms.
  The papers support each architecture, so harmonization is paused for human direction.
- Prepared the controlled next stage without starting it.
  The holdout procedure requires unchanged application to all ten papers before any revision proposal and does not use a numeric score or pass threshold.
- Reworked the human architecture gate after the first decision note lacked usable context.
  The revised note gives one decision, three options, paper-level examples, trade-offs and an exact response.
- Human review selected the paper-first architecture and clarified that it must support detailed EuroQol research discovery and synthesis.
  Paper-first is the outer structure; domain-specific instruments, versions, languages, administration, methods, statistics, findings, interpretation, implications and gaps can require fine granularity.
- Audited the 100 positive and 20 negative competency questions.
  The broad list mixes project, funding, bibliometric and article-level needs, so version 2 uses a focused set of 27 paper and corpus questions without treating them as schema fields.
- Prepared ontology experiment version 2.
  It reuses the original 30 papers for direct comparison, adds a ten-paper method-granularity calibration round, and reserves a new ten-paper holdout from disjoint project groups.
  Three lineages will start from the same paper-first purpose but no proposed ontology.
- Froze version 2 at commit `858adec` after source, manifest, overlap and independent prompt checks passed.
  Created `experiment/ontology-v2-a`, `-b` and `-c` with isolated round-one worktrees and fresh agent contexts.
- Invalidated the first version-2 round-one attempt before accepting or comparing its outputs.
  One of three agents opened and used external Neo4j modeling guidance; the other two did not.
  Preserved all three outputs under the version-2 invalid-run record and restarted every lineage with equal explicit context controls.
- Completed the valid version-2 round one with source, scope and context checks.
  The commits are `84f60d9` (A), `d5e75b8` (B) and `5ccc284` (C).
  Started round two with three new agent contexts and no cross-lineage access.
- Completed version-2 round two with commits `0977ffc` (A), `b920143` (B) and `ec3aeda` (C).
  Started round three with three new agent contexts and the same isolation controls.
- Completed version-2 round three with commits `145b7c3` (A), `22f9159` (B) and `984d1b2` (C).
  Started the targeted round-four calibration with three new agent contexts.
- Completed the targeted round-four calibration with commits `9f928ee` (A), `ee9b833` (B) and `0fa020f` (C).
  Each lineage now covers 40 papers; fresh consolidation agents are reviewing late concepts against all earlier applications.
- Completed the independent 40-paper consolidation pass for all three lineages.
  The commits are `08f6b12` (A), `babce6f` (B) and `cb56305` (C).
  Each pass normalized unstable terms, checked late concepts against all earlier applications and retained unresolved evidence limits.
- Started the frozen-probe anonymous granularity comparison.
  Seed `2026081602` defines the candidate order; the comparator has all 40 development papers but no holdout paper or candidate mapping.
- Completed and retained the anonymous granularity comparison and its exact inputs.
  All three candidates support the paper-first core and all 27 focused questions.
  The material differences concern family boundaries, role separation, administration, task purpose, assessment classes, product state and application precision.
  The frozen probes found no focal retrieval miss, but they found broad-match risks and incomplete source-conflict capture.
- Completed independent harmonization and prepared one candidate for freeze.
  It uses purpose-based families, exact method paths, independent administration and product-state axes, component-scoped evidence lineage, attributed findings and a conflict-specific extraction pass.
  It fits all 40 development papers and supports all 27 focused questions and 14 probes.
  No material ontology alternative remains unresolved before holdout.
- Applied the frozen candidate unchanged to ten new, purpose-stratified holdout papers.
  All source identities and the candidate hash matched.
  The candidate fit all ten papers without a missing relation, forced family or required structural revision.
- Prepared the final human-review candidate.
  It applies four holdout wording clarifications for valuation-scale mapping, response-process targets, proxy perspectives and documented-effect levels.
  The clarifications add no controlled term or structural concept and do not change fit across the 50 evaluated papers.

## 2026-08-05

- Connected the Nuxt application to the real Neo4j Aura ontology pilot. The
  first checked load has 5,137 nodes, 8,661 relationships, 20 projects, 174
  works, 30 accepted attributions, 30 full texts, 20 studies, and 178 findings.
- Replaced the old layer-A-only agent schema with the complete closed graph
  model. Expanded graph search to identifiers, concepts, methods, conditions,
  properties, countries, working groups, journals, and value sets.
- Added a live graph-status endpoint and interface state. Added a read-only
  connection check and made all demo seed, reset, and migration commands refuse
  remote Neo4j hosts.
- Switched the application test agent from Claude Opus 5 to Claude Sonnet 5.
- Continued the frozen screen to 300/918 batches and 6,000/18,348 records. The
  validated checkpoint had 1,151 retained and 4,849 excluded decisions. The retention
  rate was 19.18%; no prompt, rule, corpus, or retrieval state changed.
- At the 6,000-record checkpoint, drew a second nonoverlapping random sample of 100
  exclusions from a 4,707-record frame with seed `2026080502`. A fresh blinded AI
  subagent agreed on 98 and retained two for adjudication. Direct review found both
  outside scope. Audit v2 found no confirmed false exclusion, so the frozen prompt was
  approved for completion.
- Completed the frozen scale screen: 918/918 batches and 18,348/18,348 records. The
  final validated result has 3,148 retained and 15,200 excluded decisions, for a
  17.16% retention rate. Exported cumulative, retained, and excluded CSV files.
- Strengthened the cumulative collector to verify selection-to-manifest identity,
  prompt hashes, cross-batch uniqueness, decisions, codes, and complete coverage. All
  final checks pass. No scale full-text directory or PDF article file exists.
- Paused the project before scale full-text retrieval. Added
  `scale/protocol-2.0/PAUSE_2026-08-05.md` with the exact state, unresolved gates, and
  ordered restart steps. Reconciled the README, canonical protocol, scale status,
  workplan, provenance index, reproduction guide, summary protocol, and final screen
  report with this pause point. Added current-state notes to the simple method and the
  historical pilot and production-check records so that they cannot be mistaken for
  the current scale state.

## 2026-08-04

- Verified that scale screening uses the local Codex CLI with saved ChatGPT
  authentication. It does not use an OpenAI Platform API key. OpenAlex network calls
  have a separate OpenAlex cost.
- Added `docs/PROVENANCE.md` to index source data, transformations, prompt inputs, AI
  run records, validators, results, and known provenance limits.
- Labeled `docs/METHOD.md` as historical and `PROTOCOL.md` as a summary. Updated the
  work-package states and corrected the README project source of truth. Protocol 2.0
  remains the governing method.
- Replaced the obsolete pilot umbrella validator with a current validation-suite
  runner. Updated the PubMed v2 validator for the current funnel fields.
- Audited the current method for hidden thresholds and candidate caps.
- Removed lexical project ranking and the 12-project cap from the current pipeline.
- Rechecked the 41 affected pilot articles with all 259 previously omitted candidates.
  The audit selected no omitted project, so canonical project links did not change.
- Invalidated an intermediate audit that missed three IDs joined to publisher XML text.
  The corrected rule checks literal canonical project IDs.
- Replaced fuzzy abstract title matching with normalized title-and-year matching. A
  prefix is allowed only when the source title explicitly ends with an ellipsis.
- Defined the scale full-text method to classify final funding scope directly. This
  removes the need for a corrective funding pass.
- Added `docs/METHOD_SIMPLE.md` as the short governing method.
- Replaced the old unflagged-profile shortcut with binary identity QA for all 271 chosen
  profiles. Accepted 222 and held 49; the author route now excludes all holds.
- Rebuilt the scale discovery union: 27,371 works, including 22,022 articles or reviews;
  14,836 have full abstracts. The independent funding route remains included.
- Reconciled the protocol, README, reproduction guide, scale status, build log, and
  machine-readable summary. They now use the same binary terms: `accept` and `hold`.
- Retrieved 14,102 ORCID work records and 3,110 PubMed records for the 222 accepted
  profiles. PubMed used exact ORCID identifiers; name-only discovery was not used.
- Merged 44,583 OpenAlex, funding, ORCID, and PubMed source records with the fixed DOI,
  PMID, then normalized title/year rule. The result has 28,600 records and no duplicate
  key. It includes 23,175 article or review candidates.
- Retained alternate DOI and PMID values for 667 exact title/year groups in one audit
  table. This avoids source-specific exception rules.
- Found abstract text for 14,853 candidates; 14,780 meet the basic 80-character gate.
  The corpus remains closed to screening until abstract enrichment and quality QA are
  complete.
- Recovered 3,568 abstracts from Europe PMC with exact DOI or PMID matching. The
  18,348-record screening input contains the full stored text; 4,827 records remain
  unavailable or too short.
- Added one scale-only screening rule: an unusable abstract field is E5. The EuroQol
  relevance rules remain unchanged from pilot v3.
- Validated scale prompt v1 on the prior 80 reference decisions and all six known
  pseudo-abstracts. It had zero outcome errors and excluded all six invalid fields.
- Froze 918 production batches. The operator inspected the first three batches: 60
  records, 18 retained, 42 excluded, and zero outcome disagreements. This was not an
  independent check.
- Continued the scale screen to a validated checkpoint of 50/918 batches and
  1,000/18,348 records. The checkpoint has 241 retained and 759 excluded decisions.
- Continued the same frozen scale screen to 100/918 batches and 2,000/18,348 records.
  The validated checkpoint has 431 retained and 1,569 excluded decisions. No prompt,
  rule, or corpus change occurred.
- Continued the frozen screen to 200/918 batches and 4,000/18,348 records. The
  validated checkpoint has 806 retained and 3,194 excluded decisions. The current
  retention rate is 20.15%; no prompt, rule, or corpus change occurred.
- Drew a simple random sample of 100 fresh exclusions from a 1,527-record frame with
  seed `20260805`. A separate blinded AI subagent agreed on 94 and retained six for
  adjudication. Direct review found all six outside the fixed scope. The audit therefore
  found no confirmed false exclusion, and scale prompt v1 remains unchanged.
- Cumulative collection validates every record ID, code, and outcome-code pair.

## 2026-08-03

- Froze the narrow `screening-v3` prompt. It retains direct EuroQol research and
  central measurement or valuation research. It excludes generic HRQoL, clinical,
  economic-model, and treatment-preference studies.
- Validated the prompt on three fresh random batches of 20 and one 20-record boundary
  check. There were zero false exclusions and zero false inclusions against operator
  reference labels. The final run repeated all 80 decisions with zero outcome changes.
- Found six invalid pseudo-abstracts during production. Marked them unavailable and
  rebuilt the screen from 1,088 to 1,082 valid title-and-abstract inputs.
- Final screen: 1,082 decisions; 201 retained; 881 excluded. Validation passed.
- Full-text retrieval: 123/201 machine-readable texts. Sources were 106 Europe PMC XML
  files and 17 OpenAlex open-access PDF files. Kept 78 unavailable articles unassessed.
- Full-text assessment: 81 direct EuroQol and 42 adjacent measurement or valuation
  articles after two documented manual adjudications.
- Funding-scope audit: 45 current-study EuroQol-funded articles. It separated related
  work, publication fees, and nonfinancial support from study funding.
- Project assessment: 29 explicit, 9 probable, 10 possible, and 75 no-link articles.
  Exported 50 candidate edges across 27 projects.
- Wrote the integrated 201-row paper assessment and pilot evaluation. The pilot passes
  with scale conditions. The main gates are profile QA, 61.2% full-text availability,
  and independent human validation before graph publication.
- Started an initial, pre-QA scale pass. Isolated 45 profile-review cases and provisionally
  used 271 unflagged profiles. Retrieved the 29 unflagged profiles that were missing from
  the cache.
- Kept 76 unreviewed split-profile assignments out of this provisional corpus. At least one
  suggested split ID was another person's chosen profile, so automatic inclusion would
  recreate name contamination.
- Added the independent OpenAlex EuroQol funding-metadata route: 739 works, including
  686 articles or reviews and 109 works not found through the provisional author route.
- Built a 36,560-work pre-QA OpenAlex discovery union. It had 29,155 articles or reviews;
  19,721 had full reconstructed abstracts. This superseded corpus is retained as build
  history and is not the current screening corpus.
- Checked funding metadata against pilot full texts. It found 33/45 current-study
  funding cases. Only 33/49 assessed metadata matches were current-study funding, so
  full-text confirmation remains mandatory.
- Protocol 2.0 10-person pilot: 3,032 accepted source records → 1,729 deduplicated records.
- Publication gate: 328 known non-journal/document exclusions; 1,401 article records.
- Abstract audit found 503 missing/invalid abstracts before enrichment.
- Europe PMC, Crossref and OpenAlex recovered 186; 313 remained unavailable and were excluded.
- Four duplicate papers exposed by enriched DOI/PMID metadata were merged; zero identifier duplicates remain.
- Screening-ready corpus: 1,088 records; validation passed.
- Previous 40-paper AI screen invalidated: nine records lacked abstracts and the relevance scope was too broad.
- `protocol-2.0.md` is now the canonical method/status document; no valid relevance result, full-text set or project-link set exists yet.

## 2026-07-28

- Explored `data/`: 944 projects in CSV, existing graph.json (2,116 nodes) already has
  projects/researchers/methods — publications layer is the gap. Agreed pipeline design
  with Paul: replayable numbered steps, one artefact each.
- **01**: 326 raw PI names → 310 unique (stripped ", PhD" suffixes, flipped
  "Michalowsky, Bernhard", nickname parens). 7 cells looked multi-PI; all were titles.
- Scraped 125 current members from euroqol.org via subagent (server-rendered page,
  `curl` was enough; WebFetch's summarizer wrongly claimed 180+ — verified 125 in DOM).
- **02** written + piloted on 40: caught a false positive ("Akanksha Akanksha" → prolific
  namesake "Ajay Singh" ranked first on EQ-works count) → added surname-compatibility
  gate. Added works-search fallback (`raw_author_name.search`) which resolved "A Finch"
  → Aureliano Paolo Finch. Guarded against authorships with null author ids.
- Full 02 run died at 100/310: **Paul's OpenAlex API key ran out of daily budget**
  (~$0.001/request, resets midnight UTC). Made key optional (env `OPENALEX_API_KEY`),
  errored entries retry on re-run. Free polite pool worked briefly, then also 429'd:
  **the budget is enforced per account = key + mailto + IP**, so keyless didn't dodge it.
  Anonymous (no mailto) also blocked. Fully stuck until reset → wrote 02b review sheet,
  03_works.py, and shared oa.py while blocked.
- Paul bought OpenAlex credits → resumed keyed. 02 finished: 278/310 resolved, 32 no-match.
- First 03 run: **every works request 400'd** — OpenAlex renamed the `grants` field:
  select wants `awards`/`funders`, filter is `funders.id:F…` not `grants.funder:F…`.
  Fixed 03/04 for the new schema (funders = list of {id, display_name, ror}; award ids
  live in `awards[].funder_award_id`).
- Second 03 run: 269/341 profiles + all 739 funder works; 72 profiles lost to transient
  per-minute throttle bursts that outlasted the 30s retry window → hardened oa.py backoff
  (8 attempts, exp. up to 60s), 03 now exits non-zero when any author fails.

## 2026-07-29

- Third 03 pass: 341/341, zero failures. **04**: 46,620 unique papers (686MB raw,
  128MB jsonl), 739 EuroQol-funded, 29,949 with abstracts.
- Award-id check: **202 papers carry an award id exactly equal to a Project Id**;
  209 pairs after regex normalization ("EQ-Project 343-RA" → 343-RA). Free certain links.
- **05** written + run (12s, pure stdlib TF-IDF): 209 award / 166k pi / 320 funder pairs.
  Score distribution says ≥0.5 is high-precision (327 pairs, almost all eq-funded);
  0.3–0.5 band (~10k) needs per-paper ranking, not a global threshold — an eq-funded
  paper gets the +0.20 bonus against *every* project of its PI.
- Spotted contaminated profile: "Yaling yang" 3,042 works (common-name merge). Left for
  Paul's 02_review.csv pass.
- Wrote README (context/approach/steps/known issues), this log, `.env` with the OpenAlex
  key, `.gitignore` for the day the repo gets git-init'ed.

## 2026-07-30

- Phase 2 kickoff: reconcile with Kazik's `shoulders-ai/eq-graph` (assessed in
  `FRIEND_REPO_EMPIRICAL_FINDINGS.md`). Position: the pipelines are complementary —
  Kazik's is the precision engine (grant-id + full-text mining → 318 accepted links,
  canonical 1,024-project table with start/end years and budgets), ours is the recall
  engine (author œuvres, citations, abstracts). Union via a shared typed-evidence
  model, not either/or.
- Wrote `docs/METHOD.md`: relevance definition on two axes — include iff
  **EuroQol-funded (F1) OR EQ-instrument-focused (C1)**; pure applications (C2)
  excluded unless funded, exactly Paul's rule. Unified evidence table E1–E8 (Kazik's
  max-weight framework absorbing our TF-IDF/timing composite as review-band evidence),
  PRISMA-style funnels, 3-stage screening (rules → LLM codebook → human adjudication)
  with dual-label calibration (200 papers, κ ≥ 0.8 target) and a 300-paper validation
  sample. Capture–recapture idea for linkage recall from the two pipelines' overlap.
  `[decide]` items flagged for Kazik.
- Wrote `docs/COMPETENCY_QUESTIONS.md`: 100 CQs across 6 personas (tagged output type,
  data needs, pilot-answerable — 55/100 work on the proposed pilot load) + 20 negative
  questions with expected refusal/caveat behavior. Doubles as ontology requirements
  for Kazik's Neo4j pilot and later as the evaluation benchmark.
- Decision proposed: adopt the 1,024-project export as canonical (fixes the 513
  year-less project ids; 2 local-only ids to investigate). 02b review pass still
  pending on our side.
- **Broad pre-filter experiment** (100%-sensitivity goal; iterated live with Paul):
  - Filters: junk doc-types (errata/retractions/peer-review/paratext, 862 papers);
    **green lane** — EuroQol-funded papers (736) bypass everything; wide EQ/HRQoL
    term list on title+abstract; time window vs project start year.
  - Iteration 1: words-only killed 8/209 sure links (EuroQol funds off-vocabulary
    topics: decision aids, caregiver burden) → green lane fixed it structurally.
  - Iteration 2: local project years (355/944 from id prefixes) made the time filter
    useless → cloned Kazik's repo, copied his 1,024-row export to
    `data/funded-projects-canonical.csv` (1,019 with Start Year).
  - Iteration 3: real years cut pairs 167k→48k but killed 5 answer-key links: 4 are
    **fake award links** (numeric-id digit collisions with other funders' grant
    numbers — 1963 atomic physics, 1992 chip design, Spanish EV charging…), 1 real
    (paper 2 yrs before recorded start) → widened window to **−2..+10**.
  - Final funnel: 46,620 papers → 15,063 pass; 166,556 pairs → **51,639 pairs /
    8,870 distinct papers** for the smart stage. Answer-key casualties: 3, all fake.
  - TODO from this: clean award tier (award must sit on the EuroQol funder record,
    sane year) — the "209 sure links" are really ~205.
