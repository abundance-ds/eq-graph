# Round 2 independent ontology review

## Review result

The two applications assigned the same primary family, or the same family gap,
to all 15 studies. The exact primary-family agreement is 15/15 (100%). Both
applications independently identified the same missing family for S040 and
S091. This review accepts `HEALTH_OUTCOME_RESEARCH`. After this decision, all
15 round-2 studies have one controlled primary family.

The review also accepts a bounded `TaskDesign` record, a bounded `StudyFactor`
record, and the method function `PARTICIPATORY_DESIGN`. It merges the two
stakeholder proposals into one `StakeholderInvolvement` record. It accepts an
issuer relation on a product-state assertion. It does not accept a new
`evidence_basis` field because the ontology already requires item provenance
and an evidence locator.

The ontology is not yet stable enough for the planned approximately 60-paper
batch. First revise the ontology, reapply it to all 30 studies, and run one
more 15-paper confirmation round.

## Decision terms

- `MERGE`: combine equivalent proposals or map a proposed field to an existing
  structure.
- `ACCEPT`: add the proposed structure or controlled value.
- `REJECT`: do not add the proposal, gap, or mapping.
- `KEEP_OPEN`: retain the gap because the permitted evidence does not resolve
  it.

## Agreement metrics

The unit for the following metrics is one paper. For multi-part studies, the
comparison uses the set of controlled values in the paper. A value that one
application omitted counts as a disagreement. This method does not imply
agreement on the identity of each part.

| Controlled item | Exact agreement | Percent | Review note |
|---|---:|---:|---|
| Primary family or family gap | 15/15 | 100.0% | Full agreement |
| First-ranked purpose | 15/15 | 100.0% | Full agreement |
| Complete purpose set | 12/15 | 80.0% | S031, S057, and S089 differ |
| Complete ranked purpose list | 11/15 | 73.3% | S084 also differs in rank |
| Publication form | 15/15 | 100.0% | Full agreement |
| Execution state | 15/15 | 100.0% | All are `COMPLETED` |
| Result state | 15/15 | 100.0% | All are `RESULTS_REPORTED` |
| `StudyPart` count | 10/15 | 66.7% | Five part boundaries differ |
| `component_approach` set | 14/15 | 93.3% | S058 differs |
| `temporal_structure` set | 12/15 | 80.0% | S024, S058, and S091 differ |
| `comparison_structure` set | 8/15 | 53.3% | This is the least stable design axis |
| `allocation_structure` set | 9/15 | 60.0% | Most differences concern `NOT_APPLICABLE` |
| `mixed_method_integration` set | 13/15 | 86.7% | S057 and S089 differ |
| `data_origin` set | 11/15 | 73.3% | Four papers differ |
| `data_level` set | 11/15 | 73.3% | Four papers differ |
| Applicable `synthesis_design` set | 1/3 | 33.3% | S058 and S071 differ |

The applications are narrative documents, not atomic use-record exports.
Thus, this review does not calculate a percentage for every instrument,
method, protocol, model, and use-context record. The material use-record
differences are adjudicated below.

## Primary-family decision

### `HEALTH_OUTCOME_RESEARCH`

Decision: `ACCEPT`.

Definition:

Use `HEALTH_OUTCOME_RESEARCH` when the main contribution is primary empirical
research that describes, compares, explains, or follows health, HRQoL,
symptoms, functioning, utility, or well-being in a patient or
condition-defined population.

Do not use it when the main contribution is:

- population norms or reference values;
- measurement performance;
- instrument development;
- method performance;
- implementation or decision support;
- evidence synthesis; or
- an economic decision based on costs and consequences.

The value is not a synonym for `OUTCOME_DESCRIPTION`.
`OUTCOME_DESCRIPTION` is a purpose and can occur under more than one family.
The value is not a composite of the existing families. It represents one
recurring scientific contribution. Normal aims, results, and conclusions
distinguish it from its neighbours.

S040 is a determinant analysis of cancer utilities. S091 is a group and
trajectory analysis of health outcomes after COVID-19. S099 remains
`POPULATION_REFERENCE_DESCRIPTION` because its national estimates are intended
for reference across pregnancy stages.

## Structural and controlled-value proposals

### `TaskDesign`

Decision: `ACCEPT`.

