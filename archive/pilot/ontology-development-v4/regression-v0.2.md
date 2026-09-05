# Ontology version 0.2 regression

## Assessment

This regression applied `ONTOLOGY.md` version 0.2 independently to all 30
manifest papers.

The result is not stable enough to freeze.

- Twenty-eight papers map to one current primary family.
- Two papers require the same new primary-family gap.
- One co-design paper requires a new `component_approach` gap.
- The part-level design axes, data axes, use contexts, and five new structures
  otherwise work across the batch.
- Three source conflicts require source-faithful records.
- One additional source issue must not become a source-reported fact.

The repeated preference-research gap is material. The current family partition
does not cover empirical studies whose main contribution is a comparison or
explanation of health preferences, when the study does not develop a value set
and does not evaluate a method.

## Primary-family application

The first purpose is the first-ranked controlled purpose. `GAP` means that no
current primary family fits without a forced mapping.

| ID | First purpose | Primary family or gap | Main source basis |
|---|---|---|---|
| G109 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` | Develops the Moroccan EQ-5D-5L value set from current cTTO and DCE data. |
| G101 | `PREFERENCE_COMPARISON` | `GAP: UNMAPPED_VALUE` | Compares health preferences in 11 Asian populations; it neither develops a value set nor evaluates a method. |
| G125 | `POPULATION_NORMS` | `POPULATION_REFERENCE_DESCRIPTION` | Produces Italian EQ-5D-5L population norms from reused valuation-study responses. |
| G160 | `METHOD_OR_PROTOCOL_QUALITY` | `METHODS_RESEARCH` | Assesses interviewer performance and EQ-VT quality-control practice. |
| G195 | `MEASUREMENT_PROPERTY_EVALUATION` | `MEASUREMENT_PROPERTY_EVALUATION` | Tests agreement, convergent validity, and responsiveness of EQ-5D-Y-3L. |
| G010 | `DECISION_SUPPORT_DEVELOPMENT` | `APPLIED_USE_RESEARCH` | Refines EQ-5D-5L visual displays for a clinical decision aid. |
| G196 | `TRANSLATION_AND_CULTURAL_ADAPTATION` | `INSTRUMENT_VERSION_DEVELOPMENT` | Produces a Modern Standard Arabic EQ-5D-Y-5L version. |
| G116 | `CONTENT_VALIDITY_EVALUATION` | `INSTRUMENT_VERSION_DEVELOPMENT` | Uses expert consultation to review EQ-TIPS version 2.0 content. |
| G131 | `IMPLEMENTATION_EVALUATION` | `APPLIED_USE_RESEARCH` | Examines benefits, barriers, validity, and workflow for routine QoL measurement. |
| G014 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` | Systematically reviews and meta-analyzes EQ-5D outcomes in COVID-19. |
| G083 | `ECONOMIC_EVALUATION` | `HEALTH_ECONOMIC_EVALUATION` | Re-runs two Markov models and reports QALY and ICER effects of mapped utilities. |
| G015 | `MEASUREMENT_PROPERTY_EVALUATION` | `MEASUREMENT_PROPERTY_EVALUATION` | Compares internal responsiveness of two PROMs over one year. |
| G168 | `VALUATION_METHOD_EVALUATION` | `METHODS_RESEARCH` | Protocol tests the feasibility of DCE valuation with adolescents. |
| G154 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | Defines and presents a taxonomy of value-set obsolescence. |
| G146 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` | Produces the Indonesian EQ-5D-Y-3L value set from DCE and cTTO data. |
| S002 | `METHOD_OR_PROTOCOL_QUALITY` | `METHODS_RESEARCH` | Describes, critiques, and recommends EuroQol TTO protocols. |
| S017 | `VALUATION_METHOD_EVALUATION` | `METHODS_RESEARCH` | Develops and tests a personal utility function elicitation method. |
| S024 | `MAPPING_OR_CROSSWALK` | `METHODS_RESEARCH` | Tests agreement between crosswalk and direct EQ-VT value sets. |
| S031 | `PREFERENCE_COMPARISON` | `GAP: UNMAPPED_VALUE` | Explains age-related social preferences for health gains; it does not develop a value set or primarily test a method. |
| S040 | `OUTCOME_DESCRIPTION` | `HEALTH_OUTCOME_RESEARCH` | Describes cancer utilities and their association with equity-related factors. |
| S052 | `CONTENT_VALIDITY_EVALUATION` | `MEASUREMENT_PROPERTY_EVALUATION` | Tests content validity of EQ-5D-5L and four bolt-ons in two skin conditions. |
| S057 | `DECISION_SUPPORT_DEVELOPMENT` | `APPLIED_USE_RESEARCH` | Co-designs a program and decision supports for routine paediatric PROM use. |
| S058 | `INSTRUMENT_DEVELOPMENT` | `INSTRUMENT_VERSION_DEVELOPMENT` | Describes domain selection for the new EQ-HWB instrument. |
| S062 | `TRANSLATION_AND_CULTURAL_ADAPTATION` | `INSTRUMENT_VERSION_DEVELOPMENT` | Produces Singapore English EQ-5D-Y-3L and EQ-5D-Y-5L versions. |
| S071 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` | Systematically reviews comparative measurement properties of 3L and 5L. |
| S084 | `VALUATION_METHOD_EVALUATION` | `METHODS_RESEARCH` | Tests pairwise choice as a method to support bolt-on selection. |
| S089 | `METHOD_OR_PROTOCOL_QUALITY` | `METHODS_RESEARCH` | Develops and assesses survey quality controls across 15 countries. |
| S091 | `OUTCOME_DESCRIPTION` | `HEALTH_OUTCOME_RESEARCH` | Compares HRQoL and mental well-being by COVID-19 disease status over time. |
| S099 | `OUTCOME_DESCRIPTION` | `HEALTH_OUTCOME_RESEARCH` | Describes HRQoL by pregnancy and postpartum stage. |
| S100 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` | Systematically reviews statistical methods for EQ-5D data in trials. |

## Complete family partition

The counting unit is the manifest study. The denominator is 30 distinct
studies. Controlled-family counts exclude the two `UNMAPPED_VALUE` records.

| Primary family | Study IDs | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | G109, G146 | 2 |
| `MEASUREMENT_PROPERTY_EVALUATION` | G195, G015, S052 | 3 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | G196, G116, S058, S062 | 4 |
| `POPULATION_REFERENCE_DESCRIPTION` | G125 | 1 |
| `METHODS_RESEARCH` | G160, G168, S002, S017, S024, S084, S089 | 7 |
| `APPLIED_USE_RESEARCH` | G010, G131, S057 | 3 |
| `EVIDENCE_SYNTHESIS` | G014, S071, S100 | 3 |
| `HEALTH_ECONOMIC_EVALUATION` | G083 | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | G154 | 1 |
| `HEALTH_OUTCOME_RESEARCH` | S040, S091, S099 | 3 |
| `UNMAPPED_VALUE` | G101, S031 | 2 |
| **Total** |  | **30** |

## Part-level design and data application

Each row gives the necessary parts. Each tuple gives
`component_approach`; `temporal_structure`; `comparison_structure`;
`allocation_structure`. A slash between comparison values means that the same
part supports both values. Data uses follow each tuple. All codes are current
ontology codes. The only exception is the explicit S057 gap.

| ID | Necessary parts, design axes, and data uses |
|---|---|
| G109 | cTTO and DCE parts: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. Hybrid estimation part: `MODEL_BASED`; `NOT_APPLICABLE`; `BETWEEN_METHOD`; `NOT_APPLICABLE`; the same response inputs. |
| G101 | DCE reanalysis part: `QUANTITATIVE_EMPIRICAL`; `VARIABLE_SOURCE_TIME`; `BETWEEN_CONTEXT`; `NOT_APPLICABLE`; `PRIOR_RESEARCH_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| G125 | Norms reanalysis part: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`/`BETWEEN_CONTEXT`; `NOT_APPLICABLE`; `PRIOR_RESEARCH_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| G160 | Conversation-analysis part and scoring part: `QUALITATIVE_INQUIRY` then `QUANTITATIVE_EMPIRICAL`; `VARIABLE_SOURCE_TIME`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `PRIOR_RESEARCH_COLLECTION` + `QUALITATIVE_MATERIAL`; integration `SEQUENTIAL`. |
| G195 | Agreement and responsiveness part: `QUANTITATIVE_EMPIRICAL`; `LONGITUDINAL_REPEATED`; `WITHIN_DYAD`/`WITHIN_PERSON`/`BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`, plus `ROUTINE_SERVICE_COLLECTION` + `DOCUMENT` for clinical records. |
| G010 | Pre-surgery and one-year display parts, each with rating and comment subparts: `QUANTITATIVE_EMPIRICAL` plus `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `WITHIN_PERSON`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE` and `QUALITATIVE_MATERIAL`; integration `CONVERGENT_PARALLEL`. |
| G196 | Translation workflow: `TRANSLATION_ADAPTATION_WORKFLOW`; `NOT_APPLICABLE`; `BETWEEN_INSTRUMENT`; `NOT_APPLICABLE`; `DOCUMENTARY_SOURCE` + `DOCUMENT`. Card ranking and cognitive debriefing: `QUANTITATIVE_EMPIRICAL` plus `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; current participant responses and qualitative material; integration `SEQUENTIAL`. |
| G116 | Three expert-consultation parts: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `QUALITATIVE_MATERIAL`. |
| G131 | Workshop part and interview part: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `QUALITATIVE_MATERIAL`. |
| G014 | Review part: `EVIDENCE_SYNTHESIS`; `VARIABLE_SOURCE_TIME`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `REVIEW_EXTRACTED_EVIDENCE` + `AGGREGATE_ESTIMATE`; designs `SYSTEMATIC_REVIEW`, `META_ANALYSIS`, and `NARRATIVE_SYNTHESIS`. |
| G083 | Non-diabetes and diabetes model parts: `MODEL_BASED`; `NOT_APPLICABLE`; `BETWEEN_METHOD`/`BETWEEN_GROUP`; `NOT_APPLICABLE`; `PRIOR_RESEARCH_COLLECTION` + `PARTICIPANT_RESPONSE`, `PUBLISHED_MODEL_INPUT` + `MODEL_PARAMETER`, and `SIMULATED_DATA` + `SIMULATED_UNIT`. |
| G015 | Responsiveness part: `QUANTITATIVE_EMPIRICAL`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON`/`BETWEEN_INSTRUMENT`; `NOT_APPLICABLE`; `ROUTINE_SERVICE_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| G168 | Planned quantitative and qualitative parts: `QUANTITATIVE_EMPIRICAL` and `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; current participant responses and qualitative material; integration `CONVERGENT_PARALLEL`. Data collection was complete at the source date, but analysis remained planned. |
| G154 | Taxonomy part: `CONCEPTUAL`; `NOT_APPLICABLE`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; `CONCEPTUAL_MATERIAL` + `DOCUMENT`. The descriptive scan uses `DOCUMENTARY_SOURCE` + `DOCUMENT`. |
| G146 | DCE and cTTO parts: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; current participant responses. Mapping part: `MODEL_BASED`; `NOT_APPLICABLE`; `BETWEEN_METHOD`; `NOT_APPLICABLE`; current aggregate estimates. |
| S002 | Protocol critique: `CONCEPTUAL`; `NOT_APPLICABLE`; `BETWEEN_METHOD`; `NOT_APPLICABLE`; `DOCUMENTARY_SOURCE` + `DOCUMENT`. |
| S017 | Personal utility function pilot: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `WITHIN_PERSON`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| S024 | Crosswalk comparison: `MODEL_BASED`; `VARIABLE_SOURCE_TIME`; `BETWEEN_METHOD`/`BETWEEN_CONTEXT`; `NOT_APPLICABLE`; published value sets as `PUBLISHED_MODEL_INPUT` + `MODEL_PARAMETER`, unpublished value sets as `PRIOR_RESEARCH_COLLECTION` + `MODEL_PARAMETER`, and the MIC data as prior participant responses. |
| S031 | Embedded qualitative and PTO parts: `QUALITATIVE_INQUIRY` plus `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `WITHIN_PERSON`/`BETWEEN_GROUP`; `RANDOMIZED` for forced versus unforced presentation and randomized ages; current qualitative material and participant responses; integration `EMBEDDED`. |
| S040 | Equity analysis: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| S052 | Content-validity interview part: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `QUALITATIVE_MATERIAL`. |
| S057 | Co-design, feedback, and optimization parts: `UNMAPPED_VALUE` for `component_approach`; `LONGITUDINAL_REPEATED`; `NONCOMPARATIVE`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `QUALITATIVE_MATERIAL` and `DOCUMENT` artifacts. |
| S058 | Domain-selection work: `CONCEPTUAL` plus `EVIDENCE_SYNTHESIS`; `VARIABLE_SOURCE_TIME` for reviewed sources; `NONCOMPARATIVE`; `NOT_APPLICABLE`; `REVIEW_EXTRACTED_EVIDENCE` + `DOCUMENT` and `CONCEPTUAL_MATERIAL` + `DOCUMENT`; integration `SEQUENTIAL`. |
| S062 | Adaptation workflow: `TRANSLATION_ADAPTATION_WORKFLOW`; `NOT_APPLICABLE`; `BETWEEN_INSTRUMENT`; `NOT_APPLICABLE`; documentary source documents. Cognitive and content-validity parts: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; current qualitative material and participant responses; integration `SEQUENTIAL`. |
| S071 | Review part: `EVIDENCE_SYNTHESIS`; `VARIABLE_SOURCE_TIME`; `BETWEEN_INSTRUMENT`; `NOT_APPLICABLE`; review-extracted aggregate estimates and documentary sources; designs `SYSTEMATIC_REVIEW`, `META_ANALYSIS`, and `NARRATIVE_SYNTHESIS`. |
| S084 | Descriptor-refinement and pairwise-choice parts: `QUALITATIVE_INQUIRY` then `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `WITHIN_PERSON`/`BETWEEN_GROUP`; `RANDOMIZED` for block and side allocation; current qualitative material and participant responses; integration `SEQUENTIAL`. |
| S089 | UK pilot and 15-country main parts: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_CONTEXT`/`BETWEEN_GROUP`; pilot `RANDOMIZED`, main `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| S091 | Two-wave outcome part: `QUANTITATIVE_EMPIRICAL`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON`/`BETWEEN_GROUP`/`BETWEEN_CONTEXT`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. |
| S099 | Pregnancy and postpartum survey part: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION` + `PARTICIPANT_RESPONSE`. The paper estimates stages across different respondents, so it is not longitudinal. |
| S100 | Review part: `EVIDENCE_SYNTHESIS`; `VARIABLE_SOURCE_TIME`; `BETWEEN_METHOD`; `NOT_APPLICABLE`; documentary sources and review-extracted aggregate estimates; designs `SYSTEMATIC_REVIEW` and `NARRATIVE_SYNTHESIS`. |

