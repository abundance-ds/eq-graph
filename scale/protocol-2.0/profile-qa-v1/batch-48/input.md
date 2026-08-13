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
    "name": "Stella Heemskerk",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2638-RA",
        "title": "The translation of the EQ-TIPS instrument to Dutch ",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5025807986",
      "display_name": "Stella C M Heemskerk",
      "orcid": "0000-0002-1320-8084",
      "reported_affiliation": "Erasmus MC",
      "works_count": 13,
      "top_topics": [
        {
          "topic": "Gastrointestinal motility and disorders",
          "works": 5
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 5
        },
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 3
        },
        {
          "topic": "Urinary Bladder and Prostate Research",
          "works": 3
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 3
        },
        {
          "topic": "Intensive Care Unit Cognitive Disorders",
          "works": 3
        },
        {
          "topic": "COVID-19 Clinical Research Studies",
          "works": 2
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 1
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 1
        },
        {
          "topic": "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
          "works": 1
        },
        {
          "topic": "Gastroesophageal reflux and treatments",
          "works": 1
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sander M. J. van Kuijk",
          "works": 6
        },
        {
          "name": "Juanita A. Haagsma",
          "works": 5
        },
        {
          "name": "Carmen D. Dirksen",
          "works": 4
        },
        {
          "name": "Stéphanie O. Breukink",
          "works": 4
        },
        {
          "name": "Chahinda Ghossein‐Doha",
          "works": 4
        },
        {
          "name": "Marieke S. J. N. Wintjens",
          "works": 4
        },
        {
          "name": "Dorthe O. Klein",
          "works": 4
        },
        {
          "name": "Erwin Birnie",
          "works": 4
        },
        {
          "name": "Gouke J. Bonsel",
          "works": 4
        },
        {
          "name": "Bas C. T. van Bussel",
          "works": 4
        },
        {
          "name": "Susanne van Santen",
          "works": 4
        },
        {
          "name": "Michiel C. Warlé",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413865180",
          "year": 2025,
          "title": "Development and internal validation of a prediction model for post-COVID-19 condition 2 years after infection—results of the CORFU study",
          "type": "article",
          "venue": "Diagnostic and Prognostic Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 Clinical Research Studies",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4415582915",
          "year": 2025,
          "title": "Effectiveness of exercise therapy in patients with thumb carpometacarpal osteoarthritis: A multicenter, randomized controlled trial",
          "type": "article",
          "venue": "Osteoarthritis and Cartilage",
          "cited_by_count": 2,
          "topics": [
            "Orthopedic Surgery and Rehabilitation",
            "Osteoarthritis Treatment and Mechanisms",
            "Tendon Structure and Treatment"
          ]
        },
        {
          "openalex_id": "W4415299974",
          "year": 2025,
          "title": "Health-related quality of life of adult post COVID-19 condition patients three years after infection and patient characteristics associated with change over time: a longitudinal analysis from the CORFU study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4412960350",
          "year": 2025,
          "title": "Hemiarthroplasty versus nonoperative treatment of comminuted proximal humeral fractures: results of the ProCon multicenter randomized clinical trial",
          "type": "article",
          "venue": "Injury",
          "cited_by_count": 1,
          "topics": [
            "Shoulder Injury and Treatment",
            "Hip and Femur Fractures",
            "Shoulder and Clavicle Injuries"
          ]
        },
        {
          "openalex_id": "W4414146329",
          "year": 2025,
          "title": "Two years and counting: a prospective cohort study on the scope and severity of post-COVID symptoms across diverse patient groups in the Netherlands—insights from the CORFU study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 2,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Pharmacological Receptor Mechanisms and Effects"
          ]
        },
        {
          "openalex_id": "W4391109613",
          "year": 2024,
          "title": "Effectiveness, safety and cost‐effectiveness of sacral neuromodulation for idiopathic slow‐transit constipation: a systematic review",
          "type": "review",
          "venue": "Colorectal Disease",
          "cited_by_count": 9,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Urinary Bladder and Prostate Research",
            "Pelvic floor disorders treatments"
          ]
        },
        {
          "openalex_id": "W2565432385",
          "year": 2016,
          "title": "Cost-effectiveness of interventions for treating anxiety disorders: A systematic review",
          "type": "review",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 67,
          "topics": [
            "Mental Health Treatment and Access",
            "Digital Mental Health Interventions",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes"
          ]
        },
        {
          "openalex_id": "W2789680338",
          "year": 2018,
          "title": "Sacral neuromodulation versus personalized conservative treatment in patients with idiopathic slow-transit constipation: study protocol of the No.2-trial, a multicenter open-label randomized controlled trial and cost-effectiveness analysis",
          "type": "article",
          "venue": "International Journal of Colorectal Disease",
          "cited_by_count": 11,
          "topics": [
            "Pelvic floor disorders treatments",
            "Urinary Bladder and Prostate Research",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W2966860069",
          "year": 2019,
          "title": "Heterogeneous outcome reporting in adult slow‐transit constipation studies: Systematic review towards a core outcome set",
          "type": "review",
          "venue": "Journal of Gastroenterology and Hepatology",
          "cited_by_count": 15,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Gastroesophageal reflux and treatments",
            "Inflammatory Bowel Disease"
          ]
        },
        {
          "openalex_id": "W4310360068",
          "year": 2022,
          "title": "Prevalence, pathophysiology, prediction and health-related quality of life of long COVID: study protocol of the longitudinal multiple cohort CORona Follow Up (CORFU) study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 12,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 Clinical Research Studies",
            "Chronic Obstructive Pulmonary Disease (COPD) Research"
          ]
        },
        {
          "openalex_id": "W4388902676",
          "year": 2023,
          "title": "Sacral Neuromodulation Versus Conservative Treatment for Refractory Idiopathic Slow-transit Constipation",
          "type": "article",
          "venue": "Annals of Surgery",
          "cited_by_count": 12,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Pelvic floor disorders treatments",
            "Urinary Bladder and Prostate Research"
          ]
        },
        {
          "openalex_id": "W4402315064",
          "year": 2024,
          "title": "Self-perceived barriers to healthcare access for patients with post COVID-19 condition",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 9,
          "topics": [
            "Long-Term Effects of COVID-19",
            "COVID-19 and Mental Health",
            "Intensive Care Unit Cognitive Disorders"
          ]
        }
      ]
    }
  },
  {
    "name": "Stephen Coons",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2014180",
        "title": "EQ-5D-5L Electronic Measurement Equivalence Project",
        "working_group": "Others"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5052220528",
      "display_name": "Stephen Joel Coons",
      "orcid": "0000-0001-7977-5156",
      "reported_affiliation": "Critical Path Institute",
      "works_count": 203,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 65
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 18
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 17
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 15
        },
        {
          "topic": "Stoma care and complications",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 11
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 11
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 9
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 9
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 7
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 7
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jeffrey Johnson",
          "works": 19
        },
        {
          "name": "Christopher S. Wendel",
          "works": 17
        },
        {
          "name": "Robert S. Krouse",
          "works": 16
        },
        {
          "name": "Ron D. Hays",
          "works": 15
        },
        {
          "name": "Sonya Eremenco",
          "works": 15
        },
        {
          "name": "Marcia Grant",
          "works": 15
        },
        {
          "name": "JoLaine R. Draugalis",
          "works": 14
        },
        {
          "name": "James W. Shaw",
          "works": 12
        },
        {
          "name": "Carol M. Baldwin",
          "works": 12
        },
        {
          "name": "J. Jason Lundy",
          "works": 10
        },
        {
          "name": "Mark C. Hornbrook",
          "works": 10
        },
        {
          "name": "Lisa J. Herrinton",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4391470604",
          "year": 2024,
          "title": "Psychometric Evaluation of the Diary for Irritable Bowel Syndrome Symptoms-Constipation in a Prospective Observational Study",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Gastrointestinal motility and disorders",
            "Music Therapy and Health",
            "Sleep and related disorders"
          ]
        },
        {
          "openalex_id": "W4387806942",
          "year": 2023,
          "title": "Assessing asthma symptoms in children: qualitative research supporting the development of the Pediatric Asthma Diary—Child (PAD-C) and Pediatric Asthma Diary—Observer (PAD-O)",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Asthma and respiratory diseases",
            "Delphi Technique in Research",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W4382197443",
          "year": 2023,
          "title": "Recommendations on the Selection, Development, and Modification of Performance Outcome Assessments: A Good Practices Report of an ISPOR Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 24,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Practices and Patient Outcomes",
            "Pharmaceutical studies and practices"
          ]
        },
        {
          "openalex_id": "W4378803710",
          "year": 2023,
          "title": "Setting International Standards in Analyzing Patient-Reported Outcomes and Quality of Life Endpoints in Cancer Clinical Trials-Innovative Medicines Initiative (SISAQOL-IMI): stakeholder views, objectives, and procedures",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4367307890",
          "year": 2023,
          "title": "Updated Recommendations on Evidence Needed to Support Measurement Comparability Among Modes of Data Collection for Patient-Reported Outcome Measures: A Good Practices Report of an ISPOR Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 39,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4310136326",
          "year": 2022,
          "title": "Approaches to the Assessment of Clinical Benefit of Treatments for Conditions That Have Heterogeneous Symptoms and Impacts: Potential Applications in Rare Disease",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 14,
          "topics": [
            "Genomics and Rare Diseases",
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W746315985",
          "year": 1984,
          "title": "IDENTIFICATION OF CONTINUING EDUCATION CONTENT AND FORMAT PREFERENCES OF ARIZONA PHARMACISTS",
          "type": "dissertation",
          "venue": "UA Campus Repository (The University of Arizona)",
          "cited_by_count": 0,
          "topics": [
            "Foreign Language Teaching Methods",
            "Ophthalmology and Visual Health Research",
            "Indigenous Knowledge Systems and Agriculture"
          ]
        },
        {
          "openalex_id": "W793150613",
          "year": 1986,
          "title": "THE EFFECT OF SELF-CARE INFORMATION ON HEALTH-RELATED ATTITUDES AND BELIEFS.",
          "type": "dissertation",
          "venue": "UA Campus Repository (The University of Arizona)",
          "cited_by_count": 1,
          "topics": [
            "Health and Well-being Studies"
          ]
        },
        {
          "openalex_id": "W2015048180",
          "year": 1986,
          "title": "The need for evaluation of the ultimate impact of continuing pharmaceutical education",
          "type": "article",
          "venue": "Journal of Continuing Education in the Health Professions",
          "cited_by_count": 3,
          "topics": [
            "Evaluation and Performance Assessment",
            "Academic and Historical Perspectives in Psychology"
          ]
        },
        {
          "openalex_id": "W2623313926",
          "year": 1987,
          "title": "The relationship between health beliefs and compliance in a clinical trial",
          "type": "article",
          "venue": "",
          "cited_by_count": 2,
          "topics": [
            "Ethics in medical practice",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W2096782143",
          "year": 2005,
          "title": "US Valuation of the EQ-5D Health States",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 1298,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2046644339",
          "year": 1994,
          "title": "Development of the Kidney Disease Quality of Life (KDQOLTM) Instrument",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1195,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2160289137",
          "year": 2008,
          "title": "Recommendations on Evidence Needed to Support Measurement Equivalence between Electronic and Paper-Based Patient-Reported Outcome (PRO) Measures: ISPOR ePRO Good Research Practices Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 564,
          "topics": [
            "Statistical Methods in Clinical Trials",
            "Meta-analysis and systematic reviews",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2087202287",
          "year": 2012,
          "title": "Recommendations for Incorporating Patient-Reported Outcomes Into Clinical Comparative Effectiveness Research in Adult Oncology",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 488,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2062485189",
          "year": 2008,
          "title": "Best Practices for Survey Research Reports: A Synopsis for Authors and Reviewers",
          "type": "article",
          "venue": "American Journal of Pharmaceutical Education",
          "cited_by_count": 437,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
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
          "openalex_id": "W1587086507",
          "year": 1998,
          "title": "Comparison of the EQ-5D and SF-12 in an adult US sample",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 290,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W2009691381",
          "year": 1998,
          "title": "Valuation of EuroQOL (EQ-5D) Health States in an Adult US Sample",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 254,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Stevanus Pangestu",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1883-RA",
        "title": "Exploring perceived interactions between EQ-5D-5L and bolt-ons: a qualitative valuation study using EQ-PVT",
        "working_group": "Valuation"
      },
      {
        "project_id": "2003-RA",
        "title": "Composite time trade-off valuations for EQ-5D-Y-3L: exploring perspective differences within respondents",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2323-RA",
        "title": "Negative versus positive item phrasing and the ‘use of aids’ reference in the EQ-HWB long form",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2500-RA",
        "title": "The relationship between health literacy and EQ-5D-5L and EQ-HWB-9 outcomes in a general population sample in Hungary",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033743427",
      "display_name": "Stevanus Pangestu",
      "orcid": "0000-0003-2546-9449",
      "reported_affiliation": "Corvinus University of Budapest",
      "works_count": 36,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 11
        },
        {
          "topic": "Corporate Governance and Financial Management",
          "works": 8
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 7
        },
        {
          "topic": "Financial Analysis and Corporate Governance",
          "works": 6
        },
        {
          "topic": "Financial Literacy and Behavior",
          "works": 5
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Corporate Social Responsibility Disclosure",
          "works": 4
        },
        {
          "topic": "Islamic Finance and Banking Studies",
          "works": 4
        },
        {
          "topic": "SMEs Development and Digital Marketing",
          "works": 4
        },
        {
          "topic": "Corporate Finance and Governance",
          "works": 3
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Fanni Rencz",
          "works": 10
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 4
        },
        {
          "name": "Erwin Bramana Karnadi",
          "works": 3
        },
        {
          "name": "Hari Setyowibowo",
          "works": 3
        },
        {
          "name": "Clara Mukuria",
          "works": 3
        },
        {
          "name": "Enggar Putri Harjanti",
          "works": 2
        },
        {
          "name": "F A Nurdiyanto",
          "works": 2
        },
        {
          "name": "Brendan Mulhern",
          "works": 2
        },
        {
          "name": "Aureliano Paolo Finch",
          "works": 2
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 2
        },
        {
          "name": "Bram Roudijk",
          "works": 2
        },
        {
          "name": "Christiana Fara Dharmastuti",
          "works": 2
        }
      ],
      "work_examples": [
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
          "openalex_id": "W4407944051",
          "year": 2025,
          "title": "Associations between financial toxicity, health-related quality of life, and well-being in Indonesian patients with breast cancer",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 6,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4415691556",
          "year": 2025,
          "title": "Child- versus adult-perspective composite time trade-off valuations for the EQ-5D-Y-3L: evidence from the Hungarian valuation study",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4411119891",
          "year": 2025,
          "title": "Development and Use of Cognition Bolt-Ons for the EQ-5D-3L and EQ-5D-5L: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4414802248",
          "year": 2025,
          "title": "Psychometric Properties of Cognition Bolt-Ons for the EQ-5D-3L and EQ-5D-5L: A Systematic Review",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Older Adults Driving Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4415730898",
          "year": 2025,
          "title": "Psychometric testing of the ICECAP-A in patients with coeliac disease: a comparative analysis with EQ-5D-5L",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Celiac Disease Research and Management",
            "Health, psychology, and well-being",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W2896476606",
          "year": 2018,
          "title": "DETERMINAN DAN KONSEKUENSI KONSERVATISME AKUNTANSI: MEKANISME CORPORATE GOVERNANCE DAN MANAJEMEN LABA",
          "type": "article",
          "venue": "",
          "cited_by_count": 9,
          "topics": [
            "Corporate Governance and Financial Management",
            "Corporate Social Responsibility Disclosure",
            "Financial Analysis and Corporate Governance"
          ]
        },
        {
          "openalex_id": "W2891794904",
          "year": 2018,
          "title": "Financial toxicity in Indonesian cancer patients &amp; survivors: How it affects risk attitude",
          "type": "article",
          "venue": "Cogent Medicine",
          "cited_by_count": 6,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2887599169",
          "year": 2018,
          "title": "Herding Behavior in Indonesian Investors",
          "type": "article",
          "venue": "International Research Journal of Business Studies",
          "cited_by_count": 13,
          "topics": [
            "Financial Markets and Investment Strategies",
            "Stock Market Forecasting Methods",
            "Complex Systems and Time Series Analysis"
          ]
        },
        {
          "openalex_id": "W2907802801",
          "year": 2018,
          "title": "THE DETERMINANTS AND CONSEQUENCES OF TAX AVOIDANCE IN INDONESIA:THE EFFECTS OF TOP MANAGEMENT CHARACTERISTICS AND CAPITAL STRUCTURE",
          "type": "article",
          "venue": "Studi Akuntansi dan Keuangan Indonesia",
          "cited_by_count": 5,
          "topics": [
            "Corporate Taxation and Avoidance",
            "Taxation and Compliance Studies",
            "Corporate Finance and Governance"
          ]
        },
        {
          "openalex_id": "W3012981831",
          "year": 2020,
          "title": "The effects of financial literacy and materialism on the savings decision of generation Z Indonesians",
          "type": "article",
          "venue": "Cogent Business & Management",
          "cited_by_count": 82,
          "topics": [
            "Financial Literacy, Pension, Retirement Analysis",
            "Financial Literacy and Behavior",
            "Microfinance and Financial Inclusion"
          ]
        },
        {
          "openalex_id": "W4294591656",
          "year": 2022,
          "title": "Comprehensive Score for Financial Toxicity and Health-Related Quality of Life in Patients With Cancer and Survivors: A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 77,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W3186222307",
          "year": 2021,
          "title": "KECURANGAN PEMBELAJARAN DARING PADA AWAL PANDEMI: DIMENSI FRAUD PENTAGON",
          "type": "article",
          "venue": "Jurnal Pendidikan Akuntansi Indonesia",
          "cited_by_count": 16,
          "topics": [
            "Corporate Governance and Financial Management",
            "Financial Literacy and Behavior"
          ]
        },
        {
          "openalex_id": "W4390296018",
          "year": 2023,
          "title": "Financial Toxicity Experiences of Patients With Cancer in Indonesia: An Interpretive Phenomenological Analysis",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 15,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4405847501",
          "year": 2024,
          "title": "The Psychometric Properties of the EQ-HWB and EQ-HWB-S in Patients With Breast Cancer: A Comparative Analysis With EQ-5D-5L, FACT-8D, and SWEMWBS",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 15,
          "topics": [
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W3174925653",
          "year": 2021,
          "title": "DETEKSI FRAUDULENT FINANCIAL REPORTING MENGGUNAKAN FRAUD PENTAGON",
          "type": "article",
          "venue": "Ultimaccounting Jurnal Ilmu Akuntansi",
          "cited_by_count": 9,
          "topics": [
            "Corporate Governance and Financial Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Stirling Bryan",
    "member_affiliation": "University of British Columbia",
    "is_member": true,
    "projects": [
      {
        "project_id": "164-RA",
        "title": "Can adding routinely collected EQ-5D-5L administrative data improve predictions about who will be a high-cost user of healthcare?",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1787-RA",
        "title": "DOES THE EQ-5D-5L IMPROVE PREDICTIONS OF HOSPITAL READMISSION? AN EQUITY GUIDED ANALYSIS OF OVER 24,000 PATIENTS IN BRITISH COLUMBIA",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5015667412",
      "display_name": "Stirling Bryan",
      "orcid": "0000-0001-7093-3058",
      "reported_affiliation": "Vancouver Coastal Health",
      "works_count": 365,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 125
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 50
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 31
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 24
        },
        {
          "topic": "Digital Radiography and Breast Imaging",
          "works": 22
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 19
        },
        {
          "topic": "Radiology practices and education",
          "works": 19
        },
        {
          "topic": "Radiation Dose and Imaging",
          "works": 16
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 13
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 13
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 13
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        }
      ],
      "frequent_coauthors": [
        {
          "name": "David G. T. Whitehurst",
          "works": 25
        },
        {
          "name": "Martin Buxton",
          "works": 25
        },
        {
          "name": "Craig Mitton",
          "works": 24
        },
        {
          "name": "Mohsen Sadatsafavi",
          "works": 22
        },
        {
          "name": "Gwyneth C. Weatherburn",
          "works": 20
        },
        {
          "name": "Jonathan Mant",
          "works": 19
        },
        {
          "name": "Jennifer C. Davis",
          "works": 19
        },
        {
          "name": "Louisa Edwards",
          "works": 19
        },
        {
          "name": "Nick Bansback",
          "works": 17
        },
        {
          "name": "Richard Hobbs",
          "works": 16
        },
        {
          "name": "Pelham Barton",
          "works": 16
        },
        {
          "name": "Sue Jowett",
          "works": 15
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
          "openalex_id": "W7164807073",
          "year": 2026,
          "title": "Guidance from an informed public on collecting and sharing PGx test results for major depressive disorder: “It’s no different from your blood type”",
          "type": "article",
          "venue": "Pharmacogenomics",
          "cited_by_count": 0,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Ethics in Clinical Research",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W7164814085",
          "year": 2026,
          "title": "Guidance from an informed public on collecting and sharing PGx test results for major depressive disorder: “It’s no different from your blood type”",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7164818097",
          "year": 2026,
          "title": "Guidance from an informed public on collecting and sharing PGx test results for major depressive disorder: “It’s no different from your blood type”",
          "type": "dataset",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7128296445",
          "year": 2026,
          "title": "HLA Experts’ Perspectives on Precision Medicine and Molecular Matching in Kidney Transplantation: A Qualitative Study",
          "type": "article",
          "venue": "Canadian Journal of Kidney Health and Disease",
          "cited_by_count": 0,
          "topics": [
            "Renal Transplantation Outcomes and Treatments",
            "Organ Donation and Transplantation",
            "Cytomegalovirus and herpesvirus research"
          ]
        },
        {
          "openalex_id": "W7160250080",
          "year": 2026,
          "title": "Pharmacogenomic testing for major depressive disorder in British Columbia, Canada: Recommendations from a public deliberation",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 1,
          "topics": [
            "Pharmacogenetics and Drug Metabolism",
            "Ethics in Clinical Research",
            "Genetic Associations and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2014135307",
          "year": 1964,
          "title": "TFX --A Case in Policy Level Decision-Making.",
          "type": "article",
          "venue": "Academy of Management Journal",
          "cited_by_count": 8,
          "topics": [
            "Technology Assessment and Management",
            "Defense, Military, and Policy Studies",
            "Military Strategy and Technology"
          ]
        },
        {
          "openalex_id": "W1559910866",
          "year": 1990,
          "title": "Complications of pregnancy in infertile couples: Routine treatment versus assisted reproduction",
          "type": "article",
          "venue": "International Journal of Gynecology & Obstetrics",
          "cited_by_count": 21,
          "topics": [
            "Assisted Reproductive Technology and Twin Pregnancy",
            "Ectopic Pregnancy Diagnosis and Management",
            "Prenatal Screening and Diagnostics"
          ]
        },
        {
          "openalex_id": "W2012971106",
          "year": 1991,
          "title": "Chiropody and the QALY: a case study in assigning categories of disability and distress to patients",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1975130311",
          "year": 1992,
          "title": "&lt;title&gt;Evaluation of a hospital-wide PACS: costs and benefits of the Hammersmith PACS installation&lt;/title&gt;",
          "type": "conference-paper",
          "venue": "Proceedings of SPIE, the International Society for Optical Engineering/Proceedings of SPIE",
          "cited_by_count": 11,
          "topics": [
            "Radiation Dose and Imaging",
            "Radiology practices and education",
            "Digital Radiography and Breast Imaging"
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
          "openalex_id": "W2157488387",
          "year": 2010,
          "title": "Telemonitoring and self-management in the control of hypertension (TASMINH2): a randomised controlled trial",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 615,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Telemedicine and Telehealth Implementation",
            "Cardiac Health and Mental Health"
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
          "openalex_id": "W2018796325",
          "year": 2005,
          "title": "A randomised controlled trial and cost-effectiveness study of systematic screening (targeted and total population screening) versus routine practice for the detection of atrial fibrillation in people aged 65 and over. The SAFE study",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 436,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac pacing and defibrillation studies",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W2162254515",
          "year": 2006,
          "title": "A systematic review of the effectiveness of adalimumab, etanercept and infliximab for the treatment of rheumatoid arthritis in adults and an economic evaluation of their cost-effectiveness",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 411,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments",
            "Autoimmune and Inflammatory Disorders Research"
          ]
        },
        {
          "openalex_id": "W2121607038",
          "year": 2014,
          "title": "Effect of Self-monitoring and Medication Self-titration on Systolic Blood Pressure in Hypertensive Patients at High Risk of Cardiovascular Disease",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 411,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Sodium Intake and Health",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W2020061893",
          "year": 2007,
          "title": "Screening versus routine practice in detection of atrial fibrillation in patients aged 65 or over: cluster randomised controlled trial",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 409,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Acute Myocardial Infarction Research",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W2007090126",
          "year": 2004,
          "title": "Modelling in the economic evaluation of health care: selecting the appropriate approach",
          "type": "article",
          "venue": "Journal of Health Services Research & Policy",
          "cited_by_count": 289,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Operations and Scheduling Optimization",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Sun Sun",
    "member_affiliation": "Parexel/Umeå University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1561-RA",
        "title": "EQ-5D as an add-on generic measure in psoriasis, when excellent disease-specific measures are present: its psychometrical and clinical value in a representative Swedish cohort",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5081188742",
      "display_name": "Sun Sun",
      "orcid": "0000-0001-5948-3025",
      "reported_affiliation": "",
      "works_count": 97,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 17
        },
        {
          "topic": "Microgrid Control and Optimization",
          "works": 9
        },
        {
          "topic": "Smart Grid Energy Management",
          "works": 8
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 7
        },
        {
          "topic": "Electric Vehicles and Infrastructure",
          "works": 7
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 6
        },
        {
          "topic": "Cooperative Communication and Network Coding",
          "works": 6
        },
        {
          "topic": "Advanced Battery Technologies Research",
          "works": 5
        },
        {
          "topic": "Full-Duplex Wireless Communications",
          "works": 5
        },
        {
          "topic": "Bariatric Surgery and Outcomes",
          "works": 5
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 4
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kristina Burström",
          "works": 12
        },
        {
          "name": "Min Dong",
          "works": 12
        },
        {
          "name": "Ben Liang",
          "works": 12
        },
        {
          "name": "Yang Cao",
          "works": 12
        },
        {
          "name": "Lars Lindholm",
          "works": 11
        },
        {
          "name": "Klas-Göran Sahlèn",
          "works": 8
        },
        {
          "name": "Zhang Zhang",
          "works": 8
        },
        {
          "name": "Xiaoyu Tang",
          "works": 7
        },
        {
          "name": "Mevludin Memedi",
          "works": 7
        },
        {
          "name": "Ayako Hiyoshi",
          "works": 7
        },
        {
          "name": "Scott Montgomery",
          "works": 6
        },
        {
          "name": "Jiaying Chen",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7154605232",
          "year": 2026,
          "title": "Additional file 1 of Evaluation of COVID-19 policy efficiency in 27 European OECD countries: a data envelopment analysis",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Efficiency Analysis Using DEA",
            "COVID-19 Pandemic Impacts",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W7154605954",
          "year": 2026,
          "title": "Additional file 1 of Evaluation of COVID-19 policy efficiency in 27 European OECD countries: a data envelopment analysis",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Efficiency Analysis Using DEA",
            "COVID-19 Pandemic Impacts",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W7127993433",
          "year": 2026,
          "title": "Context Forcing: Consistent Autoregressive Video Generation with Long Context",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Generative Adversarial Networks and Image Synthesis",
            "Advanced Vision and Imaging",
            "Human Pose and Action Recognition"
          ]
        },
        {
          "openalex_id": "W7128096778",
          "year": 2026,
          "title": "Context Forcing: Consistent Autoregressive Video Generation with Long Context",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 0,
          "topics": [
            "Generative Adversarial Networks and Image Synthesis",
            "Advanced Vision and Imaging",
            "Human Pose and Action Recognition"
          ]
        },
        {
          "openalex_id": "W7153439362",
          "year": 2026,
          "title": "Evaluation of COVID-19 policy efficiency in 27 European OECD countries: a data envelopment analysis",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 1,
          "topics": [
            "Efficiency Analysis Using DEA",
            "COVID-19 Pandemic Impacts",
            "Business and Economic Development"
          ]
        },
        {
          "openalex_id": "W7154605226",
          "year": 2026,
          "title": "Evaluation of COVID-19 policy efficiency in 27 European OECD countries: a data envelopment analysis",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W2335564502",
          "year": 1987,
          "title": "High T<sub>c</sub> Superconductivity and S-I Transition in Ba–Y–Cu–O",
          "type": "conference-abstract",
          "venue": "Japanese Journal of Applied Physics",
          "cited_by_count": 2,
          "topics": [
            "Magnetic and transport properties of perovskites and related materials",
            "Physics of Superconductivity and Magnetism",
            "Advanced Condensed Matter Physics"
          ]
        },
        {
          "openalex_id": "W2327219964",
          "year": 1987,
          "title": "High T<sub>c</sub> Superconductivity of Ba<sub>x</sub>Y<sub>1-x</sub>CuO<sub>3-y</sub>",
          "type": "conference-abstract",
          "venue": "Japanese Journal of Applied Physics",
          "cited_by_count": 3,
          "topics": [
            "Physics of Superconductivity and Magnetism",
            "Magnetic properties of thin films",
            "Advanced Condensed Matter Physics"
          ]
        },
        {
          "openalex_id": "W2384803948",
          "year": 2001,
          "title": "Optimization of MIS Design Based on Database",
          "type": "article",
          "venue": "Jisuanji yingyong yanjiu",
          "cited_by_count": 1,
          "topics": [
            "Advanced Computational Techniques and Applications",
            "Extenics and Innovation Methods",
            "Industrial Technology and Control Systems"
          ]
        },
        {
          "openalex_id": "W2906041666",
          "year": 2002,
          "title": "Existing practices of general practitioners on diagnosis and treatment of tuberculosis in Yangon",
          "type": "article",
          "venue": "",
          "cited_by_count": 4,
          "topics": [
            "Tuberculosis Research and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2130267399",
          "year": 2013,
          "title": "Swedish experience-based value sets for EQ-5D health states",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 352,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2043007588",
          "year": 2010,
          "title": "Population health status in China: EQ-5D results, by age, sex and socio-economic status, from the National Health Services Survey 2008",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 235,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2804874827",
          "year": 2018,
          "title": "Time Trade-Off Value Set for EQ-5D-3L Based on a Nationally Representative Chinese Population Survey",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 177,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Quality Function Deployment in Product Design"
          ]
        },
        {
          "openalex_id": "W1970182218",
          "year": 2015,
          "title": "Subjective Well-Being and Its Association with Subjective Health Status, Age, Sex, Region, and Socio-economic Characteristics in a Chinese Population Study",
          "type": "article",
          "venue": "Journal of Happiness Studies",
          "cited_by_count": 166,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Health disparities and outcomes",
            "Mental Health Research Topics"
          ]
        },
        {
          "openalex_id": "W2660982722",
          "year": 2017,
          "title": "Alfapump® system vs. large volume paracentesis for refractory ascites: A multicenter randomized controlled study",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 116,
          "topics": [
            "Liver Disease and Transplantation",
            "Clinical Nutrition and Gastroenterology",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W3013295362",
          "year": 2020,
          "title": "An EQ-5D-5L Value Set for Vietnam",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 112,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W1984441731",
          "year": 2011,
          "title": "Regional differences in health status in China: Population health-related quality of life results from the National Health Services Survey 2008",
          "type": "article",
          "venue": "Health & Place",
          "cited_by_count": 104,
          "topics": [
            "Health disparities and outcomes",
            "Healthcare Systems and Reforms",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3099654264",
          "year": 2016,
          "title": "1Distributed Real-Time Power Balancing in Renewable-Integrated Power Grids with Storage and Flexible Loads",
          "type": "article",
          "venue": "",
          "cited_by_count": 103,
          "topics": [
            "Smart Grid Energy Management",
            "Microgrid Control and Optimization",
            "Electric Vehicles and Infrastructure"
          ]
        }
      ]
    }
  }
]
