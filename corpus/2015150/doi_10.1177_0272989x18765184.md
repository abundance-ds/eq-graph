---
project_id: "2015150"
work_id: "doi:10.1177/0272989x18765184"
doi: "10.1177/0272989X18765184"
pmid: "29629848"
pmcid: "PMC6587359"
title: "Setting Dead at Zero: Applying Scale Properties to the QALY Model"
journal: "Medical Decision Making"
publication_date: "2018-04-09"
volume: "38"
issue: "6"
authors:
  - name: "Bram Roudijk"
  - name: "A. Rogier T. Donders"
  - name: "Peep F.M. Stalmeier"
affiliations:
  - id: "aff1-0272989X18765184"
    name: "Department for Health Evidence, Radboud University Medical Center, Radboud Institute for Health Sciences, Nijmegen, Gelderland, the Netherlands"
  - id: "aff2-0272989X18765184"
    name: "Department for Health Evidence, Radboud University Medical Center, Radboud Institute for Health Sciences, Nijmegen, Gelderland, the Netherlands"
  - id: "aff3-0272989X18765184"
    name: "Department for Health Evidence, Radboud University Medical Center, Radboud Institute for Health Sciences, Nijmegen, Gelderland, the Netherlands"
keywords:
  - "QALY"
  - "death"
  - "health measure"
  - "health states"
  - "quality of life"
  - "quality-adjusted life year"
  - "scaling"
licence: "cc-by-nc"
licence_url: "http://creativecommons.org/licenses/by-nc/4.0/"
source_file: "input/projects/2015150/papers/doi_10.1177_0272989x18765184.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6587359/fullTextXML"
source_method: "epmc_xml"
source_sha256: "282bd855497b9d23b9a0f3965f0d22fe6f8923cc26a85e0be344de53fa3728bf"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Setting Dead at Zero: Applying Scale Properties to the QALY Model

## Abstract

**Introduction.** Scaling severe states can be a difficult task. First, the method of measurement affects whether a health state is considered better or worse than dead. Second, in discrete choice experiments, different models to anchor health states on 0 (dead) and 1 (perfect health) produce varying amounts of health states worse than dead. **Research Question.** Within the context of the quality-adjusted life year (QALY) model, this article provides insight into the value assigned to dead and its consequences for decision making. Our research questions are 1) what are the arguments set forth to assign dead the number 0 on the health–utility scale? And 2) what are the effects of the position of dead on the health–utility scale on decision making? **Methods.** A literature review was conducted to explore the arguments set forth to assign dead a value of 0 in the QALY model. In addition, scale properties and transformations were considered. **Results.** The review uncovered several practical and theoretical considerations for setting dead at 0. In the QALY model, indifference between 2 health episodes is not preserved under changes of the origin of the duration scale. Ratio scale properties are needed for the duration scale to preserve indifferences. In combination with preferences and zero conditions for duration and health, it follows that dead should have a value of 0. **Conclusions.** The health–utility and duration scales have ratio scale properties, and dead should be assigned the number 0. Furthermore, the position of dead should be carefully established, because it determines how life-saving and life-improving values are weighed in cost–utility analysis.

The quality-adjusted life year (QALY) model provides one of the most popular health measures in health economics and clinical research. The QALY model combines quality of life and survival into a single measure and is often used in cost–utility studies, in which decision makers model which treatment is best. Usually, the QALY model is represented mathematically as $`QALY = v(Q) \ast w(T)`$.<sup>1,2</sup> In this model, $`v(Q)`$ represents the utility assigned to a health state $`(Q)`$, and $`w(T)`$ is a function of duration $`(T)`$. Health states are operationalized as written descriptions of a disease, or a profile of a multiattribute instrument such as the EQ-5D or the Health Utility Index (HUI). Utility is assigned to health states using valuation methods such as the time trade-off (TTO), standard gamble (SG), Visual Analogue Scale (VAS), better than dead (BTD), or discrete choice experiments (DCEs).<sup>3–5</sup>

