---
project_id: "399-RA"
work_id: "doi:10.1177/0272989x251380556"
doi: "10.1177/0272989X251380556"
pmid: "41408725"
pmcid: "PMC12769929"
title: "Uncertainty around Health State Values Used in Cost-Effectiveness Analysis: How It Arises and How to Deal with It"
journal: "Medical Decision Making"
publication_date: "2025-12-17"
volume: "46"
issue: "2"
authors:
  - name: "David Parkin"
    affiliation_ids:
      - "aff1-0272989X251380556"
      - "aff2-0272989X251380556"
  - name: "Andrew Briggs"
    affiliation_ids:
      - "aff3-0272989X251380556"
  - name: "Giselle Abangma"
    affiliation_ids:
      - "aff4-0272989X251380556"
  - name: "Andrew Lloyd"
    affiliation_ids:
      - "aff5-0272989X251380556"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "aff6-0272989X251380556"
affiliations:
  - id: "aff1-0272989X251380556"
    name: "City St George’s, University of London, London UK"
  - id: "aff2-0272989X251380556"
    name: "Office of Health Economics, London UK"
  - id: "aff3-0272989X251380556"
    name: "London School of Hygiene and Tropical Medicine, London UK"
  - id: "aff4-0272989X251380556"
    name: "London School of Hygiene and Tropical Medicine, London UK"
  - id: "aff5-0272989X251380556"
    name: "London School of Hygiene and Tropical Medicine, London UK"
  - id: "aff6-0272989X251380556"
    name: "Melbourne School of Population of Global Health, University of Melbourne, Australia"
licence: "cc-by-nc"
source_file: "input/projects/399-RA/papers/doi_10.1177_0272989x251380556.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12769929/fullTextXML"
source_method: "epmc_xml"
source_sha256: "9fd8ac69e93b15f22ffd1385e0a0a39b57e54857a0ba7168b13355211e72bfa1"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Uncertainty around Health State Values Used in Cost-Effectiveness Analysis: How It Arises and How to Deal with It

## Abstract

Health state values, often in the form of value sets that list values applied to particular health states, are used in cost-effectiveness analyses of health care to calculate gains in quality-adjusted life-years. These values are subject to several sources of uncertainty, arising from the fact that values are not constants but variables and are of different types including variability, heterogeneity, statistical uncertainty, and methodological variation. Currently, these sources are not fully documented and are not fully accounted for when creating and analyzing economic evaluation models. This may provide to users of such models a false sense of the precision of quality-adjusted life-year gain estimates and therefore of cost-effectiveness. This article provides a comprehensive account of such sources of uncertainty and how they interact. It also provides a more detailed account of how uncertainty arises in studies that elicit and model value sets. Its aim is to encourage research to measure and report uncertainty around health state values so it can be better accounted for in cost-effectiveness analyses.

### Highlights

- Health state values (HSVs) used in cost-effectiveness analysis are subject to multiple types of uncertainty, including variability, heterogeneity, statistical uncertainty, and methodological variation.

- Current reporting and guidelines often fail to fully document or address all sources of uncertainty in HSVs, which can mislead users about the precision of QALY and cost-effectiveness estimates.

- Valuation studies should report measures of uncertainty (such as standard errors or variance/covariance matrices) for HSVs, not just point estimates.

- Researchers, decision modellers, and guideline developers should recognise, measure, and report HSV uncertainty more thoroughly to improve the reliability of cost-effectiveness analyses.

**Keywords:** health state values, cost-effectiveness analysis, quality-adjusted life years, uncertainty quantification, sensitivity analysis, health technology assessment, valuation studies, reporting standards

Received 2025 Feb 25; Accepted 2025 Aug 20; Collection date 2026 Feb.

The treatment of uncertainty is a key feature of sensitivity analysis in cost-effectiveness analysis (CEA).<sup> 1 </sup> One source of uncertainty in estimating quality-adjusted life-years (QALYs) and incremental cost-effectiveness ratios (ICERs) is the use of health state values (HSVs) attached to descriptions of health states.<sup> [^1] </sup> HSVs are not constants but variables that have a distribution as well as a point estimate. However, the main focus of valuation studies, research that identifies HSVs for particular health states, has been to generate robust point estimates. Methods for understanding, identifying, quantifying, and reporting their distributions are less developed, and no comprehensive account of their sources and nature exists.

HSVs used in CEA models rarely have one source and undergo much processing before and during modelling. As a result, there are multiple sources of uncertainty that accumulate in the final values used. This is important because it may affect a CEA’s results and decisions that follow from it. For example, a study comparing estimates of QALY gains from diabetes-related interventions in different simulation models found that differences in estimates were mainly due to different modeling methods, but “varying utility values had an impact on incremental QALYs within each of the models.”<sup> 2 </sup>

Current guidance on how to capture and use information on uncertainty does not cover all aspects<sup>ii</sup>. For example, an ISPOR Good Practice Report provides guidance on sensitivity analysis where alternative value sets are available but does not analyze other HSV relevant uncertainty sources.<sup> 3 </sup> The Decision Support Unit (DSU) of England’s National Institute for Health and Care Excellence (NICE) provides uncertainty information for dimension and level parameters for UK EQ-5D-3L values, but CEA models require uncertainty estimated for health states, which combine dimensions and levels.<sup>4,5</sup> Some papers identify and discuss different sources and types of uncertainty<sup>6–8</sup> but lack empirical evidence on their relative importance. A guide to users of EQ-5D-5L values advises that “the analyst should treat the values in economic appraisal as uncertain parameters and subject them to sensitivity analysis, as with other non-stochastic uncertain variables” but notes that “currently this is not common practice.”<sup> 9 </sup> Similarly, the NICE DSU notes that although NICE submissions require economic model parameter uncertainty to be captured, typically “the uncertainty in the estimation of preference-based valuation weights has been ignored.”<sup> 5 </sup>

A recent scoping review found few studies of methods for identifying and reporting uncertainty around HSVs used in CEA.<sup> 10 </sup> Those found mostly focused on methods for capturing one type of uncertainty, parameter uncertainty.<sup>11–13</sup>

This article addresses this gap by providing a comprehensive account of sources of uncertainty affecting HSVs used to calculate QALYs within CEAs and how they interact. It focuses on values elicitation and modeling studies rather than analyzing in detail all possible uncertainty sources. Our aim is to encourage research to measure and report uncertainty around HSVs for better inclusion in CEAs.

