# Round 1 decisions and open cases

## Important ontology decisions

### Separate research role from research object

The first two papers both concern EQ-5D-5L, but one creates preference weights and the other reviews measurement properties. A single “EQ-5D study” type would hide this difference. The ontology therefore records research role and exact object separately.

### Separate a descriptive system from its value set

The Danish adult value-set paper and the Chinese youth value-set paper use health states as objects of preference elicitation. The systematic psychometric review and the Brazilian youth study evaluate responses produced by descriptive systems. This distinction prevents utility-model evidence from being treated as item-performance evidence.

### Record evidence status

The EQ-DAPHNIE paper describes a resource and methods, while other papers report completed analyses. The ontology therefore distinguishes a protocol or resource description from completed primary studies, secondary analyses, and syntheses.

### Separate sampled source, target, and perspective

The Chinese youth valuation study motivated this decision. Adults supply preferences, the described person is a hypothetical 10-year-old child, and the value set targets child and adolescent health states. The HTA survey also needs this distinction because individuals report personal views, but the study discusses agency practice. The dyadic pain study needs it because the sample is linked dyads, but analysis is at the individual level.

### Permit component-level research objects

The pain and discomfort study compares frequency and severity response scales, not complete instruments. The randomized-trial review compares EQ-5D data outputs and their analysis. The ontology therefore permits dimensions, items, scales, recall periods, visual analogue scales, and utility outputs as first-class research objects.

### Keep property-specific findings

The Brazilian youth study shows known-group validity with poor-to-moderate test-retest reliability. The psychometric review also separates index reliability from item stability and responsiveness. The ontology does not reduce these results to one “valid” field.

### Record model selection criteria, not only model names

The two valuation papers compare several statistical models. Their decisions depend on logical consistency, coefficient monotonicity or significance, prediction, and sensitivity analysis. These criteria explain why a model became a value set. A model label alone does not.

### Record conceptual scope decisions

The Chinese quality-of-life framework excluded external, material, time-dependent, future, and biological-system concepts before comparison with EQ-HWB. These exclusions affect what “comprehensive” means. The ontology records explicit inclusion and exclusion rules under design and applicability.

### Treat representativeness as a qualified claim

Several papers target representative populations through quotas, registers, panels, or post-stratification. The methods do not provide the same support. The ontology records sampling method, design target, author claim, demonstrated comparison, and limits as separate parts.

### Include transparency and institutional relation as optional meta-research context

Every paper in this batch received EuroQol funding, and many papers report member, employee, or consultancy relationships. This information can matter for meta-research, but it does not prove bias. The ontology records the disclosed relation and any funder-role statement without a causal judgment.

## Development sequence in this round

1. Papers 1 and 2 established contribution, object, population, design, evaluation, output, and limit as the initial structure.
2. Paper 3 added evidence status and resource or protocol outputs.
3. Paper 4 added practitioner role, organization target, and observed-use context.
4. Papers 5 and 6 added artifact origin, multi-phase development, and valuation perspective.
5. Paper 7 added component-level objects, secondary data, and separate informativity and discrimination properties.
6. Paper 8 added conceptual frameworks, content coverage, and explicit scope rules.
7. Paper 9 added trial-level evidence units and analysis-practice objects.
8. Paper 10 confirmed the need for property-specific findings, a priori hypotheses, retest status, and subgroup application.

No prior lineage ontology was present, so no earlier applications required revision.

## Unresolved cases

### Internal source conflicts

- The Chinese youth value-set paper reports 14 recruitment regions or provinces and cities in its abstract and methods, but its key-points box reports 4 regions.
- The Chinese quality-of-life framework paper reports 68% sub-theme alignment and gives the fraction as `18/57`. These values are not arithmetically consistent.

The applications preserve these conflicts. A later round must not silently select one value unless new lineage evidence resolves it.

### Meaning of representativeness

The papers use “representative” for register-based sampling, quota samples, online panels, and non-probability recruitment. The current ontology qualifies the claim but does not define one threshold. More papers can show whether stable categories for achieved representativeness are useful.

### Multi-phase and multi-sample structure

