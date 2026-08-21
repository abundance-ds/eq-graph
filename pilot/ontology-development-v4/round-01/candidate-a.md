# Candidate A: typed EuroQol research ontology

## Scope and design rule

This proposal models scientific meaning. It does not specify a database design.
It uses three layers:

1. **Stable structure:** studies, components, data, uses, analyses, results, and
   evidence.
2. **Controlled science:** separate assignments for purpose, design, origin,
   status, role, and maturity.
3. **Open information:** source text, source labels, notes, and registered gaps.

A controlled value is never evidence by itself. Each assertion needs a source
pointer. Absence of evidence does not mean `NO`, `ZERO`, or `NOT_APPLICABLE`.

## Proposed records and relationships

| Record | Scientific function | Main relationships |
|---|---|---|
| `Project` | A funded or managed program of work | `HAS_STUDY`; `HAS_AGENT_ROLE`; `HAS_PUBLICATION` |
| `Publication` | One published or unpublished report | `REPORTS_STUDY`; `CITES_PUBLICATION`; `HAS_AGENT_ROLE` |
| `Study` | One research investigation with a coherent objective | `HAS_COMPONENT`; `HAS_ASSIGNMENT`; `USES_DATA`; `HAS_PRODUCT`; `HAS_CLAIM` |
| `StudyComponent` | A separable quantitative, qualitative, synthesis, or model component | `HAS_SAMPLE`; `USES_DATA`; `HAS_USE`; `HAS_ANALYSIS_STEP`; `HAS_OUTCOME` |
| `Population` | The target group about which the study makes inferences | `TARGET_OF` a study or component |
| `Sample` | The observed, elicited, reviewed, or simulated units | `SAMPLED_FROM` population; `GENERATES_DATASET`; can have attrition stages |
| `Dataset` | A coherent body of participant, qualitative, aggregate, or model-input data | `USED_BY` through `DataUse`; `DERIVED_FROM` another dataset |
| `EvidenceSynthesisUnit` | One included report, cohort, contrast, or estimate in a review | `EXTRACTED_FROM` publication; `CONTRIBUTES_TO` analysis or estimate |
| `RegistryEntity` | A canonical instrument, method, protocol, model, language, place, person, or organization | `HAS_ALIAS`; target of a use or agent role |
| `UseAssertion` | A typed use of a registry entity in one study component | `USES_ENTITY`; owner is a study or component; subtypes are instrument, method, protocol, and model use |
| `Administration` | Who completed or received an instrument or elicitation, in what setting and time | `QUALIFIES` an instrument or elicitation use |
| `AnalysisStep` | A transformation from data to an outcome, estimate, or product | `CONSUMES`; `USES_METHOD`; `USES_MODEL`; `PRODUCES` |
| `StudyFactor` | A condition, intervention, comparator, exposure, or subgroup role | Links a canonical concept to a study, sample, outcome, or contrast |
| `Outcome` | The property assessed, valued, predicted, or synthesized | `MEASURED_BY`; `HAS_ESTIMATE`; `ADDRESSES_CONCEPT` |
| `Estimate` | A numeric result with unit, denominator, time, and uncertainty | `ESTIMATES` outcome; `SUPPORTS` finding |
| `Finding` | A result claim supported by current-study evidence | `SUPPORTED_BY` evidence, estimate, or qualitative material |
| `Interpretation` | An author explanation, implication, or recommendation | `BASED_ON` finding; never merged with a finding |
| `Limitation` | An author-stated or reviewer-inferred constraint | `LIMITS` study, component, estimate, or interpretation |
| `Product` | A reusable output, such as a value set, instrument version, rubric, taxonomy, or decision aid | `PRODUCED_BY`; has its own maturity status |
| `Concept` | A canonical scientific topic or construct | `HAS_ALIAS`; target of `ADDRESSES`, `CONCERNS`, or `StudyFactor` |
| `AgentRole` | The role of a person or organization in a project, study, or publication | Roles include author, funder, sponsor, data collector, and developer |
| `Gap` | A missing, uncertain, or unsupported representation | `ABOUT` a record/key; `SUPPORTED_BY` a source pointer |
| `SourceConflict` | Two incompatible source assertions that must both be kept | `ABOUT` a record/key; `HAS_SOURCE_ASSERTION` two or more times |

`StudyComponent` is required when components have different samples, origins,
methods, or status. It is not required only because a paper lists many analyses.
`UseAssertion` is one stable structure with a controlled `registry_kind`; its
valid roles depend on that kind. This gives typed instrument, method, protocol,
and model uses without four duplicate record designs.

## Key dictionary

`1` means exactly one; `0..1` means optional; `1..n` means one or more;
`0..n` means any number.

