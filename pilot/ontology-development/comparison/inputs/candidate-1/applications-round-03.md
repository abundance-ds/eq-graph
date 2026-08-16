# Round 3 paper applications

The papers appear in batch order. Each application uses the ontology after round 3. It records source-data overlap because several papers analyze the same studies or datasets.

## Batch map

| Paper | Main contribution | Main measurement-chain layer | Evidence basis |
|---|---|---|---|
| 1. Cancer utility and equity factors | Population association analysis | Direct profile, scored utility, and decision-use context | Ontario oncology pilot baseline data |
| 2. Youth wording and perspective | Randomized valuation-method comparison | Profile wording, valuation perspective, and preference evidence | Four-country adult general-public interviews |
| 3. EQ-5D-3L versus EQ-5D-5L review | Comparative measurement-property synthesis | Dimensions, profiles, and scored indexes | 24 publications |
| 4. cTTO-only youth values | Valuation-method feasibility and model comparison | Child-health preference evidence and candidate scoring model | Reused Chinese cTTO sample |
| 5. Economic impact of vision impairment | Cost-of-illness and burden estimation | Clinical observations, DALYs, costs, and modeled societal impact | 2014 national eye survey and service data |
| 6. Immediate-death anchoring | Valuation-model and anchor comparison | DCE with duration, time preference, and QALY-scale anchors | Reused Trinidad and Tobago DCE-with-duration sample |
| 7. Trinidad and Tobago EQ-5D-5L value set | National value-set development | Preference evidence and scoring artifact | Adult general-public EQ-VT interviews |
| 8. Trinidad and Tobago population norms | Population norms, temporal comparison, and inequality | Profiles, scored indexes, EQ VAS, and inequality summaries | Three pooled 2022–2023 surveys plus a 2012 sample |
| 9. EQ-DAPHNIE quality controls | Survey-design and response-data quality evaluation | Data-collection infrastructure and data fitness | UK pilot and 15-country online survey data |
| 10. Hidden socioeconomic gradient | Within-profile outcome comparison | Health profiles, EQ VAS, and equity-use context | Eight-country EQ-DAPHNIE subset |

## 1. Examining the Association Between Equity-Related Factors and EQ-5D-3L Health Utilities of Patients with Cancer

DOI: `10.3390/curroncol32110645`

- **Contribution and stage:** Completed cross-sectional association analysis of baseline data from an earlier oncology implementation pilot.
- **Purpose and layer:** Estimate associations between patient characteristics, socioeconomic factors, EQ-5D-3L dimensions, and scored utilities. The use context is equity-informed HTA, but the report does not model QALYs or decisions.
- **Evidence source and lineage:** A prospective convenience sample of 170 adults who started publicly reimbursed systemic cancer therapy at one Toronto oncology center. Data were collected from May through November 2024. This report reuses the initial responses from the Ontario implementation pilot applied in round 2 (`10.3390/curroncol32060308`).
- **Artifact roles and derivation:** EQ-5D-3L is the data generator. Patient profiles were scored with the Canadian EQ-5D-3L TTO model through the `eq5d` software package. The resulting utilities are analyzed outcomes. Demographic data and cancer site are stratifiers and covariates; EQ VAS was collected but was not the main analyzed outcome.
- **Methods and comparison:** OLS multivariable models compared income, education, employment, marital status, ethnicity, age, and cancer-site groups. Spearman correlations linked ordinal income with each dimension. One model included all cancers without birth sex; another included birth sex after it excluded sex-specific cancers.
- **Evaluation and output:** The paper reports an association, not a measurement-property test. The lowest reported income group and undisclosed income were associated with lower utility. Pain/discomfort and anxiety/depression problem severity were associated with lower income. The output is equity-relevant population association evidence.
- **Limits and uncertainty:** The design is cross-sectional and does not identify a causal income effect. Cancer stage, comorbidity, and other confounders were not included. The sample is small, highly educated, urban, single-site, and selected during treatment. Income was missing or undisclosed for 46.5% of participants. The broad suggestion that trial utilities can overestimate real-world utilities is plausible but is not tested by a trial-versus-real-world comparison in this report.
- **Source issue:** The institutional statement gives an approval date of 17 January 2025, after the reported May-to-November 2024 collection. The supplied report does not make clear whether this date applies only to the secondary analysis or whether it is an incorrect date for the parent study.

