# Aggregate-validity rerun

Date: 2026-08-22

## Method

- Tested all 100 questions against the rebuilt public database.
- Reused a prior verdict only when its source tables did not change.
- Rechecked all person, membership, citation, and registry questions.
- Judged the scientific answer, not only whether SQL ran.
- Accepted `PARTIAL` and `NOT TESTABLE` when evidence was absent.
- Made no ontology change to improve a verdict.

Totals: 44 `PASS`, 35 `PARTIAL`, 6 `FAIL`, and 15 `NOT TESTABLE`.

## Verdicts

`PASS`: Q6, Q7, Q8, Q12, Q14, Q16, Q17, Q21, Q25, Q32, Q33, Q34,
Q35, Q36, Q38, Q41, Q42, Q44, Q47, Q50, Q51, Q52, Q53, Q54, Q58,
Q59, Q60, Q64, Q65, Q66, Q69, Q70, Q71, Q72, Q76, Q77, Q78, Q81,
Q83, Q84, Q89, Q92, Q94, Q98.

`PARTIAL`: Q1, Q2, Q3, Q5, Q9, Q13, Q15, Q19, Q22, Q23, Q24, Q29,
Q30, Q31, Q37, Q39, Q46, Q49, Q56, Q57, Q61, Q62, Q67, Q74, Q75,
Q79, Q80, Q82, Q86, Q87, Q90, Q91, Q93, Q96, Q99.

`FAIL`: Q4, Q10, Q40, Q43, Q45, Q95.

`NOT TESTABLE`: Q11, Q18, Q20, Q26, Q27, Q28, Q48, Q55, Q63, Q68,
Q73, Q85, Q88, Q97, Q100.

## Changed results

| ID | Prior | Current | Evidence and boundary |
|---|---|---|---|
| Q12 | NOT TESTABLE | PASS | OpenAlex has an exact DOI match for all 209 papers. The most cited funded paper has 950 citations and links to project 2016170. |
| Q14 | FAIL | PASS | All 1,024 projects now link to one of 297 resolved leaders. Grant and budget rankings no longer use raw PI strings. |
| Q17 | PARTIAL | PASS | A named applicant now links to their projects and accepted direct outputs through one resolved person identity. |
| Q21 | NOT TESTABLE | PASS | Observed membership and resolved authorship support a named applicant-to-member co-author query. |
| Q38 | FAIL | PASS | Resolved authorships support distinct-paper co-author counts for a named researcher. |
| Q44 | FAIL | PASS | A researcher can now link through authorship, accepted project outputs, and project working groups. Joint groups remain overlapping. |
| Q47 | NOT TESTABLE | PASS | Resolved authorship and 125 observed members support a member co-author list for a named researcher. |
| Q53 | NOT TESTABLE | PASS | Citation counts and typed study purposes support a scoped ranking of valuation-method papers. |
| Q64 | NOT TESTABLE | PASS | Citation counts and `EVIDENCE_SYNTHESIS` identify the most cited reviews in this evidence base. |
| Q70 | NOT TESTABLE | PASS | Resolved authorship supports a co-author network for the 102 observed members who appear as paper authors. |
| Q72 | NOT TESTABLE | PASS | Resolved authors, accepted project links, and citation counts support a comparison within the 209-paper corpus. |
| Q74 | FAIL | PARTIAL | First appearance in this corpus is valid. It does not prove that a person is new to the wider field. |
| Q77 | FAIL | PASS | Resolved project leaders support an output-assignment distribution. The top decile holds 36.9% of direct-output assignments. |
| Q78 | NOT TESTABLE | PASS | Resolved authorship and observed membership support non-member-to-member co-author counts. |
| Q81 | FAIL | PASS | Of 529 accepted individual paper-author identities, 443 have an ORCID: 83.7%. |
| Q84 | FAIL | PASS | The database has 683 individual people and 125 observed members. Six collective authors are separate group entities. |
| Q87 | NOT TESTABLE | PARTIAL | Resolution status and method are queryable. Detailed merge evidence remains in the audit files, not in the public database. |
| Q89 | PARTIAL | PASS | A project profile can combine accepted outputs, OpenAlex citation counts, and resolved collaborators. |
| Q91 | NOT TESTABLE | PARTIAL | Recent outputs can now be ranked by citations. “Success story” and “highly cited” still need stated editorial rules. |
| Q92 | PARTIAL | PASS | The public database now supports projects, projects with direct outputs, output papers, and dated OpenAlex citation totals. |
| Q93 | FAIL | PARTIAL | Resolved leader identities support “first recorded grant.” The data does not prove that it was the person’s first grant ever. |
| Q94 | FAIL | PASS | Resolved authorship supports a decade-by-decade co-author network without false person splits. |
| Q99 | NOT TESTABLE | PARTIAL | Membership is now available. The 209-paper corpus can give a local share, but it is not the full screened-literature denominator. |

## Stable non-pass boundaries

- Q4 and Q40 remain unsafe because source project status can be stale.
- Q10 remains unsafe because one project budget cannot be assigned in full to
  each instrument that appears in its papers.
- Q43 remains unsafe because silence about funding is not proof of no funding.
- Q45 remains unsafe because sample records do not define one comparable
  principal sample count. We accept this limit and do not add detailed sample
  fields only for this question.
- Q95 remains unsafe because project text does not provide a controlled target
  population. We accept this limit and do not add a detailed population layer
  only for this question.
- Registry questions stay conservative. Exact mapping improved, but unresolved
  labels remain explicit and do not receive forced identities.

## Decision

The ontology remains frozen. The rerun supports the person, membership,
citation, and exact-registry repairs. It does not support new sample or
population fields.
