# Candidate 2 paper-first ontology

Status: consolidated after application and backward review of batches 01, 02, 03, and 04.

## Current ontology and extraction guide

### Scope and record rule

The paper is the main research record. It contains the paper's purpose, semantic study information, products, principal results, and author-reported meaning. Deterministic bibliographic and source facts stay in the JATS layer.

Use subordinate paper-local components only when a phase, sample, evidence source, task, time point, experimental arm, comparison, or analysis must stay separate to answer a user question. Give each component a short local identifier, a type, a status when needed, and a relation to the paper or another component. Do not create a component for each section, table, model, or estimate.

Record paper status as `planned`, `in progress`, `completed`, or `mixed status`. Use `mixed status` when completed and planned components coexist. Also record the status of material components so that a completed pilot does not make a planned scale-up look complete.

### Study-family tags and purpose

Use repeatable study-family tags. The consolidated controlled terms are:

- health-state valuation study;
- value-set development;
- social-priority weighting study;
- instrument development;
- translation;
- cultural adaptation;
- measurement-property assessment;
- qualitative concept study;
- mapping or scoring study;
- population-health study;
- population-norm study;
- implementation study;
- professional-practice survey;
- study protocol;
- research-infrastructure study;
- systematic review or evidence synthesis;
- health economic evaluation;
- cost-of-illness or burden-of-disease study;
- health equity or inequality study;
- methods study.

The tags are not exclusive. Use `methods study` only when a method is a main research target, and name that method in the purpose statement. Do not use it as a substitute for a more specific family. Record design features such as cohort, trial, secondary analysis, product comparison, mixed methods, and feasibility as design or purpose facts. Do not treat them as study-family tags unless a later corpus supplies evidence for a new stable family.

The final terms split four earlier compound labels. A health-state valuation study does not necessarily produce a value set. Translation is different from same-language cultural adaptation. A professional-practice survey is not an implementation study. A study protocol is different from an operational research infrastructure. No assigned primary paper supports a separate `trial or intervention study` family, so that untested term is not in the consolidated list.

Add a concise purpose and contribution statement. A family tag supports retrieval, but it does not replace the statement.

### Paper-level content

For each paper, record:

1. Purpose, contribution, study-family tags, and status.
2. Main concepts, constructs, theories, frameworks, and practical topics.
3. Material components and their relations.
4. Evidence context, instruments, methods, comparisons, products, and provenance.
5. Principal findings, author interpretation, reported implications or documented use, limitations, and stated gaps.
6. Extraction uncertainty, conflicting source statements, and transfer limits.

Use controlled topic tags only when they support cross-paper retrieval. Keep a paper-specific conceptual framework as a structured list or concise narrative. Do not force all themes into a universal theory taxonomy.

### Components, dependencies, and relations

Useful component types are phase, sample or cohort, evidence-source set, experimental arm, survey section, elicitation task, instrument-development task, qualitative data-collection task, analysis stream, comparison, and follow-up or time point.

Useful relations include `part of paper`, `precedes`, `depends on`, `uses sample`, `analyzes data from`, `compares with`, `produces`, `tests`, `anchors`, `derives from`, `reuses`, `updates`, and `supersedes`. Use a harmonization relation only when it names the source variables or scores, the rule, and the harmonized output. Do not use the vague relation `harmonizes with` by itself.

Keep interpretation-changing differences separate. Keep cTTO and DCE tasks separate even when a hybrid model combines them. Keep translation, cognitive testing, and later psychometric testing as linked stages. Keep a review's publications, studies, trials, or data sets separate from the people in those evidence units. Record when a later wave or phase depends on changes from an earlier one and is not independently frozen.

### Evidence context and participant roles

Do not use one broad population field. Keep these roles separate:

- **Evidence supplier:** the person, publication, trial, data set, record, expert, or organization that supplies direct evidence.
- **Respondent:** the person who answers an instrument, interview, survey, or preference task.
- **Referent:** the person or state that the answer describes.
- **Target population:** the population to which the result is intended to apply.
- **Decision context:** the clinical, economic, policy, social-care, research, or instrument-development use.

For each material component, record country and subnational region, task or instrument language, age, health condition, setting, sampling frame and method, recruitment route, principal inclusion and exclusion rules, and the counts that define the evidence flow. Useful count stages are invited or frame, opened, consented, enrolled, completed, quality flagged, excluded, retained, weighted, and analyzed. Always give the denominator for a reported rate. Do not add every small loss when it does not change interpretation.

Separate design or co-design evidence suppliers from routine instrument respondents. A familiarization completion in a workshop is not clinical outcome evidence. Separate a hypothetical child referent from a child respondent and a professional opinion about proxy use from an observed proxy report.

For an observed proxy report, record proxy relation, familiarity when stated, referent, exact instrument version, time point, count, independent or joint completion, and requested perspective. Use `proxy's own assessment of the referent` and `proxy answers as the referent would answer` only when the instrument wording supports them. Cross-informant agreement is not test-retest reliability.

### Instruments, versions, roles, and data forms

Create a repeatable instrument-use entry for each material use. Record the family, exact version and variant, language version, paper-time development or licensing status when material, role, linked component, respondent, referent, recall period when material, administration, and scoring route when used.

Controlled instrument roles are:

- target of development;
- target of valuation;
- target of measurement-property assessment;
- administered measure;
- comparator measure;
- criterion or anchor measure;
- source of health-state descriptions;
- source version for translation or adaptation;
- reference version used to resolve translation choices;
- target of translation or adaptation;
- discussed in a practice survey or review;
- produced instrument version;
- scoring or mapping target;
- source of a score or utility value.

Do not treat an instrument family, descriptive-system version, language version, value set, and score as the same object. For EQ-5D, keep profile responses, EQ VAS, level sum score, mapped or directly scored utility, and QALYs distinct. Do not make an instrument-use entry for a background mention. Record an item, dimension, response label, or scale feature only when it is a research target.

### Administration bundle

Administration is a repeatable bundle. Keep these independent axes:

- reporting perspective: self-report, proxy perspective 1, proxy perspective 2, expert or professional opinion, or other stated perspective;
- contact mode: face-to-face, telephone, postal, remote, or mixed;
- medium: web, app, other digital form, paper, or spoken response;
- interviewer support: none, available for questions, guided, or full interviewer administration;
- setting: home, school, clinic, public place, panel session, or other stated setting;
- platform or protocol technology when it changes delivery, quality control, or reproducibility.

Self-report and interviewer administration can occur together and must not be alternatives on one axis. Record task order, randomization, incentive, training, feedback, tutorial, scheduling, and sequential dyad completion when they affect comparison or quality. When several features vary together, describe a pragmatic administration-package comparison. Do not assign a causal effect to one feature without an identifying contrast.

### General method, design, and quality path

For each material component, record:

`component purpose -> evidence source -> data-collection method -> analytic method -> inference or product`

Use controlled terms for stable method names. Add the exact named method when it changes retrieval or interpretation. `Regression`, `psychometric analysis`, and `qualitative analysis` are too broad when the paper gives the specific model, property, or coding method. Record named guidance only when the paper states that it shaped the work.

For a randomized or crossed design, record assigned factors, allocation, arm, interaction test, and material arm contrasts. Do not summarize interacting factors as independent main effects.

For each material quality rule, record `indicator -> threshold -> timing -> action -> affected records`, and whether the rule came from protocol, pilot evidence, external precedent, or author judgment. Distinguish prevention, a flag for review, automatic exclusion, analytic eligibility, quota action, and tested survey change. A low value, nontrading response, or unusual choice is not automatically invalid.

When uncertainty is a main topic or a material product or result feature, record:

`object -> uncertainty-generating stage -> author-named type -> inherited or generated here -> quantification or handling -> information passed downstream`

Use author terms such as variability, heterogeneity, statistical uncertainty, and methodological variation when supported. Do not turn every limitation, coefficient, or assumption into a separate uncertainty object.

### Health-state valuation and value-set development

For each preference task, record the task form and inferential purpose separately. Current purpose values are `health-state cardinal valuation`, `social-priority weighting`, and `descriptive-system preference test`. A task name does not prove its purpose or product.

For a health-state valuation task, record cTTO, conventional TTO, lead-time TTO, DCE, DCE with duration, VAS, or other task; protocol and version; respondent perspective and referent; state design and blocks; tasks per respondent; duration and death framing; administration; training; quality rules; sample; and analyzed observations.

For DCE with duration, record duration levels, immediate-death tasks, time-preference form, identified parameter, anchoring target, scale transformation, and utility range. Keep duration or zero-duration anchoring separate from immediate-death anchoring. A valuation time-preference parameter is not an economic discount rate.

For experience-based EQ VAS work, record who rates whose health, scale endpoints, death anchoring or its absence, linked profile, clinical group, and time point. An unanchored own-health EQ VAS model is not automatically a QALY-ready value set.

For modeling, record source data for each model, candidate model names, anchor or scale relation, selection criteria, sensitivity analyses, selected model, and any resulting product. Keep cTTO and DCE sources distinct inside a hybrid. Separate a tested candidate tariff or experimental model from a completed operational value set.

### Social-priority weighting

For a Person Trade Off path, record respondent role, recipient groups and ages, attributes held constant, gain type and duration, starting group sizes, search method, equivalence or forced-choice form, extreme or nontrading rule, derived weight, consistency test, and randomized presentation factors. A social-priority weight is not a health-state utility, disability weight, QALY, or value set.

### Measurement-property assessment

Record the exact property and target. Current properties include:

- feasibility and missing responses;
- distribution, ceiling, and floor effects;
- test-retest reliability and measurement error;
- content validity, with relevance, comprehensibility, and comprehensiveness kept separate;
- construct validity, including convergent validity and hypothesis testing;
- known-groups or discriminative validity;
- responsiveness and minimal important difference;
- response-scale informativity;
- item discrimination, thresholds, and differential item functioning;
- severity-preference concordance and attribute-level decision relevance for preference-based instrument tests;
- cross-informant agreement.

The target can be an instrument, item, score, value set, elicitation task, or full method. Record the inference unit when results can differ at task-response, personal-function, subgroup-tariff, or aggregate-value-set level. Link the property to the comparator or criterion, population or subgroup, time points, statistic, decision rule, and scoped result.

For responsiveness, record direction, interval, transition anchor, group rule, group count, statistic, and interpretation rule. Evidence for deterioration does not prove responsiveness to improvement. Keep cross-informant agreement separate from repeated measurement by the same informant.

### Instrument development, translation, adaptation, and qualitative concepts

Record each material stage, input, participant task, decision rule, language, and output. Useful stage terms are concept or item generation, wording or label generation, sorting or response scaling, cognitive interview or comprehension test, translation, cultural adaptation, harmonization, psychometric test, valuation, and proxy-version development.

For translation or adaptation, keep source version, reference version, and target version separate. Record translator direction and independence when applicable, reconciliation, governance review, cognitive test, response-order task, proofread, and stage-specific change. Same-language localization is cultural adaptation, not translation.

For qualitative concept or content-validity work, record the conceptual starting point, sampling, interview or group method, language, coding method, number of coders, inductive and deductive use, comparison framework, saturation rule or observation, and scoped inference. Do not transfer results to an untested instrument part, value set, or property. Keep themes as a structured product or concise summary and do not treat mention frequency as importance unless the paper does.

### Scoring, mapping, and economic evaluation

For each analyzed score, record:

`instrument and version -> response or profile -> scoring, mapping, or aggregation -> value set or algorithm -> analytic outcome`

Keep direct utility scoring, direct mapping to utility, response mapping to a profile, crosswalk between versions, unweighted level sum score, EQ VAS, and a different instrument's utility separate.

For a direct-versus-derived product pair, record both derivation paths, country, wording, preference-data period, protocol, population, mapping algorithm, and whether samples are shared, parallel, or independent. Record matched and unmatched conditions. High correlation does not prove interchangeability.

For a health economic evaluation, record intervention, comparator, clinical or model population, model form, perspective, horizon, utility source and score path for each state, QALY and ICER contrast, uncertainty method, and decision implication. Mapping transport must preserve the development sample, source instrument, target version, value set, and application sample.

### Population health, norms, equity, practice, infrastructure, and implementation

For population-health surveys, practice surveys, and research infrastructure, record the survey target, frame, quota or representativeness method, sections, mode bundle, ordering, language adaptation, quality checks, and closed- and open-response analysis. Distinguish a completed health measure from an instrument that a professional survey only discusses.

For population norms, record reference period, exact instrument and language version, score forms, scoring product, population basis, source samples, principal strata, and update relation. Rescoring old profiles with a later value set is harmonization and reuse, not new response collection.

For material socioeconomic or equity variables, record construct, observed question or source, category or harmonization rule, analytic role, reference group, and linked component. Useful roles are exposure, stratifier, quota variable, adjustment variable, inequality-ranking variable, and decomposition factor. For a conditional comparison, record what is held constant. An identical EQ-5D profile does not prove identical underlying health.

For implementation, record target, stage, site scope, workflow position, eligible and participating counts, repeat completion, acceptability, staff burden, barriers, facilitators, tested changes, and planned scale. Controlled implementation stages are `proposal`, `pilot`, `limited routine use`, and `scaled routine use`. A successful pilot is not routine use.

For a clinical PROM workflow, record:

`completion trigger -> self or proxy form -> medium and system -> score or displayed data -> recipient -> review responsibility -> flag rule -> discussion or action path`

Keep workshops, feedback, prototype, mock test, clinical pilot, and routine use separate. A mock-tested prototype does not prove adoption, clinical action, or patient benefit.

### Systematic reviews and evidence syntheses

Record databases and other sources, search period, eligibility logic, screening, duplicate handling, evidence-unit type and count, extraction, synthesis, and quality appraisal or the stated reason for its absence. Preserve publication, study, trial, and data-set cardinality when the review distinguishes them. Do not call evidence units participants. At review level, use `various or not consistently stated` for context that cannot be supported without reconstructing every included study.

### Cost of illness and burden of disease

Record condition and severity definition, prevalence or incidence basis, reference year, population, perspective, cost categories and bearers, resource and unit-cost sources, productivity method, health-loss measure, extrapolation, currency and price year, uncertainty analysis, and excluded categories. Keep direct medical, direct non-medical, productivity, informal care, transfer payment, dead-weight, and intangible effects separate when material. Keep DALYs, QALYs, disability weights, utilities, and monetized wellbeing loss distinct.

### Comparisons, reuse, and harmonization

Create a comparison entry when a contrast is part of purpose, method, or principal interpretation. Record objects, purpose, difference dimensions, evidence source, paired or independent design, conditioning rule, result, and transfer limit. Useful dimensions are version, language, response scale, task, population, respondent, referent, time, mode bundle, score route, value set, model, country, condition, and source.

Record explicit reuse of a sample, data set, protocol, value set, mapping function, model, or framework. Types include reanalysis, extension of design or protocol, use of scoring product, product comparison, duplicate reports from one study or trial, and derivation from pooled external data. Name the object when possible. Do not infer reuse from authors or settings. For pooled sources, retain source-specific sample, period, mode, order, variable definition, and quality exclusions. Record overlap as documented absent, documented present, possible, or not stated only when the paper supports that assessment.

### Products and state axes

Create a product entry only for an output that researchers can seek or reuse. Product types are value set; instrument or instrument version; language version; mapping function or scoring model; conceptual framework; protocol; data set or research infrastructure; population norms; implementation workflow or resource package; reporting or analysis guidance; and research-priority set.

Record product name, type, linked instrument, version or date, country or language, population basis, producing component, intended use, and these independent state axes when supplied:

- **Development state:** proposed concept, draft or prototype, completed named output of the reported process, or ongoing resource.
- **Evidence state:** name the actual evidence, such as technical pilot, cognitive interview, content-validity assessment, psychometric test, valuation, mock workflow test, or external validation. Do not use `tested` alone.
- **Governance state:** experimental, reviewed, endorsed, or approved, with the body named when stated.
- **Availability and access:** available, restricted, licensed, unavailable, or not stated.
- **Recommendation and use:** author-recommended, documented research use, documented routine use, or documented effect.
- **Implementation stage:** proposal, pilot, limited routine use, or scaled routine use, when applicable.

Do not use `established`, `validated`, or one generic maturity ladder without an explicit meaning. A final translation can have cognitive evidence but no psychometric or valuation evidence. A completed national value set can be author-recommended but have no documented decision effect. Tie every state to the paper's version, time, and context.

### Findings, meaning, and source uncertainty

Keep these sections separate:

- **Principal findings:** main empirical or methodological results.
- **Author interpretation:** what the authors say the findings mean, including competing explanations that the design cannot separate.
- **Reported implications or documented use:** scientific, clinical, practical, policy, implementation, or instrument-development. Label author-reported implications and distinguish them from documented use or effect.
- **Limitations and transfer limits:** author-reported limits plus extractor-noted scope and source conflicts.
- **Stated gaps and future work:** only author-stated gaps and plans.

Do not infer scientific, policy, or social impact. Do not convert one paper's future work into a corpus gap. Keep only decisive estimates that define a product, sample flow, comparison, or main inference.

For irreconcilable source statements, use one primary conflict type: `count or arithmetic`, `scope or geography`, `definition or denominator`, or `summary versus main text`. Name the locations, keep the minimum conflicting values, explain the extraction choice, and do not silently repair the source. A threshold-boundary problem can use `definition or denominator` with local detail.

## Applications to batch 01

### 1. 10.1007/s40258-021-00639-3 — Danish EQ-5D-5L value set

**Classification and purpose.** Health-state valuation study and value-set development; completed. The paper develops the first Danish EQ-5D-5L value set from adult general-population preferences and selects a model that combines cTTO and DCE data. Topics include health utility, QALYs, Danish priority setting, preference elicitation, anchoring, heteroscedasticity, censoring, and value-set transferability.

**Components.** `S1 recruitment and interview sample` supplies respondents to `T1 cTTO` and `T2 DCE`. `A1 cTTO modeling`, `A2 DCE modeling`, and `A3 hybrid modeling` analyze those tasks. `A4 sensitivity analysis` restores cTTO states rejected in the feedback module. `C1 Danish value-set comparison` compares the product with the Danish EQ-5D-3L value set and the Danish 5L crosswalk.

**Evidence context.** Respondents were adults older than 18 years from the Danish general population. The respondent and referent were the same person only for the initial self-reported EQ-5D-5L and EQ VAS. For valuation tasks, adult respondents valued hypothetical EQ-5D-5L states. The target population for preferences was the Danish adult general population. The decision context was QALY estimation and Danish health-care priority setting, with a stated use for assessment of hospital-dispensed medicines. Statistics Denmark first supplied a random sample that was balanced by age, gender, education, and region. A market-research panel later supplemented recruitment under the same representativeness targets. There were 1,052 interviews. The analysis retained 1,014 after stated interviewer, software, withdrawal, cognitive or emotional, and incomplete-task exclusions.

**Instruments and administration.** EQ-5D-5L was the target of valuation, the source of health-state descriptions, and an administered self-report measure. EQ VAS was also self-reported. The valuation used EQ-VT version 2.1 in computer-assisted personal interviews. Respondents valued ten cTTO states and seven DCE pairs. cTTO used conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states. DCE used pairwise states without duration. The EQ-VT design covered 86 cTTO states and 196 DCE pairs in randomized blocks. Interviewer training, the EQ-VT quality-control tool, fortnightly review, and the cTTO feedback module were material protocol controls.

**Method path.** cTTO candidate models were a generalized least-squares random-intercept model and a random-effects Tobit model. DCE candidate models were conditional logit and heteroscedastic conditional logit. Hybrid candidates combined DCE conditional logit with either the GLS or Tobit path. The hybrid path used a multiplicative scale parameter to link DCE and cTTO coefficients. Model selection used logical consistency and, where suitable, model fit. The paper did not use AIC or BIC to compare a hybrid model with its constituent likelihoods. A sensitivity analysis restored 712 cTTO states that respondents had marked as incorrectly ranked. The final model was the heteroscedastic censored hybrid model.

**Comparison and reuse.** The paper compared the new directly elicited 5L value set with an earlier Danish 3L value set and a crosswalk value set derived by mapping pooled 3L and 5L data from six countries. This is product comparison and external scoring-method provenance, not sample reuse in the new valuation.

**Product and states.** `Danish EQ-5D-5L value set`; completed named national value set and author-recommended for Danish use. Its evidence is the reported cTTO and DCE valuation and model-selection study. It assigns values to all 3,125 states, has a reported range of -0.757 to 1, and uses the Danish adult general population basis. Availability and downstream use are not documented in this paper.

**Principal findings.** Only the heteroscedastic censored hybrid model removed logical inconsistencies in the candidate models. Anxiety/depression had the largest decrement, followed by pain/discomfort. The worst state value was lower than in the Danish 3L and crosswalk products. The final sample was close to national population distributions, but it had somewhat more highly educated respondents.

**Author interpretation and implications.** The authors attribute data quality to the detailed standard protocol, interviewer training, and continuous quality control. They recommend the new 5L value set for Danish QALY estimation and health-care prioritization. This is an author-reported policy and implementation implication. The paper states an expected use; it does not document a downstream policy effect.

**Limitations and gaps.** Recruitment source changed during collection, young adults and people with low education were somewhat under-represented, and DCE anchoring still depends on the hybrid scale relation. The authors call for more work on the utility-theory basis of hybrid models and on alternatives such as DCE with duration. The language version of EQ-5D-5L is not stated explicitly enough in the methods for a verified language-version value.

### 2. 10.1007/s11136-020-02688-y — review of EQ-5D-5L psychometric properties

**Classification and purpose.** Systematic review or evidence synthesis and measurement-property assessment; completed. The paper summarizes published evidence on EQ-5D-5L distribution, feasibility, reliability, validity, and responsiveness and identifies knowledge gaps.

**Components.** `R1 literature identification and screening` produces `E1 included publications`. `A1 distribution synthesis`, `A2 reliability synthesis`, `A3 validity synthesis`, and `A4 responsiveness synthesis` analyze different property families. The review also pools full-health proportions, mean index values, and correlations.

**Evidence context.** The direct evidence suppliers were 99 included publications from 32 countries. They were not 99 human participants. The included papers covered adult general populations and many patient populations, with musculoskeletal or orthopedic disease and cancer as the most common condition groups. The review excluded studies of people younger than 18 years, non-English and non-German publications, experimental 5L versions, and papers that did not assess measurement properties. The target context was use and interpretation of EQ-5D-5L across populations, settings, and applications.

**Instrument scope.** The official EQ-5D-5L descriptive system was the target of measurement-property review. The review did not focus on EQ VAS because the version used in source studies was often unclear. Other HRQoL, clinical, functional, pain, life-satisfaction, and cognition measures served as comparators in source studies. Instrument language versions and value sets varied across the evidence and were not consistently extractable as one value.

**Review method.** The authors searched MEDLINE, PsycINFO, EMBASE, and the EuroQol website with updates through January 2019. Two reviewers independently screened titles, abstracts, and full texts, with senior adjudication. Data extraction used predetermined tables. The review treated multiple papers from one underlying data set as one source for duplicated quantitative data. Random-effects models with inverse-variance weights pooled selected outcomes. Correlations used Fisher z transformation, and proportions used logit transformation. Heterogeneity prevented broader pooling.

**Measurement-property path.** Feasibility used missing responses. Distribution used floor and ceiling results and the proportion in state 11111. Reliability used test-retest ICC for index values and kappa for dimensions. Validity was separated into content, construct, convergent, and known-groups evidence. Responsiveness used effect sizes, standardized response means, anchors, and minimal important differences when available.

**Principal findings.** Missing responses and floor effects were usually not problematic. Index scores had good test-retest reliability, but individual dimensions were less stable. Index values and dimensions generally had moderate to strong relations with global health, other multi-attribute utility measures, physical or functional health, pain, activities of daily living, and clinical measures. Relations with life satisfaction and cognition or communication were weak. Responsiveness evidence came from only 15 studies and was heterogeneous, though studies usually reported acceptable response to improvement.

**Author interpretation and implications.** The authors conclude that EQ-5D-5L is a reliable and valid generic health-status instrument across many populations and settings. They warn that general-population ceilings remain consistent with the instrument's focus on health problems rather than positive health. They suggest use of condition-specific measures with EQ-5D-5L when its content is not sufficient. These are author-reported scientific and measurement implications.

**Limitations and gaps.** The review excluded experimental versions and application papers that did not explicitly test measurement properties. It did not review valuation methods, even though value-set choice can affect index results. The evidence was concentrated in Western Europe, OECD countries, and East Asia. The authors call for rigorous responsiveness work, suitable anchors and MIDs, tests in additional regions, and tests in specific settings such as clinical practice and health surveillance.

**Source uncertainty.** The abstract reports 889 identified publications. The main results report 496 initial papers plus 397 update papers, which totals 893. Keep this as a conflicting source count. Do not silently select one value.

### 3. 10.1007/s11136-025-03983-2 — EQ-DAPHNIE infrastructure and survey design

**Classification and purpose.** Study protocol, research-infrastructure study, population-health study, and methods study; mixed status. The paper describes a standardized multi-country infrastructure for representative population health data and instrument evaluation. It reports completed pilot and country rounds and planned expansion.

**Components.** `P0 UK pilot` precedes `R1 five predominantly English-speaking countries` and `R2 ten countries with language adaptation`. Future rounds are planned. `S1 social determinants`, `S2 health and wellbeing`, `S3 health behaviors`, and `S4 health services and insurance` are survey sections. `V1 response-scale heterogeneity vignette` follows self-completed EQ-5D-5L. `Q1 quality assurance` includes pretests, a soft launch, attention to duplicate access, repeated age and marital-status items, and quota monitoring.

**Evidence context.** Respondents were adults aged at least 18 years in online research panels. They reported their own health and context. For the anchoring vignette, each respondent described hypothetical Alex, who was framed as the same age and background. Target populations were the adult general populations of each country. The intended context was cross-country population health assessment, health inequality analysis, population norms, and instrument evaluation.

The pilot was in the United Kingdom with 3,012 completed responses. Round 1 covered Australia, Canada, New Zealand, the United Kingdom, and the United States. Round 2 covered Argentina, Brazil, Chile, China, France, Germany, Japan, Mexico, the Netherlands, and Spain. The target was 4,500 completed responses per country. Reported completed samples were close to or above this target. Quotas used age, sex, household income, area of residence, and language where needed. Sampling used Dynata panels with first-come enrollment within quota strata. The design planned post-stratification weights. People without internet access were outside the effective frame.

**Instruments and administration.** Respondents completed EQ-5D-5L and EQ VAS, selected EQ-5D-5L bolt-ons, EQ-HWB, PROMIS-10, ASCOT SCT4, ICECAP-A, WHO-5, OPQOL-brief for people aged 65 years or older, PHQ-2, and GAD-2. The bolt-on pool included vision, hearing, breathing, sleep, tiredness, social relationships, cognition, skin irritation, and self-confidence. These were administered measures for population assessment and instrument comparison. EQ-5D-5L also supplied the response form for the Alex vignette.

The medium was LimeSurvey on the web, with self-report through a Dynata panel session. EQ-5D-5L came before the vignette. Other standardized measures were randomized. Some questions were conditional. No response was mandatory. The team used available official translations for standardized measures. Other survey content was translated into Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German and reviewed by native speakers or local researchers.

**Method and status.** The program used a cross-sectional design, a modified Delphi process for country, sample-size, measure, and variable choices, country-specific quota sampling, pretests, a 250-response soft launch, and six-week field periods. The paper does not report the planned instrument-comparison models. Record this as a design and infrastructure paper, not as a completed measurement-property result paper.

**Products and states.** `EQ-DAPHNIE standardized survey protocol` is a completed named protocol used in the pilot and completed country rounds. `EQ-DAPHNIE multi-country data infrastructure` is an ongoing research resource. Completed country data exist, but access is restricted to EuroQol members or collaboration with a member. Population norms or comparative estimates are potential later products, not outputs completed in this paper.