The instrument-development and valuation papers contain phases, countries, task-specific samples, and different quality-control procedures. The current applications describe these within one paper. A later round can test whether a reusable sub-study element improves comparison without making the ontology difficult to read.

### Informativity and discrimination

The response-scale paper uses Shannon indices for response-category informativity and item response theory for discrimination. These terms are related but not equivalent. They remain separate. Later evidence can show whether a broader parent term is useful.

### Target age and observed age

EQ-5D-Y is described for ages 8 to 15 in the instrument-development paper, but the Brazilian study applies it to ages 8 to 18. The ontology records both the stated instrument target and the observed application. It does not decide whether the extension is valid.

### Content-validity conclusion after code exclusions

The Chinese framework paper concludes that EQ-HWB is comprehensive after it excludes several external and material concepts. The current ontology treats these rules as a scope condition. Human review can decide whether those exclusions are appropriate for health and social care outcomes.

### Endpoint status in evidence synthesis

The randomized-trial review labels an EQ-5D outcome “exploratory” when a source does not identify it as primary or secondary. This supports review coding but may not represent the planned trial status. The application records the rule. A later ontology may need separate reported and review-assigned values.

### Conclusion strength in the Brazilian youth study

The paper recommends use while it also reports poor-to-moderate descriptive-system reliability and up to 12.7% missing response for one EQ-5D-Y-5L dimension. The application uses a qualified conclusion. It does not convert the authors' broad final statement into an unqualified ontology judgment.

# Round 2 decisions and open cases

## Ontology changes

### Add distinct study roles for translation, method evaluation, application, and implementation

The Arabic EQ-5D-Y-5L paper produces a language and cultural version rather than a new construct or response system (`10.1186/s41687-025-00985-z`). Translation and cultural adaptation is now an explicit role.

The DCEd paper compares valuation methods (`10.1016/j.jval.2024.05.016`). The dialysis paper tests the effect of mapping and scoring choices on a decision model (`10.1007/s10198-018-0987-x`). These papers motivated the method-evaluation role.

The health-inequality paper uses EQ-5D outputs to study a social pattern (`10.3389/fpubh.2021.744405`). The dialysis paper uses utilities inside a cost-utility analysis. These papers motivated the outcome or decision application role.

The Ontario oncology paper tests a routine collection workflow (`10.3390/curroncol32060308`). Its question differs from both instrument measurement properties and surveys of current practice. It motivated the implementation or feasibility role.

### Add derivation and compatibility as a core element

The dialysis paper contains several chains from observed or mapped measures to utilities, QALYs, and ICERs (`10.1007/s10198-018-0987-x`). The EQ-HWB-S paper pools datasets and compares utilities made by different scoring routes (`10.1016/j.jval.2024.05.007`). The Arabic paper derives a study-final language version from an English source through translation and cognitive testing (`10.1186/s41687-025-00985-z`).

The ontology now records the shortest material derivation chain. It also records compatibility conditions such as instrument version, population, language, recall period, value-set country, mode, and time. This change prevents a mapped score from appearing to be directly observed data.

### Use study components for materially different samples, tasks, or data origins

The DCEd paper uses separate EQ-VT and DCEd samples, modes, periods, and quality procedures (`10.1016/j.jval.2024.05.016`). The EQ-HWB-S paper pools two valuation-study datasets with different order, background questions, and periods (`10.1016/j.jval.2024.05.007`). These papers resolved the round-1 open case in favor of a reusable study-component element.

A component remains inside one paper application. The ontology uses it only when the distinction changes the evidence source, target, task, timing, output, or evidence status. It does not require a separate record for each analysis.

### Expand object roles and relations

Round 2 needed input and output roles in addition to focal, comparator, reference, and context. Mapping functions supply utilities to decision models (`10.1007/s10198-018-0987-x`). Bolt-ons are added to a descriptive system (`10.1016/j.jval.2024.03.2195`). A language version is translated and adapted from a source version (`10.1186/s41687-025-00985-z`). The ontology now names these relations.

### Record participation flow and implementation workflow

