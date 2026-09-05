# Expanded-corpus aggregate-validity result

Date: 2026-08-22

## Result

The 273-publication graph supports 83 of the 100 questions with either a full
or a bounded answer.

- `PASS`: 32
- `PARTIAL`: 51
- `FAIL`: 6
- `NOT TESTABLE`: 11

`PASS`: Q1, Q2, Q3, Q5, Q6, Q12, Q14, Q15, Q19, Q21, Q32, Q33, Q36,
Q37, Q38, Q42, Q44, Q47, Q50, Q51, Q57, Q58, Q61, Q64, Q65, Q69, Q70,
Q76, Q81, Q84, Q89, Q98.

`PARTIAL`: Q7, Q8, Q9, Q13, Q16, Q17, Q18, Q20, Q22, Q23, Q24, Q25,
Q26, Q27, Q28, Q29, Q30, Q31, Q34, Q35, Q39, Q41, Q46, Q48, Q49,
Q52, Q53, Q54, Q55, Q59, Q60, Q62, Q66, Q67, Q71, Q74, Q75, Q77,
Q78, Q79, Q80, Q82, Q83, Q86, Q87, Q90, Q91, Q92, Q93, Q96, Q99.

`FAIL`: Q4, Q10, Q40, Q43, Q45, Q95.

`NOT TESTABLE`: Q11, Q56, Q63, Q68, Q72, Q73, Q85, Q88, Q94, Q97,
Q100.

## Method

- Two independent reviewers tested Q1-Q50 and Q51-Q100 with read-only SQL.
- A fresh reviewer checked all 100 questions and all disputed verdicts.
- The lead review applied one rubric across all results and rechecked material
  changes against the database.
- A corpus limit alone did not reduce a corpus-scoped answer. Missing external
  evidence stayed `NOT TESTABLE`. A misleading aggregate stayed `FAIL`.
- The reviews used Claude Code through the user's subscription. The runner
  removed `ANTHROPIC_API_KEY` from each process.

The raw review records are `REVIEW_A.json`, `REVIEW_B.json`, and
`REVIEW_C.json`. They are evidence for this adjudicated result, not three
separate releases.

## Main assessment

The paper ontology remains fit for release. It supports coherent aggregation
of research family, purpose, design, instrument, method, product, finding,
limitation, author, project-link, and citation evidence. No result shows a
general missing paper entity that justifies an ontology change.

The six failures are known boundaries:

- Q4 and Q40 use project status that is stale in the source portfolio data.
- Q10 would allocate one project budget to overlapping instrument mentions.
- Q43 would infer no EuroQol funding from a selected EuroQol corpus.
- Q45 would mix respondent counts and task or observation counts.
- Q95 would turn free-text population descriptions into an unsupported
  classification.

The 11 untestable questions need data that the graph does not have. Examples
include grantee institutions, supervisors, a global value-set denominator,
unfunded literature, author countries, venue impact, citing-work topics,
pre-2015 collaboration evidence, and record-entry route.

Private JATS references support bounded answers for Q46, Q79, Q80, and Q86.
They remain `PARTIAL` because the 64 PDF papers do not yet have parsed
bibliographies and the public database does not expose reference lists.

## Change from the pre-PDF test

The earlier result was 44 pass, 35 partial, 6 fail, and 15 not testable. The
new totals are not a simple performance decline. This review used one stricter
rubric and corrected prior overclaims about complete project outputs,
international authorship, funded-versus-unfunded comparisons, and decade-level
network growth. It also promoted direct portfolio totals, exact support gaps,
typed DCE geography, the product timeline, community analysis, and ORCID
coverage where the current data supports them.

## Data correction found by the test

The public builder had labeled every publication as JATS. It now derives the
format from the private source record. The rebuilt database contains 209 JATS
and 64 PDF publications. This correction changes provenance metadata only.

## Decision

Keep ontology version 0.13 frozen. Keep unsafe answers unavailable or clearly
bounded. Do not add fine-grained sample or population structure to improve a
question score.
