---
project_id: "304-PHD"
work_id: "doi:10.1007/s40273-024-01444-1"
doi: "10.1007/s40273-024-01444-1"
pmid: "39487899"
pmcid: "PMC11782394"
title: "Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments"
journal: "Pharmacoeconomics"
publication_date: "2024-11-02"
volume: "43"
issue: "2"
authors:
  - name: "Maksat Jumamyradov"
    orcid: "http://orcid.org/0009-0008-0180-7224"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Benjamin M. Craig"
    orcid: "http://orcid.org/0000-0003-1121-1316"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/032db5x82grid.170693.a0000 0001 2353 285XDepartment of Economics, University of South Florida, Tampa, FL USA"
  - id: "Aff2"
    name: "https://ror.org/02v80fc35grid.252546.20000 0001 2297 8753Department of Health Outcomes Research and Policy, Auburn University, Auburn, AL USA"
licence: "cc-by-nc"
source_file: "input/projects/304-PHD/papers/doi_10.1007_s40273-024-01444-1.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11782394/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b908b254e120ba604b65b6fbf9515bb55da21e943ecf3337deed20ec67399722"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments

## Abstract

### Background

A key challenge in value assessment is how to summarize effectiveness, particularly the impact of interventions on patient health-related quality of life (HRQoL). One approach is to quantify the gains in HRQoL and life expectancy together as quality-adjusted life years (QALYs); however, this approach has faced various criticisms regarding its potential discriminatory aspects toward persons with disabilities, older adults, and the most vulnerable individuals in society.

### Methods

Instead of QALYs, we provide an alternative approach that summarizes HRQoL gains from the perspective of its stakeholders (e.g., patients, parents, and caregivers) using an “experience” scale. On an experience scale, a positive value signifies an experience better than having no experience at all, while a negative value indicates an experience worse than having no experience. To illustrate the merits of this approach, we examine US preferences on the relief of child health problems, namely a discrete choice experiment (DCE) with kaizen tasks and alternatives described using the EQ-5D-Y-3L.

### Results

Using this approach, we demonstrate the differences in perspectives between parents (*N* = 179), mothers (*N* = 99), and fathers (*N* = 80) of children younger than 18 years of age, as well as the feasibility of this patient-centered approach using a brief DCE survey of less than 100 respondents each (and without QALYs).

Specifically, we found that mothers place a higher value on the child’s feelings than fathers. The results also suggest other differences between the perspectives of mothers and fathers, but these differences were not statistically significant (p-values \< .05).

### Conclusions

We put forth that future value assessments may summarize gains in HRQoL on a patient experience scale (i.e., experience scale from the patient perspective) to inform decision-making.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40273-024-01444-1.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| The Inflation Redaction Act of 2022 prohibits using quality-adjusted life years (QALYs) or similar measures in the Medicare Drug Price Negotiation Program because they may discriminate against individuals who have serious illnesses, are older, or have disabilities. |
| We demonstrate the differences in perspectives between parents (N = 179), mothers (N = 99), and fathers (N = 80) of children younger than 18 years of age using a brief DCE survey of less than 100 respondents each (and without QALYs). |
| This patient-centered approach to value assessment measures effectiveness based on multiple perspectives and on a scale that reflects patient experience, instead of QALYs. |

</div>

## Introduction

Governmental organizations bear the responsibility of directing public resources toward health interventions that optimize the overall health of the population, which involves both health-related quality of life (HRQoL) and life years \[1\]. To aid in making informed decisions regarding resource allocation, health economists systematically assess the costs and effects of various interventions as part of their value assessments. Rather than expressing health outcomes in monetary terms (i.e., cost–benefit analyses), most analysts conduct cost-effectiveness analyses (CEA) \[2\], which express the net value of new interventions in terms of the ratio of incremental effectiveness to incremental costs \[3\]. As emphasized in the Second Panel on Cost-Effectiveness in Health and Medicine \[4\], it is important to consider a wide range of costs and effectiveness levels since some effects of the intervention might be overlooked or underappreciated. To expand perspectives on what defines value in healthcare, the 2018 ISPOR Special Task Force (STF) introduced the concept of the “value flower.” For this framework, the STF identified 12 essential elements for CEA, including quality-adjusted life year (QALY) gains \[5, 6\].