## What Do We Mean by Uncertainty?

Inconsistent terminology complicates a comprehensive description of uncertainty affecting HSVs. Different definitions appear in different disciplines and fields, for example, exploratory and inferential statistics, econometrics, meta-analysis, mapping, and cost-effectiveness modeling. The following are closest to those in a key health care economic evaluation text.<sup> 14 </sup>

The term “uncertainty,” in relation to HSVs, refers to the imperfect knowledge that we have about them. Uncertainty has different sources that can be categorized into different types, which we call “variability,”“heterogeneity,”“statistical uncertainty,” and “methodological variation.”

“Variability” denotes intrinsic differences between individual cases, for example, in values that different people attach to health states or responses given when self-reporting their health for the same underlying health state. This “natural” variability is not in itself a problem, although it is one source of statistical uncertainty and is not amenable to change by researchers. It is, however, important to ensure that variability is accounted for and summarized in, for example, the choice of descriptive statistics to summarize an HSV distribution, such as mean and variance or median and quantiles.

“Heterogeneity” is usefully defined as variables relating to different subgroups of a population or sample having different statistical properties, such as a different mean or variance. One source of this may be a characteristic that differs between subgroups. Such characteristics may be known, for example, population mean values differing by sociodemographic characteristics or distributions of HSVs in valuation studies differing because they use different valuation methods. Subgroup characteristics may also be identifiable but unknown, such as differences in responses to the state “dead” in valuation tasks, which can be attributed to unobserved latent classes. A slightly different definition is implied by “unobserved heterogeneity,” in which differences between observations are affected by an unmeasured variable (i.e., an omitted variable).

Heterogeneity takes different forms depending on context, and different implications result. For example, HSV distributions for different sociodemographic groups may have different means, which is uncontroversial where they simply describe each group or where they are used for making decisions about each group’s own health care. There are more difficult issues if decision making relates to the population as a whole without regard for groups’ different HSVs; however, solutions to this are in the realm of policy, not science.<sup>15,16</sup>

“Statistical uncertainty” arises from using samples to infer population variables, for example, sample mean HSVs as an estimator of a population mean, with a standard error (SE) quantifying the sample mean variation around the true population mean. Methods for assessing and handling statistical uncertainty are well developed. Essentially, these assess estimators’ performance in bias and precision. A biased estimator has an expected value over repeated samples that is not equal to the true population value. This cannot be corrected by more sampling, although if the estimator is consistent, a large sample may better approximate the true value. “Precision” concerns random sampling error, whose size can be quantified and used in, for example, statistically based sensitivity analysis. However, measuring precision can be problematic for the typical use of HSVs in CEA, where multiple estimation procedures are used cumulatively. For example, such data may result from value set modeling within valuation studies, subsequent inclusion in meta-analysis, and cost-effectiveness modeling. The cumulative effect on the final results’ precision may be difficult to estimate.

Uncertainty may also be caused by “methodological variation.” One source of this is the different methods and instruments used to elicit values within studies that generate HSVs and how the study data are collected. Participants in such a study must give precise answers to questions to which they may have only an approximate answer. Moreover, their response may be affected by how they are asked, such as the valuation task that they are given and how this was administered. Such issues are addressed by consideration of the reliability and validity of questionnaire instruments and their application. Similar issues arise with methods that analyze the resulting values data, such as population value modeling, meta-analysis, and cost-effectiveness modeling. Such variability cannot be corrected by statistical methods but can be assessed by reliability, plausibility, and acceptability criteria; nonstatistically based sensitivity analysis may also be used.

## How Uncertainty in HSVs Combines with Other Sources of Uncertainty from Health State Descriptive Systems

In principle, a CEA study could elicit HSVs from clinical trial patients, capturing all internal sources of uncertainty such as patient variability in disease severity and treatment effects as well as study design, including valuation methods. In practice, patients’ health states are defined by clinical categories, for example, a diagnosis or disability state, or a health state descriptive system (HDS), which uses generic descriptors such as mobility, pain, and effect on activities of daily living. Externally generated HSVs are then attached to these.

An important type of HDS is one that has a value set created using that system to elicit HSVs from a sample of people, often the general public, such as the EQ-5D, SF-6D, or HUI. We will call this an HDS-V.<sup> [^2] </sup> A value set is a list of HSVs that are attached to each possible health state described by an HDS-V, often reported as an algorithm that generates those HSVs. Research that elicits values is a valuation study. A CEA model may incorporate data from an HDS-V and use its associated HSVs. However, the data may sometimes describe patients by clinical categories or an HDS without associated HSVs and use mapping to an HDS-V with associated HSVs.<sup> 17 </sup> Uncertainty at each stage accumulates, and there are even more complex possibilities, which are described below.

Health technology assessment guidance issued by relevant bodies in, inter alia, Denmark, England, and the Netherlands requires HSVs to be representative of their national populations’ preferences,<sup>18–20</sup> and the development of most HDS-Vs, such as EQ-5D-5L<sup> 21 </sup> and SF-6D,<sup> 22 </sup> reflects this. A valuation study involves collecting and analyzing data; the use of the resulting HSVs in CEA inherits the uncertainty within that study. Sometimes, the sources of HSVs use studies that themselves use data from mapping and meta-analysis studies, each of which contributes further uncertainty. The HSV uncertainty in a CEA study may therefore accumulate over several studies.

<a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> illustrates this as a flow diagram. The boxes represent different types of research. Box 1 is the original source of the HSVs, and Box 7 is the end use of the HSVs. The arrows show where outputs from one study type input to other types. The output of any study includes not only uncertainty generated within the study but also uncertainty inherited from studies that input to it. Box 1 is a valuation study (defined earlier) in which stated preference data are collected from a sample of people. Some studies elicit HSVs for disease-related states described in the form of “vignettes” or “scenarios” that describe disease symptoms and their impact on quality of life.<sup> 23 </sup> Others elicit HSVs for states defined by an HDS-V, called “profiles” (see *HDS-V Profile Data*). Typically, a limited number of states are valued, and a value set that covers all states is generated from these by modeling. Box 7 represents the final use of the HSVs in a CEA. Boxes 3, 5, and 6 represent intermediate studies, described below, that process Box 1 HSV data before their use in Box 7. Boxes 2 and 4 represent studies that generate descriptive system data, either HDS or HDS-V, that may also input into Boxes 3, 5, 6, and 7. The headings below (e.g., “Valuation Studies”) link to the <a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> boxes (e.g., “Valuation”).