The Ontario pilot reports different counts for enrollment, optional feasibility responses, follow-up, interview interest, and completed interviews (`10.3390/curroncol32060308`). The DCEd study has a large quality-control exclusion flow (`10.1016/j.jval.2024.05.016`). The Graves' disease cohort has two follow-up samples (`10.1186/s12955-023-02177-z`).

The ontology now records the participation stage and denominator when they change interpretation. It also records the collection setting, schedule, and staff workflow when these are under study.

### Expand evaluation criteria without merging them

Round 2 adds translation equivalence, severity ordering, and comprehension (`10.1186/s41687-025-00985-z`); method agreement and downstream decision effect (`10.1016/j.jval.2024.05.016`; `10.1007/s10198-018-0987-x`); bolt-on ceiling reduction and added discrimination (`10.1016/j.jval.2024.03.2195`); and response burden, retention, and collection feasibility (`10.3390/curroncol32060308`).

These criteria remain separate. For example, a bolt-on can reduce the ceiling without having a value set. A collection process can be acceptable to respondents but still have low follow-up or high staff burden.

## Retention decisions

### Retain the separation of a descriptive system, score, and value set

The Graves' disease study evaluates dimension responses, a Hong Kong index, and EQ VAS as distinct outputs (`10.1186/s12955-023-02177-z`). The health-inequality study uses an equal-weight level sum score and does not use utilities (`10.3389/fpubh.2021.744405`). The EQ-HWB-S study compares descriptive content and two utility routes (`10.1016/j.jval.2024.05.007`). These cases confirm the round-1 decision.

### Retain property-specific findings and scoped conclusions

The Graves' disease study finds responsiveness for worsening but not improvement. The bolt-on study reports different strengths by bolt-on and condition. The EQ-HWB-S study shows group discrimination and convergence but also individual utility disagreement. A single “valid” result would hide these differences.

### Retain qualified representativeness

The UAE value-set study combines quotas with network, snowball, public-place, and social-media recruitment (`10.1016/j.jval.2025.01.003`). The Hungarian bolt-on study uses soft quotas in an online panel (`10.1016/j.jval.2024.03.2195`). The health-inequality study targets population distributions through web panels (`10.3389/fpubh.2021.744405`). The ontology continues to separate the design target, author claim, achieved comparison, and recruitment limit.

### Retain disclosed institutional relations as context, not a bias label

All ten round-2 papers report EuroQol funding or support. Some authors report membership, and several papers state that the funder had no role. The ontology continues to record these facts without inferring an effect on results.

## Development sequence in this round

1. Paper 1 confirmed the valuation structure and added a changing-population and bilingual compatibility case.
2. Paper 2 added method evaluation and established the study-component element.
3. Paper 3 confirmed directional responsiveness, follow-up flow, and property-specific conclusions.
4. Paper 4 extended conceptual evaluation to proxy construct boundaries and expert-stakeholder evidence.
5. Paper 5 added translation, cultural adaptation, and artifact maturity.
6. Paper 6 added bolt-ons, incremental measurement value, and conditional item selection.
7. Paper 7 added derivation chains from measures to decision outputs.
8. Paper 8 added substantive outcome application and clarified the difference between level sum scores and utilities.
9. Paper 9 added pilot implementation, workflow, and denominator-specific feasibility.
10. Paper 10 confirmed pooled study components and scoring-route compatibility.

## Unresolved cases

### Internal source conflicts remain explicit

The two round-1 conflicts remain unresolved. Round 2 adds three conflicts:

- The UAE value-set abstract and Results section report different age, sex, and national-status summaries (`10.1016/j.jval.2025.01.003`).
- The EQ-TIPS invited group counts total 43, while the stated total is 44. The listed final group counts also imply ten non-attendees, while the paper states 11 (`10.1007/s11136-025-04150-3`).
- The Ontario pilot abstract and Results section give different percentages for the same willingness counts. The Results percentages use the 160 feasibility respondents (`10.3390/curroncol32060308`).

Applications preserve all values. No lineage evidence resolves them.

### Method agreement does not yet establish interchangeability

The DCEd comparison uses one country, different samples, different modes, and a large DCEd exclusion flow (`10.1016/j.jval.2024.05.016`). The ontology records the authors' promising alternative conclusion as conditional. More settings are needed before DCEd and EQ-VT can be treated as interchangeable.