**Principal findings and author interpretation.** The paper's result is the operational design and completion of the pilot and first two rounds, not a population-health estimate. The authors state that standardized collection, broad instrument coverage, and large quota samples can support comparable population health and instrument research.

**Limitations, implications, and gaps.** The authors report internet-coverage and panel-selection bias, possible cultural differences in measure function, and the limits of cross-sectional data. They propose tests of other sampling and collection methods, longitudinal follow-up, serial panels, and expansion to Africa, the Middle East, and more of East Asia. These are author-reported research and infrastructure implications. Do not treat planned country coverage or future norms as completed impact.

### 4. 10.1017/s0266462326103602 — global survey of HTA practitioner needs

**Classification and purpose.** Professional-practice survey and methods study; completed. The paper examines HTA practitioners' use of and views about HRQoL instruments, preference methods, data sources, data quality, and research needs for QALY-based cost-effectiveness evidence.

**Components.** `S1 professional sample` supplies `Q1 closed survey sections` and `Q2 open-ended responses`. Closed sections cover utility instruments, elicitation methods, preference-data sources, data quality and appropriateness, and research priorities. `A1 descriptive country and region analysis` and `A2 qualitative content analysis` use different data forms.

**Evidence context.** Evidence suppliers were individual HTA personnel and advisers, not official agency representatives. Invitations used purposive professional networks and country recruiters. The survey reached 49 of 60 approached countries and received 238 completed responses from 45 countries and 65 agencies. Most respondents worked in the public sector, and 213 had QALY-related duties. Results were grouped into Commonwealth, Western Europe, Central or Eastern Europe, Asia, Latin America, and Middle East or Africa regions. The intended use was research planning and better HRQoL evidence for HTA.

**Instrument and method roles.** EQ-5D, SF-6D, EQ-5D-Y, EQ-HWB, bolt-ons, PROPr, and other measures were topics in a professional-practice survey. They were not HRQoL instruments administered to measure respondent health. TTO, VAS, standard gamble, DCE, and other preference methods were also discussed practices, not tasks completed by the practitioners in this study. This role distinction prevents false retrieval as a direct valuation study.

**Administration and analysis.** Participants completed an anonymous English Qualtrics web survey. They could answer open questions in another language; the team used forward and backward translation for non-English answers. Closed questions used four-point frequency responses. The analysis first summarized each country with a mode or median, then summarized regions with the median of country results. Research priorities used respondent, country, region, and global importance scores. Open responses used structured content analysis with iterative coding and categories.

**Principal findings.** EQ-5D was the most frequently reported utility instrument. SF-6D and EQ-5D-Y followed. TTO, VAS, and standard gamble were the most frequent elicitation methods. Many regions used general-public preference data from other countries more often than local public data. Frequent data-quality problems included poor sample representativeness, small utility samples, mismatch with cost-effectiveness model needs, and mixing instruments or elicitation methods. Global priorities were recent tariffs, child and adolescent instruments, and instruments that cover health and social care. Priorities differed by region.

**Author interpretation and implications.** The authors interpret the results as evidence that practice usually follows guidance but that data scarcity leads to suboptimal use. They advise closer HTA stakeholder involvement in instrument and method development, work on pediatric measures, more recent and local utility data, systematic collection of HRQoL data, and regulated data repositories. These are author-reported research, implementation, and policy implications. The survey does not document adoption of a new method.

**Limitations and transfer limits.** Some countries had fewer than three respondents. The team could not identify one ideal respondent type or verify eligibility. EuroQol professional networks may over-represent people who know or favor EuroQol instruments. Recruitment was by country, not by agency, and respondents gave personal rather than official views. The study was not powered for detailed subgroup tests. Keep regional findings as practitioner-sample findings, not formal agency policy.

**Product and states.** The ranked research-priority set is a completed output of the reported professional survey. It is not a consensus guideline or an instrument product, and the paper does not document adoption.

### 5. 10.1007/s11136-019-02115-x — development of EQ-5D-Y-5L

**Classification and purpose.** Instrument development; completed. The paper develops a multilingual five-level youth descriptive system, harmonizes the language versions, and tests comprehension, feasibility, and preference against a four-level alternative.

**Components.** `P1a label generation` uses a review of child HRQoL instruments, dictionaries, thesauruses, and focus groups. `P1b sorting and response scaling` tests labels with 255 children. `P1c draft construction` produces language-specific 4L and 5L versions. `P2 cognitive testing` compares the drafts with 120 children. `H1 cross-language harmonization` compares German, Spanish, Swedish, and UK English versions and produces the final language versions.

**Evidence context.** Respondents were children and adolescents aged 8 to 15 years in Germany, Spain, Sweden, and the United Kingdom. Phase 1 used school and community convenience samples. Phase 2 included healthy children and children receiving treatment in Germany, Spain, and Sweden. The UK phase 2 sample included schoolchildren only. Phase 1 had 255 sorting or response-scaling interviews, with 59 to 72 per country. Phase 2 had 33 German, 35 Spanish, 32 Swedish, and 20 UK participants. The target population was children and adolescents who self-report health with EQ-5D-Y.

**Instrument roles.** EQ-5D-Y-3L was the source instrument and comparison baseline. Draft EQ-5D-Y-4L and EQ-5D-Y-5L were development targets and cognitive-test instruments. Final German, Spanish, Swedish, and UK English EQ-5D-Y-5L self-report versions were products. Existing generic and condition-specific child HRQoL measures supplied possible response labels; they were not comparators in a psychometric study.

**Development method.** Phase 1 generated labels that described intensity or amount of problems and excluded frequency terms. Focus groups elicited child-friendly language and tested understanding. Children aged 8 to 10 used a five-face sorting scale. Those aged 11 to 15 used a VAS response-scaling task. All participants rated all candidate labels for each dimension, with randomized dimension and label order. Quantitative selection used target positions, agreement of median and mode, and small dispersion. Qualitative comments resolved close choices. Phase 2 used cognitive interviews, paraphrasing, and probes. Draft order varied. The UK used group review of the 5L draft only. Harmonization allowed nonliteral wording when field evidence supported a natural local term.

**Comparison.** The main comparison was 4L versus 5L comprehension, feasibility, and participant preference. In Germany, Spain, and Sweden, 66% to 88% preferred 5L because it gave more precise choices and a middle category. The study also compared severity meanings across four languages. It did not assume word-for-word translation equivalence.

**Product and states.** `EQ-5D-Y-5L self-report descriptive system` and German, Spanish, Swedish, and UK English versions; completed named outputs of the reported development process. The evidence is label scaling, cognitive testing, comprehension, feasibility, and preference comparison. Psychometric assessment, valuation, and proxy-version development were still needed. UK English was intended as the source for more translations. Availability, licensing, and routine use are not documented here.

**Principal findings.** The work generated 233 initial labels and found that children as young as eight could perform the label tasks. The five-level version was generally easy to complete and preferred to the four-level version. Some Spanish labels changed after cognitive testing. The UK changed the most severe pain and emotion wording from `terrible` to `extreme` after additional child interviews.

**Author interpretation and implications.** The authors state that direct input from children enabled age-appropriate wording and that five levels can provide more precise reporting than three levels. They expect better sensitivity and continuity with the adult 5L version, but they do not claim that these improvements were proven. This is an author-reported instrument-development implication.

**Limitations and gaps.** Samples were convenient and not nationally representative. Recruitment of children with health conditions was difficult. Country procedures differed slightly, especially in the UK. The authors call for psychometric tests in languages and conditions, comparison with EQ-5D-Y-3L, valuation research, and proxy-version development.

### 6. 10.1007/s40273-022-01216-9 — Chinese EQ-5D-Y-3L value set

**Classification and purpose.** Health-state valuation study, value-set development, and methods study; completed. The paper estimates a Chinese EQ-5D-Y-3L value set under the international protocol, expands the cTTO design, and compares mapping with joint hybrid modeling.

**Components.** `S1 DCE sample` and `S2 cTTO sample` are independent adult general-population samples. `T1 DCE` supplies relative preference data. `T2 cTTO` supplies anchored preference data. `A1 mixed-logit plus mapping` models DCE and uses cTTO for a later OLS scaling step. `A2 main-effects hybrid` models both sources jointly. `A3 hybrid with All-3 term` adds a term for state 33333. `C1 model evaluation` compares significance, monotonicity, and cTTO prediction error.

**Evidence context.** Respondents were Chinese adults, but the referent was a hypothetical 10-year-old child whose relation to the respondent was not fixed. The target population and decision context were child and adolescent health states, pediatric economic evaluation, and Chinese HTA. Quotas covered gender, age, education, and rural or urban registered residence. Recruitment used nonprobability snowball and purposive methods in 14 provinces or cities across five geographic parts of China. The full sample had 1,476 respondents: 1,058 completed DCE and 418 completed cTTO. cTTO collection covered eight regions, while DCE had broader coverage.

**Instrument and administration.** EQ-5D-Y-3L was the target of valuation and source of health-state descriptions. Respondents also reported health with EQ-5D-Y-3L as part of the interview, but this self-report use was not the source of the value set. EQ-VT delivered face-to-face, one-to-one, computer-assisted personal interviews. DCE respondents completed one block of 15 pairs from 150 Bayesian-efficient pairs. The design used two-dimension overlap and did not include a dominance or retest pair. cTTO respondents completed practice tasks and one block of ten states. The expanded cTTO design had 28 states in three blocks, with 33333 in every block.

**Protocol and quality control.** The study extended the international EQ-5D-Y-3L valuation protocol from ten to 28 cTTO states. Eight cTTO interviewers had a two-day workshop, practice interviews, quality reports, and feedback under the EuroQol protocol. DCE interviewers had a two-hour online workshop, but the paper did not apply the same DCE collection quality control.

**Modeling path.** The mapping path fit a correlated-coefficient mixed logit model to DCE, predicted latent health-state values, and used OLS against observed cTTO means to rescale the DCE coefficients. The joint path fit heteroscedastic hybrid models to DCE and cTTO. Candidate forms included a main-effects model and a hybrid model with the `All 3` or `A3` term for state 33333. Selection used coefficient significance, monotonicity, and mean absolute prediction error for 28 cTTO states. The A3 hybrid had no inconsistent or nonsignificant coefficients and the lowest error.

**Product and states.** `Chinese EQ-5D-Y-3L value set`; completed named national value set and author-recommended for Chinese pediatric utility scoring and economic evaluation. Its evidence is the reported adult valuation of hypothetical child health and hybrid model with an A3 term. Availability and downstream use are not documented here.

**Principal findings.** The mean observed cTTO value ranged from 0.924 for 11112 to -0.088 for 33333. State 33333 was the only state with a negative mean, and there was a large gap to the next-worst state. The selected hybrid predicted 33333 at about -0.089 and represented the gap better than the mapped DCE or main-effects hybrid models. DCE and cTTO implied different rank positions for some dimensions.

**Author interpretation and implications.** The authors state that the expanded cTTO design let the hybrid model use more of the observed data and handle the 33333 gap. They recommend the product for Chinese pediatric economic evaluation. They also warn that adult valuation of child health can produce high values and different dimension priorities from adult EQ-5D valuation. These are author-reported methodological and policy implications.

**Limitations and gaps.** cTTO covered only eight regions. The hypothetical child's relation to respondents was unspecified. The DCE design omitted 33333 and could not test the gap directly. The authors call for tests of lag-time TTO, DCE designs that include 33333, reasons for the value gap, effects of child age and respondent relation, adolescent preferences, and an updated valuation protocol.

**Source uncertainty.** The abstract and main methods state 14 provinces or cities and list five geographic parts. The key-points box says four regions. Store the listed 14 jurisdictions and five parts as the detailed method statement, but retain the key-points statement as a source conflict.

### 7. 10.1007/s11136-025-04003-z — frequency and severity scales for pain and discomfort

**Classification and purpose.** Measurement-property assessment and methods study; completed. The paper compares frequency and severity response scales for EQ-HWB pain and discomfort items and examines whether the scale types supply distinct information across health conditions.

**Components.** `D1 existing caregiver-care-recipient survey data` supplies `S1 individual analysis sample`. `A1 correlations`, `A2 Shannon informativity`, `A3 graded response IRT`, `A4 scale-type DIF`, and `A5 condition associations` are linked analysis streams. The caregiver and care-recipient dyads remain a sampling relation, but the analyses focus on individual item responses.

**Evidence context and reuse.** This is an explicit reanalysis of existing cross-sectional data. The sample had 1,008 adults: 504 unpaid caregivers and their 504 adult care recipients. Caregivers had provided care to an adult relative or friend for at least six months, and recipients confirmed the care relation. Respondents reported their own health conditions and completed their own instrument sequence. The target context was generic HRQoL measurement across a range of conditions. The methods section does not state the study country. U.S. institutions and an earlier cited U.S. caregiver study do not provide enough direct method evidence to store `United States` as a verified country for this analysis.

**Instrument roles and administration.** The experimental 25-item EQ-HWB profile was the target of item-level measurement-property assessment. EQ-HWB-S was a shorter nine-item classifier embedded in the long measure and was still being finalized. The exact targets were pain frequency, pain severity, discomfort frequency, and discomfort severity. EQ-5D-5L pain or discomfort was a comparator item. EQ-5D-5L and EQ-HWB recall periods differed: `today` and `last 7 days`. CarerQoL, CARE-2B, and other caregiver measures were collected in the source survey but were not targets in this analysis.

Data collection used a Qualtrics caregiver panel and sequentially linked web self-report. Each dyad completed one session without discussion. Instrument order was randomized. Quality checks used attention checks and a minimum completion time.

**Measurement-property path.** Spearman correlations assessed association among five pain or discomfort items. Shannon H and J measured absolute and relative informativity. A graded response model estimated item discrimination, four thresholds, item curves, and item information on a common latent construct. A logistic ordinal regression and IRT hybrid treated frequency as the reference scale and severity as the focal scale to test uniform and nonuniform differential item functioning. Separate ordinal logistic models related four EQ-HWB items to age, gender, and self-reported condition groups. This exact path is needed because `psychometric analysis` would hide the distinct inferences.

**Principal findings.** Pain frequency and severity had a strong correlation, and all pain or discomfort items were strongly related. Frequency scales used response categories more evenly and were more informative. Severity items discriminated better at higher trait levels. Frequency items were more sensitive at mild to moderate trait levels. Pain showed material scale-type DIF, while discomfort did not. Several condition groups had different associations with frequency and severity responses.

**Author interpretation and implications.** The authors interpret frequency and severity as complementary features, especially for pain. They suggest both scale types for a longer instrument. They suggest frequency when a short instrument needs broad informativity, but note that severity can have advantages for high-intensity clinical use, valuation, and international use. They also explain that condition-specific scale forms would require multiple value sets and reduce cross-condition comparability. These are author-reported measurement and instrument-development implications. No revised instrument was produced.

**Limitations and gaps.** Cross-sectional data do not support causal inference. Conditions were self-reported. Cultural and language transfer needs replication. Recall period differs between EQ-HWB and EQ-5D-5L and can affect the comparison. The authors call for tests across clinical populations, cultures, languages, and recall periods.

### 8. 10.1007/s11136-025-04038-2 — Chinese lay quality-of-life framework and EQ-HWB content validity

**Classification and purpose.** Qualitative concept study and measurement-property assessment; completed. The paper develops a health and wellbeing quality-of-life framework from Chinese lay accounts and compares it with the EQ-HWB framework. The assessed content-validity aspect is comprehensiveness, not relevance or comprehensibility.

**Components.** `P0 two pilot rounds` tests and changes the interview guide. `S1 healthy participants`, `S2 patients`, and `S3 informal caregivers` each have ten participants. `T1 semi-structured interviews` supplies `A1 transcript coding and framework development`. `C1 framework comparison` compares the Chinese framework with EQ-HWB at theme and subtheme levels.

**Evidence context.** Thirty Chinese adults from two regions took part under quota sampling. Quotas covered age, gender, education, health conditions, caregiver experience, and rural or urban registered residence. The sample included ten healthy people, ten patients, and ten informal caregivers. At least 15 were older than 45 years, and no more than 12 had university-level education. Recruitment used community advertisements. Interviews took place face to face in quiet public settings. The respondent described their own view of quality of life, with examples that could include other people. The target context was EQ-HWB use with healthy people, patients, and carers in China.

**Language and instrument role.** Experts developed the guide in English. The team translated it into Chinese and changed `poor well-being` to `quality of life` after six pilot interviews because the first term had an unsuitable positive meaning in Chinese. Formal interviews and analysis were in Chinese, and transcripts were verbatim Simplified Chinese. EQ-HWB and its 96 candidate items supplied the deductive starting codebook and the comparison framework. EQ-HWB was the target of content-validity assessment, not a comparator score in a quantitative test.

**Qualitative method path.** One interviewer conducted all interviews. Two trained coders read transcripts line by line and used both deductive and inductive codes. Supervisors resolved disagreements. The team removed codes under five stated outcome-focused rules, grouped codes into subthemes and themes, charted them, and compared the final structure with EQ-HWB. The analysis reduced 221 initial codes to 187 retained codes. The authors report thematic saturation in the last interviews, but they did not set a prospective saturation rule.

**Product and states.** `Chinese lay quality-of-life conceptual framework`; completed named output of the qualitative analysis, with evidence from this 30-person sample. It has eight themes: feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. It is a conceptual research product, not a scored instrument or a formal EQ-HWB revision.

**Principal findings.** Seven of eight themes aligned with EQ-HWB. The additional theme was mindset, with life attitude, adjustment of mindset, and positive or negative energy. The Chinese framework also had added subthemes such as regret, stress, emotional abilities, adaptation, appetite, and appearance. Sleep and boredom appeared under different themes from the EQ-HWB framework. The authors concluded that these differences did not materially weaken EQ-HWB comprehensiveness in this sample.

**Author interpretation and implications.** The authors interpret mindset and some language as culturally shaped but also find broad agreement with Western quality-of-life frameworks. They advise careful translation and cultural adaptation where concepts have no direct English equivalent. They state that a practical instrument must balance content coverage with length. These are author-reported scientific and instrument-adaptation implications.

**Limitations and gaps.** Participants from Harbin were younger, healthier, and more educated than desired. Patients came from community settings and mainly had chronic conditions. Theme translation was difficult. Saturation was subjective. The paper did not assess relevance or comprehensibility and states that these will be reported separately. It suggests future inclusion of hospitalized people with severe illness.

**Source uncertainty.** The paper reports `68% (18/57)` subtheme alignment. The fraction 18/57 is about 32%, not 68%. Keep the narrative claim and fraction as conflicting source statements. Do not correct the numerator or infer a missing value.

### 9. 10.1016/j.jval.2025.02.001 — review of EQ-5D analysis in randomized trials

**Classification and purpose.** Systematic review or evidence synthesis and methods study; completed. The paper describes how randomized trials analyze treatment effects in EQ-5D dimension responses, EQ VAS, and utility data. It examines data format, follow-up structure, model choice, baseline adjustment, assumptions, and missing-data methods.

**Components.** `R1 MEDLINE and EMBASE search` and `R2 registry search` feed `E1 unique randomized trials`. `A1 utility analysis methods`, `A2 EQ VAS analysis methods`, and `A3 dimension-response methods` are split by numerical or categorical format and by one or multiple postbaseline times. `A4 missing-data methods` and `A5 time-to-deterioration methods` cut across data forms.

**Evidence context.** The evidence units were 2,125 unique randomized trials, not individual trial participants. The review included any patient population or treatment if the trial analyzed postbaseline EQ-5D by treatment group. It excluded pilot and feasibility work, non-English reports, and analyses limited to QALYs or quality-adjusted time because those outcomes combine health with time. Included trial reports were journal articles, HTA reports, or registry results.

**Instrument scope.** EQ-5D was the instrument family. Exact 3L or 5L version and value-set language were not the organizing factors and can be `various or not consistently stated` at review level. The review kept three data forms distinct: dimension response, EQ VAS, and utility. It also kept numerical and categorical transformations distinct. This is necessary because the method options and findings differ.

**Review and reuse method.** The authors searched MEDLINE and EMBASE from inception through 15 November 2021 and ClinicalTrials.gov on 16 August 2023. Registry records were linked to PubMed publications where possible. Reviewers screened in duplicate and resolved differences with a third reviewer. The team mapped multiple publications to one trial identifier with registration number, indication, treatment, and sample size. This is a duplicate-evidence control relation. It is not primary data reuse by the review. Extraction used a piloted template. Results were descriptive. The authors did not appraise trial risk of bias because the review estimated method use rather than treatment effects.

**Method taxonomy used by the paper.** The review grouped methods as descriptive, bivariate, multivariable, and survival analysis. It further distinguished fixed-effect and mixed-effect linear or logistic models, generalized estimating equations, parametric and nonparametric tests, and uncommon specialized models. Single postbaseline and repeated postbaseline designs remained separate because repeated observations require a within-person correlation structure.

**Principal findings.** Utility was analyzed in 1,592 trials, EQ VAS in 1,197, and dimensions in 385. Utilities and EQ VAS were almost always numerical. Dimension responses were more often categorical. Linear fixed-effect models were most common for one postbaseline utility time, and linear mixed-effect models were most common for repeated times. Only 10.8% of trials that analyzed numerical EQ-5D reported a model-assumption check, 21.3% adjusted for baseline score, and 2.6% used a minimal important difference to interpret effects. Only 661 trials explicitly assessed missing EQ-5D data. Of the 347 that imputed values, multiple imputation and last observation carried forward were most frequent.

**Author interpretation and implications.** The authors state that common linear models can conflict with EQ-5D skewness, ceiling, and discreteness, and that method variation reduces comparability. They call for analysis guidance, clearer estimands, baseline adjustment, suitable missing-data assumptions and sensitivity analysis, more attention to dimensions, and direct comparison of specialized models. These are author-reported scientific and reporting implications. The review supplies a basis for guidance but does not itself establish a guideline.

**Limitations and gaps.** The search covered a long period in which practice changed. Publications gave limited detail for secondary and exploratory outcomes, so baseline adjustment and imputation may be under-reported. Exact model covariates and correlation structures were often absent. The review found no dominant best method and did not compare model performance directly.

### 10. 10.1007/s10198-025-01770-x — Brazilian comparison of youth HRQoL measures

**Classification and purpose.** Measurement-property assessment; completed. The paper compares EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Brazilian schoolchildren with and without self-reported musculoskeletal pain.

**Components.** `S1 musculoskeletal-pain group` and `S2 no-pain group` are baseline subgroups. `T0 baseline` and `T1 seven-day retest` supply repeat observations. `S3 clinically stable retest sample` contains people whose PIP-Kids classification did not change. Analysis streams assess feasibility and distribution, test-retest reliability and measurement error, construct-validity hypotheses, known-groups validity, and pain-severity differences.

**Evidence context.** Respondents and referents were children and adolescents who reported their own health. The sample came from public and private schools in urban Sao Paulo state, Brazil. Participants were aged 8 to 18 years and could read and write Brazilian Portuguese. Parents or guardians gave consent and children gave assent. The baseline sample had 356 participants: 181 met the paper's self-reported musculoskeletal-pain rule and 175 did not report musculoskeletal pain. The stable retest sample had 231 participants: 96 with pain and 135 without pain.

Pain classification required pain in the back, neck, arms, or legs in the prior month plus school absence or interference with normal or recreational activity. The study excluded pain attributed to trauma, sports injury, surgery, cancer, infection, fracture, inflammatory disease, or diagnosed traumatic soft-tissue injury. The condition was not confirmed by a clinician. This classification and its one-month recall differ from the instruments' `today` referent.

**Instrument roles and administration.** Official Brazilian-Portuguese self-report EQ-5D-Y-3L and EQ-5D-Y-5L were primary measurement-property targets and direct comparators. EQ VAS was analyzed separately for each youth version. Official Brazilian-Portuguese CHU9D was another target and comparator. PedsQL 4.0 was a construct-validity comparator. PIP-Kids classified pain and stability, and the numeric pain rating scale measured pain severity. The paper did not analyze EQ-5D or CHU9D utilities.

Administration was paper self-report in classrooms, with teachers and researchers available to explain questions. Baseline order was fixed for most measures. The order of the two EQ-5D-Y versions was randomized, but the versions were completed consecutively. Retest occurred after seven days and omitted the sociodemographic form and PedsQL.

**Measurement-property path.** Feasibility used missing responses and completion rates. Distribution used item responses and profile-level ceiling and floor effects. Test-retest reliability used kappa for dimensions and ICC for EQ VAS, with standard error of measurement and smallest detectable change. Construct validity used prespecified correlation hypotheses against PedsQL and between the three preference-based instruments; more than 75% confirmed hypotheses was the study's adequate-result rule. Known-groups validity compared pain and no-pain groups and compared pain-severity groups.

**Principal findings.** The three descriptive systems had poor to moderate test-retest reliability. EQ VAS reliability was stronger in the pain group than in the no-pain group. EQ-5D-Y-3L and EQ-5D-Y-5L met the paper's construct-validity rule against PedsQL in the pain group. EQ-5D-Y-5L met the rule against CHU9D in both groups; EQ-5D-Y-3L did not. All three instruments distinguished the pain and no-pain groups. EQ-5D-Y profiles had substantial ceiling effects, and the 5L reduced the profile ceiling relative to 3L.

**Author interpretation and implications.** The authors state that all three instruments are feasible and can support assessment of HRQoL in Brazilian children and adolescents, especially those with musculoskeletal pain. They link the Brazilian EQ-5D-Y-3L value set to possible economic evaluation and reimbursement use. This is an author-reported clinical and policy implication. This paper did not document a reimbursement decision or score utilities with that value set.

**Limitations and transfer limits.** Pain was heterogeneous, self-reported, and not clinically diagnosed. PIP-Kids used one month, while the three preference-based measures used today. Many children classified with prior-month pain had no pain on the administration day. Consecutive youth EQ-5D versions can cause recall or carry-over effects. Instrument response forms and recall periods differed, and no gold standard for HRQoL in musculoskeletal pain was available. A result below the 75% hypothesis threshold means that the prespecified hypotheses were not confirmed; the authors warn that it does not alone prove that an instrument is invalid. The sample includes ages 16 to 18, beyond the stated 8-to-15 target range of the EQ-5D-Y versions in the paper.

**Stated gaps.** The authors call for tests in other health conditions and settings, work in children younger than eight with self and proxy forms, utility-based tests for EQ-5D-Y-3L and CHU9D in Brazil, and studies of reliability, validity, and responsiveness.

## Granularity decisions and evidence

### Decisions retained after round 1

1. **Keep evidence supplier, respondent, referent, target population, and decision context separate.** Paper 6 uses adult respondents to value a hypothetical child's health. Paper 4 surveys HTA staff about methods instead of administering health measures. Papers 2 and 9 use publications or trials as evidence units. Without these roles, corpus queries about child respondents, direct valuation, or patient evidence will return false matches. This supports user questions 6, 19, 20, and 25.

2. **Use components only for interpretation-changing heterogeneity.** Papers 1 and 6 need separate cTTO, DCE, and model streams. Paper 5 needs ordered development phases. Paper 10 needs pain groups and baseline or retest components. Paper 3 needs pilot and country rounds. A flat paper record would lose method relations. A component for each table would add no value. This supports questions 5, 9, 10, 12, and 13.

3. **Permit more than one study-family tag.** Paper 3 is both a protocol, an infrastructure paper, a population-health study, and an instrument-comparison design. Paper 7 is both a measurement-property and methods paper. One exclusive family would hide useful retrieval. This supports questions 1, 9, 20, and 21.

4. **Separate exact instrument identity from role and product.** Paper 5 develops EQ-5D-Y-5L. Paper 6 values EQ-5D-Y-3L and produces a Chinese value set. Paper 10 administers two EQ-5D-Y versions but does not use utilities. Paper 4 only asks practitioners about instrument use. These are materially different records for questions 3, 4, 14, 20, and 23.

