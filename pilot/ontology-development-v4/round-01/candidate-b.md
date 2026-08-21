# Candidate B: typed EuroQol research ontology

## Design position

The ontology must not use one `study_type` field. That field would mix purpose, design, time, data origin, and analysis. The ontology must keep these axes separate.

The smallest stable unit is a claim about a study component, with a source anchor. A publication can report more than one study. A study can contain components with different samples, methods, and data sources. A named instrument, method, protocol, or model is not the same item as its use in a study.

Use these rules:

- Give each study exactly one `primary_research_family`. Use it for a complete and mutually exclusive count.
- Let a study have zero or more secondary purposes and design frameworks. A multi-value axis is not a partition.
- Record study status, publication form, and product state separately.
- Record each instrument, method, and model use with its role and context.
- Record a result with its denominator, unit, time, and uncertainty when the source gives them.
- Retain the exact source label for each registry match.
- Do not convert an absent statement to `no`, `zero`, or `none`.

## 1. Records and relations

| Record | Scope | Main relations |
|---|---|---|
| `Publication` | One published or submitted work. | `REPORTS` a `Study`; `CITES` a `Publication`; has authors and affiliations. |
| `Study` | One coherent research activity with one primary decision problem. | `HAS_COMPONENT`; `HAS_PURPOSE`; `PRODUCES`; `REPORTS_FINDING`; `HAS_LIMITATION`. |
| `StudyComponent` | A quantitative, qualitative, review, translation, or model part that can have its own sample and methods. | `TARGETS` a `Population`; `ANALYSES` a `Sample` or `EvidenceUnit`; `USES_DATA`; has use records. |
| `Population` | The population to which sampling or inference refers. | `SAMPLED_AS` a `Sample`; located in a `Place`. |
| `Sample` | A recruited, enrolled, completed, or analyzed group. | `DRAWN_FROM` a `Population`; `PART_OF` a component. |
| `DataAsset` | A cohort, survey data set, interview set, transcript set, routine data source, or model input set. | `COLLECTED_BY`, `REUSED_BY`, `DERIVED_FROM`. |
| `EvidenceUnit` | One included study or estimate in a review. | `INCLUDED_IN` a review component; refers to a source publication and extracted outcomes. |
| `InstrumentUse` | One instrument in one role and context. | `REFERENCES` an `Instrument`; `OCCURS_IN` a component; can use a language, protocol, time, respondent, and value set. |
| `MethodUse` | One scientific method in one role and context. | `REFERENCES` a `Method`; `OCCURS_IN` a component; can be governed by a protocol. |
| `ModelUse` | One statistical or decision model in one analysis role. | `REFERENCES` a `Model`; `CONSUMES` data or outcomes; `ESTIMATES` a result; can produce a product. |
| `Product` | A value set, instrument version, reference set, evidence synthesis, tool, framework, or guidance output. | `PRODUCED_BY`; `DERIVED_FROM`; `HAS_STATE`. |
| `Outcome` | A defined quantity, property, theme, or criterion that the study assesses. | `MEASURED_BY`; `HAS_RESULT`; `ABOUT` an instrument, method, product, or population. |
| `Result` | One numeric, categorical, or qualitative result for an outcome. | `SUPPORTS` a finding; has denominator, unit, time, comparison, and uncertainty. |
| `Finding` | An author claim that the evidence supports. | `ABOUT` one or more records; `SUPPORTED_BY` a result or evidence anchor. |
| `Limitation` | A stated or direct source limitation and its affected scope. | `CONSTRAINS` a study, component, result, finding, or product. |
| `Concept` | An open topic term, such as response bias or shared decision-making. | `ANNOTATES` any scientific record. It is not a study class. |
| `SourceConflict` | Two source statements that cannot both be correct as written. | `CONFLICTS_WITH`; links each statement to its evidence anchor. |
| `Gap` | A controlled mapping or coverage problem. | `AFFECTS` a field or record; has one required gap state. |
| `EvidenceAnchor` | A source file and exact section, table, figure, or text span. | `SUPPORTS` every extracted assertion. |

Named resources use separate registries: `Instrument`, `Method`, `Protocol`, `Model`, `Language`, `Place`, `Person`, and `Organization`.

The main relation path is:

`Publication REPORTS Study HAS_COMPONENT StudyComponent`, then the component links to population, sample, data, and typed use records. Model and derivation relations link inputs to outcomes and products. Results support findings. Limitations constrain the exact record that they affect.

## 2. Important key dictionary

`1` means exactly one. `*` means many. A controlled field accepts only a listed value or a gap state.