| Owner.key | Meaning | Card. | Value type | Evidence requirement | Controlled? |
|---|---|---:|---|---|---|
| `Project.project_id` | Stable project identity | 1 | identifier | Manifest or project statement | No |
| `Publication.publication_id` | DOI, PMID, or stable local identity | 1 | identifier | Publication metadata | No |
| `Study.study_id` | Stable investigation identity, not a paper identity | 1 | identifier | Methods/objective evidence | No |
| `StudyComponent.component_id` | Identity of a separable component | 1 | identifier | Component-specific sample, data, or method evidence | No |
| `*.canonical_label` | Preferred display label | 1 | text | Registry curation evidence | No |
| `RegistryEntity.registry_kind` | Entity registry | 1 | enum | Entity definition | Yes |
| `RegistryEntity.source_label` | Exact label used in the source | 1..n | text plus source pointer | Verbatim source occurrence | No |
| `AxisAssignment.axis` | Scientific dimension being assigned | 1 | enum | Source phrase and owner | Yes |
| `AxisAssignment.value` | Canonical value on that dimension | 1 | controlled term | Source phrase and mapping rule | Yes |
| `AxisAssignment.source_label` | Source phrase that led to the mapping | 1 | text | Verbatim or close source phrase | No |
| `AxisAssignment.certainty` | Mapping confidence | 1 | enum | Curator judgment note | Yes: `HIGH`, `MEDIUM`, `LOW` |
| `Population.description` | Population to which inference applies | 1 | text plus concepts | Explicit objective/method statement | Partly |
| `Sample.unit_type` | Participant, dyad, interview, report, estimate, or simulated unit | 1 | enum | Methods evidence | Yes |
| `Sample.size` | Count at one named sample stage | 0..1 | non-negative integer | Count plus stage and pointer | No |
| `Sample.stage` | Screened, enrolled, completed, excluded, analytic, or simulated stage | 1 | enum | Methods or results evidence | Yes |
| `DataUse.provenance_class` | How the current component obtained these data | 1 | enum | Provenance statement | Yes |
| `DataUse.data_level` | Participant, qualitative material, aggregate estimate, or model parameter | 1 | enum | Data description | Yes |
| `UseAssertion.registry_kind` | Instrument, method, protocol, or model | 1 | enum | Entity definition | Yes |
| `UseAssertion.context_role` | Current, source, object, input, planned, or discussion context | 1 | enum | Explicit use and study boundary | Yes |
| `UseAssertion.function_role` | What the entity did in that context | 1..n | controlled term | Method or analysis evidence | Yes, by registry kind |
| `UseAssertion.source_label` | Exact local name of the used entity | 1 | text | Source occurrence | No |
| `Administration.respondent_role` | Self, proxy, interviewer, expert, or other respondent | 0..1 | enum or gap | Administration evidence | Yes |
| `Administration.perspective` | Whose health or values the response represents | 0..1 | canonical concept | Explicit framing | Partly |
| `Administration.mode` | Face-to-face, video, online, paper, or other mode | 0..n | controlled term | Administration evidence | Yes |
| `Administration.language` | Canonical language plus source label | 0..n | registry reference | Explicit report | Registry |
| `Administration.time_reference` | Named measurement or elicitation time | 0..n | text/time offset | Explicit schedule | No |
| `AnalysisStep.sequence` | Order in a derivation | 0..1 | positive integer | Analysis description | No |
| `Outcome.outcome_domain` | Broad type of assessed property | 1 | enum | Objective/analysis evidence | Yes |
| `Estimate.*` | Value, statistic, unit, denominator, time, subgroup, comparator, uncertainty | As reported | typed scalar/text/reference | Result table or text; denominator is mandatory for rates | Partly |
| `Finding.finding_type` | Form of result claim | 1 | enum | Result evidence | Yes |
| `Finding.direction` | Increase, decrease, difference, association, no detected difference, or not applicable | 0..1 | enum | Explicit contrast and estimate | Yes |
| `Limitation.limitation_type` | Source of constraint | 1..n | enum | Author statement or marked reviewer inference | Yes |
| `Product.product_type` | Reusable scientific output type | 1 | enum | Explicit output evidence | Yes |
| `Product.maturity` | State of this product, not state of the study | 1 | enum | Explicit development/use evidence | Yes |
| `AgentRole.role` | Relationship of an agent to its owner | 1 | enum | Author, funding, or contribution statement | Yes |
| `*.evidence_pointer` | File and section, table, figure, or quoted span locator | 1..n per assertion | source reference | Required for each scientific assertion | No |
| `Gap.gap_code` | Reason a safe assertion cannot be made | 1 | enum | Source evidence and curator note | Yes |
| `Gap.target_key` | Field or relation affected by the gap | 1 | key reference | Curator statement | No |
| `SourceConflict.asserted_value` | One value in a source conflict | 2..n | typed value plus source pointer | Each incompatible source assertion | No |

## Initial controlled vocabulary

### Research purpose

Purpose is multi-value. A primary purpose is required when the source supports
one. Secondary purposes keep their own rank.

| Value | Include when | Exclude when |
|---|---|---|
| `VALUE_SET_DEVELOPMENT` | The study estimates preference weights or a scoring algorithm | A value set is only applied to score data |
| `PREFERENCE_METHOD_RESEARCH` | The study tests elicitation, anchoring, or preference-analysis methods | Preference data only support a new value set with no method question |
| `POPULATION_NORMS` | The intended product is reference values for a population | Health levels are only sample descriptors |
| `MEASUREMENT_PROPERTY_EVALUATION` | Reliability, validity, agreement, responsiveness, or feasibility as a measure is assessed | The instrument only measures an outcome |
| `INSTRUMENT_DEVELOPMENT` | Content or form of an instrument is developed or refined | Only translation is done |
| `TRANSLATION_ADAPTATION` | Linguistic or cultural adaptation is the objective | Language is only an administration attribute |
| `METHOD_OR_PROTOCOL_QUALITY` | Quality, fidelity, or performance of a research method or protocol is assessed | General study quality control is only a procedure |
| `IMPLEMENTATION_OR_USE` | Routine use, adoption, acceptability, or workflow is studied | A future use is only recommended |
| `DECISION_SUPPORT_DEVELOPMENT` | A patient or policy decision-support form is designed or tested | A statistical decision model is analyzed |
| `OUTCOME_DESCRIPTION` | Burden, status, trajectory, or predictors are the main objective | Outcomes only test a measurement property |
| `ECONOMIC_EVALUATION` | Costs, QALYs, ICERs, or decisions are modeled | Economic use is only discussed |
| `EVIDENCE_SYNTHESIS` | Evidence from multiple reports is systematically combined | Several source datasets are compared without a review process |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | A taxonomy, definition, or conceptual guidance is the main output | An empirical classification model is fitted |

### Study design axes

