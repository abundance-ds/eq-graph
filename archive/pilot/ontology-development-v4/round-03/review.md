# Round 3 confirmation review

## Review result

The two round-3 applications agree on the primary family, or the same family
gap, for all 15 studies.
Exact round-3 primary-family agreement is 15/15 (100%).
The blind version 0.2 regression agrees with the prior reviewed 30-study
partition for 27/30 studies (90%).
The three differences are material:

- G101 and S031 do not fit `METHODS_RESEARCH`.
- S099 does not fit `POPULATION_REFERENCE_DESCRIPTION` as its primary family.

This review accepts two narrow primary families:

- `HEALTH_PREFERENCE_RESEARCH` for G101 and S031; and
- `ECONOMIC_BURDEN_RESEARCH` for C005.

It also accepts:

- `ECONOMIC_BURDEN_ESTIMATION` as a purpose;
- `PARTICIPATORY_DESIGN` as a part-level `component_approach`;
- a source-dated `PublicationStatusAssertion` with `RETRACTED` as its first
  controlled state;
- `HEALTH_BEHAVIOR` as an outcome family; and
- a bounded extension of `HEALTH_OUTCOME_RESEARCH` to health behavior.

After these decisions, all 45 studies map to exactly one controlled primary
family. Version 0.2 is not stable enough to freeze because the accepted changes
affect the primary partition, part design, publication status, purpose, and
outcome typing.

## Agreement metrics

The unit is one round-3 paper.
For a multi-part paper, a metric compares the set of controlled values.
An omitted value is a disagreement.

| Controlled item | Exact agreement | Percent | Main differences |
|---|---:|---:|---|
| Primary family or family gap | 15/15 | 100.0% | Both applications leave C005 unmapped. |
| First-ranked purpose | 15/15 | 100.0% | Full agreement |
| Complete purpose set | 10/15 | 66.7% | C001, C007, C008, C009, and C010 |
| Publication form | 15/15 | 100.0% | Full agreement |
| Execution state | 15/15 | 100.0% | Full agreement |
| Result state | 15/15 | 100.0% | Full agreement |
| `StudyPart` count | 9/15 | 60.0% | Six part boundaries differ. |
| `component_approach` set | 13/15 | 86.7% | C009 and C012 |
| `temporal_structure` set | 12/15 | 80.0% | C006, C009, and C012 |
| `comparison_structure` set | 10/15 | 66.7% | Five papers differ. |
| `allocation_structure` set | 5/15 | 33.3% | Task randomization and no allocation cause most differences. |
| `mixed_method_integration` set | 13/15 | 86.7% | C009 and C012 |
| `data_origin` set | 11/15 | 73.3% | C004, C005, C009, and C012 |
| `data_level` set | 12/15 | 80.0% | C009, C012, and C014 |
| Applicable `synthesis_design` set | 0/1 | 0.0% | C014 narrative synthesis |

The applications are narrative records. Record-level percentages for every
use record are therefore not reliable. Material differences are adjudicated
below.

## Primary-family decisions

### Empirical health-preference research

Decision: `ACCEPT` `HEALTH_PREFERENCE_RESEARCH`.
Use it when the main contribution is direct empirical comparison,
description, or explanation of health preferences and none of these conditions
applies:

- the study develops a value set;
- the study primarily evaluates a valuation method or protocol;
- the study maps between instruments or scales; or
- the study is an evidence synthesis.

G101 compares preference patterns across 11 Asian DCE datasets. Its main output
is preference heterogeneity, not method performance or a new value set.
S031 explains preferences for health gains across recipient ages and gain
types. Its main output is an empirical preference result, not a method-quality
decision.
Decision: `REJECT` `METHODS_RESEARCH` for G101 and S031.
`PREFERENCE_COMPARISON` remains a multi-family purpose.
It does not replace this primary family.

### S099 population-reference boundary

Decision: `ACCEPT` the regression mapping to `HEALTH_OUTCOME_RESEARCH`.
Decision: `REJECT` the prior `POPULATION_REFERENCE_DESCRIPTION` mapping.
The stated aim is to assess HRQoL through pregnancy and postpartum.
The main result and conclusion describe change by pregnancy stage.
The statement that values can be used for future reference is a secondary use.
A national sample does not by itself make a population-reference study.
Use `POPULATION_REFERENCE_DESCRIPTION` only when norms, reference values, or
reference data are the stated main aim or principal output.
C004 meets this boundary.
Its aim is population health status, and its text calls the output population
data or population reference data.
S099 does not meet this boundary.