| Owner | Key | Meaning | Cardinality | Value type | Required evidence | Controlled |
|---|---|---|---|---|---|---|
| Publication | `publication_id` | DOI, PMID, or stable local ID. | 1 | identifier | Metadata | No |
| Publication | `title_source` | Title as published. | 1 | text | Metadata | No |
| Publication | `publication_form` | Form of the report, not the design. | 1 | term | Title, abstract, or methods | Yes |
| Publication | `publication_date` | Source publication date. | 0..1 | date | Metadata | No |
| Study | `primary_research_family` | Main scientific decision problem and product. | 1 | term | Aim plus main product | Yes |
| Study | `secondary_purpose` | Other explicit aims. | 0..* | term | Aim or research question | Yes |
| Study | `study_status` | State of the research at the stated source date. | 1 | term | Methods, results, or protocol status statement | Yes |
| StudyComponent | `design_framework` | Evidence-generation framework. | 1..* | term | Methods | Yes |
| StudyComponent | `temporal_structure` | Time relation among observations. | 1 | term | Methods and time points | Yes |
| StudyComponent | `data_origin` | Relation between this component and its input evidence. | 1 | term | Methods and data source | Yes |
| Population | `population_description` | Open description of the intended population. | 1 | text | Eligibility or sampling frame | No |
| Population | `age_range` | Reported age bounds or summary. | 0..1 | interval or text | Eligibility or table | No |
| Sample | `sample_stage` | Recruited, enrolled, completed, or analyzed. | 1 | term | Flow or methods | Yes |
| Sample | `n` | Count at the stated stage. | 0..1 | integer | Flow, text, or table | No |
| Sample | `sampling_strategy` | Exact sampling method. | 0..* | registry reference | Methods | No |
| DataAsset | `origin_role` | New collection, reused source data, published evidence, or model input. | 1 | term | Methods | Yes |
| DataAsset | `collection_period` | Dates for source data collection. | 0..1 | interval | Methods | No |
| InstrumentUse | `instrument_id` | Canonical instrument identity. | 1 | registry reference | Exact source label and context | No |
| InstrumentUse | `instrument_role` | What the component did with the instrument. | 1 | term | Methods, results, or explicit future plan | Yes |
| InstrumentUse | `use_context` | Current, source-study, planned, or discussion context. | 1 | term | Sentence context | Yes |
| InstrumentUse | `respondent_role` | Self, proxy, general public, patient, caregiver, or other stated role. | 0..1 | term or text | Methods | Yes |
| InstrumentUse | `valuation_perspective` | Whose health and viewpoint the valuation task used. | 0..1 | text | Task framing | No |
| InstrumentUse | `administration_mode` | Face-to-face, online, paper, interview, or other mode. | 0..* | term | Methods | Yes |
| InstrumentUse | `language_id` | Canonical language with source label. | 0..* | registry reference | Methods or instrument description | No |
| InstrumentUse | `measurement_time` | Baseline, discharge, follow-up, or exact time. | 0..* | text or duration | Methods | No |
| InstrumentUse | `scoring_value_set` | Named value set used to score responses. | 0..1 | product reference | Scoring methods | No |
| MethodUse | `method_id` | Canonical scientific method. | 1 | registry reference | Exact method statement | No |
| MethodUse | `method_role` | Collection, elicitation, analysis, quality control, synthesis, or derivation role. | 1 | term | Methods | Yes |
| MethodUse | `protocol_id` | Named protocol that governed this use. | 0..* | registry reference | Explicit protocol statement | No |
| ModelUse | `model_id` | Canonical statistical or decision model. | 1 | registry reference | Analysis methods | No |
| ModelUse | `model_role` | Candidate, comparator, preferred, final, sensitivity, or subgroup role. | 1 | term | Analysis or selection statement | Yes |
| ModelUse | `analysis_context` | Current, source-study, planned, or background context. | 1 | term | Sentence context | Yes |
| Product | `product_type` | Broad output class. | 1 | term | Aim, results, or conclusion | Yes |
| Product | `product_state` | Planned, draft, approved, final, validated, or in use. | 1 | term | Source status statement | Yes |
| Product | `product_label` | Exact output name. | 1 | text | Source | No |
| Product | `intended_scope` | Intended instrument, population, place, or use. | 0..* | record reference or text | Source claim | No |
| Outcome | `outcome_type` | Scientific outcome class. | 1 | term | Methods | Yes |
| Outcome | `outcome_label` | Exact source name. | 1 | text | Source | No |
| Result | `value` | Numeric, categorical, or qualitative value. | 1 | typed value | Results | No |
| Result | `denominator` | Population or evidence base for the result. | 0..1 | sample or evidence-unit reference | Results | No |
| Result | `unit` | Percent, utility unit, score, coefficient, theme, or other unit. | 0..1 | term or text | Results | No |
| Result | `time_or_contrast` | Time point, group, reference, or comparison. | 0..* | record reference or text | Results | No |
| Result | `uncertainty` | Confidence interval, standard error, or other reported uncertainty. | 0..* | typed value | Results | No |
| Finding | `claim_text` | Short faithful summary of the author claim. | 1 | text | Results or conclusion | No |
| Finding | `support_kind` | Numeric, qualitative, mixed, conceptual, or author interpretation. | 1 | term | Linked evidence | Yes |
| Limitation | `limitation_type` | Main source of constraint. | 1 | term | Stated limitation or direct source conflict | Yes |
| Limitation | `scope` | Record or claim that the limitation affects. | 1..* | record reference | Source context | No |
| Registry entry | `canonical_label` | Stable display label. | 1 | text | Registry rule | No |
| Registry entry | `source_label` | Exact label from the article. | 1..* | text | Source span | No |
| Registry entry | `external_id` | DOI, ORCID, ROR, language code, or place ID. | 0..* | identifier | Metadata or verified registry | No |
| Gap | `gap_state` | Reason that a controlled or required mapping is not present. | 1 | term | Source and curator note | Yes |
| EvidenceAnchor | `source_locator` | File plus section, table, figure, or line span. | 1 | locator | Source file | No |

