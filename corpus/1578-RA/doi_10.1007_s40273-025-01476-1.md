---
project_id: "1578-RA"
work_id: "doi:10.1007/s40273-025-01476-1"
doi: "10.1007/s40273-025-01476-1"
pmid: "39960567"
pmcid: "PMC12011929"
title: "A Taxonomy for Assessing Whether HRQoL Value Sets Are Obsolete"
journal: "Pharmacoeconomics"
publication_date: "2025-02-17"
volume: "43"
issue: "5"
authors:
  - name: "Richard Norman"
    orcid: "http://orcid.org/0000-0002-3112-3893"
    affiliation_ids:
      - "Aff1"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff2"
  - name: "Marcel Jonker"
    affiliation_ids:
      - "Aff3"
  - name: "Elly Stolk"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Saskia Knies"
    affiliation_ids:
      - "Aff3"
      - "Aff4"
  - name: "Raoh-Fang Pwu"
    affiliation_ids:
      - "Aff5"
  - name: "Ciaran O’Neill"
    affiliation_ids:
      - "Aff6"
  - name: "Kirsten Howard"
    affiliation_ids:
      - "Aff7"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "Aff8"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/02n415q13grid.1032.00000 0004 0375 4078School of Population Health, Curtin University, Perth, Australia"
  - id: "Aff2"
    name: "https://ror.org/01mrvqn21grid.478988.20000 0004 5906 3508EuroQol Research Foundation, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "https://ror.org/057w15z03grid.6906.90000 0000 9262 1349Erasmus School of Health Policy and Management, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "https://ror.org/000kng648grid.511999.cZorginstituut Nederland, Diemen, The Netherlands"
  - id: "Aff5"
    name: "https://ror.org/04je98850grid.256105.50000 0004 1937 1063Data Science Center, Fu Jen Catholic University, New Taipei City, Taiwan"
  - id: "Aff6"
    name: "https://ror.org/00hswnk62grid.4777.30000 0004 0374 7521School of Medicine, Dentistry and Biomedical Sciences, Queen’s University Belfast, Belfast, Northern Ireland UK"
  - id: "Aff7"
    name: "https://ror.org/0384j8v12grid.1013.30000 0004 1936 834XMenzies Centre for Health Policy and Economics, Faculty of Medicine and Health, University of Sydney, Sydney, Australia"
  - id: "Aff8"
    name: "https://ror.org/01ej9dk98grid.1008.90000 0001 2179 088XMelbourne School of Population and Global Health, University of Melbourne, Parkville, Australia"
licence: "cc-by-nc"
source_file: "input/projects/1578-RA/papers/doi_10.1007_s40273-025-01476-1.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12011929/fullTextXML"
source_method: "epmc_xml"
source_sha256: "7b2a9d7cea906a48eaabb3cc82974ae51cc8dd0f357d575cc7a8a802ff58ce7f"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# A Taxonomy for Assessing Whether HRQoL Value Sets Are Obsolete

## Abstract

Providing health-related quality of life (HRQoL) value sets to enable estimation of quality adjusted life years (QALYs) is important in facilitating economic evaluation and in supporting reliable decision-making about healthcare. However, as the field matures, many value sets across a range of HRQoL instruments are now old, based on potentially outdated valuation methodologies and preference data from samples that no longer represent the contemporary population. Having a clear strategy for identification and mitigation of obsolescence is important to ensure policy makers retain confidence in their country-specific value sets. In this Current Opinion, we develop a taxonomy of value set obsolescence. We then explore how the different types of obsolescence might be identified and how methodologists might work with local policymakers to address obsolescence and therefore ensure HRQoL instruments remain relevant for use. The taxonomy of obsolescence consists of four main areas: (1) the value set no longer aligns with current normative health technology assessment (HTA) requirements; (2) the methods used to generate it are no longer considered robust or adequately close to best practice; (3) the population composition has moved too far from the characteristics of the sample in which the original value set was derived; and (4) even after controlling for population differences, preferences are likely to have changed since the original data collection. Through identification of the type of obsolescence that applies in a particular setting, we then suggest a range of possible solutions to each, ranging from recommending particular sensitivity analyses, through reweighting of existing data to better account for population differences, to collecting new data for an updated value set. Obsolescence of existing value sets is driven by more than just time since data collection is often a matter of judgment rather than based on a clear definition. The taxonomy presented here provides a tool for assessing whether value sets are obsolete and what the appropriate response to this obsolescence should be. Working closely with local policymakers and involving discussions regarding the ongoing appropriateness of existing value sets should form an important part of future activities. This should include the consideration of updating value sets in contemporary populations using current best-practice methods. However, the benefits of updating value sets have to be balanced against the cost of doing so, including the challenges faced by policymakers when new values sets require a transition to new local decision-making processes.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| Over time, our value sets for valuing health have the potential to become obsolete, and we do not yet have clear guidance about how to address this growing issue. |
| To help policymakers and analysts explore the issue in their context, we provide a taxonomy of obsolescence for value sets and describe possible approaches for risk mitigation. |
| The development of new value sets can reflect improved methods and/or contemporary data in a sample that aligns more closely with the current population; however, the decision to update value sets has to be balanced against a range of practical concerns around cost and acceptability. |