<figure id="fig1-0272989X251380556">
Diagram: Health Decision Systems flowchart: Steps from HDS-V profile data to cost-effectiveness modelling, including disease states and meta analysis, with uncertainty sources.
<p><img src="10.1177_0272989X251380556-fig1.jpg" /></p>
<p><img src="10.1177_0272989X251380556-fig1.gif" /></p>
<figcaption>Sources of uncertainty in health state values.</figcaption>
</figure>

### Valuation Studies

Valuation studies estimate a population mean HSV for each health state described by a descriptive system or other classification, using a sample representative of a wider population. Typically, this summarizes over a sample the distribution of different individuals’ subjective estimates of values for described health states if they experienced them. It assumes that individuals’ different expressed values result from different underlying preferences, rather than differing precision in value estimation.

Methodological variation arises from the different empirical methods used. For example, in methods that require respondents to choose between different health outcome scenarios, important features include the framing of choices offered, how different scenarios are presented, prompts given, and the choice of health outcomes included. Each study interviewer may conduct the interview and record data differently.

Statistical uncertainty arises from sampling uncertainty and modeling uncertainty. An important aspect of dealing with sampling uncertainty is testing that the sample is representative of a population. This is normally based on externally observable sociodemographic and personal characteristics, for example, age, sex, and experience of ill health. However, what is required is a sample that is representative of the population’s preferences, but the distribution of this over a population is unobserved and therefore unknown. The assumption is therefore that the tested characteristics are the dominant source of variations in preferences.

Assuming a representative sample, sampling uncertainty concerns the precision with which each health state’s population mean HSV is estimated, measured by the SE of the mean. This is normally estimated using the sample standard deviation and the sample size; however, because HSVs are usually estimated using statistical modeling (see below), this is not straightforward.

Modeling uncertainty arises when the mean population HSVs for health states defined by an HDS-V are estimated using regression analysis, for example, estimating coefficients for the severity level within a health domain or dimension.<sup> [^3] </sup> This generates a mean population estimate for each coefficient and an associated SE. However, this does not generate SEs for the mean population HSVs for the health states themselves, although they can be calculated for health states included in the estimation data set. The SEs for other health states can also be estimated, but calculations will depend on both the form of the model and an assumed joint distribution of regression coefficients errors (see the “Discussion” section for an example). Sources of variation arise from both parameter uncertainty and model specification.

### HDS-V Profile Data

A profile is a health state described according to an HDS-V. For example, an EQ-5D-5L profile might be:

> No problems in walking about
>
> Slight problems washing or dressing
>
> Moderate problems doing usual activities
>
> No pain or discomfort
>
> Slightly anxious or depressed

Profile data collection studies aim to estimate a population distribution of observed profiles using a sample representative of a wider population.

Methodological uncertainty again arises from the reliability of the instrument used to capture health states and how data are collected. Studies that do not rely on a person’s estimate of their health state, such as proxy completion, have additional complexities. Proxy and own health state data reliability may differ, an issue where data sets include both.<sup>24,25</sup>

Statistical uncertainty arises from sampling, the precision with which the population distribution for severity levels within each HDS-V dimension is measured. Similar to valuation studies, sampling uncertainty is normally dealt with by testing or assuming that the sample is representative of a population based on sociodemographic and biological characteristics, for example age, sex, and clinical ill-health measures. However, the distributions over people of their subjective perception of severity levels are unobserved and therefore unknown.

### Mapping

Mapping studies generate HSVs for health states defined by an HDS using values attached to equivalent states from an HDS-V.<sup>17,26</sup> It may also be used to convert values between HDS-Vs. Data are usually collected from people who complete questionnaires that identify them on both the HDS and HDS-V. There are two methods for generating HSVs for the HDS. Response mapping generates a correspondence between HDS and the HDS-V health states. An HDS-V value set is applied to the modeled distribution of the HDS. Direct mapping is used where the HDS also has a summary score calculated by applying an algorithm to questionnaire responses. Regression modeling generates HSVs for particular summary scores, which are applied to the HDS’s health states. A special case is where two or more HDS-Vs are mapped. For example, there are mappings between 6 different HDS-Vs<sup> 27 </sup> and between different versions of the EQ-5D.<sup>28,29</sup>

As <a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> shows, mapping uses profile data, other HDS data, and value sets from valuation studies. It inherits all of the uncertainty from these, plus 3 additional sources. First, statistical uncertainty relating to the precision with which the joint distribution of the responses to the HDS and HDS-V that would be observed in the population is measured by that observed in the sample. How representative the sample is of the relevant population can be tested using sociodemographic, biological, and clinical characteristics, but again, the population distribution of severity responses is unknown.

Second, response mapping may have methodological uncertainty. In practice, it does not simply apply the joint distribution of the HDS and the HDS-V but uses rules to ensure consistency. For instance, responses indicating “full health” in one HDS might always be converted to “full health” in another, regardless of the actual response in the latter. How the resulting uncertainty can be quantified is not obvious.

Third, direct mapping will inherit uncertainty from whatever methods or assumptions are used to create the HDS’s summary score algorithm. Similarly, where different HDS-Vs’ value sets are mapped, this inherits uncertainty from both valuation studies used to create them.

### Other HDS Data

All of the uncertainty sources described in 3.2 also apply to HDS self-reported health. If the HDS has a summary score, similar issues to those described in *Valuation Studies* apply.

### Disease State Studies

These studies aim to estimate the value of clinically defined health states according to a particular value set. The usual method is to survey people with specified disease states using an HDS-V and use its value set to calculate the mean value for each state. Some studies use data from patients with one particular condition, such as stroke, coronary artery disease, osteoarthritis, and specific cancers<sup> 30 </sup>; others use data from patients with different conditions collected from sources such as hospital records or health surveys.<sup>31,32</sup> There are catalogues of different studies’ results for, for example, chronic diseases measured by the EQ-5D.<sup>33,34</sup>

As <a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> shows, disease state studies may use profile data and value sets from valuation studies or mapping. Normal sampling variance reflects the selection of data as a sample from a wider population. These HSVs also inherit all uncertainty sources from the profile data collection and from their source (valuation studies, response mapping or other mapping).

