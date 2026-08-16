# Origin decisions and open cases

## Important origin decisions

Round 1 created the ontology from an empty lineage state. These decisions define the current structure.

### D1. Use the measurement chain as the main structure

**Decision:** Separate construct, framework, instrument, component, observation, preference evidence, value set, analyzed outcome, and use context.

**Reason:** The papers study different objects that all can be called EQ-5D evidence. Kreimeier et al. develop response labels (`10.1007/s11136-019-02115-x`). Yang et al. and Jensen et al. develop value sets (`10.1007/s40273-022-01216-9`; `10.1007/s40258-021-00639-3`). Yan et al. review the later analysis of utilities and dimension responses in trials (`10.1016/j.jval.2025.02.001`). A single *instrument study* class would hide these differences.

### D2. Separate report type, study activity, and completion stage

**Decision:** A report can contain several activities, and stage is not inferred from the article label.

**Reason:** EQ-DAPHNIE is a protocol and infrastructure description, but several rounds were already complete (`10.1007/s11136-025-03983-2`). The youth 5L paper contains label generation, scaling, cognitive testing, and harmonization (`10.1007/s11136-019-02115-x`). The pain-scale paper is a secondary analysis of a prior dyadic survey (`10.1007/s11136-025-04003-z`).

### D3. Give each artifact a study-specific role

**Decision:** Record whether an instrument is a development target, evaluation target, comparator, reference, anchor, data generator, context measure, or reported option.

**Reason:** EQ-5D-5L is a reference item in the EQ-HWB pain-scale paper, an evaluation target in the psychometric review, a data generator in the Danish value-set paper, and one reported instrument in the HTA survey. Instrument name alone does not show its function.

### D4. Keep sampled person, target population, and valuation perspective separate

**Decision:** Record who responds, whose state is described or valued, and whose evidence the output is meant to represent.

**Reason:** Adults value their own general-public preferences for adult health in the Danish study. Adults value the health of an unspecified hypothetical 10-year-old in the Chinese youth valuation study. Children self-report their own health in the Brazilian measurement study. HTA personnel report professional practice but not an official agency position.

### D5. Attach evaluation properties to the correct target level

**Decision:** An evaluation must state whether it concerns an item, dimension, profile, VAS, index, value set, or full instrument.

**Reason:** Feng et al. find strong index test-retest reliability but weaker item-level stability (`10.1007/s11136-020-02688-y`). Santo et al. also report different reliability for youth dimension responses and EQ VAS (`10.1007/s10198-025-01770-x`). A report-level statement of *reliable* loses this distinction.

### D6. Make comparisons explicit objects

**Decision:** Record comparison objects, basis, design symmetry, and important confounding factors.

**Reason:** The batch compares 3L with 5L, 4L with 5L, frequency with severity, cTTO with DCE, mapping with hybrid models, Chinese lay concepts with EQ-HWB, pain with no-pain groups, and analytic practice for one versus several postbaseline measurements. These comparisons are central research contributions.

### D7. Separate output type from maturity

**Decision:** Record what was produced and whether it is draft, experimental, selected, established, planned, or still in need of validation.

**Reason:** The Danish and Chinese studies present jurisdiction-specific value sets for use. The youth 5L paper presents a new version but asks for psychometric and valuation work. EQ-DAPHNIE presents working infrastructure but not the later instrument comparisons. The EQ-HWB source version in the pain analysis was experimental during collection.

### D8. Record context and transfer limits

**Decision:** Place country, language, culture, population, condition, recall period, and use setting next to the evaluated property or comparison.

**Reason:** The Chinese QoL paper tests cultural comprehensiveness. Value-set papers show that preferences and valuation perspective can change scores. The pain-scale and Brazilian papers show that recall period and health condition can change apparent performance. The HTA survey shows regional data scarcity and use of foreign values.

### D9. Do not create a detailed result claim graph

**Decision:** Keep a short output and interpretation with material qualifiers. Do not encode every coefficient, correlation, or subgroup result.