</div>

## Introduction

Value sets for health-related quality of life (HRQoL) instruments are widely used to support decisions about health and healthcare in a range of settings and applications. This use is based on the premise that improving health is a core function of the healthcare sector and that HRQoL is a central component of this. These applications can be divided into two broad categories. First, value sets are used in “quality weighting” life years in the calculation of quality-adjusted life years (QALYs) in cost utility analyses (CUA) of healthcare interventions. This evidence is widely used to inform health technology assessment (HTA) and other decisions concerning healthcare resource allocation \[1\]. Second, value sets are also used as a convenient means of summarizing the profile data generated from HRQoL instruments \[such as European Quality of Life-5 Dimensions (EQ-5D) or Short-Form-6 Dimensions (SF-6D)\] into a single number, for ease of statistical analysis. For example, values have been used by healthcare systems \[e.g., the English National Health Service (NHS)\] to summarize EQ-5D data collected as part of routine outcomes measurement (PROMs) to evaluate treatment effectiveness and assess provider performance \[2\]. The use of value sets in “QALY” and “non-QALY” applications may have different implications for the properties required of value sets \[3\].

The development of HRQoL values for QALY estimation has a tradition dating back half a century \[4, 5\]. Country-specific value sets for instruments became increasingly common since 1997, with the publication of the seminal Measurement and Valuation of Health study \[6\] reporting the first UK value set for the EQ-5D-3L and building on preceding work using tools such as the Rosser index \[7\]; thus, there are value sets that are approaching 30 years old. Indicating the chronological pattern of value set availability, we identified all value sets for key generic preference-weighted instruments EQ-5D-3L, EQ-5D-5L, EQ-5D-Y, SF-6D, Health Utilities Index (HUI), 15-D, and Assessment of Quality of Life (AQoL)\] using the relevant instrument websites and/or other desktop review methods. These are plotted in Fig. <a href="#Fig1" data-ref-type="fig">1</a> and illustrate some of the context behind this current paper. There is clear growth in valuation studies over time, driven largely by the development of value sets to accompany new instruments such as the EQ-5D-5L \[8\] and the EQ-5D-Y-3L \[9\], but it is notable that the number of older studies is large. These older value sets are often still widely used and cited in literature.

<figure id="Fig1">
<p><img src="40273_2025_1476_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Publication of value sets, by year</figcaption>
</figure>

While there are instances of value sets being updated and replacing initial value sets (e.g., the EQ-5D-3L in Slovenia \[10\] or the EQ-5D-3L in China \[11\]), most of these older value sets have not been updated. Where multiple value sets do exist, as is the case in China for the EQ-5D-3L \[11–13\], they tend to coexist with limited guidance for users about their use. This gives rise to the question about the extent to which these older value sets still offer adequate input for decision-making. Value sets may become outdated for various reasons and, at a certain point, deemed obsolete, i.e., not be useable for their original intended purpose. To date, this issue has not been explicitly addressed by stakeholders (including instrument developers, researchers, policymakers, and patients), and this represents an important gap in literature, increasingly so, as time and methods progress.

The aims of this paper are to (a) discuss key issues in the definition of obsolescence in value sets, (n) provide a taxonomy of the various factors that contribute to a given value set being deemed obsolete, (c) consider the criteria (and related evidence requirements), which instrument developers (or users of value sets) could use, to judge value set obsolescence and to identify the need for updated value sets, and (d) highlight implications of a decision to update/replace a value set, such as transitional issues for value set users and decision-makers in switching between value sets with different properties.

The following paper considers these issues using examples drawn predominantly from EQ-5D value sets. The key reason for this is that there are more country-specific value sets for EQ-5D instruments than for any other HRQoL instrument. However, the issues discussed in this paper are equally relevant to other HRQoL instruments accompanied by preference weights.

## Challenges in Defining Obsolescence in Value Sets

It is important to note that it is challenging to define value set obsolescence, to determine who is responsible for making such a decision, and to explore the appropriate course of action resulting from a value set meeting obsolescence criteria. On the first of these, to date, value set obsolescence has neither been defined nor have the criteria used to identify it been explicitly identified. Therefore, the field exists with this uncertainty and the identification of value set obsolescence has been open to interpretation and ad hoc judgement \[14–16\].

