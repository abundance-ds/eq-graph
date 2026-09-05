## Historical 10-person pilot result

This pilot used the former topic-based scope. It remains evidence about source
retrieval and model behavior, but its eligibility labels do not govern the
corrected screen.

- Projects: **1,024**.
- Current members: **125**.
- Deduplicated people: **316** = 297 project leaders + 125 members; overlap 106.

### Pilot funnel

1. Select **10 people**.
2. Identify and verify their ORCID, PubMed, OpenAlex and known Scholar profiles.
3. Retrieve publication records: ORCID 757 + OpenAlex 1,554 + PubMed 578 + Scholar 300 = **3,189**.
4. Reject one contaminated PubMed profile containing 157 records, leaving **3,032 accepted source records**.
5. Merge repeated papers across people and sources using DOI, PMID, then normalized
   title and year, producing **1,729 unique records**.
6. Exclude 307 non-journal outputs and 21 document-junk records, leaving **1,401 candidate articles**.
7. Abstracts: 896 valid source abstracts + 186 recovered from Europe PMC, Crossref,
   or OpenAlex; 313 unavailable and 6 invalid abstracts excluded.
8. Screen **1,082** articles; retain **201** and exclude **881**.
9. Retrieve machine-readable full text for **123/201** retained articles; keep 78 as
   unavailable and unassessed.
10. Assess 123 full texts: 81 direct EuroQol studies and 42 adjacent measurement or
    valuation studies.
11. Find current-study EuroQol funding in 45 assessed articles.
12. Find 29 explicit, 9 probable, and 10 possible project links. The 50 candidate
    article-project edges cover 27 projects. Possible links require review.

- Identifier duplicates exposed during enrichment: **4 merged; 0 remain**.
- Previous 40-paper AI screen: **invalid**; included records without abstracts and used an over-broad scope.
- Screening prompt validation: 60 fresh random records plus 20 boundary records; zero
  false exclusions and zero false inclusions against operator reference labels.
- Production repeatability: the same 80 records had zero retain/exclude disagreements.
- Full-text availability: **61.2%**. Funding and project links are not inferred for the
  78 unavailable articles.
- Project candidate audit: 41 articles received all 259 candidates omitted by the first
  12-project shortlist. The audit selected no omitted project, so canonical links did
  not change. The current method has no score and no cap.
- Pilot decision: pass with scale conditions. See
  `pilot/protocol-2.0/PILOT_EVALUATION.md`.

## Current files

- Project frame: `data/funded-projects-canonical.csv`
- Member source: `artefacts/00_euroqol_members.csv`
- People frame: `artefacts/01_people.csv`
- Pilot works: `pilot/protocol-2.0/derived/works.json`
- Per-person funnel: `pilot/protocol-2.0/person-funnel.csv`
- Abstract audit: `pilot/protocol-2.0/derived/abstract-enrichment.json`
- Screening prompt: `pilot/protocol-2.0/screening-v3/SYSTEM.md`
- Screening validation: `pilot/protocol-2.0/screening-final/validation.json`
- Full-text manifest: `pilot/protocol-2.0/fulltext/manifest.csv`
- Integrated paper assessment: `pilot/protocol-2.0/paper-assessment.csv`
- Article-project links: `pilot/protocol-2.0/article-project-links.csv`
- Pilot evaluation: `pilot/protocol-2.0/pilot-evaluation.json`
- Simple method: `docs/METHOD_SIMPLE.md`
- Provenance index: `docs/PROVENANCE.md`
- Scale full-text pilot: `scale/protocol-2.0/fulltext-pilot-v1/RESULTS.md`
- Corrected abstract prompt: `pipeline/prompts/abstract_screen_v2.md`
- Corrected abstract runner: `pipeline/run_codex_abstract_screen.py`
- Corrected screen result: `docs/ABSTRACT_SCREEN_RESULT.md`
- Full-text package builder: `pipeline/build_fulltext_paper_packages.py`
- Full-text retrieval runner: `pipeline/run_scale_fulltext_retrieval.py`
- Full-text retrieval result: `docs/FULLTEXT_RETRIEVAL_RESULT.md`
- Full-text preparation runner: `pipeline/prepare_scale_fulltexts.py`
- Full-text preparation result: `docs/FULLTEXT_PREPARATION_RESULT.md`
- Full-text processing result: `docs/FULLTEXT_PROCESSING_RESULT.md`
- Final SQL-interface pilot:
  `pilot/ontology-development-v4/production/sql-agent-pilot/RESULTS.md`
- Visual method map: `docs/methodology-workflow.html`

## Scale conditions and next work