**Reason:** The task asks for comparison support, not a claim-evidence reconstruction. Detailed estimates can remain in the source papers. The ontology records the property, method, direction, context, and main uncertainty needed for meta-research.

### D10. Keep method detail only when it changes comparison

**Decision:** Record method families by default. Record exact models or procedures when the paper compares them or uses them to select an output.

**Reason:** Exact hybrid, Tobit, mixed-logit, mapping, IRT, and DIF methods are central in some papers. Software versions and every descriptive test are not usually ontology elements.

## Round 2 change and retention decisions

### D11. Add explicit outcome derivation and provenance

**Decision:** Distinguish a direct response, a score calculated from that response, a mapped or predicted score, an unweighted aggregate, and a downstream modeled endpoint. Record the source, transformation, and target representation.

**Origin:** Yang et al. hold two dialysis decision models constant but replace directly collected and scored EQ-5D-5L with five EQ-5D-3L mappings and SF-6D scores (`10.1007/s10198-018-0987-x`). The choice changes incremental QALYs and ICERs. Spronk et al. use an equal-weight level-sum score, not a utility (`10.3389/fpubh.2021.744405`). The EQ-HWB-S paper compares a directly estimated experimental EQ-HWB-S score with EQ-5D-5L scores mapped to a 3L value set (`10.1016/j.jval.2024.05.007`). The outcome name alone does not show these differences.

### D12. Separate operational implementation from response feasibility

**Decision:** Split response and distribution properties from implementation and acceptability properties.

**Origin:** The Ontario oncology pilot evaluates reach, repeat completion, willingness, timing, format, language barriers, and coordinator burden (`10.3390/curroncol32060308`). These are properties of a collection workflow in a care setting. They are not the same as missing item responses, completion time, ceiling, or floor within an instrument.

### D13. Make respondent, referent, and requested perspective explicit

**Decision:** Record who answers, whose condition or preferences the answer describes, the requested response perspective, and relevant proxy knowledge or spillover.

**Origin:** EQ-TIPS asks an adult proxy to describe an infant or toddler, while experts warned that caregiver expectations and family spillover can enter the answer (`10.1007/s11136-025-04150-3`). The oncology pilot made a proxy form available but did not report the number of proxy answers (`10.3390/curroncol32060308`). This evidence extends the round-1 separation of respondent and valuation perspective beyond preference studies.

### D14. Add language and cultural versions as measurement artifacts

**Decision:** Treat a translated or culturally adapted version as an artifact with a source version, language, intended jurisdiction, approval status, and remaining validation scope.

**Origin:** The Egyptian study creates a Modern Standard Arabic EQ-5D-Y-5L through forward and back translation, cognitive testing, version-management review, and proofreading (`10.1186/s41687-025-00985-z`). The resulting version is more than a method note, but its approval does not establish psychometric validity or use across all Arabic-speaking settings.

### D15. Replace the broad idea of a direct comparison with alignment facets

**Decision:** In addition to the authors' comparison label, record whether a comparison is within-person, within-sample, between parallel samples, or across reused sources. Record alignment of population, timing, mode, language, source instrument, and transformation.

**Origin:** The DCEd paper calls its test a direct comparison, but cTTO/EQ-VT and DCEd use separate samples, modes, and periods in the same country (`10.1016/j.jval.2024.05.016`). The dialysis comparison uses the same patients and decision models but different instrument, mapping, recall, and value-set origins (`10.1007/s10198-018-0987-x`). The EQ-HWB-S paper combines two valuation samples with different orders, dates, and background questions (`10.1016/j.jval.2024.05.007`). A single direct or indirect label is not enough.

### D16. Extend purposes and methods without new top-level study classes

**Decision:** Add translation, implementation, population-association analysis, and downstream scoring-effect analysis as activity purposes. Add their method families. Keep them under study activity, method, evaluation, comparison, and output.

**Origin:** The Arabic youth version (`10.1186/s41687-025-00985-z`), oncology collection pilot (`10.3390/curroncol32060308`), European inequality study (`10.3389/fpubh.2021.744405`), and dialysis mapping study (`10.1007/s10198-018-0987-x`) fit the existing entity structure when their purpose and method are stated. Separate report classes would add labels but little comparison value.

