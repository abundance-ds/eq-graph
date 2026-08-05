# Author profile QA v1

## Purpose

Decide whether each supplied OpenAlex profile belongs to the named EuroQol researcher.
Use only the supplied names, affiliations, projects, topics, coauthors, and work examples.
Do not search the web or inspect other files.

Choose one decision:

- `accept`: The name and research record form one coherent identity that is consistent
  with the supplied EuroQol person evidence.
- `hold`: The profile is the wrong person, is mixed, is ambiguous, or lacks enough
  evidence for safe inclusion.

Use `hold` when the given name is incompatible, the field is unrelated, or the profile
contains substantial name-collision contamination. A broad clinical portfolio is not by
itself contamination when the field, affiliations, and coauthors remain coherent.

The only task tool is:

`./submit_profile "PERSON_NAME" DECISION "REASON"`

Call it once for every supplied person. The reason must be factual, record-specific, and
no more than 400 characters. Then run `./submit_profile status` and finish.


# Profiles

Assess all 5 people.

[
  {
    "name": "Nan Luo",
    "member_affiliation": "National University of Singapore",
    "is_member": true,
    "projects": [
      {
        "project_id": "128-RA",
        "title": "A global survey of HTA agencies for their views on health utility instruments and data: protocol development",
        "working_group": "Others"
      },
      {
        "project_id": "1504-RA",
        "title": "Testing EQ-5D-5L bolt-ons in patients with sleep & sleep breathing disorders: an exploratory study for making EQ-5D a clinically attractive patient-reported outcomes measure.",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1505-RA",
        "title": "Phase-2 study of the Global HTA Agency Survey project",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1517-RA",
        "title": "EQ-5D for proxy assessment of nursing home residents: A systematic review of feasibility and measurement properties",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1522-RA",
        "title": "Developing an online person trade-off survey for determining the weight between child and adult QALYs based on the preferences of the general public: the phase-1 study",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1535-RA",
        "title": "Comparing a new TTO method with cTTO for valuation of EQ-5D-5L health states in a general population sample",
        "working_group": "Valuation"
      },
      {
        "project_id": "1599-RA",
        "title": "Can EQ-5D capture the impact of climate change? A study of the health impact of heatwaves",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1608-RA",
        "title": "How do HTA practitioners and researchers in Asia perceive EuroQol instruments? A qualitative study",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "1738-TVG",
        "title": "A visit to APERSU in Alberta for learning and exploring research collaborations aiming to establish an EQ-5D support unit in SIngapore",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1741-RA",
        "title": "Unravelling the puzzle of low TTO values for establishing a trustworthy EQ-5D-5L value set for Singapore",
        "working_group": "Valuation"
      },
      {
        "project_id": "180-RA",
        "title": "A fast-track proposal for supporting a fresh PhD graduate to do post-doc research work on EQ-5D",
        "working_group": "Others"
      },
      {
        "project_id": "1818-RA",
        "title": "A Systematic Review of the Validity, Reliability, and Responsiveness Studies of EQ-5D-5L: Methodological Insights and Future Directions",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "188-RA",
        "title": "A comparison of proxy 1 and proxy 2 of EQ-5D-Y: validity, reliability and responsiveness",
        "working_group": "Youth"
      },
      {
        "project_id": "2012060",
        "title": "Valuation of EQ-5D-5L health states for healthcare decision making in Singapore",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014100",
        "title": "Two EQ workshops at ISPOR Asia",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2015220",
        "title": "The effect of chronic conditions on valuation of EQ?5D?5L health states",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015410",
        "title": "Writing a manuscript titled 'valuation of health outcomes using the time trade-off technique: the EuroQol protocols' for publication in the journal of Pharmacoeconomics",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016010",
        "title": "Writing up a manuscript titled 'Estimating a time trade-off EQ-5D-5L value set for China' for publication",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016070",
        "title": "EuroQol workshops back-to-back with ISPOR 7th Asia-Pacific Conference in Singapore on September 3, 2016",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016130",
        "title": "SOME NEW STRATEGIES FOR ELICITING AND MODELING UTILITY VALUES OF MULTI-ATTRIBUTE HEALTH STATES",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016230",
        "title": "The use and research of EQ-5D instruments in East and South-East Asia: a systematic review",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016290",
        "title": "A qualitative study to explore the interpretation and relevance of the EQ‐5D questionnaire in 4 Asian countries",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016310",
        "title": "A head‐to‐head comparison of EQ‐5D‐3L and EQ‐5D‐5L index scores: more levels is better responsiveness?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016600",
        "title": "Pre-conference EQ-5D Short Course for South China Pharm-economics Forum 2016",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20170330",
        "title": "Psychometric validation of the Chinese version of EQ‐5D‐Y for China in three medical conditions",
        "working_group": "Youth"
      },
      {
        "project_id": "20170430",
        "title": "Comparison of 3L and 5L health profiles and valuation in patients with ischemic heart diseases",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170450",
        "title": "Publishing a paper titled “Cost-utility analysis using EQ-5D: does how the utility values are derived matter?”",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170460",
        "title": "Comparison between EQ-5D-3L-Y and EQ-5D-5L-Y in a patient population in Hong Kong",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "20170640",
        "title": "Testing the potential of multiplicative models for efficient EQ-5D bolton/off valuation study design",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "20180060",
        "title": "Testing the face and content validity of E‐QALY domains and items: a study of the Chinese population",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20180160",
        "title": "Testing 4 cognition bolt-on items in a community dwelling elderly group",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20180250",
        "title": "The EQ-5D-5L INSTRUMENT: PAST, PRESENT AND FUTURE",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20180270",
        "title": "2nd EQ-5D training workshop for China",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20180600",
        "title": "Initial psychometric testing of E-QALY and 3L-5L comparison in China",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2019-EO",
        "title": "Organizing a EuroQol workshop in Singapore to engage Asian HTA leaders and practitioners",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20190010",
        "title": "QALY estimation for HTA: The EuroQol approach. 2019 HTAsiaLink Annual Conference",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20190600",
        "title": "Does EQ-5D cover the most undesirable health problems in different cultures? A study of seven countries using a mixed methods",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190820",
        "title": "travel scholarship for Qingqing Chai",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20190830",
        "title": "travel scholarship for Xueyun Zeng",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2120-RA",
        "title": "A Head-to-Head Comparison of Construct Validity and Responsiveness between EQ-5D-5L and EQ-HWB-S in Gastrointestinal Cancer Patients undergoing anticancer treatment",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2176-RA",
        "title": "Testing a lag-time time trade-off design for valuation of EQ-TIPS: An exploratory study",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2222-EO",
        "title": "Application for a grant to prepare and conduct a workshop in ISPOR Real-World Evidence Summit 2025 on 30 September in Tokyo, Japan",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "232-RA",
        "title": "Measurement properties of EQ-5D-Y and other commonly used generic preference-based measures for children and adolescents: a systematic review",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2362-BT",
        "title": "Testing hearing bolt-on and other bolt-ons related to hearing function in individuals receiving hearing aids or cochlear implantation",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2418-BT",
        "title": "Testing fatigue and breathing bolt-ons in the EQ-5D toolbox in three different types of cancers",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2451-RA",
        "title": "Transitioning between the EQ-5D-Y-5L and EQ-5D-5L in Chinese adolescents aged 12–18 years with atopic dermatitis or mental health problems",
        "working_group": "Youth"
      },
      {
        "project_id": "2455-PHD",
        "title": "Advancing EQ-TIPS in Low and Middle-Income Countries: Evidence map, cultural adaptation, and psychometric validation in Indonesian infants and toddlers",
        "working_group": "Youth"
      },
      {
        "project_id": "274-RA",
        "title": "Testing the psychometric properties of two respiratory bolt-ons",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "320-VS",
        "title": "Resubmission of pre-approved EQ Project 20190450: Re-estimating the EQ-5D-5L value set for China",
        "working_group": "Valuation"
      },
      {
        "project_id": "321-VS",
        "title": "A multi-country EQ-5D-Y valuation study in Asia (Resubmission of project 154-2020RA)",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "364-RA",
        "title": "Exploring the relevance and coverage of the EQ-5D-Y in Asia",
        "working_group": "Youth"
      },
      {
        "project_id": "402-RA",
        "title": "The ceiling effects of EQ-5D in general population health surveys: A systematic review and meta-regression",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "439-PHD",
        "title": "Development and evaluation of an EQ-5D-based decision aid for individuals considering bariatric surgery (revised for resubmission)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "69-RA",
        "title": "A mixed methods approach to testing alternative recall periods for EQ-5D (2nd revision)",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "76-RA",
        "title": "A PhD grant to investigate the valuation of worse-than-dead health states",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5064398143",
      "display_name": "Nan Luo",
      "orcid": "0000-0001-7980-6979",
      "reported_affiliation": "National University of Singapore",
      "works_count": 477,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 219
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 53
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 29
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 25
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 24
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 23
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 19
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 18
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 16
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 15
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 14
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Zhihao Yang",
          "works": 44
        },
        {
          "name": "Julian Thumboo",
          "works": 42
        },
        {
          "name": "Pei Wang",
          "works": 29
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 25
        },
        {
          "name": "Gerald Choon‐Huat Koh",
          "works": 25
        },
        {
          "name": "Michael Herdman",
          "works": 24
        },
        {
          "name": "Philip Yap",
          "works": 23
        },
        {
          "name": "Hwee Lin Wee",
          "works": 22
        },
        {
          "name": "Yin Bun Cheung",
          "works": 21
        },
        {
          "name": "Mihir Gandhi",
          "works": 20
        },
        {
          "name": "Ling Jie Cheng",
          "works": 18
        },
        {
          "name": "Rachel Lee-Yin Tan",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162409369",
          "year": 2026,
          "title": "A framework for building a synthetic cell from the SynCell Asia Initiative",
          "type": "article",
          "venue": "Nature Biotechnology",
          "cited_by_count": 1,
          "topics": [
            "Single-cell and spatial transcriptomics",
            "Pluripotent Stem Cells Research",
            "Gene Regulatory Network Analysis"
          ]
        },
        {
          "openalex_id": "W7168188268",
          "year": 2026,
          "title": "Correction: Factors associated with preoperative health-related quality of life in patients undergoing lumbar spine surgery: a multi-ethnic Asian cohort",
          "type": "erratum",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Spine and Intervertebral Disc Pathology",
            "Cardiac, Anesthesia and Surgical Outcomes",
            "Enhanced Recovery After Surgery"
          ]
        },
        {
          "openalex_id": "W7171291792",
          "year": 2026,
          "title": "Development and psychometric evaluation of a new itch assessment questionnaire for use in multi-ethnic Asian population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Dermatology and Skin Diseases",
            "Nail Diseases and Treatments",
            "Dermatological diseases and infestations"
          ]
        },
        {
          "openalex_id": "W7160385346",
          "year": 2026,
          "title": "Dopamine-mediated signal amplification integrated with CCK-8 detection for highly sensitive colorimetric immunoassay",
          "type": "article",
          "venue": "Spectrochimica Acta Part A Molecular and Biomolecular Spectroscopy",
          "cited_by_count": 0,
          "topics": [
            "Biosensors and Analytical Detection",
            "Advanced biosensing and bioanalysis techniques",
            "Advanced Biosensing Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W7166114740",
          "year": 2026,
          "title": "PCR9 CONTENT VALIDITY OF THE EQ-HWB-9 IN PATIENTS WITH ADVANCED ILLNESSES: A COGNITIVE DEBRIEFING STUDY",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis",
            "Lung Cancer Treatments and Mutations"
          ]
        },
        {
          "openalex_id": "W7168145076",
          "year": 2026,
          "title": "Quality-aware visual-inertial GPS/SINS coarse alignment in a transverse frame for robust polar navigation",
          "type": "article",
          "venue": "The Visual Computer",
          "cited_by_count": 0,
          "topics": [
            "Inertial Sensor and Navigation",
            "Robotics and Sensor-Based Localization",
            "GNSS positioning and interference"
          ]
        },
        {
          "openalex_id": "W863521785",
          "year": 1989,
          "title": "活性氢氧化铁处理含钒（V）废水的研究",
          "type": "article",
          "venue": "Acta Scientiarum Naturalium Universitatis Sunyatseni",
          "cited_by_count": 0,
          "topics": [
            "Military Technology and Strategies",
            "Legal and Regulatory Analysis",
            "Linguistic, Cultural, and Literary Studies"
          ]
        },
        {
          "openalex_id": "W2370076496",
          "year": 1999,
          "title": "Change of neuropeptide Y and neurotensin of plasma and platelet extract liquid in patients with ischemic cerebrovascular disease",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Neuropeptides and Animal Physiology",
            "Inflammatory Biomarkers in Disease Prognosis",
            "Platelet Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W2385236327",
          "year": 1999,
          "title": "Effect of change of transforming growth factor α content on homedialysis patients",
          "type": "article",
          "venue": "Chinese Journal of Dialysis and Artificial Organs",
          "cited_by_count": 0,
          "topics": [
            "Clinical practice guidelines implementation",
            "Medical Research and Treatments"
          ]
        },
        {
          "openalex_id": "W2370160903",
          "year": 1999,
          "title": "Expression of the platelet extract's neuropeptide and neurotensin in hemodialysis",
          "type": "article",
          "venue": "Zhongguo mianyixue zazhi",
          "cited_by_count": 0,
          "topics": [
            "Neuropeptides and Animal Physiology"
          ]
        },
        {
          "openalex_id": "W2982638381",
          "year": 2019,
          "title": "Landscape and Dynamics of Single Immune Cells in Hepatocellular Carcinoma",
          "type": "article",
          "venue": "Cell",
          "cited_by_count": 1685,
          "topics": [
            "Immune Cell Function and Interaction",
            "Immune cells in cancer",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W2587471491",
          "year": 2017,
          "title": "Estimating an EQ-5D-5L Value Set for China",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 737,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4221120384",
          "year": 2022,
          "title": "Immune phenotypic linkage between colorectal cancer and liver metastasis",
          "type": "article",
          "venue": "Cancer Cell",
          "cited_by_count": 475,
          "topics": [
            "Immune Cell Function and Interaction",
            "Cancer Immunotherapy and Biomarkers",
            "Immune cells in cancer"
          ]
        },
        {
          "openalex_id": "W2788315630",
          "year": 2018,
          "title": "Is EQ-5D-5L Better Than EQ-5D-3L? A Head-to-Head Comparison of Descriptive Systems and Value Sets from Seven Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 400,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2295298510",
          "year": 2016,
          "title": "The EQ-5D-5L valuation study in Korea",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 396,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2088673482",
          "year": 2005,
          "title": "Self-Reported Health Status of the General Adult U.S. Population as Assessed by the EQ-5D and Health Utilities Index",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 392,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2115838673",
          "year": 2014,
          "title": "Chinese Time Trade-Off Values for EQ-5D Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 389,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2568974466",
          "year": 2017,
          "title": "Instrument-Defined Estimates of the Minimally Important Difference for EQ-5D-5L Index Scores",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 351,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        }
      ]
    }
  },
  {
    "name": "Nancy Devlin",
    "member_affiliation": "University of Melbourne",
    "is_member": true,
    "projects": [
      {
        "project_id": "1404-RA",
        "title": "Revised title: Are there any challenges in valuing Y-5L arising from the descriptive system? A multi-country study Previous title: A multi-country pilot study of EQ-5D-Y-5L valuation",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1497-RA",
        "title": "Values for EQ-5D-Y-3L: a comparative analysis of value sets and meta-analysis of international valuation data",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2012050",
        "title": "Extension EQ-5D-5L study England for other UK countries",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013040",
        "title": "An investigation of EQ-5D-5L values in the United Arab Emirates: a feasibility study",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014020",
        "title": "Supplementary funding 5L value set study England: LSE",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014170",
        "title": "Directly eliciting personal utility functions: a feasibility study of an innovative approach to valuing HRQoL",
        "working_group": "Others"
      },
      {
        "project_id": "2015060",
        "title": "EuroQol past, present & future publication",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2015100",
        "title": "The distribution of the EQ-5D-5L Index in patient populations",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016320",
        "title": "New methods for analysing the distribution of EQ-5D observations in data sets",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2016570",
        "title": "Anchoring discrete choice experiment values at 0=death for the EQ-5D-Y",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016571",
        "title": "(Proposal extension) Anchoring discrete choice experiment values at 0=dead for the EQ-5D-Y: additional data collection to control for instrument",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016630",
        "title": "An online DCE study to support the development of an EQ-5D-Y value set for the UK",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016631",
        "title": "(Proposal extension) An online DCE study to support the development of an EQ-5D-Y value set for the UK: including an adolescent arm in the study",
        "working_group": "Youth"
      },
      {
        "project_id": "20170010",
        "title": "Guidance on methods for analysing data from EQ-5D instruments",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20180210",
        "title": "Drop dead: an assessment of the conceptual basis for ‘death’ as an anchor in health state valuation",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180650",
        "title": "An international meeting of health system users of EQ-5D in routine outcomes measurement",
        "working_group": "Populations and Health Systems, Education and Outreach"
      },
      {
        "project_id": "20190220",
        "title": "Exploring the relationship between EQ-5D-5L and PROMIS-29",
        "working_group": "Descriptive Systems, Valuation, Populations and Health Systems"
      },
      {
        "project_id": "202-RA",
        "title": "Using EQ-5D-Y to capture children’s HRQoL in economic evaluation: conceptual and empirical challenges for cost effectiveness modelling and implications for modellers and decision makers.",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2274-TVG",
        "title": "Proposed 1-week visit to EuroQol offices & Erasmus University, Rotterdam, November 2025",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "370-RA",
        "title": "A research programme to support and strengthen the use of EQ-5D instruments in China",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "399-RA",
        "title": "Uncertainty around EQ-5D values used in cost effectiveness analysis: identifying types of uncertainty & strengthening the methods to address them",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5103206776",
      "display_name": "Nancy Devlin",
      "orcid": "0000-0002-1561-5361",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 379,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 280
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 88
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 83
        },
        {
          "topic": "Global Health Care Issues",
          "works": 52
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 27
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 26
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 25
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 21
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 13
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 13
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Brendan Mulhern",
          "works": 69
        },
        {
          "name": "David Parkin",
          "works": 52
        },
        {
          "name": "Koonal Shah",
          "works": 44
        },
        {
          "name": "Kim Dalziel",
          "works": 43
        },
        {
          "name": "John Brazier",
          "works": 39
        },
        {
          "name": "Aki Tsuchiya",
          "works": 35
        },
        {
          "name": "Ken Buckingham",
          "works": 34
        },
        {
          "name": "Donna Rowen",
          "works": 32
        },
        {
          "name": "Michael Herdman",
          "works": 24
        },
        {
          "name": "Louise Longworth",
          "works": 24
        },
        {
          "name": "Nick Bansback",
          "works": 22
        },
        {
          "name": "Yan Feng",
          "works": 21
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165187454",
          "year": 2026,
          "title": "The impact of forced choice on person trade-offs: Evidence on age weights for paediatric health gains",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4407630154",
          "year": 2025,
          "title": "A Taxonomy for Assessing Whether HRQoL Value Sets Are Obsolete",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4415746872",
          "year": 2025,
          "title": "A qualitative study to understand public views on the relative value of health gains for children and young people in Australia compared to adults",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "demographic modeling and climate adaptation"
          ]
        },
        {
          "openalex_id": "W4412196677",
          "year": 2025,
          "title": "Assessing the experimental EuroQol toddler and infant populations (EQ-TIPS) descriptive system: a protocol integrating discrete choice experiment (DCE) surveys in instrument development",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4408566995",
          "year": 2025,
          "title": "Can Adolescents Value the EQ-5D-Y-5L and EQ-5D-5L, and How Do the Values Compare? A Feasibility Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4412751203",
          "year": 2025,
          "title": "Comparison of the psychometric performance of experimental EuroQol Toddler and Infant Populations Instrument (EQ-TIPS) and Pediatric Quality of Life Inventory™ (PedsQL) in young children",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Family and Disability Support Research",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W108248000",
          "year": 1994,
          "title": "The costs of mammography screening in New Zealand: evidence from the pilot programmes.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 4,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Survey Methodology and Nonresponse",
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W1999129369",
          "year": 1994,
          "title": "The effects of denturism: New Zealand dentists' response to competition.",
          "type": "article",
          "venue": "American Journal of Public Health",
          "cited_by_count": 7,
          "topics": [
            "Dental Education, Practice, Research",
            "Occupational and Professional Licensing Regulation"
          ]
        },
        {
          "openalex_id": "W4255400076",
          "year": 1995,
          "title": "Comment",
          "type": "article",
          "venue": "Agenda - A Journal of Policy Analysis and Reform",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W3152324104",
          "year": 1995,
          "title": "Comment: Financing New Zealand’s Tertiary Education: How Much Subsidy?",
          "type": "article",
          "venue": "Agenda - A Journal of Policy Analysis and Reform",
          "cited_by_count": 0,
          "topics": [
            "Education Systems and Policy",
            "Higher Education Research Studies",
            "New Zealand Economic and Social Studies"
          ]
        },
        {
          "openalex_id": "W2343426002",
          "year": 2017,
          "title": "Valuing health-related quality of life: An EQ-5D-5L value set for England",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 1416,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2587851012",
          "year": 2017,
          "title": "EQ-5D and the EuroQol Group: Past, Present and Future",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 1218,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2029997282",
          "year": 2010,
          "title": "Development of the EQ-5D-Y: a child-friendly version of the EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 901,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W166560170",
          "year": 2015,
          "title": "Methods for the estimation of the National Institute for Health and Care Excellence cost-effectiveness threshold",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 859,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2239810687",
          "year": 2016,
          "title": "Multiple Criteria Decision Analysis for Health Care Decision Making—An Introduction: Report 1 of the ISPOR MCDA Emerging Good Practices Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 734,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2020460752",
          "year": 2004,
          "title": "Does NICE have a cost‐effectiveness threshold and what other factors influence its decisions? A binary choice analysis",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 712,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2116342090",
          "year": 2002,
          "title": "Preventing Injuries in Older People by Preventing Falls: A Meta‐Analysis of Individual‐Level Data",
          "type": "article",
          "venue": "Journal of the American Geriatrics Society",
          "cited_by_count": 540,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Cerebral Palsy and Movement Disorders",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W1466167365",
          "year": 2007,
          "title": "EQ-5D value sets : inventory, comparative review, and user guide",
          "type": "other",
          "venue": "",
          "cited_by_count": 499,
          "topics": [
            "Product Development and Customization",
            "Manufacturing Process and Optimization"
          ]
        }
      ]
    }
  },
  {
    "name": "Narcis Gusi",
    "member_affiliation": "University of Extremadura (Spain)",
    "is_member": true,
    "projects": [
      {
        "project_id": "20170290",
        "title": "Testing and comparing the Spanish version of EQ-5D-3L-Y and EQ-5D-5L-Y in general and cancer young population",
        "working_group": "Youth"
      },
      {
        "project_id": "355-RA",
        "title": "Feasibility, reliability and validity and of the EQ-5D-Y (3L&5L) in children and adolescents with ADHD",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5042480120",
      "display_name": "Narcís Gusi",
      "orcid": "0000-0002-1001-8883",
      "reported_affiliation": "Complejo Hospitalario de Cáceres",
      "works_count": 254,
      "top_topics": [
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 66
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 56
        },
        {
          "topic": "Balance, Gait, and Falls Prevention",
          "works": 36
        },
        {
          "topic": "Physical Activity and Health",
          "works": 35
        },
        {
          "topic": "Nutrition and Health in Aging",
          "works": 30
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 29
        },
        {
          "topic": "Effects of Vibration on Health",
          "works": 28
        },
        {
          "topic": "Occupational Health and Performance",
          "works": 24
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 16
        },
        {
          "topic": "Children's Physical and Motor Development",
          "works": 16
        },
        {
          "topic": "Ergonomics and Musculoskeletal Disorders",
          "works": 14
        },
        {
          "topic": "Health and Lifestyle Studies",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Santos Villafaina",
          "works": 63
        },
        {
          "name": "Daniel Collado‐Mateo",
          "works": 58
        },
        {
          "name": "José Carmelo Adsuar",
          "works": 57
        },
        {
          "name": "Pedro R. Olivares",
          "works": 56
        },
        {
          "name": "Marcela González‐Gross",
          "works": 43
        },
        {
          "name": "Francisco Javier Domínguez‐Muñoz",
          "works": 40
        },
        {
          "name": "Ignacio Ara",
          "works": 33
        },
        {
          "name": "José A. Casajús",
          "works": 29
        },
        {
          "name": "Juan Luis Leon‐Llamas",
          "works": 28
        },
        {
          "name": "José A. Parraça",
          "works": 27
        },
        {
          "name": "Susana Aznar",
          "works": 24
        },
        {
          "name": "Alba Gómez‐Cabello",
          "works": 24
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160944027",
          "year": 2026,
          "title": "Breastfeeding and dietary habits in childhood and adolescence: the PASOS study",
          "type": "article",
          "venue": "International Breastfeeding Journal",
          "cited_by_count": 0,
          "topics": [
            "Breastfeeding Practices and Influences",
            "Enterobacteriaceae and Cronobacter Research",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W7127619536",
          "year": 2026,
          "title": "Effects of a Strength and Creative Dance Intervention on Brain Electrical Activity, Heart Rate Variability, and Dual-Task Performance in Women with Fibromyalgia: A Randomized Controlled Trial Protocol",
          "type": "article",
          "venue": "Sports",
          "cited_by_count": 0,
          "topics": [
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Diversity and Impact of Dance",
            "Musicians’ Health and Performance"
          ]
        },
        {
          "openalex_id": "W7147047214",
          "year": 2026,
          "title": "Exercise‐Based Interventions for Metabolic and Immune Modulation in Prostate Cancer: A Systematic Review and Meta‐Analysis of RCTs",
          "type": "review",
          "venue": "European Journal of Cancer Care",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Exercise and Physiological Responses",
            "Adipokines, Inflammation, and Metabolic Diseases"
          ]
        },
        {
          "openalex_id": "W7140300366",
          "year": 2026,
          "title": "Family Eating Habits and Dietary Quality of Spanish Children and Adolescents: The PASOS Study",
          "type": "article",
          "venue": "Nutrients",
          "cited_by_count": 0,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Nutritional Studies and Diet",
            "Agriculture Sustainability and Environmental Impact"
          ]
        },
        {
          "openalex_id": "W7161574502",
          "year": 2026,
          "title": "Informational and structural barriers to exercise oncology care in Spain: development of the MOVE-Onco questionnaire and preliminary findings",
          "type": "article",
          "venue": "Clinical & Translational Oncology",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Nutrition and Health in Aging",
            "Lymphatic System and Diseases"
          ]
        },
        {
          "openalex_id": "W7163917115",
          "year": 2026,
          "title": "Latent profiles of movement behaviour compositions and their associations with adiposity and health-related quality of life in Australian children: a cross-sectional and 12-month longitudinal study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Children's Physical and Motor Development",
            "Physical Activity and Health"
          ]
        },
        {
          "openalex_id": "W1543361315",
          "year": 1992,
          "title": "La investigació social de l'esport a Catalunya",
          "type": "article",
          "venue": "Revista d'etnologia de Catalunya",
          "cited_by_count": 0,
          "topics": [
            "Sports and Physical Education Studies",
            "Physical Education and Pedagogy",
            "Physical Education and Sports Studies"
          ]
        },
        {
          "openalex_id": "W84905418",
          "year": 1995,
          "title": "Análisis de la investigación en ciencias del deporte en Cataluña (I): ¿quién, qué y cómo investiga?",
          "type": "article",
          "venue": "Apunts Educación Física y Deportes",
          "cited_by_count": 3,
          "topics": [
            "Sports and Physical Education Studies",
            "Physical Education and Pedagogy",
            "Sports Performance and Training"
          ]
        },
        {
          "openalex_id": "W193061915",
          "year": 1995,
          "title": "Análisis de la investigación en ciencias del deporte en Cataluña (III): estudio prospectivo",
          "type": "article",
          "venue": "Apunts Educación Física y Deportes",
          "cited_by_count": 1,
          "topics": [
            "Sports and Physical Education Studies",
            "Physical Education and Pedagogy",
            "Health, Education, and Physical Culture"
          ]
        },
        {
          "openalex_id": "W109934871",
          "year": 1997,
          "title": "El entrenamiento de la fuerza de salto en gimnasia artística femenina",
          "type": "article",
          "venue": "Apunts Educación Física y Deportes",
          "cited_by_count": 3,
          "topics": [
            "Sports Performance and Training",
            "Sports and Physical Education Studies",
            "Children's Physical and Motor Development"
          ]
        },
        {
          "openalex_id": "W2029997282",
          "year": 2010,
          "title": "Development of the EQ-5D-Y: a child-friendly version of the EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 901,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2064869088",
          "year": 2010,
          "title": "Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 475,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W3007172259",
          "year": 2016,
          "title": "Proceedings of the 3rd IPLeiria’s International Health Congress",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 462,
          "topics": [
            "Digital Mental Health Interventions",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W2133712295",
          "year": 2006,
          "title": "Low-frequency vibratory exercise reduces the risk of bone fracture more than walking: a randomized controlled trial",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 316,
          "topics": [
            "Effects of Vibration on Health",
            "Bone health and osteoporosis research",
            "Exercise and Physiological Responses"
          ]
        },
        {
          "openalex_id": "W3118911070",
          "year": 2021,
          "title": "Impact of COVID-19 Confinement on Physical Activity and Sedentary Behaviour in Spanish University Students: Role of Gender",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 196,
          "topics": [
            "Physical Activity and Health",
            "Health and Lifestyle Studies",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W1970383366",
          "year": 2012,
          "title": "Balance training reduces fear of falling and improves dynamic balance and isometric strength in institutionalised older people: a randomised trial",
          "type": "article",
          "venue": "Journal of physiotherapy",
          "cited_by_count": 172,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Prosthetics and Rehabilitation Robotics",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W2031207378",
          "year": 2006,
          "title": "Exercise in waist‐high warm water decreases pain and improves health‐related quality of life and strength in the lower extremities in women with fibromyalgia",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 168,
          "topics": [
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Musculoskeletal pain and rehabilitation",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W4301258562",
          "year": 2009,
          "title": "The EQ-5D Health-Related Quality of Life Questionnaire",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 158,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare cost, quality, practices"
          ]
        }
      ]
    }
  },
  {
    "name": "Nick Bansback",
    "member_affiliation": "School of Population and Public Health",
    "is_member": true,
    "projects": [
      {
        "project_id": "1624-EO",
        "title": "Developing and delivering a workshop for promoting the use of the EQ-5D as a PROM for improving clinical and shared decision-making in routine care in Asia",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1880-TVG",
        "title": "Visit to National University of Singapore to complete and develop EuroQol projects",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2013290",
        "title": "Investigating the validity of values worse than dead estimated using DCE with duration",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015040",
        "title": "Using routine collection of the EQ-5D to enhance shared decision making: a proof of concept study",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016030",
        "title": "A PROMs based patient decision aid for patients considering total knee arthroplasty: development and a pilot randomized controlled trial.",
        "working_group": "Others"
      },
      {
        "project_id": "20190470",
        "title": "Bringing Patients Back to the PROM. Development and delivery of a workshop to promote the use of the EQ-5D to inform patients",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2133-TVG",
        "title": "Visit to National University of Singapore",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5052496992",
      "display_name": "Nick Bansback",
      "orcid": "0000-0002-1510-3462",
      "reported_affiliation": "Providence Health Care",
      "works_count": 335,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 105
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 89
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 42
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 41
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 34
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 33
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 18
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 16
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 13
        },
        {
          "topic": "Obstructive Sleep Apnea Research",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Aslam H. Anis",
          "works": 66
        },
        {
          "name": "Mark Harrison",
          "works": 47
        },
        {
          "name": "John Brazier",
          "works": 33
        },
        {
          "name": "Aki Tsuchiya",
          "works": 31
        },
        {
          "name": "Brendan Mulhern",
          "works": 31
        },
        {
          "name": "Daphne Guh",
          "works": 30
        },
        {
          "name": "Larry D. Lynd",
          "works": 30
        },
        {
          "name": "Carlo A. Marra",
          "works": 26
        },
        {
          "name": "Louise Longworth",
          "works": 24
        },
        {
          "name": "Donna Rowen",
          "works": 23
        },
        {
          "name": "Nancy Devlin",
          "works": 22
        },
        {
          "name": "Arne Risa Hole",
          "works": 22
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7139932305",
          "year": 2026,
          "title": "Can Patient-Reported Outcome Measures Help Predict Unplanned Hospital Readmission?",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 0,
          "topics": [
            "Heart Failure Treatment and Management",
            "Hospital Admissions and Outcomes",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4415522504",
          "year": 2025,
          "title": "Active remote monitoring of long-term conditions with mobile devices: a systematic review of cost-effectiveness analyses",
          "type": "review",
          "venue": "npj Digital Medicine",
          "cited_by_count": 1,
          "topics": [
            "Mobile Health and mHealth Applications",
            "Telemedicine and Telehealth Implementation",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4407922422",
          "year": 2025,
          "title": "Biosimilar Policies and Their Impact on Market Penetration of Adalimumab, Etanercept and Infliximab: A Policy Synthesis and Descriptive Analysis in 13 OECD Countries",
          "type": "article",
          "venue": "BioDrugs",
          "cited_by_count": 5,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Pharmaceutical Economics and Policy",
            "Inflammatory Bowel Disease"
          ]
        },
        {
          "openalex_id": "W4415930097",
          "year": 2025,
          "title": "Bridging the gap between expanded pharmacy services and payment models: A jurisdictional scan",
          "type": "article",
          "venue": "Journal of the American Pharmacists Association",
          "cited_by_count": 1,
          "topics": [
            "Medication Adherence and Compliance",
            "Pharmaceutical Practices and Patient Outcomes",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4407073231",
          "year": 2025,
          "title": "Client preferences for the design and delivery of injectable opioid agonist treatment services: Results From a best-worst scaling task",
          "type": "article",
          "venue": "Drug and Alcohol Dependence",
          "cited_by_count": 0,
          "topics": [
            "Opioid Use Disorder Treatment",
            "Pharmaceutical Practices and Patient Outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4414618890",
          "year": 2025,
          "title": "Community partnered peer support after traumatic brain injury: a feasibility case study",
          "type": "article",
          "venue": "Brain Impairment",
          "cited_by_count": 1,
          "topics": [
            "Traumatic Brain Injury Research",
            "Mental Health and Patient Involvement",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W2587222402",
          "year": 2000,
          "title": "A Review of the Clinical and Cost-effectiveness of Gemcitabine for the Treatment of Pancreatic Cancer",
          "type": "review",
          "venue": "",
          "cited_by_count": 3,
          "topics": [
            "Pancreatic and Hepatic Oncology Research",
            "Colorectal Cancer Treatments and Studies",
            "Gastric Cancer Management and Outcomes"
          ]
        },
        {
          "openalex_id": "W2034557246",
          "year": 2001,
          "title": "A rapid and systematic review of the clinical effectiveness and cost-effectiveness of gemcitabine for the treatment of pancreatic cancer",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 27,
          "topics": [
            "Pancreatic and Hepatic Oncology Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W1757970254",
          "year": 2002,
          "title": "A rapid and systematic review of the evidence for the clinical effectiveness and cost-effectiveness of irinotecan, oxaliplatin and raltitrexed for the treatment of advanced colorectal cancer.",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 42,
          "topics": [
            "Colorectal Cancer Treatments and Studies",
            "Gastric Cancer Management and Outcomes",
            "Colorectal and Anal Carcinomas"
          ]
        },
        {
          "openalex_id": "W1983060138",
          "year": 2004,
          "title": "?Economic evaluation of gemcitabine in the treatment of pancreatic cancer in the UK?",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 4,
          "topics": [
            "Pancreatic and Hepatic Oncology Research",
            "Gastric Cancer Management and Outcomes",
            "Colorectal Cancer Screening and Detection"
          ]
        },
        {
          "openalex_id": "W1994014704",
          "year": 2009,
          "title": "The incidence of co-morbidities related to obesity and overweight: A systematic review and meta-analysis",
          "type": "review",
          "venue": "BMC Public Health",
          "cited_by_count": 3879,
          "topics": [
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Bariatric Surgery and Outcomes",
            "Cardiovascular Function and Risk Factors"
          ]
        },
        {
          "openalex_id": "W2405193268",
          "year": 2015,
          "title": "A Time Trade-off-derived Value Set of the EQ-5D-5L for Canada",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 490,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2055936215",
          "year": 2010,
          "title": "Measuring and valuing productivity loss due to poor health: A critical review",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 353,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Workplace Health and Well-being",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W1980705643",
          "year": 2010,
          "title": "Validity of the work productivity and activity impairment questionnaire - general health version in patients with rheumatoid arthritis",
          "type": "article",
          "venue": "Arthritis Research & Therapy",
          "cited_by_count": 293,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2020438811",
          "year": 2011,
          "title": "Using a discrete choice experiment to estimate health state utility values",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 261,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2001600469",
          "year": 2009,
          "title": "Obesity and overweight in Canada: an updated cost‐of‐illness study",
          "type": "article",
          "venue": "Obesity Reviews",
          "cited_by_count": 251,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Obesity and Health Practices",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1710831723",
          "year": 2015,
          "title": "Physician attitudes toward shared decision making: A systematic review",
          "type": "review",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 248,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Healthcare Systems and Technology",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2140801668",
          "year": 2011,
          "title": "The financial cost of doctors emigrating from sub-Saharan Africa: human capital analysis",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 246,
          "topics": [
            "Global Health Workforce Issues",
            "Global Health and Surgery",
            "Global Maternal and Child Health"
          ]
        }
      ]
    }
  },
  {
    "name": "Nils Gutacker",
    "member_affiliation": "Centre for Health Economics, University of York",
    "is_member": true,
    "projects": [
      {
        "project_id": "123-RA",
        "title": "Decomposing the socioeconomic gradient in health-related quality of life over the life course (DeQoL-LIFE)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1479-TVG",
        "title": "Research visit to University of Auckland to facilitate collaborative working and engage with local stakeholders to promote routine PROM data collection and analysis in the New Zealand healthcare system.",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1925-TVG",
        "title": "Research visit to University Technology Sydney, Macquarie University, Monash University and National University of Singapore to facilitate collaborative working on existing and planned research projects and build new networks.",
        "working_group": "Descriptive Systems, Populations and Health Systems, Education and Outreach"
      },
      {
        "project_id": "2016450",
        "title": "The role of EQ-5D value sets based on patient preferences in the context of hospital choice in the national PROM programme in England",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20190910",
        "title": "Case-mix adjustment of EQ-5D health profiles for the purpose of hospital performance assessment",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2192-RA",
        "title": "Differences in utility scores between the forthcoming UK EQ-5D-5L tariff and the 3L-to-5L crosswalk across population groups",
        "working_group": "Valuation, Populations and Health Systems"
      },
      {
        "project_id": "2415-TVG",
        "title": "Research visit to University of British Columbia, University of Alberta, and McMaster University to facilitate collaborative working and engage with local stakeholders to promote routine PROM data collection and analysis in the Canadian healthcare system",
        "working_group": "Populations and Health Systems, Education and Outreach"
      },
      {
        "project_id": "2653-TVG",
        "title": "Presentation at APERSU conference & development of joint research projects on value-based pricing using EQ-5D",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5023093255",
      "display_name": "Nils Gutacker",
      "orcid": "0000-0002-2833-0621",
      "reported_affiliation": "University of York",
      "works_count": 120,
      "top_topics": [
        {
          "topic": "Healthcare Policy and Management",
          "works": 50
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 45
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 31
        },
        {
          "topic": "Global Health Care Issues",
          "works": 21
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 12
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 12
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 12
        },
        {
          "topic": "Hip and Femur Fractures",
          "works": 12
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 11
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 10
        },
        {
          "topic": "Healthcare Operations and Scheduling Optimization",
          "works": 7
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Hugh Gravelle",
          "works": 26
        },
        {
          "name": "Andrew Street",
          "works": 22
        },
        {
          "name": "Luigi Siciliani",
          "works": 21
        },
        {
          "name": "Anne Mason",
          "works": 21
        },
        {
          "name": "Rowena Jacobs",
          "works": 20
        },
        {
          "name": "Tim Doran",
          "works": 18
        },
        {
          "name": "Karen Bloor",
          "works": 15
        },
        {
          "name": "Chris Bojke",
          "works": 15
        },
        {
          "name": "Maria Goddard",
          "works": 15
        },
        {
          "name": "Tony Kendrick",
          "works": 12
        },
        {
          "name": "Simon Gilbody",
          "works": 12
        },
        {
          "name": "Richard Cookson",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155192421",
          "year": 2026,
          "title": "Effect of NHS surgical hubs on elective primary hip-and-knee replacement volume, length of stay and waiting times: national longitudinal difference-in-differences study",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Healthcare Operations and Scheduling Optimization",
            "Surgical site infection prevention"
          ]
        },
        {
          "openalex_id": "W7167940777",
          "year": 2026,
          "title": "Is higher-quality secondary mental healthcare more costly? A systematic review",
          "type": "review",
          "venue": "Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Mental Health Treatment and Access",
            "Primary Care and Health Outcomes",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W7126008405",
          "year": 2026,
          "title": "Paying for Health Gains Using Patient Reported Outcome Measures",
          "type": "article",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W7131269027",
          "year": 2026,
          "title": "Paying for Health Gains Using Patient Reported Outcome Measures",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W7161000161",
          "year": 2026,
          "title": "Public service and private profit: a mixed methods study of cataract surgery in England",
          "type": "article",
          "venue": "Health Economics Policy and Law",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare innovation and challenges",
            "Healthcare Operations and Scheduling Optimization"
          ]
        },
        {
          "openalex_id": "W7138928284",
          "year": 2026,
          "title": "Shared clinical governance arrangements between NHS and independent acute hospitals in England: Findings from a national survey of senior leaders",
          "type": "article",
          "venue": "Journal of Health Services Research & Policy",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Quality and Management",
            "Primary Care and Health Outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2131145329",
          "year": 2009,
          "title": "Amputations in PAD patients: Data from the German Federal Statistical Office",
          "type": "article",
          "venue": "Vascular Medicine",
          "cited_by_count": 16,
          "topics": [
            "Peripheral Artery Disease Management",
            "Diabetic Foot Ulcer Assessment and Management",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W1983566202",
          "year": 2011,
          "title": "PHP43 Exploring Social Determinants of the Health of International Immigrants in Chile: The Global Health Status Index",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Public Health and Social Inequalities",
            "Migration, Education, Indigenous Social Dynamics",
            "Migration, Health and Trauma"
          ]
        },
        {
          "openalex_id": "W3123578216",
          "year": 2011,
          "title": "Truly Inefficient or Providing Better Quality of Care? Analysing the Relationship between Risk-Adjusted Hospital Costs and Patients’ Health Outcomes",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1556962627",
          "year": 2012,
          "title": "Analysing hospital variation in health outcome at the level of EQ-5D dimensions",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2515465447",
          "year": 2016,
          "title": "Choice of hospital: Which type of quality matters?",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 167,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2637653848",
          "year": 2017,
          "title": "Socioeconomic inequality of access to healthcare: Does choice explain the gradient?",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 165,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2530421404",
          "year": 2016,
          "title": "Proceedings of Patient Reported Outcome Measure’s (PROMs) Conference Sheffield 2016: advances in patient reported outcomes research",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 152,
          "topics": [
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W3206005223",
          "year": 2021,
          "title": "Need, demand, supply in health care: working definitions, and their implications for defining access",
          "type": "article",
          "venue": "Health Economics Policy and Law",
          "cited_by_count": 107,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4291164944",
          "year": 2022,
          "title": "Quality-Adjusted Life Expectancy Norms for the English Population",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 102,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2470991196",
          "year": 2016,
          "title": "Location, quality and choice of hospital: Evidence from England 2002–2013",
          "type": "article",
          "venue": "Regional Science and Urban Economics",
          "cited_by_count": 99,
          "topics": [
            "Healthcare Policy and Management",
            "Patient Satisfaction in Healthcare",
            "Hospital Admissions and Outcomes"
          ]
        },
        {
          "openalex_id": "W2125606670",
          "year": 2015,
          "title": "Comparing the performance of the Charlson/Deyo and Elixhauser comorbidity measures across five European countries and three conditions",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 83,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Chronic Disease Management Strategies",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W1546099627",
          "year": 2015,
          "title": "Addressing Missing Data in Patient‐Reported Outcome Measures (PROMS): Implications for the Use of PROMS for Comparing Provider Performance",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 72,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Statistical Methods and Inference"
          ]
        }
      ]
    }
  }
]