## 3. Initial controlled vocabulary

### Primary research family

This is the only study-level partition. Assign one value from the aim and principal output.

| Value | Include | Exclude |
|---|---|---|
| `value_set_development` | The main output is a new or revised value set or scoring algorithm. | Studies that only compare valuation data or methods. |
| `measurement_property_evaluation` | The main output concerns reliability, validity, agreement, or responsiveness of a measure. | Instrument wording or translation work. |
| `instrument_development_or_adaptation` | The main output is instrument content, wording, translation, cultural adaptation, or refinement evidence. | Psychometric evaluation of a stable version. |
| `population_health_or_norms` | The main output is population reference data, prevalence, or norms. | Clinical measurement-property studies. |
| `methods_research` | The main output assesses a research method, task, model, interviewer process, or feasibility. | A value set where the method is only a means to the product. |
| `clinical_or_implementation_research` | The main output concerns clinical use, decision support, routine measurement, workflow, or implementation. | Instrument-development work outside a use setting. |
| `evidence_synthesis` | The main output systematically combines prior studies. | Informal narrative background. |
| `health_economic_evaluation` | The main output is cost, QALY, ICER, or decision-model evidence. | Studies that only develop utilities for later use. |
| `conceptual_or_policy_research` | The main output is a taxonomy, definition, policy framework, or normative argument. | Empirical method comparisons. |

For the 15 papers, this partition gives: value-set development 2; measurement-property evaluation 2; instrument development or adaptation 2; population health or norms 1; methods research 3; clinical or implementation research 2; evidence synthesis 1; health economic evaluation 1; conceptual or policy research 1. Total: 15.

### Other independent axes

| Axis | Initial values | Rule |
|---|---|---|
| `secondary_purpose` | `produce_value_set`, `compare_preferences`, `establish_norms`, `assess_method_or_process`, `evaluate_measurement_property`, `develop_or_adapt_instrument`, `assess_use_or_implementation`, `synthesize_evidence`, `evaluate_economic_impact`, `develop_framework` | Multi-value. Use only for explicit aims. |
| `design_framework` | `quantitative_empirical`, `qualitative_inquiry`, `mixed_methods`, `evidence_review`, `decision_analytic_modeling`, `translation_adaptation_workflow`, `conceptual_synthesis` | Multi-value. Do not use it as a partition. |
| `temporal_structure` | `cross_sectional`, `longitudinal`, `mixed_or_variable_source_time`, `not_applicable` | Exactly one per component. Longitudinal is not a research family. |
| `data_origin` | `new_participant_data`, `reused_participant_data`, `published_evidence`, `modeled_or_simulated_inputs`, `author_synthesis`, `mixed_origin` | Exactly one primary value per component. Link each input `DataAsset` for mixed origins. |
| `study_status` | `planned_not_started`, `data_collection_active`, `data_collected_analysis_incomplete`, `completed`, `unclear` | Exactly one at the source date. Do not infer current status from the publication date. |
| `publication_form` | `original_research_report`, `protocol`, `systematic_review_and_meta_analysis`, `conceptual_or_current_opinion` | Exactly one per publication. |
| `product_state` | `planned`, `draft`, `approved`, `final`, `validated`, `in_use`, `unclear` | Keep separate from study status. |
| `sample_stage` | `approached`, `recruited`, `enrolled`, `completed`, `analyzed`, `included_evidence` | One `Sample` record per reported stage. |
| `use_context` | `current_study`, `source_study_reused`, `planned`, `background_or_discussion` | Required for instrument and model uses. |
| `model_role` | `candidate`, `comparator`, `preferred`, `final`, `sensitivity`, `subgroup` | One role per `ModelUse`; one model can have more than one use record. |
| `product_type` | `value_set_or_scoring_algorithm`, `reference_data`, `instrument_or_translation`, `research_tool_or_material`, `empirical_evidence`, `evidence_synthesis`, `taxonomy_or_framework`, `guidance` | Use exact `product_label` for the specific output. |
| `outcome_type` | `utility_or_index`, `visual_analogue_score`, `dimension_prevalence`, `preference_structure`, `measurement_property`, `feasibility`, `usability_or_comprehension`, `qualitative_theme`, `cost_qaly_or_icer`, `pooled_estimate`, `method_performance`, `instrument_content` | Each outcome can have many results. |
| `limitation_type` | `sampling_or_representation`, `setting_or_generalizability`, `measurement`, `analysis_or_model`, `missing_or_confounding`, `implementation`, `data_quality`, `reporting_or_source_conflict` | Keep the source text and affected scope. |

