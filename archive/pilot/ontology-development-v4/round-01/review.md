# Round 1 independent typed-ontology review

## Overall verdict

Use a merge. Candidate B supplies the exact-one primary research family that is needed for coherent study counts. Candidate A supplies the stronger scientific separations for purpose, provenance, use context, status, findings, interpretations, and products. Neither candidate is ready unchanged.

The merged model can support broad aggregation if every controlled key represents one scientific dimension. It must not treat design, time, data origin, publication form, and purpose as alternative study types.

## Agreements

Both candidates correctly support these points:

- `Publication`, `Study`, and `StudyComponent` are different records.
- A paper can report more than one component, purpose, population, sample, data asset, method, instrument, outcome, and result.
- Instruments, methods, protocols, models, and languages need registries. Exact source labels and version text must remain available.
- Current use, source-study use, planned use, and discussion-only mention must not be merged.
- Missing evidence must use an explicit gap state. It must not become `NO`.
- Passage-level evidence anchors and source conflicts are necessary.
- Open scientific concepts must remain open until repeated evidence supports a controlled list.
- A catch-all `OTHER` value is not a safe substitute for a missing concept or an uncertain mapping.

## Material differences and tradeoffs

| Topic | Candidate A | Candidate B | Review decision |
|---|---|---|---|
| Research classification | Rich, ranked, multi-value purposes | Exact-one broad family plus secondary purposes | `MERGE`: keep the exact-one family and the ranked purpose layer. Revise composite family labels. |
| Use assertions | One generic record with separate context and function | Separate typed records, but several roles contain context | `MERGE`: use typed records with A's separate context and function axes. |
| Design | Detailed axes, but `MIXED` and source-data reanalysis occur on design axes | Simpler axes, but translation and modeling are mixed with empirical approach | `MERGE`: classify each component. Put integration, time, and data origin on separate axes. |
| Data origin | One origin per data use, but one value also contains data level | One origin per component and a `mixed_origin` value | `ACCEPT` A's per-use structure after value revision. `REJECT` `mixed_origin`. |
| Study status | Separate execution and result state | One progression field | `ACCEPT` the separate axes. Add an evidence date. |
| Product state | One maturity field | One field that mixes development, approval, validation, and use | `REJECT` both single fields. Use state assertions with separate axes. |
| Results and claims | Separates estimate, finding, and interpretation | Allows author interpretation as a finding support kind | `ACCEPT` the separation. Use one general `Result` record for quantitative and qualitative results. |
| Products | Restricted to reusable outputs | Includes generic empirical evidence | `ACCEPT` the restricted scope. A result or finding is not a product. |
| Gaps and conflicts | Separate records | Separate records, but some conflicts are coded as uncertain mappings | `ACCEPT` separate records and enforce their boundaries. |

## Paper-backed decisions

Only disagreements that could change the vocabulary were checked against article passages.

- **G083:** The paper evaluates mapped utilities inside two Markov cost-utility models and reports QALYs and cost-effectiveness results. Its primary family is `HEALTH_ECONOMIC_EVALUATION`. Method comparison is a secondary purpose. This case shows why a method name must not determine the research family.
- **G131:** The paper uses material from several steps of a wider project. The present analysis uses selected parts of those steps. A single study-level `new` or `reused` flag loses this detail. Each data asset needs its own `DataUse` and origin.
- **G168:** At protocol submission, data collection was complete and analysis had not started. The instrument administrations are completed current-study activities, while the analyses are planned activities. `PROTOCOL_ARTICLE`, execution state, result state, and use context must be separate.
- **G160:** The authors call the scoring version used on the remaining interviews final. They also call the study exploratory and the comparison with quantitative quality-control indicators preliminary. This supports `FINALIZED` on a development axis, but it does not support `VALIDATED` or `DEPLOYED`.
- **G196:** The paper reports a final Arabic version approved through the version-management process. It also states that psychometric results will be reported separately. `FINALIZED`, `APPROVED`, and `VALIDATED` are different state axes.
- **G195:** Children aged 4–7 gave their own responses while trained staff read text aloud and gave limited clarification. This is assisted self-completion, not proxy report. Administration mode and completion assistance must be separate.

