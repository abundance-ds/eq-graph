---
project_id: "237-RA"
work_id: "doi:10.1007/s10198-023-01612-8"
doi: "10.1007/s10198-023-01612-8"
pmid: "37420133"
pmcid: "PMC11136812"
title: "The effect of duration and time preference on the gap between adult and child health state valuations in time trade-off"
journal: "The European Journal of Health Economics"
publication_date: "2023-07-08"
volume: "25"
issue: "4"
authors:
  - name: "Zhongyu Lang"
    orcid: "http://orcid.org/0000-0002-2399-6942"
    affiliation_ids:
      - "Aff1"
  - name: "Arthur E. Attema"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Stefan A. Lipman"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/057w15z03grid.6906.90000 0000 9262 1349Erasmus Centre for Health Economics Rotterdam (EsCHER), Erasmus School of Health Policy and Management (ESHPM), Erasmus University, P.O. Box 1738, 3000 DR Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "https://ror.org/057w15z03grid.6906.90000 0000 9262 1349Erasmus School of Health Policy and Management, Erasmus University, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "Erasmus Centre for Health Economics Rotterdam, Rotterdam, The Netherlands"
keywords:
  - "EQ-5D-Y"
  - "I10"
  - "QALY model"
  - "Time preference"
  - "Time trade-off"
licence: "cc-by"
source_file: "input/projects/237-RA/papers/doi_10.1007_s10198-023-01612-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11136812/fullTextXML"
source_method: "epmc_xml"
source_sha256: "ce0f554e8bc7a7711ceee5310c780d9b4ab2bab912610dc2662bb4a47039bb14"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The effect of duration and time preference on the gap between adult and child health state valuations in time trade-off

## Abstract

Composite time trade-off (cTTO) utilities have been found to be higher when adults value health states for children than for themselves. It is not clear if these differences reflect adults assigning truly higher utilities to the same health state in different perspectives, or if they are caused by other factors, which are not accounted for in the valuation procedure. We test if the difference between children’s and adults’ cTTO valuations changes if a longer duration than the standard 10 years is used. Personal interviews with a representative sample of 151 adults in the UK were conducted. We employed the cTTO method to estimate utilities of four different health states, where adults considered states both from their own and a 10-year-old child’s perspective, for durations of 10 and 20 years. We corrected the cTTO valuations for perspective-specific time preferences in a separate task, again for both perspectives. We replicate the finding that cTTO utilities are higher for the child perspective than for the adult perspective, although the difference is only significant when controlling for other variables in a mixed effects regression. Time preferences are close to 0 on average, and smaller for children than adults. After correcting TTO utilities for time preferences, the effect of perspective is no longer significant. No differences were found for cTTO tasks completed with a 10- or 20-year duration. Our results suggest that the child–adult gap is partially related to differences in time preferences and, hence, that correcting cTTO utilities for these preferences could be useful.

## Introduction

The valuation of health states is an important prerequisite for the implementation of health economic evaluations of new drugs and medical treatments. Researchers are showing increasing interest in extending this methodology to valuing children’s health states \[1, 2\]. A separate instrument has been developed for this purpose by the EuroQol Group, known as EQ-5D-Y-3L \[3, 4\], for which a valuation protocol has been published recently \[5\]. The EQ-5D-Y-3L instrument describes health according to 5 dimensions: mobility, looking after oneself, doing usual activities, pain, or discomfort, and feeling worried, sad, or unhappy. Each of them includes 3 levels of severity (level 1 indicating no problems, level 2 some problems, and level 3 a lot of problems). For example, someone with some problems walking about, no problems with looking after oneself, some problems with doing their usual activities, a lot of pain or discomfort, and not feeling worried, sad, or unhappy, is classified as being in health state 21231.

The EQ-5D-Y-3L classification system has been widely used in measuring children’s health states \[6–8\]. Yet, an area of ongoing discussion is the perspective that is used for valuation of EQ-5D-Y-3L health states \[9, 10\]. Its valuation protocol asks adult respondents to value health states considering the life of a 10-year-old child, rather than adults valuing hypothetical health states for themselves, which has been conventional for other EQ-5D instruments. Note that, henceforth, we will refer to these two perspectives as *child perspective* and *adult perspective*.

The EQ-5D-Y-3L valuation protocol recommends the use of the time trade-off (TTO) method to assess utilities in the EQ-5D-Y-3L instrument (as well as discrete choice experiments). The TTO method elicits utilities for health states by asking respondents how many years in full health is equivalent to 10 years in a specified imperfect health state, according to the EQ-5D-Y-3L. The corresponding utility of this health state is then estimated to be equal to y/10, with y being the number of years in full health making the respondents indifferent.

Recent work has found differences in TTO utilities for the same health states when valued from different perspectives \[11, 12\]. In particular, some studies found that TTO utilities elicited with adult perspectives are lower than those elicited with child perspectives \[11, 13\]. However, current evidence is not very robust. Some studies reported no or only a small difference \[14–16\], while another study found differences in both directions \[17\]. Although collectively these studies clearly suggest effects of perspectives may occur, it is unclear why. One explanation for a perspective effect may be the unrealistically short life duration of 10 years of the TTO task. That is, the 10 years in imperfect health (followed by death) respondents are asked to consider imply a large reduction in lifespan compared to the actuarial life expectancy of most adult respondents and the more so for children. Earlier work for adults has shown that beliefs about life expectancy \[18–20\] and the importance assigned to longevity may explain the reluctance to trade life duration, and Lipman \[21\] explored if such beliefs also affect TTO utilities elicited with child perspectives but found little to no evidence. The motivation of the present study was to explore the effect of TTO durations more directly, by extending the life duration considered in both perspectives by 10 years. In absolute terms, such an extension in life duration is equal in both perspectives. Yet, the extension in life duration is (proportionally) much larger in a child perspective than when adults value their own health. For example, for a 40-year-old adult, 10 extra years in a TTO task are an increase equal to 25% of their current age, whereas for a 10-year-old child, the extension equals 100%. In this study, we explore if these differences in relative life extensions yield differential effects in adult and child perspectives.

There is substantial evidence that utilities obtained with a TTO task depend on the gauge duration used, implying a violation of the constant proportional trade-off (CPTO) property \[22\], albeit there is mixed evidence on the direction of this relation. Some studies found utilities to be increasing with a longer duration \[23, 24\], others found a decreasing \[25–28\], or mixed pattern \[29\], while still others did not find a violation of CPTO \[30, 31\]. These studies, however, have all been performed from the adult perspective. Predicting the exact direction on TTO utilities elicited with a child perspective is therefore not straightforward. For example, extending the duration of TTO tasks by 10 years allows respondents to trade-off more years whilst still making sure children reach adulthood and, hence, might make this perspective more comparable to the adult perspective for longer durations. However, when extending durations in TTO, it is important to consider disadvantages of longer durations. One important disadvantage is that longer durations introduce more potential for distortion by time preferences \[31–34\]. This distortion need not be equal between adult and child perspectives: some studies found time preferences for someone else’s health or money to differ from time preferences for our own health or money \[16, 35, 36\].

The aims of our study are therefore to investigate how duration and time preferences affect (the difference between) TTO valuations with child and adult perspectives. To this end, we elicit health state utility by means of a TTO task using two durations, i.e., the standard 10-year timeframe, and a longer timeframe of 20 years for both perspectives. In addition, we estimate time preferences for both these perspectives, and we use these estimates to investigate the effect of perspective-specific time preferences on TTO utilities.

## Method

### Time tradeoff method

We denote a chronic health state q that lasts for t years by (t,q). The TTO method assigns a utility u(q) to q by asking a respondent to compare x years in q to y years in full health (FH), where x is usually set equal to 10. TTO involves a series of choices through which we search the value for y such that (q,x) ~ (FH,y), where ~ denotes indifference. According to the general QALY model \[37\], this indifference is represented as follows:

<div id="Equ1" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{H}}\left( {\text{q}} \right)*{\text{L}}\left( {\text{x}} \right) = {\text{ H}}\left( {{\text{FH}}} \right)*{\text{L}}\left( {\text{y}} \right).$$\end{document}
```

</div>

Here, L(t) is the utility of life duration, and H(q) is the utility of health state q. The common scaling for H(q) is to set H(FH) = 1, and for L(t) to set L(0) = 0 and L(T) = 1, with T the final period under consideration. Solving for H(q) yields:

<div id="Equ2" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{H}}\left( {\text{q}} \right) = {\text{L}}\left( {\text{y}} \right)/{\text{L}}\left( {\text{x}} \right).$$\end{document}
```

</div>