### Instrument roles

Create a separate `InstrumentUse` for each role and context.

| Role | Include | Exclude |
|---|---|---|
| `administered_current_health` | Participants report their own or a proxy person's current health in this study. | A screenshot, example, or historic score. |
| `administered_source_study_reused` | The current analysis reuses responses collected in a source study. | New collection for the current component. |
| `planned_administration` | The protocol specifies future administration. | Completed collection. |
| `valued_hypothetical_states` | Respondents value profiles with DCE, cTTO, or another task. | Reporting personal health. |
| `planned_valuation` | The protocol specifies future preference tasks. | Completed valuation. |
| `scored_responses` | A named value set or scoring rule converts responses. | Valuing hypothetical profiles. |
| `mapping_source` | Instrument variables predict another instrument's utility. | The predicted target. |
| `mapping_target` | The utility scale is predicted by mapping. | The source predictors. |
| `comparator` | The study compares the instrument with another measure. | Background mention. |
| `translated_or_culturally_adapted` | The study changes language or culturally adapts wording. | Routine use of a translated version. |
| `content_tested` | Participants or experts assess wording, content, or severity order. | Psychometric performance tests. |
| `development_or_refinement_object` | The study develops or refines the instrument. | Use of an established instrument as an outcome measure. |
| `historical_scores_visualized` | A tool displays historic instrument scores. | Current health assessment. |
| `evidence_synthesized` | A review extracts evidence about instrument results. | Direct administration by the review team. |
| `implementation_object` | The study assesses routine or clinical use of the instrument. | General discussion of possible use. |
| `background_or_discussion_only` | The instrument occurs only in background, example, or discussion text. | Any direct scientific use. |

### Method and model roles

`MethodUse.method_role` accepts `sampling`, `data_collection`, `preference_elicitation`, `quality_control`, `qualitative_analysis`, `statistical_description_or_inference`, `measurement_property_analysis`, `evidence_identification`, `evidence_synthesis`, `mapping_or_derivation`, `economic_evaluation`, and `mixed_method_integration`.

A model is a fitted statistical or decision structure. A method is a procedure. Thus, `hybrid model`, `mixed logit`, `Tobit`, and `Markov model` are models. DCE, cTTO, cognitive debriefing, thematic analysis, and meta-analysis procedures are methods.

### Gap states

| State | Use |
|---|---|
| `UNMAPPED_VALUE` | The source gives a value for a controlled field, but the reviewed vocabulary has no valid value. Retain the source label. |
| `UNMODELED_ASPECT` | The source reports an important aspect, but the ontology has no suitable key, record, or relation. |
| `UNCERTAIN_MAPPING` | Two or more mappings remain plausible, or the source conflicts with itself. Do not choose one silently. |
| `NOT_REPORTED` | The source does not report a required item after full-text review. This does not mean `no` or `zero`. |

Each gap needs an evidence anchor, an affected field, a short reason, and a proposed review action. A builder must not create a new controlled value during paper application.

## 4. Canonical registries

Every registry entry stores `canonical_label`, all exact `source_label` values, aliases, version, and external IDs when available. A use record, not the registry entry, stores the scientific role.

| Registry | Identity rule | Initial examples: canonical label <- retained source label |
|---|---|---|
| Instrument | Keep family, youth or adult form, level count, component, and version separate. | `EQ-5D-5L` <- “EQ-5D-5L”; `EQ-5D-Y-3L` <- “EQ-5D-Y-3L”; `EQ-5D-Y-5L` <- “EQ-5D-Y-5L”; `EQ VAS` <- “EQ-Visual Analogue Scale”; `EQ-TIPS-3L version 2.0` <- “EQ-TIPS-3L v2.0”; `EQ-HWB` <- “EQ-HWB”; `EORTC QLQ-C30 version 3.0` <- “EORTC QLQ-C30 version 3.0”; `SF-12`, `SF-6D`, and `KDQOL-36`. |
| Method | One entry per scientific procedure. Do not use software as a method. | `discrete choice experiment` <- “DCE”; `composite time trade-off` <- “cTTO”; `cognitive debriefing`; `conversation analysis`; `thematic analysis`; `qualitative content analysis`; `Paretian Classification of Health Change`; `random-effects meta-analysis`; `utility mapping`; `cost-utility analysis`. |
| Protocol | Identify issuer, title, instrument scope, and version. | `EQ-VT version 2.6.1` <- “EQ-VT 2.6.1”; `International Valuation Protocol for the EQ-5D-Y-3L`; `EuroQol VMC translation guidelines`; `PRISMA`; `SRQR`. |
| Model | Keep model family, link, error structure, and key transformation separate when they affect interpretation. | `mixed logit`; `heteroskedastic conditional logit`; `heteroskedastic censored Tobit`; `hybrid value-set model`; `power mapping without constant`; `DerSimonian-Laird random-effects model`; `ordinary least squares regression`; `Markov cohort model`. |
| Language | Use a standard language code. Store register and local form as qualifiers. | `ar` Arabic, Modern Standard Arabic register <- “Modern Standard Arabic”; `am` Amharic <- “Amharic”; `it` Italian; `fr` French; `en` English; `nl` Dutch; `id` Indonesian. |
| Place | Prefer a verified geographic ID and type. Keep historical or study wording. | Morocco <- “Morocco”; Italy <- “Italy”; Ethiopia <- “Ethiopia”; Indonesia <- “Indonesia”; Hamilton, Ontario <- “Hamilton”; Greater Toronto Area <- “Greater Toronto Areas”. |
| Person | Prefer ORCID. Otherwise, use the full published name plus affiliation context. Do not merge initials alone. | Brittany Humphries, ORCID 0000-0001-9364-5788; Feng Xie, ORCID 0000-0003-3454-6266; Titi Sahidah Fitriana, ORCID 0000-0001-5062-6886. |
| Organization | Prefer ROR. Otherwise, use verified legal name plus place. Strip converter noise only after verification. | EuroQol Research Foundation <- “EuroQol Research Foundation”; McMaster University <- “McMaster University”; Erasmus MC University Medical Center <- “Erasmus MC University Medical Center”; YARSI University <- “YARSI University”. |