In most studies, the health–utility scale is anchored on 0 (dead) and 1 (perfect health). Health states considered worse than dead have negative utility values on this scale, and health states considered better than dead have a positive utility value. Rank ordering health states close to dead is problematic, because it depends on the measurement method whether a health state is considered better or worse than dead.<sup>6–7</sup> In other words, the relative position of dead on the rank order is subject to uncertainty due to the choice of measurement method. Another source of uncertainty regarding the position of dead can be identified. In DCEs, paired comparisons of health states allow for a rank ordering of health states. This is used to assign cardinal values to health states by using random utility models.<sup>8</sup> There are several models to anchor DCE data on (dead) 0 and (perfect health) 1 in the EQ-5D or other health–utility valuation studies.<sup>9–11</sup> Even within the same valuation study, however, each of these models leads to a different position of dead, resulting in varying amounts of health states that are considered worse than dead. Again, the relative position of dead on the rank order varies, but this is now due to uncertainty about the choice of random utility model.

The variation in the rank order position of dead causes variation in the values of health states on the health–utility scale. For example, to assess whether health states are positive or negative, the origin of the health–utility scale needs to be established. In some valuation methods such as TTO, SG, and BTD, it seems obvious to assign a value of 0 to dead, because health states are directly compared to dead. For example, in TTO, a health state is considered equal to dead if it is considered equal to 0 years in perfect health, and dead is then assigned a value of 0. For other methods such as the DCE, setting dead at 0 seems less obvious because health states are not directly compared to dead.

DCE valuations of health states produce a latent scale for health utilities that does not directly incorporate dead.<sup>9</sup> Equally important, however, are the theoretical considerations regarding the position of dead, which will be the focus of this article. Because DCE is becoming a more popular valuation method for health states, with substantial benefits regarding data collection, it is important to improve our understanding of the position of dead on the health–utility scale. Two research questions are formulated: 1) what are the arguments set forth to assign dead the number 0 on the health–utility scale, and 2) what are the effects of the position of dead on the health–utility scale on decision making? To accomplish this purpose, a literature review is conducted to explore the arguments put forward for setting dead at 0 on the health–utility scale. Furthermore, the effect of alternative values for dead on decision making with the QALY model is examined.

## Literature Review

