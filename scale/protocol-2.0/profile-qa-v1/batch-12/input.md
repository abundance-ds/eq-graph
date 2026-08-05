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
    "name": "Darshini Govindasamy",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "144-RA",
        "title": "The feasibility, reliability and validity of the EQ-5D-Y-5L versus the EQ-5D-Y-3L and CHU9D in routine healthcare settings among adolescents living with HIV in KwaZulu-Natal, South Africa: a mixed-method study",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5050754442",
      "display_name": "Darshini Govindasamy",
      "orcid": "0000-0001-5984-3588",
      "reported_affiliation": "South African Medical Research Council",
      "works_count": 65,
      "top_topics": [
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 38
        },
        {
          "topic": "Adolescent Sexual and Reproductive Health",
          "works": 28
        },
        {
          "topic": "HIV, Drug Use, Sexual Risk",
          "works": 12
        },
        {
          "topic": "Poverty, Education, and Child Welfare",
          "works": 9
        },
        {
          "topic": "HIV Research and Treatment",
          "works": 8
        },
        {
          "topic": "HIV/AIDS Impact and Responses",
          "works": 7
        },
        {
          "topic": "HIV/AIDS drug development and treatment",
          "works": 6
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 6
        },
        {
          "topic": "Family Support in Illness",
          "works": 5
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 4
        },
        {
          "topic": "Food Security and Health in Diverse Populations",
          "works": 4
        },
        {
          "topic": "Tuberculosis Research and Epidemiology",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Catherine Mathews",
          "works": 19
        },
        {
          "name": "Stanley Carries",
          "works": 19
        },
        {
          "name": "Kim Jonas",
          "works": 15
        },
        {
          "name": "Eugene Lee Davids",
          "works": 12
        },
        {
          "name": "Katharina Kranzer",
          "works": 11
        },
        {
          "name": "Zibuyisile Mkhwanazi",
          "works": 10
        },
        {
          "name": "Audrey Moyo",
          "works": 10
        },
        {
          "name": "Reuben Christopher Moyo",
          "works": 8
        },
        {
          "name": "Carl Lombard",
          "works": 8
        },
        {
          "name": "Mireille Cheyip",
          "works": 8
        },
        {
          "name": "Linda‐Gail Bekker",
          "works": 7
        },
        {
          "name": "Zoe Duby",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7159600267",
          "year": 2026,
          "title": "<p>Comparison of ever experienced HIV-related intersectional stigma scores by selected variables N = 100.</p>",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7159661910",
          "year": 2026,
          "title": "<p>Description of caregivers of ALHIV in the sample (N = 100).</p>",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7159673791",
          "year": 2026,
          "title": "<p>Description of variables.</p>",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "HIV/AIDS oral health manifestations"
          ]
        },
        {
          "openalex_id": "W7159675347",
          "year": 2026,
          "title": "<p>Univariable and multivariable linear regression model coefficients for correlates of HIV-related intersectional stigma among caregivers of ALHIV (N = 100).</p>",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7159574390",
          "year": 2026,
          "title": "<p>Univariable and multivariable robust Poisson regression model for HIV-related intersectional stigma among caregivers of ALHIV (N = 100).</p>",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7127616930",
          "year": 2026,
          "title": "A synthesis of dimensions of wellbeing among adolescents and young people living with HIV from Sub-Saharan Africa for measurement in economic evaluation: a qualitative overview of reviews",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Poverty, Education, and Child Welfare",
            "HIV/AIDS Research and Interventions",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2140154490",
          "year": 2010,
          "title": "Early treatment outcomes and HIV status of patients with extensively drug-resistant tuberculosis in South Africa: a retrospective cohort study",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 250,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Infectious Diseases and Tuberculosis",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W2155896563",
          "year": 2011,
          "title": "Incentivized recruitment of a population sample to a mobile HIV testing service increases the yield of newly diagnosed cases, including those in need of antiretroviral therapy",
          "type": "article",
          "venue": "HIV Medicine",
          "cited_by_count": 37,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV Research and Treatment",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W2043388296",
          "year": 2011,
          "title": "Linkage to HIV Care From a Mobile Testing Unit in South Africa by Different CD4 Count Strata",
          "type": "article",
          "venue": "JAIDS Journal of Acquired Immune Deficiency Syndromes",
          "cited_by_count": 99,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV Research and Treatment",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2145151789",
          "year": 2012,
          "title": "Feasibility, Yield, and Cost of Active Tuberculosis Case Finding Linked to a Mobile HIV Service in Cape Town, South Africa: A Cross-sectional Study",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 76,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "Diagnosis and treatment of tuberculosis"
          ]
        },
        {
          "openalex_id": "W2184272173",
          "year": 2015,
          "title": "Management of latent<i>Mycobacterium tuberculosis</i>infection: WHO guidelines for low tuberculosis burden countries",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 592,
          "topics": [
            "Tuberculosis Research and Epidemiology",
            "Mycobacterium research and diagnosis",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        },
        {
          "openalex_id": "W2048986863",
          "year": 2012,
          "title": "Risk factors, barriers and facilitators for linkage to antiretroviral therapy care",
          "type": "article",
          "venue": "AIDS",
          "cited_by_count": 443,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS drug development and treatment",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2159899509",
          "year": 2012,
          "title": "Quantifying and addressing losses along the continuum of care for people living with HIV infection in sub‐Saharan Africa: a systematic review",
          "type": "review",
          "venue": "Journal of the International AIDS Society",
          "cited_by_count": 309,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS drug development and treatment",
            "HIV Research and Treatment"
          ]
        },
        {
          "openalex_id": "W2114990707",
          "year": 2014,
          "title": "Interventions to improve or facilitate linkage to or retention in pre‐ART (HIV) care and initiation of ART in low‐ and middle‐income settings – a systematic review",
          "type": "review",
          "venue": "Journal of the International AIDS Society",
          "cited_by_count": 286,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS drug development and treatment",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W1913337589",
          "year": 2015,
          "title": "Uptake and yield of HIV testing and counselling among children and adolescents in sub‐Saharan Africa: a systematic review",
          "type": "review",
          "venue": "Journal of the International AIDS Society",
          "cited_by_count": 118,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Adolescent Sexual and Reproductive Health",
            "HIV, Drug Use, Sexual Risk"
          ]
        },
        {
          "openalex_id": "W2140761594",
          "year": 2013,
          "title": "Linkage to HIV, TB and Non-Communicable Disease Care from a Mobile Testing Unit in Cape Town, South Africa",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 97,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV, Drug Use, Sexual Risk",
            "Adolescent Sexual and Reproductive Health"
          ]
        }
      ]
    }
  },
  {
    "name": "David Mott",
    "member_affiliation": "Office of Health Economics",
    "is_member": true,
    "projects": [
      {
        "project_id": "104-RA",
        "title": "Using TTO data to anchor DCE data and produce EQ-5D-Y value sets: comparing alternative approaches using existing and simulated data",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "432-RA",
        "title": "Using the online personal utility functions (OPUF) tool to explore issues in the valuation of EQ-5D-Y",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5009132187",
      "display_name": "David Mott",
      "orcid": "0000-0001-5959-8447",
      "reported_affiliation": "University of Wisconsin–Madison",
      "works_count": 63,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 30
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 18
        },
        {
          "topic": "Advanced X-ray and CT Imaging",
          "works": 7
        },
        {
          "topic": "Medical Imaging Techniques and Applications",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 5
        },
        {
          "topic": "Radiation Dose and Imaging",
          "works": 5
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 4
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 3
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 3
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 3
        },
        {
          "topic": "Medical Image Segmentation Techniques",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Chris Skedgel",
          "works": 15
        },
        {
          "name": "Koonal Shah",
          "works": 12
        },
        {
          "name": "Nancy Devlin",
          "works": 7
        },
        {
          "name": "Priscila Radu",
          "works": 6
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 5
        },
        {
          "name": "Patricia Cubí‐Mollá",
          "works": 5
        },
        {
          "name": "Samantha Nier",
          "works": 5
        },
        {
          "name": "Oliver Rivero‐Arias",
          "works": 4
        },
        {
          "name": "Nicolas Scheuer",
          "works": 4
        },
        {
          "name": "Grace Hampson",
          "works": 4
        },
        {
          "name": "Jake Hitch",
          "works": 4
        },
        {
          "name": "Nadine Henderson",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7122532710",
          "year": 2026,
          "title": "P-871. Can We Change What We Do Not Measure? Antibiotic Prescribing Patterns in Wisconsin’s Urgent Care Centers in 2022",
          "type": "article",
          "venue": "Open Forum Infectious Diseases",
          "cited_by_count": 0,
          "topics": [
            "Antibiotic Use and Resistance",
            "Antimicrobial Resistance in Staphylococcus",
            "Nosocomial Infections in ICU"
          ]
        },
        {
          "openalex_id": "W7164348563",
          "year": 2026,
          "title": "Patient Preferences for Treatment in Relapsed/Refractory Acute Leukemia: A Multinational Discrete Choice Experiment",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4417002264",
          "year": 2025,
          "title": "A multinational study to explore patient preferences for chronic myeloid leukaemia treatments",
          "type": "conference-abstract",
          "venue": "Blood",
          "cited_by_count": 0,
          "topics": [
            "Chronic Myeloid Leukemia Treatments",
            "Medication Adherence and Compliance",
            "Acute Myeloid Leukemia Research"
          ]
        },
        {
          "openalex_id": "W4413790438",
          "year": 2025,
          "title": "CML-981: A Multinational Study to Explore Patient Preferences for Chronic Myeloid Leukemia Treatments",
          "type": "conference-abstract",
          "venue": "Clinical Lymphoma Myeloma & Leukemia",
          "cited_by_count": 0,
          "topics": [
            "Chronic Myeloid Leukemia Treatments"
          ]
        },
        {
          "openalex_id": "W4417479995",
          "year": 2025,
          "title": "EPH231 The Cost of Complacency: Projecting the Burden of HIV Care in Eight European Countries",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Impact and Responses",
            "HIV/AIDS Research and Interventions",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4412490688",
          "year": 2025,
          "title": "Effect of caregiver burden on the quality of life of informal caregivers of people with cystic fibrosis in the United Kingdom: a cross-sectional study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Family and Disability Support Research",
            "Family Caregiving in Mental Illness"
          ]
        },
        {
          "openalex_id": "W2168571737",
          "year": 1983,
          "title": "Enhancement of computed tomographic scanner based digital radiographic images",
          "type": "article",
          "venue": "British Journal of Radiology",
          "cited_by_count": 3,
          "topics": [
            "Medical Image Segmentation Techniques",
            "Medical Imaging Techniques and Applications",
            "Digital Radiography and Breast Imaging"
          ]
        },
        {
          "openalex_id": "W2131443639",
          "year": 1983,
          "title": "Tilt and slew on CT scanners and consequential problems in treatment planning with the IGE RT/PLAN system",
          "type": "article",
          "venue": "British Journal of Radiology",
          "cited_by_count": 1,
          "topics": [
            "Advanced Radiotherapy Techniques",
            "Medical Imaging Techniques and Applications",
            "Radiomics and Machine Learning in Medical Imaging"
          ]
        },
        {
          "openalex_id": "W2057312668",
          "year": 1984,
          "title": "Image noise reduction on the EMI 7070 CT scanner by the reduction of the noise resident in the CT wedge profiles",
          "type": "article",
          "venue": "Medical Physics",
          "cited_by_count": 3,
          "topics": [
            "Advanced X-ray and CT Imaging",
            "Medical Imaging Techniques and Applications",
            "Radiation Dose and Imaging"
          ]
        },
        {
          "openalex_id": "W2073007303",
          "year": 1985,
          "title": "The removal of a “cupping” artefact from brain images produced by the EMI 7070 CT scanner",
          "type": "article",
          "venue": "British Journal of Radiology",
          "cited_by_count": 7,
          "topics": [
            "Medical Imaging Techniques and Applications",
            "Advanced X-ray and CT Imaging",
            "Radiation Dose and Imaging"
          ]
        },
        {
          "openalex_id": "W2027324522",
          "year": 1998,
          "title": "Clinical variability of target volume description in conformal radiotherapy planning",
          "type": "article",
          "venue": "International Journal of Radiation Oncology*Biology*Physics",
          "cited_by_count": 130,
          "topics": [
            "Advanced Radiotherapy Techniques",
            "Prostate Cancer Diagnosis and Treatment",
            "Advances in Oncology and Radiotherapy"
          ]
        },
        {
          "openalex_id": "W4225128199",
          "year": 2022,
          "title": "Accounting for Preference Heterogeneity in Discrete-Choice Experiments: An ISPOR Special Interest Group Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 80,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W3139395459",
          "year": 2021,
          "title": "Valuing EQ-5D-Y-3L Health States Using a Discrete Choice Experiment: Do Adult and Adolescent Preferences Differ?",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 64,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2794170646",
          "year": 2018,
          "title": "Incorporating Quantitative Patient Preference Data into Healthcare Decision Making Processes: Is HTA Falling Behind?",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4225706373",
          "year": 2022,
          "title": "Considering Severity in Health Technology Assessment: Can We Do Better?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4281285777",
          "year": 2022,
          "title": "EQ-5D-Y Value Set for Germany",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 43,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4225135404",
          "year": 2022,
          "title": "Criteria for developing, assessing and selecting candidate EQ-5D bolt-ons",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 37,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3042898623",
          "year": 2020,
          "title": "Reporting Quality of Marginal Rates of Substitution in Discrete Choice Experiments That Elicit Patient Preferences",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 27,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "David Parkin",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "20170440",
        "title": "Creating a laboratory for testing differences between the 3L and 5L Index in patient populations: simulating profile and valuation data",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5081956728",
      "display_name": "David Parkin",
      "orcid": "0000-0002-9990-8208",
      "reported_affiliation": "",
      "works_count": 221,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 76
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 51
        },
        {
          "topic": "Global Health Care Issues",
          "works": 29
        },
        {
          "topic": "Astro and Planetary Science",
          "works": 15
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 14
        },
        {
          "topic": "Planetary Science and Exploration",
          "works": 14
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 10
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 10
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 8
        },
        {
          "topic": "African history and culture studies",
          "works": 8
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nancy Devlin",
          "works": 58
        },
        {
          "name": "Yan Feng",
          "works": 14
        },
        {
          "name": "Nigel Rice",
          "works": 10
        },
        {
          "name": "Bas Janssen",
          "works": 8
        },
        {
          "name": "John Appleby",
          "works": 7
        },
        {
          "name": "R. A. L. Sullivan",
          "works": 7
        },
        {
          "name": "W. Hunter",
          "works": 7
        },
        {
          "name": "Brian Yule",
          "works": 6
        },
        {
          "name": "Elaine McColl",
          "works": 6
        },
        {
          "name": "Bernarda Zamora",
          "works": 6
        },
        {
          "name": "Michael Herdman",
          "works": 5
        },
        {
          "name": "Alistair McGuire",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160389381",
          "year": 2026,
          "title": "16 Indirect Communication: Seeking Therapy and Avoiding Stigmatization",
          "type": "book-chapter",
          "venue": "Multilingual Matters eBooks",
          "cited_by_count": 0,
          "topics": [
            "Attachment and Relationship Dynamics",
            "Psychotherapy Techniques and Applications",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W7160402293",
          "year": 2026,
          "title": "Indirect Communication:",
          "type": "book-chapter",
          "venue": "Channel View Publications eBooks",
          "cited_by_count": 0,
          "topics": [
            "South Asian Cinema and Culture",
            "Cybernetics and Technology in Society",
            "Sound Studies and Aurality"
          ]
        },
        {
          "openalex_id": "W4415953323",
          "year": 2025,
          "title": "Health State Values Should Not Be Used as Minimal Important Differences",
          "type": "editorial",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4417448277",
          "year": 2025,
          "title": "Uncertainty around Health State Values Used in Cost-Effectiveness Analysis: How It Arises and How to Deal with It",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4399327403",
          "year": 2024,
          "title": "Is anchoring at ‘dead’ a theoretical requirement for health state valuation?",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4390125848",
          "year": 2023,
          "title": "EE449 Uncertainty Around HRQoL Values Is Under-Reported: Are We Misleading Decision Makers?",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2008791290",
          "year": 1959,
          "title": "Cosmic Dust in the Atmosphere",
          "type": "article",
          "venue": "Nature",
          "cited_by_count": 6,
          "topics": [
            "Atmospheric Ozone and Climate",
            "Atmospheric aerosols and clouds",
            "Atmospheric chemistry and aerosols"
          ]
        },
        {
          "openalex_id": "W2073121699",
          "year": 1960,
          "title": "Cosmic Dust in Recent Deep-Sea Sediments",
          "type": "article",
          "venue": "Proceedings of the Royal Society A Mathematical Physical and Engineering Sciences",
          "cited_by_count": 37,
          "topics": [
            "Geomagnetism and Paleomagnetism Studies",
            "Astro and Planetary Science",
            "Geology and Paleoclimatology Research"
          ]
        },
        {
          "openalex_id": "W2084257115",
          "year": 1961,
          "title": "Cosmic dust in Tertiary rock and the lunar surface",
          "type": "article",
          "venue": "Geochimica et Cosmochimica Acta",
          "cited_by_count": 9,
          "topics": [
            "Astro and Planetary Science",
            "Planetary Science and Exploration",
            "Space Science and Extraterrestrial Life"
          ]
        },
        {
          "openalex_id": "W2032079583",
          "year": 1962,
          "title": "Metallic Cosmic Dust with Amorphous Attachments",
          "type": "article",
          "venue": "Nature",
          "cited_by_count": 10,
          "topics": [
            "Material Science and Thermodynamics"
          ]
        },
        {
          "openalex_id": "W1990166011",
          "year": 2011,
          "title": "Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 10156,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Health Policy Implementation Science"
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
          "openalex_id": "W2154795762",
          "year": 2003,
          "title": "A single European currency for EQ-5D health states",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 465,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3045207140",
          "year": 2020,
          "title": "Methods for Analysing and Reporting EQ-5D Data",
          "type": "book",
          "venue": "",
          "cited_by_count": 364,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1600351176",
          "year": 1987,
          "title": "Aggregate health care expenditures and national income",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 341,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Policy and Management",
            "Fiscal Policy and Economic Growth"
          ]
        },
        {
          "openalex_id": "W2158509657",
          "year": 2013,
          "title": "Assessing the performance of the EQ-VAS in the NHS PROMs programme",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 334,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diagnosis and Treatment of Venous Diseases",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W2087374856",
          "year": 1967,
          "title": "Airborne dust collected at Barbados",
          "type": "article",
          "venue": "Geochimica et Cosmochimica Acta",
          "cited_by_count": 305,
          "topics": [
            "Marine Biology and Ecology Research",
            "Space Exploration and Technology"
          ]
        },
        {
          "openalex_id": "W1495661518",
          "year": 2007,
          "title": "Economic Analysis in Health Care",
          "type": "article",
          "venue": "",
          "cited_by_count": 278,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "David Whitehurst",
    "member_affiliation": "Simon Fraser University",
    "is_member": true,
    "projects": [
      {
        "project_id": "2016350",
        "title": "Symposium Sponsorship & Panel Session: 38th Annual North American Meeting of the Society for Medical Decision Making",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5045933977",
      "display_name": "David G. T. Whitehurst",
      "orcid": "0000-0002-7890-6756",
      "reported_affiliation": "Simon Fraser University",
      "works_count": 107,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 44
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 20
        },
        {
          "topic": "Spinal Cord Injury Research",
          "works": 19
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 15
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 10
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Urban Transport and Accessibility",
          "works": 9
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 6
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 6
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 5
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Stirling Bryan",
          "works": 25
        },
        {
          "name": "Lidia Engel",
          "works": 15
        },
        {
          "name": "Elaine M. Hay",
          "works": 12
        },
        {
          "name": "Vanessa K. Noonan",
          "works": 11
        },
        {
          "name": "Nadine E. Foster",
          "works": 10
        },
        {
          "name": "Martyn Lewis",
          "works": 9
        },
        {
          "name": "B. Catharine Craven",
          "works": 8
        },
        {
          "name": "Scott A. Lear",
          "works": 8
        },
        {
          "name": "Meghan Winters",
          "works": 7
        },
        {
          "name": "Marcel F. Dvorak",
          "works": 6
        },
        {
          "name": "Joel Singer",
          "works": 6
        },
        {
          "name": "Mathias Barra",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7125603029",
          "year": 2026,
          "title": "An Overdue Denunciation of the Minimal Important Difference When Applied to Health State Values",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W7160522918",
          "year": 2026,
          "title": "Investigating the Multifaceted Needs and Challenges of Family Caregivers of Individuals with Spinal Cord Injury: A Qualitative Study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Spinal Cord Injury Research",
            "Family and Disability Support Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W7160525067",
          "year": 2026,
          "title": "Investigating the Multifaceted Needs and Challenges of Family Caregivers of Individuals with Spinal Cord Injury: A Qualitative Study",
          "type": "article",
          "venue": "Occupational Therapy In Health Care",
          "cited_by_count": 0,
          "topics": [
            "Family and Disability Support Research",
            "Spinal Cord Injury Research",
            "Family Caregiving in Mental Illness"
          ]
        },
        {
          "openalex_id": "W7160558989",
          "year": 2026,
          "title": "Investigating the Multifaceted Needs and Challenges of Family Caregivers of Individuals with Spinal Cord Injury: A Qualitative Study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Spinal Cord Injury Research",
            "Family and Disability Support Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W4414497854",
          "year": 2025,
          "title": "Codeveloping a Novel Intervention to Promote the Well-Being of Family Caregivers of Individuals With Spinal Cord Injury: Protocol for a Feasibility Randomized Control Trial",
          "type": "article",
          "venue": "JMIR Research Protocols",
          "cited_by_count": 0,
          "topics": [
            "Spinal Cord Injury Research",
            "Family and Disability Support Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W4410112395",
          "year": 2025,
          "title": "Did a digital quality of life (QOL) assessment and practice support system in home health care improve the QOL of older adults living with life-limiting conditions and of their family caregivers? A mixed-methods pragmatic randomized controlled trial",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 4,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Geriatric Care and Nursing Homes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4234407992",
          "year": 1977,
          "title": "LETTERS TO THE EDITOR",
          "type": "letter",
          "venue": "Aquaculture Research",
          "cited_by_count": 0,
          "topics": [
            "Fish Ecology and Management Studies",
            "Aquaculture Nutrition and Growth",
            "Marine and fisheries research"
          ]
        },
        {
          "openalex_id": "W2036178474",
          "year": 2007,
          "title": "A brief pain management program compared with physical therapy for low back pain: Results from an economic analysis alongside a randomized clinical trial",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 60,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Cerebral Palsy and Movement Disorders",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2167863584",
          "year": 2008,
          "title": "A randomised clinical trial of subgrouping and targeted treatment for low back pain compared with best current care. The STarT Back Trial Study Protocol",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 126,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2119278790",
          "year": 2010,
          "title": "IMPaCT Back study protocol. Implementation of subgrouping for targeted treatment systems for low back pain patients in primary care: a prospective population-based sequential comparison",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 25,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2160769294",
          "year": 2011,
          "title": "Comparison of stratified primary care management for low back pain with current best practice (STarT Back): a randomised controlled trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1319,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2131158372",
          "year": 2014,
          "title": "Effect of Stratified Care for Low Back Pain in Family Practice (IMPaCT Back): A Prospective Population-Based Sequential Comparison",
          "type": "article",
          "venue": "The Annals of Family Medicine",
          "cited_by_count": 285,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2738540502",
          "year": 2017,
          "title": "Health Conditions: Effect on Function, Health-Related Quality of Life, and Life Satisfaction After Traumatic Spinal Cord Injury. A Prospective Observational Registry Cohort Study",
          "type": "article",
          "venue": "Archives of Physical Medicine and Rehabilitation",
          "cited_by_count": 136,
          "topics": [
            "Spinal Cord Injury Research",
            "Traumatic Brain Injury Research",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2516100673",
          "year": 2016,
          "title": "Cost-Effectiveness of Non-Invasive and Non-Pharmacological Interventions for Low Back Pain: a Systematic Literature Review",
          "type": "review",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 116,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Biofield Effects and Biophysics"
          ]
        },
        {
          "openalex_id": "W2125163971",
          "year": 2012,
          "title": "Exploring the cost–utility of stratified primary care management for low back pain compared with current best practice within risk-defined subgroups",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 88,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2471269811",
          "year": 2016,
          "title": "Older adults' quality of life – Exploring the role of the built environment and social cohesion in community-dwelling seniors on low income.",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 80,
          "topics": [
            "Urban Transport and Accessibility",
            "Health disparities and outcomes",
            "Urban Green Space and Health"
          ]
        },
        {
          "openalex_id": "W2134799417",
          "year": 2011,
          "title": "Systematic Review and Empirical Comparison of Contemporaneous EQ-5D and SF-6D Group Mean Scores",
          "type": "review",
          "venue": "Medical Decision Making",
          "cited_by_count": 69,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        }
      ]
    }
  },
  {
    "name": "Deborah Marshall",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1752-RA",
        "title": "Validity and Responsiveness of the EQ-5D-Y-5L Instruments in the Juvenile Idiopathic Arthritis",
        "working_group": "Descriptive Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5049401142",
      "display_name": "Deborah A. Marshall",
      "orcid": "0000-0002-8467-8008",
      "reported_affiliation": "University of Calgary",
      "works_count": 547,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 103
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 81
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 71
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 56
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 42
        },
        {
          "topic": "Genomics and Rare Diseases",
          "works": 37
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 34
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 31
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 30
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 28
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 27
        },
        {
          "topic": "Musculoskeletal Disorders and Rehabilitation",
          "works": 20
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Karen V. MacDonald",
          "works": 52
        },
        {
          "name": "Gillian Currie",
          "works": 49
        },
        {
          "name": "Glen Hazlewood",
          "works": 45
        },
        {
          "name": "Claire Barber",
          "works": 45
        },
        {
          "name": "Dianne Mosher",
          "works": 42
        },
        {
          "name": "Peter Faris",
          "works": 40
        },
        {
          "name": "Cheryl Barnabé",
          "works": 36
        },
        {
          "name": "Maarten J. IJzerman",
          "works": 35
        },
        {
          "name": "Éric Bohm",
          "works": 33
        },
        {
          "name": "Tom Noseworthy",
          "works": 33
        },
        {
          "name": "Gillian Hawker",
          "works": 31
        },
        {
          "name": "Susanne M. Benseler",
          "works": 31
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7124446009",
          "year": 2026,
          "title": "Addressing the Challenges of Psychosocial Experiences with Food in IBD Clinical Care: A Study Protocol for a Two-Phase Mixed-Methods Study",
          "type": "preprint",
          "venue": "OSF Preprints (OSF Preprints)",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Bowel Disease",
            "Gastrointestinal motility and disorders",
            "Celiac Disease Research and Management"
          ]
        },
        {
          "openalex_id": "W7164830992",
          "year": 2026,
          "title": "From disability to daily life: functional status, quality of life and work productivity in real-world inflammatory arthritis",
          "type": "article",
          "venue": "Lara D. Veeken",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments",
            "Systemic Sclerosis and Related Diseases"
          ]
        },
        {
          "openalex_id": "W7117988537",
          "year": 2026,
          "title": "Navigation, Adoption, and Use of Digital Health Technologies for Irritable Bowel Syndrome Self-Management: Focus Group Study of Patient Experience and Decision-Making",
          "type": "article",
          "venue": "JMIR Human Factors",
          "cited_by_count": 1,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Mobile Health and mHealth Applications",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W7125524238",
          "year": 2026,
          "title": "Patient-reported Symptoms Are Independent of Extent of Disease in Longstanding Ulcerative Colitis",
          "type": "article",
          "venue": "Journal of Clinical Gastroenterology",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Bowel Disease",
            "Gut microbiota and health",
            "Liver Diseases and Immunity"
          ]
        },
        {
          "openalex_id": "W7167502136",
          "year": 2026,
          "title": "Ten high-priority areas for health policy research in 2026-2027",
          "type": "editorial",
          "venue": "Health Affairs Scholar",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W4412111488",
          "year": 2025,
          "title": "A national curriculum and community of practice for health services and policy research training: Insights from the Health System Impact Fellowship National Cohort Training Program ( <scp>HSIF NCTP</scp> )",
          "type": "article",
          "venue": "Learning Health Systems",
          "cited_by_count": 1,
          "topics": [
            "Primary Care and Health Outcomes",
            "Global Health Workforce Issues",
            "Health and Medical Research Impacts"
          ]
        },
        {
          "openalex_id": "W2473608083",
          "year": 1962,
          "title": "Intraepithelial carcinoma of the cervix: a clinical reappraisal.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 18,
          "topics": [
            "Cervical Cancer and HPV Research"
          ]
        },
        {
          "openalex_id": "W2418070017",
          "year": 1967,
          "title": "Doctor, how can MARMP be of greatest value to you?",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Health and Medical Research Impacts",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2469447859",
          "year": 1980,
          "title": "CORONARY BLOOD FLOW IN NONWORKING, ATROPHIC RAT HEARTS.",
          "type": "conference-abstract",
          "venue": "Medicine & Science in Sports & Exercise",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Renin-Angiotensin System Studies",
            "Adipose Tissue and Metabolism"
          ]
        },
        {
          "openalex_id": "W4206629313",
          "year": 1983,
          "title": "Intracranial complications of rhinoplasty",
          "type": "article",
          "venue": "British Journal of Plastic Surgery",
          "cited_by_count": 6,
          "topics": [
            "Nasal Surgery and Airway Studies",
            "Body Image and Dysmorphia Studies",
            "Digital Imaging in Medicine"
          ]
        },
        {
          "openalex_id": "W2036125852",
          "year": 1996,
          "title": "Meta-analysis of how well measures of bone mineral density predict occurrence of osteoporotic fractures",
          "type": "review",
          "venue": "BMJ",
          "cited_by_count": 3714,
          "topics": [
            "Bone health and osteoporosis research",
            "Parathyroid Disorders and Treatments",
            "Hip and Femur Fractures"
          ]
        },
        {
          "openalex_id": "W2121619367",
          "year": 2011,
          "title": "Conjoint Analysis Applications in Health—a Checklist: A Report of the ISPOR Good Research Practices for Conjoint Analysis Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2056,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods and Bayesian Inference"
          ]
        },
        {
          "openalex_id": "W2159936838",
          "year": 2013,
          "title": "Constructing Experimental Designs for Discrete-Choice Experiments: Report of the ISPOR Conjoint Analysis Experimental Design Good Research Practices Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1826,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2367707061",
          "year": 2016,
          "title": "Statistical Methods for the Analysis of Discrete Choice Experiments: A Report of the ISPOR Conjoint Analysis Good Research Practices Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1331,
          "topics": [
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W2157450846",
          "year": 2007,
          "title": "Using Real-World Data for Coverage and Payment Decisions: The ISPOR Real-World Data Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 707,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W1590210216",
          "year": 2010,
          "title": "Conjoint Analysis Applications in Health – How are Studies being Designed and Reported?",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 362,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1562415841",
          "year": 2006,
          "title": "Using and interpreting cost-effectiveness acceptability curves: an example using data from a trial of management strategies for atrial fibrillation",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 282,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Atrial Fibrillation Management and Outcomes",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2238427603",
          "year": 2015,
          "title": "Cost-effectiveness of nurse practitioners in primary and specialised ambulatory care: systematic review",
          "type": "review",
          "venue": "BMJ Open",
          "cited_by_count": 255,
          "topics": [
            "Nursing Roles and Practices",
            "Interprofessional Education and Collaboration",
            "Clinical practice guidelines implementation"
          ]
        }
      ]
    }
  }
]