### D17. Retain the measurement chain and property-level interpretation

**Decision:** Keep the round-1 main structure and do not add a generic finding entity.

**Origin:** All ten round-2 papers fit one or more existing layers. The Graves' disease paper supports reliability at dimension and score levels but gives asymmetric responsiveness evidence for worsening and improvement (`10.1186/s12955-023-02177-z`). The bolt-on paper reports different results for ceiling, structural validity, known-group discrimination, and explanatory power (`10.1016/j.jval.2024.03.2195`). Property-level interpretation remains clearer than one report-level label such as *valid*.

## Round 3 change and retention decisions

### D18. Add research-data lineage and report overlap

**Decision:** Record the source study, dataset or collection wave, final analysis cohort, material exclusions, and known overlap with other reports.

**Origin:** The cTTO-only youth analysis reuses the 418-person component of the Chinese value-set study already applied in round 1 (`10.1016/j.jval.2023.03.003`; `10.1007/s40273-022-01216-9`). The immediate-death paper reuses the 970-person DCE-with-duration sample from the round-2 method comparison (`10.1177/0272989x251325828`; `10.1016/j.jval.2024.05.016`). The Trinidad and Tobago norms paper combines that sample, the 1,079-person EQ-VT sample, and a third survey (`10.1186/s12955-024-02323-1`; `10.1186/s12955-024-02266-7`). Two EQ-DAPHNIE papers analyze data from the resource described in round 1 (`10.1007/s11136-025-04074-y`; `10.1007/s11136-026-04294-w`; `10.1007/s11136-025-03983-2`). Without lineage, a synthesis can count one set of respondents as independent evidence several times.

### D19. Extend outcome provenance to population, inequality, burden, and cost outcomes

**Decision:** Record the chain from responses or clinical observations through scoring, population scaling, inequality aggregation, disability weighting, costing, or monetization. Record perspective and cost bearer when relevant.

**Origin:** The Trinidad and Tobago norms paper derives profiles, current-value-set indexes, EQ VAS summaries, ceilings, odds ratios, and Kakwani indexes from three surveys (`10.1186/s12955-024-02323-1`). The vision paper combines clinical observations, prevalence weights, utilization, unit costs, disability weights, DALYs, and a statistical-life assumption to estimate societal costs (`10.1038/s41433-023-02860-x`). These outcomes are not interchangeable and are not direct observations.

### D20. Separate response-data integrity from population fitness and measurement properties

**Decision:** Treat bot likelihood, speeding, duplicates, repeated-item consistency, implausible values, missingness, and exclusion rules as response-data integrity. Keep sampling coverage, quota attainment, weighting, and target-population fit as data fitness. Do not call either one an instrument measurement property.

**Origin:** The EQ-DAPHNIE quality-control paper evaluates survey records and workflow rules, while the health instruments only generate data (`10.1007/s11136-025-04074-y`). The Trinidad and Tobago valuation uses interview quality flags (`10.1186/s12955-024-02266-7`). The inequality paper excludes VAS values and low BMI values before its within-profile analysis (`10.1007/s11136-026-04294-w`). These operations affect the analysis cohort but do not test validity or reliability of EQ-5D by themselves.

### D21. Make valuation framing and scale assumptions explicit

**Decision:** Record the described person, self-versus-other frame, wording, death or full-health definition, anchor, duration, and time-preference assumption when these change valuation output.

**Origin:** Random assignment shows that EQ-5D-3L versus EQ-5D-Y wording interacts with adult-self versus hypothetical-child perspective (`10.1016/j.jval.2018.05.002`). A secondary DCE analysis shows that duration versus immediate-death anchoring and linear versus nonlinear time preference produce materially different tariff ranges (`10.1177/0272989x251325828`). The cTTO-only youth study asks adults to imagine a 10-year-old child (`10.1016/j.jval.2023.03.003`). A generic label such as *DCE value* or *cTTO value* does not preserve these differences.