If someone prefers immediate death over (q,x), then the health state is classified as worse than dead (WTD). This requires a modified TTO approach, and in valuation of EQ-5D instruments typically the composite TTO (cTTO) is used for this purpose \[34\]. In this procedure, WTD health states are valued by adding 10 years in full health to the 10 years in state considered WTD (i.e., 10 years lead-time). More generally, this entails that the x years in q are preceded by a lead time of z years in FH \[38\]). The indifference (FH,z;q,x) ~ (FH,y) obtained by this procedure is evaluated by:

<div id="Equ3" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{H}}\left( {\text{q}} \right) = \left[ {{\text{L}}\left( {\text{y}} \right) - {\text{L}}\left( {\text{z}} \right)} \right]/\left[ {{\text{L}}\left( {{\text{x}} + {\text{z}}} \right) - {\text{L}}\left( {\text{z}} \right)} \right].$$\end{document}
```

</div>

In case of the linear QALY model, L(t) = t, and Eq. (<a href="#Equ2" data-ref-type="disp-formula">2</a>) reduces to H(q) = y/x while Eq. (<a href="#Equ3" data-ref-type="disp-formula">3</a>) becomes H(q) = (y–z)/x. In the typical cTTO task with a 10-year duration and a 10-year lead time for WTD states, the linear QALY model implies y/10, and (y-10)/10 for better than dead and WTD states, respectively. In this study we consider an extension of cTTO by 10 years, whilst maintaining the 10-year lead-time, which gives: y/20 and (y-10)/20, respectively. The duration of 20 years was chosen to be a substantial increase compared to 10 years, while still being a realistic life expectancy for most respondents in a general public sample. Moreover, we opted for a fixed duration within the entire sample instead of an individual-specific gauge duration, such as the respondent’s subjective or actuarial life expectancy, because the latter would create a lot of heterogeneity, making the results harder to compare.

In order to have a fair comparison between the durations, the 10- and 20-year TTOs would need to have the same utility range of −1 to + 1; therefore, a lead time of 20 years would have to be used in the 20-year TTO, which would result in a total horizon of 40 years. Because this is unrealistic for part of the general public, we instead use a 10-year lead time for the 20-year TTO as well. This means the lowest attainable (uncorrected) utility for this task is − 0.5, vs. − 1.0 for the 10-year TTO (i.e., if one would still prefer immediate death to living 10 years in full health followed by 20 years in health state X, the cutoff value for the uncorrected TTO weight would result from: 10\*1 + 20\*X \< 0, so X would be set to X = −10/20 = −0.5). Still, we think that the benefits of more realism outweigh the costs in terms of decreased comparability, since the use of a 10-year lead time in both tasks increases similarity in the WTD task. To test the effect of these different ranges, we perform a robustness analysis where all utilities of the 10-year condition are censored at −0.5.

### Time preference

In order to estimate H(q) from Eq. (<a href="#Equ2" data-ref-type="disp-formula">2</a>), we first need a measure of L(t) or make assumptions about its shape. We use the direct method \[39\] for this purpose, which has been used to measure time preferences in the context of TTO in several previous studies \[40–44\]. The advantages of this method are that it is not distorted by risk, does not need to make parametric assumptions about the shape of the discount function, and that it uses a similar context as a TTO task (i.e., quality-of-life improvements, for which we can use the same health states as in the TTO task) \[39\]. In this method, respondents are asked to compare two health profiles, each consisting of the same two health states, but experienced in a different order. One profile (A) starts with a good health state (γ) and ends with a poorer health state (β), whilst the other profile (B) starts with the poorer health state and ends with good health. The starting and ending periods of the health profiles are identical (T = 30 years), as is the period in which the health state changes. We used a total timeframe of 30 years because it was the maximum duration in the 20-year TTO task (i.e., in the case the WTD procedure with a 10-year-lead time was started). Figure <a href="#Fig1" data-ref-type="fig">1</a> illustrates the task by means of a screenshot of one of the questions in this task. In Profile A, the respondent first lives in full health for 15 years, followed by 15 years in State X. In Profile B, the order of these states is reversed and the respondent first lives in State X for 15 years, followed by 15 years in full health. The respondents were instructed that after this total of 30 years, there was no difference between the two profiles anymore, but the state itself was not specified.

<figure id="Fig1">
<p><img src="10198_2023_1612_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Screenshot of a time preference task</figcaption>
</figure>

Intuitively, respondents must trade off the onset of the poor health state with its duration. In case of positive discounting, an individual will prefer to start with the good health state and postpone the poor health state. Hence, such an individual will choose Profile A in the first question. In the next question, the amount of time spent in full health is then lowered in Profile A, say to 8 years, whilst the amount of time spent in poor health that follows afterward increases automatically (to 30 − 8 = 22 years). The reverse happens for Profile B, where the amount of time spent in poor health decreases to 8 years and the amount of time spent in full health increases toward 22 years. As such, Profile B has become more attractive, and even respondents with a positive discount rate may prefer it now. Only those respondents with a sufficiently high discount rate keep on preferring Profile A because of its earlier onset of the episode in full health (and, equivalently, the later onset of the episode in poor health). As elaborated further in the discussion section, drawbacks of this method are, inter alia, that it may be distorted by a sequence effect, which holds that respondents could be inclined to choose Profile B because they do not like the anticipation of a decline in their health in the future. Additionally, as in most other methods, respondents could use some heuristics, such as maximizing the time spent in full health.

In formal terms, Profile A is denoted by (\[t<sub>0</sub>,t<sub>0.5</sub>\], γ; \[t<sub>0.5</sub> + 1,T\], β) and Profile B is denoted by (\[t<sub>0</sub>,t<sub>0.5</sub>\], β; \[t<sub>0.5</sub> + 1,T\], γ), where t<sub>0</sub> is the starting point of the considered episode (year 0 in Fig. <a href="#Fig1" data-ref-type="fig">1</a>) and T is the end point (year 30). The time point t<sub>0.5</sub> is looked for, such that the respondent is indifferent between the two profiles: (\[t<sub>0</sub>,t<sub>0.5</sub>\], γ; \[t<sub>0.5</sub> + 1,T\], β) ~ (\[t<sub>0</sub>,t<sub>0.5</sub>\], β; \[t<sub>0.5</sub> + 1,T\], γ). In the general QALY model, this indifference is represented as follows:

<div id="Equ4" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\left[ {{\text{L}}\left( {{\text{t}}_{0.{5}} } \right) - {\text{L}}\left( {{\text{t}}_0 } \right)} \right]*{\text{H}}(\gamma ) \, + \, \left[ {{\text{L}}\left( {\text{T}} \right) - {\text{ L}}\left( {{\text{t}}_{0.{5}} } \right)} \right]*{\text{H}}(\beta ) \, = \, \left[ {{\text{L}}\left( {{\text{t}}_{0.{5}} } \right) - {\text{L}}\left( {{\text{t}}_0 } \right)} \right]*{\text{H}}(\beta ) \, + \, \left[ {{\text{L}}\left( {\text{T}} \right) - {\text{L}}\left( {{\text{t}}_{0.{5}} } \right)} \right]*{\text{H}}(\gamma ).$$\end{document}
```

</div>

This equation can be rearranged into:

<div id="Equ5" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\left[ {{\text{L}}\left( {{\text{t}}_{0.{5}} } \right) - {\text{L}}\left( {{\text{t}}_0 } \right)} \right]*\left[ {{\text{H}}\left( \gamma \right) - {\text{H}}\left( \beta \right)} \right] \, + {\text{ L}}\left( {\text{T}} \right)*{\text{H}}\left( \beta \right) \, = \, \left[ {{\text{L}}\left( {\text{T}} \right) - {\text{L}}\left( {{\text{t}}_{0.{5}} } \right)} \right]*\left[ {{\text{H}}\left( \gamma \right) - {\text{H}}\left( \beta \right)} \right] \, + {\text{ L}}\left( {\text{T}} \right)*{\text{H}}\left( \beta \right).$$\end{document}
```

</div>

Given our scaling of L(t<sub>0</sub>) = 0 and L(T) = 1, this can be simplified into:

<div id="Equ6" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{L}}\left( {{\text{t}}_{0.{5}} } \right) = { 1} - {\text{L}}\left( {{\text{t}}_{0.{5}} } \right).$$\end{document}
```

</div>

Hence, H(γ) and H(β) drop from the equation, and we can estimate the value of t<sub>0.5</sub> for which L(t) = 0.5, without needing to know H(q).

