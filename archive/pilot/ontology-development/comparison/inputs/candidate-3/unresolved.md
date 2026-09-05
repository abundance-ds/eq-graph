# Unresolved and poorly fitting cases

## EQ-DAPHNIE report status

`10.1007/s11136-025-03983-2` reports completed collection dates and sample counts for the first 15 countries. It also uses protocol language and gives no main instrument or population results. “Design/resource report” is the current answer. A later round can test whether the ontology needs separate terms for a cohort profile, data note, and study protocol.

## Organizational versus individual HTA evidence

`10.1017/s0266462326103602` samples people who work with HTA agencies, but respondents answer as individuals. The paper cannot support formal agency-level practice claims. The current ontology uses “agency-associated respondent” as the evidence unit. It leaves the agency as context, not as the respondent.

## Dyadic recruitment with individual analysis

`10.1007/s11136-025-04003-z` has caregiver and care-recipient dyads, but its focal psychometric analysis uses individual responses. It is not clear whether future applications will need a formal distinction between sampling unit, response unit, and analysis unit. The current application states the difference in text.

## Hybrid empirical and development studies

`10.1007/s11136-019-02115-x` combines label generation, response scaling, cognitive testing, version selection, and cross-language harmonization. It also has a material protocol difference in the UK. One design label would hide this structure. The current ontology permits multiple study components but does not define a formal component hierarchy.

## Value-set representativeness and geographic counts

The China youth value-set paper (`10.1007/s40273-022-01216-9`) uses quotas with non-probability recruitment. Its DCE and cTTO samples have different geographic coverage. In addition, its Key Points say “4 different regions,” while its Methods list 14 provinces or cities across five geographical parts. This conflict is unresolved. Applications must not reduce this evidence to a binary “representative” flag.

## Content-validity boundary

`10.1007/s11136-025-04038-2` evaluates comprehensiveness, not all aspects of content validity. Its code-filter rules exclude external, economic, future, and some objective concepts. The resulting framework supports one defined outcome-measurement view of quality of life. Future papers can show whether “construct boundary decision” needs its own ontology element.

## Interpretation of failed hypotheses

The Brazilian measurement study (`10.1007/s10198-025-01770-x`) warns that disagreement with prespecified construct-validity hypotheses does not directly prove that an instrument has poor validity. The ontology records the hypothesis and result basis, but it does not yet define a standard interpretation rule.

## Review scope versus publication date

The RCT methods review (`10.1016/j.jval.2025.02.001`) combines database searches through 2021 with a registry search in 2023. A single “search end date” would be inaccurate. The current ontology permits source-specific scope notes. The supplied structured record also lacks authors, journal, and publication date. These gaps require deterministic metadata work outside this ontology task.

## Level of method detail

Value-set and statistical-method papers can support a much more detailed ontology of model assumptions and estimands. This round keeps only method features that help compare the papers. More detail could move the ontology toward a claim or software schema before the research use is clear.

# Round 2 additions and updates

## Status of inherited cases

- **Dyadic recruitment with individual analysis:** Addressed in the current ontology through separate recruitment, respondent, analysis, and modeled units. The round 1 application already records the needed distinction.
- **Hybrid empirical and development studies:** Still open. The EQ-TIPS expert consultation (`10.1007/s11136-025-04150-3`) and the two-sample valuation-method comparison (`10.1016/j.jval.2024.05.016`) reinforce the need for multiple components, but they do not justify a fixed component hierarchy.
- **Content-validity boundary:** Still open. The EQ-TIPS paper shows that construct definition, caregiver spillover, development, and health-related quality of life can affect item relevance. The ontology records the boundary but does not prescribe one.
- **Level of method detail:** Still open. The new valuation, mapping, and utility-comparison papers add more possible model details. The current ontology keeps only details that affect comparison, transfer, or a decision.
- **Other inherited cases:** The batch does not resolve EQ-DAPHNIE report status, agency versus individual HTA evidence, interpretation of failed hypotheses, or source-specific review dates.

## National preference perspective in a mobile population