### D22. Record inferential aim and identification limits

**Decision:** State whether an activity is descriptive, associational, predictive, causal, psychometric, or methodological when the distinction changes interpretation. Record competing mechanisms when the design cannot distinguish them.

**Origin:** The cancer paper estimates cross-sectional income-utility associations but discusses possible HTA bias (`10.3390/curroncol32110645`). The within-profile EQ-DAPHNIE paper cannot distinguish omitted health content from socioeconomic response-scale heterogeneity (`10.1007/s11136-026-04294-w`). The Trinidad and Tobago temporal norms paper cannot assign changes to population health, reporting practice, survey mode, or the pandemic (`10.1186/s12955-024-02323-1`). The ontology must preserve what the design identifies.

### D23. Extend comparison alignment and retain the main structure

**Decision:** Add source-study overlap, calendar period, and scoring-version alignment to comparison. Keep the measurement chain, study activity, evaluation, comparison, output, and interpretation as the main structure. Do not add exclusive top-level classes for inequality, cost-of-illness, or data-quality reports.

**Origin:** The temporal norms paper applies the same current value set to 2012 and 2022–2023 profiles but still differs in samples, modes, and context (`10.1186/s12955-024-02323-1`). The new Trinidad and Tobago value set differs from the crosswalk in year, source descriptive system, protocol, and transformation (`10.1186/s12955-024-02266-7`). The vision-cost and EQ-DAPHNIE papers fit when their activities, transformations, properties, and outputs are explicit (`10.1038/s41433-023-02860-x`; `10.1007/s11136-025-04074-y`). New report classes would not improve comparison.

## Elements considered but not retained as independent top-level concepts

- **Finding:** Merged into evaluation, output, and interpretation. A generic finding entity would invite detailed claim extraction.
- **Country:** Kept as a context facet of evidence, artifact, value set, or use. A country alone is not a research object in this batch.
- **Representativeness:** Kept as an assessment supported by sampling details. It is not a binary population property.
- **Quality:** Split into measurement property, valuation-model performance, data fitness, and analytic adequacy. One broad quality label would mix distinct judgments.
- **EQ-5D study:** Not retained. It would collapse studies of labels, profiles, utility scoring, trial analysis, and HTA use.

Round 2 also considered but did not retain:

- **Mapped observation:** Not retained as a synonym for an observed response. A mapped value is a derived outcome with a source measure and mapping transformation.
- **Implementation study:** Not retained as an exclusive report class. Implementation can be one activity in a report, and it has a workflow target, methods, properties, and outputs.
- **Health inequality:** Kept as a study purpose and use context. It is not a measurement property of EQ-5D by itself.
- **Best bolt-on:** Not retained as a stable artifact property. Added value depends on the target construct, population, condition, outcome, and number of added items.

Round 3 also considered but did not retain:

- **Report family:** Not retained as a broad publication class. The useful relation is shared source evidence, with the specific dataset, wave, and cohort recorded.
- **Representative dataset:** Not retained as a binary dataset property. Quality controls, quotas, and weighting do not remove all coverage and selection limits.
- **Invalid response:** Not retained as an asserted person-level fact. A bot score, speed threshold, repeated-item disagreement, or author-defined VAS threshold is an operational quality rule with possible classification error.
- **Socioeconomic status:** Not retained as one universal variable. Income, education, employment, perceived income adequacy, and related stratifiers have different meanings and cannot be merged without a study-specific mapping.
- **Overall inequality:** Not retained as one result type. Dimension odds, profile distributions, scored-index gradients, EQ VAS gradients, and inequality indexes use different outcome representations.
- **True health:** Not retained as a latent entity inferred from profile and VAS disagreement. The supplied papers do not identify whether disagreement reflects omitted content, response style, or another mechanism.

## Unresolved cases

### 1. How should representativeness be summarized?

Probability samples, quotas, online panels, snowball recruitment, and mixed recruitment all appear in the batch. A later round can test whether a small set of sampling-evidence terms gives consistent comparisons. For now, applications preserve the recruitment facts and any stated departure.

