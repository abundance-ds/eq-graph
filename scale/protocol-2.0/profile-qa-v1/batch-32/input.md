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
    "name": "Leida Lamers",
    "member_affiliation": "Ministry of Health, Welfare and Sports",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5091647381",
      "display_name": "Leida M. Lamers",
      "orcid": "",
      "reported_affiliation": "Institut für Forschung und Transfer",
      "works_count": 51,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 27
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 23
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 3
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 3
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 3
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 3
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 2
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 2
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "René C.J.A. van Vliet",
          "works": 11
        },
        {
          "name": "Peep F. M. Stalmeier",
          "works": 7
        },
        {
          "name": "Paul F. M. Krabbe",
          "works": 7
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 7
        },
        {
          "name": "Wynand P.M.M. van de Ven",
          "works": 7
        },
        {
          "name": "Gerrit T. Koopmans",
          "works": 4
        },
        {
          "name": "Erik M. van Barneveld",
          "works": 4
        },
        {
          "name": "Jan Bleeker",
          "works": 4
        },
        {
          "name": "Ruud A.M. Erdman",
          "works": 4
        },
        {
          "name": "Maarten F. Bobbert",
          "works": 3
        },
        {
          "name": "Ineke M. Leenders",
          "works": 3
        },
        {
          "name": "Dick C. Kruyssen",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407128944",
          "year": 2024,
          "title": "Investigation of Quality Criteria in the Production of PEM Electrolyzer Stacks",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Catalysis and Hydrodesulfurization Studies"
          ]
        },
        {
          "openalex_id": "W4254083311",
          "year": 2010,
          "title": "Announcements",
          "type": "article",
          "venue": "Psychotherapy and Psychosomatics",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2041487033",
          "year": 2010,
          "title": "Psychological and Knowledge Factors Related to Delay of Help-Seeking by Patients with Acute Myocardial Infarction",
          "type": "article",
          "venue": "Psychotherapy and Psychosomatics",
          "cited_by_count": 46,
          "topics": [
            "Cardiac Health and Mental Health",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W2591887533",
          "year": 2010,
          "title": "Subject Index Vol. 63, 1995",
          "type": "paratext",
          "venue": "Psychotherapy and Psychosomatics",
          "cited_by_count": 0,
          "topics": [
            "Diverse Scientific and Economic Studies",
            "Human auditory perception and evaluation",
            "Legal Cases and Commentary"
          ]
        },
        {
          "openalex_id": "W1998635598",
          "year": 2009,
          "title": "Holistic Preferences for 1-Year Health Profiles Describing Fluctuations in Health",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 45,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W2066346982",
          "year": 2008,
          "title": "Cost‐effectiveness of temozolomide for the treatment of newly diagnosed glioblastoma multiforme",
          "type": "article",
          "venue": "Cancer",
          "cited_by_count": 51,
          "topics": [
            "Glioma Diagnosis and Treatment",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Brain Metastases and Treatment"
          ]
        },
        {
          "openalex_id": "W2021432763",
          "year": 1983,
          "title": "Diminished Na+/K+ and Ca2+ pump activities in the Ca2+ depleted heart: possible role in the development of Ca2+ overload during the Ca2+ paradox",
          "type": "article",
          "venue": "European Heart Journal",
          "cited_by_count": 25,
          "topics": [
            "Cardiac electrophysiology and arrhythmias",
            "Ion channel regulation and function",
            "Integrated Circuits and Semiconductor Failure Analysis"
          ]
        },
        {
          "openalex_id": "W1535001711",
          "year": 1993,
          "title": "Vertraging bij de opname van hartinfarctpatienten",
          "type": "article",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Dutch Social and Cultural Studies",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W2101068352",
          "year": 1994,
          "title": "Risk-Adjusted Capitation: Recent Experiences in the Netherlands",
          "type": "article",
          "venue": "Health Affairs",
          "cited_by_count": 58,
          "topics": [
            "Healthcare Policy and Management",
            "Emergency and Acute Care Studies",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W2048183110",
          "year": 1996,
          "title": "Multiyear Diagnostic Information from Prior Hospitalizations as a Risk-Adjuster for Capitation Payments",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 37,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2096463904",
          "year": 2006,
          "title": "The Dutch tariff: results and arguments for an effective design for national EQ‐5D valuation studies",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 636,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2118332255",
          "year": 2005,
          "title": "[Measuring the quality of life in economic evaluations: the Dutch EQ-5D tariff].",
          "type": "other",
          "venue": "PubMed",
          "cited_by_count": 581,
          "topics": []
        },
        {
          "openalex_id": "W2050998086",
          "year": 2006,
          "title": "Gender and health care utilization: The role of mental distress and help-seeking propensity",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 212,
          "topics": [
            "Health disparities and outcomes",
            "Mental Health Treatment and Access",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W2166503382",
          "year": 2002,
          "title": "Risk adjustment and risk selection on the sickness fund insurance market in five European countries",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 162,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2105997341",
          "year": 2006,
          "title": "Comparison of EQ-5D and SF-6D utilities in mental health patients",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 143,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Practices and Patient Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1968778871",
          "year": 2003,
          "title": "The Pharmacy-based Cost Group model: validating and adjusting the classification of medications for chronic conditions to the Dutch situation",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 104,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2152518278",
          "year": 2007,
          "title": "The effect of induced forelimb lameness on thoracolumbar kinematics during treadmill locomotion",
          "type": "article",
          "venue": "Equine Veterinary Journal",
          "cited_by_count": 98,
          "topics": [
            "Veterinary Equine Medical Research",
            "Veterinary Orthopedics and Neurology",
            "Veterinary Pharmacology and Anesthesia"
          ]
        },
        {
          "openalex_id": "W4239607618",
          "year": 2008,
          "title": "The effect of induced hindlimb lameness on thoracolumbar kinematics during treadmill locomotion",
          "type": "article",
          "venue": "Equine Veterinary Journal",
          "cited_by_count": 82,
          "topics": [
            "Veterinary Equine Medical Research",
            "Mechanics and Biomechanics Studies",
            "Sports Performance and Training"
          ]
        }
      ]
    }
  },
  {
    "name": "Lidia Engel",
    "member_affiliation": "Monash University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1481-PHD",
        "title": "Incorporating informal carers' quality of life in health economic evaluation using the EQ-5D",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "150-RA",
        "title": "Feasibility and validity of routine collection of patient-reported outcome measures (PROMs) in residential aged care facilities",
        "working_group": "Descriptive Systems, Populations and Health Systems, EQ-HWB"
      },
      {
        "project_id": "2008-RA",
        "title": "Examining carer outcomes using the EQ-5D-5L and EQ-HWB: Evidence from the EQ DAPHNIE Survey",
        "working_group": "Populations and Health Systems, EQ-HWB"
      },
      {
        "project_id": "20190960",
        "title": "An exploratory analysis of the Pain/Discomfort dimension of the EQ-5D-5L in people living with physical and mental health conditions",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2173-RA",
        "title": "Examining the psychometric performance of eleven bolt-ons for the EQ-5D-5L in older adults",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2453-RA",
        "title": "Measurement Performance of the EQ-5D-5L in Hospitalised Older Adults: Routine PROMs Evidence",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5039737173",
      "display_name": "Lidia Engel",
      "orcid": "0000-0002-7959-3149",
      "reported_affiliation": "Australian Regenerative Medicine Institute",
      "works_count": 141,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 56
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 25
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 24
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 16
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 15
        },
        {
          "topic": "Global Health Care Issues",
          "works": 13
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 12
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 11
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 10
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 9
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 8
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Cathrine Mihalopoulos",
          "works": 68
        },
        {
          "name": "Long Khanh‐Dao Le",
          "works": 27
        },
        {
          "name": "Brendan Mulhern",
          "works": 22
        },
        {
          "name": "Nikki McCaffrey",
          "works": 17
        },
        {
          "name": "Jessica Bucholc",
          "works": 16
        },
        {
          "name": "David G. T. Whitehurst",
          "works": 15
        },
        {
          "name": "Frances Batchelor",
          "works": 15
        },
        {
          "name": "Yong Yi Lee",
          "works": 14
        },
        {
          "name": "Mary Lou Chatterton",
          "works": 13
        },
        {
          "name": "Tessa Peasgood",
          "works": 13
        },
        {
          "name": "Julie Ratcliffe",
          "works": 13
        },
        {
          "name": "Stirling Bryan",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7125947648",
          "year": 2026,
          "title": "Examining the face validity of the EQ-HWB-9 in dementia: caregiver interpretation across “Today” and “7-Day” recall periods",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7160109756",
          "year": 2026,
          "title": "IMMERSE-2 IMpleMenting Effective infection prevention and control in ReSidential aged carE through Communities of Practice: protocol for a before-and-after study (Preprint)",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Infection Control in Healthcare",
            "Pressure Ulcer Prevention and Management"
          ]
        },
        {
          "openalex_id": "W7125026808",
          "year": 2026,
          "title": "Moving together to facilitate equity and inclusion in research. The co-production of interventions for clinical trials to facilitate participation of people from ethnically diverse communities",
          "type": "article",
          "venue": "Health Research Policy and Systems",
          "cited_by_count": 2,
          "topics": [
            "Mental Health and Patient Involvement",
            "Diabetes Management and Education",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7162016954",
          "year": 2026,
          "title": "Preferences for Cancer Information and Support Services—A Discrete Choice Experiment",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Cancer survivorship and care",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W7167727387",
          "year": 2026,
          "title": "The Cost Effectiveness of Treatment Strategies for Depression in Ethiopia: A Multiple Cohort Markov Model Analysis",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Mental Health Treatment and Access",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W4414089117",
          "year": 2025,
          "title": "1235 Post-death reflections of bereaved family members on quality of end-of-life care in residential aged care",
          "type": "conference-paper",
          "venue": "Poster",
          "cited_by_count": 0,
          "topics": [
            "Grief, Bereavement, and Mental Health"
          ]
        },
        {
          "openalex_id": "W2001790155",
          "year": 2013,
          "title": "Determining the current state-of-play for variants of the ‘short form' health-related quality of life instrument in spinal cord injury: A systematic literature review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Spinal Cord Injury Research",
            "Cerebral Palsy and Movement Disorders",
            "Spinal Dysraphism and Malformations"
          ]
        },
        {
          "openalex_id": "W2135361259",
          "year": 2013,
          "title": "Perceptions of individuals living with spinal cord injury toward preference-based quality of life instruments: A qualitative exploration",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Spinal Cord Injury Research"
          ]
        },
        {
          "openalex_id": "W1984861503",
          "year": 2014,
          "title": "Exploring psychometric properties of the SF-6D, a preference-based health-related quality of life measure, in the context of spinal cord injury",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 13,
          "topics": [
            "Spinal Cord Injury Research",
            "Traumatic Brain Injury Research",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2170991750",
          "year": 2014,
          "title": "Perceptions of individuals living with spinal cord injury toward preference-based quality of life instruments: a qualitative exploration",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 30,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cerebral Palsy and Movement Disorders",
            "Spinal Cord Injury Research"
          ]
        },
        {
          "openalex_id": "W3162151314",
          "year": 2021,
          "title": "Cost-effectiveness evidence of mental health prevention and promotion interventions: A systematic review of economic evaluations",
          "type": "review",
          "venue": "PLoS Medicine",
          "cited_by_count": 254,
          "topics": [
            "Mental Health Treatment and Access",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Digital Mental Health Interventions"
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
          "openalex_id": "W3112786231",
          "year": 2020,
          "title": "Physical Health, Media Use, and Mental Health in Children and Adolescents With ADHD During the COVID-19 Pandemic in Australia",
          "type": "article",
          "venue": "Journal of Attention Disorders",
          "cited_by_count": 152,
          "topics": [
            "Attention Deficit Hyperactivity Disorder",
            "Autism Spectrum Disorder Research",
            "Child Development and Digital Technology"
          ]
        },
        {
          "openalex_id": "W2945362832",
          "year": 2019,
          "title": "The economic costs of loneliness: a review of cost-of-illness and economic evaluation studies",
          "type": "article",
          "venue": "Social Psychiatry and Psychiatric Epidemiology",
          "cited_by_count": 145,
          "topics": [
            "Health disparities and outcomes",
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
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
          "openalex_id": "W4280573135",
          "year": 2022,
          "title": "The EMPOWER blended digital intervention for relapse prevention in schizophrenia: a feasibility cluster randomised controlled trial in Scotland and Australia",
          "type": "article",
          "venue": "The Lancet Psychiatry",
          "cited_by_count": 74,
          "topics": [
            "Digital Mental Health Interventions",
            "Schizophrenia research and treatment",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4389272687",
          "year": 2023,
          "title": "Recommendations for Emerging Good Practice and Future Research in Relation to Family and Caregiver Health Spillovers in Health Economic Evaluations: A Report of the SHEER Task Force",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Lina Maria Serna Higuita",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2338-RA",
        "title": "Longitudinal Assessment of the EQ-5D-5L Anxiety/Depression Dimension in Cancer Patients with Emotional Distress: Structural Validity, Responsiveness, and Subgroup Performance Compared with PHQ-4 and HADS",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5022647682",
      "display_name": "Lina María Serna-­Higuita",
      "orcid": "0000-0001-5182-8295",
      "reported_affiliation": "Institute for Medical Informatics and Biostatistics",
      "works_count": 227,
      "top_topics": [
        {
          "topic": "Renal Diseases and Glomerulopathies",
          "works": 24
        },
        {
          "topic": "Renal Transplantation Outcomes and Treatments",
          "works": 23
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 15
        },
        {
          "topic": "Pediatric Urology and Nephrology Studies",
          "works": 15
        },
        {
          "topic": "Complement system in diseases",
          "works": 14
        },
        {
          "topic": "Cardiac Imaging and Diagnostics",
          "works": 11
        },
        {
          "topic": "Acute Kidney Injury Research",
          "works": 9
        },
        {
          "topic": "Muscle and Compartmental Disorders",
          "works": 9
        },
        {
          "topic": "Chronic Kidney Disease and Diabetes",
          "works": 8
        },
        {
          "topic": "Urinary Tract Infections Management",
          "works": 8
        },
        {
          "topic": "Polyomavirus and related diseases",
          "works": 8
        },
        {
          "topic": "Cardiovascular Function and Risk Factors",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Fredy Nieto‐Ríos",
          "works": 93
        },
        {
          "name": "Gustavo Adolfo Zuluaga-­Valencia",
          "works": 61
        },
        {
          "name": "Arbey Aristizábal­-Alzate",
          "works": 57
        },
        {
          "name": "Catalina Ocampo-­Kohn",
          "works": 45
        },
        {
          "name": "Peter Martus",
          "works": 29
        },
        {
          "name": "Juan José Vanegas-Ruiz",
          "works": 19
        },
        {
          "name": "Diana Carolina Bello-Márquez",
          "works": 18
        },
        {
          "name": "Catalina Vélez-Echeverri",
          "works": 17
        },
        {
          "name": "Juan José Vanegas Ruiz",
          "works": 14
        },
        {
          "name": "Franz Schaefer",
          "works": 12
        },
        {
          "name": "Peter Rosenberger",
          "works": 12
        },
        {
          "name": "Catalina Vélez Echeverri",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7155567534",
          "year": 2026,
          "title": "Diminished plasma levels of GPIb-α predict mortality in a prospective ARDS cohort",
          "type": "article",
          "venue": "Frontiers in Medicine",
          "cited_by_count": 0,
          "topics": [
            "Platelet Disorders and Treatments",
            "Heparin-Induced Thrombocytopenia and Thrombosis",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation"
          ]
        },
        {
          "openalex_id": "W7154595534",
          "year": 2026,
          "title": "Quantitative Assessment of Peripheral Nerve Echogenicity in Children and Adolescents Aged 2–17 Years: A Retrospective Cross-Sectional Ultrasound Study",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 0,
          "topics": [
            "Peripheral Nerve Disorders",
            "Peripheral Neuropathies and Disorders",
            "Nerve injury and regeneration"
          ]
        },
        {
          "openalex_id": "W4410696937",
          "year": 2025,
          "title": "Anticoagulation versus antiplatelet therapy in patients with embolic stroke of unknown source: A systematic review and meta-analysis",
          "type": "review",
          "venue": "EP Europace",
          "cited_by_count": 0,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Venous Thromboembolism Diagnosis and Management",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4413790265",
          "year": 2025,
          "title": "Comparative Analysis of Cardiac CT and Invasive Coronary Angiography for Suspected Stable Coronary Artery Disease and Subsequent Functional Testing and Revascularization: A Prespecified Secondary DISCHARGE Randomized Trial Analysis",
          "type": "article",
          "venue": "Radiology Cardiothoracic Imaging",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Coronary Interventions and Diagnostics",
            "Advanced X-ray and CT Imaging"
          ]
        },
        {
          "openalex_id": "W4414982298",
          "year": 2025,
          "title": "Differential Hypoxemia During Veno‐Arterial Extracorporeal Organ Support: Its Impact on Mortality and Different Treatment Strategies",
          "type": "article",
          "venue": "Artificial Organs",
          "cited_by_count": 0,
          "topics": [
            "Mechanical Circulatory Support Devices",
            "Cardiac and Coronary Surgery Techniques",
            "Transplantation: Methods and Outcomes"
          ]
        },
        {
          "openalex_id": "W4407045909",
          "year": 2025,
          "title": "Discontinuation of immune checkpoint inhibitors for reasons other than disease progression and the impact on relapse and survival of advanced melanoma patients. A systematic review and meta-analysis",
          "type": "review",
          "venue": "Frontiers in Immunology",
          "cited_by_count": 14,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Cutaneous Melanoma Detection and Management",
            "Melanoma and MAPK Pathways"
          ]
        },
        {
          "openalex_id": "W1510506739",
          "year": 2000,
          "title": "A search for genetic loci involved in predisposition to bipolar mood disorder in the population of Antioquia, Colombia.",
          "type": "conference-paper",
          "venue": "Queensland's institutional digital repository (The University of Queensland)",
          "cited_by_count": 1,
          "topics": [
            "Bipolar Disorder and Treatment"
          ]
        },
        {
          "openalex_id": "W2041250881",
          "year": 2000,
          "title": "An association study of bipolar mood disorder (type I) with the 5-HTTLPR serotonin transporter polymorphism in a human population isolate from Colombia",
          "type": "article",
          "venue": "Neuroscience Letters",
          "cited_by_count": 79,
          "topics": [
            "Bipolar Disorder and Treatment",
            "Neurotransmitter Receptor Influence on Behavior",
            "Receptor Mechanisms and Signaling"
          ]
        },
        {
          "openalex_id": "W1896502226",
          "year": 2000,
          "title": "Evaluación de ligamiento del Trastorno Afectivo Bipolar con marcadores STR en las regiones cromosómicas 18p12, 18q22-23, 21q22 Y 12q23",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 0,
          "topics": [
            "Bipolar Disorder and Treatment"
          ]
        },
        {
          "openalex_id": "W2942737227",
          "year": 2000,
          "title": "Lack of association between a serotonin transporter promoter polymorphism and BP1 in Antioquia, Colombia",
          "type": "article",
          "venue": "Queensland's institutional digital repository (The University of Queensland)",
          "cited_by_count": 1,
          "topics": [
            "Bipolar Disorder and Treatment"
          ]
        },
        {
          "openalex_id": "W2618084763",
          "year": 2017,
          "title": "Long-Term Outcome of Steroid-Resistant Nephrotic Syndrome in Children",
          "type": "article",
          "venue": "Journal of the American Society of Nephrology",
          "cited_by_count": 224,
          "topics": [
            "Renal Diseases and Glomerulopathies",
            "Autoimmune Bullous Skin Diseases",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W2035537416",
          "year": 2013,
          "title": "Genetic screening in adolescents with steroid-resistant nephrotic syndrome",
          "type": "article",
          "venue": "Kidney International",
          "cited_by_count": 94,
          "topics": [
            "Renal Diseases and Glomerulopathies",
            "Ion Transport and Channel Regulation",
            "Coagulation, Bradykinin, Polyphosphates, and Angioedema"
          ]
        },
        {
          "openalex_id": "W4390102230",
          "year": 2023,
          "title": "Apixaban versus Aspirin for Embolic Stroke of Undetermined Source",
          "type": "article",
          "venue": "NEJM Evidence",
          "cited_by_count": 84,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Acute Ischemic Stroke Management",
            "Cardiac Arrhythmias and Treatments"
          ]
        },
        {
          "openalex_id": "W3009675256",
          "year": 2020,
          "title": "Multi-Modal Characterization of the Coagulopathy Associated With Extracorporeal Membrane Oxygenation",
          "type": "article",
          "venue": "Critical Care Medicine",
          "cited_by_count": 71,
          "topics": [
            "Mechanical Circulatory Support Devices",
            "Nosocomial Infections in ICU",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W4281572264",
          "year": 2022,
          "title": "Oral Coenzyme Q10 supplementation leads to better preservation of kidney function in steroid-resistant nephrotic syndrome due to primary Coenzyme Q10 deficiency",
          "type": "article",
          "venue": "Kidney International",
          "cited_by_count": 64,
          "topics": [
            "Coenzyme Q10 studies and effects",
            "Biochemical Acid Research Studies"
          ]
        },
        {
          "openalex_id": "W4379615372",
          "year": 2023,
          "title": "Deep learning-based scoring of tumour-infiltrating lymphocytes is prognostic in primary melanoma and predictive to PD-1 checkpoint inhibition in melanoma metastases",
          "type": "article",
          "venue": "EBioMedicine",
          "cited_by_count": 51,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Cutaneous Melanoma Detection and Management",
            "Immunotherapy and Immune Responses"
          ]
        },
        {
          "openalex_id": "W1964007876",
          "year": 2015,
          "title": "Risk factors for loss of residual renal function in children treated with chronic peritoneal dialysis",
          "type": "article",
          "venue": "Kidney International",
          "cited_by_count": 48,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Acute Kidney Injury Research",
            "Chronic Kidney Disease and Diabetes"
          ]
        }
      ]
    }
  },
  {
    "name": "Ling Jie Cheng",
    "member_affiliation": "University of Oxford",
    "is_member": true,
    "projects": [
      {
        "project_id": "1663-TVG",
        "title": "Scientific Summer Exchange Program to the Alberta PROMs and EQ-5D Research and Support Unit (APERSU)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1961-EO",
        "title": "ISPOR 2024 Dissemination: Advancing Understanding of Psychometric Validation in EQ-5D-Y Instruments and Health State Valuation",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2078-RA",
        "title": "Evaluating Value Sets for Multi-Attribute Utility Instruments: A Comprehensive Analysis",
        "working_group": "Valuation"
      },
      {
        "project_id": "2246-EO",
        "title": "Advancing the interpretation and dissemination of EQ-5D and EQ VAS outcomes across general populations and clinical contexts",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2267-EO",
        "title": "Advancing the interpretation and policy relevance of EQ-5D outcomes through methodological and empirical insights",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2329-RA",
        "title": "Feasibility of the EQ-TIPS-5L Latent Scale DCE: A Qualitative Study in the UK and Singapore",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2531-EO",
        "title": "From Population Health to Valuation Methodology: Disseminating EQ-5D Research at ISPOR 2026",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2605-RA",
        "title": "Characterising and Explaining Socioeconomic Gradients in EQ VAS: A Multinational Analysis of Response Heterogeneity and Health Inequality Underestimation (Project UNVEIL - UNcovering VAS-Education Inequalities in heaLth states)",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5082193621",
      "display_name": "Ling Jie Cheng",
      "orcid": "0000-0002-5338-578X",
      "reported_affiliation": "National University of Singapore",
      "works_count": 150,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 20
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 12
        },
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 10
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 9
        },
        {
          "topic": "Sleep and related disorders",
          "works": 9
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 7
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 6
        },
        {
          "topic": "Mobile Health and mHealth Applications",
          "works": 6
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 6
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 5
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 5
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Ying Lau",
          "works": 38
        },
        {
          "name": "Nan Luo",
          "works": 26
        },
        {
          "name": "Siew Tiang Lau",
          "works": 17
        },
        {
          "name": "Xi Vivien Wu",
          "works": 17
        },
        {
          "name": "Jing Ying Cheng",
          "works": 13
        },
        {
          "name": "Wenru Wang",
          "works": 12
        },
        {
          "name": "Annushiah Vasan Thakumar",
          "works": 11
        },
        {
          "name": "Sai Ho Wong",
          "works": 10
        },
        {
          "name": "Runze Huang",
          "works": 9
        },
        {
          "name": "Huaidong Cheng",
          "works": 9
        },
        {
          "name": "Hwee Weng Dennis Hey",
          "works": 9
        },
        {
          "name": "Le Ann Chen",
          "works": 8
        }
      ],
      "work_examples": [
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
          "openalex_id": "W7128930504",
          "year": 2026,
          "title": "Economic evaluation of national immunization program vaccines in China: a systematic review",
          "type": "review",
          "venue": "Health Economics Review",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Bacterial Infections and Vaccines",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W7167238716",
          "year": 2026,
          "title": "Effectiveness of decision aids on decisional conflict and treatment or disease knowledge among women diagnosed with breast cancer: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Journal of Cancer Survivorship",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Palliative Care and End-of-Life Issues",
            "Ethics and Legal Issues in Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W7141749813",
          "year": 2026,
          "title": "Effectiveness of physio-cognitive dual-task training on improving global cognition, health-related quality of life, and physical outcomes among older adults with neurocognitive disorders: an umbrella review",
          "type": "article",
          "venue": "Age and Ageing",
          "cited_by_count": 1,
          "topics": [
            "Traumatic Brain Injury Research",
            "Balance, Gait, and Falls Prevention",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W7159960610",
          "year": 2026,
          "title": "Factors associated with preoperative health-related quality of life in patients undergoing lumbar spine surgery: a multi-ethnic Asian cohort",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Spine and Intervertebral Disc Pathology",
            "Scoliosis diagnosis and treatment",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7163924617",
          "year": 2026,
          "title": "Measuring health-related quality of life in sepsis survivors and caregivers: a mapping review and a preliminary conceptual framework",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Intensive Care Unit Cognitive Disorders",
            "Family and Patient Care in Intensive Care Units"
          ]
        },
        {
          "openalex_id": "W1990110828",
          "year": 2000,
          "title": "Effect of prophylactic treatment with ursodeoxycholic acid on the gallbladder muscle of guinea pigs with acute cholecystitis",
          "type": "article",
          "venue": "Gastroenterology",
          "cited_by_count": 0,
          "topics": [
            "Liver Disease and Transplantation",
            "Gout, Hyperuricemia, Uric Acid"
          ]
        },
        {
          "openalex_id": "W2615058808",
          "year": 2006,
          "title": "Biomolecular motor-driven selective binding and concentrating of protein analytes",
          "type": "other",
          "venue": "Scholarworks@UNIST (Ulsan National Institute of Science and Technology)",
          "cited_by_count": 0,
          "topics": [
            "Microfluidic and Capillary Electrophoresis Applications",
            "Microfluidic and Bio-sensing Technologies",
            "Electrowetting and Microfluidic Technologies"
          ]
        },
        {
          "openalex_id": "W2530879984",
          "year": 2009,
          "title": "OSTEOPENIA IN CANCELLOUS BONE OF SHEEP INDUCED BY GLUCOCORTICOID ALONE (SELVIK AWARD 2008)",
          "type": "article",
          "venue": "Orthopaedic Proceedings",
          "cited_by_count": 0,
          "topics": [
            "Bone health and osteoporosis research",
            "Bone Metabolism and Diseases",
            "Bone health and treatments"
          ]
        },
        {
          "openalex_id": "W2007351276",
          "year": 2012,
          "title": "Effect of epimedium pubescen flavonoid on bone mineral status and bone turnover in male rats chronically exposed to cigarette smoke",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 21,
          "topics": [
            "Medicinal Plant Pharmacodynamics Research",
            "Bone Metabolism and Diseases",
            "Bone health and osteoporosis research"
          ]
        },
        {
          "openalex_id": "W4229082340",
          "year": 2021,
          "title": "Chatbot-Delivered Psychotherapy for Adults With Depressive and Anxiety Symptoms: A Systematic Review and Meta-Regression",
          "type": "review",
          "venue": "Behavior Therapy",
          "cited_by_count": 164,
          "topics": [
            "Digital Mental Health Interventions",
            "Mental Health Research Topics",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W4312130054",
          "year": 2022,
          "title": "Global prevalence of social isolation among community-dwelling older adults: A systematic review and meta-analysis",
          "type": "review",
          "venue": "Archives of Gerontology and Geriatrics",
          "cited_by_count": 151,
          "topics": [
            "Health disparities and outcomes",
            "Stroke Rehabilitation and Recovery",
            "Health and Well-being Studies"
          ]
        },
        {
          "openalex_id": "W3158966385",
          "year": 2021,
          "title": "Measurement Properties of the EQ VAS Around the Globe: A Systematic Review and Meta-Regression Analysis",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 107,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W2049371126",
          "year": 2012,
          "title": "The influence of the intercondylar notch dimensions on injury of the anterior cruciate ligament: a meta‐analysis",
          "type": "article",
          "venue": "Knee Surgery Sports Traumatology Arthroscopy",
          "cited_by_count": 100,
          "topics": [
            "Knee injuries and reconstruction techniques",
            "Osteoarthritis Treatment and Mechanisms",
            "Lower Extremity Biomechanics and Pathologies"
          ]
        },
        {
          "openalex_id": "W4212991034",
          "year": 2022,
          "title": "Effectiveness of resilience interventions for higher education students: A meta-analysis and metaregression.",
          "type": "article",
          "venue": "Journal of Educational Psychology",
          "cited_by_count": 95,
          "topics": [
            "Resilience and Mental Health"
          ]
        },
        {
          "openalex_id": "W2074587699",
          "year": 2012,
          "title": "The influence of the tibial plateau slopes on injury of the anterior cruciate ligament: a meta‐analysis",
          "type": "article",
          "venue": "Knee Surgery Sports Traumatology Arthroscopy",
          "cited_by_count": 94,
          "topics": [
            "Knee injuries and reconstruction techniques",
            "Foot and Ankle Surgery",
            "Total Knee Arthroplasty Outcomes"
          ]
        },
        {
          "openalex_id": "W2913369524",
          "year": 2019,
          "title": "Factors associated with glycaemic control in patients with diabetes mellitus: A systematic literature review",
          "type": "review",
          "venue": "Journal of Clinical Nursing",
          "cited_by_count": 93,
          "topics": [
            "Diabetes Management and Education",
            "Diabetes Management and Research",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W3001740779",
          "year": 2020,
          "title": "Personalised eHealth interventions in adults with overweight and obesity: A systematic review and meta-analysis of randomised controlled trials",
          "type": "review",
          "venue": "Preventive Medicine",
          "cited_by_count": 87,
          "topics": [
            "Mobile Health and mHealth Applications",
            "Digital Mental Health Interventions",
            "Nutrition, Genetics, and Disease"
          ]
        }
      ]
    }
  },
  {
    "name": "Ling-Hsiang Chuang",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "1482-RA",
        "title": "Performance of EQ-5D-Y in psychiatric/mental health conditions. Examples from autism and phobia",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2407-BT",
        "title": "EQ-5D Bolt-on Toolbox exploration and validation in haematological malignancy. Example from a large UK population-based Haematological Malignancy Research Network (HMRN) ",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "241-RA",
        "title": "Ordinal relationship of TTO and DCE preference data",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5057802030",
      "display_name": "Ling‐Hsiang Chuang",
      "orcid": "",
      "reported_affiliation": "Dutch Health Care Inspectorate",
      "works_count": 136,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 36
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 15
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 13
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 9
        },
        {
          "topic": "Shoulder Injury and Treatment",
          "works": 8
        },
        {
          "topic": "Diagnosis and Treatment of Venous Diseases",
          "works": 8
        },
        {
          "topic": "Diverse Scientific and Economic Studies",
          "works": 8
        },
        {
          "topic": "Shoulder and Clavicle Injuries",
          "works": 7
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Global Health Care Issues",
          "works": 7
        },
        {
          "topic": "Lymphoma Diagnosis and Treatment",
          "works": 7
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "David Torgerson",
          "works": 82
        },
        {
          "name": "Catherine Hewitt",
          "works": 51
        },
        {
          "name": "Stephen Brealey",
          "works": 49
        },
        {
          "name": "Ada Keding",
          "works": 49
        },
        {
          "name": "Belén Corbacho",
          "works": 49
        },
        {
          "name": "Amar Rangan",
          "works": 48
        },
        {
          "name": "Helen HG Handoll",
          "works": 48
        },
        {
          "name": "Laura Jefferson",
          "works": 47
        },
        {
          "name": "Lorna Goodchild",
          "works": 47
        },
        {
          "name": "Marta Soares",
          "works": 33
        },
        {
          "name": "Arthur R Kang’ombe",
          "works": 30
        },
        {
          "name": "Pedro Saramago",
          "works": 30
        }
      ],
      "work_examples": [
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
          "openalex_id": "W4415228180",
          "year": 2025,
          "title": "Extracorporeal photopheresis (ECP) in cutaneous T-cell lymphoma – a systematic literature review of the impact of ECP on clinical and non-clinical outcomes",
          "type": "review",
          "venue": "European Journal of Cancer",
          "cited_by_count": 0,
          "topics": [
            "Cutaneous lymphoproliferative disorders research",
            "Lymphoma Diagnosis and Treatment",
            "T-cell and Retrovirus Studies"
          ]
        },
        {
          "openalex_id": "W4417482296",
          "year": 2025,
          "title": "P1 Predicting EQ-5D Index Scores: A Comparison Study of Machine Learning and Statistical Methods on Health Survey for England Data",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4415227364",
          "year": 2025,
          "title": "Real-World Treatment Patterns and Outcomes in Cutaneous T-Cell Lymphoma (CTCL) Patients Treated with Extracorporeal Photopheresis (ECP) Combined Therapy – A Chart Review Study Protocol",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 0,
          "topics": [
            "Cutaneous lymphoproliferative disorders research",
            "T-cell and Retrovirus Studies",
            "Lymphoma Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4414663954",
          "year": 2025,
          "title": "Self-reported health status in the general population over 2 decades: variation in EQ-5D-3L in Health Survey for England",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4403243625",
          "year": 2024,
          "title": "A-225 The efficacy and safety of extracorporeal photopheresis (ECP) for treatment of mycosis fungoides and/or sézary syndrome in cutaneous T-cell lymphoma",
          "type": "conference-abstract",
          "venue": "European Journal of Cancer",
          "cited_by_count": 0,
          "topics": [
            "Cutaneous lymphoproliferative disorders research",
            "Lymphoma Diagnosis and Treatment",
            "CAR-T cell therapy research"
          ]
        },
        {
          "openalex_id": "W2060677069",
          "year": 1970,
          "title": "Measurement of Absorbed Dose Rate from Terrestrial Background Radiation in Hong Kong",
          "type": "article",
          "venue": "Journal of Radiation Research",
          "cited_by_count": 2,
          "topics": [
            "Radioactivity and Radon Measurements",
            "Radioactive contamination and transfer",
            "Radiation Detection and Scintillator Technologies"
          ]
        },
        {
          "openalex_id": "W2162937108",
          "year": 2008,
          "title": "Hispanic Valuation of the EQ-5D Health States: A Social Value Set for Latin Americans",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 66,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2157081180",
          "year": 2009,
          "title": "A pragmatic multi-centred randomised controlled trial of yoga for chronic low back pain: Trial protocol",
          "type": "article",
          "venue": "Complementary Therapies in Clinical Practice",
          "cited_by_count": 21,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Musculoskeletal pain and rehabilitation",
            "Martial Arts: Techniques, Psychology, and Education"
          ]
        },
        {
          "openalex_id": "W2037249496",
          "year": 2009,
          "title": "Converting the SF-12 into the EQ-5D",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 40,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1991632422",
          "year": 2015,
          "title": "Surgical vs Nonsurgical Treatment of Adults With Displaced Fractures of the Proximal Humerus",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 547,
          "topics": [
            "Shoulder Injury and Treatment",
            "Shoulder and Clavicle Injuries",
            "Nerve Injury and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W1965077146",
          "year": 2009,
          "title": "South Korean Time Trade-Off Values for EQ-5D Health States: Modeling with Observed Values for 101 Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 488,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2135372691",
          "year": 2011,
          "title": "Yoga for Chronic Low Back Pain",
          "type": "article",
          "venue": "Annals of Internal Medicine",
          "cited_by_count": 240,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Musculoskeletal pain and rehabilitation",
            "Biofield Effects and Biophysics"
          ]
        },
        {
          "openalex_id": "W2007820809",
          "year": 2015,
          "title": "The ProFHER (PROximal Fracture of the Humerus: Evaluation by Randomisation) trial – a pragmatic multicentre randomised controlled trial evaluating the clinical effectiveness and cost-effectiveness of surgical compared with non-surgical treatment for proximal fracture of the humerus in adults",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 146,
          "topics": [
            "Shoulder Injury and Treatment",
            "Shoulder and Clavicle Injuries",
            "Nerve Injury and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W2061422450",
          "year": 2014,
          "title": "VenUS IV (Venous leg Ulcer Study IV) – compression hosiery compared with compression bandaging in the treatment of venous leg ulcers: a randomised controlled trial, mixed-treatment comparison and decision-analytic model",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 90,
          "topics": [
            "Diagnosis and Treatment of Venous Diseases",
            "Wound Healing and Treatments",
            "Planarian Biology and Electrostimulation"
          ]
        },
        {
          "openalex_id": "W2016681914",
          "year": 2012,
          "title": "A Pragmatic Multicentered Randomized Controlled Trial of Yoga for Chronic Low Back Pain",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 71,
          "topics": [
            "Mindfulness and Compassion Interventions",
            "Musculoskeletal pain and rehabilitation",
            "Workplace Spirituality and Leadership"
          ]
        },
        {
          "openalex_id": "W2929448145",
          "year": 2019,
          "title": "Health-related quality of life and mortality in patients with pulmonary embolism: a prospective cohort study in seven European countries",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 63,
          "topics": [
            "Venous Thromboembolism Diagnosis and Management",
            "Atrial Fibrillation Management and Outcomes",
            "Inflammatory Biomarkers in Disease Prognosis"
          ]
        }
      ]
    }
  }
]