A further complication is that the variance of a distribution of HSVs depends not only on the different profile responses that respondents give but also the value set. This variance is a complex weighted sum of both the variances of each response level within every domain or dimension that the HDS-V has and all of the covariances between them, where the weights are the coefficients from the value set.<sup> 35 </sup> The covariance element introduces interactions between coefficients that are not in the value sets themselves. Moreover, the greater the differences between coefficients, the higher the variance.

### Meta-Analysis

In this context, meta-analysis estimates disease state HSVs using data from different disease state studies.<sup> 36 </sup> This inherits all of the uncertainty from the disease state studies plus uncertainty from how different studies’ data are combined.

This is important because many such meta-analyses use aggregate data, in which the weights assigned to different studies’ estimates of the mean are the inverse of their variance. If the different studies’ HSVs are calculated using the same value set, the variances will not be truly independent. As described, variances are determined by the value sets’ coefficients and variance attributable to differences between study patients’ responses. They therefore have a fixed element that may mean that observed differences are smaller than true differences.

### Cost-Effectiveness Modeling

Cost-effectiveness modeling uses HSV data to estimate QALY gains, comparing 1 or more alternative treatments or other health interventions or policies. As <a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> shows, there are multiple possible uncertainty sources depending on how the model defines health states and their attached HSVs. Modeling data may be from a clinical trial that collects HDS or HDS-V data or a clinical disease state measures, with HSV data from a valuation study, mapping, a disease state study, or meta-analysis. There are other uncertainty sources in estimating QALY gains, such as illness duration and survival, but we focus here on HSVs.

- *Clinical trials that include primary HDS-V data.* Where a clinical trial contains patient HDS-V data converted to HSVs, HSV variance, as before, depends on both variations between patients’ profile responses and the coefficients used to calculate HSVs.

- *Clinical trials that do not include primary HDS-V data but include another HDS.* Where clinical trials collect patient HDS data that are converted to HDS-Vs, HSV variance depends on variations between patients’ responses to the HDS and uncertainty from the HDS and HDS-V mapping. Mapping-derived uncertainty includes uncertainty inherited from an HDS-V valuation study and studies used to create the HDS.

- *Clinical data that measure only clinically defined disease states.* The variance depends on variations between patients within and between disease states and on the study, or studies if using meta-analysis data, used to create disease state HSVs. These will include uncertainty inherited from an HDS-V valuation study and may also include mapping uncertainties.

Where SEs or information on HSV distributions are missing, functional form assumptions are commonly made, for example, that HSVs follow a beta distribution.

In summary, HSVs used in cost-effectiveness modeling are the cumulation of a wide range of sources that multiply and combine uncertainty.

## Sources of Uncertainty within Valuation Studies

This section focuses on the HSV uncertainty generated by valuation studies. The other study types in <a href="#fig1-0272989X251380556" data-ref-type="fig">Figure 1</a> add to uncertainty around HSVs used in CEA modeling, but valuation studies are especially important as the HSV uncertainty they produce is always present in such models. <a href="#table1-0272989X251380556" data-ref-type="table">Table 1</a> lists these uncertainty sources. The presentation order broadly reflects the process of a valuation study: study design, eliciting stated preferences, and modeling value sets. In each case, we identify uncertainty sources and how these are currently addressed in methods that generate and report value sets. This is not exhaustive, and the presentation order for uncertainty sources does not necessarily reflect their importance order.

<div id="table1-0272989X251380556" class="table-wrap">

<div class="caption">