We take, as our starting point, that obsolescence is linked to the question of whether or not a value set is considered valid in a contemporary setting. There is rarely an external gold standard which can be used to judge the validity of a value set, and there is no agreed definition of what “validity” means in the context of HRQoL values. It can be argued that it is almost impossible to validate HRQoL values in the way we can validate stated preferences in other applications and sectors. There are few opportunities to observe real choices people make about HRQoL, so we lack the kind of revealed preferences data that would allow us to check that values are meaningful representations of the preferences embodied in decisions \[17\].

However, we do need to advance a working definition for this work to proceed. For the purposes of this paper, we tentatively propose the following definition of HRQoL value set validity:

> HRQoL value set validity concerns the extent to which any given set of values for an HRQoL descriptive system (a) are a sufficiently good representation of the average preferences of the population of interest and (b) have empirical and theoretical properties which are acceptable in the decision-making context.

The definition touches on two things. First, it considers whether the values sufficiently reflect the average preferences of the members of a given society or some subset of it deemed to be relevant on normative grounds. For example, in the National Institute for Health and Care Excellence (NICE) methods guide, it is noted that values for adult HRQoL should be obtained from adult members of the general public \[18\]. Regarding the term “sufficiently good representation,” we suggest that such a definition cannot be easily made more precise, partly because we do not know how precise is precise enough, and we do not know who is responsible for making such a determination. The second part of the definition of validity concerns whether the characteristics of the values are a good match with any stated requirements of decision-makers and have empirical characteristics with desired properties. This includes the basic requirement, for use in QALY estimation, that values be anchored at 0 and 1 (but can lie below 0 if health states are considered to be worse than being dead) and should have interval scale properties. For example, NICE’s methods guide notes that values should be “choice-based” (indicating a requirement around methods) \[18\]. Value sets which meet such decision-maker requirements might be considered to have “context validity” \[19\]. Every aspect of the research process employed to produce value sets may give rise to considerations regarding appropriateness, acceptability, and whether the resulting values are “fit for purpose,” i.e., choice of sample frame, methods used to elicit stated preference, quality assurance processes applied during or after data collection, modeling approaches, the selection of a “best” model, etc.

Using this working definition of the validity of HRQoL values, in the following section we identify factors which arguably *compromise* validity and which might lead to value set obsolescence.

## A Taxonomy of Factors That Affect Value Set Obsolescence

### Type 1 Obsolescence—The Value Set Is Misaligned with Normative Views

We believe that a value set is obsolete in a particular context if the decision-making body advocates for or moves toward a different normative basis for deriving value sets. For example, given the increasing focus on HTA incorporating patients’ perspectives, there may be a shift toward seeking patients’ values for HRQoL \[20\]. Similarly, in the valuation of child health, there is increasing interest from stakeholders (e.g., in the USA, UK, and elsewhere) in HRQoL values reflecting children’s own views about their health \[21–23\]. In both cases, value sets based exclusively on the stated preferences of the adult general public may become less relevant as the sole basis for generating evidence; this would typically trigger further valuation work to develop results using the preferred normative approach. On a related point, it may be that this kind of obsolescence can apply to certain kinds of analysis within the same jurisdiction. For example, value sets obtained from general population preferences may align well with what decision-making bodies need but might be less relevant and appropriate as a means of summarizing patient data in the context of PROMs programs (e.g., where the goal is to measure the performance of procedures or providers in improving patient health).

Similarly, we argue that a value set becomes obsolete if the relevant decision-making body moves away from the use of a particular HRQoL instrument to support decision-making. If a value set is for an instrument that is no longer recommended by a particular governmental body, then the value set is itself, in a sense, obsolete for that purpose but would not require a further valuation survey (but might cause the need to begin valuation of health states described using other replacement HRQoL instruments).

In an extreme case, the decision-making body might move away from the QALY metric as a central part of their processes—the recent proposal to ban use of QALYs by the US Federal Government, for example \[24\]. Such a move could require a complete reconsideration of how HRQoL is integrated into the decision-making process. This would depend on the selected alternative; for example, the generalized risk-adjusted cost-effectiveness (GRACE) approach \[25\] continues to require assessments of HRQoL. However, if the alternative paradigm did not use such measures, then the value set would be obsolete, but this obsolescence would not trigger the need for a new valuation project.

### Type 2 Obsolescence—Methods Used Have Become Outdated and/or Unreliable