5. **Treat EQ-5D profile, EQ VAS, and utility as distinct data forms when analyzed.** Paper 9 shows large differences in use and statistical method across these forms. Paper 10 analyzes profiles and EQ VAS but no utility. A single `uses EQ-5D` label cannot answer what data a paper analyzed. This supports questions 3, 12, 13, 20, and 21.

6. **Represent administration as several axes.** Paper 1 uses interviewer-administered EQ-VT on a computer. Paper 3 uses web self-report. Paper 5 uses interviews and child response-scaling tasks. Paper 10 uses paper self-report in classrooms with help available. These differences can affect selection, comprehension, and data quality. This supports questions 11, 13, 20, and 24.

7. **Use detailed method paths for the paper's domain, not one universal level of depth.** For valuation, task, protocol, design, anchor, model, and product are necessary in papers 1 and 6. For paper 8, coders, inductive and deductive coding, language, and framework comparison are necessary. For papers 2 and 9, search, evidence unit, duplicate handling, and synthesis are necessary. This supports questions 9 through 12 and 21.

8. **Keep measurement-property subtypes controlled and linked to methods.** Papers 2, 7, and 10 show that reliability, construct validity, known-groups validity, responsiveness, informativity, item discrimination, and DIF answer different questions. `Psychometrics` alone is too broad. The target item, comparator, subgroup, statistic, and time point also change interpretation. This supports questions 9, 12, 20, 21, and 22.

9. **Keep valuation task and model distinctions.** cTTO, DCE, conventional and lead-time TTO, DCE anchoring, mapping, and hybrid models are not interchangeable. Paper 6 shows different dimension rankings by task and a result that changes when an A3 term is added. Paper 1 selects a censored heteroscedastic hybrid because simpler component models are inconsistent. This supports questions 10, 12, 13, 20, and 21.

10. **Record development stages and product maturity.** Paper 5 produced a comprehensible self-report instrument but still required psychometric tests, valuation, and proxy forms. Paper 3 has completed data rounds inside an ongoing infrastructure. `Developed` without stage and future step would overstate both products. This supports questions 14, 18, and 23.

11. **Keep comparisons explicit and record the difference dimensions.** Paper 10 compares instruments, pain groups, and recall periods. Paper 7 compares response-scale forms at item level. Paper 1 compares directly elicited and crosswalk value sets. A generic comparison flag cannot show whether population, version, scale, scoring route, or model causes the contrast. This supports questions 13, 20, 21, and 22.

12. **Record reuse and evidence provenance.** Paper 7 reanalyzes an earlier dyadic data set. Paper 2 avoids duplicate extraction from publications that use one data set. Paper 9 maps several publications to one trial. Papers 1 and 6 extend standard protocols but collect new samples. These relations are needed to avoid treating dependent evidence as independent. This supports questions 19 and 25.

13. **Separate findings, author interpretation, implications, limitations, and gaps.** Paper 5 expects better sensitivity but does not test it. Paper 4 suggests research priorities but does not document adoption. Papers 1 and 6 recommend value sets but do not prove downstream policy effects. This boundary prevents inferred impact and supports questions 15 through 18 and 22.

14. **Store source conflicts and transfer limits as semantic uncertainty.** Papers 2, 6, and 8 contain internal numerical or geographic conflicts. Paper 10 uses a self-reported one-month pain definition against `today` measures and includes participants older than the stated EQ-5D-Y range. These facts change confidence or applicability and support questions 13 and 16.

15. **Use controlled terms for recurring, stable distinctions and narrative for paper-specific detail.** Control instrument roles, study families, administration axes, valuation tasks, measurement properties, product types, maturity, and provenance relations. Use repeatable structured values for samples, counts, countries, languages, methods, and comparisons. Use concise narrative for purpose, complex recruitment, conceptual themes, findings, interpretation, limitations, and gaps. This balance supports precise retrieval without an unstable item-level schema.

### Distinctions considered and rejected

- **A component for each reported analysis or table:** rejected. It would create many nodes with no retrieval or interpretation benefit. Keep principal analysis streams only.
- **One exclusive study type:** rejected. Multi-purpose papers in this batch require repeatable family tags.
- **One broad method label such as survey, regression, qualitative, or psychometric:** rejected. It hides task, model, property, and inference differences that change user answers.
- **Every coefficient, correlation, confidence interval, or country table:** rejected. Keep decisive values and concise principal findings. Full numerical result extraction belongs to a different claim or data layer.
- **All instrument items and dimensions for each administration:** rejected. Exact instrument version normally supplies this information. Keep item or dimension detail only when it is the study target.
- **A universal taxonomy for every quality-of-life theme:** rejected for now. Paper 8 shows culturally and linguistically sensitive concepts. Preserve its framework as a product and use broad topic tags for cross-paper retrieval.
- **Treating a value set as an instrument version:** rejected. A value set is a population-based scoring product linked to an instrument version.
- **Treating every named software package as a controlled method:** rejected. Record EQ-VT, survey platforms, or software versions only when they define delivery, quality control, or a reproducible protocol. Routine analysis software can stay in narrative or be omitted.
- **Treating professional discussion of an instrument as administration:** rejected. Paper 4 would otherwise appear to measure practitioners' health with EQ-5D.
- **Treating review evidence units as participants:** rejected. Papers 2 and 9 require publication, data-set, and trial evidence units.
- **A binary positive or negative finding:** rejected. It removes population, comparator, method, and transfer context.
- **A general impact field:** rejected. Keep author-reported implication type separate from documented use or effect.
- **Automatic inference of country or language from author affiliation or study title:** rejected. Paper 7 shows why the methods must state this context. Store `not stated` and a scoped uncertainty instead.
- **Detailed recruitment incentives as controlled values:** rejected. Keep them only in narrative when they can affect selection or representativeness.

## Unresolved cases for later rounds

1. The preliminary product-maturity terms fit this batch but can overlap. Later papers can show whether `established`, `recommended by authors`, `available`, `licensed`, and `in current use as documented` need stricter definitions.
2. EQ-DAPHNIE has completed national collections inside an ongoing infrastructure. Later protocol and implementation papers must test whether paper-level `mixed status` plus component status is sufficient.
3. The exact boundary between content validity, concept elicitation, and cultural adaptation remains open. Paper 8 tests only comprehensiveness and does not revise the instrument. Later translation papers can test whether these need separate study-family tags or only linked method stages.
4. Paper 7 treats frequency and severity scales as comparison groups in DIF. This is not the usual person-group DIF use. Keep the exact focal and reference definitions in the method path until more response-scale papers show a stable term.
5. Country and language are often absent or mixed in systematic reviews. Later rounds must test how much evidence-level context is practical without recreating every included study.
6. Review papers can report publications, studies, trials, and underlying data sets at different counts. The current evidence-unit and reuse relations can express this, but later reviews can require more explicit cardinality guidance.
7. Paper 10 includes ages 16 to 18 although the paper describes EQ-5D-Y for ages 8 to 15. Keep this as a transfer limit. Do not create a general age-validity rule until instrument documentation is in the allowed evidence context.
8. Internal source conflicts currently use concise narrative. Later rounds can test whether a controlled conflict type, such as count conflict, scope conflict, or arithmetic conflict, improves retrieval.

## Short run note

This was the first round for Candidate 2. There was no prior lineage record to extend. The ten assigned files matched the manifest SHA-256 values and byte counts. The batch added strong evidence for detailed valuation paths, measurement-property subtypes, instrument-development stages, evidence-role separation, product maturity, and review evidence units. No fixed JSON schema was used.

## Applications to batch 02

### 1. 10.1016/j.jval.2025.01.003 — United Arab Emirates EQ-5D-5L value set

**Classification and purpose.** Health-state valuation study and value-set development; completed. The paper develops the first United Arab Emirates value set for EQ-5D-5L. It uses preferences from UAE nationals and long-term expatriate residents and compares cTTO-only, DCE-only, and hybrid model forms. Topics include local HTA evidence, a multilingual valuation, mixed interview contact modes, expatriate population membership, and model robustness.

**Components.** `S1 analyzed valuation sample` supplies `T1 cTTO` and `T2 DCE without duration`. `Q1 interviewer training and continuing quality control` governs both tasks. `A1 cTTO models`, `A2 DCE model`, and `A3 hybrid models` remain separate model streams. `A4 observation-exclusion sensitivity analysis` compares four data sets. `A5 leave-state-out and leave-block-out cross-validation` assesses prediction. `C1 language and contact-mode quality comparison` supports the decision to pool Arabic and English and face-to-face and online interviews.

**Evidence context.** Respondents were adults aged at least 18 years from all seven Emirates. They were UAE nationals or expatriates who had lived in the UAE for at least five years. The respondent valued hypothetical adult EQ-5D-5L states. The target preference population was the current UAE adult general population, which the study defines to include nationals and qualifying expatriates. The decision contexts were UAE cost-utility analysis, HTA, population health assessment, and health-system PROM use. Recruitment used Emirate strata and age and sex quotas, followed by professional and personal networks, snowball recruitment, public-place outreach, posters, and social media. The study conducted 1,145 interviews and treated 140 early practice interviews as exclusions. The main analysis included 1,005 respondents, 10,050 cTTO observations, and 7,035 DCE observations. The analyzed sample included 115 UAE nationals and 890 expatriates.

**Instrument, language, and administration.** EQ-5D-5L was the target of valuation, source of health-state descriptions, and an initial administered self-report measure. EQ VAS was also self-reported. Arabic respondents used the UAE Arabic EQ-5D-5L. English respondents used the UK English version because no UAE English version was available. EQ-VT delivered computer-based, interviewer-administered interviews either face to face or online. In-person settings included the research office, university facilities, workplaces, and public places. Each analyzed respondent completed ten cTTO states and seven DCE pairs. The paper reports only small quality differences by language and contact mode and combines the groups. It does not establish linguistic or mode equivalence outside this valuation.

**Protocol and modeling path.** The study followed the EuroQol EQ-5D-5L valuation protocol. cTTO used conventional TTO for better-than-dead states, lead-time TTO for worse-than-dead states, and the feedback module. Fourteen interviewers entered training. Seven completed data collection after practice and quality review. The study paused at 25%, 50%, and 75% of collection for interim quality checks. Ten candidate models included random-intercept, Tobit-censored, heteroskedastic, DCE conditional-logit, and hybrid variants. Hybrid models estimated a scale parameter between cTTO and DCE. Selection used logical consistency, parsimony, AIC and BIC within comparable model families, RMSE, MAE, and cross-validation. Sensitivity paths included all observations, exclusion of 55555 inconsistencies, exclusion of feedback-flagged values, and both exclusions.

**Product and states.** `United Arab Emirates EQ-5D-5L value set`; completed named national value set and author-recommended for UAE use. Its evidence is the reported bilingual, mixed-contact valuation and model-selection study. The selected model is a heteroskedastic hybrid Tobit model with cTTO censoring at -1. Values range from 1 for 11111 to -0.654 for 55555, and 15.3% of modeled states are worse than dead. The population basis combines nationals and qualifying long-term expatriates. It is not an Arabic-only product. Downstream use is not documented here.

**Principal findings and author interpretation.** All main candidate models were largely logically consistent. The selected hybrid model used both data types and addressed censoring and heteroskedasticity. Mobility had the largest decrement, followed by pain or discomfort and anxiety or depression. The authors interpret the quality checks and stable sensitivity results as evidence of robust data. They state that online interviewer administration can be a viable valuation mode when quality control is strong.

**Reported implications, limitations, and gaps.** The authors recommend the value set for local QALY estimation, resource allocation, and health-policy evidence. This is an author-reported policy and implementation implication, not evidence of a completed national decision. The five-year expatriate residence rule has no conclusive validation. National or expatriate status, language, country of origin, employment, and lived experience can be related and were not modeled as separate preference effects. The UK English version can introduce wording transfer limits. The authors call for qualitative research on expatriate valuation choices and raise questions about universal language versions and the time validity of value sets in mobile populations.

**Source conflict.** `summary versus main text`: the abstract reports a mean age of 39 years, while the main results report 32.1 years. Use 32.1 as the detailed results value and retain the abstract value as a conflict.

### 2. 10.1016/j.jval.2024.05.016 — direct comparison of DCE with duration and EQ-VT methods

**Classification and purpose.** Health-state valuation study and methods study; completed. The paper tests whether a split-triplet DCE with duration, or DCEd, can produce EQ-5D-5L values similar to cTTO and EQ-VT models when the DCEd model allows nonlinear time preference. It does not establish a national value set for operational use.

**Components and reuse.** `D1 Trinidad and Tobago EQ-VT data` is a previously reported data source with `S1 EQ-VT sample`, `T1 cTTO`, and `T2 DCE without duration`. `D2 new DCEd survey` has an independent `S2 DCEd sample` and `T3 split-triplet DCEd`. `A1 cTTO heteroskedastic Tobit`, `A2 rescaled DCE mixed logit`, and `A3 hybrid heteroskedastic Tobit` analyze D1. `A4 linear-time DCEd` and `A5 nonlinear-time DCEd` analyze D2. `C1 all-state agreement` compares 3,125 predicted states. `C2 observed-state agreement` compares predictions with the means for 86 cTTO states. The paper explicitly reuses EQ-VT data reported in an earlier article. The DCEd sample is new and independent.

**Evidence context and administration.** Both respondent samples came from the Trinidad and Tobago adult general population. The referents were hypothetical EQ-5D-5L health states and lives with duration. The EQ-VT sample had 1,079 respondents, each with ten cTTO tasks and twelve DCE pairs. Panel recruits had face-to-face interviews in their homes after four-day interviewer training and EQ-VT quality control. The DCEd survey had 1,581 completers. It retained 970 after quality exclusions. Respondents self-completed 18 split-triplet tasks in LimeSurvey on a sufficiently large digital device. Recruitment first used an online panel link and public-place recruiters with supplied laptops. The study removed all data from the recruiter or shared-IP route because of speeding and flatlining.

**Task and design path.** Each split triplet first compared two impaired EQ-5D-5L states with equal duration. The next choice compared one of those lives with full health for a shorter duration. Fifteen triplets used full health for a positive duration, and three used immediate death. A near-orthogonal starting design supplied priors. The team updated the Bayesian-efficient design three times after batches of 200 respondents. This adaptive design history is material to replication and is separate from the final task type.

**Quality and modeling path.** The main DCEd exclusion threshold was less than 12.5 seconds per split triplet. IP-level rules removed unusually fast recruited groups. Sensitivity analyses used 10- and 15-second thresholds. The DCEd analysis compared mixed-logit models with linear time and an exponential nonlinear discount rate. It also estimated a separate immediate-death parameter. EQ-VT paths used a cTTO heteroskedastic Tobit, a latent-scale DCE mixed logit rescaled with cTTO information, and a hybrid heteroskedastic Tobit. Scatterplots, correlations, Bland-Altman plots, mean difference, mean absolute difference, and error against observed cTTO means assessed agreement.

**Principal findings.** The linear DCEd model valued 55555 at about -1.214. The nonlinear-time model valued it at about -0.543 and gave the same main level-5 dimension order as the EQ-VT models. Nonlinear DCEd predictions correlated from 0.954 to 0.973 with the three EQ-VT paths. Agreement was best with the rescaled DCE and hybrid paths, and DCEd predicted slightly higher values in the middle of the scale. The empirical mean annual discount correction was 23.5%. Treat this as a DCEd correction factor, not as an HTA policy discount rate.

**Author interpretation and implications.** The authors interpret the agreement as evidence that nonlinear-time DCEd and EQ-VT measure a similar health-value construct. They present unattended online DCEd as a possible lower-cost substitute for interviewer-intensive EQ-VT. This is an author-reported methods implication from one country, not proof that the methods are interchangeable in all settings.

**Limitations and gaps.** The samples differed in education, ethnicity, sex, and age and were collected about six months apart. A DCEd flatliner can reflect inattention or a genuine strong duration or quality preference, and the model cannot distinguish these causes. The public-place collection route failed quality checks, which limits claims about all unattended or recruiter-assisted administration. The authors call for choice-position randomization, tests in other languages and cultures, and replication under different sampling conditions before parallel use with EQ-VT.

### 3. 10.1186/s12955-023-02177-z — EQ-5D-5L measurement properties in Graves' disease

**Classification and purpose.** Measurement-property assessment; completed. The paper assesses distribution, convergent validity, one-month test-retest reliability, and six-month responsiveness of EQ-5D-5L for adults with relapsed Graves' disease in Hong Kong.

**Components.** `S1 baseline cohort` contains 125 patients. `T0 baseline`, `T1 one-month follow-up`, and `T2 six-month follow-up` are separate time points. `S2 one-month stable group` has 64 patients with self-reported unchanged health. At six months, `S3 worsened`, `S4 unchanged`, and `S5 improved` have 21, 38, and 41 patients. `A1 distribution and ceiling`, `A2 convergent validity`, `A3 dimension agreement`, `A4 score reliability`, and `A5 direction-specific responsiveness` are separate analysis streams.

**Evidence context and administration.** A convenience sample came from endocrinology and surgical outpatient clinics in three Hong Kong public hospitals. Eligible patients had relapsed Graves' disease, were at least 18 years old, could read Chinese or English questionnaires, and were not pregnant or cognitively impaired. Patients self-completed baseline instruments. Follow-up instruments were online. The paper does not report how many respondents used each language or the exact language version in each case. It retained 101 patients at one month and 100 at six months. Clinical and treatment data came from Hong Kong Hospital Authority electronic records.

**Instrument and scoring roles.** EQ-5D-5L was the measurement-property target. Its profile, Hong Kong-value-set utility, and EQ VAS were analyzed separately. ThyPRO-39 overall quality-of-life impact and composite scores were convergent-validity comparators. A patient global transition question at six months anchored improved, unchanged, and worsened health. This anchor is separate from Graves' disease treatment or laboratory change.

**Measurement-property path.** Distribution analysis used dimension responses, state 11111, and a 15% ceiling or floor rule. Spearman correlations tested prespecified moderate or strong convergence with ThyPRO-39. For stable patients, Gwet's AC2 and percentage agreement tested dimension response agreement. A two-way random-effects absolute-agreement average-measure ICC tested EQ-5D-5L utility and EQ VAS. Six-month within-group change used Wilcoxon signed-rank tests. Standardized effect size and standardized response mean assessed responsiveness separately for worsened and improved groups.

**Principal findings.** State 11111 occurred in 28% at baseline, which indicates a profile ceiling under the paper's rule. ThyPRO-39 correlations with utility and EQ VAS were moderate to strong. Dimension agreement was very good for mobility, self-care, and usual activities and lower for pain or discomfort and anxiety or depression. Utility and EQ VAS ICCs were about 0.70, which the paper classified as moderate reliability. Both outcomes changed in the expected direction for the worsened group. The evidence did not support responsiveness to improvement; utility was limited by baseline ceiling and small groups.

**Author interpretation, limitations, and gaps.** The authors support EQ-5D-5L use with a disease-specific measure in Graves' disease because the instruments cover different content. They describe the deterioration result as responsive evidence but acknowledge that improvement was not detected. Loss to follow-up was 20%, responsive subgroups were small, and confidence intervals were wide. The outpatient convenience sample limits transfer to other Graves' disease populations. The authors call for larger studies of responsiveness to improvement and for work on the meaning of observed change.

### 4. 10.1007/s11136-025-04150-3 — expert content review of EQ-TIPS version 2.0

**Classification and purpose.** Instrument development and measurement-property assessment; completed consultation within an ongoing instrument program. The paper asks three expert groups to review experimental EQ-TIPS-3L version 2.0 and to discuss its construct, content, proxy completion, intended uses, and development challenges.

**Components.** `G1 EuroQol expert consultation`, `G2 pediatric health and development consultation`, and `G3 pediatric instrument-developer consultation` use different expertise. G1 and G2 include breakout discussions. G2 also receives an emailed facilitator summary for correction. The consultation guides change in sequence after earlier groups. `A1 deductive and inductive thematic analysis` analyzes all transcripts. `C1 cross-group synthesis` identifies agreement, disagreement, and development recommendations.

**Evidence context and role boundary.** The evidence suppliers were 33 experts from 15 countries: 17 EuroQol experts, 11 pediatric health and development experts, and five pediatric instrument developers. They were purposively selected through author networks and literature. They are not proxy respondents who rated a child. The intended future respondent is a proxy, usually a caregiver, and the referent is a child aged zero to three years. The target contexts are pediatric clinical research, routine outcomes, trials, economic evaluation, and health decision making. Do not retrieve this paper as direct HRQoL evidence from infants, toddlers, parents, or clinicians acting as child proxies.

**Instrument role and status.** Generic English experimental EQ-TIPS-3L version 2.0 was the target of content review. It had six dimensions, three severity levels, a `today` recall period, and a proxy-rated VAS. A five-level version existed later but was not available for this study. The paper tests expert views of relevance, comprehensibility, and comprehensiveness. It does not test a revised version, psychometric performance, or valuation. EQ-5D-Y and adult EQ-5D were discussed as lifespan-transition references, not administered comparators.

**Qualitative method.** Three semi-structured Zoom consultations occurred from December 2022 to February 2023. Participants received the instrument, a short introduction, and earlier development papers. Sessions and breakout rooms were recorded, transcribed, and de-identified. Two analysts used Braun and Clarke's six-phase thematic analysis in NVivo. Codes started deductively from the guides but allowed inductive themes. The wider facilitator team checked the extraction table. The paper reports SRQR use.

**Principal findings.** Experts generally considered the instrument short, clear, useful, and broadly relevant. They asked for a clear definition of the measured construct and for content to describe the child's HRQoL rather than caregiver or family spillover. Most accepted the zero-to-three age range, but development and context can differ within it. They preferred observable examples to the phrase `age-appropriate`, because developmental norms and translations can vary. They supported `today` for acute or repeated measurement but noted limits for fluctuating or chronic conditions. All six dimensions received support. Communication and social interaction could overlap. Sleep and emotions need further testing. Eating wording must not turn normal parental concern into a child health problem, and pain behavior can be confused with distress.

**Proxy and development implications.** Experts said the best proxy can depend on context and familiarity with the child. A parent may not always be best during hospitalization or absence. Proxy relation, caregiving experience, and proxy HRQoL can affect responses and should be captured outside the child score when appropriate. The paper produces a set of `proposed` refinement and testing recommendations. It does not produce a new EQ-TIPS version. EQ-TIPS remains experimental and unvalued in this paper.

**Limitations and gaps.** Recruitment through known networks can bias the views. Expertise and prior EQ-TIPS knowledge differed. Breakout rooms improved participation but limited full-group debate and formal consensus. The study did not collect expert parenting or caregiving characteristics. The instrument needs direct work with parents and caregivers, lower-literacy respondents, varied socioeconomic and cultural settings, diverse health conditions, and empirical tests of examples, sleep, emotions, response levels, and age-range performance.

**Source conflict.** `count or arithmetic`: the paper reports 44 invited experts and 11 non-attenders, which agrees with 33 participants. However, the reported invited group counts of 21, 13, and 9 total 43. Keep 44 as the stated total, keep the three group counts as reported, and do not repair the missing unit.

### 5. 10.1186/s41687-025-00985-z — Modern Standard Arabic EQ-5D-Y-5L for Egypt

**Classification and purpose.** Translation, cultural adaptation, and instrument development; completed. The paper translates the self-report EQ-5D-Y-5L into Modern Standard Arabic for use in Egypt and tests response-level order and comprehension with children.

**Components and version roles.** `V1 UK English EQ-5D-Y-5L` is the source version. `V2 Egyptian Arabic EQ-5D-Y-3L` is a reference version used where wording could remain consistent. `P1 two independent forward translations` produces a reconciled Arabic draft for paper and digital forms. `P2 two independent back translations` tests meaning and produces a second draft. `P3 initial cognitive debriefing` has eight children and includes card ranking, self-completion, and detailed probing. `P4 focused cognitive debriefing` has three additional children and tests revised pain, digital-item, and VAS wording without card ranking. `P5 proofreading and version approval` produces the final version. EuroQol's Version Management Committee reviews decisions across stages.

**Evidence context and administration.** Eleven Egyptian children aged 8 to 15 years took part: six girls, five boys, six healthy children, and five with chronic conditions. A convenience sample covered Cairo and Menoufia Governorates, different school types, and low-to-middle socioeconomic settings. A trained Arabic-speaking interviewer conducted one-to-one face-to-face interviews in participant homes, the interviewer's home, or Cairo University. Parents were present. Children self-completed the questionnaire and described their understanding. The target population was Arabic-speaking children and adolescents who self-report health, with Egypt as the directly tested country.

**Translation method.** Two native-Arabic professional translators independently translated the UK English paper and digital versions. Two native-English translators, who had not seen the source, independently back translated the reconciled draft. The research team and Version Management Committee resolved conflicts. The card-ranking task tested four response-label sets before children saw the questionnaire. It omitted usual activities because its qualifiers duplicate other sets. The detailed probes asked for paraphrases and examples. Changes were linked to evidence from each stage instead of literal word equivalence alone.

**Principal findings.** Eight children ranked 160 cards, with ten order inversions. Later examples indicated that the children understood the severity order. All 11 described the questionnaire as clear and easy. Six needed a second reading or interviewer confirmation for general or VAS instructions, mainly at younger ages. Some children interpreted the first Arabic pain term as emotional pain even after a body reference. A replacement term produced physical-pain examples in the focused interviews. The digital prompt changed its word for `item` to the child-understood word for `question`. Mean questionnaire completion time was 5.2 minutes.

**Product and states.** `Modern Standard Arabic EQ-5D-Y-5L self-report version for Egypt`, with paper and digital forms; completed named output of the reported translation process. Evidence covers response ordering and comprehension in 11 children. EuroQol Version Management Committee review and approval are documented. The paper does not supply psychometric results, a value set, a proxy form, or routine-use evidence. Licensing remains under EuroQol control.

**Author interpretation, implications, and transfer limits.** The authors state that the version is acceptable for use in Egypt and may support comparisons and later adaptation in Arabic-speaking countries. They recommend interviewer support for children aged eight to ten. The wider-country claim is an author-reported transfer implication, not local validation in each Arabic-speaking culture. Modern Standard Arabic has regional dialect and vocabulary limits. The convenience sample was small and came from two Egyptian Governorates. The paper states that psychometric work in health conditions will be reported separately; do not treat that evidence as part of this paper.

### 6. 10.1016/j.jval.2024.03.2195 — psychometric assessment of nine EQ-5D-5L bolt-ons

**Classification and purpose.** Measurement-property assessment and methods study; completed. The paper assesses the item performance and added measurement value of nine existing five-level bolt-ons for EQ-5D-5L in Hungary.

**Components and provenance.** `D1 November 2020 Hungarian web survey` contains 1,700 adult respondents before data checks. `S1 analysis sample` contains 1,587 after 113 inconsistent records were removed by rules described in earlier reports. `A1 response distribution and ceiling`, `A2 divergence from EQ-5D-5L items`, `A3 convergence with external items`, `A4 PCA and CFA structural validity`, `A5 known-group validity`, and `A6 explanatory power` are distinct analysis streams. `A7 stepwise bolt-on combinations` tests the added value of more than one item. The data set and exclusions were reported in earlier papers, but this article does not give a stable data-set name. Record reuse of the 2020 survey and do not infer a new independent sample.

**Evidence context and administration.** Respondents were Hungarian adults aged at least 18 years who could read Hungarian. Soft quotas covered age, gender, residence, and region. They self-completed a fixed-order online questionnaire. The referent was each respondent's own health and wellbeing. The target contexts were general-population surveys and later selection of relevant bolt-ons for patient studies. Physician-diagnosed condition groups included 13 prevalent chronic conditions. The paper does not test clinical severity within those groups.