## Vocabulary proposals

| Mark | Proposal | Reason |
|---|---|---|
| `MERGE` | Exact-one `primary_research_family` plus ranked, multi-value `research_purpose` | The family supports a complete study partition. Purposes preserve real multi-purpose work. |
| `ACCEPT` | Base the primary family on the main scientific decision or reusable output | A design, method, instrument, or time structure must not select the family. |
| `REJECT` | Composite family labels such as `clinical_or_implementation_research` and `conceptual_or_policy_research` | Each label joins different scientific purposes. Use the revised labels below. |
| `ACCEPT` | Separate `InstrumentUse`, `MethodUse`, `ProtocolUse`, and `ModelUse` records | Their function vocabularies differ and need separate checks. |
| `REJECT` | An exposed generic `UseAssertion` as the only use record | It permits invalid role and registry combinations. A shared internal structure is acceptable. |
| `ACCEPT` | Exact-one use context and exact-one function per use assertion | Multiple assertions preserve multiple roles without ambiguous lists. |
| `REJECT` | Function values that contain `current`, `source`, `planned`, or `discussion` | These words encode context, not scientific function. |
| `ACCEPT` | Component-level approach, time structure, comparison structure, allocation, and mixed-method integration | These are independent dimensions. |
| `REJECT` | `SOURCE_DATA_REANALYSIS` as a time or observation design | Reanalysis is about data origin and use. |
| `REJECT` | `MIXED` as an evidence approach and `mixed_origin` as a data origin | Mixed methods is an integration property. Mixed origin means that more than one `DataUse` is needed. |
| `ACCEPT` | One origin and one data level per `DataUse` | G131 shows that origin can differ between assets in one study. |
| `ACCEPT` | Separate, source-dated execution state and result state | G168 has completed collection and no completed analysis at the same date. |
| `REJECT` | One product-state enum containing `final`, `approved`, `validated`, and `in_use` | These states answer different questions. |
| `ACCEPT` | Separate `Result`, `Finding`, and `Interpretation` records | A numeric or qualitative result, an evidence claim, and an author's meaning are not synonyms. |
| `REJECT` | `empirical_evidence` as a general `Product` type | Empirical evidence belongs in results and findings. Products are reusable outputs. |
| `ACCEPT` | A distinct scoring relation from instrument responses to a value-set product | A value set is not an instrument role. |
| `ACCEPT` | Separate administration mode and completion-assistance qualifiers | G195 must remain self-report even when help is given. |
| `ACCEPT` | Separate `SourceConflict` and `Gap` records | A source contradiction is not an uncertain ontology mapping. |
| `KEEP_OPEN` | A new primary family for etiologic or health-outcome studies | No manifest paper requires it as its primary family. Test it in round 2 before addition. |
| `KEEP_OPEN` | A new `StakeholderInvolvement` record | G168 can be represented with `AgentRole` now. One case does not justify another record type. |
| `KEEP_OPEN` | The full controlled value list for `StudyFactor.factor_role` | Intervention, comparator, condition, exposure, and subgroup are useful, but the boundary needs another application round. |

## Recommended typed ontology

### Record structure

Use these records in the synthesis:

1. `Project`, `Publication`, `Study`, and `StudyComponent`.
2. `Population`, `Sample`, `DataAsset`, `DataUse`, and `EvidenceUnit`.
3. `Instrument`, `Method`, `Protocol`, `Model`, and `Language` registry records.
4. `InstrumentUse`, `MethodUse`, `ProtocolUse`, `ModelUse`, `ScoringUse`, `Administration`, and `AnalysisStep`.
5. `StudyFactor`, `Outcome`, `Result`, `Finding`, `Interpretation`, `Limitation`, and `Product`.
6. `StateAssertion`, `SampleSizeAssertion`, `Concept`, `AgentRole`, `Gap`, `SourceConflict`, and `EvidenceAnchor`.

`Project` contains studies and publications. A publication reports one or more studies or components. A component uses a data asset through `DataUse`. Scientific use records connect a registry entity to a study component. Results support findings. Findings support interpretations. Every controlled assignment and every important claim can point to an `EvidenceAnchor`.