A literature review was conducted to explore the arguments set forth for anchoring the QALY model at dead (0) and perfect health (1). Six literature databases were examined: PubMed, Embase, Web of Science, PsycINFO, EconLit, and Cochrane. These databases span literature in the 3 most important domains for quality of life and health economic research: the biomedical, psychological, and economic sciences. The search strategy for each of these databases can be found in [Supplementary Appendix A](http://journals.sagepub.com/doi/suppl/10.1177/0272989X18765184).

The search strategy resulted in the identification of 3873 papers, of which 1697 were duplicates, leaving 2176 papers to be further evaluated. In the next phase, 2082 papers were excluded because their title was irrelevant to the subject of this review, dealing with applied economic evaluations of treatments or medicines. Thus, a selection of 94 papers remained, of which 53 more papers were excluded based on their abstracts, dealing mainly with EQ-5D valuation studies and studies on utility assessment; 41 papers were read in the review. For final inclusion in the review, papers, books, or theses should at least be on a topic related to the QALY model, health utilities, scale properties, or methods for the elicitation of health utilities. An overview of the search results is provided in <a href="#table1-0272989X18765184" data-ref-type="table">Table 1</a>.

<div id="table1-0272989X18765184" class="table-wrap">

<div class="caption">

Results of the Literature Search, by Database and Phase

</div>

![](10.1177_0272989X18765184-table1.jpg)

|                                     | Number of papers |
|:------------------------------------|------------------|
| PubMed                              | 995              |
| Embase                              | 1712             |
| Web of Science                      | 1014             |
| PsycINFO                            | 102              |
| EconLit                             | 47               |
| Cochrane                            | 3                |
| **Total**                           | **3873**         |
| Duplicates                          | 1697             |
| **Total after removing duplicates** | **2176**         |
| Removed after reading titles        | 2082             |
| **Remaining**                       | **94**           |
| Removed after reading abstracts     | 53               |
| **Remaining**                       | **41**           |
| Excluded after reading paper        | 34               |
| **Included for final review**       | **7**            |

</div>

Because a literature review in electronic databases leads to the inclusion of research papers and does not include other sources, an additional selection of 11 health economic and decision analytical handbooks is included in our review, as well as 5 PhD theses.

Out of the papers, books, and theses that were included in the final selection, some papers provided arguments or comments dealing with topics related to setting dead to 0. An overview is provided in <a href="#table2-0272989X18765184" data-ref-type="table">Table 2</a>. Furthermore, for inclusion in the final review, the paper, book, or thesis must touch on the topic of anchoring the health–utility scale or QALY model. Literature on measurement theory is included if it is on scale anchoring, related to the topic of research. Literature was excluded if these criteria were not met, or if the paper was unavailable or only available in a language other than English.

<div id="table2-0272989X18765184" class="table-wrap">

<div class="caption">

Arguments Identified by the Literature Review or the Books and PhD Theses Review

</div>

![](10.1177_0272989X18765184-table2.jpg)

| Argument | Source |
|:---|:---|
| Dead and good health are anchored at 0 and 1 by definition or for convenience. | Found in multiple studies (Refs.<sup>6,10,12</sup>) and is common in the literature |
| “To estimate utility values for each health state defined by a classification system, the results of the TTO study are modelled using multivariate regression. The disutility coefficient for each severity level of each dimension is calculated using level 1 (no problem) as the baseline. Therefore, full health is anchored at 1, and the utility value for each overall health state is calculated by subtracting the disutility value for each dimension from 1.”<sup>13</sup> (*It is convenient to assign perfect health the value 1, because it makes the calculation of utility values based on TTO results easier. When using multivariate regression, disutility is simply subtracted from full health for each dimension of health.—BR*)<sup><a href="#table-fn1-0272989X18765184" data-ref-type="table-fn">a</a></sup> | Mulhern et al. (2014) |
| “We set H(FH)=1 and U(death)=0, which is allowed by the uniqueness properties of U.”<sup>14</sup> (*Here, U denotes the QALY model and H(FH) denotes the value of full health on the health–utility scale.—BR*) | Bleichrodt et al. (2002) |
| “If the preference weights do not produce utility values on the full health-dead scale they cannot be used in economic evaluation using cost per QALY analysis.”<sup>15</sup> | Brazier et al. (2012) |
| The anchoring of DCE data on the 0–1 dead–full health scale is problematic. Four different methods are tested, and all provide varying amounts of health states considered WTD.<sup>9</sup> | Norman et al. (2016) |
| Using dead as a health state in DCE is problematic, because this might lead to a violation of the random utility model that is used to assign values to health states.<sup>16</sup> | Flynn et al. (2008) |
| For single-attribute health measures, a 0 (dead) to 1 (best health imaginable) scale is preferable, because it corresponds to the utilities and probabilities of basic reference lotteries (like SG). This is extended to multiattribute health measures such as the QALY.<sup>17</sup> | Weinstein and Fineberg (1980) (book) |
| “In the measurement of such attributes as attitudes, esthetics, preferences, and value, the natural origin occurs within the series and can be described as a neutral point such that all stimuli or individuals in one direction are favourable, pleasant, liked, or wanted as the case may be, whereas all those on the other side are unfavourable, unpleasant, disliked or not wanted.”<sup>18</sup> (*Dead could function as such a neutral zero point that divides all health states between desirable and undesirable.—BR*) | Torgerson (1958) (book) |
| Using 0 (dead) and 1 (perfect health) as anchors makes QALYs comparable to survival analyses. “Partly by convention but principally as a consequence of the data requirements of the analytic methods used, for example in the quality adjustment of survival, the unit interval of health is defined in terms of the distance between full health and death, valued as 1 and 0, respectively.”<sup>19</sup> | Macran and Kind (2001)<sup><a href="#table-fn2-0272989X18765184" data-ref-type="table-fn">b</a></sup> |
| The zero-condition papers by Miyamoto et al.<sup>1</sup> and Bleichrodt et al.<sup>20</sup> make no explicit assumption that dead should have a value of 0, merely stating that individuals are indifferent between health states if the duration of such a health episode is 0. | Miyamoto et al. (1998) and Bleichrodt et al. (1997)<sup><a href="#table-fn2-0272989X18765184" data-ref-type="table-fn">b</a></sup> |

Author comments for clarification are reported in italics.

Arguments that were not identified by the literature review but were identified by the authors as other relevant papers.

</div>

## Scale Properties and Decision Making

In addition to the arguments found above, we examine whether scale types can provide more arguments for setting dead at 0. First, we provide a short exposition of ratio and interval scales. Second, we provide an example that shows that, in the QALY model, the duration scale $`w(T)`$ has ratio scale properties. Then, we apply the “zero condition” to derive that for a duration of 0 years, $`w(0) = 0`$.<sup>1</sup> Next, the indifference between $`\left. (Q,0) \right.\sim({Dead},T)`$ implies that $`v({Dead})`$ should equal 0. This in turn implies that the health–utility scale has ratio scale properties as well.

### Scale Properties

The QALY model is a utility function containing duration and health as attributes.<sup>2</sup> Utilities for expected utility calculations should have interval-scale properties, which will be defined later.<sup>21</sup> Below, interval and ratio scale types are considered, followed by their consequences for the QALY model and the position of dead.

Following Torgersen, measurement entails the assignment of numbers to objects to represent the degree of some common property of the objects.<sup>18</sup> The order of these numbers corresponds to the magnitude of the objects’ property. On interval scales, the size of the numeric difference between pairs of the objects is meaningful. These so-called intervals reflect the distance between different amounts of the objects’ properties.<sup>18</sup> An example of an interval scale is the Celsius temperature scale. On this scale, the difference between 10 and 20 °C is equal to the difference between 30 and 40 °C.<sup>[^1]</sup> Coombs et al.<sup>22</sup> show that values on an interval scale can be linearly transformed by $`f(x) = {ax} + b,\forall a > 0`$ while preserving interval scale properties. In this transformation, the interval scale has an arbitrary origin ($`b`$) and unit of measurement ($`a`$). The arbitrary origin suggests that, on an interval scale, dead can be assigned any number, including 0.

On interval scales, the distances between the objects on the scale are meaningful. On ratio scales, the numbers themselves, assigned to the objects, are meaningful, because they correspond to the distance of the object from the natural origin.<sup>18</sup> An example of a ratio scale is the metric system of length, in which it is possible to state that an object with a length of 2 m is twice as long as an object with a length of 1 m. This assertion is possible because the origin is not arbitrary, as on interval scales; ratio scales have a natural origin, which means that an object of length 0 should be assigned the number 0 on the length scale. Statements about ratios are enabled by the natural 0, and ratio scales can be only multiplicatively transformed, $`f(x) = {ax},\forall a > 0`$, while preserving ratio scale properties.<sup>22</sup> An example of such a transformation is converting meters to yards, where only the unit of measurement $`(a)`$ is changed.

### Scale Transformations, Indifference, and the QALY Model

The different properties of ratio and interval scales may affect QALY calculations differently. To illustrate whether scale transformations in the QALY model leave decisions invariant, examples are provided in <a href="#fig1-0272989X18765184" data-ref-type="fig">Figure 1</a>. Suppose that a respondent is indifferent between 2 health episodes A and B, as in <a href="#fig2-0272989X18765184" data-ref-type="fig">Figure 2</a>. Episode A yields 10 years in perfect health, followed by 10 years in a mild state. Episode B yields 15 years in perfect health, followed by 5 years in a moderate state. If we apply the standard health–utility scale with values 0 (dead) and 1 (perfect health) together with the QALY model, $`U(Q,T) = v(Q)*w(T)`$, where $`w(T) = T`$, we can see that for an indifferent respondent, $`\left( 10*1 + 10*v({Mild}) = 15*1 + 5*v({Moderate}) \right)`$; it follows that $`v({Mild}) = \frac{1}{2} + \frac{v({Moderate})}{2}`$. Let’s set $`v({Mild}) = 0.7`$ and $`v({Moderate}) = 0.4`$, so both episodes yield 17 QALYs. This agrees with the respondents’ indifference.

<figure id="fig1-0272989X18765184">
<p><img src="10.1177_0272989X18765184-fig1.jpg" /></p>
<figcaption>Different quality-adjusted life year (QALY) values after performing scale transformations on the value <span class="math inline"><em>w</em>(<em>T</em>)</span> of the duration axis.</figcaption>
</figure>

<figure id="fig2-0272989X18765184">
<p><img src="10.1177_0272989X18765184-fig2.jpg" /></p>
<figcaption>The decision maker is indifferent between 2 options, A and B.</figcaption>
</figure>

Before discussing the health–utility scale $`v(Q)`$, we shall first discuss the duration scale $`w(T).`$ Suppose that the duration scale $`w(T)`$ is an interval scale, so that we can make an interval scale transformation by adding 2 to every value of $`w(T)`$ to construct $`w(T) = T + 2`$, as in row B of <a href="#fig1-0272989X18765184" data-ref-type="fig">Figure 1</a>. After this transformation, episode A yields 20.4 QALYs, whereas episode B yields 19.8 QALYs, and they no longer represent the respondents’ indifference. In other words, when interval scale transformations are applied to the duration scale, the QALY model no longer represents indifferences. After the transformation as in the example, $`w(0) = 2`$. This means that periods of 0 duration generate nonzero amounts of QALYs. Furthermore, under interval scale transformations, it is impossible to split $`w(2T)`$ into 2 equal parts, because $`w(2T) \neq w(T) + w(T)`$, because $`2T + 2 \neq (T + 2) + (T + 2)`$. This holds for any linear transformation $`f\left( w(T) \right) = {aw}(T) + b,\forall a,b \neq 0.`$ These observations suggest that interval scale properties are not sufficient.

Row C of <a href="#fig1-0272989X18765184" data-ref-type="fig">Figure 1</a> is meant to illustrate that, on ratio scales, indifferences do not change under ratio scale transformations. As stated before, ratio scales permit only positive multiplicative transformations. Row C of <a href="#fig1-0272989X18765184" data-ref-type="fig">Figure 1</a> provides an illustration of such a transformation. Again, we use health episodes A and B, as in <a href="#fig2-0272989X18765184" data-ref-type="fig">Figure 2</a>, and apply the QALY model. Let us now assume that the duration scale is a ratio scale and apply a ratio scale transformation by multiplying all values on the duration scale by 2 to construct $`w(T) = 2*T`$, as in row C of <a href="#fig1-0272989X18765184" data-ref-type="fig">Figure 1</a>. Episodes A and B now yield $`34`$ QALYs each, which represents the respondents’ indifference. In other words, the indifference between 2 health episodes is preserved by the ratio scale transformation.

Summarizing, the examples above show that interval scale transformations on the duration scale do not leave QALY indifferences invariant. Instead, ratio scale transformations are necessary to preserve the indifferences calculated with the QALY model. Therefore, $`w(T)`$ needs to have ratio scale properties.

### Anchoring Duration at 0

Next, an argument is given for setting the value of a duration of 0 years at 0. The zero condition by Miyamoto et al. states that all health states are equally preferred when the duration of those health episodes is 0, or $`\left. (Q,0\ {years}) \right.\sim(Q',0\ {years}).`$<sup>1</sup> Then, by the QALY model, $`v(Q)*w(0) = v(Q')*w(0)`$, while $`v(Q) \neq v(Q')`$, which means that $`w(0\ {years}) = 0.`$ Therefore, $`w(0) = 0`$, which establishes the 0 needed for the ratio scale $`w(T)`$.

### Anchoring Dead at 0

To set dead to 0, consider 2 health episodes: 1 episode $`(Q,0)`$ is being in health state $`Q`$ for 0 years, followed by dead. The other episode $`({Dead},T)`$ is being dead for some unknown duration $`T \neq 0`$. It is reasonable to assume that respondents are indifferent between these health episodes, that is, $`\left. ({Dead},T) \right.\sim(Q,0)`$. This indifference, for instance, also occurs in the TTO, where 0 years in good health is considered as equal to dead. It follows that $`U({Dead},T) = U(Q,0)`$. By the QALY model, $`U(Q,0)`$ yields 0 QALYs because $`v(Q)*w(0) = v(Q)*0 = 0`$. This implies that $`v({Dead})*w(T) = 0`$, $`T \neq 0`$, and it follows that $`v({Dead}) = 0.`$Thus, dead should be assigned the number 0 on the health–utility scale.

In the reasoning above, we have set 0 years at 0, using the zero condition for duration.<sup>1</sup> In essence, this zero condition asks which duration nullifies health differences. Symmetrically, one may ask which health state nullifies time differences, a zero condition for health. When considering $`\left. \left( {Dead},T_{1} \right) \right.\sim\left( {Dead},T_{2} \right)`$, for $`T_{1} \neq T_{2}`$ it is reasonable to assume that dead nullifies duration differences and, by the QALY model, should be assigned the number 0.

### Scale Properties of the QALY Model

To summarize, the position of dead is fixed at 0; thus, additive transformations changing the value of dead are not allowed. Therefore, the health–utility scale has ratio scale properties, just like the duration scale. This is required because the QALY model is a multiplicative model, implying that both the duration and the health–utility scale must have ratio scale properties. Only when both scales have a true natural 0 will the multiplication be logically meaningful.<sup>23</sup> With dead and a duration of 0 years being assigned the number 0 on the 2 scales, this criterion is met.

### The Position of Dead Relative to Other Health States

So far, we have discussed the effects of linear and multiplicative transformations of the duration scale $`w(T)`$ and shown that dead must have a value of 0. The position of dead relative to other health states is, however, also important. To illustrate this, 2 health–utility scales are drawn in <a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a>, on which the position of dead differs relative to the other health states. In <a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a> (top), dead is located relatively close to perfect health; in <a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a> (bottom), dead is located relatively far away from perfect health. The value of dead is 0, and values for other health states change accordingly. <a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a> (top) leads to an emphasis on life-improving treatments, because the value gain between perfect health and dead is small compared to gains for other health states. <a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a> (bottom) leads to an emphasis on life-saving treatments, because the value gain from dead to perfect health is relatively large compared to other health states. Thus, the position of dead relative to other health states weighs the importance of life-saving and life-improving values, which affect the results of cost–utility studies.

<figure id="fig3-0272989X18765184">
<p><img src="10.1177_0272989X18765184-fig3.jpg" /></p>
<figcaption>Position of dead on the health–utility scale. (Top) A health–utility scale with an emphasis on life-improving treatments. (Bottom) A health–utility scale with an emphasis on life-saving treatments. These figures illustrate altered priorities when the position of dead changes relative to other health states. In the top figure, the quality-adjusted life year (QALY) gain from dead to perfect health is smaller than the gain from HS1 (health state 1) to perfect health; in the bottom figure, it is larger.</figcaption>
</figure>

<a href="#fig3-0272989X18765184" data-ref-type="fig">Figure 3</a> also illustrates the importance of getting the ordinal position of dead right. This position determines the amount of health states considered worse than dead. Negative values are assigned to health states worse than dead, indicating that shorter durations are preferred to longer durations for these health states. This means that the ordinal position of dead again affects cost–utility analyses and as a consequence the allocation of resources in health care.

## Discussion

The main findings of this article consist of the arguments found in the literature review, the arguments derived from the scale properties of the health–utility and duration scales of the QALY model, and the effect of the position of dead on decision making. The arguments from the literature review can be divided into practical arguments and theoretical arguments. The most common practical argument simply says that dead is anchored at 0 by definition or for convenience, or mentions that it is possible to do so. Other practical arguments explain why anchoring dead at 0 and perfect health at 1 is convenient in cost–utility analyses, a common application of the QALY. One example is that these anchors make the QALY comparable to survival analyses, and another example is that these anchors allow for a convenient calculation of QALYs by subtracting disutility from perfect health.<sup>13,15,19</sup> A theoretical argument from the literature is that it is possible, but not necessary, to assign the number 0 to dead due to the uniqueness property of the QALY model.<sup>20</sup>

Scale properties provide additional arguments for assigning the value 0 to dead. First, interval scale properties for the duration scale are not sufficient for QALY calculations. Specifically, applying interval scale transformations to the duration scale misrepresents the preferences of a respondent indifferent between 2 health episodes. Instead, ratio scale properties are necessary for the duration scale to calculate QALYs. This also holds for the health–utility scale. Second, we show that $`w(0\ {years}) = 0`$, and $`v\left( {Dead} \right) = 0`$, under the following assumptions: 1) that $`{QALY} = v(Q)*w(T)`$, 2) that indifference between episodes implies equal QALYs for both episodes, 3) the zero condition for duration, and 4) that $`\left. (Q,0) \right.\sim({Dead},T)`$ or, alternatively, the zero condition for health.