We can proceed with this elicitation by using the estimate of t<sub>0.5</sub> in a follow-up question. Specifically, we can elicit t<sub>0.25</sub> for which L(t<sub>0.25</sub>) = 0.25, such that the respondent is indifferent between the profiles (\[t<sub>0</sub>,t<sub>0.25</sub>\], γ; \[t<sub>0.25</sub> + 1,t<sub>x</sub>\], β) and (\[t<sub>0</sub>,t<sub>0.25</sub>\], β; \[t<sub>0.25</sub> + 1,t<sub>0.5</sub>\], γ), or we can elicit t<sub>0.75</sub> for which L(t<sub>0.75</sub>) = 0.75, such that the respondent is indifferent between the profiles (\[t<sub>0.5</sub>,t<sub>0.75</sub>\], γ; \[t<sub>0.75</sub> + 1,T\], β) and (\[t<sub>0.5</sub>,t<sub>0.75</sub>\], β; \[t<sub>0.75</sub> + 1,T\], γ), or both. In the first case, we obtain the equation L(t<sub>0.25</sub>) = 0.5 − L(t<sub>0.25</sub>) = 0.25, and in the second case we obtain L(t<sub>0.75</sub>) − 0.5 = 1 − L(t<sub>0.75</sub>), so L(t<sub>0.75</sub>) = 0.75. One can continue this way to get a measurement of L(t) up to any desired degree of precision. In our study, as described below, we elicited the following five points of the discount function: L(t<sub>0.125</sub>) = 0.125, L(t<sub>0.25</sub>) = 0.25, L(t<sub>0.5</sub>) = 0.5, L(t<sub>0.75</sub>) = 0.75, and L(t<sub>0.875</sub>) = 0.875.

## Experiment

### Design and participants

After elaborate pilot testing with students and university staff, who were not part of the formal study, personal interviews were conducted with 151 respondents. We aimed to recruit a sample representative of the English adult population in terms of age, gender, and education. Respondents were recruited by a survey company (Dynata) and received a reward in terms of an addition to their panel points, equivalent to about £30, which could for instance be exchanged into a gift voucher. One of the co-authors (ZL) administrated interviews by using videocalls on Zoom or Google Meet. Only the language of English was used during the whole interview. Participants could complete the designed tasks by following the written steps with the interviewer on the shared screen that was controlled by the interviewer. Any questions could be asked during the interview, which lasted for a maximum of 1 h. The video calls were not recorded for privacy reasons. Ethical approval for this study was provided by the Research Ethics Review Committee of Erasmus School of Health Policy & Management.

#### Interview procedure

The experiment started by participants completing the EQ-5D-Y-3L instrument to allow them to familiarize themselves with its descriptive system. Before the cTTO task, respondents received a cTTO warm-up task featuring the health state “being in a wheelchair”. The interviewer used this example to explain the cTTO task and how their choices would invoke two scenarios: better than dead and worse than dead. After this, two more practice tasks were presented. One of them involved a severe health state that was included expecting it could be considered WTD by many respondents, providing more practice with the WTD procedure included in cTTO.

#### TTO operationalization

TTO was operationalized in 2 blocks, one with a 10-year duration and one with a 20-year duration, which were presented in random order. We completed 4 blocks of TTO tasks (2 perspectives, 2 durations) for 4 health states in a computer-instructed setting. We selected the following health states: 22222, 32211, 32223 and 23232, where the first health state means moderate problems in all 5 dimensions, etc. These health states were also incorporated in Kreimeier et al. \[11\] and cover a wide spectrum of severity.

We implemented the EQ-VT protocol \[45, 46\], with the standard time horizon logically changed from 10 to 20 years for the 20-year task. The EQ-VT protocol involved a bisection procedure for the first three steps followed by upward/downward titration with 1-year or 6-month increments. For the 20-year task, an extension of the standard cTTO task in the EQ-VT protocol was developed by MathsinHealth (a consulting firm which is an expert in health economics research).

#### Time preference measurement

Health states β = 32211 and γ = 11111 were used to serve as the respective bad and good health states in the time preference task, from both the adult and child perspective. The corrected TTO utilities were computed by applying this discounting information to the TTO answers, using linear interpolation if a TTO answer was between two points on the discount function. For example, suppose someone values 7 years in full health the same as 20 years in health state 32211. From the discounting task, we have elicited t<sub>0.125</sub> = 3, t<sub>0.25</sub> = 6, t<sub>0.5</sub> = 14, t<sub>0.75</sub> = 21 and t<sub>0.875</sub> = 24 for this respondent. Then we estimate L(7) to be 0.25 + (7 − 6)/(14 − 6)\*(0.5 − 0.25) = 0.281 and L(20) to be 0.5 + (20 − 14)/(21 − 14)\*0.25 = 0.714. Applying Eq. (<a href="#Equ2" data-ref-type="disp-formula">2</a>) then gives h(32211) = 0.281/0.714 = 0.394. Note that without correcting for discounting we would obtain h(32211) = 7/20 = 0.35. Details about correcting TTO utilities for discounting with the Direct Method can be found in Attema et al. \[41\]. The task was programmed using software in Shiny.[^1]

The framing in the child perspective part of the Direct Method was similar as in the TTO task. That is, the respondents had to consider health improvements for a 10-year-old child. In the first question, they would for example choose between a direct health improvement to full health for the child for the next 15 years, followed by state 32211 in the subsequent 15 years, and a postponed health improvement. The latter would entail the child first living in state 32211 for 15 years, followed by 15 years in full health.

The order of the blocks was randomized, as well as the order of the tasks within the TTO and time preference blocks and the order of the health states within the TTO tasks.

### Analysis

#### Data quality

A data quality check was performed for all 4 TTO tasks. This included the number of non-trading responses (i.e. h(q) = 1), the number of all-in-trading responses (i.e. h(q) = -1 for the 10-year-task and h(q) = −0.5 for the 20-year-task), the number of responses implying a state was valued the same as death (i.e. h(q) = 0), and the number of respondents per task who valued all health states the same \[47\]. Furthermore, we could perform some dominance tests, because state 22222 is strictly better than states 32223 and 23232, and state 32211 is strictly better than 32223. For example, if weak dominance holds, we should have h(22222) ≥ h(32223) and strict dominance would imply h(22222) \> h(32223). We counted the number of weak and strict dominance violations for all these 3 health state pairs.

#### Utilities

We compare the TTO utilities between the perspectives for all 4 health states and 2 durations, using paired t-tests. Second, we compute the differences between the utilities obtained from the adult and child perspective for all health states and perform paired *t*-tests that compare these gaps for the 10- and 20-year durations. Finally, we compare these gaps for the uncorrected and the corrected TTO utilities, again performing paired t-tests.

#### Time preferences

We also compare the discount functions obtained from the two perspectives. This is captured by the ‘area-under-the-curve’ (AUC) approach \[48–52\]. Because of our normalization, this area is bounded between 0 and 1, and a value of AUC of 0.5 equals zero discounting, i.e., no time preferences. AUC \> ( \<) 0.5 indicate positive (negative) discounting. As such, someone who has AUC \> 0.5 considers years in the future to have less value than years today, whereas the opposite holds for AUC \< 0.5.

#### Mixed effects regressions

Finally, we perform mixed-effects regressions of both the uncorrected and the corrected TTO utilities, with subject random effects and dummies for perspective, duration, and health states, as well as several socio-demographic variables:

<div id="Equ7" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${h}_{i,q}=\alpha +{HS}_{q}{\beta }^{^{\prime}}+\gamma {D}_{20}+\delta {P}_{C}+{{x}_{i}\gamma }^{^{\prime}}+\varepsilon .$$\end{document}
```

</div>

In this model, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${h}_{i,q}$$\end{document}`$ are the utilities, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${HS}_{q}$$\end{document}`$ is a matrix containing the health state dummies, D<sub>20</sub> is a duration dummy taking value 1 for the 20-year task, and P<sub>C</sub> denotes a perspective dummy taking value 1 for the child perspective. Furthermore, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${x}_{i}$$\end{document}`$ is a matrix containing the other variables (gender, age, own health rating, education, children, religion, subjective life expectancy of children and adults), $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha$$\end{document}`$ is a constant reflecting the adult perspective of the 10-year task valuing health state 22222, and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\varepsilon$$\end{document}`$ is an error term.

## Results

### Sample description

