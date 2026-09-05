# Version 0.3 final review

## Review result

The blind version 0.3 regression gives one family to each of the 45 earlier
studies, but it does not preserve the reviewed partition in
`round-03/review.md`. Exact family agreement is 41/45 (91.1%). The four
differences are S058, S084, C004, and C011.

Source checks support two regression changes:

- `ACCEPT` S058 as `METHODS_RESEARCH` instead of
  `INSTRUMENT_VERSION_DEVELOPMENT`.
- `ACCEPT` C011 as `HEALTH_PREFERENCE_RESEARCH` instead of
  `METHODS_RESEARCH`.

Source checks reject the other two regression changes:

- `REJECT` `HEALTH_PREFERENCE_RESEARCH` for S084. Keep
  `METHODS_RESEARCH`.
- `REJECT` `HEALTH_OUTCOME_RESEARCH` for C004. Keep
  `POPULATION_REFERENCE_DESCRIPTION`.

The two round-4 applications agree on the primary family for 13/15 studies.
This review maps D005 and D013 to `METHODS_RESEARCH`. All 15 new studies then
have one family. The new batch needs no new primary family, record type, key,
design value, or other controlled value.

Version 0.3 must not freeze. The two accepted earlier-paper family changes are
structural under the protocol. The 15 new studies do not add another structural
change, but they cannot remove the regression failure.

## Agreement metrics

The unit is one round-4 study. For a multi-part study, the metric compares the
set of stated controlled values. An omitted value is a disagreement.

| Controlled item | Exact agreement | Percent | Main differences |
|---|---:|---:|---|
| Primary family | 13/15 | 86.7% | D005 and D013 |
| First-ranked purpose | 12/15 | 80.0% | D004, D005, and D013 |
| Complete purpose set | 14/15 | 93.3% | D005 |
| Publication form | 15/15 | 100.0% | Full agreement |
| Execution state | 15/15 | 100.0% | Full agreement |
| Result state | 15/15 | 100.0% | Full agreement |
| `StudyPart` count | 14/15 | 93.3% | D015 |
| `component_approach` set | 12/15 | 80.0% | D005, D009, and D013 |
| `temporal_structure` set | 14/15 | 93.3% | D013 |
| `comparison_structure` set | 9/15 | 60.0% | D001, D002, D003, D005, D009, and D012 |
| `allocation_structure` set | 14/15 | 93.3% | D004 |
| `mixed_method_integration` set | 14/15 | 93.3% | D003 |
| `data_origin` set | 12/15 | 80.0% | D007, D009, and D011 |
| `data_level` set | 14/15 | 93.3% | D002 |
| Outcome-family set | 10/15 | 66.7% | D005, D006, D008, D009, and D010 |
| Applicable `synthesis_design` set | 1/2 | 50.0% | D013 |
| Gap presence | 10/15 | 66.7% | B proposes gaps for D001, D006, D010, D013, and D014; A proposes none. |
| Source-conflict set by paper | 9/15 | 60.0% | D003, D005, D009, D012, D013, and D015 |

The application files are narrative records. Exact agreement for all
individual use records is not reliable. The material use-record differences
are adjudicated below.

## The 45-paper regression result

Both files contain 45 distinct studies with no duplicate family assignment and
no family gap. This cardinality agreement does not mean that the reviewed
partition is preserved.

| Study | Blind regression | Round-3 reviewed mapping | Decision after source check |
|---|---|---|---|
| S058 | `METHODS_RESEARCH` | `INSTRUMENT_VERSION_DEVELOPMENT` | `ACCEPT` regression. The paper's stated aim and conclusion concern the choice of a domain-identification approach. EQ-HWB is the application context. |
| S084 | `HEALTH_PREFERENCE_RESEARCH` | `METHODS_RESEARCH` | `REJECT` regression. The main decision is whether a low-cost pairwise-comparison method can inform bolt-on selection. |
| C004 | `HEALTH_OUTCOME_RESEARCH` | `POPULATION_REFERENCE_DESCRIPTION` | `REJECT` regression. The paper states the absence of adolescent population data and presents population health status for later reference and comparison. |
| C011 | `HEALTH_PREFERENCE_RESEARCH` | `METHODS_RESEARCH` | `ACCEPT` regression. The paper disentangles empirical self/other and adult/child preference effects. Method quality is secondary. |