### Core controlled keys

| Owner | Key | Cardinality and control |
|---|---|---|
| `Study` | `primary_research_family` | Exactly one controlled value, or one explicit mapping gap |
| `Study` | `research_purpose` | One or more controlled values, with rank and evidence |
| `Publication` | `publication_form` | Exactly one controlled value |
| `Publication` | `publication_status` | One source-dated controlled value |
| `StudyComponent` | `component_approach` | Exactly one controlled value |
| `StudyComponent` | `temporal_structure` | Exactly one controlled value or `NOT_REPORTED` |
| `StudyComponent` | `comparison_structure` | Zero or more controlled values |
| `StudyComponent` | `allocation_structure` | One controlled value when applicable |
| `Study` or `StudyComponent` | `mixed_method_integration` | One controlled value when more than one empirical approach is integrated |
| `DataUse` | `data_origin` | Exactly one controlled value |
| `DataUse` | `data_level` | Exactly one controlled value |
| `DataAsset` | `availability_state` | One controlled value when availability is in scope |
| Typed use record | `use_context` | Exactly one controlled value |
| Typed use record | `function_role` | Exactly one type-specific controlled value |
| State assertion | `state_axis`, `state_value`, `as_of` | Exactly one value on one axis at one evidence date |
| Sample-size assertion | `sample_stage`, `count` | One named stage and one count per assertion |
| `Administration` | `respondent_role`, `delivery_mode`, `completion_assistance` | Separate controlled qualifiers; no inferred negative value |

### Primary research family

Use this exact-one broad partition for the current domain:

- `VALUE_SET_DEVELOPMENT`: the main output is a preference-based scoring system or value set.
- `MEASUREMENT_PROPERTY_EVALUATION`: the main decision concerns reliability, validity, responsiveness, agreement, or related measurement performance.
- `INSTRUMENT_VERSION_DEVELOPMENT`: the main output is new or adapted instrument content or a language version.
- `POPULATION_REFERENCE_DESCRIPTION`: the main output describes population health, reference values, or norms.
- `METHODS_RESEARCH`: the main decision concerns the performance, feasibility, quality, or choice of a research method or protocol.
- `APPLIED_USE_RESEARCH`: the main decision concerns practical use, implementation, or decision support with an instrument.
- `EVIDENCE_SYNTHESIS`: the main output synthesizes prior studies.
- `HEALTH_ECONOMIC_EVALUATION`: the main output compares costs and health consequences for decisions.
- `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`: the main output is a taxonomy, framework, or conceptual classification.

Apply the family from the stated aim, main reported output, and conclusion. Put additional aims in `research_purpose`. If the evidence does not select one family, use `UNCERTAIN_MAPPING`; do not force a value.

The diagnostic assignment covers the 15 papers without overlap:

| Primary family | Papers | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | G109, G146 | 2 |
| `MEASUREMENT_PROPERTY_EVALUATION` | G015, G195 | 2 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | G116, G196 | 2 |
| `POPULATION_REFERENCE_DESCRIPTION` | G125 | 1 |
| `METHODS_RESEARCH` | G101, G160, G168 | 3 |
| `APPLIED_USE_RESEARCH` | G010, G131 | 2 |
| `EVIDENCE_SYNTHESIS` | G014 | 1 |
| `HEALTH_ECONOMIC_EVALUATION` | G083 | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | G154 | 1 |

These rows sum to 15 studies. The purpose layer must preserve the additional aims that this partition does not show.

### Purpose and design values

Use Candidate A's finer purpose values after these naming changes: `VALUE_SET_DEVELOPMENT`, `PREFERENCE_METHOD_RESEARCH`, `POPULATION_NORMS`, `MEASUREMENT_PROPERTY_EVALUATION`, `INSTRUMENT_DEVELOPMENT`, `TRANSLATION_AND_CULTURAL_ADAPTATION`, `METHOD_QUALITY_EVALUATION`, `IMPLEMENTATION_EVALUATION`, `DECISION_SUPPORT_DEVELOPMENT`, `OUTCOME_DESCRIPTION`, `ECONOMIC_EVALUATION`, `EVIDENCE_SYNTHESIS`, and `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`.

