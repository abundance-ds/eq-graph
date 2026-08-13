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
    "name": "Peep Stalmeier",
    "member_affiliation": "Radboudumc",
    "is_member": true,
    "projects": [
      {
        "project_id": "115-RA",
        "title": "Facing death to understand the construct validity of the (c)TTO method: a conceptual approach",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1487-RA",
        "title": "Terror Management Theory: a new observation window on TTO and VAS",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013010",
        "title": "States worse than Dead: Exposing the measurement properties of the Better than Dead preference method",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015150",
        "title": "Values for severe states: a methodological and cultural view",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5013523692",
      "display_name": "Peep F. M. Stalmeier",
      "orcid": "0000-0002-7553-562X",
      "reported_affiliation": "Radboud University Nijmegen",
      "works_count": 163,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 47
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 43
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 37
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 18
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 16
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 14
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 14
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 13
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 13
        },
        {
          "topic": "Prostate Cancer Diagnosis and Treatment",
          "works": 10
        },
        {
          "topic": "Color perception and design",
          "works": 9
        },
        {
          "topic": "Visual perception and processing mechanisms",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Linda Oostendorp",
          "works": 25
        },
        {
          "name": "W.A.J. van Daal",
          "works": 17
        },
        {
          "name": "Ivonne J. H. Schoenaker",
          "works": 17
        },
        {
          "name": "Petronella Beatrix Ottevanger",
          "works": 15
        },
        {
          "name": "Julia J. van Tol‐Geerdink",
          "works": 14
        },
        {
          "name": "Petronella B. Ottevanger",
          "works": 14
        },
        {
          "name": "A. Donders",
          "works": 14
        },
        {
          "name": "Agnes Wouw",
          "works": 14
        },
        {
          "name": "Tineke Smilde",
          "works": 14
        },
        {
          "name": "Winette van der Graaf",
          "works": 14
        },
        {
          "name": "J.W.H. Leer",
          "works": 13
        },
        {
          "name": "Bram Roudijk",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7152736398",
          "year": 2026,
          "title": "Effect of a patient decision aid on shared decision making in patients with differentiated thyroid cancer: a randomized controlled trial",
          "type": "article",
          "venue": "The Oncologist",
          "cited_by_count": 0,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Clinical Reasoning and Diagnostic Skills",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W7127301341",
          "year": 2026,
          "title": "Unconscious death thoughts: Do they play a role in time trade-off and visual analogue scale scores for health?",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Death Anxiety and Social Exclusion",
            "Grief, Bereavement, and Mental Health",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4416137330",
          "year": 2025,
          "title": "Do Worse than Dead Values Add Relevant Information in (Composite) Time-Tradeoff Valuations?",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Financial Reporting and Valuation Research",
            "Credit Risk and Financial Regulations",
            "Auditing, Earnings Management, Governance"
          ]
        },
        {
          "openalex_id": "W4407947786",
          "year": 2025,
          "title": "Making Composite Time Trade-Off Sensitive for Worse-than-Dead Health States",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Financial Impacts of Cancer"
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
          "openalex_id": "W4403443095",
          "year": 2024,
          "title": "What Makes the Time Tradeoff Tick? A Sociopsychological Explanation",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 2,
          "topics": [
            "Death Anxiety and Social Exclusion",
            "Suicide and Self-Harm Studies",
            "Religion, Spirituality, and Psychology"
          ]
        },
        {
          "openalex_id": "W1973054456",
          "year": 1980,
          "title": "A tandem mass spectrometer for collision-induced dissociation",
          "type": "article",
          "venue": "International Journal of Mass Spectrometry and Ion Physics",
          "cited_by_count": 50,
          "topics": [
            "Mass Spectrometry Techniques and Applications",
            "Spectroscopy and Laser Applications",
            "Advanced Chemical Physics Studies"
          ]
        },
        {
          "openalex_id": "W2753687854",
          "year": 1980,
          "title": "High Sensitivity in CID Mass Spectrometry, Structure Analysis of Pyrolysis Fragments",
          "type": "article",
          "venue": "Zeitschrift für Naturforschung C",
          "cited_by_count": 16,
          "topics": [
            "Mass Spectrometry Techniques and Applications",
            "Molecular Biology Techniques and Applications",
            "Mycobacterium research and diagnosis"
          ]
        },
        {
          "openalex_id": "W2085928903",
          "year": 1988,
          "title": "Binocular rivalry with chromatic contours",
          "type": "article",
          "venue": "Perception & Psychophysics",
          "cited_by_count": 8,
          "topics": [
            "Visual perception and processing mechanisms",
            "Color Science and Applications",
            "Color perception and design"
          ]
        },
        {
          "openalex_id": "W2095527279",
          "year": 1988,
          "title": "Large colour differences measured by spontaneous gestalt formation",
          "type": "article",
          "venue": "Color Research & Application",
          "cited_by_count": 48,
          "topics": [
            "Visual perception and processing mechanisms",
            "Color perception and design",
            "Color Science and Applications"
          ]
        },
        {
          "openalex_id": "W2113217158",
          "year": 2002,
          "title": "Extended Transthoracic Resection Compared with Limited Transhiatal Resection for Adenocarcinoma of the Esophagus",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 1647,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Esophageal and GI Pathology",
            "Metastasis and carcinoma case studies"
          ]
        },
        {
          "openalex_id": "W2147145155",
          "year": 2004,
          "title": "Is a single-item visual analogue scale as valid, reliable and responsive as multi-item scales in measuring quality of life?",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 741,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Cancer survivorship and care",
            "Gastroesophageal reflux and treatments"
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
          "openalex_id": "W2763882359",
          "year": 2017,
          "title": "Standards for UNiversal reporting of patient Decision Aid Evaluation studies: the development of SUNDAE Checklist",
          "type": "article",
          "venue": "BMJ Quality & Safety",
          "cited_by_count": 214,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W2133262035",
          "year": 2004,
          "title": "Quality of Life After Transhiatal Compared With Extended Transthoracic Resection for Adenocarcinoma of the Esophagus",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 171,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Gastroesophageal reflux and treatments",
            "Esophageal and GI Pathology"
          ]
        },
        {
          "openalex_id": "W2134382710",
          "year": 2004,
          "title": "Randomized Trial of a Shared Decision-Making Intervention Consisting of Trade-Offs and Individualized Treatment Information for <i>BRCA1/2</i> Mutation Carriers",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 120,
          "topics": [
            "BRCA gene mutations in cancer",
            "Patient-Provider Communication in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2125541970",
          "year": 2003,
          "title": "Palliative chemotherapy or best supportive care? A prospective study explaining patients' treatment preference and choice",
          "type": "article",
          "venue": "British Journal of Cancer",
          "cited_by_count": 116,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Patient-Provider Communication in Healthcare",
            "Patient Dignity and Privacy"
          ]
        }
      ]
    }
  },
  {
    "name": "Philip Clarke",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "118-RA",
        "title": "An international comparison of the impacts of COVID-19 using EQ-5D",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1415-RA",
        "title": "Using the EQ-5D to understand how health impacts on preventative behaviour in rural Ghana as part of large randomized experiment of incentives for TB screening",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "310-RA",
        "title": "CANDOUR study: Using EQ-5D-5L to assess the impact of global use of COVID-19 vaccines on health-related quality of life",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5072230333",
      "display_name": "Philip Clarke",
      "orcid": "0000-0002-7555-5348",
      "reported_affiliation": "The University of Melbourne",
      "works_count": 500,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 96
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 45
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 43
        },
        {
          "topic": "Global Health Care Issues",
          "works": 41
        },
        {
          "topic": "Diabetes, Cardiovascular Risks, and Lipoproteins",
          "works": 37
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 35
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 34
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 34
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 28
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 27
        },
        {
          "topic": "Health and Medical Research Impacts",
          "works": 21
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 20
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Thomas Lung",
          "works": 44
        },
        {
          "name": "Paul Glasziou",
          "works": 43
        },
        {
          "name": "Adrian Barnett",
          "works": 43
        },
        {
          "name": "Richard Stevens",
          "works": 41
        },
        {
          "name": "Laurence Roope",
          "works": 41
        },
        {
          "name": "Andrew Farmer",
          "works": 40
        },
        {
          "name": "Rafael Perera",
          "works": 35
        },
        {
          "name": "Jennifer Hirst",
          "works": 35
        },
        {
          "name": "Brian Shine",
          "works": 35
        },
        {
          "name": "Raymond Duch",
          "works": 27
        },
        {
          "name": "Alastair Gray",
          "works": 26
        },
        {
          "name": "Emily McFadden",
          "works": 25
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164053191",
          "year": 2026,
          "title": "Attitudes to mandatory COVID-19 vaccination in early life: findings from the multi-country cross-sectional CANDOUR study",
          "type": "article",
          "venue": "Health Promotion International",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "COVID-19 and Mental Health",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W7150822330",
          "year": 2026,
          "title": "Public preferences for saving lives versus life-years: evidence from a person-trade-off experiment in 12 countries during the COVID-19 pandemic",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4412078418",
          "year": 2025,
          "title": "Accuracy of online surveys in predicting COVID-19 uptake and demand: A cohort study investigating vaccine sentiments and switching in 13 countries from 2020 to 2022",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "COVID-19 Pandemic Impacts",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W4416152965",
          "year": 2025,
          "title": "Author response for \"Estimating the risk of cardiovascular outcomes and all-cause mortality in individuals with type 2 diabetes: Validation of the UKPDS Outcomes Model using TECOS and EXSCEL data\"",
          "type": "peer-review",
          "venue": "",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4416153254",
          "year": 2025,
          "title": "Author response for \"Estimating the risk of cardiovascular outcomes and all-cause mortality in individuals with type 2 diabetes: Validation of the UKPDS Outcomes Model using TECOS and EXSCEL data\"",
          "type": "peer-review",
          "venue": "",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4417050333",
          "year": 2025,
          "title": "Corrigendum to “Accuracy of online surveys in predicting COVID-19 vaccine uptake and demand: A cohort study investigating vaccine sentiments and switching in 13 countries from 2020 to 2022” [Vaccines 62 (2025) 127450]",
          "type": "erratum",
          "venue": "Vaccine",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Data-Driven Disease Surveillance",
            "COVID-19 Pandemic Impacts"
          ]
        },
        {
          "openalex_id": "W1998801951",
          "year": 1955,
          "title": "Fallacies in nutritional requirement experimentation",
          "type": "article",
          "venue": "Archives of Biochemistry and Biophysics",
          "cited_by_count": 0,
          "topics": [
            "Child Nutrition and Feeding Issues",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2509507593",
          "year": 1969,
          "title": "Some Errors in Gauge Calibration",
          "type": "report",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Scientific Measurement and Uncertainty Evaluation",
            "Advanced Measurement and Metrology Techniques",
            "Advanced Sensor Technologies Research"
          ]
        },
        {
          "openalex_id": "W2095393956",
          "year": 1977,
          "title": "Powder neutron diffraction–refinement of the total pattern",
          "type": "article",
          "venue": "Journal of Applied Crystallography",
          "cited_by_count": 11,
          "topics": [
            "X-ray Diffraction in Crystallography",
            "Nuclear Physics and Applications",
            "Crystallography and Radiation Phenomena"
          ]
        },
        {
          "openalex_id": "W2007921491",
          "year": 1979,
          "title": "Deuterium β-alumina, DAl11O17: Atom location and structure refinement by powder neutron diffraction",
          "type": "article",
          "venue": "Journal of Solid State Chemistry",
          "cited_by_count": 16,
          "topics": [
            "Nuclear materials and radiation effects",
            "X-ray Diffraction in Crystallography",
            "Ferroelectric and Piezoelectric Materials"
          ]
        },
        {
          "openalex_id": "W2126252058",
          "year": 2004,
          "title": "A model to estimate the lifetime health outcomes of patients with Type 2 diabetes: the United Kingdom Prospective Diabetes Study (UKPDS) Outcomes Model (UKPDS no. 68)",
          "type": "article",
          "venue": "Diabetologia",
          "cited_by_count": 622,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2104706609",
          "year": 2002,
          "title": "Adrenocortical, Autonomic, and Inflammatory Causes of the Metabolic Syndrome",
          "type": "article",
          "venue": "Circulation",
          "cited_by_count": 535,
          "topics": [
            "Stress Responses and Cortisol",
            "Heart Rate Variability and Autonomic Control",
            "Cardiac Health and Mental Health"
          ]
        },
        {
          "openalex_id": "W2091237544",
          "year": 2013,
          "title": "UKPDS Outcomes Model 2: a new version of a model to simulate lifetime health outcomes of patients with type 2 diabetes mellitus using data from the 30 year United Kingdom Prospective Diabetes Study: UKPDS 82",
          "type": "article",
          "venue": "Diabetologia",
          "cited_by_count": 501,
          "topics": [
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W3038080478",
          "year": 2020,
          "title": "Effects of Allopurinol on the Progression of Chronic Kidney Disease",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 471,
          "topics": [
            "Gout, Hyperuricemia, Uric Acid",
            "Kidney Stones and Urolithiasis Treatments",
            "Chronic Kidney Disease and Diabetes"
          ]
        },
        {
          "openalex_id": "W4236501586",
          "year": 2002,
          "title": "Estimating Utility Values for Health States of Type 2 Diabetic Patients Using the EQ-5D (UKPDS 62)",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 432,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2062033943",
          "year": 2002,
          "title": "Estimating Utility Values for Health States of Type 2 Diabetic Patients Using the EQ-5D (UKPDS 62)",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 427,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W2060139770",
          "year": 2010,
          "title": "Applied Methods of Cost-effectiveness Analysis in Healthcare",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 347,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1971883474",
          "year": 2002,
          "title": "Missing.... presumed at random: cost‐analysis of incomplete data",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 347,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Philip Powell",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1711-RA",
        "title": "A Scoping Review of Stakeholder Engagement in Health State Valuation: What Is Currently Being Done and What Could Be Done Better?",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1877-RA",
        "title": "Is the EQ-VT TTO Protocol Suitable for Use in 16- and 17-Year-Old Adolescents?",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "307-RA",
        "title": "Who Should Be Asked in Health State Valuation Exercises for Children and Adolescents? Views of the Adult and Adolescent General Public",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5072704582",
      "display_name": "Philip A. Powell",
      "orcid": "0000-0003-1169-3431",
      "reported_affiliation": "Philips (Finland)",
      "works_count": 116,
      "top_topics": [
        {
          "topic": "Psychology of Moral and Emotional Judgment",
          "works": 24
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Muscle Physiology and Disorders",
          "works": 9
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 8
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 7
        },
        {
          "topic": "Emotions and Moral Behavior",
          "works": 6
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 5
        },
        {
          "topic": "Stroke Rehabilitation and Recovery",
          "works": 5
        },
        {
          "topic": "Optimism, Hope, and Well-being",
          "works": 5
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 5
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 5
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jill Carlton",
          "works": 37
        },
        {
          "name": "Donna Rowen",
          "works": 24
        },
        {
          "name": "Paul G. Overton",
          "works": 17
        },
        {
          "name": "Jane Simpson",
          "works": 14
        },
        {
          "name": "Jennifer Roberts",
          "works": 12
        },
        {
          "name": "John Brazier",
          "works": 12
        },
        {
          "name": "F.G. Chandler",
          "works": 8
        },
        {
          "name": "Emily McDool",
          "works": 6
        },
        {
          "name": "Lambros Lazuras",
          "works": 6
        },
        {
          "name": "Antonia Ypsilanti",
          "works": 6
        },
        {
          "name": "Nathan S. Consedine",
          "works": 6
        },
        {
          "name": "J. Godfrey",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7163164575",
          "year": 2026,
          "title": "A Systematic Literature Review of Health Economic Modelling Approaches Used to Evaluate Treatment Resistant and Uncontrolled Hypertension: A Critical Appraisal and Considerations for the Design of Future Model Analyses",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 0,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Heart Failure Treatment and Management",
            "Sodium Intake and Health"
          ]
        },
        {
          "openalex_id": "W7162632676",
          "year": 2026,
          "title": "Assessing the association of physical distancing to avoid COVID-19 with health-related quality of life in immunocompromised adolescents: results from the cross-sectional observational EAGLE study",
          "type": "article",
          "venue": "Frontiers in Pediatrics",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "COVID-19 and Mental Health",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W7165190745",
          "year": 2026,
          "title": "Assessing the association of physical distancing to avoid COVID-19 with health-related quality of life in immunocompromised adults: results from the cross-sectional observational EAGLE study",
          "type": "article",
          "venue": "BMJ Public Health",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "Long-Term Effects of COVID-19",
            "Multiple Sclerosis Research Studies"
          ]
        },
        {
          "openalex_id": "W7140369020",
          "year": 2026,
          "title": "Measuring health-related quality of life in facioscapulohumeral muscular dystrophy: a COSMIN systematic review and conceptual framework",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Muscle Physiology and Disorders",
            "Cardiomyopathy and Myosin Studies",
            "Muscle activation and electromyography studies"
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
          "openalex_id": "W7162488726",
          "year": 2026,
          "title": "SAT-301 Investigating the burden of illness in primary sclerosing cholangitis (PSC): a multinational study",
          "type": "conference-abstract",
          "venue": "Journal of Hepatology",
          "cited_by_count": 0,
          "topics": [
            "Liver Diseases and Immunity",
            "Gallbladder and Bile Duct Disorders",
            "Systemic Lupus Erythematosus Research"
          ]
        },
        {
          "openalex_id": "W3033706734",
          "year": 1973,
          "title": "Paradise Lost and the book of Job: A comparison of forbidden knowledge, sin intercession, restoration and theodicy",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Theology and Philosophy of Evil"
          ]
        },
        {
          "openalex_id": "W1586188118",
          "year": 1979,
          "title": "The practical writer: Paragraph to theme",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 0,
          "topics": [
            "Discourse Analysis in Language Studies",
            "Publishing and Scholarly Communication",
            "Educational Leadership and Practices"
          ]
        },
        {
          "openalex_id": "W1634756990",
          "year": 1981,
          "title": "Guide to effective solar heating and cooling practice",
          "type": "report",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Solar Thermal and Photovoltaic Systems",
            "Photovoltaic System Optimization Techniques",
            "Solar Radiation and Photovoltaics"
          ]
        },
        {
          "openalex_id": "W1503528599",
          "year": 1981,
          "title": "Writing Research Papers: A Practical Guide",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 4,
          "topics": [
            "Academic Writing and Publishing"
          ]
        },
        {
          "openalex_id": "W2519027667",
          "year": 2016,
          "title": "Patient-Reported Outcomes after Monitoring, Surgery, or Radiotherapy for Prostate Cancer",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 1341,
          "topics": [
            "Prostate Cancer Diagnosis and Treatment",
            "Advanced Radiotherapy Techniques",
            "Cancer survivorship and care"
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
          "openalex_id": "W2553027802",
          "year": 2016,
          "title": "Situational determinants of cognitive, affective, and compassionate empathy in naturalistic digital interactions",
          "type": "article",
          "venue": "Computers in Human Behavior",
          "cited_by_count": 134,
          "topics": [
            "Media Influence and Health",
            "Communication in Education and Healthcare",
            "Team Dynamics and Performance"
          ]
        },
        {
          "openalex_id": "W4323928304",
          "year": 2023,
          "title": "Patient-Reported Outcomes 12 Years after Localized Prostate Cancer Treatment",
          "type": "article",
          "venue": "NEJM Evidence",
          "cited_by_count": 102,
          "topics": [
            "Prostate Cancer Diagnosis and Treatment",
            "Prostate Cancer Treatment and Research",
            "Bladder and Urothelial Cancer Treatments"
          ]
        },
        {
          "openalex_id": "W2892337451",
          "year": 2018,
          "title": "Self-disgust as a potential mechanism explaining the association between loneliness and depression",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 80,
          "topics": [
            "Psychology of Moral and Emotional Judgment",
            "Face Recognition and Perception",
            "Aging and Gerontology Research"
          ]
        },
        {
          "openalex_id": "W2791378344",
          "year": 2018,
          "title": "Individual differences in emotion regulation moderate the associations between empathy and affective distress",
          "type": "article",
          "venue": "Motivation and Emotion",
          "cited_by_count": 78,
          "topics": [
            "Child and Adolescent Psychosocial and Emotional Development",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Emotional Intelligence and Performance"
          ]
        },
        {
          "openalex_id": "W2048312910",
          "year": 2013,
          "title": "When disgust leads to dysphoria: A three-wave longitudinal study assessing the temporal relationship between self-disgust and depressive symptoms",
          "type": "article",
          "venue": "Cognition & Emotion",
          "cited_by_count": 67,
          "topics": [
            "Psychology of Moral and Emotional Judgment",
            "Humor Studies and Applications",
            "Emotions and Moral Behavior"
          ]
        },
        {
          "openalex_id": "W1561215207",
          "year": 2013,
          "title": "The Revolting Self: An Interpretative Phenomenological Analysis of the Experience of Self‐Disgust in Females With Depressive Symptoms",
          "type": "article",
          "venue": "Journal of Clinical Psychology",
          "cited_by_count": 65,
          "topics": [
            "Psychology of Moral and Emotional Judgment",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Emotions and Moral Behavior"
          ]
        }
      ]
    }
  },
  {
    "name": "Piyameth Dilokthornsakul",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1982-VS",
        "title": "DEVELOPMENT OF EQ-5D-Y VALUE SET FOR THAI CHILDREN AGED 8 – 15 YEARS OLD",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5013970219",
      "display_name": "Piyameth Dilokthornsakul",
      "orcid": "0000-0002-6981-1771",
      "reported_affiliation": "Nakornping Hospital",
      "works_count": 175,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 28
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 13
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 12
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 11
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 11
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 11
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 8
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 7
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 6
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 6
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 6
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 6
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nathorn Chaiyakunapruk",
          "works": 84
        },
        {
          "name": "Teerapon Dhippayom",
          "works": 32
        },
        {
          "name": "Unchalee Permsuwan",
          "works": 22
        },
        {
          "name": "Surasak Saokaew",
          "works": 17
        },
        {
          "name": "Rosarin Sruamsiri",
          "works": 14
        },
        {
          "name": "Ratree Sawangjit",
          "works": 14
        },
        {
          "name": "Jonathan D. Campbell",
          "works": 11
        },
        {
          "name": "Surakit Nathisuwan",
          "works": 9
        },
        {
          "name": "Mantiwee Nimworapan",
          "works": 9
        },
        {
          "name": "Nilawan Upakdee",
          "works": 9
        },
        {
          "name": "Khachen Kongpakwattana",
          "works": 8
        },
        {
          "name": "Witoo Dilokthornsakul",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7128532548",
          "year": 2026,
          "title": "Budget Impact of Secukinumab in Psoriatic Arthritis Patients with Contraindication to TNF-Alpha Inhibitors",
          "type": "article",
          "venue": "ClinicoEconomics and Outcomes Research",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7166664690",
          "year": 2026,
          "title": "Cost-Effectiveness of Vaccine for the Prevention of Herpes Zoster in Kidney Transplant Recipients in Thailand",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Herpesvirus Infections and Treatments",
            "Cytomegalovirus and herpesvirus research",
            "Facial Nerve Paralysis Treatment and Research"
          ]
        },
        {
          "openalex_id": "W7121497720",
          "year": 2026,
          "title": "Economic Evaluation and Budget Impact Analysis of Secukinumab as a Second-Line Treatment Among Patients With Psoriatic Arthritis Who Were Tumor Necrosis Factor Inadequate Responders in Thailand",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        },
        {
          "openalex_id": "W7128709601",
          "year": 2026,
          "title": "Economic evaluation of single-inhaler triple therapy for chronic obstructive pulmonary disease in Thailand",
          "type": "article",
          "venue": "BMJ Open Respiratory Research",
          "cited_by_count": 0,
          "topics": [
            "Inhalation and Respiratory Drug Delivery",
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W7164817081",
          "year": 2026,
          "title": "Electrospun fibers as cosmetic carriers: A systematic review of formulation components and clinical evidence",
          "type": "review",
          "venue": "Drug Delivery and Translational Research",
          "cited_by_count": 0,
          "topics": [
            "Electrospun Nanofibers in Biomedical Applications",
            "Facial Rejuvenation and Surgery Techniques",
            "Advancements in Transdermal Drug Delivery"
          ]
        },
        {
          "openalex_id": "W7125509416",
          "year": 2026,
          "title": "Global prevalence of iron deficiency anaemia among children aged 5–12 years: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Journal of Global Health",
          "cited_by_count": 6,
          "topics": [
            "Iron Metabolism and Disorders",
            "Erythropoietin and Anemia Treatment",
            "Hemoglobinopathies and Related Disorders"
          ]
        },
        {
          "openalex_id": "W1140365015",
          "year": 2010,
          "title": "Carbamazepine- but not phenytoin-induced severe cutaneous adverse drug reactions are associated with HLA-B*1502 in a Thai population",
          "type": "article",
          "venue": "วารสารเภสัชวิทยา (Thai Journal of Pharmacology)",
          "cited_by_count": 0,
          "topics": [
            "Drug-Induced Adverse Reactions",
            "Autoimmune Bullous Skin Diseases",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W2045488885",
          "year": 2010,
          "title": "Estimation of Financial Burden Due to Oversupply of Medications for Chronic Diseases",
          "type": "article",
          "venue": "Asia Pacific Journal of Public Health",
          "cited_by_count": 11,
          "topics": [
            "Medication Adherence and Compliance",
            "Pharmaceutical Economics and Policy",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2066046344",
          "year": 2010,
          "title": "PCV11 EFFECTS OF MEDICATION SUPPLY ON HEALTH-CARE COSTS AND RE-HOSPITALIZATIONS IN PATIENTS WITH CHRONIC HEART FAILURE",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2068102295",
          "year": 2010,
          "title": "PHP39 THE EFFECTS OF DIRECT BILLING SYSTEM IN PATIENTS WITH CIVIL-SERVANT MEDICAL BENEFIT SCHEMES ON PRESCRIBING PATTERNS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Healthcare Operations and Scheduling Optimization",
            "Pharmaceutical Practices and Patient Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2911658427",
          "year": 2019,
          "title": "The prevalence of MS in the United States",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 1110,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Vaccine Coverage and Hesitancy",
            "Systemic Sclerosis and Related Diseases"
          ]
        },
        {
          "openalex_id": "W2288073912",
          "year": 2016,
          "title": "Multiple sclerosis prevalence in the United States commercially insured population",
          "type": "article",
          "venue": "Neurology",
          "cited_by_count": 278,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Vaccine Coverage and Hesitancy",
            "Systemic Sclerosis and Related Diseases"
          ]
        },
        {
          "openalex_id": "W2145019170",
          "year": 2013,
          "title": "Meta-analysis of randomized controlled trials on cognitive effects of Bacopa monnieri extract",
          "type": "review",
          "venue": "Journal of Ethnopharmacology",
          "cited_by_count": 161,
          "topics": [
            "Medicinal Plants and Neuroprotection",
            "Phytochemicals and Medicinal Plants",
            "GABA and Rice Research"
          ]
        },
        {
          "openalex_id": "W2883527838",
          "year": 2018,
          "title": "The Effects of Telemedicine on Asthma Control and Patients' Quality of Life in Adults: A Systematic Review and Meta-analysis",
          "type": "review",
          "venue": "The Journal of Allergy and Clinical Immunology In Practice",
          "cited_by_count": 156,
          "topics": [
            "Asthma and respiratory diseases",
            "Mobile Health and mHealth Applications",
            "Telemedicine and Telehealth Implementation"
          ]
        },
        {
          "openalex_id": "W2611576380",
          "year": 2017,
          "title": "Prevention and Control of Multidrug-Resistant Gram-Negative Bacteria in Adult Intensive Care Units: A Systematic Review and Network Meta-analysis",
          "type": "review",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 135,
          "topics": [
            "Antibiotic Resistance in Bacteria",
            "Nosocomial Infections in ICU",
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W2752029125",
          "year": 2017,
          "title": "Effects of Centella asiatica (L.) Urb. on cognitive function and mood related outcomes: A Systematic Review and Meta-analysis",
          "type": "review",
          "venue": "Scientific Reports",
          "cited_by_count": 128,
          "topics": [
            "Medicinal Plants and Neuroprotection",
            "Cholinesterase and Neurodegenerative Diseases",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W4281644967",
          "year": 2022,
          "title": "Trends in advanced oral drug delivery system for curcumin: A systematic review",
          "type": "review",
          "venue": "Journal of Controlled Release",
          "cited_by_count": 114,
          "topics": [
            "Curcumin's Biomedical Applications",
            "Advancements in Transdermal Drug Delivery",
            "Advanced Drug Delivery Systems"
          ]
        },
        {
          "openalex_id": "W2196497827",
          "year": 2015,
          "title": "Risk Factors of Prescription Opioid Overdose Among Colorado Medicaid Beneficiaries",
          "type": "article",
          "venue": "Journal of Pain",
          "cited_by_count": 82,
          "topics": [
            "Opioid Use Disorder Treatment",
            "Pain Management and Opioid Use",
            "Poisoning and overdose treatments"
          ]
        }
      ]
    }
  },
  {
    "name": "Prudence Cheung",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1808-RA",
        "title": "Mapping of Y5L from EQ-5D-5L in the population of orthopaedic paediatric patients in Hong Kong",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5011025629",
      "display_name": "Prudence Wing Hang Cheung",
      "orcid": "0000-0002-3213-7373",
      "reported_affiliation": "University of Hong Kong",
      "works_count": 117,
      "top_topics": [
        {
          "topic": "Scoliosis diagnosis and treatment",
          "works": 80
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 55
        },
        {
          "topic": "Spinal Fractures and Fixation Techniques",
          "works": 37
        },
        {
          "topic": "Cervical and Thoracic Myelopathy",
          "works": 20
        },
        {
          "topic": "Hip disorders and treatments",
          "works": 15
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 10
        },
        {
          "topic": "Shoulder Injury and Treatment",
          "works": 9
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 6
        },
        {
          "topic": "Foot and Ankle Surgery",
          "works": 5
        },
        {
          "topic": "Connective tissue disorders research",
          "works": 5
        },
        {
          "topic": "Bone fractures and treatments",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jason Pui Yin Cheung",
          "works": 110
        },
        {
          "name": "Carlos King Ho Wong",
          "works": 26
        },
        {
          "name": "Dino Samartzis",
          "works": 18
        },
        {
          "name": "Kmc Cheung",
          "works": 18
        },
        {
          "name": "K.D.K. Luk",
          "works": 16
        },
        {
          "name": "Nan Luo",
          "works": 7
        },
        {
          "name": "Sin Ting Lau",
          "works": 7
        },
        {
          "name": "Keith D.K. Luk",
          "works": 6
        },
        {
          "name": "Cindy Lo Kuen Lam",
          "works": 6
        },
        {
          "name": "Marcus Kin Long Lai",
          "works": 6
        },
        {
          "name": "Helen Hoi Lun Tsang",
          "works": 6
        },
        {
          "name": "Hideki Shigematsu",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7160768128",
          "year": 2026,
          "title": "Preoperative Fulcrum Flexibility &gt;80% Is Associated With Clinical Success in Vertebral Body Tethering",
          "type": "article",
          "venue": "Global Spine Journal",
          "cited_by_count": 0,
          "topics": [
            "Craniofacial Disorders and Treatments",
            "Spinal Fractures and Fixation Techniques",
            "Spinal Dysraphism and Malformations"
          ]
        },
        {
          "openalex_id": "W4410281044",
          "year": 2025,
          "title": "Assessing quality of life gains in knee replacement patients across several post-operative time points",
          "type": "article",
          "venue": "Journal of Orthopaedics Trauma and Rehabilitation",
          "cited_by_count": 1,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Knee injuries and reconstruction techniques"
          ]
        },
        {
          "openalex_id": "W4411967805",
          "year": 2025,
          "title": "Comparisons of Preferences Toward EQ-5D-Y-3L Health States Between Adult Own and Child Perspectives",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4409283172",
          "year": 2025,
          "title": "Exploring the potential relationships between idiopathic scoliosis and various multifactorial diseases: a systematic scoping review",
          "type": "article",
          "venue": "Spine Deformity",
          "cited_by_count": 2,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Temporomandibular Joint Disorders",
            "Hip disorders and treatments"
          ]
        },
        {
          "openalex_id": "W4410869090",
          "year": 2025,
          "title": "Factors contributing to bracing success in juvenile idiopathic scoliosis and current limitations",
          "type": "article",
          "venue": "Bone & Joint Open",
          "cited_by_count": 3,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spinal Fractures and Fixation Techniques",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W4408884205",
          "year": 2025,
          "title": "How Accurate Are Fulcrum Bending Radiographs in Estimating Postoperative Outcomes in Adolescent Idiopathic Scoliosis? A Systematic Review and Meta-analysis",
          "type": "review",
          "venue": "Clinical Orthopaedics and Related Research",
          "cited_by_count": 2,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spinal Fractures and Fixation Techniques",
            "Shoulder Injury and Treatment"
          ]
        },
        {
          "openalex_id": "W2409158737",
          "year": 1994,
          "title": "Continuous wave Doppler measurements of aortic bloodflow during exercise in patients with chronic heart failure.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Cardiovascular and exercise physiology",
            "Cardiovascular Function and Risk Factors",
            "Cardiovascular Health and Disease Prevention"
          ]
        },
        {
          "openalex_id": "W2277314182",
          "year": 1995,
          "title": "Psychosocial evaluation after brace treatment for scoliosis",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Scoliosis diagnosis and treatment"
          ]
        },
        {
          "openalex_id": "W2569372523",
          "year": 2007,
          "title": "Femoral tunnel widening after quadrupled hamstring anterior cruculate ligament reconstruction using femoral cross pin fixation or bioabsorable screw fixation",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Knee injuries and reconstruction techniques",
            "Total Knee Arthroplasty Outcomes",
            "Sports injuries and prevention"
          ]
        },
        {
          "openalex_id": "W2291782817",
          "year": 2015,
          "title": "Reliability Analysis of the Distal Radius and Ulna Classification for Assessing Skeletal Maturity for Patients with Adolescent Idiopathic Scoliosis",
          "type": "article",
          "venue": "Global Spine Journal",
          "cited_by_count": 29,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Hip disorders and treatments",
            "Shoulder Injury and Treatment"
          ]
        },
        {
          "openalex_id": "W2502035244",
          "year": 2016,
          "title": "Psychometric validation of the EuroQoL 5-Dimension 5-Level (EQ-5D-5L) in Chinese patients with adolescent idiopathic scoliosis",
          "type": "article",
          "venue": "Scoliosis and Spinal Disorders",
          "cited_by_count": 96,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spine and Intervertebral Disc Pathology",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W2902508544",
          "year": 2018,
          "title": "How Common Is Back Pain and What Biopsychosocial Factors Are Associated With Back Pain in Patients With Adolescent Idiopathic Scoliosis?",
          "type": "article",
          "venue": "Clinical Orthopaedics and Related Research",
          "cited_by_count": 89,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spine and Intervertebral Disc Pathology",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2793387094",
          "year": 2018,
          "title": "Curve Progression in Adolescent Idiopathic Scoliosis Does Not Match Skeletal Growth",
          "type": "article",
          "venue": "Clinical Orthopaedics and Related Research",
          "cited_by_count": 81,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Hip disorders and treatments",
            "Shoulder Injury and Treatment"
          ]
        },
        {
          "openalex_id": "W3037120822",
          "year": 2020,
          "title": "An Ensemble-Based Densely-Connected Deep Learning System for Assessment of Skeletal Maturity",
          "type": "article",
          "venue": "IEEE Transactions on Systems Man and Cybernetics Systems",
          "cited_by_count": 74,
          "topics": [
            "Forensic Anthropology and Bioarchaeology Studies",
            "Dermatoglyphics and Human Traits",
            "Dental Radiography and Imaging"
          ]
        },
        {
          "openalex_id": "W2943479836",
          "year": 2018,
          "title": "An Insight Into the Health-Related Quality of Life of Adolescent Idiopathic Scoliosis Patients Who Are Braced, Observed, and Previously Braced",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 64,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Spinal Fractures and Fixation Techniques",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2907197105",
          "year": 2019,
          "title": "A head-to-head comparison of five-level (EQ-5D-5L-Y) and three-level EQ-5D-Y questionnaires in paediatric patients",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 60,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W3163204491",
          "year": 2021,
          "title": "Impact of sleep duration, physical activity, and screen time on health-related quality of life in children and adolescents",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 60,
          "topics": [
            "Child Development and Digital Technology",
            "Obesity, Physical Activity, Diet",
            "Impact of Technology on Adolescents"
          ]
        },
        {
          "openalex_id": "W2807662734",
          "year": 2018,
          "title": "Skeletal Maturity Recognition Using a Fully Automated System With Convolutional Neural Networks",
          "type": "article",
          "venue": "IEEE Access",
          "cited_by_count": 59,
          "topics": [
            "Forensic Anthropology and Bioarchaeology Studies",
            "Dental Radiography and Imaging",
            "Medical Imaging and Analysis"
          ]
        }
      ]
    }
  }
]