In CEA, incremental effectiveness may be expressed in terms of gains in QALYs, a standardized measure that combines HRQoL and life years based on the preferences of the general population. The QALY is anchored at 0 and 1, where the lower anchor on the QALY scale represents “dying immediately” and the upper anchor represents “starting today, 1 year with no health problems then die” \[7\]. Policymakers in many countries endorse QALYs as a summary measure for assessing health benefits alongside incremental cost in drug coverage decisions within national healthcare systems and negotiations with manufacturers regarding pricing \[8\]. QALYs facilitate comprehensive decision-making by offering a single, uniform metric that allows for quantitative evaluation of the effects of various conditions and treatments on overall health. Thus, QALYs allow for direct comparison of various health treatments and interventions \[9\] and can help determine the most efficient allocation of resources for optimizing overall population health \[10\].

However, the summary of HRQoL and life expectancy on a QALY scale has faced various criticisms, particularly regarding its potential discriminatory aspects toward persons with disabilities, older adults, and the most vulnerable individuals in society. Since some groups generally have lower HRQoL, QALY gains from extending their life expectancies are less than for other groups \[11\]. In the USA, these criticisms have led to lobbying efforts against the use of QALY by various interest groups and disability rights advocates, particularly in the context of federal programs. Specifically, the National Council on Disability (NCD) reported that “QALYs place a lower value on treatments which extend the lives of people with chronic illnesses and disabilities” \[12\] and suggested to Congress, other federal agencies, and public and private insurers to reject QALYs for the summary of effectiveness in CEA \[13\].

Although economists remain supportive of QALYs \[5, 6, 14\], these criticisms have been gaining traction. For example, the Inflation Reduction Act (IRA) of 2022, under section 1194(e)(2), states, “The secretary shall not use evidence from comparative clinical effectiveness research in a manner that treats extending the life of an elderly, disabled, or terminally ill individual as of lower value than extending the life of an individual who is younger, nondisabled, or not terminally ill” \[15\]. This prohibits the use of QALYs or other similar measures in the Medicare Drug Price Negotiation Program, in part because they can discriminate against those who have serious illnesses, are older, or have disabilities \[16, 17\].

This paper puts forth an alternative approach to value assessments that summarizes gains in HRQoL apart from life expectancy. Using small samples, researchers can summarize HRQoL gains from the perspectives of multiple stakeholders on an “experience” scale. On this scale, a positive value signifies an experience better than having no experience at all (i.e., “being in a coma”), while a negative value indicates an experience worse than having no experience. Regarding the “value flower,” decision scientists may split QALY gains into their components (HRQoL and life expectancy) and, thus, account for the diverse perspectives on the effectiveness of interventions. We acknowledge that this approach does not fully replace QALYs; however, this alternative approach is responsive to recent criticisms, relatively inexpensive, and feasible in small samples (less than 100 surveys).

To illustrate this approach, we examined US preferences on the relief of child health problems, namely, a discrete choice experiment (DCE) with kaizen tasks and alternatives described using the EQ-5D-Y-3L \[18–20\]. Kaizen is a Japanese term that describes continuous improvement, which in this case, is the discrete evolution of an object over a sequence of choices. Kaizen tasks elicit preference paths (i.e., each respondent’s optimal sequence of improvements from an initial profile toward an idealized destination).

The results demonstrate the differences in perspective between parents (*N* = 179), mothers (*N* = 99), and fathers (*N* = 80), as well as how such a DCE with kaizen tasks is feasible with less than 100 respondents (and without QALYs). It is not difficult to imagine a similar study being conducted based on policy recommendations from the IRA regarding specific populations (e.g., patients enrolled in a clinical trial). Given that this approach involves a brief survey with a small sample (less than 100 respondents), we put forth that future value assessments may summarize the HRQoL gains of specific interventions on a patient experience scale (i.e., experience scale from the patient perspective) instead of QALYs.

## Methods

Between 29 September and 10 October 2023, we conducted a child health valuation survey with a DCE with a representative sample of US adults. Out of 631 respondents who completed the survey, there are 179 parents. Among these, there are 99 mothers and 80 fathers. The study protocol, including the survey instrument, experimental design, and data analysis plan, is available in an open-access publication \[20\].