The blind regression therefore agrees with the source-adjudicated result for
43/45 studies (95.6%). It changes two earlier reviewed families. Its statement
that no earlier primary family changes is not supported by its own family
table when that table is compared with `round-03/review.md`.

## Source-backed primary-family boundaries

### Method choice versus instrument development

Use `METHODS_RESEARCH` when the stated aim and main decision concern how to
identify domains, select content, or choose a procedure, even if the procedure
is applied in an instrument-development project. S058 meets this rule. Use
`INSTRUMENT_VERSION_DEVELOPMENT` when new or revised instrument content is the
main output.

### Empirical preference versus method evaluation

Use `HEALTH_PREFERENCE_RESEARCH` when empirical differences in health
preferences are the main result and the paper does not make a primary decision
about method performance. C011 and D009 meet this rule. Use
`METHODS_RESEARCH` when method reliability, assumptions, performance,
feasibility, quality, or choice is the main decision. S084, D001, D004, D005,
D010, and D013 meet this rule.

### Population reference versus health outcome

A representative sample is not sufficient for
`POPULATION_REFERENCE_DESCRIPTION`. The paper must state norms, population
data, or reference data as a main aim or output. C004 meets this rule. D015
instead explains health and quality-of-life outcomes by riverbank exposure and
maps to `HEALTH_OUTCOME_RESEARCH`.

### Applied use versus health outcome

Use `APPLIED_USE_RESEARCH` when an instrument, practice, workflow, or decision
support is the main object and health events are targets or secondary outcomes.
D006 tests the incremental value of routine PROMs for readmission prediction
and postdischarge care. It is not primary health-outcome research. D014 studies
current HTA practice, use, and evidence needs. Its survey form does not make it
population-reference or methods research.

### Conceptual work

- D005 is not conceptual framework development. It empirically tests an
  experience-scaling method and proposes its use in value assessment.
- D007 gives a taxonomy and process account of health-state-value uncertainty.
  Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`.
- D011 classifies 13 arguments and applies them to child involvement. Its
  `OPINION_ARTICLE` form does not change its conceptual family.
- D012 first develops a Chinese quality-of-life framework and then compares it
  with the EQ-HWB framework. Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`;
  `CONTENT_VALIDITY_EVALUATION` is a secondary purpose.

### Evidence synthesis versus method research

An article title that says “evidence synthesis” does not alone set the family.
D013 reanalyses three selected prior respondent datasets to test kaizen-task
performance and to make task-design recommendations. It does not report a
systematic evidence search or a narrative synthesis. Map it to
`METHODS_RESEARCH` with `QUANTITATIVE_EMPIRICAL` and `MODEL_BASED` parts and
`PRIOR_RESEARCH_COLLECTION` data.

## Round-4 paper adjudication