Use these component approaches: `QUANTITATIVE_EMPIRICAL`, `QUALITATIVE_INQUIRY`, `MODEL_BASED`, `EVIDENCE_SYNTHESIS`, `CONCEPTUAL`, and `TRANSLATION_ADAPTATION_WORKFLOW`. A mixed-method study has two or more components plus an integration assertion. It does not need a `MIXED` component value.

Use these time values: `CROSS_SECTIONAL`, `LONGITUDINAL_REPEATED`, `VARIABLE_SOURCE_TIME`, `NOT_APPLICABLE`, and `NOT_REPORTED`.

Use report-form values that do not contain a study design: `ORIGINAL_RESEARCH_ARTICLE`, `PROTOCOL_ARTICLE`, `REVIEW_ARTICLE`, `CONCEPTUAL_ARTICLE`, and `OPINION_ARTICLE`. Record systematic review, meta-analysis, and narrative synthesis on a separate synthesis-design axis.

### Data origin and level

Use these origin values per `DataUse`: `CURRENT_STUDY_COLLECTION`, `PRIOR_RESEARCH_COLLECTION`, `ROUTINE_SERVICE_COLLECTION`, `REVIEW_EXTRACTED_EVIDENCE`, `DOCUMENTARY_SOURCE`, `PUBLISHED_MODEL_INPUT`, `SIMULATED_DATA`, `CONCEPTUAL_MATERIAL`, and `NOT_REPORTED`.

Keep data level separate. Initial values are `PARTICIPANT_RESPONSE`, `QUALITATIVE_MATERIAL`, `AGGREGATE_ESTIMATE`, `MODEL_PARAMETER`, `SIMULATED_UNIT`, `DOCUMENT`, and `NOT_REPORTED`.

Keep data availability separate from origin. Use `OPEN`, `ON_REQUEST`, `RESTRICTED`, `NOT_AVAILABLE`, and `NOT_REPORTED`. Use `NOT_AVAILABLE` only when the source makes that negative statement.

### Use context and function

Use one of these contexts on each typed use assertion: `DIRECT_CURRENT_ACTIVITY`, `CURRENT_STUDY_OBJECT`, `SOURCE_STUDY_ACTIVITY`, `INPUT_DATA_PROVENANCE`, `PLANNED_ACTIVITY`, or `DISCUSSION_ONLY`.

Function vocabularies must be type-specific. The first synthesis should include at least:

- Instrument: administration, outcome measure, predictor measure, content-test object, health-state description source, valuation target, mapping source, mapping target, comparator, visualization object, development object, translation source, translation target, synthesis target, implementation object, and reference.
- Method: elicitation, sampling, qualitative data collection, quantitative analysis, qualitative analysis, evidence synthesis, mapping, economic evaluation, validation, and quality control.
- Protocol: governing study protocol, valuation protocol, translation protocol, quality-control protocol, reporting guideline, and critical-appraisal protocol.
- Model function: statistical estimation, choice modeling, mapping, meta-analysis, decision analysis, and scoring.

Give `ModelUse` a separate analytic-role key with `CANDIDATE`, `COMPARATOR`, `PRIMARY_REPORTED`, `SENSITIVITY`, and `SUBGROUP`. Record model selection as a result, not as a model function or status.

Create separate assertions when one entity has more than one function. Aggregate counts must count distinct studies or components as stated by the question, not raw use assertions.

### State, evidence, and open information

Represent study execution and result availability on separate, dated axes. Represent product development, formal approval, validation, and deployment on separate state axes. Do not infer `NOT_VALIDATED`, `NOT_APPROVED`, or `NOT_IN_USE` from silence.

Keep publication status separate from publication form. Initial status values are `CURRENT`, `RETRACTED`, `WITHDRAWN`, `SUPERSEDED`, and `NOT_REPORTED`. Represent a correction as a linked publication, not as a study design or scientific status.