Regarding our second research question, the position of dead strongly affects decision making. It determines the trade-off between life-saving and life-improving interventions. Furthermore, it determines which states are negative, with the accompanying notion of preferences for shorter durations.

### Limitations and Strengths

One of the limitations of this study is that potentially relevant information was not presented in the titles and abstracts of the electronic literature that was searched. Because the topic of research is relatively unexplored, more information might have been found in full texts. Another limitation is that the book and PhD theses review was limited due to practical constraints. Be that as it may, the health economic handbooks that we did examine did not provide relevant arguments.

A strength of this study is the literature on measurement theory that provided relevant information. Another strength of this study is that we address our topic through a literature search as well as a theoretical analysis. In addition, multiple literature databases were searched for relevant electronic literature, which decreases the probability of missing relevant literature.

### Relation to Other Studies

A study by Prieto and Sacristan also concludes that the health–utility scale should have ratio scale properties.<sup>24</sup> Prieto and Sacristan state that ratio scale properties are needed for the health–utility scale, because ratios between QALYs calculated for 2 different health episodes are not invariant under interval scale transformations of the health–utility scale.<sup>24</sup> There are some differences between Prieto and Sacristan’s reasoning and ours. Our reasoning starts from the duration scale, and our aim is to establish the origin of the health–utility scale. Prieto and Sacristan instead start from the health–utility scale and are not concerned with the origin of scales.