Sources of Uncertainty in Values Generated within Valuation Studies

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;">Source of Uncertainty</th>
<th style="text-align: center;">Why Does It Arise?</th>
<th style="text-align: center;">How Is It Evident?</th>
<th style="text-align: center;">How Is It Currently Handled?</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4" style="text-align: left;">1. Arising from <em>study design</em> choices</td>
<td style="text-align: left;">a. Which population’s values are taken into account?</td>
<td style="text-align: left;">Uncertainty about whose values are relevant, for example, the ongoing debate about whether children’s HSVs should be based on adults’ or children’s preferences, which may differ.</td>
<td style="text-align: left;">Differences between HSVs applicable to the same population from different studies.</td>
<td style="text-align: left;">Methodological studies are used to ascertain whether normative choices affect results. Some HTA bodies have clear guidance on whose stated values are relevant, which reduces uncertainty.</td>
</tr>
<tr>
<td style="text-align: left;">b. Choice of sample frame and generalizability of the sample’s values to the population</td>
<td style="text-align: left;">There may be differences in the distribution of values between the sample from which values are obtained and the wider population.</td>
<td style="text-align: left;">Inconsistency between values generated for the same population by different studies.</td>
<td style="text-align: left;">By ensuring that samples are representative of the general public with respect to <em>observable</em> (sociodemographic) characteristics. However, this does not account for residual differences between those who have similar characteristics.</td>
</tr>
<tr>
<td style="text-align: left;">c. Selection of the subset of states for which to seek values and from which value sets are created</td>
<td style="text-align: left;">While some studies have attempted a “saturation” approach to valuing HDS-Vs,<sup> <span class="citation" data-cites="bibr37-0272989X251380556">37</span> </sup> most descriptive systems contain too many health states to make that feasible, so researchers must select a subset of states to value.</td>
<td style="text-align: left;">Which states are selected (and why), their characteristics (e.g., severity), and in what order states are presented may affect the values which are elicited.</td>
<td style="text-align: left;">Use of optimal designs (e.g., in DCEs). Randomization of the order of states in valuation tasks.</td>
</tr>
<tr>
<td style="text-align: left;">d. Prior assumptions about the desired characteristics of values</td>
<td style="text-align: left;">Valuation methods are developed (or data manipulated ex post) to conform to researchers’ prior judgments about, for example, what the minimum value should be (e.g., −1), whether or not values &lt;0 are intended to be generated, and how the anchor of 0 is defined.</td>
<td style="text-align: left;">In the characteristics of values that are produced, such as the length/range of the value scale.</td>
<td style="text-align: left;">These aspects of design are generally clearly reported, but the implications of different choices that could have been made tend not to be highlighted (e.g., to users).</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">2. Arising in the <em>elicitation</em> of values</td>
<td style="text-align: left;">a. Unfamiliarity or lack of engagement with valuation tasks</td>
<td style="text-align: left;">Respondents do not understand or are not properly engaged with valuation tasks and refuse to answer or answer randomly.<br />
Respondents understand and are engaged with the valuation tasks, are unfamiliar with them, so they may: improvise, constructing their preferences, and perhaps learning with each additional task.<br />
• use heuristics to simplify and short-cut responses.<br />
• have different response styles—the manner in which they respond to the stimuli offered by the valuation tasks—which leads to variation in responses.<br />
• make mistakes in undertaking valuation tasks.</td>
<td style="text-align: left;">A respondent’s responses to different health state descriptions or the same description repeated are inconsistent.<br />
There are differences between different respondents who have similar characteristics.<br />
Many missing values or complete failure to complete the tasks.</td>
<td style="text-align: left;">If seen as “poor-quality data,” it is captured by quality control and other ex post rules, for example, excluding logically inconsistent responses.<br />
Variances around observed means are reported but may not be partitioned into different uncertainty sources.<br />
Reporting of missing data.</td>
</tr>
<tr>
<td style="text-align: left;">b. Heterogeneity in preferences</td>
<td style="text-align: left;">Respondents have different preferences for the HSVs; there may be subgroups defined ex ante by characteristics (e.g., sociodemographic, language, or cultural) or identified ex post as different “preference types” or latent classes.</td>
<td style="text-align: left;">These may be associated with individual variation or, where linked to language, cultural or other factors, and be shared with a subgroup of respondents.</td>
<td style="text-align: left;">Differences between groups may be reported.<br />
Some studies address preference heterogeneity using latent class modeling.</td>
</tr>
<tr>
<td style="text-align: left;">c. Valuation methods</td>
<td style="text-align: left;">Different valuation methods yield data with fundamentally different properties.<br />
This applies both to choices between methods but also to specific aspects of the chosen method. In addition, it may be that more than 1 method is used and the results combined.</td>
<td style="text-align: left;">Differences in the characteristics of values that are produced, for example, whether the method has a lower bound value by design.</td>
<td style="text-align: left;">By fully reporting the methods used. Using standardized protocols or similar methods can facilitate interstudy comparability.</td>
</tr>
<tr>
<td style="text-align: left;">d. Mode of administration and interviewer effects</td>
<td style="text-align: left;">Interviewers may have different understanding, diligence, and approaches.<br />
Within both interviewer-led tasks and self-completion valuation tasks, differences in respondent engagement and understanding.</td>
<td style="text-align: left;">Significantly different patterns of data between interviewers.</td>
<td style="text-align: left;">Reporting interviewer effects.<br />
Self-completion engagement and understanding are only crudely measured, for example, time taken per task and choice of the same option in each task.</td>
</tr>
<tr>
<td style="text-align: left;">e. Fraud</td>
<td style="text-align: left;">Where online survey respondents or panel providers or face-to-face interviewers are paid for each questionnaire, there may be an incentive to fabricate data.</td>
<td style="text-align: left;">For online surveys, data quality may be affected, for example, speed of completion using bots.</td>
<td style="text-align: left;">Checks and preventive measures are used to ensure online responses are not from bots, such as Captcha and honeypots.</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">3. Arising in the <em>modeling</em> of valuation data</td>
<td style="text-align: left;">a. Which summary measure of values is used for modeling?</td>
<td style="text-align: left;">The choice of summary measure of values, such as mean, trimmed mean, or median, will affect results. Although it is largely a technical judgment, it may also involve a value judgement.<sup> <span class="citation" data-cites="bibr38-0272989X251380556">38</span> </sup></td>
<td style="text-align: left;">Differences between mean and median in values for the subset of states included in a study. The effect of excluding “outliers,” which has a greater effect on the mean than the median.</td>
<td style="text-align: left;">Few valuation studies report results from different possible summary measures.</td>
</tr>
<tr>
<td style="text-align: left;">b. Valuation modeling and interpolation across the descriptive system</td>
<td style="text-align: left;">Decisions about how to model valuation data, for example, the number of parameters included; the use and interpretation of a constant term; the inclusion or not of interaction effects.</td>
<td style="text-align: left;">Different coefficients and value sets with different models using the same data.</td>
<td style="text-align: left;">Alternative models are estimated. Their overall statistical performance is reported, and criteria for choosing the final model are sometimes stated.<br />
The properties of the <em>values</em> of the value sets and particularly how they compare to those of alternative value sets are underreported. The variance around <em>estimated coefficient</em>s is reported, but there is no guidance available on how to combine these to calculate variance around the <em>values contained in value sets</em>.</td>
</tr>
<tr>
<td style="text-align: left;">c. Model misspecification</td>
<td style="text-align: left;">No model fitted to the data will be “correct,” and therefore, there is some model misspecification.</td>
<td style="text-align: left;">Model misspecification shows up as uncertainty in the value set. Evidence suggests this may be far larger than the uncertainty in the regression coefficients of whatever model is fitted.<sup> <span class="citation" data-cites="bibr12-0272989X251380556">12</span> </sup></td>
<td style="text-align: left;">Not usually reported</td>
</tr>
</tbody>
</table>

DCE, discrete choice experiment; HDS-V, health state descriptive system with a value set; HSV, health state values; HTA, health technology assessment.

</div>

According to the earlier classification of uncertainty sources, only 1 section (1b) refers to variability and heterogeneity, 4 refer to statistical uncertainty (2b, 2c, 3b, 3c), and 8 refer to methodological uncertainty (1a, 1c, 1d, 2a, 2d, 3a, 3b, 3c). This reflects how this list was devised rather than suggesting greater importance or prevalence of different uncertainty sources. However, it suggests that methodological uncertainty and how to deal with it is less understood than other types and deserves more attention. By contrast, there is a large body of knowledge from general statistical and econometric theory and practice to handle statistical uncertainty.

The list illustrates the multiple uncertainty sources in each step of a valuation study. Specific design features of valuation tasks, for example, whether HSVs \< 0 are sought and what minimum value is possible, will affect the characteristics of the resulting HSVs. The designs of valuation studies include linked statistical choices concerning which HDS-V states to include, how many choices each participant can reasonably undertake, and sample size—all of which generate statistical uncertainty. There are also normative considerations regarding whose HSVs are considered relevant. For example, in the valuation of adults’ health states, there is ongoing debate about whether to use general population or patient HSVs and, in the valuation of pediatric health states, whether to use adult or children’s HSVs. Different populations may have different HSVs,<sup>39–43</sup> so where such issues are unresolved, for example, where decision makers lack a clear view, researchers’ sample choices will determine the HSVs’ characteristics.