Create an optional `TaskDesign` record for a reusable elicitation or assessment
task structure.

Link it to the applicable `MethodUse` or `ProtocolUse`.

The initial fields can store:

- exact task label;
- target profile or profiles;
- attributes and levels;
- duration;
- comparator or choice alternatives;
- task count;
- block;
- presentation order;
- randomization unit; and
- indifference or stopping rule.

Keep exact task content and labels source-faithful. Do not replace the
study-level allocation axis with task-level randomization. Do not create one
record for each observed response.

S017, S031, and S084 contain central and extractable task structures. The
structure also applies to several round-1 valuation and method studies.
Protocol-linked text alone does not support reliable task-level comparison.

### `StudyFactor`

Decision on the record: `ACCEPT`.

Decision on the initial controlled roles: `ACCEPT` with the limits below.

Create one factor-use record for an exact factor and its level or levels.

Link it to the applicable study part, outcome, analysis, or finding.

Use these initial analytic roles:

- `STUDIED_CONDITION`;
- `EXPOSURE_OR_DETERMINANT`;
- `COMPARATOR`;
- `STRATIFIER`;
- `EFFECT_MODIFIER`; and
- `TARGET_STAGE`.

`EFFECT_MODIFIER` requires a source-reported interaction or modification
claim. `STRATIFIER` means that results are reported separately without such a
claim. `COMPARATOR` identifies the reference factor level. It does not replace
the study-part comparison axis. Keep intervention roles open until another
batch supplies direct evidence. Keep factor names and levels open and
source-faithful.

S040 supports `EXPOSURE_OR_DETERMINANT` and `COMPARATOR`. S091 supports
`STUDIED_CONDITION` and `COMPARATOR`. S099 supports `TARGET_STAGE` and subgroup
factor uses. In S031, recipient age and gain type belong first in `TaskDesign`.
Do not duplicate those task attributes as study factors without a separate
analytic use.

### `StakeholderInvolvement`

Decision: `MERGE` the application A and application B proposals.

Accept one optional structure that links:

- a person, organization, or stakeholder group;
- the study part or product activity;
- the exact involvement activity;
- the study stage;
- a short source-faithful influence statement; and
- the existing evidence locator.

Do not add a closed involvement-role list in this round. The evidence supports
a recurring structure, but it does not yet support stable role boundaries.
S057 reports joint creation and direct design influence. S058 reports
consultation during domain selection. The structure resolves the form of the
round-1 G168 gap.

### `PARTICIPATORY_DESIGN`

Decision: `ACCEPT` as a `method_function` value.

Use it when intended users or stakeholders jointly create, refine, or select a
product, service, workflow, display, or implementation program.

It is not a synonym for `QUALITATIVE_DATA_COLLECTION`. Create separate
method-use records when the same activity also collects or analyses
qualitative data. It is not a component approach and it is not a stakeholder
role.

S057 directly supports this value. S058 supports stakeholder consultation but
does not, from the checked passage, establish joint creation to the same
degree.

### Product-state issuer and evidence

Decision on `issuer`: `ACCEPT`.

Add an `asserted_by` relation from a product-state assertion to a person or
organization.

Keep the exact source term for the state, such as `endorsed` or `approved`. Do
not infer an assertion date from the publication date. Use `NOT_REPORTED` when
the approval or endorsement date is absent.

Decision on a new `evidence_basis` field: `MERGE` into existing item
provenance.

Every extracted item already has a source file and locator. A second generic
evidence field would duplicate that structure.

For S062, map the exact term `endorsed` to an approval assertion, link the
issuer to `EuroQol Research Foundation`, and keep the endorsement date as
`NOT_REPORTED`.

Do not infer psychometric validation or deployment.

## Material paper-level mapping decisions