Round 2 strengthens this unresolved case. The UAE study combines quotas with networks and snowball recruitment in a population that is mostly expatriate (`10.1016/j.jval.2025.01.003`). The Hungarian and three-country studies use quota-selected online panels (`10.1016/j.jval.2024.03.2195`; `10.3389/fpubh.2021.744405`). The ontology still records evidence for coverage and selection. It does not assign one representative or non-representative label.

Round 3 adds probability cluster sampling with differential response, household quota recruitment, mixed online and public-place panels, and 15 country panels with large quota shortfalls in some cells (`10.1038/s41433-023-02860-x`; `10.1186/s12955-024-02266-7`; `10.1186/s12955-024-02323-1`; `10.1007/s11136-025-04074-y`). No short summary term captures these differences. The open case remains.

### 2. What is the best unit for reviews?

One review has publications as its included unit, while another deduplicates publications into trials. The evidence-source concept supports both. A future application must test reports that contain several cohorts or several instruments.

The round-3 comparative review includes 24 publications and permits separate publications from the same data when they report different properties (`10.1007/s40273-018-0642-5`). Research-data lineage now records this overlap, but a synthesis must still choose whether its unit is report, study, dataset, cohort, instrument evaluation, or property estimate.

### 3. How should related but non-equivalent constructs be mapped?

Health status, HRQoL, QoL, wellbeing, capability, and social-care-related QoL overlap but are not synonyms. The current ontology records the authors' construct and any direct framework comparison. It does not impose a universal construct hierarchy.

EQ-TIPS experts disputed whether the target was health, health status, HRQoL, or development (`10.1007/s11136-025-04150-3`). EQ-HWB-S adds wellbeing content to an EQ-5D comparison (`10.1016/j.jval.2024.05.007`). The added evidence supports retention of the open case.

The within-profile inequality paper adds a related problem: EQ VAS can reflect health content outside the five EQ-5D dimensions, response-scale use, or both (`10.1007/s11136-026-04294-w`). The ontology records the reported measures and competing explanations. It does not define one latent true-health construct.

### 4. When does a cultural difference require an instrument change?

The Chinese QoL study identifies *mindset* and several new subthemes but concludes that EQ-HWB remains comprehensive. The ontology can record both overlap and omission. It does not define a threshold that requires a new item or domain.

### 5. How should response-scale comparisons handle confounding?

Frequency and severity can differ in wording, recall needs, response distributions, and trait coverage. The EQ-HWB comparison holds the respondent sample constant but not all semantic features. A future round can test whether the comparison entity needs a standard confounder facet.

Round 2 adds severity-label translation and a comparison of instruments with different recall periods (`10.1186/s41687-025-00985-z`; `10.1016/j.jval.2024.05.007`). Standard alignment facets now capture these differences, but the ontology does not assign a numerical comparability grade.

Round 3 adds a randomized wording-by-perspective design (`10.1016/j.jval.2018.05.002`). It shows that wording and perspective can interact. The design also changes self-versus-other referent with age perspective, so even randomization does not isolate every semantic feature.

### 6. How should value-set usability be separated from model fit?

Logical consistency, coefficient significance, prediction error, theoretical justification, anchor choice, and ethical acceptability can point in different directions. The current ontology keeps them as separate valuation-model properties. It does not calculate an overall rank.

The DCEd study adds agreement with another method and correction for temporal preference (`10.1016/j.jval.2024.05.016`). The UAE study adds cross-validation, mixed language and mode, and a dynamic target population (`10.1016/j.jval.2025.01.003`). These do not supply a general threshold for method interchangeability or value-set usability.

Round 3 shows that a cTTO-only youth model can be statistically feasible, while duration anchor and time-preference assumptions can change a DCE tariff range (`10.1016/j.jval.2023.03.003`; `10.1177/0272989x251325828`). The new Trinidad and Tobago value set is wider than its crosswalk but differs in several design dimensions (`10.1186/s12955-024-02266-7`). No single fit statistic resolves protocol, ethical, transfer, and decision-use questions.