A wide range of changes in valuation methods have occurred in recent years, including the type of stated preference tasks \[26\], mode of task administration, quality control processes \[27\], data analysis, and modeling methods \[28\]. These changes arise for a variety of reasons. Some arise as pragmatic responses to circumstances, such as the shift to online interviews as a result of the pandemic \[29–31\]. Others arise from changes in underlying theoretical emphasis, such as recent discussions over the role of time preference in trade-offs between the quality and duration of life, leading to interest in nonlinear discrete choice experiment (DCE) methods \[32\]. Such changes can be broken down into those supported by strong scientific evidence around methods superiority and those that represent a change in approach *preferred* by methodologists (e.g., because they prefer one kind of underlying theory to another for instance, such as random utility theory versus utility under uncertainty) \[33\], although the dichotomy will often be much less clear, with changes reflecting elements of both.

If original data analysis can be updated to, for example, run a different model or exclude data no longer considered reliable, then analysis can simply be re-run. Hence, the value set might be obsolete but amenable to updating, thus not necessitating new valuation data to be collected.

However, if the original data analysis that generated the value set cannot be updated, then it may be worth exploring whether the magnitude of the effect can be estimated and therefore inform a decision of whether or not to rely on the older value set or to conduct new valuation work. One option here would be to run a small methodological study using previous and new methods to quantify the difference. If it is demonstrated to exist and to be of an adequately large size to matter (however that might be defined), then that would then potentially be a trigger to conduct a larger valuation study using updated methods.

### Type 3 Obsolescence—Populations Have Changed since the Original Valuation Work

Over time, populations may change both in terms of their demographic composition (type 3a) and their preferences (type 3b). With respect to 3a, even if the average preferences of any one sub-group of society (e.g., defined by age, culture, or any other factor(s)) remain unchanged through time, a change in the composition of the population (e.g., arising through an ageing population or through patterns of immigration) could change the overall average “societal” preferences. Recent data from Jonker \[14\] suggested that the effect of changing population composition is modest, but this conclusion may not generalize to specific shifts in population composition or over much longer periods of time. With respect to 3b, changes in health-state preferences might plausibly arise through time as a result of changing societal expectations about HRQoL, i.e., greater awareness of types of health problems (e.g., mental health), and as a result of relevant issues being debated at a societal level (e.g., experiences relating to the coronavirus disease-2019 (COVID-19) pandemic, euthanasia \[34\], end-of-life care, or abortion).

The kinds of changes in 3a and 3b might be addressed in quite different ways, with the latter relatively more likely to trigger new valuation data collection. Regarding population compositional change (type 3a), existing data can, in principle, be reweighted to explore the magnitude of the effect and to potentially develop an updated value set. However, this is dependent on there being adequate data for growing population sub-groups in the original dataset, which may not be the case for situations such as growth in immigration from countries from which people did not previously emigrate in large numbers.

Regarding preference change independent of population composition (type 3b), it may be that preferences can be monitored using a standard, low-cost survey, which can, if results indicate a change, trigger a larger valuation study. If underlying preferences have changed, then that represents evidence that the original value set has moved toward obsolescence. However, it is also important to ensure that any change has restabilized around new norms, potentially through a series of low-cost surveys. Further, a challenge here is that small quantitative studies are likely to only be able to detect very large changes in preferences; one possibility is to use results from this kind of small quantitative study as a prior in an expected value of perfect information (EVPI)-type framework to judge the value of a larger valuation study.

### Type 4 Obsolescence—The Instrument Has Changed and Now the Value Set Is Not an Exact Match for the Descriptive System

The development of value sets to accompany existing instruments occurs after considerable instrument development and refinement. While instrument developers will tend to finalize an instrument before valuation commences, it may be that evidence accrues around the appropriateness of the instrument subsequent to valuation work being disseminated. For example, it may be that the severity of levels is different between countries owing to the challenge of translation. If any such issues prompt the developer to update the instrument, then it may be that any valuation work done on the outdated version of the instrument is similarly obsolete. The question to be addressed is whether the change in wording is likely to produce different values if the same valuation study were conducted using updated wording.

## What Evidence Is Needed to Test for Each Type of Obsolescence and What Solutions Are Suggested?

Table <a href="#Tab1" data-ref-type="table">1</a> summarizes the evidence required to test for each type of obsolescence and the likely solution if obsolescence is identified. These findings are not intended to be definitive, as every case of obsolescence is likely to need a tailored solution reflecting local conditions.

<div id="Tab1" class="table-wrap">

<div class="caption">

What evidence is needed on each type of redundancy, and what actions are possible in each case?

</div>

