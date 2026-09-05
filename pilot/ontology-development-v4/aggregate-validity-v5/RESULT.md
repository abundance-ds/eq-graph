# Release aggregate-validity result

Date: 2026-08-27

## Result

The 797-publication release supports 90 of the 100 competency questions with a
full or bounded scientific answer.

- `PASS`: 54
- `PARTIAL`: 36
- `FAIL`: 6
- `NOT TESTABLE`: 4

`PASS`: Q1, Q3, Q4, Q6, Q7, Q8, Q12, Q14, Q16, Q17, Q19, Q24, Q27,
Q28, Q31, Q32, Q36, Q38, Q41, Q42, Q44, Q45, Q46, Q47, Q49, Q50,
Q52, Q53, Q54, Q57, Q59, Q60, Q61, Q64, Q65, Q67, Q69, Q71, Q72,
Q74, Q76, Q77, Q79, Q80, Q81, Q84, Q86, Q89, Q90, Q91, Q92, Q94,
Q96, Q98.

`PARTIAL`: Q2, Q5, Q9, Q10, Q13, Q15, Q18, Q20, Q21, Q22, Q23,
Q25, Q26, Q29, Q30, Q33, Q34, Q35, Q37, Q39, Q40, Q48, Q51, Q56,
Q58, Q62, Q66, Q68, Q70, Q75, Q78, Q82, Q83, Q87, Q93, Q95.

`FAIL`: Q11, Q55, Q73, Q85, Q88, Q97.

`NOT TESTABLE`: Q43, Q63, Q99, Q100.

## Method

- Two independent Sol reviewers tested Q1-Q50 and Q51-Q100 with read-only SQL.
- A fresh Sol reviewer adjudicated all 100 questions and all disagreements.
- A targeted check corrected one adjudication error: template questions were
  tested with real database examples instead of being rejected for a missing
  placeholder value.
- Opus was attempted first through Claude Code. Its subscription returned a
  zero-token limit response. No API key was available to either provider.
- `REVIEW_A.json` to `REVIEW_D.json` retain the raw verdicts and correction.

## Assessment

The paper ontology remains fit for release. No result shows a repeated missing
paper entity or relation that justifies changing it.

The six failures concern external enrichment, not fine-grained paper evidence:

- Q11 and Q55 need project recipient or host institutions.
- Q73 and Q97 need normalized author-country evidence.
- Q85 needs metadata about works that cite the included papers.
- Q88 needs a defined and sourced venue-impact measure.

The four unavailable answers are intentionally bounded. Missing funding text
cannot prove no funding; an incomplete corpus cannot prove global absence; the
included database cannot calculate an exclusion share; and the database does
not store the discovery route for each paper.

Three bounded questions need a stated analytical method: lexical similarity
for Q18 and Q20, and a community algorithm for Q70. These are query choices,
not ontology gaps. The test also found one stale hard-coded publication count
in the chat prompt. It was replaced with a requirement to query current counts.

## Decision

Keep the ontology frozen. Keep unsafe negative and absence claims unavailable.
Treat institutions, author countries, citing-work topics, and venue metrics as
optional external data work, not as reasons to expand paper extraction.
