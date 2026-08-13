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
    "name": "Suzana Karim",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "138-RA",
        "title": "Preference heterogeneity in health valuation: Peru EQ-VT data",
        "working_group": "Valuation"
      },
      {
        "project_id": "139-RA",
        "title": "Preference heterogeneity in health valuation: Dutch BWS data",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190230R1",
        "title": "Preference heterogeneity in health valuation",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5003389681",
      "display_name": "Suzana Karim",
      "orcid": "0000-0002-3370-1554",
      "reported_affiliation": "University of Dhaka",
      "works_count": 6,
      "top_topics": [
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 3
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 2
        },
        {
          "topic": "Sensory Analysis and Statistical Methods",
          "works": 1
        },
        {
          "topic": "Customer Service Quality and Loyalty",
          "works": 1
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 1
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Benjamin M. Craig",
          "works": 5
        },
        {
          "name": "Karin Groothuis‐Oudshoorn",
          "works": 2
        },
        {
          "name": "Romina A. Tejada",
          "works": 2
        },
        {
          "name": "Federico Augustovski",
          "works": 2
        },
        {
          "name": "Caroline Vass",
          "works": 1
        },
        {
          "name": "Stephen Poteet",
          "works": 1
        },
        {
          "name": "Atonu Rabbani",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407269429",
          "year": 2025,
          "title": "Examining the association between service coverage of UHC and global disease burden: A cross-country panel analysis",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 1,
          "topics": [
            "Global Health Care Issues",
            "Global Public Health Policies and Epidemiology",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4313476109",
          "year": 2023,
          "title": "Preference heterogeneity in health valuation: a latent class analysis of the Peru EQ-5D-5L values",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4291144272",
          "year": 2022,
          "title": "Current Practices for Accounting for Preference Heterogeneity in Health-Related Discrete Choice Experiments: A Systematic Review",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 22,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Sensory Analysis and Statistical Methods"
          ]
        },
        {
          "openalex_id": "W4281486671",
          "year": 2022,
          "title": "Exploring the importance of controlling heteroskedasticity and heterogeneity in health valuation: a case study on Dutch EQ-5D-5L",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4280619924",
          "year": 2022,
          "title": "Preference Heterogeneity in Health Valuation: A Latent Class Analysis of the Peru EQ-5D-5L Values",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3134404192",
          "year": 2021,
          "title": "Does Controlling for Scale Heterogeneity Better Explain Respondents’ Preference Segmentation in Discrete Choice Experiments? A Case Study of US Health Insurance Demand",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 9,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Customer Service Quality and Loyalty"
          ]
        }
      ]
    }
  },
  {
    "name": "Taavi Lai",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2602-SG",
        "title": "Translation, cultural adaptation, and feasibility testing of the EQ-HWB-9 in Estonian and Russian languages within Estonia’s emerging integrated care networks (TERVIK)",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5109074641",
      "display_name": "Taavi Lai",
      "orcid": "",
      "reported_affiliation": "The Fourth People's Hospital",
      "works_count": 46,
      "top_topics": [
        {
          "topic": "Health disparities and outcomes",
          "works": 12
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Air Quality and Health Impacts",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 7
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 5
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 4
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 3
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 3
        },
        {
          "topic": "HIV/AIDS Impact and Responses",
          "works": 3
        },
        {
          "topic": "Substance Abuse Treatment and Outcomes",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Semaw Ferede Abera",
          "works": 8
        },
        {
          "name": "Tom Achoki",
          "works": 8
        },
        {
          "name": "Zewdie Aderaw Alemu",
          "works": 8
        },
        {
          "name": "Walid Ammar",
          "works": 8
        },
        {
          "name": "Palwasha Anwari",
          "works": 8
        },
        {
          "name": "Raghib Ali",
          "works": 7
        },
        {
          "name": "Nelson Alvis‐Guzmán",
          "works": 7
        },
        {
          "name": "Sanjay Basu",
          "works": 7
        },
        {
          "name": "Ibrahim Abubakar",
          "works": 7
        },
        {
          "name": "Elena Álvarez",
          "works": 7
        },
        {
          "name": "Reza Assadi",
          "works": 7
        },
        {
          "name": "Jerry Abraham",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128071457",
          "year": 2026,
          "title": "Health-Related Quality of Life Among Ukrainian War Refugees Compared to the General Population in Estonia",
          "type": "article",
          "venue": "International Journal of Public Health",
          "cited_by_count": 1,
          "topics": [
            "Migration, Health and Trauma",
            "Posttraumatic Stress Disorder Research",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7120120859",
          "year": 2026,
          "title": "Using a return on investment analysis to estimate the economic impact of potential changes to alcohol control policies in Estonia",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 1,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W4400103463",
          "year": 2024,
          "title": "Health system performance assessment and reforms, Oman",
          "type": "article",
          "venue": "Bulletin of the World Health Organization",
          "cited_by_count": 7,
          "topics": [
            "Global Maternal and Child Health",
            "Middle East and Rwanda Conflicts",
            "HIV/AIDS Impact and Responses"
          ]
        },
        {
          "openalex_id": "W4307168746",
          "year": 2022,
          "title": "Conducting national burden of disease studies and knowledge translation in eight small European states: challenges and opportunities",
          "type": "article",
          "venue": "Health Research Policy and Systems",
          "cited_by_count": 7,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Health Policy Implementation Science",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4281756842",
          "year": 2022,
          "title": "Estimating risk factor attributable burden – challenges and potential solutions when using the comparative risk assessment methodology",
          "type": "article",
          "venue": "Archives of Public Health",
          "cited_by_count": 47,
          "topics": [
            "Environmental and Social Impact Assessments",
            "Air Quality and Health Impacts",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2900658421",
          "year": 2018,
          "title": "Cost-effectiveness of strategies to prevent road traffic injuries in eastern sub-Saharan Africa and Southeast Asia: new results from WHO-CHOICE",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 23,
          "topics": [
            "Traffic and Road Safety",
            "Injury Epidemiology and Prevention",
            "Automotive and Human Injury Biomechanics"
          ]
        },
        {
          "openalex_id": "W96918666",
          "year": 2005,
          "title": "Cost-Effectiveness of Mental Health Interventions in Estonia",
          "type": "article",
          "venue": "",
          "cited_by_count": 9,
          "topics": [
            "Mental Health Treatment and Access",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2135626434",
          "year": 2007,
          "title": "Costs, health effects and cost-effectiveness of alcohol and tobacco control strategies in Estonia",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 54,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2911314529",
          "year": 2008,
          "title": "Parkinson's Disease Questionnaire--Estonian Version",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments"
          ]
        },
        {
          "openalex_id": "W2172144373",
          "year": 2008,
          "title": "Validation of an Estonian version of the Parkinson's Disease Questionnaire (PDQ-39)",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 19,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Voice and Speech Disorders",
            "Balance, Gait, and Falls Prevention"
          ]
        },
        {
          "openalex_id": "W2163710303",
          "year": 2014,
          "title": "Global, regional, and national prevalence of overweight and obesity in children and adults during 1980–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 12111,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Child Nutrition and Water Access",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W2098082628",
          "year": 2015,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 301 acute and chronic diseases and injuries in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 6529,
          "topics": [
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W3143437408",
          "year": 2015,
          "title": "Global, regional, and national comparative risk assessment of 79 behavioural, environmental and occupational, and metabolic risks or clusters of risks in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2758,
          "topics": [
            "Health, Environment, Cognitive Aging",
            "Air Quality and Health Impacts",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2142472354",
          "year": 2015,
          "title": "Global, regional, and national disability-adjusted life years (DALYs) for 306 diseases and injuries and healthy life expectancy (HALE) for 188 countries, 1990–2013: quantifying the epidemiological transition",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2022,
          "topics": [
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2043449557",
          "year": 2014,
          "title": "Global, regional, and national levels and causes of maternal mortality during 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1676,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and fetal healthcare",
            "HIV/AIDS Research and Interventions"
          ]
        },
        {
          "openalex_id": "W2128886090",
          "year": 2014,
          "title": "Global, regional, and national incidence and mortality for HIV, tuberculosis, and malaria during 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 995,
          "topics": [
            "HIV/AIDS Impact and Responses",
            "Global Maternal and Child Health",
            "HIV/AIDS Research and Interventions"
          ]
        },
        {
          "openalex_id": "W2163987497",
          "year": 2014,
          "title": "Global, regional, and national levels of neonatal, infant, and under-5 mortality during 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 809,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2148635296",
          "year": 2012,
          "title": "New Methodology for Estimating the Burden of Infectious Diseases in Europe",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 141,
          "topics": [
            "Zoonotic diseases and public health",
            "Viral gastroenteritis research and epidemiology",
            "Animal Disease Management and Epidemiology"
          ]
        }
      ]
    }
  },
  {
    "name": "Takeru Shiroiwa",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180280",
        "title": "EQ-5D-Y valuation study in Japan",
        "working_group": "Youth"
      },
      {
        "project_id": "2098-RA",
        "title": "A Comparison Study of the New Discrete Choice Method and Traditional Composite Time Trade-Off in Japan",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5007564965",
      "display_name": "Takeru Shiroiwa",
      "orcid": "0000-0003-3055-9932",
      "reported_affiliation": "National Institute of Public Health",
      "works_count": 166,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 83
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 22
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 18
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 17
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 17
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 14
        },
        {
          "topic": "Colorectal Cancer Treatments and Studies",
          "works": 14
        },
        {
          "topic": "Pharmacy and Medical Practices",
          "works": 10
        },
        {
          "topic": "Global Health Care Issues",
          "works": 9
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 8
        },
        {
          "topic": "Patient Safety and Medication Errors",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Takashi Fukuda",
          "works": 90
        },
        {
          "name": "Kojiro Shimozuma",
          "works": 67
        },
        {
          "name": "Shunya Ikeda",
          "works": 32
        },
        {
          "name": "Shinichi Noto",
          "works": 31
        },
        {
          "name": "Shinya Saito",
          "works": 25
        },
        {
          "name": "Naruto Taira",
          "works": 20
        },
        {
          "name": "Yasuhiro Hagiwara",
          "works": 20
        },
        {
          "name": "Ataru Igarashi",
          "works": 15
        },
        {
          "name": "Takuya Kawahara",
          "works": 14
        },
        {
          "name": "Yasuo Ohashi",
          "works": 14
        },
        {
          "name": "Kiichiro Tsutani",
          "works": 13
        },
        {
          "name": "Naomi Akiyama",
          "works": 13
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7126069466",
          "year": 2026,
          "title": "Departures from health universalism? A value set of AP-7D in Japan as an attempt to develop a “culture-specific” preference-based measure",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W7162491165",
          "year": 2026,
          "title": "Multicenter open-label randomized trial of the utility of electronic patient-reported outcome monitoring system in patients with advanced solid tumors (PRO-MOTE).",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Cancer survivorship and care",
            "Advanced Breast Cancer Therapies",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W7137939674",
          "year": 2026,
          "title": "Psychometric performance of the EQ-HWB-25 and EQ-HWB-9 in Japan: evidence from a large web-based survey of multimorbidity and depression",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Chronic Disease Management Strategies",
            "Cardiovascular Health and Risk Factors",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W4417022934",
          "year": 2025,
          "title": "A cross-country comparison of the psychometric performance of SF-6Dv2 and EQ-5D-5L",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W7145116806",
          "year": 2025,
          "title": "Conceptual framework for caregivers' quality of life and well-being supporting children with special health and medical needs in East Asia: a systematic review and narrative synthesis",
          "type": "article",
          "venue": "Institutional Repositories DataBase (IRDB)",
          "cited_by_count": 0,
          "topics": [
            "Family and Disability Support Research",
            "Childhood Cancer Survivors' Quality of Life",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W4414162400",
          "year": 2025,
          "title": "Conceptual framework for caregivers’ quality of life and well-being supporting children with special health and medical needs in East Asia: a systematic review and narrative synthesis",
          "type": "book-review",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Family and Disability Support Research",
            "Childhood Cancer Survivors' Quality of Life",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W2159241012",
          "year": 2004,
          "title": "Identification of Renieramycin A as an Antileishmanial Substance in a Marine Sponge Neopetrosia sp.",
          "type": "article",
          "venue": "Marine Drugs",
          "cited_by_count": 59,
          "topics": [
            "Synthesis and Biological Activity",
            "Traditional and Medicinal Uses of Annonaceae",
            "Marine Sponges and Natural Products"
          ]
        },
        {
          "openalex_id": "W1990076987",
          "year": 2007,
          "title": "Cost-effectiveness analysis of bevacizumab combined with chemotherapy for the treatment of metastatic colorectal cancer in Japan",
          "type": "article",
          "venue": "Clinical Therapeutics",
          "cited_by_count": 46,
          "topics": [
            "Colorectal Cancer Treatments and Studies",
            "Economic and Financial Impacts of Cancer",
            "Cancer Treatment and Pharmacology"
          ]
        },
        {
          "openalex_id": "W2100717480",
          "year": 2007,
          "title": "The model-based cost-effectiveness analysis of 1-year adjuvant trastuzumab treatment: based on 2-year follow-up HERA trial data",
          "type": "article",
          "venue": "Breast Cancer Research and Treatment",
          "cited_by_count": 49,
          "topics": [
            "HER2/EGFR in Cancer Research",
            "Breast Cancer Treatment Studies",
            "Protease and Inhibitor Mechanisms"
          ]
        },
        {
          "openalex_id": "W1978314406",
          "year": 2008,
          "title": "PMC34 INTERNATIONAL SURVEY ONWTP FOR ONE ADDITIONAL QALY GAIN—HOW MUCH IS THE THRESHOLD OF COST-EFFECTIVENESS ANALYSIS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2119440126",
          "year": 2009,
          "title": "International survey on willingness‐to‐pay (WTP) for one additional QALY gained: what is the threshold of cost effectiveness?",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 693,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W1936620973",
          "year": 2015,
          "title": "Japanese population norms for preference-based measures: EQ-5D-3L, EQ-5D-5L, and SF-6D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 341,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W2343671706",
          "year": 2016,
          "title": "Comparison of Value Set Based on DCE and/or TTO Data: Scoring for EQ-5D-5L Health States in Japan",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 320,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2561287536",
          "year": 2015,
          "title": "Developing a Japanese version of the EQ-5D-5L value set",
          "type": "article",
          "venue": "Hoken iryou kagaku",
          "cited_by_count": 162,
          "topics": [
            "Risk and Safety Analysis",
            "Quality Function Deployment in Product Design",
            "Technology Assessment and Management"
          ]
        },
        {
          "openalex_id": "W2534063642",
          "year": 2016,
          "title": "Development of an Official Guideline for the Economic Evaluation of Drugs/Medical Devices in Japan",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 159,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Pharmacy and Medical Practices"
          ]
        },
        {
          "openalex_id": "W2172023244",
          "year": 2013,
          "title": "WTP for a QALY and health states: More money for severer health states?",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 139,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2995914467",
          "year": 2019,
          "title": "Formal Implementation of Cost-Effectiveness Evaluations in Japan: A Unique Health Technology Assessment System",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 116,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W3157544365",
          "year": 2021,
          "title": "Japanese Population Norms of EQ-5D-5L and Health Utilities Index Mark 3: Disutility Catalog by Disease and Symptom in Community Settings",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 114,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Systems and Reforms"
          ]
        }
      ]
    }
  },
  {
    "name": "Teresa Tsui",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1456-PD",
        "title": "EQ-5D-5L health utilities to inform cancer drug funding decisions",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5089652474",
      "display_name": "Teresa Tsui",
      "orcid": "0000-0002-9806-9393",
      "reported_affiliation": "Sunnybrook Health Science Centre",
      "works_count": 17,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "COVID-19 and healthcare impacts",
          "works": 3
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 3
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 3
        },
        {
          "topic": "Complementary and Alternative Medicine Studies",
          "works": 3
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 3
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 2
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Circadian rhythm and melatonin",
          "works": 1
        },
        {
          "topic": "Dietary Effects on Health",
          "works": 1
        },
        {
          "topic": "Genetics, Aging, and Longevity in Model Organisms",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Murray Krahn",
          "works": 8
        },
        {
          "name": "Karen E. Bremner",
          "works": 6
        },
        {
          "name": "Maureen Trudeau",
          "works": 4
        },
        {
          "name": "Nicholas Mitsakakis",
          "works": 4
        },
        {
          "name": "Aileen M. Davis",
          "works": 4
        },
        {
          "name": "Seraphine Zeitouny",
          "works": 3
        },
        {
          "name": "Douglas C. Cheung",
          "works": 3
        },
        {
          "name": "Reka Pataky",
          "works": 3
        },
        {
          "name": "Stuart Peacock",
          "works": 3
        },
        {
          "name": "Lauren Lapointe‐Shaw",
          "works": 3
        },
        {
          "name": "Andrew Mendlowitz",
          "works": 3
        },
        {
          "name": "Carol Mulder",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4416392341",
          "year": 2025,
          "title": "Examining the Association Between Equity-Related Factors and EQ-5D-3L Health Utilities of Patients with Cancer",
          "type": "article",
          "venue": "Current Oncology",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4410782729",
          "year": 2025,
          "title": "Patient Experiences Regarding Feasibility of Implementing Real-World EQ-5D Collection at an Oncology Centre in Ontario, Canada",
          "type": "article",
          "venue": "Current Oncology",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4396889150",
          "year": 2024,
          "title": "A scoping review to create a framework for the steps in developing condition-specific preference-based instruments de novo or from an existing non-preference-based instrument: use of item response theory or Rasch analysis",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health Education and Validation",
            "Mental Health Research Topics"
          ]
        },
        {
          "openalex_id": "W4394610985",
          "year": 2024,
          "title": "Creating a Multiply Imputed Value Set for the EQ-5D-5L in Canada: State-Level Misspecification Terms Are Needed to Characterize Parameter Uncertainty Correctly",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4386559886",
          "year": 2023,
          "title": "The impact of the early COVID-19 pandemic on healthcare system resource use and costs in two provinces in Canada: An interrupted time series analysis",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 33,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 epidemiological studies",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4313065328",
          "year": 2022,
          "title": "Breast Utility Instrument",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Breast Implant and Reconstruction",
            "Cancer Risks and Factors",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W2170181695",
          "year": 2011,
          "title": "Melatonin as Adjuvant Cancer Care With and Without Chemotherapy",
          "type": "article",
          "venue": "Integrative Cancer Therapies",
          "cited_by_count": 172,
          "topics": [
            "Circadian rhythm and melatonin",
            "Dietary Effects on Health",
            "Genetics, Aging, and Longevity in Model Organisms"
          ]
        },
        {
          "openalex_id": "W2549378677",
          "year": 2012,
          "title": "The Role of Scientific Evidence in Natural Health Product Consumer Decision Making in Osteoarthritis",
          "type": "dissertation",
          "venue": "TSpace (University of Toronto)",
          "cited_by_count": 0,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Pharmaceutical Quality and Counterfeiting",
            "Botanical Studies and Applications"
          ]
        },
        {
          "openalex_id": "W2025029372",
          "year": 2012,
          "title": "Understanding the role of scientific evidence in consumer evaluation of natural health products for osteoarthritis an application of the means end chain approach",
          "type": "article",
          "venue": "BMC Complementary and Alternative Medicine",
          "cited_by_count": 15,
          "topics": [
            "Cognitive and psychological constructs research",
            "Sensory Analysis and Statistical Methods",
            "Pain Management and Placebo Effect"
          ]
        },
        {
          "openalex_id": "W1984010276",
          "year": 2015,
          "title": "2014 IN-CAM Research Symposium: The Next Wave of Complementary and Integrative Medicine and Health Care Research",
          "type": "article",
          "venue": "Journal of Complementary and Integrative Medicine",
          "cited_by_count": 1,
          "topics": [
            "Acupuncture Treatment Research Studies",
            "Medicinal Plants and Bioactive Compounds"
          ]
        },
        {
          "openalex_id": "W4210802657",
          "year": 2022,
          "title": "Developing the Breast Utility Instrument, a preference-based instrument to measure health-related quality of life in women with breast cancer: Confirmatory factor analysis of the EORTC QLQ-C30 and BR45 to establish dimensions",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 10,
          "topics": [
            "Cancer survivorship and care",
            "Breast Cancer Treatment Studies",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4296511223",
          "year": 2022,
          "title": "Initial health care costs for COVID-19 in British Columbia and Ontario, Canada: an interprovincial population-based cohort study",
          "type": "article",
          "venue": "CMAJ Open",
          "cited_by_count": 9,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W2899418922",
          "year": 2018,
          "title": "Naturopathy Special Interest Group Research Capacity and Needs Assessment Survey",
          "type": "article",
          "venue": "The Journal of Alternative and Complementary Medicine",
          "cited_by_count": 8,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Therapeutic Uses of Natural Elements",
            "Health and Medical Research Impacts"
          ]
        },
        {
          "openalex_id": "W4229033896",
          "year": 2022,
          "title": "“Bring the Hoses to Where the Fire Is!”: Differential Impacts of Marginalization and Socioeconomic Status on COVID-19 Case Counts and Healthcare Costs",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 7,
          "topics": [
            "COVID-19 epidemiological studies",
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4312066442",
          "year": 2022,
          "title": "Developing the Breast Utility Instrument to Measure Health-Related Quality-of-Life Preferences in Patients with Breast Cancer: Selecting the Item for Each Dimension",
          "type": "article",
          "venue": "MDM Policy & Practice",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Cancer Incidence and Screening",
            "Breast Cancer Treatment Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Tessa Peasgood",
    "member_affiliation": "University of Sheffield",
    "is_member": true,
    "projects": [
      {
        "project_id": "1823-RA",
        "title": "Developing an interviewer administered version of O-PUF (Online Personal Utility Function): a first step involving co-design with members of the public.",
        "working_group": "Valuation"
      },
      {
        "project_id": "1916-RA",
        "title": "Testing the validity of the EQ-HWB-S in a clinical setting with patients with rare neurological conditions, and their carers",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "20180350",
        "title": "Extending the QALY Valuation Study in the UK: A feasibility study of applying different valuation methods to a health and wellbeing classification system",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190260",
        "title": "Budget transfer from international Psychometric surveys to TUOS",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2207-RA",
        "title": "What are the additional benefits and challenges of collecting the 25 item EQ-HWB compared to the EQ-HWB-S in care home settings?",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "224-RA",
        "title": "A review of the impact of a one day versus a seven-day recall period on domains from the EQ-5D and EQ-HWB instruments",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2366-EO",
        "title": "Sponsporship request for UK PROMS conference 2026",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2470-RA",
        "title": "Exploring the validity of EQ-5D-5L in older populations using SIPHER data from the UK",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2488-TVG",
        "title": "Speaking at an Issues Panel at ISPOR Europe (Glasgow, November 2025) in which transitions between EuroQol instruments (EQ-TIPs to EQ-5D-Y-5L to EQ-5D-5L) will be discussed \"Handling Transitions Between Child and Adult HRQoL in Economic Evaluation\"",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2493-RA",
        "title": "Guidance for qualitative studies to test the content validity of bolt-ons",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "282-RA",
        "title": "Randomised equivalence study to compare online interviews versus face-to-face interviews to value the EQ-5D-5L using cTTO: Australian arm",
        "working_group": "Valuation"
      },
      {
        "project_id": "348-PHD",
        "title": "The social value of avoiding poor health states in children",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5022446221",
      "display_name": "Tessa Peasgood",
      "orcid": "0000-0001-8024-7801",
      "reported_affiliation": "University of Sheffield",
      "works_count": 121,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 66
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 18
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 15
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 13
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 11
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 7
        },
        {
          "topic": "Health Education and Validation",
          "works": 6
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 5
        },
        {
          "topic": "Attention Deficit Hyperactivity Disorder",
          "works": 4
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Brazier",
          "works": 35
        },
        {
          "name": "Clara Mukuria",
          "works": 30
        },
        {
          "name": "Brendan Mulhern",
          "works": 23
        },
        {
          "name": "Nancy Devlin",
          "works": 22
        },
        {
          "name": "Jill Carlton",
          "works": 20
        },
        {
          "name": "Janice Connell",
          "works": 15
        },
        {
          "name": "Lidia Engel",
          "works": 13
        },
        {
          "name": "Cate Bailey",
          "works": 13
        },
        {
          "name": "Donna Rowen",
          "works": 12
        },
        {
          "name": "Richard Norman",
          "works": 11
        },
        {
          "name": "Suzy Paisley",
          "works": 10
        },
        {
          "name": "Alan Brennan",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128304736",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7128313152",
          "year": 2026,
          "title": "<b>Protocol for Assessing Content Validity in Generic Preference-weighted Measures: A Scoping Review</b>",
          "type": "other",
          "venue": "ORDA - The University of Sheffield Research Data Catalogue and Repository",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7159926856",
          "year": 2026,
          "title": "A direct comparison of the measurement properties of the PROMIS-16 and EQ-5D-5L in the U.S. general population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W7128209919",
          "year": 2026,
          "title": "Are Health Gains to Children and Adolescents More Important Than Health Gains to Adults? A Person Trade-Off Study",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Pediatric Pain Management Techniques",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W7124132998",
          "year": 2026,
          "title": "Content validity, face validity and comprehensiveness of generic quality-of-life measures in adults and children with rare genetic conditions and their carers: a think aloud qualitative study",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W7147252400",
          "year": 2026,
          "title": "Measuring health-related quality of life in infants and toddlers: conceptual challenges and proposed recommendations",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Infant Development and Preterm Care",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1536008289",
          "year": 1997,
          "title": "Gender and primary schooling in Tanzania.",
          "type": "report",
          "venue": "OpenGrey (Institut de l'Information Scientifique et Technique)",
          "cited_by_count": 14,
          "topics": [
            "Poverty, Education, and Child Welfare"
          ]
        },
        {
          "openalex_id": "W2063016114",
          "year": 1998,
          "title": "Educational attainments and household characteristics in Tanzania",
          "type": "article",
          "venue": "Economics of Education Review",
          "cited_by_count": 116,
          "topics": [
            "Poverty, Education, and Child Welfare",
            "Microfinance and Financial Inclusion",
            "Gender, Labor, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W2141618324",
          "year": 2005,
          "title": "Estimating the Intangible Victim Costs of Violent Crime",
          "type": "article",
          "venue": "The British Journal of Criminology",
          "cited_by_count": 131,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Health and Conflict Studies",
            "Traffic and Road Safety"
          ]
        },
        {
          "openalex_id": "W53175465",
          "year": 2005,
          "title": "Modelling subjective well-being",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Income, Poverty, and Inequality",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1978050391",
          "year": 2007,
          "title": "Do we really know what makes us happy? A review of the economic literature on the factors associated with subjective well-being",
          "type": "article",
          "venue": "Journal of Economic Psychology",
          "cited_by_count": 3120,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Financial Literacy, Pension, Retirement Analysis",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2065524809",
          "year": 2014,
          "title": "A systematic review, psychometric analysis and qualitative assessment of generic preference-based measures of health in mental health populations and the estimation of mapping functions from widely used specific measures",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 279,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W4220774050",
          "year": 2022,
          "title": "The EQ-HWB: Overview of the Development of a Measure of Health and Wellbeing and Key Results",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 175,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2333413009",
          "year": 2016,
          "title": "The impact of ADHD on the health and well-being of ADHD children and their siblings",
          "type": "article",
          "venue": "European Child & Adolescent Psychiatry",
          "cited_by_count": 154,
          "topics": [
            "Attention Deficit Hyperactivity Disorder",
            "Functional Brain Connectivity Studies"
          ]
        },
        {
          "openalex_id": "W2114064370",
          "year": 2006,
          "title": "Estimating the Economic and Social Costs of the Fear of Crime",
          "type": "article",
          "venue": "The British Journal of Criminology",
          "cited_by_count": 142,
          "topics": [
            "Health disparities and outcomes",
            "Crime Patterns and Interventions",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W2010030230",
          "year": 2010,
          "title": "Health-state utility values in breast cancer",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 140,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W2114529215",
          "year": 2009,
          "title": "An updated systematic review of Health State Utility Values for osteoporosis related conditions",
          "type": "review",
          "venue": "Osteoporosis International",
          "cited_by_count": 134,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Hip and Femur Fractures"
          ]
        }
      ]
    }
  }
]
