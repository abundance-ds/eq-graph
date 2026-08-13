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
    "name": "madeeha malik",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1670-VS",
        "title": "Developing an EQ-5D-5L Value Set for Pakistan",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180660",
        "title": "Developing an EQ-5D-3L Value Set and Population Norms for Pakistan – A Pilot Study",
        "working_group": "Valuation"
      },
      {
        "project_id": "344-VS",
        "title": "Testing the feasibility and acceptability of the EQ-5D-Y-3L valuation protocol in adolescents and adults in Pakistan",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5053689562",
      "display_name": "Madeeha Malik",
      "orcid": "0000-0001-5824-9405",
      "reported_affiliation": "Health Services Academy",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 19
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 14
        },
        {
          "topic": "Health and Well-being Studies",
          "works": 12
        },
        {
          "topic": "Malaria Research and Control",
          "works": 9
        },
        {
          "topic": "Antibiotic Use and Resistance",
          "works": 8
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 8
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 7
        },
        {
          "topic": "Health and Wellbeing Research",
          "works": 6
        },
        {
          "topic": "Pharmaceutical Quality and Counterfeiting",
          "works": 5
        },
        {
          "topic": "Eating Disorders and Behaviors",
          "works": 5
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 5
        },
        {
          "topic": "Diverse Scientific Research Studies",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Azhar Hussain",
          "works": 76
        },
        {
          "name": "Ayisha Hashmi",
          "works": 27
        },
        {
          "name": "Mohamed Azmi Hassali",
          "works": 13
        },
        {
          "name": "Asrul Akmal Shafie",
          "works": 11
        },
        {
          "name": "Shazia Jamshed",
          "works": 6
        },
        {
          "name": "Márió Gajdács",
          "works": 4
        },
        {
          "name": "Mohamed Izham Mohamed Ibrahim",
          "works": 4
        },
        {
          "name": "Shazana Rana",
          "works": 4
        },
        {
          "name": "Martie S. Lubbe",
          "works": 4
        },
        {
          "name": "Ning Yan Gu",
          "works": 3
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 3
        },
        {
          "name": "Nida Nadeem",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7169611373",
          "year": 2026,
          "title": "Attitude of healthcare professionals in Pakistan towards inter-professional collaborative competencies: A cross-sectional study",
          "type": "article",
          "venue": "Medicine",
          "cited_by_count": 0,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Innovations in Medical Education",
            "Competency Development and Evaluation"
          ]
        },
        {
          "openalex_id": "W4414479755",
          "year": 2025,
          "title": "1355 Use of Pharmacist eCare Plan and EHR Integration to Promote Team-based Care: Early Experiences in Bridging Community Pharmacists and Prescribers",
          "type": "article",
          "venue": "Journal of the American Pharmacists Association",
          "cited_by_count": 0,
          "topics": [
            "Pharmacy and Medical Practices",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W4409381348",
          "year": 2025,
          "title": "A Case Report of Summer Seasonal Affective Disorder: An Underrecognized Condition in Tropical Regions.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Circadian rhythm and melatonin"
          ]
        },
        {
          "openalex_id": "W4415444256",
          "year": 2025,
          "title": "Effects of Design Thinking on Learners' Motivation at Higher Education Level",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Education and Learning Interventions"
          ]
        },
        {
          "openalex_id": "W4411895617",
          "year": 2025,
          "title": "Findings from a roundtable discussion with Pakistani stakeholders on measuring and valuing health and health-related quality of life for children and adolescents",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4414639312",
          "year": 2025,
          "title": "Pharmacovigilance in Pakistan: A Neglected Link",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Pharmacovigilance and Adverse Drug Reactions",
            "Pharmaceutical Economics and Policy",
            "Computational Drug Discovery Methods"
          ]
        },
        {
          "openalex_id": "W2998229533",
          "year": 2005,
          "title": "THE IMPACT OF RHEUMATOID ARTHRITIS ON HEALTH RELATED QUALITY OF LIFE: A LITERATURE REVIEW OF DEVELOPED AND DEVELOPING WORLD",
          "type": "review",
          "venue": "Journal of Medical Pharmaceutical",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies",
            "Systemic Lupus Erythematosus Research",
            "Hepatitis C virus research"
          ]
        },
        {
          "openalex_id": "W2160618843",
          "year": 2007,
          "title": "Plantar fibromatosis and Dupuytren's disease: an association to remember in patients with diabetes",
          "type": "article",
          "venue": "Diabetic Medicine",
          "cited_by_count": 16,
          "topics": [
            "Dupuytren's Contracture and Treatments",
            "Skin Diseases and Diabetes",
            "Genital Health and Disease"
          ]
        },
        {
          "openalex_id": "W4245391468",
          "year": 2011,
          "title": "Letters to the Editor",
          "type": "letter",
          "venue": "Journal of Pharmacy Practice and Research",
          "cited_by_count": 1,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Pharmaceutical studies and practices",
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W1969130826",
          "year": 2011,
          "title": "PIN100 Why Don't Health Practitioners Prescribe Rationally in Malaria? A qualitative Study from Pakistan",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Antibiotic Use and Resistance"
          ]
        },
        {
          "openalex_id": "W3035962087",
          "year": 2020,
          "title": "Sale of WHO AWaRe groups antibiotics without a prescription in Pakistan: a simulated client study",
          "type": "article",
          "venue": "Journal of Pharmaceutical Policy and Practice",
          "cited_by_count": 110,
          "topics": [
            "Antibiotic Use and Resistance",
            "Pharmaceutical Quality and Counterfeiting",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4387026668",
          "year": 2023,
          "title": "International consensus on patient-centred outcomes in eating disorders",
          "type": "article",
          "venue": "The Lancet Psychiatry",
          "cited_by_count": 46,
          "topics": [
            "Eating Disorders and Behaviors",
            "Child Nutrition and Feeding Issues",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W2806439355",
          "year": 2017,
          "title": "Health Literacy as a Global Public Health Concern: A Systematic Review",
          "type": "review",
          "venue": "Journal of pharmacology & clinical research",
          "cited_by_count": 41,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Global Public Health Policies and Epidemiology",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W2004939027",
          "year": 2012,
          "title": "Effects of drug-polymer dispersions on solubility and in vitro diffusion of artemisinin across a polydimethylsiloxane membrane",
          "type": "article",
          "venue": "Chinese Science Bulletin",
          "cited_by_count": 31,
          "topics": [
            "Drug Solubulity and Delivery Systems",
            "Advancements in Transdermal Drug Delivery",
            "Pharmacological Effects of Natural Compounds"
          ]
        },
        {
          "openalex_id": "W2118720310",
          "year": 2013,
          "title": "Assessment of disease management of insomnia at community pharmacies through simulated visits in Pakistan",
          "type": "article",
          "venue": "Pharmacy Practice",
          "cited_by_count": 24,
          "topics": [
            "Sleep and related disorders",
            "Pharmaceutical Practices and Patient Outcomes",
            "Sleep and Wakefulness Research"
          ]
        },
        {
          "openalex_id": "W2015164718",
          "year": 2013,
          "title": "A Literature Review: Pharmaceutical Care an Evolving Role at Community Pharmacies in Pakistan",
          "type": "article",
          "venue": "Pharmacology &amp Pharmacy",
          "cited_by_count": 23,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W3025434622",
          "year": 2020,
          "title": "A step towards gender equity to strengthen the pharmaceutical workforce during COVID-19",
          "type": "article",
          "venue": "Journal of Pharmaceutical Policy and Practice",
          "cited_by_count": 23,
          "topics": [
            "Diversity and Career in Medicine",
            "Sex and Gender in Healthcare",
            "Gender Diversity and Inequality"
          ]
        },
        {
          "openalex_id": "W3202128814",
          "year": 2021,
          "title": "Adoption of health technologies for effective health information system: Need of the hour for Pakistan",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 21,
          "topics": [
            "Electronic Health Records Systems"
          ]
        }
      ]
    }
  },
  {
    "name": "Maja Kuharic",
    "member_affiliation": "Northwestern University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1514-RA",
        "title": "Comparing Measurement Properties of the EQ Health and Wellbeing Experimental Version (Long and Short) and the EQ-5D-5L in the Italian Population",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1811-RA",
        "title": "EQ-5D-5L and EQ-HWB: Assessing Distinctiveness of Frequency vs. Severity Response Scales in Pain and Discomfort & Instruments Convergent Validity in the Context of Self-Reported Chronic Conditions",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "1915-RA",
        "title": "Evaluating Changes to the EQ-HWB/EQ-HWB-S: Examining the Psychometric Properties Using Modern Test Theory of Merged Double-Barreled Items (Concentrating/Thinking Clearly and Walking Inside/Outside) in the EQ-HWB/EQ-HWB-S among Patients and Caregivers",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2037-RA",
        "title": "Evaluating Psychometric Properties of EQ-5D-5L Skin Bolt-On in Patients with Mild-to-Moderate Psoriasis: A Longitudinal Analysis of three Phase III Clinical Trial Data",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2040-RA",
        "title": "Investigating the Interpretation of EQ-HWB and EQ-HWB-S Response Options in the UK, USA, Germany, and China",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2042-RA",
        "title": "Exploring Stakeholder Preferences for Presenting EQ-5D Data in U.S. Clinical Rheumatology Practice to Enhance Outcome Assessment and Clinical Care",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "414-PHD",
        "title": "Exploration of patient self-perceived burden to caregivers as a construct captured by existing EQ measures and assessing measurement properties of EQ-HWB as a measure for caregivers",
        "working_group": "Descriptive Systems, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5007210675",
      "display_name": "Maja Kuharić",
      "orcid": "0000-0003-3696-9086",
      "reported_affiliation": "Northwestern University",
      "works_count": 84,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 22
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 13
        },
        {
          "topic": "Inflammatory Bowel Disease",
          "works": 8
        },
        {
          "topic": "Parkinson's Disease Mechanisms and Treatments",
          "works": 6
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 5
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 5
        },
        {
          "topic": "Polyomavirus and related diseases",
          "works": 5
        },
        {
          "topic": "Anorectal Disease Treatments and Outcomes",
          "works": 5
        },
        {
          "topic": "Health Education and Validation",
          "works": 4
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 4
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "A. Simon Pickard",
          "works": 29
        },
        {
          "name": "David Cella",
          "works": 20
        },
        {
          "name": "Brendan Mulhern",
          "works": 12
        },
        {
          "name": "John Devin Peipert",
          "works": 11
        },
        {
          "name": "Courtney N. Hurt",
          "works": 11
        },
        {
          "name": "A Monteiro",
          "works": 10
        },
        {
          "name": "Robin S. Turpin",
          "works": 10
        },
        {
          "name": "Justin D. Smith",
          "works": 9
        },
        {
          "name": "Sara Shaunfield",
          "works": 9
        },
        {
          "name": "Kimberly Webster",
          "works": 7
        },
        {
          "name": "Kevin Fowler",
          "works": 7
        },
        {
          "name": "Tessa Peasgood",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162426747",
          "year": 2026,
          "title": "Additional file 1 of Burden and disutility of sleep disturbance and early morning OFF symptoms in people with advancing Parkinson’s disease: a vignette-based approach using the EQ-5D-5L",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Balance, Gait, and Falls Prevention",
            "Sleep and related disorders"
          ]
        },
        {
          "openalex_id": "W7162455699",
          "year": 2026,
          "title": "Additional file 1 of Burden and disutility of sleep disturbance and early morning OFF symptoms in people with advancing Parkinson’s disease: a vignette-based approach using the EQ-5D-5L",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Balance, Gait, and Falls Prevention",
            "Sleep and related disorders"
          ]
        },
        {
          "openalex_id": "W7121409146",
          "year": 2026,
          "title": "Additional file 1 of Development of a conceptual model of BKV impacts on health-related quality of life in kidney transplant recipients: a qualitative study",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Polyomavirus and related diseases",
            "Viral Infections and Outbreaks Research",
            "Viral-associated cancers and disorders"
          ]
        },
        {
          "openalex_id": "W7121596055",
          "year": 2026,
          "title": "Additional file 1 of Development of a conceptual model of BKV impacts on health-related quality of life in kidney transplant recipients: a qualitative study",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Polyomavirus and related diseases",
            "Viral Infections and Outbreaks Research",
            "Viral-associated cancers and disorders"
          ]
        },
        {
          "openalex_id": "W7131637639",
          "year": 2026,
          "title": "Additional file 1 of Psychometric properties of the Clinical Sustainability Assessment Tool (CSAT) short form across three research centers evaluating effectiveness and implementation of a cancer symptom surveillance and management intervention",
          "type": "article",
          "venue": "Open MIND",
          "cited_by_count": 0,
          "topics": [
            "Climate Change and Health Impacts",
            "Health Policy Implementation Science",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W7131664923",
          "year": 2026,
          "title": "Additional file 1 of Psychometric properties of the Clinical Sustainability Assessment Tool (CSAT) short form across three research centers evaluating effectiveness and implementation of a cancer symptom surveillance and management intervention",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Climate Change and Health Impacts",
            "Health Policy Implementation Science",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2955067070",
          "year": 2019,
          "title": "PNS135 ATTITUDES TOWARD DRUG PRICING IN THE US: FINDINGS FROM A SURVEY IN THE GENERAL POPULATION",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical industry and healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2956039522",
          "year": 2019,
          "title": "PNS247 PATIENT BURDEN TO FAMILY: AN EXAMINATION OF IMPORTANCE AND WORDING",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W3134135434",
          "year": 2020,
          "title": "E-QALY: face validity testing the items for a new generic preference-based measure",
          "type": "conference-paper",
          "venue": "Deakin Research Online (Deakin University)",
          "cited_by_count": 1,
          "topics": [
            "Impact of AI and Big Data on Business and Society"
          ]
        },
        {
          "openalex_id": "W3027263985",
          "year": 2020,
          "title": "PMU107 CONTEMPORARY TRENDS IN USE OF PATIENT-REPORTED OUTCOME MEASURES OF HEALTH IN CLINICAL TRIALS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
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
          "openalex_id": "W4214702737",
          "year": 2022,
          "title": "Generation, Selection, and Face Validation of Items for a New Generic Measure of Quality of Life: The EQ-HWB",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 38,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4220657799",
          "year": 2022,
          "title": "A Comparison of a Preliminary Version of the EQ-HWB Short and the 5-Level Version EQ-5D",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4392812797",
          "year": 2024,
          "title": "Comparison of the EQ-HWB and EQ-HWB-S With Other Preference-Based Measures Among United States Informal Caregivers",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 28,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Intergenerational Family Dynamics and Caregiving",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4392815424",
          "year": 2024,
          "title": "The Measurement Properties of the EQ-HWB and the EQ-HWB-S in Italian Population: A Comparative Study With EQ-5D-5L",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 20,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Education",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4410079601",
          "year": 2025,
          "title": "Web-Based Cancer Symptom Self-Management System",
          "type": "article",
          "venue": "JAMA Network Open",
          "cited_by_count": 11,
          "topics": [
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4391542822",
          "year": 2024,
          "title": "Care recipient self-perceived burden: Perspectives of individuals with chronic health conditions or personal experiences with caregiving on caregiver burden in the US",
          "type": "article",
          "venue": "SSM - Qualitative Research in Health",
          "cited_by_count": 10,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues",
            "Family and Patient Care in Intensive Care Units"
          ]
        }
      ]
    }
  },
  {
    "name": "Maksat Jumamyradov",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1716-TVG",
        "title": "Scale and rate heterogeneity in EQ-5D-5L valuation.",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "207-RA",
        "title": "Fast-Track Proposal: Scale, Rate, and Premium (SCRAP) in Health Valuation",
        "working_group": "Valuation"
      },
      {
        "project_id": "2428-RA",
        "title": "Comparison of modes of administration and data Quality Control in DCE with duration surveys",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5067862987",
      "display_name": "Maksat Jumamyradov",
      "orcid": "0009-0008-0180-7224",
      "reported_affiliation": "University of South Florida",
      "works_count": 10,
      "top_topics": [
        {
          "topic": "Economic and Environmental Valuation",
          "works": 7
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 3
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Environmental Education and Sustainability",
          "works": 1
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 1
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 1
        },
        {
          "topic": "Statistical Methods and Bayesian Inference",
          "works": 1
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 1
        },
        {
          "topic": "Statistical Methods and Inference",
          "works": 1
        },
        {
          "topic": "Survey Methodology and Nonresponse",
          "works": 1
        },
        {
          "topic": "Quality and Management Systems",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Benjamin M. Craig",
          "works": 8
        },
        {
          "name": "Murat K. Munkin",
          "works": 4
        },
        {
          "name": "William H. Greene",
          "works": 3
        },
        {
          "name": "Michał Jakubczyk",
          "works": 3
        },
        {
          "name": "Oliver Rivero‐Arias",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413441169",
          "year": 2025,
          "title": "Revisiting the Valuation of Child Health-Related Quality of Life",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        },
        {
          "openalex_id": "W4393217008",
          "year": 2024,
          "title": "Biases in the Maximum Simulated Likelihood Estimation of the Mixed Logit Model",
          "type": "article",
          "venue": "Econometrics",
          "cited_by_count": 2,
          "topics": [
            "Statistical Methods and Inference"
          ]
        },
        {
          "openalex_id": "W4400578645",
          "year": 2024,
          "title": "Comparing the Mixed Logit Estimates and True Parameters under Informative and Uninformative Heterogeneity: A Simulated Discrete Choice Experiment",
          "type": "article",
          "venue": "Computational Economics",
          "cited_by_count": 12,
          "topics": [
            "Economic and Environmental Valuation",
            "Environmental Education and Sustainability",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4403997215",
          "year": 2024,
          "title": "Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4416511331",
          "year": 2024,
          "title": "Referee report. For: Using the OPUF approach to create a value set for the EQ-HWB-S: An exploratory feasibility study [version 1; peer review: 1 approved]",
          "type": "article",
          "venue": "Faculty of 1000 Research Ltd",
          "cited_by_count": 0,
          "topics": [
            "Quality and Management Systems",
            "Delphi Technique in Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4400608645",
          "year": 2024,
          "title": "Scale and rate heterogeneity in the EQ-5D-5L valuation",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4200192334",
          "year": 2021,
          "title": "Biases in Maximum Simulated Likelihood Estimation of Bivariate Models",
          "type": "article",
          "venue": "Journal of Econometric Methods",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Statistical Methods and Bayesian Inference",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4387940627",
          "year": 2023,
          "title": "Child health valuation protocol for a discrete choice experiment comparing paired comparison and kaizen tasks and estimating US EQ-5D-Y-3L values on an experience scale",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 6,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4318052529",
          "year": 2023,
          "title": "Comparing the Conditional Logit Estimates and True Parameters under Preference Heterogeneity: A Simulated Discrete Choice Experiment",
          "type": "article",
          "venue": "Econometrics",
          "cited_by_count": 11,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4400850897",
          "year": 2024,
          "title": "The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Survey Methodology and Nonresponse"
          ]
        }
      ]
    }
  },
  {
    "name": "Malin Regardt",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "352-RA",
        "title": "Exploring the potential of using EQ-5D-3L versus EQ-5D-5L to assess the value of a national large-scale health care improvement initiative in rheumatology in Sweden",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5010406225",
      "display_name": "Malin Regardt",
      "orcid": "0000-0002-1908-5708",
      "reported_affiliation": "Karolinska University Hospital",
      "works_count": 57,
      "top_topics": [
        {
          "topic": "Inflammatory Myopathies and Dermatomyositis",
          "works": 31
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 15
        },
        {
          "topic": "Parkinson's Disease and Spinal Disorders",
          "works": 11
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 10
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 6
        },
        {
          "topic": "Systemic Sclerosis and Related Diseases",
          "works": 4
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 4
        },
        {
          "topic": "Muscle and Compartmental Disorders",
          "works": 4
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 3
        },
        {
          "topic": "Myofascial pain diagnosis and treatment",
          "works": 3
        },
        {
          "topic": "Muscle Physiology and Disorders",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Helene Alexanderson",
          "works": 26
        },
        {
          "name": "Ingrid E. Lundberg",
          "works": 19
        },
        {
          "name": "Ingrid de Groot",
          "works": 13
        },
        {
          "name": "Lisa Christopher‐Stine",
          "works": 13
        },
        {
          "name": "Catherine Sarver",
          "works": 12
        },
        {
          "name": "Christopher A. Mecoli",
          "works": 10
        },
        {
          "name": "Emelie Heintz",
          "works": 10
        },
        {
          "name": "Ioannis Parodis",
          "works": 10
        },
        {
          "name": "Elisabet Welin Henriksson",
          "works": 9
        },
        {
          "name": "Jin Kyun Park",
          "works": 9
        },
        {
          "name": "Merrilee Needham",
          "works": 8
        },
        {
          "name": "Yeong Wook Song",
          "works": 8
        }
      ],
      "work_examples": [
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
          "openalex_id": "W7163699897",
          "year": 2026,
          "title": "P.311 Structured assessment of patients with raynaud’s phenomenon- a way to follow patients with signs of very early diagnosis of systemic sclerosis",
          "type": "conference-paper",
          "venue": "Poster presentations",
          "cited_by_count": 0,
          "topics": [
            "Systemic Sclerosis and Related Diseases",
            "Vasculitis and related conditions",
            "Diagnosis and Treatment of Venous Diseases"
          ]
        },
        {
          "openalex_id": "W7151938732",
          "year": 2026,
          "title": "The value of EQ-5D-3L and EQ VAS as a patient-reported outcome measure for patients with ankylosing spondylitis in routine healthcare: an evaluation of construct validity and responsiveness based on the Swedish Rheumatology Quality Register",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7152023812",
          "year": 2026,
          "title": "The value of EQ-5D-3L and EQ VAS as a patient-reported outcome measure for patients with ankylosing spondylitis in routine healthcare: an evaluation of construct validity and responsiveness based on the Swedish Rheumatology Quality Register",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4416977462",
          "year": 2025,
          "title": "Health outcomes in hospitalised and non-hospitalised individuals after COVID-19, an observational, cross-sectional study",
          "type": "article",
          "venue": "Communications Medicine",
          "cited_by_count": 3,
          "topics": [
            "Long-Term Effects of COVID-19",
            "Intensive Care Unit Cognitive Disorders",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W2105986513",
          "year": 2010,
          "title": "Patients with polymyositis or dermatomyositis have reduced grip force and health-related quality of life in comparison with reference values: an observational study",
          "type": "article",
          "venue": "Lara D. Veeken",
          "cited_by_count": 70,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Parkinson's Disease and Spinal Disorders",
            "Muscle Physiology and Disorders"
          ]
        },
        {
          "openalex_id": "W2332664084",
          "year": 2012,
          "title": "AB1459-HPR Despite low disease activity patients with poly- and dermatomyositis perceive activity limitation, reduced grip force and quality of life longitudinally",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 0,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis"
          ]
        },
        {
          "openalex_id": "W1890498445",
          "year": 2013,
          "title": "Improvement in Health and Possible Reduction in Disease Activity Using Endurance Exercise in Patients With Established Polymyositis and Dermatomyositis: A Multicenter Randomized Controlled Trial With a 1‐Year Open Extension Followup",
          "type": "article",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 103,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W2330919466",
          "year": 2013,
          "title": "SAT0579-HPR The Work Ability in Patients with Polymy- and Dermatomyositis is Affected: a Cross-Sectional Study",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 0,
          "topics": [
            "Polish Legal and Social Issues",
            "Fibromyalgia and Chronic Fatigue Syndrome Research"
          ]
        },
        {
          "openalex_id": "W2890646705",
          "year": 2018,
          "title": "Perceptions of Patients, Caregivers, and Healthcare Providers of Idiopathic Inflammatory Myopathies: An International OMERACT Study",
          "type": "article",
          "venue": "The Journal of Rheumatology",
          "cited_by_count": 49,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Parkinson's Disease and Spinal Disorders",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W2513888049",
          "year": 2016,
          "title": "Health-Related Quality of Life (HRQoL) in Idiopathic Inflammatory Myopathy: A Systematic Review",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 46,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Celiac Disease Research and Management",
            "Eosinophilic Disorders and Syndromes"
          ]
        },
        {
          "openalex_id": "W2915016030",
          "year": 2019,
          "title": "OMERACT 2018 Modified Patient-reported Outcome Domain Core Set in the Life Impact Area for Adult Idiopathic Inflammatory Myopathies",
          "type": "article",
          "venue": "The Journal of Rheumatology",
          "cited_by_count": 46,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Inflammatory Myopathies and Dermatomyositis"
          ]
        },
        {
          "openalex_id": "W3205612535",
          "year": 2021,
          "title": "Inflammatory Arthritis and the Effect of Physical Activity on Quality of Life and <scp>Self‐Reported</scp> Function: A Systematic Review and <scp>Meta‐Analysis</scp>",
          "type": "review",
          "venue": "Arthritis Care & Research",
          "cited_by_count": 40,
          "topics": [
            "Spondyloarthritis Studies and Treatments",
            "Rheumatoid Arthritis Research and Therapies",
            "Autoimmune and Inflammatory Disorders Research"
          ]
        },
        {
          "openalex_id": "W2012144287",
          "year": 2015,
          "title": "Patients’ Experience of Myositis and Further Validation of a Myositis-specific Patient Reported Outcome Measure — Establishing Core Domains and Expanding Patient Input on Clinical Assessment in Myositis. Report from OMERACT 12",
          "type": "article",
          "venue": "The Journal of Rheumatology",
          "cited_by_count": 40,
          "topics": [
            "Inflammatory Myopathies and Dermatomyositis",
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments"
          ]
        },
        {
          "openalex_id": "W3175659160",
          "year": 2021,
          "title": "Exercise as a multi-modal disease-modifying medicine in systemic sclerosis: An introduction by The Global Fellowship on Rehabilitation and Exercise in Systemic Sclerosis (G-FoRSS)",
          "type": "article",
          "venue": "Best Practice & Research Clinical Rheumatology",
          "cited_by_count": 37,
          "topics": [
            "Systemic Sclerosis and Related Diseases",
            "Inflammatory Myopathies and Dermatomyositis",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis"
          ]
        }
      ]
    }
  },
  {
    "name": "Marcel Jonker",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "1413-RA",
        "title": "Fitting mixed logit models with a garbage class instead of manually screening for respondents with low data quality",
        "working_group": "Valuation"
      },
      {
        "project_id": "1484-RA",
        "title": "The impact of traffic-light color coding in discrete choice health-state valuations",
        "working_group": "Valuation"
      },
      {
        "project_id": "1489-RA",
        "title": "Estimating interactions between the health domains in stand-alone DCE valuation studies",
        "working_group": "Valuation"
      },
      {
        "project_id": "1611-RA",
        "title": "Pilot valuation of the EQ-HWB-S using the VWG DCE with duration protocol",
        "working_group": "Valuation, EQ-HWB"
      },
      {
        "project_id": "1612-RA",
        "title": "Impact of demographic change on expected value set redundancy",
        "working_group": "Valuation"
      },
      {
        "project_id": "163-RA",
        "title": "Mixed logit estimation of QALY tariffs corrected for non-linear time preferences",
        "working_group": "Valuation"
      },
      {
        "project_id": "1679-RA",
        "title": "Garbage in, garbage out? Evaluating the ability of the garbage class MIXL model to identify random response patterns",
        "working_group": "Valuation"
      },
      {
        "project_id": "1693-RA",
        "title": "RAndomized Matched PAirwise Choice Tasks (RAMPACT): making the stand-alone DCE with duration protocol robust to flatliners and validate the protocol’s results with cTTO.",
        "working_group": "Valuation"
      },
      {
        "project_id": "1695-RA",
        "title": "Improving DCE design efficiency with (automated) design updates",
        "working_group": "Valuation"
      },
      {
        "project_id": "1919-RA",
        "title": "Online Personal Utility Function (OPUF) estimation based on Adaptive Discrete Choice Analysis with sign and monotonicity constraints",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180320",
        "title": "User-friendly tool to optimize (D)efficient DCE duration designs for the EQ-5D-Y / EQ-5D-5L.",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190170",
        "title": "Which utility function do respondents (actually) use when completing DCE-duration choice tasks?",
        "working_group": "Valuation"
      },
      {
        "project_id": "20191070",
        "title": "A comparison of methods to evaluate DCE response quality",
        "working_group": "Valuation"
      },
      {
        "project_id": "20191180",
        "title": "Improved anchoring of stand-alone DCE duration value sets by incorporating immediate death and maximum endurable time; a mixed methods approach based on the EQ-5D-5L and E-QALY instruments",
        "working_group": "Valuation"
      },
      {
        "project_id": "2178-RA",
        "title": "Joint modelling of time and health preferences in DCE with duration valuation studies",
        "working_group": "Valuation"
      },
      {
        "project_id": "2204-RA",
        "title": "Improving DCE design efficiency with monotonicity constraints",
        "working_group": "Valuation"
      },
      {
        "project_id": "356-PHD",
        "title": "Methodological improvements in health-state valuations using discrete choice experiments.",
        "working_group": "Valuation, EQ-HWB"
      },
      {
        "project_id": "415-RA",
        "title": "Modelling interactions in the EQ-5D descriptive system",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5063358434",
      "display_name": "Marcel F. Jonker",
      "orcid": "0000-0001-8433-1402",
      "reported_affiliation": "Erasmus University Rotterdam",
      "works_count": 61,
      "top_topics": [
        {
          "topic": "Economic and Environmental Valuation",
          "works": 29
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 24
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 9
        },
        {
          "topic": "Global Health Care Issues",
          "works": 8
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 6
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 5
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Consumer Market Behavior and Pricing",
          "works": 4
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 4
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 3
        },
        {
          "topic": "Climate Change and Health Impacts",
          "works": 3
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bas Donkers",
          "works": 22
        },
        {
          "name": "Elly Stolk",
          "works": 16
        },
        {
          "name": "Esther W. de Bekker‐Grob",
          "works": 11
        },
        {
          "name": "Alex Burdorf",
          "works": 10
        },
        {
          "name": "Maureen Rutten‐van Mölken",
          "works": 9
        },
        {
          "name": "Johan P. Mackenbach",
          "works": 9
        },
        {
          "name": "Lucas Goossens",
          "works": 8
        },
        {
          "name": "Bram Roudijk",
          "works": 8
        },
        {
          "name": "Jorien Veldwijk",
          "works": 7
        },
        {
          "name": "Peter Congdon",
          "works": 6
        },
        {
          "name": "A.C.D. Donkers",
          "works": 6
        },
        {
          "name": "Frank J. van Lenthe",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7122436979",
          "year": 2026,
          "title": "Revisiting health state preferences after 20 years: A new EQ-5D-3L value set for the Netherlands",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Public Health Policies and Education"
          ]
        },
        {
          "openalex_id": "W7133568900",
          "year": 2026,
          "title": "Understanding decision-making strategies in discrete choice experiment tasks when valuing health states that include duration, a cognitive interview study with Australian adults",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4407630154",
          "year": 2025,
          "title": "A Taxonomy for Assessing Whether HRQoL Value Sets Are Obsolete",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4408672482",
          "year": 2025,
          "title": "Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4411316975",
          "year": 2025,
          "title": "Optimal DCE design for modelling nonlinear time preferences in EQ-5D-5L valuation studies: exploration of data from Denmark and Peru",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 2,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4399359799",
          "year": 2024,
          "title": "A Direct Comparison Between Discrete Choice With Duration and Composite Time Trade-Off Methods: Do They Produce Similar Results?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 17,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2037491179",
          "year": 1996,
          "title": "Middle Cerebral Artery Occlusion in Wistar and Fischer-344 Rats: Functional and Morphological Assessment of the Model",
          "type": "article",
          "venue": "Journal of Cerebral Blood Flow & Metabolism",
          "cited_by_count": 41,
          "topics": [
            "Barrier Structure and Function Studies",
            "Advanced Neuroimaging Techniques and Applications",
            "MRI in cancer diagnosis"
          ]
        },
        {
          "openalex_id": "W2142341971",
          "year": 2012,
          "title": "Comparison of Bayesian Random-Effects and Traditional Life Expectancy Estimations in Small-Area Applications",
          "type": "article",
          "venue": "American Journal of Epidemiology",
          "cited_by_count": 42,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2296618626",
          "year": 2012,
          "title": "Summary Measures and Determinants of Small-Area Population Health",
          "type": "dissertation",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "demographic modeling and climate adaptation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2025792173",
          "year": 2012,
          "title": "The impact of nursing homes on small-area life expectancies",
          "type": "article",
          "venue": "Health & Place",
          "cited_by_count": 12,
          "topics": [
            "demographic modeling and climate adaptation",
            "Migration, Aging, and Tourism Studies",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2032869670",
          "year": 2015,
          "title": "Sample Size Requirements for Discrete-Choice Experiments in Healthcare: a Practical Guide",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 939,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2953602043",
          "year": 2019,
          "title": "Are Healthcare Choices Predictable? The Impact of Discrete Choice Experiment Designs and Models",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 140,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W3048399669",
          "year": 2020,
          "title": "COVID-19 Contact Tracing Apps: Predicted Uptake in the Netherlands Based on a Discrete Choice Experiment",
          "type": "article",
          "venue": "JMIR mhealth and uhealth",
          "cited_by_count": 125,
          "topics": [
            "COVID-19 Digital Contact Tracing",
            "COVID-19 epidemiological studies",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W2905128009",
          "year": 2018,
          "title": "Attribute level overlap (and color coding) can reduce task complexity, improve choice consistency, and decrease the dropout rate in discrete choice experiments",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 110,
          "topics": [
            "Economic and Environmental Valuation",
            "Environmental Education and Sustainability",
            "Environmental Sustainability in Business"
          ]
        },
        {
          "openalex_id": "W2793054015",
          "year": 2018,
          "title": "The impact of vaccination and patient characteristics on influenza vaccination uptake of elderly people: A discrete choice experiment",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 85,
          "topics": [
            "Influenza Virus Research Studies",
            "Vaccine Coverage and Hesitancy",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W2769781016",
          "year": 2017,
          "title": "Effect of Level Overlap and Color Coding on Attribute Non-Attendance in Discrete Choice Experiments",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 75,
          "topics": [
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics",
            "Consumer Market Behavior and Pricing"
          ]
        },
        {
          "openalex_id": "W2273818270",
          "year": 2016,
          "title": "High resolution exposure modelling of heat and air pollution and the impact on mortality",
          "type": "article",
          "venue": "Environment International",
          "cited_by_count": 65,
          "topics": [
            "Climate Change and Health Impacts",
            "Air Quality and Health Impacts",
            "Thermoregulation and physiological responses"
          ]
        },
        {
          "openalex_id": "W2145000637",
          "year": 2014,
          "title": "The effect of urban green on small-area (healthy) life expectancy",
          "type": "article",
          "venue": "Journal of Epidemiology & Community Health",
          "cited_by_count": 65,
          "topics": [
            "Urban Green Space and Health",
            "Health disparities and outcomes",
            "Climate Change and Health Impacts"
          ]
        }
      ]
    }
  }
]