## 2. Valuation of EQ-5D-Y and EQ-5D-3L Health States: The Impact of Wording and Perspective

DOI: `10.1016/j.jval.2018.05.002`

- **Contribution and stage:** Completed randomized, four-arm methodological valuation study. It produces comparative preference evidence, not a national value set.
- **Purpose and layer:** Test the separate and interacting effects of descriptive-system wording and valuation perspective on health-state values.
- **Evidence source and perspective:** 805 adults from convenience samples in England, Germany, the Netherlands, and Spain completed computer-assisted personal interviews from May through July 2015. Adults were randomized to value EQ-5D-3L or EQ-5D-Y states and to imagine either their own adult health or the health of a hypothetical 10-year-old child.
- **Artifact roles and framing:** EQ-5D-3L and EQ-5D-Y profiles are co-targets. Adult-self and hypothetical-child perspectives are randomized task frames. cTTO and DCE with immediate-death comparisons provide preference evidence. Immediate death is a comparison option and scale reference, not a health observation from a respondent.
- **Methods and comparison:** The 2-by-2 design aligns interview method and respondent source while changing wording and perspective. Two-way MANOVA, post-hoc tests, and choice-probability tests compare arms. The study also compares cTTO with DCE-plus-death patterns.
- **Evaluation and output:** Wording and perspective interacted. Differences appeared for some intermediate states but not for the worst state. The output supports separate EQ-5D-Y value sets and cautions against using EQ-5D-3L values to score EQ-5D-Y states.
- **Limits and uncertainty:** The adult frame concerns the respondent's own health, while the child frame concerns another hypothetical person. Thus, referent age and self-versus-other perspective change together. Recruitment differed by country, and country-specific tests lacked power. A technical error implemented only one planned DCE block, which reduced the state coverage and prevented the planned DCE model comparison.
- **Metadata and conversion issue:** The structured YAML omits authors, journal, and publication date, although the PDF-derived body contains these fields. The converted text has page furniture and broken line wrapping, but the main sections are readable.

## 3. A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D

DOI: `10.1007/s40273-018-0642-5`

- **Contribution and stage:** Completed systematic review with descriptive synthesis and pooled profile ceilings.
- **Purpose and layer:** Compare the official EQ-5D-3L and EQ-5D-5L descriptive systems and indexes on distribution, informativity, response consistency, responsiveness, and test-retest reliability.
- **Evidence source and lineage:** Twenty-four English- or German-language publications from searches for 2007 through January 2018. Sixteen used patient samples and eight used population samples across 18 countries. Publications could share underlying data when they reported different properties.
- **Artifact roles and provenance:** EQ-5D-3L and EQ-5D-5L are co-targets. Direct profiles and dimension responses support distribution and informativity analyses. Some 5L index analyses used interim crosswalk scores, so their responsiveness or reliability results concern both instrument response and scoring provenance.
- **Methods and comparison:** Most studies used within-person head-to-head administration, often with 5L first. Two did not use direct comparison. The review used a tailored quality appraisal, ranges, counts, Shannon indices, inconsistency rules, and random-effects pooling of full-health proportions.
- **Evaluation and output:** Missingness and profile floors were usually low. The 5L usually reduced ceilings and always increased Shannon information richness. Response inconsistencies were mostly below 5%. Dimension reliability and responsiveness were mixed; index reliability gave more support to 5L. The output is a comparative evidence inventory with qualified support for both versions.
- **Limits and uncertainty:** Populations, languages, order, mode, value sets, and study designs varied. Only three studies assessed responsiveness and six assessed retest reliability. The review-level statement that 5L is similar or better must not be applied to each property. Crosswalk-derived 5L indexes weaken a clean descriptive-system comparison.