## 5. Application to all 15 papers

### Classification, data, and status

| ID | Purpose | Primary family | Design and time | Data origin and status | Population and sample |
|---|---|---|---|---|---|
| G109 | Produce a Moroccan EQ-5D-5L value set. | `value_set_development` | Quantitative empirical; cross-sectional. | New participant data; completed. | Moroccan adults. 1,590 approached, 1,048 interviewed, 976 analyzed after incomplete and poor-quality exclusions. |
| G101 | Compare EQ-5D-5L DCE preference patterns across 11 Asian populations. | `methods_research` | Quantitative comparative analysis; source studies cross-sectional. | Reused participant DCE data; completed. | General-population samples from China, Indonesia, Japan, South Korea, Malaysia, Singapore, Thailand, the Philippines, Vietnam, Hong Kong, and Taiwan; at least 1,000 per source study. |
| G125 | Produce Italian EQ-5D-5L population norms and compare them with other countries. | `population_health_or_norms` | Quantitative empirical; cross-sectional. | Reused participant data from an Italian valuation survey; completed. | 1,182 non-institutionalized Italian adults. |
| G160 | Identify interviewer conversational patterns that affect valuation interview quality. | `methods_research` | Qualitative inquiry with a scoring step; cross-sectional source interviews. | Reused recordings and transcripts; completed. | 152 recorded Italian valuation interviews; 24 transcripts developed the scheme; 42 interviews from seven interviewers were scored. |
| G195 | Assess self-proxy agreement, validity, and responsiveness of EQ-5D-Y-3L. | `measurement_property_evaluation` | Quantitative empirical; longitudinal admission to discharge. | New participant data; completed. | Ethiopian pediatric inpatients aged 4-18 and proxies; 985 dyads enrolled and 957 analyzed. |
| G010 | Test patient comprehension and preference for EQ-5D-5L decision-aid visualizations. | `clinical_or_implementation_research` | Mixed quantitative and qualitative usability study; cross-sectional. | Mixed origin: new feedback and historic routine PROM data; completed. | Adults with knee osteoarthritis in Alberta; Part 1 n=24 and Part 2 n=25. |
| G196 | Translate and culturally adapt EQ-5D-Y-5L for Egypt. | `instrument_development_or_adaptation` | Translation and adaptation workflow; cross-sectional testing. | New participant data; completed. | Eleven Egyptian children aged 8-15, six healthy and five with chronic conditions. |
| G116 | Assess expert views on EQ-TIPS-3L version 2.0 content, use, and challenges. | `instrument_development_or_adaptation` | Qualitative inquiry; cross-sectional. | New participant data; completed. | 33 experts from 15 countries: 17 EuroQol experts, 11 pediatric experts, and five instrument developers. |
| G131 | Assess benefits, barriers, validity, and implementation of routine quality-of-life measurement in residential aged care. | `clinical_or_implementation_research` | Qualitative inquiry; cross-sectional. | New participant data from a broader project; completed. | Three Melbourne facilities; two workshops and interviews with 29 proxies and 24 residents. |
| G014 | Synthesize EQ-5D HRQoL evidence after COVID-19. | `evidence_synthesis` | Systematic review and meta-analysis; variable source time. | Published evidence; completed. | 187 included studies with 116,525 adult participants. |
| G083 | Test how mapped rather than observed utilities affect dialysis cost-utility results. | `health_economic_evaluation` | Quantitative secondary analysis plus decision-analytic modeling; cross-sectional utility source. | Mixed origin: reused participant utilities and prior model inputs; completed. | Singapore source sample: 75 hemodialysis and 75 peritoneal dialysis patients; two 10,000-person modeled cohorts. |
| G015 | Compare internal responsiveness of EQ-5D-5L and EORTC QLQ-C30 after breast cancer surgery. | `measurement_property_evaluation` | Quantitative empirical; longitudinal at pre-surgery, 6 months, and 12 months. | Reused routine clinical PROM data; completed. | 333 women treated with curative intent at one Dutch center. |
| G168 | Assess whether Canadian youth can complete and explain EQ-5D-Y-5L DCE tasks. | `methods_research` | Convergent parallel mixed methods; cross-sectional session. | New participant data; data collection complete but analysis had not started at submission. | Purposive stratified target n=36, ages 13-18, in six age-by-gender focus groups. |
| G154 | Define and apply a taxonomy of value-set obsolescence. | `conceptual_or_policy_research` | Conceptual synthesis with desktop identification of value sets; not applicable time structure. | Author synthesis and published sources; completed. | No participant sample. |
| G146 | Produce an Indonesian EQ-5D-Y-3L value set and test DCE-to-cTTO mapping. | `value_set_development` | Quantitative empirical; cross-sectional. | New participant data; completed. | Indonesian adults: 1,072 analyzed for DCE and 222 analyzed for cTTO, from separate samples. |

