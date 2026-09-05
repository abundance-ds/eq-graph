# Origin decisions and important changes

Round 1 had no inherited lineage ontology. These decisions created the initial structure.

## Separate contribution role from study design

The same design can serve different research contributions. The EQ-DAPHNIE paper (`10.1007/s11136-025-03983-2`) and the HTA survey (`10.1017/s0266462326103602`) both use cross-sectional online surveys. The first defines a reusable data infrastructure. The second maps professional practice and needs. Therefore, “cross-sectional survey” is a design, not a sufficient paper type.

## Separate study status from evidence origin

The EQ-DAPHNIE report describes a resource after several data-collection rounds, but it does not give substantive analytic results. It fits neither a simple “protocol” nor a normal “completed study” label. The ontology now records status and evidence origin separately.

## Separate the focal entity from the paper's action on it

The same instrument can have different roles. The EQ-5D-Y-5L paper (`10.1007/s11136-019-02115-x`) develops an instrument version. The Brazilian study (`10.1007/s10198-025-01770-x`) evaluates that version. The Chinese qualitative paper (`10.1007/s11136-025-04038-2`) evaluates conceptual coverage of EQ-HWB. A relation such as **develops**, **uses**, or **evaluates** prevents these roles from becoming one ambiguous instrument field.

## Separate data contributor, target of judgment, and intended population

The China EQ-5D-Y-3L valuation study (`10.1007/s40273-022-01216-9`) collects responses from adults who value a hypothetical child's health. The HTA survey collects individual practitioner opinions about professional practice. The child instrument studies collect child self-reports. One “population” element cannot represent these differences.

## Distinguish instrument data products

The RCT review (`10.1016/j.jval.2025.02.001`) shows that dimension responses, EQ VAS, and utilities are analyzed in different ways. The Brazilian measurement study evaluates profiles and VAS but not utility. The ontology now records the analyzed data product instead of treating all EQ-5D data as one outcome.

## Use evaluation families, not one broad psychometrics label

The systematic psychometric review (`10.1007/s11136-020-02688-y`) covers distribution, reliability, validity, and responsiveness. The response-scale study (`10.1007/s11136-025-04003-z`) adds informativity, IRT discrimination, threshold coverage, and differential item functioning. The value-set papers use logical order, fit, anchoring, and prediction error. These criteria support separate evaluation families.

## Make comparisons explicit relations

Most papers compare entities, but the compared entities differ: response-level versions, instruments, scale formats, statistical models, value sets, conceptual frameworks, or regional practices. The ontology represents “compares X with Y on criterion Z” as a reusable pattern. This is more useful than a generic “comparative study” label.

## Record cultural and language scope without making it a paper type

Country and cultural context affect value sets, label harmonization, conceptual coverage, and transfer of evidence. This is clear in the Danish and Chinese value sets, the four-language EQ-5D-Y-5L development study, and the Chinese EQ-HWB content-validity study. Context belongs with target population, perspective, and limitations. It is not a separate contribution class.

## Keep outputs distinct from detailed findings

The ontology records outputs such as a value set, instrument version, conceptual framework, evidence map, and priority list. Applications include only a short decision or result summary. This boundary follows the task instruction not to build a detailed claim-evidence representation.

# Round 2 changes and retention decisions

## Add translation and cultural adaptation as a contribution role

The Modern Standard Arabic EQ-5D-Y-5L paper (`10.1186/s41687-025-00985-z`) does more than test content and less than create a new descriptive system. It produces a language-specific version through forward translation, back translation, cognitive testing, revision, and approval. Translation is now a separate role, with **adapts** as a relation and linguistic equivalence, response-order preservation, and cultural usability as evaluation criteria.

## Add method development or evaluation as a contribution role

The DCE-with-duration paper (`10.1016/j.jval.2024.05.016`) tests whether one valuation method can give results like another. The dialysis paper (`10.1007/s10198-018-0987-x`) tests how mapping and instrument choice affect modeled QALYs and cost-effectiveness ratios. These are method evaluations. They are not value-set development and do not only describe current analysis practice. The new role keeps this distinction.

## Add substantive outcome analysis without making the instrument the study topic

The inequality paper (`10.3389/fpubh.2021.744405`) uses EQ-5D results to study a population-health question as well as to compare outcome formats. The dialysis paper also estimates economic outcomes. The ontology now permits a health, care, economic, or policy outcome role. This prevents every paper that uses EQ-5D from being labeled as an instrument study.

## Add implementation feasibility and acceptability

The Ontario oncology pilot (`10.3390/curroncol32060308`) tests routine data collection within a treatment workflow. Completion, willingness, timing, mode, accessibility, patient experience, and coordinator burden are not standard psychometric properties. The ontology now has an implementation role, an **implements** relation, and a separate evaluation family.

## Make study components and source roles explicit

Several round 2 papers connect components that have different units and evidence origins. The DCE-with-duration comparison (`10.1016/j.jval.2024.05.016`) uses two samples and administration modes. The dialysis analysis (`10.1007/s10198-018-0987-x`) sends patient utilities into two Markov models. The EQ-HWB-S analysis (`10.1016/j.jval.2024.05.007`) pools two datasets with different periods, definitions, and available variables. The ontology now asks for component designs, links between components, and dataset-compatibility limits.

## Distinguish recruitment, respondent, analysis, and modeled units

The dialysis study starts with individual patients but makes its final comparison in model scenarios and hypothetical cohorts. This evidence supports a formal distinction between recruitment or sampling unit, respondent, analysis unit, and modeled unit. It also resolves the round 1 question raised by the caregiver and care-recipient dyads in `10.1007/s11136-025-04003-z`. That application already states that recruitment is dyadic and analysis is individual, so no rewrite is necessary.