| Paper | Decision | Adjudicated mapping |
|---|---|---|
| S002 | `REJECT` application A's duplicate conceptual data use | Use `DOCUMENTARY_SOURCE` / `DOCUMENT` for the protocol and prior-research documents. Do not add `CONCEPTUAL_MATERIAL` for the same input. |
| S017 | `MERGE` | Use one current pilot part. Treat the pre-pilot as source context because its findings are reported elsewhere. Use `NOT_APPLICABLE` allocation. Record the pilot `VALUE_SET`, the developed PUF `PROTOCOL`, and the available Excel/booklet `CHECKLIST_OR_TOOL`. |
| S024 | `ACCEPT` application A's temporal value | P1 is `VARIABLE_SOURCE_TIME`; time between source valuation studies is an analysed input. P2 remains cross-sectional. |
| S031 | `ACCEPT` application A's purpose and comparison | Add `HEALTH_STATE_VALUATION`. Use `WITHIN_PERSON` for the PTO choices and retain `RANDOMIZED` for forced versus unforced arm allocation. Store the arms and task rules in `TaskDesign`. |
| S040 | `REJECT` the unresolved origin gap | Use `PRIOR_RESEARCH_COLLECTION` / `PARTICIPANT_RESPONSE` for the earlier feasibility collection. Use a separate `ROUTINE_SERVICE_COLLECTION` / `DOCUMENT` use for cancer-site abstraction. Assign `HEALTH_OUTCOME_RESEARCH`. |
| S052 | `MERGE` | Use one part because concept elicitation and debriefing occur in the same interviews with the same sample. Use `WITHIN_PERSON` for base and bolt-on assessment. Use `NOT_APPLICABLE` allocation. |
| S057 | `MERGE` | Keep only `DECISION_SUPPORT_DEVELOPMENT`; deployed implementation was not evaluated. Use three qualitative parts, `NONCOMPARATIVE`, and `NOT_APPLICABLE` allocation. Do not assign mixed-method integration to three qualitative parts. Add `PARTICIPATORY_DESIGN`. |
| S058 | `MERGE` | Use three parts: conceptual option comparison, narrative evidence synthesis, and current stakeholder consultation. Use `BETWEEN_METHOD` for the conceptual comparison. The sequence supports `SEQUENTIAL` integration. |
| S062 | `ACCEPT` application B's design axes | The validation part is `NONCOMPARATIVE` with `NOT_APPLICABLE` allocation. Healthy and ill children provide coverage; the paper does not make their difference the main comparison. Preserve the exact endorsement assertion and issuer. |
| S071 | `MERGE` | Use a `SYSTEMATIC_REVIEW` part and a separable `META_ANALYSIS` part for pooled ceiling effects. Create current-object uses for the synthesis targets and source-study uses for their administrations in included studies. |
| S084 | `ACCEPT` application A's comparison and purpose rank | Use `WITHIN_PERSON` and `RANDOMIZED` for the survey part. Rank `PREFERENCE_COMPARISON` before `INSTRUMENT_DEVELOPMENT`. Add `TaskDesign` for profiles, levels, blocks, order, and two randomization units. |
| S089 | `REJECT` `IMPLEMENTATION_EVALUATION` | The implementation of data-quality controls is part of `METHOD_OR_PROTOCOL_QUALITY`; it is not a separate implementation-research purpose. Do not assign mixed-method integration to two quantitative parts. |
| S091 | `ACCEPT` application A's part boundary and origin | Use one `LONGITUDINAL_REPEATED` part. The T2 group comparison is an analysis, not a separate part. Use `CURRENT_STUDY_COLLECTION` because both waves are presented as POPCORN study collection. Assign `HEALTH_OUTCOME_RESEARCH`. |
| S099 | `ACCEPT` application A's comparison; `REJECT` the product mapping | Use `BETWEEN_GROUP` for distinct participants at pregnancy and postpartum stages. Represent stage with `StudyFactor`. The published estimates are findings, not an explicit reusable `POPULATION_REFERENCE_DATA` product. |
| S100 | `MERGE` the use contexts | Create `CURRENT_STUDY_OBJECT` uses for EQ-5D and EQ VAS as synthesis targets. Create separate `SOURCE_STUDY_ACTIVITY` uses for instruments and analysis methods used in the reviewed trials. |

## Gap adjudication