### Uses, products, outcomes, findings, limitations, and concepts

| ID | Instrument, method, and model uses | Product and outcomes | Main finding | Main limitation and concepts |
|---|---|---|---|---|
| G109 | EQ-5D-5L current health, EQ VAS, and hypothetical-state valuation; EQ-VT 2.6.1; cTTO, DCE, and quality control; Tobit, conditional logit, and preferred hybrid model. | Final Moroccan value set; utility range and dimension weights. | 11111=1 and 55555=-1.492; pain/discomfort had the largest weight. | Rural and low-literacy groups were under-represented. Concepts: national tariff, preference weighting, interview quality. |
| G101 | Reused EQ-5D-5L DCE data only for the current analysis. Source studies also used cTTO, self-report, EQ VAS, and EQ-VT, but those data were not current inputs. Mixed logit was primary; heteroskedastic conditional logit was comparator. | Comparative preference evidence; relative dimension importance and coefficient differences. | No single Asian preference pattern appeared; about 9.3 of 20 coefficients differed on average between population pairs. | Unknown common scale and minimally important difference; sampling, language, and culture effects could not be isolated. |
| G125 | Reused Italian EQ-5D-5L current-health responses and EQ VAS; scored with the Italian value set. cTTO and DCE belong to the source valuation context. Descriptive tests, ANOVA, and OLS. | Final Italian norms; dimension prevalence, index, and VAS outcomes. | 34.7% reported 11111; mean index was 0.93 and mean VAS was 81.8. | Older adults were under-represented; videoconference use can select for digital literacy. Concepts: population norms, representativeness. |
| G160 | Reused EQ-VT cTTO interviews; conversation analysis, thematic categorization, independent coding, and a weighted pattern score. Quantitative EQ-VT quality control was a comparison source. | Final pattern taxonomy and candidate interviewer score: 20 positive and 14 negative patterns. | Pattern scores generally distinguished strong and weak interviewers in the same direction as quantitative quality control. | Pattern development used only two interviewers; non-verbal behavior and later interview batches were absent. Concepts: interviewer behavior, response bias, quality control. |
| G195 | EQ-5D-Y-3L and EQ VAS self and proxy administration at admission and discharge; Zimbabwe value set used for scoring. Kappa, ICC, Spearman correlation, paired tests, and Paretian Classification of Health Change. | Measurement-property evidence: agreement, convergent validity, and responsiveness. | Dimension agreement was fair; 91.4% improved by the Paretian classification; child index rose from 0.422 to 0.810. | The Zimbabwe tariff is not Ethiopian; the acute inpatient setting favors improvement. Concepts: proxy agreement, pediatric HRQoL, responsiveness. |
| G010 | Historic EQ-5D-5L pain/discomfort data were visualized, not used to measure current participant health. Paper prototypes, a checklist, Wilcoxon and McNemar tests, and directed content analysis were used. | Prototype visualizations and design guidance; comprehension, usefulness, readability, and preference outcomes. | 58.3% preferred the first pre-surgery option and 64% preferred the second post-surgery option; comprehension was 50-72%. | The study tested paper parts after a surgery decision, not the full online aid. Concepts: decision support, shared decision-making, data visualization. |
| G196 | EQ-5D-Y-5L was translated, culturally adapted, and content tested. The workflow used forward translation, reconciliation, back translation, cognitive debriefing, card ranking, and proofreading under VMC guidance. | Approved Egyptian Modern Standard Arabic paper and digital translation; content and comprehension outcomes. | Children made 10 incorrect rankings among 160 card rankings; wording changes improved clarity. | Dialect differences remain, and local psychometric validation is still needed. Concepts: semantic equivalence, cultural suitability, severity ordering. |
| G116 | EQ-TIPS-3L version 2.0 was the refinement object and discussion stimulus. Virtual focus groups and thematic analysis were reported under SRQR. | Instrument-refinement evidence and recommendations; perceived content, use, and challenge themes. | Experts found it short and generally suitable, but raised missing sleep and emotion content and possible overlap between communication and social interaction. | Recruitment used known networks and did not capture caregiver lived experience. Concepts: content validity, developmental suitability, proxy perspective. |
| G131 | EQ-HWB was an implementation and face-validity object in interviews; other aged-care quality-of-life measures were broader-project or discussion context. Workshops, semi-structured interviews, and qualitative interpretive thematic analysis were used. | Implementation evidence and guidance; four theme groups. | Participants supported use in care planning but identified burden, manipulation, acquiescence, and weak proxy knowledge as risks. | One provider context and pre-rollout data limit transfer. Concepts: routine measurement, care planning, proxy validity, conflicts of interest. |
| G014 | EQ-5D evidence was synthesized; the review did not administer EQ-5D. PRISMA search and selection, NOS appraisal, DerSimonian-Laird random-effects meta-analysis, subgroup, sensitivity, and Egger analyses were used. | Final evidence synthesis and pooled estimates. | Pooled utility was 0.76 and VAS was 70.76, both with I-squared above 99%; pain/discomfort problems were most frequent at 51%. | Extreme heterogeneity, English-only selection, final-time-point use, and many missing tariffs constrain pooled claims. Concepts: COVID-19, recovery, geographic heterogeneity. |
| G083 | Observed EQ-5D-5L was a utility source; SF-12 was a mapping source; EQ-5D-3L was a mapping target; SF-6D was a comparator. Five mapping algorithms and two Markov cost-utility models were used. | Economic and methodological evidence; utilities, QALYs, and ICERs. | Mapped utilities reduced incremental QALYs by 14.9-33.2% and increased ICERs by 17.5-49.7%. | One Singapore dialysis evaluation and mismatched source samples and tariffs limit transfer. Concepts: mapping uncertainty, measure choice, reimbursement consistency. |
| G015 | Dutch EQ-5D-5L and EQ VAS were administered and scored; EORTC QLQ-C30 version 3.0 was the comparator. Paired tests, effect sizes, standardized response means, and chemotherapy subgroup analysis were used. | Measurement-property evidence for internal responsiveness. | EQ-5D-5L index changed by -0.05 at 6 months and -0.03 at 12 months; all full-sample effect sizes and response means were below 0.5. | No external responsiveness criterion was used, and the cohort had limited true change. Concepts: internal responsiveness, minimally important change, cancer PROMs. |
| G168 | Planned EQ-5D-Y-5L current-health and EQ VAS administration, 13 DCE tasks, and three DCE-with-duration tasks for older youth. Planned focus groups, field notes, descriptive indicators, content analysis, and narrative integration. | Planned feasibility evidence; incompletion, speeding, flatlining, dominance violation, and qualitative experience outcomes. | `NOT_REPORTED`: analysis had not started at the stated source date. | n=36 is too small for preference modeling; snowball recruitment can miss disadvantaged youth. Concepts: youth valuation, task engagement, mixed-method convergence. |
| G154 | EQ-5D and other preference-based instruments were examples, not administered instruments. Authors used conceptual synthesis and desktop review; no fitted model. | Final obsolescence taxonomy and response framework. | Obsolescence depends on normative fit, methods, population composition, preference change, and instrument change; elapsed time alone is insufficient. | No external validity standard or agreed decision authority exists. Concepts: value-set validity, obsolescence, HTA transition cost. |
| G146 | EQ-5D-Y-3L hypothetical states were valued from an adult perspective about a 10-year-old child. DCE and cTTO followed the youth protocol with quality control. Mixed logit fed linear and power mappings; power mapping without a constant was final. | Final Indonesian youth value set and methodological evidence. | The final range was 1.000 to -0.086; pain/discomfort had the largest weight. Non-linear mapping fit better. | cTTO states were sparse where the curve bent; DCE and cTTO samples differed; the final non-linear transform does not preserve an interval scale. Concepts: anchoring, commensurability, nonlinear mapping. |

