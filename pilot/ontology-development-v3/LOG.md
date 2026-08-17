# Version-3 experiment log

## 2026-08-16: reset

- Reason: the version-2 candidate used generic concepts that did not feel natural to EuroQol research.
- Correction: center the work on exact, queryable domain facts and the 100 competency questions.
- Design: 100 broad papers; three 50-paper and 50-question ontology lineages; 50% shared inputs.
- Summary model: lower-cost agents create one fixed dense summary per paper.
- Ontology model: three independent Sol agents write plain Markdown proposals.
- Final responsibility: the primary agent compares all proposals and writes the final proposal for human review.

## Controls

- Fixed random seed `20260816` for question assignment.
- Positive questions Q1-Q100 included; negative controls B1-B20 excluded from this design round.
- Each lineage receives 25 shared questions and 25 private questions.
- Prompt audit completed before paper summarization.
- Audit changes: preserve verbatim source terms, add source pointers, label unsupported facts, and separate source labels from derived classifications.
- Deliberate decision: keep question assignment random as requested. Do not rebalance by topic.
- Planned summary quality check: verify the 25 shared papers before ontology generation.

## 2026-08-16: paper selection and assignment

- Initial selection: 100 unique papers, but approximately 50 were valuation papers.
- First correction: retain 30 core valuation papers and replace 20 papers with broader research purposes.
- Independent audit: repeated paediatric psychometric work remained overrepresented.
- Second correction: ten exact swaps added population norms, adult language validation, applied value-set updating, preference-based bolt-on selection, interviewer research, and multi-country data-quality work.
- Final selection: 100 unique DOIs and paths; all source hashes and byte counts verified.
- Paper assignment seed: `20260817`.
- Each lineage receives 25 shared papers and 25 private papers.
- `papers.tsv` SHA-256: `2526048498c39f2659d18bbdc15dd66e856082f39b51187ccffe0054a4d58258`.

## 2026-08-16: fixed paper summaries

- Lower-cost agents wrote one dense Markdown summary for each of the 100 papers.
- Summary length: 74,138 words in total; 496 to 1,011 words per paper after QA.
- All summaries contain the paper DOI, source path, source hash, source pointers, and high-value query terms.
- Three agents audited all 25 shared summaries against the full papers.
- Seven additional agents audited the 75 private summaries for ontology-critical facts.
- Corrections included language, administration mode, task order, respondent counts, model interpretation, product derivation, principal findings, and exact source wording.
- All final summary hashes, byte counts, and word counts are frozen in `summaries.tsv`.
- `summaries.tsv` SHA-256: `11e8cfff8b970009c7fa4f30941fba4e403d523b697ee9bb8663f45875a02b98`.

## 2026-08-16: Sol input packets

- Each packet contains 50 frozen paper summaries and 50 positive competency questions.
- Pairwise paper overlap: 25; union: 100.
- Pairwise question overlap: 25; union: 100.
- Paper-order seeds: A `20260818`, B `20260819`, C `20260820`.
- Question-order seeds: A `20260821`, B `20260822`, C `20260823`.
- Packet files do not label inputs as shared or private.
- Proposal agents can read only their packet, the common purpose, and the common ontology task.

## 2026-08-16: invalid proposal attempts

- The first A, B, and C Sol attempts each read the repository Neo4j modeling skill.
- This violated the packet allowlist and could bias the conceptual ontology toward graph-modeling patterns.
- All three attempts are preserved under `proposals/invalid/` and are excluded from comparison and synthesis.
- Fresh Sol contexts reran all three lineages with an explicit no-skill and no-standard instruction.

## 2026-08-16: valid independent proposals

- Three fresh Sol agents completed independent Markdown proposals from packets A, B, and C.
- Each agent verified all 50 supplied summary hashes and covered all 50 assigned questions.
- Each input audit lists only the repository `AGENTS.md` outside the packet allowlist.
- Proposal A: 9,409 words; SHA-256 `dda0ad89e576a0a9de058062bf8e5f397bd874293569bb5efd5b11a377417e08`.
- Proposal B: 10,559 words; SHA-256 `5285fab0e350851ef7c46a4b3d09f46d66fbf88c10bde46b9aacdad2d2c87ef0`.
- Proposal C: 7,889 words; SHA-256 `c338ce45c95daf29612bcfe34a43660327ce7535a82b5be97b5bc33bbb3546d7`.

## 2026-08-16: primary review and synthesis