## `TaskDesign`

| Applicable paper | Supported task structure |
|---|---|
| G109 | cTTO: 10 real states after practice, randomized order, 10-year horizon, lead-time rule; DCE: seven pairs, 28 blocks, randomized pair order. |
| G101 | Source-study EQ-VT DCE: 196 pairs, 28 blocks, seven pairs per respondent, randomized pair and side order; context is `SOURCE_STUDY_ACTIVITY`. |
| G160 | Source-study cTTO interview task through the fifth non-practice task; the task is the object of conversation analysis. |
| G010 | Two prototype versions for each of pre-surgery and one-year displays, with checklist items for comprehension, usefulness, and visual appeal. |
| G196 | Card-ranking sets with five severity positions between stated endpoints, followed by self-completion and structured debriefing. |
| G168 | Planned 13 DCE tasks for all ages, three duration tasks for ages 15–18, and one dominant pair. |
| G146 | DCE: ten blocks of 15 pairs, randomized pair and side order; cTTO: 23 states in two blocks with a 10-year child perspective and an indifference rule. |
| S002 | Conventional TTO, composite TTO, iteration, horizon, visual aid, warm-up, and stopping-rule structures are current study objects. |
| S017 | Ranked dimensions, swing ratings, level allocation, two tailored validation pairs, five bisection tasks for dead, and two interaction tasks. |
| S031 | Seven PTO tasks and three attitude questions; ages, health-gain type, forced arm, and unforced arm are explicit task features. |
| S052 | Concept elicitation, think-aloud completion, retrospective probes, bolt-on ranking, and comprehensiveness prompts. |
| S057 | Sensitization tasks, case vignettes, independent sketches, group consensus, feedback rounds, and mock visit optimization. |
| S062 | Random-order severity showcards, cognitive debriefing, concept elicitation, self-completion, and structured relevance prompts. |
| S084 | Eight forced pairwise choices per respondent, six blocks, three base state pairs, five bolt-ons, levels 1/3/5, randomized block and side. |
| S089 | Six randomized pilot survey versions, repeated-item checks, and EQ-5D response-heterogeneity vignette variants. |