A fundamental issue of both study design and data collection is how stated preferences are elicited. There is no health economics consensus about which stated preference method is “best” or about which criteria should determine choice of methods, although preferred methods are stated in some countries’ health technology assessment agency guidelines.<sup> 44 </sup> Different methods produce HSVs with different characteristics.<sup>45–49</sup> Valuation studies usually select and report HSVs from one method selected ex ante, rather than reporting how much HSVs might differ by using different methods.

Data analysis methods vary between studies. For example, HSVs cannot take a value greater than 1, meaning “full health,” but they may take negative values, with no theoretically defined lowest value, which may lead to problems of interpretability of the resulting data. This issue is commonly dealt with by transforming or truncating data; how this is done varies. An important uncertainty source is that, except for a small number of studies using a “saturation” design, value set generation entails estimating HSVs for all HDS-V states from directly observed HSVs for a subset. Uncertainty exists around both the parameters within the selected model and its specification.

<a href="#table1-0272989X251380556" data-ref-type="table">Table 1</a> describes efforts made to address some uncertainty sources by, for example, improved study designs, standardized protocols, processes to identify poor-quality data, and modeling methods. However, the way value sets are currently reported to users reflects little of the associated uncertainty.

## Discussion

The issue of HSVs uncertainty is important and more complex than usually acknowledged. The question is how we can improve methods for measuring and reporting it.

Some aspects are easy to deal with. For example, as discussed earlier, the SEs of level and dimension coefficients from regression modeling used to generate EQ-5D HSVs are widely reported, but what would be required for use in CEA are the SEs for HSVs attached to profiles. These can be calculated using the regression model’s variance/covariance matrix (VCM), but this is rarely if ever reported by valuation studies. We showed how to do this<sup> 5 </sup> using data from the influential Measurement and Valuation of Health study<sup> 50 </sup> by generating a variance/covariance matrix and calculating SEs for every possible EQ-5D-3L profile’s HSV. The SEs range from 0.008171 to 0.012203, which are small compared with the HSVs’ range, from −0.594 to 1.

This relatively small range is evidence of how robust this study’s HSVs are, resulting from a strong research design and a large sample. In studies with greater variances, for example with a small sample and a less constrained range of possible HSVs, the relative size of the SEs may be significantly larger. We therefore recommend that where relevant either the SEs attached to HSVs for health states should be reported or the VCM so that those HSVs can be derived.

Other uncertainty aspects may be harder to conceptualize and measure. But without a full account of uncertainty and the availability of methods for identifying and reporting it, value sets for HDS-Vs published in journals and books will continue to provide incomplete information about it. It will remain difficult for users to incorporate HSV uncertainty into both cost-effectiveness models and other applications of HSVs, for example, summarizing population health survey data.

Jurisdictions with well-established HTA processes that routinely use cost-effectiveness evidence may have available a local value set for each HDS-V and a preferred HDS-V. Where there are alternative acceptable value sets and it is unclear which to use, a deterministic sensitivity analysis of HSVs may suffice. However, as value sets reporting does not adequately cover HSVs uncertainty, a proper sensitivity analysis of them is precluded. Nevertheless, the processes for generating average HSVs yield valuable information on uncertainty, which may be underreported. HDS-V developers, such as the EuroQol Group, have a responsibility to better support value set users by providing more complete information about them.

Despite much work reporting methods for estimating HSVs, limited information is available about the associated uncertainty. For example, no studies reporting value sets for the EQ-5D-5L<sup> 21 </sup> or -3L<sup> 51 </sup> report uncertainty information for the estimated health state profile HSVs. To our knowledge, this also applies to other reported HDS-V value sets.<sup>22,52</sup> Value set users lack relevant evidence and have limited ways to test QALY and ICER estimation implications.

Clinical, ethical, social, economic, and political perspectives support medical decision making that takes account of people’s preferences by using HSVs. Our analysis aims to strengthen that by improving the confidence that we can place in estimates of them. We therefore recommend the following:

- Clinical trial researchers, decision modelers, and health care decision makers should recognize and account for uncertainty more extensively than is currently practiced.

- HSV studies should fully report information on uncertainty; best practice guidelines should include this issue.

- Researchers should find solutions for unresolved issues of handling uncertainty.

## Conclusions

Despite more than 50 years of research on HSVs, limited attention has been given to identifying all sources of uncertainty around them and developing methods to quantify and report them. Consequently, HSV uncertainty is not adequately reflected in QALY estimates or CEAs based on them. We described multiple sources of uncertainty that affect the elicitation and modeling of value sets and showed that HSV uncertainty affects CEA in complex ways, especially where HSVs are inputs to mapping exercises and meta-analyses, where uncertainty combines at each step. Health state valuation studies should advance beyond providing point estimates and include detailed accounts of HSV uncertainty to better serve their users.

## Acknowledgments

We thank the members of a study advisory group for their detailed input: Nigel Rice, Ben van Hout, Bas Janssen, Eleanor Pullenayegum, Bram Roudijk, and Mark Sculpher. We thank participants in a discussion of a EuroQol Group conference paper on this topic, in particular our discussant Michał Jakubczyk. David Parkin, Nancy Devlin, and Andrew Lloyd are members of the EuroQol group, but the views expressed in this article are those of the authors and not necessarily those of the EuroQol Research Foundation, who funded this study.

## Footnotes

## Contributor Information

David Parkin, City St George’s, University of London, London UK; Office of Health Economics, London UK.

Andrew Briggs, London School of Hygiene and Tropical Medicine, London UK.

Giselle Abangma, London School of Hygiene and Tropical Medicine, London UK.

Andrew Lloyd, London School of Hygiene and Tropical Medicine, London UK.

Nancy Devlin, Melbourne School of Population of Global Health, University of Melbourne, Australia.

## References

## References

1. Briggs A, Claxton K, Sculpher M. Decision Modelling for Health Economic Evaluation. Oxford (UK): Oxford University Press; 2006.

2. Tew M, Willis M, Asseburg C, et al. Exploring structural uncertainty and impact of health state utility values on lifetime outcomes in diabetes economic simulation models: findings from the ninth Mount Hood Diabetes Quality-of-Life Challenge. Med Decis Making. 2022;42(5):599–611. DOI: 10.1177/0272989X211065479

