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
    "name": "Emelie Heintz",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180760",
        "title": "Health-related quality of life in patients with amputation of the lower extremity: a comparison of EQ-5D-3L and -5L performance",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5052327641",
      "display_name": "Emelie Heintz",
      "orcid": "0000-0002-0715-7591",
      "reported_affiliation": "Stockholm School of Economics",
      "works_count": 81,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 35
        },
        {
          "topic": "Prostate Cancer Diagnosis and Treatment",
          "works": 9
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 8
        },
        {
          "topic": "Prostate Cancer Treatment and Research",
          "works": 6
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 4
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 4
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 4
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 4
        },
        {
          "topic": "Social and Educational Sciences",
          "works": 4
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 3
        },
        {
          "topic": "Electroconvulsive Therapy Studies",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Shuang Hao",
          "works": 12
        },
        {
          "name": "Malin Regardt",
          "works": 11
        },
        {
          "name": "Ioannis Parodis",
          "works": 11
        },
        {
          "name": "Mark Clements",
          "works": 10
        },
        {
          "name": "Tobias Nordström",
          "works": 7
        },
        {
          "name": "Thomas Davidson",
          "works": 7
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 7
        },
        {
          "name": "Martin Eklund",
          "works": 6
        },
        {
          "name": "Lars‐Åke Levin",
          "works": 6
        },
        {
          "name": "Lars Sandman",
          "works": 6
        },
        {
          "name": "Julius Lindblom",
          "works": 6
        },
        {
          "name": "Kinza Degerlund-Maldi",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169831773",
          "year": 2026,
          "title": "Additional file 1 of Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7169893901",
          "year": 2026,
          "title": "Additional file 1 of Variations in health-related quality of life across sociodemographic groups, health conditions, and modifiable risk factors: a population-based EQ-5D-3L study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7151971431",
          "year": 2026,
          "title": "Additional file 2 of The value of EQ-5D-3L and EQ VAS as a patient-reported outcome measure for patients with ankylosing spondylitis in routine healthcare: an evaluation of construct validity and responsiveness based on the Swedish Rheumatology Quality Register",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7152117115",
          "year": 2026,
          "title": "Additional file 2 of The value of EQ-5D-3L and EQ VAS as a patient-reported outcome measure for patients with ankylosing spondylitis in routine healthcare: an evaluation of construct validity and responsiveness based on the Swedish Rheumatology Quality Register",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7170131856",
          "year": 2026,
          "title": "Construct validity and responsiveness of EQ-5D-3L and EQ VAS in psoriatic arthritis: an evaluation based on the Swedish Rheumatology Quality Register",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W7128261797",
          "year": 2026,
          "title": "The value of EQ-5D-3L and EQ VAS as a patient-reported outcome measure for patients with ankylosing spondylitis in routine healthcare: an evaluation of construct validity and responsiveness based on the Swedish Rheumatology Quality Register",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2148394335",
          "year": 2001,
          "title": "Comparison of Somatostatin Analog and Meta-Iodobenzylguanidine Radionuclides in the Diagnosis and Localization of Advanced Neuroendocrine Tumors",
          "type": "article",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 260,
          "topics": [
            "Neuroendocrine Tumor Research Advances",
            "Neuroblastoma Research and Treatments",
            "Lung Cancer Research Studies"
          ]
        },
        {
          "openalex_id": "W2167046068",
          "year": 2008,
          "title": "The cost-effectiveness of foetal monitoring with ST analysis",
          "type": "dissertation",
          "venue": "KTH Publication Database DiVA (KTH Royal Institute of Technology)",
          "cited_by_count": 2,
          "topics": [
            "Infant Development and Preterm Care",
            "Cerebral Palsy and Movement Disorders",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2098718172",
          "year": 2008,
          "title": "The long‐term cost‐effectiveness of fetal monitoring during labour: a comparison of cardiotocography complemented with ST analysis versus cardiotocography alone",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 37,
          "topics": [
            "Neonatal and fetal brain pathology",
            "Neonatal Respiratory Health Research",
            "ECG Monitoring and Analysis"
          ]
        },
        {
          "openalex_id": "W2141132233",
          "year": 2010,
          "title": "Nationellt system för utvärdering, prioritering och införandebeslut av icke-farmakologiska sjukvårdsteknologier en förstudie",
          "type": "report",
          "venue": "KTH Publication Database DiVA (KTH Royal Institute of Technology)",
          "cited_by_count": 2,
          "topics": [
            "Social and Educational Sciences"
          ]
        },
        {
          "openalex_id": "W2113690422",
          "year": 2014,
          "title": "Internet-Delivered Psychological Treatments for Mood and Anxiety Disorders: A Systematic Review of Their Efficacy, Safety, and Cost-Effectiveness",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 351,
          "topics": [
            "Digital Mental Health Interventions",
            "Impact of Technology on Adolescents",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes"
          ]
        },
        {
          "openalex_id": "W2562390848",
          "year": 2016,
          "title": "Is the acute care of frail elderly patients in a comprehensive geriatric assessment unit superior to conventional acute medical care?",
          "type": "article",
          "venue": "Clinical Interventions in Aging",
          "cited_by_count": 120,
          "topics": [
            "Frailty in Older Adults",
            "Geriatric Care and Nursing Homes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W1996708310",
          "year": 2010,
          "title": "Prevalence and healthcare costs of diabetic retinopathy: a population-based register study in Sweden",
          "type": "article",
          "venue": "Diabetologia",
          "cited_by_count": 108,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2104025691",
          "year": 2015,
          "title": "Is There a European View on Health Economic Evaluations? Results from a Synopsis of Methodological Guidelines Used in the EUnetHTA Partner Countries",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 87,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1907218431",
          "year": 2015,
          "title": "FRAMEWORK FOR SYSTEMATIC IDENTIFICATION OF ETHICAL ASPECTS OF HEALTHCARE TECHNOLOGIES: THE SBU APPROACH",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 54,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Ethics in Clinical Research"
          ]
        },
        {
          "openalex_id": "W2933982531",
          "year": 2019,
          "title": "Treatment of radius or ulna fractures in the elderly: A systematic review covering effectiveness, safety, economic aspects and current practice",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 50,
          "topics": [
            "Orthopedic Surgery and Rehabilitation",
            "Bone fractures and treatments",
            "Elbow and Forearm Trauma Treatment"
          ]
        },
        {
          "openalex_id": "W2020092164",
          "year": 2012,
          "title": "QALY Weights for Diabetic Retinopathy—A Comparison of Health State Valuations with HUI-3, EQ-5D, EQ-VAS, and TTO",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ophthalmology and Visual Impairment Studies",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Emily McDool",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1455-RA",
        "title": "A comparison of the EQ Health and Wellbeing (EQ-HWB) and EQ-5D-5L instruments.",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "1665-RA",
        "title": "Evaluating the validity of the EQ Health and Wellbeing short (EQ-HWB-S) in a large general population sample.",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2097-RA",
        "title": "The relationship between the EQ Health and Wellbeing short (EQ-HWB-S) and age in a large UK general population sample. A comparison with the EQ-5D-5L.",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5006458172",
      "display_name": "Emily McDool",
      "orcid": "0000-0002-3530-7921",
      "reported_affiliation": "University of Sheffield",
      "works_count": 25,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "School Choice and Performance",
          "works": 5
        },
        {
          "topic": "Impact of Technology on Adolescents",
          "works": 3
        },
        {
          "topic": "Psychological and Temporal Perspectives Research",
          "works": 3
        },
        {
          "topic": "Child Development and Digital Technology",
          "works": 3
        },
        {
          "topic": "Urban, Neighborhood, and Segregation Studies",
          "works": 3
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Early Childhood Education and Development",
          "works": 2
        },
        {
          "topic": "Parental Involvement in Education",
          "works": 2
        },
        {
          "topic": "Global Health Care Issues",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Clara Mukuria",
          "works": 8
        },
        {
          "name": "Philip A. Powell",
          "works": 6
        },
        {
          "name": "Donna Rowen",
          "works": 6
        },
        {
          "name": "John Brazier",
          "works": 6
        },
        {
          "name": "Jill Carlton",
          "works": 5
        },
        {
          "name": "Tessa Peasgood",
          "works": 4
        },
        {
          "name": "Jennifer Roberts",
          "works": 3
        },
        {
          "name": "Karl Taylor",
          "works": 3
        },
        {
          "name": "Richard Norman",
          "works": 2
        },
        {
          "name": "P. Schneider",
          "works": 2
        },
        {
          "name": "Kristina Ludwig",
          "works": 2
        },
        {
          "name": "Ole Marten",
          "works": 2
        }
      ],
      "work_examples": [
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
          "openalex_id": "W4409841488",
          "year": 2025,
          "title": "Psychometric Performance of a New Condition-Specific Preference-Weighted Measure, Vision Impairment in Low Luminance-Utility Index, and EQ-5D-5L in Patients With Age-Related Macular Degeneration: A MACUSTAR Study Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4403905837",
          "year": 2024,
          "title": "Deriving a Preference-Weighted Measure for People With Hypoglycemia From the Hypo-RESOLVE QoL",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4405748406",
          "year": 2024,
          "title": "EE391 Psychometric Performance of EQ-5D-5L and VILL-UI, a New Condition-Specific Preference-Weighted Measure, in Patients With Age-Related Macular Degeneration: A Macustar Study Report",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4399600108",
          "year": 2024,
          "title": "Measuring Health-Related Quality of Life in Amyotrophic Lateral Sclerosis",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 13,
          "topics": [
            "Amyotrophic Lateral Sclerosis Research",
            "Parkinson's Disease and Spinal Disorders",
            "Genetic Neurodegenerative Diseases"
          ]
        },
        {
          "openalex_id": "W2563015429",
          "year": 2016,
          "title": "Evaluation of neighbourhood, class setting and academy school effects on education outcomes in the UK",
          "type": "dissertation",
          "venue": "White Rose eTheses Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "School Choice and Performance",
            "Education Systems and Policy",
            "Urban, Neighborhood, and Segregation Studies"
          ]
        },
        {
          "openalex_id": "W2572694853",
          "year": 2016,
          "title": "Social Media Use and Children's Wellbeing",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 35,
          "topics": [
            "Impact of Technology on Adolescents",
            "Child Development and Digital Technology",
            "Psychological and Temporal Perspectives Research"
          ]
        },
        {
          "openalex_id": "W3125076786",
          "year": 2016,
          "title": "Social Media Use and Children's Wellbeing",
          "type": "report",
          "venue": "Econstor (Econstor)",
          "cited_by_count": 1,
          "topics": [
            "Impact of Technology on Adolescents",
            "Child Development and Digital Technology",
            "Psychological and Temporal Perspectives Research"
          ]
        },
        {
          "openalex_id": "W2598808111",
          "year": 2016,
          "title": "The Effect of Primary Converter Academies on Pupil Performance",
          "type": "book",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "School Choice and Performance",
            "Urban, Neighborhood, and Segregation Studies",
            "Higher Education Research Studies"
          ]
        },
        {
          "openalex_id": "W2995715396",
          "year": 2019,
          "title": "The internet and children’s psychological wellbeing",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 186,
          "topics": [
            "Impact of Technology on Adolescents",
            "Psychological and Temporal Perspectives Research",
            "Child Development and Digital Technology"
          ]
        },
        {
          "openalex_id": "W4321254282",
          "year": 2023,
          "title": "Valuing the EQ Health and Wellbeing Short Using Time Trade-Off and a Discrete Choice Experiment: A Feasibility Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W3165116286",
          "year": 2021,
          "title": "A Comparison of the SF-6Dv2 and SF-6D UK Utility Values in a Mixed Patient and Healthy Population",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 24,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4403790081",
          "year": 2024,
          "title": "The Short Form 6 Dimensions (SF-6D): Development and Evolution",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 22,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4398248596",
          "year": 2024,
          "title": "Psychometric Performance of the EQ Health and Wellbeing Short in a United Kingdom Population Sample",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4285391510",
          "year": 2022,
          "title": "A Systematic Review of the Methodologies and Modelling Approaches Used to Generate International EQ-5D-5L Value Sets",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 13,
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
    "name": "Eri Hoshino",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2085-VS",
        "title": "Valuation study of EQ-5D-Y-5L in Japan",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5068533812",
      "display_name": "Eri Hoshino",
      "orcid": "0000-0003-2308-2048",
      "reported_affiliation": "National Center For Child Health and Development",
      "works_count": 77,
      "top_topics": [
        {
          "topic": "Pediatric Hepatobiliary Diseases and Treatments",
          "works": 11
        },
        {
          "topic": "Gallbladder and Bile Duct Disorders",
          "works": 8
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Migraine and Headache Studies",
          "works": 6
        },
        {
          "topic": "Dysphagia Assessment and Management",
          "works": 5
        },
        {
          "topic": "Nutrition and Health in Aging",
          "works": 4
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 4
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        },
        {
          "topic": "Neonatal Health and Biochemistry",
          "works": 4
        },
        {
          "topic": "Disaster Response and Management",
          "works": 3
        },
        {
          "topic": "Metabolism and Genetic Disorders",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kotomi Sakai",
          "works": 14
        },
        {
          "name": "Mitsuyoshi Suzuki",
          "works": 13
        },
        {
          "name": "Keiko Konomura",
          "works": 8
        },
        {
          "name": "Kevin Y. Urayama",
          "works": 7
        },
        {
          "name": "Masayuki Obatake",
          "works": 7
        },
        {
          "name": "Kazuki Fujita",
          "works": 6
        },
        {
          "name": "Kojiro Shimozuma",
          "works": 6
        },
        {
          "name": "Takeru Shiroiwa",
          "works": 6
        },
        {
          "name": "Kuniyoshi Hayashi",
          "works": 5
        },
        {
          "name": "Osamu Takahashi",
          "works": 5
        },
        {
          "name": "Ryo Momosaki",
          "works": 5
        },
        {
          "name": "Takashi Fukuda",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7147283173",
          "year": 2026,
          "title": "Cost-Effectiveness of Newborn Screening for Infantile-Onset Pompe Disease in Japan",
          "type": "article",
          "venue": "International Journal of Neonatal Screening",
          "cited_by_count": 1,
          "topics": [
            "Lysosomal Storage Disorders Research",
            "Genomics and Rare Diseases",
            "Metabolism and Genetic Disorders"
          ]
        },
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
          "openalex_id": "W7132850587",
          "year": 2026,
          "title": "Quality of Life Research in Parents and Informal Caregivers of Children With Chronic Illnesses: A Scoping Review",
          "type": "article",
          "venue": "Academic Pediatrics",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Family and Disability Support Research",
            "Adolescent and Pediatric Healthcare"
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
          "openalex_id": "W4406162388",
          "year": 2025,
          "title": "Economic evaluation of newborn screening for congenital cytomegalovirus infection: A systematic review",
          "type": "review",
          "venue": "European Journal of Pediatrics",
          "cited_by_count": 4,
          "topics": [
            "Cytomegalovirus and herpesvirus research",
            "Immunodeficiency and Autoimmune Disorders",
            "Neonatal Health and Biochemistry"
          ]
        },
        {
          "openalex_id": "W1977798436",
          "year": 2005,
          "title": "Simple Analysis for Inorganic Anions in Air Samples by Means of Capillary Electrophoresis",
          "type": "article",
          "venue": "BUNSEKI KAGAKU",
          "cited_by_count": 0,
          "topics": [
            "Advanced Chemical Sensor Technologies",
            "Microfluidic and Capillary Electrophoresis Applications",
            "Biosensors and Analytical Detection"
          ]
        },
        {
          "openalex_id": "W1983038359",
          "year": 2010,
          "title": "A novel nonsecosteroidal VDR agonist (CH5036249) exhibits efficacy in a spontaneous benign prostatic hyperplasia beagle model",
          "type": "article",
          "venue": "The Journal of Steroid Biochemistry and Molecular Biology",
          "cited_by_count": 15,
          "topics": [
            "Urinary Bladder and Prostate Research",
            "Hormonal and reproductive studies",
            "Urological Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W2035416828",
          "year": 2012,
          "title": "Nuclear disaster and the medical problems during the earthquake in Japan, 2011",
          "type": "article",
          "venue": "Critical Care",
          "cited_by_count": 1,
          "topics": [
            "Disaster Response and Management"
          ]
        },
        {
          "openalex_id": "W2056742006",
          "year": 2013,
          "title": "Erratum to: Serum level of soluble (pro)renin receptor is modulated in chronic kidney disease",
          "type": "erratum",
          "venue": "Clinical and Experimental Nephrology",
          "cited_by_count": 1,
          "topics": [
            "Renin-Angiotensin System Studies",
            "Eicosanoids and Hypertension Pharmacology"
          ]
        },
        {
          "openalex_id": "W2775239209",
          "year": 2017,
          "title": "A prospective phase II study of combined androgen blockade in patients with androgen receptor-positive metastatic or locally advanced unresectable salivary gland carcinoma",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 222,
          "topics": [
            "Salivary Gland Tumors Diagnosis and Treatment",
            "Head and Neck Cancer Studies",
            "Salivary Gland Disorders and Functions"
          ]
        },
        {
          "openalex_id": "W2075717734",
          "year": 2013,
          "title": "Serum level of soluble (pro)renin receptor is modulated in chronic kidney disease",
          "type": "article",
          "venue": "Clinical and Experimental Nephrology",
          "cited_by_count": 83,
          "topics": [
            "Renin-Angiotensin System Studies",
            "Nitric Oxide and Endothelin Effects",
            "Genetics and Physical Performance"
          ]
        },
        {
          "openalex_id": "W4285596309",
          "year": 2022,
          "title": "Association of Oral Function and Dysphagia with Frailty and Sarcopenia in Community-Dwelling Older Adults: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "Cells",
          "cited_by_count": 74,
          "topics": [
            "Nutrition and Health in Aging",
            "Dysphagia Assessment and Management",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2801664613",
          "year": 2018,
          "title": "Current Vitamin D Status in Healthy Japanese Infants and Young Children",
          "type": "article",
          "venue": "Journal of Nutritional Science and Vitaminology",
          "cited_by_count": 56,
          "topics": [
            "Vitamin D Research Studies",
            "Breastfeeding Practices and Influences",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W2603961714",
          "year": 2017,
          "title": "Reassessing the Ecology of Medical Care in Japan",
          "type": "article",
          "venue": "Journal of Community Health",
          "cited_by_count": 44,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4362457996",
          "year": 2023,
          "title": "Age at surgery and native liver survival in biliary atresia: a systematic review and meta-analysis",
          "type": "review",
          "venue": "European Journal of Pediatrics",
          "cited_by_count": 37,
          "topics": [
            "Pediatric Hepatobiliary Diseases and Treatments",
            "Gallbladder and Bile Duct Disorders",
            "Congenital Anomalies and Fetal Surgery"
          ]
        },
        {
          "openalex_id": "W2921086336",
          "year": 2019,
          "title": "Enhanced outcomes for coronary artery disease obtained by a multidisciplinary heart team approach",
          "type": "article",
          "venue": "General Thoracic and Cardiovascular Surgery",
          "cited_by_count": 29,
          "topics": [
            "Cardiac and Coronary Surgery Techniques",
            "Coronary Interventions and Diagnostics",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W2906339758",
          "year": 2018,
          "title": "Variation in somatic symptoms by patient health questionnaire-9 depression scores in a representative Japanese sample",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 27,
          "topics": [
            "Mental Health Treatment and Access",
            "Musculoskeletal pain and rehabilitation",
            "Psychosomatic Disorders and Their Treatments"
          ]
        }
      ]
    }
  },
  {
    "name": "Erica Lubetkin",
    "member_affiliation": "City University of New York School of Medicine",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5037314317",
      "display_name": "Erica I. Lubetkin",
      "orcid": "0000-0001-9962-7775",
      "reported_affiliation": "CUNY School of Law",
      "works_count": 94,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 37
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 25
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 7
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 6
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 6
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 6
        },
        {
          "topic": "Bariatric Surgery and Outcomes",
          "works": 5
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Haomiao Jia",
          "works": 47
        },
        {
          "name": "Marthe R. Gold",
          "works": 17
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 13
        },
        {
          "name": "Peter Franks",
          "works": 9
        },
        {
          "name": "Juanita A. Haagsma",
          "works": 9
        },
        {
          "name": "Gouke J. Bonsel",
          "works": 9
        },
        {
          "name": "Peter Muennig",
          "works": 7
        },
        {
          "name": "Jennifer L. Hay",
          "works": 7
        },
        {
          "name": "Jack E. Burkhalter",
          "works": 6
        },
        {
          "name": "Debra Brennessel",
          "works": 5
        },
        {
          "name": "Andrew Webb",
          "works": 5
        },
        {
          "name": "Kathleen Lynch",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411241524",
          "year": 2025,
          "title": "Comparing Potential Contributors of Health-Related Quality of Life and Mortality Among US Older Adults",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Frailty in Older Adults",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W4416297506",
          "year": 2025,
          "title": "Design and implementation of data quality controls in the EQ-DAPHNIE study: insights from the pilot phase and 15-country analysis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Census and Population Estimation",
            "Data Quality and Management"
          ]
        },
        {
          "openalex_id": "W4410056786",
          "year": 2025,
          "title": "EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, Environment, Cognitive Aging"
          ]
        },
        {
          "openalex_id": "W4408179401",
          "year": 2025,
          "title": "Health-Related Quality of Life for Persons Treated or Monitored for Anal High-Grade Squamous Intraepithelial Lesions (AMC-A01)",
          "type": "article",
          "venue": "JCO Oncology Practice",
          "cited_by_count": 2,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Colorectal and Anal Carcinomas",
            "Anorectal Disease Treatments and Outcomes"
          ]
        },
        {
          "openalex_id": "W4414898827",
          "year": 2025,
          "title": "Health-related quality of life in COVID-19 patients: a systematic review and meta-analysis of EQ-5D studies",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 8,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4417326083",
          "year": 2025,
          "title": "Net effects of correlated determinants of health among U.S. older adults",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Aging and Gerontology Research",
            "Retirement, Disability, and Employment"
          ]
        },
        {
          "openalex_id": "W1986988131",
          "year": 1995,
          "title": "Gastrointestinal complications following orthotopic lung transplantation",
          "type": "article",
          "venue": "Gastroenterology",
          "cited_by_count": 0,
          "topics": [
            "Transplantation: Methods and Outcomes",
            "Organ and Tissue Transplantation Research",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W2031595751",
          "year": 1999,
          "title": "Risks and benefits of early clinical exposure",
          "type": "article",
          "venue": "Academic Medicine",
          "cited_by_count": 5,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W1971585152",
          "year": 1999,
          "title": "The use of questionnaires to assess achievement of course goals in medical studentsʼ longitudinal community-based clinical experiences",
          "type": "article",
          "venue": "Academic Medicine",
          "cited_by_count": 17,
          "topics": [
            "Innovations in Medical Education",
            "Nursing education and management",
            "Medical Education and Admissions"
          ]
        },
        {
          "openalex_id": "W2777831103",
          "year": 2001,
          "title": "Using self-administered surveys to measure health-related quality of life for patients at a community health center: results of a pilot study",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Primary Care and Health Outcomes",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W2100171985",
          "year": 2005,
          "title": "The impact of obesity on health-related quality-of-life in the general adult US population",
          "type": "article",
          "venue": "Journal of Public Health",
          "cited_by_count": 562,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Obesity and Health Practices",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2039195371",
          "year": 2005,
          "title": "Relationship Among Sociodemographic Factors, Clinical Conditions, and Health-related Quality of Life: Examining the EQ-5D in the U.S. General Population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 268,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2082505826",
          "year": 2006,
          "title": "Gender and the Burden of Disease Attributable to Obesity",
          "type": "article",
          "venue": "American Journal of Public Health",
          "cited_by_count": 245,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Obesity and Health Practices",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2091545728",
          "year": 2010,
          "title": "Trends in Quality-Adjusted Life-Years Lost Contributed by Smoking and Obesity",
          "type": "article",
          "venue": "American Journal of Preventive Medicine",
          "cited_by_count": 183,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1888647731",
          "year": 2010,
          "title": "The use of the EQ-5D preference-based health status measure in adults with Type 2 diabetes mellitus",
          "type": "article",
          "venue": "Diabetic Medicine",
          "cited_by_count": 176,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W2122589980",
          "year": 2008,
          "title": "I Think Therefore I Am: Perceived Ideal Weight as a Determinant of Health",
          "type": "article",
          "venue": "American Journal of Public Health",
          "cited_by_count": 134,
          "topics": [
            "Eating Disorders and Behaviors",
            "Obesity and Health Practices",
            "Bariatric Surgery and Outcomes"
          ]
        },
        {
          "openalex_id": "W1985332092",
          "year": 2004,
          "title": "Mapping the SF-12 to the EuroQol EQ-5D Index in a National US Sample",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 124,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2042903601",
          "year": 2005,
          "title": "The burden of disease associated with being African-American in the United States and the contribution of socio-economic status",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 113,
          "topics": [
            "Health disparities and outcomes",
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Ernest Law",
    "member_affiliation": "Pfizer",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5040405517",
      "display_name": "Ernest H. Law",
      "orcid": "0000-0002-6111-8008",
      "reported_affiliation": "Pfizer (United States)",
      "works_count": 126,
      "top_topics": [
        {
          "topic": "Hair Growth and Disorders",
          "works": 40
        },
        {
          "topic": "Advanced Breast Cancer Therapies",
          "works": 30
        },
        {
          "topic": "Breast Cancer Treatment Studies",
          "works": 22
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 14
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Facial Rejuvenation and Surgery Techniques",
          "works": 13
        },
        {
          "topic": "Multiple and Secondary Primary Cancers",
          "works": 9
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 8
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 6
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 5
        },
        {
          "topic": "Cancer-related cognitive impairment studies",
          "works": 5
        },
        {
          "topic": "Wound Healing and Treatments",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kent A. Hanson",
          "works": 17
        },
        {
          "name": "Debanjali Mitra",
          "works": 16
        },
        {
          "name": "Helen Tran",
          "works": 15
        },
        {
          "name": "Samantha K. Kurosky",
          "works": 15
        },
        {
          "name": "Robert Wołk",
          "works": 14
        },
        {
          "name": "J. Cueto",
          "works": 12
        },
        {
          "name": "Gregory S. Calip",
          "works": 10
        },
        {
          "name": "Sérgio Vañó-Galván",
          "works": 10
        },
        {
          "name": "A. Simon Pickard",
          "works": 9
        },
        {
          "name": "Fida Bacha",
          "works": 9
        },
        {
          "name": "Dalia Wajsbrot",
          "works": 9
        },
        {
          "name": "Rodney Sinclair",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164313570",
          "year": 2026,
          "title": "A Cost-per-Responder Analysis of Ritlecitinib vs Baricitinib in Severe Alopecia Areata",
          "type": "article",
          "venue": "Journal of health economics and outcomes research",
          "cited_by_count": 0,
          "topics": [
            "Hair Growth and Disorders",
            "Facial Rejuvenation and Surgery Techniques",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W7130372232",
          "year": 2026,
          "title": "Correction: Impact of adding palbociclib on treatment adherence to ongoing adjuvant endocrine treatment in the global randomized PALLAS randomized trial in patients with early breast cancer",
          "type": "erratum",
          "venue": "Breast Cancer Research and Treatment",
          "cited_by_count": 0,
          "topics": [
            "Advanced Breast Cancer Therapies",
            "Cancer-related Molecular Pathways",
            "HER2/EGFR in Cancer Research"
          ]
        },
        {
          "openalex_id": "W7134844216",
          "year": 2026,
          "title": "Cost‐Effectiveness Analysis of Ritlecitinib Compared With No Treatment in Patients With Severe Alopecia Areata in Japan",
          "type": "article",
          "venue": "The Journal of Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Cytokine Signaling Pathways and Interactions",
            "Hair Growth and Disorders"
          ]
        },
        {
          "openalex_id": "W7163519730",
          "year": 2026,
          "title": "The Efficacy and Safety of Etrasimod in Mildly to Moderately Active Ulcerative Colitis: Results From the Phase II GLADIATOR Trial",
          "type": "article",
          "venue": "Clinical Gastroenterology and Hepatology",
          "cited_by_count": 1,
          "topics": [
            "Inflammatory Bowel Disease",
            "Helicobacter pylori-related gastroenterology studies",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W7140122793",
          "year": 2026,
          "title": "Treatment priorities and unmet needs according to adults and adolescents with nonsegmental vitiligo in the United States",
          "type": "article",
          "venue": "Journal of Dermatological Treatment",
          "cited_by_count": 0,
          "topics": [
            "melanin and skin pigmentation",
            "Acne and Rosacea Treatments and Effects",
            "Retinal Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W7140124327",
          "year": 2026,
          "title": "Treatment priorities and unmet needs according to adults and adolescents with nonsegmental vitiligo in the United States",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "melanin and skin pigmentation",
            "Retinal Diseases and Treatments",
            "Retinal Development and Disorders"
          ]
        },
        {
          "openalex_id": "W4231051146",
          "year": 1917,
          "title": "Authors of Quotations Wanted",
          "type": "article",
          "venue": "Notes and Queries",
          "cited_by_count": 0,
          "topics": [
            "Legal principles and applications",
            "Legal Cases and Commentary",
            "Legal case studies and regulations"
          ]
        },
        {
          "openalex_id": "W2764375935",
          "year": 1998,
          "title": "Women's health in Manchester.",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1812152075",
          "year": 2008,
          "title": "Pathology and Therapeutics for Pharmacists: A Basis for Clinical Pharmacy Practice, 3rd Edition",
          "type": "article",
          "venue": "Journal of Pharmacy & Pharmaceutical Sciences",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical studies and practices",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2087098137",
          "year": 2010,
          "title": "Aspirin Use Rates in Diabetes: A Systematic Review Cross-Sectional Study",
          "type": "review",
          "venue": "Canadian Journal of Diabetes",
          "cited_by_count": 6,
          "topics": [
            "Antiplatelet Therapy and Cardiovascular Diseases",
            "Diabetes Treatment and Management",
            "Lipoproteins and Cardiovascular Health"
          ]
        },
        {
          "openalex_id": "W2945409099",
          "year": 2019,
          "title": "United States Valuation of EQ-5D-5L Health States Using an International Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 399,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3048694137",
          "year": 2020,
          "title": "Parallel Valuation of the EQ-5D-3L and EQ-5D-5L by Time Trade-Off in Hungary",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2768939817",
          "year": 2017,
          "title": "Insulin Sensitivity and Diabetic Kidney Disease in Children and Adolescents With Type 2 Diabetes: An Observational Analysis of Data From the TODAY Clinical Trial",
          "type": "article",
          "venue": "American Journal of Kidney Diseases",
          "cited_by_count": 90,
          "topics": [
            "Diabetes Management and Research",
            "Chronic Kidney Disease and Diabetes",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W3130416374",
          "year": 2021,
          "title": "Risk of recurrence among patients with HR-positive, HER2-negative, early breast cancer receiving adjuvant endocrine therapy: A systematic review and meta-analysis",
          "type": "review",
          "venue": "The Breast",
          "cited_by_count": 69,
          "topics": [
            "Breast Cancer Treatment Studies",
            "Advanced Breast Cancer Therapies",
            "HER2/EGFR in Cancer Research"
          ]
        },
        {
          "openalex_id": "W4384493020",
          "year": 2023,
          "title": "Efficacy and safety of ritlecitinib in adolescents with alopecia areata: Results from the <scp>ALLEGRO</scp> phase 2b/3 randomized, double‐blind, placebo‐controlled trial",
          "type": "article",
          "venue": "Pediatric Dermatology",
          "cited_by_count": 59,
          "topics": [
            "Hair Growth and Disorders",
            "Cytokine Signaling Pathways and Interactions",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W2118848045",
          "year": 2014,
          "title": "Corticosteroids in Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis",
          "type": "article",
          "venue": "Annals of Pharmacotherapy",
          "cited_by_count": 51,
          "topics": [
            "Drug-Induced Adverse Reactions",
            "Contact Dermatitis and Allergies",
            "Urticaria and Related Conditions"
          ]
        },
        {
          "openalex_id": "W3023200119",
          "year": 2016,
          "title": "Association Between Proton Pump Inhibitors and Microscopic Colitis",
          "type": "article",
          "venue": "Annals of Pharmacotherapy",
          "cited_by_count": 49,
          "topics": [
            "Microscopic Colitis",
            "Spondyloarthritis Studies and Treatments",
            "Celiac Disease Research and Management"
          ]
        },
        {
          "openalex_id": "W2900979192",
          "year": 2018,
          "title": "The Shape of the Glucose Response Curve During an Oral Glucose Tolerance Test: Forerunner of Heightened Glycemic Failure Rates and Accelerated Decline in β-Cell Function in TODAY",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 48,
          "topics": [
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes and associated disorders",
            "Adipokines, Inflammation, and Metabolic Diseases"
          ]
        }
      ]
    }
  }
]