## 4. Using Time Trade-Off Values to Estimate EQ-5D-Y Value Sets: An Exploratory Study

DOI: `10.1016/j.jval.2023.03.003`

- **Contribution and stage:** Completed secondary methodological analysis. It estimates a candidate cTTO-only model and recommends the method as an option; it does not replace the published Chinese hybrid value set.
- **Purpose and layer:** Test the feasibility of eliciting and modeling enough cTTO evidence to estimate an EQ-5D-Y-3L value set without DCE data.
- **Evidence source and lineage:** 418 Chinese adults completed face-to-face cTTO interviews from November 2019 through June 2020 in eight provinces or cities. This is the cTTO component of the Chinese youth valuation study applied in round 1 (`10.1007/s40273-022-01216-9`), not an independent valuation sample.
- **Perspective and artifacts:** Adults imagined a hypothetical 10-year-old child. EQ-5D-Y-3L profiles are the valuation target. Twenty-eight selected states and a three-block design provide preference evidence. OLS, heteroscedastic, and random-effects models are candidate transformation artifacts.
- **Methods and comparison:** Feasibility used interview duration, task moves, and three respondent feedback items. The study compared these results descriptively with an earlier Chinese adult EQ-5D-5L valuation study that differed in perspective and quality-control procedures. Candidate models were compared on monotonicity, coefficient significance, and leave-one-state-out prediction.
- **Evaluation and output:** The random-effects model with an all-level-3 term performed best among the tested models. The cTTO distribution was mostly smooth, with one non-trader, and respondents generally reported that tasks and state differences were understandable. The output is evidence that cTTO-only youth models can be feasible when enough states are valued.
- **Limits and uncertainty:** Recruitment combined quotas with public-place and social-network sources and slightly over-represented higher education and women. The feasibility comparison with adult EQ-5D-5L was not a randomized or concurrent comparison. Different perspective, protocol quality control, state design, and interviews can explain the reported differences. High youth-state values and the large drop for `33333` remain substantive modeling questions.
- **Metadata and conversion issue:** The structured YAML omits authors, journal, and publication date, although the PDF-derived body contains these fields. The body is readable but contains page furniture and broken line wrapping.

## 5. The Societal Economic Impact of Vision Impairment in Adults 40 Years and Above

DOI: `10.1038/s41433-023-02860-x`

- **Contribution and stage:** Completed prevalence-based, bottom-up cost-of-illness study with clinical, service-use, burden, and economic-model components.
- **Purpose and layer:** Estimate the 2014 societal impact of presenting vision impairment in Trinidad and Tobago. This extends the measurement chain from clinical observations and survey responses to prevalent cases, cost categories, DALYs, and monetized burden.
- **Evidence source and lineage:** The 2014 National Eye Survey used multistage probability-proportional-to-size cluster sampling. Of 4,263 eligible adults aged 40 or older, 3,589 had vision assessment, 2,792 supplied utilization data, and 2,516 supplied cost data. A contemporaneous national eye-service survey and external unit-cost and disability-weight sources supplied other model inputs.
- **Artifact roles and derivation:** Presenting visual-acuity categories and utilization questionnaires are data generators. Survey weights and national population counts transform sample observations to prevalent cases. Cost categories, unit costs, productivity assumptions, disability weights, DALY rules, and an estimated value of a statistical life are transformation artifacts. The outputs are direct medical, direct non-medical, indirect, intangible, and total societal costs.
- **Methods and comparison:** Survey weighting, post-stratification, multilevel regression, resource-use costing, human-capital productivity estimation, prevalent YLD/DALY estimation, monetization, cost-bearer allocation, and one-way sensitivity analysis. The paper compares vision categories, cost components, and alternative disability weights.
- **Evaluation and output:** The estimated total societal cost was TT$3.84 billion, of which monetized loss of wellbeing was 73.3%. Excluding intangible loss, indirect costs were the largest component. The output is a national burden and cost benchmark, not a psychometric evaluation or a cost-effectiveness result.
- **Limits and uncertainty:** Response differed by questionnaire and was lowest among blind participants. The study excluded people under 40 and institutional residents. It used recall, external unit costs, unmeasured cost assumptions, and a human-capital approach. Alternative disability weights changed the wellbeing estimate about fourfold. Monetizing DALYs through a statistical-life estimate is conceptually and ethically contested, as the authors state.
- **Metadata issue:** The structured author list contains two entries named `S S Ramsewak` with different affiliations. The body refers to Samuel and Shivaa Ramsewak, so the structured names do not distinguish them.