### Economic-burden research

Decision: `MERGE` application A's `BURDEN_OF_ILLNESS_RESEARCH` and application
B's `ECONOMIC_BURDEN_RESEARCH` into `ECONOMIC_BURDEN_RESEARCH`.
Decision: `ACCEPT` the merged family. Use `ECONOMIC_BURDEN_RESEARCH` when the
main contribution estimates the cost,
resource, productivity, or monetized wellbeing burden attributable to a
condition and does not compare decision alternatives.
Decision: `ACCEPT` `ECONOMIC_BURDEN_ESTIMATION` as the matching purpose.
Decision: `REJECT` `HEALTH_ECONOMIC_EVALUATION` for C005.
C005 estimates prevalent societal cost and monetized wellbeing loss.
It does not compare interventions or other decision alternatives.
Decision analysis and cost-of-illness estimation are not synonyms.
The new family is narrow. It is not a general burden or other-family category.

### C006 clinical-practice utilization

Decision: `ACCEPT` `APPLIED_USE_RESEARCH` for C006.
The primary outcome is PNB utilization.
The main analysis explains variation in that utilization.
The conclusion asks for more standardized PNB provision.
The clinical outcomes are secondary.
This meets the practical-use and implementation boundary of
`APPLIED_USE_RESEARCH`.
Decision: `REJECT` `HEALTH_OUTCOME_RESEARCH` for C006.
Use `HEALTH_OUTCOME_RESEARCH` when patient health is the main outcome.
Do not use it when use of a clinical practice is the main outcome and patient
outcomes are secondary.

### C015 health behavior with no EQ use

Decision: `ACCEPT` `HEALTH_OUTCOME_RESEARCH` for C015 with a bounded definition
change.
Add health-related behavior to the family definition.
Permit patient, condition-defined, exposure-defined, and general-population
samples when the main contribution describes, compares, explains, or follows a
health or health-behavior outcome.
Decision: `ACCEPT` `HEALTH_BEHAVIOR` as an outcome family.
Alcohol-consumption change is a health behavior.
It is not health status, HRQoL, or EQ VAS.
Decision: `REJECT` a new primary health-behavior family in this round.
The outcome contribution already fits the bounded health-outcome family after
the definition states the missing type.
C015 has no EQ instrument use.
EuroQol affiliation, support, or corpus selection does not create an
`InstrumentUse`.

## Structural decisions

### Part-level participatory design

Decision: `ACCEPT` `PARTICIPATORY_DESIGN` as a `component_approach`.
Keep the existing `PARTICIPATORY_DESIGN` method function.
These are separate controlled axes that use the same clear term.
Use the component approach when joint creation, refinement, or selection is
the defining way that a study part produces its output.
Use the method function for the exact co-design or participatory procedure.
Keep qualitative collection and analysis as separate method uses.
Do not force a co-design part to `QUALITATIVE_INQUIRY` when the source reports
no qualitative analysis and the principal process is generative design.
S057 directly supports the part-level value.
Its participants created artifacts, developed prototypes, tested them in mock
visits, and made final refinements.
C008 supports a completed participatory development part for consumer review
and pilot refinement.
C009 supports a participatory checklist-development part.
C012 supports a participatory bolt-on development part.
Decision: `REJECT` a current `PARTICIPATORY_DESIGN` use for C007.
C007 is Phase 1 qualitative inquiry.
Its findings inform later Phase 2 co-design.
The source assigns joint design work to the later phase.
The C007 participants still have `StakeholderInvolvement` records because the
source states their influence on later design scope.

### `TaskDesign`

Decision: `ACCEPT` the current `TaskDesign` structure without expansion.
The round confirms its value for C001, C008, C009, C010, and C011.
Store task blocks, task order, alternatives, profiles, and stopping rules in
`TaskDesign`.
Task randomization does not set study allocation.
C001 and C010 randomize cTTO and DCE blocks.
C011 randomizes task and perspective order.
Their study allocation is `NOT_APPLICABLE`.
C008 randomizes people to forced and unforced task arms.
Its survey-part allocation is `RANDOMIZED`.

### `StudyFactor`