| A. Redundancy type | B. What evidence would be required to test for redundancy? | C. What solutions are possible if there is evidence of redundancy? |
|----|----|----|
| 1\. The value set no longer aligns with current normative HTA requirements | None as it is driven by the underlying methodological guidelines of the HTA body | Development of new value set better aligned with guidelines |
| 2\. Methods used have become outdated and/or unreliable | Evidence that the value set is likely to change due to changing methods | If data can be re-analysed using contemporary methods, this is optimal. If not, retain current value set if changes are shown to be modest. Or, if not, development of new value set using gold standard methodology |
| 3a. Change in average preferences, due to changes in population composition | Resampling of original data to explore whether there is a significant change in mean preferences | Assuming the appropriate population characteristic data was collected, and there are enough respondents to do so, reweighting of existing responses to better account for new population composition |
| 3b. Change in average preferences, due to changes in society’s preferences | Indication of changing attitudes, such as qualitative work, or small quantitative work exploring preferences | Development of new value set using gold standard methodology, and contemporary sample |
| 4\. The instrument has changed and now the value sets is not an exact match for the descriptive system | Small valuation study using original and updated wording | Development of new value set using updated wording |

</div>

We believe that the sub-categories of obsolescence require quite different methods for identification and, additionally, different responses if obsolescence is identified. For instance, identification of obsolescence can happen without any additional work (e.g., for type 1 obsolescence) but can also require re-analysis of existing data and/or small quantitative or qualitative data collection to establish obsolescence. Subsequent to obsolescence identification, the solution typically requires either re-analysis of existing data (types 2 and 3a) or de novo data collection (types 1, 3b, 4). The role of re-analysis of existing data depends on the accessibility of data used for the original valuation study, which is currently variable.

It is important to note that the solution may not always require new data collection. It may be possible to re-analyze existing data in new ways (as is the case in type 3a obsolescence), use improved modeling methods (as may be the case in type 2 obsolescence), impose higher standards of quality control ex post by excluding data, or to re-weight data to address changes in the composition of the population.

However, in some cases it will be necessary to undertake a new value set study to replace the obsolete one. Given the cost (both financial and in the broader sense described in Sect. <a href="#Sec9" data-ref-type="sec">5</a>) of undertaking such studies, there should be clear evidence based on agreed criteria that these efforts are warranted. Further—as we discuss in the next section—new value sets are not only costly to produce but also, perhaps more importantly, impose broader societal costs in terms of adoption, which need to be taken into account when deciding to denote a value set as obsolete.

## The Cost of Transitions to New Value Sets and Implications for Judging Obsolescence

For type 1 obsolescence, the case for value set obsolescence is normally clear. However, for types 2 and 3 obsolescence, there is a balance between the advantage of a more contemporary value set using current gold standard methods and the acceptability of their update by decision-makers. Updating value sets has the advantage of better reflecting the values of the community in which decisions are being made (either by administration in a more contemporary sample or in using methods which we as a field believe to be more rigorous than what was the gold standard previously). However, this updating process comes at a cost. First, deriving value sets is expensive and draws resources away from other research. This argument may benefit from the development of an expected value of perfect information (EVPI)-type framework \[35\], and it should also be noted that the cost of resource misallocation based on obsolete HRQoL values can be significant. This is similar to an existing discussion in literature around identifying appropriate values for other input parameters \[36–38\].

Second, having a new value set requires good stakeholder engagement to ensure there is comfort with switching to it as a substitute for the incumbent value set \[39\]. Change has to be well justified given the potential for gaming in HTA where multiple competing value sets are available; it may be that the commissioning of new value sets has to operate in tandem with the process of actively decommissioning older value sets. However, given we are operating in an environment without external validation of values, can we unequivocally say the older value set is inferior and hence should be decommissioned? For type 1 obsolescence, this is easier, but our expectation is that types 2 and 3 obsolescence will be more common and will eventually apply to all value sets.

A further point is how HTA processes should use new value sets. A new value set will potentially change how quality of life and length of life are valued against one another, as well as the relative importance of different aspects of quality of life. Such changes will generally be considered to provide a more robust estimate of contemporary societal views on health. However, to the extent that the characteristics of the value sets differ, estimates of incremental QALY gains \[and hence also incremental cost-effectiveness ratios (ICERs)\] estimated under different value sets may also differ, ceteris paribus. This may affect the comparability of QALYs and ICERs produced using the new value set with historical evidence produced using older value sets—and comparability against cost-effectiveness thresholds. This raises a number of questions. If an obsolete value set is replaced, should that change how decision-makers assess ICERs presented in HTA? How should decision-makers address any inconsistencies between the QALY estimates compared with those from older value sets? For example, is this best achieved through HTA bodies recommending use of new value sets but requesting sensitivity analyses using older, previously recommended value sets? To our knowledge, there is currently no clear guidance on this provided by any HTA body, but there is good evidence suggesting it requires consideration given the potential for value set selection to affect results \[40\].