## 6. Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be

DOI: `10.1177/0272989x251325828`

- **Contribution and stage:** Completed secondary valuation-method analysis.
- **Purpose and layer:** Test how the time-preference model and anchor definition affect DCE-with-duration EQ-5D-5L tariffs and their agreement with cTTO values.
- **Evidence source and lineage:** 970 adults in the Trinidad and Tobago DCE-with-duration study, recruited through an internet panel and public places. This is the DCE-with-duration sample used in the round-2 direct-comparison report (`10.1016/j.jval.2024.05.016`). The cTTO benchmark came from a different 1,079-person EQ-VT sample reported in paper 7 of this round.
- **Artifact roles and derivation:** EQ-5D-5L profiles are the valuation target. Split-triplet DCE tasks supply choices involving full-health duration or immediate death. Mixed-logit models with linear or nonlinear time preference generate latent utilities. Anchoring on immediate death or zero duration produces four candidate tariffs.
- **Methods and comparison:** The study compares two time-preference assumptions by two anchors. It then compares the population-level DCE tariffs with the cTTO tariff. The comparison is across separate samples, modes, periods, and task designs; it is not an individual agreement test.
- **Evaluation and output:** Time preferences were nonlinear. Immediate death had a modeled utility below zero when duration was the anchor. Nonlinear time preference with duration anchoring best matched the cTTO tariff. The output is a method recommendation to estimate time preference and use duration, rather than immediate death, as the anchor in similar DCE designs.
- **Limits and uncertainty:** The DCE study had no interview debrief and could not directly confirm understanding or engagement. Speeders were excluded. The cTTO and DCE evidence came from different respondents. A single country and instrument do not establish transfer to other cultures or instruments. Agreement with cTTO is a benchmark comparison, not proof that cTTO gives a true scale.

## 7. The EQ-5D-5L Valuation Study for Trinidad and Tobago

DOI: `10.1186/s12955-024-02266-7`

- **Contribution and stage:** Completed primary valuation study. It produces and recommends a national Trinidad and Tobago EQ-5D-5L value set.
- **Purpose and layer:** Directly elicit national adult preferences, compare valuation models, select a scoring artifact, and compare it with the earlier 5L-to-3L crosswalk set.
- **Evidence source and lineage:** 1,079 adults completed face-to-face interviews from July through September 2022. Household recruitment used age, sex, and geographic quotas. The response rate was 34%. This cTTO/EQ-VT sample is also the comparison sample in the round-2 DCE-with-duration paper and paper 6 of this round. Its self-reported EQ-5D data form survey 1 of paper 8.
- **Artifact roles and derivation:** EQ-5D-5L profiles are the target. cTTO and DCE supply preference evidence. Heteroscedastic Tobit, mixed-logit, and hybrid models are candidate transformations. The selected hybrid heteroscedastic Tobit model is the scoring artifact. The older crosswalk is a comparator with different descriptive-system, source-preference, and method provenance.
- **Methods and comparison:** EQ-VT 2.1 interviews, quality-control flags, cTTO and DCE designs, censoring and heteroscedasticity treatment, hybrid estimation, feedback exclusions, prediction error, leave-one-state-out tests, and comparison of all 3,125 values with the crosswalk.
- **Evaluation and output:** The selected model had ordered, significant coefficients and good single-state prediction. Its values were lower and covered a wider range than the crosswalk. The paper recommends it for Trinidad and Tobago QALY calculations and as a possible regional reference when appropriate.
- **Limits and uncertainty:** Education and some age-sex groups were over-represented. Interviewer protocol and distribution effects remained despite pilot and quality control. The comparison with the crosswalk changes valuation year, protocol, descriptive system, mapping, and source population, so differences cannot be assigned to one cause. Regional use needs evidence of population and decision-context fit.
- **Source issue:** The abstract reports 236 negative states (7.6%), while the Results report 275 negative states (8.8%). Both use 3,125 as the denominator. The supplied paper does not resolve which count is correct.

