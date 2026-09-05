# Methods — EuroQol research knowledge graph

This document describes the study like a research project: aim, data sources,
definitions (inclusion/exclusion), the two independent pipelines, the reconciliation
protocol, the screening funnels, validation, and limitations. Empirical facts about
the project-first pipeline come from [`2026-07-29-grant-mining-pipeline-assessment.md`](2026-07-29-grant-mining-pipeline-assessment.md) (assessed at commit
`68ebeab`, 2026-07-29).

---

## 1. Aim

Build a knowledge graph of EuroQol-related research that links **funded projects**,
**publications**, **researchers**, and derived entities (instruments, methods,
conditions, countries, working groups), with typed, provenance-carrying edges, such
that the competency questions in `COMPETENCY_QUESTIONS.md` can be answered by graph
queries. Target store: Neo4j, fed from replayable pipeline artefacts.

## 2. Study design

Two pipelines were built independently and are now merged:

| | Pipeline A (literature-first) | Pipeline B (project-first, `abundance-ds/eq-graph`) |
|---|---|---|
| Strategy | **Author-centric** (recall): resolve every PI to an OpenAlex identity, harvest their full œuvre | **Project-centric** (precision): search funder indexes and full text for grant evidence per project |
| Sources | OpenAlex (works, authors, funders, references, citations, abstracts) | Europe PMC, Crossref, OpenAlex funder sweep, Unpaywall, CORE; full-text harvest |
| Strength | Complete publication universe of the researcher community; citation/reference edges; abstracts | Near-certain project↔paper links via grant-ID mining in full text; start/end years + budgets in project table |
| Weakness | Linking papers to *specific* projects is probabilistic | Finds only papers that leave an indexed funding trace; 80% of projects get no accepted link |

Design principle: **B supplies the certain links and the canonical project table;
A supplies the publication universe, author identities, and citation structure.**
Neither replaces the other; both write into one merged artefact set (§7).

## 3. Data sources

| Source | Role | Access |
|---|---|---|
| EuroQol grant export, 1,024 projects | Canonical project table (id, title, abstract, PI, WG, **status, start/end year, budget**) | public export, downloaded 2026-07-28 (project-first pipeline) |
| Local grant CSV, 944 projects | Superseded by the above; 2 project ids (`2015080`, `2016400`) exist only here — investigate, then retire | internal |
| OpenAlex | Author disambiguation, works, ORCID, funder field (`F4320323856`), references, citation counts, reconstructed abstracts | REST, cached, keyed |
| Europe PMC | Funding index, `GRANT_ID` queries, free-text "EuroQol Research Foundation", JATS full text | REST, cached |
| Crossref | Funder sweep (`501100006419`) | REST, cached |
| Unpaywall / CORE | OA full-text locations | REST, cached |
| euroqol.org | 125 current members (name, institute, profile URL) | scraped 2026-07-28 |
| `data/extractions.json` | Per-project LLM extractions: instruments, methods, countries, conditions, sample size, key finding | derived |

Adopt the 1,024-row export as the canonical project table. It strictly
dominates the local CSV (adds status/years/budget, fixes the 513 year-less ids) and
agrees with it on id/title/PI/WG for all 942 shared projects.

## 4. Definitions

### 4.1 Publication relevance ("is this paper EuroQol-related?")

Unit: one publication (article, chapter, preprint). Two orthogonal axes:

**Funding axis**
- **F1 — EuroQol-funded**: verifiable evidence that EuroQol (co-)funded the work.
  Accepted evidence, strongest first:
  1. structured grant metadata (OpenAlex `funders.id:F4320323856`, Crossref funder
     `501100006419`, Europe PMC funding index / `GRANT_ID`);
  2. a known Project Id within 300 characters of a "EuroQol" mention in full text
     (project-first full-text miner);
  3. free-text "EuroQol Research Foundation" in acknowledgements without a project id
     (paper-level funding evidence even when no project link resolves).
- **F0** — no such evidence.