### Translation completion and measurement validation are different stages

The Arabic paper produces a final version within its process, but it does not report reliability, validity, responsiveness, or a value set (`10.1186/s41687-025-00985-z`). It also proposes use outside Egypt only after local validation. Later rounds can test whether artifact maturity needs a controlled set of stages.

### Proxy reports can capture the wrong construct

EQ-TIPS experts could not fully resolve whether proxy answers describe child health, development, caregiver concern, or family spillover (`10.1007/s11136-025-04150-3`). They also disagreed about dimension overlap and the age range. The ontology records respondent, described person, and construct boundary, but it does not decide the final EQ-TIPS framework.

### Bolt-on measurement value does not establish valuation suitability

Several bolt-ons improve ceiling and discrimination, but their effect on valuation tasks, value sets, and reference-case comparability remains unknown (`10.1016/j.jval.2024.03.2195`). The ontology keeps measurement evidence separate from valuation evidence.

### Mapping evidence is conditional on the full derivation chain

The dialysis result combines instrument, version, recall, source-sample, value-set, and country differences (`10.1007/s10198-018-0987-x`). It cannot isolate one cause of the QALY and ICER differences. A later paper can test whether a more formal compatibility vocabulary improves comparison without creating a detailed data-lineage model.

### Level sum scores need careful comparison

The bolt-on and health-inequality papers use equal-weight sum scores for method comparison (`10.1016/j.jval.2024.03.2195`; `10.3389/fpubh.2021.744405`). These scores are useful study outcomes but can equate different response profiles and are not utilities. The ontology records the scoring rule but does not set a general rule for when a sum score is preferable.

### Pilot feasibility does not establish scale-up feasibility

The Ontario pilot finds high acceptability but only 60.6% follow-up and material staff, timing, and language barriers (`10.3390/curroncol32060308`). Province-wide implementation also proposes a change from EQ-5D-3L to EQ-5D-5L. The application limits the conclusion to the pilot site and tested version.

### Directional responsiveness depends on the change anchor

The Graves' disease study uses patient-rated overall change after the focal instrument as its six-month anchor (`10.1186/s12955-023-02177-z`). It finds change for worsening but not improvement. The current ontology records the anchor and direction. More studies can show whether anchor independence needs a separate rigor field.

# Round 3 decisions and open cases

## Ontology changes

### Add population or burden estimation as a study role

The vision-impairment paper estimates prevalence-based direct costs, productivity loss, DALYs, and monetized lost wellbeing (`10.1038/s41433-023-02860-x`). The Trinidad and Tobago norms paper estimates national population norms and inequality over time (`10.1186/s12955-024-02323-1`). These contributions are not instrument development or decision-model comparisons. The ontology now gives population or burden estimation an explicit role and adds norms, inequality measures, disability weights, burden measures, and cost categories as research objects.

### Add evidence provenance and sample overlap

Round 3 contains a connected set of reused data. The Ontario equity paper reuses the round-2 implementation sample (`10.3390/curroncol32110645`). The Chinese cTTO paper reuses a round-1 valuation component (`10.1016/j.jval.2023.03.003`). Three Trinidad and Tobago papers reuse or pool the EQ-VT and DCE-with-duration components from the round-2 method comparison (`10.1177/0272989x251325828`; `10.1186/s12955-024-02266-7`; `10.1186/s12955-024-02323-1`). The DAPHNIE quality paper extends the round-1 resource description, and the inequality paper reuses eight-country DAPHNIE data (`10.1007/s11136-025-04074-y`; `10.1007/s11136-026-04294-w`).

The ontology now records whether a paper reuses, filters, pools, extends, or overlaps another study component. This prevents related publications from appearing to provide independent samples.

### Separate the recruited sample from the analysis population

The DAPHNIE quality paper removes bots, speeders, and duplicates and monitors missingness and quotas (`10.1007/s11136-025-04074-y`). The eight-country inequality paper adds age, BMI, profile, and EQ VAS exclusions before analysis (`10.1007/s11136-026-04294-w`). The Trinidad and Tobago norms paper uses a component that had already excluded 611 respondents through valuation-task quality rules (`10.1186/s12955-024-02323-1`).