If a new value set replaces a previous one, does that then cause a problem in terms of the need to reappraise historical decisions? If we assume that a new value set is in some sense correct and the older one is not, and that switching between value sets moves interventions across some cost-effectiveness threshold, should decision-makers then reverse decisions in light of new evidence? It is highly unlikely that positive recommendations would be reversed if the value set were to change the implied ICER; in an expected value of information context, Eckermann and Willan describe a situation where the cost of reversing a decision is high enough to mean that the decision to adopt becomes irreversible \[41\]. We would argue that this applies here, with costs defined broadly in terms of reputational risk. Conversely, our view is that it is certainly plausible that sponsors would ask for reconsideration of evidence if previously rejected interventions become more cost-effective when a new value set is applied to the data that they previously presented. This asymmetry poses a problem by recommending interventions with poor cost-effectiveness data.

## Conclusions

In this paper, we have tentatively identified an emerging problem for developers of HRQoL instruments with accompanying value sets. As time and methods advance, the bedrock of applied valuation research naturally becomes increasingly unreliable, and, as a field, we need to consider how to approach this challenge. Here, we have presented a framework for describing and addressing value set obsolescence but have left questions unanswered. Some questions, such as those about how large of a difference in expected values warrants new valuation work, we believe are best addressed on a case-by-case basis and, at worst, may be unanswerable as we do not know how big of a difference is “too big to ignore.” However, some other questions, such as the value of adjusting existing data for different population composition and the best way to engage with decision-makers around this issue, are fruitful avenues for ongoing research and something we would be keen to see taken on by the field more generally to help keep our value sets fit for purpose and reflective of broader societal views. We have not reached consensus on who is responsible for monitoring and declaring whether an existing value set is obsolete. This may be the instrument developer, the end-user of the instrument and value set, or some combination of the two. Further, it may be that the solution to this question differs across jurisdictions.

### Acknowledgements

We thank members of the EuroQol group for feedback on a draft of this paper at the 2024 EuroQol Plenary Meeting. In particular, we acknowledge Edward Webb who provided valuable comments as a discussant of the work.

### Declarations

#### Funding

Open Access funding enabled and organized by CAUL and its Member Institutions. Work on this paper was supported by EuroQol Research Foundation grant EQ 1578-RA. Views expressed in this paper are those of the authors and are not necessarily those of the EuroQol Research Foundation or their employer.

#### Conflict of interest

R.N., B.R., E.S., M.J., and N.D. are members of the EuroQol Group. Elly Stolk and Ciaran O’Neill are Editorial Board Members of PharmacoEconomics. Neither was involved in the selection of peer reviewers for the manuscript, nor in any of the subsequent editorial decisions.

#### Author contributions

R.N. and N.D. conceptualized the work. All authors contributed to the development of the taxonomy, drafting of the manuscript, and approving the submitted version.

## References

1. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, Busschbach J, Boye KS. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020. 10.1007/s10198-020-01195-8.32514643 10.1007/s10198-020-01195-8PMC7561556

2. Appleby J, Devlin N, Parkin D. Using patient reported outcomes to improve health care. Wiley-Blackwell; ISBN: 978-1-118-94860-6. 2016

3. Devlin N, Finch A, Parkin D. Guidance to users of EQ-5D-5L value sets. In: Value sets for EQ-5D-5L: a compendium, comparative review & user guide [Internet], Chapter 5. Cham: Springer; 2022.

4. Spencer A, Rivero-Arias O, Wong R, Tsuchiya A, Bleichrodt H, Edwards RT, Norman R, Lloyd A, Clarke P. The QALY at 50: one story many voices. Soc Sci Med. 2022. 10.1016/j.socscimed.2021.114653.35184921 10.1016/j.socscimed.2021.114653

5. Torrance GW, Thomas WH, Sackett DL. A utility maximization model for evaluation of health care programs. Health Serv Res. 1972;7(2):118–33.5044699 PMC1067402

6. Dolan P. Modeling valuations for EuroQol health states. Med Care. 1997. 10.1097/00005650-199711000-00002.9366889 10.1097/00005650-199711000-00002

7. Rosser R, Kind P. A scale of valuations of states of illness: is there a social consensus? Int J Epidemiol. 1978. 10.1093/ije/7.4.347.744673 10.1093/ije/7.4.347

8. Devlin N, Roudijk B, Ludwig K. Value sets for EQ-5D-5L: a compendium, comparative review and user guide. Berlin: Springer; 2022.36810025

9. Ramos-Goñi JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, Devlin N. International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020. 10.1007/s40273-020-00909-3.32297224 10.1007/s40273-020-00909-3