| Paper | Decision | Adjudicated mapping |
|---|---|---|
| D001 | `MERGE` | Keep `METHODS_RESEARCH`. Add `BETWEEN_GROUP` to `WITHIN_PERSON` because the source tests general-population versus patient-group effects. `REJECT` `METHOD_EVALUATION_OBJECT`; use `CURRENT_STUDY_OBJECT` with the scientific function `PREFERENCE_ELICITATION`. Use a separate direct use when context changes. |
| D002 | `MERGE` | Keep `EVIDENCE_SYNTHESIS`; add `BETWEEN_INSTRUMENT` and `BETWEEN_CONTEXT`. Keep both `DOCUMENT` for 79 papers and `AGGREGATE_ESTIMATE` for the 1,504 source-defined study units. |
| D003 | `MERGE` | Keep two sequential adaptation and validation parts. The current direct instrument is PedsQL, not an EQ instrument. EuroQol funding and a reference to separately published EQ-5D-Y analyses do not create a direct EQ use. Keep the reported Mapi approval assertion. |
| D004 | `ACCEPT` A's allocation | Use `NOT_APPLICABLE`. The pandemic stopped face-to-face collection, and the remaining interviews used video. The study did not assign people or units to modes. `REJECT` `NONRANDOMIZED`. |
| D005 | `ACCEPT` B's family; `MERGE` A's products | Use `METHODS_RESEARCH` and first-ranked `VALUATION_METHOD_EVALUATION`. The main output is the feasibility and proposed use of experience scaling. Keep the three reported experience-scale value sets as `VALUE_SET` products because the source calls them value sets, even though they are not standard Y-3L value sets. Use `BETWEEN_GROUP`, not `BETWEEN_CONTEXT`. Source DCE tasks are `SOURCE_STUDY_ACTIVITY`; the current analysis is direct. |
| D006 | `MERGE` | Keep `APPLIED_USE_RESEARCH`. Use `METHOD_PERFORMANCE_OR_DATA_QUALITY` for prediction performance and `ECONOMIC_OR_BURDEN` for emergency-department use and readmission because its definition includes resource use. `REJECT` a new `HEALTH_SERVICE_USE_OR_CLINICAL_EVENT` value and reject `HEALTH_STATUS_OR_EQ_VAS` and `IMPLEMENTATION` for the readmission event. |
| D007 | `MERGE` | Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. Use both `CONCEPTUAL_MATERIAL` and `DOCUMENTARY_SOURCE`. Exact uncertainty types remain open concepts. |
| D008 | `MERGE` | Keep `MEASUREMENT_PROPERTY_EVALUATION`. Use 20 analyzed interviews; retain the two guide-development interviewees at their separate activity. Keep both `CONTENT_VALIDITY` and `CONCEPTUAL_CLASSIFICATION` outcomes because the source also reports four concept categories. |
| D009 | `MERGE` | Keep `HEALTH_PREFERENCE_RESEARCH`, not methods or health-outcome research. Use `MODEL_BASED`, `WITHIN_PERSON`, and `BETWEEN_GROUP`; patient groups and the general population are groups, not contexts. Keep both `PREFERENCE_OR_UTILITY` and `HEALTH_STATUS_OR_EQ_VAS` outcomes. Do not create a current value-set product; the source states future potential. |
| D010 | `MERGE` | Keep `METHODS_RESEARCH`. Add `METHOD_PERFORMANCE_OR_DATA_QUALITY` to `PREFERENCE_OR_UTILITY`. `REJECT` `METHOD_EVALUATION_OBJECT`; `CURRENT_STUDY_OBJECT` plus `PREFERENCE_ELICITATION` gives the evaluation and scientific roles on separate axes. Task-order randomization stays in `TaskDesign`. |
| D011 | `MERGE` | Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` and both `DOCUMENTARY_SOURCE` and `CONCEPTUAL_MATERIAL`. Retain a `StakeholderInvolvement` record for the advisory group's manuscript feedback. Discussion and recommended future methods are not direct current uses. |
| D012 | `MERGE` | Keep `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. Use `BETWEEN_INSTRUMENT` for the planned content comparison because the comparator is the EQ-HWB measurement framework; do not use place or mode as the comparison. Keep the Chinese framework as `TAXONOMY_OR_FRAMEWORK`. |
| D013 | `ACCEPT` A's family; `MERGE` design | Use `METHODS_RESEARCH`, `QUANTITATIVE_EMPIRICAL`, `MODEL_BASED`, `VARIABLE_SOURCE_TIME`, `BETWEEN_METHOD`, and `BETWEEN_CONTEXT`. `REJECT` primary `EVIDENCE_SYNTHESIS`, component `EVIDENCE_SYNTHESIS`, and `NARRATIVE_SYNTHESIS`. `REJECT` `METHOD_EVALUATION_OBJECT`. Keep the source-dated planned open-source software assertion; do not convert recommendations alone into an `IMPLEMENTATION_GUIDANCE` product. |
| D014 | `ACCEPT` family; `REJECT` method gap | Keep `APPLIED_USE_RESEARCH`. Instruments and elicitation methods are `CURRENT_STUDY_OBJECT` records. For a method, retain `PREFERENCE_ELICITATION` as its scientific function; the context states that the current survey examines rather than performs it. Do not copy the instrument-only `IMPLEMENTATION_OBJECT` value into `method_function`. |
| D015 | `ACCEPT` A's part boundary; `MERGE` registry labels | Use one current-collection part and one prior-comparison-data part. The three comparison samples come from one larger prior study and do not require three parts. Keep direct current uses separate from input-provenance uses. Treat “Life Satisfaction Index” as the abstract source label for the Cantril measure described in Methods, not as a contradiction or an unreviewed second instrument. |