1. Consolidate scientific identities and controlled-value extensions.
2. Load the included records and run database, aggregate, and release checks.
3. Keep the 72 unavailable articles unassessed for funding and project links.
4. Treat possible project links as review items, not confirmed graph edges.
5. Process newly accepted people as a separate deduplicated discovery tranche.

## Historical scale-screen result

The counts below describe the former topic-based screen. They do not establish
eligibility under the funded-project scope.

- Profiles accepted by binary identity QA: **222/316**.
- People held outside the author route: **94/316** = 45 original flags + 49 new QA
  holds.
- Additional plausible profile assignments held for review: **76** across 59 people.
  These IDs are not in the author route. The combined final review queue contains 137
  people.
- OpenAlex author-route works: **27,244**.
- Independent EuroQol funding-metadata works: **739**, including 127 works outside the
  accepted author route.
- Discovery union: **27,371** works.
- Accepted ORCID records: **14,102**. Exact-ORCID PubMed records: **3,110**.
- Full source input: **44,583** records. Exact DOI, PMID, and normalized title/year
  deduplication produced **28,600** records.
- Articles or reviews: **23,175**. Exact-identifier Europe PMC enrichment recovered
  3,568 abstracts. The frozen screening input has **18,348** records with at least 80
  abstract characters; 4,827 records remain unavailable or too short.
- The exact title/year step merged 667 groups with alternate DOI or PMID values. The
  alternate identifiers remain in the record and in an audit table.
- Scale prompt v1 changes no relevance rule from pilot v3. It adds one rule: exclude an
  unusable abstract field as E5 instead of stopping the batch. On the prior 80 reference
  records plus six known invalid abstracts, it had zero outcome errors. An operator
  check of the first 60 scale records also found zero outcome errors. These checks are
  not independent validation.
- Scale screening complete: 918/918 batches; 18,348/18,348 records; 3,148 retained and
  15,200 excluded. All record IDs, decision codes, and outcome-code pairs validate.
  The retention rate is 17.16%.
- A separate AI subagent reviewed a blinded simple random sample of 100 fresh
  production exclusions. It agreed on 94 and retained six for adjudication. Direct
  review found all six outside the fixed scope, so the audit has 100 true negatives
  and no confirmed false exclusion. This is an AI check, not independent human
  validation. Continue the frozen prompt unchanged.
- A fresh separate AI subagent reviewed a second blinded simple random sample of 100
  exclusions at the 6,000-record checkpoint. It agreed on 98 and retained two for
  adjudication. Both measured or presented constructs outside the fixed scope. Audit
  v2 also has 100 true negatives and no confirmed false exclusion. The frozen prompt
  is approved for completion.
- Funding metadata remains a discovery signal. Full text must confirm funding scope.
- In the assessed pilot subset, this route found 33/45 current-study funding cases. Of
  49 metadata matches with full text, 33 were current-study funding cases.
- Current scale files: `scale/protocol-2.0/`.
- Dated restart handoff: `scale/protocol-2.0/PAUSE_2026-08-05.md`.

---

# Protocol

## Aim

Identify EuroQol-funded publications, verify project links, and extract graph-ready data.

## Workflow

```text
1. People → 2. Publications → 3. Metadata screen → 4. Full-text verification → 5. Data extraction
```

## Phase 1 — People

| Step | Input | Action | Output | Result |
|---|---|---|---|---|
| 1. Projects | [EuroQol download](https://euroqol.org/research-at-euroqol/our-research-portfolio/funded-projects-download/) | Save all rows; key = `Project Id` | [`funded-projects-canonical.csv`](../../input/Funded projects – Table for Download - EuroQol.csv) | 1,024 projects |
| 2. Members | [EuroQol members](https://euroqol.org/about-us/our-members/current-members/) | Save name, affiliation, member ID and URL | [`00_euroqol_members.csv`](../../artefacts/00_euroqol_members.csv) | 125 unique members |
| 3. Project leaders | Project CSV | Normalise names; merge documented aliases | [`01_authors.csv`](../../artefacts/01_authors.csv); [alias decisions](../../data/person-name-overrides.csv) | 297 unique leaders |
| 4. Merge people | Leaders + members | Merge by normalised name and aliases | [`01_people.csv`](../../artefacts/01_people.csv) | 316 people; 106 both |
| 5. Resolve profiles | Merged people | Match in OpenAlex using name, EQ work, affiliation and ORCID; reuse prior results | [`02_author_ids.json`](../../artefacts/02_author_ids.json) | 282 reused; 34 queried; 286 OpenAlex IDs; 263 ORCIDs |
| 6. Review | Resolution results | Flag missing, ambiguous or suspicious profiles | [`02_review.csv`](../../artefacts/02_review.csv) | 45 flagged |

Google Scholar is not used. Unresolved people remain in the table.