These axes must not be combined into one `study_type` field.

| Axis | Initial values and rules |
|---|---|
| `evidence_approach` | `QUANTITATIVE`, `QUALITATIVE`, `MIXED_METHODS`, `EVIDENCE_SYNTHESIS`, `MODEL_BASED`, `CONCEPTUAL`. Use the data and inference form, not the journal label. |
| `observation_structure` | `CROSS_SECTIONAL`, `LONGITUDINAL_REPEATED`, `SOURCE_DATA_REANALYSIS`, `NO_DIRECT_OBSERVATION`. A source study can be cross-sectional while the current study is a reanalysis. |
| `comparison_structure` | `NONCOMPARATIVE`, `BETWEEN_GROUP`, `WITHIN_PERSON`, `WITHIN_DYAD`, `BETWEEN_METHOD`, `BETWEEN_INSTRUMENT`, `MULTI_CONTEXT`. Apply more than one only when contrasts differ. |
| `allocation` | `RANDOMIZED`, `NONRANDOMIZED`, `NOT_APPLICABLE`, `NOT_REPORTED`. This is intervention or exposure assignment, not sampling. Do not infer nonrandomized from silence. |
| `mixed_method_integration` | `CONVERGENT_PARALLEL`, `SEQUENTIAL`, `EMBEDDED`, `NOT_APPLICABLE`, `NOT_REPORTED`. |
| `synthesis_design` | `SYSTEMATIC_REVIEW`, `META_ANALYSIS`, `NARRATIVE_SYNTHESIS`, `NOT_APPLICABLE`. Meta-analysis does not replace systematic review. |

“Valuation,” “psychometric,” “translation,” and “implementation” are purposes
or activities. They are not values on a design axis. “Protocol” and “Current
Opinion” are publication genres. They are not study designs.

### Data origin

Each dataset gets one provenance class. A study can use more than one dataset,
so a forced study-level `MIXED` value is not necessary.

| Value | Include when | Exclude when |
|---|---|---|
| `CURRENT_PRIMARY` | Current investigators collect data for this investigation | Existing clinical, project, or study data are reused |
| `PRIOR_STUDY_PARTICIPANT_DATA` | Participant-level data from a named prior study are reanalyzed | Data came from routine care |
| `ROUTINE_CARE_PARTICIPANT_DATA` | Clinical or service data were collected in routine care | Data were collected only for research |
| `PRIOR_PROJECT_QUALITATIVE_DATA` | Existing interviews, workshops, transcripts, or recordings are reused | Current participants generate the material |
| `REVIEW_EXTRACTED_AGGREGATE` | Estimates or characteristics are extracted from included reports | Raw participant data from many studies are pooled |
| `DOCUMENTARY_SOURCE_DATA` | Facts or classifications are taken from documents or websites without a formal review sample | The work only cites examples during conceptual argument |
| `PUBLISHED_MODEL_INPUT` | Literature parameters or existing model structures are inputs | Review estimates are the outcome of synthesis |
| `SIMULATED_COHORT` | Units are generated for a model | Participants were observed |
| `CONCEPTUAL_MATERIAL` | The work develops concepts without an empirical analytic dataset | A literature synthesis has formal included units |

`data_level` is separate: `PARTICIPANT`, `DYAD`, `QUALITATIVE_MATERIAL`,
`AGGREGATE_ESTIMATE`, `MODEL_PARAMETER`, or `SIMULATED_UNIT`.

### Status and maturity

| Owner/axis | Values | Rule |
|---|---|---|
| Study `execution_state` | `PLANNED`, `RECRUITING`, `DATA_COLLECTION_ACTIVE`, `DATA_COLLECTION_COMPLETE`, `ANALYSIS_ACTIVE`, `COMPLETED`, `NOT_REPORTED` | Report the state at the source date. Do not infer present-day state. |
| Study `result_state` | `NO_RESULTS_YET`, `PARTIAL_RESULTS`, `RESULTS_REPORTED`, `NOT_APPLICABLE`, `NOT_REPORTED` | Keep this separate from data collection. |
| Product `maturity` | `PLANNED`, `PROTOTYPE`, `EXPERIMENTAL`, `PRELIMINARY`, `FINAL`, `VALIDATED`, `DEPLOYED`, `NOT_REPORTED` | This applies only to the named product. |
| Data `availability` | `OPEN`, `ON_REQUEST`, `RESTRICTED`, `NOT_AVAILABLE`, `NOT_REPORTED` | A missing statement is `NOT_REPORTED`, not `NOT_AVAILABLE`. |

### Use context

| Value | Include when | Exclude when |
|---|---|---|
| `DIRECT_CURRENT_ACTIVITY` | The entity performs a current data-collection or analysis task | It only generated source data |
| `CURRENT_STUDY_OBJECT` | The entity itself, its content, use, performance, or output is examined | It only provides a measurement |
| `SOURCE_STUDY_ACTIVITY` | The entity was used to create reused source data | The current paper repeats that activity |
| `INPUT_DATA_PROVENANCE` | Its output enters the current analysis as data | The entity is only mentioned in the introduction |
| `PLANNED_ACTIVITY` | The source states that a future component will use it | Data collection already occurred |
| `DISCUSSION_CONTEXT` | It appears only as background, comparison, or recommendation | It contributes data or a formal study object |

### Function roles by registry kind