### Implications for Research

For decision making, the position of dead relative to other health states is critical. The ordinal position of dead determines the amount of health states considered worse than dead and the trade-off between life-saving and life-improving values. In practice, the position of dead is determined by the choice of model and the choice of valuation method. Some valuation methods value states using dead, for example TTO, SG, and BTD.<sup>5,12</sup> The position of dead is then fixed, and health states are positioned on the health–utility scale relative to dead. These methods establish positive and negative health states in a more or less straightforward way.

In DCEs, setting dead at zero is less straightforward because health states are not compared to dead. Different models to incorporate dead into DCEs lead to varying results, and it is unclear which model should be preferred.<sup>9,25,26</sup> We have shown that dead needs to have the value 0 in the QALY model, but we also argue that the ordinal position of dead needs to be carefully established. Then, for DCEs, more attention should be given to anchoring dead relative to other health states. Although our study highlights the importance of getting the relative position of dead right, it does not provide a direct solution for the problems related to discrete choice experiments.

## Conclusion

This article provides insight into the arguments for setting dead at 0 in the QALY model and the effects of the position of dead on decision making. Our main conclusions are that both the health–utility scale and duration scale should have ratio scale properties and that dead should be assigned the value 0, via preferences and the 2 zero conditions. The position of dead relative to other health states should be carefully established, because it weighs the relative contribution of life-saving and life-improving values in cost–utility analyses and separates positive and negative health states. Given that dead is the origin of the health–utility scale, measurement methods comparing health states to dead should, in our opinion, receive more attention.