| Gap or proposal | Decision | Result |
|---|---|---|
| S040 and S091 primary family | `ACCEPT` | Add `HEALTH_OUTCOME_RESEARCH`. |
| S017, S031, and S084 task structure | `ACCEPT` | Add bounded `TaskDesign`. |
| S031, S040, S091, and S099 factor roles | `ACCEPT` with scope correction | Add `StudyFactor`; keep S031 task attributes in `TaskDesign` unless separately analysed. |
| S057 and S058 stakeholder contribution | `MERGE` | Add one bounded `StakeholderInvolvement` record; keep role terms open. |
| S057 co-design method function | `ACCEPT` | Add `PARTICIPATORY_DESIGN`. |
| S062 product-state issuer | `ACCEPT` | Add `asserted_by`; keep exact issuer and source term. |
| S062 product-state evidence basis | `MERGE` | Use existing item provenance and evidence locator. |
| S040 data origin uncertainty | `REJECT` as an open gap | Map the participant data to prior research and the chart fact to routine service collection. |
| S058 included-evidence count | `KEEP_OPEN` | Retain `NOT_REPORTED`; do not inspect the linked review. |
| S017 early convenience-test count | `KEEP_OPEN` | Retain `NOT_REPORTED`. |
| S040 completion mode, channel, and language | `KEEP_OPEN` | Retain `NOT_REPORTED`; do not inspect the parent report. |
| S089 exact language and version identities | `KEEP_OPEN` | Retain `NOT_REPORTED`; country does not identify a registry version. |
| S091 exact language and version identities | `KEEP_OPEN` | Retain `NOT_REPORTED`. |
| S100 source-trial EQ-5D version distribution | `KEEP_OPEN` | Retain `NOT_REPORTED`; do not infer versions from broad `EQ-5D`. |

The open missing-information items do not require new ontology keys or values.

## Source conflicts

Each item below is a `SourceConflict`, not an ontology gap. Decision for each
listed conflict: `ACCEPT` the conflict record.

| Paper | Conflict | Required handling |
|---|---|---|
| S040 | Accrual is May to November 2024, but the reported ethics approval date is 17 January 2025. | Preserve both dates. Do not infer retrospective approval or repair a date. |
| S057 | The abstract reports nine service providers; Results reports 11 workshop service providers. | Preserve both values with locators. Use 11 only when the Results count is requested. |
| S062 | Table 3 gives five of 14 children with a chronic condition as 53.7%. | Preserve count and percentage. Exclude the percentage from aggregation. |
| S071 | The flow text gives 215 full texts and 190 exclusions, then says 20 remained before four update studies. | Preserve the flow statements. Use the explicit final included count of 24. |
| S084 | The abstract and numeric level-3 results place energy before relationships; Discussion reverses them. | Use the numerical result for the principal finding and retain the prose conflict. |
| S089 | The abstract reports 68,411 rollout completers; the 15 country counts sum to 68,416. | Preserve both values. Do not create a repaired total. |
| S089 | One section defines a bot score below 0.5; another excludes 0.5 or less. | Preserve both operators. Do not normalize the boundary. |
| S099 | Nine of 6,661 completers is reported as 1.4%. | Preserve count and percentage. Exclude the percentage from aggregation. |
| S099 | The bisexual total is 302, but wave counts are 171 and 13; 13 is also labelled 4.8%. | Preserve the printed cells. Do not infer a missing digit. |

The source-conflict count is nine.

## Revised round-2 family application

The counting unit is a distinct study. The denominator is 15.

| Primary family | Studies | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | None | 0 |
| `MEASUREMENT_PROPERTY_EVALUATION` | S052 | 1 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | S058, S062 | 2 |
| `POPULATION_REFERENCE_DESCRIPTION` | S099 | 1 |
| `METHODS_RESEARCH` | S002, S017, S024, S031, S084, S089 | 6 |
| `APPLIED_USE_RESEARCH` | S057 | 1 |
| `EVIDENCE_SYNTHESIS` | S071, S100 | 2 |
| `HEALTH_ECONOMIC_EVALUATION` | None | 0 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | None | 0 |
| `HEALTH_OUTCOME_RESEARCH` | S040, S091 | 2 |
| **Total** |  | **15** |

This table is one complete partition.

## Revised cumulative 30-study family application

