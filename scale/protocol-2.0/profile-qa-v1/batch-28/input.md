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
    "name": "Judith Bosmans",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "71-RA",
        "title": "Does the scoring matter? The impact of using different EQ-5D scoring methods on cost-utility results",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5016039203",
      "display_name": "Judith E. Bosmans",
      "orcid": "0000-0002-1443-1026",
      "reported_affiliation": "Department of Health",
      "works_count": 377,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 86
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 38
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 36
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 35
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 31
        },
        {
          "topic": "Treatment of Major Depression",
          "works": 29
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 23
        },
        {
          "topic": "Frailty in Older Adults",
          "works": 19
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 19
        },
        {
          "topic": "Physical Activity and Health",
          "works": 15
        },
        {
          "topic": "Balance, Gait, and Falls Prevention",
          "works": 15
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 15
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Maurits W. van Tulder",
          "works": 80
        },
        {
          "name": "Johanna M. van Dongen",
          "works": 53
        },
        {
          "name": "Hein van Hout",
          "works": 43
        },
        {
          "name": "Harm van Marwijk",
          "works": 38
        },
        {
          "name": "Mohamed El Alili",
          "works": 29
        },
        {
          "name": "Ângela Jornada Ben",
          "works": 29
        },
        {
          "name": "Raymond Ostelo",
          "works": 25
        },
        {
          "name": "Pim Cuijpers",
          "works": 18
        },
        {
          "name": "Henriëtte E. van der Horst",
          "works": 18
        },
        {
          "name": "Janet L. MacNeil Vroomen",
          "works": 17
        },
        {
          "name": "Anneke van Schaik",
          "works": 16
        },
        {
          "name": "Willem van Mechelen",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162672484",
          "year": 2026,
          "title": "Cost-effectiveness of stepped care compared to continuous glucose monitoring in hypoglycemia-prone individuals with type 1 diabetes",
          "type": "article",
          "venue": "Diabetes Epidemiology and Management",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Research",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W7135414748",
          "year": 2026,
          "title": "Cost‐effectiveness of percutaneous nephrostomy vs <scp>JJ</scp> stent in obstructive urolithiasis: economic evaluation alongside the STent Or NEphrostomy (STONE) randomised controlled trial",
          "type": "article",
          "venue": "British Journal of Urology",
          "cited_by_count": 0,
          "topics": [
            "Kidney Stones and Urolithiasis Treatments",
            "Ureteral procedures and complications",
            "Bladder and Urothelial Cancer Treatments"
          ]
        },
        {
          "openalex_id": "W7161270374",
          "year": 2026,
          "title": "Effectiveness and cost-effectiveness of orthopaedic modifications to off-the-shelf footwear for people with first metatarsophalangeal joint osteoarthritis: study protocol for a randomised controlled trial",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Foot and Ankle Surgery",
            "Osteoarthritis Treatment and Mechanisms",
            "Diabetic Foot Ulcer Assessment and Management"
          ]
        },
        {
          "openalex_id": "W7161001821",
          "year": 2026,
          "title": "Oxygen saturation thresholds in children with acute respiratory distress (OxyKids): a multicentre, open, parallel-group, randomised clinical trial",
          "type": "article",
          "venue": "The Lancet Respiratory Medicine",
          "cited_by_count": 0,
          "topics": [
            "Respiratory Support and Mechanisms",
            "Neonatal Respiratory Health Research",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W7125612683",
          "year": 2026,
          "title": "The effectiveness of a nation-wide implemented fall prevention intervention in the Netherlands in reducing falls and fall-related injuries among community-dwelling older adults with an increased risk of falls: a randomized controlled trial",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Physical Activity and Health",
            "Context-Aware Activity Recognition Systems"
          ]
        },
        {
          "openalex_id": "W7170078588",
          "year": 2026,
          "title": "Transcranial magnetic stimulation for patients with exposure therapy resistant obsessive-compulsive disorder: TETRO - a study protocol for a multicenter randomized controlled trial (Preprint)",
          "type": "article",
          "venue": "JMIR Research Protocols",
          "cited_by_count": 0,
          "topics": [
            "Transcranial Magnetic Stimulation Studies",
            "Obsessive-Compulsive Spectrum Disorders",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W1989479757",
          "year": 1974,
          "title": "Ten years lyophilization of pathogenic fungi",
          "type": "article",
          "venue": "Mycopathologia",
          "cited_by_count": 17,
          "topics": [
            "Plant Pathogens and Fungal Diseases"
          ]
        },
        {
          "openalex_id": "W2014547452",
          "year": 1982,
          "title": "Prevalence of<i>Candida albicans</i>in patients receiving total parenteral nutrition",
          "type": "article",
          "venue": "Medical Mycology",
          "cited_by_count": 2,
          "topics": [
            "Antifungal resistance and susceptibility",
            "Neutropenia and Cancer Infections",
            "Central Venous Catheters and Hemodialysis"
          ]
        },
        {
          "openalex_id": "W961978345",
          "year": 1988,
          "title": "[Post-traumatic parietal pulmonary hernia].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Congenital Diaphragmatic Hernia Studies",
            "Trauma Management and Diagnosis",
            "Pleural and Pulmonary Diseases"
          ]
        },
        {
          "openalex_id": "W2613710301",
          "year": 1994,
          "title": "Milieu en kanker",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Family Support in Illness",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2922477494",
          "year": 2019,
          "title": "What does quality of life mean to older adults? A thematic synthesis",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 402,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Frailty in Older Adults",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2500628273",
          "year": 2016,
          "title": "European COMPARative Effectiveness research on blended Depression treatment versus treatment-as-usual (E-COMPARED): study protocol for a randomized controlled, non-inferiority trial in eight European countries",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 150,
          "topics": [
            "Digital Mental Health Interventions",
            "Mental Health Treatment and Access",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W1983677579",
          "year": 2010,
          "title": "Effect of integrated care for sick listed patients with chronic low back pain: economic evaluation alongside a randomised controlled trial",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 149,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Interprofessional Education and Collaboration",
            "Occupational Therapy Practice and Research"
          ]
        },
        {
          "openalex_id": "W2913806601",
          "year": 2019,
          "title": "The effect of a programme to improve men’s sedentary time and physical activity: The European Fans in Training (EuroFIT) randomised controlled trial",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 149,
          "topics": [
            "Physical Activity and Health",
            "Sports Performance and Training",
            "Cardiovascular and exercise physiology"
          ]
        },
        {
          "openalex_id": "W3004549148",
          "year": 2020,
          "title": "The effects of once- versus twice-weekly sessions on psychotherapy outcomes in depressed patients",
          "type": "article",
          "venue": "The British Journal of Psychiatry",
          "cited_by_count": 143,
          "topics": [
            "Digital Mental Health Interventions",
            "Psychotherapy Techniques and Applications",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W3014176310",
          "year": 2020,
          "title": "Low back pain should be considered a health and research priority in Brazil: Lost productivity and healthcare costs between 2012 to 2016",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 141,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Pesticide Exposure and Toxicity",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W2055098083",
          "year": 2012,
          "title": "Short‐Term Oral Nutritional Intervention with Protein and Vitamin D Decreases Falls in Malnourished Older Adults",
          "type": "article",
          "venue": "Journal of the American Geriatrics Society",
          "cited_by_count": 115,
          "topics": [
            "Nutrition and Health in Aging",
            "Frailty in Older Adults",
            "Balance, Gait, and Falls Prevention"
          ]
        },
        {
          "openalex_id": "W2140465986",
          "year": 2011,
          "title": "Post-Discharge Nutritional Support in Malnourished Elderly Individuals Improves Functional Limitations",
          "type": "article",
          "venue": "Journal of the American Medical Directors Association",
          "cited_by_count": 112,
          "topics": [
            "Nutrition and Health in Aging",
            "Frailty in Older Adults",
            "Clinical Nutrition and Gastroenterology"
          ]
        }
      ]
    }
  },
  {
    "name": "Julie Ratcliffe",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "194-RA",
        "title": "Assessing older people's health related quality of life in aged care settings: unravelling the EQ-5D self-report proxy conundrum.",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070505553",
      "display_name": "Julie Ratcliffe",
      "orcid": "0000-0001-7365-1988",
      "reported_affiliation": "Flinders University",
      "works_count": 506,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 198
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 97
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 87
        },
        {
          "topic": "Global Health Care Issues",
          "works": 42
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 37
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 35
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 35
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 31
        },
        {
          "topic": "Healthcare innovation and challenges",
          "works": 28
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 27
        },
        {
          "topic": "Frailty in Older Adults",
          "works": 24
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 20
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rachel Milte",
          "works": 79
        },
        {
          "name": "Gang Chen",
          "works": 76
        },
        {
          "name": "Maria Crotty",
          "works": 73
        },
        {
          "name": "John Brazier",
          "works": 57
        },
        {
          "name": "Jyoti Khadka",
          "works": 47
        },
        {
          "name": "Claire Hutchinson",
          "works": 47
        },
        {
          "name": "Billingsley Kaambwa",
          "works": 35
        },
        {
          "name": "Emily Lancsar",
          "works": 26
        },
        {
          "name": "Ian D. Cameron",
          "works": 26
        },
        {
          "name": "Craig Whitehead",
          "works": 25
        },
        {
          "name": "Christine Mpundu‐Kaambwa",
          "works": 23
        },
        {
          "name": "Stacey George",
          "works": 21
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169684198",
          "year": 2026,
          "title": "A Review of the Application of Generic Preference-Based Instruments with Older People Across Care Settings",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W7156015616",
          "year": 2026,
          "title": "A new health economic measure for improving the health and wellbeing of older Australians in subacute care settings: a study protocol",
          "type": "article",
          "venue": "BMC Geriatrics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Frailty in Older Adults",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W7163757207",
          "year": 2026,
          "title": "Determining the quality of life-aged care consumer threshold to identify good quality of life in older adults in long-term care",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Intergenerational Family Dynamics and Caregiving",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W7161347929",
          "year": 2026,
          "title": "Implementing iSupport in Dementia Care: a Playbook for Carers and Professionals",
          "type": "article",
          "venue": "Flinders University Library Research Data",
          "cited_by_count": 0,
          "topics": [
            "Technology Use by Older Adults",
            "Mobile Health and mHealth Applications",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W7151669996",
          "year": 2026,
          "title": "Lost in Translation? A Scoping Review to Explore the Translation and Cultural Adaptation of Preference-Based Measures of Quality of Life",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 2,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Cultural Differences and Values",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7163677720",
          "year": 2026,
          "title": "Measuring quality of life in autistic children and young people: comparing the performance of common generic health related quality of life instruments",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Family and Disability Support Research",
            "Childhood Cancer Survivors' Quality of Life",
            "Autism Spectrum Disorder Research"
          ]
        },
        {
          "openalex_id": "W2076536475",
          "year": 1890,
          "title": "OEsophageal Varices as a Cause of Haematemesis in Cirrhosis of the Liver",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 7,
          "topics": [
            "Liver Disease and Transplantation",
            "Liver Disease Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W1983089370",
          "year": 1979,
          "title": "Aneurysm after arterial puncture in Behcet's disease.",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 70,
          "topics": [
            "Ocular Diseases and Behçet’s Syndrome",
            "Retinal and Optic Conditions",
            "Vasculitis and related conditions"
          ]
        },
        {
          "openalex_id": "W1963769842",
          "year": 1993,
          "title": "Extra-market incentives in the new NHS",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 6,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare innovation and challenges",
            "Health Services Management and Policy"
          ]
        },
        {
          "openalex_id": "W80086533",
          "year": 1994,
          "title": "IVF (in-vitro fertilisation): the need to evaluate value for money.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 2,
          "topics": [
            "Assisted Reproductive Technology and Twin Pregnancy",
            "Reproductive Health and Technologies",
            "Family Dynamics and Relationships"
          ]
        },
        {
          "openalex_id": "W2523753543",
          "year": 2016,
          "title": "Health-related quality of life measured using the EQ-5D–5L: South Australian population norms",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 507,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W3145434052",
          "year": 2007,
          "title": "Measuring and Valuing Health Benefits for Economic Evaluation",
          "type": "article",
          "venue": "OUP Catalogue",
          "cited_by_count": 439,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1993655814",
          "year": 2011,
          "title": "Time Trade-Off Derived EQ-5D Weights for Australia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 267,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4382011420",
          "year": 2023,
          "title": "Patient navigation across the cancer care continuum: An overview of systematic reviews and emerging literature",
          "type": "review",
          "venue": "CA A Cancer Journal for Clinicians",
          "cited_by_count": 256,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Global Cancer Incidence and Screening",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W1968248151",
          "year": 2006,
          "title": "Randomised clinical trial, observational study and assessment of cost-effectiveness of the treatment of varicose veins (REACTIV trial)",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 225,
          "topics": [
            "Diagnosis and Treatment of Venous Diseases",
            "Dermatologic Treatments and Research",
            "Body Contouring and Surgery"
          ]
        },
        {
          "openalex_id": "W2949835654",
          "year": 2019,
          "title": "Aboriginal and Torres Strait Islander people's domains of wellbeing: A comprehensive literature review",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 216,
          "topics": [
            "Indigenous Health, Education, and Rights",
            "Global Health Workforce Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2143728664",
          "year": 2005,
          "title": "Longer term clinical and economic benefits of offering acupuncture care to patients with chronic low back pain",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 200,
          "topics": [
            "Acupuncture Treatment Research Studies",
            "Musculoskeletal pain and rehabilitation",
            "Complementary and Alternative Medicine Studies"
          ]
        },
        {
          "openalex_id": "W2010126736",
          "year": 2007,
          "title": "Effectiveness and Cost-Effectiveness of Three Types of Physiotherapy Used to Reduce Chronic Low Back Pain Disability",
          "type": "article",
          "venue": "Spine",
          "cited_by_count": 188,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Occupational Health and Performance"
          ]
        }
      ]
    }
  },
  {
    "name": "Juntana Pattanaphesaj",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2013030",
        "title": "Development of Thai population-based preference scores for EQ-5D-5L",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5040546783",
      "display_name": "Juntana Pattanaphesaj",
      "orcid": "0000-0003-1426-6777",
      "reported_affiliation": "Ministry of Public Health",
      "works_count": 9,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Diabetes Management and Education",
          "works": 1
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 1
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 1
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 1
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 1
        },
        {
          "topic": "Adolescent Sexual and Reproductive Health",
          "works": 1
        },
        {
          "topic": "Sex work and related issues",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Yot Teerawattananon",
          "works": 4
        },
        {
          "name": "Nan Luo",
          "works": 3
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 3
        },
        {
          "name": "Min‐Woo Jo",
          "works": 3
        },
        {
          "name": "Montarat Thavorncharoensap",
          "works": 2
        },
        {
          "name": "Sirinart Tongsiri",
          "works": 2
        },
        {
          "name": "Zhihao Yang",
          "works": 2
        },
        {
          "name": "Jeonghoon Ahn",
          "works": 2
        },
        {
          "name": "Eliza Lai‐Yi Wong",
          "works": 2
        },
        {
          "name": "Asrul Akmal Shafie",
          "works": 2
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 2
        },
        {
          "name": "Alia Luz",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4226324209",
          "year": 2022,
          "title": "Do health preferences differ among Asian populations? A comparison of EQ-5D-5L discrete choice experiments data from 11 Asian studies",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2955830860",
          "year": 2019,
          "title": "Cultural Values: Can They Explain Differences in Health Utilities between Countries?",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 69,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2795477621",
          "year": 2018,
          "title": "Identifying priority technical and context-specific issues in improving the conduct, reporting and use of health economic evaluation in low- and middle-income countries",
          "type": "article",
          "venue": "Health Research Policy and Systems",
          "cited_by_count": 37,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2810546336",
          "year": 2018,
          "title": "The EQ-5D-5L Valuation study in Thailand",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 202,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2904847110",
          "year": 2018,
          "title": "Valuation of EQ-5D-5L health states: a comparison of seven Asian populations",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 41,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2763074885",
          "year": 2017,
          "title": "Identifying Priority Methodological Issues in Economic Evaluation in Low- and Middle-Income Countries: Finding the Holy Grail",
          "type": "other",
          "venue": "Faculty of 1000 Research Ltd",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3197223485",
          "year": 2008,
          "title": "A report on identifying information regardingeffectiveness and cost-effectiveness of policy and strategies reorientation to mitigate the impact of HIV/AIDS in Thailand / by Juntana Pattanaphesaj ... [et al.]",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Impact and Responses"
          ]
        },
        {
          "openalex_id": "W2099490315",
          "year": 2010,
          "title": "Reviewing the evidence on effectiveness and cost-effectiveness of HIV prevention strategies in Thailand",
          "type": "article",
          "venue": "BMC Public Health",
          "cited_by_count": 20,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Adolescent Sexual and Reproductive Health",
            "Sex work and related issues"
          ]
        },
        {
          "openalex_id": "W2145356422",
          "year": 2015,
          "title": "Measurement properties of the EQ-5D-5L compared to EQ-5D-3L in the Thai diabetes patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 137,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Diabetes Management and Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Katie Page",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180301",
        "title": "Extension to 20180300: What aspects of quality of life are important to people with experience of cognitive or visual impairment? A qualitative investigation",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5103147397",
      "display_name": "Karen Page",
      "orcid": "0000-0001-9183-9175",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 276,
      "top_topics": [
        {
          "topic": "Pregnancy and preeclampsia studies",
          "works": 23
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 19
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 18
        },
        {
          "topic": "Birth, Development, and Health",
          "works": 18
        },
        {
          "topic": "Cancer Genomics and Diagnostics",
          "works": 17
        },
        {
          "topic": "Intensive Care Unit Cognitive Disorders",
          "works": 15
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 14
        },
        {
          "topic": "Genetic factors in colorectal cancer",
          "works": 12
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 11
        },
        {
          "topic": "Infection Control in Healthcare",
          "works": 10
        },
        {
          "topic": "Lymphoma Diagnosis and Treatment",
          "works": 10
        },
        {
          "topic": "Patient Safety and Medication Errors",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "D. R. Abramovich",
          "works": 42
        },
        {
          "name": "Linda Worrall‐Carter",
          "works": 40
        },
        {
          "name": "John Rolley",
          "works": 23
        },
        {
          "name": "Aidín McKinney",
          "works": 20
        },
        {
          "name": "Nicholas Graves",
          "works": 18
        },
        {
          "name": "Jacqui Shaw",
          "works": 17
        },
        {
          "name": "Aaron Conway",
          "works": 15
        },
        {
          "name": "David S. Guttery",
          "works": 14
        },
        {
          "name": "Allison Hills",
          "works": 14
        },
        {
          "name": "Daniel Fernández-García",
          "works": 14
        },
        {
          "name": "Kate Goddard",
          "works": 14
        },
        {
          "name": "Robert Hastings",
          "works": 14
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407888612",
          "year": 2025,
          "title": "Investigation of cancer specific DNA changes using oxford nanopore technology (ONT) and more traditional sequencing technologies in the surveillance of patients with neuroendocrine neoplasms",
          "type": "conference-abstract",
          "venue": "Endocrine Abstracts",
          "cited_by_count": 0,
          "topics": [
            "Nanopore and Nanochannel Transport Studies",
            "Microfluidic and Capillary Electrophoresis Applications",
            "Cancer Genomics and Diagnostics"
          ]
        },
        {
          "openalex_id": "W4407977226",
          "year": 2025,
          "title": "Outcomes from the Victorian Healthy Homes Program: a randomised control trial of home energy upgrades",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 2,
          "topics": [
            "Building Energy and Comfort Optimization",
            "Climate Change and Health Impacts",
            "Healthcare Facilities Design and Sustainability"
          ]
        },
        {
          "openalex_id": "W4404643703",
          "year": 2024,
          "title": "A qualitative systematic review of the impact of hearing on quality of life",
          "type": "review",
          "venue": "Quality of Life Research",
          "cited_by_count": 27,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Hearing Impairment and Communication",
            "Hearing, Cochlea, Tinnitus, Genetics"
          ]
        },
        {
          "openalex_id": "W4396944914",
          "year": 2024,
          "title": "Modelling the Impact of Organic Molecules and Phosphate Ions on Biosilica Pattern Formation in Diatoms",
          "type": "preprint",
          "venue": "arXiv (Cornell University)",
          "cited_by_count": 0,
          "topics": [
            "Diatoms and Algae Research"
          ]
        },
        {
          "openalex_id": "W4400973344",
          "year": 2024,
          "title": "Outcomes from the Victorian Healthy Homes Program: a randomised control trial of home energy upgrades",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 2,
          "topics": [
            "Building Energy and Comfort Optimization",
            "Energy Efficiency and Management"
          ]
        },
        {
          "openalex_id": "W4361952535",
          "year": 2023,
          "title": "Data from Mutation Analysis of Cell-Free DNA and Single Circulating Tumor Cells in Metastatic Breast Cancer Patients with High Circulating Tumor Cell Counts",
          "type": "other",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Cancer Genomics and Diagnostics",
            "Cancer Cells and Metastasis",
            "Chemical Reactions and Isotopes"
          ]
        },
        {
          "openalex_id": "W1983604496",
          "year": 1965,
          "title": "The development of dichlofenthion for the control of sheep maggot fly in the United Kingdom",
          "type": "article",
          "venue": "Veterinary Record",
          "cited_by_count": 2,
          "topics": [
            "Forensic Entomology and Diptera Studies",
            "Diptera species taxonomy and behavior",
            "Insect behavior and control techniques"
          ]
        },
        {
          "openalex_id": "W2016554711",
          "year": 1965,
          "title": "The use of chlorfenvinphos for the control of sheep maggot fly",
          "type": "article",
          "venue": "Veterinary Record",
          "cited_by_count": 4,
          "topics": [
            "Forensic Entomology and Diptera Studies",
            "Diptera species taxonomy and behavior",
            "Insect behavior and control techniques"
          ]
        },
        {
          "openalex_id": "W2041275317",
          "year": 1972,
          "title": "PATHWAYS OF WATER EXCHANGE IN THE FETOPLACENTAL UNIT AT MID‐PREGNANCY",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 20,
          "topics": [
            "Congenital Anomalies and Fetal Surgery",
            "Pregnancy and preeclampsia studies",
            "Urological Disorders and Treatments"
          ]
        },
        {
          "openalex_id": "W1986556958",
          "year": 1973,
          "title": "Pathways of water transfer between liquor amnii and the fetoplacental unit at term",
          "type": "article",
          "venue": "European Journal of Obstetrics & Gynecology and Reproductive Biology",
          "cited_by_count": 18,
          "topics": [
            "Pregnancy and preeclampsia studies"
          ]
        },
        {
          "openalex_id": "W2044002436",
          "year": 2010,
          "title": "Does Cognitive Impairment Predict Poor Self-Care in Patients with Heart Failure?",
          "type": "article",
          "venue": "European Journal of Heart Failure",
          "cited_by_count": 273,
          "topics": [
            "Heart Failure Treatment and Management",
            "Nursing care and research",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2053687970",
          "year": 1997,
          "title": "Long-chain polyunsaturated fatty acid transport across the perfused human placenta",
          "type": "article",
          "venue": "Placenta",
          "cited_by_count": 187,
          "topics": [
            "Fatty Acid Research and Health",
            "Birth, Development, and Health",
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W3125445170",
          "year": 2007,
          "title": "Organizations Non Gratae? The Impact of Unethical Corporate Acts on Interorganizational Networks",
          "type": "article",
          "venue": "Organization Science",
          "cited_by_count": 168,
          "topics": [
            "Management and Organizational Studies",
            "Ethics in Business and Education",
            "Corporate Social Responsibility Reporting"
          ]
        },
        {
          "openalex_id": "W2043586804",
          "year": 2000,
          "title": "A Quantitative Study on the Effects of Maternal Smoking on Placental Morphology and Cadmium Concentration",
          "type": "article",
          "venue": "Placenta",
          "cited_by_count": 139,
          "topics": [
            "Air Quality and Health Impacts",
            "Birth, Development, and Health",
            "Pregnancy and preeclampsia studies"
          ]
        },
        {
          "openalex_id": "W2040607098",
          "year": 2010,
          "title": "Symptom Recognition in Elders With Heart Failure",
          "type": "article",
          "venue": "Journal of Nursing Scholarship",
          "cited_by_count": 138,
          "topics": [
            "Traumatic Brain Injury Research",
            "Hearing Loss and Rehabilitation",
            "Vestibular and auditory disorders"
          ]
        },
        {
          "openalex_id": "W2029073075",
          "year": 2012,
          "title": "Screening for mild cognitive impairment in patients with heart failure: Montreal Cognitive Assessment versus Mini Mental State Exam",
          "type": "article",
          "venue": "European Journal of Cardiovascular Nursing",
          "cited_by_count": 132,
          "topics": [
            "Intensive Care Unit Cognitive Disorders",
            "Heart Failure Treatment and Management",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W2019474595",
          "year": 1999,
          "title": "Effect of Maternal Polyunsaturated Fatty Acid Concentration on Transport by the Human Placenta",
          "type": "article",
          "venue": "Neonatology",
          "cited_by_count": 107,
          "topics": [
            "Fatty Acid Research and Health",
            "Birth, Development, and Health",
            "Pregnancy and preeclampsia studies"
          ]
        },
        {
          "openalex_id": "W2344165861",
          "year": 2016,
          "title": "Absolute risk of cardiovascular disease events, and blood pressure‐ and lipid‐lowering therapy in Australia",
          "type": "article",
          "venue": "The Medical Journal of Australia",
          "cited_by_count": 104,
          "topics": [
            "Lipoproteins and Cardiovascular Health",
            "Health Promotion and Cardiovascular Prevention",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        }
      ]
    }
  },
  {
    "name": "Katie Spencer",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180670",
        "title": "EQ-5D-3L as an outcome indicator: analysis of its performance in a longitudinal study of patients receiving palliative care",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5073760994",
      "display_name": "Katie Spencer",
      "orcid": "0000-0002-6846-4341",
      "reported_affiliation": "University of Leeds",
      "works_count": 89,
      "top_topics": [
        {
          "topic": "Advances in Oncology and Radiotherapy",
          "works": 27
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 18
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 15
        },
        {
          "topic": "Management of metastatic bone disease",
          "works": 12
        },
        {
          "topic": "Advanced Radiotherapy Techniques",
          "works": 12
        },
        {
          "topic": "Lung Cancer Treatments and Mutations",
          "works": 7
        },
        {
          "topic": "COVID-19 and healthcare impacts",
          "works": 6
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 6
        },
        {
          "topic": "Colorectal Cancer Screening and Detection",
          "works": 6
        },
        {
          "topic": "Colorectal Cancer Surgical Treatments",
          "works": 6
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 5
        },
        {
          "topic": "Hepatocellular Carcinoma Treatment and Prognosis",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Eva Morris",
          "works": 11
        },
        {
          "name": "David Sebag‐Montefiore",
          "works": 11
        },
        {
          "name": "Christopher M. Jones",
          "works": 9
        },
        {
          "name": "K. Franks",
          "works": 8
        },
        {
          "name": "P J Finan",
          "works": 7
        },
        {
          "name": "Ann Henry",
          "works": 6
        },
        {
          "name": "M. Snee",
          "works": 6
        },
        {
          "name": "Daniela Tataru",
          "works": 6
        },
        {
          "name": "Gerard Walls",
          "works": 6
        },
        {
          "name": "Catherine Roe",
          "works": 5
        },
        {
          "name": "Yvette M. van der Linden",
          "works": 5
        },
        {
          "name": "Peter S Hall",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7129016208",
          "year": 2026,
          "title": "Influence of stage at cancer diagnosis on NHS hospital care costs in England: a national, retrospective, population-based cohort study using individual patient-level data",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 0,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Medical Coding and Health Information",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W7164842472",
          "year": 2026,
          "title": "Pulmonary extracellular vesicles drive alveolar macrophage dysfunction via microRNA transfer in Acute Respiratory Distress Syndrome",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Extracellular vesicles in disease",
            "Immune cells in cancer",
            "Neutrophil, Myeloperoxidase and Oxidative Mechanisms"
          ]
        },
        {
          "openalex_id": "W7126063117",
          "year": 2026,
          "title": "Research training in radiation oncology: a scoping review of global pathways, barriers and enablers",
          "type": "article",
          "venue": "Critical Reviews in Oncology/Hematology",
          "cited_by_count": 1,
          "topics": [
            "Advances in Oncology and Radiotherapy",
            "Radiology practices and education",
            "Health and Medical Research Impacts"
          ]
        },
        {
          "openalex_id": "W4410588574",
          "year": 2025,
          "title": "1532 A Systematic Review of Global Pathways for, and Barriers and Enablers to, Clinical Academic Training in Radiation Oncology",
          "type": "article",
          "venue": "Radiotherapy and Oncology",
          "cited_by_count": 0,
          "topics": [
            "Advances in Oncology and Radiotherapy",
            "Economic and Financial Impacts of Cancer",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W4413173148",
          "year": 2025,
          "title": "A Scoping Review of Global Enablers and Barriers to Training the Next Generation of Radiation Oncology Physician Scientists",
          "type": "article",
          "venue": "International Journal of Radiation Oncology*Biology*Physics",
          "cited_by_count": 0,
          "topics": [
            "Advances in Oncology and Radiotherapy",
            "Health and Medical Research Impacts",
            "Global Health and Surgery"
          ]
        },
        {
          "openalex_id": "W4416634950",
          "year": 2025,
          "title": "Extracellular vesicles mediate macrophage dysfunction and metabolic reprogramming in idiopathic pulmonary fibrosis",
          "type": "conference-abstract",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis",
            "Extracellular vesicles in disease",
            "Pulmonary Hypertension Research and Treatments"
          ]
        },
        {
          "openalex_id": "W2077850998",
          "year": 1995,
          "title": "Essential oils and massage in cancer",
          "type": "article",
          "venue": "International Journal of Aromatherapy",
          "cited_by_count": 0,
          "topics": [
            "Complementary and Alternative Medicine Studies"
          ]
        },
        {
          "openalex_id": "W1644244337",
          "year": 2002,
          "title": "Full-scale clinical implementation of a video based respiratory gating system",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "Advanced Radiotherapy Techniques",
            "Lung Cancer Diagnosis and Treatment",
            "Advances in Oncology and Radiotherapy"
          ]
        },
        {
          "openalex_id": "W2330780483",
          "year": 2004,
          "title": "Chemical durability of phosphate laser glasses",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Glass properties and applications",
            "Solid State Laser Technologies",
            "Laser Material Processing Techniques"
          ]
        },
        {
          "openalex_id": "W1980797870",
          "year": 2004,
          "title": "Public awareness of risk factors and screening for colorectal cancer in Europe",
          "type": "article",
          "venue": "European Journal of Cancer Prevention",
          "cited_by_count": 111,
          "topics": [
            "Colorectal Cancer Screening and Detection",
            "Genetic factors in colorectal cancer",
            "Gastric Cancer Management and Outcomes"
          ]
        },
        {
          "openalex_id": "W3121455070",
          "year": 2021,
          "title": "Impact of the COVID-19 pandemic on the detection and management of colorectal cancer in England: a population-based study",
          "type": "article",
          "venue": "The Lancet. Gastroenterology & hepatology",
          "cited_by_count": 334,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 Clinical Research Studies",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W3121958975",
          "year": 2021,
          "title": "The impact of the COVID-19 pandemic on radiotherapy services in England, UK: a population-based study",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 168,
          "topics": [
            "COVID-19 and healthcare impacts",
            "Advances in Oncology and Radiotherapy",
            "Infection Control and Ventilation"
          ]
        },
        {
          "openalex_id": "W2986230280",
          "year": 2018,
          "title": "Palliative radiotherapy",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 98,
          "topics": [
            "Management of metastatic bone disease",
            "Brain Metastases and Treatment",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W2945592235",
          "year": 2019,
          "title": "Systematic Review of the Role of Stereotactic Radiotherapy for Bone Metastases",
          "type": "review",
          "venue": "JNCI Journal of the National Cancer Institute",
          "cited_by_count": 86,
          "topics": [
            "Management of metastatic bone disease",
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Advanced Radiotherapy Techniques"
          ]
        },
        {
          "openalex_id": "W3131433923",
          "year": 2021,
          "title": "Low‐dose pembrolizumab in the treatment of advanced non‐small cell lung cancer",
          "type": "article",
          "venue": "International Journal of Cancer",
          "cited_by_count": 62,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Lung Cancer Treatments and Mutations",
            "Esophageal Cancer Research and Treatment"
          ]
        },
        {
          "openalex_id": "W2046157316",
          "year": 2015,
          "title": "30 day mortality in adult palliative radiotherapy – A retrospective population based study of 14,972 treatment episodes",
          "type": "article",
          "venue": "Radiotherapy and Oncology",
          "cited_by_count": 58,
          "topics": [
            "Management of metastatic bone disease",
            "Palliative Care and End-of-Life Issues",
            "Lung Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2281289152",
          "year": 2016,
          "title": "Wide Variation in the Use of Radiotherapy in the Management of Surgically Treated Rectal Cancer Across the English National Health Service",
          "type": "article",
          "venue": "Clinical Oncology",
          "cited_by_count": 58,
          "topics": [
            "Colorectal Cancer Surgical Treatments",
            "Advances in Oncology and Radiotherapy",
            "Colorectal and Anal Carcinomas"
          ]
        }
      ]
    }
  }
]