In each preference elicitation task, child health problems were described using the EQ-5D-Y-3L (Supplementary File 1 in Electronic Supplementary Material \[ESM\]), a generic instrument developed to measure HRQoL in children and adolescents aged 8–15 years \[21\]. It has five domains (mobility, looking after myself, doing usual activities, having pain or discomfort, and feeling worried, sad, or unhappy; Table <a href="#Tab1" data-ref-type="table">1</a>), and each domain can be classified from level 1 (best) to level 3 (worst).

<div id="Tab1" class="table-wrap">

<div class="caption">

Gains in child health-related quality of life on an experience scale

</div>

| Child health-related quality of life | Parents (*N* = 179) | Mothers (*N* = 99) | Fathers (*N* = 80) |
|----|----|----|----|
| Mobility (walking around) |  |  |  |
|  MO1: Some-to-no problems walking around | 0.123\*\*\* (0.023) | 0.143\*\*\* (0.030) | 0.092\*\* (0.051) |
|  MO2: A lot-to-some problems walking around | 0.121\*\*\* (0.023) | 0.117\*\*\* (0.029) | 0.130\*\*\* (0.065) |
| Looking after myself |  |  |  |
|  SC1: Some-to-no problems taking a bath or shower by myself or getting dressed by myself | 0.040\* (0.020) | 0.049\* (0.023) | 0.027 (0.042) |
|  SC2: A lot-to-some problems taking a bath or shower by myself or getting dressed by myself | 0.073\*\*\* (0.020) | 0.063\*\* (0.023) | 0.091\*\* (0.046) |
| Doing usual activities |  |  |  |
|  UA1: Some-to-no problems doing my usual activities | 0.068\*\*\* (0.019) | 0.056\* (0.025) | 0.088\*\* (0.042) |
|  UA2: A lot-to-some problems doing my usual activities | 0.109\*\*\* (0.022) | 0.095\*\*\* (0.026) | 0.131\*\*\* (0.090) |
| Having pain or discomfort |  |  |  |
|  PD1: Some-to-no pain or discomfort | 0.276\*\*\* (0.035) | 0.251\*\*\* (0.038) | 0.316\*\*\* (0.168) |
|  PD2: A lot-to-some pain or discomfort | 0.334\*\*\* (0.048) | 0.301\*\*\* (0.054) | 0.387\*\*\* (0.213) |
| Feeling worried, sad or unhappy |  |  |  |
|  AD1: A bit-to-not worried, sad, or unhappy | 0.029 (0.022) | 0.068\*\* (0.026) | −0.031 (0.069) |
|  AD2: Very-to-a-bit worried, sad, or unhappy | 0.121\*\*\* (0.028) | 0.128\*\*\* (0.033) | 0.111\* (0.067) |

Each estimate represents the value associated with an improvement in child HRQoL on an experience scale, namely the incremental effect of relieving a child health problem based on stakeholder values. Significance levels (*P* values): ‘\*\*\*’ 0.001, ‘\*\*’ 0.01, ‘\*’ 0.05

</div>

Instead of asking respondents to choose between two terminally ill children such as in paired comparisons \[22\], the ten kaizen tasks in this DCE survey \[20\] introduced a single profile of a 10-year-old child with health problems and asked the respondents to express their preferences on the relief of these problems. To identify the lower anchor of the experience scale, the DCE also included five paired comparisons asking whether experiencing specific problems was better or worse than “being in a coma” (i.e., no experience). Compared with other choice tasks, the two key advantages of kaizen tasks are that they elicit preferences more efficiently (i.e., more preference evidence per task) and in a manner that is less burdensome on respondents (i.e., relieving a child’s problems instead of choosing between problems).

To demonstrate the values on an experience scale, we conducted a secondary analysis and estimated three conditional logit models in three samples (see Supplementary File 1 for more details on technical analysis): parents, mothers, and fathers of children age 18 years or younger (*N* = 179, 99, and 80, respectively). Each model has 10 incremental effects (MO1, MO2, SC1, SC2, UA1, UA2, PD1, PD2, AD1, and AD2), as well as two scaling terms (one for kaizen tasks and another for paired comparisons). To account for within-respondent correlations, the *P* values and standard errors were estimated using the cluster bootstrap technique (with replacement) and the percentile method. The demographic and socioeconomic characteristics of the three samples can be found in the Supplementary File 2 of ESM.