| Round | Study | Primary family after review | Change |
|---|---|---|---|
| 1 | G109 | `VALUE_SET_DEVELOPMENT` | None |
| 1 | G101 | `METHODS_RESEARCH` | None |
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
| 2 | S031 | `METHODS_RESEARCH` | None |
| 2 | S040 | `HEALTH_OUTCOME_RESEARCH` | Resolves `UNMAPPED_VALUE` |
| 2 | S052 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 2 | S057 | `APPLIED_USE_RESEARCH` | None |
| 2 | S058 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 2 | S062 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 2 | S071 | `EVIDENCE_SYNTHESIS` | None |
| 2 | S084 | `METHODS_RESEARCH` | None |
| 2 | S089 | `METHODS_RESEARCH` | None |
| 2 | S091 | `HEALTH_OUTCOME_RESEARCH` | Resolves `UNMAPPED_VALUE` |
| 2 | S099 | `POPULATION_REFERENCE_DESCRIPTION` | None |
| 2 | S100 | `EVIDENCE_SYNTHESIS` | None |

### Cumulative partition

| Primary family | Count |
|---|---:|
| `VALUE_SET_DEVELOPMENT` | 2 |
| `MEASUREMENT_PROPERTY_EVALUATION` | 3 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | 4 |
| `POPULATION_REFERENCE_DESCRIPTION` | 2 |
| `METHODS_RESEARCH` | 9 |
| `APPLIED_USE_RESEARCH` | 3 |
| `EVIDENCE_SYNTHESIS` | 3 |
| `HEALTH_ECONOMIC_EVALUATION` | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | 1 |
| `HEALTH_OUTCOME_RESEARCH` | 2 |
| **Total** | **30** |

## Round-1 regression effects

No round-1 primary family changes.

The new health-outcome family does not absorb G125 because G125 has explicit
population norms.

It does not absorb G015 because G015 evaluates responsiveness.

It does not absorb G014 because G014 synthesizes prior evidence.

`TaskDesign` can add detail to G109, G101, G146, G160, and G168.

For G101, create task records only when the round-1 evidence gives sufficient
source-study task detail.

The new record does not change a method, protocol, purpose, or family.

`StudyFactor` can refine determinant, comparator, subgroup, and stage uses in
round-1 studies.

It must not replace a population, sample, outcome, study part, or open concept.

`StakeholderInvolvement` resolves the structural form of G168's youth
co-researcher gap.

G010 and G131 are candidates only if their sources report direct stakeholder
influence on an output.

`PARTICIPATORY_DESIGN` can apply to a round-1 activity only when the source
reports joint creation or refinement.

The round-1 summaries alone do not authorize that remapping.

The product-state issuer relation can refine G196's approved language-version
assertion.

It must not imply validation or deployment.

G160's interviewer-score construction and weighting gap remains open.

All round-1 source conflicts and other uncertainties remain unchanged.

## Stability and growth decision

Decision: do not increase directly to the approximately 60-paper cumulative
batch.

The primary-family rule is stable after one clear additive value.

The round identified three new record types, one new relation, and one new
method function.

The comparison and allocation axes also had only 53.3% and 60.0% exact
paper-level agreement.

These are structural changes, not registry additions or open concepts.

Required next actions are:

1. Revise the ontology with the accepted decisions.
2. Reapply the revised ontology to all 30 studies.
3. Confirm that the 30 primary-family assignments remain unchanged.
4. Confirm task, factor, stakeholder, and product-state rules on the applicable
   earlier studies.
5. Run one more diverse 15-paper round before batch growth.

Growth can proceed after that round if new issues are principally registry
identities, aliases, or open concepts.

## Exact inputs

The repository `AGENTS.md` instructions were supplied with the task. The review
read these repository files:

- `pilot/ontology-development-v4/ROUND_REVIEW_TASK.md`;
- `pilot/ontology-development-v4/ONTOLOGY.md`;
- `pilot/ontology-development-v4/PROTOCOL.md`;
- `pilot/ontology-development-v4/round-02.tsv`;
- `pilot/ontology-development-v4/round-02/application-a.md`;
- `pilot/ontology-development-v4/round-02/application-b.md`;
- `pilot/ontology-development-v4/round-01/applications.md`; and
- `pilot/ontology-development-v4/round-01/gaps.md`.

The review did not read Neo4j guidance, older ontology versions, old proposals,
graph records, prior extraction records, or other research files.

## Exact article source-check log

The review checked only passages that could change a key, value, mapping, or
regression decision.