Decision: `ACCEPT` the current `StudyFactor` structure and roles without a new
role.
Store a task attribute in `TaskDesign` first.
Create a separate `StudyFactor` only when the source analyses the attribute as
a determinant, comparator, stratifier, modifier, condition, or stage.
C011 valuation perspective is an analysed determinant and also an
administration fact.
It can therefore have both records.
Use `EFFECT_MODIFIER` only for a reported interaction or modification claim.
C011 supports it for severity where the source reports a severity-dependent
perspective effect.
Do not call PNB receipt in C006 a `STUDIED_CONDITION`.
It is the implementation outcome for the first analysis and an exposure for
the secondary outcome analysis.
`EXPOSURE_OR_DETERMINANT` is sufficient for the second use.

### `StakeholderInvolvement`

Decision: `ACCEPT` the current structure without a controlled role list.
C007 confirms that stated influence can exist without current joint design.
C008, C009, and C012 confirm joint refinement and support both stakeholder and
participatory records.
Ordinary interview, survey, or instrument completion does not create a
stakeholder record.

### Product-state rules

Decision: `ACCEPT` the current separate product-state assertions and
`asserted_by` relation without expansion.
Keep `preferred`, `developed`, `final`, `approved`, `validated`, `deployed`,
and `withdrawn` as distinct source assertions.
Do not infer a state date from publication date.
Do not convert ethics approval into product approval.
Do not convert article retraction into product invalidation or withdrawal.

## Publication retraction

Decision: `MERGE` both C010 proposals into `PublicationStatusAssertion`.
Decision: `ACCEPT` the record and initial controlled status `RETRACTED`.
Store:

- the exact editorial state;
- assertion date;
- `asserted_by` organization;
- notice identifier or relation;
- reason text; and
- the normal evidence locator.

The supplied C010 title states `RETRACTED ARTICLE`.
The supplied file does not include a notice, notice date, reason, or asserting
organization.
Decision: `KEEP_OPEN` those notice facts as `NOT_REPORTED` in this input.
The reported study remains `COMPLETED` with `RESULTS_REPORTED`.
The publication form remains `ORIGINAL_RESEARCH_ARTICLE`.
The publication status is `RETRACTED`.
These facts can coexist because they are separate axes.

## Round-3 paper-level adjudication

| Paper | Decision | Adjudicated mapping |
|---|---|---|
| C001 | `MERGE` | Keep value-set purposes, but reject `METHOD_OR_PROTOCOL_QUALITY`. Use separate cTTO, DCE, and hybrid-estimation parts. Study allocation is `NOT_APPLICABLE`; block assignment stays in `TaskDesign`. |
| C002 | `MERGE` | Use one reanalysis part. Record source administrations as source-study or input-provenance uses, and QI-Disability/QID-12 as current study objects where they are reduced or tested. |
| C003 | `ACCEPT` application B's allocation and context | Use one qualitative part, `NOT_APPLICABLE` allocation, and `CURRENT_STUDY_OBJECT` for the content-test object. Do not add participatory design. |
| C004 | `ACCEPT` application A's origin | Use `ROUTINE_SERVICE_COLLECTION` because the paper reuses the county Life & Health survey. Keep `POPULATION_REFERENCE_DESCRIPTION`. |
| C005 | `MERGE` | Use `ECONOMIC_BURDEN_RESEARCH` and `ECONOMIC_BURDEN_ESTIMATION`. The NESTT economic questionnaire is current collection for this investigation; published weights and costs are separate inputs. The burden model is noncomparative. |
| C006 | `ACCEPT` family; `MERGE` design | Keep `APPLIED_USE_RESEARCH`. Use THA and TKA parts, longitudinal claims observation, `DOCUMENT` data level, and no study allocation. Keep the two printed sample totals in conflict. |
| C007 | `ACCEPT` application B's boundary | Keep `IMPLEMENTATION_EVALUATION` and `CONTENT_VALIDITY_EVALUATION`. Reject current decision-support development and current participatory design. Retain stakeholder influence on planned co-design. |
| C008 | `MERGE` | Keep method purposes without `DECISION_SUPPORT_DEVELOPMENT`. Add a completed participatory development part. The planned survey is `BETWEEN_GROUP` and `RANDOMIZED` for forced/unforced arms. |
| C009 | `MERGE` | Use a participatory expert-development part and a quantitative member-survey part with `SEQUENTIAL` integration. Reject `DECISION_SUPPORT_DEVELOPMENT`. |
| C010 | `MERGE` | Keep value-set purposes without `METHOD_OR_PROTOCOL_QUALITY`. Separate pilot, cTTO, DCE, and estimation work when part-level detail is required. Task blocks do not create study allocation. Add retracted publication status. |
| C011 | `MERGE` | Use one coherent within-person experiment with VAS and TTO method uses. Study allocation is `NOT_APPLICABLE`; order randomization is a task fact. Store analysed perspective as an `EXPOSURE_OR_DETERMINANT`. |
| C012 | `MERGE` | Use a participatory development part and a quantitative survey part with `SEQUENTIAL` integration. Use separate data uses for literature, prior interviews, current panel input, and current survey responses. |
| C013 | `MERGE` | Use one pooled longitudinal analysis part with two prior-research DataUses. Use `WITHIN_PERSON` and `BETWEEN_GROUP` where applicable. Source instrument administrations are not direct current activities. |
| C014 | `MERGE` | Use `BETWEEN_CONTEXT`, `SYSTEMATIC_REVIEW`, and `NARRATIVE_SYNTHESIS`. Use separate document and aggregate-estimate levels. |
| C015 | `ACCEPT` with boundary change | Keep `HEALTH_OUTCOME_RESEARCH`, add `HEALTH_BEHAVIOR` outcome, and record no EQ use. EuroQol affiliation or support is not an instrument use. |