## Proposal decision register

| Proposal or dispute | Decision | Result |
|---|---|---|
| Blind regression preserves the reviewed 45-family partition | `REJECT` | Exact agreement is 41/45. |
| S058 as methods research | `ACCEPT` | Change the earlier reviewed family to `METHODS_RESEARCH`. |
| S084 as health-preference research | `REJECT` | Keep `METHODS_RESEARCH`. |
| C004 as health-outcome research | `REJECT` | Keep `POPULATION_REFERENCE_DESCRIPTION`. |
| C011 as health-preference research | `ACCEPT` | Change the earlier reviewed family to `HEALTH_PREFERENCE_RESEARCH`. |
| D005 as value-set development | `REJECT` | The method decision is primary. |
| D005 as methods research | `ACCEPT` | Use `VALUATION_METHOD_EVALUATION` first. |
| D005 experience-scale outputs as products | `ACCEPT` | Keep three `VALUE_SET` products with the source qualification. |
| D013 as evidence synthesis | `REJECT` | The paper is a method-performance reanalysis. |
| D013 as methods research | `ACCEPT` | Use `METHOD_OR_PROTOCOL_QUALITY` first. |
| New `METHOD_EVALUATION_OBJECT` function for D001, D010, or D013 | `REJECT` | `CURRENT_STUDY_OBJECT` already gives the role; retain the scientific function. |
| Method-level `IMPLEMENTATION_OBJECT` for D014 | `REJECT` | The value is instrument-specific; context plus `PREFERENCE_ELICITATION` is sufficient. |
| New D006 clinical-event outcome value | `REJECT` | Existing `ECONOMIC_OR_BURDEN` covers resource use. |
| D006 as health-outcome research | `REJECT` | PROM-supported prediction and care use are primary. |
| D009 as methods research | `REJECT` | Patient valuations are the main empirical result. |
| D009 as health-outcome research | `REJECT` | Health-status reporting is an outcome axis, not the primary family. |
| D012 as measurement-property primary family | `REJECT` | New framework development is the first aim and main product. |
| D014 survey as methods research | `REJECT` | It describes HTA practice, use, and needs. |
| D003 direct EQ instrument use | `REJECT` | Funding and separately published EQ analyses do not create a direct use. |
| D015 abstract and Methods labels as separate registry identities | `MERGE` | Preserve both labels as source terms for one described Cantril measure. |
| New catch-all family | `REJECT` | The 60-study partition is complete without one. |

## Source conflicts and open items

### New regression source conflicts

The blind regression lists seven conflicts for the earlier 45 studies. Four
were already in the 19 conflicts accepted in `round-03/review.md`: S057,
C006, C013, and C014. Source checks support the other three as new
`SourceConflict` records:

| Paper | Conflict |
|---|---|
| G109 | Methods calls the DCE design 196 health states, but it also reports 28 blocks of seven choice pairs, which gives 196 pairs rather than 196 states. |
| G195 | Abstract says 957 dyads participated; Results says 985 participated and 957 were analyzed after 28 exclusions. |
| G116 | Results reports 44 invited experts, but the three invited group counts are 21, 13, and 9, which sum to 43. |

Decision: `ACCEPT` these three conflicts. The 15 round-3 conflicts that the
regression omits remain active.

### New round-4 source conflicts

Decision for each conflict below: `ACCEPT` a `SourceConflict`. Preserve all
printed statements with their locators. Do not repair the source silently.