| Paper | Checked passages | Decision supported |
|---|---|---|
| S017 | `Sample and administration of survey`; `Survey instrument`; `Using PUF data to estimate a social utility function`; `Discussion and conclusions` | One current part; task structure; value-set, protocol, and tool products |
| S024 | `Aims of the Study`; `Methods`; time-span analysis | `VARIABLE_SOURCE_TIME` for P1 |
| S031 | aim and objectives; `Survey design`; `Data collection`; qualitative results | `HEALTH_STATE_VALUATION`; within-person tasks; randomized arms; task fields |
| S040 | final Introduction paragraph; `Study Design and Population`; `Institutional Review Board Statement` | health-outcome family; prior participant origin; routine chart origin; ethics conflict |
| S052 | `Study design`; `Procedures`; `Analysis` | one part; within-person base and bolt-on assessment |
| S057 | Abstract; `Participants`; workshops; feedback and optimisation; final prototype; Discussion and Conclusion | participatory function; stakeholder influence; no deployed implementation evaluation; count conflict |
| S058 | `Options for identifying domains`; `Domain selection approach`; consultation paragraph | three parts; between-method conceptual comparison; stakeholder structure |
| S062 | adaptation process; content-validation procedures; Results; Table 3 | noncomparative validation; exact endorsement and issuer; percentage conflict |
| S071 | distributional methods; review flow; pooled ceiling results | separate meta-analysis part; flow conflict |
| S084 | objectives; task and block design; randomization; numeric results; Discussion | within-person comparison; `TaskDesign`; level-3 result conflict |
| S089 | objective; pilot and main design; quality-control rules; Table 1; data availability | no implementation purpose; two threshold rules; rollout total conflict; dataset availability |
| S091 | aim; `Study design and population`; data collection; statistical analyses | health-outcome family; one longitudinal part; current-study origin |
| S099 | aim; `Study Design and Data Collection`; Results; Table 1; Discussion | population-reference family boundary; between-group design; stage factor; no explicit product; two conflicts |

No article passage was checked for S002 or S100 because their disagreements did
not require a source check after application and ontology comparison.

## Manifest verification

The review calculated raw byte counts and SHA-256 hashes for all 15 article
files. All values matched `round-02.tsv`.

| Record | Bytes | SHA-256 | Result |
|---|---:|---|---|
| S002 | 56286 | `467cb82e557941064c134149dbaf410ed7cffd108084fcd2507a051db5c532c9` | Match |
| S017 | 80616 | `9a859cd03aa3256bbd52a6fac01749ca85e7d878770f3d212d83ce3ec304a741` | Match |
| S024 | 68428 | `de0405964ea0d43d90d3fa0acc825ce046c65bff84aef08a44942b8040365452` | Match |
| S031 | 163225 | `87a2c313ac7b1cdde3152331e303e0015897a8f79614135163db1d1f16701e70` | Match |
| S040 | 58691 | `c56fde022f3c5b0ab1a9fe9a206c95f38c6f711c734b82bb98778c78058e1ba4` | Match |
| S052 | 64852 | `f8d32a59a6e392759fc0c38accaee1b28f75699d4ff172abdcc62c41f4c4719f` | Match |
| S057 | 69560 | `5e7dd427dd3e9ecb19ee3957b0623b7b932aa6d983274de82d67e97340ed5464` | Match |
| S058 | 92752 | `3fd5eca21b9429c79f5c0947e286ee07919dea027a79fd7f4a03fd45cd902b0b` | Match |
| S062 | 52978 | `9ee7dfff9c287e3c6dd4abab83be9d2f3d32ca4212aa8fae20b4b93c39a717f0` | Match |
| S071 | 84553 | `2db101c7ed9e576690145c64ba93fbb06f684053fb8ed9af2058f27508d0b6fa` | Match |
| S084 | 65568 | `3ae3da8629d8b0716d2e0a96569796b3bf81b1eb5c5c13fe54038d2d46676d99` | Match |
| S089 | 90076 | `228dc3ca0c53db29e5f6de64f2702c80bcdf1e110f3a67319d213c77b3859e02` | Match |
| S091 | 82786 | `5f3bd0b79e50eb3cc64cc38855dc6166f24d0376f5cf183e648cb1d8459485c3` | Match |
| S099 | 50592 | `a3b76abaf1369572ffe8c9a3fd3d132e04aef1abb93c8730546f5020fc85320b` | Match |
| S100 | 50386 | `45d9c8ae457cb963d4fb0be5882c72526e7fbcff050b234d29f5bbe94719f2ac` | Match |