| Registry kind | Initial function roles |
|---|---|
| Instrument | `MEASUREMENT_ADMINISTERED`, `COGNITIVE_TEST_OBJECT`, `HEALTH_STATE_DESCRIPTION`, `VALUATION_TARGET`, `SCORING_RULE_APPLIED`, `PREDICTOR_MEASURE`, `MAPPING_TARGET`, `COMPARATOR_MEASURE`, `VISUALIZED_INPUT`, `DEVELOPMENT_TARGET`, `TRANSLATION_SOURCE`, `TRANSLATION_TARGET`, `EVIDENCE_SYNTHESIS_TARGET`, `REFERENCE_ONLY` |
| Method | `SAMPLING`, `DATA_COLLECTION`, `PREFERENCE_ELICITATION`, `QUALITATIVE_ANALYSIS`, `STATISTICAL_ANALYSIS`, `EVIDENCE_SYNTHESIS`, `DATA_TRANSFORMATION`, `QUALITY_ASSURANCE`, `DESIGN_OR_DEVELOPMENT`, `ECONOMIC_EVALUATION`, `MIXED_METHOD_INTEGRATION` |
| Protocol | `DATA_COLLECTION_STANDARD`, `TRANSLATION_STANDARD`, `REPORTING_GUIDANCE`, `QUALITY_CONTROL_STANDARD`, `RISK_OF_BIAS_TOOL`, `IMPLEMENTATION_GUIDANCE` |
| Model | `STATISTICAL_ESTIMATION`, `CHOICE_MODEL`, `MAPPING_MODEL`, `META_ANALYTIC_MODEL`, `DECISION_ANALYTIC_MODEL`, `SCORING_ALGORITHM` |

The function role states what the entity did. It does not replace the canonical
entity name. For example, `cTTO` is a method with
`PREFERENCE_ELICITATION`; “hybrid model” is a model with
`STATISTICAL_ESTIMATION`; and `EQ-VT` is a data-collection protocol or
platform, not an outcome instrument.

### Result and product values

| Axis | Values |
|---|---|
| `outcome_domain` | `PREFERENCE_OR_UTILITY`, `HEALTH_STATUS`, `MEASUREMENT_PROPERTY`, `AGREEMENT`, `CONTENT_VALIDITY`, `FEASIBILITY`, `USABILITY_ACCEPTABILITY`, `DATA_QUALITY`, `IMPLEMENTATION`, `COST_EFFECTIVENESS`, `CONCEPTUAL_CLASSIFICATION` |
| `finding_type` | `DESCRIPTIVE`, `COMPARISON`, `ASSOCIATION`, `MODEL_SELECTION`, `SYNTHESIZED_ESTIMATE`, `QUALITATIVE_THEME`, `DEVELOPMENT_DECISION` |
| `limitation_type` | `SAMPLING`, `GENERALIZABILITY`, `MEASUREMENT`, `DATA_PROVENANCE`, `METHOD`, `MODEL`, `IMPLEMENTATION_CONTEXT`, `REPORTING`, `TEMPORAL` |
| `product_type` | `VALUE_SET`, `SCORING_ALGORITHM`, `POPULATION_NORMS`, `INSTRUMENT_VERSION`, `CHECKLIST_OR_RUBRIC`, `TAXONOMY_OR_FRAMEWORK`, `DECISION_SUPPORT_ARTEFACT`, `IMPLEMENTATION_GUIDANCE`, `POOLED_ESTIMATE_SET`, `STUDY_PROTOCOL` |
| `gap_code` | `UNMAPPED_VALUE`, `UNMODELED_ASPECT`, `UNCERTAIN_MAPPING`, `NOT_REPORTED` |

A study with no reusable product gets a `NOT_REPORTED` gap when the output is
required for an audit. It does not get a product named “None.” A null outcome
or limitation is treated in the same way.

## Application to the 15 papers

The matrix gives canonical values. Text in quotation marks is a retained source
label. Semicolons separate assignments on different axes or separate uses.

### Classification and entity uses