### 7. How should broad conclusions be qualified?

Several papers conclude that an instrument is valid, reliable, representative, or usable while results contain property-level exceptions. Current applications keep the author conclusion and the main qualifier. More rounds must test whether short interpretation terms stay consistent.

### 8. How much instrument structure should be repeated?

The supplied structured records hold bibliographic data but not instrument definitions. Applications record only instrument characteristics needed for a paper's comparisons. A later shared instrument catalog could reduce repetition, but this round does not justify one.

### 9. When is a proxy answer about the person rather than the proxy?

EQ-TIPS experts identify familiarity, developmental expectations, culture, and caregiver spillover as influences (`10.1007/s11136-025-04150-3`). The ontology records the requested perspective and these conditions. It does not give a rule that makes parent, clinician, or other caregiver answers equivalent.

### 10. When can a translated version transfer to another jurisdiction?

Modern Standard Arabic supports communication across countries, but regional dialects, cultural meaning, and local comprehension can differ (`10.1186/s41687-025-00985-z`). Approval of an Egyptian version does not define an automatic boundary for use or validation elsewhere.

### 11. What agreement is enough to treat methods or scores as interchangeable?

Nonlinear DCEd and EQ-VT outputs agree closely in one country (`10.1016/j.jval.2024.05.016`). EQ-HWB-S and mapped EQ-5D-5L scores have high concordance but material individual differences (`10.1016/j.jval.2024.05.007`). The ontology records agreement methods, scale region, and alignment. It does not supply a universal interchangeability threshold.

The immediate-death analysis confirms close population-level agreement for one DCE specification but cannot test individual agreement because different respondents supplied DCE and cTTO data (`10.1177/0272989x251325828`). This supports retention of the open case.

### 12. How far should downstream provenance extend?

The dialysis paper shows a path from responses through mapping and value sets to QALYs and ICERs (`10.1007/s10198-018-0987-x`). The ontology records enough of this path to explain the comparison. It does not yet define whether every economic-model assumption must become part of a measurement application.

The vision paper extends the path through prevalence scaling, disability weights, DALYs, monetization, cost categories, and cost bearers (`10.1038/s41433-023-02860-x`). The ontology records assumptions that materially explain the reported outcome. It still does not require every service unit cost or model parameter.

### 13. When does pilot feasibility support scale-up?

The Ontario study combines strong initial acceptability with 60.6% follow-up completion, staff burden, one site, and language barriers (`10.3390/curroncol32060308`). The ontology separates observed site-level feasibility from a proposed broader implementation. It does not set a completion threshold for scale-up.

### 14. When is an exclusion a quality control rather than removal of meaningful variation?

Bot scores, response-time limits, duplicate checks, and implausible numerical values have operational rationales (`10.1007/s11136-025-04074-y`). The within-profile inequality paper also removes EQ VAS responses below fixed thresholds, although omitted health content is one proposed reason for profile-VAS discordance (`10.1007/s11136-026-04294-w`). The ontology records the rule, affected cohort, and rationale. It does not label all excluded responses invalid or define one universal threshold.

### 15. How should temporal population comparisons separate change sources?

The Trinidad and Tobago norms paper applies the same current value set to profiles from both periods, which removes one scoring difference (`10.1186/s12955-024-02323-1`). Recruitment, mode, survey context, response behavior, and population composition can still differ. The ontology records alignment but does not apportion the observed change among these causes.

### 16. How should inequality representations be compared?

Round 3 uses income-utility regression, dimension-level odds, profile ceilings, scored-index and EQ VAS gradients, and modified Kakwani indexes (`10.3390/curroncol32110645`; `10.1186/s12955-024-02323-1`; `10.1007/s11136-026-04294-w`). Each has a different scale and target. The ontology keeps their provenance and does not define one cross-measure inequality score.

### 17. When should a value set or population norm be updated?

Trinidad and Tobago papers recommend an updated directly elicited value set and new population norms after observed differences across years (`10.1186/s12955-024-02266-7`; `10.1186/s12955-024-02323-1`). The evidence shows that time and methods matter. It does not give a general update interval or threshold.

