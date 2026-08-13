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
    "name": "Martin Härter",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1719-RA",
        "title": "Psychometric performance of an EXtended version of the EQ-5D-5L in a cohort of German health care workers with AND without late consequences of SARS-CoV-2 infection (EXPAND)",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5048738092",
      "display_name": "Martin Härter",
      "orcid": "0000-0001-7443-9890",
      "reported_affiliation": "Universität Hamburg",
      "works_count": 856,
      "top_topics": [
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 142
        },
        {
          "topic": "Psychiatric care and mental health services",
          "works": 135
        },
        {
          "topic": "Health and Medical Studies",
          "works": 135
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 125
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 75
        },
        {
          "topic": "Treatment of Major Depression",
          "works": 74
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 62
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 59
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 49
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 47
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 45
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 41
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Levente Kriston",
          "works": 175
        },
        {
          "name": "Jörg Dirmaier",
          "works": 91
        },
        {
          "name": "Isabelle Scholl",
          "works": 78
        },
        {
          "name": "Holger Schulz",
          "works": 59
        },
        {
          "name": "Thomas Berger",
          "works": 59
        },
        {
          "name": "Karl Wegscheider",
          "works": 54
        },
        {
          "name": "Anja Mehnert",
          "works": 51
        },
        {
          "name": "Katrin Reuter",
          "works": 47
        },
        {
          "name": "Isaac Bermejo",
          "works": 44
        },
        {
          "name": "Frank Schneider",
          "works": 43
        },
        {
          "name": "Lars P. Hölzel",
          "works": 42
        },
        {
          "name": "Sarah Liebherz",
          "works": 42
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4404059511",
          "year": 2026,
          "title": "Development of a Patient‐Centered Communication Skills Training: A Qualitative Exploration of Nurse Managers' Perspectives",
          "type": "article",
          "venue": "Nursing Open",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Interprofessional Education and Collaboration",
            "Family and Patient Care in Intensive Care Units"
          ]
        },
        {
          "openalex_id": "W7165031798",
          "year": 2026,
          "title": "Measurement Properties of the 9-Item Shared Decision Making Questionnaire (SDM-Q-9)",
          "type": "article",
          "venue": "European Journal of Psychological Assessment",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare",
            "Attachment and Relationship Dynamics"
          ]
        },
        {
          "openalex_id": "W7160606392",
          "year": 2026,
          "title": "Perspektiven, Handlungsstrategien und Lösungsansätze für eine klimaresiliente und treibhausgasarme Gesundheitsversorgung",
          "type": "article",
          "venue": "Das Gesundheitswesen",
          "cited_by_count": 0,
          "topics": [
            "Climate Change and Health Impacts",
            "Climate Change and Sustainable Development",
            "Zoonotic diseases and public health"
          ]
        },
        {
          "openalex_id": "W7164579004",
          "year": 2026,
          "title": "Updated International Patient Decision Aid Standards (IPDAS version 5.0): modified Delphi, evidence informed consensus process",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W4411850009",
          "year": 2025,
          "title": "A qualitative interview study on psycho-oncologists’ experiences with patient deaths in Germany",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 4,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Grief, Bereavement, and Mental Health",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W4414124487",
          "year": 2025,
          "title": "Affective disorders—developments of ICD-11 in comparison with ICD-10",
          "type": "article",
          "venue": "Der Nervenarzt",
          "cited_by_count": 0,
          "topics": [
            "Mental Health and Psychiatry",
            "Personality Disorders and Psychopathology"
          ]
        },
        {
          "openalex_id": "W2403124883",
          "year": 1965,
          "title": "[2 CASES OF NESIDIOBLASTOMA OF THE PANCREAS. CLINICAL, BIOLOGICAL AND ANATOMICAL STUDY].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Tumors and Oncological Cases",
            "Oral and Maxillofacial Pathology",
            "Sarcoma Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2434344780",
          "year": 1965,
          "title": "[2 CASES OF PANCREATIC NESIDIOBLASTOMAS. CLINICAL, BIOLOGICAL AND ANATOMIC STUDY].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Oral and Maxillofacial Pathology",
            "Tumors and Oncological Cases",
            "Head and Neck Surgical Oncology"
          ]
        },
        {
          "openalex_id": "W228089839",
          "year": 1966,
          "title": "[Critical study of the clinical results of implantations of radioactive isotopes in the pituitary in certain endocrine or cancerous diseases (62 cases)].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Radiation Dose and Imaging",
            "Radiopharmaceutical Chemistry and Applications",
            "Medical Imaging Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2439458516",
          "year": 1966,
          "title": "[Intersititial hypophyseal irradiation in malignant edematous exophthalmia].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Ocular Oncology and Treatments"
          ]
        },
        {
          "openalex_id": "W2767867182",
          "year": 2017,
          "title": "A three-talk model for shared decision making: multistage consultation process",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 1031,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Healthcare Systems and Technology",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2004111414",
          "year": 2009,
          "title": "The 9-item Shared Decision Making Questionnaire (SDM-Q-9). Development and psychometric properties in a primary care sample",
          "type": "article",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 939,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2883003988",
          "year": 2018,
          "title": "Social support in the general population: standardization of the Oslo social support scale (OSSS-3)",
          "type": "article",
          "venue": "BMC Psychology",
          "cited_by_count": 808,
          "topics": [
            "Health disparities and outcomes",
            "Health Promotion and Cardiovascular Prevention",
            "Cardiac Health and Mental Health"
          ]
        },
        {
          "openalex_id": "W2079906298",
          "year": 2014,
          "title": "An Integrative Model of Patient-Centeredness – A Systematic Review and Concept Analysis",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 792,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W3000661394",
          "year": 2020,
          "title": "Sensitivity to change and minimal clinically important difference of the 7-item Generalized Anxiety Disorder Questionnaire (GAD-7)",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 649,
          "topics": [
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Treatment of Major Depression",
            "Personality Disorders and Psychopathology"
          ]
        },
        {
          "openalex_id": "W2115395024",
          "year": 2014,
          "title": "Four-Week Prevalence of Mental Disorders in Patients With Cancer Across Major Tumor Entities",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 645,
          "topics": [
            "Cancer survivorship and care",
            "Cancer-related cognitive impairment studies",
            "Tryptophan and brain disorders"
          ]
        },
        {
          "openalex_id": "W2619881061",
          "year": 2017,
          "title": "One in two cancer patients is significantly distressed: Prevalence and indicators of distress",
          "type": "article",
          "venue": "Psycho-Oncology",
          "cited_by_count": 634,
          "topics": [
            "Cancer survivorship and care",
            "Pain Management and Opioid Use",
            "Nausea and vomiting management"
          ]
        },
        {
          "openalex_id": "W2126194308",
          "year": 2010,
          "title": "Reboxetine for acute treatment of major depression: systematic review and meta-analysis of published and unpublished placebo and selective serotonin reuptake inhibitor controlled trials",
          "type": "review",
          "venue": "BMJ",
          "cited_by_count": 593,
          "topics": [
            "Treatment of Major Depression",
            "Meta-analysis and systematic reviews",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes"
          ]
        }
      ]
    }
  },
  {
    "name": "Martine Hoogendoorn",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20190850",
        "title": "Validation of the EQ-5D plus respiratory bolt-on in the birmingham copd cohort study",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2339-BT",
        "title": "Validation of the breathing bolt-on for the EQ-5D-5L in patients with pulmonary fibrosis and patients with an acute COPD exacerbation",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033706754",
      "display_name": "Martine Hoogendoorn",
      "orcid": "0000-0002-7122-9780",
      "reported_affiliation": "Erasmus MC",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 43
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 20
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 12
        },
        {
          "topic": "Respiratory Support and Mechanisms",
          "works": 8
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 6
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 5
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 5
        },
        {
          "topic": "Respiratory and Cough-Related Research",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Dutch Social and Cultural Studies",
          "works": 4
        },
        {
          "topic": "Emergency and Acute Care Studies",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maureen Rutten‐van Mölken",
          "works": 54
        },
        {
          "name": "Talitha Feenstra",
          "works": 24
        },
        {
          "name": "Rudolf T. Hoogenveen",
          "works": 13
        },
        {
          "name": "Maiwenn Al",
          "works": 13
        },
        {
          "name": "Isaac Corro Ramos",
          "works": 11
        },
        {
          "name": "Penny Whiting",
          "works": 9
        },
        {
          "name": "Laura Burgers",
          "works": 9
        },
        {
          "name": "Steve Ryder",
          "works": 9
        },
        {
          "name": "Nigel Armstrong",
          "works": 9
        },
        {
          "name": "Alex Allen",
          "works": 9
        },
        {
          "name": "Hans Severens",
          "works": 9
        },
        {
          "name": "Jos Kleijnen",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164860903",
          "year": 2026,
          "title": "Preference-based scoring algorithm to estimate societal utilities based on the patient-reported experience of cognitive impairment in schizophrenia (PRECIS) instrument",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Schizophrenia research and treatment",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4410271161",
          "year": 2025,
          "title": "The Cost Impact of Informal Care for Patients With COPD and Exacerbations in the Netherlands",
          "type": "conference-abstract",
          "venue": "American Journal of Respiratory and Critical Care Medicine",
          "cited_by_count": 0,
          "topics": [
            "Chronic Disease Management Strategies",
            "Health, psychology, and well-being",
            "Interprofessional Education and Collaboration"
          ]
        },
        {
          "openalex_id": "W4377939059",
          "year": 2023,
          "title": "The lifetime health and economic burden of obesity in five European countries: what is the potential impact of prevention?",
          "type": "article",
          "venue": "Diabetes Obesity and Metabolism",
          "cited_by_count": 24,
          "topics": [
            "Obesity and Health Practices",
            "Obesity, Physical Activity, Diet",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3187797177",
          "year": 2021,
          "title": "Cost-effectiveness of the fixed-dose combination tiotropium/olodaterol versus tiotropium monotherapy or a fixed-dose combination of long-acting β2-agonist/inhaled corticosteroid for COPD in Finland, Sweden and the Netherlands: a model-based study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 9,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Asthma and respiratory diseases",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W3192813625",
          "year": 2021,
          "title": "Performance of the EQ-5D-5L Plus Respiratory Bolt-On in the Birmingham Chronic Obstructive Pulmonary Disease Cohort Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 18,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cystic Fibrosis Research Advances"
          ]
        },
        {
          "openalex_id": "W3040328066",
          "year": 2020,
          "title": "How to Address Uncertainty in Health Economic Discrete-Event Simulation Models: An Illustration for Chronic Obstructive Pulmonary Disease",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 18,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2980628694",
          "year": 1990,
          "title": "Vereenvoudigingen en verduidelijkingen van het jaarrekeningenrecht Accountantscontrole en rechtmatigheid bij de rijksoverheid",
          "type": "article",
          "venue": "Maandblad Voor Accountancy en Bedrijfseconomie",
          "cited_by_count": 0,
          "topics": [
            "Comparative and International Law Studies",
            "Legal and Social Philosophy",
            "Taxation and Legal Issues"
          ]
        },
        {
          "openalex_id": "W2980767901",
          "year": 1995,
          "title": "Derogatie: afwijking van wettelijke bepalingen ten behoeve van het inzicht",
          "type": "article",
          "venue": "Maandblad Voor Accountancy en Bedrijfseconomie",
          "cited_by_count": 1,
          "topics": [
            "Comparative and International Law Studies",
            "Criminal Law and Evidence",
            "Dutch Social and Cultural Studies"
          ]
        },
        {
          "openalex_id": "W1573598242",
          "year": 1995,
          "title": "Hedendaags accounting-onderzoek",
          "type": "article",
          "venue": "UvA-DARE (University of Amsterdam)",
          "cited_by_count": 0,
          "topics": [
            "Hermeneutics and Narrative Identity",
            "Aging, Elder Care, and Social Issues",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W2980407406",
          "year": 1995,
          "title": "Nawoord bij reacties Beekman en Damen",
          "type": "article",
          "venue": "Maandblad Voor Accountancy en Bedrijfseconomie",
          "cited_by_count": 1,
          "topics": [
            "Dutch Social and Cultural Studies",
            "Psychological Treatments and Assessments",
            "Counseling, Therapy, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W2152912650",
          "year": 2013,
          "title": "An Official American Thoracic Society/European Respiratory Society Statement: Key Concepts and Advances in Pulmonary Rehabilitation",
          "type": "article",
          "venue": "American Journal of Respiratory and Critical Care Medicine",
          "cited_by_count": 3878,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Delphi Technique in Research",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2103258141",
          "year": 2010,
          "title": "Case fatality of COPD exacerbations: a meta-analysis and statistical modelling approach",
          "type": "review",
          "venue": "European Respiratory Journal",
          "cited_by_count": 228,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory Support and Mechanisms",
            "Emergency and Acute Care Studies"
          ]
        },
        {
          "openalex_id": "W2113638497",
          "year": 2009,
          "title": "Short- and long-term efficacy of a community-based COPD management programme in less advanced COPD: a randomised controlled trial",
          "type": "article",
          "venue": "Thorax",
          "cited_by_count": 186,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Delphi Technique in Research",
            "Philosophy, Health, and Society"
          ]
        },
        {
          "openalex_id": "W2122787559",
          "year": 2010,
          "title": "Long-term effectiveness and cost-effectiveness of smoking cessation interventions in patients with COPD",
          "type": "article",
          "venue": "Thorax",
          "cited_by_count": 139,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Smoking Behavior and Cessation",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W1996959689",
          "year": 2010,
          "title": "Efficacy and Costs of Nutritional Rehabilitation in Muscle-Wasted Patients With Chronic Obstructive Pulmonary Disease in a Community-Based Setting: A Prespecified Subgroup Analysis of the INTERCOM Trial",
          "type": "article",
          "venue": "Journal of the American Medical Directors Association",
          "cited_by_count": 133,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Cardiovascular and exercise physiology",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W1982684708",
          "year": 2005,
          "title": "A dynamic population model of disease progression in COPD",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 127,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Health Promotion and Cardiovascular Prevention",
            "Emergency and Acute Care Studies"
          ]
        },
        {
          "openalex_id": "W2120298704",
          "year": 2010,
          "title": "Association between lung function and exacerbation frequency in patients with COPD",
          "type": "article",
          "venue": "International Journal of COPD",
          "cited_by_count": 99,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Delphi Technique in Research",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W1973960158",
          "year": 2014,
          "title": "Ivacaftor for the treatment of patients with cystic fibrosis and the G551D mutation: a systematic review and cost-effectiveness analysis",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 98,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Hemophilia Treatment and Research",
            "Immunodeficiency and Autoimmune Disorders"
          ]
        }
      ]
    }
  },
  {
    "name": "Marufa Sultana",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1646-RA",
        "title": "Building the health-related quality of life evidence for Bangladesh’s children: piloting EQ-5D-Y Bangla version instrument for Bangladesh",
        "working_group": "Youth"
      },
      {
        "project_id": "2106-RA",
        "title": "Translation, Cultural Adaptation, and Validation of EQ-TIPS for Bangladeshi Infant and Toddler Populations",
        "working_group": "Youth"
      },
      {
        "project_id": "2417-RA",
        "title": "Health-Related Quality of Life in Bangladeshi Children and Adolescents: Population reference data and Comparison of EQ-5D-Y-3L Value Sets",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5035318354",
      "display_name": "Marufa Sultana",
      "orcid": "0000-0003-2475-6497",
      "reported_affiliation": "Deakin University",
      "works_count": 107,
      "top_topics": [
        {
          "topic": "Global Maternal and Child Health",
          "works": 40
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 28
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 25
        },
        {
          "topic": "Global Health Care Issues",
          "works": 15
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 8
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 7
        },
        {
          "topic": "Global Health and Epidemiology",
          "works": 6
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 6
        },
        {
          "topic": "Child Nutrition and Feeding Issues",
          "works": 6
        },
        {
          "topic": "Pneumonia and Respiratory Infections",
          "works": 6
        },
        {
          "topic": "Viral gastroenteritis research and epidemiology",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Abdur Razzaque Sarker",
          "works": 54
        },
        {
          "name": "Rashidul Alam Mahumud",
          "works": 44
        },
        {
          "name": "Jahangir Khan",
          "works": 25
        },
        {
          "name": "Nausad Ali",
          "works": 25
        },
        {
          "name": "Nurnabi Sheikh",
          "works": 20
        },
        {
          "name": "Sayem Ahmed",
          "works": 18
        },
        {
          "name": "Raisul Akram",
          "works": 18
        },
        {
          "name": "Alec Morton",
          "works": 16
        },
        {
          "name": "Zia Ul Islam",
          "works": 15
        },
        {
          "name": "Khorshed Alam",
          "works": 13
        },
        {
          "name": "Vicki Brown",
          "works": 12
        },
        {
          "name": "Tahmeed Ahmed",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160847705",
          "year": 2026,
          "title": "Co‐Benefits of Nutrition Interventions: A Systematic Review",
          "type": "review",
          "venue": "Obesity Reviews",
          "cited_by_count": 0,
          "topics": [
            "Child Nutrition and Water Access",
            "Agriculture Sustainability and Environmental Impact",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W7164151809",
          "year": 2026,
          "title": "Refeeding Syndrome Complicated by Wernicke’s Encephalopathy Following Severe Hyperemesis Gravidarum and Medical Management of Miscarriage: A Case Report",
          "type": "article",
          "venue": "Cureus",
          "cited_by_count": 0,
          "topics": [
            "Alcoholism and Thiamine Deficiency",
            "Folate and B Vitamins Research",
            "Prenatal Substance Exposure Effects"
          ]
        },
        {
          "openalex_id": "W4415100392",
          "year": 2025,
          "title": "Effects of Integrated Nutrient Management on the Growth Performance of Beetroot &lt;i&gt;(Beta vulgaris &lt;/i&gt;L.) under Acidic Soil Conditions in Smallholder Farmer Fields",
          "type": "article",
          "venue": "Jurnal Biota",
          "cited_by_count": 0,
          "topics": [
            "Botanical Research and Applications",
            "Plant Physiology and Cultivation Studies",
            "Plant Growth Enhancement Techniques"
          ]
        },
        {
          "openalex_id": "W4410555609",
          "year": 2025,
          "title": "How Is Scale Incorporated Into the Economic Evaluation of Interventions to Prevent Obesity or to Improve Obesity‐Related Risk Factors: A Systematic Scoping Review",
          "type": "article",
          "venue": "Obesity Reviews",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4408343366",
          "year": 2025,
          "title": "Incidence, healthcare-seeking behavior and barriers associated with seeking care for severe childhood pneumonia in rural Bangladesh: A prospective study",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Global Maternal and Child Health",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W4412834321",
          "year": 2025,
          "title": "Investigating the effect of herbal component-based natural hair oil using the Indigenous source of Bangladesh",
          "type": "article",
          "venue": "South African Journal of Botany",
          "cited_by_count": 0,
          "topics": [
            "Phytochemistry and biological activity of medicinal plants",
            "Hops Chemistry and Applications",
            "Ginger and Zingiberaceae research"
          ]
        },
        {
          "openalex_id": "W2334691526",
          "year": 2009,
          "title": "Determinants of Malnutrition among the Children under 2 Years of Age",
          "type": "article",
          "venue": "Pakistan Journal of Nutrition",
          "cited_by_count": 4,
          "topics": [
            "Child Nutrition and Water Access",
            "Nutrition and Health in Aging",
            "Child Nutrition and Feeding Issues"
          ]
        },
        {
          "openalex_id": "W2080121377",
          "year": 2014,
          "title": "Herbal Healing: An Old Practice for Healthy Living among Khumi, Marma and Tripura Communities of Thanchi Upazila, Bangladesh",
          "type": "article",
          "venue": "European Journal of Medicinal Plants",
          "cited_by_count": 17,
          "topics": [
            "Ethnobotanical and Medicinal Plants Studies",
            "Fisheries and Aquaculture Studies",
            "Agricultural Economics and Practices"
          ]
        },
        {
          "openalex_id": "W2127406033",
          "year": 2014,
          "title": "The impact of age and sex on healthcare expenditure of households in Bangladesh",
          "type": "article",
          "venue": "SpringerPlus",
          "cited_by_count": 41,
          "topics": [
            "Global Health Care Issues",
            "Global Maternal and Child Health",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2529375427",
          "year": 2016,
          "title": "Benefit incidence analysis of healthcare in Bangladesh – equity matters for universal health coverage",
          "type": "article",
          "venue": "Health Policy and Planning",
          "cited_by_count": 43,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2563153563",
          "year": 2016,
          "title": "Distribution and Determinants of Low Birth Weight in Developing Countries",
          "type": "article",
          "venue": "Journal of Preventive Medicine and Public Health",
          "cited_by_count": 277,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare"
          ]
        },
        {
          "openalex_id": "W2271241286",
          "year": 2016,
          "title": "Willingness-to-Pay for Community-Based Health Insurance among Informal Workers in Urban Bangladesh",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 152,
          "topics": [
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2582910874",
          "year": 2016,
          "title": "Prevalence and Health Care–Seeking Behavior for Childhood Diarrheal Disease in Bangladesh",
          "type": "article",
          "venue": "Global Pediatric Health",
          "cited_by_count": 127,
          "topics": [
            "Child Nutrition and Water Access",
            "Global Maternal and Child Health",
            "Food Security and Health in Diverse Populations"
          ]
        },
        {
          "openalex_id": "W2752075573",
          "year": 2017,
          "title": "Prevalence and associated determinants of malaria parasites among Kenyan children",
          "type": "article",
          "venue": "Tropical Medicine and Health",
          "cited_by_count": 120,
          "topics": [
            "Malaria Research and Control",
            "Mosquito-borne diseases and control",
            "Statistical Methods in Epidemiology"
          ]
        },
        {
          "openalex_id": "W2910457294",
          "year": 2019,
          "title": "Prevalence, determinants and health care-seeking behavior of childhood acute respiratory tract infections in Bangladesh",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 120,
          "topics": [
            "Pediatric health and respiratory diseases",
            "Antibiotic Use and Resistance",
            "Respiratory viral infections research"
          ]
        },
        {
          "openalex_id": "W2598319394",
          "year": 2017,
          "title": "Distribution and Determinants of Out-of-pocket Healthcare Expenditures in Bangladesh",
          "type": "article",
          "venue": "Journal of Preventive Medicine and Public Health",
          "cited_by_count": 90,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2810820839",
          "year": 2018,
          "title": "Coverage, Timelines, and Determinants of Incomplete Immunization in Bangladesh",
          "type": "article",
          "venue": "Tropical Medicine and Infectious Disease",
          "cited_by_count": 89,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Immune responses and vaccinations",
            "Virology and Viral Diseases"
          ]
        },
        {
          "openalex_id": "W2781897851",
          "year": 2018,
          "title": "Economic costs of hospitalized diarrheal disease in Bangladesh: a societal perspective",
          "type": "article",
          "venue": "Global Health Research and Policy",
          "cited_by_count": 87,
          "topics": [
            "Child Nutrition and Water Access",
            "Viral gastroenteritis research and epidemiology",
            "Global Health and Epidemiology"
          ]
        }
      ]
    }
  },
  {
    "name": "María Belizán",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1885-RA",
        "title": "Development of Argentinean Spanish Mock-up Versions of the Experimental and Modified EQ-HWB and EQ-HWB-S Instruments",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2412-BT",
        "title": "Content Validity of the EQ-5D Bolt-On Toolbox: Hearing, Vision, and Respiratory Bolt-Ons in Patients in Argentina",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2589-RA",
        "title": "Assessing the Relevance of EQ-TIPS Compared with EQ-5D-Y in Children Aged 4–6 Years with Severe Health Conditions in Argentina: A Qualitative Study with Primary Caregivers",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5058351382",
      "display_name": "María Belizán",
      "orcid": "0000-0002-8739-5249",
      "reported_affiliation": "Instituto de Efectividad Clínica y Sanitaria",
      "works_count": 100,
      "top_topics": [
        {
          "topic": "Global Maternal and Child Health",
          "works": 23
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 14
        },
        {
          "topic": "Maternal and Perinatal Health Interventions",
          "works": 10
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 9
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 9
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 8
        },
        {
          "topic": "Mosquito-borne diseases and control",
          "works": 8
        },
        {
          "topic": "Maternal and Neonatal Healthcare",
          "works": 6
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 6
        },
        {
          "topic": "COVID-19 Impact on Reproduction",
          "works": 5
        },
        {
          "topic": "Colorectal Cancer Screening and Detection",
          "works": 5
        },
        {
          "topic": "Reliability and Agreement in Measurement",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Juan Pedro Alonso",
          "works": 30
        },
        {
          "name": "Ariel Bardach",
          "works": 20
        },
        {
          "name": "Mabel Berrueta",
          "works": 19
        },
        {
          "name": "Federico Augustovski",
          "works": 18
        },
        {
          "name": "Luz Gibbons",
          "works": 17
        },
        {
          "name": "Verónica Pingray",
          "works": 14
        },
        {
          "name": "Karen Klein",
          "works": 13
        },
        {
          "name": "Fernando Althabe",
          "works": 12
        },
        {
          "name": "Javier Roberti",
          "works": 12
        },
        {
          "name": "Mariana Comolli",
          "works": 12
        },
        {
          "name": "María Luisa Cafferata",
          "works": 11
        },
        {
          "name": "Agustina Mazzoni",
          "works": 11
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167275189",
          "year": 2026,
          "title": "Content validity of the modified EQ-HWB-9 in a sample of Argentinean patients, informal caregivers, and members of the general public",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4406411832",
          "year": 2025,
          "title": "A core outcome set for maternal and neonatal health research and surveillance of emerging and ongoing epidemic threats (MNH-EPI-COS): a modified Delphi-based international consensus",
          "type": "article",
          "venue": "EClinicalMedicine",
          "cited_by_count": 8,
          "topics": [
            "Delphi Technique in Research",
            "Reliability and Agreement in Measurement",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W7126318826",
          "year": 2025,
          "title": "A core outcome set for maternal and neonatal health research and surveillance of emerging and ongoing epidemic threats (MNH-EPI-COS): a modified Delphi-based international consensus",
          "type": "article",
          "venue": "Conicet",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "Reliability and Agreement in Measurement",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W4409075284",
          "year": 2025,
          "title": "Acceptability and perceived barriers to adoption of the core outcome set for maternal and neonatal health research and surveillance during emerging and ongoing epidemic threats (MNH-EPI-COS). An online survey",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4416664417",
          "year": 2025,
          "title": "Acceptability and perceived barriers to adoption of the core outcome set for maternal and neonatal health research and surveillance during emerging and ongoing epidemic threats (MNH-EPI-COS): An online survey",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "Health, Environment, Cognitive Aging",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W4412094588",
          "year": 2025,
          "title": "Conceptual Mapping of Health-Related Quality of Life, Quality of Life, and Wellbeing: A Systematic Review and Assessment of Commonly Used Patient-Reported Outcomes Measures",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W633933515",
          "year": 2000,
          "title": "Costs of Antenatal and related care in Argentina: A cost-minimisation analysis of the new WHO Antenatal Care Package",
          "type": "article",
          "venue": "",
          "cited_by_count": 3,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2276562737",
          "year": 2003,
          "title": "Child survival [letter]",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 0,
          "topics": [
            "Health and Conflict Studies"
          ]
        },
        {
          "openalex_id": "W2142380882",
          "year": 2003,
          "title": "Costs of publicly provided maternity services in Rosario, Argentina",
          "type": "article",
          "venue": "Salud Pública de México",
          "cited_by_count": 35,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare",
            "Maternal and Perinatal Health Interventions"
          ]
        },
        {
          "openalex_id": "W7126290360",
          "year": 2003,
          "title": "Costs of publicly provided maternity services in Rosario, Argentina",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Global Maternal and Child Health",
            "Poverty, Education, and Child Welfare",
            "Gender, Labor, and Family Dynamics"
          ]
        },
        {
          "openalex_id": "W2145817447",
          "year": 2011,
          "title": "Stillbirths: how can health systems deliver for mothers and babies?",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 216,
          "topics": [
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access",
            "Maternal and Neonatal Healthcare"
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
          "openalex_id": "W2110446304",
          "year": 2015,
          "title": "Barriers to providing quality emergency obstetric care in Addis Ababa, Ethiopia: Healthcare providers’ perspectives on training, referrals and supervision, a mixed methods study",
          "type": "article",
          "venue": "BMC Pregnancy and Childbirth",
          "cited_by_count": 116,
          "topics": [
            "Global Maternal and Child Health",
            "Trauma and Emergency Care Studies",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W2137668314",
          "year": 2015,
          "title": "Challenges and opportunities for implementing evidence-based antenatal care in Mozambique: a qualitative study",
          "type": "article",
          "venue": "BMC Pregnancy and Childbirth",
          "cited_by_count": 81,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and Perinatal Health Interventions",
            "Global Health and Surgery"
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
          "openalex_id": "W2132400120",
          "year": 2006,
          "title": "Facilitators and barriers to adoption of evidence-based perinatal care in Latin American hospitals: a qualitative study",
          "type": "article",
          "venue": "Health Education Research",
          "cited_by_count": 76,
          "topics": [
            "Maternal and Perinatal Health Interventions",
            "Global Maternal and Child Health",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2017854788",
          "year": 2011,
          "title": "Stages of change: A qualitative study on the implementation of a perinatal audit programme in South Africa",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 68,
          "topics": [
            "Global Maternal and Child Health",
            "Health Policy Implementation Science",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W1982181577",
          "year": 2007,
          "title": "Health inequality in Latin America",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 42,
          "topics": [
            "Global Maternal and Child Health",
            "Poverty, Education, and Child Welfare",
            "Global Public Health Policies and Epidemiology"
          ]
        }
      ]
    }
  },
  {
    "name": "Matthijs Versteegh",
    "member_affiliation": "Huygens & Versteegh",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013310",
        "title": "Test of reference dependency in EQ-5D-5L health state valuations",
        "working_group": "Valuation"
      },
      {
        "project_id": "2359-PHD",
        "title": "Valuing Health Trajectories: Developing a Framework for Duration and Sequence-Adjusted Quality-Adjusted Life Years",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5086031530",
      "display_name": "Matthijs Versteegh",
      "orcid": "0000-0003-4804-235X",
      "reported_affiliation": "Huygens Institute for History and Culture of the Netherlands",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 56
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 15
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 12
        },
        {
          "topic": "Multiple Sclerosis Research Studies",
          "works": 11
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 10
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Global Health Care Issues",
          "works": 7
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 6
        },
        {
          "topic": "Amyotrophic Lateral Sclerosis Research",
          "works": 5
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 5
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 4
        },
        {
          "topic": "Diet and metabolism studies",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Simone Huygens",
          "works": 31
        },
        {
          "name": "Maureen Rutten‐van Mölken",
          "works": 20
        },
        {
          "name": "Werner Brouwer",
          "works": 16
        },
        {
          "name": "Heleen Vellekoop",
          "works": 16
        },
        {
          "name": "Sarah Wordsworth",
          "works": 14
        },
        {
          "name": "Rositsa Koleva‐Kolarova",
          "works": 13
        },
        {
          "name": "László Szilberhorn",
          "works": 13
        },
        {
          "name": "Tamás Zelei",
          "works": 13
        },
        {
          "name": "Balázs Nagy",
          "works": 12
        },
        {
          "name": "Apostolos Tsiachristas",
          "works": 12
        },
        {
          "name": "Elly Stolk",
          "works": 10
        },
        {
          "name": "Arthur E. Attema",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7140136920",
          "year": 2026,
          "title": "Antiarrhythmic drugs vs catheter ablation as rhythm control for atrial fibrillation: A systematic review and meta-analysis of randomized controlled trials",
          "type": "review",
          "venue": "Heart Rhythm",
          "cited_by_count": 1,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac Arrhythmias and Treatments",
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W7138941209",
          "year": 2026,
          "title": "Cost-effectiveness of treatment sequences following first-line rituximab in relapsing-remitting multiple sclerosis: a Norwegian microsimulation study",
          "type": "article",
          "venue": "Frontiers in Neurology",
          "cited_by_count": 0,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Peripheral Neuropathies and Disorders",
            "Polyomavirus and related diseases"
          ]
        },
        {
          "openalex_id": "W7125228769",
          "year": 2026,
          "title": "P0547 Fecal incontinence and sexual distress significantly impact quality of life in ulcerative proctitis: results from the prospective multicenter SNAP-UP study",
          "type": "conference-abstract",
          "venue": "Journal of Crohn s and Colitis",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Bowel Disease",
            "Reproductive tract infections research",
            "Diverticular Disease and Complications"
          ]
        },
        {
          "openalex_id": "W7139973176",
          "year": 2026,
          "title": "The Cost Utility of Rhythm Control Treatment Sequences in Patients with Atrial Fibrillation: Anti-arrhythmic Drugs Versus Catheter Ablation",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac Arrhythmias and Treatments",
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W4413190438",
          "year": 2025,
          "title": "Comparative Efficacy of all Available Pharmaceutical Therapies for Moderate to Severe Crohn’s Disease: A Systematic Review and Network Meta-Analysis",
          "type": "review",
          "venue": "Gastro Hep Advances",
          "cited_by_count": 3,
          "topics": [
            "Inflammatory Bowel Disease",
            "Autoimmune and Inflammatory Disorders",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W4413447252",
          "year": 2025,
          "title": "Cost–Utility Analysis of Treatment Sequences for Moderate-to-Severe Crohn’s Disease",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Bowel Disease",
            "Biosimilars and Bioanalytical Methods",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2100869289",
          "year": 2010,
          "title": "Mapping onto Eq-5 D for patients in poor health",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 74,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2112268677",
          "year": 2011,
          "title": "Mapping QLQ-C30, HAQ, and MSIS-29 on EQ-5D",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 70,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2001151965",
          "year": 2011,
          "title": "PCN197 Health Related Quality of Life in Long Term Survivors of Lymphoma: A Population Based Study",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Multiple and Secondary Primary Cancers"
          ]
        },
        {
          "openalex_id": "W1999439167",
          "year": 2011,
          "title": "PIH37 The Royal Road or the Middle Way? Public and Patient Preferences for Health Outcomes",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2334353679",
          "year": 2016,
          "title": "Dutch Tariff for the Five-Level Version of EQ-5D",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1144,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2502386956",
          "year": 2016,
          "title": "Patient and general public preferences for health states: A call to reconsider current guidelines",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 165,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2091278357",
          "year": 2013,
          "title": "Time trade-off: one methodology, different methods",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 163,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2077591238",
          "year": 2013,
          "title": "Introducing the composite time trade-off: a test of feasibility and face validity",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 156,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Mental Health Research Topics"
          ]
        },
        {
          "openalex_id": "W2890408626",
          "year": 2018,
          "title": "When is it too expensive? Cost-effectiveness thresholds and health care decision-making",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 116,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1992029200",
          "year": 2012,
          "title": "Condition-Specific Preference-Based Measures: Benefit or Burden?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 112,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2507833965",
          "year": 2016,
          "title": "From Good to Better: New Dutch Guidelines for Economic Evaluations in Healthcare",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 111,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2947435062",
          "year": 2019,
          "title": "Severity-Adjusted Probability of Being Cost Effective",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 83,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Palliative Care and End-of-Life Issues"
          ]
        }
      ]
    }
  }
]