## General design boundary rules

Use `RANDOMIZED` or `NONRANDOMIZED` only for study assignment.
Use `NOT_APPLICABLE` when the study does not assign participants or units.
Task-block, screen-side, item-order, and perspective-order randomization belong
in `TaskDesign`.
Routine-care exposure does not become study allocation.
Use `LONGITUDINAL_REPEATED` when the same units contribute observations across
defined time windows.
This includes claims follow-up around an index event.
Use `VARIABLE_SOURCE_TIME` when variation in source dates is an input feature,
not as a substitute for longitudinal follow-up.
Use `ROUTINE_SERVICE_COLLECTION` for data collected as part of an established
service or monitoring system.
Use `CURRENT_STUDY_COLLECTION` when collection was designed for the reported
investigation, even when it occurs inside a larger named survey.
Use `DOCUMENT` for claims, charts, and source reports.
Do not map administrative records to `PARTICIPANT_RESPONSE`.

## Proposal decision register

| Proposal or dispute | Decision | Result |
|---|---|---|
| Empirical preference primary family | `ACCEPT` | Add `HEALTH_PREFERENCE_RESEARCH`. |
| G101 and S031 as methods research | `REJECT` | Map both to the new preference family. |
| S099 as population reference | `REJECT` | Map to `HEALTH_OUTCOME_RESEARCH`. |
| Cost-of-illness family names | `MERGE` | Add `ECONOMIC_BURDEN_RESEARCH`. |
| Cost-of-illness purpose names | `MERGE` | Add `ECONOMIC_BURDEN_ESTIMATION`. |
| C005 as health economic evaluation | `REJECT` | No comparative decision is present. |
| Part-level co-design gap | `ACCEPT` | Add `PARTICIPATORY_DESIGN` to `component_approach`. |
| C007 current participatory design | `REJECT` | Phase 1 informs later co-design. |
| Retraction status structures | `MERGE` | Add `PublicationStatusAssertion`. |
| Initial publication state | `ACCEPT` | Add `RETRACTED`. |
| Retraction as product invalidity | `REJECT` | Keep publication and product state separate. |
| C015 health-behavior outcome | `ACCEPT` | Add `HEALTH_BEHAVIOR`. |
| New C015 primary family | `REJECT` | Use bounded `HEALTH_OUTCOME_RESEARCH`. |
| C006 as health outcome | `REJECT` | Keep applied-use family. |
| New task fields | `REJECT` | Current `TaskDesign` fields are sufficient. |
| New factor role | `REJECT` | Current roles are sufficient for this batch. |
| Closed stakeholder role list | `REJECT` | Keep source-faithful activities and influence. |
| New product maturity sequence | `REJECT` | Keep independent source-dated assertions. |
| Catch-all primary family | `REJECT` | No catch-all is needed. |

## Source conflicts and source issues