| ID | Purpose | Design | Data origin and status | Instrument use | Method, protocol, and model use | Product |
|---|---|---|---|---|---|---|
| G109 | Primary `VALUE_SET_DEVELOPMENT`; secondary `PREFERENCE_METHOD_RESEARCH` | `QUANTITATIVE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; allocation `NOT_APPLICABLE` | `CURRENT_PRIMARY`, participant; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-5L and EQ VAS: `MEASUREMENT_ADMINISTERED`; hypothetical EQ-5D-5L states: `VALUATION_TARGET`; Moroccan Arabic/French retained on administration | cTTO and DCE: direct `PREFERENCE_ELICITATION`; quota sampling and quality control: direct; EQ-VT v2.6.1: `DATA_COLLECTION_STANDARD`; CREATE: `REPORTING_GUIDANCE`; heteroskedastic censored Tobit, conditional logit, and preferred hybrid heteroskedastic Tobit: models | Moroccan EQ-5D-5L `VALUE_SET` and `SCORING_ALGORITHM`, `FINAL` |
| G101 | Primary `PREFERENCE_METHOD_RESEARCH` | `QUANTITATIVE`; `SOURCE_DATA_REANALYSIS`; `MULTI_CONTEXT`; `BETWEEN_GROUP` | Eleven `PRIOR_STUDY_PARTICIPANT_DATA` datasets; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-5L states: current `VALUATION_TARGET` and input; source EQ-5D/EQ VAS administration: `SOURCE_STUDY_ACTIVITY` only | DCE: current input and source elicitation; cTTO and EQ-VT: source context, not current analysis; coefficient and interaction comparisons: direct statistics; 20-parameter mixed logit primary; heteroscedastic conditional logit sensitivity; 40-term interaction model | `NOT_REPORTED` reusable product |
| G125 | Primary `POPULATION_NORMS`; secondary `OUTCOME_DESCRIPTION` | `QUANTITATIVE`; `SOURCE_DATA_REANALYSIS`; source survey `CROSS_SECTIONAL`; `BETWEEN_GROUP` | `PRIOR_STUDY_PARTICIPANT_DATA` from Italian value-set study; `COMPLETED`; `RESULTS_REPORTED` | Italian EQ-5D-5L and EQ VAS: source administration and current input; Italian value set: current `SCORING_RULE_APPLIED`; cTTO/DCE: source context only | Descriptive statistics, chi-square, t test, and ANOVA: direct; robust OLS: `STATISTICAL_ESTIMATION`; EQ-VT: source protocol; cross-country comparison: direct | Italian `POPULATION_NORMS`, `FINAL` |
| G160 | Primary `METHOD_OR_PROTOCOL_QUALITY` | `QUALITATIVE`; `SOURCE_DATA_REANALYSIS`; `BETWEEN_METHOD` | `PRIOR_PROJECT_QUALITATIVE_DATA`: video recordings and transcripts; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-5L health-state tasks: `CURRENT_STUDY_OBJECT`; DCE section: source context, not analyzed | Conversation analysis and transcript coding: direct `QUALITATIVE_ANALYSIS`; checklist construction and normalized scoring: direct development; cTTO interviews: `CURRENT_STUDY_OBJECT`; quantitative EQ-VT quality control: comparator; model use `NOT_REPORTED` | Interviewer-performance `CHECKLIST_OR_RUBRIC`, `PRELIMINARY` |
| G195 | Primary `MEASUREMENT_PROPERTY_EVALUATION`; secondary `OUTCOME_DESCRIPTION` | `QUANTITATIVE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON`; self-proxy `WITHIN_DYAD` | `CURRENT_PRIMARY`, child-caregiver dyads; `COMPLETED`; `RESULTS_REPORTED` | Amharic EQ-5D-Y-3L self and proxy plus EQ VAS: direct administration at admission/discharge; Zimbabwe value set: `SCORING_RULE_APPLIED` | Weighted kappa, ICC, Spearman, PCHC, paired tests, and percent reduction: direct statistical methods; model use `NOT_REPORTED` | `NOT_REPORTED` reusable product |
| G010 | Primary `DECISION_SUPPORT_DEVELOPMENT`; secondary `IMPLEMENTATION_OR_USE` | `MIXED_METHODS`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; prototype test | Current participant feedback plus historical input of uncertain provenance; `COMPLETED`; `RESULTS_REPORTED` | Historical EQ-5D-5L values: `VISUALIZED_INPUT`, not administered to current participants; demographic form/checklist: direct administration | Directed content analysis, descriptive tests, Wilcoxon, and McNemar: direct; visualization development: direct; model use `NOT_REPORTED` | Enhanced EQ-5D visualization for a TKA decision aid, `PROTOTYPE` |
| G196 | Primary `TRANSLATION_ADAPTATION`; secondary `MEASUREMENT_PROPERTY_EVALUATION` for content validity | `QUALITATIVE`; `CROSS_SECTIONAL`; `NONCOMPARATIVE` | `CURRENT_PRIMARY`, cognitive-interview material; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-Y-5L: `TRANSLATION_TARGET`, `DEVELOPMENT_TARGET`, and `COGNITIVE_TEST_OBJECT`; UK English source and Arabic EQ-5D-Y-3L reference: `TRANSLATION_SOURCE` | Forward/back translation, reconciliation, cognitive debriefing, card ranking, and proofreading: direct; EuroQol VMC process: `TRANSLATION_STANDARD`; model use `NOT_REPORTED` | Modern Standard Arabic EQ-5D-Y-5L paper/digital `INSTRUMENT_VERSION`, `FINAL` for translation, not psychometric validation |
| G116 | Primary `INSTRUMENT_DEVELOPMENT`; secondary `MEASUREMENT_PROPERTY_EVALUATION` for content validity | `QUALITATIVE`; `CROSS_SECTIONAL`; `MULTI_CONTEXT` | `CURRENT_PRIMARY`, expert focus groups; `COMPLETED`; `RESULTS_REPORTED` | EQ-TIPS v2: `CURRENT_STUDY_OBJECT` and `DEVELOPMENT_TARGET`, not a health measurement administration; earlier instruments/survey: discussion or source context | Purposive expert sampling, online focus groups, breakout discussion, and thematic analysis: direct; model use `NOT_REPORTED` | EQ-TIPS refinement recommendations and candidate content, `EXPERIMENTAL`; no final validated version claimed |
| G131 | Primary `IMPLEMENTATION_OR_USE` | `QUALITATIVE`; `SOURCE_DATA_REANALYSIS`; `MULTI_CONTEXT` | `PRIOR_PROJECT_QUALITATIVE_DATA` from interviews/workshops; `COMPLETED`; `RESULTS_REPORTED` | EQ-HWB and four QoL measures: source project activity; QOL-ACC: background policy context after source data collection; none is a current psychometric test | Interviews, workshops, and interpretive thematic analysis with mixed deductive/inductive coding: current or source-project use as qualified; model use `NOT_REPORTED` | Routine-measurement `IMPLEMENTATION_GUIDANCE`, `PRELIMINARY` |
| G014 | Primary `EVIDENCE_SYNTHESIS`; secondary `OUTCOME_DESCRIPTION` | `EVIDENCE_SYNTHESIS`; `SYSTEMATIC_REVIEW`; `META_ANALYSIS`; `NARRATIVE_SYNTHESIS`; `MULTI_CONTEXT` | `REVIEW_EXTRACTED_AGGREGATE`, 187 included studies; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-3L/5L: `EVIDENCE_SYNTHESIS_TARGET`, not current administration | Database search, dual screening/extraction, subgroup and leave-one-out analyses, and Egger test: direct; Newcastle-Ottawa Scale: `RISK_OF_BIAS_TOOL`; PRISMA: `REPORTING_GUIDANCE`; DerSimonian-Laird random-effects: `META_ANALYTIC_MODEL` | COVID-19 EQ-5D `POOLED_ESTIMATE_SET`, `FINAL` |
| G083 | Primary `PREFERENCE_METHOD_RESEARCH`; secondary `ECONOMIC_EVALUATION` | `MODEL_BASED`; `SOURCE_DATA_REANALYSIS`; `BETWEEN_METHOD`; `BETWEEN_INSTRUMENT` | `PRIOR_STUDY_PARTICIPANT_DATA`; `PUBLISHED_MODEL_INPUT`; `SIMULATED_COHORT`; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-5L and SF-12: observed input; EQ-5D-3L: `MAPPING_TARGET`; SF-6D: derived comparator; value sets: `SCORING_RULE_APPLIED` | Five mapping methods, bootstrap, and Markov cohort simulation: direct; three OLS and two multinomial mapping models; two existing Markov `DECISION_ANALYTIC_MODEL` records | `NOT_REPORTED` new reusable product; comparative method evidence is a finding |
| G015 | Primary `MEASUREMENT_PROPERTY_EVALUATION` | `QUANTITATIVE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON`; `BETWEEN_INSTRUMENT` | `ROUTINE_CARE_PARTICIPANT_DATA`; `COMPLETED`; `RESULTS_REPORTED` | Dutch EQ-5D-5L, EQ VAS, and EORTC QLQ-C30 v3: routine administration at pre-operation, 6 months, and 12 months; Dutch value set: scoring | Paired tests, delta/MCID comparison, effect size, standardized response mean, and chemotherapy subgroup analysis: direct; model use `NOT_REPORTED` | `NOT_REPORTED` reusable product |
| G168 | Primary `PREFERENCE_METHOD_RESEARCH`; secondary `MEASUREMENT_PROPERTY_EVALUATION` for DCE feasibility | `MIXED_METHODS`; `CROSS_SECTIONAL`; `CONVERGENT_PARALLEL`; allocation `NOT_APPLICABLE` | `CURRENT_PRIMARY`; at submission `DATA_COLLECTION_COMPLETE` and analysis not started; `NO_RESULTS_YET` | EQ-5D-Y-5L and EQ VAS: completed current administration; EQ-5D-Y-5L states: DCE `VALUATION_TARGET` | Online questionnaire/DCE, focus groups, and field notes: completed data collection; planned descriptive statistics, content analysis, and narrative integration; explicitly no choice model | Published `STUDY_PROTOCOL`, `FINAL`; intended evidence product remains `PLANNED` |
| G154 | Primary `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`; secondary `IMPLEMENTATION_OR_USE` | Main component `CONCEPTUAL` and `NO_DIRECT_OBSERVATION`; supporting documentary inventory; `NOT_APPLICABLE` allocation | `CONCEPTUAL_MATERIAL`; `DOCUMENTARY_SOURCE_DATA` for value-set publication inventory; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D, SF-6D, HUI, 15D, and AQoL families: `DISCUSSION_CONTEXT`; value sets are the conceptual object | Conceptual taxonomy development and desktop review: direct; proposed small studies/reweighting are recommendations, not current methods; model use `NOT_REPORTED` | Value-set obsolescence `TAXONOMY_OR_FRAMEWORK`, `PRELIMINARY` |
| G146 | Primary `VALUE_SET_DEVELOPMENT`; secondary `PREFERENCE_METHOD_RESEARCH` | `QUANTITATIVE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; allocation `NOT_APPLICABLE` | Two `CURRENT_PRIMARY` adult samples; `COMPLETED`; `RESULTS_REPORTED` | EQ-5D-Y-3L states: `VALUATION_TARGET` framed as a 10-year-old child; final algorithm: scoring product | DCE and cTTO: direct elicitation; stratified quota sampling and quality control: direct; EQ-Y valuation protocol and portable EQ-VT: protocols; mixed logit: choice model; linear/power mapping models; hybrid model sensitivity | Indonesian EQ-5D-Y-3L `VALUE_SET` and `SCORING_ALGORITHM`, `FINAL` |