The ontology now records the analysis population after quality-control, missing-data, and analytic rules. It also records the stage and rationale for each material rule. This is separate from ordinary participation flow.

### Add task framing, anchor, and time preference to compatibility

Wording and the imagined adult or child perspective interact in valuation (`10.1016/j.jval.2018.05.002`). A cTTO-only youth model uses adults who imagine a 10-year-old child (`10.1016/j.jval.2023.03.003`). DCE utilities change materially with the immediate-death or duration anchor and with linear or nonlinear time preference (`10.1177/0272989x251325828`).

The ontology now includes task framing, anchor definition, and the assumed form of time preference as compatibility conditions. A shared descriptive system and country are not sufficient for value-set comparability.

### Add survey integrity, inequality, and burden criteria

The DAPHNIE paper evaluates bots, speeders, duplicates, missingness, consistency, and quota achievement rather than a measurement property of one instrument (`10.1007/s11136-025-04074-y`). The two inequality papers examine demographic gradients and residual differences between profiles and EQ VAS (`10.1186/s12955-024-02323-1`; `10.1007/s11136-026-04294-w`). The vision paper tests cost coverage and sensitivity to disability weights and monetary assumptions (`10.1038/s41433-023-02860-x`).

These criteria are now explicit under evaluation and rigor. They remain separate from reliability, validity, and responsiveness.

## Retention decisions

### Retain the separation of descriptive systems, profiles, scores, and value sets

The 3L-versus-5L review compares descriptive-system properties but uses index values only for selected reliability and responsiveness evidence (`10.1007/s40273-018-0642-5`). The national valuation paper compares a direct value set with a crosswalk (`10.1186/s12955-024-02266-7`). The norms paper applies one value set to both survey years (`10.1186/s12955-024-02323-1`). The DAPHNIE inequality paper holds profiles constant and studies EQ VAS variation (`10.1007/s11136-026-04294-w`). These papers confirm that these objects cannot be merged.

### Retain study components

The norms paper pools three mutually exclusive samples with different modes, dates, recruitment, and quality rules (`10.1186/s12955-024-02323-1`). The component element keeps their provenance visible without turning each analysis into a separate paper record.

### Retain property-specific and scoped conclusions

The systematic review finds a clearer 5L advantage for ceiling and informativity than for reliability or responsiveness (`10.1007/s40273-018-0642-5`). The cTTO-only youth paper supports feasibility but does not replace the hybrid national value set (`10.1016/j.jval.2023.03.003`). The residual inequality paper cannot distinguish omitted content from reporting heterogeneity (`10.1007/s11136-026-04294-w`). One overall positive or negative label would misstate each contribution.

### Retain qualified representativeness

The national value-set sample matches age, sex, and geography but has a 34% response rate and education imbalance (`10.1186/s12955-024-02266-7`). The norms paper pools household and panel samples (`10.1186/s12955-024-02323-1`). DAPHNIE uses non-probability panels, quotas, and weights, with country quota shortfalls and unobserved selection (`10.1007/s11136-025-04074-y`). The ontology continues to distinguish design target, achieved balance, author claim, and remaining limit.

### Retain institutional relations as context

Most round-3 papers report EuroQol funding, membership, employment, or grants. The vision-burden paper has other public and charity funding, and the Ontario equity paper reports an author relationship with Canada's Drug Agency. These relations remain contextual facts. They do not receive an inferred bias label.

## Development sequence in this round

1. Paper 1 linked a secondary equity analysis to its earlier implementation sample.
2. Paper 2 added randomized task framing and an interaction between wording and perspective.
3. Paper 3 confirmed property-specific synthesis and value-set compatibility limits.
4. Paper 4 separated a candidate cTTO-only product from a published hybrid value set.
5. Paper 5 added population burden, cost categories, DALYs, and monetization assumptions.
6. Paper 6 added anchor and time-preference compatibility.
7. Paper 7 confirmed direct-value-set maturity and exposed an internal result conflict.
8. Paper 8 added a pooled population-norm application and made sample overlap material.
9. Paper 9 added resource-level quality gates and analysis-population rules.
10. Paper 10 showed that an exclusion rule can use the focal outcome and affect the phenomenon under study.