Decision for every conflict below: `ACCEPT` the `SourceConflict` record.
Keep both statements with locators.
Do not silently repair a value.

### Carried 30-study conflicts

The prior review or blind regression already accepted these 11 conflicts:

| Paper | Conflict |
|---|---|
| G154 | Abstract and body use different taxonomy numbering for preference and instrument change. |
| S040 | Accrual precedes the printed ethics approval date. |
| S057 | Abstract gives nine service providers; Results gives 11 workshop service providers. |
| S058 | Abstract says the measure was developed; body text places instrument development and valuation in the future. |
| S062 | Table 3 gives five of 14 as 53.7%. |
| S071 | Review-flow text does not arithmetically produce the stated included set before update studies. |
| S084 | Abstract and numeric results order two level-3 bolt-ons differently from Discussion. |
| S089 | Abstract rollout total is 68,411; country counts sum to 68,416. |
| S089 | Bot threshold is below 0.5 in one place and 0.5 or less in another. |
| S099 | Nine of 6,661 is printed as 1.4%. |
| S099 | The bisexual total and wave cells do not agree. |

### Round-3 conflicts

| Paper | Conflict | Required handling |
|---|---|---|
| C002 | Alpha is 0.85 in Abstract/Discussion and 0.84 in Results. | Preserve both values. |
| C002 | Martin-Loef is greater than 0.99 in Abstract and 0.12 in Results. | Preserve both values; both statements say the test does not reject unidimensionality. |
| C006 | Abstract gives 52,926 THA and 94,795 TKA cases; Results gives 52,000 and 93,448. | Preserve both sets. Do not repair the total. |
| C011 | Abstract says VAS variance is higher for child perspectives; Results and Discussion say it is higher for adult perspectives. | Preserve both directions. Use numeric Results only when a locator-specific result is requested. |
| C013 | Methods gives 842 manifest patients, but cohort components 525 and 310 sum to 835. | Preserve all printed counts. |
| C013 | Abstract gives negative SARA and PHQ-9 correlations; Results prints positive values while it describes inverse trends. | Keep direction unresolved. |
| C014 | Abstract periods are 1990–2010 and 2011–2020; Methods periods are 1999–2010 and 2011–2019. | Preserve both period definitions. |
| C014 | Preference-source denominator is 4,025; the review total is 4,052 HSUs. | Preserve both denominators. |

The cumulative conflict count is 19.
The following four items are `SourceIssue` records, not `SourceConflict`:

- G015 reverses the EQ VAS anchors in one statement.
- C009 says seven items were required by more than 100% of respondents.
- C013 calls a one-year change with `p = 0.095` significant.
- C015 gives the GAD-7 range as 0–21 but uses an upper category of 10–27.

## Open items

Decision: `KEEP_OPEN` C010 notice date, notice identifier, reason, and asserting
organization as `NOT_REPORTED` in the supplied file.
Decision: `KEEP_OPEN` all 19 conflicting exact values until an authoritative
correction or linked notice resolves them.
The following prior missing-information items remain open as `NOT_REPORTED`:

- G160 interviewer-score construction and weighting detail;
- S017 early convenience-test count;
- S040 completion mode, channel, and language;
- S058 included-evidence count;
- S089 exact language and version identities;
- S091 exact language and version identities; and
- S100 source-trial EQ-5D version distribution.

These open items do not require a new primary family or catch-all value.

## Revised 45-study family table