Non-applicable boundary cases:

- G195, G015, S040, S091, and S099 administer standard instruments. The
  instrument structure belongs in `InstrumentUse` and `Administration`, not in
  a duplicate `TaskDesign`.
- S024 analyzes completed value sets. The source valuation tasks are input
  provenance, but the paper does not report enough task structure for a new
  record.
- G154 discusses possible future valuation studies. These mentions use
  `DISCUSSION_ONLY` and do not create a current task design.

## `StudyFactor`

| Applicable papers | Exact factors and roles |
|---|---|
| G101, S024 | Country or population is a `STRATIFIER`; derivation route in S024 is the studied method condition, with direct EQ-VT as the stated reference. |
| G125 | Age and sex are `STRATIFIER` factors; chronic condition and income are `EXPOSURE_OR_DETERMINANT` factors. |
| G160 | Interviewer and batch are `STRATIFIER` factors; batch is also a source-faithful `TARGET_STAGE`. |
| G195 | Reporter type is the self/proxy comparison factor; admission and discharge are `TARGET_STAGE`; age, residence, and income are reported stratifiers or determinants. |
| G010 | Pre-surgery and one-year post-surgery are `TARGET_STAGE`; prototype version is the assessed presentation factor. |
| G014 | Region, national income, instrument version, study design, age, and assessment time are `STRATIFIER`; reported predictors are `EXPOSURE_OR_DETERMINANT`. |
| G083 | Dialysis type has a stated reference level and uses `COMPARATOR`; diabetes status is `STUDIED_CONDITION`; utility derivation method is the tested factor. |
| G015 | Baseline, six months, and 12 months are `TARGET_STAGE`; chemotherapy is a `STRATIFIER`, not an `EFFECT_MODIFIER`. |
| G168 | Age group is a `STRATIFIER` because duration tasks apply only to older participants. |
| S031 | Recipient age, adult reference age, health-gain type, and forced/unforced arm are studied factors; participant age and parental status are `STRATIFIER`. |
| S040 | Income, education, employment, marital status, ethnicity, age, sex, and cancer site are `EXPOSURE_OR_DETERMINANT`; stated reference categories use `COMPARATOR`. The null age-by-sex test is not an `EFFECT_MODIFIER` claim. |
| S052, S062 | Condition or health status group is `STUDIED_CONDITION` or `STRATIFIER` when separate results are reported. |
| S084 | Bolt-on identity and severity level are studied factors; no-bolt-on and level 1 are stated comparison levels. |
| S089 | Country is a `STRATIFIER`; survey version is the pilot study condition; pilot, soft launch, and full rollout are `TARGET_STAGE`. |
| S091 | Disease status is `STUDIED_CONDITION`; T1 and T2 are `TARGET_STAGE`; country is a `STRATIFIER`. |
| S099 | Pregnancy month and postpartum month are `TARGET_STAGE`; medical condition and severe anxiety/depression are `STRATIFIER`. |
| S100 | EQ-5D data type, variable format, and single versus multiple post-baselines are review `STRATIFIER` factors. |