### 18. How should data quality and representativeness support reuse?

EQ-DAPHNIE provides country-level indicators for authenticity, completion, missingness, consistency, and quota attainment (`10.1007/s11136-025-04074-y`). These indicators can support a use-specific fitness judgment, but no overall quality grade is justified. A variable can be suitable as a covariate in one analysis and too incomplete as an outcome in another.

## Source and metadata issues

- `10.1007/s40273-022-01216-9`: the key-points box states that the sample came from four regions. The abstract and detailed methods state 14 regions or provinces/cities and list them. The applications use the detailed methods and retain the conflict.
- `10.1007/s11136-025-04038-2`: the paper reports subtheme alignment as "68% (18/57)." The fraction is about 32%, not 68%. The intended numerator or percentage is unclear.
- `10.1016/j.jval.2025.02.001`: the supplied YAML record has the DOI, title, license, and conversion provenance but lacks authors, journal, and publication date. The body contains some of this information. In line with the task, the missing structured fields were flagged and not reconstructed.
- The PDF-derived Markdown for `10.1016/j.jval.2025.02.001` contains page furniture and broken line wrapping. The substantive sections were still readable. No scientific value was inferred from missing figures or supplements.
- `10.1016/j.jval.2025.01.003`: the abstract reports a mean age of 39 years, while the main results report 32.1 years. The supplied paper does not resolve the difference.
- `10.1007/s11136-025-04150-3`: the report says that 44 experts were invited, but its three group counts are 21, 13, and 9, which sum to 43.
- `10.3390/curroncol32060308`: the abstract appears to calculate willingness percentages from all 170 enrolled patients and reports `115 (67.3%)`. The results use the 160 feasibility-survey respondents and report `115 (71.9%)`. The intended denominator is unclear, and 115 of 170 is not 67.3%.
- `10.1186/s12955-023-02177-z`: the global change question is described at six months, but the paper does not clearly describe how it selected the stable subgroup for the one-month retest.
- `10.1016/j.jval.2025.01.003`, `10.1016/j.jval.2024.05.016`, `10.1016/j.jval.2024.03.2195`, and `10.1016/j.jval.2024.05.007`: the supplied YAML records omit authors, journal, and publication date. Some article bodies contain some of these data. This lineage record flags the structured-record gap and does not reconstruct the fields.
- The four PDF-derived round-2 Markdown files contain page furniture, split words, and table text in reading order. The main methods, results, and limitations were readable. No result was inferred from omitted supplements.
- `10.3390/curroncol32110645`: the institutional statement gives 17 January 2025 as the approval date, after the reported May-to-November 2024 data collection. It is not clear whether this approval applies to the secondary analysis or whether the date is incorrect for the parent study.
- `10.1016/j.jval.2018.05.002` and `10.1016/j.jval.2023.03.003`: the supplied YAML records omit authors, journal, and publication date. The PDF bodies contain these fields. The conversions contain page furniture and broken line wrapping, but the substantive sections were readable.
- `10.1038/s41433-023-02860-x`: the structured author list contains two entries named `S S Ramsewak` with different affiliations. The body refers to Samuel and Shivaa Ramsewak, so the YAML names are ambiguous.
- `10.1186/s12955-024-02266-7`: the abstract reports 236 negative states, or 7.6%, while the Results report 275 negative states, or 8.8%, from 3,125 states. The correct count is unclear.
- `10.1186/s12955-024-02323-1`: the abstract says that collection ended in May 2023, while the Methods say that the third survey ran through August 2023. The Methods and Table 6 define the income contrast as lowest income, but the Discussion describes higher income as increasing the odds of problems.
- `10.1007/s11136-025-04074-y`: the structured author list contains a malformed concatenated project-team entry followed by repeated individual names. The abstract calls link-click percentages response rates, although it separately reports much lower completion rates.
- `10.1007/s11136-026-04294-w`: the Data Availability statement says that no datasets were generated or analyzed, while the Methods and Results report analysis of 32,327 EQ-DAPHNIE records.