**Content axis** — what role EQ instruments play in the paper:
- **C1 — instrument-focused (methodological)**: the paper's *contribution is about an
  EQ instrument or its methodology*. Includes: valuation studies / value sets;
  descriptive-system development; psychometric validation; translations and cultural
  adaptations; mapping/crosswalks **to or from** an EQ instrument; population norms;
  EQ-VT protocol work; bolt-on development; EQ-5D-Y / EQ-TIPS / EQ-HWB development;
  head-to-head comparisons where an EQ instrument is a primary subject; systematic
  reviews of EQ instrument properties or use.
- **C2 — instrument-as-tool (application)**: EQ-5D (etc.) used to measure outcomes or
  derive utilities in a trial, cohort, registry, or economic evaluation; the paper's
  contribution is about the disease/intervention/policy, not the instrument.
- **C3 — adjacent methodology**: health-state valuation or HRQoL-measurement
  methodology with **no** EQ instrument involvement (e.g., generic TTO/DCE methods work).
- **C0 — unrelated.**

**Inclusion rule:**

> **Include a publication iff F1 (EuroQol-funded, any content) OR C1
> (EQ-instrument-focused, any funder).**
> C2 pure applications are excluded unless F1. C3 defaults to exclude unless F1;
> borderline C1/C3 cases go to the review queue. The only open judgment is the C3 default-exclude rule.

Worked examples:

| Paper (sketch) | Funding | Content | Decision |
|---|---|---|---|
| "Valuing EQ-5D-5L health states in Indonesia: a TTO study" (no EQ funding) | F0 | C1 | **include** |
| "Refining the EQ-VT protocol" (EuroQol grant) | F1 | C1 | **include** |
| "Drug X vs placebo in NSCLC; EQ-5D secondary endpoint" | F0 | C2 | **exclude** |
| Same trial, but acknowledges a EuroQol grant | F1 | C2 | **include** (funded) |
| "Mapping FACT-G onto EQ-5D-3L" | F0 | C1 | **include** |
| "Cost-effectiveness of screening, using the UK value set" | F0 | C2 | **exclude** |
| "TTO vs DCE for health-state valuation" (no EQ instrument, unfunded) | F0 | C3 | review, default **exclude** |
| "EQ-5D-5L population norms for Poland" | F0 | C1 | **include** |

Note the split between two different properties:
- **Relevance** (paper-level) decides whether a publication node exists in the graph.
- **Linkage** (pair-level, §4.2) decides whether an `OUTPUT_OF` edge to a specific
  project exists. A paper can be relevant without any project link (e.g., an unfunded
  Polish norms study), and F1 can hold without a resolvable project id.

Graph membership: publication nodes only for the *included* set; the full
46k corpus stays in artefacts (needed for meta-analyses like "what share of a
researcher's output is applications"). Alternative: load everything with a
`relevance_class` property. Proposed: relevant-only nodes, corpus-level aggregates
stored as researcher properties.

### 4.2 Project linkage — unified evidence model

Merge both matchers into one **typed-evidence** model (the project-first framework, absorbing the literature-first signals). Each (paper, project) pair carries a list of evidence items; the pair
score is the **max** individual weight (no summing). Proposed weights:

| # | Evidence | Origin | Weight |
|---|---|---|---|
| E1 | Structured grant metadata credits the Project Id (OpenAlex `awards`, EPMC `GRANT_ID`, Crossref) | both | 1.00 |
| E2 | Project Id within 300 chars of "EuroQol" in harvested full text | B | 1.00 |
| E3 | Normalized project and paper titles identical | B | 0.95 |
| E4 | EPMC acknowledgement/full-text query returns the paper for this Project Id | B | 0.90 |
| E5 | Title similarity ≥ 0.95 | B | 0.80 |
| E6 | Title similarity ≥ 0.88 + PI is lead author | B | 0.65 |
| E7 | PI authorship + TF-IDF cosine (title+abstract vs project title+abstract) + timing window, per A's composite | A | 0.30–0.60 (maps A's score bands) |
| E8 | Paper is EuroQol-funded (F1) + PI authorship + plausible year, but no id-level evidence | both | 0.45 |