## Results

Table <a href="#Tab1" data-ref-type="table">1</a> presents the value of gains in child HRQoL on an experience scale from the perspective of parents, mothers, and fathers of children age 18 or younger (i.e., the value of each incremental improvement and their standard errors). Mothers and fathers place a positive value on each gain in child HRQoL (*P* value \< 0.05), except that fathers seem ambivalent about the gains from some to no problems in self-care (SC1) and a bit to not worried, sad, or unhappy (AD1) for a week. Upon closer inspection, mothers place a higher value on the child’s feelings than fathers (*P* value for the differences in AD1 is 0.023). Table <a href="#Tab1" data-ref-type="table">1</a> suggests other differences between the perspectives of mothers and fathers, but these differences were not statistically significant (*P* values \< 0.05).

On an experience scale, having each problem at their worst (33333) is equal to 1 minus the sum of the ten incremental effects. From the perspective of parents, this worst-case scenario has a value of −0.294, which implies that it is worse than no experience (i.e., “being in a coma”; *P* value = 0.03). Using the results from Table <a href="#Tab1" data-ref-type="table">1</a>, a value assessment can summarize the gains in child HRQoL from three perspectives on an experience scale. These are not standard Y-3L value sets. This use of experience scale is an unconventional feature in health valuation at this time.

## Discussion

Among its merits, experience scaling has three noteworthy advantages over QALYs and traditional approaches. First, unlike QALYs, expressing the value of gains in experience scaling does not discriminate against extending the life expectancy of groups with generally lower HRQoL. Gains in HRQoL or life expectancy among persons with disabilities or older adults have the same value as any other groups. This is particularly responsive to section 1194(e)(2) of the IRA \[15–17\].

The second advantage is that experience scaling allows us to summarize HRQoL gains from the perspectives of multiple stakeholders. This inclusive approach acknowledges that value of HRQoL gains is subjective and varies among different groups (e.g., mothers versus fathers). By summarizing HRQoL gains from various perspectives, decision-makers benefit from a more comprehensive understanding of the value of an intervention and the various components of that comprise that value. This broader view can inform more targeted and inclusive healthcare policies and interventions.

A third advantage of experience scaling is that these value sets do not require as many resources as a national value set on a QALY scale (e.g., over 1000 interview surveys) \[22\]. Unlike traditional methods that require trained interviewers and large samples (e.g., time tradeoff), a brief DCE survey with kaizen tasks can yield precise results in a matter of days with a relatively small number of respondents, often less than 100. This efficiency not only saves time but also reduces respondent burden, making it a practical choice for value assessments \[23\].

The merits of experience scaling must be balanced against their potential limitations. Experience scaling only summarizes HRQoL, not life expectancy. In this example, respondents were asked about their preferences on the relief of child health problems, not whether the child lives or dies. We recommend that value assessments express gains in life expectancy apart from HRQoL, thus broadening the concept of value \[6\].

The primary argument for QALYs is that they are applicable to all interventions. As Steven Pearson, president of the Institute for Clinical and Economic Review (ICER), put it, using this common metric protects “the patient not in the room” \[24\]. He wrote further, “Although every added dollar the United States spends on health care may generate added health, at least for those directly benefiting from that extra spending, it also puts more pressure on health insurance premiums, harming patients not in the room.” Furthermore, it is important to note that QALY can be modified to accommodate differential weighting of benefits \[25\] according to equity principles such as preference for severity \[26\] or willingness to prioritize end-of-life treatments \[27\].

The use of experience scaling can emphasize the patients’ authority to characterize what constitutes a good or bad experience; however, this advantage makes it poorly suited for decisions across all conditions. A gain of 0.1 from the perspective of diabetes patients may not be comparable with a 0.1 gain from the perspective of cancer patients. In a sense, the summary of HRQoL using national or patient values is similar to the federalist debate about the distribution of power between states and the federal government.

