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
    "name": "Ning Yan Gu",
    "member_affiliation": "University of San Francisco",
    "is_member": true,
    "projects": [
      {
        "project_id": "246-RA",
        "title": "Assessing the impact of COVID-19 population health over time: a cross-country comparison between US, Sweden and Norway using the EQ-5D-5L repeated measures",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "358-RA",
        "title": "{(RRM + RUM) + DCE} *EQ-5D-5L = Preference",
        "working_group": "Valuation"
      },
      {
        "project_id": "409-RA",
        "title": "Developing a value set for the EQ-5D-Y-3L in the United States",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "84-RA",
        "title": "Assessing the impact of COVID-19 on population health using the longitudinal panel surveys in the US, Sweden and Norway",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5063972558",
      "display_name": "Ning Yan Gu",
      "orcid": "0000-0002-1250-7605",
      "reported_affiliation": "Exact Sciences (United States)",
      "works_count": 84,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 23
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 6
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 5
        },
        {
          "topic": "Cardiac pacing and defibrillation studies",
          "works": 4
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 4
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 4
        },
        {
          "topic": "Blind Source Separation Techniques",
          "works": 4
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 3
        },
        {
          "topic": "COVID-19 Impact on Reproduction",
          "works": 3
        },
        {
          "topic": "Advanced Adaptive Filtering Techniques",
          "works": 3
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Simon Pickard",
          "works": 6
        },
        {
          "name": "Marc Botteman",
          "works": 6
        },
        {
          "name": "Xiang Ji",
          "works": 6
        },
        {
          "name": "Joel W. Hay",
          "works": 5
        },
        {
          "name": "Cynthia L. Gong",
          "works": 5
        },
        {
          "name": "Melanie R. Palomares",
          "works": 5
        },
        {
          "name": "Annette K. Regan",
          "works": 4
        },
        {
          "name": "Aifeng Liu",
          "works": 4
        },
        {
          "name": "Ben van Hout",
          "works": 4
        },
        {
          "name": "Yunwei Gai",
          "works": 4
        },
        {
          "name": "Tun Lu",
          "works": 4
        },
        {
          "name": "Sumeyye Samur",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7129224831",
          "year": 2026,
          "title": "Abstract PS2-04-01: Early Adoption of Molecular Residual Disease Testing in Breast Cancer Patients using Real World Data",
          "type": "conference-abstract",
          "venue": "Clinical Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Cancer Genomics and Diagnostics",
            "Advanced Breast Cancer Therapies",
            "PARP inhibition in cancer therapy"
          ]
        },
        {
          "openalex_id": "W7129377539",
          "year": 2026,
          "title": "Abstract PS2-06-21: Real-word utilization of the 21-gene assay for guiding treatment decisions in patients with HR+/HER2- early breast cancer in the US",
          "type": "conference-abstract",
          "venue": "Clinical Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Advanced Breast Cancer Therapies",
            "Breast Cancer Treatment Studies",
            "PARP inhibition in cancer therapy"
          ]
        },
        {
          "openalex_id": "W7135196686",
          "year": 2026,
          "title": "Microsimulation model to identify suboptimal recurrence detection in patients with colorectal cancer following the current standard of care",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Cancer Genomics and Diagnostics",
            "demographic modeling and climate adaptation",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W7166028689",
          "year": 2026,
          "title": "PCR203 COMPARING HEALTH, HEALTH AND WELLBEING (HWB), AND QUALITY OF LIFE (QOL) VISUAL ANALOGUE SCALE (VAS) CONSTRUCTS WITH THE EQ-HWB-9 IN THE UNITED STATES (US), UNITED KINGDOM (UK), AND GERMANY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Molecular Biology Techniques and Applications",
            "Forensic and Genetic Research",
            "Gene expression and cancer classification"
          ]
        },
        {
          "openalex_id": "W4409690265",
          "year": 2025,
          "title": "Abstract 1933: Improving detection of colorectal cancer recurrence using serial ctDNA measurements: A systematic literature review",
          "type": "review",
          "venue": "Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Molecular Biology Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W4417298502",
          "year": 2025,
          "title": "AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 0,
          "topics": [
            "Computational and Text Analysis Methods",
            "Topic Modeling",
            "Machine Learning in Materials Science"
          ]
        },
        {
          "openalex_id": "W2018763082",
          "year": 1997,
          "title": "Effects of apolipoprotein E on dementia and aging in the Shanghai Survey of Dementia",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 79,
          "topics": [
            "Alzheimer's disease research and treatments",
            "Cerebrovascular and genetic disorders",
            "Lipoproteins and Cardiovascular Health"
          ]
        },
        {
          "openalex_id": "W1599875470",
          "year": 2004,
          "title": "Medical Care Variations in Florida",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes",
            "Pharmaceutical industry and healthcare"
          ]
        },
        {
          "openalex_id": "W2108017967",
          "year": 2006,
          "title": "Blind Equalization of Nonirreducible Systems Using the CM Criterion",
          "type": "article",
          "venue": "IEEE Transactions on Circuits and Systems II Analog and Digital Signal Processing",
          "cited_by_count": 21,
          "topics": [
            "Blind Source Separation Techniques",
            "Advanced Adaptive Filtering Techniques",
            "Control Systems and Identification"
          ]
        },
        {
          "openalex_id": "W2787887787",
          "year": 2007,
          "title": "Using computer algebra to certify the global convergence of a numerical optimization process",
          "type": "conference-paper",
          "venue": "HAL (Le Centre pour la Communication Scientifique Directe)",
          "cited_by_count": 0,
          "topics": [
            "Blind Source Separation Techniques",
            "Spectroscopy and Chemometric Analyses",
            "Control Systems and Identification"
          ]
        },
        {
          "openalex_id": "W2751848401",
          "year": 2017,
          "title": "Complications and Health Care Costs Associated With Transvenous Cardiac Pacemakers in a Nationwide Assessment",
          "type": "article",
          "venue": "JACC. Clinical electrophysiology",
          "cited_by_count": 146,
          "topics": [
            "Cardiac pacing and defibrillation studies",
            "Mechanical Circulatory Support Devices",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W2228384076",
          "year": 2011,
          "title": "Comparison of One and Two-Stage Revision of Total Hip Arthroplasty Complicated by Infection",
          "type": "article",
          "venue": "Journal of Bone and Joint Surgery",
          "cited_by_count": 137,
          "topics": [
            "Orthopedic Infections and Treatments",
            "Orthopaedic implants and arthroplasty",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W3112593009",
          "year": 2021,
          "title": "A US Population Health Survey on the Impact of COVID-19 Using the EQ-5D-5L",
          "type": "article",
          "venue": "Journal of General Internal Medicine",
          "cited_by_count": 77,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4294904777",
          "year": 2022,
          "title": "COVID-19 vaccine acceptance and coverage among pregnant persons in the United States",
          "type": "article",
          "venue": "Preventive Medicine Reports",
          "cited_by_count": 32,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Vaccine Coverage and Hesitancy",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W4284898468",
          "year": 2022,
          "title": "Predicting panel attrition in longitudinal HRQoL surveys during the COVID-19 pandemic in the US",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 32,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Social Media in Health Education",
            "Data-Driven Disease Surveillance"
          ]
        },
        {
          "openalex_id": "W2113583603",
          "year": 2008,
          "title": "The effect of patient satisfaction with pharmacist consultation on medication adherence: an instrumental variable approach",
          "type": "article",
          "venue": "Pharmacy Practice",
          "cited_by_count": 27,
          "topics": [
            "Medication Adherence and Compliance",
            "Pharmaceutical Practices and Patient Outcomes",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4310136766",
          "year": 2022,
          "title": "Findings from a Roundtable Discussion with US Stakeholders on Valuation of the EQ-5D-Y-3L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 26,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Child Welfare and Adoption",
            "Children's Rights and Participation"
          ]
        }
      ]
    }
  },
  {
    "name": "Nyantara Wickramasekera",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2102-RA",
        "title": "Visualising EQ-5D-5L Outcomes for Routine Clinical Use: A Mixed-Methods Study in Sciatica Care",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5077076014",
      "display_name": "Nyantara Wickramasekera",
      "orcid": "0000-0002-6552-5153",
      "reported_affiliation": "University of Sheffield",
      "works_count": 58,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 14
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 6
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 6
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 6
        },
        {
          "topic": "Urban Green Space and Health",
          "works": 5
        },
        {
          "topic": "Peripheral Artery Disease Management",
          "works": 4
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Human-Animal Interaction Studies",
          "works": 3
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 3
        },
        {
          "topic": "Anorectal Disease Treatments and Outcomes",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Phil Shackley",
          "works": 23
        },
        {
          "name": "Anju Keetharuth",
          "works": 14
        },
        {
          "name": "Helen Elsey",
          "works": 12
        },
        {
          "name": "Elizabeth Lumley",
          "works": 12
        },
        {
          "name": "Emma Wilson",
          "works": 12
        },
        {
          "name": "Aoife Howard",
          "works": 12
        },
        {
          "name": "Ahmed Aber",
          "works": 12
        },
        {
          "name": "Jonathan Michaels",
          "works": 12
        },
        {
          "name": "Stephen Radley",
          "works": 11
        },
        {
          "name": "Gill Rooney",
          "works": 11
        },
        {
          "name": "Simon Palfreyman",
          "works": 11
        },
        {
          "name": "Sandy Tubeuf",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7134961444",
          "year": 2026,
          "title": "Beyond the Average: Modeling Individual-Specific Preferences for Ulcerative Colitis Surgery",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Bowel Disease",
            "Gastrointestinal motility and disorders",
            "Diverticular Disease and Complications"
          ]
        },
        {
          "openalex_id": "W7132837468",
          "year": 2026,
          "title": "Evaluating the Validity of the EQ Health and Wellbeing (EQ-HWB-9) in a Large United Kingdom General Population Sample",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cardiac Imaging and Diagnostics",
            "Liver Disease Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7131384634",
          "year": 2026,
          "title": "Why Object to Inequalities in Health and Well-Being? A Mixed-Methods Exploration of Inequality Aversion With Members of the General Public",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Income, Poverty, and Inequality"
          ]
        },
        {
          "openalex_id": "W4414983851",
          "year": 2025,
          "title": "A Large Scale Population Survey of Health and Wellbeing to Allow Comparisons Between Outcome Measures: the SIPHER-HWMIC Dataset",
          "type": "article",
          "venue": "Social Indicators Research",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4406688629",
          "year": 2025,
          "title": "Embedding a Choice Experiment in an Online Decision Aid or Tool: Scoping Review",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W7117485122",
          "year": 2025,
          "title": "OP23 Developing A Personalized Decision Aid Incorporating A Discrete Choice Experiment: A Case Study In Ulcerative Colitis",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Game Theory and Voting Systems"
          ]
        },
        {
          "openalex_id": "W3122765484",
          "year": 2014,
          "title": "Cost of crime: a systematic review",
          "type": "review",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Crime Patterns and Interventions",
            "Traffic and Road Safety"
          ]
        },
        {
          "openalex_id": "W2188096884",
          "year": 2014,
          "title": "For peer review only Understanding the Impacts of Care Farms on Health and Well-being of Disadvantaged Populations: The Evaluating Community Orders (ECO) Study",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Migration, Aging, and Tourism Studies",
            "Homelessness and Social Issues"
          ]
        },
        {
          "openalex_id": "W2959345224",
          "year": 2014,
          "title": "PROTOCOL: The impact of care farms on quality of life among different population groups: protocol for a systematic review",
          "type": "review",
          "venue": "Campbell Systematic Reviews",
          "cited_by_count": 2,
          "topics": [
            "Health, psychology, and well-being",
            "Human-Animal Interaction Studies",
            "Urban Green Space and Health"
          ]
        },
        {
          "openalex_id": "W66937154",
          "year": 2014,
          "title": "The Impact of Care Farms on Quality of Life among Different Population Groups: A Systematic Review",
          "type": "review",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Migration, Aging, and Tourism Studies",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W1535457917",
          "year": 2015,
          "title": "Cost of crime: A systematic review",
          "type": "review",
          "venue": "Journal of Criminal Justice",
          "cited_by_count": 159,
          "topics": [
            "Criminal Justice and Corrections Analysis",
            "Crime Patterns and Interventions",
            "Elder Abuse and Neglect"
          ]
        },
        {
          "openalex_id": "W2989965789",
          "year": 2019,
          "title": "The impact of care farms on quality of life, depression and anxiety among different population groups: A systematic review",
          "type": "review",
          "venue": "Campbell Systematic Reviews",
          "cited_by_count": 52,
          "topics": [
            "Human-Animal Interaction Studies",
            "Urban Green Space and Health",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W3161319679",
          "year": 2021,
          "title": "Person-centred experiential therapy versus cognitive behavioural therapy delivered in the English Improving Access to Psychological Therapies service for the treatment of moderate or severe depression (PRaCTICED): a pragmatic, randomised, non-inferiority trial",
          "type": "article",
          "venue": "The Lancet Psychiatry",
          "cited_by_count": 48,
          "topics": [
            "Digital Mental Health Interventions",
            "Personality Disorders and Psychopathology",
            "Psychotherapy Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W3091472244",
          "year": 2020,
          "title": "Can electronic assessment tools improve the process of shared decision-making? A systematic review",
          "type": "review",
          "venue": "Health Information Management",
          "cited_by_count": 27,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare",
            "Healthcare Systems and Technology"
          ]
        },
        {
          "openalex_id": "W3133563932",
          "year": 2021,
          "title": "Patient decision‐making and regret in pilonidal sinus surgery: a mixed‐methods study",
          "type": "article",
          "venue": "Colorectal Disease",
          "cited_by_count": 26,
          "topics": [
            "Anorectal Disease Treatments and Outcomes",
            "Hidradenitis Suppurativa and Treatments",
            "Congenital gastrointestinal and neural anomalies"
          ]
        },
        {
          "openalex_id": "W4315928422",
          "year": 2023,
          "title": "Patient preferences for pilonidal sinus treatments: A discrete choice experiment survey",
          "type": "article",
          "venue": "Colorectal Disease",
          "cited_by_count": 19,
          "topics": [
            "Anorectal Disease Treatments and Outcomes",
            "Hidradenitis Suppurativa and Treatments",
            "Infectious Diseases and Tuberculosis"
          ]
        },
        {
          "openalex_id": "W2056565808",
          "year": 2014,
          "title": "Understanding the impacts of care farms on health and well-being of disadvantaged populations: a protocol of the Evaluating Community Orders (ECO) pilot study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 18,
          "topics": [
            "Urban Green Space and Health",
            "Geriatric Care and Nursing Homes",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2793746868",
          "year": 2018,
          "title": "Assessing the impact of care farms on quality of life and offending: a pilot study among probation service users in England",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 16,
          "topics": [
            "Urban Green Space and Health",
            "Geriatric Care and Nursing Homes",
            "Urban Agriculture and Sustainability"
          ]
        }
      ]
    }
  },
  {
    "name": "Ole Marten",
    "member_affiliation": "Bielefeld University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1951-RA",
        "title": "Translating the EQ-HWB and EQ-HWB-S for Germany",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2024-RA",
        "title": "EQ-HWB translation and cognitive debriefing methodology: Disseminating methodology, experiences and findings from Germany, Hungary, the Netherlands and Slovenia",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2623-RA",
        "title": "Evaluating the Psychometric Performance and Design Characteristics of a Health and Wellbeing VAS for the EQ-HWB-9 in Informal Caregivers",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033160244",
      "display_name": "Ole Marten",
      "orcid": "0000-0002-2576-9110",
      "reported_affiliation": "Bielefeld University",
      "works_count": 19,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 12
        },
        {
          "topic": "Health Education and Validation",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 2
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 2
        },
        {
          "topic": "Health and Medical Studies",
          "works": 2
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 2
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Wolfgang Greiner",
          "works": 11
        },
        {
          "name": "Tessa Peasgood",
          "works": 9
        },
        {
          "name": "Clara Mukuria",
          "works": 8
        },
        {
          "name": "Kristina Ludwig",
          "works": 7
        },
        {
          "name": "Brendan Mulhern",
          "works": 6
        },
        {
          "name": "María Belizán",
          "works": 6
        },
        {
          "name": "A Monteiro",
          "works": 6
        },
        {
          "name": "John Brazier",
          "works": 5
        },
        {
          "name": "Simone Kreimeier",
          "works": 5
        },
        {
          "name": "Nan Luo",
          "works": 5
        },
        {
          "name": "Federico Augustovski",
          "works": 5
        },
        {
          "name": "Lidia Engel",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4410463015",
          "year": 2025,
          "title": "How well do participants understand the questions asked in the Online Personal Utility Functions (OPUF) approach? A cognitive debrief of the EQ-HWB-S (EQ Health and Wellbeing Short version) valuation",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4417481846",
          "year": 2025,
          "title": "PCR162 Multinational Qualitative Testing of the Experimental EuroQol Toddler and Infant Populations (EQ-TIPS) Instrument",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W4408218600",
          "year": 2025,
          "title": "Test-retest reliability of the Online Elicitation of Personal Utility Functions (OPUF) approach for valuing the EQ-HWB-S",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4400538585",
          "year": 2024,
          "title": "Using the OPUF approach to create a value set for the EQ-HWB-S: An exploratory feasibility study",
          "type": "article",
          "venue": "Wellcome Open Research",
          "cited_by_count": 5,
          "topics": [
            "Advanced Statistical Process Monitoring"
          ]
        },
        {
          "openalex_id": "W4386158155",
          "year": 2023,
          "title": "Exploring differences and similarities of EQ-5D-3L, EQ-5D-5L and WHOQOL-OLD in recipients of aged care services in Germany",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W4205569690",
          "year": 2022,
          "title": "Developing a New Generic Health and Wellbeing Measure: Psychometric Survey Results for the EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 81,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health Education and Validation",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2589428653",
          "year": 2017,
          "title": "Einflussfaktoren auf die Standortwahl von hausärztlichen Land- und Stadtärzten in Niedersachsen",
          "type": "article",
          "venue": "Gesundheitsökonomie & Qualitätsmanagement",
          "cited_by_count": 4,
          "topics": [
            "Health and Medical Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2607533417",
          "year": 2017,
          "title": "Einflussfaktoren auf die Standortwahl von hausärztlichen Land- und Stadtärzten in Niedersachsen",
          "type": "article",
          "venue": "Institutional Repository of Leibniz Universität Hannover (Leibniz Universität Hannover)",
          "cited_by_count": 0,
          "topics": [
            "Health and Medical Studies",
            "Global Health Workforce Issues",
            "Musculoskeletal Disorders and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W7128874110",
          "year": 2018,
          "title": "Obeldicks light Follow-up: Long-term effects of an intervention for overweight children and adolescents and health economic assessment (OLF)",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2946984536",
          "year": 2019,
          "title": "A DELPHI study on aspects of study design to overcome knowledge gaps on the burden of disease caused by serogroup B invasive meningococcal disease",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 11,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Peripheral Neuropathies and Disorders",
            "Cystic Fibrosis Research Advances"
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
          "openalex_id": "W3134681403",
          "year": 2021,
          "title": "EQ-5D-5L reference values for the German general elderly population",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 79,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W3202578641",
          "year": 2021,
          "title": "Feasibility of the EQ-5D in the elderly population: a systematic review of the literature",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 65,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4214702737",
          "year": 2022,
          "title": "Generation, Selection, and Face Validation of Items for a New Generic Measure of Quality of Life: The EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4281739222",
          "year": 2022,
          "title": "Feasibility and validity of the EQ-5D-3L in the elderly Europeans: a secondary data analysis using SHARE(d) data",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes"
          ]
        }
      ]
    }
  },
  {
    "name": "Oliver Rivero-Arias",
    "member_affiliation": "University of Oxford",
    "is_member": true,
    "projects": [
      {
        "project_id": "20180240",
        "title": "Developing and testing a new Stata command to calculate country-specific index values from EQ-5D-5L responses",
        "working_group": "Valuation"
      },
      {
        "project_id": "2021-RA",
        "title": "Measuring family spillover effects with EuroQol instruments over time associated with the care of babies with necrotising enterocolitis",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "206-RA",
        "title": "Estimating an EQ-5D-Y-3L value set in the United Kingdom",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5121462085",
      "display_name": "Oliver Rivero-Arias",
      "orcid": "",
      "reported_affiliation": "University of Oxford",
      "works_count": 19,
      "top_topics": [
        {
          "topic": "Infant Nutrition and Health",
          "works": 11
        },
        {
          "topic": "Neonatal Respiratory Health Research",
          "works": 11
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 6
        },
        {
          "topic": "Neonatal and Maternal Infections",
          "works": 6
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 2
        },
        {
          "topic": "Clinical Nutrition and Gastroenterology",
          "works": 1
        },
        {
          "topic": "Neonatal and fetal brain pathology",
          "works": 1
        },
        {
          "topic": "Advanced Causal Inference Techniques",
          "works": 1
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 1
        },
        {
          "topic": "Cardiovascular Issues in Pregnancy",
          "works": 1
        },
        {
          "topic": "Acute Myocardial Infarction Research",
          "works": 1
        },
        {
          "topic": "Pregnancy and Medication Impact",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Christina Cole",
          "works": 14
        },
        {
          "name": "Helen Campbell",
          "works": 14
        },
        {
          "name": "Madeleine Hurd",
          "works": 14
        },
        {
          "name": "Pollyanna Hardy",
          "works": 14
        },
        {
          "name": "Andrew King",
          "works": 14
        },
        {
          "name": "Louise Linsell",
          "works": 14
        },
        {
          "name": "Charles C. Roehr",
          "works": 14
        },
        {
          "name": "Kayleigh Stanbury",
          "works": 14
        },
        {
          "name": "Richard Welsh",
          "works": 14
        },
        {
          "name": "Joy Wiles",
          "works": 14
        },
        {
          "name": "Amy D. Rodriquez",
          "works": 13
        },
        {
          "name": "Iza Andrzejewksa",
          "works": 13
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7127993347",
          "year": 2026,
          "title": "Additional file 1 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Neonatal and Maternal Infections"
          ]
        },
        {
          "openalex_id": "W7128078176",
          "year": 2026,
          "title": "Additional file 1 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Neonatal and Maternal Infections"
          ]
        },
        {
          "openalex_id": "W7128020803",
          "year": 2026,
          "title": "Additional file 2 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W7128090279",
          "year": 2026,
          "title": "Additional file 2 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W7127958553",
          "year": 2026,
          "title": "Additional file 3 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Neonatal and Maternal Infections"
          ]
        },
        {
          "openalex_id": "W7128055666",
          "year": 2026,
          "title": "Additional file 3 of Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Infant Nutrition and Health",
            "Neonatal and Maternal Infections"
          ]
        },
        {
          "openalex_id": "W7134839030",
          "year": 2025,
          "title": "Optimising the monitoring and management of raised blood pressure including proteinuria testing during pregnancy: the BUMP research programme including 2 RCTs",
          "type": "article",
          "venue": "Programme Grants for Applied Research",
          "cited_by_count": 0,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Blood Pressure and Hypertension Studies",
            "Sodium Intake and Health"
          ]
        },
        {
          "openalex_id": "W7117471546",
          "year": 2025,
          "title": "Trial protocol: DOLFIN trial: Developmental Outcomes of Long-term Feed Supplementation in Neonates—A UK multicentre, blinded, stratified, randomised controlled trial",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 1,
          "topics": [
            "Neonatal and fetal brain pathology",
            "Neonatal Respiratory Health Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W7118349013",
          "year": 2026,
          "title": "Avoiding routine gastric residual volume measurement in neonatal critical care (the neoGASTRIC trial): study protocol for a multi-centre, unblinded, randomised, controlled trial",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 4,
          "topics": [
            "Infant Nutrition and Health",
            "Infant Development and Preterm Care",
            "Clinical Nutrition and Gastroenterology"
          ]
        },
        {
          "openalex_id": "W7127319717",
          "year": 2026,
          "title": "Development and Pretesting of the Children and Young People’s Time-Use Questionnaire for Use in Economic Evaluation",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W7135044007",
          "year": 2026,
          "title": "Incidence, prevalence, and mortality of maternal cardiac disease: a systematic review and meta-analysis",
          "type": "review",
          "venue": "The Lancet Obstetrics Gynaecology & Women s Health",
          "cited_by_count": 1,
          "topics": [
            "Cardiovascular Issues in Pregnancy",
            "Acute Myocardial Infarction Research",
            "Pregnancy and Medication Impact"
          ]
        }
      ]
    }
  },
  {
    "name": "Oriana Ciani",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "316-EO",
        "title": "The EQ-5D-5L value set for Italy – Dissemination and Outreach",
        "working_group": "Valuation, Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5008052793",
      "display_name": "Oriana Ciani",
      "orcid": "0000-0002-3607-0508",
      "reported_affiliation": "University of Exeter",
      "works_count": 259,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 111
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 48
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 31
        },
        {
          "topic": "Advanced Causal Inference Techniques",
          "works": 22
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 19
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 15
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 14
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 12
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 12
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 11
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 11
        },
        {
          "topic": "Biomedical Ethics and Regulation",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rosanna Tarricone",
          "works": 59
        },
        {
          "name": "Rod S Taylor",
          "works": 54
        },
        {
          "name": "Anthony Muchai Manyara",
          "works": 31
        },
        {
          "name": "Sylwia Bujkiewicz",
          "works": 22
        },
        {
          "name": "Michela Meregaglia",
          "works": 21
        },
        {
          "name": "Joseph S. Ross",
          "works": 20
        },
        {
          "name": "Vittoria Ardito",
          "works": 18
        },
        {
          "name": "Michael Drummond",
          "works": 17
        },
        {
          "name": "Professor Gary S. Collins",
          "works": 16
        },
        {
          "name": "Philippa Davies",
          "works": 16
        },
        {
          "name": "Derek Stewart",
          "works": 16
        },
        {
          "name": "Christopher J. Weir",
          "works": 16
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7118869004",
          "year": 2026,
          "title": "ESG Performance, Debt Financing, and R&amp;D Output: Evidence From the Healthcare Sector",
          "type": "article",
          "venue": "Business Strategy and the Environment",
          "cited_by_count": 1,
          "topics": [
            "Environmental Sustainability in Business",
            "Corporate Social Responsibility Reporting",
            "Business and Economic Development"
          ]
        },
        {
          "openalex_id": "W7165976850",
          "year": 2026,
          "title": "Methods for Evaluation of Surrogate Endpoints for Health Technology Assessment Decision Making: A Good Practices Report of an ISPOR Task Force.",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W7155627754",
          "year": 2026,
          "title": "WP1 - Deliverable 1.2: Policy recommendations about successful and flexible implementation of the different schemes to promote access to high-quality affordable innovative health technologies",
          "type": "article",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Biomedical and Engineering Education"
          ]
        },
        {
          "openalex_id": "W7155652285",
          "year": 2026,
          "title": "WP1 - Deliverable 1.2: Policy recommendations about successful and flexible implementation of the different schemes to promote access to high-quality affordable innovative health technologies",
          "type": "article",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Biomedical and Engineering Education"
          ]
        },
        {
          "openalex_id": "W7155636345",
          "year": 2026,
          "title": "WP1 - Milestone 2: Within-country performance of novel payment/pricing schemes: costs and benefits of implementation",
          "type": "article",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": [
            "Digital Platforms and Economics",
            "ICT Impact and Policies"
          ]
        },
        {
          "openalex_id": "W7155643144",
          "year": 2026,
          "title": "WP1 - Milestone 2: Within-country performance of novel payment/pricing schemes: costs and benefits of implementation",
          "type": "article",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": [
            "Digital Platforms and Economics",
            "ICT Impact and Policies"
          ]
        },
        {
          "openalex_id": "W2144016135",
          "year": 2008,
          "title": "Pervasive technology in Neonatal Intensive Care Unit: A prototype for newborns unobtrusive monitoring",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 8,
          "topics": [
            "Bluetooth and Wireless Communication Technologies",
            "Context-Aware Activity Recognition Systems",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W1541077651",
          "year": 2009,
          "title": "Method for Movement and Gesture Assessment (MMGA) in Ergonomics",
          "type": "conference-paper",
          "venue": "Lecture notes in computer science",
          "cited_by_count": 28,
          "topics": [
            "Ergonomics and Musculoskeletal Disorders",
            "Musculoskeletal pain and rehabilitation",
            "Ergonomics and Human Factors"
          ]
        },
        {
          "openalex_id": "W1516544881",
          "year": 2010,
          "title": "New Emerging Biomedical Technologies for Home-care and Telemedicine Applications: the Sensorwear Project",
          "type": "book-chapter",
          "venue": "InTech eBooks",
          "cited_by_count": 3,
          "topics": [
            "Advanced Sensor and Energy Harvesting Materials",
            "Wireless Body Area Networks"
          ]
        },
        {
          "openalex_id": "W2151496454",
          "year": 2010,
          "title": "Quantitative body movement and gesture assessment in ergonomics",
          "type": "article",
          "venue": "International Journal of Human Factors Modelling and Simulation",
          "cited_by_count": 4,
          "topics": [
            "Ergonomics and Musculoskeletal Disorders",
            "Musculoskeletal pain and rehabilitation",
            "Ergonomics and Human Factors"
          ]
        },
        {
          "openalex_id": "W2924144362",
          "year": 2019,
          "title": "Impact of Exercise Rehabilitation on Exercise Capacity and Quality-of-Life in Heart Failure",
          "type": "article",
          "venue": "Journal of the American College of Cardiology",
          "cited_by_count": 277,
          "topics": [
            "Cardiovascular and exercise physiology",
            "Cardiac Health and Mental Health",
            "Cardiovascular Function and Risk Factors"
          ]
        },
        {
          "openalex_id": "W2900196560",
          "year": 2018,
          "title": "Impact of Exercise-Based Cardiac Rehabilitation in Patients with Heart Failure (ExTraMATCH II) on Mortality and Hospitalisation: An Individual Patient Data Meta-Analysis of Randomised Trials",
          "type": "review",
          "venue": "European Journal of Heart Failure",
          "cited_by_count": 192,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular and exercise physiology",
            "Cardiovascular Function and Risk Factors"
          ]
        },
        {
          "openalex_id": "W2021046234",
          "year": 2013,
          "title": "Comparison of treatment effect sizes associated with surrogate and final patient relevant outcomes in randomised controlled trials: meta-epidemiological study",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 163,
          "topics": [
            "Meta-analysis and systematic reviews",
            "Advanced Causal Inference Techniques",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2562521254",
          "year": 2016,
          "title": "Time to Review the Role of Surrogate End Points in Health Policy: State of the Art and the Way Forward",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 151,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W2053456265",
          "year": 2012,
          "title": "Determinants of demand for total hip and knee arthroplasty: a systematic literature review",
          "type": "review",
          "venue": "BMC Health Services Research",
          "cited_by_count": 145,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4401027269",
          "year": 2024,
          "title": "Sample size in multistakeholder Delphi surveys: at what minimum sample size do replicability of results stabilize?",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 136,
          "topics": [
            "Delphi Technique in Research",
            "Survey Methodology and Nonresponse",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W3097860716",
          "year": 2020,
          "title": "Harnessing Digital Health Technologies During and After the COVID-19 Pandemic: Context Matters",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 92,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "COVID-19 Digital Contact Tracing",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W3211171162",
          "year": 2021,
          "title": "An EQ-5D-5L value set for Italy using videoconferencing interviews and feasibility of a new mode of administration",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  }
]
