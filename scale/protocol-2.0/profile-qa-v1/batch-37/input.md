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
    "name": "Maureen Rutten-van Molken",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2015020",
        "title": "Valuation of the EQ-5D-5L+R",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5010272673",
      "display_name": "Maureen Rutten‐van Mölken",
      "orcid": "0000-0001-8706-3159",
      "reported_affiliation": "Erasmus University Rotterdam",
      "works_count": 478,
      "top_topics": [
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 170
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 124
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 91
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 48
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 37
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 37
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 36
        },
        {
          "topic": "Interprofessional Education and Collaboration",
          "works": 32
        },
        {
          "topic": "Respiratory Support and Mechanisms",
          "works": 24
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 22
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 18
        },
        {
          "topic": "Respiratory and Cough-Related Research",
          "works": 17
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Apostolos Tsiachristas",
          "works": 77
        },
        {
          "name": "Melinde Boland",
          "works": 55
        },
        {
          "name": "Martine Hoogendoorn",
          "works": 54
        },
        {
          "name": "Lucas Goossens",
          "works": 52
        },
        {
          "name": "Niels H. Chavannes",
          "works": 51
        },
        {
          "name": "Talitha Feenstra",
          "works": 33
        },
        {
          "name": "Maiwenn Al",
          "works": 28
        },
        {
          "name": "Annemarije Kruis",
          "works": 27
        },
        {
          "name": "Onno C. P. van Schayck",
          "works": 27
        },
        {
          "name": "Simone Huygens",
          "works": 26
        },
        {
          "name": "Isaac Corro Ramos",
          "works": 23
        },
        {
          "name": "Matthijs Versteegh",
          "works": 20
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7171097433",
          "year": 2026,
          "title": "Added value of a specialized mobile palliative care team compared to the usual care in the primary care setting of Croatia: a 3-month prospective cohort study",
          "type": "article",
          "venue": "BMC Palliative Care",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Frailty in Older Adults",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W7120085762",
          "year": 2026,
          "title": "Bridging affordability and sustainability of health innovations via novel pricing, cost-effectiveness, and reimbursement models to improve patient access: The ASCERTAIN project",
          "type": "article",
          "venue": "Health Policy and Technology",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Biomedical Ethics and Regulation"
          ]
        },
        {
          "openalex_id": "W7164752653",
          "year": 2026,
          "title": "Development and Validation of an Artificial Intelligence Tool for Automated Population, Intervention, Comparator, Outcome Scoping for the European Joint Clinical Assessment: A Proof of Concept",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Artificial Intelligence in Healthcare and Education",
            "Clinical Reasoning and Diagnostic Skills",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7166187127",
          "year": 2026,
          "title": "EPH84 TRANSFORMING DISEASE PREVENTION THROUGH INNOVATIVE INVESTMENT MODELS: DEVELOPMENT OF A TYPOLOGY AND TOOLKIT TO SUPPORT SUSTAINABLE PREVENTION FINANCING",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Community Development and Social Impact",
            "HIV/AIDS Impact and Responses"
          ]
        },
        {
          "openalex_id": "W7124686589",
          "year": 2026,
          "title": "Evaluating international collaboration on horizon scanning for pharmaceuticals: developing key performance indicators for the international horizon scanning initiative",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W7162659799",
          "year": 2026,
          "title": "From evidence to implementation: key priorities for pharmacogenomics-guided treatment and prevention from a European expert workshop",
          "type": "article",
          "venue": "European Journal of Human Genetics",
          "cited_by_count": 1,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Genetic Associations and Epidemiology",
            "Genomics and Rare Diseases"
          ]
        },
        {
          "openalex_id": "W1558020340",
          "year": 1992,
          "title": "Two-Year Bronchodilator Treatment in Patients with Mild Airflow Obstruction",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 66,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Asthma and respiratory diseases",
            "Inhalation and Respiratory Drug Delivery"
          ]
        },
        {
          "openalex_id": "W2090921856",
          "year": 1993,
          "title": "Cost Effectiveness of Inhaled Corticosteroid plus Bronchodilator Therapy versus Bronchodilator Monotherapy in Children with Asthma",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 73,
          "topics": [
            "Asthma and respiratory diseases",
            "Inhalation and Respiratory Drug Delivery",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W2030110651",
          "year": 1993,
          "title": "Health related utility measurement in rheumatology: an introduction",
          "type": "article",
          "venue": "Patient Education and Counseling",
          "cited_by_count": 22,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2099646927",
          "year": 1994,
          "title": "Cost and effects of pharmacotherapy in asthma and COPD",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Asthma and respiratory diseases"
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
          "openalex_id": "W2167941825",
          "year": 2008,
          "title": "Outcomes for COPD pharmacological trials: from lung function to biomarkers",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 858,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Asthma and respiratory diseases",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W2045749557",
          "year": 2005,
          "title": "Effects of N-acetylcysteine on outcomes in chronic obstructive pulmonary disease (Bronchitis Randomized on NAC Cost-Utility Study, BRONCUS): a randomised placebo-controlled trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 684,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory and Cough-Related Research",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W2096723137",
          "year": 2011,
          "title": "Tiotropium versus Salmeterol for the Prevention of Exacerbations of COPD",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 682,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Asthma and respiratory diseases",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W4294967892",
          "year": 2022,
          "title": "Towards the elimination of chronic obstructive pulmonary disease: a Lancet Commission",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 665,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory Support and Mechanisms",
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W2155416296",
          "year": 2014,
          "title": "Nutritional assessment and therapy in COPD: a European Respiratory Society statement",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 352,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Nutrition and Health in Aging",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W1882792209",
          "year": 2000,
          "title": "The cost diary",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 345,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Musculoskeletal pain and rehabilitation",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W1963619764",
          "year": 2013,
          "title": "Real-life compliance and persistence among users of subcutaneous and sublingual allergen immunotherapy",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 306,
          "topics": [
            "Allergic Rhinitis and Sensitization",
            "Dermatology and Skin Diseases",
            "Asthma and respiratory diseases"
          ]
        }
      ]
    }
  },
  {
    "name": "Meixia Liao",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1979-EO",
        "title": "Travel scholarship request to attend ISPOR Europe 2024 for findings dissemination.",
        "working_group": "Dissemination, OA fee"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5079423723",
      "display_name": "Meixia Liao",
      "orcid": "0000-0001-7859-3684",
      "reported_affiliation": "National University of Singapore",
      "works_count": 17,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 6
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 2
        },
        {
          "topic": "Acute Kidney Injury Research",
          "works": 2
        },
        {
          "topic": "Healthcare Quality and Management",
          "works": 2
        },
        {
          "topic": "Patient Safety and Medication Errors",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 2
        },
        {
          "topic": "Chronic Kidney Disease and Diabetes",
          "works": 1
        },
        {
          "topic": "Renal Transplantation Outcomes and Treatments",
          "works": 1
        },
        {
          "topic": "Quality and Supply Management",
          "works": 1
        },
        {
          "topic": "Clinical Reasoning and Diagnostic Skills",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 8
        },
        {
          "name": "Zhihao Yang",
          "works": 7
        },
        {
          "name": "Dan Zhang",
          "works": 5
        },
        {
          "name": "Pusheng Wang",
          "works": 4
        },
        {
          "name": "Fei Yang",
          "works": 2
        },
        {
          "name": "Yongguang Liu",
          "works": 2
        },
        {
          "name": "Tingfang Liu",
          "works": 2
        },
        {
          "name": "Ling Jie Cheng",
          "works": 2
        },
        {
          "name": "Herng‐Chia Chiu",
          "works": 2
        },
        {
          "name": "Kim Rand",
          "works": 2
        },
        {
          "name": "Zheng Yang",
          "works": 1
        },
        {
          "name": "Nick Bansback",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164819429",
          "year": 2026,
          "title": "The EQ-5D-5L valuation study in Nigeria",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W7150744095",
          "year": 2026,
          "title": "Validity and responsiveness of the EQ-5D-5L, EQ-HWB and EQ-HWB-9 to measure health and wellbeing impact of heatwaves among older adults",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health and Wellbeing Research",
            "Climate Change and Health Impacts",
            "Thermoregulation and physiological responses"
          ]
        },
        {
          "openalex_id": "W7117105613",
          "year": 2025,
          "title": "Is There a Shelf Life for EQ-5D Value Sets: Evidence of Evolving Societal Preferences From Asia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4401715625",
          "year": 2024,
          "title": "Testing four cognition bolt-on items to the EQ-5D in a general Chinese population",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W4398248582",
          "year": 2024,
          "title": "Testing “Pits” Time Trade-Off: Can Data Quality be Improved by Removing Death From Valuation of Health States?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4387253902",
          "year": 2023,
          "title": "AN EXPLORATORY STUDY OF TWO RESPIRATORY BOLT-ONS FOR EQ-5D-5L AMONG MULTI-ETHNIC ASIANS WITH OBSTRUCTIVE AIRWAY DISEASES (OAD): AN ANALYSIS OF 184 PATIENTS",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 0,
          "topics": [
            "Air Quality and Health Impacts",
            "Noise Effects and Management"
          ]
        },
        {
          "openalex_id": "W2986820254",
          "year": 2019,
          "title": "Quality control circle: a tool for enhancing perceptions of patient safety culture among hospital staff in Chinese hospitals",
          "type": "article",
          "venue": "International Journal for Quality in Health Care",
          "cited_by_count": 21,
          "topics": [
            "Patient Safety and Medication Errors",
            "Occupational Health and Safety Research",
            "Workplace Violence and Bullying"
          ]
        },
        {
          "openalex_id": "W3049267685",
          "year": 2020,
          "title": "&lt;p&gt;Implementation and Promotion of Quality Control Circle: A Starter for Quality Improvement in Chinese Hospitals&lt;/p&gt;",
          "type": "article",
          "venue": "Risk Management and Healthcare Policy",
          "cited_by_count": 20,
          "topics": [
            "Healthcare Quality and Management",
            "Patient Safety and Medication Errors",
            "Quality and Supply Management"
          ]
        },
        {
          "openalex_id": "W3034987158",
          "year": 2020,
          "title": "Research on Mathematics Culture and Mathematics Education",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "History and Theory of Mathematics",
            "Mathematics Education and Teaching Techniques",
            "Diverse Interdisciplinary Research Innovations"
          ]
        },
        {
          "openalex_id": "W3092179187",
          "year": 2020,
          "title": "The Cost-Effectiveness of Kidney Replacement Therapy Modalities: A Systematic Review of Full Economic Evaluations",
          "type": "review",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 73,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Acute Kidney Injury Research",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W3127456273",
          "year": 2021,
          "title": "Cost-effectiveness analysis of renal replacement therapy strategies in Guangzhou city, southern China",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 35,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Acute Kidney Injury Research",
            "Renal Transplantation Outcomes and Treatments"
          ]
        },
        {
          "openalex_id": "W4362692377",
          "year": 2023,
          "title": "Patient decision support interventions for candidates considering elective surgeries: a systematic review and meta-analysis",
          "type": "review",
          "venue": "International Journal of Surgery",
          "cited_by_count": 9,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Clinical Reasoning and Diagnostic Skills",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W4312115725",
          "year": 2022,
          "title": "Censoring in the time trade-off valuation of worse-than-dead EQ-5D-5L health states: can a time-based willingness-to-accept question be the solution?",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 8,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Frailty in Older Adults",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W3119839364",
          "year": 2021,
          "title": "Development and validation of an instrument in job evaluation factors of physicians in public hospitals in Beijing, China",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 7,
          "topics": [
            "Healthcare professionals’ stress and burnout",
            "Advanced Technologies in Various Fields",
            "Job Satisfaction and Organizational Behavior"
          ]
        },
        {
          "openalex_id": "W4353015483",
          "year": 2023,
          "title": "Urban/rural differences in preferences for EQ-5D-5L health states: a study of a multi-ethnic region in China",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
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
    "name": "Michael Herdman",
    "member_affiliation": "Insight Consulting & Research",
    "is_member": true,
    "projects": [
      {
        "project_id": "2014110",
        "title": "Assessing the health of the general population in England: how do the EQ-5D 3L and 5L versions compare?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016730",
        "title": "Workshop to discuss the legitimacy, estimation, and uses of the Minimal Important Difference (MID) with EQ-5D",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5006750775",
      "display_name": "Michael Herdman",
      "orcid": "0000-0002-8189-5357",
      "reported_affiliation": "National University of Singapore",
      "works_count": 87,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 61
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 10
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 10
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 7
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 5
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 5
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 4
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 19
        },
        {
          "name": "Nancy Devlin",
          "works": 18
        },
        {
          "name": "Xavier Badı́a",
          "works": 15
        },
        {
          "name": "Rachel Lee-Yin Tan",
          "works": 8
        },
        {
          "name": "Paul Kind",
          "works": 6
        },
        {
          "name": "Simone Kreimeier",
          "works": 6
        },
        {
          "name": "Wolfgang Greiner",
          "works": 5
        },
        {
          "name": "Narcís Gusi",
          "works": 5
        },
        {
          "name": "Koonal Shah",
          "works": 5
        },
        {
          "name": "Kristina Burström",
          "works": 4
        },
        {
          "name": "Ann‐Charlotte Egmar",
          "works": 4
        },
        {
          "name": "Ulrike Ravens‐Sieberer",
          "works": 4
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
          "openalex_id": "W4413001612",
          "year": 2025,
          "title": "A Head-to-Head Comparison of the Psychometric Properties of the EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Children Aged 8 to 18 Years With Eczema",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Dermatology and Skin Diseases",
            "Psoriasis: Treatment and Pathogenesis",
            "Body Image and Dysmorphia Studies"
          ]
        },
        {
          "openalex_id": "W4414090964",
          "year": 2025,
          "title": "A Head-to-Head Comparison of the Psychometric Properties of the EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Children With Asthma",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Asthma and respiratory diseases",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4408246071",
          "year": 2025,
          "title": "Are EQ‐5D‐Y‐3L and EQ‐5D‐Y‐5L Useful Tools to Assess Health Outcomes in Children With Asthma? An Analysis of Child and Parental Carer Reporting",
          "type": "article",
          "venue": "Pediatric Pulmonology",
          "cited_by_count": 2,
          "topics": [
            "Asthma and respiratory diseases",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4412555489",
          "year": 2025,
          "title": "Assessing the Health-Related Quality of Life of Children With Asthma or Eczema by a Proxy: Does Assessment Perspective Matter?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Dermatology and Skin Diseases",
            "Asthma and respiratory diseases",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4409450625",
          "year": 2025,
          "title": "Head-to-Head Comparisons of the Distributional Characteristics and Measurement Properties of the 3-Level and 5-Level Versions of the EQ-5D-Y: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W156335384",
          "year": 1997,
          "title": "‘Equivalence’ and the translation and adaptation of health-related quality of life questionnaires",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 471,
          "topics": [
            "Health, psychology, and well-being",
            "Health disparities and outcomes",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W4245157584",
          "year": 1998,
          "title": "",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 772,
          "topics": []
        },
        {
          "openalex_id": "W4244838765",
          "year": 1998,
          "title": "",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 225,
          "topics": []
        },
        {
          "openalex_id": "W1587877887",
          "year": 1998,
          "title": "A model of equivalence in the cultural adaptation of HRQoL instruments: the universalist approach.",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 856,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes"
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
          "openalex_id": "W2396459437",
          "year": 1999,
          "title": "[The Spanish version of EuroQol: a description and its applications. European Quality of Life scale].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 553,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Aging, Health, and Disability",
            "Stress and Burnout Research"
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
          "openalex_id": "W2039973247",
          "year": 2001,
          "title": "El EuroQol-5D: una alternativa sencilla para la medición de la calidad de vida relacionada con la salud en atención primaria",
          "type": "article",
          "venue": "Atención Primaria",
          "cited_by_count": 465,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Musculoskeletal pain and rehabilitation"
          ]
        }
      ]
    }
  },
  {
    "name": "Michał Jakubczyk",
    "member_affiliation": "SGH Warsaw School of Economics, Poland",
    "is_member": true,
    "projects": [
      {
        "project_id": "1530-RA",
        "title": "Re(re)visiting negative composite time trade-off utilities – can threshold hypothesis really save the day?",
        "working_group": "Valuation"
      },
      {
        "project_id": "1574-RA",
        "title": "Alternative approach to value set construction – accounting for interpersonal utility comparisons taboo based on axiomatic approach",
        "working_group": "Valuation"
      },
      {
        "project_id": "1585-RA",
        "title": "Making composite time trade-off method sensitive for worse-than-dead states",
        "working_group": "Valuation"
      },
      {
        "project_id": "1689-RA",
        "title": "Estimating the relative importance of health when being a child vs when being an adult at an individual respondent level",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1930-RA",
        "title": "Investigating alternative methods for linking bolt-on and base instrument value sets",
        "working_group": "Valuation"
      },
      {
        "project_id": "2009-RA",
        "title": "Valuation of bolt-ons using measurement data",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015320",
        "title": "A fuzzy approach to time trade-off experiment in EQ-5D-3L valuation",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016640",
        "title": "Building values sets based on TTO results by averaging model predictions and actually observed means",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190070",
        "title": "Making both ends neat: exploring the effects of modifying the TTO on non trading and all in trading",
        "working_group": "Valuation"
      },
      {
        "project_id": "2132-RA",
        "title": "Does a spoonful of honey improve a barrel of tar? Comparing 33333+1 with 33333",
        "working_group": "Valuation"
      },
      {
        "project_id": "2143-RA",
        "title": "Measuring interactions in bolt-on valuation using lotteries",
        "working_group": "Valuation"
      },
      {
        "project_id": "2144-RA",
        "title": "Getting more from the core in bolt-on valuation",
        "working_group": "Valuation"
      },
      {
        "project_id": "404-RA",
        "title": "Better than dead? – but this or that? Testing how framing impacts viewing a health state as worse than dead.",
        "working_group": "Valuation"
      },
      {
        "project_id": "431-RA",
        "title": "TTOFU is good for health (valuation)! - Time Trade-Off Follow-Up questions in measuring the discounting, fear of death, and value of life per se",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5015781187",
      "display_name": "Michał Jakubczyk",
      "orcid": "0000-0002-0006-6769",
      "reported_affiliation": "SGH Warsaw School of Economics",
      "works_count": 128,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 50
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 27
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 19
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 16
        },
        {
          "topic": "Global Health Care Issues",
          "works": 15
        },
        {
          "topic": "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
          "works": 13
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 12
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 8
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 5
        },
        {
          "topic": "Hepatitis B Virus Studies",
          "works": 4
        },
        {
          "topic": "Nutrition and Health Studies",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maciej Niewada",
          "works": 60
        },
        {
          "name": "Dominik Golicki",
          "works": 28
        },
        {
          "name": "Marcin Czech",
          "works": 22
        },
        {
          "name": "J. Pawèska",
          "works": 17
        },
        {
          "name": "Elżbieta Rdzanek",
          "works": 17
        },
        {
          "name": "Witold Wrona",
          "works": 16
        },
        {
          "name": "Tomasz Hermanowski",
          "works": 16
        },
        {
          "name": "Olga Adamowicz-Sidor",
          "works": 11
        },
        {
          "name": "T Macioch",
          "works": 11
        },
        {
          "name": "Bogumił Kamiński",
          "works": 8
        },
        {
          "name": "Ewa Kowalik",
          "works": 6
        },
        {
          "name": "Adam Witkowski",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164732578",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7164751425",
          "year": 2026,
          "title": "1st EuroQol Central and Eastern Europe Regional Meeting: Book of Abstracts",
          "type": "other",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7162664709",
          "year": 2026,
          "title": "Exploring Perceived Interactions between EQ-5D-5L and Bolt-ons Using Composite Time-Tradeoff Valuations: A Qualitative Study",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4412572730",
          "year": 2025,
          "title": "Assessing a dire fate: Standard gamble and time trade-off utilities for states worse than dead",
          "type": "article",
          "venue": "Theory and Decision",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4405996400",
          "year": 2025,
          "title": "Central statistical monitoring in clinical trial management: A scoping review",
          "type": "article",
          "venue": "Clinical Trials",
          "cited_by_count": 2,
          "topics": [
            "Statistical Methods in Clinical Trials",
            "Advanced Statistical Process Monitoring",
            "Biosimilars and Bioanalytical Methods"
          ]
        },
        {
          "openalex_id": "W4416138446",
          "year": 2025,
          "title": "Eliciting discounting model and direction at the individual level with time trade-off follow-up questions",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Forecasting Techniques and Applications",
            "Experimental Behavioral Economics Studies"
          ]
        },
        {
          "openalex_id": "W1170570035",
          "year": 2003,
          "title": "O niespójności preferencji w decyzjach sekwencyjnych",
          "type": "article",
          "venue": "Prace Naukowe / Akademia Ekonomiczna w Katowicach",
          "cited_by_count": 0,
          "topics": [
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2977603774",
          "year": 2004,
          "title": "Analiza wymiaru korelacyjnego przy użyciu testów surogatowych w badaniu efektywności rynku kapitałowego w Polsce",
          "type": "article",
          "venue": "Prace Naukowe / Akademia Ekonomiczna w Katowicach",
          "cited_by_count": 0,
          "topics": [
            "Finance, Markets, and Regulation",
            "Agricultural economics and policies",
            "Accounting Theory and Financial Reporting"
          ]
        },
        {
          "openalex_id": "W2033845430",
          "year": 2004,
          "title": "PIN18 ASSESSING THE COST-EFFECTIVENESS OF DROTRECOGIN ALFA (ACTIVATED) IN SEVERE SEPSIS IN POLAND",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2041600250",
          "year": 2006,
          "title": "PIN5 THE COST EFFECTIVENESS ANALYSIS OF TREATMENT WITH PEGINTERFERON ALFA-2A (40KD) IN PATIENTS WITH HBEAG-NEGATIVE CHRONIC HEPATITIS B",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis B Virus Studies",
            "Hepatitis C virus research",
            "Liver Disease Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2618613105",
          "year": 2017,
          "title": "A framework for sensitivity analysis of decision trees",
          "type": "article",
          "venue": "Central European Journal of Operations Research",
          "cited_by_count": 522,
          "topics": [
            "Risk and Portfolio Optimization",
            "Bayesian Modeling and Causal Inference",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W162429609",
          "year": 2015,
          "title": "Coronary Computed Tomographic Prediction Rule for Time-Efficient Guidewire Crossing Through Chronic Total Occlusion",
          "type": "article",
          "venue": "JACC: Cardiovascular Interventions",
          "cited_by_count": 179,
          "topics": [
            "Coronary Interventions and Diagnostics",
            "Cardiac Imaging and Diagnostics",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W1978393391",
          "year": 2009,
          "title": "Valuation of EQ-5D Health States in Poland: First TTO-Based Social Value Set in Central and Eastern Europe",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 115,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2948766088",
          "year": 2019,
          "title": "Valuation of EQ-5D-5L Health States in Poland: the First EQ-VT-Based Study in Central and Eastern Europe",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 100,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2025711782",
          "year": 2014,
          "title": "Cost-effectiveness versus Cost-Utility Analyses: What Are the Motives Behind Using Each and How Do Their Results Differ?—A Polish Example",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 50,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Advances in Oncology and Radiotherapy"
          ]
        },
        {
          "openalex_id": "W2472116823",
          "year": 2016,
          "title": "CT Angiography for the Detection of Coronary Artery Stenoses in Patients Referred for Cardiac Valve Surgery",
          "type": "article",
          "venue": "JACC. Cardiovascular imaging",
          "cited_by_count": 49,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Cardiac Valve Diseases and Treatments",
            "Coronary Interventions and Diagnostics"
          ]
        },
        {
          "openalex_id": "W3043930122",
          "year": 2020,
          "title": "Outcomes of ex vivo liver resection and autotransplantation: A systematic review and meta-analysis",
          "type": "review",
          "venue": "Surgery",
          "cited_by_count": 48,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Cholangiocarcinoma and Gallbladder Cancer Studies",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W3202443669",
          "year": 2021,
          "title": "Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health states",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 46,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        }
      ]
    }
  },
  {
    "name": "Michela Meregaglia",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2043-RA",
        "title": "Assessing Psychometric Properties and Implementation of EQ-HWB-S in Residential Aged Care Facilities: Evidence from Italy.",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "351-RA",
        "title": "Behind the scenes: a mixed method investigation of the impact of quality control procedures on interviewers performance",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5038451583",
      "display_name": "Michela Meregaglia",
      "orcid": "0000-0003-0092-5970",
      "reported_affiliation": "Bocconi University",
      "works_count": 73,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 37
        },
        {
          "topic": "Genomics and Rare Diseases",
          "works": 8
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 8
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 8
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 6
        },
        {
          "topic": "Head and Neck Cancer Studies",
          "works": 6
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 4
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 3
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Oriana Ciani",
          "works": 21
        },
        {
          "name": "Giovanni Fattore",
          "works": 13
        },
        {
          "name": "Francesco Malandrini",
          "works": 10
        },
        {
          "name": "Elena Nicod",
          "works": 8
        },
        {
          "name": "Rosanna Tarricone",
          "works": 8
        },
        {
          "name": "John Cairns",
          "works": 8
        },
        {
          "name": "Michael Drummond",
          "works": 7
        },
        {
          "name": "Carmine Pinto",
          "works": 7
        },
        {
          "name": "Amanda Whittal",
          "works": 6
        },
        {
          "name": "Ludovica Borsoi",
          "works": 6
        },
        {
          "name": "Claudio Jommi",
          "works": 5
        },
        {
          "name": "Massimo Di Maïo",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7153970342",
          "year": 2026,
          "title": "Implementing the EU HTA regulation and joint clinical assessment: a multi-stakeholder perspective from Italy",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W7130650969",
          "year": 2026,
          "title": "Optimism and participation in breast cancer screening: evidence from the United States",
          "type": "article",
          "venue": "Rivista italiana di economia, demografia e statistica",
          "cited_by_count": 0,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Optimism, Hope, and Well-being",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W7128697098",
          "year": 2026,
          "title": "Patient reported outcome measures in spinal muscular atrophy and duchenne muscular dystrophy: review of instruments and their inclusion in clinical and regulatory processes",
          "type": "article",
          "venue": "Neurological Sciences",
          "cited_by_count": 0,
          "topics": [
            "Neurogenetic and Muscular Disorders Research",
            "Muscle Physiology and Disorders",
            "Genetic Neurodegenerative Diseases"
          ]
        },
        {
          "openalex_id": "W4408704002",
          "year": 2025,
          "title": "Envisioning an Italian Head and Neck Proton Therapy Model-Based Selection: Challenge and Opportunity",
          "type": "editorial",
          "venue": "International Journal of Particle Therapy",
          "cited_by_count": 0,
          "topics": [
            "Head and Neck Cancer Studies",
            "Advanced Radiotherapy Techniques",
            "Oral health in cancer treatment"
          ]
        },
        {
          "openalex_id": "W4412545663",
          "year": 2025,
          "title": "Improvement of medication adherence in osteoporosis through telemedicine combined with email: a patient-reported experience and outcome measure-based prospective study",
          "type": "article",
          "venue": "BMJ Health & Care Informatics",
          "cited_by_count": 1,
          "topics": [
            "Bone health and osteoporosis research",
            "Bone health and treatments",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4414879142",
          "year": 2025,
          "title": "Recommended methods for the collection of clinical expert judgment in rare diseases: Generating evidence to support reimbursement of orphan drugs",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 1,
          "topics": [
            "Genomics and Rare Diseases",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical Ethics and Regulation"
          ]
        },
        {
          "openalex_id": "W2106833427",
          "year": 2013,
          "title": "Parent “cocoon” immunization to prevent pertussis-related hospitalization in infants: The case of Piemonte in Italy",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 26,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Pneumonia and Respiratory Infections",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W2164210695",
          "year": 2014,
          "title": "Critical review of economic evaluation studies of interventions promoting low-fat diets",
          "type": "article",
          "venue": "Nutrition Reviews",
          "cited_by_count": 11,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Consumer Attitudes and Food Labeling",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W1979863898",
          "year": 2014,
          "title": "Health-Related Quality of Life in Italian Patients With Moderate and Severe Crohn's Disease: Interim Results from the Sole Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Inflammatory Bowel Disease",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Microscopic Colitis"
          ]
        },
        {
          "openalex_id": "W1651602512",
          "year": 2014,
          "title": "Italy: Health System Review.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 465,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare Quality and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W3122582132",
          "year": 2021,
          "title": "The Use of Patient-Reported Outcome Measures in Rare Diseases and Implications for Health Technology Assessment",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 93,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genomics and Rare Diseases",
            "BRCA gene mutations in cancer"
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
        },
        {
          "openalex_id": "W2286194308",
          "year": 2015,
          "title": "Efficacy and Safety of Ferric Carboxymaltose and Other Formulations in Iron-Deficient Patients: A Systematic Review and Network Meta-analysis of Randomised Controlled Trials",
          "type": "review",
          "venue": "Clinical Drug Investigation",
          "cited_by_count": 73,
          "topics": [
            "Iron Metabolism and Disorders",
            "Erythropoietin and Anemia Treatment",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W2750582352",
          "year": 2017,
          "title": "A systematic literature review of health state utility values in head and neck cancer",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 57,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2531205478",
          "year": 2016,
          "title": "Mud‐Bath Therapy in Addition to Usual Care in Bilateral Knee Osteoarthritis: An Economic Evaluation Alongside a Randomized Controlled Trial",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 43,
          "topics": [
            "Therapeutic Uses of Natural Elements",
            "Gut microbiota and health",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W4310076212",
          "year": 2022,
          "title": "EQ-5D-5L Population Norms for Italy",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 41,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W1966875484",
          "year": 2015,
          "title": "Health and Economic Outcomes of Introducing the New MenB Vaccine (Bexsero) into the Italian Routine Infant Immunisation Programme",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 40,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Virology and Viral Diseases",
            "Pneumonia and Respiratory Infections"
          ]
        }
      ]
    }
  }
]