## 6. Gap and ambiguity log

| ID | State | Affected item | Evidence and reason | Proposed resolution |
|---|---|---|---|---|
| G015 | `UNCERTAIN_MAPPING` | EQ VAS direction | The instrument description states 0 is best and 100 is worst, but the reported scale use and standard EQ VAS direction suggest the reverse. | Retain the source statement and result values. Check the publisher XML or correction before direction coding. |
| G014 | `UNCERTAIN_MAPPING` | Quality appraisal counts | The reported NOS categories are 5 low, 110 moderate, and 73 high. They total 188, but the review reports 187 included studies. | Store each count with one `SourceConflict`. Do not repair the denominator. |
| G125 | `UNCERTAIN_MAPPING` | Household-size table denominator | A household-size count in the source exceeds the study sample. This can be a source or conversion error. | Check the rendered publisher table before extraction of that result. |
| G146 | `UNCERTAIN_MAPPING` | cTTO observation count | The results report 2,664 observations, which equals 222 by 12. The discussion gives 222 by 10=2,220. | Preserve both statements in a `SourceConflict`; use 2,664 only for the explicitly reported result after source review. |
| G154 | `UNCERTAIN_MAPPING` | Taxonomy label | The table uses “redundancy” while the text defines “obsolescence.” It is unclear whether the terms are intended as exact synonyms. | Retain both source labels. Ask the domain review to select the canonical product-term relation. |
| G168 | `UNMODELED_ASPECT` | Youth co-researcher involvement | Two adolescents acted as student investigators in design, data collection, and planned analysis. The core records do not represent public involvement roles. | Consider a later `StakeholderInvolvement` use record if this aspect recurs. |
| G195 | `UNMODELED_ASPECT` | Assistance for young self-report | Children aged 4-7 received read-aloud assistance. Respondent role alone does not express assistance. | Add an optional `completion_assistance` key to `InstrumentUse` after domain review. |
| G154 | `NOT_REPORTED` | Formal taxonomy-development protocol | The article reports author conceptualization and group feedback but does not report a formal selection or consensus protocol. | Keep the protocol absent. Do not infer Delphi, consensus, or systematic-review methods. |