## Supplemental Material

<div class="caption">

###### DS_10.1177_0272989X18765184 – Supplemental material for Setting Dead at Zero: Applying Scale Properties to the QALY Model

</div>

<div class="caption">

Click here for additional data file.

</div>

Supplemental material, DS_10.1177_0272989X18765184 for Setting Dead at Zero: Applying Scale Properties to the QALY Model by Bram Roudijk, A. Rogier T. Donders, and Peep F.M. Stalmeier in Medical Decision Making

The authors thank Eddy Adang, Balder Stalmeier, Richard Norman, and 3 anonymous reviewers for helpful suggestions and comments on an earlier draft of this article.

## References

1. MiyamotoJMet al The zero-condition: a simplifying assumption in QALY measurement and multiattribute utility. Manage Sci. 1998;44(6):839–49.

2. PliskinJSShepardDSWeinsteinMC. Utility functions for life years and health status. Oper Res. 1980;28(1):206–24.

3. FrobergDGKaneRL. Methodology for measuring health-state preferences—II: scaling methods. J Clin Epidemiol. 1989;42(5):459–71.10.1016/0895-4356(89)90136-42732774

4. SalomonJA. Reconsidering the use of rankings in the valuation of health states: a model for estimating cardinal values from ordinal data. Popul Health Metr. 2003;1(1):12.1468741910.1186/1478-7954-1-12PMC344742

