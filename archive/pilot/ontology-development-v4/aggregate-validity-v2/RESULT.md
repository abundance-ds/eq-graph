# Version-2 aggregate-validity test

Date: 2026-08-21

## Scope and method

- Tested all 100 competency questions against the version-2 release.
- Used `web/server/data/serving.sqlite` as the user-facing data source.
- Used `research-v2-v013.sqlite` only to diagnose citations, provenance, and
  other data that the public serving database omits.
- Judged the scientific answer, not only whether SQL could run.
- `NOT TESTABLE` is acceptable. It means that the required input is absent.
- No ontology, extraction record, registry, or database changed during this
  test.

Totals: 26 `PASS`, 33 `PARTIAL`, 15 `FAIL`, and 26 `NOT TESTABLE`. Of the 74
testable questions, 26 pass without a material qualification.

Verdicts:

- `PASS`: coherent and supported in the stated evidence-base scope.
- `PARTIAL`: useful, but an important scope, identity, field, or denominator is
  missing.
- `FAIL`: a current answer would be misleading or internally incoherent.
- `NOT TESTABLE`: the required evidence or external input is absent.

## Results

| ID | Verdict | Current result | Main cause |
|---|---|---|---|
| Q1 | PARTIAL | The stored portfolio has 1,024 projects and EUR 51,108,489 in approved budgets. Twenty-one budgets are zero and one project is an explicit test row. | Missing evidence |
| Q2 | PARTIAL | Start-year counts are available from 2012 to 2027. Five projects have no start year, and start year is not necessarily award year. | Missing evidence |
| Q3 | PARTIAL | The stored median is EUR 30,000 and the maximum is EUR 1,439,446. Zero cannot be separated from an unknown amount. | Missing evidence |
| Q4 | FAIL | Stored status gives 711 completed, 312 ongoing, and 1 closed. Fifty-six ongoing projects ended before 2026, and the closed row is the test project. | Extraction |
| Q5 | PARTIAL | Valuation is the largest source group. Joint groups have no budget allocation, so full attribution double-counts budgets and forced allocation invents precision. | Query or view |
| Q6 | PASS | Of 711 completed projects, 136 have at least one direct publication output in this evidence base. The link rule and denominator are clear. | — |
| Q7 | PASS | For 150 projects with usable years and a direct output, the median start-to-first-publication lag is 3 years. | — |
| Q8 | PASS | Direct output counts give a coherent ranking. Project 361-RA has 6 publications and project 2013240 has 5. | — |
| Q9 | PARTIAL | There are 219 completed projects that ended by 2023 and have no recorded direct output. Link absence is not proof that no publication exists. | Missing evidence |
| Q10 | FAIL | Paper instruments can be linked to 123 projects, but 221 project-instrument pairs result. Assigning the full project budget to each instrument double-counts funds. | Ontology |
| Q11 | NOT TESTABLE | Projects have no recipient-institution or recipient-country relation. Publication affiliations are not grant recipients. | Missing evidence |
| Q12 | NOT TESTABLE | The private database has within-corpus references, but it has no external citation counts. “Most cited” cannot be answered as stated. | Missing evidence |
| Q13 | PARTIAL | Study-family trends are coherent for publications. Project topics are not classified, and working-group labels are overlapping administrative categories. | Ontology |
| Q14 | FAIL | The 1,024 projects use 344 raw PI strings. Name variants change grant and budget rankings. | Extraction |
| Q15 | PARTIAL | Eight supported publications have no accepted project link. They are review candidates, but absence of a link does not show that no project can be identified. | Extraction |
| Q16 | PASS | The data can identify a funded country-specific value-set study. Morocco returns the 2025 EQ-5D-5L value-set study and project 1411-VS. | — |
| Q17 | PARTIAL | Linked outputs can be listed for a named project or exact author string. Applicant identity is not resolved across publications and projects. | Extraction |
| Q18 | NOT TESTABLE | No proposal abstract was supplied, and no stored similarity result exists. | Missing evidence |
| Q19 | PARTIAL | Cognition bolt-on projects and papers can be found. Project subject and instrument roles still depend on project-text screening. | Extraction |
| Q20 | NOT TESTABLE | No proposal aims were supplied. Project aims also lack a controlled subject layer. | Missing evidence |
| Q21 | NOT TESTABLE | Membership data is absent. | Missing evidence |
| Q22 | PARTIAL | A named grant with a clear PI and direct output can be timed. “Applicant X’s previous grant” is unsafe without resolved identity and exact award dates. | Extraction |
| Q23 | PARTIAL | Project text contains 248 value-set mentions. A mention is not a promised output, and missing links do not prove non-publication. | Ontology |
| Q24 | PARTIAL | Direct preference methods can be grouped by country and support link. Region membership is external, and unresolved method aliases split cTTO and DCE variants. | Registry |
| Q25 | PASS | The explicit `-SG` rule finds 11 student grants; 1 has a direct linked publication. The denominator is clear. | — |
| Q26 | NOT TESTABLE | No proposal target was supplied. Projects also lack controlled condition and instrument targets. | Missing evidence |
| Q27 | NOT TESTABLE | No proposal budget or agreed budget-band rule was supplied. | Missing evidence |
| Q28 | NOT TESTABLE | No proposal reference list was supplied. DOI matching is possible after such a list is provided. | Missing evidence |
| Q29 | PARTIAL | Country-specific value-set products can be listed for this 209-publication evidence base. It is not a complete global value-set register. | Missing evidence |
| Q30 | PARTIAL | EQ-VT versions 2.0, 2.1, and 2.6.1 are present. Unresolved protocol aliases and version-free labels prevent stable totals. | Registry |
| Q31 | PARTIAL | Ongoing EQ-HWB valuation candidates can be found, including project 1611-RA. Project status is stale in some rows and project targets are text only. | Extraction |
| Q32 | PASS | Publications from a named working group and time window can be listed. Joint group membership must be stated as overlapping. | — |
| Q33 | PASS | Existing 3L and 5L value sets can be identified as study objects or comparators. `ProductUse` now separates this from creating or applying a value set. | — |
| Q34 | PASS | Population-norm studies can be selected by primary family or ranked purpose and grouped by country within this evidence base. | — |
| Q35 | PASS | Mapping source and target functions support a coherent list of crosswalk studies. A scoped empty result is also safe. | — |
| Q36 | PASS | Youth self-report and proxy work can be selected from instrument uses, administration, and agreement findings. | — |
| Q37 | PARTIAL | Direct DCE valuation work is identifiable in multiple countries. Unresolved DCE aliases and missing study geography make exact totals unstable. | Registry |
| Q38 | FAIL | Frequent co-author rankings change with the selected person ID. Nancy Devlin has 30 publications but 27 person IDs. | Extraction |
| Q39 | PARTIAL | Bolt-on objects and study conditions can be listed. Condition labels and population roles are open text, so grouped condition totals need manual review. | Ontology |
| Q40 | FAIL | “Ongoing” project text mixes national valuation, methods, psychometrics, and background mentions; some stored ongoing projects have already ended. | Extraction |
| Q41 | PASS | Protocol objects and method-quality purposes distinguish papers that introduce or assess EQ-VT from routine protocol use. | — |
| Q42 | PASS | DCE-with-duration is separate from DCE without duration, direct use, source-study use, and discussion. | — |
| Q43 | FAIL | No funding statement or project link does not prove no EuroQol funding. The project-first evidence base is also unsuitable for this negation. | Missing evidence |
| Q44 | FAIL | Raw PI and author names are not resolved, and working-group fields can contain several groups. Researcher-span totals are unstable. | Extraction |
| Q45 | FAIL | Numeric sample rows mix respondents, interviewers, pilots, exclusions, and analysis inputs. Stage is controlled, but the counting unit and principal denominator are not. | Ontology |
| Q46 | PARTIAL | The private source has 25 publications that cite the 1997 Dolan paper. Citations are deliberately absent from the public serving database. | Query or view |
| Q47 | NOT TESTABLE | Membership data is absent, and person identity is not resolved. | Missing evidence |
| Q48 | NOT TESTABLE | Only 17 of 312 ongoing projects have any linked publication. Papers cannot supply a complete project-to-instrument target table. | Missing evidence |
| Q49 | PARTIAL | Test–retest work can be screened through measurement-property objects and findings. The exact property is not always linked to the tested instrument. | Extraction |
| Q50 | PASS | Direct current-study cTTO or TTO and DCE use can be required in the same value-set study. Context filters exclude reviews and discussion. | — |
| Q51 | PASS | Seven publications contain direct or object-level EQ-TIPS work. Use context supports a useful evidence summary. | — |
| Q52 | PASS | Translation targets, instrument language, product type, and publication form support a scoped list of published EQ-HWB adaptations. | — |
| Q53 | NOT TESTABLE | The data has no external citation counts, so a “ten most cited” reading list cannot be ranked. | Missing evidence |
| Q54 | PASS | Mapping functions, direct value-set products, and comparison papers support the crosswalk-versus-native distinction. | — |
| Q55 | NOT TESTABLE | Project host institutions are absent. Raw paper affiliations cannot replace them. | Missing evidence |
| Q56 | PARTIAL | `-PHD` and `-SG` identify 21 PhD and 11 student-grant projects. Supervisor and host-institution roles are not structured. | Missing evidence |
| Q57 | PARTIAL | Direct preference-method functions now separate elicitation from analysis. Unresolved aliases still split cTTO and DCE counts, and “should learn” needs a stated criterion. | Registry |
| Q58 | PASS | Twenty-six publications contain explicit EQ-5D-Y-5L use. Context and function support development, testing, valuation, and application views. | — |
| Q59 | PASS | Open-access status plus instrument-development purpose identifies the principal EQ-HWB development papers. | — |
| Q60 | PASS | Primary research family gives a coherent annual topic view. The answer must state that 2026 is incomplete and that the corpus is project-first. | — |
| Q61 | PARTIAL | Ninety-six reusable products can support a selected timeline. There is no neutral milestone rule, so completeness and importance need human criteria. | Ontology |
| Q62 | PARTIAL | Publication-time affiliation text can find candidates at an institution. It cannot show current employment, and institution and person identities are not normalized. | Extraction |
| Q63 | NOT TESTABLE | The evidence base is incomplete and has no authoritative country-by-value-set register. Absence cannot prove a gap. | Missing evidence |
| Q64 | NOT TESTABLE | Systematic reviews can be selected, but external citation counts are absent. | Missing evidence |
| Q65 | PASS | Youth-instrument use and journal metadata give a coherent scoped journal distribution. | — |
| Q66 | PASS | Project 1987-SG has one direct output, and its findings can be returned with the project and paper. | — |
| Q67 | PARTIAL | Topic, family, method, findings, and review status can produce candidates. No citation or importance signal supports a “good starter” ranking. | Missing evidence |
| Q68 | NOT TESTABLE | The denominator of all EQ-5D methodological literature is absent. The project-first corpus cannot supply the requested share. | Missing evidence |
| Q69 | PASS | The 209-publication evidence-base timeline is coherent: 2015–2026, with 50 publications in 2025 and 21 so far in 2026. | — |
| Q70 | NOT TESTABLE | Member status is absent and person identity is fragmented. | Missing evidence |
| Q71 | PASS | Of 193 distinct direct-output publications, 185 are marked open access. Annual counts and shares can be reported together. | — |
| Q72 | NOT TESTABLE | External citations and a complete set of researchers’ other corpus papers are absent. | Missing evidence |
| Q73 | NOT TESTABLE | Affiliations have no normalized institution-country relation. Study country is not author country. | Missing evidence |
| Q74 | FAIL | Publication-local person IDs make established authors appear as new entrants. | Extraction |
| Q75 | PARTIAL | All 172 evaluable links fall in the −1 to +8-year window; 70 of 242 links lack a required year and remain unknown. | Missing evidence |
| Q76 | PASS | Thirty publications link to more than one project. The maximum is 11, with study, dataset, person, and publication support kept separate. | — |
| Q77 | FAIL | PI strings are not resolved, and one publication can contribute to several PI-project assignments. Top-decile concentration is unstable. | Extraction |
| Q78 | NOT TESTABLE | Member status is absent. | Missing evidence |
| Q79 | PARTIAL | The private database has 573 resolved within-corpus citation edges across 162 citing and 130 cited publications. The public database omits them. | Query or view |
| Q80 | PARTIAL | Private citation and accepted project links can form an inter-project citation network. The public serving database cannot answer it. | Query or view |
| Q81 | FAIL | The raw rate is 150 ORCIDs among 1,151 person IDs. These IDs are not resolved researchers, so the denominator is invalid. | Extraction |
| Q82 | PARTIAL | One publication lacks an abstract; all have DOI and journal. There is no general metadata-quality or truncated-author-list flag. | Missing evidence |
| Q83 | PASS | Papers per project can be compared across working-group memberships if joint projects enter each group and the overlap rule is stated. | — |
| Q84 | FAIL | The 1,151 person IDs are not distinct researchers, and member status is absent. | Extraction |
| Q85 | NOT TESTABLE | OpenAlex topics and external citing-work fields are absent. | Missing evidence |
| Q86 | PARTIAL | Citation lag is available for 573 private within-corpus edges, from −1 to 10 years. The public database omits it. | Query or view |
| Q87 | NOT TESTABLE | There is no person-identity resolution audit log. | Missing evidence |
| Q88 | NOT TESTABLE | Venue-impact metrics are absent. Journal names are not impact measures. | Missing evidence |
| Q89 | PARTIAL | Project outputs and collaborators can be listed. External citations are absent and collaborator identity is fragmented. | Extraction |
| Q90 | PARTIAL | Private citation edges and exact product objects can identify candidate downstream references. Public citations and much product registry mapping are absent. | Query or view |
| Q91 | NOT TESTABLE | “Highly cited” needs external citation counts, which are absent. | Missing evidence |
| Q92 | PARTIAL | The project-to-output stages are coherent. Citation occurrences exist only in the private database and are within this 209-publication source set. | Query or view |
| Q93 | FAIL | PI-name variants and same-year ties prevent a valid first-time-PI classification. | Extraction |
| Q94 | FAIL | Publication-local person IDs create false collaboration nodes and false network growth. | Extraction |
| Q95 | FAIL | Population labels and roles are open text, and project topics are not typed. “Children” and “cognition” searches mix populations, instruments, and concepts. | Ontology |
| Q96 | PARTIAL | Seven strong bolt-on papers are identifiable by current-object and direct-use roles. Unresolved bolt-on identities prevent a complete “all papers” claim. | Registry |
| Q97 | NOT TESTABLE | Researcher countries cannot be derived from unnormalized affiliation text. | Missing evidence |
| Q98 | PASS | DOI lookup, accepted project link, support target, output flag, and support scope give a clear link explanation. | — |
| Q99 | NOT TESTABLE | Membership data and the full relevance-classified literature denominator are absent. | Missing evidence |
| Q100 | NOT TESTABLE | The source-ingestion route is not stored as a publication provenance field. | Missing evidence |

## Result

The paper ontology is not a dead end. Its primary family, purpose, design,
scientific-use context, function, product-use, finding, and limitation layers
support many coherent answers.

The release is not ready for unrestricted aggregate claims. Most remaining
failures do not require a new paper ontology. They require identity resolution,
project enrichment, safe registry work, explicit aggregate rules, and selected
private-to-public serving views.