Non-applicable boundary cases:

- G109 and G146 store health-state attributes and levels in `TaskDesign`. They
  do not duplicate them as study factors.
- S071 stores EQ-5D-3L and EQ-5D-5L as instrument objects and comparators. It
  does not replace these records with a generic factor.
- G154 stores taxonomy classes as concept and product content. They are not
  analytic factors.

## `StakeholderInvolvement`

| Paper | Stakeholder activity and reported influence |
|---|---|
| G010 | Patients assessed prototype displays; their preferences and comments determined the elements planned for the final displays. |
| G196 | Children completed ranking and cognitive interviews; their responses led to wording and instruction changes. The EuroQol Version Management Committee reviewed and approved versions. |
| G116 | Three expert groups reviewed wording, dimensions, use, and development challenges; their recommendations guide future EQ-TIPS revisions. |
| G131 | Residents, family members, and staff joined workshops or interviews; their views defined benefits, barriers, validity concerns, and workflow recommendations. |
| G168 | Two adolescent student investigators joined the research team before, during, and after data collection and contributed to materials, recruitment, field notes, analysis, and interpretation. |
| S031 | The QUOKKA Decision Makers' Panel requested inclusion of adolescents, which changed the sample design. |
| S052 | Patients with AD or CU evaluated relevance, wording, importance, and comprehensiveness of four bolt-ons. The paper reports evidence, but no completed product revision. |
| S057 | Service providers, adolescents, and caregivers took part in workshops, feedback, and optimization; they created the P-PROM ROCK resources and program. |
| S058 | The PPIE group, NICE groups and staff, EuroQol working group, steering group, and advisory group contributed to domain dropping, merging, and selection. |
| S062 | Paediatricians, teachers, children, and the EuroQol Research Foundation influenced draft and final Singapore English versions. |
| S084 | General-public and patient focus groups assessed candidate bolt-on wording; results modified and selected final descriptors. |
| S089 | Pilot respondents gave feedback that changed survey content; independent country experts refined translated and localized versions. |