| Paper | Conflict |
|---|---|
| D003 | Abstract expands Generic Core Scales as `GSC`; the title and body use `GCS`. |
| D003 | Abstract calls missing data below 5% problematic; Methods flag 5% or more, and Results describe values above 5% as high. |
| D005 | Abstract and Results say other mother-father differences were not significant but print `p-values < .05`. |
| D009 | Abstract calls 172,070 units patients; Methods calls them patient records. The distinct-person denominator is not stated. |
| D012 | The reported sub-theme alignment is 68%, but the printed fraction is 18/57, approximately 31.6%. |
| D013 | Table 1 reports 1,026 of 1,357 as 69%; the fraction is approximately 75.6%. |
| D013 | Table 1 reports 1,026 finishers, 230 additional exclusions, and an analysis sample of 807; 1,026 minus 230 is 796. |

Decision: `REJECT` a D015 `SourceConflict`. The abstract's generic “Life
Satisfaction Index” label and the Methods name “Cantril’s Self-Anchoring
Striving Scale” refer to the same described life-satisfaction measure. Keep
both source labels through the registry alias record.

The 19 conflicts accepted in `round-03/review.md` remain active. The three new
regression conflicts and seven new round-4 conflicts give 29 cumulative
conflicts. Regression omission of an accepted conflict does not remove it.

Decision: `KEEP_OPEN` all 29 conflicting exact values until an authoritative
correction resolves them. Also keep open:

- C010 notice date, identifier, reason, and asserting organization;
- G160 interviewer-score construction and weighting detail;
- S017 early convenience-test count;
- S040 completion mode, channel, and language;
- S058 included-evidence count;
- S089 exact language and version identities;
- S091 exact language and version identities; and
- S100 source-trial EQ-5D version distribution.

No round-4 controlled gap remains after adjudication. Source-specific factors,
concepts, and aliases remain open information and do not make the ontology
unstable.

## Revised 60-study family table

| Round | Study | Final primary family | Review effect |
|---:|---|---|---|
| 1 | G109 | `VALUE_SET_DEVELOPMENT` | None |
| 1 | G101 | `HEALTH_PREFERENCE_RESEARCH` | None |
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
| 2 | S031 | `HEALTH_PREFERENCE_RESEARCH` | None |
| 2 | S040 | `HEALTH_OUTCOME_RESEARCH` | None |
| 2 | S052 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 2 | S057 | `APPLIED_USE_RESEARCH` | None |
| 2 | S058 | `METHODS_RESEARCH` | Replaces round-3 reviewed instrument-version family |
| 2 | S062 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 2 | S071 | `EVIDENCE_SYNTHESIS` | None |
| 2 | S084 | `METHODS_RESEARCH` | Regression change rejected |
| 2 | S089 | `METHODS_RESEARCH` | None |
| 2 | S091 | `HEALTH_OUTCOME_RESEARCH` | None |
| 2 | S099 | `HEALTH_OUTCOME_RESEARCH` | None |
| 2 | S100 | `EVIDENCE_SYNTHESIS` | None |
| 3 | C001 | `VALUE_SET_DEVELOPMENT` | None |
| 3 | C002 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 3 | C003 | `MEASUREMENT_PROPERTY_EVALUATION` | None |
| 3 | C004 | `POPULATION_REFERENCE_DESCRIPTION` | Regression change rejected |
| 3 | C005 | `ECONOMIC_BURDEN_RESEARCH` | None |
| 3 | C006 | `APPLIED_USE_RESEARCH` | None |
| 3 | C007 | `APPLIED_USE_RESEARCH` | None |
| 3 | C008 | `METHODS_RESEARCH` | None |
| 3 | C009 | `METHODS_RESEARCH` | None |
| 3 | C010 | `VALUE_SET_DEVELOPMENT` | None |
| 3 | C011 | `HEALTH_PREFERENCE_RESEARCH` | Replaces round-3 reviewed methods family |
| 3 | C012 | `INSTRUMENT_VERSION_DEVELOPMENT` | None |
| 3 | C013 | `HEALTH_OUTCOME_RESEARCH` | None |
| 3 | C014 | `EVIDENCE_SYNTHESIS` | None |
| 3 | C015 | `HEALTH_OUTCOME_RESEARCH` | None |
| 4 | D001 | `METHODS_RESEARCH` | Applications agree |
| 4 | D002 | `EVIDENCE_SYNTHESIS` | Applications agree |
| 4 | D003 | `INSTRUMENT_VERSION_DEVELOPMENT` | Applications agree |
| 4 | D004 | `METHODS_RESEARCH` | Applications agree |
| 4 | D005 | `METHODS_RESEARCH` | Accept B; reject A's value-set family |
| 4 | D006 | `APPLIED_USE_RESEARCH` | Applications agree |
| 4 | D007 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | Applications agree |
| 4 | D008 | `MEASUREMENT_PROPERTY_EVALUATION` | Applications agree |
| 4 | D009 | `HEALTH_PREFERENCE_RESEARCH` | Applications agree |
| 4 | D010 | `METHODS_RESEARCH` | Applications agree |
| 4 | D011 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | Applications agree |
| 4 | D012 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | Applications agree |
| 4 | D013 | `METHODS_RESEARCH` | Accept A; reject B's synthesis family |
| 4 | D014 | `APPLIED_USE_RESEARCH` | Applications agree |
| 4 | D015 | `HEALTH_OUTCOME_RESEARCH` | Applications agree |