3. Brazier J, Ara R, Azzabi R, et al. Identification, review, and use of health state utilities in cost-effectiveness models: an ISPOR good practices for outcomes research task force report. Value Health. 2019;22:267–75. DOI: 10.1016/j.jval.2019.01.004

4. Ara R, Wailoo AJ. NICE DSU technical support document 12: the use of health state utility values in decision models. 2011. Available from: https://www.sheffield.ac.uk/nice-dsu/tsds/utilities

5. Devlin NJ, Abangma G, Lloyd A, Parkin D, Briggs A. Reporting uncertainty around health-state values: a standard method and worked example. Value Health. 2025;28(2):191–6. DOI: 10.1016/j.jval.2024.11.010

6. Lenert L, Kaplan RM. Validity and interpretation of preference-based measures of health-related quality of life. Med Care. 2000;38:Ii138–50. doi:10.1097/00005650-200009002-00021

7. Whately-Smith C, Watkins C, Mann H, Fletcher C, Ducournau P. Utility values in health technology assessments: a statistician’s perspective. Pharm Stat. 2014;13:184–95. DOI: 10.1002/pst.1616

8. Kharroubi SA, Beyh Y. The importance of accounting for the uncertainty around the preference-based health-related quality-of-life measures value sets: a systematic review. J Med Econ. 2019;22:671–83. doi:10.1080/13696998.2019.1592178

9. Devlin N, Finch A, Parkin D. Guidance to users of EQ-5D-5L value sets. In: Devlin N, Ludwig K, Roudijk B. eds. Value Sets for EQ-5D-5L: A Compendium, Comparative Review and User Guide. New York (NY: ): Springer; 2021.

10. Abangma, et al. Methods for Capturing and Reporting Uncertainty around HRQoL Values: A Scoping Review. Health Economics, forthcoming; Epub ahead of print 2025.

11. Pullenayegum EM, Chan KW, Xie F. Quantifying parameter uncertainty in EQ-5D-3L value sets and its impact on studies that use the EQ-5D-3L to measure health utility: a Bayesian approach. Med Decis Making. 2016;36:223–33. DOI: 10.1177/0272989x15591966

12. Chan KK, Xie F, Willan AR, Pullenayegum EM. Underestimation of variance of predicted health utilities derived from multiattribute utility instruments. Med Decis Making. 2017;37:262–72. DOI: 10.1177/0272989x16650181

13. Poulimenos S, Round J, Baio G. Capturing valuation study sampling uncertainty in the estimation of health state utility values using the EQ-5D-3L. Med Decis Making. 2024;44(4):393–404. DOI: 10.1177/0272989x241239899

14. Drummond MF, Sculpher M, Claxton K, Stoddart G, Torrance G. Methods for the Economic Evaluation of Health Care Programmes. Oxford (UK): Oxford Medical Publications; 2015.

15. Robinson A, Parkin D. Recognising diversity in public preferences: the use of preference sub-groups in cost-effectiveness analysis. A response to Sculpher and Gafni. Health Econ. 2002;11(7):649–51; discussion 653-4. DOI: 10.1002/hec.735

16. Versteegh MM, Brouwer WBF. Patient and general public preferences for health states: a call to reconsider current guidelines. Soc Sci Med. 2016;165:66–74. DOI: 10.1016/j.socscimed.2016.07.043

17. Mortimer D, Segal L. Comparing the incomparable? A systematic review of competing techniques for converting descriptive measures of health status into QALY-weights. Med Decis Making. 2008;28(1):66–89. DOI: 10.1177/0272989X07309642

18. Danish Medicines Council. The Danish Medicines Council methods guide for assessing new pharmaceuticals. 2021. Available from: https://medicinraadet-classic.azureedge.net/media/5eibukbr/the-danish-medicines-council-methods-guide-for-assessing-new-pharmaceuticals-version-1-3.pdf

19. National Institute for Health and Care Excellence. NICE health technology evaluations: the manual. NICE process and methods [PMG36]; 2022. Available from: www.nice.org.uk/process/pmg36/chapter/economic-evaluation#measuring-and-valuing-health-effects-in-cost-utility-analyses

20. National Health Care Institute. Guideline for economic evaluations in healthcare; 2024. Available from: english.zorginstituutnederland.nl/publications/reports/2024/01/16/guideline-for-economic-evaluations-in-healthcare

21. Devlin N, Roudijk B, Ludwig K, eds. Value Sets for EQ-5D-5L: A Compendium, Comparative Review & User Guide. Cham (Switzerland): Springer; 2022.

22. Mulhern BJ, Bansback N, Norman R, Brazier J; SF-6Dv2 International Project Group. Valuing the SF-6Dv2 classification system in the United Kingdom using a discrete-choice experiment with duration. Med Care. 2020;58(6):566–73. DOI: 10.1097/mlr.0000000000001324

23. Matza LS, Stewart KD, Lloyd AJ, Rowen D, Brazier JE. Vignette-based utilities: usefulness, limitations, and methodological recommendations. Value Health. 2021;24(6):812–21. DOI: 10.1016/j.jval.2020.12.017

24. Hutchinson C, Khadka J, Crocker M, et al. Examining interrater agreement between self-report and proxy-report responses for the Quality of Life-Aged Care Consumers (QOL-ACC) instrument. J Patient Rep Outcomes. 20248(1):28. DOI: 10.1186/s41687-024-00705-z

25. Khanna D, Khadka J, Mpundu-Kaambwa C, et al. An investigation of inter-rater and intra-proxy agreement in measuring quality of life of children in the community using the EQ-5D-Y-3L. Pharmacoeconomics. 2024;42(suppl 1):113–28. DOI: 10.1007/s40273-024-01356-0

26. Dakin H, Abel L, Burns R, Yang Y. Review and critical appraisal of studies mapping from quality of life or clinical measures to EQ-5D: an online database and application of the MAPS statement. Health Qual Life Outcomes. 2018;16:31. DOI: 10.1186/s12955-018-0857-3

27. Chen G, Khan MA, Iezzi A, Ratcliffe J, Richardson J. Mapping between 6 multiattribute utility instruments. Med Decis Making. 2016;36(2):160–75. DOI: 10.1177/0272989X15578127

28. van Hout B, Janssen MF, Feng YS, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15(5):708–15. DOI: 10.1016/j.jval.2012.02.008