Non-applicable boundary cases:

- Standard recruitment or questionnaire completion alone does not create
  `StakeholderInvolvement`. This boundary applies to G109, G125, G195, G015,
  S040, S091, and S099.
- Authorship, ethics review, funding, and normal quality-control work do not by
  themselves prove stakeholder influence.

## `PARTICIPATORY_DESIGN`

| Applicable paper | Direct source support |
|---|---|
| G010 | Intended users compared alternative displays, and the team states that preferred elements will be used to finalize the decision aid display. |
| G196 | Intended child users and the version-management stakeholder iteratively refined the translated instrument. |
| G168 | The source explicitly calls the adolescent investigator work a co-creation process across design, implementation, and evaluation. |
| S057 | The source explicitly uses co-design frameworks; stakeholders jointly created, tested, and optimized the implementation program. |
| S058 | Stakeholder groups took part in an iterative and deliberative process that dropped, merged, and selected instrument domains. |
| S062 | Experts, intended child users, the study team, and the instrument developer jointly refined the final versions. |
| S084 | Intended users refined and selected bolt-on descriptors before the preference experiment. |

Non-applicable boundary cases:

- G116 records consultation and recommendations, but the paper does not report
  a jointly completed product revision.
- G131 elicits perspectives before implementation. It does not report joint
  creation or refinement of an implementation program.