The UAE value-set paper (`10.1016/j.jval.2025.01.003`) includes nationals and expatriates who had lived in the country for at least five years. The authors intend a national decision perspective, but residency, language, citizenship, employment, and future residence can affect preferences. The ontology can record these features, but it does not define when a mobile population constitutes a stable national preference population.

The same article has an unresolved reporting conflict: its abstract gives a mean age of 39 years, while its Results give 32.1 years.

## Agreement versus method interchangeability

The DCE-with-duration study (`10.1016/j.jval.2024.05.016`) finds close agreement after nonlinear time correction. It uses different samples, modes, periods, and extensive DCE-with-duration exclusions in one country. The ontology records agreement and transfer limits. It does not define a general threshold at which two methods become interchangeable.

## Development-stage output

The EQ-TIPS paper (`10.1007/s11136-025-04150-3`) evaluates an experimental version and makes recommendations, but it does not release the revised version. “Completed development stage” plus an **informs** relation is the current treatment. More development papers are needed before separate terms for consultation, candidate version, approved version, and final instrument would help comparison.

The article also reports 44 invited experts, but its three group counts total 43. The source does not explain the difference.

## Language version versus geographic scope

The Arabic EQ-5D-Y-5L paper (`10.1186/s41687-025-00985-z`) produces Modern Standard Arabic for Egypt and suggests possible use in other Arabic-speaking countries. Dialect, schooling, culture, and local cognitive interpretation can differ. The ontology separates language, culture, and country, but it does not specify the evidence that permits transfer of one language version to another country.

## Psychometric benefit versus utility suitability

The bolt-on study (`10.1016/j.jval.2024.03.2195`) shows that added items can reduce ceiling and improve discrimination. It does not test valuation-task feasibility or the comparability of resulting utilities. The ontology now separates incremental measurement value from valuation performance. The evidence needed to connect these two stages remains unresolved.

## Source-to-model dependency detail

The dialysis paper (`10.1007/s10198-018-0987-x`) links observed patient responses, mapped or direct utilities, regression estimates, Markov models, QALYs, and cost-effectiveness ratios. A formal dependency graph could show where assumptions enter, but it would approach the detailed claim-evidence representation excluded by the task. The current application records the main chain in text. Later papers can test whether a small formal component relation is useful.

## Dual substantive and measurement purpose

The inequality paper (`10.3389/fpubh.2021.744405`) both studies education-related health differences and tests a level sum score against EQ VAS. The ontology permits both roles. It remains unclear whether future applications will need to identify one role as primary when a paper gives both equal weight.

## Implementation denominator and perspective

The Ontario oncology pilot (`10.3390/curroncol32060308`) uses the same willingness numerators with different reported percentages in the abstract and Results. The Results use 160 feasibility-questionnaire respondents, but the abstract appears to use the 170 enrolled patients and gives one percentage that does not exactly match that denominator. The intended denominator needs source clarification.

The paper supplies patient experience and some process observations, but it does not provide a full staff, system, equity, or cost perspective. The ontology records the assessed perspective. It does not treat patient acceptability alone as system-level feasibility.

## Compatibility of pooled secondary datasets

The EQ-HWB-S study (`10.1016/j.jval.2024.05.007`) pools two valuation datasets with different collection periods, administration modes, instrument order, long-term-condition definitions, and variable availability. The current ontology records these differences but does not assign a compatibility score. A standard score would imply a judgment that this batch does not support.

# Round 3 additions and updates

## Status of inherited cases