This approach does not dictate the deliberative authority of one perspective over another. Instead, we recognize that the value of HRQoL gains varies between groups and suggest that value assessments be inclusive of diverse perspectives. In this example, we show that child HRQoL gains can be summarized from the perspective of mothers, fathers, or parents generally. When faced with strategic incentives, analysts may “cherry pick” among the perspectives, presenting only those that favor their interventions. To address this potential bias, we further recommend that value assessments summarize HRQoL gains from the perspectives of all groups involved and test for systematic differences (e.g., mothers versus fathers). We demonstrate the feasibility of the approach and avoid defining deliberative authority, which is beyond the scope of this paper.

Recently, criticisms against the QALY scale led to the development of alternative tools. In 2018, the Institute of Clinical and Economic Review (ICER) developed the equal value of life years gained (evLYG) which, similar to this study, entails the measurement of the quality of life equally for everyone during any periods of life extensions \[28\]. Likewise, researchers at the University of Washington introduced the healthy years in total (HYT) where they separate life years extended from HRQoL and take an additive approach instead of multiplicative \[29\]. However, it is unclear whether these alternative approaches promote weighing qualities of life using preference evidence. Lakdawalla and Phelps \[30\] introduced the generalized risk-adjusted QALY (GRA-QALY) where they consider risk-aversion in their assessment of quality of life. Specifically, GRA-QALY allows for various willingness-to-pay thresholds depending on the illness severity but ignores prospect theory (i.e., a common non-linearity in risk where individuals evaluate potential gains and losses relative to a reference point rather than absolute outcomes). This paper proposes an alternative approach that is scalable to multiple involved groups and summarizes patient experience on a scale where outcomes with positive (negative) values are better (worse) than no experience (i.e., being in a coma).

One should also keep in mind that when adults assess the value of child HRQoL from a child’s perspective, significant discrepancies often emerge compared with how they rate the same HRQoL for themselves \[31, 32\]. This discrepancy highlights a potential bias in how HRQoL may be perceived differently. Our study examines how adults, namely mothers and fathers, assess the value of child HRQoL from their own perspective. Analogously, an adult may assess value of a vaccine for a child from the child’s perspective, for an adult from their own perspective or for a child from their own perspective (like this study). While differences in value are expected between these alternative applications and perspectives, we further recognize that authority over resource allocation decisions that affect child HRQoL typically resides with the general population (i.e., societal perspective), not mothers and fathers.

The methodology used to create these value sets on an experience scale is innovative and specialized (e.g., kaizen tasks or online survey). Further methodologic development is warranted. For instance, researchers may analyze how experience scale will perform with different child ages and problems durations as well as assess its performance in other countries and marginalized groups. Unlike paired comparisons, DCE surveys with kaizen tasks may not be accessible within the broader research community (e.g., no open-source software available). It may take years for this approach to be integrated into health economics curricula generally.

## Conclusions

This paper introduces experience scaling as an alternative to QALYs and shows how a DCE survey with kaizen tasks can summarize HRQoL with a small sample of respondents. The example detailed here demonstrates the differences in perspectives between parents (*N* = 179), mothers (*N* = 99), and fathers (*N* = 80) of children younger than 18 years of age. For example, the findings show that mothers generally place a higher value on a child’s feelings than fathers.

Since experience scaling directly addresses section 1194 (e)(2) of the IRA and is feasible in small samples, this approach may be considered a scalable and fair alternative to QALYs for value assessment, characterizing a diversity of perspectives. In the future, the summary of HRQoL gains on a patient experience scale (i.e., an experience scale from the patient perspective) may become commonplace when describing the effectiveness of interventions to the Medicare Drug Price Negotiation Program.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 18 KB)

</div>

<div class="caption">

Supplementary file2 (DOCX 24 KB)

</div>

### Acknowledgement

The authors acknowledge the EuroQol Research Foundation for their support of M.J.’s dissertation (304-PHD), under the supervision of Drs. Murat K. Munkin and B.M.C., University of South Florida, Tampa, USA.

### Declarations

#### Funding/Support

This study was funded by the EuroQol Research Foundation supported.

#### Conflicts of Interest

M.J. reports grant funding from the EuroQol Research Foundation (no: 304-PHD), during the conduct of the study. B.M.C. reports no disclosures.

#### Role of Funder/Sponsor