The earlier applications did not need a change to their conclusions. The round-3 shared-evidence map adds explicit cross-paper links for earlier source studies.

## Unresolved cases

### Earlier open cases remain

No round-3 paper resolves the earlier internal conflicts, proxy-construct questions, bolt-on valuation gap, level-sum-score question, translation-validation boundary, or anchor-dependent responsiveness. The current lineage retains them as stated in rounds 1 and 2.

### Round-3 source conflicts and terminology

- The Trinidad and Tobago value-set abstract reports 236 negative state values, or 7.6%, while the Results section reports 275, or 8.8% (`10.1186/s12955-024-02266-7`).
- The Trinidad and Tobago norms paper calls its data sources three studies in the abstract and then two studies before it describes three survey components (`10.1186/s12955-024-02323-1`).
- The DAPHNIE quality paper defines its reCAPTCHA boundary as below 0.5 in one method section and as 0.5 or less in another. It also uses “response rate” for link clicks in the abstract while it reports consent and completion separately (`10.1007/s11136-025-04074-y`).
- The DAPHNIE inequality paper states that no datasets were analyzed, despite its reported analysis of 32,327 records (`10.1007/s11136-026-04294-w`).

The applications preserve these statements and do not choose a corrected value.

### Outcome-based exclusion can remove the target phenomenon

The DAPHNIE inequality paper excludes EQ VAS below 50 for full-health profiles and below 30 for other selected mild profiles (`10.1007/s11136-026-04294-w`). The authors treat these values as response errors. However, large profile-versus-VAS disagreement is also relevant to their explanations of omitted content and reporting heterogeneity. No unfiltered sensitivity analysis is reported. It remains unclear how much the rule changes the estimated gradient.

### Immediate death and zero duration are not empirically interchangeable anchors

The DCE analysis estimates immediate death below zero when duration zero anchors the scale (`10.1177/0272989x251325828`). The earlier wording-and-perspective paper also shows that death-based choices change with the imagined person (`10.1016/j.jval.2018.05.002`). The ontology records the anchor and framing but does not define one universal anchor for all countries, instruments, or perspectives.

### A candidate cTTO-only youth set and a final hybrid set have different maturity

The exploratory Chinese paper finds that a cTTO-only model is feasible (`10.1016/j.jval.2023.03.003`). The earlier Chinese valuation paper selected a hybrid model from cTTO and DCE data (`10.1007/s40273-022-01216-9`). The lineage does not select between them. The candidate supports a method option; the hybrid is the final product in the national value-set paper.

### Monetized DALYs combine unlike uncertainty sources

The vision-burden paper combines prevalence, disability weights, a value of statistical life, and cost assumptions (`10.1038/s41433-023-02860-x`). Alternative disability weights change the lost-wellbeing estimate by about fourfold. Reporting totals with and without monetized wellbeing helps, but no ontology rule can make the ethical valuation assumption neutral. Comparative use must retain the full derivation chain.

### Shared respondents can look like repeated confirmation

At least seven round-3 papers reuse data described elsewhere in the lineage. Their analyses answer different questions, but evidence counts must not treat the publications as independent respondent replications. The ontology now records overlap. Exact person-level overlap remains not reported for the possible panel duplication noted within the Trinidad and Tobago norms paper.

### Change in population norms has several possible causes

The 2012 and 2022–2023 Trinidad and Tobago states use a common new value set, which removes one scoring mismatch (`10.1186/s12955-024-02323-1`). Sampling, mode, response behavior, social change, and the post-pandemic period still differ. The paper cannot identify one cause of the lower norms and higher measured inequality.

### Data integrity does not establish population representativeness

Bot, speed, duplicate, and consistency controls improve the DAPHNIE analysis set (`10.1007/s11136-025-04074-y`). They do not address all non-probability panel selection. Quotas and post-stratification also cannot correct unknown factors. Later users must not convert a high data-integrity rating into an unqualified representativeness claim.