## 8. EQ-5D-5L Population Norms and Health Inequality for Trinidad and Tobago in 2022–2023 and Comparison with 2012

DOI: `10.1186/s12955-024-02323-1`

- **Contribution and stage:** Completed secondary population-norm, inequality, and temporal-comparison study.
- **Purpose and layer:** Produce 2022–2023 EQ-5D-5L norms, assess demographic and socioeconomic inequality, and compare response and outcome distributions with 2012.
- **Evidence source and lineage:** The 2,989-person sample combines three surveys that were intended to be mutually exclusive: 1,079 EQ-VT respondents from paper 7, 970 retained DCE-with-duration respondents from paper 6 and the round-2 comparison paper, and 940 additional online-panel respondents. It compares these data with a separate 2012 sample of 2,036 adults.
- **Artifact roles and derivation:** EQ-5D-5L and EQ VAS are data generators. Profiles from both periods were scored with the newly published Trinidad and Tobago 5L value set, which holds scoring constant for the index comparison. Age-sex norms, demographic subgroup summaries, ceilings, ordered-logit odds ratios, and modified Kakwani indexes are derived population outcomes.
- **Methods and comparison:** Descriptive norms, Welch tests, dimension distributions, ordered-logit models, inequality decomposition, and a ten-year comparison. The temporal comparison aligns instrument and index scoring, but not recruitment source, mode, survey context, or calendar conditions.
- **Evaluation and output:** The 2022–2023 mean index was 0.921, mean EQ VAS was 79.6, and profile ceiling was 31.5%. These were lower than in 2012. The paper reports a higher EQ VAS inequality index and changed dimension associations. The outputs are updated national norms and inequality evidence, not a causal estimate of pandemic or social change.
- **Limits and uncertainty:** Two component surveys used an online panel; one used household recruitment. Response rates were unavailable for two surveys, incentives differed, and repeat participation across survey sources could not be fully excluded. The 2012 and later collections differed in context and method. Dichotomized socioeconomic variables support historical comparison but hide gradients. The modified Kakwani index, index-value associations, EQ VAS associations, and dimension odds ratios describe different inequality representations and must not be treated as interchangeable.
- **Source issues:** The abstract says that collection ended in May 2023, while the Methods say that survey 3 ran from March through August 2023. The Methods and Table 6 define the income contrast as lowest income versus the reference, but the Discussion says that higher income increased the odds of problems. The direction intended by that sentence is unclear.

## 9. Design and Implementation of Data Quality Controls in the EQ-DAPHNIE Study

DOI: `10.1007/s11136-025-04074-y`

