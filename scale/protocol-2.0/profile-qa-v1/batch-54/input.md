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
    "name": "Yifan Ding",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2188-TVG",
        "title": "A travel grant to support the psychometric evaluation and cultural relevance of EQ instruments in China",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5076822287",
      "display_name": "Yifan Ding",
      "orcid": "0009-0006-8112-628X",
      "reported_affiliation": "",
      "works_count": 9,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 4
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 3
        },
        {
          "topic": "Traditional Chinese Medicine Studies",
          "works": 1
        },
        {
          "topic": "Biofield Effects and Biophysics",
          "works": 1
        },
        {
          "topic": "Complementary and Alternative Medicine Studies",
          "works": 1
        },
        {
          "topic": "Cardiovascular Health and Risk Factors",
          "works": 1
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 1
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 1
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 1
        },
        {
          "topic": "Technology Assessment and Management",
          "works": 1
        },
        {
          "topic": "Q Methodology Applications",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Zhuxin Mao",
          "works": 6
        },
        {
          "name": "Zhihao Yang",
          "works": 6
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 5
        },
        {
          "name": "Guangjie Zhang",
          "works": 4
        },
        {
          "name": "Nan Luo",
          "works": 2
        },
        {
          "name": "Yue Sun",
          "works": 2
        },
        {
          "name": "Anle Shen",
          "works": 2
        },
        {
          "name": "Pei Wang",
          "works": 2
        },
        {
          "name": "Z. Samidurai",
          "works": 1
        },
        {
          "name": "Ann Vandeleur",
          "works": 1
        },
        {
          "name": "Darin V. Goss",
          "works": 1
        },
        {
          "name": "Donna Cartwright",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7140243462",
          "year": 2026,
          "title": "Understanding quality of life in China:Cultural influences and measurements challenges when East meets West",
          "type": "dissertation",
          "venue": "EUR Research Repository (Erasmus University Rotterdam)",
          "cited_by_count": 0,
          "topics": [
            "Cultural Differences and Values",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4409110356",
          "year": 2025,
          "title": "Correction to: Evaluating the content validity of the EQ-5D-Y for Chinese children and adolescents",
          "type": "erratum",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Technology Assessment and Management"
          ]
        },
        {
          "openalex_id": "W4414796183",
          "year": 2025,
          "title": "Developing a quality of life framework from the perspective of laypeople: a qualitative comparison with the EQ-HWB framework",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W4415528949",
          "year": 2025,
          "title": "Development and external validation of risk prediction model of non-suicidal self-injury among adolescents with mood disorders",
          "type": "article",
          "venue": "Journal of Psychiatric Research",
          "cited_by_count": 0,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Digital Mental Health Interventions",
            "Personality Disorders and Psychopathology"
          ]
        },
        {
          "openalex_id": "W4407423961",
          "year": 2025,
          "title": "Evaluating the content validity of the EQ-5D-Y for Chinese children and adolescents",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4413354774",
          "year": 2025,
          "title": "Exploring subjective constructions of quality of life in patients, carers and the healthy general public: a Q-methodological study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Q Methodology Applications",
            "Psychological Well-being and Life Satisfaction",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2769591542",
          "year": 2016,
          "title": "Service and quality improvement: 'the million dollar abstract'-improving list utilisation, reducing bed days and delivering a better service to patients can be profitable",
          "type": "conference-paper",
          "venue": "Queensland's institutional digital repository (The University of Queensland)",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4396853968",
          "year": 2024,
          "title": "Differences and common ground in the frameworks of health-related quality of life in traditional Chinese medicine and modern medicine: a systematic review",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 11,
          "topics": [
            "Traditional Chinese Medicine Studies",
            "Biofield Effects and Biophysics",
            "Complementary and Alternative Medicine Studies"
          ]
        },
        {
          "openalex_id": "W4409002196",
          "year": 2025,
          "title": "The EQ-5D and EQ-HWB fit the perceptions of quality of life from a Chinese perspective: a concept mapping study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Cardiovascular Health and Risk Factors"
          ]
        }
      ]
    }
  },
  {
    "name": "Yirga Legesse Niriayo",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2563-RA",
        "title": "Response Shift and Response Scale Heterogeneity in EQ-5D-5L among Patients with Heart Failure ",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5025678242",
      "display_name": "Yirga Legesse Niriayo",
      "orcid": "0000-0002-6943-753X",
      "reported_affiliation": "Mekelle University",
      "works_count": 28,
      "top_topics": [
        {
          "topic": "Medication Adherence and Compliance",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 5
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 5
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 4
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 4
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 4
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 3
        },
        {
          "topic": "Pharmacological Effects and Toxicity Studies",
          "works": 3
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "Nosocomial Infections in ICU",
          "works": 2
        },
        {
          "topic": "Surgical site infection prevention",
          "works": 2
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kidu Gidey",
          "works": 20
        },
        {
          "name": "Solomon Weldegebreal Asgedom",
          "works": 14
        },
        {
          "name": "Gebre Teklemariam Demoz",
          "works": 11
        },
        {
          "name": "Tesfay Mehari Atey",
          "works": 6
        },
        {
          "name": "Shishay Wahdey",
          "works": 5
        },
        {
          "name": "Berhane Yohannes Hailu",
          "works": 4
        },
        {
          "name": "Tesfaye Kassa",
          "works": 4
        },
        {
          "name": "Gebremicheal Gebreslassie Kasahun",
          "works": 3
        },
        {
          "name": "Degena Bahrey",
          "works": 3
        },
        {
          "name": "Kalay Hagazy",
          "works": 3
        },
        {
          "name": "Nigusse Tesfay",
          "works": 3
        },
        {
          "name": "Meles Tekie Gidey",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162291684",
          "year": 2026,
          "title": "Metformin dose up-titration and glycemic control in type 2 diabetes in a resource-limited setting, northern Ethiopia: a retrospective cohort study",
          "type": "article",
          "venue": "BMC Endocrine Disorders",
          "cited_by_count": 0,
          "topics": [
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Treatment and Management",
            "Metabolism, Diabetes, and Cancer"
          ]
        },
        {
          "openalex_id": "W4414751286",
          "year": 2025,
          "title": "Effect of Self‐Care Activities on Blood Pressure Control Among Patients With Hypertension",
          "type": "article",
          "venue": "BioMed Research International",
          "cited_by_count": 2,
          "topics": [
            "Health and Well-being Studies"
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
          "openalex_id": "W4390753002",
          "year": 2024,
          "title": "Antimicrobial Use-Related Problems Among Hospitalized Pediatric Patients: A Prospective Observational Study",
          "type": "article",
          "venue": "Infection and Drug Resistance",
          "cited_by_count": 7,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical studies and practices",
            "Antibiotics Pharmacokinetics and Efficacy"
          ]
        },
        {
          "openalex_id": "W4390863498",
          "year": 2024,
          "title": "Drug therapy problems among hospitalized patients with cardiovascular disease",
          "type": "article",
          "venue": "BMC Cardiovascular Disorders",
          "cited_by_count": 12,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Potassium and Related Disorders",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4392545103",
          "year": 2024,
          "title": "Drug therapy problems and contributing factors among patients with epilepsy",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 4,
          "topics": [
            "Epilepsy research and treatment",
            "Pharmacological Effects and Toxicity Studies",
            "Cancer Research and Treatment"
          ]
        },
        {
          "openalex_id": "W2896656711",
          "year": 2018,
          "title": "Drug therapy problems and contributing factors in the management of heart failure patients in Jimma University Specialized Hospital, Southwest Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 94,
          "topics": [
            "Heart Failure Treatment and Management",
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2799888224",
          "year": 2018,
          "title": "Spending on health and HIV/AIDS: domestic health spending and development assistance in 188 countries, 1995–2015",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 170,
          "topics": [
            "Healthcare Systems and Reforms",
            "HIV/AIDS Impact and Responses",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2900970314",
          "year": 2018,
          "title": "Treatment outcome and associated factors among patients with epilepsy",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 73,
          "topics": [
            "Epilepsy research and treatment",
            "Pharmacological Effects and Toxicity Studies",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W2942174024",
          "year": 2019,
          "title": "Medication Belief and Adherence among Patients with Epilepsy",
          "type": "article",
          "venue": "Behavioural Neurology",
          "cited_by_count": 69,
          "topics": [
            "Epilepsy research and treatment",
            "Medication Adherence and Compliance",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W4321607915",
          "year": 2023,
          "title": "Clinical and economic burden of healthcare-associated infections: A prospective cohort study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 160,
          "topics": [
            "Nosocomial Infections in ICU",
            "Infection Control in Healthcare",
            "Surgical site infection prevention"
          ]
        },
        {
          "openalex_id": "W2943019294",
          "year": 2019,
          "title": "Predictors of poor glycemic control among patients with type 2 diabetes on follow-up care at a tertiary healthcare setting in Ethiopia",
          "type": "article",
          "venue": "BMC Research Notes",
          "cited_by_count": 96,
          "topics": [
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Diabetes Management and Education",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2953649359",
          "year": 2019,
          "title": "Practice and predictors of self-care behaviors among ambulatory patients with hypertension in Ethiopia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 64,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Medication Adherence and Compliance",
            "Sodium Intake and Health"
          ]
        },
        {
          "openalex_id": "W3048320397",
          "year": 2020,
          "title": "&lt;p&gt;Prescribing Pattern of Antibiotics Using WHO Prescribing Indicators Among Inpatients in Ethiopia: A Need for Antibiotic Stewardship Program&lt;/p&gt;",
          "type": "article",
          "venue": "Infection and Drug Resistance",
          "cited_by_count": 53,
          "topics": [
            "Antibiotic Use and Resistance",
            "Antibiotic Resistance in Bacteria",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Yiting Luo",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1867-RA",
        "title": "Assessment of the use of EQ-5D and other generic health-related quality of life measures to evaluate the health outcomes associated with extreme weather events and related climate change impacts: A systematic review",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2036-RA",
        "title": "Exposure and psychological responses to climate change and their association with EQ-5D: a secondary data analysis from the POPCORN study",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2458-RA",
        "title": "Testing EQ-TIPS using latent discrete choice experiments: a mixed-methods study",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5101270824",
      "display_name": "Yiting Luo",
      "orcid": "",
      "reported_affiliation": "Anhui Polytechnic University",
      "works_count": 52,
      "top_topics": [
        {
          "topic": "Advanced biosensing and bioanalysis techniques",
          "works": 7
        },
        {
          "topic": "Extracellular vesicles in disease",
          "works": 5
        },
        {
          "topic": "Advanced Proteomics Techniques and Applications",
          "works": 4
        },
        {
          "topic": "Indoor and Outdoor Localization Technologies",
          "works": 3
        },
        {
          "topic": "Hydrogels: synthesis, properties, applications",
          "works": 3
        },
        {
          "topic": "Glycosylation and Glycoproteins Research",
          "works": 3
        },
        {
          "topic": "Plant Stress Responses and Tolerance",
          "works": 3
        },
        {
          "topic": "Underwater Vehicles and Communication Systems",
          "works": 2
        },
        {
          "topic": "Bone Tissue Engineering Materials",
          "works": 2
        },
        {
          "topic": "Uterine Myomas and Treatments",
          "works": 2
        },
        {
          "topic": "Endometriosis Research and Treatment",
          "works": 2
        },
        {
          "topic": "Gynecological conditions and treatments",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Yinghua Yan",
          "works": 10
        },
        {
          "name": "Chuan‐Fan Ding",
          "works": 9
        },
        {
          "name": "Yunfei Li",
          "works": 5
        },
        {
          "name": "Shaodan Ma",
          "works": 5
        },
        {
          "name": "Bing Wang",
          "works": 5
        },
        {
          "name": "Zheng Shi",
          "works": 4
        },
        {
          "name": "Shan Ding",
          "works": 4
        },
        {
          "name": "Mingxian Liu",
          "works": 4
        },
        {
          "name": "Changren Zhou",
          "works": 4
        },
        {
          "name": "Binghong Luo",
          "works": 4
        },
        {
          "name": "Ruchong Chen",
          "works": 4
        },
        {
          "name": "Xiaoya Zhang",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164170335",
          "year": 2026,
          "title": "Joint Secure Localization and Attack Detection for Vehicular Networks With Quantized Measurements: A Variational Bayesian Approach",
          "type": "article",
          "venue": "IEEE Transactions on Vehicular Technology",
          "cited_by_count": 0,
          "topics": [
            "Vehicular Ad Hoc Networks (VANETs)",
            "Autonomous Vehicle Technology and Safety",
            "Wireless Communication Security Techniques"
          ]
        },
        {
          "openalex_id": "W4406814360",
          "year": 2025,
          "title": "An evaluation of mepolizumab as an add-on maintenance treatment for severe eosinophilic asthma",
          "type": "article",
          "venue": "Expert Opinion on Biological Therapy",
          "cited_by_count": 3,
          "topics": [
            "Asthma and respiratory diseases",
            "Delphi Technique in Research",
            "IL-33, ST2, and ILC Pathways"
          ]
        },
        {
          "openalex_id": "W4417129699",
          "year": 2025,
          "title": "Chiral Lead-Oxyiodide Nonlinear Optical Crystals Constructed on <scp>l</scp> -Malate Groups",
          "type": "article",
          "venue": "Inorganic Chemistry",
          "cited_by_count": 2,
          "topics": [
            "Crystal Structures and Properties",
            "Perovskite Materials and Applications",
            "Nonlinear Optical Materials Research"
          ]
        },
        {
          "openalex_id": "W4411592683",
          "year": 2025,
          "title": "Chitin whisker liquid crystal hydrogel embedded with polyacrylic acid templating osteoid-like Bouligand structure for guiding internal mineralization",
          "type": "article",
          "venue": "Carbohydrate Polymers",
          "cited_by_count": 5,
          "topics": [
            "Hydrogels: synthesis, properties, applications",
            "Bone Tissue Engineering Materials",
            "3D Printing in Biomedical Research"
          ]
        },
        {
          "openalex_id": "W4410818514",
          "year": 2025,
          "title": "Controllable Synthesis of a Strong Ultraviolet Nonlinear Optical Crystal by Tailoring the Lead Oxychloride Polyhedron",
          "type": "article",
          "venue": "Inorganic Chemistry",
          "cited_by_count": 3,
          "topics": [
            "Crystal Structures and Properties",
            "Nonlinear Optical Materials Research",
            "Photorefractive and Nonlinear Optics"
          ]
        },
        {
          "openalex_id": "W4417252112",
          "year": 2025,
          "title": "Cough syncope: a retrospective study of 101 patients",
          "type": "article",
          "venue": "ERJ Open Research",
          "cited_by_count": 1,
          "topics": [
            "Cardiovascular Syncope and Autonomic Disorders",
            "Respiratory and Cough-Related Research",
            "Pathogenesis and Treatment of Hiccups"
          ]
        },
        {
          "openalex_id": "W2392068855",
          "year": 2012,
          "title": "A 3D Position Algorithm Based on Euclidean for Wireless Sensor Networks",
          "type": "article",
          "venue": "Dianzi xuebao",
          "cited_by_count": 0,
          "topics": [
            "Energy Efficient Wireless Sensor Networks",
            "Indoor and Outdoor Localization Technologies"
          ]
        },
        {
          "openalex_id": "W2044903762",
          "year": 2013,
          "title": "Positioning Algorithms by Information Fusion in Wireless Sensor Networks",
          "type": "article",
          "venue": "Wireless Personal Communications",
          "cited_by_count": 6,
          "topics": [
            "Indoor and Outdoor Localization Technologies",
            "Energy Efficient Wireless Sensor Networks",
            "Underwater Vehicles and Communication Systems"
          ]
        },
        {
          "openalex_id": "W2743325989",
          "year": 2016,
          "title": "PCB上に作成した低価格交差指電極による鉛(II)の検出のための新しいインピーダンス測定バイオセンサ【Powered by NICT】",
          "type": "article",
          "venue": "Electroanalysis",
          "cited_by_count": 0,
          "topics": [
            "Military Technology and Strategies",
            "Legal and Regulatory Analysis",
            "Linguistic, Cultural, and Literary Studies"
          ]
        },
        {
          "openalex_id": "W2528624884",
          "year": 2016,
          "title": "The Study on the Attribution of Urbanization Mass Incidents in China's West National Areas - based on the Grounded Theory",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Evaluation Methods in Various Fields"
          ]
        },
        {
          "openalex_id": "W2891018755",
          "year": 2018,
          "title": "Big data analysis adaptation and enterprises’ competitive advantages: the perspective of dynamic capability and resource-based theories",
          "type": "article",
          "venue": "Technology Analysis and Strategic Management",
          "cited_by_count": 172,
          "topics": [
            "Innovation and Knowledge Management",
            "Big Data and Business Intelligence",
            "Economic and Technological Innovation"
          ]
        },
        {
          "openalex_id": "W4293250912",
          "year": 2022,
          "title": "Are We Agreed? Self- Versus Proxy-Reporting of Paediatric Health-Related Quality of Life (HRQoL) Using Generic Preference-Based Measures: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 79,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4393405225",
          "year": 2024,
          "title": "Variational Bayesian Learning Based Localization and Channel Reconstruction in RIS-Aided Systems",
          "type": "article",
          "venue": "IEEE Transactions on Wireless Communications",
          "cited_by_count": 35,
          "topics": [
            "Indoor and Outdoor Localization Technologies",
            "Advanced Wireless Communication Technologies",
            "Underwater Vehicles and Communication Systems"
          ]
        },
        {
          "openalex_id": "W4391650578",
          "year": 2024,
          "title": "Chitin whisker/chitosan liquid crystal hydrogel assisted scaffolds with bone-like ECM microenvironment for bone regeneration",
          "type": "article",
          "venue": "Carbohydrate Polymers",
          "cited_by_count": 32,
          "topics": [
            "Bone Tissue Engineering Materials",
            "Hydrogels: synthesis, properties, applications",
            "Graphene and Nanomaterials Applications"
          ]
        },
        {
          "openalex_id": "W4378953305",
          "year": 2023,
          "title": "Modulating of Bouligand Structure and Chirality Constructed Bionically Based on the Self-Assembly of Chitin Whiskers",
          "type": "article",
          "venue": "Biomacromolecules",
          "cited_by_count": 24,
          "topics": [
            "Liquid Crystal Research Advancements",
            "Pickering emulsions and particle stabilization",
            "Polydiacetylene-based materials and applications"
          ]
        },
        {
          "openalex_id": "W4282973707",
          "year": 2022,
          "title": "Learning Best Combination for Efficient N:M Sparsity",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 23,
          "topics": [
            "Machine Learning and ELM",
            "Domain Adaptation and Few-Shot Learning",
            "Multimodal Machine Learning Applications"
          ]
        },
        {
          "openalex_id": "W4386008185",
          "year": 2023,
          "title": "Mesoporous materials for glycopeptide separation",
          "type": "article",
          "venue": "TrAC Trends in Analytical Chemistry",
          "cited_by_count": 23,
          "topics": [
            "Glycosylation and Glycoproteins Research",
            "Proteoglycans and glycosaminoglycans research",
            "Advanced Proteomics Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W4397293270",
          "year": 2024,
          "title": "Comparing the effects of aquatic-based exercise and land-based exercise on balance in older adults: a systematic review and meta-analysis",
          "type": "review",
          "venue": "European Review of Aging and Physical Activity",
          "cited_by_count": 21,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Scoliosis diagnosis and treatment",
            "Stroke Rehabilitation and Recovery"
          ]
        }
      ]
    }
  },
  {
    "name": "You-Shan Feng",
    "member_affiliation": "Medical University Tübingen, Germany",
    "is_member": true,
    "projects": [
      {
        "project_id": "127-RA",
        "title": "Developing Scoring Methods for the 25-item EQALY Instrument",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1593-RA",
        "title": "Full Title: Population norms and inequalities based on EQ-5D-5L general population surveys (POPS 2)",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1600-RA",
        "title": "Population norms and inequalities based on EQ-5D-5L general population surveys (POPS 2): Pilot on Methodology",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1898-RA",
        "title": "Quantifying Health Inequality: Systematic literature review of the application of EuroQol instruments",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1901-RA",
        "title": "Exploring psychometric properties and scoring approaches for the EQ-5D-5L psoriasis bolt-on: Supporting decisions on its IP status",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1902-RA",
        "title": "Examining the internal structure of the EQ-HWB with a focus on positively and negatively framed items: analysis of three general population datasets",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2200-RA",
        "title": "Which framework of Health-related quality of life best fit the EQ-5D-5L? An exploration of Deep-Dive approaches for developing Dimension Specific Modules (DSMs).",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2312-BT",
        "title": "Content validity of EQ-5D-5L plus Bolt-ons for metastatic urological cancer patients: a qualitative investigation of patients and caregivers",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2373-RA",
        "title": "How “representative” are internet panels for general population health surveys?: a comparison of four UK/England population health surveys using different sampling approaches",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2544-RA",
        "title": "Exploring outcome measure iteming order effects: An evidence synthesis of overall and dimension-specific questions ",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "329-RA",
        "title": "EQ VAS: What does it measure? A structured analysis of the EQ VAS in national population surveys (the Health Survey of England)",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5091571513",
      "display_name": "You‐Shan Feng",
      "orcid": "0000-0003-1509-3409",
      "reported_affiliation": "Universitätsklinikum Tübingen",
      "works_count": 67,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 8
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 3
        },
        {
          "topic": "Breast Implant and Reconstruction",
          "works": 3
        },
        {
          "topic": "Medical Practices and Rehabilitation",
          "works": 3
        },
        {
          "topic": "Pain Management and Placebo Effect",
          "works": 3
        },
        {
          "topic": "Vasculitis and related conditions",
          "works": 3
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Craniofacial Disorders and Treatments",
          "works": 3
        },
        {
          "topic": "Traumatic Brain Injury and Neurovascular Disturbances",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Thomas Kohlmann",
          "works": 24
        },
        {
          "name": "Ines Buchholz",
          "works": 9
        },
        {
          "name": "Peter Rosenberger",
          "works": 7
        },
        {
          "name": "Harry Magunia",
          "works": 7
        },
        {
          "name": "Arne Estler",
          "works": 6
        },
        {
          "name": "Adelana Santos Stahl",
          "works": 6
        },
        {
          "name": "Stéphane Stahl",
          "works": 6
        },
        {
          "name": "Konstantin Nikolaou",
          "works": 5
        },
        {
          "name": "Marius Keller",
          "works": 5
        },
        {
          "name": "Christian Schlensak",
          "works": 5
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 4
        },
        {
          "name": "A. Simon Pickard",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166433823",
          "year": 2026,
          "title": "Comparative performance of EQ-5D-5L bolt-ons in China and the Netherlands: results from the EQ-DAPHNIE project",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ophthalmology and Visual Impairment Studies",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W7162654363",
          "year": 2026,
          "title": "DEPECA-1 (Defeating Penile Cancer 1): A phase II study to evaluate a first-line systemic therapy with enfortumab vedotin plus avelumab for advanced and metastatic penile carcinoma.",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Genital Health and Disease",
            "Bladder and Urothelial Cancer Treatments",
            "Urinary and Genital Oncology Studies"
          ]
        },
        {
          "openalex_id": "W7165649061",
          "year": 2026,
          "title": "Development, Use, and Psychometric Properties of Vision and Hearing Bolt-Ons for EQ-5D-3L and EQ-5D-5L: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Ophthalmology and Visual Impairment Studies",
            "Assistive Technology in Communication and Mobility"
          ]
        },
        {
          "openalex_id": "W7163923881",
          "year": 2026,
          "title": "Socioeconomic inequalities in health-related quality of life during the COVID-19 pandemic: a six-country comparison using the EQ-5D-5 L",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W7160083222",
          "year": 2026,
          "title": "TEG 6s thrombelastography versus conventional coagulation assays in infants and toddlers during craniosynostosis surgery: a prospective observational clinical study",
          "type": "article",
          "venue": "Blood Coagulation & Fibrinolysis",
          "cited_by_count": 0,
          "topics": [
            "Craniofacial Disorders and Treatments",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Vitamin K Research Studies"
          ]
        },
        {
          "openalex_id": "W4409834181",
          "year": 2025,
          "title": "Exploring the origin and conceptual framework of the EQ VAS",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2059214029",
          "year": 2008,
          "title": "Modulation von Ang-2 beeinflusst die Bildung von Endprodukten des Hexosamin Signalweges",
          "type": "article",
          "venue": "Diabetologie und Stoffwechsel",
          "cited_by_count": 0,
          "topics": [
            "Retinal Diseases and Treatments",
            "Advanced Glycation End Products research",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W126380487",
          "year": 2011,
          "title": "Rückenschmerz und Sozialschicht bei Berufstätigen",
          "type": "article",
          "venue": "Der Schmerz",
          "cited_by_count": 25,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Health and Medical Studies",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1972368696",
          "year": 2011,
          "title": "Self-perceived quality of life predicts mortality risk better than a multi-biomarker panel, but the combination of both does best",
          "type": "article",
          "venue": "BMC Medical Research Methodology",
          "cited_by_count": 86,
          "topics": [
            "Health disparities and outcomes",
            "Frailty in Older Adults",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4242975130",
          "year": 2012,
          "title": "Autorinnen und Autoren",
          "type": "book-chapter",
          "venue": "Elsevier eBooks",
          "cited_by_count": 0,
          "topics": [
            "Diverse Scientific and Economic Studies",
            "Human auditory perception and evaluation",
            "Regional Development and Environment"
          ]
        },
        {
          "openalex_id": "W2013564592",
          "year": 2012,
          "title": "Interim Scoring for the EQ-5D-5L: Mapping the EQ-5D-5L to EQ-5D-3L Value Sets",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2231,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W3111512677",
          "year": 2020,
          "title": "Psychometric properties of the EQ-5D-5L: a systematic review of the literature",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 940,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W2119408292",
          "year": 2014,
          "title": "Systematic literature review and validity evaluation of the Expanded Disability Status Scale (EDSS) and the Multiple Sclerosis Functional Composite (MSFC) in patients with multiple sclerosis",
          "type": "review",
          "venue": "BMC Neurology",
          "cited_by_count": 634,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Amyotrophic Lateral Sclerosis Research",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2794316606",
          "year": 2018,
          "title": "A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 375,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W1919258584",
          "year": 2012,
          "title": "Oral anticoagulation use by patients with atrial fibrillation in Germany",
          "type": "article",
          "venue": "Thrombosis and Haemostasis",
          "cited_by_count": 130,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac Arrhythmias and Treatments",
            "Venous Thromboembolism Diagnosis and Management"
          ]
        },
        {
          "openalex_id": "W2124699569",
          "year": 2012,
          "title": "L-Carnitine-supplementation in advanced pancreatic cancer (CARPAN) - a randomized multicentre trial",
          "type": "article",
          "venue": "Nutrition Journal",
          "cited_by_count": 122,
          "topics": [
            "Metabolism and Genetic Disorders",
            "Nutrition and Health in Aging",
            "Clinical Nutrition and Gastroenterology"
          ]
        },
        {
          "openalex_id": "W2035768288",
          "year": 2014,
          "title": "Measuring changes in health over time using the EQ-5D 3L and 5L: a head-to-head comparison of measurement properties and sensitivity to change in a German inpatient rehabilitation sample",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 51,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medical Practices and Rehabilitation",
            "Clinical practice guidelines implementation"
          ]
        }
      ]
    }
  },
  {
    "name": "Zhihao Yang",
    "member_affiliation": "Guizhou Medical University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1485-RA",
        "title": "Content and face validity of the EQ-HWB China and HongKong",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1534-EO",
        "title": "Organizing an EQ-5D-Y workshop in Asia at the ISPOR Asia Pacific Summit 2022 (a virtual event)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1598-RA",
        "title": "Using EQ-5D-Y to measure the health of patients for multiple paediatric health conditions: a project to validate the self-complete, interviewer-administered and proxy administered versions of EQ-5D-Y-3L and EQ-5D-Y-5L in China",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "1941-RA",
        "title": "A VMC research proposal: developing and testing online Cognitive Debriefing interviews: these are ‘necessary’ – but are they ‘feasible’?",
        "working_group": "Others"
      },
      {
        "project_id": "20180070R1",
        "title": "Use EQ‐PVT to develop a cancer patient preferences based EQ‐5D‐5L value set",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180230",
        "title": "A fast-track proposal: write and publish a paper comparing DCE data from 11 Asian EQ-5D-5L valuation studies",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180610",
        "title": "An investigation of constructing EQ-5D-5L value sets by censoring time-trade off data at 0",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190150R1",
        "title": "Exploring non-iterative time trade-off methods for valuation of EQ-5D-5L health states",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190151",
        "title": "extension of 20190150: Exploring non-iterative time trade-off methods for valuation of EQ-5D-5L health states: an on-line experiment",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190370",
        "title": "Compare the TTO and DCE modelling results on individual level",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190900",
        "title": "An investigation of the ‘shrinking factor’ model for predicting vision and cognition bolt-on values elicited from the general public",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "20191020",
        "title": "Estimating an EQ-5D-Y value set for China",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "215-2020RA",
        "title": "Translating the ‘Methods for analysing and reporting EQ-5D data’ into Chinese",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2180-RA",
        "title": "Advancing the Scaling Factor Approach for Bolt-On Valuation: A Research Program for Methodological Development, Model Refinement, and sample size requirement",
        "working_group": "Valuation"
      },
      {
        "project_id": "221-RA",
        "title": "Testing two alternative TTO methods for valuation of EQ-5D-Y health states by trading life years in adulthood",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2225-BT",
        "title": "A study to evaluate the EQ-5D Bolt-on Toolbox cognition items in Parkinson’s disease: content validity and psychometric testing",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2276-RA",
        "title": "Investigating Boundary-Induced non-additivity in cTTO and DCE Valuation Models: A cross-study analysis of ten EQ-5D-5L valuation datasets",
        "working_group": "Valuation"
      },
      {
        "project_id": "2348-BT",
        "title": "Validating the Vision Bolt-on for EQ-5D-5L in three health conditions: Content Validity (Patients, Caregivers, Clinicians) and Quantitative Psychometrics with Responsiveness to Intervention",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "353-RA",
        "title": "Psychometric testing of E-QALY in China: a new study using face-to-face survey method",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "456-RA",
        "title": "Testing the partially-fixed model for bolt-on valuation: a multi-country study",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "75-EO",
        "title": "Presenting E-QALY study results in 2020 ISOQOL",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "92-2020RA",
        "title": "Investigating the effect of interaction terms in modelling EQ-5D value set and its impact on sample size requirements using three VAS saturated data",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5028809099",
      "display_name": "Zhihao Yang",
      "orcid": "0000-0001-5468-0847",
      "reported_affiliation": "Guiyang Medical University",
      "works_count": 108,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 71
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 16
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 9
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 8
        },
        {
          "topic": "Hydrocarbon exploration and reservoir analysis",
          "works": 7
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 6
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 6
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 6
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 6
        },
        {
          "topic": "Global Health Care Issues",
          "works": 6
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 5
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 50
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 30
        },
        {
          "name": "Zhuxin Mao",
          "works": 14
        },
        {
          "name": "Pei Wang",
          "works": 13
        },
        {
          "name": "Elly Stolk",
          "works": 9
        },
        {
          "name": "Bin Wu",
          "works": 8
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 8
        },
        {
          "name": "Wenjing Zhou",
          "works": 8
        },
        {
          "name": "Michael Herdman",
          "works": 8
        },
        {
          "name": "Brendan Mulhern",
          "works": 7
        },
        {
          "name": "Guangjie Zhang",
          "works": 7
        },
        {
          "name": "Tessa Peasgood",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167238360",
          "year": 2026,
          "title": "A pre-illness reference reminder alters cross-sectional patient-reported outcome responses: evidence from EQ-5D-5L and EQ-HWB-9",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4416190694",
          "year": 2026,
          "title": "Improving the accuracy and generalizability of molecular property regression models with a substructure-substitution-rule-informed framework",
          "type": "article",
          "venue": "Chemical Science",
          "cited_by_count": 0,
          "topics": [
            "Computational Drug Discovery Methods",
            "Machine Learning in Materials Science",
            "Machine Learning in Bioinformatics"
          ]
        },
        {
          "openalex_id": "W7167257919",
          "year": 2026,
          "title": "Marine heatwaves drive phytoplankton community shifts and chlorophyll a decline in the Bay of Bengal",
          "type": "article",
          "venue": "Acta Oceanologica Sinica",
          "cited_by_count": 0,
          "topics": [
            "Marine and coastal ecosystems",
            "Oceanographic and Atmospheric Processes",
            "Marine Invertebrate Physiology and Ecology"
          ]
        },
        {
          "openalex_id": "W7166157577",
          "year": 2026,
          "title": "PCR206 RESPONSE OPTION INTERPRETATION TO INFORM PRO MEASURE DESIGNS: A MULTINATIONAL STUDY",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Molecular Biology Techniques and Applications",
            "Optimal Experimental Design Methods",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W7154101748",
          "year": 2026,
          "title": "Spatiotemporal patterns of phytoplankton communities in coastal waters near the Taishan Nuclear Power Plant",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Marine and coastal ecosystems",
            "Radioactive contamination and transfer",
            "Marine and Coastal Research"
          ]
        },
        {
          "openalex_id": "W7166663308",
          "year": 2026,
          "title": "Spatiotemporal patterns of phytoplankton communities in coastal waters near the Taishan Nuclear Power Plant",
          "type": "article",
          "venue": "Marine Environmental Research",
          "cited_by_count": 0,
          "topics": [
            "Radioactive contamination and transfer",
            "Marine and coastal ecosystems",
            "Aquatic Ecosystems and Phytoplankton Dynamics"
          ]
        },
        {
          "openalex_id": "W2370161606",
          "year": 2010,
          "title": "Numerical simmlation for dynamic response of a T-shape pipe and fluid inside",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Geotechnical Engineering and Underground Structures",
            "Soil, Finite Element Methods",
            "Water Systems and Optimization"
          ]
        },
        {
          "openalex_id": "W2049953842",
          "year": 2013,
          "title": "A drainage data-based calculation method for coalbed permeability",
          "type": "article",
          "venue": "Journal of Geophysics and Engineering",
          "cited_by_count": 11,
          "topics": [
            "Coal Properties and Utilization",
            "Hydrocarbon exploration and reservoir analysis",
            "Hydraulic Fracturing and Reservoir Analysis"
          ]
        },
        {
          "openalex_id": "W2064297571",
          "year": 2013,
          "title": "Seismic analysis of a long tunnel based on multi-scale method",
          "type": "article",
          "venue": "Engineering Structures",
          "cited_by_count": 150,
          "topics": [
            "Geotechnical Engineering and Underground Structures",
            "Seismic Waves and Analysis",
            "Dam Engineering and Safety"
          ]
        },
        {
          "openalex_id": "W1970867597",
          "year": 2014,
          "title": "Combined equivalent &amp; multi-scale simulation method for 3-D seismic analysis of large-scale shield tunnel",
          "type": "article",
          "venue": "Engineering Computations",
          "cited_by_count": 24,
          "topics": [
            "Geotechnical Engineering and Underground Structures",
            "Geotechnical Engineering and Analysis",
            "Tunneling and Rock Mechanics"
          ]
        },
        {
          "openalex_id": "W2900226942",
          "year": 2018,
          "title": "EQ-5D-5L norms for the urban Chinese population in China",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 204,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Efficiency Analysis Using DEA"
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
          "openalex_id": "W4309264997",
          "year": 2022,
          "title": "Estimating an EQ-5D-Y-3L Value Set for China",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 65,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3217165750",
          "year": 2021,
          "title": "The remarkably frequent use of EQ-5D in non-economic research",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W3217092198",
          "year": 2021,
          "title": "Developing the EQ-5D-5L Value Set for Uganda Using the ‘Lite’ Protocol",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2760270932",
          "year": 2017,
          "title": "Logical inconsistencies in time trade-off valuation of EQ-5D-5L health states: Whose fault is it?",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 44,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  }
]