The sample is summarized in Table <a href="#Tab1" data-ref-type="table">1</a> below and is reasonably representative of the UK adult public in terms of age, gender, and education, with a slight overrepresentation of highly educated respondents. According to the summary of the UK census in 2020, 23.34% fall under the age of 19, 26.14% are aged between 19 and 39, 31.87% belong to the 40 to 65 age group, and 18.65% are over 65 years; females and males account for 51% and 49% of the whole population, respectively. By the year 2020, among individuals aged from 25 to 64 years, 18.3% had education level below the upper secondary, 32.3% had finished upper secondary or post-secondary non-tertiary education, while 49.4% had completed tertiary education, which includes short-cycle tertiary education, bachelor’s or equivalent, master’s or equivalent and doctoral or equivalent \[53\].

<div id="Tab1" class="table-wrap">

<div class="caption">

Summary statistics

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variables</th>
<th style="text-align: left;">Percentage</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;"></td>
<td rowspan="4" style="text-align: left;">51.6</td>
<td rowspan="4" style="text-align: left;">15.7</td>
</tr>
<tr>
<td style="text-align: left;">19–39</td>
<td style="text-align: left;">29.1%</td>
</tr>
<tr>
<td style="text-align: left;">40–65</td>
<td style="text-align: left;">45.7%</td>
</tr>
<tr>
<td style="text-align: left;">65+</td>
<td style="text-align: left;">25.2%</td>
</tr>
<tr>
<td style="text-align: left;">Gender</td>
<td style="text-align: left;"></td>
<td rowspan="4" style="text-align: left;"></td>
<td rowspan="4" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">% Male</td>
<td style="text-align: left;">48.3</td>
</tr>
<tr>
<td style="text-align: left;">% Female</td>
<td style="text-align: left;">51.7</td>
</tr>
<tr>
<td style="text-align: left;">% Other</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Education</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Lower</td>
<td style="text-align: left;">20.5</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Middle</td>
<td style="text-align: left;">21.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Higher</td>
<td style="text-align: left;">57.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Health status: VAS</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">79.4</td>
<td style="text-align: left;">14.3</td>
</tr>
<tr>
<td style="text-align: left;">Expected age of own death</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">83.7</td>
<td style="text-align: left;">8.4</td>
</tr>
<tr>
<td style="text-align: left;">Expected age of death of child of 10 years</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">87.5</td>
<td style="text-align: left;">9.3</td>
</tr>
<tr>
<td style="text-align: left;">Having children</td>
<td style="text-align: left;">61.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Being religious</td>
<td style="text-align: left;">27.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Low education: elementary school or pre-vocational secondary education; middle education: secondary vocational education or upper-level secondary school); high education: higher professional education or university

</div>

### Data quality