10. Prevolnik Rupel V, Ogorevc M. EQ-5D-5L value set for Slovenia. Pharmacoeconomics. 2023. 10.1007/s40273-023-01280-9.37341959 10.1007/s40273-023-01280-9PMC10570207

11. Zhou L, Xu L, Ye J, Sun S, Zhang Y, Burstrom K, Chen J. Time trade-off value set for EQ-5D-3L based on a nationally representative Chinese population survey. Value Health. 2018. 10.1016/j.jval.2018.04.1370.10.1016/j.jval.2018.04.137030442281

12. Liu GG, Guan H, Jin X, Zhang H, Vorthems SA, Wu H. Rural population’s preferences matter: a value set for the EQ-5D-3L health states for China’s rural population. Health Qual Life Outcomes. 2022. 10.1186/s12955-022-01917-x.35093084 10.1186/s12955-022-01917-xPMC8800217

13. Yang Z, Jiang J, Wang P, Jin X, Wu J, Fang Y, Feng D, Xi X, Li S, Jing M, Zheng B, Huang W, Luo N. Estimating an EQ-5D-Y-3L value set for China. Pharmacoeconomics. 2022. 10.1007/s40273-022-01216-9.36396878 10.1007/s40273-022-01216-9PMC9758244

14. Jonker MF. The impact of demographic change on value set validity and obsolescence. Qual Life Res. 2024. 10.1007/s11136-024-03770-5.39269579 10.1007/s11136-024-03770-5PMC11541319

15. Pickard AS. Is it time to update societal value sets for preference-based measures of health? Pharmacoeconomics. 2015. 10.1007/s40273-015-0253-3.25586758 10.1007/s40273-015-0253-3

16. Law EH, Pickard AS, Walton SM, Xie F, Lee TA, Schwarz A. Time-specific differences in stated preferences for health in the United States. Med Care. 2022. 10.1097/MLR.0000000000001714.35315380 10.1097/MLR.0000000000001714

17. Devlin NJ. Valuing child health isn’t child’s play. Value Health. 2022. 10.1016/j.jval.2022.05.009.35667949 10.1016/j.jval.2022.05.009

18. National Institute for Health and Care Excellence (2023). NICE health technology evaluations: the manual. https://www.nice.org.uk/process/pmg36. Accessed 30 Sept 2024.

19. Bailey C, Howell M, Raghunandan R, Howard K, Mulhern B, Petrou S, Rowen D, Salisbury A, Lancsar E, Devlin N. The RETRIEVE checklist for studies reporting the elicitation of stated preferences for child health-related quality of life. Pharmacoeconomics. 2024. 10.1007/s40273-023-01333-z.38217776 10.1007/s40273-023-01333-zPMC10937763

20. Hiligsmann M, Liden B, Beaudart C, Germeni E, Hanna A, Joshi M, Koola CP, Stein B, Tonkinson M, Marshall D, Fifer S. HTA community perspectives on the use of patient preference information: lessons learned from a survey with members of HTA bodies. Int J Technol Assess Health Care. 2024. 10.1017/S0266462324000138.38439624 10.1017/S0266462324000138PMC11569952

21. Nazari JL, Pickard AS, Gu NY. Findings from a roundtable discussion with US stakeholders on valuation of the EQ-5D-Y-3L. Pharmacoeconomics. 2022. 10.1007/s40273-022-01222-x.36443519 10.1007/s40273-022-01222-xPMC9758239

22. Powell PA, Rowen D, Keetharuth A, Mukuria C. Understanding UK public views on normative decisions made to value health-related quality of life in children: a qualitative study. Soc Sci Med. 2024. 10.1016/j.socscimed.2023.116506.38104438 10.1016/j.socscimed.2023.116506

23. Xie F, Xie S, Pullenayegum E, Ohinmaa A. Understanding Canadian stakeholders’ views on measuring and valuing health for children and adolescents: a qualitative study. Qual Life Res. 2024. 10.1007/s11136-024-03618-y.38438665 10.1007/s11136-024-03618-yPMC11045599

24. Devlin NJ, Drummond MF, Mullins CD. Quality-adjusted life years, quality-adjusted life-year-like measures, or neither? The debate continues. Value Health. 2024. 10.1016/j.jval.2024.04.021.38705459 10.1016/j.jval.2024.04.021

25. Lakdawalla DN, Phelps CE. Health technology assessment with diminishing returns to health: the Generalized Risk-Adjusted Cost-Effectiveness (GRACE) approach. Value Health. 2021. 10.1016/j.jval.2020.10.003.33518031 10.1016/j.jval.2020.10.003