**Instrument roles.** EQ-5D-5L was the core administered measure and comparison baseline. The targets of item-level and added-value assessment were breathing, cognition, hearing, self-confidence, skin irritation, sleep, social relationships, tiredness, and vision bolt-ons. All used a five-level format and `today`. PROMIS-29+2 v2.1, SF-6D derived from SF-36v1, PROMIS Global Health v1.2, and the Satisfaction With Life Scale supplied construct comparators and dependent outcomes. EQ VAS was an explanatory-power outcome. No bolt-on value set or new bolt-on wording was produced.

**Measurement-property path.** Distribution analysis examined level use, floor, ceiling, profile diversity, age trends, and chronic-condition groups. Divergent validity used correlations between bolt-ons and core EQ-5D-5L items. Convergent validity linked each bolt-on to external items intended to cover the same construct. PCA informed a CFA that placed 63 retained items on nine factors. Known-group validity used a transformed, equal-weight level sum score and bootstrapped relative efficiency for healthy versus condition, age, health, and wellbeing groups. Linear models tested added explanation of EQ VAS, PROMIS Global Health, and life satisfaction. A stepwise rule added bolt-ons while another item gave a statistically significant efficiency or adjusted-R-squared improvement.

**Principal findings.** EQ-5D-5L state 11111 occurred in 41% of the sample, and 77% of that group reported a problem on at least one bolt-on. Sleep, tiredness, vision, and self-confidence gave the largest individual ceiling reductions. Seven bolt-ons loaded on factors not represented by EQ-5D-5L. Cognition and self-confidence shared the psychological factor with anxiety or depression. Relevant sensory, breathing, skin, and sleep bolt-ons improved known-group discrimination in corresponding conditions. Hearing and vision better represented age-related decline. Tiredness added the most EQ VAS explanation in many conditions. In most tests, one or two bolt-ons supplied most of the gain, and further items gave small added measurement benefit.

**Author interpretation and implications.** The authors state that relevant bolt-ons can improve content coverage and discrimination in population and patient surveys. They offer condition-specific item-selection evidence and a test framework for future bolt-on development. They do not establish one universal bolt-on set. They also warn that a measurement gain does not establish that the extended descriptive system is suitable for valuation or comparable with national EQ-5D-5L value sets.

**Limitations and gaps.** Severe response levels were rare. Core EQ-5D-5L and bolt-on items had intervening questions, and bolt-on order was fixed. The level sum score can give the same total to profiles with different severity patterns. Condition groups lacked clinical severity. Some CFA constructs had too few external items, which can force different physical symptoms onto one factor. The authors call for item-response-theory work, patient-population tests, valuation research, and tests of the number of bolt-ons that balance content, burden, and comparability.

### 7. 10.1007/s10198-018-0987-x — effect of mapped utility on dialysis cost effectiveness

**Classification and purpose.** Mapping or scoring study, health economic evaluation, and methods study; completed. The paper tests how five mappings from SF-12 to EQ-5D, and direct SF-6D scoring from SF-12, change QALYs and ICERs relative to directly observed EQ-5D-5L in two dialysis decision models.

**Components and reuse.** `D1 dialysis quality-of-life survey` reuses a cross-sectional sample of 75 hemodialysis and 75 peritoneal-dialysis patients. `M1 non-diabetic Markov model` and `M2 diabetic Markov model` rerun models from an earlier Singapore cost-utility study. Each model compares hemodialysis with peritoneal dialysis over ten years from a societal perspective. `U1 observed EQ-5D-5L scoring`, `U2-U4 direct utility mappings`, `U5-U6 response mappings`, and `U7 SF-6D scoring` provide alternative utility routes. `A1 cost-utility output` compares incremental QALYs and ICERs. `A2 bootstrap` propagates utility uncertainty. Transplant utility comes from a published meta-analysis. These reuse relations are necessary to identify dependent evidence.

**Evidence context and administration.** The source sample was 150 Singapore patients who had received hemodialysis or peritoneal dialysis for at least three months. Patients completed EQ-5D-5L, SF-12, kidney-disease questions, and demographics in an interview. EQ-5D-5L described the survey day. SF-12 used a four-week recall period. Hemodialysis respondents completed the survey during treatment, which can make the time-reference difference material. The modeled cohorts were hypothetical groups of 10,000 non-diabetic or diabetic patients with end-stage renal disease. The decision context was Singapore dialysis resource allocation.

**Score-construction paths.** Observed EQ-5D-5L profiles used the England EQ-5D-5L value set. Three direct mappings used ordinary least-squares functions from SF-12 physical and mental component summaries to EQ-5D-3L utility. Two response mappings used multinomial-logit functions from SF-12 summaries or items to predicted EQ-5D-3L responses, then the UK EQ-5D-3L value set. The five functions came from United States general-population or low-income patient samples. SF-6D used seven SF-12 items and a UK general-population standard-gamble value set. Thus, source measure, target EQ-5D version, mapping form, development population, and value set all differ.

**Economic method.** Linear models first estimated mean utility for hemodialysis and peritoneal dialysis with demographic adjustment. The Markov models used those means, fixed state utilities, a ten-year horizon, 2015 Singapore costs, 3% annual cost and QALY discounting, and a societal perspective. The study calculated incremental QALYs and hemodialysis-versus-peritoneal-dialysis ICERs. A 1,000-replication nonparametric percentile bootstrap supplied uncertainty intervals for utility-driven results.

**Principal findings.** All five mapped EQ-5D routes produced smaller hemodialysis-versus-peritoneal-dialysis utility differences than directly observed EQ-5D-5L. They reduced incremental QALYs by about 14.9% to 33.2% and increased ICERs by about 17.5% to 49.7%. SF-6D gave the same direction of change. Response mapping did not remove the discrepancy. The exact size differed between diabetic and non-diabetic models.

**Author interpretation and implications.** The authors attribute the difference to instrument content and recall periods, transport of mapping relations from unlike samples, regression prediction bias, and the mismatch between observed 5L scoring and 3L mapping targets. They advise direct EQ-5D collection when possible and one jurisdictional reference measure for consistent decisions. They state that a mapped score can change a reimbursement conclusion at a fixed threshold. This is an author-reported policy implication; the paper does not document an actual changed decision.

**Limitations and gaps.** This is one dialysis evaluation in Singapore. The observed EQ-5D-5L used an England value set because a local one was not used, and all mapped functions used UK EQ-5D-3L scoring. No dialysis-specific SF-12-to-EQ-5D mapping was available. The source survey was small, and the model held utilities constant. Do not generalize the direction or magnitude to every mapping, condition, value set, or model.

### 8. 10.3389/fpubh.2021.744405 — EQ-5D-5L level sum score in European health-inequality analysis

**Classification and purpose.** Population-health study, health equity or inequality study, and methods study; completed. The paper tests whether the multi-item EQ-5D-5L level sum score distinguishes education-related health inequalities better than EQ VAS in Italy, the Netherlands, and the United Kingdom.

**Components and provenance.** `S1 Italy`, `S2 Netherlands`, and `S3 United Kingdom` are country samples. `C1 transformed level sum score versus EQ VAS` is the main paired data-form comparison. `C2 education groups`, `C3 country groups`, and `C4 chronic-condition strata` preserve the main condition differences. `A1 descriptive and group tests`, `A2 univariate regression`, and `A3 country-specific multivariable regression` answer different questions. The paper analyzes a 2017 three-country web survey that it links to an earlier report and the CENTER-TBI study context. Treat this as related-data provenance. The article does not provide a stable data-set name or a complete cross-publication overlap statement.

**Evidence context and administration.** Respondents were adults aged 18 to 75 years in general-population internet panels. Survey Sampling International selected quota samples to represent age, gender, and education. Only complete questionnaires entered analysis. There were 10,172 respondents: 3,026 in Italy, 3,027 in the Netherlands, and 4,119 in the UK. Respondents reported their own current health, education, work, income, and chronic conditions. The paper does not state the exact administered language versions. The decision context was European public-health and social-policy analysis of health inequality.

**Instrument and score roles.** EQ-5D-5L profile responses supplied an unweighted level sum score from 5 to 25. The paper transformed it to a 0-to-100 direction in which higher means better health. This is not a utility and uses no preference weights. EQ VAS supplied a separate 0-to-100 self-rating. Education was an ISCED-based socioeconomic-status proxy. The comparison is between analytic data forms from one instrument family, not between two different respondent samples.

**Analysis path.** ANOVA and Kruskal-Wallis tests compared transformed level sum score and EQ VAS by country and low, middle, or high education. Stratified analyses repeated contrasts in people with and without specified chronic conditions. Univariate regressions related respondent characteristics to each outcome. Country-specific backward stepwise models started with age and sex and then considered education, work status, household income, and number of chronic conditions. The multivariable model estimates association, not causal mediation, even though the discussion uses explanatory language.

**Principal findings.** In the UK and the Netherlands, low education was associated with worse transformed level sum scores and EQ VAS. Italy did not show the same ordered pattern. Differences by education were usually slightly larger for the level sum score. The UK showed the strongest relations. In full multivariable models, number of chronic conditions and inability to work were strong predictors, and most education coefficients were no longer present. Some condition-specific exceptions favored EQ VAS, so the level sum score did not dominate every subgroup.

**Author interpretation and implications.** The authors interpret the level sum score as a slightly more discriminating health-inequality outcome than EQ VAS. They state that its added information must be balanced against the extra respondent burden of a multi-item measure. They also conclude that chronic morbidity and inability to work account for much of the observed education relation. Keep this as an association-based author interpretation, not causal proof.

**Limitations and transfer limits.** Internet and literacy requirements can exclude lower-socioeconomic-status groups. Quota representativeness does not give nonresponse data. Education alone does not cover all socioeconomic status. An Italian EQ-5D-5L value set was unavailable, so the study chose an unweighted score rather than an arbitrary foreign utility set. That choice supports profile-severity comparison but not QALY or welfare interpretation. Country differences can reflect response behavior and unmeasured context as well as health.

### 9. 10.3390/curroncol32060308 — Ontario oncology EQ-5D collection pilot

**Classification and purpose.** Implementation study; completed single-site pilot. The paper tests patient acceptability and repeat completion of real-world EQ-5D-3L collection during publicly reimbursed systemic cancer therapy. It uses the pilot to inform a planned Ontario-wide collection program.

**Components.** `S1 enrolled cohort` has 170 patients and one initial EQ-5D-3L. `T1 one or more follow-ups` has 103 patients. `Q1 optional feasibility and demographic questionnaire` has 160 respondents. `S2 interview volunteer pool` has 57 patients, and `T2 semi-structured interview` has nine participants. `A1 feasibility counts` and `A2 qualitative content analysis` remain separate. `P1 single-site pilot` is tested. `P2 provincial scale-up` is planned and was not implemented by this paper.

**Evidence context.** Adults with histologically confirmed solid or hematological cancer started any publicly reimbursed systemic therapy at Sunnybrook Odette Cancer Centre in Ontario. Recruitment was a convenience sample from May to November 2024 with follow-up through February 2025. Four coordinators screened appointment lists and approached patients during chemotherapy. The top condition groups included gynecological, head and neck, breast, hematological, and upper gastrointestinal cancers. The direct evidence comes from participating patients. Staff-reported workflow barriers also come from the study team. The target was routine collection across Ontario oncology care.

**Instrument, proxy, and administration.** EQ-5D-3L profile and EQ VAS were administered measures. Paper and REDCap forms were available, and all responses entered REDCap, but the paper does not give the actual count by self-completion medium. English EQ-5D-3L proxy version 1 was available for a caregiver to rate the patient from the caregiver's own opinion. The paper does not report how many proxy forms were used. EQ-5D-3L was selected for comparison with historic clinical-trial utilities. The authors later recommend EQ-5D-5L for wider implementation. This planned version change must stay separate from the tested 3L pilot.

**Feasibility and qualitative methods.** Main feasibility outcomes were initial participation, at least one repeat questionnaire, and willingness to answer at later visits. Follow-up count, not fixed-interval retention, was used. Nine two-on-one Zoom interviews examined overall experience, paper or digital presentation, collection frequency, and analysis or interpretation. Three researchers used inductive content analysis and developed a codebook as themes emerged. The paper does not report saturation or an independent double-code count.

**Principal findings.** All 170 enrollees completed an initial EQ-5D-3L, and 103 completed at least one follow-up. Of the 160 optional feasibility respondents, 115 said they would definitely continue and 35 said they were very likely to continue. Most rated the questionnaire clear, easy, acceptable, and short. Interviews supported feasibility but identified limited cancer-content coverage, small font, moment-to-moment treatment effects, and different preferences for paper, remote digital, or in-person support. Patients proposed collection before treatment, at selected treatment stages, or away from the infusion moment. Coordinators reported missed appointments, short treatments, sleeping or busy patients, language barriers, and high staff burden.

**Implementation product and interpretation.** `Sunnybrook oncology EQ-5D collection pilot and patient-informed scale-up recommendations`; completed single-site pilot with patient acceptability, repeat-completion, and qualitative evidence. The implementation stage is `pilot`. The authors interpret it as a template for use with Ontario's existing patient-reported-outcome platform. Province-wide collection, dashboards, and clinical or economic effects were not produced by this study. The article describes actual programs in Alberta and national orthopedic collection as external context, not as impact of this pilot.

**Limitations and gaps.** One center, convenience recruitment, English-language barriers, coordinator burden, and variable follow-up limit transfer. The interview sample had nine people from 57 volunteers. Infusion-day answers can depend on treatment timing, and EQ-5D-3L can omit cancer-specific experience. The authors plan inequity analyses, stakeholder consultation, electronic acceptability work, testing at more sites, and Ontario-wide scale-up.

**Source conflict.** `definition or denominator`: the abstract reports 115 as 67.3% and 35 as 20.5%, which uses all 170 enrollees. The main results report the same numerators as 71.9% and 21.9%, which uses the 160 optional feasibility respondents. Store the counts and both denominators; use 160 for the direct willingness-question analysis.

### 10. 10.1016/j.jval.2024.05.007 — psychometric performance of EQ-HWB-S in a UK population sample

**Classification and purpose.** Measurement-property assessment and mapping or scoring study; completed. The paper tests the construct validity and distribution of experimental EQ-HWB-S version 1.0 against EQ-5D-5L in a pooled United Kingdom general-population sample.

**Components and reuse.** `D1 E-QALY feasibility valuation data` has 429 respondents with both measures from 521 EQ-HWB-S valuation participants. `D2 UK EQ-5D-5L valuation pilot data` has 248 respondents with both measures. `D3 pooled analysis sample` has 677. `A1 response distribution`, `A2 convergent validity`, `A3 utility agreement`, and `A4 known-group validity` are distinct analysis streams. The paper reuses two valuation data sets and two existing scoring products. It does not collect a new sample or produce a definitive new value set.

**Data-source differences and harmonization.** D1 was collected from May to November 2021. Participants completed EQ-HWB-S before EQ-5D-5L in an online valuation interview. D2 was collected from October 2022 to February 2023, mostly online and partly face to face. Participants completed EQ-5D-5L before valuation exercises and EQ-HWB-S later. The long-term-condition question asks for a diagnosed lasting condition in D1 but asks for activity limitation in D2. The pooled binary variable combines these unlike definitions. Life satisfaction, health satisfaction, and carer status exist only for D1. These differences and availability rules must remain linked to the source components.

**Evidence context and administration.** All respondents were UK adult general-population members recruited by online advertising or targeted postal invitation. The pooled sample had 677 people, mean age 47 years, and 59% women. Respondents reported their own health and wellbeing. Most valuation contacts were online; D2 included 19% face-to-face interviews. Both instruments were self-completed within valuation-study sessions. The target contexts were health, public-health, and social-care economic evaluation, including possible use with patients, carers, and social-care users.

**Instrument and scoring paths.** Experimental EQ-HWB-S version 1.0 was the measurement-property target. Its nine items use a seven-day recall period and include mobility, activities, exhaustion, loneliness, cognition, anxiety, sadness or depression, control, and physical pain. It used the UK feasibility value set from cTTO, DCE, and a hybrid heteroskedastic Tobit model. EQ-5D-5L was the comparator and used `today`. Its main utility route mapped 5L profiles to the UK EQ-5D-3L value set under the stated NICE recommendation. An alternate value set supplied a known-group sensitivity analysis. Thus, utility agreement reflects both instrument content and different scoring routes.

**Measurement-property path.** Distribution analysis examined item floor and ceiling and full-instrument no-problem states. Spearman correlations tested overlapping and nonoverlapping items, while Pearson correlation tested utilities. Prespecified convergent pairs included mobility, activity, anxiety, depression, and pain. Bland-Altman plots, mean absolute difference, and Lin's concordance coefficient tested utility agreement. Known groups used EQ VAS, long-term-condition status, health satisfaction, life satisfaction, carer status, age, and employment. Mean differences and Cohen's d tested discrimination.

**Principal findings.** Full-health ceiling was 9.45% for EQ-HWB-S and 36% for EQ-5D-5L. Overlapping items and utility scores showed strong convergence. Loneliness, cognition, exhaustion, and control generally had weak or moderate relations with EQ-5D-5L, which supports added content rather than interchangeability. Utility concordance was high overall but had large individual outliers and a mean absolute difference of 0.17. Both measures strongly distinguished EQ-VAS health groups, long-term-condition groups, and health or life satisfaction groups. EQ-HWB-S also distinguished employment from unemployment or long-term sickness. Carer and age effects were small.

**Author interpretation and implications.** The authors interpret the results as favorable initial construct-validity evidence for the current experimental EQ-HWB-S. They identify possible value when EQ-5D-5L omits wellbeing content, especially in social care and carer contexts. They do not claim that EQ-HWB-S is interchangeable with EQ-5D-5L or adopted by NICE. A definitive EQ-HWB-S value set was still pending.

**Limitations and gaps.** The analysis pools different periods, modes, instrument orders, variable definitions, and partial covariate sets. D1 occurred during the COVID-19 pandemic. Both sources are valuation samples rather than condition-specific samples. The EQ-5D-5L crosswalk compresses its score distribution, and the two instruments use different recall periods. Future work must test disease and care groups, revisit comparisons with a definitive EQ-HWB-S value set and a new UK EQ-5D-5L value set, and assess responsiveness.

**Source conflict.** `summary versus main text`: the methods state that the mapped EQ-5D-5L route can range up to 0.960, while the results report an observed EQ-5D-5L utility maximum of 0.988. Retain both values as a scoring-report conflict. Do not infer which of the several tabled EQ-5D score routes produced the latter maximum without more source detail.

## Round 2 granularity decisions and evidence

### Decisions added or revised

16. **Represent score construction as a path, not as one utility field.** Paper 7 compares observed 5L utility, direct mappings to 3L utility, response mappings to 3L profiles, and SF-6D scoring. Paper 10 compares an EQ-HWB-S feasibility value set with an EQ-5D crosswalk. Paper 8 uses an unweighted level sum score and no utility. These routes can change QALYs, agreement, and interpretation. This supports user questions 3, 12, 13, 19, 20, 21, and 25.

17. **Record responsiveness by direction and anchor.** Paper 3 supports response to deterioration but not to improvement. The same paper uses a self-reported global transition anchor and different analysis groups at six months. A single `responsive` label would overstate the result. This supports questions 9, 12, 13, 15, 16, and 22.

18. **Separate implementation stage from product maturity and planned scale.** Paper 9 completes a single-site 3L pilot, recommends 5L for later scale-up, and cites external routine systems. None of these facts means that Ontario had routine EQ-5D collection. The new implementation-stage terms prevent false claims of adoption. This supports questions 14, 17, 18, 23, and 24.

19. **Keep source, reference, and target versions separate in translation.** Paper 5 uses UK English EQ-5D-Y-5L as the source, Egyptian Arabic EQ-5D-Y-3L as a wording reference, and Modern Standard Arabic EQ-5D-Y-5L as the target. Without these roles, a query can mistake the 3L reference for the translated product. This supports questions 3, 4, 9, 13, 14, 20, and 23.

20. **Use separate product axes for development, evidence, governance, availability, and use.** Paper 5 reports a final version-management output with cognitive testing but no published psychometric result or value set. Paper 4 assesses an experimental version but produces recommendations, not a revised instrument. Paper 9 tests a workflow but has not scaled it. One ladder cannot represent these states without overstatement. This supports questions 14, 16, 17, 18, and 23.

21. **Record proxy use only with an observed administration relation.** Paper 4 discusses the choice and bias of future EQ-TIPS proxies but collects only expert views. Paper 9 makes proxy version 1 available but does not report a proxy-use count. A proxy topic or available form is not observed proxy evidence. This supports questions 6, 11, 13, 20, and 24.

22. **Keep pooled data sources and harmonization rules explicit.** Paper 10 pools two valuation samples with different periods, modes, instrument order, long-term-condition definitions, and covariate availability. A pooled sample total alone hides conditions that can explain results. This supports questions 5, 8, 11, 13, 16, 19, and 25.

23. **Add health economic evaluation or decision-model study as a family and give it a domain method path.** Paper 7 uses a Markov model, societal perspective, ten-year horizon, utility routes, QALYs, ICERs, and bootstrap uncertainty. `Mapping study` alone does not retrieve the decision consequence. The family remains repeatable with `mapping or scoring study` and `methods study`. This supports questions 1, 9, 12, 13, 17, 20, and 21.

24. **Keep direct utility mapping and response mapping distinct.** Paper 7 shows different targets, algorithms, prediction behavior, and uncertainty. These are stable method types with different transport assumptions. This supports questions 9, 12, 13, 20, and 21.

25. **Represent adaptive design and quality exclusions as method details when they change validity.** Paper 2 updates its DCEd design three times and later discards a complete recruiter mode because of speeding and flatlining. Paper 1 uses staged interviewer qualification and periodic pauses. Broad tags such as `DCE` or `quality control` would hide why data were retained or excluded. This supports questions 8, 9, 10, 11, 12, 13, and 16.

26. **Separate population membership rules from preference target.** Paper 1 defines the UAE general-population basis to include nationals and expatriates with at least five years of residence. Citizenship, residence duration, interview language, and target population are related but not interchangeable. This supports questions 6, 7, 8, 13, 20, and 24.

27. **Treat level sum score as a score form, not as utility.** Paper 8 transforms an equal-weight sum for direction and scale. It deliberately avoids foreign value sets. This score can support profile-severity and discrimination analyses but not QALY interpretation. This supports questions 3, 12, 13, 20, 21, and 22.

28. **Use a small controlled source-conflict type with local narrative.** Papers 1, 4, 9, and 10 supply repeated evidence for summary-main-text, arithmetic, denominator, and scoring conflicts. The type supports audit and later retrieval, while the exact statements stay in narrative. This resolves part of round-1 unresolved case 8 and supports question 16.

29. **Broaden the implementation family to include feasibility studies.** Paper 9 is not a professional-practice survey and does not yet document scaled implementation. The term `implementation, feasibility, or practice study` retrieves it without forcing a completed adoption claim. This supports questions 1, 14, 17, 20, and 21.

30. **Keep method-comparison evidence separate from a reusable product.** Paper 2 produces comparative evidence about DCEd and EQ-VT, but it does not recommend an operational Trinidad and Tobago value set in this paper. Paper 6 tests nine bolt-ons but produces no valued bolt-on instrument. This avoids inflating the product inventory for questions 14 and 23.

### Important distinctions considered and rejected in round 2

- **One field for any EQ-5D utility:** rejected. It would mix observed profile scoring, crosswalk, direct mapping, response mapping, and non-EQ-5D utility routes.
- **`Responsive` without improvement or deterioration direction:** rejected. Paper 3 has materially asymmetric evidence.
- **`Implemented` for a successful pilot:** rejected. Paper 9 tests one site and plans scale-up.
- **`Validated translation` as one status:** rejected. Paper 5 supplies linguistic, governance, and cognitive evidence but not the published psychometric and valuation evidence that this broad label can imply.
- **Treating a source-language or reference version as the produced translation:** rejected. Paper 5 requires three version roles.
- **Treating availability of a proxy form as proof of proxy use:** rejected. Paper 9 does not report the number of proxy completions.
- **Treating expert views about a child instrument as child or caregiver response data:** rejected. Paper 4 includes experts only.
- **Treating an empirical DCEd discount factor as a jurisdictional economic discount rate:** rejected. Paper 2 uses it to separate time preference from health-state preference.
- **Treating direct and response mapping as one method:** rejected. Paper 7 maps to different target data forms.
- **Treating a level sum score as a value set or preference-weighted utility:** rejected. Paper 8 uses an equal-weight aggregation.
- **Collapsing pooled samples before source definitions are recorded:** rejected. Paper 10's long-term-condition variables are not the same question.
- **Treating every bolt-on combination as a product or component:** rejected. Paper 6 tests many analytic combinations. Only the material analysis stream and selection rule need structure.
- **Treating cited routine programs as the focal paper's documented impact:** rejected. Paper 9 cites Alberta and national programs as context, not effects of the Ontario pilot.
- **Treating loss of a regression coefficient as proof of causal mediation:** rejected. Paper 8 reports cross-sectional associations and stepwise models.
- **A product for every method comparison:** rejected. Paper 2 gives evidence about method agreement, and paper 6 gives item-selection evidence, but neither creates an operational product in the paper.
- **A component for each of ten valuation candidate models in paper 1:** rejected. Keep cTTO, DCE, and hybrid streams, then store candidate names within them. Separate components for each model add structure without a new evidence source or task.
- **A controlled category for every reported barrier or theme:** rejected. Paper 9's implementation barriers and paper 4's expert themes are clearer as concise structured lists linked to their component.

## Status of unresolved cases after round 2

1. **Product maturity is partly resolved.** Papers 4, 5, 9, and 10 show that one ladder is not sufficient. The guide now separates development, evidence, governance, availability, recommendation, and documented use. Later products must test the exact controlled terms for each axis.
2. **Mixed paper and component status remains useful.** Paper 9 confirms that a completed pilot and planned scale-up can coexist. The current paper-level status plus component-specific implementation stage is sufficient in this batch.
3. **Content validity, concept elicitation, and cultural adaptation remain separate but linked.** Paper 4 assesses expert relevance, comprehensibility, and comprehensiveness without revision. Paper 5 performs translation and cognitive adaptation. These papers support separate study families or stages. The boundary for a study that both elicits concepts and revises an instrument still needs later evidence.
4. **Unusual scale-type DIF remains unresolved.** Batch 02 adds no second case that tests the paper-7 round-1 focal and reference scale issue.
5. **Evidence-level country and language in large reviews remains unresolved.** Batch 02 has no new systematic review.
6. **Review publication, study, trial, and data-set cardinality remains unresolved.** Batch 02 has reused and pooled primary data, but it does not add a review with more complex evidence units.
7. **External age-validity rules remain out of scope.** Paper 5 directly includes the stated 8-to-15 target ages. It does not resolve the round-1 paper that included older adolescents.
8. **Source-conflict handling is partly resolved.** Four round-2 papers support a small controlled type plus local narrative. Later rounds must test whether `definition or denominator` and `summary versus main text` stay stable or overlap.
9. **Proxy perspective terminology needs more application evidence.** Paper 9 names proxy version 1 and its own-opinion perspective but gives no observed proxy count. Later direct proxy studies must test the controlled perspective values.
10. **Implementation-stage terms need calibration.** `Pilot` is clear for paper 9. The boundary between limited routine use and scaled routine use needs a paper with documented operational collection.
11. **Mapping transport needs a concise representation.** Paper 7 shows that development population, target population, source measure, target version, and value set all matter. Later mapping papers must test whether these remain one path or need a repeatable transport-assessment entry.
12. **Pooled-variable harmonization can remain narrative for now.** Paper 10 has one important binary variable with different source definitions. More complex pooled studies can show whether a controlled harmonization-relation type is necessary.
13. **Scoring-source conflicts can be difficult to resolve from one article.** Paper 10 reports several EQ-5D score routes and conflicting upper values. Keep the local conflict rather than infer a mislabeled algorithm. Later scoring papers can test whether a dedicated scoring-version identifier is practical.

## Round 2 run note