### Outcomes, findings, limitations, and concepts

| ID | Outcome and central finding | Main limitation | Main concepts and explicit gaps |
|---|---|---|---|
| G109 | Utility/preferences: preferred hybrid model; values range from 1 to -1.492; 1,271 of 3,125 states are below zero | Rural and low-literacy groups are underrepresented; EQ-VT is difficult for some respondents | National value set, WTD, cross-language equivalence, HTA |
| G101 | Cross-country preference coefficients: mean 9.3 of 20 coefficients differ pairwise; no universal regional pattern | Scale, confidence-interval, MID, sample, translation, and respondent-heterogeneity limits | Cross-country comparability, preference heterogeneity, local value sets; product `NOT_REPORTED` |
| G125 | Population health norms and subgroup differences for EQ-5D-5L/EQ VAS | Younger/video-call sample, computer access, social desirability, COVID period, and simple OLS | Population norms, representativeness, cross-country norms; household-size count has `UNCERTAIN_MAPPING` because one table value conflicts with the sample |
| G160 | Interview data quality: 20 positive and 14 negative interviewer patterns; preliminary agreement with quantitative quality control | Small recording subset, early batches, video setting, and no nonverbal analysis | Interviewer effects, protocol fidelity, conversation analysis; detailed weighting logic is an `UNMODELED_ASPECT` |
| G195 | Agreement and responsiveness: self-proxy agreement is fair overall and poorer for emotional health; scores improve by discharge | Expected treatment change, no collector reliability test, no cognitive interviews for younger children, exclusions, and external value set | Self/proxy perspective, pediatric HRQoL, responsiveness; duplicate “malaria” rows are a source conflict |
| G010 | Usability and comprehension: patients prefer the enhanced display and identify ways to improve it | Prototype was outside the full aid, on paper, and after decision screening | Shared decision-making, visualization, TKA; exact historical-data provenance is `UNCERTAIN_MAPPING` |
| G196 | Content validity: the translation process produced an accepted Modern Standard Arabic version | Arabic dialect variation and need for local validation | Translation equivalence, cultural adaptation, content validity; future psychometrics are planned, not findings |
| G116 | Content validity: experts accept six core dimensions and recommend testing sleep/emotions and revised examples | Network recruitment, participant heterogeneity, short orientation, breakout limits, no current caregiver sample | Infant/toddler HRQoL, proxy report, age appropriateness; final validity is not reported |
| G131 | Implementation themes: benefits, barriers, validity concerns, and conditions for good routine use | Pre-implementation setting, one provider, group influence, and resident fatigue | Routine QoL measurement, aged care, implementation, proxy response; exact boundary between reused project steps and current reanalysis is `UNCERTAIN_MAPPING` |
| G014 | Pooled health status: utility 0.76 and EQ VAS 70.76 with high heterogeneity; pain/discomfort 51% and anxiety/depression 46% | Variable quality, missing planned subgroup data, final follow-up selection, converted means, and English-only search | COVID-19 HRQoL, utility, heterogeneity, recovery; risk-of-bias category counts sum to 188 for 187 studies, a source conflict |
| G083 | Cost-effectiveness: mapped EQ-5D lowers QALYs by 14.9-33.2% and raises ICERs by 17.5-49.7% versus observed EQ-5D-5L | One dialysis case and jurisdiction, unmatched algorithms, 3L/5L mismatch, and UK values on Singapore data | Mapping, direct measurement, QALY, ICER, Markov model; new product `NOT_REPORTED` |
| G015 | Internal responsiveness: both instruments show small changes; most effect sizes are below 0.5 and change is larger to 6 than 12 months | Internal responsiveness only, no external anchor, limited instruments, and limited subgroup analysis | Responsiveness, MCID, breast cancer, routine PROMs; EQ VAS endpoint wording conflicts with the standard direction |
| G168 | Planned feasibility outcomes: incompletion, speeding, flatlining, dominant-task violation, and qualitative experience; no empirical finding yet | Small snowball sample and no ability to fit a choice model | Youth valuation feasibility, engagement, mixed-method integration; empirical finding is `NOT_REPORTED`, not “no effect” |
| G154 | Conceptual classification: four main obsolescence areas, with population composition and preference change separated; responses range from reanalysis to new data | Threshold for meaningful change and responsible authority remain unresolved | Value-set validity, context validity, obsolescence, transition cost; publication genre “Current Opinion” is an `UNMAPPED_VALUE` outside study design |
| G146 | Preference/model outcome: power mapping without a constant is preferred; range is 1 to -0.086; pain/discomfort has the largest weight | Small and Java-only cTTO sample, sparse severe states, sample mismatch, and non-linear transform violates interval-scale assumptions | Youth value set, anchoring, commensurability, adult perspective; detailed DCE block design is an `UNMODELED_ASPECT` |

