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
    "name": "Alex Bató",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2260-RA",
        "title": "EQ-HWB-9 modifications testing using a one-at-a-time approach",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2441-RA",
        "title": "EQ-HWB VAS anchors: a mixed-methods study",
        "working_group": "Descriptive Systems, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5009546494",
      "display_name": "Alex Bató",
      "orcid": "0000-0002-1450-4790",
      "reported_affiliation": "Semmelweis University",
      "works_count": 16,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 5
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 5
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Hidradenitis Suppurativa and Treatments",
          "works": 3
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 2
        },
        {
          "topic": "Acne and Rosacea Treatments and Effects",
          "works": 2
        },
        {
          "topic": "Anorectal Disease Treatments and Outcomes",
          "works": 2
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 2
        },
        {
          "topic": "Psychometric Methodologies and Testing",
          "works": 2
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Suicide and Self-Harm Studies",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Fanni Rencz",
          "works": 15
        },
        {
          "name": "Valentin Brodszky",
          "works": 14
        },
        {
          "name": "Andrea Szegedi",
          "works": 6
        },
        {
          "name": "Miklós Sárdy",
          "works": 6
        },
        {
          "name": "Zsuzsanna Beretzky",
          "works": 5
        },
        {
          "name": "L Gergely",
          "works": 4
        },
        {
          "name": "Kamilla Koszorú",
          "works": 4
        },
        {
          "name": "K. Hajdu",
          "works": 4
        },
        {
          "name": "Krisztián Gáspár",
          "works": 3
        },
        {
          "name": "Ágnes Kinyó",
          "works": 3
        },
        {
          "name": "Éva Remenyik",
          "works": 3
        },
        {
          "name": "Norbert Kiss",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407617525",
          "year": 2025,
          "title": "Development of updated population norms for the SF-36 for Hungary and comparison with 1997–1998 norms",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 9,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Suicide and Self-Harm Studies",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W4407582998",
          "year": 2025,
          "title": "Harmonic development index: a novel approach to measure environmental, social, and economic development",
          "type": "article",
          "venue": "Regional Statistics",
          "cited_by_count": 1,
          "topics": [
            "Sustainable Development and Environmental Policy"
          ]
        },
        {
          "openalex_id": "W4320895998",
          "year": 2023,
          "title": "Hungarian PROMIS-29+2: psychometric properties and population reference values",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 10,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Cancer survivorship and care",
            "Psychological Testing and Assessment"
          ]
        },
        {
          "openalex_id": "W4390129230",
          "year": 2023,
          "title": "PCR161 Population Norms for the SF-36 Health Status Measure in Hungary",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W4382344742",
          "year": 2023,
          "title": "Psychometric properties and general population reference values for PROMIS Global Health in Hungary",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 10,
          "topics": [
            "Psychometric Methodologies and Testing",
            "Health Education and Validation",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4309472643",
          "year": 2022,
          "title": "082 Comparing psychometric properties of EQ-5D-3L and EQ-5D-5L in atopic dermatitis",
          "type": "article",
          "venue": "Journal of Investigative Dermatology",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dermatology and Skin Diseases",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W3111236877",
          "year": 2020,
          "title": "PSY30 The Measurement Performance of the EQ-5D-5L Versus EQ-5D-3L in Patients with Hidradenitis Suppurativa",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Hidradenitis Suppurativa and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3039598350",
          "year": 2020,
          "title": "Validity of EQ‐5D‐5L, Skindex‐16, DLQI and DLQI‐R in patients with hidradenitis suppurativa",
          "type": "article",
          "venue": "Journal of the European Academy of Dermatology and Venereology",
          "cited_by_count": 51,
          "topics": [
            "Hidradenitis Suppurativa and Treatments",
            "Acne and Rosacea Treatments and Effects",
            "Anorectal Disease Treatments and Outcomes"
          ]
        },
        {
          "openalex_id": "W3205343234",
          "year": 2021,
          "title": "080 The impact of atopic dermatitis on health-related quality of life",
          "type": "article",
          "venue": "Journal of Investigative Dermatology",
          "cited_by_count": 1,
          "topics": [
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W3126244119",
          "year": 2021,
          "title": "The measurement performance of the EQ-5D-5L versus EQ-5D-3L in patients with hidradenitis suppurativa",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 28,
          "topics": [
            "Hidradenitis Suppurativa and Treatments",
            "Acne and Rosacea Treatments and Effects",
            "Anorectal Disease Treatments and Outcomes"
          ]
        },
        {
          "openalex_id": "W4296336196",
          "year": 2022,
          "title": "Value Set for the EQ-5D-Y-3L in Hungary",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 40,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4224435280",
          "year": 2022,
          "title": "A qualitative investigation of the relevance of skin irritation and self-confidence bolt-ons and their conceptual overlap with the EQ-5D in patients with psoriasis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psoriasis: Treatment and Pathogenesis",
            "Dermatology and Skin Diseases"
          ]
        },
        {
          "openalex_id": "W4223487230",
          "year": 2022,
          "title": "Comparing the psychometric properties of the EQ-5D-3L and EQ-5D-5L descriptive systems and utilities in atopic dermatitis",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 30,
          "topics": [
            "Dermatology and Skin Diseases",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        }
      ]
    }
  },
  {
    "name": "Alexander Arons",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013120",
        "title": "Rescaling relative health-state values from discrete choice experiments unbiased onto the QALY metric",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013250",
        "title": "Examining interviewer performance in the Dutch EQVT studies",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013260",
        "title": "Project Save TTO valuations",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014140",
        "title": "Quantification of EQ-5D health-state values by scaling similarity data (studies 1 and 2)",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016220",
        "title": "An individual-level comparison of EQ-5D-5L values derived from paired comparison and best-worst data",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5044999875",
      "display_name": "Alexander M. M. Arons",
      "orcid": "",
      "reported_affiliation": "Novartis (Netherlands)",
      "works_count": 13,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 6
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 3
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 2
        },
        {
          "topic": "Reliability and Agreement in Measurement",
          "works": 2
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 1
        },
        {
          "topic": "Acute Lymphoblastic Leukemia research",
          "works": 1
        },
        {
          "topic": "Virus-based gene therapy research",
          "works": 1
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Global Health Care Issues",
          "works": 1
        },
        {
          "topic": "Reproductive Health and Technologies",
          "works": 1
        },
        {
          "topic": "Family Dynamics and Relationships",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Paul F. M. Krabbe",
          "works": 8
        },
        {
          "name": "Carla J.M. Schölzel-Dorenbos",
          "works": 5
        },
        {
          "name": "Marcel G. M. Olde Rikkert",
          "works": 5
        },
        {
          "name": "Gert Jan van der Wilt",
          "works": 3
        },
        {
          "name": "Frederick W. Thielen",
          "works": 1
        },
        {
          "name": "Annemieke van Dongen‐Leunis",
          "works": 1
        },
        {
          "name": "Judith R. Ladestein",
          "works": 1
        },
        {
          "name": "Peter M. Hoogerbrugge",
          "works": 1
        },
        {
          "name": "Joost Wammes",
          "works": 1
        },
        {
          "name": "MarcelGMOlde Rikkert",
          "works": 1
        },
        {
          "name": "Kimberley Hubens",
          "works": 1
        },
        {
          "name": "Marieke Krol",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3015970146",
          "year": 2020,
          "title": "Cost‐effectiveness of Anti‐CD19 chimeric antigen receptor T‐Cell therapy in pediatric relapsed/refractory B‐cell acute lymphoblastic leukemia. A societal view",
          "type": "article",
          "venue": "European Journal Of Haematology",
          "cited_by_count": 42,
          "topics": [
            "CAR-T cell therapy research",
            "Acute Lymphoblastic Leukemia research",
            "Virus-based gene therapy research"
          ]
        },
        {
          "openalex_id": "W2996057723",
          "year": 2019,
          "title": "PCN64 COST-EFFECTIVENESS OF IMATINIB SINCE ITS INTRODUCTION AS FIRST-LINE TREATMENT IN THE NETHERLANDS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Chronic Myeloid Leukemia Treatments"
          ]
        },
        {
          "openalex_id": "W2903392934",
          "year": 2018,
          "title": "Measurement and evaluation of quality of life and well-being in individuals having or having had fertility problems: a systematic review",
          "type": "review",
          "venue": "The European Journal of Contraception & Reproductive Health Care",
          "cited_by_count": 19,
          "topics": [
            "Reproductive Health and Technologies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Family Dynamics and Relationships"
          ]
        },
        {
          "openalex_id": "W2753310333",
          "year": 2017,
          "title": "Structural validity and internal consistency of the Qualidem in people with severe dementia",
          "type": "article",
          "venue": "International Psychogeriatrics",
          "cited_by_count": 17,
          "topics": [
            "Reliability and Agreement in Measurement",
            "Meta-analysis and systematic reviews",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W2173370971",
          "year": 2015,
          "title": "A Simple and Practical Index to Measure Dementia-Related Quality of Life",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 13,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W829518162",
          "year": 2014,
          "title": "A contribution to dementia-related quality of life measurement.",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Aging, Elder Care, and Social Issues",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W1972729222",
          "year": 2012,
          "title": "Improving the Measurement of QALYs in Dementia: Some Important Considerations",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Mental Health and Psychiatry",
            "Diet and metabolism studies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2169507110",
          "year": 2012,
          "title": "Thurstone scaling revealed systematic health-state valuation differences between patients with dementia and proxies",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 13,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2146009051",
          "year": 2012,
          "title": "Validation study of the prototype of a disease-specific index measure for health-related quality of life in dementia",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 29,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W2112427069",
          "year": 2012,
          "title": "Visual analogue scales: scale recalibration by patients with dementia and their proxies",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 13,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health disparities and outcomes",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W2118788275",
          "year": 2013,
          "title": "Quality of life in dementia: a study on proxy bias",
          "type": "article",
          "venue": "BMC Medical Research Methodology",
          "cited_by_count": 118,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2033634729",
          "year": 2013,
          "title": "Probabilistic choice models in health-state valuation research: background, theories, assumptions and applications",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 24,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  },
  {
    "name": "Alexander Geissler",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "301-SG",
        "title": "Crafting and elaborating the potential of clinical dashboards incorporating PROMs",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5089010455",
      "display_name": "Alexander Geißler",
      "orcid": "0000-0002-7445-2929",
      "reported_affiliation": "University of St.Gallen",
      "works_count": 231,
      "top_topics": [
        {
          "topic": "Healthcare Policy and Management",
          "works": 33
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 28
        },
        {
          "topic": "Health and Medical Studies",
          "works": 22
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 21
        },
        {
          "topic": "Functional Brain Connectivity Studies",
          "works": 19
        },
        {
          "topic": "Advanced MRI Techniques and Applications",
          "works": 17
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 16
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 16
        },
        {
          "topic": "Advanced Neuroimaging Techniques and Applications",
          "works": 15
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 13
        },
        {
          "topic": "Emergency and Acute Care Studies",
          "works": 12
        },
        {
          "topic": "Medical and Health Sciences Research",
          "works": 12
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Reinhard Busse",
          "works": 48
        },
        {
          "name": "Wilm Quentin",
          "works": 40
        },
        {
          "name": "Roland Beisteiner",
          "works": 35
        },
        {
          "name": "Justus Vogel",
          "works": 34
        },
        {
          "name": "David Kuklinski",
          "works": 24
        },
        {
          "name": "Thomas Foki",
          "works": 20
        },
        {
          "name": "Jakob Rath",
          "works": 18
        },
        {
          "name": "Nicolaus Klinger",
          "works": 15
        },
        {
          "name": "Moritz C. Wurnig",
          "works": 14
        },
        {
          "name": "Siegfried Trattnig",
          "works": 14
        },
        {
          "name": "Florian Ph. S. Fischmeister",
          "works": 14
        },
        {
          "name": "Koen Van den Heede",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7117253535",
          "year": 2025,
          "title": "Additional file 1 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Medication Adherence and Compliance",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W7117265264",
          "year": 2025,
          "title": "Additional file 1 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Medication Adherence and Compliance",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W7117240113",
          "year": 2025,
          "title": "Additional file 2 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Medication Adherence and Compliance",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W7117248792",
          "year": 2025,
          "title": "Additional file 2 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Medication Adherence and Compliance",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W7117234432",
          "year": 2025,
          "title": "Additional file 3 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Ethics in Clinical Research",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W7117259676",
          "year": 2025,
          "title": "Additional file 3 of Enhancing type 2 diabetes care by an individualized and group-based therapeutic patient education program: study protocol for a cluster randomized trial",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Education",
            "Ethics in Clinical Research",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W1596188867",
          "year": 1959,
          "title": "Die Immunreaktionen der weifɛen Maus nach der Impfung mit Abortug‐Bang‐Impfstoffen",
          "type": "article",
          "venue": "Zentralblatt für Veterinärmedizin",
          "cited_by_count": 0,
          "topics": [
            "Brucella: diagnosis, epidemiology, treatment",
            "Immunotherapy and Immune Responses",
            "vaccines and immunoinformatics approaches"
          ]
        },
        {
          "openalex_id": "W2344853210",
          "year": 1965,
          "title": "[On mental hygiene of recreation of 10 to 14-year-old children].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Physical Education and Training Studies",
            "Human Health and Disease"
          ]
        },
        {
          "openalex_id": "W1878527652",
          "year": 1967,
          "title": "Compendium of animal diseases regulations.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Animal Disease Management and Epidemiology"
          ]
        },
        {
          "openalex_id": "W1521292395",
          "year": 1968,
          "title": "Compendium of animal disease regulations. First supplement.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Animal Disease Management and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2154065395",
          "year": 2013,
          "title": "Diagnosis related groups in Europe: moving towards transparency, efficiency, and quality in hospitals?",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 510,
          "topics": [
            "Healthcare Quality and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W1970089769",
          "year": 2014,
          "title": "A Comparison Of Hospital Administrative Costs In Eight Nations: US Costs Exceed All Others By Far",
          "type": "article",
          "venue": "Health Affairs",
          "cited_by_count": 217,
          "topics": [
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4239902744",
          "year": 2015,
          "title": "Utilization rates of knee-arthroplasty in OECD countries",
          "type": "article",
          "venue": "Osteoarthritis and Cartilage",
          "cited_by_count": 215,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty",
            "Knee injuries and reconstruction techniques"
          ]
        },
        {
          "openalex_id": "W2803156967",
          "year": 2018,
          "title": "Projections of hip arthroplasty in OECD countries up to 2050",
          "type": "article",
          "venue": "Hip International",
          "cited_by_count": 202,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Total Knee Arthroplasty Outcomes",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W2899693997",
          "year": 2018,
          "title": "Emergency and urgent care systems in Australia, Denmark, England, France, Germany and the Netherlands – Analyzing organization, payment and reforms",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 144,
          "topics": [
            "Emergency and Acute Care Studies",
            "Trauma and Emergency Care Studies",
            "Emergency Medicine Education and Research"
          ]
        },
        {
          "openalex_id": "W2055491692",
          "year": 2011,
          "title": "Clinical fMRI: Evidence for a 7T benefit over 3T",
          "type": "article",
          "venue": "NeuroImage",
          "cited_by_count": 131,
          "topics": [
            "Advanced MRI Techniques and Applications",
            "Functional Brain Connectivity Studies",
            "Advanced Neuroimaging Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2139975414",
          "year": 2013,
          "title": "Hospital Payment Based On Diagnosis-Related Groups Differs In Europe And Holds Lessons For The United States",
          "type": "article",
          "venue": "Health Affairs",
          "cited_by_count": 109,
          "topics": [
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2162757404",
          "year": 2008,
          "title": "Comparison of the novel hydroxyethylstarch 130/0.4 and hydroxyethylstarch 200/0.6 in brain-dead donor resuscitation on renal function after transplantation",
          "type": "article",
          "venue": "British Journal of Anaesthesia",
          "cited_by_count": 104,
          "topics": [
            "Organ Donation and Transplantation",
            "Organ Transplantation Techniques and Outcomes",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation"
          ]
        }
      ]
    }
  },
  {
    "name": "Alexander van Heusden",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1739-EO",
        "title": "ISOQOL Dissemination of the of the adapted (modified) EQ-5D-Y validation study",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070658848",
      "display_name": "Alexander van Heusden",
      "orcid": "0009-0007-8055-5450",
      "reported_affiliation": "Murdoch Children's Research Institute",
      "works_count": 37,
      "top_topics": [
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 17
        },
        {
          "topic": "Cardiovascular Effects of Exercise",
          "works": 7
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 6
        },
        {
          "topic": "Cardiac electrophysiology and arrhythmias",
          "works": 5
        },
        {
          "topic": "Cardiovascular Function and Risk Factors",
          "works": 4
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 3
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 3
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 3
        },
        {
          "topic": "Autopsy Techniques and Outcomes",
          "works": 3
        },
        {
          "topic": "Cardiovascular Issues in Pregnancy",
          "works": 3
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "E. Paratz",
          "works": 23
        },
        {
          "name": "Karen Smith",
          "works": 22
        },
        {
          "name": "Andreas Pflaumer",
          "works": 22
        },
        {
          "name": "Dion Stub",
          "works": 22
        },
        {
          "name": "André La Gerche",
          "works": 21
        },
        {
          "name": "Dominica Zentner",
          "works": 20
        },
        {
          "name": "Sarah Parsons",
          "works": 20
        },
        {
          "name": "Natalie Morgan",
          "works": 19
        },
        {
          "name": "Tina Thompson",
          "works": 19
        },
        {
          "name": "Paul A. James",
          "works": 19
        },
        {
          "name": "Christopher Semsarian",
          "works": 18
        },
        {
          "name": "Jodie Ingles",
          "works": 18
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7130841275",
          "year": 2026,
          "title": "Higher long-term healthcare utilization in children conceived through medically assisted reproduction: findings from a 16-year cohort study",
          "type": "article",
          "venue": "American Journal of Obstetrics and Gynecology",
          "cited_by_count": 0,
          "topics": [
            "Assisted Reproductive Technology and Twin Pregnancy",
            "Reproductive Health and Technologies",
            "Reproductive Health and Contraception"
          ]
        },
        {
          "openalex_id": "W4416809966",
          "year": 2025,
          "title": "Correction: How do Health State Values Differ When Respondents Consider Adults Versus Children Living in Those States? A Systematic Review",
          "type": "erratum",
          "venue": "PharmacoEconomics",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4417078470",
          "year": 2025,
          "title": "Exploring valuation of a modified EQ-5D-Y-3L adapted for 2–4 year olds: a think-aloud study",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4409653755",
          "year": 2025,
          "title": "How do Health State Values Differ When Respondents Consider Adults Versus Children Living in Those States? A Systematic Review",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4410370423",
          "year": 2025,
          "title": "Use of a generic Paediatric Patient Reported Outcome Measure (P-PROM) in Routine hospital Outpatient Care for Kids (ROCK): A qualitative exploration of adolescent, caregiver and service provider perspectives (P-PROM ROCK Phase 1)",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient Satisfaction in Healthcare",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4390971332",
          "year": 2024,
          "title": "Psychometric Performance Comparison of the Adapted versus Original Versions of the EQ-5D-Y-3L and -Y-5L in Proxy Respondents for 2- to 4-Year-Olds",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 14,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W2535248108",
          "year": 1963,
          "title": "[PREGNANCY AND SICKLE CELL ANEMIA].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Iron Metabolism and Disorders",
            "Erythrocyte Function and Pathophysiology"
          ]
        },
        {
          "openalex_id": "W2028229807",
          "year": 2007,
          "title": "A retroperitoneal pregnancy of an anencephalic fetus",
          "type": "article",
          "venue": "Journal of Obstetrics and Gynaecology",
          "cited_by_count": 13,
          "topics": [
            "Ectopic Pregnancy Diagnosis and Management",
            "Gestational Trophoblastic Disease Studies"
          ]
        },
        {
          "openalex_id": "W3103082964",
          "year": 2020,
          "title": "The End Unexplained Cardiac Death (EndUCD) Registry for Young Australian Sudden Cardiac Arrest",
          "type": "article",
          "venue": "Heart Lung and Circulation",
          "cited_by_count": 27,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Cardiac electrophysiology and arrhythmias",
            "Cardiovascular Effects of Exercise"
          ]
        },
        {
          "openalex_id": "W3158519958",
          "year": 2021,
          "title": "Effect of multimorbidity on utilisation and out-of-pocket expenditure in Indonesia: quantile regression analysis",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 51,
          "topics": [
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3130230332",
          "year": 2021,
          "title": "Medical costs and out-of-pocket expenditures associated with multimorbidity in China: quantile regression analysis",
          "type": "article",
          "venue": "BMJ Global Health",
          "cited_by_count": 57,
          "topics": [
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4293476254",
          "year": 2022,
          "title": "Causes, circumstances, and potential preventability of cardiac arrest in the young: insights from a state-wide clinical and forensic registry",
          "type": "article",
          "venue": "EP Europace",
          "cited_by_count": 47,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Cardiovascular Effects of Exercise",
            "Cardiac electrophysiology and arrhythmias"
          ]
        },
        {
          "openalex_id": "W3154428721",
          "year": 2021,
          "title": "The economic impact of sudden cardiac arrest",
          "type": "article",
          "venue": "Resuscitation",
          "cited_by_count": 31,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Cardiovascular Effects of Exercise",
            "Heart Failure Treatment and Management"
          ]
        },
        {
          "openalex_id": "W3158739100",
          "year": 2021,
          "title": "The Prevalence of Metabolic Disease Multimorbidity and Its Associations With Spending and Health Outcomes in Middle-Aged and Elderly Chinese Adults",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 28,
          "topics": [
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4210712985",
          "year": 2022,
          "title": "Predictors and outcomes of in-hospital referrals for forensic investigation after young sudden cardiac death",
          "type": "article",
          "venue": "Heart Rhythm",
          "cited_by_count": 14,
          "topics": [
            "Cardiac Arrest and Resuscitation",
            "Autopsy Techniques and Outcomes",
            "Cardiac electrophysiology and arrhythmias"
          ]
        }
      ]
    }
  },
  {
    "name": "Alice Yu",
    "member_affiliation": "Centre for Health Economics and Research Evaluation (CHERE)",
    "is_member": true,
    "projects": [
      {
        "project_id": "1888-RA",
        "title": "Valuing EQ-5D-Y-5L in adolescents using DCE methods accounting for nonlinear time preferences: An extension to ongoing data collection as part of the QUOKKA program",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1890-RA",
        "title": "What are the implications for using different mental health descriptors for the EQ-5D-5L and EQ-5D-Y-5L in valuation studies? A comparison study using DCE",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "20180150",
        "title": "Furthering the DCE research agenda: Comparing anchoring and design methods for the valuation of EQ-5D",
        "working_group": "Valuation"
      },
      {
        "project_id": "2335-RA",
        "title": "What features characterise good quality data? An exploration of quality control measures in the valuation of the EQ-5D-5L using a nonlinear DCE modelling method ",
        "working_group": "Valuation"
      },
      {
        "project_id": "2584-RA",
        "title": "The EQ-HWB-S as a quality of life assessment tool in disability service support provision: An exploratory study",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5055148154",
      "display_name": "Alice L. Yu",
      "orcid": "0000-0003-2444-0505",
      "reported_affiliation": "Chang Gung University",
      "works_count": 491,
      "top_topics": [
        {
          "topic": "Neuroblastoma Research and Treatments",
          "works": 110
        },
        {
          "topic": "Glycosylation and Glycoproteins Research",
          "works": 49
        },
        {
          "topic": "Cancer, Hypoxia, and Metabolism",
          "works": 47
        },
        {
          "topic": "Cancer therapeutics and mechanisms",
          "works": 33
        },
        {
          "topic": "Immune Cell Function and Interaction",
          "works": 32
        },
        {
          "topic": "RNA modifications and cancer",
          "works": 31
        },
        {
          "topic": "Acute Lymphoblastic Leukemia research",
          "works": 29
        },
        {
          "topic": "Cancer Cells and Metastasis",
          "works": 29
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 27
        },
        {
          "topic": "Monoclonal and Polyclonal Antibodies Research",
          "works": 23
        },
        {
          "topic": "Biochemical and Molecular Research",
          "works": 21
        },
        {
          "topic": "Cancer-related Molecular Pathways",
          "works": 17
        }
      ],
      "frequent_coauthors": [
        {
          "name": "John Yu",
          "works": 94
        },
        {
          "name": "Mitchell B. Diccianni",
          "works": 76
        },
        {
          "name": "Jung‐Tung Hung",
          "works": 68
        },
        {
          "name": "Paul M. Sondel",
          "works": 50
        },
        {
          "name": "Wendy B. London",
          "works": 49
        },
        {
          "name": "Julie R. Park",
          "works": 42
        },
        {
          "name": "Arlene Naranjo",
          "works": 42
        },
        {
          "name": "John M. Maris",
          "works": 39
        },
        {
          "name": "Andrew L. Gilman",
          "works": 36
        },
        {
          "name": "Jacquelyn A. Hank",
          "works": 36
        },
        {
          "name": "Ayse Batova",
          "works": 36
        },
        {
          "name": "M. Fevzi Özkaynak",
          "works": 35
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7130359126",
          "year": 2026,
          "title": "Abstract A020: Novel natural killer cell therapy using unique NK cell subset",
          "type": "conference-abstract",
          "venue": "Cancer Immunology Research",
          "cited_by_count": 0,
          "topics": [
            "Immune Cell Function and Interaction",
            "CAR-T cell therapy research",
            "Monoclonal and Polyclonal Antibodies Research"
          ]
        },
        {
          "openalex_id": "W7130577527",
          "year": 2026,
          "title": "Abstract B025: Anti-GD2 combined with anti-PD1 enhances tumor immunity with T cell memory via inducing immunogenic cell death",
          "type": "conference-abstract",
          "venue": "Cancer Research",
          "cited_by_count": 0,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "CAR-T cell therapy research",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W7134053261",
          "year": 2026,
          "title": "Globo H ceramide confers chemoresistance and poor prognosis to advanced gallbladder cancer via A2AR/cAMP/PKA pathway",
          "type": "article",
          "venue": "Theranostics",
          "cited_by_count": 0,
          "topics": [
            "Protein Kinase Regulation and GTPase Signaling",
            "Sphingolipid Metabolism and Signaling",
            "Adenosine and Purinergic Signaling"
          ]
        },
        {
          "openalex_id": "W7147346998",
          "year": 2026,
          "title": "Immunotherapeutic Strategies Targeting GD2-Expressing Malignancies",
          "type": "book-chapter",
          "venue": "Advances in experimental medicine and biology",
          "cited_by_count": 0,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "CAR-T cell therapy research",
            "Monoclonal and Polyclonal Antibodies Research"
          ]
        },
        {
          "openalex_id": "W7147031193",
          "year": 2026,
          "title": "Impacts of Globo H Ceramide on Tumor Microenvironment",
          "type": "book-chapter",
          "venue": "Advances in experimental medicine and biology",
          "cited_by_count": 0,
          "topics": [
            "Glycosylation and Glycoproteins Research",
            "Monoclonal and Polyclonal Antibodies Research",
            "Neuroblastoma Research and Treatments"
          ]
        },
        {
          "openalex_id": "W7162559889",
          "year": 2026,
          "title": "RAPID: A pilot feasibility study of rapid dinutuximab infusion in patients with relapsed/refractory (RR) high-risk neuroblastoma (HRNBL).",
          "type": "conference-abstract",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Lung Cancer Research Studies",
            "Cancer therapeutics and mechanisms"
          ]
        },
        {
          "openalex_id": "W2468235813",
          "year": 1971,
          "title": "[Teaching of urology to undergraduates at the Medical Institute].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Medicine and Dermatology Studies History",
            "Diversity and Career in Medicine",
            "Innovations in Medical Education"
          ]
        },
        {
          "openalex_id": "W1532927955",
          "year": 1974,
          "title": "Studies on the effect of specific antisera on the metabolism of cellular antigens. I. Isolation of thymus leukemia antigens.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 19,
          "topics": [
            "Monoclonal and Polyclonal Antibodies Research",
            "Cancer and biochemical research",
            "Glycosylation and Glycoproteins Research"
          ]
        },
        {
          "openalex_id": "W1570733349",
          "year": 1974,
          "title": "Studies on the effect of specific antisera on the metabolism of cellular antigens. II. The synthesis and degradation of TL antigens of mouse cells in the presence of TL antiserum.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 30,
          "topics": [
            "Monoclonal and Polyclonal Antibodies Research",
            "Glycosylation and Glycoproteins Research",
            "Click Chemistry and Applications"
          ]
        },
        {
          "openalex_id": "W1917259224",
          "year": 1975,
          "title": "Detection of a TL(+) murine leukemia cell line that resists the cytotoxic effects of guinea pig complement and specific antiserum.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 4,
          "topics": [
            "Monoclonal and Polyclonal Antibodies Research",
            "Radiopharmaceutical Chemistry and Applications",
            "Animal Genetics and Reproduction"
          ]
        },
        {
          "openalex_id": "W2130465135",
          "year": 2010,
          "title": "Anti-GD2 Antibody with GM-CSF, Interleukin-2, and Isotretinoin for Neuroblastoma",
          "type": "article",
          "venue": "New England Journal of Medicine",
          "cited_by_count": 1822,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Toxin Mechanisms and Immunotoxins",
            "Virus-based gene therapy research"
          ]
        },
        {
          "openalex_id": "W2155118053",
          "year": 1984,
          "title": "Detection of ganglioside GD2 in tumor tissues and sera of neuroblastoma patients.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 373,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Glycosylation and Glycoproteins Research",
            "Toxin Mechanisms and Immunotoxins"
          ]
        },
        {
          "openalex_id": "W2068619849",
          "year": 1999,
          "title": "Intensive high-dose asparaginase consolidation improves survival for pediatric patients with T cell acute lymphoblastic leukemia and advanced stage lymphoblastic lymphoma: a Pediatric Oncology Group study",
          "type": "article",
          "venue": "Leukemia",
          "cited_by_count": 347,
          "topics": [
            "Acute Lymphoblastic Leukemia research",
            "Childhood Cancer Survivors' Quality of Life",
            "Lymphoma Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2136462971",
          "year": 2013,
          "title": "Purged versus non-purged peripheral blood stem-cell transplantation for high-risk neuroblastoma (COG A3973): a randomised phase 3 trial",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 312,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Cancer, Hypoxia, and Metabolism",
            "Cancer therapeutics and mechanisms"
          ]
        },
        {
          "openalex_id": "W2618869560",
          "year": 2017,
          "title": "Irinotecan–temozolomide with temsirolimus or dinutuximab in children with refractory or relapsed neuroblastoma (COG ANBL1221): an open-label, randomised, phase 2 trial",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 276,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Cancer therapeutics and mechanisms",
            "Glioma Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2017990475",
          "year": 1987,
          "title": "Importance of FSH-releasing protein and inhibin in erythrodifferentiation",
          "type": "article",
          "venue": "Nature",
          "cited_by_count": 274,
          "topics": [
            "Lipid metabolism and disorders",
            "Growth Hormone and Insulin-like Growth Factors",
            "Metabolism, Diabetes, and Cancer"
          ]
        },
        {
          "openalex_id": "W121485390",
          "year": 1983,
          "title": "Specific toxicity of 2-chlorodeoxyadenosine toward resting and proliferating human lymphocytes",
          "type": "article",
          "venue": "Blood",
          "cited_by_count": 273,
          "topics": [
            "Acute Lymphoblastic Leukemia research",
            "Biochemical and Molecular Research",
            "Chronic Lymphocytic Leukemia Research"
          ]
        },
        {
          "openalex_id": "W1936567301",
          "year": 1998,
          "title": "Phase I trial of a human-mouse chimeric anti-disialoganglioside monoclonal antibody ch14.18 in patients with refractory neuroblastoma and osteosarcoma.",
          "type": "article",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 253,
          "topics": [
            "Neuroblastoma Research and Treatments",
            "Toxin Mechanisms and Immunotoxins",
            "Cancer therapeutics and mechanisms"
          ]
        }
      ]
    }
  }
]