This round extended the preserved round-1 Candidate 2 record with all ten batch-02 applications. All ten assigned article files matched the manifest SHA-256 values and byte counts. The main additions are score-construction paths, direction-specific responsiveness, translation version roles, proxy evidence boundaries, implementation stage, economic-evaluation detail, pooled-source harmonization, and controlled source-conflict types. The product guidance now uses separate status axes instead of one implied maturity ladder. One initial verification command used `status`, which is a read-only zsh variable. It stopped before it could print results or change files. A corrected command used `verify_state`, and all checks passed. No fixed JSON schema was used.

## Applications to batch 03

### 1. 10.3390/curroncol32110645 — income and EQ-5D-3L utility in Ontario oncology

**Classification and purpose.** Health equity or inequality study and population-health study; completed. The paper tests whether age, sex, education, marital status, employment, family income, ethnicity, and cancer site are associated with EQ-5D-3L utility in a real-world cancer sample. Its intended use is equity-informed HTA and future economic modeling.

**Components and reuse.** `D1 Ontario oncology collection pilot` is the cohort reported in the earlier implementation paper, 10.3390/curroncol32060308. This paper reuses the initial EQ-5D-3L responses and demographic data. `S1 all-cancer analysis` has 170 patients and omits birth sex from the model. `S2 non-sex-specific-cancer analysis` has 111 patients and includes birth sex after breast, gynecological, and prostate cancers are removed. `A1 income-dimension association`, `A2 all-cancer OLS`, `A3 birth-sex OLS`, and `A4 age-by-birth-sex interaction test` are separate analysis streams. This is dependent evidence from the pilot, not a new sample.

**Evidence context.** Adults with a solid tumor or hematological malignancy started publicly reimbursed systemic therapy at Sunnybrook Odette Cancer Centre in Toronto, Canada. Recruitment was a prospective convenience sample during chemotherapy appointments from May through November 2024. Patients reported their own health and optional demographic information. The sample was older and more highly educated than the wider Ontario population and included several cancer sites. The target context was real-world oncology utility and Canadian HTA, not national population norms.

**Instrument and score path.** EQ-5D-3L profile and EQ VAS were collected, but EQ-5D-3L utility was the primary analyzed outcome. The score path was `EQ-5D-3L profile -> Canadian EQ-5D-3L TTO value set -> utility`. Dimension levels were analyzed separately against ordered income. EQ VAS was not a reported outcome in the association models. The questionnaire was completed during a treatment visit. This paper does not restate the number of paper and REDCap completions from the source pilot.

**Equity and analysis path.** Family income was a categorical exposure, with at least CAD 150,000 as the privileged reference and `prefer not to answer` retained as a category. OLS multivariable models estimated conditional utility differences. ANOVA tested the interaction, and BIC compared nested models. Spearman correlations linked ordered disclosed-income bands to each EQ-5D-3L dimension. These are associations. They do not identify a causal effect of income or financial toxicity.

**Principal findings.** Family income below CAD 30,000 and undisclosed income were associated with lower utility in both main models. Lower income was also associated with more pain or discomfort and anxiety or depression problems. Colorectal cancer had a higher utility than the head-and-neck reference group. The age-by-birth-sex interaction was not significant.

**Author interpretation and implications.** The authors interpret income as an important source of utility heterogeneity in cancer. They suggest that trial-based utilities from selected and advantaged samples can overestimate real-world health and that equity-informed HTA should consider real-world utility and socioeconomic position. These are author-reported research and policy implications. The direction of any change in incremental QALYs remains unclear, and the paper documents no changed HTA decision.

**Limitations and stated gaps.** The analysis is cross-sectional, single-site, small, and subject to wide uncertainty. It does not adjust for cancer stage, comorbidity, or other unmeasured confounding. EQ-5D-3L ceiling effects can reduce discrimination. The authors call for wider longitudinal collection, analysis of changes after diagnosis, gender analysis in a larger sample, and use in distributional cost-effectiveness analysis.

### 2. 10.1016/j.jval.2018.05.002 — crossed wording and perspective valuation experiment

**Classification and purpose.** Health-state valuation study and methods study; completed. The paper tests the joint effects of EQ-5D-3L versus EQ-5D-Y wording and adult-self versus hypothetical-child perspective on health-state values.

**Components.** A two-by-two design creates four randomized `experimental arm` components: `3L-adult`, `3L-child`, `Y-adult`, and `Y-child`. Each arm contains `T1 response-label ranking`, `T2 cTTO`, and `T3 DCE plus immediate-death comparisons`. `A1 two-factor cTTO interaction`, `A2 arm contrasts`, and `A3 DCE choice comparison` analyze the tasks. The instrument factor and perspective factor must remain crossed because the interaction prevents a valid independent main-effect summary.

**Evidence context.** The 805 respondents were adult general-population members from Germany, the Netherlands, Spain, and England. Convenience recruitment differed by country, but teams monitored age and sex. Respondents were randomly assigned to one arm. Under the adult perspective, respondents imagined their own health. Under the child perspective, they imagined an unspecified 10-year-old child. This perspective changes both referent age and self-versus-other relation. It does not collect preferences from children.

**Instrument, task, and administration.** EQ-5D-3L and EQ-5D-Y were sources of health-state wording and valuation targets. Exact administered language versions are not stated in the extracted methods. An adapted EQ-VT protocol used computer-assisted personal interviews, trained interviewers, pilot interviews, and EQ-VT quality control. Interviews took place at central sites in Germany, Spain, and the Netherlands and in respondent homes in England. Each respondent valued nine cTTO states. The DCE sequence had nine paired-state choices and a comparison of each state with immediate death, for 27 choices. cTTO used conventional and lead-time paths through the composite procedure.

**Design and analysis path.** The cTTO design used 17 states in two blocks, with 33333 in both. A two-way MANOVA first tested wording-by-perspective interaction. Bonferroni-adjusted Hotelling and t tests then compared arms and states. Chi-square tests compared DCE and death choices. A technical error omitted the intended second DCE block. Therefore, the DCE evidence covers only the implemented states and has limited alignment with the cTTO design.

**Principal findings.** cTTO showed a significant wording-by-perspective interaction. Perspective differences occurred for EQ-5D-3L, and instrument-wording differences occurred under the adult perspective. The severe state 33333 did not differ across arms. Child-perspective values were generally higher, and immediate death was chosen less often for the child referent, but the Netherlands showed the opposite direction in a country-level pattern. The study was not powered for full country-specific inference.

**Author interpretation and implications.** The authors conclude that adult EQ-5D-3L value sets must not score EQ-5D-Y states. They interpret wording and perspective as changing relative dimension or level importance and possibly the meaning of the death anchor. They raise possible consequences for child and adult QALY comparisons and thresholds, but these are author-reported methodological and policy implications, not tested decision rules.

**Limitations and stated gaps.** The DCE implementation error reduced the state coverage and prevented the planned DCE model comparison. Country recruitment and unobserved characteristics differed. Pooled data could hide country effects. Adult-self and child-other framing prevents attribution to age alone. The authors call for more work on death anchoring, child perspective, country differences, and child-specific valuation methods.

### 3. 10.1007/s40273-018-0642-5 — systematic review of EQ-5D-3L and 5L measurement properties

**Classification and purpose.** Systematic review or evidence synthesis and measurement-property assessment; completed. The paper compares the final EQ-5D-3L and EQ-5D-5L descriptive systems for missing data, distribution, informativity, response inconsistency, responsiveness, and test-retest reliability.

**Components and evidence units.** `R1 2007-May 2016 search` and `R2 May 2016-January 2018 update` produce `E1 24 included articles`. `A1 missing and distribution`, `A2 Shannon informativity`, `A3 paired-response inconsistency`, `A4 responsiveness`, and `A5 test-retest reliability` are separate property syntheses. The evidence units are publications. Eight cover general-population samples and 16 cover patient samples across 18 countries. Twenty-two are direct head-to-head studies.

**Review method and duplicate handling.** PubMed, EMBASE, PsycINFO, and the EuroQol website were searched for English or German primary studies and conference papers in adults. Experimental instrument versions were excluded. Two reviewers independently screened titles and abstracts. One reviewer extracted full texts and a second checked for omissions. If papers used the same data, the review retained the paper with more information for a duplicated indicator and retained both only when they supplied different indicators. A nine-item observational-study appraisal classified all included papers as good or excellent. Random-effects logit models pooled full-health proportions. Other findings were summarized as ranges and comparative counts because design heterogeneity limited pooling.

**Measurement-property path.** Distribution covered missing responses, dimension and profile ceilings, and floors. Shannon H and J assessed absolute and relative informativity. Inconsistency mapped 3L levels to 5L levels 1, 3, and 5 and treated a paired difference greater than one level as inconsistent. Responsiveness used effect size, standardized response mean, probability of superiority, Wilcoxon tests, anchors, and area under the ROC curve where available. Reliability used ICC, kappa, weighted kappa, and percentage agreement. Index-level responsiveness often used 5L-to-3L crosswalk scores, which is a scoring-route limit.

**Principal findings.** Missing data and profile floors were generally low for both versions. The 5L usually reduced ceiling effects and always had higher Shannon H. Relative Shannon J was similar or better in most studies. Inconsistencies were usually below 5%, with usual activities highest on average. Responsiveness evidence came from only three studies and was mixed. Six reliability articles gave no clear dimension-level winner, while index ICCs often favored 5L.

**Author interpretation and implications.** The authors support both versions across broad adult contexts and find modest distribution and substantial absolute-informativity advantages for 5L. They suggest 5L when discrimination among mild states is important. They state that instrument choice must also consider population, language version, administration, value-set availability, and purpose. This is comparative measurement evidence, not a guideline product.

**Limitations and stated gaps.** Populations, languages, value sets, order, interval, and methods varied. Responsiveness and reliability evidence was sparse, and crosswalk scoring could compress 5L change. The authors call for more sensitivity-to-change and reliability research and for reporting standards for preference-based measures.

### 4. 10.1016/j.jval.2023.03.003 — cTTO-only EQ-5D-Y-3L value-set modeling

**Classification and purpose.** Health-state valuation study and methods study; completed. The paper tests whether a sufficiently large cTTO design can estimate an EQ-5D-Y-3L value set without DCE data.

**Components and reuse.** `D1 Chinese EQ-5D-Y-3L cTTO data` reuses all 418 cTTO respondents from the earlier Chinese valuation paper, 10.1007/s40273-022-01216-9. `A1 task feasibility`, `A2 cTTO distribution`, and `A3 cTTO-only models` are separate streams. `C1 adult Chinese EQ-5D-5L cTTO comparison` uses published results as a feasibility reference. No new respondent sample was collected, and this analysis does not use the source study's DCE data.

**Evidence context and administration.** Adult Chinese general-population respondents were quota sampled by sex, age, education, and rural or urban hukou in eight provinces or cities. Recruitment used public places and interviewer networks. Each respondent valued the health of a hypothetical 10-year-old child in a face-to-face, one-to-one, computer-assisted EQ-VT interview. Eight interviewers received two days of training and continuing quality review. The exact administered language version is not stated in this brief paper.

**Task and modeling path.** Twenty-eight EQ-5D-Y-3L states were split across three ten-state blocks, with 33333 in each. Respondents completed warm-up and practice work, then ten cTTO tasks. Feasibility used interview time, moves to indifference, and three respondent feedback questions. Two model specifications used main effects alone or main effects plus an `All 3` term for 33333. OLS, heteroscedastic, and random-effects models were compared for monotonicity, coefficient significance, uncertainty, and leave-one-state-out MAE.

**Principal findings.** Interviews took a mean of 35.7 minutes. Most respondents reported that the task was easy to understand and states were easy to distinguish, while 11.5% reported difficulty deciding. About 21.9% of values were negative, and one respondent was a non-trader. State 33333 was the only state with a negative mean and had a large gap from the next state. All models with the All-3 term were monotonic. The random-effects model had the lowest cross-validation MAE and more precise coefficients.

**Product and states.** `Chinese cTTO-only EQ-5D-Y-3L scoring model`; completed candidate model from a secondary analysis and author-proposed as a future valuation option. Its evidence is feasibility assessment, model comparison, and cross-validation on the reused cTTO sample. It is not a second operational Chinese national value set. The source valuation study selected a hybrid product that used both cTTO and DCE.

**Author interpretation, limitations, and gaps.** The authors interpret the smooth distribution, feedback, and model performance as evidence that cTTO-only youth value sets can be feasible when enough states are valued. They state that this route avoids uncertain hybrid modeling. Transfer is limited by nonprobability recruitment, modest over-representation of women and higher education, a single national sample, and the child referent. The adult-5L comparison also differs in referent and quality control. The paper calls for cTTO-only consideration in later youth valuation studies while the best way to combine cTTO and DCE remains unsettled.

### 5. 10.1038/s41433-023-02860-x — societal cost of vision impairment in Trinidad and Tobago

**Classification and purpose.** Cost-of-illness or burden-of-disease study and population-health study; completed. The paper estimates the 2014 societal cost of presenting distance and near vision impairment among people aged at least 40 years in Trinidad and Tobago.

**Components and reuse.** `D1 2014 National Eye Survey of Trinidad and Tobago` supplies household sampling, visual acuity, clinical assessment, utilization, socioeconomic, employment, and informal-care evidence. `D2 2014 national eye-care-system survey` supplies provider activity and unit costs. `D3 census and external parameter sources` supplies population, wages, disability weights, value of statistical life, and some unit costs. Cost streams are `C1 direct medical`, `C2 direct non-medical`, `C3 productivity and sick leave`, `C4 informal care`, and `C5 intangible wellbeing loss`. `A1 prevalence extrapolation`, `A2 cost aggregation`, `A3 bearer allocation`, and `A4 one-way sensitivity analysis` link these sources.

**Evidence context.** A multistage probability-proportional-to-size household sample covered 9,913 eligible people, including 4,263 aged at least 40 years. Visual acuity was measured for 3,589. Medical or ophthalmic questionnaires were available for 2,792 and socioeconomic questionnaires for 2,516. Clinic respondents reported their own use, costs, employment, and care. Results were weighted for survey design, cluster response, age, sex, municipality, and finite-population stages. The target was the non-institutional population aged at least 40 years in Trinidad and Tobago in 2014.

**EuroQol and health-loss boundary.** No EuroQol instrument was administered, scored, analyzed, reviewed, or produced in this paper. QALYs are mentioned only to contrast them with DALYs and to cite a prior analysis. Wellbeing loss used external vision-impairment disability weights to estimate prevalent years lived with disability, with years of life lost set to zero. The authors then monetized a year of wellbeing through a country-level value-of-statistical-life calculation. These are DALY and monetary-loss paths, not EQ-5D utility or a QALY result.

**Economic method path.** The paper used a societal perspective and a 2014 prevalence basis. Direct costs combined reported service use with public or private unit costs. Productivity used a human-capital employment-gap method. Informal care used an opportunity-cost wage. Transfer payments and dead-weight losses were reported or considered but excluded from final societal cost. Costs were assigned to individuals, families, government, health care, insurers, and employers under stated assumptions. Values were converted to 2014 Trinidad and Tobago dollars and UK sterling. Sensitivity analysis varied confidence limits, unavailable parameters by 50%, alternative wages, and alternative disability weights.

**Principal findings.** Total societal impact was estimated at TT$3.842 billion, or UK£365.7 million. Monetized wellbeing loss supplied 73.3%. Excluding it, total economic cost was TT$1.025 billion. Indirect costs supplied 70.5% of that subtotal, followed by direct medical and direct non-medical costs. The study estimated 64,431 cases of distance impairment, of which about 86% were potentially avoidable, and 120,842 cases of avoidable near impairment. Affected people and families bore most of the total cost. Results differed greatly under alternative disability weights.

**Author interpretation and implications.** The authors describe the estimates as a national benchmark for eye-care investment and later cost-effectiveness work. They argue that health-sector costs alone omit most societal burden and identify possible investment in prevention, spectacles, low-vision support, workforce enablement, and public access to treatment. These are author-reported policy implications. The analysis does not compare interventions or calculate an ICER.

**Limitations and stated gaps.** Response was 59% to 66% for key cost questionnaires, with possible under-representation of blind and housebound people. The study excludes institutions, long-term care, some injury and depression costs, transfer payments, dead-weight loss, and caregiver opportunity cost beyond valued hours. Recall covered up to 12 months. Several costs depend on assumptions, and monetizing DALYs is conceptually and ethically disputed. The authors call for international standardization of cost-of-vision study design and measurement tools.

### 6. 10.1177/0272989x251325828 — immediate death, duration anchoring, and nonlinear time preference

**Classification and purpose.** Health-state valuation study and methods study; completed. The paper asks whether a DCE tariff should be anchored on immediate death or zero duration and whether nonlinear time preference changes agreement with cTTO.

**Components and reuse.** `D1 retained Trinidad and Tobago DCEd sample` reuses the 970 respondents analyzed in the earlier direct DCEd and EQ-VT comparison, 10.1016/j.jval.2024.05.016. `T1 equal-duration state choice`, `T2 shorter full-health duration`, and `T3 immediate-death choice` are linked parts of the split triplet. Four model conditions cross `linear versus exponential nonlinear time` with `immediate-death versus duration anchor`. `C1 cTTO tariff benchmark` compares these models with the independently collected Trinidad and Tobago EQ-VT product from paper 7. The cTTO raw respondent data are not pooled with D1.

**Evidence context and administration.** Respondents were adults from the Trinidad and Tobago general population. The source study used age, sex, and geography quotas. The retained sample came from a wider web and recruiter-assisted collection after source-study quality exclusions. Respondents self-completed 18 split triplets. Fifteen used a shorter period in full health as the third life, and three used immediate death. Health-state durations ranged from six months to 15 years. The referents were hypothetical EQ-5D-5L lives, not respondents' own current health.

**Task design and modeling.** Each first choice compared two lives of equal duration that differed on three EQ-5D-5L dimensions. The second choice compared the retained impaired life with full health for a shorter duration or immediate death. The adaptive design started near orthogonal and was updated after the first 211 responses and later 200-response batches. Bayesian mixed logit models used respondent-specific health coefficients. One fixed time as linear. The other estimated an exponential discount parameter. Each model was then scaled by the immediate-death coefficient or the full-health duration coefficient. OpenBUGS chains, convergence checks, utility range, and state-level correspondence supplied the evaluation path.

**Principal findings.** The estimated annual time-preference parameter was about 23%. Under linear time, immediate death had a utility near -2.1 when duration supplied the anchor. Under nonlinear time, it was near -0.28. Anchoring on immediate death compressed and raised the health-state scale. Nonlinear time with duration anchoring produced a 55555 value near -0.54 and the closest population-level agreement with the cTTO value near -0.61. The other anchor and time combinations had poor scale agreement.

**Product and states.** The four DCE-based tariffs are completed comparative analytic outputs from the model experiment. They are not separate operational Trinidad and Tobago value sets. The completed cTTO and DCE hybrid national value set remains the benchmark product. The time-preference parameter is part of health-state valuation and is not a jurisdictional economic discount rate.

**Author interpretation and implications.** The authors state that immediate death does not behave like zero duration and that a DCEd design must identify nonlinear time preference. They recommend duration anchoring and suggest removal of immediate-death tasks when full-health duration tasks supply the anchor. This is author-reported valuation guidance based on one country and instrument.

**Limitations and stated gaps.** Country and cultural transfer are uncertain. DCEd had no interviewer debrief, so speeding exclusions cannot prove task understanding. cTTO and DCEd used different respondents, which permits population-level but not individual-level agreement. The paper does not establish that the model transfers to other instruments despite the authors' reasoned expectation.

### 7. 10.1186/s12955-024-02266-7 — Trinidad and Tobago EQ-5D-5L value set

**Classification and purpose.** Health-state valuation study, value-set development, and methods study; completed. The paper develops a directly elicited EQ-5D-5L value set for Trinidad and Tobago and compares it with the existing 5L crosswalk from the 2016 national 3L value set.

**Components.** `S1 valuation sample` supplies `T1 cTTO` and `T2 DCE without duration`. `Q1 pilot, interviewer qualification, and continuing EQ-VT quality control` governs data collection. `A1 cTTO models`, `A2 DCE models`, and `A3 hybrid models` remain separate. `A4 feedback-exclusion sensitivity`, `A5 leave-state-out prediction`, and `A6 leave-block-out prediction` test robustness. `C1 direct value set versus crosswalk` compares the new and existing products.

**Evidence context.** The study used a target of 1,000 adult general-population respondents with quotas for age, sex, and the administrative regions of Trinidad and Tobago. A market-research firm randomly selected streets, visited one in four houses, and used the most recent birthday to select one adult. The final sample had 1,079 respondents and a reported 34% response rate. Data were collected from July through September 2022. Respondents valued hypothetical adult EQ-5D-5L states. The preference target and decision context were national utility scoring, clinical research, QALYs, and resource allocation.

**Instrument, task, and administration.** EQ-5D-5L was the valuation target, source of health-state descriptions, and an initial self-completed health measure. EQ VAS was also self-completed. EQ-VT version 2.1 delivered face-to-face computer-assisted personal interviews. Each respondent completed ten cTTO states from the standard 86-state design and 12 DCE pairs from 20 Bayesian-efficient blocks. cTTO used conventional TTO for better-than-dead states and lead-time TTO for worse-than-dead states, followed by the feedback module.

**Quality and modeling path.** Fourteen interviewers received one week of training and pilot work. Four were removed after quality failure. Batches were flagged for insufficient task explanation, short practice or main-task time, or a large 55555 ordering inconsistency. The sample supplied 10,790 cTTO and 12,948 DCE observations. cTTO candidates included random-intercept, censored Tobit, heteroskedastic, and heteroskedastic Tobit models. DCE used conditional and mixed logit. Hybrid forms modeled both sources. Heteroskedasticity, censoring, coefficient consistency, significance, MAE, and two cross-validation paths informed selection. The hybrid heteroskedastic Tobit was selected because single-state prediction was prioritized.

**Product and states.** `Trinidad and Tobago EQ-5D-5L value set`; completed named national value set and author-recommended for local QALY and decision use. Its evidence is the reported EQ-VT valuation, model comparison, and prediction checks. It covers all 3,125 profiles and ranges from -0.563 to 1.000. The authors suggest regional reference use only for settings with similar populations. This is not evidence of validation or use in each Caribbean jurisdiction.

**Principal findings and author interpretation.** Pain or discomfort had the largest decrement, then mobility, anxiety or depression, self-care, and usual activities. The new set had lower mean values, a wider range, and many more negative profiles than the crosswalk. The authors relate the difference to protocol, quality control, direct 5L wording, crosswalk transport from European data, and possible preference change since the older 3L study. These explanations are author interpretations and are not separately identified causal effects.

**Limitations and gaps.** Some age-sex and education groups were over-represented. Interviewer protocol problems and small interviewer effects remained despite quality control. The paper recommends current local values and later review as methods and preferences change.

**Source conflict.** `summary versus main text`: the abstract reports 236 negative profiles, or 7.6%, while the main results report 275, or 8.8%. Use the main-results count for the detailed comparison and retain the abstract count as a conflict.

### 8. 10.1186/s12955-024-02323-1 — updated Trinidad and Tobago norms and inequality

**Classification and purpose.** Population-health study, population-norm study, and health equity or inequality study; completed. The paper produces 2022-2023 EQ-5D-5L population norms, measures inequality, and compares them with 2012 norms under a common scoring route.

**Components and reuse.** `D1 2022 EQ-VT survey` reuses all 1,079 respondents from paper 7. `D2 2022-2023 DCEd survey` reuses the retained 970 respondents from the earlier DCEd papers. `D3 2023 norms-only panel survey` adds 940 respondents. These make `S1 current pooled sample` of 2,989. `D4 2012 norms data` supplies 2,036 earlier profiles. `A1 current norms`, `A2 demographic comparisons`, `A3 ordered-logit inequality`, `A4 Kakwani inequality`, and `C1 harmonized 2012-current comparison` are separate streams.

**Evidence context and source differences.** Respondents were adults from the Trinidad and Tobago general population. D1 used household recruitment and face-to-face computer-assisted valuation interviews. D2 used panel web links and recruiter-assisted digital completion before the source study removed 611 poor-quality cases. D3 used e-mailed panel links and collected only EQ-5D and demographics. D1 and D2 also contained valuation tasks that are not outcomes in this norms analysis. Employment exists only for D3. The three sources used different incentives. Their separate modes, variables, and quality routes must stay linked to each component.

**Instrument and harmonized score path.** Respondents self-completed the Trinidad and Tobago English EQ-5D-5L digital form and EQ VAS. Current profile utility used the 2024 directly elicited Trinidad and Tobago 5L value set from paper 7. For the temporal comparison, the paper rescored 2012 EQ-5D-5L profiles with the same 2024 value set. This holds scoring constant and replaces the earlier crosswalk only for the comparison. Profile ceiling, EQ VAS, and utility remain separate outcomes.

**Equity method.** Norms were stratified by age-sex and by income, education, ethnicity, marital status, employment, insurance, and work type where available. Welch tests and ANOVA compared means. Ordered logit models used dichotomized demographic factors to match the 2012 analysis. Modified Kakwani indices quantified and decomposed inequality for current utility and EQ VAS. The Kakwani EQ VAS comparison reused the 2012 result; no 2012 utility index was available.

**Product and states.** `Trinidad and Tobago 2022-2023 EQ-5D-5L population norms`; completed dated national reference product and author-recommended until a later update. The product includes profile, utility, EQ VAS, ceiling, age-sex, and demographic results. It updates the 2012 reference and is not a new value set. Downstream routine use is not documented here.

**Principal findings.** Current mean utility was 0.921, mean EQ VAS was 79.6, and the ceiling was 31.5%. Pain or discomfort and anxiety or depression had the highest problem rates. The current Kakwani indices were 0.058 for utility and 0.113 for EQ VAS. The 2012 EQ VAS index was 0.103. Rescored utility, EQ VAS, and ceiling were lower in 2022-2023 across the reported demographic comparisons, with some nonsignificant utility contrasts. Mild problems accounted for much of the profile change.

**Author interpretation and implications.** The authors interpret the results as lower reported population health and greater inequality after ten years. They suggest that health, perception, and social context can change and recommend periodic norm updates. They discuss the pandemic and mental-health salience as possible contributors but do not establish these causes. This is a documented update to a research reference product, not proof of a policy effect.

**Limitations and unresolved source statements.** Mixed modes, panel selection, incentives, categorical age ending at 65+, harmonized dichotomies, and measures limited to EQ-5D constrain interpretation. Some overlap between D1 and the panel sources was possible even though efforts were made to prevent it. `summary versus main text`: the abstract and later discussion end collection in May 2023, while the survey-specific methods state that D3 ran from March through August 2023. Use the survey-specific period and retain the May statement as a conflict. `scope or overlap`: the abstract calls samples mutually exclusive, while the limitations state that duplication between the household and panel sources may have occurred. Do not assert proven independence.

### 9. 10.1007/s11136-025-04074-y — EQ-DAPHNIE data-quality controls

**Classification and purpose.** Research-infrastructure study and methods study; completed quality analysis within an ongoing program. The paper describes how the UK pilot changed the EQ-DAPHNIE survey and reports quality indicators for the full 15-country collection.

**Components and reuse.** `P1 UK pilot` has 3,012 completers and tests six randomized survey versions. It precedes `P2 main soft launches` and `P3 full 15-country collection`, which has 68,411 completers from a 175,392-person panel frame. `Q1 bot detection`, `Q2 speeding`, `Q3 duplicate control`, `Q4 completion flow`, `Q5 missingness and outliers`, `Q6 repeated-item consistency`, and `Q7 quota monitoring` are distinct quality streams. The paper reuses the EQ-DAPHNIE samples and protocol described in 10.1007/s11136-025-03983-2. Its new contribution is the quality-control and pilot-adaptation evidence.