- S052 evaluates content validity but does not report that participants changed
  a product in this study.
- S089 uses pilot feedback and expert review, but the paper reports researcher-
  controlled survey revision, not joint design.

## Product-state `asserted_by`

| Paper | Product-state assertion | `asserted_by` |
|---|---|---|
| G196 | Drafts and changes to the Modern Standard Arabic EQ-5D-Y-5L were approved during the translation workflow. No assertion date is reported. | EuroQol Version Management Committee |
| G116 | EQ-TIPS version 2.0 has the exact state term `Experimental Version` and is not a final product. | EuroQol Research Foundation |
| S062 | All modifications in the final Singapore English Y-3L and Y-5L versions were endorsed. No assertion date is reported. | EuroQol Research Foundation |

Non-applicable boundary cases:

- A paper author's statement that a value set or program was developed does not
  identify a separate asserting person or organization. Do not infer
  `asserted_by` for G109, G146, S017, S057, or S058.
- Ethics approval is approval of study conduct. It is not formal approval of a
  product.
- Publication date is not a product-state date.
- S057 reports that EQ-5D-Y-5L was officially launched in September 2024, but
  the sentence does not name the asserting actor. Preserve the state and date
  without `asserted_by`.

## Material use-context decisions

| Paper or group | Required context distinction |
|---|---|
| G101, G125 | DCE or EQ-5D administration occurred in source valuation studies, so those uses are `SOURCE_STUDY_ACTIVITY`, not direct current activity. Current reanalysis methods are `DIRECT_CURRENT_ACTIVITY`. |
| G160 | EQ-VT and the valuation interview are `CURRENT_STUDY_OBJECT`; video recordings are `INPUT_DATA_PROVENANCE`; conversation analysis and scoring are direct current methods. |
| G014, S071, S100 | EQ-5D administrations in included studies are `SOURCE_STUDY_ACTIVITY`; the review methods are direct current activities; raw mentions are not direct uses. |
| G083 | EQ-5D-5L, SF-12, and KDQOL-36 are source-study activities. Mapping and Markov modeling are direct current activities. Published transition and transplant inputs use `INPUT_DATA_PROVENANCE`. |
| G168 | Completed data collection is source-dated current activity. Analyses written in future tense remain `PLANNED_ACTIVITY` because the paper states that analysis had not begun. |
| G154 | TTO, DCE, reweighting, and new surveys proposed as future responses to obsolescence are `DISCUSSION_ONLY`, not direct methods. |
| S024 | Crosswalk and value-set comparisons are direct current methods. The original valuation methods are input provenance unless the paper only discusses them. |
| S057 | Co-design is direct current activity. Phase 3 pilot and evaluation are `PLANNED_ACTIVITY`. |

## Source conflicts and source issue

| ID | Type | Conflicting or problematic source statements | Treatment |
|---|---|---|---|
| G154 | `SourceConflict` | The abstract lists preference change as main area 4. The body and Table 1 place preference change under type 3b and define type 4 as an instrument change. | Preserve both statements. Do not silently normalize the taxonomy numbering. |
| S058 | `SourceConflict` | The abstract says that the project “developed the new measure,” but the domain-selection section says, “Once the instrument is developed and valued,” NICE will consider it. | Keep product development state uncertain at the paper date. Do not infer completion, valuation, approval, or deployment. |
| S089 | `SourceConflict` | The project overview flags a bot when any score is below 0.5. The analysis section excludes a response at 0.5 or less. | Preserve both thresholds. The treatment of an exact score of 0.5 is unresolved. |
| G015 | `SourceIssue`, not `SourceConflict` | The Methods section reverses the EQ VAS anchors and states 0 is best and 100 is worst. No second explicit anchor statement in the article creates an internal conflict. | Preserve the quotation as a source issue. Do not overwrite the canonical instrument definition. |

## New gaps

### Gap 1: empirical preference research primary family

- State: `UNMAPPED_VALUE`.
- Affected key: `primary_research_family`.
- Papers: G101 and S031.
- Evidence: G101 compares the relative importance of EQ-5D dimensions and
  levels across 11 Asian populations. S031 explains how recipient age and
  health-gain type shape social allocation preferences.
- Why it matters: Both are direct empirical preference studies. Neither paper
  develops a value set. Neither paper primarily evaluates method performance,
  feasibility, quality, or choice. Mapping either paper to `METHODS_RESEARCH`
  would broaden that family beyond its operational definition.