- **EQ-DAPHNIE report status:** Addressed for the current record. The later quality paper (`10.1007/s11136-025-04074-y`) confirms that the earlier paper (`10.1007/s11136-025-03983-2`) described an active resource with completed rounds. “Design/resource report” remains the best status for the earlier paper because it reports no substantive outcome analysis.
- **Source-to-model dependency detail:** Partly addressed. The ontology now records cross-paper reuse, shared samples, and supplied inputs. It does not create a full within-paper claim and assumption graph.
- **Compatibility of pooled secondary datasets:** Still open. The Trinidad and Tobago population-norm paper adds mixed recruitment modes, incentives, and source-study exclusions. The ontology records them but does not calculate a compatibility score.
- **Dual substantive and measurement purpose:** Still open as a primary-role question. The EQ-DAPHNIE inequality paper again supports nonexclusive roles, but it does not show that a mandatory primary role would help research use.
- **Content-validity boundary:** Still open. The EQ-DAPHNIE inequality paper cannot distinguish omitted health content from response-style differences.
- **Agreement versus method interchangeability:** Still open. The anchoring paper (`10.1177/0272989x251325828`) finds population-level agreement with cTTO but uses different respondents.
- **Development-stage output:** Addressed in part. The cTTO-only youth paper reinforces the distinction between a candidate analytic tariff and an official national tariff.
- **Other inherited cases:** Round 3 does not resolve organizational versus individual HTA evidence, the Chinese geographic-count conflict, failed-hypothesis interpretation, source-specific review dates, national perspective in mobile populations, language transfer, or psychometric benefit versus utility suitability.

## Cross-paper sample overlap and independence

The Trinidad and Tobago papers have a dense evidence lineage. The population-norm analysis (`10.1186/s12955-024-02323-1`) includes the national value-set sample and the retained DCE-with-duration sample. The anchoring paper and the earlier DCE comparison also use the latter sample. These are not independent bodies of evidence. The exact participant links are clear at the dataset level.

The population-norm authors intended its three samples to be mutually exclusive, but they state that overlap between the household sample and panel sources remains possible. The exact duplicate risk is unknown.

## Trinidad and Tobago value-set count conflict

The abstract of `10.1186/s12955-024-02266-7` reports 236 negative tariff values, or 7.6%. The Results report 275, or 8.8%. The source does not identify which count is correct. Applications must not select one without clarification.

## Trinidad and Tobago population-norm collection period

The abstract of `10.1186/s12955-024-02323-1` gives a July 2022 to May 2023 collection period. The Methods state that the third survey ran from March through August 2023. This date conflict matters for the claimed period and for interpretation after COVID-19 restrictions. The study also cannot separate temporal health change from changes in mode, recruitment, reporting, and source-study filters.

## Online-panel quality and “response rate”

The EQ-DAPHNIE quality paper (`10.1007/s11136-025-04074-y`) calls the 80.1% to 100% share that clicked the invitation link a response rate in the abstract. The Results separately report link clicks, consent, completion, and noncompletion. Researchers need an explicit denominator before they compare response rates with other surveys.

Quota matching and post-stratification do not establish population representativeness for a non-probability panel. The ontology records coverage and weighting limits, but it does not define a threshold at which a panel supports national norms.

## EQ-DAPHNIE inequality mechanism and exclusion rules

The within-profile gradient in `10.1007/s11136-026-04294-w` can result from health content outside the EQ-5D-5L dimensions, socioeconomic response-style differences on EQ VAS, shared psychological determinants of perceived income and EQ VAS, or a mixture. The cross-sectional design cannot select one mechanism.

The study excludes EQ VAS values below 50 for profile 11111 and below 30 for other selected mild profiles. These rules preserve replication of the parent method, but the claim that the values are incompatible with the profiles is an analyst judgment. The sensitivity of the gradient to other reasonable rules is not reported.

The Data Availability statement says that no datasets were generated or analyzed, while the Methods and Results describe analysis of EQ-DAPHNIE data. This internal reporting conflict needs correction.

## Child-health valuation anchors and transfer

The four-arm study (`10.1016/j.jval.2018.05.002`) shows that wording and adult-versus-child perspective interact. It also changes self valuation to valuation of another person. The cTTO-only youth study (`10.1016/j.jval.2023.03.003`) supports feasibility in one Chinese sample. Together, they do not establish how to compare child and adult QALYs, whether they need different decision thresholds, or how results transfer across countries.

## Monetized disability burden

The vision-impairment study (`10.1038/s41433-023-02860-x`) monetizes DALYs as part of total societal burden. Its sensitivity analysis shows that disability-weight choice changes the well-being-loss estimate about fourfold. The ontology can record the perspective, weight source, and output chain, but it does not prescribe whether a monetized DALY belongs in a cost-of-illness total or which disability weights should govern.