5. van HoornRet al The better than dead method: feasibility and interpretation of a valuation study. PharmacoEconomics. 2014;32(8):789–99.10.1007/s40273-014-0168-424846761

6. StalmeierPFet al The gap effect: discontinuities of preferences around dead. Health Econ. 2005;14(7):679–85.10.1002/hec.98615744750

7. RobinsonADolanPWilliamsA. Valuing health status using VAS and TTO: what lies behind the numbers? Soc Sci Med. 1997;45(8):1289–97.10.1016/s0277-9536(97)00057-99381241

8. LouviereJJLancsarE. Choice experiments in health: the good, the bad, the ugly and toward a brighter future. Health Econ Policy Law. 2009;4(04):527–46.10.1017/S174413310999019319715635

9. NormanRMulhernBVineyR. The impact of different DCE-based approaches when anchoring utility scores. PharmacoEconomics. 2016;34(8):805–14.10.1007/s40273-016-0399-727034244

10. StolkEAet al Discrete choice modeling for the quantification of health states: the case of the EQ-5D. Value Health. 2010;13(8):1005–13.10.1111/j.1524-4733.2010.00783.x20825618

11. FlynnTNet al Rescaling quality of life values from discrete choice experiments for use as QALYs: a cautionary tale. Popul Health Metr. 2008;6(1):6.1894535810.1186/1478-7954-6-6PMC2599891