## Gap and ambiguity log

Source conflicts are recorded as conflict records. They are not silently changed
to a gap code.

| ID | Code/type | Target | Safe representation |
|---|---|---|---|
| G125 | `UNCERTAIN_MAPPING` plus source conflict | Household-size sample count | Keep both source values and do not aggregate this cell until resolved |
| G160 | `UNMODELED_ASPECT` | Internal weights and normalization of interviewer-pattern score | Keep method text and product link; do not claim full reproducibility |
| G195 | Source conflict | Duplicate diagnosis label “malaria” with different counts | Keep both table rows with one conflict record; do not sum them |
| G010 | `UNCERTAIN_MAPPING` | Identity and provenance of historical EQ-5D input | Keep `VISUALIZED_INPUT`; do not assign a source study |
| G116 | `NOT_REPORTED` | Final psychometric validity of EQ-TIPS | Product stays `EXPERIMENTAL`; do not infer validation |
| G131 | `UNCERTAIN_MAPPING` | Boundary between the article analysis and earlier project steps | Keep component-level evidence and avoid one forced origin for all material |
| G014 | Source conflict | Risk-of-bias totals | Keep reported category counts and total 187 with a conflict flag |
| G083 | `NOT_REPORTED` | New reusable research product | Keep findings and recommendations; create no “None” product |
| G015 | Source conflict | Direction of EQ VAS endpoints | Keep source wording and a conflict record; do not normalize silently |
| G168 | `NOT_REPORTED` | Empirical findings | Store planned outcomes only; do not encode zero findings |
| G154 | `UNMAPPED_VALUE` | Source genre “Current Opinion” | Retain publication genre text; do not add it to study design |
| G146 | `UNMODELED_ASPECT` | DCE block construction, overlap, color coding, and task order | Keep protocol evidence; defer a task-design extension |
| G101, G195 | `NOT_REPORTED` | Reusable product | Do not create a null or “None” category |

## Rejected distinctions

- Reject one mutually exclusive `study_type`. It mixes purpose, temporal
  structure, evidence approach, and activity.
- Reject `primary study` and `secondary study` as complete design labels. Data
  origin belongs to each dataset use.
- Reject `uses EQ-5D` as a sufficient relation. Administration, valuation
  target, scoring, mapping target, visualized input, study object, and discussion
  have different meanings.
- Reject method names as study types. DCE, cTTO, thematic analysis, and mapping
  are methods with roles.
- Reject protocols and software as instruments. EQ-VT is a protocol/platform;
  CREATE and PRISMA are guidance.
- Reject “hybrid” as one general category. It must name the model or integration
  context.
- Reject product maturity as study status. A completed study can produce an
  experimental instrument or a prototype.
- Reject inferred `NO`, `ZERO`, `NONE`, and `NOT_APPLICABLE`. Use a supported
  negative assertion or a gap.