- Proposed resolution: Review a narrow family for empirical health-preference
  research that does not produce a value set. A candidate review label is
  `HEALTH_PREFERENCE_RESEARCH`. Do not accept this label in extraction.

### Gap 2: co-design as the main component approach

- State: `UNMAPPED_VALUE`.
- Affected key: `component_approach`.
- Paper: S057.
- Evidence: The study uses co-design and Double Diamond frameworks. Participants
  create artifacts, reach consensus, test a prototype in mock visits, and make
  final refinements. The paper does not report a qualitative analytic method
  for the main co-design output.
- Why it matters: `QUALITATIVE_INQUIRY` would misstate a generative design
  process as an inquiry. `CONCEPTUAL` would omit the empirical and
  participatory work. `PARTICIPATORY_DESIGN` exists only as a method function,
  so the required part-level approach remains unmapped.
- Proposed resolution: Review a distinct component approach for participatory
  or co-design studies. Do not add it during extraction.

No other new controlled-value or schema gap is required for this batch.
`NOT_REPORTED` remains sufficient when a paper omits an applicable detail.

## Stability verdict

Version 0.2 is materially improved but not stable.

The `HEALTH_OUTCOME_RESEARCH` family cleanly maps S040, S091, and S099 and keeps
them separate from population norms and measurement-property studies. The new
task, factor, stakeholder, participatory-design, and product assertion
structures also prevent several forced free-text mappings.

However, the primary-family partition fails for two repeated empirical
preference studies, and the component approach fails for one explicit co-design
study. These are structural gaps, not isolated missing reports. The ontology
needs review before the 45-paper confirmation point can support a freeze.

## Exact inputs and verification

Only these instruction and ontology files were read:

- `AGENTS.md`
- `pilot/ontology-development-v4/REGRESSION_TASK.md`
- `pilot/ontology-development-v4/PROTOCOL.md`
- `pilot/ontology-development-v4/ONTOLOGY.md`
- `pilot/ontology-development-v4/EXTRACTION_TASK.md`
- `pilot/ontology-development-v4/round-01.tsv`
- `pilot/ontology-development-v4/round-02.tsv`

The following table lists every article input. `OK` means that both the actual
byte count and actual SHA-256 equal the manifest values.