29. Hernández Alava M, Pudney S, Wailoo A. Estimating the relationship between EQ-5D-5L and EQ-5D-3L: results from a UK population study. Pharmacoeconomics. 2023;41:199–207. DOI: 10.1007/s40273-022-01218-7

30. Dyer MT, Goldsmith KA, Sharples LS, Buxton MJ. A review of health utilities using the EQ-5D in studies of cardiovascular disease. Health Qual Life Outcomes. 2010;8:13. DOI: 10.1186/1477-7525-8-13

31. Sullivan PW, Ghushchyan V. Preference-based EQ-5D index scores for chronic conditions in the United States. Med Decis Making. 2006;26(4):410–20. DOI: 10.1177/0272989X06290495

32. Falk Hvidberg M, Hernández Alava M. Catalogues of EQ-5D-3L health-related quality of life scores for 199 chronic conditions and health risks for use in the UK and the USA. Pharmacoeconomics. 2023;41(10):1287–388. DOI: 10.1007/s40273-023-01285-4

33. van Wilder L, Rammant E, Clays E, Devleesschauwer B, Pauwels N, De Smedt D. A comprehensive catalogue of EQ-5D scores in chronic disease: results of a systematic review. Qual Life Res. 2019;28(12):3153–61. DOI: 10.1007/s11136-019-02300-y

34. Zhou T, Guan H, Wang L, Zhang Y, Rui M, Ma A. Health-related quality of life in patients with different diseases measured with the EQ-5D-5L: a systematic review. Front Public Health. 2021;29:675523. DOI: 10.3389/fpubh.2021.675523

35. Parkin D, Rice N, Devlin N. Statistical analysis of EQ-5D profiles: does the use of value sets bias inference? Med Decis Making. 2010;30(5):556–65. DOI: 10.1177/0272989x09357473

36. Petrou S, Kwon J, Madan J. A practical guide to conducting a systematic review and meta-analysis of health state utility values. Pharmacoeconomics. 2018;36(9):1043–61. DOI: 10.1007/s40273-018-0670-1

37. Santos M, Cintra MA, Monteiro AL, et al. Brazilian valuation of EQ-5D-3L health states: results from a saturation study. Med Decis Making. 2016;36(2):253–63. DOI: 10.1177/0272989X15613521

38. Devlin N, Shah K, Buckingham K. What Is the Normative Basis for Selecting the Measure of ‘Average’ Preferences for Use in Social Choices? OHE Research Paper 17/01. London (UK): Office of Health Economics; 2017. Available from: https://www.ohe.org/publications/what-normative-basis-selecting-measure-average-preferences-use-social-choices/

39. Lundberg L, Johannesson M, Isacson D, Borgquist L. Health-state utilities in a general population in relation to age, gender and socioeconomic factors. Eur J Public Health. 1999;9(3):211–17. DOI: 10.1093/eurpub/9.3.211

40. Craig BM, Reeve BB, Cella D, Hays RD, Pickard AS, Revicki DA. Demographic differences in health preferences in the United States. Med Care. 2014;52(4):307–13. DOI: 10.1097/MLR.0000000000000066

41. Feng Y, Herdman M, van Nooten F, et al. An exploration of differences between Japan and two European countries in the self-reporting and valuation of pain and discomfort on the EQ-5D. Qual Life Res. 2017;26(8):2067–78. DOI: 10.1007/s11136-017-1541-5

42. Roudijk B, Donders ART, Stalmeier PFM; Cultural Values Group. Cultural values: can they explain differences in health utilities between countries? Med Decis Making. 2019;39(5):605–16. DOI: 10.1177/0272989X19841587

43. van Dongen JM, van Hooff ML, Finch AP, et al. Do socio-demographic characteristics and/or health status explain the magnitude of differences between patient and general public utility values? A chronic low back pain patients case study. Health Qual Life Outcomes. 2019;17:166. DOI: 10.1186/s12955-019-1240-8

44. Rowen D, Azzabi Zouraq I, Chevrou-Severac H, van Hout B. International regulations and recommendations for utility data for health technology assessment. Pharmacoeconomics. 2017;35(suppl 1):11–19. DOI: 10.1007/s40273-017-0544-y

45. Dolan P, Gudex C, Kind P, Williams A. Valuing health states: a comparison of methods. J Health Econ. 1996;15(2):209–31. DOI: 10.1016/0167-6296(95)00038-0

46. Bleichrodt H, Johannesson M. Standard gamble, time trade-off and rating scale: experimental results on the ranking properties of QALYs. J Health Econ. 1997;16:155–75. DOI: 10.1016/s0167-6296(96)00509-7

47. Robinson A, Dolan P, Williams A. Valuing health status using VAS and TTO: what lies behind the numbers? Soc Sci Med. 1997;45:1289–97. DOI: 10.1016/S0277-9536(97)00057-9

48. Shiroiwa T, Ikeda S, Noto S, et al. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5): 648–54. DOI: 10.1016/j.jval.2016.03.1834

49. Lipman SA, Brouwer WBF, Attema AE. What is it going to be, TTO or SG? A direct test of the validity of health state valuation. Health Econ. 2020;29:1475–81. DOI: 10.1002/hec.4131

50. MVH Group. The Measurement and Valuation of Health. Final Report on the Modelling of Valuation Tariffs. York (UK): Centre for Health Economics, University of York; 1995. Available from: https://www.york.ac.uk/media/che/documents/reports/MVH%20Final%20Report.pdf

51. Szende A, Oppe M, Devlin N. EQ-5D Value Sets: Inventory, Comparative Review & User Guide. New York (NY): Springer; 2007.

52. Feeny D, Furlong W, Torrance GW, et al. Multiattribute and single-attribute utility functions for the health utilities index mark 3 system. Med Care. 2002;40(2):113–28. DOI: 10.1097/00005650-200202000-00006

[^1]: We use “values” instead of “weights” or “scores” to identify that they are based on people’s preferences and instead of “utilities,” which refers to HSVs that conform to probabilistic choice theories such as expected utility and random utility.

[^2]: This type of HDS is sometimes incorrectly referred to as a “preference-based measure,” but that description properly applies only to the HSVs attached to an HDS, not the HDS itself, which has no basis in preferences.

[^3]: Where the HSVs may legitimately be regarded as utilities, this is known as a multiattribute utility model.
