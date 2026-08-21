# Version 0.13 gap audit

This audit covers all 210 `Gap` items in 150 of 209 corrected records and all
77 review-level ontology-gap mentions in 63 records. The two counts overlap and
must not be added. `G/R` gives the Gap-item count and review-mention count.
Record IDs in the tables use the common `V2-` prefix.

## MERGE

| Missing feature | G/R | Record IDs | Exact controlled change |
|---|---:|---|---|
| Quality-control software | 8/8 | P001, P051, P088, P095, P133, P139, P158, P175 | Add `software_function=QUALITY_CONTROL`: software checks data quality, protocol compliance, fraud, or operator performance. |
| Model comparison | 2/0 | P021, P156 | Add `comparison_structure=BETWEEN_MODEL`. |
| Product comparison | 2/2 | P050, P139 | Add `comparison_structure=BETWEEN_PRODUCT` for frameworks, value sets, and other reusable products. |
| Clinical classification guidance | 4/4 | P007, P035, P153, P169 | Add `protocol_function=CLINICAL_DEFINITION_OR_CLASSIFICATION`: supplies diagnostic, severity, staging, case-definition, or recovery criteria without governing study conduct. |
| Data management method | 2/2 | P021, P093 | Add `method_function=DATA_MANAGEMENT`: links, merges, cleans, transforms, or constructs datasets. |
| Expert consensus | 3/1 | P057, P110, P151 | Add `method_function=EXPERT_CONSENSUS`. Require an explicit consensus or Delphi procedure, not an ordinary investigator decision. |
| External anchor | 3/3 | P022, P035, P144 | Add `instrument_function=EXTERNAL_CRITERION`: supplies an anchor or criterion for validity, change, responsiveness, or group classification. |
| Feasibility or acceptability purpose | 3/2 | P005, P030, P203 | Add `research_purpose=FEASIBILITY_OR_ACCEPTABILITY_EVALUATION`. |
| Instrument-content method | 3/2 | P004, P094, P117 | Add `method_function=INSTRUMENT_CONTENT_DEVELOPMENT`: generates, selects, reduces, or refines items, dimensions, or labels. |
| Methodological guidance | 5/1 | P055, P104, P185, P193, P209 | Add `protocol_function=METHODOLOGICAL_GUIDANCE`: an external standard or framework supplies design, analysis, classification, or quality criteria but does not govern the full study. |
| Reusable method product | 2/2 | P064, P182 | Add `product_type=METHOD` for a reusable scientific method or experimental design produced by the study. |
| Observed data | 3/2 | P031, P114, P160 | Add `data_level=OBSERVED_MEASUREMENT`: a unit-level device, clinician, observer, or researcher measurement that is not participant-supplied. |
| Existing product used as input | 5/5 | P009, P025, P060, P137, P167 | Add `product_function=INPUT`: an existing product supplies values, content, or structure for analysis, rescaling, design, or product development and is not itself tested. |
| Sample-characterization instrument | 3/2 | P005, P091, P130 | Add `instrument_function=SAMPLE_CHARACTERIZATION`. Use it only for descriptive demographic, clinical, socioeconomic, or contextual data. |
| Training protocol | 2/1 | P069, P095 | Add `protocol_function=TRAINING_PROTOCOL`. |

## NEXT_VERSION

| Structural change | G/R | Record IDs | Exact change |
|---|---:|---|---|
| Multiple comparison structures | 14/11 | P014, P017, P031, P065, P072, P085, P087, P107, P120, P135, P176, P186, P189, P202 | Permit multiple `comparison_structure` Design items for one study or part. Make `NONCOMPARATIVE` exclusive. Do not add compound values. |
| Study registration | 4/4 | P057, P150, P164, P200 | Add `StudyRegistration` linked to `Study`, with exact `registry_label`, `registration_identifier`, and optional source-reported date or prospective status. Do not use scientific-use `registry_id`. |
| Views and priorities outcome | 3/3 | P104, P148, P162 | Add candidate `outcome_family=VIEWS_OR_PRIORITIES` for normative views, recommendations, or priority scores that are not health preferences, usability, or conceptual classifications. Confirm its boundary with open `Concept` and `Finding` items before release. |

## KEEP_AS_GAP

| Class | G/R | Record IDs | Governance result |
|---|---:|---|---|
| Source absence or optional missingness | 76/2 | P001, P003, P005, P008, P010, P016, P019, P026, P034, P042, P048, P053, P054, P055, P060, P062, P063, P068, P070, P071, P073, P075, P076, P081, P084, P088, P090, P091, P092, P093, P100, P106, P109, P110, P111, P114, P115, P119, P121, P123, P129, P132, P136, P137, P139, P140, P141, P143, P144, P146, P149, P150, P154, P159, P167, P168, P171, P174, P175, P178, P180, P184, P190, P192, P194, P197, P200, P204, P205; review-only P207 | No controlled change. Keep `NOT_REPORTED` only for required or scientifically material facts. Routine absent language, software, source labels, and optional flow details should be omitted, not emitted as ontology gaps. |
| Data-origin or context uncertainty | 18/0 | P002, P003, P006, P019, P043, P044, P052, P065, P097, P108, P118, P125, P128, P176, P184, P190, P202, P206 | Source-specific provenance uncertainty. Resolve from companion papers or authors; do not add an origin value. |
| One-paper or unresolved boundary cases | 45/20 | P010, P011, P018, P020, P025, P033, P034, P041, P047, P049, P050, P051, P056, P059, P061, P062, P063, P074, P088, P093, P094, P098, P113, P115, P116, P122, P124, P125, P131, P138, P142, P154, P157, P158, P162, P170, P182, P191, P200, P203, P207 | Keep the current gaps. These cover isolated hardware, protocol-deviation, revision-relation, scoping-review, paradata, eligibility-screening, special-outcome, and type-boundary cases. A new value would overfit the present evidence. |

## Reconciliation and release implication

The reconciled totals are **MERGE 50/37**, **NEXT_VERSION 21/18**, and
**KEEP_AS_GAP 139/22**. They sum to 210 Gap items and 77 review-level mentions.

The current version-0.13 records remain valid because all unresolved mappings
are explicit. The MERGE changes are candidates for a focused version-0.14
repair. The NEXT_VERSION changes need more design work before implementation.
KEEP_AS_GAP does not change the schema.