12. TorranceGWThomasWHSackettDL. A utility maximization model for evaluation of health care programs. Health Serv Res. 1972;7(2):118.5044699PMC1067402

13. MulhernBet al Preparatory study for the revaluation of the EQ-5D tariff: methodology report. Health Technol Assess. 2014;18(12):vii–xxvi,1–191.10.3310/hta18120PMC478120424568945

14. BleichrodtH. A new explanation for the difference between time trade-off utilities and standard gamble utilities. Health Econ. 2002;11(5):447–56.10.1002/hec.68812112493

15. BrazierJet al Comparison of health state utility values derived using time trade-off, rank and discrete choice data anchored on the full health-dead scale. Eur J Health Econ. 2012;13(5):575–87.10.1007/s10198-011-0352-921959651

16. FlynnTNet al Rescaling quality of life values from discrete choice experiments for use as QALYs: a cautionary tale. Popul Health Metr. 2008;6:6.1894535810.1186/1478-7954-6-6PMC2599891

17. WeinsteinMCFinebergHV. Clinical Decision Analysis. Philadelphia: Saunders; 1980.

18. TorgersonWS. Theory and Methods of Scaling. New York: John Wiley; 1958.

19. MacranSKindP. “Death” and the valuation of health-related quality of life. Med Care. 2001;39(3):217–27.10.1097/00005650-200103000-0000311242317

20. BleichrodtHWakkerPJohannessonM. Characterizing QALYs by risk neutrality. J Risk Uncertainty. 1997;15(2):107–14.

21. Von NeumannJMorgensternO Theory of Games and Economic Behavior. Princeton: Princeton University Press; 2007.

22. CoombsCHDawesRMTverskyA. Mathematical Psychology: An Elementary Introduction. Englewood Cliffs (NJ): Prentice Hall; 1970.

23. SchmidtFL. Implications of a measurement problem for expectancy theory research. Org Behav Human Perf. 1973;10(2):243–51.

24. PrietoLSacristánJA. Problems and solutions in calculating quality-adjusted life years (QALYs). Health Qual Life Outcomes. 2003;1(1):80.1468742110.1186/1477-7525-1-80PMC317370

25. Ramos-GoñiJMet al Dealing with the health state ‘dead’ when using discrete choice experiments to obtain values for EQ-5D-5L health states. Euro J Health Econ. 2013;14(1):33–42.10.1007/s10198-013-0511-2PMC372844123900663

26. NormanRCroninPVineyR. A pilot discrete choice experiment to explore preferences for EQ-5D-5L health states. Appl Health Econ Health Pol. 2013;11(3):287–98.10.1007/s40258-013-0035-z23649892

[^1]: It is wrong, however, to state that 40 °C is twice as warm as 20 °C, whereas on a ratio scale it is possible to make such statements.