The funder had no role in the design and conduct of the study; data collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

#### Data Availability

The data are available from the authors upon reasonable request.

#### Author Contributions

Concept and design: M.J. and B.M.C. Acquisition of data: M.J. and B.M.C. Analysis and interpretation of data: M.J. and B.M.C. Drafting of the manuscript: M.J. and B.M.C. Critical revision of paper for important intellectual content: M.J. and B.M.C. Statistical analysis: M.J. and B.M.C. Obtaining funding: B.M.C. Supervision: B.M.C.

## References

1. Berg RL. Health status indexes. Health Serv Res. 1975;10(4):416–7.

2. Robinson R. Cost-effectiveness analysis. BMJ. 1993;307:793–5. 10.1136/bmj.307.6907.793.8219957 10.1136/bmj.307.6907.793PMC1696433

3. Levin HM, Mcewan PJ. Cost-effectiveness analysis: methods and applications. New York: Sage Publications; 2001.

4. Neumann PJ, Sanders GD, Russell LB, Siegel JE, Ganiats TG. Cost effectiveness in health and medicine. Oxford: Oxford University Press; 2017.

5. Lakdawalla DN, Doshi JA, Garrison LP, Phelps CE, Basu A, Danzon PM. Defining elements of value in health care—a health economics approach: an ISPOR special task force report [3]. Value Health. 2018;21(2):131–9. 10.1016/j.jval.2017.12.007.29477390 10.1016/j.jval.2017.12.007

6. Garrison LP Jr, Kamal-Bahl S, Towse A. Toward a broader concept of value: identifying and defining elements for an expanded cost-effectiveness analysis. Value Health. 2017;20(2):213–6. 10.1016/j.jval.2016.12.005.28237197 10.1016/j.jval.2016.12.005

7. Craig BM, Rand K, Bailey H, Stalmeier PF. Quality-adjusted life-years without constant proportionality. Value Health. 2018;21(9):1124–31. 10.1016/j.jval.2018.02.004.30224118 10.1016/j.jval.2018.02.004

8. Rand LZ, Kesselheim AS. An international review of health technology assessment approaches to prescription drugs and their ethical principles. J Law Med Ethics. 2020;48(3):583–94. 10.1177/1073110520958885.33021189 10.1177/1073110520958885

9. Whitehead SJ, Ali S. Health outcomes in economic evaluation: the QALY and utilities. Br Med Bull. 2010;96(1):5–21. 10.1093/bmb/ldq033.21037243 10.1093/bmb/ldq033

10. Gold MR, Stevenson D, Fryback DG. HALYS and QALYS and DALYS, oh my: similarities and differences in summary measures of population health. Annu Rev Public Health. 2002;23(1):115–34. 10.1146/annurev.publhealth.23.100901.140513.11910057 10.1146/annurev.publhealth.23.100901.140513

11. Rand LZ, Kesselheim AS. Controversy over using quality-adjusted life-years in cost-effectiveness analyses: a systematic literature review. Health Aff. 2021;40(9):1402–10. 10.1377/hlthaff.2021.00343.10.1377/hlthaff.2021.0034334495724

12. National Council on Disability. Quality-adjusted life years and the devaluation of life with disability. National Council on Disability; 2019. https://ncd.gov/sites/default/files/NCD_Quality_Adjusted_Life_Report_508.pdf

13. US Senate Committee on Finance. [Letter to Secretary Becerra and Administrator Brooks-LaSure]; 2023. https://www.finance.senate.gov/imo/media/doc/sfc_gop_letter_to_hhs_cms.pdf

14. Dolan P, Shaw R, Tsuchiya A, Williams A. QALY maximisation and people’s preferences: a methodological review of the literature. Health Econ. 2005;14(2):197–208. 10.1002/hec.924.15386656 10.1002/hec.924

15. Inflation Redaction Act of 2022, Public L No. 117-169, 124 Stat 1818 (2022). https://www.congress.gov/bill/117th-congress/house-bill/5376

16. Poudel N, Ngorsuraches S. Using a patient-centered value assessment to optimize fair prices for inflation reduction act’s medicare drug price negotiation program. J Manage Care Spec Pharm. 2023;30(3):217–301. 10.8553/jmcp.2023.23233.10.18553/jmcp.2023.23233PMC1090644838140902

