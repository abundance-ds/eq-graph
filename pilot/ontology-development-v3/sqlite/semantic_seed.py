"""Curated semantic seed for the source-checked SQLite pilot."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


STUDIES = {
    "H01": ("German national EQ-5D-5L valuation study", "used"),
    "H02": ("Australian DCE design and respondent-engagement study", "used"),
    "H03": ("German OPUF test-retest reliability study", "used"),
    "H04": ("QID-12 instrument-development study", "mentioned-only"),
    "H05": ("EQ-HWB proxy-perspective study in residential aged care", "used"),
    "H06": ("Swedish adolescent population-health study", "used"),
    "H07": ("Asian preference-based-measure measurement-property review", "used"),
    "H08": ("Chichewa EQ-5D-Y psychometric study", "used"),
    "H10": ("EQ-5D-5L decision-aid visualization study", "used"),
    "H11": ("Cultural values and self-reported health study", "none-reported"),
}

CLASSIFICATIONS = [
    ("H01", "research-purpose", "value-set development"),
    ("H01", "research-purpose", "valuation research"),
    ("H01", "study-design", "national valuation survey"),
    ("H02", "research-purpose", "valuation-method research"),
    ("H02", "research-purpose", "respondent data-quality evaluation"),
    ("H02", "study-design", "multi-arm DCE experiment"),
    ("H03", "research-purpose", "valuation-method research"),
    ("H03", "research-purpose", "measurement-property evaluation"),
    ("H03", "study-design", "test-retest study"),
    ("H04", "research-purpose", "instrument development"),
    ("H04", "study-design", "multi-dataset psychometric development study"),
    ("H05", "research-purpose", "content-validity and appropriateness evaluation"),
    ("H05", "research-purpose", "proxy-reporting research"),
    ("H05", "study-design", "qualitative think-aloud study"),
    ("H06", "research-purpose", "population health"),
    ("H06", "study-design", "cross-sectional population survey"),
    ("H07", "research-purpose", "evidence synthesis"),
    ("H07", "research-purpose", "measurement-property evaluation"),
    ("H07", "study-design", "systematic review"),
    ("H08", "research-purpose", "measurement-property evaluation"),
    ("H08", "study-design", "cross-sectional psychometric study"),
    ("H10", "research-purpose", "implementation research"),
    ("H10", "research-purpose", "data-visualization evaluation"),
    ("H10", "study-design", "prototype usability study"),
    ("H11", "research-purpose", "cultural determinants of self-reported health"),
    ("H11", "study-design", "cross-national secondary observational analysis"),
]

CONCEPTS = {
    "H01": ["states worse than dead", "health-state anchoring", "value-set transferability", "interviewer quality control"],
    "H02": ["respondent engagement", "attribute non-attendance", "task complexity", "choice-design overlap"],
    "H03": ["personal utility functions", "test-retest reliability", "individual versus aggregate reliability", "digital preference elicitation"],
    "H04": ["child and adolescent health", "proxy reporting", "respondent burden", "intellectual disability"],
    "H05": ["proxy reporting and proxy perspective", "caregiver and staff judgement", "cognitive impairment", "residential aged care"],
    "H06": ["child and adolescent health", "population health", "health inequality", "mental distress"],
    "H07": ["cross-cultural comparability", "measurement properties", "evidence quality", "research gaps"],
    "H08": ["child and adolescent health", "cross-cultural comparability", "instrument sensitivity", "language adaptation"],
    "H10": ["digital health", "clinical decision support", "PROM implementation", "data visualization"],
    "H11": ["cultural values", "cross-cultural comparability", "self-reported health", "ecological fallacy", "response styles"],
}

POPULATIONS = [
    ("H01", "German adults", "target", "Germany", "18 years and older", None),
    ("H02", "Australian general population", "target", "Australia", "adults", None),
    ("H03", "German general-population and patient adults", "target", "Germany", "adults", "diabetes or rheumatic disease subgroups"),
    ("H04", "children with intellectual disability", "target", "multiple countries and datasets", "3 to 18 years", "intellectual disability"),
    ("H05", "residential aged-care residents represented by proxies", "target", "Australia", "older adults", "frailty or cognitive impairment common"),
    ("H06", "adolescents in the Life & Health survey", "target", "Sweden", "13 to 18 years", None),
    ("H07", "East and South-East Asian measurement-property evidence", "review scope", "East and South-East Asia", None, "general and disease populations"),
    ("H08", "healthy and sick children and adolescents in Blantyre", "target", "Malawi", "8 to 17 years", "healthy, acute, and chronic groups"),
    ("H10", "adults considering total knee arthroplasty", "target", "Alberta, Canada", "18 years and older", "knee osteoarthritis"),
    ("H11", "World Values Survey and European Values Survey respondents", "target", "51 countries", None, None),
]

SAMPLES = [
    ("H01", "completed and retained interviews", 1158, "analytic"),
    ("H02", "recruited respondents", 3365, "recruited"),
    ("H02", "eight-design article subset", 1432, "analytic"),
    ("H03", "initial survey", 330, "completed"),
    ("H03", "matched final sample", 220, "analytic"),
    ("H04", "pooled development dataset", 1699, "analytic"),
    ("H05", "family proxies", 9, "completed"),
    ("H05", "staff proxies", 20, "completed"),
    ("H06", "all survey respondents", 7399, "completed"),
    ("H06", "complete EQ-5D-Y-3L sample", 6574, "analytic"),
    ("H07", "retained publications", 79, "review-publication"),
    ("H07", "source-defined measurement-property assessments", 1504, "review-evidence-unit"),
    ("H08", "completed all questionnaires", 289, "analytic"),
    ("H10", "pre-surgery prototype group", 24, "completed"),
    ("H10", "one-year post-surgery prototype group", 25, "completed"),
    ("H11", "source Integrated Values Survey", 506268, "source"),
    ("H11", "within-country regressions", 157583, "analytic"),
    ("H11", "mixed-effects models", 100590, "analytic"),
    ("H11", "country-level regression", 51, "analytic-country"),
]

INSTRUMENTS = [
    ("eq-5d-5l", "EQ-5D-5L", "EQ-5D", "5L", None),
    ("eq-vas", "EQ VAS", "EQ VAS", None, None),
    ("eq-hwb-s", "EQ-HWB-S", "EQ-HWB", "short", None),
    ("qi-disability", "QI-Disability", "QI-Disability", "32-item", "caregiver proxy"),
    ("qid-12", "QID-12", "QI-Disability", "12-item", "caregiver proxy"),
    ("eq-hwb-proxy-v2", "EQ-HWB proxy version 2", "EQ-HWB", "25-item", "proxy"),
    ("eq-5d-y-3l", "EQ-5D-Y-3L", "EQ-5D-Y", "3L", "youth self-report"),
    ("eq-5d-y-5l", "EQ-5D-Y-5L", "EQ-5D-Y", "5L", "youth self-report"),
    ("pedsql-4-gcs", "PedsQL 4.0 Generic Core Scales", "PedsQL", "4.0", "child and teen self-report"),
    ("sf-6d", "SF-6D", "SF-6D", None, None),
    ("hui", "HUI", "Health Utilities Index", "HUI2 or HUI3", None),
    ("qwb", "QWB", "Quality of Well-Being", None, None),
    ("wvs-srh", "World Values Survey self-reported-health item", "WVS", None, "single item"),
]

INSTRUMENT_USES = [
    ("H01", "eq-5d-5l", "valued", "German", None),
    ("H01", "eq-5d-5l", "administered to describe respondent health", "German", None),
    ("H01", "eq-vas", "administered to describe respondent health", "German", None),
    ("H02", "eq-5d-5l", "used in DCE choice tasks", None, None),
    ("H02", "eq-5d-5l", "administered to describe respondent health", None, None),
    ("H03", "eq-hwb-s", "valued", None, None),
    ("H04", "qi-disability", "source instrument for item reduction", None, None),
    ("H04", "qid-12", "developed and psychometrically evaluated", None, None),
    ("H05", "eq-hwb-proxy-v2", "content and appropriateness evaluated", "English", None),
    ("H06", "eq-5d-y-3l", "administered for population health", "Swedish", None),
    ("H06", "eq-vas", "administered for population health", "Swedish", None),
    ("H07", "eq-5d-5l", "measurement-property evidence synthesized", "multiple", None),
    ("H07", "eq-vas", "measurement-property evidence synthesized", "multiple", None),
    ("H07", "sf-6d", "measurement-property evidence synthesized", "multiple", None),
    ("H07", "hui", "measurement-property evidence synthesized", "multiple", None),
    ("H07", "qwb", "measurement-property evidence synthesized", "multiple", None),
    ("H08", "eq-5d-y-3l", "administered and psychometrically evaluated", "Chichewa", "US adult EQ-5D-3L value set"),
    ("H08", "eq-5d-y-5l", "administered and psychometrically evaluated", "Chichewa", "US adult EQ-5D-5L value set"),
    ("H08", "pedsql-4-gcs", "used as comparator", "Chichewa", None),
    ("H10", "eq-5d-5l", "historical data visualized in decision support", "English", None),
    ("H11", "wvs-srh", "secondary outcome measure", "multiple", None),
]

ADMINISTRATIONS = [
    ("H01", "eq-5d-5l", "general-public adult", "societal", "interviewer-administered", "computer-assisted in person", "public venue or home", "German", None, "one interview"),
    ("H02", "eq-5d-5l", "general-public adult", "self", "self-completed", "web", "remote", None, None, "one survey"),
    ("H03", "eq-hwb-s", "general-public or patient adult", "self", "self-completed", "web", "remote", None, None, "test and two-week retest"),
    ("H05", "eq-hwb-proxy-v2", "family or staff proxy", "proxy-person with observed drift", "interviewer-administered think-aloud", "in person", "residential aged care", "English", "7 days", "one interview"),
    ("H06", "eq-5d-y-3l", "adolescent", "self", "self-completed", "paper", "school", "Swedish", "today", "one survey"),
    ("H08", "eq-5d-y-3l", "child or adolescent", "self", "self-completed", "paper questionnaire", "school or outpatient clinic", "Chichewa", "same day", "one wave"),
    ("H08", "eq-5d-y-5l", "child or adolescent", "self", "self-completed", "paper questionnaire", "school or outpatient clinic", "Chichewa", None, "one wave"),
    ("H10", "eq-5d-5l", "adult TKA candidate", "self", "researcher-administered prototype review", "paper prototype", "orthopedic clinic", "English", None, "post-screening"),
]

METHODS = [
    ("H01", "cTTO", "valuation method", "preference elicitation", "EQ-VT 2.0", "ten tasks plus feedback"),
    ("H01", "DCE", "valuation method", "preference elicitation", "EQ-VT 2.0", "seven forced-choice pairs"),
    ("H02", "DCE", "valuation method", "task-design experiment", None, "21 tasks; eight focal designs"),
    ("H03", "Online Elicitation of Personal Utility Functions", "valuation method", "preference elicitation", None, "ranking, swing weighting, level rating, pairwise comparison, anchoring"),
    ("H04", "Genetic Algorithm item reduction", "instrument-development method", "item reduction", None, "500 runs with domain constraints"),
    ("H04", "psychometric assessment", "measurement-property method", "validation", None, None),
    ("H05", "cognitive think-aloud interview", "qualitative method", "response-process assessment", None, None),
    ("H05", "semi-structured interview", "qualitative method", "content and proxy assessment", None, None),
    ("H06", "population survey", "survey method", "population health", "Life & Health—young people", None),
    ("H07", "systematic literature review", "evidence-synthesis method", "measurement-property synthesis", "COSMIN-guided", "four databases through August 2019"),
    ("H08", "psychometric assessment", "measurement-property method", "instrument comparison", None, "cross-instrument validity and informativity"),
    ("H10", "visualization prototype comparison", "implementation method", "usability and comprehension", None, "two pre-surgery and two post-surgery versions"),
    ("H10", "directed content analysis", "qualitative analysis", "open-ended feedback", None, None),
    ("H11", "secondary cross-national survey analysis", "observational method", "within- and between-country association", "WVS integration protocol", "WVS and EVS linked with World Bank data"),
]

MODELS = [
    ("H01", "censored Tobit model", "Tobit", "candidate", "cTTO valuation", "left-censored at -1"),
    ("H01", "conditional logit model", "conditional logit", "candidate", "DCE valuation", None),
    ("H01", "hybrid model 3a", "hybrid cTTO-DCE", "candidate", "combined valuation", None),
    ("H01", "hybrid model 3b", "hybrid cTTO-DCE", "preferred-final", "value-set estimation", "cTTO censoring and heteroskedastic error variance"),
    ("H02", "equality constrained latent class model", "latent class", "primary", "attribute-attendance classification", "32 possible attendance strategies"),
    ("H02", "multinomial logit model", "multinomial logit", "comparator", "choice modeling", None),
    ("H03", "additive utility model", "additive utility", "final", "personal utility functions", "anchored decrements"),
    ("H03", "two-way mixed-effects ICC", "intraclass correlation", "primary", "test-retest reliability", None),
    ("H04", "Rasch partial credit model", "Rasch", "final", "psychometric validation", None),
    ("H06", "multiple linear regression", "linear regression", "final", "EQ VAS subgroup analysis", "seven adjusted model specifications"),
    ("H07", "COSMIN and GRADE rule-based synthesis", "rule-based evidence synthesis", "final", "measurement-property evidence", "no pooled meta-analysis"),
    ("H08", "relative efficiency analysis", "relative efficiency", "primary", "empirical validity", "ratio of squared t-statistics"),
    ("H10", "Wilcoxon signed-rank test", "nonparametric paired test", "primary", "prototype comparison", None),
    ("H10", "McNemar test", "paired categorical test", "primary", "prototype comparison", None),
    ("H11", "within-country linear regressions", "linear regression", "primary", "individual-level cultural associations", "51 country-specific models"),
    ("H11", "multilevel mixed-effects models", "mixed-effects regression", "primary", "individual and country variation", "random country intercepts and cultural-value slopes"),
    ("H11", "country-level linear regression", "linear regression", "primary", "between-country cultural associations", "51 country observations"),
]

PRODUCTS = [
    ("H01", "German EQ-5D-5L value set", "native value set", "final and recommended", "EQ-5D-5L", "Germany"),
    ("H02", "DCE design guidance for attribute overlap", "method guidance", "produced", "EQ-5D-5L", None),
    ("H03", "aggregate EQ-HWB-S value set", "value set", "supported at aggregate level", "EQ-HWB-S", "Germany"),
    ("H03", "individual personal utility functions", "personal utility function", "unstable in test-retest", "EQ-HWB-S", "Germany"),
    ("H04", "QID-12", "instrument short form", "developed; independent validation needed", "QI-Disability", None),
    ("H06", "Swedish adolescent EQ-5D-Y-3L reference results", "population reference results", "produced", "EQ-5D-Y-3L", "Sweden"),
    ("H07", "Asian PBM measurement-property evidence synthesis", "evidence synthesis", "produced", None, "East and South-East Asia"),
    ("H08", "Chichewa EQ-5D-Y psychometric evidence", "measurement-property evidence", "produced", "EQ-5D-Y-3L and EQ-5D-Y-5L", "Malawi"),
    ("H10", "individualized TKA decision-aid visualizations", "implementation prototype", "tested as paper prototype; online implementation planned", "EQ-5D-5L", "Alberta, Canada"),
    ("H11", "cross-national interpretation evidence for self-reported health", "interpretation guidance", "produced", None, "51 countries"),
]

OUTCOMES = [
    ("H01", "health-state utility", "preference outcome"),
    ("H01", "dimension relative importance", "valuation result"),
    ("H02", "attribute attendance", "respondent data quality"),
    ("H02", "respondent engagement", "survey process"),
    ("H03", "test-retest reliability", "measurement property"),
    ("H04", "internal consistency", "measurement property"),
    ("H04", "Rasch model fit", "measurement property"),
    ("H05", "content appropriateness", "content validity"),
    ("H05", "proxy response process", "response process"),
    ("H06", "EQ-5D-Y dimension problems", "population health"),
    ("H06", "EQ VAS score", "population health"),
    ("H07", "construct validity", "measurement property"),
    ("H07", "test-retest reliability", "measurement property"),
    ("H07", "responsiveness", "measurement property"),
    ("H08", "ceiling and floor effects", "measurement property"),
    ("H08", "convergent and known-group validity", "measurement property"),
    ("H10", "comprehension", "usability"),
    ("H10", "usefulness", "usability"),
    ("H10", "visual appeal", "usability"),
    ("H11", "self-reported health", "population health"),
    ("H11", "association with cultural values", "observational association"),
]

FINDINGS = {
    "H01": [
        ("Preferred hybrid model 3b produced logically consistent and precise coefficients.", "model selection", None, "The model was selected for the national value set.", "EQ-5D-5L", "cTTO and DCE", "health-state utility"),
        ("Predicted utilities ranged from -0.661 to 1.", "range", None, "The range was wider than the German 3L value set and crosswalk.", "EQ-5D-5L", "hybrid model 3b", "health-state utility"),
        ("Dimension importance was pain/discomfort, anxiety/depression, self-care, mobility, and usual activities.", "rank", None, "Pain/discomfort had the largest effect.", "EQ-5D-5L", "hybrid model 3b", "dimension relative importance"),
        ("The authors recommend the produced value set for German economic evaluation and clinical assessment.", "recommendation", None, None, "EQ-5D-5L", None, "research use"),
    ],
    "H02": [
        ("Attribute overlap increased estimated full attendance, with the largest increases in the Ngene and SAS modified Fedorov designs.", "difference", "positive", "Overlap and design construction can improve engagement.", "EQ-5D-5L", "DCE", "attribute attendance"),
        ("Relative attribute importance changed after restriction to full attenders, especially for mobility and anxiety/depression.", "difference", None, None, "EQ-5D-5L", "ECLC classification", "relative attribute importance"),
        ("Attendance classes aligned with straightlining, completion time, task difficulty, and reported consideration of the full description.", "association", None, "ECLC classification can support data-quality review.", "EQ-5D-5L", "ECLC model", "respondent engagement"),
    ],
    "H03": [
        ("Individual OPUF task responses had poor to moderate test-retest reliability.", "reliability", "poor-to-moderate", None, "EQ-HWB-S", "OPUF", "test-retest reliability"),
        ("The anchoring-factor ICC was 0.12.", "estimate", "poor", None, "EQ-HWB-S", "OPUF", "anchoring reliability"),
        ("Aggregate utility decrements were similar at test and retest, with a mean overall decrement of 0.08 in both administrations.", "similarity", "stable", "Aggregate value sets were reliable despite unstable individual responses.", "EQ-HWB-S", "OPUF", "aggregate reliability"),
        ("The authors support OPUF for aggregate value sets but not stable individual personal utility functions.", "interpretation", None, None, "EQ-HWB-S", "OPUF", "product reliability"),
    ],
    "H04": [
        ("The Genetic Algorithm selected a 12-item set that retained all six QI-Disability domains.", "development result", None, None, "QID-12", "Genetic Algorithm", "item reduction"),
        ("QID-12 correlated 0.97 with the full QI-Disability score.", "association", "strong", None, "QID-12", None, "convergent validity"),
        ("Rasch analysis showed satisfactory fit and person separation reliability of 0.84.", "validity", "satisfactory", None, "QID-12", "Rasch partial credit model", "model fit"),
        ("QID-12 can reduce respondent burden but does not replace the full measure for domain-level assessment.", "interpretation", None, None, "QID-12", None, "intended use"),
    ],
    "H05": [
        ("Proxies found the EQ-HWB broadly relevant but identified ambiguous, double-barrelled, repetitive, or unsuitable items and examples.", "content validity", "mixed", "Item wording and examples need revision.", "EQ-HWB proxy version 2", "think-aloud interview", "content appropriateness"),
        ("Some proxies did not maintain the proxy-person perspective and sometimes used their own judgement.", "response process", None, "Proxy perspective must be explicit and supported.", "EQ-HWB proxy version 2", "think-aloud interview", "proxy response process"),
        ("Observable physical items were easier for proxies than psychological items.", "difference", None, None, "EQ-HWB proxy version 2", None, "proxy ability"),
        ("The authors retain self-report as the default and recommend further study of proxy type, perspective, wording, and examples.", "recommendation", None, None, "EQ-HWB proxy version 2", None, "instrument use"),
    ],
    "H06": [
        ("Girls reported more problems in usual activities, pain/discomfort, and mood and had lower EQ VAS scores than boys.", "group difference", "poorer", None, "EQ-5D-Y-3L", "population survey", "population health"),
        ("Adolescents with one or both parents unemployed reported poorer health on several dimensions and lower EQ VAS scores.", "group difference", "poorer", None, "EQ-5D-Y-3L", "population survey", "health inequality"),
        ("Disease, functional impairment, and mental distress were associated with more problems and lower EQ VAS scores.", "association", "poorer", None, "EQ-5D-Y-3L", "multiple linear regression", "population health"),
        ("The authors support EQ-5D-Y-3L for adolescent population-health assessment and prioritization.", "interpretation", None, None, "EQ-5D-Y-3L", None, "research use"),
    ],
    "H07": [
        ("The review retained 79 papers containing 1,504 source-defined measurement-property assessments.", "evidence volume", None, None, "multiple PBMs", "systematic review", "evidence coverage"),
        ("EQ-5D had the broadest evidence and generally sufficient construct validity and responsiveness.", "evidence synthesis", "mostly sufficient", None, "EQ-5D", "COSMIN and GRADE synthesis", "measurement properties"),
        ("EQ-5D test-retest reliability was sufficient in none of eight assessed countries or districts and three of ten disease groups.", "evidence synthesis", "weak-or-inconsistent", None, "EQ-5D", "COSMIN and GRADE synthesis", "test-retest reliability"),
        ("Evidence for HUI and QWB was scarce.", "evidence gap", "scarce", None, "HUI and QWB", "systematic review", "evidence coverage"),
        ("The authors prefer EQ-5D when a generic PBM is needed in Asia but call for stronger reliability and responsiveness research.", "recommendation", None, None, "EQ-5D", None, "research use"),
    ],
    "H08": [
        ("Missing responses were uncommon overall but more problematic for younger children, especially with EQ-5D-Y-5L.", "feasibility", "mixed", None, "EQ-5D-Y-5L", "psychometric assessment", "missingness"),
        ("EQ-5D-Y-5L generally reduced ceiling effects, while EQ-5D-Y-3L had higher Shannon informativity.", "comparison", "mixed", None, "EQ-5D-Y-3L and EQ-5D-Y-5L", "psychometric assessment", "ceiling and informativity"),
        ("Known-group validity was supported and was generally stronger among adolescents.", "validity", "supported", None, "EQ-5D-Y versions", "psychometric assessment", "known-group validity"),
        ("EQ-5D-Y-5L was less efficient than EQ-5D-Y-3L for detecting differences on the reported external measures.", "comparison", "less efficient", None, "EQ-5D-Y-5L", "relative efficiency", "empirical validity"),
        ("The authors judged EQ-5D-Y-3L more suitable for ages 8 to 12 and EQ-5D-Y-5L more suitable for ages 13 to 17 in this setting.", "interpretation", None, None, "EQ-5D-Y versions", None, "instrument choice"),
    ],
    "H10": [
        ("Part 1 slightly favored prototype version 1, while Part 2 favored version 2; no statistically significant version differences were reported.", "comparison", "no-clear-difference", None, "EQ-5D-5L historical data", "prototype comparison", "visualization preference"),
        ("Most participants showed adequate comprehension of the visualizations.", "usability", "positive", None, "EQ-5D-5L historical data", "prototype comparison", "comprehension"),
        ("Participants found possible-outcome information useful for risks, benefits, and expectation setting, but some did not know how to use it.", "usability", "mixed", None, "EQ-5D-5L historical data", "prototype comparison", "usefulness"),
        ("The authors recommend combining preferred elements and further testing the complete online decision aid before routine implementation.", "recommendation", None, None, "EQ-5D-5L historical data", None, "implementation"),
    ],
    "H11": [
        ("Survival and self-expression values were positively associated with self-reported health.", "association", "positive", None, "WVS self-reported health item", "cross-national regression", "self-reported health"),
        ("Traditional and rational-secular values were negatively associated with self-reported health, contrary to the directional hypothesis.", "association", "negative", "The authors could not establish a firm mechanism.", "WVS self-reported health item", "cross-national regression", "self-reported health"),
        ("The cultural-value associations had similar directions within countries and between countries.", "similarity", "similar", "This reduces the risk of an unsupported ecological inference.", "WVS self-reported health item", "within- and between-country models", "cross-cultural interpretation"),
        ("Cultural values explained 4% to 17% of within-country variation, and the country-level effect could reach about 0.75 on the five-point health scale.", "magnitude", None, None, "WVS self-reported health item", "regression models", "self-reported health"),
        ("The authors recommend considering cultural values when interpreting self-reported health between countries.", "recommendation", None, None, "WVS self-reported health item", None, "cross-cultural interpretation"),
    ],
}

LIMITATIONS = {
    "H01": [
        ("The sample clustered in six regions and had a small middle-class bias.", "sample"),
        ("Patient-population discrimination and practical evaluation space need further study.", "generalizability"),
    ],
    "H02": [
        ("The article analyzes only eight of nineteen designs and only zero-prior designs.", "design scope"),
        ("The model cannot fully separate inattention from genuine low attribute importance.", "interpretation"),
        ("Transfer to other populations and administration modes is not established.", "generalizability"),
    ],
    "H03": [
        ("Excluding illogical or indifferent responses can overestimate agreement.", "analysis"),
        ("Online-panel recruitment can select people with better digital literacy.", "sample"),
        ("The study cannot separate method, instrument-complexity, and online-mode causes of inconsistency.", "interpretation"),
    ],
    "H04": [
        ("QID-12 was developed and validated in the same pooled dataset.", "validation"),
        ("Three items had disordered intermediate category thresholds.", "measurement property"),
        ("The short form can lose domain-level detail.", "intended use"),
    ],
    "H05": [
        ("The study used convenience sampling and proxy views only.", "sample"),
        ("It could not compare proxy reports with residents' self-reports.", "comparison"),
        ("A problem-focused interview may have underrepresented positive comments.", "method"),
    ],
    "H06": [
        ("The survey was cross-sectional and does not support causal conclusions.", "design"),
        ("Adolescent reports of parental occupational status can be inaccurate.", "measure"),
        ("No EQ-5D-Y value set was available at the time.", "scoring"),
    ],
    "H07": [
        ("The authors modified COSMIN methods for a multi-measure, multi-population review.", "review method"),
        ("Exclusion of non-English papers can underrepresent evidence.", "review scope"),
        ("Different language versions and administration modes were not analyzed separately.", "granularity"),
    ],
    "H08": [
        ("COVID-19 restrictions prevented test-retest and responsiveness assessment.", "design"),
        ("Urban convenience recruitment and literacy exclusions limit generalizability.", "sample"),
        ("Adult US value sets were used because youth value sets were unavailable.", "scoring"),
    ],
    "H10": [
        ("Participants reviewed paper prototypes rather than the complete online decision aid.", "product status"),
        ("The two small samples came from one urban clinic after surgical screening.", "sample"),
        ("The paper does not state whether Part 1 and Part 2 participants overlapped.", "sample provenance"),
    ],
    "H11": [
        ("Missing data and unasked questions reduced the analytic sample substantially.", "sample"),
        ("Collapsed survey waves assume stable associations over time.", "time"),
        ("Country aggregates cannot represent all cultural subgroups within countries.", "population"),
        ("The source data did not measure response styles.", "measure"),
        ("Linear regression treated a categorical health outcome as continuous.", "model"),
    ],
}

PROJECT_LINKS = {
    "H01": ("2012020", "accepted", "co-funded study", "direct article funding statement", "Funding"),
    "H02": ("2016260", "accepted", "partial study funding", "direct article funding statement", "Funding"),
    "H03": ("1508-RA", "accepted", "study funding", "direct article funding statement", "Funding"),
    "H04": ("429-RA", "accepted", "data-collection funding", "direct article funding statement", "Funding"),
    "H05": ("150-RA", "accepted", "study funding", "direct article funding statement", "Funding"),
    "H06": ("2015400", "accepted", "study funding", "direct article funding statement", "Funding"),
    "H07": ("2016230", "accepted", "study funding", "direct article funding statement", "Funding"),
    "H08": ("20190200", "accepted", "researcher and study funding", "direct article funding statement", "Acknowledgements; Funding; Competing interests"),
    "H10": ("445-RA", "accepted", "work funding", "direct article funding statement", "Funding"),
    "H11": ("2015150", "accepted", "study funding", "direct article funding statement", "Acknowledgements"),
}


def load_semantic(
    connection: sqlite3.Connection,
    repo_root: Path,
    pilot_rows: dict[str, dict[str, str]],
) -> None:
    for record_id, (title, eq_status) in STUDIES.items():
        row = pilot_rows[record_id]
        publication_id = f"doi:{row['doi'].lower()}"
        connection.execute(
            "INSERT INTO study "
            "(study_id, publication_id, title, eq_instrument_status, record_path, review_status) "
            "VALUES (?, ?, ?, ?, ?, 'source-checked')",
            (record_id, publication_id, title, eq_status, row["record_path"]),
        )
        connection.execute(
            "INSERT INTO study_publication VALUES (?, ?, 'primary report', ?)",
            (record_id, publication_id, "source-checked extraction record"),
        )

    for study_id, kind, label in CLASSIFICATIONS:
        connection.execute(
            "INSERT INTO study_classification "
            "(study_id, classification_type, preferred_label, source_locator) VALUES (?, ?, ?, ?)",
            (study_id, kind, label, "source-checked extraction record, sections 1 and 12"),
        )

    for study_id, labels in CONCEPTS.items():
        for label in labels:
            connection.execute(
                "INSERT INTO study_concept "
                "(study_id, preferred_label, source_term, review_status, source_locator) "
                "VALUES (?, ?, ?, 'accepted', ?)",
                (study_id, label, label, "source-checked extraction record, section 3"),
            )

    for row in POPULATIONS:
        connection.execute(
            "INSERT INTO population "
            "(study_id, label, role, country_or_region, age_text, condition_text, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 2"),
        )

    for row in SAMPLES:
        connection.execute(
            "INSERT INTO sample (study_id, label, count_value, count_status, source_locator) "
            "VALUES (?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 2"),
        )

    connection.executemany(
        "INSERT INTO instrument VALUES (?, ?, ?, ?, ?)",
        INSTRUMENTS,
    )
    for study_id, instrument_id, role, language, scoring_source in INSTRUMENT_USES:
        connection.execute(
            "INSERT INTO instrument_use "
            "(study_id, instrument_id, role, language, scoring_source, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (study_id, instrument_id, role, language, scoring_source, "source-checked extraction record, section 4"),
        )

    for row in ADMINISTRATIONS:
        connection.execute(
            "INSERT INTO administration "
            "(study_id, instrument_id, respondent, perspective, interaction, channel, setting, language, recall_period, timepoint, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 4"),
        )

    for row in METHODS:
        connection.execute(
            "INSERT INTO research_method "
            "(study_id, preferred_label, method_family, role, protocol, task_details, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 5"),
        )

    for row in MODELS:
        connection.execute(
            "INSERT INTO statistical_model "
            "(study_id, preferred_label, model_family, role, analysis_purpose, qualifiers, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 6"),
        )

    for row in PRODUCTS:
        connection.execute(
            "INSERT INTO research_product "
            "(study_id, label, product_type, status, target_instrument, jurisdiction, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 7"),
        )

    for row in OUTCOMES:
        connection.execute(
            "INSERT INTO study_outcome (study_id, preferred_label, outcome_type, source_locator) "
            "VALUES (?, ?, ?, ?)",
            (*row, "source-checked extraction record, section 8"),
        )

    for study_id, findings in FINDINGS.items():
        for sequence, row in enumerate(findings, start=1):
            statement, finding_type, direction, interpretation, instrument, method, outcome = row
            connection.execute(
                "INSERT INTO finding "
                "(study_id, sequence, statement, finding_type, direction, interpretation, "
                "instrument_context, method_context, outcome_context, source_locator) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    study_id,
                    sequence,
                    statement,
                    finding_type,
                    direction,
                    interpretation,
                    instrument,
                    method,
                    outcome,
                    "source-checked extraction record, section 9",
                ),
            )

    for study_id, limitations in LIMITATIONS.items():
        for sequence, (statement, applies_to) in enumerate(limitations, start=1):
            connection.execute(
                "INSERT INTO limitation (study_id, sequence, statement, applies_to, source_locator) "
                "VALUES (?, ?, ?, ?, ?)",
                (study_id, sequence, statement, applies_to, "source-checked extraction record, section 10"),
            )

    connection.execute(
        "INSERT INTO source_conflict "
        "(study_id, fact_name, value_a, source_a, value_b, source_b, resolution) "
        "VALUES ('H04', 'Cronbach alpha', '0.85', 'Abstract', '0.84', 'Results', 'unresolved')"
    )
    connection.execute(
        "INSERT INTO source_conflict "
        "(study_id, fact_name, value_a, source_a, value_b, source_b, resolution) "
        "VALUES ('H08', 'all-participant sample', '289', 'Results and Table 1', '298', 'Table 3 header', 'unresolved')"
    )

    connection.execute(
        "INSERT INTO review_evidence_unit "
        "(study_id, unit_type, result_text, source_locator) VALUES (?, ?, ?, ?)",
        (
            "H07",
            "source-defined measurement-property assessment",
            "The review contains 1,504 hypothesis, ICC, or standardized-effect-size assessments across 79 publications.",
            "H07 Methods—Data Extraction; Results",
        ),
    )

    for study_id, info in PROJECT_LINKS.items():
        project_id, status, support_type, evidence_class, locator = info
        publication_id = f"doi:{pilot_rows[study_id]['doi'].lower()}"
        connection.execute(
            "INSERT INTO project_publication "
            "(project_id, publication_id, link_status, support_type, evidence_class, evidence_locator) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (project_id, publication_id, status, support_type, evidence_class, locator),
        )

    h09_publication = f"doi:{pilot_rows['H09']['doi'].lower()}"
    for project_id in ("341-RA", "357-RA"):
        connection.execute(
            "INSERT INTO project_publication "
            "(project_id, publication_id, link_status, support_type, evidence_class, evidence_locator, note) "
            "VALUES (?, ?, 'rejected', NULL, 'article evidence review', 'Funding; Competing interests', ?)",
            (
                project_id,
                h09_publication,
                "Study funding names other funders; an author grant disclosure does not link EuroQol to this work.",
            ),
        )