26. Soekhai V, Whichello C, Levitan B, Veldwijk J, Pinto CA, Donkers B, Huys I, van Overbeeke E, Juhaeri J, de Bekker-Grob E. Methods for exploring and eliciting patient preferences in the medical product lifecycle: a literature review. Drug Discov Today. 2019. 10.1016/j.drudis.2019.05.001.31077814 10.1016/j.drudis.2019.05.001

27. Ramos-Goñi JM, Oppe M, Slaap B, van Busschbach JJV, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017. 10.1016/j.jval.2016.10.012.28292492 10.1016/j.jval.2016.10.012

28. Feng Y, Devlin NJ, Shah KK, Mulhern B, van Hout B. New methods for modelling EQ-5D-5L value sets: an application to English data. Health Econ. 2018. 10.1002/hec.3560.28833854 10.1002/hec.3560PMC5836982

29. Peasgood T, Bourke M, Devlin N, Rowen D, Yang Y, Dalziel K. Randomised comparison of online interviews versus face-to-face interviews to value health states. Soc Sci Med. 2023. 10.1016/j.socscimed.2023.115818.36940582 10.1016/j.socscimed.2023.115818PMC9993735

30. Jiang R, Shaw J, Muhlbacher A, Lee TA, Walton S, Kohlmann T, Norman R, Pickard AS. Comparison of online and face-to-face valuation of the EQ-5D-5L using composite time trade-off. Qual Life Res. 2021. 10.1007/s11136-020-02712-1.33247810 10.1007/s11136-020-02712-1PMC8068705

31. Hill SR, Gibson A, Oluboyede Y, Longworth L, Bennett B, Shaw JW. A methodological study to compare alternative modes of administration with value EQ-5D using preference-elicitation techniques. Value Health. 2024. 10.1016/j.jval.2024.02.020.38467189 10.1016/j.jval.2024.02.020

32. Jonker MF, Donkers B, de Bekker-Grob EW, Stolk EA. Advocating a paradigm shift in health-state valuations: the estimation of time-preference corrected QALY tariffs. Value Health. 2018. 10.1016/j.jval.2018.01.016.30098678 10.1016/j.jval.2018.01.016

33. Hess S, Daly A, Batley R. Revisiting consistency with random utility maximisation: theory and implications for practical work. Theory. 2018. 10.1007/s11238-017-9651-7.10.1007/s11238-017-9651-7PMC695399431983783

34. Augestad LA, Rand-Hendriksen K, Stavem K, Sonbo KI. Time trade-off and attitudes toward euthanasia: implications of using ‘death’ as an anchor in health state valuation. Qual Life Res. 2013. 10.1007/s11136-012-0192-9.22678351 10.1007/s11136-012-0192-9

35. Claxton K, Sculpher M, Drummond M. A rational framework for decision making by the National Institute for Clinical Excellence (NICE). Lancet. 2002. 10.1016/S0140-6736(02)09832-X.12241891 10.1016/S0140-6736(02)09832-X

36. Saramago P, Manca A, Sutton AJ. Deriving input parameters for cost-effectiveness modeling: taxonomy of data types and approaches to their statistical synthesis. Value Health. 2012. 10.1016/j.jval.2012.02.009.22867772 10.1016/j.jval.2012.02.009

37. Paisley S. Identification of evidence for key parameters in decision-analytic models of cost effectiveness: a description of sources and a recommended minimum search requirement. Pharmacoeconomics. 2016. 10.1007/s40273-015-0372-x.26861793 10.1007/s40273-015-0372-x

38. Sculpher M, Pang FS, Manca A, Drummond MF, Golder S, Urdahl H, Davies LM, Eastwood A. Generalisability in economic evaluation studies in healthcare: a review and case studies. Health Technol Assess. 2004. 10.3310/hta8490.15544708 10.3310/hta8490

39. Xie RZ, deFur ME, Linthicum MT, Bright JL. Putting stakeholder engagement at the Center of Health Economic Modeling for Health Technology Assessment in the United States. Pharmacoeconomics. 2021. 10.1007/s40273-021-01036-3.33982198 10.1007/s40273-021-01036-3PMC8166701

40. Ackerman IN, Norman R, Harris IA, Cashman K, Lorimer M, Gill S, Lewis P, Soh SE. How does the new Australian EQ-5D-5L value set impact utility scores? Analysis of data from the Australian Orthopaedic Association National Joint Replacement Registry. Appl Health Econ Health Policy. 2024. 10.1007/s40258-024-00894-0.38878238 10.1007/s40258-024-00894-0PMC11339144

41. Eckermann S, Willan AR. Expected value of information and decision making in HTA. Health Econ. 2007. 10.1002/hec.1161.16981193 10.1002/hec.1161