Use one `Result` type with typed subkinds for quantitative estimates, qualitative results, classifications, and model outputs. Keep a source-supported `Finding` separate from an author's `Interpretation`. Keep reusable value sets, instrument versions, scoring systems, taxonomies, decision-support tools, and protocols as products.

Keep aims, inclusion criteria, result text, finding text, interpretation text, limitation text, source labels, and new concept labels as open text. A limitation is source-stated unless its assertion origin is explicitly `REVIEWER_INFERRED`.

Use only these gap states: `UNMAPPED_VALUE`, `UNMODELED_ASPECT`, `UNCERTAIN_MAPPING`, and `NOT_REPORTED`. Use `SourceConflict` for disagreement between source passages or metadata.

Use one sample-size assertion for each stated stage. Initial stages are `APPROACHED`, `ENROLLED`, `COMPLETED`, `ANALYZED`, `EXCLUDED`, `INCLUDED_EVIDENCE`, and `SIMULATED`. Use a mapping gap when a source word such as “recruited” does not identify one stage.

### Aggregation rules

- Every response must state its counting unit and denominator.
- Primary-family rows count distinct studies. The scientific rows must sum to the number of mapped studies. Report mapping gaps separately; a gap is not a research family.
- Multi-value purpose, design, outcome, and use-role summaries are not partitions. State that their totals can exceed the study count.
- `NOT_REPORTED` and `UNCERTAIN_MAPPING` are audit results. Do not display them as `None`, `No`, or a scientific category.
- Instrument, method, protocol, and model counts must filter by use context and count the requested distinct unit. Raw assertion counts are not study counts.
- Source-dated states answer “as reported in the article.” They do not claim a current state.
- Registry matching must preserve the exact source label and version. Do not merge records only because their labels are similar.

## Unresolved decisions

1. Test the primary-family decision rule with independent coding, especially on mixed-purpose cases like G083, G101, G160, and G168.
2. Define the boundary between one multi-approach component and two linked components.
3. Decide how to code G131 when the paper does not make the present-study boundary fully explicit. Keep the uncertainty at the affected `DataUse`.
4. Define product-state issuers and evidence rules. A publisher statement, developer approval, psychometric validation, and real-world use are not interchangeable.
5. Test whether `HEALTH_OUTCOME_RESEARCH` is needed as another primary family in round 2.
6. Test and then freeze `StudyFactor.factor_role` values.
7. Define a rule for ambiguous sample-stage words such as “recruited.” Preserve the source term when it does not prove enrollment or analysis.

## Readiness

The candidates are ready for synthesis into one revised ontology. They are not ready for a frozen round-2 vocabulary without revision.

Before wider application, apply the merged vocabulary to all 15 papers, compare independent primary-family assignments, and run the aggregate question set again. The main pass condition is that study-family counts form one coherent partition while purpose, design, time, origin, use role, and status remain separate summaries.

## Exact input note

I read these task and review inputs:

- `pilot/ontology-development-v4/REVIEW_TASK.md`
- `pilot/ontology-development-v4/PROTOCOL.md`
- `pilot/ontology-development-v4/round-01.tsv`
- `pilot/ontology-development-v4/BUILDER_TASK.md`
- `pilot/ontology-development-v4/round-01/candidate-a.md`
- `pilot/ontology-development-v4/round-01/candidate-b.md`
- `pilot/ontology-development-v3/questions.tsv`
- `pilot/ontology-development-v3/aggregate-validity/SYNTHESIS.md`

I checked passages only in these manifest articles:

- G083: `corpus/20170450/doi_10.1007_s10198-018-0987-x.md`
- G131: `corpus/150-RA/doi_10.1007_s40271-025-00729-7.md`
- G160: `corpus/351-RA/doi_10.1007_s41669-024-00486-7.md`
- G168: `corpus/1704-RA/doi_10.1136_bmjopen-2024-097598.md`
- G196: `corpus/1492-RA/doi_10.1186_s41687-025-00985-z.md`
- G195: `corpus/436-RA/doi_10.1186_s41687-025-00928-8.md`

I did not inspect old ontology proposals, graph records, prior extraction records, or Neo4j material.