## Complete 60-study partition

The counting unit is one distinct manifest study. The denominator is 60.

| Primary family | Study IDs | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | G109, G146, C001, C010 | 4 |
| `MEASUREMENT_PROPERTY_EVALUATION` | G195, G015, S052, C003, D008 | 5 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | G196, G116, S062, C002, C012, D003 | 6 |
| `POPULATION_REFERENCE_DESCRIPTION` | G125, C004 | 2 |
| `METHODS_RESEARCH` | G160, G168, S002, S017, S024, S058, S084, S089, C008, C009, D001, D004, D005, D010, D013 | 15 |
| `APPLIED_USE_RESEARCH` | G010, G131, S057, C006, C007, D006, D014 | 7 |
| `EVIDENCE_SYNTHESIS` | G014, S071, S100, C014, D002 | 5 |
| `HEALTH_ECONOMIC_EVALUATION` | G083 | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | G154, D007, D011, D012 | 4 |
| `HEALTH_OUTCOME_RESEARCH` | S040, S091, S099, C013, C015, D015 | 6 |
| `HEALTH_PREFERENCE_RESEARCH` | G101, S031, C011, D009 | 4 |
| `ECONOMIC_BURDEN_RESEARCH` | C005 | 1 |
| Family gap | None | 0 |
| **Total** | **All 60 studies, each once** | **60** |

## Stability and freeze decision

Version 0.3 is not stable enough to freeze.

The 15-paper batch confirms the existing controlled structure. It adds no
family, record type, key, design value, outcome value, method function, or
other controlled value. It also confirms that registry identities, source
aliases, open concepts, and source conflicts do not by themselves make the
ontology unstable.

However, the required blind regression does not preserve the reviewed
45-study partition. Source checks accept two earlier family changes, S058 and
C011. An earlier-paper family change is structural. Freeze is therefore
`REJECT`.

Required next actions are:

1. Correct the reviewed mappings for S058 and C011.
2. Keep S084 and C004 at their reviewed families.
3. Reapply the compact ontology to all 60 studies without using this review as
   extraction evidence.
4. Confirm an exact 60/60 family match with the partition above.
5. Consider freeze only if that blind reapplication causes no earlier family
   change and adds no controlled structure.

## Exact inputs

This review read these repository files in full:

- `AGENTS.md`;
- `pilot/ontology-development-v4/ROUND4_REVIEW_TASK.md`;
- `pilot/ontology-development-v4/PROTOCOL.md`;
- `pilot/ontology-development-v4/ONTOLOGY.md`;
- `pilot/ontology-development-v4/VOCABULARY.tsv`;
- `pilot/ontology-development-v4/EXTRACTION_TASK.md`;
- `pilot/ontology-development-v4/round-01.tsv`;
- `pilot/ontology-development-v4/round-02.tsv`;
- `pilot/ontology-development-v4/round-03.tsv`;
- `pilot/ontology-development-v4/round-04.tsv`;
- `pilot/ontology-development-v4/regression-v0.3.md`;
- `pilot/ontology-development-v4/round-03/review.md`;
- `pilot/ontology-development-v4/round-04/application-a.md`; and
- `pilot/ontology-development-v4/round-04/application-b.md`.