| Round | Study | Primary family after review | Change from supplied reviewed state |
|---:|---|---|---|
| 1 | G109 | `VALUE_SET_DEVELOPMENT` | None |
| 1 | G101 | `HEALTH_PREFERENCE_RESEARCH` | Replaces prior methods mapping and regression gap |
| 1 | G125 | `POPULATION_REFERENCE_DESCRIPTION` | None |
| 1 | G160 | `METHODS_RESEARCH` | None |
| 1 | G195 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 1 | G010 | `APPLIED_USE_RESEARCH` | None |
| 1 | G196 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 1 | G116 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 1 | G131 | `APPLIED_USE_RESEARCH` | None |
| 1 | G014 | `EVIDENCE_SYNTHESIS` | None |
| 1 | G083 | `HEALTH_ECONOMIC_EVALUATION` | None |
| 1 | G015 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 1 | G168 | `METHODS_RESEARCH` | None |
| 1 | G154 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | None |
| 1 | G146 | `VALUE_SET_DEVELOPMENT` | None |
| 2 | S002 | `METHODS_RESEARCH` | None |
| 2 | S017 | `METHODS_RESEARCH` | None |
| 2 | S024 | `METHODS_RESEARCH` | None |
| 2 | S031 | `HEALTH_PREFERENCE_RESEARCH` | Replaces prior methods mapping and regression gap |
| 2 | S040 | `HEALTH_OUTCOME_RESEARCH` | None |
| 2 | S052 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 2 | S057 | `APPLIED_USE_RESEARCH` | None |
| 2 | S058 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 2 | S062 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 2 | S071 | `EVIDENCE_SYNTHESIS` | None |
| 2 | S084 | `METHODS_RESEARCH` | None |
| 2 | S089 | `METHODS_RESEARCH` | None |
| 2 | S091 | `HEALTH_OUTCOME_RESEARCH` | None |
| 2 | S099 | `HEALTH_OUTCOME_RESEARCH` | Replaces prior population-reference mapping |
| 2 | S100 | `EVIDENCE_SYNTHESIS` | None |
| 3 | C001 | `VALUE_SET_DEVELOPMENT` | None |
| 3 | C002 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 3 | C003 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 3 | C004 | `POPULATION_REFERENCE_DESCRIPTION` | None |
| 3 | C005 | `ECONOMIC_BURDEN_RESEARCH` | Resolves `UNMAPPED_VALUE` |
| 3 | C006 | `APPLIED_USE_RESEARCH` | Confirmed after source check |
| 3 | C007 | `APPLIED_USE_RESEARCH` | None |
| 3 | C008 | `METHODS_RESEARCH` | None |
| 3 | C009 | `METHODS_RESEARCH` | None |
| 3 | C010 | `VALUE_SET_DEVELOPMENT` | Retraction is separate |
| 3 | C011 | `METHODS_RESEARCH` | None |
| 3 | C012 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 3 | C013 | `HEALTH_OUTCOME_RESEARCH` | None |
| 3 | C014 | `EVIDENCE_SYNTHESIS` | None |
| 3 | C015 | `HEALTH_OUTCOME_RESEARCH` | Confirmed with health-behavior boundary |

## Complete 45-study partition

The counting unit is one distinct manifest study. The denominator is 45.

| Primary family | Study IDs | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | G109, G146, C001, C010 | 4 |
| `MEASUREMENT_PROPERTY_EVALUATION` | G195, G015, S052, C003 | 4 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | G196, G116, S058, S062, C002, C012 | 6 |
| `POPULATION_REFERENCE_DESCRIPTION` | G125, C004 | 2 |
| `METHODS_RESEARCH` | G160, G168, S002, S017, S024, S084, S089, C008, C009, C011 | 10 |
| `APPLIED_USE_RESEARCH` | G010, G131, S057, C006, C007 | 5 |
| `EVIDENCE_SYNTHESIS` | G014, S071, S100, C014 | 4 |
| `HEALTH_ECONOMIC_EVALUATION` | G083 | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | G154 | 1 |
| `HEALTH_OUTCOME_RESEARCH` | S040, S091, S099, C013, C015 | 5 |
| `HEALTH_PREFERENCE_RESEARCH` | G101, S031 | 2 |
| `ECONOMIC_BURDEN_RESEARCH` | C005 | 1 |
| **Total** | **All 45 studies, each once** | **45** |

No `UNMAPPED_VALUE` remains, and no catch-all family was added.

## Regression effects

The blind regression correctly detects two repeated preference-family gaps.
It also correctly detects the S057 part-level co-design gap.
The accepted `HEALTH_PREFERENCE_RESEARCH` family resolves G101 and S031.
The accepted part-level `PARTICIPATORY_DESIGN` value resolves S057.
The regression mapping of S099 to `HEALTH_OUTCOME_RESEARCH` is retained.
This changes one prior reviewed family assignment.
No other earlier primary family changes.
The task, factor, stakeholder, method-function, and product assertion structures
remain valid.
The round-3 evidence adds boundary rules but does not require replacement of
those structures.
All 11 carried source conflicts remain active.
Regression omission of a prior accepted conflict does not remove its record.

## Stability and next-batch decision

Version 0.2 is not stable enough to freeze.
This confirmation round produces:

