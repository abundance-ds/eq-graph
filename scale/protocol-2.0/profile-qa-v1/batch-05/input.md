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
    "name": "Annette Regan",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1796-RA",
        "title": "Monthly measurement of health-related quality of life (HRQoL) from early pregnancy to postpartum: An Ecological Momentary Assessment (EMA) of the EQ-5D-5L",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "260-RA",
        "title": "Health-Related Quality-of-life of the Pregnant and Postpartum Women during the COVID-19 Pandemic (Phase I)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "384-RA",
        "title": "Fasttrack application to evaluate the emergence of SARS-CoV-2, B.1.1.7 variant and continued assessment of HRQoL of the pregnant and postpartum women: a Wave 2 survey using the EQ-5D-5L",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5010948852",
      "display_name": "Annette K. Regan",
      "orcid": "0000-0002-3879-6193",
      "reported_affiliation": "Kaiser Permanente",
      "works_count": 226,
      "top_topics": [
        {
          "topic": "Influenza Virus Research Studies",
          "works": 91
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 85
        },
        {
          "topic": "COVID-19 Impact on Reproduction",
          "works": 65
        },
        {
          "topic": "Respiratory viral infections research",
          "works": 47
        },
        {
          "topic": "Reproductive Health and Contraception",
          "works": 23
        },
        {
          "topic": "Bacterial Infections and Vaccines",
          "works": 19
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 15
        },
        {
          "topic": "Ectopic Pregnancy Diagnosis and Management",
          "works": 15
        },
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 14
        },
        {
          "topic": "Pregnancy and preeclampsia studies",
          "works": 13
        },
        {
          "topic": "Gestational Diabetes Research and Management",
          "works": 12
        },
        {
          "topic": "Data-Driven Disease Surveillance",
          "works": 12
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gavin Pereira",
          "works": 50
        },
        {
          "name": "Paul V. Effler",
          "works": 41
        },
        {
          "name": "Deshayne B. Fell",
          "works": 29
        },
        {
          "name": "Siri E. Håberg",
          "works": 28
        },
        {
          "name": "Sheena G. Sullivan",
          "works": 26
        },
        {
          "name": "Hannah C. Moore",
          "works": 21
        },
        {
          "name": "Christopher C. Blyth",
          "works": 20
        },
        {
          "name": "Jeffrey C. Kwong",
          "works": 19
        },
        {
          "name": "Donna B Mak",
          "works": 19
        },
        {
          "name": "Amanuel Tesfay Gebremedhin",
          "works": 18
        },
        {
          "name": "Onyebuchi A. Arah",
          "works": 17
        },
        {
          "name": "Damien Foo",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169648047",
          "year": 2026,
          "title": "CAUSAL-RSV: A study protocol for a causal mediation analysis of RSV vaccine effects in infants using real-world data",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "COVID-19 Clinical Research Studies",
            "Immune responses and vaccinations"
          ]
        },
        {
          "openalex_id": "W7124419890",
          "year": 2026,
          "title": "Method matters: prenatal paracetamol use and neurodevelopmental outcomes",
          "type": "article",
          "venue": "The Lancet Obstetrics Gynaecology & Women s Health",
          "cited_by_count": 1,
          "topics": [
            "Anesthesia and Neurotoxicity Research",
            "Pregnancy and Medication Impact",
            "Pharmacological Effects and Toxicity Studies"
          ]
        },
        {
          "openalex_id": "W7122380669",
          "year": 2026,
          "title": "P-1594. Incidence and Severity of Post-Pandemic SARS-CoV-2 Infection during Pregnancy",
          "type": "article",
          "venue": "Open Forum Infectious Diseases",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "COVID-19 Pandemic Impacts"
          ]
        },
        {
          "openalex_id": "W7122575951",
          "year": 2026,
          "title": "P-519. Detection &amp; Severity of Respiratory Virus Co-Infections with SARS-CoV-2, Influenza, or RSV in U.S. Children &amp;lt;2 Years Old",
          "type": "conference-abstract",
          "venue": "Open Forum Infectious Diseases",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Pneumonia and Respiratory Infections",
            "Influenza Virus Research Studies"
          ]
        },
        {
          "openalex_id": "W7167826122",
          "year": 2026,
          "title": "Risk of Severe Coronavirus Disease 2019 (COVID-19) in Pregnant and Postpartum Individuals After the Pandemic Emergency",
          "type": "article",
          "venue": "Obstetrics and Gynecology",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "COVID-19 epidemiological studies",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W4412839062",
          "year": 2025,
          "title": "<scp>COVID</scp>‐19 vaccination around the time of conception and risk of placenta‐mediated adverse pregnancy outcomes",
          "type": "article",
          "venue": "Acta Obstetricia Et Gynecologica Scandinavica",
          "cited_by_count": 2,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        },
        {
          "openalex_id": "W2170403361",
          "year": 2010,
          "title": "Are Irish women following the food pyramid recommendations for pregnancy?",
          "type": "article",
          "venue": "Proceedings of The Nutrition Society",
          "cited_by_count": 0,
          "topics": [
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2140039456",
          "year": 2010,
          "title": "Perceptions of Menthol Cigarette Use Among U.S. Adults and Adult Smokers: Findings From the 2009 HealthStyles Survey",
          "type": "article",
          "venue": "Nicotine & Tobacco Research",
          "cited_by_count": 14,
          "topics": [
            "Smoking Behavior and Cessation",
            "Alcohol Consumption and Health Effects",
            "Substance Abuse Treatment and Outcomes"
          ]
        },
        {
          "openalex_id": "W2102207967",
          "year": 2010,
          "title": "Smokers who are also using smokeless tobacco products in the US: a national assessment of characteristics, behaviours and beliefs of ‘dual users’: Table 1",
          "type": "article",
          "venue": "Tobacco Control",
          "cited_by_count": 73,
          "topics": [
            "Smoking Behavior and Cessation",
            "Substance Abuse Treatment and Outcomes",
            "Antioxidant Activity and Oxidative Stress"
          ]
        },
        {
          "openalex_id": "W1882503735",
          "year": 2011,
          "title": "Are women in early pregnancy following the national pyramid recommendations?",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 5,
          "topics": [
            "Gestational Diabetes Research and Management",
            "Obesity, Physical Activity, Diet",
            "Breastfeeding Practices and Influences"
          ]
        },
        {
          "openalex_id": "W2130209540",
          "year": 2011,
          "title": "Electronic nicotine delivery systems: adult use and awareness of the ‘e-cigarette’ in the USA",
          "type": "article",
          "venue": "Tobacco Control",
          "cited_by_count": 494,
          "topics": [
            "Smoking Behavior and Cessation",
            "Nicotinic Acetylcholine Receptors Study",
            "Substance Abuse Treatment and Outcomes"
          ]
        },
        {
          "openalex_id": "W2897893390",
          "year": 2018,
          "title": "Influenza Vaccine Effectiveness in Preventing Influenza-associated Hospitalizations During Pregnancy: A Multi-country Retrospective Test Negative Design Study, 2010–2016",
          "type": "article",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 187,
          "topics": [
            "Influenza Virus Research Studies",
            "Respiratory viral infections research",
            "COVID-19 Impact on Reproduction"
          ]
        },
        {
          "openalex_id": "W4220968998",
          "year": 2022,
          "title": "Association of COVID-19 Vaccination in Pregnancy With Adverse Peripartum Outcomes",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 162,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "SARS-CoV-2 and COVID-19 Research",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W2753711896",
          "year": 2017,
          "title": "Risk of stillbirth, preterm delivery, and fetal growth restriction following exposure in a previous birth: systematic review and meta‐analysis",
          "type": "review",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 135,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Birth, Development, and Health",
            "Gestational Diabetes Research and Management"
          ]
        },
        {
          "openalex_id": "W4322492440",
          "year": 2023,
          "title": "Changes in preterm birth and stillbirth during COVID-19 lockdowns in 26 countries",
          "type": "article",
          "venue": "Nature Human Behaviour",
          "cited_by_count": 123,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Global Maternal and Child Health",
            "Maternal Mental Health During Pregnancy and Postpartum"
          ]
        },
        {
          "openalex_id": "W2769065949",
          "year": 2017,
          "title": "Randomized Controlled Trial of Text Message Reminders for Increasing Influenza Vaccination",
          "type": "article",
          "venue": "The Annals of Family Medicine",
          "cited_by_count": 122,
          "topics": [
            "Influenza Virus Research Studies",
            "Vaccine Coverage and Hesitancy",
            "Data-Driven Disease Surveillance"
          ]
        },
        {
          "openalex_id": "W4205639392",
          "year": 2022,
          "title": "A Prospective Cohort Study of COVID-19 Vaccination, SARS-CoV-2 Infection, and Fertility",
          "type": "article",
          "venue": "American Journal of Epidemiology",
          "cited_by_count": 114,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Global Maternal and Child Health",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W3013317867",
          "year": 2020,
          "title": "Stillbirth risk prediction using machine learning for a large cohort of births from Western Australia, 1980–2015",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 79,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Global Maternal and Child Health",
            "Maternal and Perinatal Health Interventions"
          ]
        }
      ]
    }
  },
  {
    "name": "Annushiah Vasan Thakumar",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2297-EO",
        "title": "Travel scholarship application to attend ISPOR Europe 2025",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2629-RA",
        "title": "Psychometric Evaluation of EQ-TIPS and EQ-5D-Y in Malaysian Children with Autism Spectrum Disorder",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5007225491",
      "display_name": "Annushiah Vasan Thakumar",
      "orcid": "0000-0001-7261-1255",
      "reported_affiliation": "Taylor's University",
      "works_count": 32,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 21
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 5
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 3
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 2
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 2
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 2
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 2
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 2
        },
        {
          "topic": "Artificial Intelligence in Healthcare and Education",
          "works": 2
        },
        {
          "topic": "Radiomics and Machine Learning in Medical Imaging",
          "works": 2
        },
        {
          "topic": "Global Health Care Issues",
          "works": 2
        },
        {
          "topic": "Quality and Management Systems",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 14
        },
        {
          "name": "Ling Jie Cheng",
          "works": 11
        },
        {
          "name": "Xun Li",
          "works": 9
        },
        {
          "name": "Asrul Akmal Shafie",
          "works": 8
        },
        {
          "name": "Calvin Wei Jie Chern",
          "works": 5
        },
        {
          "name": "Xin Zhang",
          "works": 4
        },
        {
          "name": "L Cheng",
          "works": 4
        },
        {
          "name": "Kim Rand",
          "works": 3
        },
        {
          "name": "Siew Chin Ong",
          "works": 3
        },
        {
          "name": "Hwee Weng Dennis Hey",
          "works": 3
        },
        {
          "name": "Tessa Kennedy‐Martin",
          "works": 3
        },
        {
          "name": "Kristina S. Boye",
          "works": 3
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
          "openalex_id": "W7166031551",
          "year": 2026,
          "title": "EPH106 FACTORS ASSOCIATED WITH PREOPERATIVE HEALTH-RELATED QUALITY OF LIFE IN PATIENTSUNDERGOING SURGERYFOR DEGENERATIVE LUMBAR SPINE CONDITIONS: A CROSS-SECTIONAL EQ-5D STUDYIN A MULTI-ETHNIC ASIAN POPULATION",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance",
            "Nausea and vomiting management"
          ]
        },
        {
          "openalex_id": "W7166049043",
          "year": 2026,
          "title": "EPH226 VALUE SETS FOR AQOL, EQ-5D, HUI, QWB AND SF-6D: A SYSTEMATIC REVIEW OF THEIR AVAILABILITY AND CHARACTERISTICS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Free Radicals and Antioxidants",
            "Chemical and Physical Properties in Aqueous Solutions",
            "Chemistry and Chemical Engineering"
          ]
        },
        {
          "openalex_id": "W7160906615",
          "year": 2026,
          "title": "Economic hardship, food insecurity, and mental health across 15 countries after the COVID-19 pandemic: a cross-sectional analysis of 67,178 adults",
          "type": "other",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": []
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
          "openalex_id": "W2903723251",
          "year": 2018,
          "title": "EQ-5D-5L Valuation for the Malaysian Population",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 91,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2897003883",
          "year": 2018,
          "title": "Psychometric performance assessment of Malay and Malaysian English version of EQ-5D-5L in the Malaysian population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 40,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W3083601110",
          "year": 2020,
          "title": "Multiplicative modelling of EQ-5D-3L TTO and VAS values",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 10,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3093212260",
          "year": 2020,
          "title": "Perspectives of the public on the consumption of unregistered health products in Malaysia",
          "type": "article",
          "venue": "International Journal of Pharmacy Practice",
          "cited_by_count": 11,
          "topics": [
            "Pharmaceutical Quality and Counterfeiting",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4413827585",
          "year": 2025,
          "title": "Developing an EQ-5D-5L Value Set for Singapore",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4320482298",
          "year": 2023,
          "title": "Quantifying health-related quality of life in Malaysian type 2 diabetes: focusing on complication types and severity",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4407035816",
          "year": 2025,
          "title": "Patient-reported quality of life outcomes with mandibular advancement versus continuous positive airway pressure: insights from the CRESCENT trial",
          "type": "article",
          "venue": "SLEEP",
          "cited_by_count": 5,
          "topics": [
            "Obstructive Sleep Apnea Research",
            "Sleep and related disorders",
            "Nasal Surgery and Airway Studies"
          ]
        },
        {
          "openalex_id": "W4415765685",
          "year": 2025,
          "title": "Who Prefers Death to Life in Composite Time Trade-off Interviews, and Why? A Mixed-Methods Study among Asians in Singapore",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Palliative Care and End-of-Life Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Antony Martin",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "319-RA",
        "title": "An examination of the psychometric performance of the EQ-5D in haemophilia: A systematic literature review",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070568819",
      "display_name": "Antony P. Martin",
      "orcid": "0000-0003-4383-6038",
      "reported_affiliation": "",
      "works_count": 125,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Hemophilia Treatment and Research",
          "works": 14
        },
        {
          "topic": "Hemoglobinopathies and Related Disorders",
          "works": 13
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 12
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 10
        },
        {
          "topic": "Colorectal Cancer Surgical Treatments",
          "works": 7
        },
        {
          "topic": "Bioenergy crop production and management",
          "works": 6
        },
        {
          "topic": "Endometrial and Cervical Cancer Treatments",
          "works": 5
        },
        {
          "topic": "Iron Metabolism and Disorders",
          "works": 5
        },
        {
          "topic": "Advanced Fluorescence Microscopy Techniques",
          "works": 4
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 4
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Brian Godman",
          "works": 33
        },
        {
          "name": "Jamie O’Hara",
          "works": 16
        },
        {
          "name": "Alan Haycox",
          "works": 14
        },
        {
          "name": "Melanie Calvert",
          "works": 14
        },
        {
          "name": "Nanxin Li",
          "works": 14
        },
        {
          "name": "Tomasz Bochenek",
          "works": 13
        },
        {
          "name": "Farrukh Shah",
          "works": 13
        },
        {
          "name": "Jennifer Drahos",
          "works": 12
        },
        {
          "name": "Zahra Pakbaz",
          "works": 12
        },
        {
          "name": "Brendan Collins",
          "works": 12
        },
        {
          "name": "Amanj Kurdi",
          "works": 11
        },
        {
          "name": "Jurij Fürst",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7138945340",
          "year": 2026,
          "title": "Designing and Implementing Real-World Patient-Reported Outcomes—Emerging Recommendations: A Good Practices Report of an ISPOR Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4414055483",
          "year": 2025,
          "title": "An examination of inpatient ward and secondary community care stay costs for individuals with complex mental health needs in the UK",
          "type": "article",
          "venue": "PLOS mental health.",
          "cited_by_count": 0,
          "topics": [
            "Psychiatric care and mental health services",
            "Mental Health Treatment and Access",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W4416399778",
          "year": 2025,
          "title": "Health Equity Concerns in People with Sickle Cell Disease and Recurrent Vaso-Occlusive Crises: Results from an International Survey Study",
          "type": "article",
          "venue": "Drugs - Real World Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Hemoglobinopathies and Related Disorders",
            "Iron Metabolism and Disorders",
            "Blood groups and transfusion"
          ]
        },
        {
          "openalex_id": "W4409529349",
          "year": 2025,
          "title": "Health-related quality of life and economic impacts in adults with sickle cell disease with recurrent vaso-occlusive crises: findings from a prospective longitudinal real-world survey",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 9,
          "topics": [
            "Hemoglobinopathies and Related Disorders",
            "Iron Metabolism and Disorders",
            "Folate and B Vitamins Research"
          ]
        },
        {
          "openalex_id": "W4409537643",
          "year": 2025,
          "title": "Health-related quality of life and economic impacts in adults with transfusion-dependent β-thalassemia: findings from a prospective longitudinal real-world study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 9,
          "topics": [
            "Hemoglobinopathies and Related Disorders",
            "Blood groups and transfusion",
            "Erythropoietin and Anemia Treatment"
          ]
        },
        {
          "openalex_id": "W4401000167",
          "year": 2024,
          "title": "Acceptability and willingness to pay for a hypothetical HIV vaccine in Brazil and the implications: a cross-sectional study",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W351002430",
          "year": 1975,
          "title": "Minding their own business: Zambia",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 0,
          "topics": [
            "Family Business Performance and Succession"
          ]
        },
        {
          "openalex_id": "W121077369",
          "year": 2005,
          "title": "Chronic kidney disease in the elderly; a silent epidemic.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 6,
          "topics": [
            "Dialysis and Renal Disease Management"
          ]
        },
        {
          "openalex_id": "W2613427988",
          "year": 2006,
          "title": "Medicine: What Matters Tomorrow",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Science, Research, and Medicine",
            "Health and Medical Research Impacts",
            "Climate Change and Health Impacts"
          ]
        },
        {
          "openalex_id": "W2017008099",
          "year": 2007,
          "title": "A Proactive Authentication Integration for the Network Mobility",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 8,
          "topics": [
            "Advanced Authentication Protocols Security",
            "IPv6, Mobility, Handover, Networks, Security",
            "RFID technology advancements"
          ]
        },
        {
          "openalex_id": "W2790130032",
          "year": 2018,
          "title": "Advantages and Limitations of Current Imaging Techniques for Characterizing Liposome Morphology",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 232,
          "topics": [
            "Nanoparticle-Based Drug Delivery",
            "RNA Interference and Gene Delivery",
            "Lipid Membrane Structure and Behavior"
          ]
        },
        {
          "openalex_id": "W3048223582",
          "year": 2020,
          "title": "Response to the Novel Corona Virus (COVID-19) Pandemic Across Africa: Successes, Challenges, and Implications for the Future",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 216,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Viral Infections and Outbreaks Research",
            "Legal, Health, Environmental and COVID-19 Challenges"
          ]
        },
        {
          "openalex_id": "W2810865753",
          "year": 2018,
          "title": "Incidence, aetiology, and sequelae of viral meningitis in UK adults: a multicentre prospective observational cohort study",
          "type": "article",
          "venue": "The Lancet Infectious Diseases",
          "cited_by_count": 194,
          "topics": [
            "Bacterial Infections and Vaccines",
            "Herpesvirus Infections and Treatments",
            "Multiple Sclerosis Research Studies"
          ]
        },
        {
          "openalex_id": "W2160520387",
          "year": 2011,
          "title": "High invertase activity in tomato reproductive organs correlates with enhanced sucrose import into, and heat tolerance of, young fruit",
          "type": "article",
          "venue": "Journal of Experimental Botany",
          "cited_by_count": 175,
          "topics": [
            "Plant nutrient uptake and metabolism",
            "Plant Stress Responses and Tolerance",
            "Plant Micronutrient Interactions and Effects"
          ]
        },
        {
          "openalex_id": "W2994473715",
          "year": 2019,
          "title": "Ongoing strategies to improve the management of upper respiratory tract infections and reduce inappropriate antibiotic use particularly among lower and middle-income countries: findings and implications for the future",
          "type": "article",
          "venue": "Current Medical Research and Opinion",
          "cited_by_count": 173,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pneumonia and Respiratory Infections",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W2899026268",
          "year": 2018,
          "title": "Barriers for Access to New Medicines: Searching for the Balance Between Rising Costs and Limited Budgets",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 163,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2885328264",
          "year": 2018,
          "title": "Advantages and Limitations of Current Techniques for Analyzing the Biodistribution of Nanoparticles",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 151,
          "topics": [
            "Nanoparticle-Based Drug Delivery",
            "Nanoparticles: synthesis and applications",
            "Field-Flow Fractionation Techniques"
          ]
        },
        {
          "openalex_id": "W4392294166",
          "year": 2024,
          "title": "Recommendations to address respondent burden associated with patient-reported outcome assessment",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 124,
          "topics": [
            "Delphi Technique in Research",
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Arjun Bhadhuri",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2506-RA",
        "title": "Measurement properties of the EQ-5D-5L instrument and the CarerQoL instrument, when administered to the informal caregivers of patients with post-stroke aphasia",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5064578943",
      "display_name": "Arjun Bhadhuri",
      "orcid": "0000-0003-1220-0731",
      "reported_affiliation": "University of Basel",
      "works_count": 23,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 3
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Cancer Immunotherapy and Biomarkers",
          "works": 3
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 3
        },
        {
          "topic": "Esophageal Cancer Research and Treatment",
          "works": 3
        },
        {
          "topic": "Neurobiology of Language and Bilingualism",
          "works": 2
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 2
        },
        {
          "topic": "Acute Ischemic Stroke Management",
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
          "topic": "Cystic Fibrosis Research Advances",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Matthias Schwenkglenks",
          "works": 11
        },
        {
          "name": "Paola Salari",
          "works": 5
        },
        {
          "name": "Kate Jolly",
          "works": 3
        },
        {
          "name": "Katharina Tabea Jungo",
          "works": 3
        },
        {
          "name": "Stephen Byrne",
          "works": 3
        },
        {
          "name": "Wilma Knol",
          "works": 3
        },
        {
          "name": "Denis O’Mahony",
          "works": 3
        },
        {
          "name": "Nicolas Rodondi",
          "works": 3
        },
        {
          "name": "Nadine Schur",
          "works": 3
        },
        {
          "name": "C. Simone Sutherland",
          "works": 3
        },
        {
          "name": "Sandro Stoffel",
          "works": 3
        },
        {
          "name": "Alexander Siebenhüner",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407856204",
          "year": 2025,
          "title": "Estimating the indirect costs associated with adenocarcinoma or squamous cell carcinoma of the oesophagus in Switzerland: evidence from a cross-sectional survey",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 1,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Economic and Financial Impacts of Cancer",
            "Head and Neck Cancer Studies"
          ]
        },
        {
          "openalex_id": "W7131869164",
          "year": 2025,
          "title": "Estimating the indirect costs associated with adenocarcinoma or squamous cell carcinoma of the oesophagus in Switzerland: evidence from a cross-sectional survey",
          "type": "article",
          "venue": "Open Access CRIS of the University of Bern",
          "cited_by_count": 0,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Economic and Financial Impacts of Cancer",
            "Head and Neck Cancer Studies"
          ]
        },
        {
          "openalex_id": "W4385782461",
          "year": 2023,
          "title": "Cost Effectiveness and Budget Impact of Nivolumab Plus Ipilimumab Versus Platinum Plus Pemetrexed (with and Without Bevacizumab) in Patients with Unresectable Malignant Pleural Mesothelioma in Switzerland",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 7,
          "topics": [
            "Occupational and environmental lung diseases",
            "Myasthenia Gravis and Thymoma",
            "Pleural and Pulmonary Diseases"
          ]
        },
        {
          "openalex_id": "W4388975291",
          "year": 2023,
          "title": "Cost-Effectiveness of Neoadjuvant Pembrolizumab plus Chemotherapy Followed by Adjuvant Pembrolizumab in Patients with High-Risk, Early-Stage, Triple-Negative Breast Cancer in Switzerland",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 13,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Breast Cancer Treatment Studies",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4319333694",
          "year": 2023,
          "title": "Cost-effectiveness of pembrolizumab as an adjuvant treatment for patients with resected stage IIB or IIC melanoma in Switzerland",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 11,
          "topics": [
            "Cutaneous Melanoma Detection and Management",
            "Cancer Immunotherapy and Biomarkers",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4390126038",
          "year": 2023,
          "title": "EE374 Estimating the Impact of Tumors of the Oesophageal and Gastro-Oesophageal Junction on Work, Leisure and Household Activity Times: Evidence from a Patient Survey in Switzerland",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Esophageal Cancer Research and Treatment"
          ]
        },
        {
          "openalex_id": "W2614343903",
          "year": 2017,
          "title": "A Comparison of the Validity and Responsiveness of the EQ-5D-5L and SF-6D for Measuring Health Spillovers: A Study of the Family Impact of Meningitis",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 33,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2738366735",
          "year": 2017,
          "title": "The effects of educational curricula and training on LGBT‐specific health issues for healthcare students and professionals: a mixed‐method systematic review",
          "type": "review",
          "venue": "Journal of the International AIDS Society",
          "cited_by_count": 281,
          "topics": [
            "LGBTQ Health, Identity, and Policy",
            "HIV/AIDS Research and Interventions",
            "African Sexualities and LGBTQ+ Issues"
          ]
        },
        {
          "openalex_id": "W2801437309",
          "year": 2018,
          "title": "Including health spillovers in economic evaluations",
          "type": "dissertation",
          "venue": "University of Birmingham Institutional Research Archive (University of Birmingham)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2997549790",
          "year": 2019,
          "title": "Cost effectiveness of pembrolizumab vs chemotherapy as first-line treatment for metastatic NSCLC that expresses high levels of PD-L1 in Switzerland",
          "type": "article",
          "venue": "Swiss Medical Weekly",
          "cited_by_count": 29,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Lung Cancer Diagnosis and Treatment",
            "Lung Cancer Treatments and Mutations"
          ]
        },
        {
          "openalex_id": "W3090613169",
          "year": 2020,
          "title": "Measurement properties of EQ-5D-3L and EQ-5D-5L in recording self-reported health status in older patients with substantial multimorbidity and polypharmacy",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 61,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W3021035864",
          "year": 2020,
          "title": "Computerised speech and language therapy or attention control added to usual care for people with long-term post-stroke aphasia: the Big CACTUS three-arm RCT",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 52,
          "topics": [
            "Neurobiology of Language and Bilingualism",
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management"
          ]
        },
        {
          "openalex_id": "W4220694403",
          "year": 2022,
          "title": "Systematic Review of Cost-Utility Analyses That Have Included Carer and Family Member Health-Related Quality of Life",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 32,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Family Support in Illness",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W3108397861",
          "year": 2020,
          "title": "Self-managed, computerised word finding therapy as an add-on to usual care for chronic aphasia post-stroke: An economic evaluation",
          "type": "article",
          "venue": "Clinical Rehabilitation",
          "cited_by_count": 19,
          "topics": [
            "Neurobiology of Language and Bilingualism",
            "Stroke Rehabilitation and Recovery",
            "Acute Ischemic Stroke Management"
          ]
        },
        {
          "openalex_id": "W3142708666",
          "year": 2021,
          "title": "Cost Effectiveness and Budget Impact of Siponimod Compared to Interferon Beta-1a in the Treatment of Adult Patients with Secondary Progressive Multiple Sclerosis with Active Disease in Switzerland",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 18,
          "topics": [
            "Sphingolipid Metabolism and Signaling",
            "Plant-derived Lignans Synthesis and Bioactivity",
            "Multiple Sclerosis Research Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Arthur Attema",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1602-RA",
        "title": "The effect of perspective, duration and views on life after death on valuation of severe states of EQ-5D-Y-3L",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "236-RA",
        "title": "Does priority setting when deciding between adults and children correspond to valuation of EQ-5D(-Y)?",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "237-RA",
        "title": "The effect of duration on the gap between adults’ and children’s TTO valuations",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "435-RA",
        "title": "Employing Episodic Future Thinking to reduce the distortion of time preference in TTO",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5082166488",
      "display_name": "Arthur E. Attema",
      "orcid": "0000-0003-3607-6579",
      "reported_affiliation": "Erasmus University Rotterdam",
      "works_count": 120,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 82
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 70
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 59
        },
        {
          "topic": "Global Health Care Issues",
          "works": 26
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 16
        },
        {
          "topic": "Behavioral Health and Interventions",
          "works": 6
        },
        {
          "topic": "Optimism, Hope, and Well-being",
          "works": 5
        },
        {
          "topic": "Experimental Behavioral Economics Studies",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 3
        },
        {
          "topic": "Economic theories and models",
          "works": 3
        },
        {
          "topic": "Psychology of Moral and Emotional Judgment",
          "works": 3
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Werner Brouwer",
          "works": 46
        },
        {
          "name": "Olivier L’Haridon",
          "works": 26
        },
        {
          "name": "Stefan A. Lipman",
          "works": 21
        },
        {
          "name": "Han Bleichrodt",
          "works": 15
        },
        {
          "name": "Matthijs Versteegh",
          "works": 10
        },
        {
          "name": "José Luis Pinto Prades",
          "works": 10
        },
        {
          "name": "Job van Exel",
          "works": 9
        },
        {
          "name": "Peter P. Wakker",
          "works": 7
        },
        {
          "name": "Zhongyu Lang",
          "works": 6
        },
        {
          "name": "Marieke Krol",
          "works": 6
        },
        {
          "name": "Elly Stolk",
          "works": 5
        },
        {
          "name": "Gijs van de Kuilen",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7171458555",
          "year": 2026,
          "title": "Employing Psychological Distance to Explain Perspective-Specific EQ-5D-Y-3L Health State Valuation: A Bayesian Hierarchical Analysis",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral Health and Interventions",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W7154692873",
          "year": 2026,
          "title": "Special Issue on Behavioral Decision Theory in Health",
          "type": "editorial",
          "venue": "Theory and Decision",
          "cited_by_count": 0,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Behavioral Health and Interventions",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4406425584",
          "year": 2025,
          "title": "Are we ready for the next pandemic? Public preferences and trade-offs between vaccine characteristics and societal restrictions across 21 countries",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 14,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "COVID-19 epidemiological studies",
            "COVID-19 Pandemic Impacts"
          ]
        },
        {
          "openalex_id": "W4415665962",
          "year": 2025,
          "title": "Correction: Is episodic future thinking effective in mitigating the influence of time preference in time trade-off?",
          "type": "erratum",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Psychological and Temporal Perspectives Research",
            "Decision-Making and Behavioral Economics",
            "Optimism, Hope, and Well-being"
          ]
        },
        {
          "openalex_id": "W4414142451",
          "year": 2025,
          "title": "Is episodic future thinking effective in mitigating the influence of time preference in time trade-off?",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics",
            "Optimism, Hope, and Well-being"
          ]
        },
        {
          "openalex_id": "W4416713495",
          "year": 2025,
          "title": "The Effect of Perspective, Duration, and Views on Death on the Valuation of Severe Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1751470693",
          "year": 2002,
          "title": "Studies on Intertemporal Preferences with Applications to Health Economics",
          "type": "dissertation",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Organizational Management and Leadership",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2060849112",
          "year": 2007,
          "title": "Can we fix it? Yes we can! But what? A new test of procedural invariance in TTO‐measurement",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 22,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2011868615",
          "year": 2008,
          "title": "The correction of TTO-scores for utility curvature using a risk-free utility elicitation method",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 47,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Capital Investment and Risk Analysis"
          ]
        },
        {
          "openalex_id": "W2166411915",
          "year": 2009,
          "title": "De TTO-methode en correctie voor tijdsvoorkeur",
          "type": "article",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dutch Social and Cultural Studies",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2803602511",
          "year": 2018,
          "title": "Discounting in Economic Evaluations",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 351,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Climate Change Policy and Economics"
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
          "openalex_id": "W1793842085",
          "year": 2009,
          "title": "Intertemporal Tradeoffs for Gains and Losses: An Experimental Measurement of Discounted Utility",
          "type": "article",
          "venue": "The Economic Journal",
          "cited_by_count": 115,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Economic theories and models"
          ]
        },
        {
          "openalex_id": "W2138086868",
          "year": 2010,
          "title": "Time-Tradeoff Sequences for Analyzing Discounting and Time Inconsistency",
          "type": "article",
          "venue": "Management Science",
          "cited_by_count": 114,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W3123828639",
          "year": 2013,
          "title": "Prospect theory in the health domain: A quantitative assessment",
          "type": "article",
          "venue": "EUR Research Repository (Erasmus University Rotterdam)",
          "cited_by_count": 97,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3126904951",
          "year": 2021,
          "title": "Beliefs and Risk Perceptions About COVID-19: Evidence From Two Successive French Representative Surveys During Lockdown",
          "type": "article",
          "venue": "Frontiers in Psychology",
          "cited_by_count": 77,
          "topics": [
            "Optimism, Hope, and Well-being",
            "Psychology of Moral and Emotional Judgment",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2471322408",
          "year": 2016,
          "title": "Measuring Discounting without Measuring Utility",
          "type": "article",
          "venue": "American Economic Review",
          "cited_by_count": 60,
          "topics": [
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation",
            "Housing Market and Economics"
          ]
        },
        {
          "openalex_id": "W2346499838",
          "year": 2016,
          "title": "An elicitation of utility for quality of life under prospect theory",
          "type": "article",
          "venue": "Journal of Health Economics",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  }
]
