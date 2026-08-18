# Protocol 2.0

Canonical method and status. Graph construction excluded. The short, governing method
is in `docs/METHOD_SIMPLE.md`.

**Paused 2026-08-05:** the complete 18,348-record scale screen is validated. No scale
full text has been downloaded. Resume from `scale/protocol-2.0/PAUSE_2026-08-05.md`.

**Separate local result, 2026-08-18:** 209 project-first JATS publications have
completed full-text assessment, source verification, project linkage, and
typed SQLite graph loading. They produced 207 included studies. This result
does not change the pause or imply assessment of the 3,148 retained scale
records. See `docs/PIPELINE_RECAP.md`.

## Aim

- Identify journal articles plausibly produced by EuroQol-funded research.
- Assess EuroQol connection and possible funded-project link.
- Extract graph-ready evidence.

## Method

1. **Portfolio:** public EuroQol export → normalize → `data/funded-projects-canonical.csv`.
2. **People:** project leaders + current members → normalize/deduplicate → `artefacts/01_people.csv`.
3. **Profiles:** verify identity with name, affiliation, field, coauthors, and works.
4. **Profile QA:** check name, affiliation, field, coauthors, and works. Assign one
   binary decision: accept or hold. Only accepted profiles enter the author route.
5. **Paper discovery:** use accepted OpenAlex and ORCID IDs plus explicit EuroQol
   funding metadata. PubMed can add a paper only through an exact accepted ORCID ID.
   Do not use name-only PubMed discovery at scale.
6. **Bibliographic QA:** normalize metadata, then deduplicate by DOI, PMID, and
   normalized title and year, in that order.
7. **Article gate:** exclude non-journal outputs and document junk. Exclude abstract
   fields shorter than 80 characters. The AI screen assigns E5 to any longer field
   that is not a usable article abstract. It does not infer relevance from the title.
8. **Title/abstract screen:** AI excludes clearly unrelated papers and ineligible formats; uncertainty retained.
9. **Full text:** retrieve retained papers; unavailable full text flagged, never inferred.
10. **Paper assessment:** AI reads full text and directly classifies EuroQol connection
    and funding scope.
11. **Project assessment:** compare the paper with every project linked to its known
    people and every canonical project ID stated in the full text. Use no similarity
    score and no candidate cap. Allow no project, one project, or multiple projects.
12. **Extraction:** papers, authors, institutions, countries, instruments, methods, populations, topics, projects, citations and evidence → graph-ready tables.

## Fixed rules

- Include: full journal articles and reviews.
- Exclude: conference abstracts/proceedings, books/chapters, theses, preprints, blogs, editorials, commentaries, letters, corrections and retractions.
- No abstract or fewer than 80 abstract characters → exclude before AI screening.
- A longer field that is not a usable article abstract → exclude as E5 during AI
  screening. Do not decide relevance from the title.
- Generic HRQoL or health-economics content alone is insufficient.
- AI must cite brief record-specific evidence.
- No project matching before full text.
- Funding scope is classified directly. Publication fees, related-work funding, and
  nonfinancial support are not study funding.
- Every input, source response, exclusion, prompt, output and count is retained.

## Completed 10-person pilot result

- Projects: **1,024**.
- Current members: **125**.
- Deduplicated people: **316** = 297 project leaders + 125 members; overlap 106.

### Pilot funnel

1. Select **10 people**.
2. Identify and verify their ORCID, PubMed, OpenAlex and known Scholar profiles.
3. Retrieve publication records: ORCID 757 + OpenAlex 1,554 + PubMed 578 + Scholar 300 = **3,189**.
4. Reject one contaminated PubMed profile containing 157 records → **3,032 accepted source records**.
5. Merge repeated papers across people and sources using DOI, PMID, then normalized
   title and year → **1,729 unique records**.
6. Exclude 307 non-journal outputs and 21 document-junk records → **1,401 candidate articles**.
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

## Scale conditions and next work

1. Keep the frozen screening prompt and prompt hash.
2. Complete profile QA before each person's records enter the scaled corpus.
3. Improve lawful full-text retrieval and keep a manual retrieval queue.
4. Keep unavailable articles unassessed for funding and project links.
5. Add an independent human check before scale full-text processing. The pilot
   reference labels came from the same project operator.
6. Treat possible project links as review items, not confirmed graph edges.
7. Scale publication retrieval to all 316 people and add the separate funding-metadata
   discovery route.

## Scale-up status — paused after screening

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
