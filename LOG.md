# Build log

Chronological record of what was done, what broke, and how it was fixed.
Stable knowledge lives in README.md; this file is the narrative.

## 2026-08-05

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