| ID | Article path | Bytes | SHA-256 | Result |
|---|---|---:|---|---|
| G109 | `corpus/1411-VS/doi_10.1007_s11136-025-03930-1.md` | 73318 | `06cd47ce7b8c4e8d26327e3407a25539e756606d602863d3d907f73fd8c71dc7` | OK |
| G101 | `corpus/20180230/doi_10.1007_s11136-021-03075-x.md` | 57070 | `b74d1da3c908098efdcdb1f163991e4cc891ea8737c285ddf5b5ea1c3665186b` | OK |
| G125 | `corpus/20190460/doi_10.1007_s40258-022-00772-7.md` | 132749 | `a7845f657f23302e62c6915868cbcf0c8530bab59d535c2ddd02031a21b3d02f` | OK |
| G160 | `corpus/351-RA/doi_10.1007_s41669-024-00486-7.md` | 62604 | `dd0eab4abc6332fc9965a9e57ff912ee12fa04bd7b6f6e9f6836cb54f1a8094f` | OK |
| G195 | `corpus/436-RA/doi_10.1186_s41687-025-00928-8.md` | 95266 | `544b05d801a8cf385f60d4784e189a2bd1bb54e8148c9072199907de1e38775c` | OK |
| G010 | `corpus/445-RA/doi_10.1186_s12891-024-07304-5.md` | 57114 | `866438ce4bdc844c0cc7a3929828e48acfe2aab09c5d6b7461a5fec9219f4997` | OK |
| G196 | `corpus/1492-RA/doi_10.1186_s41687-025-00985-z.md` | 49236 | `975b85316c338820d1694979d7df6a5fde53cfa68dc0bfab4a9609330c958d7f` | OK |
| G116 | `corpus/365-RA/doi_10.1007_s11136-025-04150-3.md` | 101717 | `84b48b2cb480dfcce2baff045168cea58615e2e013c0c9a5d31243c1c6e472be` | OK |
| G131 | `corpus/150-RA/doi_10.1007_s40271-025-00729-7.md` | 70997 | `fb4d743f9a0e75d57decc78b76c41075602e60ef190ae1c99d2df742b6f455ec` | OK |
| G014 | `corpus/1627-RA/doi_10.1186_s12955-025-02421-8.md` | 219415 | `4537712ebff158ad24bb9a223e9000698a6355d4538599d3bb44287adc91f7e5` | OK |
| G083 | `corpus/20170450/doi_10.1007_s10198-018-0987-x.md` | 39487 | `fc488afa7b1a983ed266cae605368061b0e9fb85c5648b5e2a1ee89cec5aa645` | OK |
| G015 | `corpus/285-PHD/doi_10.3390_cancers16111952.md` | 92054 | `988ed7c0fbcde3d5739aa46e55f11b691a9cf0cfc7adaa248e24427f931a764a` | OK |
| G168 | `corpus/1704-RA/doi_10.1136_bmjopen-2024-097598.md` | 48411 | `21f3eb92df6f2e28b4fa4d44f0559ef20deb1192ab09cfe164c764142621f53d` | OK |
| G154 | `corpus/1578-RA/doi_10.1007_s40273-025-01476-1.md` | 43713 | `5458440de4fda7b5d6a24520f6806e84f8655377b767d63a053525ddced5fe11` | OK |
| G146 | `corpus/20180490/doi_10.1007_s40273-022-01210-1.md` | 61466 | `2d9a0b8e02c0f5c456e661027b22c536aed26c1a76529ec00e1001cb8fd003f2` | OK |
| S002 | `corpus/2015410/doi_10.1007_s40273-016-0404-1.md` | 56286 | `467cb82e557941064c134149dbaf410ed7cffd108084fcd2507a051db5c532c9` | OK |
| S017 | `corpus/2014170/doi_10.1007_s10198-018-0993-z.md` | 80616 | `9a859cd03aa3256bbd52a6fac01749ca85e7d878770f3d212d83ce3ec304a741` | OK |
| S024 | `corpus/1767-RA/doi_10.1007_s40258-025-00954-z.md` | 68428 | `de0405964ea0d43d90d3fa0acc825ce046c65bff84aef08a44942b8040365452` | OK |
| S031 | `corpus/348-PHD/doi_10.1371_journal.pone.0319227.md` | 163225 | `87a2c313ac7b1cdde3152331e303e0015897a8f79614135163db1d1f16701e70` | OK |
| S040 | `corpus/1456-PD/doi_10.3390_curroncol32110645.md` | 58691 | `c56fde022f3c5b0ab1a9fe9a206c95f38c6f711c734b82bb98778c78058e1ba4` | OK |
| S052 | `corpus/1475-RA/doi_10.1007_s11136-024-03875-x.md` | 64852 | `f8d32a59a6e392759fc0c38accaee1b28f75699d4ff172abdcc62c41f4c4719f` | OK |
| S057 | `corpus/330-PHD/doi_10.1007_s11136-025-03996-x.md` | 69560 | `5e7dd427dd3e9ecb19ee3957b0623b7b932aa6d983274de82d67e97340ed5464` | OK |
| S058 | `corpus/2016710/doi_10.1007_s10198-021-01306-z.md` | 92752 | `3fd5eca21b9429c79f5c0947e286ee07919dea027a79fd7f4a03fd45cd902b0b` | OK |
| S062 | `corpus/364-RA/doi_10.1186_s12955-024-02290-7.md` | 52978 | `9ee7dfff9c287e3c6dd4abab83be9d2f3d32ca4212aa8fae20b4b93c39a717f0` | OK |
| S071 | `corpus/2016170/doi_10.1007_s40273-018-0642-5.md` | 84553 | `2db101c7ed9e576690145c64ba93fbb06f684053fb8ed9af2058f27508d0b6fa` | OK |
| S084 | `corpus/20170210/doi_10.1177_0272989x20969686.md` | 65568 | `3ae3da8629d8b0716d2e0a96569796b3bf81b1eb5c5c13fe54038d2d46676d99` | OK |
| S089 | `corpus/367-RA/doi_10.1007_s11136-025-04074-y.md` | 90076 | `228dc3ca0c53db29e5f6de64f2702c80bcdf1e110f3a67319d213c77b3859e02` | OK |
| S091 | `corpus/460-RA/doi_10.3389_fepid.2023.1144162.md` | 82786 | `5f3bd0b79e50eb3cc64cc38855dc6166f24d0376f5cf183e648cb1d8459485c3` | OK |
| S099 | `corpus/2021-RA/doi_10.1007_s40258-023-00798-5.md` | 50592 | `a3b76abaf1369572ffe8c9a3fd3d132e04aef1abb93c8730546f5020fc85320b` | OK |
| S100 | `corpus/345-PHD/doi_10.1016_j.jval.2025.02.001.md` | 50386 | `45d9c8ae457cb963d4fb0be5882c72526e7fbcff050b234d29f5bbe94719f2ac` | OK |

Verification result: 30 of 30 byte counts matched, and 30 of 30 SHA-256
values matched. No excluded research file was read. No other file was edited.