- two new primary families;
- one new purpose;
- one new outcome family;
- one part-level approach;
- one publication-status record and state; and
- two material family-boundary clarifications.

The low allocation agreement also shows that the allocation rule needs the
explicit study-assignment boundary above.
Do not move directly to a larger batch or the full corpus.
Required next actions are:

1. Revise the ontology to version 0.3 with the accepted decisions.
2. Reapply version 0.3 to all 45 studies.
3. Confirm the exact-one primary-family partition.
4. Confirm the part-level participatory mapping on S057, C008, C009, and C012.
5. Confirm publication-status separation on C010.
6. Run one more diverse 15-paper batch to reach 60 cumulative studies.

A freeze can be considered after that batch if it adds no family, key, record,
or controlled design value and causes no earlier family change.

## Exact inputs

The review read these repository files in full:

- `AGENTS.md`;
- `pilot/ontology-development-v4/ROUND3_REVIEW_TASK.md`;
- `pilot/ontology-development-v4/PROTOCOL.md`;
- `pilot/ontology-development-v4/ONTOLOGY.md`;
- `pilot/ontology-development-v4/EXTRACTION_TASK.md`;
- `pilot/ontology-development-v4/round-01.tsv`;
- `pilot/ontology-development-v4/round-02.tsv`;
- `pilot/ontology-development-v4/round-03.tsv`;
- `pilot/ontology-development-v4/regression-v0.2.md`;
- `pilot/ontology-development-v4/round-02/review.md`;
- `pilot/ontology-development-v4/round-03/application-a.md`; and
- `pilot/ontology-development-v4/round-03/application-b.md`.

The review did not use an old ontology, old proposal, graph record, production
extraction, or excluded research file as scientific evidence.

## Exact article source-check log

Only passages that could change a controlled mapping, family decision,
structural decision, or conflict record were checked.

| Paper | Checked passages | Decision supported |
|---|---|---|
| G101 | Abstract; aim; Methods; Discussion; Conclusion | Empirical preference family |
| S031 | aims; PTO design; Results; Conclusion | Empirical preference family |
| S057 | Abstract; co-design methods; workshops; prototype; Conclusion | Part-level participatory design |
| S099 | Abstract; aim; Discussion; Conclusion | Health-outcome versus population-reference boundary |
| C001 | Study Design; Valuation Interview; Data Analysis | Part boundary and task versus allocation |
| C002 | Abstract; Results; Discussion | Two psychometric conflicts |
| C003 | Objective; Sample and Recruitment; Procedure; Analysis | No allocation; current study object; no participatory design |
| C004 | aim; Study design; Discussion; Conclusion | Population reference and routine-service origin |
| C005 | Aim; introduction; Methods; burden calculations; Conclusion | Economic-burden family and purpose; current collection |
| C006 | Abstract; aim; Data; Outcomes; Results; Conclusion | Applied-use family; claims data level; sample conflict |
| C007 | Purpose; Study design; Phase boundary; Discussion; Conclusion | Stakeholder influence without current co-design |
| C008 | randomization; sample plan; consumer input; pilots; analysis plan | Study allocation and participatory development part |
| C009 | objective; CREATE Development; Results | Participatory checklist development; source issue |
| C010 | title; pilot; interview process; modeling | Retraction separation; part and task rules |
| C011 | experiment; task order; variance Results; Discussion | Allocation, factor role, and variance conflict |
| C012 | Objectives; bolt-on development; survey; Conclusion | Participatory development part and data uses |
| C013 | cohorts; sample selection; Results; Discussion | Part boundary, use context, and three source problems |
| C014 | Abstract; Methods; Results; Discussion | Comparison, synthesis design, and two conflicts |
| C015 | aim; measures; Results; Discussion; Conclusion; affiliations | Health-behavior outcome, no EQ use, and source issue |

No article passage was checked for the other 26 studies.
Their current mapping did not have a material disagreement that required a new
source check.

## Manifest verification

The review calculated raw byte counts and SHA-256 values for all 45 article
files.

| Manifest | Files | Byte matches | SHA-256 matches | Result |
|---|---:|---:|---:|---|
| `round-01.tsv` | 15 | 15 | 15 | Match |
| `round-02.tsv` | 15 | 15 | 15 | Match |
| `round-03.tsv` | 15 | 15 | 15 | Match |
| **Total** | **45** | **45** | **45** | **Match** |

No article failed verification.