## Extend the data-product chain

The dialysis paper (`10.1007/s10198-018-0987-x`) shows a chain from administered questionnaires to mapped or direct utilities, QALYs, and cost-effectiveness ratios. The inequality paper (`10.3389/fpubh.2021.744405`) uses a level sum score rather than a utility. The EQ-HWB-S paper (`10.1016/j.jval.2024.05.007`) compares utilities produced by different scoring routes. The ontology now asks which instrument component is administered, how the score is derived, and how a downstream analysis uses it.

## Add incremental measurement value

The nine-bolt-on paper (`10.1016/j.jval.2024.03.2195`) tests the benefit of adding items to a base instrument. Ceiling reduction, extra construct coverage, discrimination, explanatory power, and respondent or valuation burden form a useful comparison family. This family is separate from the validity of an item in isolation.

## Retain overlapping contribution roles

Round 2 confirms that one exclusive paper type would lose information. The EQ-TIPS consultation (`10.1007/s11136-025-04150-3`) is both an instrument-development stage and a content-validity evaluation. The inequality paper (`10.3389/fpubh.2021.744405`) is both a substantive outcome analysis and a measure comparison. Roles remain nonexclusive.

## Retain action relations and distinct instrument data products

The new papers reinforce both round 1 decisions. The Arabic paper **adapts** an instrument, while the Graves' disease and bolt-on papers **evaluate** instruments. The inequality paper uses a level sum score, the EQ-HWB-S paper uses utilities, and the oncology pilot studies profile collection. A focal-entity list without an action or data-product distinction would merge these different uses.

## Retain the boundary between reusable output and detailed findings

Round 2 adds value sets, translated versions, method recommendations, modeled decision impacts, population-outcome profiles, and implementation recommendations. The applications record the product and a short decision summary. They do not encode each coefficient, correlation, subgroup result, or interview quotation.

# Round 3 changes and retention decisions

## Add evidence lineage and dependence

“Primary” and “secondary” evidence do not show whether papers use the same people or pass outputs between analyses. Round 3 contains several direct links. The cancer-equity paper (`10.3390/curroncol32110645`) reuses the oncology implementation cohort from `10.3390/curroncol32060308`. The cTTO-only youth analysis (`10.1016/j.jval.2023.03.003`) reuses part of the Chinese valuation study in `10.1007/s40273-022-01216-9`. The Trinidad and Tobago value-set, DCE, anchoring, and population-norm papers share samples, tariffs, and comparators. The EQ-DAPHNIE quality paper extends the design report, and the inequality paper reuses the resulting data.

The ontology now records source datasets, shared or possibly overlapping respondents, supplied inputs, replication, and extension. This supports meta-research on nonindependent evidence without creating a detailed claim graph.

## Add data integrity and sample quality as an evaluation family

The EQ-DAPHNIE quality paper (`10.1007/s11136-025-04074-y`) evaluates bots, duplicates, speeding, dropout, missing data, outliers, repeated-item consistency, quota achievement, coverage, and weighting limits. These are not psychometric properties of an instrument. They are also more specific than general implementation feasibility. The new evaluation family keeps the survey process and the health measure separate.

## Extend the procedure and data-product chain

The vision-impairment paper (`10.1038/s41433-023-02860-x`) connects individual use and cost reports, prevalence, disability weights, direct and indirect costs, DALYs, and a monetized well-being loss. The population-norm paper (`10.1186/s12955-024-02323-1`) connects profiles, a national tariff, utilities, EQ VAS, ceilings, norms, and inequality indices. The ontology now lists these products explicitly. It still records only the main dependency chain, not each estimate.

## Extend conceptual coverage to residual and reporting differences

The EQ-DAPHNIE inequality paper (`10.1007/s11136-026-04294-w`) compares EQ VAS among people with the same EQ-5D-5L profile. The result can reflect omitted health content, socioeconomic reporting heterogeneity, or both. The conceptual-coverage family now permits within-profile residual differences and possible reporting heterogeneity. It does not force one mechanism when the design cannot distinguish them.

## Retain overlapping contribution roles

Round 3 again rejects one exclusive paper type. The EQ-DAPHNIE inequality paper is both a substantive inequality analysis and a conceptual or measurement evaluation. The cTTO-only youth paper is both a method evaluation and a candidate value-set analysis. The EQ-DAPHNIE quality paper develops infrastructure and evaluates survey methods. Roles remain nonexclusive.

## Retain health, economic, or policy outcome analysis as a broad role

The vision-impairment cost study does not administer EQ-5D and is not an instrument study. Its direct costs, productivity loss, DALYs, and policy implications fit the existing outcome role. A separate cost-of-illness contribution role would add little for this corpus, so no new role was added.

## Retain the distinction between candidate, official, and reused outputs

The cTTO-only youth analysis (`10.1016/j.jval.2023.03.003`) supports a candidate method and model. It does not replace the official Chinese hybrid tariff. The Trinidad and Tobago valuation study (`10.1186/s12955-024-02266-7`) selects a national tariff, which later papers reuse as a benchmark and scoring input. Output maturity and evidence lineage now show these differences.

## Retain descriptive treatment of representativeness

Round 3 includes household sampling, quota samples, public-place recruitment, and non-probability online panels. Several papers use “representative” after quota matching, although coverage and response propensity remain unknown. The ontology continues to record the sampling basis, achieved composition, weighting, and shortfall instead of a yes-or-no representativeness property.