No paper required an `UNMAPPED_VALUE` for the initial primary research family. If a later paper supplies a new controlled source value, record `UNMAPPED_VALUE` until review. Open product labels, concepts, and registry source labels do not create this gap.

## 7. Rejected distinctions

- Reject a mixed list such as `longitudinal`, `valuation study`, `qualitative`, and `economic evaluation` as one study-type vocabulary. These terms belong to different axes.
- Reject one general `USES_INSTRUMENT` relation. It loses administration, valuation, scoring, mapping, display, synthesis, and discussion roles.
- Reject `hybrid` as a method when it names a fitted value-set model.
- Reject `secondary study` as a complete data description. Record the reused data asset and its source-study relation.
- Reject one sample-size number. Keep approached, completed, excluded, analyzed, and modeled counts separate.
- Reject publication form as study status. G168 is a protocol publication, but data collection was complete at submission.
- Reject product state as study status. An approved translation can come from a completed study; a completed study can produce planned guidance.
- Reject `none` for a missing model, protocol, result, or value set. Use a justified absence, `NOT_REPORTED`, or `not applicable` only on an axis that defines it.
- Reject comma-joined multi-value text for methods, instruments, countries, languages, or concepts. Each value needs a separate relation and source label.
- Reject automatic identity merges from titles, author initials, organization strings, or instrument family names.
- Reject a finding without a result or evidence anchor. A pooled claim also needs its source-study denominator and heterogeneity evidence.

## 8. Stability and next risks

The stable core is the separation of study, component, data, use, product, outcome, result, finding, and evidence. This structure represented all 15 papers without a forced research-family value. The exact-one primary family also produced a complete 15-paper count.

The main next-round risks are:

1. Dual-purpose studies can make the primary family unstable. G146 develops a value set and tests a mapping method. The principal product rule assigns value-set development, but a second reviewer must test this rule.
2. A study-component boundary needs a coding guide. G168 has parallel quantitative and qualitative components. G083 has utility estimation and two decision models.
3. Instrument identity can fail at version, level, language, proxy, and digital-form boundaries.
4. Review `EvidenceUnit` volume can become large. The ontology must retain source-study roles without flattening them into review-level claims.
5. Result granularity needs a profile. It must preserve denominator, time, scale direction, comparison, and uncertainty without creating unusable atomic records.
6. Conceptual papers need open product content. Their internal taxonomy values must not become general study classes.
7. Protocol reports can become stale. A later publication must update status through a dated assertion, not by overwriting the source state.
8. Registry matches for people, organizations, places, and languages need verified identifiers. The article metadata alone can contain converter noise.

For round 2, two reviewers should independently code a larger and diverse paper set. They should compare the exact-one primary family, component boundaries, use roles, gap use, and denominators. Aggregate tests should declare the study universe, unit of count, multi-value behavior, missing-data rule, and source date before they return a count.

## 9. Question coverage audit

The 100 questions were used only as a coverage audit. They require five query views:

- identity and eligibility by publication, study, person, organization, place, and language;
- complete study counts by primary family, with separate filters for design, time, origin, status, and publication form;
- instrument, method, protocol, and model use by role and context;
- products, outcomes, results, findings, limitations, and concepts with denominators and evidence;
- missingness, conflicts, and source-date views that do not treat unknown as no.

The questions did not define the ontology. The 15 articles supplied the scientific distinctions.

## 10. Inputs and source verification

I used only these support inputs: `pilot/ontology-development-v4/PROTOCOL.md`, `pilot/ontology-development-v4/round-01.tsv`, `pilot/ontology-development-v3/ONTOLOGY_V1.md`, `pilot/ontology-development-v3/questions.tsv`, and `pilot/ontology-development-v3/aggregate-validity/SYNTHESIS.md`.

I read all 15 manifest articles in full. On 2026-08-20, each file matched the manifest byte count and SHA-256 exactly:

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