Tiers: **accepted** ≥ 0.85 (auto-edge), **review** 0.60–0.85 (human/LLM adjudication),
**weak** < 0.60 (retained in artefacts, no edge). E7/E8 additionally use **per-paper
best-project ranking** (an F1 paper must not link to *all* of its PI's projects —
A's calibration showed this is the dominant failure mode of a global threshold).
Tie-breakers for ranking: `extractions.json` overlap (instrument, country, method,
condition between paper and project).

`OUTPUT_OF` edges carry provenance: evidence kinds, weight, source pipeline(s),
snippet (for E2), retrieval dates, and adjudication status.

## 5. Funnels (PRISMA-style reporting)

Every count below is reported in the paper-trail; TBD cells get filled as the merge
lands. "A"/"B" mark which pipeline the number comes from.

**Funnel 1 — Projects**

```
1,024 canonical projects (B export)
  ├── 942 shared with local CSV (id/title/PI/WG agree; 82 abstracts differ)
  ├──  82 only in export (69 ongoing — mostly 2025–2027 starts)
  └──   2 only in local CSV (2015080, 2016400) → investigate         [TBD]
```

**Funnel 2 — Researcher identity (A)**

```
326 raw PI name strings → 310 unique names
  → 278 resolved to OpenAlex ids (257 ok, 11 via works, 9 ambiguous, 1 weak)
  →  32 unresolved (mostly early-career student-grant PIs)
  → human review of 42 flagged rows                                   [pending]
  → final identity table                                              [TBD]
```

**Funnel 3 — Publication identification (union, deduped by DOI, then PMID, then OpenAlex id)**

```
A: 46,620 works from 341 author profiles
A:    739 works via OpenAlex funder sweep (F4320323856)
B:    EPMC funding-index + "EuroQol Research Foundation" + Crossref sweeps  [count TBD]
  → union, deduplicated                                               [TBD]
```

**Funnel 4 — Relevance screening (§6)**

```
identified works
  → rule stage:  auto-include (F1 evidence or accepted link)          [~1,000+]
                 candidate band (EQ-term / title rules; ~3,070 have EQ terms in
                 title/abstract in A's corpus)
                 auto-exclude (no signal) + audit sample
  → LLM stage:   candidate band classified C1/C2/C3 with codebook     [TBD]
  → human stage: UNCLEAR + disagreements adjudicated                  [TBD]
  → included set (graph publication nodes)                            [TBD]
```

**Funnel 5 — Project linkage**

```
B: 209/1,024 projects (20.4%) with ≥1 accepted link; 318 accepted links (305 works)
   evidence: 223 full-text id-near-EuroQol, 217 structured grant id, 98 EPMC ack,
   11 exact title, 4 strong title, 2 fuzzy+PI
B:   9 review-band, 563 weak-only, 243 no candidate
A: 209 award-tier pairs (structured award id = Project Id), 166k gated PI pairs,
   320 funder-tier pairs; score ≥0.85 → 224 pairs / 147 projects
  → merged evidence model (§4.2): accepted / review / weak            [TBD]
```

(N.B. A's "209" counts *pairs* with award-id evidence; B's "209" counts *projects*
with an accepted candidate — same number by coincidence, different units.)

**Funnel 6 — Full text (B)**

```
318 accepted links → 257 with full text on disk (220 EPMC XML, 17 repository PDF,
15 manual browser, 3 indexed PDF, 2 publisher PDF) → 61 skipped
```

## 6. Relevance screening protocol

Three stages, each cheaper stage feeding the next only what it can't decide:

1. **Deterministic rules.** F1 evidence or an accepted link includes the paper. Title/abstract
   matching EQ-instrument terms (`EQ-5D`, `EuroQol`, `EQ-VT`, `EQ-HWB`, `EQ-TIPS`,
   value set/valuation/crosswalk/mapping/norms + instrument mention) places it in the candidate band.
   No signal auto-excludes, with a **100-paper random audit** of the excluded pool to
   estimate the false-exclusion rate.
2. **LLM classification** of the candidate band (title + abstract) into
   `FUNDED / METHOD (C1) / APPLIED (C2) / ADJACENT (C3) / OFF / UNCLEAR`, using a
   written **codebook** (§4.1 definitions + worked examples + decision rules).
   Calibration first: the two project leads independently hand-label the same **200 papers**
   (stratified over the band); measure inter-rater agreement (target Cohen's κ ≥ 0.8),
   reconcile the codebook, then measure LLM-vs-consensus agreement before running at
   scale. Model + prompt + version recorded.
3. **Human adjudication** of `UNCLEAR` and of LLM/rule disagreements; decisions logged
   (paper id, decision, reason) in an adjudication file, so every inclusion is
   reproducible or attributable.

**Validation.** Stratified sample of 300 (100 auto-included / 100 LLM-band /
100 auto-excluded), dual human labels, report precision and recall of the automated
funnel with 95% Wilson intervals. For *linkage* recall — where no gold standard
exists — use the two pipelines' quasi-independence: a **capture–recapture
(Lincoln–Petersen) estimate** of the total linkable population from the overlap of
A-accepted and B-accepted links (caveat: both depend on indexed metadata, so the
estimate is a lower bound on what full-text access would find).

## 7. Reconciliation & merge protocol

Canonical keys: **project** = Project Id (1,024 export); **work** = lowercased DOI,
else PMID, else OpenAlex id (merge records that share any key); **researcher** =
OpenAlex author id (never name — "Jeffrey Johnson" duplicates), ORCID attached.

Merge steps:
1. Adopt canonical project table; map both pipelines' outputs onto it.
2. **Cross-validation:** compare A's 209 award-tier pairs with B's structured-grant
   links (217) and full-text-mined links (223). Expect heavy overlap; every
   discrepancy is diagnostic (OpenAlex vs EPMC indexing gaps, id-normalization bugs).
   Deliverable: agreement table + discrepancy notes.
3. Build merged `works.jsonl` (union, with per-source provenance) and `links.jsonl`
   (typed evidence per pair, §4.2 tiers).
4. Run the relevance funnel (§6) over the merged universe.
5. Graph build: nodes (Project, Publication, Researcher, Institution, Instrument,
   Method, Condition, Country, WorkingGroup), edges (`OUTPUT_OF`, `AUTHORED_BY`,
   `CITES` from A's `referenced_works` within the included set, `FUNDED_BY`,
   `MEMBER_OF`/`is_member`, plus extraction-derived `USES_INSTRUMENT`, `USES_METHOD`,
   `STUDIES_CONDITION`, `IN_COUNTRY`). All edges carry provenance + snapshot date.

## 8. Neo4j pilot

Ontology design is **competency-question-driven**: the classes/relations above must be
sufficient to answer `COMPETENCY_QUESTIONS.md`; any good question the schema cannot
express is a schema gap, not a question problem.

Proposed pilot population: all 1,024 project nodes (cheap, enables
portfolio questions) + the **318 accepted links / 305 works** + their resolved authors
+ working groups + extraction entities for the 209 accepted projects + within-set
citation edges from A. Acceptance test: ≥ 15 of the competency questions answered
correctly in Cypher (the CQ doc marks which are pilot-answerable), and all 20 bad
questions handled per their expected behavior.

## 9. Limitations

- **Indexed-metadata dependence:** funding acknowledgements not indexed by
  OpenAlex/EPMC/Crossref are invisible unless full text was harvested; linkage recall
  is a lower bound, and the 55% weak-only projects partly reflect this, not absence of
  outputs.
- **Grey literature:** EuroQol plenary proceedings, theses, and reports are not
  covered; some projects' only outputs live there.
- **Author-profile noise:** OpenAlex merges/splits (e.g., "Yaling yang", 3,042 works);
  ~120 truncated author lists; mitigated by 02b human review, not eliminated.
- **Abstract availability:** ~36% of A's corpus lacks abstracts, so content
  classification for those rests on titles (lower confidence, routed to review).
- **Snapshot character:** citation counts and OA status are dated snapshots; the graph
  records retrieval dates and must be re-run to refresh.
- **Classification error:** C1/C2 boundary is genuinely fuzzy (e.g., a trial paper with
  a substantial EQ-5D psychometric analysis inside); quantified by the validation
  sample, not assumed away.

## 10. Reproducibility

Both pipelines are replayable from HTTP caches; all screening decisions (rules
output, LLM labels + prompt/model version, human adjudications) are written to
artefacts. Every reported funnel number must be recomputable by a script from
artefacts — no hand-maintained counts.