**Evidence context and administration.** Adult Dynata panel members came from Australia, Argentina, Brazil, Canada, Chile, China, France, Germany, Japan, Mexico, the Netherlands, New Zealand, Spain, the United Kingdom, and the United States. LimeSurvey supplied web self-report. Countries used age, sex, income, urban or rural setting, and sometimes language quotas. Target sample size was 4,500 per country. Local experts reviewed translated and adapted surveys. After a 200-person soft launch, countries collected data for about six weeks, with extension and later quota relaxation when needed.

**Instrument-role boundary.** EQ-5D-5L, EQ VAS, EQ-HWB, and other measures were administered within the infrastructure, but this paper analyzes survey operation and data quality rather than population health or measurement properties. The UK pilot compared EQ-HWB length and EQ-5D-5L vignette forms to control burden. A moderate, gender-neutral EQ-5D-5L and EQ VAS vignette remained in the main survey. Do not treat the paper as reporting comparative health outcomes from these instruments.

**Quality-control path and pilot changes.** Google reCAPTCHA v3 ran at four interactions. A low score could exclude a response as a bot. Dynata also used IP and panel controls. Five minutes was the speeding threshold. Duplicate identifiers, completion time, missing responses, numerical outliers, and repeated age and marital-status answers were reviewed. Real-time quota dashboards triggered recruitment adjustment. Pilot evidence led to one vignette instead of three, shorter mental-health screeners, nonmandatory questions without a `prefer not to answer` option, demographics earlier in the survey, bounded numeric response choices, information icons, and removal of political affiliation.

**Principal findings.** Main completion rates ranged from 22.9% to 60.8%, with a 42.4% average. Mean completion time ranged from 18.3 to 31.4 minutes. Bot exclusions averaged 3.0% and reached 11.7% in China. Speeding averaged 0.3%, and duplicate records were rare. Missingness and quota achievement varied materially. Repeated marital status and age had about 96% average agreement. Average proportional quota achievement ranged from 68.7% to 98.6%.

**Product and states.** `EQ-DAPHNIE survey quality-control workflow`; completed named workflow with UK pilot evidence and documented research use across the 15-country collection. It is part of the ongoing EQ-DAPHNIE protocol and infrastructure. The paper offers lessons for later surveys, but it does not establish a general population-survey guideline or new national norms.

**Author interpretation, limitations, and gaps.** The authors interpret the checks as effective against bots, speeders, and duplicates, but warn that quality and quota variation must inform later norms and cross-country work. Nonprobability panels, unequal panel capacity, internet coverage, unobserved selection, missingness, and residual bias remain. Weighting cannot remove all bias. They suggest alternative panels or offline supplements, adaptive recruitment, new bot controls, and sensitivity analysis.

**Source uncertainty.** `definition or denominator`: the abstract calls the 80.1% to 100% link-opening proportions `response rates`, while the main text separates link opening, consent, and completion. Store the defined stages and denominators, not one generic response rate. `definition or threshold`: one method statement flags a bot score below 0.5, while another excludes a score of 0.5 or less. Retain the boundary difference and do not infer how exact 0.5 scores were handled.

### 10. 10.1007/s11136-026-04294-w — socioeconomic gradients within identical EQ-5D-5L profiles

**Classification and purpose.** Health equity or inequality study, population-health study, and methods study; completed. The paper tests whether education and subjective income status remain associated with EQ VAS after respondents are conditioned on one of ten identical EQ-5D-5L profiles.

**Components and reuse.** `D1 eight-country EQ-DAPHNIE data` reuses the samples from Australia, Canada, France, Germany, the Netherlands, New Zealand, the United Kingdom, and the United States. `S1 edited analysis sample` contains 32,327 respondents aged 25 to 79 years. `C1 ten profile-conditioned comparisons` supports parallel `A1 education-gradient` and `A2 subjective-income-gradient` models. `A3 country-stratified 11111` and `A4 country-stratified 11121` test the two profiles with adequate samples in every country.

**Evidence context and administration.** Dynata panel members self-reported health in the EQ-DAPHNIE web survey. The source used country quotas for age, sex, income, region, and language. This paper excluded respondents younger than 25, respondents above its upper age rule, and BMI at or below 15. The ten profile strata covered 61% of the edited sample. The target contexts were population-health inequality and equity-informative HTA in high-income countries.

**Instrument and conditioning roles.** EQ-5D-5L profiles define the strata held constant. EQ VAS is the outcome. No preference-weighted utility is analyzed. Education is harmonized as low, medium, or tertiary. Subjective income status is comfortable, coping, or difficult, with difficult and very difficult combined. A same-profile comparison holds the five reported dimensions constant. It does not prove equal underlying health because the descriptive system can omit relevant content and response behavior can differ.

**Analysis and exclusion path.** Separate weighted linear regressions were fitted within each profile and adjusted for age, sex, and country. Country models for 11111 and 11121 adjusted for age and sex. Full-information maximum likelihood handled missing data under a missing-at-random assumption. The paper also excluded EQ VAS below 50 for 11111 and below 30 for the nine mild profiles. These inherited author-judgment thresholds removed 0.6% to 3.1% per profile and are part of the analytic eligibility rule, not a platform fraud control.

**Principal findings.** Tertiary education had a positive coefficient in all ten profile models and met the paper's significance convention in seven. Subjective income had a stronger gradient and was significant in nine. For profile 11121, the adjusted EQ VAS difference was about 2.1 points for tertiary versus low education and about 5.0 points for comfortable versus difficult income. The country-specific comfortable-income coefficient was positive in all eight countries for 11111 and 11121, although precision differed. Education was less stable across countries.

**Author interpretation and implications.** The authors give two nonexclusive explanations: unmeasured health content and socioeconomic reporting heterogeneity. The study cannot distinguish them. They state that profile or utility analysis can understate differences seen in overall self-rated health. They recommend complementary use of EQ VAS, selected bolt-ons, or direct socioeconomic indicators when equity is central. These are author-reported population-health and HTA implications. The paper does not show that EQ-5D-5L failed its intended construct.

**Limitations and transfer limits.** The design is cross-sectional and noncausal. Online-panel selection, subjective income and EQ VAS sharing psychological influences, response-style differences, high-income-country scope, and limited precision constrain transfer. FIML relies on missing at random. The lower-tail VAS filter can change the distribution used to estimate the gradient and was not presented with a no-filter sensitivity analysis. Treat it as a declared analytic rule, not verified response error. `definition or boundary`: the abstract reports ages 25 to 79, while the methods say that respondents older than 80 were excluded. The latter rule would not exclude age 80. Retain the reported 25-to-79 range and the age-boundary conflict.

## Round 3 granularity decisions and evidence

### Decisions added or revised

31. **Add anchor target and time-preference form to the valuation path.** Paper 6 shows that immediate-death and duration anchors produce different utility ranges and that a nonlinear time model changes the result. Paper 2 shows that the death anchor can also interact with child perspective. `DCE with duration` alone cannot retrieve or interpret these differences. This supports user questions 9, 10, 12, 13, 20, and 21.

32. **Add experimental arms and crossed factors as components.** Paper 2 randomizes a two-by-two combination of instrument wording and perspective. Its significant interaction means that separate wording and perspective tags are not sufficient. Record assignment and arm contrasts without making a component for each test statistic. This supports questions 5, 6, 10, 12, 13, and 21.

33. **Add health equity or inequality as a repeatable study family.** Papers 1, 8, and 10 have equity or inequality as a main purpose, but they belong to different clinical, population, and secondary-analysis families. A topic tag alone cannot distinguish an equity-purpose paper from a paper that only reports sample demographics. This supports questions 1, 2, 7, 17, 20, 21, 22, and 24.

34. **Structure material socioeconomic variables by construct and analytic role.** Paper 1 uses reported income bands as an exposure. Paper 8 uses income and other variables for stratification, ordered logit, and Kakwani decomposition. Paper 10 harmonizes education and uses subjective income adequacy in conditional models. These variables are not interchangeable. This supports questions 2, 7, 9, 12, 13, 20, and 22.

35. **Record the conditioning rule for a comparison.** Paper 10 compares EQ VAS within an identical profile. Paper 8 compares survey periods after both profile sets use the same value set. Paper 1 compares income groups with a selected regression reference. A comparison entry that names only the outcomes and groups hides what was held constant. This supports questions 12, 13, 15, 16, 20, and 22.

36. **Keep temporal data and scoring harmonization explicit.** Paper 8 uses a common 2024 value set for 2012 and 2022-2023 profiles, but modes, samples, demographic categories, and collection periods still differ. This permits a valid score-route comparison without implying that all other conditions match. This supports questions 5, 12, 13, 19, 22, 25, and 26.

37. **Represent population norms as a dated, scored product.** Paper 8 produces an updated national reference, not only descriptive findings. The reference period, profile version, language, value set, strata, source samples, and update relation affect reuse. This supports questions 14, 19, 23, 24, 25, and 26.

38. **Record survey flow stages with their denominators.** Paper 9 separates panel frame, link opening, consent, completion, quality exclusion, and quota achievement. Its abstract's `response rate` label would mix these stages. Paper 5 and paper 7 also report different participation and retained counts. This supports questions 8, 9, 16, 20, and 24.

39. **Represent a material quality rule as indicator, threshold, action, and affected data.** Papers 7 and 9 use protocol and platform rules. Paper 8 inherits source-study exclusions. Paper 10 applies author-judgment EQ VAS filters that shape the analytic sample. A broad `quality control used` tag hides whether a record was flagged, reviewed, automatically excluded, or selected for analysis. This supports questions 8, 9, 12, 13, 16, 19, and 25.

40. **Strengthen multi-source reuse and overlap records.** Paper 8 combines two earlier batch papers and a new survey, then reuses 2012 data. Paper 6 reuses DCEd respondents but compares with a separate cTTO product. Paper 1 reuses the oncology pilot's initial responses. Sample identity, raw-data reuse, product reuse, and possible overlap must remain different relations. This supports questions 5, 8, 13, 19, and 25.

41. **Add cost-of-illness or burden-of-disease as a study family with a distinct economic path.** Paper 5 has no intervention, comparator, incremental QALY, or ICER. Its prevalence, cost categories, societal bearers, productivity method, DALY path, and monetary assumptions answer different questions from the decision-model path added in round 2. This supports questions 1, 2, 7, 9, 12, 17, 20, and 21.

42. **Keep DALY, QALY, utility, disability weight, and monetized wellbeing loss distinct.** Paper 5 calculates DALY-based wellbeing loss and only mentions QALYs. Paper 7 creates utilities for QALYs. Collapsing these data forms would falsely retrieve paper 5 as EQ-5D utility analysis. This supports questions 2, 3, 12, 13, 20, and 21.

43. **Do not create an instrument-use record for a contextual mention.** Paper 5 does not use EQ-5D even though it discusses QALYs. Paper 9 administers instruments but does not analyze their health results. Paper 4 discusses a candidate scoring route but reuses the same valuation sample. Instrument retrieval must depend on an explicit role and linked component. This supports questions 3, 4, 9, 14, and 20.

44. **Keep an experimental tariff or candidate scoring model separate from an established value set.** Papers 4 and 6 estimate usable coefficient sets to answer method questions. Paper 7 produces the operational national product. Product inventories would be inflated if every model became an established value set. This supports questions 12, 14, 18, 20, and 23.

45. **Preserve competing author explanations when the design cannot separate them.** Paper 10 cannot distinguish omitted health content from reporting heterogeneity. Paper 7 cannot isolate protocol, wording, time, or social-change explanations for value-set differences. Record the alternatives as author interpretation, not as resolved mechanisms. This supports questions 15, 16, and 22.

### Important distinctions considered and rejected in round 3

- **`DCE with duration` without anchor and time-preference form:** rejected. Paper 6 obtains materially different tariffs from the four combinations.
- **Independent wording and perspective effects in paper 2:** rejected. The reported interaction requires arm-level interpretation.
- **Treating adult-self and child-other framing as an age-only contrast:** rejected. Referent age and self-versus-other relation change together.
- **One generic socioeconomic-status field:** rejected. Education, disclosed income bands, undisclosed income, and perceived income adequacy have different constructs and analytic roles.
- **Treating identical EQ-5D profiles as proof of identical health:** rejected. Paper 10 tests residual differences and cannot separate omitted content from reporting behavior.
- **Treating a cross-sectional socioeconomic association as causal:** rejected for papers 1, 8, and 10.
- **One survey response rate:** rejected. Invitation, link opening, consent, completion, exclusion, and analysis use different denominators.
- **One quality-control flag for all rules:** rejected. Platform fraud controls, interviewer flags, source exclusions, and author-judgment analytic filters have different evidence and consequences.
- **An EQ-5D use entry for paper 5:** rejected. The paper does not administer or analyze a EuroQol instrument.
- **Treating DALYs as QALYs or disability weights as utilities:** rejected. Paper 5 defines and uses a different health-loss path.
- **One total economic-cost value without categories and bearers:** rejected. Paper 5's main interpretation depends on intangible, indirect, direct, and household burden.
- **Treating the three current norm sources in paper 8 as one homogeneous sample:** rejected. Mode, task context, variables, incentives, and quality exclusions differ.
- **Attributing the norm change to COVID-19 or mental-health awareness:** rejected. Paper 8 discusses possible explanations but does not identify a cause.
- **Treating the cTTO-only model in paper 4 or four tariffs in paper 6 as established national products:** rejected. They are comparative method outputs.
- **Treating paper 9 as proof that its panel is representative:** rejected. Quotas and weights reduce observed imbalance but do not remove unobserved selection.
- **A controlled category for every pilot change or quality indicator:** rejected. Keep the stable rule form structured and the exact survey changes in a concise list.
- **A new product type for every national burden estimate:** rejected for now. Paper 5's estimates are principal findings and a benchmark, but the current reusable-product inventory does not need every modeled estimate.

## Status of unresolved cases after round 3

1. **Product status axes remain necessary and are more stable.** Paper 7 is an established and author-recommended value set. Paper 8 is an established dated norms product. Papers 4 and 6 have tested candidate models. Paper 9 documents a workflow in use inside a research program. The separate development, evidence, governance, availability, recommendation, and use axes fit all four.
2. **Mixed paper and component status remains sufficient.** Paper 9 reports a completed quality analysis inside ongoing EQ-DAPHNIE infrastructure. No new paper requires a different paper-level status system.
3. **Content validity, concept elicitation, and cultural adaptation remain separate but linked.** Batch 03 gives no new direct adaptation paper. Paper 10 raises omitted content as one possible explanation but does not perform content-validity work.
4. **Unusual scale-type DIF remains unresolved.** Batch 03 has no second response-scale DIF paper.
5. **Evidence-level country and language in reviews remains partly unresolved.** Paper 3 can support counts for 18 countries and broad sample types, but detailed language and value-set context would require reconstruction of every included study. Keep review-level `various` and principal transfer limits.
6. **Review publication and data-set cardinality remains manageable with current relations.** Paper 3 repeats the rule to retain the most informative duplicate paper or both for different indicators. A more complex review can still require explicit many-to-many counts.
7. **External age-validity rules remain out of scope.** No round-3 paper supplies direct evidence that changes the earlier rule.
8. **Source-conflict types remain useful but can overlap.** Papers 7, 8, and 9 fit the existing types. Paper 9 shows that a threshold boundary can be both definition and implementation detail. Keep one primary type and local narrative.
9. **Proxy perspective terminology still needs direct application evidence.** Paper 2 uses a hypothetical child referent, not a proxy report.
10. **Implementation-stage terms need further calibration.** Paper 9 shows a workflow used across 15 research collections, but it does not resolve the boundary between limited and scaled routine clinical or policy use.
11. **Mapping transport remains a concise path.** Batch 03 adds a crosswalk comparison in paper 7 but no new mapping-development application. The current source measure, target version, development population, value set, and application population path remains sufficient.
12. **Pooled-variable harmonization now needs a repeatable relation only when it affects comparison.** Papers 8 and 10 show stable cases for category, scoring, and source harmonization. Keep ordinary covariate recoding in narrative, but use an explicit relation when it defines cross-source comparability.
13. **Scoring-source conflicts remain local.** Paper 7 adds a count conflict about negative profiles, not a new scoring-version identifier problem.
14. **Quality control versus analytic eligibility needs later calibration.** Paper 10 calls lower EQ VAS values inconsistent and excludes them, but the rule also trims the outcome used to test residual heterogeneity. Keep rule source and action explicit. A later paper with sensitivity analysis can test whether `analytic eligibility filter` is a stable controlled term.
15. **Population-norm update maturity is provisionally clear.** Paper 8 produces a dated established reference and recommends periodic replacement. Later norms papers can test whether `supersedes` and `coexists with` need controlled product relations.
16. **Cost estimates are not yet a controlled product type.** Paper 5 uses its national estimate as a benchmark. More cost or burden papers are needed before deciding whether such estimates belong in the reusable product inventory.
17. **Within-profile residual gradients have an unresolved mechanism.** Paper 10 supports structured conditioning and alternative interpretations, but it cannot decide between omitted content, response-scale behavior, and other residual confounding.
18. **Possible sample overlap needs a confidence value.** Paper 8 states both intended mutual exclusion and possible duplication. Current narrative uncertainty is sufficient for one case. Later pooled panel studies can test a controlled `documented independent`, `documented overlap`, or `possible overlap` value.

## Round 3 run note

This round extended the preserved round-1 and round-2 Candidate 2 record with all ten batch-03 applications. All ten assigned article files matched the manifest SHA-256 values and byte counts. The main additions are DCE anchor and time-preference detail, experimental arms, equity-variable roles, conditional comparisons, dated population norms, survey-flow and quality-rule paths, cost-of-illness methods, DALY and QALY boundaries, and stronger multi-source provenance. The run used the frozen version-2 task and batch 03 on branch `experiment/anonymous-candidate-2` at base commit `ec3aeda3c2b97e2dda36c9bb33fa4b4d2ce119da`. Agent: fresh Candidate 2 round-3 Codex agent. Run time: 2026-08-16 19:35 CEST. No fixed JSON schema was used. No mechanical issue occurred.

## Applications to batch 04

### 1. 10.1371/journal.pone.0302886 — Australian Person Trade Off protocol for child and adult health gains

**Classification and purpose.** Social-priority weighting study, study protocol, and methods study; mixed status. The main online survey and qualitative samples are planned. Consumer input, convenience pilots, and initial qualitative pilots are complete. The paper develops and justifies a protocol to estimate how the Australian public values equal health gains for people aged from infancy through young adulthood relative to gains for adults. It also tests the effect of forced choice versus an available equivalence response.

**Components and status.** `P0 consumer input and survey pilots` changed wording, removed a proposed life-expectancy factor, and refined the sensitive qualitative work. `S1 planned online PTO sample` has a target of 2,000 respondents. `T1 life-extension PTO` covers gains of two and five years. `T2 quality-of-life PTO` covers two-year improvements in distress, mobility, and pain. `E1 forced-choice arm` and `E2 equivalence-available arm` are randomized. `C1 chained PTO test` assesses individual ratio consistency. `Q1 think-aloud interviews` targets about 40 people. `Q2 deliberative focus groups` targets about four groups with no more than five people each. The qualitative components explain reasoning and test the meaning of apparent inconsistencies; they do not supply the main weights.

**Evidence context and perspective.** Planned online respondents are Australian panel members aged at least 16 years. Age, gender, education, and broad geography guide quotas. Qualitative recruitment purposively includes young people, parents of younger or older children, parents of children with health problems, and adults without children. Respondents act as social decision makers who advise a resource-constrained health system. The referents are hypothetical groups defined by one of 13 ages from one month through 24 years and an adult group aged 40 or 55. The intended decision context is Australian HTA and possible age weighting of health gains.

**PTO design and administration.** The question framing holds treatment cost, health gain, carer effects, and work or income effects constant. Life-extension tasks end in death after the stated gain. Quality-of-life tasks prevent a two-year illness and then return the patient to full health. Each comparison starts with 100 patients in each group. The initially preferred group is reduced while the other group stays at 100. Three or four follow-up choices, with a possible fifth for an extreme response, use a bisection path. The younger or older group position, PTO question order, adult comparison age, and availability of equivalence are randomized. The main survey is unattended online self-report. Mandatory video instruction, practice, an attention check, repeated age, minimum-time rules, a honeypot, unique panel identifiers, and free-text review support quality control.

**Analysis path.** If an exact equivalence point is absent, the analysis assigns the midpoint of the final interval. A respondent who always prefers one group can receive an inferred midpoint between zero and the smallest offered group, and such responses are also reported as extreme preferences. Group results use a ratio of means and a median of individual ratios, with percentile bootstrap intervals. The paper plans preference classes, multinomial logistic models, tests of forced and unforced arms, tests across gain types, and a chained ratio comparison. Apparent disagreement with attitudinal questions is described cautiously and is not an automatic data-quality failure.

**Instrument and product boundary.** No EuroQol instrument is administered, scored, or produced. QALYs are part of the policy rationale, but the tasks separate years of life from quality-of-life domains and do not elicit health-state utility. The product is a completed named mixed-method PTO protocol with formative consumer and pilot evidence. Its main survey and resulting social-priority weights are not complete.

**Principal result, interpretation, and implications.** The paper's result is the protocol and its design rationale. It does not report Australian age weights. The authors expect the study to inform whether decision makers should give greater weight to gains for children and young people. They also expect the forced-choice test to improve PTO methods. These are author-reported policy and methods implications, not documented use.

**Limitations and stated gaps.** The online panel can omit social groups and can reduce engagement. PTO responses can be skewed, sensitive to focusing and order, and difficult to aggregate. The isolated age contrast can give age more salience than it has in a full decision. Results from Australia may not transfer to other countries. The authors use the qualitative work to examine these limits, but it cannot remove them.

### 2. 10.1186/s12955-023-02115-z — Swedish experience-based EQ VAS valuation across patient registers

**Classification and purpose.** Health-state valuation study, population-health study, and methods study; completed. The paper uses EQ VAS as an experience-based valuation of respondents' own EQ-5D-3L health and compares patterns across nine patient groups, baseline and one-year follow-up, and a Swedish general-population sample.

**Components and reuse.** `D1-D6 intervention registers` cover spine surgery, hip replacement, knee replacement, ankle replacement, cruciate-ligament treatment, and first-line osteoarthritis treatment. `D7-D9 diagnosis registers` cover heart failure, respiratory failure, and bipolar disorder. Each register can have `T0 baseline` and `T1 one-year follow-up`. `D10 general-population surveys` contains 41,761 complete respondents from Scania in 2004 and Stockholm in 2006. `A1 selected-profile comparison`, `A2 EQ VAS-index correlation`, `A3 dimension-decrement models`, and `A4 pooled patient-group models` are distinct streams. The study reuses Swedish National Quality Register data, the two population surveys, and a prior project protocol. It also uses the general-population surveys that produced the Swedish experience-based EQ-5D-3L VAS value set.

**Evidence context.** The patient evidence contains 172,070 records with EQ VAS and complete required data across nine clinical groups. Ages and disease courses differ greatly by register. The general-population comparator is cross-sectional and does not have a one-year follow-up. The paper states that EQ-5D collection methods can differ between registers. Exact administration mode and language-version detail are not consistent enough for one value across all sources.

**Instrument and valuation roles.** EQ-5D-3L profiles describe respondents' own current health and supply the health-state predictors. EQ VAS is the own-health rating and experienced-value outcome. Its endpoints are worst and best imaginable health; death is not fixed at zero. The Swedish experience-based VAS value set converts EQ-5D-3L profiles to an index for correlation comparison. EQ-5D-5L data from the osteoarthritis and hip groups support an additional model check. No new national value set is produced.

**Analysis and comparison path.** The paper compares mean EQ VAS for nine selected profiles across patient groups and time. Spearman correlations compare EQ VAS with the Swedish experience-based index and compare their changes. Separate and pooled OLS models regress EQ VAS on EQ-5D-3L dimension levels, with age and sex adjustment. Two-level random-intercept and random-slope models are sensitivity analyses. A decrement is called inconsistent when a severe level has a smaller decrement than a milder level. These models describe conditional associations and experienced valuations. They do not estimate a choice-based utility scale.

**Principal findings.** EQ VAS generally decreased as profiles became more severe. Baseline correlations with the EQ-5D-3L index were moderate and increased at follow-up, with strong correlations in the spine and hip groups. Intervention registers usually showed larger follow-up EQ VAS gains than diagnosis registers. Anxiety or depression had the largest decrement in most groups. Self-care level 3 was the main source of inconsistent decrements, and mobility also showed some inconsistency. The same profile received different EQ VAS ratings across groups and times.

**Author interpretation and implications.** The authors interpret the variation as evidence that disease experience, treatment stage, and health content beyond the five descriptive dimensions affect own-health valuation. They argue that EQ VAS can reveal aspects of health that matter to patients and can support clinical and population-health assessment. They discuss a possible future role for patient experience-based values in QALYs, but the present unanchored EQ VAS models are not an operational QALY value set.

**Limitations and stated gaps.** Register collection methods differ, and clinical group composition and timing can explain part of the comparison. Few respondents use the most severe self-care and mobility levels. EQ VAS has no trade-off and can have endpoint avoidance. The absence of a death anchor limits immediate economic use. Moderate or strong correlation still leaves disagreement between EQ VAS and the profile index. The authors call for clinimetric work and more study of patient-based valuation.

### 3. 10.1007/s11136-020-02712-1 — online versus face-to-face cTTO valuation

**Classification and purpose.** Health-state valuation study and methods study; completed. The paper tests whether unattended online cTTO can reproduce interviewer-supervised face-to-face valuation of EQ-5D-5L in United States adult general-population samples.

**Components and reuse.** `D1 US face-to-face valuation data` has 1,134 respondents and 11,340 cTTO observations. `S1 face-to-face full` retains all these responses. `S2 face-to-face valid` excludes 72 respondents judged not to understand and removes 1,234 respondent-flagged tasks, leaving 1,062 respondents and 9,386 observations. `S3 face-to-face invalid` is a post hoc comparison. `D2 US online experimental data` has 501 respondents and 5,010 observations. `A1 raw-value patterns`, `A2 engagement`, `A3 dominance inconsistencies`, and `A4 random-intercept value-set models` compare the sources. The paper explicitly reuses two earlier United States valuation studies.

**Evidence context and mode bundles.** Both sources use adult quotas for age, gender, race, and ethnicity. The face-to-face source recruits by several routes in six metropolitan areas and pays USD 30. It uses one-to-one computer-assisted personal interviews. Respondents read states aloud, think aloud, can ask questions, and use a feedback module. The online source recruits panel members for low-value survey credit. It uses unattended self-completion, automated narration, an interactive tutorial, and a warning for tasks below 15 seconds. It has no feedback module. Thus, respondent source, incentive, interviewer support, platform, tutorial, and feedback differ together with contact mode.

**Instrument, task, and protocol.** EQ-5D-5L is the valuation target and source of 86 health states in ten common blocks. Each respondent completes five practice tasks and ten modeled cTTO tasks. cTTO uses conventional TTO for better-than-dead values and lead-time TTO for worse-than-dead values. The face-to-face source uses EQ-VT and valuation protocol version 2.0. The online SurveyEngine platform is designed to resemble EQ-VT but changes delivery to replace interviewer cues.

**Quality and analysis path.** Quality evidence includes value distributions by level sum score, use of worse-than-dead values, nontrading, better-than-dead-only trading, number of moves, task time, and dominance inconsistencies, especially cases in which 55555 is not lowest. Random-intercept linear models produce comparable experimental tariffs. Joint models estimate the package association before and after respondent adjustment. These tariffs are analytic comparison outputs, not recommended United States value sets.

**Principal findings.** Online responses had fewer worse-than-dead values, more nontrading and low-move patterns, and many more inconsistencies. About 41% of online respondents did not place 55555 lowest, compared with about 12% in the face-to-face full sample. The online tariff had eight nonsignificant parameters, two inversions, a small range, an intercept of about 0.846, and a value near 0.400 for 55555. Its modeled values were about 0.27 to 0.31 higher after covariate adjustment. Online respondents had about 3.6 times the adjusted odds of any inconsistency relative to the face-to-face full sample.