The review did not use Neo4j guidance, an old ontology, an old graph record, a
production extraction, or another candidate record as scientific evidence.

## Exact article source-check log

Only passages that could change a controlled mapping, family decision,
structural decision, gap, or source-conflict record were checked.

| Paper | Checked passages | Decision supported |
|---|---|---|
| G109 | valuation techniques and DCE design counts | DCE count conflict |
| G195 | Abstract; sample-size Methods; Results participant flow | Participant-stage conflict |
| G116 | Results sample characteristics | Invited-expert count conflict |
| S058 | Abstract; stated aim; domain-identification options; Discussion; conclusion | Methods versus instrument-version family |
| S084 | study aim; bolt-on development; analysis; Discussion; conclusion | Methods versus preference family |
| C004 | Abstract; population-data rationale; aim; Discussion; conclusion | Population-reference versus outcome family |
| C011 | Abstract; perspective experiment; quality analyses; Discussion; conclusion | Preference versus methods family |
| D001 | Abstract; sample; test-retest methods; factor analysis; Discussion; conclusion | Method-function gap and comparison set |
| D002 | Abstract; selection; data extraction; COSMIN assessment; Discussion | Comparison and data-level sets |
| D003 | Abstract; instruments; translation; cognitive interviews; item analysis; Discussion; funding | No direct EQ use, product approval, and two conflicts |
| D004 | Abstract; protocol; sampling and collection; statistical comparison; Discussion | Allocation and source-study context |
| D005 | Abstract; Introduction; Methods; Results; Discussion; Conclusions | Method versus value-set family, product, and conflict |
| D006 | Abstract; outcome; predictors; model evaluation; Discussion; Conclusions | Applied-use boundary and outcome mapping |
| D007 | Abstract; uncertainty definitions; process figure; Discussion; Conclusions | Conceptual family and data origins |
| D008 | Abstract; participants; analysis; concept results; Discussion; Conclusion | Measurement-property family, sample stages, and outcomes |
| D009 | Abstract; objective; data; sample size; analysis; Discussion; Conclusions | Preference, methods, and outcome boundary; counting-unit conflict |
| D010 | stated aims; task design; analysis; Discussion; Conclusion | Methods family, task allocation, function gap, and outcomes |
| D011 | Abstract; public-involvement method; Tables 1–2; conclusion; Acknowledgements | Conceptual family, data origins, and stakeholder involvement |
| D012 | stated aims; framework analysis; framework comparison; Results; Discussion | Conceptual family, comparison axis, and conflict |
| D013 | Abstract; secondary datasets; Table 1; analyses; Discussion; Conclusions | Methods versus synthesis family, design, gap, product, and conflicts |
| D014 | Abstract; objectives; survey form; method-use results; Discussion; Conclusions | Applied-use survey boundary and method-function gap |
| D015 | Abstract; respondents; measures; analysis; Discussion | Part boundary and registry alias |

No article passage was checked for the other 38 studies. Their mapping had no
material disagreement that required a source check in this review.

## Manifest verification

The review recomputed the raw byte count and SHA-256 digest for every article
in all four manifests.

| Manifest | Files | Bytes | Byte matches | SHA-256 matches | Result |
|---|---:|---:|---:|---:|---|
| `round-01.tsv` | 15 | 1,204,617 | 15 | 15 | Match |
| `round-02.tsv` | 15 | 1,131,349 | 15 | 15 | Match |
| `round-03.tsv` | 15 | 1,174,236 | 15 | 15 | Match |
| `round-04.tsv` | 15 | 1,100,254 | 15 | 15 | Match |
| **Total** | **60** | **4,610,456** | **60** | **60** | **Match** |

No article failed verification.