17. O’Brien JM. Setion 50 of the inflation reduction act drug price negotiation program: considerations for the centers for medicare & medicaid services, manufacturers, and the health economics and outcomes research community. Value Health. 2023;26(12):1681–5. 10.1016/j.jval.2023.09.2995.37827492 10.1016/j.jval.2023.09.2995

18. Craig BM, Rand K, Hartman JD. Preference paths and their kaizen tasks for small samples. Patient. 2021;15(2):187–96. 10.1007/s40271-021-00541-z.34327605 10.1007/s40271-021-00541-zPMC8321769

19. Craig BM. United States COVID-19 vaccination preferences (CVP): 2020 hindsight. Patient. 2021;14(3):309–18. 10.1007/s40271-021-00508-0.33783724 10.1007/s40271-021-00508-0PMC8008018

20. Jumamyradov M, Craig BM, Rivero-Arias O, Jakubczyk M. Child health valuation protocol for a discrete choice experiment comparing paired comparison and kaizen tasks and estimating US EQ-5D-Y-3L values on an experience scale. BMJ Open. 2023;13: e077256. 10.1136/bmjopen-2023-077256.37879694 10.1136/bmjopen-2023-077256PMC10603523

21. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the instrument’s characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22(1):31–7. 10.1016/j.jval.2018.11.001.30661631 10.1016/j.jval.2018.11.001

22. Craig BM, Greiner W, Brown DS, Reeve BB. Valuation of child health-related quality of life in the United States. Health Econ. 2016;25(6):768–77. 10.1002/hec.3184.25926161 10.1002/hec.3184

23. Craig BM, Jumamyradov M, Rivero-Arias O. The performance of kaizen tasks across three online DCE surveys: an evidence synthesis. Patient-Center Outcomes Res. 2024. 10.1007/s40271-024-00708-4.10.1007/s40271-024-00708-4PMC1146164539031285

24. Pearson SD. The patient not in the room. Ann Intern Med. 2021;174(1):109–10. 10.7326/M20-7052.33136425 10.7326/M20-7052

25. Williams A. QALYs and ethics: a health economist’s perspective. Soc Sci Med. 1996;43(12):1795–804. 10.1016/S0277-9536(96)00082-2.8961422 10.1016/s0277-9536(96)00082-2

26. Cookson R, Dolan R. Public views on health care rationing: a group discussion study. Health Policy. 1999;49:63–74. 10.1016/S0168-8510(99)00043-3.10827291 10.1016/s0168-8510(99)00043-3

27. Pinto-Prades JL, Sánchez-Martínez FI, Corbacho B, Baker R. Valuing QALYs at the end of life. Soc Sci Med. 2014;113:5–14. 10.1016/j.socscimed.2014.04.039.24820408 10.1016/j.socscimed.2014.04.039

28. Institute for Clinical and Economic Review. Cost-effectiveness, the QALY, and the evLYG; 2021. https://icer.org/our-approach/methods-process/cost-effectiveness-the-qaly-and-the-evlyg/

29. Anirban B, Carlson J, Veenstra D. Health years in total: a new health objective function for cost-effectiveness analysis. Value Health. 2020;23(1):96–103. 10.1016/j.jval.2019.10.014.31952678 10.1016/j.jval.2019.10.014

30. Lakdawalla DN, Phelps CE. Health technology assessment with risk aversion in health. J Health Econ. 2020;72: 102346. 10.1016/j.jhealeco.2020.102346.32592923 10.1016/j.jhealeco.2020.102346PMC7402585

31. Attema AE, Lang Z, Lipman SA. Can independently elicited adult- and child-perspective health-state utilities explain priority setting? Value Health. 2023;26(11):1645–54. 10.1016/j.jval.2023.08.002.37659690 10.1016/j.jval.2023.08.002

32. Lipman SA, Essers BAB, Finch AP, et al. In a child’s shoes: composite time trade-off valuations for EQ-5D-Y-3L with different proxy perspectives. Pharmacoeconomics. 2022;40(2):181–92. 10.1007/s40273-022-01202-1.36255560 10.1007/s40273-022-01202-1PMC9579618