Table <a href="#Tab2" data-ref-type="table">2</a> gives some statistics related to data quality. The results indicate that respondents give more non-trading responses (h(q) = 1) for children (10y: 18.9%; 20y: 15.1%) than for adults (10y: 13.8%; 20y: 14.1%) under both conditions, which is statistically significant for the 10-year condition (binomial proportion test: *p* \< 0.02), but not for the 20-year condition (*p* = 0.62). The other comparisons between adult and child tasks were not significant at the 5% level. Comparing the 2 durations, we find some evidence for more non-trading for the 10-year variant than for the 20-year variant. A binomial test for proportions shows significance at the 10% level for children (*p* = 0.079), but not for adults (*p* = 0.87). There is no evidence suggesting that the increased duration affects all-in-trading responses (sacrificing all 10 years of lead-time, *p* \> 0.33). There were also no significant differences for the number of h(q) = 0 values (*p*'s \> 0.30), the number of respondents that value all states the same (*p*'s \> 0.11), and the proportion of dominated responses (*p*'s \> 0.17).

<div id="Tab2" class="table-wrap">

<div class="caption">

Data quality for both durations of adult and child perspectives

</div>

| Categories | TTO (10y)-Adult | TTO (10y)-Child | TTO (20y)-Adult | TTO (20y)-Child |
|----|----|----|----|----|
| Responses without trading (h(q) = 1) (out of 604 observations)\* | 83 (13.7%) | 114 (18.8%) | 85 (14.1%) | 91 (15.1%) |
| All-in trading responses (h(q) = −1/−0.5) (out of 604 observations)\* | 12 (2.0%) | 11 (1.8%) | 8 (1.3%) | 16 (2.6%) |
| Responses implying zero trading h(q) = 0 (out of 604 observations)\* | 19 (3.1%) | 21 (3.5%) | 19 (3.1%) | 15 (2.5%) |
| All states valued the same (out of 151)\*\* | 12 (7.9%) | 11 (7.3%) | 7 (4.6%) | 14 (9.3%) |
| Respondents without 0.5-year increments (out of 151) | 78 (51.7%) | 82 (54.3%) | 100 (66.2%) | 96 (63.6%) |
| Weak dominance violation (e.g., h(q)(22222) \<  = h(q)(32223), h(q)(22222) \<  = h(q)(23232)) (out of 453)<sup>†</sup> | 139 (30.7%) | 140 (30.9%) | 114 (25.2%) | 132 (29.1%) |
| Strict dominance violation (e.g., h(q)(22222) \< h(q)(23232), h(q)(22222) \< h(q)(32223)) (out of 453)<sup>†</sup> | 34 (7.5%) | 29 (6.4%) | 33 (7.3%) | 31 (6.8%) |

<sup>\*</sup>151 respondents × 4 health states

<sup>\*\*</sup>151 respondents

<sup>†</sup>151 respondents × 3 health state pairs

</div>

### Time preference

Figure <a href="#Fig2" data-ref-type="fig">2</a> plots the AUC derived from the direct method completed with a child- or self-perspective, within-subjects. This scatterplot indicates large heterogeneity of time preferences. Furthermore, we find that AUC for children is slightly smaller than for adults, but the difference is not significant (means: 0.502 (Adults), 0.489 (Children); paired *t*-test: *p* = 0.14). Both AUCs are not significantly different from 0.50 (*t* test: *p*’s \> 0.11).

<figure id="Fig2">
<p><img src="10198_2023_1612_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Scatterplot of area-under-the-curve (AUC) for the adult and child perspectives</figcaption>
</figure>

We also classified respondents according to their time preferences and determined if their AUC was larger for adult or child perspectives, as shown in Table <a href="#Tab3" data-ref-type="table">3</a> below. Sixty out of 151 respondents (39.7%) discounted negatively for both children and adults, compared with 39 out of 151 respondents (25.8%) who discounted positively.

<div id="Tab3" class="table-wrap">

<div class="caption">

Classification of respondents according to their time preferences

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Children</th>
<th colspan="3" style="text-align: left;">Adults</th>
</tr>
<tr>
<th style="text-align: left;">Positive discounting</th>
<th style="text-align: left;">No discounting</th>
<th style="text-align: left;">Negative discounting</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Positive discounting</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">24</td>
</tr>
<tr>
<td style="text-align: left;">No discounting</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">5</td>
</tr>
<tr>
<td style="text-align: left;">Negative discounting</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">60</td>
</tr>
</tbody>
</table>

</div>

### TTO utilities

We investigated the mean uncorrected and corrected utilities for all health states, by perspectives and conditions, as presented in Table <a href="#Tab4" data-ref-type="table">4</a>. It is clear from this table that health states are valued higher from the child perspective than from the adult perspective, with the former perspective yielding higher mean utilities for all 4 health states in both durations. However, this difference is not significant for any of the comparisons (paired *t*-tests, all *p*’s \> 0.07 for the uncorrected utilities and all *p*’s \> 0.30 for the corrected utilities).

<div id="Tab4" class="table-wrap">

<div class="caption">

Mean TTO utilities (standard deviations in parentheses)\*

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Health state</th>
<th colspan="6" style="text-align: left;">10-year</th>
<th colspan="6" style="text-align: left;">20-year</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Adult</th>
<th colspan="2" style="text-align: left;">Child</th>
<th colspan="2" style="text-align: left;">Sig. adult versus child</th>
<th colspan="2" style="text-align: left;">Adult</th>
<th colspan="2" style="text-align: left;">Child</th>
<th colspan="2" style="text-align: left;">Sig. adult versus child</th>
</tr>
<tr>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
<th style="text-align: left;">U</th>
<th style="text-align: left;">Cor</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">22222</td>
<td style="text-align: left;">0.7 (0.35)</td>
<td style="text-align: left;">0.71 (0.39)</td>
<td style="text-align: left;">0.74 (0.32)</td>
<td style="text-align: left;">0.72 (0.42)</td>
<td>0.08</td>
<td>0.61</td>
<td style="text-align: left;">0.71 (0.32)</td>
<td style="text-align: left;">0.72 (0.32)</td>
<td style="text-align: left;">0.73 (0.3)</td>
<td style="text-align: left;">0.71 (0.36)</td>
<td>0.21</td>
<td>0.70</td>
</tr>
<tr>
<td style="text-align: left;">32111</td>
<td style="text-align: left;">0.73 (0.31)</td>
<td style="text-align: left;">0.74 (0.31)</td>
<td style="text-align: left;">0.76 (0.31)</td>
<td style="text-align: left;">0.76 (0.3)</td>
<td>0.19</td>
<td>0.31</td>
<td style="text-align: left;">0.71 (0.31)</td>
<td style="text-align: left;">0.72 (0.31)</td>
<td style="text-align: left;">0.75 (0.31)</td>
<td style="text-align: left;">0.73 (0.37)</td>
<td>0.08</td>
<td>0.71</td>
</tr>
<tr>
<td style="text-align: left;">32223</td>
<td style="text-align: left;">0.52 (0.42)</td>
<td style="text-align: left;">0.54 (0.41)</td>
<td style="text-align: left;">0.55 (0.45)</td>
<td style="text-align: left;">0.54 (0.49)</td>
<td>0.29</td>
<td>0.95</td>
<td style="text-align: left;">0.52 (0.36)</td>
<td style="text-align: left;">0.54 (0.36)</td>
<td style="text-align: left;">0.56 (0.38)</td>
<td style="text-align: left;">0.53 (0.42)</td>
<td>0.13</td>
<td>0.75</td>
</tr>
<tr>
<td style="text-align: left;">23232</td>
<td style="text-align: left;">0.45 (0.46)</td>
<td style="text-align: left;">0.47 (0.49)</td>
<td style="text-align: left;">0.49 (0.47)</td>
<td style="text-align: left;">0.47 (0.56)</td>
<td>0.20</td>
<td>0.93</td>
<td style="text-align: left;">0.51 (0.37)</td>
<td style="text-align: left;">0.52 (0.39)</td>
<td style="text-align: left;">0.52 (0.38)</td>
<td style="text-align: left;">0.49 (0.45)</td>
<td>0.69</td>
<td>0.37</td>
</tr>
</tbody>
</table>

<sup>\*</sup>U = uncorrected; Cor = corrected

</div>

Correction for time preference had little effect on mean utilities. Out of the 16 observations (4 health states, 2 perspectives, 2 conditions), there were only 2 states for which we found evidence that correcting for time preference yielded significant differences in utilities. When using non-parametric tests, slightly more evidence is observed, i.e., paired Wilcoxon tests are significant for 3 states. Still, the between-perspective difference has decreased, and the *p*-values have correspondingly increased. It is also noteworthy that the corrected utilities are lower than the uncorrected utilities for the child perspective, due to negative average time preference, while the opposite holds for the adult perspective. Consequently, the perspective gap decreases after correction for time preference.

There is also no evidence in favor of significant differences between the 10- and 20-year duration, neither for the adult, nor for the child perspective (all *p*’s \> 0.17, except for state 23232 with higher utility for 20 years than 10 years under the adult perspective, *p* \< 0.01). These results were similar when using the censored 10-year TTO (all *p*’s \> 0.50).

Finally, we do find several significant differences when comparing the adult–child gaps for the uncorrected utilities with the adult–child gaps for the corrected utilities. In particular, the gap is lower for the corrected utilities for all 8 comparisons, with the difference being significant for state 32223 for the 10-year duration (*p* = 0.04) and for all 4 states for the 20-year duration (*p* \< 0.05).

### Regression results

The results of the mixed effects regressions are reported in Table <a href="#Tab5" data-ref-type="table">5</a>. It shows that health state 32223 and 23232 receive lower utilities than state 22222, reflecting their higher impairments on several dimensions. Most demographic variables are not significant, except for one's own health rating, with healthier people trading off slightly more lifetime, and a marginal significance of income with larger incomes trading off less lifetime, but only in Model 1. Interestingly, the dummy for child perspective is positive and highly significant in Model 1, indicating uncorrected TTO utilities measured from the child perspective are on average 0.03 higher than TTO utilities measured from the own perspective. Model 2 illustrates that most results are similar for the corrected TTO utilities as for the uncorrected ones, with one notable exception. That is, the perspective dummy has become close to 0 and is no longer significant. This indicates that utilities are no longer valued higher from the child perspective than the adult perspective after correction for time preferences.

<div id="Tab5" class="table-wrap">

<div class="caption">

Mixed effects regression on uncorrected and corrected TTO utilities

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: left;">Model 1: Uncorrected TTO<br />
Coefficient (std. error)</th>
<th style="text-align: left;">Model 2: Corrected TTO<br />
Coefficient (std. error)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;"><p>0.827</p>
<p>(0.293)***</p></td>
<td style="text-align: left;">0.836 (0.307)***</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;"><p>− 0.0003</p>
<p>(0.002)</p></td>
<td style="text-align: left;">0.001 (0.002)</td>
</tr>
<tr>
<td style="text-align: left;">Male (reference: non-male)</td>
<td style="text-align: left;"><p>0.050</p>
<p>(0.050)</p></td>
<td style="text-align: left;">0.058 (0.053)</td>
</tr>
<tr>
<td style="text-align: left;">EQVAS Own health today</td>
<td style="text-align: left;"><p>− 0.004</p>
<p>(0.002)**</p></td>
<td style="text-align: left;">− 0.005 (0.002)**</td>
</tr>
<tr>
<td style="text-align: left;">Religious (reference: not religious)</td>
<td style="text-align: left;"><p>− 0.026</p>
<p>(0.056)</p></td>
<td style="text-align: left;">− 0.009 (0.059)</td>
</tr>
<tr>
<td style="text-align: left;">Medium education (reference: low education)</td>
<td style="text-align: left;"><p>− 0.058</p>
<p>(0.078)</p></td>
<td style="text-align: left;">− 0.061 (0.081)</td>
</tr>
<tr>
<td style="text-align: left;">High education (reference: low education)</td>
<td style="text-align: left;"><p>− 0.029</p>
<p>(0.068)</p></td>
<td style="text-align: left;">− 0.026 (0.071)</td>
</tr>
<tr>
<td style="text-align: left;">Income (in categories)</td>
<td style="text-align: left;"><p>0.030</p>
<p>(0.018)*</p></td>
<td style="text-align: left;">0.023 (0.018)</td>
</tr>
<tr>
<td style="text-align: left;">Has as at least one child (reference: no children)</td>
<td style="text-align: left;"><p>− 0.000</p>
<p>(0.060)</p></td>
<td style="text-align: left;">0.006 (0.063)</td>
</tr>
<tr>
<td style="text-align: left;">Expected age of own death</td>
<td style="text-align: left;"><p>− 0.000</p>
<p>(0.004)</p></td>
<td style="text-align: left;">− 0.000 (0.004)</td>
</tr>
<tr>
<td style="text-align: left;">Expected age of death 10y-old child</td>
<td style="text-align: left;"><p>0.002</p>
<p>(0.003)</p></td>
<td style="text-align: left;">0.002 (0.003)</td>
</tr>
<tr>
<td style="text-align: left;">Dummy state 32111 (reference: 22222)</td>
<td style="text-align: left;"><p>0.020</p>
<p>(0.014)</p></td>
<td style="text-align: left;">0.027 (0.016)</td>
</tr>
<tr>
<td style="text-align: left;">Dummy state 32223 (reference: 22222)</td>
<td style="text-align: left;"><p>− 0.188</p>
<p>(0.014)***</p></td>
<td style="text-align: left;">− 0.181 (0.016) ***</td>
</tr>
<tr>
<td style="text-align: left;">Dummy state 23232 (reference: 22222)</td>
<td style="text-align: left;"><p>− 0.231</p>
<p>(0.014)***</p></td>
<td style="text-align: left;">− 0.230 (0.016) ***</td>
</tr>
<tr>
<td style="text-align: left;">Dummy child perspective (reference: own perspective)</td>
<td style="text-align: left;"><p>0.028</p>
<p>(0.010)***</p></td>
<td style="text-align: left;">− 0.001 (0.011)</td>
</tr>
<tr>
<td style="text-align: left;">Dummy 20y TTO (reference: 10y TTO)</td>
<td style="text-align: left;"><p>0.010</p>
<p>(0.010)</p></td>
<td style="text-align: left;">0.005 (0.011)</td>
</tr>
</tbody>
</table>

Model 1: Log restricted likelihood: − 226.66. Wald Chi squared: 534.85, *p* \< 0.001

Model 2: Log restricted likelihood: − 577.13. Wald Chi squared: 389.58, *p* \< 0.001

\*\*\*Significant at the 1%-level. \*\*Significant at the 5%-level. \*Significant at the 10%-level

</div>

## Discussion

This paper sought to investigate the effect of duration on the difference between TTO utilities measured from the adult’s own perspective and TTO utilities measured from a 10-year-old child’s perspective. In addition, we studied the effect of time preferences on both these TTO utilities and their difference. Although we found no significant differences between child and adult utilities in within-subjects tests, we did find significantly higher utilities for the child perspective than for the adult perspective after controlling for other variables in a mixed effects regression. Interestingly, correcting for time preferences removed this gap. Hence, the gap between child and adult TTO utilities may be partially driven by a difference in time preference between these perspectives. Extending the duration considered in TTO had no impact on utilities, neither from the adult perspective nor from the child perspective. The implication of these findings is that while a longer duration does not attribute to a smaller adult–child gap in TTO utilities (in line with the null-results reported in Lipman \[21\]), correcting for perspective-dependent time preferences does. Therefore, such a correction appears to be a worthwhile exercise.

The literature comparing adult and child TTO utilities shows mixed results, with some studies finding no systematic differences \[14, 16, 17\], but those studies that do, all report higher utilities for the child perspective than for the adult perspective \[11, 13, 15\]. The results of our study confirm the latter, although the gap is not substantial and only significant when controlling for other variables. To the best of our knowledge, there is only one previous study that compared child and adult perspective for time-preference-corrected TTO utilities, whose results are partly in line with our results \[16\]. Like us, they also found close to zero discounting and no significant differences between discounting from the two perspectives. However, in contrast to us, they reported no difference in health state utilities between the adult and child perspective. An explanation for this difference may be that their sample included Dutch respondents instead of UK respondents. Future work could directly test for country differences in perspective-specific time preferences by including both Dutch and UK respondents in their sample.

Our findings of a lack of discounting (on average) are worth discussing. Although these results confirm some previous studies \[16, 43, 44, 54\], other studies found higher discount rates\[39, 48, 55–57\].[^2] One explanation for the low amount of discounting in this and other recent studies is the use of the direct method. Because of its use of sequences, the sequence effect might induce respondents to prefer improving sequences over deteriorating sequences, which results in low, or even negative, discount rates \[58, 59\]. More specifically, we found 39.3% respondents were negative discounters for children and adults, while 25.3% discounted positively for both. However, similar findings of negative discounting have been present in other studies \[16, 44, 54, 60, 61\]. It is also worth noting that some popular methods ignore the possibility of negative discounting altogether \[62\], biasing estimates of discount rates upwards. Hence, it is advisable to replicate our study with an alternative time preference elicitation method that is less susceptible to a sequence effect (whilst still allowing negative time preference). It is unclear, however, if differences between child and adult perspectives would be similarly reduced with other methods.

Additionally, the method we used to elicit time preferences may also have captured other considerations. Respondents may think their ability to cope with a deteriorated health varies with their age \[63\]. For instance, they may reason that a poorer health state at the age of 80 is more acceptable than at the age of 50, being the result of the aging process. Alternatively, someone may argue that it is easier to cope with a health impairment at a young age than at an old age when they anticipate being more fragile. The answers given in the discounting task would then reflect a recognition of different life stage rather than discounting. We believe that exploring the influence of these alternative possibilities on time preference measurements is an interesting direction for future research.

Another limitation is that we did not perform validity checks for the time preference elicitation. Therefore, we cannot draw any conclusions about the robustness of our findings on this part. However, the time preference measurement was mainly included for supplementary analyses, while the main objective of this research was to test if the utility difference between child and adult perspective would be affected by incorporating a longer duration of 20 years instead of the standard 10 years. We encourage research in the future to further investigate the role of time preferences in cTTO valuation, including validity checks, such as test–retest reliability and an extensive test phase.

Compared to previous literature we observe a slightly higher percentage of weak and strict violations of dominance than in Lipman et al. \[16\], but comparable to Attema et al. \[14\]. This may have been caused by the relatively small differences between the health states in our study. In addition, we find more non-trading, more respondents without negative utilities, and less all-in trading than in Attema et al. \[14\], which can be attributed to the lack of very severe health states in our study. Our study is subject to a set of limitations. First, a limitation of our study is the use of video-interviews instead of physical interviews. This was unavoidable given the severe Covid-19 restrictions at the time of the data collection (autumn 2021). However, evidence suggests that video-interviews do not seriously decrease data quality \[64, 65\]. Second, the minimum admissible utility was higher for the 20-year duration (−0.5) than for the 10-year duration (−1). Here we had to make a trade-off between equal scales on the one hand and a realistic time horizon and identical lead-times on the other hand. For instance, if we wanted to maintain equal proportions of lead-time and time in impaired health, the maximum time horizon for states considered worse than dead would be 40 years. This would imply most years are spent in adulthood even in a child perspective, reducing differences with the adult perspective for WTD states. Moreover, the distortion caused by time preference would become even larger. Still, we do not think this has largely distorted our comparison, because not more than 2.6% of the responses was at the lower end of the scale for the 20-year duration, and this was only slightly higher than the maximum percentage of values equal to −1 (2.0%) for the 10-year duration. Furthermore, a robustness analysis where all utilities of the 10-year-task were censored at −0.5 generated similar results as the initial analysis. Still, we are unable to rule out the possibility that the difference in lead-time-to-disease-time ratio explains the similarity between the 10-year and 20-year TTO utilities.

A final limitation of this study is that it only provides a partial explanation of *why* utilities differ between adult and child perspectives. Earlier qualitative work has suggested a wide array of factors, not related to severity of health states, to influence valuation with child perspectives, e.g., Reckers-Droog et al. \[66\]. Besides our exclusively quantitative focus, the design used here allows concluding that time preferences differ between adult deciding for themselves or for 10-year-old children. As such, it is not clear if any effects are driven by differences between time preferences in deciding for self or other, or between deciding for adults or children. To identify such effects, a design like that of Lipman et al. \[17\] would be needed, who identified that the difference between adult and child perspectives appears mostly driven by the difference between deciding for other and deciding for self.

## Conclusion

We conclude that there is a small but significant discrepancy between uncorrected health state utilities elicited from the child and adult perspective in the EQ-VT protocol when controlling for other variables. In particular, respondents give up fewer life years in a TTO task when the child perspective is taken than when the adult (own) perspective is taken. This discrepancy is robust to the use of a longer gauge duration of 20 years, but it decreases after correcting for time preference. Therefore, similar health states do not seem to be valued systematically differently when they concern children than when they concern adults. Instead, individual, perspective-specific, time preferences may be partially driving the TTO responses.

##### Appendix: Experimental instructions

###### Introduction

Demographic questions are asked first, e.g., experience with serious illness, age, and gender. Interviewees then start this experiment by completing the regular EQ-5D-3L-Y assessment, which includes mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. They will then be asked to overall evaluate how good or bad their health is today, from 0 to 100, where 0 represents the worst health, you can imagine and 100 means the best. A slider is used to indicate their choice. To be noted, the best or worst health states are not referred to being super rich or super poor, it is overall not related to material status. After that, they are assumed to be familiar with this system and move to the warmup section.

###### Warmup section

###### Task 1

They are then asked to choose between two lives shown on the screen, A and B, which involves different health states and life duration. Respondents are informed that both lives would not change in any way as no medication or other possible treatment can extend or shorten the life duration (euthanasia). They can only think and choose from what they see on the screen, instead of thinking about how their choices could impact further tasks. After both lives, it is painless and immediate death. In the first example, life with a wheelchair, they start with choosing between 10 years in full health and 10 years in a wheelchair.

###### Task 2

A worse than death (WTD) or better than death (BTD) task will be invoked, based on respondents’ decision in task 1. That is, if the original answer indicates that the state is WTD, then a BTD choice is shown, otherwise, it is the WTD pathway after a BTD decision on the first task. The lead time trade-off method is expected to be explained in the WTD part for the respondents.

###### Task 3

Respondents are now asked to make a series of choices for themselves between Life A and B. They are reminded that at the end of the described period, it is immediate and painless death. The length of life (e.g., by changing your lifestyle or choosing euthanasia) cannot be changed. The quality of life (e.g., through pain relief or other medication) cannot be changed. Which life do you think is better? The first TTO task is then introduced and starts with letting the respondents choose between 10 years in full health and 10 years in a health state (21112). After that, they start with choosing between 10 years in full health and 10 years in another health state (32323).

###### TTO part

###### Section 1

Respondents are now asked to make several choices for themselves between Life A and B. They are reminded that at the end of the described period, it is immediate and painless death. The length of life (e.g., by changing your lifestyle or choosing euthanasia) cannot be changed. The quality of life (e.g., through pain relief or other medication) cannot be changed. Which life do you think is better?

###### Section 2

Respondents are now asked to make several choices for a 10-year-old child between Life A and B. They are reminded that at the end of the described period, it is immediate and painless death. The length of life (e.g., by changing your lifestyle or choosing euthanasia) cannot be changed. The quality of life (e.g., through pain relief or other medication) cannot be changed. Which life do you think is better?

###### Section 3

Respondents are now asked to make several choices for themselves between Life A and B for 20 years. They are reminded that at the end of the described period, it is immediate and painless death. The length of life (e.g., by changing your lifestyle or choosing euthanasia) cannot be changed. The quality of life (e.g., through pain relief or other medication) cannot be changed. Which life do you think is better?

###### Section 4

Respondents are now asked to make several choices for a 10-year-old child between Life A and B for 20 years. They are reminded that at the end of the described period, it is immediate and painless death. The length of life (e.g., by changing your lifestyle or choosing euthanasia) cannot be changed. The quality of life (e.g., through pain relief or other medication) cannot be changed. Which life do you think is better?

###### TTO feedback

Respondents are asked to answer whether they think the TTO tasks are easy to understand, whether is it easy to make the difference between those lives they are asked to think about, whether it is difficult to decide on the exact points where A and B are about the same. Their answers are indicated by five levels, strongly agree, agree, nether agree nor disagree, disagree, strongly disagree.

###### Background questions

We then ask other demographic questions, including their religious belief, the highest level of education they have completed, total gross yearly income of their household, whether they have children and their life expectancy.

### Acknowledgements

This research was made possible through a grant from The EuroQol Group, project number EQ Project 237-RA. The views expressed in this paper are those of the authors and do not necessarily reflect the views of The EuroQol Group. We are grateful to Matthijs Versteegh for advice in developing the study. Dr. Lipman is also co-funded by Smarter Choices for Better Health Initiative. The authors declare to have no conflicts of interest. Data are available from the authors upon reasonable request.

### Data availability

Data are available from the authors upon request.

## References

1. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the Instrument’s characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22:31–37. doi:10.1016/j.jval.2018.11.001

2. Devlin NJ. Valuing child health isn’t child’s play. Value Health. 2022;25:1087–1089. doi:10.1016/j.jval.2022.05.009

3. van Reenen, M., Janssen, B., Oppe, M., Kreimeier, S., Greiner, W.: EQ-5D-Y user guide: basic information on how to use the EQ-5D-Y instrument. EuroQol Group (2014)

4. Wille N, Badia X, Bonsel G, Burström K, Cavrini G, Devlin N, Egmar A-C, Greiner W, Gusi N, Herdman M. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual. Life Res. 2010;19:875–886. doi:10.1007/s11136-010-9648-y

5. Ramos-Goñi JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, Devlin N. International Valuation Protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020;7:653–663. doi:10.1007/s40273-020-00909-3

6. Noyes J, Edwards RT. EQ-5D for the assessment of health-related quality of life and resource allocation in children: a systematic methodological review. Value Health. 2011;14:1117–1129. doi:10.1016/j.jval.2011.07.011

7. Ravens-Sieberer U, Wille N, Badia X, Bonsel G, Burström K, Cavrini G, Devlin N, Egmar A-C, Gusi N, Herdman M. Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study. Qual. Life Res. 2010;19:887–897. doi:10.1007/s11136-010-9649-x

8. Golicki D, Młyńczak K. Measurement properties of the EQ-5D-Y: a systematic review. Value Health. 2022;25:1910–1921. doi:10.1016/j.jval.2022.05.013

9. Lipman SA, Reckers-Droog VT, Kreimeier S. Think of the children: a discussion of the rationale for and implications of the perspective used for EQ-5D-Y health state valuation. Value Health. 2021;24:976–982. doi:10.1016/j.jval.2021.01.011

10. Rowen D, Rivero-Arias O, Devlin N, Ratcliffe J. Review of valuation methods of preference-based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going?. Pharmacoeconomics. 2020;38:325–340. doi:10.1007/s40273-019-00873-7

11. Kreimeier S, Oppe M, Ramos-Goñi JM, Cole A, Devlin N, Herdman M, Mulhern B, Shah KK, Stolk E, Rivero-Arias O. Valuation of EuroQol five-dimensional questionnaire, youth version (EQ-5D-Y) and EuroQol five-dimensional questionnaire, three-level version (EQ-5D-3L) health states: the impact of wording and perspective. Value Health. 2018;21:1291–1298. doi:10.1016/j.jval.2018.05.002

12. Lipman SA, Essers BAB, Finch AP, Sajjad A, Stalmeier PFM, Roudijk B. In a child’s shoes: composite time trade-off valuations for EQ-5D-Y-3L with different proxy perspectives. Pharmacoeconomics. 2022;40:181–192. doi:10.1007/s40273-022-01202-1

13. Shah KK, Ramos-Goñi JM, Kreimeier S, Devlin NJ. An exploration of methods for obtaining 0= dead anchors for latent scale EQ-5D-Y values. Eur. J. Health Econ. 2020;21:1091–1103. doi:10.1007/s10198-020-01205-9

14. Attema, A.E., Lang, Z., Lipman, S.A.: Can differences between adult- and child-perspective health state utilities explain priority setting? https://drive.google.com/file/d/1tmbIsNH17tUXsXHaFlW6STpZn61c7TSn/view. Accessed 7 Jul 202310.1016/j.jval.2023.08.00237659690

15. Dewilde S, Janssen B, Lloyd A, Shah K. Exploration of the reasons why health state valuation differs for children compared to adults: a MIXED methods approach. Value Health. 2020;23:S677. doi:10.1016/j.jval.2020.08.1658

16. Lipman SA, Zhang L, Shah KK, Attema AE. Time and lexicographic preferences in valuation of EQ-5D-Y with time trade-off methodology. Eur J Health Econ. 2023;24:293–305. doi:10.1007/s10198-022-01466-6

17. Lipman, S.A., Reckers-Droog, V.T., Karimi, M., Jakubczyk, M., Attema, A.E.: Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health states. Eur. J. Health Econ. 22, 1507–1518 (2021)10.1007/s10198-021-01377-yPMC849245534611793

18. van Nooten FE, Koolman X, Brouwer WBF. The influence of subjective life expectancy on health state valuations using a 10 year TTO. Health Econ. 2009;18:549–558. doi:10.1002/hec.1385

19. Heintz E, Krol M, Levin LA. The impact of patients’ subjective life expectancy on time trade-off valuations. Med. Decis. Mak. 2013;33:261–270. doi:10.1177/0272989X12465673

20. Lipman, S.A., Brouwer, W.B.F., Attema, A.E.: Living up to expectations: Experimental tests of subjective life expectancy as reference point in time trade-off and standard gamble. J. Health Econ. (2020). 10.1016/j.jhealeco.2020.10231810.1016/j.jhealeco.2020.10231832229049

21. Lipman SA. Expect nothing: the (lack of) influence of subjective life expectancy on valuation of child health states. Front. Health Serv. 2022;2:10. doi:10.3389/frhs.2022.803109

22. Pliskin JS, Shepard D, Weinstein MC. Utility functions for life years and health status. Oper Res. 1980;28:206–224. doi:10.1287/opre.28.1.206

23. Attema AE, Brouwer WBF. On the (not so) constant proportional trade-off in TTO. Qual. Life Res. 2010;19:489–497. doi:10.1007/s11136-010-9605-9

24. Unic I, Stalmeier PF, Verhoef LC, van Daal WA. Assessment of the time-tradeoff values for prophylactic mastectomy of women with a suspected genetic predisposition to breast cancer. Med. Decis. Making. 1998;18:268–277. doi:10.1177/0272989X9801800303

25. Matza LS, Boye KS, Feeny DH, Bowman L, Johnston JA, Stewart KD, McDaniel K, Jordan J. The time horizon matters: results of an exploratory study varying the timeframe in time trade-off and standard gamble utility elicitation. Eur. J. Health Econ. 2015;8:979–990. doi:10.1007/s10198-015-0740-7

26. Stiggelbout AM, Kiebert GM, Kievit J, Leer JW, Habbema JD, De Haes JC. The “utility” of the Time Trade-Off method in cancer patients: feasibility and proportional Trade-Off. J. Clin. Epidemiol. 1995;48:1207–1214. doi:10.1016/0895-4356(95)00011-R

27. Martin AJ, Glasziou PP, Simes RJ, Lumley T. A comparison of standard gamble, time trade-off, and adjusted time trade-off scores. Int. J. Technol Assess Health Care. 2000;16:137–147. doi:10.1017/S0266462300161124

28. Dolan P, Stalmeier PFM. The validity of time trade-off values in calculating QALYs: constant proportional time trade-off versus the proportional heuristic. J. Health Econ. 2003;22:445–458. doi:10.1016/S0167-6296(02)00120-0

29. Attema AE, Brouwer WBF. Constantly proving the opposite? A test of CPTO using a broad time horizon and correcting for discounting. Qual. Life Res. 2012;21:25–34. doi:10.1007/s11136-011-9917-4

30. Bleichrodt H, Johannesson M. The validity of QALYs: an empirical test of constant proportional tradeoff and utility independence. Med. Decis. Mak. 1997;17:21–32. doi:10.1177/0272989X9701700103

31. van der Pol M, Roux L. Time preference bias in time trade-off. Eur. J. Health Econ. 2005;6:107–111. doi:10.1007/s10198-004-0265-y

32. Attema AE, Brouwer WBF. The value of correcting values: influence and importance of correcting TTO scores for time preference. Value Health. 2010;13:879–884. doi:10.1111/j.1524-4733.2010.00773.x

33. van Osch SM, Wakker PP, van den Hout WB, Stiggelbout AM. Correcting biases in standard gamble and time tradeoff utilities. Med. Decis. Mak. 2004;24:511–517. doi:10.1177/0272989X04268955

34. Bleichrodt H. A new explanation for the difference between time trade-off utilities and standard gamble utilities. Health Econ. 2002;456:447–456. doi:10.1002/hec.688

35. Attema, A.E., Lipman, S.A.: Decreasing impatience for health outcomes and its relation with healthy behavior. Front Appl Math Stat. 4 (2018)

36. Rau HA. Time preferences in decisions for others. Econ Lett. 2021;200:109766. doi:10.1016/j.econlet.2021.109766

37. Miyamoto JM, Eraker SA. A multiplicative model of the utility of survival duration and health quality. J. Exp. Psychol. Gen. 1988;117:3–20. doi:10.1037/0096-3445.117.1.3

38. Versteegh M, Vermeulen K, Evers SMAA, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19:343–352. doi:10.1016/J.JVAL.2016.01.003

39. Attema AE, Bleichrodt H, Wakker PP. A direct method for measuring discounting and QALYs more easily and reliably. Med. Decis. Mak. 2012;32:583–593. doi:10.1177/0272989X12451654

40. Attema AE, Brouwer WBF. Can we fix it? Yes we can! But what? A new test of procedural invariance in TTO-measurement. Health Econ. 2008;17:877–885. doi:10.1002/hec.1315

41. Attema AE, Brouwer WBF. The correction of TTO-scores for utility curvature using a risk-free utility elicitation method. J. Health Econ. 2009;28:234–243. doi:10.1016/j.jhealeco.2008.10.004

42. Attema AE, Brouwer WBF. The way that you do it? An elaborate test of procedural invariance of TTO, using a choice-based design. Eur. J. Health Econ. 2012;13:491–500. doi:10.1007/s10198-011-0318-y

43. Attema AE, Brouwer WBF. Deriving time discounting correction factors for TTO tariffs. Health Econ. 2014;23:410–425. doi:10.1002/hec.2921

44. Lipman SA, Attema AE, Versteegh MM. Correcting for discounting and loss aversion in composite time trade-off. Health Econ. 2022;31:1633–1648. doi:10.1002/hec.4529

45. Oppe M, Devlin NJ, van Hout B, Krabbe PFM, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17:445–453. doi:10.1016/J.JVAL.2014.04.002

46. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34:993–1004. doi:10.1007/s40273-016-0404-1

47. Alava MH, Pudney S, Wailoo A. The EQ-5D-5L value set for England: findings of a quality assurance program. Value Health. 2020;23:642–648. doi:10.1016/j.jval.2019.10.017

48. Attema AE, Bleichrodt H, L’Haridon O, Peretti-Watel P, Seror V. Discounting health and money: new evidence using a more robust method. J Risk Uncertain. 2018;56:117–140. doi:10.1007/s11166-018-9279-1

49. Lipman, S.A., Brouwer, W.B.F., Attema, A.E.: A QALY loss is a QALY loss is a QALY loss: a note on independence of loss aversion from health states. Eur. J. Health Econ. 20 (2019). 10.1007/s10198-018-1008-910.1007/s10198-018-1008-9PMC643893630229374

50. Attema AE. Developments in time preference and their implications for medical decision making. J. Oper. Res. Soc. 2012;63:1388–1399. doi:10.1057/jors.2011.137

51. Myerson J, Green L, Warusawitharana M. Area under the curve as a measure of discounting. J. Exp. Anal. Behav. 2001;76:235–243. doi:10.1901/jeab.2001.76-235

52. Lipman SA, Brouwer W, Attema AE. QALYs without bias? Non-parametric correction of time trade-off and standard gamble utilities based on prospect theory. Health Econ. 2019;8:843–854. doi:10.1002/hec.3895

53. OECD: No Title. https://stats.oecd.org/Index.aspx?datasetcode=EAG_NEAC

54. Van der Pol MM, Cairns JA. Negative and zero time preference for health. Health Econ. 2000;9:171–175. doi:10.1002/(SICI)1099-1050(200003)9:2<171::AID-HEC492>3.0.CO;2-Z

55. Wakker P, Deneffe D. Eliciting von Neumann–Morgenstern utilities when probabilities are distorted or unknown. Manag. Sci. 1996;42:1131–1150. doi:10.1287/mnsc.42.8.1131

56. Hardisty DJ, Weber EU. Discounting future green: Money versus the environment. J. Exp. Psychol. Gen. 2009;138:329–340. doi:10.1037/a0016433

57. Chapman GB. Temporal discounting and utility for health and money. J. Exp. Psychol. Learn. Mem. Cogn. 1996;22:771–791. doi:10.1037/0278-7393.22.3.771

58. Chapman GB. Expectations and preferences for sequences of health and money. Organ Behav. Hum. Decis. Process. 1996;67:59–75. doi:10.1006/obhd.1996.0065

59. Chapman GB. Preferences for improving and declining sequences of health outcomes. J. Behav. Decis. Mak. 2000;13:203–218. doi:10.1002/(SICI)1099-0771(200004/06)13:2<203::AID-BDM317>3.0.CO;2-S

60. Abdellaoui M, Gutierrez C, Kemel E. Temporal discounting of gains and losses of time: an experimental investigation. J. Risk Uncertain. 2018;57:1–28. doi:10.1007/S11166-018-9287-1/FIGURES/10

61. Story GW, Vlaev I, Seymour B, Winston JS, Darzi A, Dolan RJ. Dread and the disvalue of future pain. PLoS Comput. Biol. 2013;9:e1003335. doi:10.1371/journal.pcbi.1003335

62. Kirby KN, Marakovic NN. Delay-discounting probabilistic rewards: rates decrease as amounts increase. Psychon. Bull. Rev. 1996;3:100–104. doi:10.3758/BF03210748

63. Infurna FJ, Wiest M, Gerstorf D, Ram N, Schupp J, Wagner GG, Heckhausen J. Changes in life satisfaction when losing one’s spouse: individual differences in anticipation, reaction, adaptation and longevity in the German Socio-economic Panel Study (SOEP). Ageing Soc. 2017;37:899–934. doi:10.1017/S0144686X15001543

64. Rowen, D., Mukuria, C., Bray, N., Carlton, J., Longworth, L., Meads, D., O’Neill, C., Shah, K., Yang, Y.: Assessing the comparative feasibility, acceptability and equivalence of videoconference interviews and face-to-face interviews using the time trade-off technique. Soc Sci Med. 309, 115227 (2022)10.1016/j.socscimed.2022.11522735969979

65. Lipman SA. Time for tele-TTO? Lessons learned from digital interviewer-assisted time trade-off data collection. The Patient: Patient-Centered Outcomes Res. 2021;14:459–469. doi:10.1007/s40271-020-00490-z

66. Reckers-Droog V, Karimi M, Lipman S, Verstraete J. Why do adults value EQ-5D-Y-3L health states differently for themselves than for children and adolescents: a think-aloud study. Value Health. 2022;25:1174–1184. doi:10.1016/j.jval.2021.12.014

[^1]: The complete set of instructions is presented in Appendix A. The survey can be found here: <https://referencepoints.shinyapps.io/GapDuration/>.

[^2]: However, other older studies also found little to no discounting on the aggregate level \[54\].