- The primary agent read all three valid proposals in full.
- Main agreement: exact study types, instruments, instrument uses, populations, administration details, methods, protocols, task designs, models, products, and findings must be queryable.
- Main rejected agreement: all three proposals made a generic source-assertion layer too central. This would recreate a heavy claim-evidence structure.
- Final decision: use direct domain records with record-level provenance. Use a special conflict record only when sources disagree.
- Final decision: keep project and corpus records in a linked portfolio module. Keep calculated answers in a separate analytics layer.
- Final decision: use a relational database for the pilot. Do not let the database engine define the ontology.
- Comparison: `review/COMPARISON.md`; SHA-256 `4c86731c3c09185a5a8f37ed2b05b40cfed97fdece1f2fef1d71dc060578b695`.
- Final proposal: `review/FINAL_PROPOSAL.md`; SHA-256 `898b0001d1a4b61605805a27b0899c958840a4f6afa7b805a0d14ab06639ec02`.
- Question map: `review/QUESTION_COVERAGE.md`; SHA-256 `d2e4c4e431a2d044f8bd4b6898e8ca427943d9cd212f7a68feab5c8e539be31e`.
- Validation: Q1-Q100 each have one coverage row; all three review documents parse as GitHub-flavored Markdown; no trailing whitespace was found.

## 2026-08-17: unseen-paper holdout validation

- Selected ten unique DOI records outside the 100-paper ontology design set.
- Stress coverage: national valuation, DCE design, OPUF, instrument development, proxy content validity, population health, systematic review, language-version psychometrics, economic burden, and decision-support implementation.
- Three lower-cost agents produced ten compact Markdown extraction records from full articles.
- Different agents checked all ten records against the full sources. The primary agent also reviewed every record and the relevant article sections.
- Source QA result: ten passes after minor factual or terminology corrections; no extraction failure.
- Question tests: ten pass, two partial, zero fail.
- The H09 selection note incorrectly expected EQ-5D-5L. The article reports no EQ instrument. Extraction did not copy the assumption.
- Required revisions: separate research purpose from design; add source-dataset lineage; add review evidence units; add instrument-data reuse and visualization roles; keep family-specific detail inside existing concepts.
- The H09 economic-analysis profile is deferred because its EuroQol project link is not verified.
- No relational schema was designed. The next step requires human review of the concrete records.
- Revised holdout manifest SHA-256: `782c1ca68d29088d04b7b3763358ac1a0077699203ee1beead58397542b6d807`.
- Revised extraction task SHA-256: `830ac78f23cfce7f9cc3fa17b061996096ee8177ff8a43552eb69e097bac31ab`.
- Revised question test SHA-256: `d988ccdc27fac270e78dee9345ec50cbec34f2046f4d07bfe49da2829f2929a4`.
- Revised pilot revisions SHA-256: `4228e279c4ae1d3184265bc3b8a3a1cc03444c2ac03a04d8cb2152edaa2615be`.
- Revised pilot result SHA-256: `45883bf2fdd5be95c2c0a74d787aea5c5ade19f5ea2581b6fe41d9fe0fa7e6ca`.

## 2026-08-17: human policy review before database design

- Approved the exact-domain ontology direction.
- Added flexible, source-grounded concepts and themes for cross-study discovery. These terms do not replace exact core fields.
- Removed the fixed finding-count proposal. Extraction depth now follows the paper's contribution.
- Made reported limitations, data-quality caveats, scope limits, research gaps, and source conflicts explicit.
- Confirmed deterministic JATS publication metadata as required input before semantic AI extraction.
- Audited papers with no EQ instrument. Verified direct support can include travel grants, study funding, and data-collection funding.
- Reclassified H09 as an unverified project-link candidate. Its Funding section names other funders; EuroQol grants occur only in an author's competing-interest statement.
- Paused the relational pilot until final human confirmation.
- Revised final proposal SHA-256: `fb9f4074d3f77314ae96b171accfc37869b1009d3db7af13c39c1342f462d671`.
- Funding audit SHA-256: `5507125934a4b6395c58f731a0da84e646194cb41a8df3d3848d182f06b4b10c`.
- Metadata policy SHA-256: `3d13470f3f447c2e5094234306f83b0570e54fb2af551191125ae3f7a18119f3`.

## 2026-08-17: relational pilot and deterministic metadata gate

- Replaced the unverified H09 semantic case with H11, a verified
  EuroQol-funded paper that has no EQ instrument.
- Kept H09 as a rejected-link boundary case. It does not enter funded counts.
- Built a temporary SQLite implementation for ten scientific studies and one
  boundary publication.
- Stored exact domain facts in typed tables and flexible concepts in a
  discovery table.
- Stored 42 findings and 31 limitations. Finding depth varies by study.
- Ran 15 executable competency-query tests; all passed.
- Parsed all 220 repository JATS XML files twice.
- Metadata result: zero parse failures and zero nondeterministic outputs.
- Corrected group-author, licence-link, and reference-identifier handling.
- Decision: JATS XML supplies publication metadata before semantic AI
  extraction. Missing metadata remains null.
- The relational schema remains provisional until the broader extraction test.

## 2026-08-17: broader extraction and ontology v1

- Froze a second 20-paper batch outside the 100-paper design set and the first
  holdout.
- Stress cases include non-EQ funded research, translation, proxy research,
  evidence synthesis, longitudinal outcomes, remote valuation, recall,
  implementation, conceptual methods, a protocol, a retracted article, and a
  correction notice.