- Reject a single study-level sample size. Enrollment, completion, exclusion,
  analysis, dyad, review, and simulated stages need named denominators.
- Reject automatic merging of adult/youth instrument versions, self/proxy
  forms, languages, value sets, or model specifications.
- Reject author recommendations as empirical findings. Link them through
  `Interpretation`.
- Reject “statistically significant” without contrast, estimate, denominator,
  test, and source pointer.

## Coverage audit against the question set

The structure can support coherent counts by purpose, each design axis, data
origin, study status, product type, and product maturity. It can also support
counts of instruments, methods, protocols, and models by current/source/planned
role. Population, sample-stage, place, language, funder, outcome, finding, and
limitation questions have explicit owners and evidence.

The following question families need strict response conditions:

- Portfolio percentages need an explicit denominator, inclusion rule, and
  multi-value policy.
- Trend questions need complete temporal coverage and stable identities.
- Effect and significance questions need structured estimates, not finding text
  alone.
- Cross-study comparisons need compatible outcome definitions, units, time
  points, populations, and value sets.
- “Best,” “most effective,” and causal questions need comparative evidence. The
  graph must return insufficient evidence when that evidence is absent.

Thus, the questions audit the ontology. They do not define one field per
question.

## Stability and next-round risks

The stable core is the separation of study/component, dataset use, registry
entity use, administration, derivation, outcome/estimate, claim, product, and
evidence. The controlled lists are initial and can grow through reviewed gaps.

Main next-round risks are identity resolution across project and publication
boundaries; incorrect component splits; weak denominators; loss of instrument
version, perspective, or language; over-normalization of method names; and
conversion of planned or source-study activity into current evidence. Reviewers
should also test whether `StudyFactor` is sufficient for complex interventions
and whether review units need a separate contrast level.

## Exact inputs and source verification

The task instruction read was
`pilot/ontology-development-v4/BUILDER_TASK.md`. Research inputs read were
exactly:

- `pilot/ontology-development-v4/PROTOCOL.md`
- `pilot/ontology-development-v4/round-01.tsv`
- `pilot/ontology-development-v3/ONTOLOGY_V1.md`
- `pilot/ontology-development-v3/questions.tsv`
- `pilot/ontology-development-v3/aggregate-validity/SYNTHESIS.md`
- the 15 article files below

On 2026-08-20, each article was read in full. Direct byte counts and SHA-256
hashes matched the manifest:

| ID | Article path | Bytes | SHA-256 |
|---|---|---:|---|
| G109 | `corpus/1411-VS/doi_10.1007_s11136-025-03930-1.md` | 73318 | `06cd47ce7b8c4e8d26327e3407a25539e756606d602863d3d907f73fd8c71dc7` |
| G101 | `corpus/20180230/doi_10.1007_s11136-021-03075-x.md` | 57070 | `b74d1da3c908098efdcdb1f163991e4cc891ea8737c285ddf5b5ea1c3665186b` |
| G125 | `corpus/20190460/doi_10.1007_s40258-022-00772-7.md` | 132749 | `a7845f657f23302e62c6915868cbcf0c8530bab59d535c2ddd02031a21b3d02f` |
| G160 | `corpus/351-RA/doi_10.1007_s41669-024-00486-7.md` | 62604 | `dd0eab4abc6332fc9965a9e57ff912ee12fa04bd7b6f6e9f6836cb54f1a8094f` |
| G195 | `corpus/436-RA/doi_10.1186_s41687-025-00928-8.md` | 95266 | `544b05d801a8cf385f60d4784e189a2bd1bb54e8148c9072199907de1e38775c` |
| G010 | `corpus/445-RA/doi_10.1186_s12891-024-07304-5.md` | 57114 | `866438ce4bdc844c0cc7a3929828e48acfe2aab09c5d6b7461a5fec9219f4997` |
| G196 | `corpus/1492-RA/doi_10.1186_s41687-025-00985-z.md` | 49236 | `975b85316c338820d1694979d7df6a5fde53cfa68dc0bfab4a9609330c958d7f` |
| G116 | `corpus/365-RA/doi_10.1007_s11136-025-04150-3.md` | 101717 | `84b48b2cb480dfcce2baff045168cea58615e2e013c0c9a5d31243c1c6e472be` |
| G131 | `corpus/150-RA/doi_10.1007_s40271-025-00729-7.md` | 70997 | `fb4d743f9a0e75d57decc78b76c41075602e60ef190ae1c99d2df742b6f455ec` |
| G014 | `corpus/1627-RA/doi_10.1186_s12955-025-02421-8.md` | 219415 | `4537712ebff158ad24bb9a223e9000698a6355d4538599d3bb44287adc91f7e5` |
| G083 | `corpus/20170450/doi_10.1007_s10198-018-0987-x.md` | 39487 | `fc488afa7b1a983ed266cae605368061b0e9fb85c5648b5e2a1ee89cec5aa645` |
| G015 | `corpus/285-PHD/doi_10.3390_cancers16111952.md` | 92054 | `988ed7c0fbcde3d5739aa46e55f11b691a9cf0cfc7adaa248e24427f931a764a` |
| G168 | `corpus/1704-RA/doi_10.1136_bmjopen-2024-097598.md` | 48411 | `21f3eb92df6f2e28b4fa4d44f0559ef20deb1192ab09cfe164c764142621f53d` |
| G154 | `corpus/1578-RA/doi_10.1007_s40273-025-01476-1.md` | 43713 | `5458440de4fda7b5d6a24520f6806e84f8655377b767d63a053525ddced5fe11` |
| G146 | `corpus/20180490/doi_10.1007_s40273-022-01210-1.md` | 61466 | `2d9a0b8e02c0f5c456e661027b22c536aed26c1a76529ec00e1001cb8fd003f2` |