**Author interpretation and implications.** The authors interpret the difference as lower engagement and task understanding in this online implementation. They advise against this unattended online cTTO approach as the first choice for general-population valuation. They suggest that simpler tasks, better validity checks, or more support can improve later online work. This is a methods implication, not proof that every online TTO design fails.

**Limitations and transfer limits.** The comparison does not isolate interviewer presence or contact mode because recruitment source, incentive, platform, feedback, and other controls also differ. Samples have unequal size, and unmeasured respondent traits remain. Some trading patterns can be genuine preferences, so aggressive cleaning can remove valid evidence. The result applies to this online cTTO package and does not establish a universal mode effect.

### 4. 10.1186/s12955-022-01996-w — Indonesian proxy and self-report comparison for EQ-5D-Y-3L and 5L

**Classification and purpose.** Measurement-property assessment; completed. The paper compares Bahasa Indonesia EQ-5D-Y-3L and experimental EQ-5D-Y-5L proxy version 1 and tests agreement with paired child self-report.

**Components.** `S1 baseline child-proxy pairs` has 286 children and proxies. Disease subgroups are beta-thalassemia major, hemophilia, acute lymphoblastic leukemia, and acute illness. `T1 stable retest` has 59 pairs whose proxy reports no change. `T2 follow-up` has 222 proxy reports, of which 91.4% report improvement. `A1 feasibility and distribution`, `A2 3L-to-5L redistribution`, `A3 convergent validity`, `A4 proxy test-retest`, `A5 direction-specific responsiveness`, and `A6 proxy-self agreement` remain separate.

**Evidence context and proxy perspective.** Children are aged 8 to 16 years and receive care in five hospitals in Jakarta and Bandung, Indonesia. Most proxies are mothers, but fathers, siblings, grandparents, and other relatives also participate. All report that they know the child's health. Proxy version 1 asks for the proxy's own assessment of the child. It does not ask the proxy to answer as the child would answer. Children and proxies complete forms independently, with staff present to prevent discussion. This is observed proxy evidence, not only a proxy topic.

**Instruments and administration.** Bahasa Indonesia EQ-5D-Y-3L and experimental EQ-5D-Y-5L are paired targets in proxy and self-report form. The in-progress UK English 5L versions were translated with EuroQol version-management involvement. Proxy PedsQL Generic and disease-specific PedsQL Cancer, TranQol, or Haemo-QoL measures are convergent comparators. Administration is pen-and-paper in hospital, at bedside or while waiting for an appointment. Help is limited to reading or writing difficulty. The 5L form always precedes 3L. The EQ-5D-Y recall period is `today`, while several comparator measures use the prior month.

**Measurement-property path.** Feasibility uses missing responses. Distribution uses dimension and profile full-health proportions. The article places ceiling under a content-validity heading, but the direct inference is distribution and classification. Redistribution uses language-specific semantic matches and defines a difference of two or more levels as inconsistent. Spearman correlations test convergent hypotheses. Gwet's agreement coefficient assesses proxy test-retest and paired proxy-self agreement. Responsiveness uses the proportion whose dimension level changes in the direction of a proxy global-change report. It does not use utility change because no 5L youth value set is available.

**Principal findings.** Missingness is low for both versions. Full-health profiles are slightly less frequent with 5L at baseline. Logical redistribution dominates, with the largest added separation in pain or discomfort. Test-retest agreement is high and similar for 3L and 5L. Convergent results are similar. In the large improved group, 5L shows more improvement in four of five dimensions. Baseline proxy-self agreement is generally higher for 5L, except that agreement is low in acutely ill children. Agreement rises after recovery.

**Author interpretation and implications.** The authors conclude that five levels can improve classification and change detection without reducing test-retest reliability. They support 5L proxy use when a child cannot self-report. They do not say that proxy report can replace self-report in every child or that proxy version 2 has been tested here.

**Limitations and transfer limits.** Only 59 stable pairs support test-retest, and very few worsened or stable participants support follow-up direction comparisons. Acute health can change faster than a proxy can observe. Fixed 5L-first order can affect response use. Recall periods differ across measures. The sample includes age 16 although the paper describes the youth instrument mainly for ages 8 to 15. No utility comparison is possible.

### 5. 10.1186/s12955-024-02290-7 — Singapore English EQ-5D-Y adaptation and content validity

**Classification and purpose.** Cultural adaptation, instrument development, qualitative concept study, and measurement-property assessment; completed. The paper adapts UK English EQ-5D-Y-3L and EQ-5D-Y-5L to Singapore English and separately assesses relevance and comprehensiveness of the descriptive system with children in Singapore.

**Components and version roles.** `V1 UK English Y-3L` and `V2 UK English Y-5L` are source versions. `P1 expert review` includes six pediatricians and two primary-school teachers. `P2 Y-3L cognitive debriefing` includes six children after one noisy interview caused an extra recruitment. `P3 Y-5L cognitive debriefing and label ranking` includes five children. These stages produce `V3 Singapore English Y-3L` and `V4 Singapore English Y-5L`. A separate `S1 content-validity sample` has 14 children and feeds `A1 open concept elicitation`, `A2 framework analysis`, and `A3 instrument-focused relevance and comprehensiveness review`.

**Evidence context and administration.** Adaptation respondents are Singaporean children, mean age about 9.8 years. Content-validity respondents are aged 8 to 15 years and include eight healthy children and six with acute, chronic, or combined health experience. Purposive sampling covers age, gender, ethnicity, and illness experience. Interviews are one-to-one, face-to-face, private, and in English. Children supply direct evidence. Parents can sit out of the child's sight but do not answer for the child.

**Adaptation and qualitative paths.** This is same-language, cross-cultural adaptation, not a forward and back translation into a different language. Local experts review UK wording. Children paraphrase and answer probes. Five-level respondents rank randomized severity cards. The EuroQol Research Foundation reviews and endorses modifications. The final versions use familiar Singapore phrases and approved examples for discomfort. In the separate content-validity work, children first discuss direct and indirect experiences of poor health without seeing an instrument. Two independent coders apply and extend an existing Singapore framework. Children then complete Singapore English Y-3L and comment on the five dimensions. Data saturation is defined as no new information in the last three transcripts.

**Products and evidence scope.** `Singapore English EQ-5D-Y-3L` and `Singapore English EQ-5D-Y-5L` are completed named adaptation products with EuroQol Research Foundation endorsement. Both have cognitive comprehension evidence from small samples. The descriptive system has relevance and comprehensiveness evidence, but part 2 administers Y-3L only. The content-validity result does not cover EQ VAS, relative concept importance, psychometric performance, valuation, or a new bolt-on.

**Principal findings.** Children understand the adapted versions and rank the 5L labels in the intended order. All five descriptive-system dimensions arise spontaneously from poor-health accounts and are judged relevant. The elicited framework also includes sleep, appetite, tiredness, basic functions, appearance, and social relationships. Some children suggest more mental-health content, sleep, appetite, or family and friend relationships. The authors judge the short system generally relevant and comprehensive while recognizing these omissions.

**Author interpretation and implications.** The authors state that Singapore-specific wording improves linguistic equivalence and child understanding. They present appetite and social relationships as candidates for later bolt-on research, not as approved additions. They advise separate psychometric testing before wide Singapore use.

**Limitations, gaps, and source uncertainty.** Young children can have limited direct poor-health experience, which the study partly addresses through indirect accounts and children with conditions. The study does not rank concept importance and does not assess EQ VAS content validity. The small local samples limit transfer. The authors call for construct-validity, reliability, responsiveness, EQ VAS work, and bolt-on tests. `count or arithmetic`: the content-validity table reports five children with a chronic condition as 53.7%. Keep the count of five and the reported percentage as a conflict; do not silently repair it.

### 6. 10.1007/s10198-025-01769-4 — test-retest reliability of OPUF valuation for EQ-HWB-S

**Classification and purpose.** Health-state valuation study, measurement-property assessment, and methods study; completed. The paper tests the two-week reliability of the Online Elicitation of Personal Utility Functions approach for valuing EQ-HWB-S. It distinguishes task-level, personal, subgroup, and aggregate results.

**Components and reuse.** `D1 initial German validation survey` has 330 respondents: 110 general-population members, 110 people with diabetes, and 110 people with rheumatic disease. `T1 two-week retest` has 257 respondents. Matching and stated exclusions produce `S1 paired analysis sample` of 220, with 73 general-population and 147 patient respondents. `A1 dimension ranks`, `A2 swing weights`, `A3 intermediate-level ratings`, `A4 death anchoring`, `A5 personal utility decrements`, and `A6 aggregate value sets` are separate reliability targets. The baseline survey is reused from an earlier OPUF validation study. The retest is new repeated evidence.

**Evidence context and administration.** Adults are recruited in Germany through a Bilendi online panel and receive EUR 7.50. Unique identifiers link the two web surveys. Patient and general-population results are reported separately. The study assumes that preferences should remain stable over two weeks, but it does not verify stable disease symptoms. Older people are more common in the patient sample.

**Instrument and OPUF task path.** EQ-HWB-S is the valuation target and source of nine five-level health and wellbeing dimensions. Respondents first report their own EQ-HWB-S state and adapted EQ VAS. They then rank worst-level dimensions, give relative swing weights, rate intermediate levels on a 0-to-100 scale, compare state 555555555 with death, and place the preferred state between full health and the less preferred anchor. Utility decrements multiply normalized level ratings, dimension weights, and a death-anchoring factor. An additive model creates personal and aggregate health-state values, with anchoring censored at -1.

**Reliability and exclusion path.** More than two illogical responses and indifference between full health and the death or worst-state anchor can exclude a respondent from complete utility-function analysis. Additional task-specific exclusions apply to illogical level ratings. Spearman correlation assesses rank stability. Two-way mixed-effects ICC assesses swing weights, level ratings, anchoring factors, and personal decrements. Kappa and percentage agreement assess the pairwise death choice. Paired tests, Kolmogorov-Smirnov tests, and distribution plots compare aggregate decrements. This is reliability of a valuation method applied to EQ-HWB-S, not test-retest reliability of EQ-HWB-S self-reported health.

**Principal findings.** Only about 42% select the same top-ranked dimension, and about 36% have a positive correlated dimension ranking. Most individual swing weights, level ratings, anchoring factors, and utility decrements have poor or moderate agreement. The pairwise death comparison is more stable, with about 83% agreement and kappa near 0.64. Aggregate decrements are very similar, with a mean absolute difference near 0.004, even though personal health-state rankings have only a low correlation. Patient respondents show poorer task reliability than the general-population group, but age explains part of this difference.

**Product and interpretation boundary.** Test and retest generate two aggregate EQ-HWB-S tariff outputs. They are comparative method outputs, not completed operational German EQ-HWB-S value sets. The authors interpret aggregation as cancelling some individual variation. They conclude that OPUF can give stable group-level tariffs in this sample but does not yet support stable personal utility functions.

**Limitations and stated gaps.** Exclusion of illogical or unusable responses can overstate reliability. The VAS-like tasks can cause response spreading. Online recruitment selects for digital access and may allow inattention. The study cannot separate OPUF complexity, EQ-HWB-S complexity, online delivery, current symptoms, and respondent understanding. The authors call for qualitative task research, design refinement, observer or interviewer support tests, repeat reliability tests, and a minimum-sample-size study.

### 7. 10.1136/bmjopen-2025-100897 — DCE protocol for preference testing of EQ-TIPS-5L version 3.0

**Classification and purpose.** Instrument development, study protocol, and methods study; mixed status. The survey, design, and analysis materials for wave 1 have completed beta and pilot work. The two main Australian DCE waves are planned. The paper tests whether EQ-TIPS-5L severity labels follow preference order and whether adjacent attribute levels affect choices. It does not plan to anchor a value set.

**Components and dependencies.** `P0 prior EQ-TIPS development` supplies experimental generic-English EQ-TIPS-5L version 3.0. `W1 kaizen DCE` plans 400 respondents, two blocks, and 14 tasks per person. `W2 paired-comparison DCE` plans 1,000 respondents, five blocks, and 28 tasks per person. Wave 2 design and survey materials will be revised from wave 1 evidence. `A1 discordance analysis`, `A2 main-effects conditional logit`, and `A3 cross-wave agreement and prediction` are separate streams. `Q1 beta and technical pilot` supports the first-wave materials.

**Evidence context and referents.** Planned evidence suppliers are 1,400 Australian adults from an online market panel. Quotas use age, gender, and ancestry. Adults first imagine a real one-year-old child whom they know and complete a child-description and EQ-TIPS familiarization task for that child. In the DCE, the referent is a hypothetical one-year-old child with a one-month acute episode starting today and full recovery after one month. Adults make the choices; infants and toddlers are not respondents.

**Instrument roles and administration.** Experimental EQ-TIPS-5L version 3.0 is the target of descriptive-system preference testing and source of seven-attribute profiles. It is not produced by this paper. Respondents also complete EQ-5D-5L and 13 bolt-on questions about their own health as survey familiarization and context. Those health results are not principal outcomes. LimeSurvey supplies unattended web self-report. A representation task, checklists, warm-up, information buttons, open-text review, a ten-minute speeding rule, and duplicate prevention are planned quality controls.

**Task and analysis path.** Each kaizen task starts with one profile and asks the respondent to select sequential improvements. Four changes improve the profile, and one `aku` change makes it worse. Selecting the worse change early is type-1 discordance; leaving an improvement last is type-2 discordance. The task produces a preference path and more choice probabilities than one paired comparison. Wave 2 asks respondents to choose between two problem profiles. Conditional-logit main effects test decision relevance. Cluster bootstrap methods support uncertainty, and Lin's concordance and out-of-wave prediction compare task forms. Sensitivity analyses cover block, task order, attribute order, respondent discordance, and sample size.

**Product and states.** `Two-wave DCE protocol for descriptive-system development` is a completed named methodological product. The wave-1 survey, experimental design, and analysis plan have beta and technical-pilot evidence. Main preference evidence is not complete. The paper does not produce a revised EQ-TIPS version, a value set, or a psychometric result.

**Author interpretation and implications.** The authors expect preference evidence to identify inversions or redundant response levels before an instrument is final. They present kaizen tasks as a less burdensome and statistically efficient development tool and plan to compare them with conventional paired choices. These are planned instrument-development and methods implications.

**Limitations, gaps, and source uncertainty.** Online panel data can have fraud, selection, and comprehension limits. Kaizen asks respondents to choose improvements, while paired comparison asks them to choose between problems, so task framing changes with task form. The child scenario can cause distress. Wave 2 is not frozen independently because wave 1 will shape it. `definition or boundary`: planned age quotas are listed as 18-29, 30-44, 45-64, and 55 or older. The last two bands overlap. Retain the stated bands and do not repair 55 to another value.

### 8. 10.1007/s40258-025-00954-z — direct and crosswalk EQ-5D-5L value-set comparison

**Classification and purpose.** Mapping or scoring study, health-state valuation study, and methods study; completed. The paper compares national EQ-5D-5L crosswalk value sets derived from 3L products with directly elicited EQ-VT 5L value sets. It tests scale, rank, profile-level agreement, the mobility wording difference, and score effects in observed profiles.

**Components and provenance.** `P1-P19 country product pairs` cover 18 countries: Canada, China, Denmark, France, Germany, Italy, Japan, the Netherlands, Poland, Portugal, South Korea, Spain, Taiwan, Thailand, Trinidad and Tobago, the United States, Hungary, and Romania. The United States has two pairs. Sixteen countries use 3L and 5L products from separate studies. `G1 parallel valuation pairs` covers Hungary, Romania, and a second United States pair in which the same respondents completed 3L and 5L EQ-VT tasks. `A1 full-state agreement`, `A2 severe-state and one-dimension ranks`, `A3 mobility-level pattern`, and `A4 reverse crosswalk` compare products. `D1 multi-instrument comparison data` applies all pairs to 7,933 profiles from healthy people and people with nine stated conditions.

**Score-construction paths.** Each derived path is `national EQ-5D-3L value set -> Van Hout response-mapping algorithm -> national EQ-5D-5L crosswalk value set`. Each direct path is `national EQ-5D-5L EQ-VT preference data -> national EQ-VT value set`. Source 3L products use TTO or DCE plus TTO and can be older. EQ-VT products use cTTO and DCE under a standard protocol. The crosswalk algorithm was developed with European patient response data. The extreme mobility wording changes from `confined to bed` in 3L to `unable to walk about` in 5L. In the three parallel pairs, sample and much of the protocol are held constant, but each respondent values a smaller 3L task subset.

**Comparison method.** The study compares value range, mean, 55555, negative-state proportion, single-dimension level-5 ranks, and severe profiles. Spearman, Pearson, and Lin correlations, mean absolute difference, scatterplots, and Bland-Altman plots assess association and agreement across all 3,125 profiles. Publication interval is a proxy for preference-data time difference. Reverse crosswalks test the mobility pattern in 3L. Application to observed profiles tests mean utility differences overall, for severe profiles, and for respondents unable to walk.

**Products and states.** The paper generates 19 crosswalk tariff outputs for comparison. They are completed derived analytic scoring outputs, not newly recommended national value sets. The direct national value sets and source 3L products are reused completed products from their source studies. The paper's reusable contribution is comparative evidence and author guidance about when crosswalk scoring is acceptable.

**Principal findings.** Spearman correlations range from 0.831 to 0.989 and are below 0.9 in 11 pairs. Average mean absolute difference is 0.149 and is below 0.1 in only five pairs. Negative-state proportions, ranges, and 55555 values differ materially. No pair keeps the same rank across the five isolated level-5 dimensions. Mobility-level-5 profiles form a distinct Bland-Altman band in 15 pairs, including the three parallel studies. All 19 pairs give different mean utilities in the multi-instrument data, and the direction differs by country and subgroup.

**Author interpretation and implications.** The authors conclude that direct and crosswalk 5L products are not interchangeable. Parallel studies support a material role for the mobility wording change. The authors still recommend direct 5L valuation where feasible and allow crosswalk use for very small populations where direct studies are impractical. This is author guidance, not an observed reimbursement effect.

**Limitations and stated gaps.** Across most countries, protocol, sample, time, modeling, and crosswalk-population transport differ together. Even the three parallel cases cannot quantify every driver. Publication interval is only a proxy for collection interval. The observed-profile mobility subgroup has only 28 people. The paper cannot assign the total difference to wording alone or predict one direction for all decision models. It calls for more pairs and tests of aligned mobility wording, modeling choice, and diagnostic performance.

### 9. 10.1177/0272989x251380556 — uncertainty in health-state values used in cost-effectiveness analysis

**Classification and purpose.** Methods study; completed. The paper defines sources of uncertainty around health-state values, traces how they enter and accumulate from valuation to cost-effectiveness analysis, and recommends information that value-set producers and users should report.

**Components and evidence boundary.** `F1 uncertainty-type framework` distinguishes variability, heterogeneity, statistical uncertainty, and methodological variation. `F2 evidence-processing chain` links valuation, profile data, other descriptive-system data, mapping, disease-state studies, meta-analysis, and cost-effectiveness modeling. `F3 valuation-study source table` organizes design, elicitation, and modeling sources. `E1 EQ-5D-3L worked example` shows how a variance-covariance matrix can yield standard errors for profile values. The paper uses prior literature and an analytic example. It does not report a systematic search, an included-study count, or a quality appraisal, and it has no new human respondent sample.

**Instrument and data roles.** EQ-5D-3L, EQ-5D-5L, SF-6D, HUI, and other descriptive systems are examples in the framework. They are not administered measures in this paper. The central objects are health-state profiles, coefficients, value sets, mapped values, disease-state means, QALYs, and ICERs. A value attached to a profile is distinct from the regression coefficients that generate it and from a patient distribution that later uses it.

**Uncertainty path.** Valuation studies generate uncertainty through population choice, sample frame, selected states, normative scale assumptions, engagement, preference heterogeneity, task method, administration, fraud, summary statistic, model form, and misspecification. Profile studies add response and sampling uncertainty. Mapping inherits source profile and value-set uncertainty and adds joint-distribution, algorithm, and transport uncertainty. Disease-state estimates add clinical sampling and profile-distribution uncertainty. Meta-analysis adds dependence and combination choices. Cost-effectiveness models inherit these sources and add health-state, duration, survival, and modeling choices. The paper stresses that inherited uncertainty can be hidden when only a point estimate enters the next stage.

**Product and states.** `Health-state-value uncertainty taxonomy and propagation framework`; completed conceptual output and author-proposed reporting and methods guidance. It asks studies to report profile-level standard errors or the value-model variance-covariance matrix. It is not a formal consensus guideline and does not establish one required sensitivity-analysis method.

**Principal findings and author interpretation.** The authors find that value-set publications usually emphasize point estimates and coefficient uncertainty but do not give profile-value uncertainty needed by decision models. In the worked EQ-5D-3L example, profile standard errors are small relative to the value range, but the authors state that this need not hold in smaller or less constrained studies. They interpret methodological uncertainty and cumulative propagation as underdeveloped areas.

**Implications, limitations, and stated gaps.** The authors ask valuation researchers, instrument developers, trial researchers, decision modelers, HTA bodies, and guideline developers to report and use uncertainty more fully. This is an author-reported methods and policy implication. The framework is stated to be nonexhaustive and does not estimate the relative importance of its sources. It does not give an empirical propagation analysis for a complete valuation-to-CEA chain. The authors call for methods to quantify unresolved sources and for reporting standards that make sensitivity analysis possible.

### 10. 10.1007/s11136-025-03996-x — co-designed EQ-5D-Y-5L outpatient workflow

**Classification and purpose.** Implementation study; mixed status. This completed phase co-designs the P-PROM ROCK Program for EQ-5D-Y-5L use in Australian pediatric outpatient visits. A later clinical pilot and outcome evaluation remain planned.

**Components and reuse.** `D1 phase-1 qualitative findings` supplies four design topics: display, workflow integration, response to problems, and family engagement. `W1-W5 co-design workshops` combine discovery, definition, development, and delivery tasks. `F1-F9 feedback sessions` refine prototypes. `O1-O2 optimization sessions` use mock patient-clinician visits in Epic. `P2 final P-PROM ROCK prototype` combines six workflow elements. `P3 phase-3 clinical pilot` is planned. The paper reuses phase-1 findings and recruits some people from phase 1 and the Australian pediatric multi-instrument study, but it does not reuse their health outcomes.

**Evidence context and participant roles.** The setting is the Royal Children's Hospital tertiary outpatient service in Melbourne, Australia. Main-text co-design participants are two adolescents aged 14 and 16, three mothers of children aged 7 to 11, and 11 service providers from clinical and electronic-record roles. They supply design evidence and lived experience. They are not a sample of routine EQ-5D-Y-5L health responses. Optimization sessions add two mock patients and two providers. Recruitment uses earlier participants, professional networks, and snowballing.

**Method path.** The study combines a seven-step public-service co-design framework with the Double Diamond model. Participants receive sensitization material and complete EQ-5D-Y-5L to learn the task. Workshops use discussion, anonymous input, vignettes, creative design, and electronic-record demonstrations. The team makes draft prototypes and returns them for feedback. Mock consultations test workflow navigation and prompt final changes. This is iterative design and mock workflow testing, not a psychometric assessment or clinical-effect study.

**Instrument role and clinical data-use path.** EQ-5D-Y-5L is the target of implementation design. Planned routine completion can be child self-report or caregiver proxy report. Completion links to a visit and can occur in Epic MyChart up to seven days before the appointment or on paper that day, with reminders. The system displays item wording and levels, not a preference-weighted utility. A longitudinal display reverses the item direction so that higher indicates better health. Patients or caregivers select the items that they want to discuss. The assigned clinician must review results and can use discussion prompts, urgent pathways, or community resources. Separate family resources follow self and proxy completion.

**Product and implementation state.** `P-PROM ROCK Program` is an `implementation workflow or resource package`. It includes clinician training, patient information, item and longitudinal displays, a journey map, family resources, and clinician decision support. Development state is `co-designed prototype`; evidence consists of two mock patient-clinician workflow sessions; implementation stage is `proposal`. It is not yet a clinical pilot, limited routine use, or scaled routine use. Phase 3 will test feasibility, active use, decisions, and patient-care effects.

**Principal findings and author interpretation.** Participants reject a utility-only display for individual visits and prefer item-level results, patient-controlled flags, clear review ownership, and action resources. The authors interpret these features as necessary for PROM data to affect a visit. They state that collection without review and action is insufficient. They do not report actual improvement in communication, decisions, health, or service performance.

**Limitations, gaps, and source uncertainty.** Few adolescents and caregivers participate, several workshops include providers only, and not all participants attend each workshop. Online technology and joint professional-consumer settings can create participation and power barriers. Participants can favor early adoption. Non-English-speaking families are absent, and transfer to other ages, hospitals, or health systems is unknown. `summary versus main text`: the abstract reports nine service providers, while the main results report 11 across the workshops. Retain 11 as the detailed main-text count and keep the abstract count as a conflict.

## Round 4 granularity decisions and evidence

### Decisions added or revised

46. **Separate the preference task from its inferential purpose.** PTO, EQ VAS, cTTO, and DCE can all elicit preferences, but they estimate different objects and support different products. Record task form, perspective, anchor, target, analysis, and intended inference separately. Papers 1, 2, 3, and 7 support this decision. It supports user questions 1, 9, 10, 12, 14, 20, and 21.

47. **Add a social value or priority-weighting study family and a PTO-specific path.** A PTO path must identify the two recipients, their ages, health gains, equivalence or forced-choice form, search procedure, and the social weight inferred from the threshold. Do not represent the result as a health-state utility. Paper 1 supports this decision. It supports user questions 1, 2, 6, 9, 10, 12, 13, 17, 20, and 21.

48. **Record the perspective and scale of experienced valuation.** For an EQ VAS or related experienced-health analysis, record who reports health, whether the scale is anchored at death, whether coefficients are adjusted population associations, and whether a value set is produced. Paper 2 supports this decision. It supports user questions 3, 6, 10, 12, 13, 15, 20, and 21.

49. **Represent administration comparisons as bundles when factors co-vary.** Mode, interviewer presence, scheduling, supervision, task interface, and sample recruitment can change together. Record each feature and the comparison, but do not assign a causal effect to one feature without an identifying contrast. Paper 3 supports this decision. It supports user questions 8, 9, 11, 13, 16, 20, 21, and 24.

50. **Resolve direct proxy paths and cross-informant agreement.** Record the proxy role, requested perspective, target person, relation to the target, independent or joint completion, and the self-report comparator. Treat proxy-self agreement as cross-informant evidence, not test-retest reliability. Paper 4 supports this decision. It supports user questions 4, 6, 8, 11, 12, 13, 20, and 24.

51. **Keep adaptation and content-validity components separate when they occur in one paper.** Link each component to its own sample, method, instrument scope, finding, and product state. Do not transfer content findings to untouched instrument elements. Paper 5 supports this decision. It supports user questions 3, 4, 5, 9, 14, 16, 20, 21, and 23.

52. **Let measurement properties target methods and analytic products, and record the aggregation level.** Reliability can concern elicited weights, anchoring factors, personal functions, or aggregate tariffs. Stable aggregate outputs do not establish stable individual outputs. Paper 6 supports this decision. It supports user questions 9, 12, 13, 15, 16, 20, and 21.

53. **Treat preference tests of a descriptive system as instrument development unless they estimate a scoring product.** DCE evidence can test level order or attribute relevance without producing an anchored value set. Paper 7 supports this decision. It supports user questions 1, 3, 9, 10, 12, 14, 20, 21, and 23.

54. **Make direct and derived scoring-product pairs explicit.** Each comparison must preserve the direct product, source product, mapping algorithm, derived product, population, date, protocol, and matched or unmatched design features. Paper 8 supports this decision. It supports user questions 3, 4, 12, 13, 19, 20, 22, 23, and 25.