- **Contribution and stage:** Completed methodological and implementation analysis of a UK pilot and completed data collection in 15 countries. It refines a live multi-country data resource.
- **Purpose and layer:** Design, apply, and evaluate survey-quality controls for online population-health data. The direct target is the response dataset and collection workflow, not the psychometric performance of a named health instrument.
- **Evidence source and lineage:** A UK pilot had 3,012 completers. The main collection had 68,411 completers from 15 non-probability online panels, usually about 4,500 per country. This is the same EQ-DAPHNIE program described in the round-1 protocol and resource paper (`10.1007/s11136-025-03983-2`). Paper 10 reuses eight country datasets.
- **Artifact and workflow roles:** The LimeSurvey questionnaire, local language versions, reCAPTCHA, panel-provider controls, repeated questions, response fields, quota dashboards, and exclusion rules are workflow and data-quality artifacts. EQ-5D-5L, EQ VAS, EQ-HWB, and other measures generate data but are not psychometric evaluation targets here.
- **Methods and comparison:** Randomized pilot versions tested mandatory questions, response options, vignettes, and survey burden. The main study used soft launches, quota monitoring, response-time rules, bot and duplicate detection, repeated-item agreement, missingness checks, outlier review, and post-stratification. Countries are compared on recruitment flow, completion, duration, exclusions, missingness, consistency, and quota attainment.
- **Evaluation and output:** The pilot caused material changes to question position, field format, vignette count, mental-health content, and sensitivity guidance. Main-study bot, speeding, and duplicate exclusions were low overall, but completion, missingness, and quota attainment varied materially. The output is a set of tested controls and country-specific data-fitness warnings.
- **Limits and uncertainty:** A quota-matched non-probability panel is not automatically representative. Some quota cells were far from target, internet access and literacy affect coverage, and weighting cannot remove unobserved selection. Bot and speeding thresholds operationalize likely quality risks but do not prove that each excluded response was invalid. The abstract calls link-click percentages of 80.1% to 100% “response rates,” while it separately reports completion of 22.9% to 60.8%; these stages need distinct labels.
- **Metadata issue:** The structured author list includes a malformed concatenated project-team entry and then repeats individual team names. Authorship cannot be used reliably from the supplied YAML without correction.

## 10. Measuring Inequality in Quality of Life: Further Evidence That the EQ-5D-5L May Underestimate It

DOI: `10.1007/s11136-026-04294-w`

- **Contribution and stage:** Completed secondary cross-country association analysis and replication.
- **Purpose and layer:** Test whether EQ VAS differs by education or perceived income among respondents with the same EQ-5D-5L profile. The paper addresses content coverage, reporting heterogeneity, and equity-use implications.
- **Evidence source and lineage:** 32,327 EQ-DAPHNIE respondents aged 25 to 79 from Australia, Canada, France, Germany, the Netherlands, New Zealand, the UK, and the US. The analysis reuses eight country datasets evaluated in paper 9 and described by the earlier EQ-DAPHNIE resource report.
- **Artifact roles and derivation:** Ten selected EQ-5D-5L profiles are conditioning groups. EQ VAS is the analyzed outcome. Harmonized education and subjective income status are socioeconomic stratifiers. Survey weights, full-information maximum likelihood, and profile-specific regression models transform the source responses into adjusted gradients.
- **Methods and comparison:** Separate within-profile regressions compare socioeconomic groups while adjusting for age, sex, and country. Two sufficiently common profiles also support country-specific models. The analysis excludes low BMI values and, by profile, EQ VAS scores below fixed thresholds.
- **Evaluation and output:** Higher education and, more consistently, more comfortable income were associated with higher EQ VAS within most identical profiles. The output is evidence of residual within-profile heterogeneity with implications for equity analysis. It is not direct proof that the descriptive system omits content or that one socioeconomic group uses the VAS incorrectly.
- **Limits and uncertainty:** Content not represented in the five dimensions and socioeconomic response-style differences are competing, non-exclusive explanations that the design cannot distinguish. Perceived income and EQ VAS can share psychological influences. The online, high-income-country sample limits transfer. The author-defined VAS exclusions can remove genuine discordance caused by omitted health content, which is also one of the mechanisms under study. Sensitivity to retaining these responses is not reported in the supplied paper.
- **Source issue:** The Data Availability statement says that no datasets were generated or analyzed, but the Methods and Results describe analysis of 32,327 EQ-DAPHNIE records. These statements conflict.