- Verified all 40 article and JATS hashes and all 20 JATS DOI values.
- Completed 20 source-checked Markdown records with 12 fixed semantic headings.
- Loaded 19 studies and 21 publications into a separate SQLite database. The
  correction notice is a publication but not a study; its parent publication
  is the twenty-first publication.
- Loaded 44 instrument uses, 37 methods, 28 models, 20 products, 98 findings,
  and 76 limitations.
- Added publication lifecycle and relations, study execution state,
  study-publication roles, input datasets, measurement-time roles, and material
  derivation steps to the relational model.
- Kept B05 and B18 project links as candidates because their articles do not
  report EuroQol funding.
- Preserved the B09 abstract-versus-Results conflict.
- Ran 23 executable broader competency checks; all passed.
- Confirmed that SQLite is sufficient for the tested use case. No graph
  database is justified at this stage.
- Consolidated the evidence into `ONTOLOGY_V1.md`.
- Next gate: human approval for a controlled 50-paper production calibration,
  before any full-corpus scale-up.
- Ontology v1 SHA-256: `2a0756e739f226ff63baa339472ba6cf4c14d2416719e45f098266318ea3ea21`.
- Scale-up decision SHA-256: `ebf6bf7ff66c0e09bc4aa20b9805a0cba50ef58c3e8aafab8ef29fc2cdb1d98b`.
- Broader source QA SHA-256: `53f1c775fe765909fc67866bce8cc24ed694a66d3b4660973bec2e591f9c2297`.
- Broader ontology fit SHA-256: `237c8654f8e00408a78b6a2de58c2ffc9a8227972504e963fdfafa8f5f3a54d7`.
- Broader query evaluation SHA-256: `bc903ba126305a95ea780a7fdf6cace1c2232e9bc822024c8ef333e53d827c5d`.
- Relational schema SHA-256: `deba37a1f9480c22516407c343ca550a2dfa18c1d6a5558b2c0d812eeaccf503`.

## 2026-08-17: one-pass production calibration

- Replaced the long ontology prompt with a one-page domain graph, one compact
  assessment and extraction task, and one flat typed search index.
- Kept full-text filtering and conditional extraction in one AI pass. Kept
  metadata preparation, validation, normalization, and SQLite loading
  deterministic. A second AI call occurs only when a check fails.
- Tested 30 source-checked papers. The initial pass made 29/30 correct corpus
  decisions and passed 21/22 critical safety checks. Two short boundary rules
  fixed the only failure: unrelated grants in competing interests do not fund
  the current output, and QALY or DALY use alone is application-only research.
- Found known abstract, body, and table conflicts in stress papers. Corrected
  the JATS parser so that it keeps the complete funding statement.
- Selected `gpt-5.6-luna` for the first pass after a seven-paper hard-case test
  passed all seven decisions and all 12 safety checks.
- Froze a random 50-paper JATS sample outside the 30 calibration papers with
  seed `20260817`. The first pass completed all 50 records with no run failure.
- Three records used prose instead of bullets under one or more headings. A
  targeted repair fixed all three. The composite result passes deterministic
  decision, structure, heading, and index checks for 50/50 records.
- The final set contains 47 direct EQ studies, two adjacent measurement
  studies, and one EuroQol-supported application-only study.
- Loaded the result into SQLite: 50 publications, 1,156 normalized terms,
  1,474 record-term links, and 4,174 fact bullets. All nine database and search
  tests pass.
- Source locators use several valid styles. The parser recognizes 87.2% of
  substantive bullets. The final task now requires one exact locator syntax.
- This stage used existing local JATS full texts only. It did not retrieve new
  papers or change the completed Protocol 2.0 abstract screen.

## 2026-08-17: complete local JATS pass

- Applied the final task to the remaining 129 unique JATS papers. All AI calls
  completed without a run failure.
- Repaired three structural failures and reviewed eight connection labels. The
  final 129/129 records pass deterministic checks.
- Audited all initial non-direct records, all no-support direct records, direct
  study types and titles, and ten varied papers against full text. No sampled
  substantive fact needed correction.
- Confirmed that EQ use only as a health outcome is `application_only`.
  Instrument, valuation, mapping, reference-norm, and measurement-
  implementation research is `direct_eq`.
- Reran the final task on the 30 source-checked calibration papers. Two targeted
  repairs produced 30/30 expected dispositions, 30/30 clean records, and 22/22
  safety checks.
- Loaded all three partitions into one local SQLite database. It contains 209
  unique publications, 3,731 normalized terms, 5,786 record-term links, and
  16,471 fact bullets. All nine database and search checks pass.
- Preserved ignored run trees with tracked workspace manifests. No new full
  text was retrieved, and the Protocol 2.0 screen did not change.
- Next gate: calibrate text preparation and extraction on the 60 local PDF-only
  files before scale retrieval.