55. **Add concise uncertainty provenance for material results and products.** Record the source of uncertainty, the object affected, inherited inputs, propagation step, reported uncertainty representation, and any missing propagation. Do not create one ontology entity for every coefficient or hypothetical source. Paper 9 supports this decision. It supports user questions 12, 13, 16, 19, 21, 22, and 25.

56. **Add an implementation workflow or resource-package product.** It can contain training, displays, reminders, decision support, workflow ownership, and family resources. Record its development, evidence, and implementation states separately from the instrument. Paper 10 supports this decision. It supports user questions 5, 6, 9, 11, 12, 14, 17, 18, 20, 23, and 24.

57. **Separate co-design evidence suppliers from routine instrument respondents.** Familiarization completion in a workshop is not clinical outcome evidence. Record the participant's design role, lived-experience role, and any mock-patient role separately from the planned routine respondent role. Papers 7 and 10 support this decision. It supports user questions 3, 6, 9, 11, 15, 20, and 24.

58. **Record dependency between adaptive or phased components.** A later wave or phase can depend on evidence and design changes from an earlier component. Such a component is planned but not independently frozen. Papers 1, 7, and 10 support this decision. It supports user questions 5, 9, 14, 18, and 19.

59. **Tie product status to version, time, and context.** An instrument described as experimental in one paper can later become official, and a protocol can target a named version that changes again. Preserve the paper-time status and do not silently replace it with later status. Papers 4, 7, and 10 support this decision. It supports user questions 4, 14, 19, 23, and 26.

### Important distinctions considered and rejected in round 4

- **One generic valuation study class for PTO, EQ VAS, cTTO, and DCE:** rejected. The tasks, anchors, perspectives, estimands, and products differ.
- **PTO as TTO, or a social priority weight as a health-state utility or QALY weight:** rejected. PTO compares recipients and benefits to estimate relative social priority.
- **Unanchored experienced EQ VAS associations as a QALY-ready value set:** rejected. Paper 2 does not anchor values at death or produce a preference tariff.
- **An online versus face-to-face label as an isolated causal effect:** rejected. Paper 3 changes several administration and recruitment features together.
- **Automatic removal of better-than-dead or non-trader responses as invalid:** rejected. Their analytic meaning depends on the protocol and stated estimand.
- **Parent, caregiver, and proxy as synonyms, or proxy 1 and proxy 2 as one perspective:** rejected. Role and requested viewpoint are separate facts.
- **Proxy-self agreement as test-retest reliability:** rejected. It compares informants, not repeated measurements from one informant.
- **A ceiling distribution as content-validity evidence only because it appears under that paper heading:** rejected. Preserve the actual distribution result and its measurement-property meaning.
- **A five-level proxy instrument as superior on every property:** rejected. Relative performance differs by property, informant, and subgroup.
- **Content-validity results transferred to EQ VAS, untouched response levels, or psychometric performance:** rejected. Each claim keeps its tested scope.
- **Stable aggregate OPUF tariffs as evidence of stable personal utility functions:** rejected. Paper 6 shows that these aggregation levels can give different conclusions.
- **Test and retest OPUF tariff outputs as established German EQ-HWB-S products:** rejected. They are comparative analytic outputs from one methods study.
- **A DCE protocol as a completed value set or final instrument:** rejected. Paper 7 tests descriptive-system preferences and has not completed either main wave.
- **Co-design participants as routine PROM respondents:** rejected. They supply design evidence, not a clinical response distribution.
- **Reversed item display values as utility scores:** rejected. Paper 10 displays transformed item directions, not preference weights.
- **A mock-tested prototype as implemented routine use or demonstrated impact:** rejected. Clinical pilot and outcome evidence remain planned.
- **High correlation between crosswalk and direct products as interchangeability:** rejected. Agreement, scale, ranks, and applied mean differences can remain material.
- **Mobility wording as the sole proven cause of all direct-crosswalk differences:** rejected. Parallel pairs support a material role but do not identify the complete effect.
- **Paper 9 as a systematic review, or all cited studies as included evidence units:** rejected. It is a conceptual framework and analytic example without a systematic review method.
- **A separate ontology entity for every uncertainty source and coefficient:** rejected. Use a concise provenance path for material uncertainty and expand only when an application needs it.
- **One universal maturity ladder for all products and evidence:** rejected again. Instruments, value sets, analytic outputs, protocols, guidance, and implementation packages require separate state axes.

## Status of unresolved cases after round 4

1. **Product maturity axes:** The separate development, evidence, and implementation axes remain stable. Papers 5, 7, and 10 show adapted instruments, tested protocol materials, and a mock-tested workflow prototype. Papers 6 and 8 add analytic tariff outputs that must not inherit established-product status.
2. **Mixed study status:** The `mixed` status remains necessary. Papers 1, 7, and 10 contain completed preparatory or design work with planned main evidence.
3. **Concept elicitation, adaptation, and content validity:** Paper 5 resolves part of the boundary. Adaptation and content-validity components can coexist in one paper but remain separate linked components. A direct concept-elicitation-to-instrument-revision case still needs more evidence.
4. **Unusual-scale DIF:** No new round-4 evidence resolves this case.
5. **Evidence-level review context:** Paper 9 does not resolve it because it is not a systematic review. Evidence-level review methods and appraisal still need another application.
6. **Review cardinality and overlapping reports:** No new round-4 evidence resolves this case.
7. **External age rules:** Paper 4 records age 16 as an observed transfer pattern only. A general age-boundary rule remains outside scope.
8. **Conflict types:** The conflict model remains stable. Papers 5, 7, and 10 add arithmetic, definition-or-boundary, and summary-versus-main-text examples.
9. **Proxy perspective:** Paper 4 gives direct proxy-1 evidence and supports the resolved path. An observed proxy-2 application is still absent from the assigned corpus.
10. **Implementation-stage calibration:** Paper 10 sharply identifies proposal and mock-tested prototype states. Limited and scaled routine-use cases still need application evidence.
11. **Mapping transport:** Paper 8 strengthens the path for source product, mapping algorithm, target product, and transport population. The model is usable, but further external validation can test it.
12. **Harmonization relations:** No round-4 application requires a change. The current relation remains provisional.
13. **Scoring source conflicts:** No new round-4 case changes the local conflict rule.
14. **Quality and analytic eligibility:** Papers 3 and 6 reinforce task-specific exclusion, source uncertainty, and analysis sensitivity. A general rule for the effect of exclusions still needs empirical sensitivity evidence.
15. **Normative reference populations:** No new round-4 evidence resolves this case.
16. **Cost constructs:** No new round-4 evidence resolves this case.
17. **Within-profile gradients:** No new round-4 evidence resolves this case.
18. **Overlap confidence and reuse identity:** No new round-4 evidence resolves this case.
19. **Social priority weighting:** Paper 1 supports the new family and PTO path, but it is a protocol. A completed PTO result or another priority-weighting method is needed to test result and product granularity.
20. **Uncertainty propagation:** Paper 9 supports a concise path, but it does not empirically propagate uncertainty through a complete valuation-to-CEA chain. Such an application remains needed.
21. **Reliability aggregation level:** Paper 6 supports separate individual and aggregate targets. Another compositional valuation method is needed to test whether the distinction generalizes.
22. **Co-design workflow evidence:** Paper 10 supports the workflow-package product and mock-test state. Its planned clinical pilot is needed to test routine-use stages and action-effect claims.
23. **Time-specific version status:** Papers 4, 7, and 10 show that status and version can change between publications. Future applications must preserve the status date and exact version when the source supplies them.

## Round 4 run note

- This round preserved the round-1 to round-3 record and added ten batch-04 applications.
- SHA-256 hashes and byte counts matched the batch manifest for all ten assigned papers.
- The main additions are purpose-specific preference-elicitation paths, PTO social priority weights, administration bundles, direct proxy perspectives, separate adaptation and content-validity components, method reliability at individual and aggregate levels, DCE instrument tests distinct from value-set development, paired scoring-product provenance, uncertainty propagation, and co-designed clinical workflows.
- The input context remained the supplied version-2 purpose, questions, task, protocol, README, current Candidate 2 record, batch-04 manifest, and its ten papers.
- One combined display was clipped by the tool. The lineage record was then read fully in smaller sections. No content, manifest, paper, or file issue remained unresolved.
- Agent: fresh version-2 Candidate 2 round-4 agent.
- Run date: 2026-08-16.

## Consolidation review of all 40 applications

The consolidation rechecked every application against its source paper and the final guide. Family-tag normalization was necessary because the development record used several compound or unstable labels. Product-state wording changed only where `established`, bare `tested`, or another general maturity term could hide the type or limit of evidence. Other application content changed only when a late concept exposed a real ambiguity. The table states why no further update was needed.

### Batch 01 backward review

| Paper | Consolidation result |
|---|---|
| 10.1007/s40258-021-00639-3 | Family tags now separate health-state valuation from value-set development. Product states now name a completed national output, valuation evidence, author recommendation, and absent downstream-use evidence. The existing cTTO, DCE, hybrid-model, administration, comparison, and uncertainty limits already support the later guide. |
| 10.1007/s11136-020-02688-y | Family tags now use systematic review or evidence synthesis and measurement-property assessment. No further change was needed because evidence-unit type, duplicate handling, property subtypes, pooling, transfer limits, and review-level context were already explicit. |
| 10.1007/s11136-025-03983-2 | Study protocol and research infrastructure are now separate tags, with population health and methods retained. Product states now distinguish a completed protocol, an ongoing resource, restricted access, and unproduced future norms. Existing phase, language, mode, and planned-expansion detail fits the dependency guidance. |
| 10.1017/s0266462326103602 | The over-broad implementation or practice label is now professional-practice survey. The priority set is a completed survey output, not a tested guideline. Existing instrument-discussion roles prevent false retrieval as instrument administration or valuation. |
| 10.1007/s11136-019-02115-x | The family tag is now instrument development; multilingual wording and harmonization remain stage facts. Product states now identify completed named instrument versions and their exact comprehension, feasibility, and preference evidence. Existing linked label, scaling, cognitive, and harmonization stages already support the later stage and version rules. |
| 10.1007/s40273-022-01216-9 | Family tags now separate health-state valuation, value-set development, and methods. Product states now identify a completed national output and author recommendation. Existing task, child referent, expanded design, model-source, and hybrid-product detail already supports the later inferential-purpose and component rules. |
| 10.1007/s11136-025-04003-z | Family tags now use measurement-property assessment and methods study. No further change was needed because the exact items, response-scale target, task-response inference, DIF reference and focal scales, condition comparisons, and recall-period transfer limit were already explicit. |
| 10.1007/s11136-025-04038-2 | Content validity is now represented as measurement-property assessment, with qualitative concept study retained. Product states name the qualitative sample evidence. Existing comprehensiveness scope prevents transfer to relevance, comprehensibility, or a revised instrument. |
| 10.1016/j.jval.2025.02.001 | Family tags now use systematic review or evidence synthesis and methods study. No further change was needed because trials, reports, and publications are separated; duplicate reports are mapped to trial identity; and profile, EQ VAS, utility, data format, time structure, and missing-data methods are distinct. |
| 10.1007/s10198-025-01770-x | The family tag is now measurement-property assessment. No further change was needed because property, instrument version, language, recall, pain grouping, time point, administration, and no-utility boundary were already explicit. |

### Batch 02 backward review

| Paper | Consolidation result |
|---|---|
| 10.1016/j.jval.2025.01.003 | Family tags now separate health-state valuation from value-set development. Product states now name the bilingual, mixed-contact evidence and population basis. The existing administration bundle and language comparison do not claim causal mode or linguistic equivalence. |
| 10.1016/j.jval.2024.05.016 | Family tags now use health-state valuation and methods study. No further change was needed because DCE with duration, nonlinear time, sample independence, adaptive design, quality exclusions, candidate tariffs, and nonoperational product status were already explicit. |
| 10.1186/s12955-023-02177-z | The family tag is now measurement-property assessment. No further change was needed because responsiveness already has direction, transition anchor, time, subgroup counts, and separate evidence for improvement and deterioration. |
| 10.1007/s11136-025-04150-3 | Content review is now measurement-property assessment linked to instrument development. No further change was needed because expert evidence suppliers, future proxy roles, exact experimental version, content-validity aspects, and absence of a revised product were already explicit. |
| 10.1186/s41687-025-00985-z | Translation, cultural adaptation, and instrument development are now separate tags. Product states now name the translation evidence, committee governance, licensing, and absent psychometric, valuation, proxy, and routine-use evidence. |
| 10.1016/j.jval.2024.03.2195 | Family tags now use measurement-property assessment and methods study. No further change was needed because every property is linked to the bolt-on target and method, while analytic bolt-on combinations are not treated as products. |
| 10.1007/s10198-018-0987-x | The existing mapping or scoring, health economic evaluation, and methods tags already match the final families. No update was needed because score routes, mapping transport, model path, QALY and ICER effects, bootstrap handling, and decision boundary were already explicit. |
| 10.3389/fpubh.2021.744405 | Family tags now use population health, health equity or inequality, and methods study. No further change was needed because level sum score is explicitly not utility and the socioeconomic associations are not causal. |
| 10.3390/curroncol32060308 | The family tag is now implementation study. Product wording now names single-site pilot evidence. Existing proxy-count uncertainty, tested 3L versus planned 5L, workflow burden, and planned scale prevent claims of routine use or impact. |
| 10.1016/j.jval.2024.05.007 | Family tags now use measurement-property assessment and mapping or scoring study. No further change was needed because pooled sources, harmonized variables, recall periods, scoring routes, utility agreement, and paper-time experimental status were already explicit. |

### Batch 03 backward review

| Paper | Consolidation result |
|---|---|
| 10.3390/curroncol32110645 | Family tags now use health equity or inequality and population-health study. No further change was needed because sample reuse, score construction, income construct and reference, model conditioning, noncausal inference, and absent decision effect were already explicit. |
| 10.1016/j.jval.2018.05.002 | Family tags now use health-state valuation and methods study. No further change was needed because experimental arms, crossed wording and perspective, interaction, death tasks, implementation error, and child-referent boundary were already explicit. |
| 10.1007/s40273-018-0642-5 | Family tags now use systematic review or evidence synthesis and measurement-property assessment. No further change was needed because evidence units, duplicate handling, exact properties, crosswalk limit, appraisal, and sparse responsiveness evidence were already explicit. |
| 10.1016/j.jval.2023.03.003 | Family tags now use health-state valuation and methods study. Product states now identify a candidate scoring model with feasibility and cross-validation evidence, not a second national value set. |
| 10.1038/s41433-023-02860-x | Family tags now use cost of illness or burden of disease and population health. No further change was needed because cost categories, bearers, DALY path, monetized wellbeing, excluded categories, and the no-EuroQol-use boundary were already explicit. |
| 10.1177/0272989x251325828 | Family tags now use health-state valuation and methods study. Product wording now identifies comparative analytic tariffs, not national products. Existing anchor, nonlinear-time, scale, reuse, and sample-independence detail already supports the late valuation guide. |
| 10.1186/s12955-024-02266-7 | Family tags now separate health-state valuation, value-set development, and methods. Product states now identify the completed national output and author recommendation. Existing direct-crosswalk comparison and competing explanations remain correctly scoped. |
| 10.1186/s12955-024-02323-1 | Population health and population norms are now separate tags, with equity retained. Product states now identify a dated national reference and update relation. Existing source, mode, scoring harmonization, possible overlap, and temporal limits already support the late guide. |
| 10.1007/s11136-025-04074-y | The compound protocol, infrastructure, and implementation label is now research-infrastructure study and methods study. Product states now name UK pilot evidence and documented research use across 15 countries. Existing quality-rule paths prevent a generic response-rate or representativeness claim. |
| 10.1007/s11136-026-04294-w | Family tags now use health equity or inequality, population health, and methods study. No further change was needed because the identical-profile conditioning rule, outcome filter, source of the rule, alternative mechanisms, and no-filter sensitivity gap were already explicit. |

### Batch 04 final-fit review

| Paper | Consolidation result |
|---|---|
| 10.1371/journal.pone.0302886 | Family tags now use social-priority weighting, study protocol, and methods study. Product states now name formative evidence and absent main results. The PTO path fits without treating the result as utility or QALY weight. |
| 10.1186/s12955-023-02115-z | Family tags now use health-state valuation, population health, and methods study. The application already records own-health perspective, unanchored EQ VAS, source registers, conditional association, time point, and absence of a QALY-ready value set. |
| 10.1007/s11136-020-02712-1 | Family tags now use health-state valuation and methods study. The administration-package representation fits the earlier paper without assigning the result to contact mode or interviewer presence alone. |
| 10.1186/s12955-022-01996-w | The family tag is now measurement-property assessment. The application already separates proxy perspective 1, proxy relation, paired independent self-report, proxy test-retest, cross-informant agreement, and direction-specific responsiveness. |
| 10.1186/s12955-024-02290-7 | Same-language localization is now cultural adaptation, not translation. Instrument development, qualitative concept study, and measurement-property assessment remain separate. Product states now name governance and cognitive evidence, with content-validity scope limited to the tested descriptive system. |
| 10.1007/s10198-025-01769-4 | Measurement-property assessment is now explicit with health-state valuation and methods study. The application already records task, personal-function, subgroup, and aggregate targets, so stable aggregate tariffs do not imply stable personal functions. |
| 10.1136/bmjopen-2025-100897 | Family tags now use instrument development, study protocol, and methods study. Product states now name beta and technical-pilot evidence. The application already separates a descriptive-system preference test from cardinal valuation and records the dependency of wave 2 on wave 1. |
| 10.1007/s40258-025-00954-z | Family tags now use mapping or scoring, health-state valuation, and methods study. Product states now distinguish derived analytic outputs from reused national products. The paired provenance path and matched or unmatched design conditions fit the final guide. |
| 10.1177/0272989x251380556 | The family tag is now methods study. Product states now identify a completed conceptual output and author-proposed guidance. Its concise uncertainty path fits earlier value-set, mapping, review, and economic applications without requiring a separate object for every possible source. |
| 10.1007/s11136-025-03996-x | The family tag is now implementation study. The application already separates co-design roles from routine respondents and records the workflow data path, prototype, mock test, proposal stage, planned clinical pilot, and absent outcome effect. |

## Consolidation decisions

1. **Split over-broad study-family labels.** Health-state valuation and value-set development, translation and cultural adaptation, professional practice and implementation, study protocol and research infrastructure, and population health and population norms now have separate repeatable tags. Papers can take both tags when evidence supports both. This improves retrieval for user questions 1, 3, 9, 14, 20, 21, and 23. Papers 1, 3, 4, and 6 in batch 01; papers 5 and 9 in batch 02; papers 8 and 9 in batch 03; and papers 2 and 5 in batch 04 show the query consequences.

2. **Remove the unsupported primary trial or intervention family.** The assigned corpus contains systematic evidence about trials but no primary trial or intervention application. Trial design remains an evidence-unit or design fact. A future primary application can justify adding a family. This avoids a controlled term with no development-paper application.

3. **Keep content validity inside measurement-property assessment and keep qualitative concept study separate.** Content validity has exact aspects and targets. Qualitative concept work can exist without an instrument assessment. Papers 8 in batch 01, 4 in batch 02, and 5 in batch 04 support this boundary. It resolves a duplicate family and supports questions 2, 3, 9, 12, 14, 20, and 21.

4. **Separate reporting perspective from interviewer support.** Self-report, proxy perspective, and professional opinion describe who reports and from which viewpoint. Interviewer support describes administration. Papers 1 and 10 in batch 01, paper 1 in batch 02, and papers 3 and 4 in batch 04 show that self-report or own preferences can coexist with full interviewer administration. This supports questions 6, 11, 13, 20, and 24.

5. **Retain one preference-task path with a required inferential purpose.** cTTO, DCE, DCE with duration, EQ VAS, PTO, and kaizen tasks remain task forms. `health-state cardinal valuation`, `social-priority weighting`, and `descriptive-system preference test` state what the task supports. This distinction applies cleanly to earlier value-set and methods papers and prevents false product retrieval. It supports questions 1, 9, 10, 12, 14, 20, 21, and 23.

6. **Replace generic product maturity with independent state axes.** The final guide does not use bare `established`, `validated`, or `tested`. It records development state, exact evidence, governance, availability, author recommendation, documented use or effect, and implementation stage. All value-set, language-version, protocol, norms, infrastructure, and workflow applications support these axes. This supports questions 14, 16, 17, 18, 23, and 26.

7. **Keep feasibility as a property, purpose, or implementation result instead of one study family.** Missing-response feasibility, cTTO task feasibility, translation comprehension, technical pilot feasibility, and clinical implementation feasibility are different. Papers 10 in batch 01, 3 and 9 in batch 02, 4 in batch 03, and 7 and 10 in batch 04 show that one family would create false matches. This supports questions 9, 11, 14, 20, and 21.

8. **Require a measurement target and inference level.** Properties can target an instrument, item, score, elicitation task, method, personal function, subgroup tariff, or aggregate product. Papers 7 in batch 01, 3 and 6 in batch 02, and 4 and 6 in batch 04 support this decision. It prevents transfer from aggregate reliability to individual reliability or from distribution to content validity. It supports questions 9, 12, 13, 15, 16, 20, and 21.

9. **Use explicit provenance, harmonization, and dependency relations.** `harmonizes with` was too vague. The final relation names source variables or scores, the rule, and output. It also distinguishes reanalysis, reused scoring products, possible overlap, and a later component that depends on an earlier result. Papers 10 in batch 02, 1, 6, 8, 9, and 10 in batch 03, and 7, 8, and 10 in batch 04 support this decision. It supports questions 5, 13, 19, 25, and 26.

10. **Keep uncertainty provenance concise and conditional.** Use it when uncertainty is a main topic or material to a product or finding. Earlier valuation, mapping, review, and economic applications fit the path, but they do not require a node for every coefficient or hypothetical source. Papers 7 in batch 02 and 9 in batch 04 support this scope. It supports questions 12, 13, 16, 19, 21, 22, and 25.

11. **Retain the paper-first structure and scoped narrative.** Components, controlled terms, repeatable values, and relations remain subordinate to the paper. Exact themes, complex recruitment, principal findings, author interpretation, limitations, and gaps remain concise narrative when further structure does not improve retrieval or comparison. All 40 applications fit this structure without a fixed JSON contract.

## Rejected distinctions after consolidation

- **One combined valuation and value-set family:** rejected because method studies and experience-based valuation need retrieval without implying a completed scoring product.
- **One translation or adaptation family:** rejected because Singapore English is same-language cultural adaptation, while the Egyptian study includes translation into Modern Standard Arabic.
- **One implementation, feasibility, or practice family:** rejected because a practitioner survey, a cTTO feasibility analysis, a translation comprehension study, and a clinical collection pilot answer different questions.
- **One protocol or infrastructure family:** rejected because a protocol can be planned while an infrastructure already contains completed collections and restricted data.
- **Content-validity study as a separate family parallel to measurement-property assessment:** rejected as duplicate. Store content-validity aspects under measurement properties and add qualitative concept study only when concept work is a main purpose.
- **Self-report and interviewer-administered as alternatives on one mode axis:** rejected because respondents can give self or own preferences in a fully interviewer-administered session.
- **A general `validated`, `established`, or `tested` product status:** rejected because it hides which evidence, governance, access, recommendation, or use exists.
- **A separate study-family tag for every design or output:** rejected. Cohort, secondary analysis, product comparison, mixed methods, research priority, and feasibility remain design, purpose, method, or product facts.
- **A controlled primary trial or intervention family without a primary application:** rejected for this candidate. The systematic review applications still record trials as evidence units.
- **One universal method-depth requirement:** rejected. Valuation, measurement, translation, qualitative work, review, implementation, mapping, economic evaluation, norms, equity, and burden studies require different evidence-based extensions.
- **A product for each coefficient set, candidate model, bolt-on combination, or burden estimate:** rejected. Keep an output as a product only when researchers can seek or reuse it and preserve candidate analytic outputs without calling them operational products.
- **Retrospective replacement of a paper-time version or status with later knowledge:** rejected. The application records what the focal paper supports at its time and version.

## Unresolved cases after consolidation

1. **Proxy perspective 2:** The corpus contains observed proxy perspective 1 but no observed application in which a proxy answers as the referent would answer. The terminology is retained because instrument wording can require it, but a future application must test it.
2. **Routine implementation stages:** The corpus supports proposal, mock workflow test, and single-site pilot. It does not contain a focal paper with limited or scaled routine clinical use and measured action or patient effects.
3. **Completed social-priority weights:** The PTO paper is a protocol with formative evidence. No assigned paper tests the result and product detail for completed priority weights or another social-priority method.
4. **Complete uncertainty propagation:** The uncertainty framework traces the chain but does not empirically propagate uncertainty through a full valuation-to-cost-effectiveness path.
5. **Scale-form DIF generalization:** One paper compares frequency and severity as DIF reference and focal forms. More response-scale applications are needed before a narrower controlled subtype is justified.
6. **Concept elicitation that directly changes an instrument:** Adaptation and content-validity components coexist in the Singapore paper, but its open concept work does not directly revise the tested descriptive system. The transition from concept evidence to an instrument change needs another application.
7. **Review context and many-to-many evidence identity:** The current review relations handle publications, trials, and duplicate data, but detailed language, country, version, and overlapping-report context can require study-level reconstruction. No assigned review resolves how much of this is practical.
8. **External age rules:** Two applications include age 16 or ages 16 to 18 against a paper-stated youth target range. These remain paper-scoped transfer limits because external instrument documentation is outside the experiment.
9. **Causal effect of quality exclusions:** The corpus records rule source, threshold, action, and sensitivity when available. It does not give enough evidence for a general claim about how exclusions change validity.
10. **Mapping transport validation:** Source instrument, development sample, target version, value set, algorithm, and application sample are stable parts of the path. More external validation studies are needed to test a controlled transport conclusion.
11. **Normative reference-population boundaries:** The UAE paper supports an explicit membership rule for a mobile national population. The corpus does not establish a general rule for citizenship, residence, language, or eligibility in preference populations.
12. **Within-profile socioeconomic gradients:** The application preserves omitted health content and reporting heterogeneity as competing author explanations. The design does not separate these mechanisms.
13. **Reuse overlap confidence:** `documented absent`, `documented present`, `possible`, and `not stated` work for current cases, but no application tests more complex probabilistic or partial overlap.
14. **Generalization of aggregation-level reliability:** OPUF shows stable aggregate tariffs with unstable personal functions. Another compositional valuation method is needed before this pattern can be generalized.
15. **National burden estimates as reusable products:** One cost-of-illness paper uses its estimate as a benchmark. The evidence is not enough to add a separate controlled product type for modeled burden estimates.

## Consolidation run note

- The consolidation preserved all four development-round applications, decisions, rejected distinctions, unresolved cases, and run notes.
- It reviewed the final guide and all 40 applications against the 40 assigned source papers. Every paper has a row in the backward-review tables above.
- All four manifests contain ten papers. SHA-256 hashes and byte counts match for all 40 paper files.
- The final guide integrates late concepts into the core instead of leaving them only as round-specific additions. Application family tags now use the consolidated vocabulary. Product-state wording was updated where a general maturity label could overstate evidence or use.
- Filesystem inputs were `AGENTS.md`; `PURPOSE.md`; `USER_QUESTIONS.md`; `TASK.md`; `PROTOCOL.md`; `README.md`; the complete prior `candidates/candidate-2.md`; all four batch manifests; and the 40 article paths listed in those manifests.
- Filesystem inputs read outside those supplied files: none.
- Mechanical issue: one large display of the lineage record and one combined display of PDF-derived papers were clipped by the tool. The affected material was read again in smaller sections. No paper, hash, byte-count, Markdown, or file-availability issue remained.
- No version-1 file, legacy graph or extraction, hidden selection label, hidden probe, holdout paper, or other lineage was inspected.
- No external guidance or skill file was opened. No paper was added. No commit was made.
- Agent: fresh version-2 Candidate 2 consolidation agent.
- Run date: 2026-08-16.
