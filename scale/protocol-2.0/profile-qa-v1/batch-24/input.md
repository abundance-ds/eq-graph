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
    "name": "Jennifer Jelsma",
    "member_affiliation": "University of Cape Town",
    "is_member": true,
    "projects": [
      {
        "project_id": "1713-RA",
        "title": "Alternative Wordings for the EQ-5D descriptive Systems: Optimising Measurement Excellence - Stage 1 (AWESOME 1)",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "2013110",
        "title": "The feasibility and usefulness of using the EQ-5D-Y as a routine measure of outcome in a facility for children with chronic illness",
        "working_group": "Youth"
      },
      {
        "project_id": "2014200",
        "title": "Development of a proxy English Health-Related Quality of Life (HRQoL) instrument for children under six years of age, derived from the EQ-5D-Y: Part 1",
        "working_group": "Youth"
      },
      {
        "project_id": "2016120",
        "title": "A comparison of the validity of the two proxy versions of the EQ-5D-Y instrument in acutely ill and chronically ill children in South Africa. A cross sectional analytical descriptive study",
        "working_group": "Youth"
      },
      {
        "project_id": "2016180",
        "title": "Exploring the possibilities for developing a EuroQol instrument for use in very young children: a workshop on feasibility, relevant issues, and potential methodology",
        "working_group": "Youth"
      },
      {
        "project_id": "20170250",
        "title": "Cross-sectional validity and feasibility of the self-report EQ-5D-Y as a generic Health Related Quality of Life outcome measure in children and adolescents with Juvenile Rheumatoid Arthritis (JRA) in Western Cape, South Africa",
        "working_group": "Youth"
      },
      {
        "project_id": "20170540",
        "title": "Validity and Reliability testing of the EQ-5D-Y Proxy version 1 in young children.",
        "working_group": "Youth"
      },
      {
        "project_id": "20170650",
        "title": "Comparison of the performance of an integrated Interviewer Administered EQ-5D-5L version with the Face to Face and Telephone Interviewer administered versions",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190030",
        "title": "Use of the VAS in the EQ-5D-Y",
        "working_group": "Descriptive Systems, Youth"
      },
      {
        "project_id": "20190500",
        "title": "Funding a two-day Academy Workshop in Cape Town in January or February 2020.",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20191210",
        "title": "Testing of the ranking exercise -EUQ2137080 (TRF2191) - English (US) | Face Validity Results",
        "working_group": "Others"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5064611767",
      "display_name": "Jennifer Jelsma",
      "orcid": "0000-0003-4049-8395",
      "reported_affiliation": "University of Cape Town",
      "works_count": 162,
      "top_topics": [
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 45
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 28
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 22
        },
        {
          "topic": "Disability Rights and Representation",
          "works": 16
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 16
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 14
        },
        {
          "topic": "Assistive Technology in Communication and Mobility",
          "works": 14
        },
        {
          "topic": "HIV-related health complications and treatments",
          "works": 11
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 9
        },
        {
          "topic": "Occupational Therapy Practice and Research",
          "works": 9
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 8
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Soraya Maart",
          "works": 16
        },
        {
          "name": "Lieselotte Corten",
          "works": 15
        },
        {
          "name": "Matthew Chiwaridzo",
          "works": 13
        },
        {
          "name": "Romy Parker",
          "works": 13
        },
        {
          "name": "Tecla Mlambo",
          "works": 12
        },
        {
          "name": "Willy De Weerdt",
          "works": 12
        },
        {
          "name": "Paul De Cock",
          "works": 10
        },
        {
          "name": "Gillian Ferguson",
          "works": 10
        },
        {
          "name": "Jermaine M. Dambi",
          "works": 8
        },
        {
          "name": "Janine Verstraete",
          "works": 8
        },
        {
          "name": "Dan J. Stein",
          "works": 7
        },
        {
          "name": "Cathrine Tadyanemhandu",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4416337963",
          "year": 2025,
          "title": "Multinational stakeholder engagement to inform future development and refinement of the EuroQol toddler and infant populations (EQ-TIPS)",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 2,
          "topics": [
            "Infant Development and Preterm Care",
            "Delphi Technique in Research",
            "Early Childhood Education and Development"
          ]
        },
        {
          "openalex_id": "W4401993913",
          "year": 2024,
          "title": "He/She/They - gender inclusivity in developing and using health-related questionnaires: a scoping review",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 7,
          "topics": [
            "Sex and Gender in Healthcare",
            "Rheumatoid Arthritis Research and Therapies",
            "LGBTQ Health, Identity, and Policy"
          ]
        },
        {
          "openalex_id": "W4389625076",
          "year": 2023,
          "title": "Let’s talk about it: an exploration of the comparative use of three different digital platforms to gather patient-reported outcome measures",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 8,
          "topics": [
            "Cancer survivorship and care",
            "Digital Mental Health Interventions",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4387302159",
          "year": 2023,
          "title": "P100 Perceived barriers and facilitators of behavioral change towards a more active lifestyle in people living with neuromuscular disorders",
          "type": "conference-abstract",
          "venue": "Neuromuscular Disorders",
          "cited_by_count": 0,
          "topics": [
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W4390124881",
          "year": 2023,
          "title": "PCR245 Stakeholder Engagement and Expert Consultation on the EuroQol Toddler and Infant Populations (EQ-TIPS) Measure of Health-Related Quality of Life (HRQoL)",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Delphi Technique in Research",
            "Child and Adolescent Health"
          ]
        },
        {
          "openalex_id": "W3134118815",
          "year": 2021,
          "title": "A New Approach to Assessing Children’s Interpretation of Severity Qualifiers in a Multi-Attribute Utility Instrument–The EQ-5D-Y-5L: Development and Testing",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Cerebral Palsy and Movement Disorders"
          ]
        },
        {
          "openalex_id": "W2741696761",
          "year": 1995,
          "title": "Learning about learning in the development of biotechnology",
          "type": "book-chapter",
          "venue": "University of Twente Research Information",
          "cited_by_count": 9,
          "topics": [
            "Biomedical and Engineering Education",
            "Problem and Project Based Learning",
            "Biotechnology and Related Fields"
          ]
        },
        {
          "openalex_id": "W2737772320",
          "year": 1995,
          "title": "Military implications of biotechnology",
          "type": "book-chapter",
          "venue": "University of Twente Research Information",
          "cited_by_count": 1,
          "topics": [
            "Biotechnology and Related Fields",
            "Science, Research, and Medicine"
          ]
        },
        {
          "openalex_id": "W2075601412",
          "year": 1995,
          "title": "The Childrenʼs Rehabilitation Unit, Harare, Zimbabwe",
          "type": "article",
          "venue": "Pediatric Physical Therapy",
          "cited_by_count": 6,
          "topics": [
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W2157022207",
          "year": 1996,
          "title": "Appreciation of community-based rehabilitation by caregivers of children with a disability",
          "type": "article",
          "venue": "Disability and Rehabilitation",
          "cited_by_count": 20,
          "topics": [
            "Family and Disability Support Research",
            "Cerebral Palsy and Movement Disorders",
            "Inclusion and Disability in Education and Sport"
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
          "openalex_id": "W2805576752",
          "year": 2018,
          "title": "A systematic review of the psychometric properties of the cross-cultural translations and adaptations of the Multidimensional Perceived Social Support Scale (MSPSS)",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 274,
          "topics": [
            "Health disparities and outcomes",
            "Cardiac Health and Mental Health",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W1978050054",
          "year": 2014,
          "title": "Pain in people living with HIV/AIDS: a systematic review",
          "type": "review",
          "venue": "Journal of the International AIDS Society",
          "cited_by_count": 240,
          "topics": [
            "HIV Research and Treatment",
            "HIV-related health complications and treatments",
            "HIV/AIDS Research and Interventions"
          ]
        },
        {
          "openalex_id": "W2052262122",
          "year": 2005,
          "title": "An investigation into the health-related quality of life of individuals living with HIV who are receiving HAART",
          "type": "article",
          "venue": "AIDS Care",
          "cited_by_count": 178,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "HIV/AIDS drug development and treatment"
          ]
        },
        {
          "openalex_id": "W1730711634",
          "year": 2011,
          "title": "Monitoring vital signs using early warning scoring systems: a review of the literature",
          "type": "article",
          "venue": "Journal of Nursing Management",
          "cited_by_count": 176,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Healthcare Technology and Patient Monitoring",
            "Patient Safety and Medication Errors"
          ]
        },
        {
          "openalex_id": "W2135174968",
          "year": 2003,
          "title": "How do Zimbabweans value health states?",
          "type": "article",
          "venue": "Population Health Metrics",
          "cited_by_count": 175,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2055424215",
          "year": 2009,
          "title": "Use of the International Classification of Functioning, Disability and health: A literature survey",
          "type": "article",
          "venue": "Journal of Rehabilitation Medicine",
          "cited_by_count": 164,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Disability Rights and Representation",
            "Down syndrome and intellectual disability research"
          ]
        }
      ]
    }
  },
  {
    "name": "Jenny Downs",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "429-RA",
        "title": "Assessing the suitability of the EQ-5D-Y for children and adolescents with intellectual disability",
        "working_group": "Descriptive Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5045593878",
      "display_name": "Jenny Downs",
      "orcid": "0000-0001-7358-9037",
      "reported_affiliation": "The Kids Research Institute Australia",
      "works_count": 333,
      "top_topics": [
        {
          "topic": "Genetics and Neurodevelopmental Disorders",
          "works": 176
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 102
        },
        {
          "topic": "Autism Spectrum Disorder Research",
          "works": 66
        },
        {
          "topic": "Child Nutrition and Feeding Issues",
          "works": 42
        },
        {
          "topic": "Neurogenetic and Muscular Disorders Research",
          "works": 42
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 41
        },
        {
          "topic": "Down syndrome and intellectual disability research",
          "works": 33
        },
        {
          "topic": "Epilepsy research and treatment",
          "works": 26
        },
        {
          "topic": "Genomic variations and chromosomal abnormalities",
          "works": 24
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 23
        },
        {
          "topic": "Genomics and Rare Diseases",
          "works": 16
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Helen Leonard",
          "works": 204
        },
        {
          "name": "Peter Jacoby",
          "works": 79
        },
        {
          "name": "Kingsley Wong",
          "works": 75
        },
        {
          "name": "Andrew Wilson",
          "works": 37
        },
        {
          "name": "Tim A. Benke",
          "works": 33
        },
        {
          "name": "Scott Demarest",
          "works": 31
        },
        {
          "name": "Amy Epstein",
          "works": 23
        },
        {
          "name": "Jacinta Saldaris",
          "works": 23
        },
        {
          "name": "Andrew Whitehouse",
          "works": 22
        },
        {
          "name": "Eric D. Marsh",
          "works": 21
        },
        {
          "name": "Amy Finlay‐Jones",
          "works": 17
        },
        {
          "name": "Emma J. Glasson",
          "works": 16
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7126062747",
          "year": 2026,
          "title": "Addressing the challenges of intellectual disability identification for health policy and research in Australia",
          "type": "article",
          "venue": "Frontiers in Psychiatry",
          "cited_by_count": 0,
          "topics": [
            "Down syndrome and intellectual disability research",
            "Genomics and Rare Diseases",
            "Medical Coding and Health Information"
          ]
        },
        {
          "openalex_id": "W7169502656",
          "year": 2026,
          "title": "Applying adaptive research methods to explore health literacy in young people with intellectual disability",
          "type": "article",
          "venue": "Health Promotion International",
          "cited_by_count": 0,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Down syndrome and intellectual disability research",
            "Disability Rights and Representation"
          ]
        },
        {
          "openalex_id": "W7169657455",
          "year": 2026,
          "title": "Effectiveness and Cost‐Effectiveness of Models of Healthcare for People With Intellectual Disability in Australia: A Scoping Review",
          "type": "article",
          "venue": "Journal of Intellectual Disability Research",
          "cited_by_count": 0,
          "topics": [
            "Down syndrome and intellectual disability research",
            "Disability Rights and Representation",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W7167354565",
          "year": 2026,
          "title": "Understanding parents’ experiences and needs when managing menstruation with young people with intellectual disability",
          "type": "article",
          "venue": "Women s Health",
          "cited_by_count": 0,
          "topics": [
            "Disability Rights and Representation",
            "Inclusion and Disability in Education and Sport",
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W7167073815",
          "year": 2026,
          "title": "Validity Data for the Developmental Profile-4 in Individuals With Profound Intellectual and Multiple Disabilities and Developmental Epileptic Encephalopathies",
          "type": "article",
          "venue": "American Journal on Intellectual and Developmental Disabilities",
          "cited_by_count": 0,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Down syndrome and intellectual disability research",
            "Attention Deficit Hyperactivity Disorder"
          ]
        },
        {
          "openalex_id": "W4416292640",
          "year": 2025,
          "title": "Beyond Seizures as an Outcome Measure: A Global Severity Scoring System for CDKL5 Deficiency Disorder",
          "type": "article",
          "venue": "Brain and Behavior",
          "cited_by_count": 0,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Genetic Neurodegenerative Diseases",
            "Genetic Associations and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2029112287",
          "year": 1989,
          "title": "Addison's disease in the dog",
          "type": "article",
          "venue": "Veterinary Record",
          "cited_by_count": 8,
          "topics": [
            "Adrenal Hormones and Disorders",
            "Veterinary Medicine and Surgery"
          ]
        },
        {
          "openalex_id": "W1641986250",
          "year": 1990,
          "title": "Multiple personality disorder in India",
          "type": "article",
          "venue": "American Journal of Psychiatry",
          "cited_by_count": 1,
          "topics": [
            "Autism Spectrum Disorder Research",
            "Personality Disorders and Psychopathology"
          ]
        },
        {
          "openalex_id": "W2017148431",
          "year": 1991,
          "title": "Effect of intervention on development of hip posture in very preterm babies.",
          "type": "article",
          "venue": "Archives of Disease in Childhood",
          "cited_by_count": 36,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Neuroscience of respiration and sleep"
          ]
        },
        {
          "openalex_id": "W2089074436",
          "year": 1995,
          "title": "Effect of neck rotation on the timing and pattern of infant tidal breathing",
          "type": "article",
          "venue": "Pediatric Pulmonology",
          "cited_by_count": 10,
          "topics": [
            "Neonatal Respiratory Health Research",
            "Neuroscience of respiration and sleep",
            "Obstructive Sleep Apnea Research"
          ]
        },
        {
          "openalex_id": "W2076825430",
          "year": 2012,
          "title": "The CDKL5 disorder is an independent clinical entity associated with early-onset encephalopathy",
          "type": "article",
          "venue": "European Journal of Human Genetics",
          "cited_by_count": 314,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Genomic variations and chromosomal abnormalities",
            "Chromatin Remodeling and Cancer"
          ]
        },
        {
          "openalex_id": "W3029495836",
          "year": 2020,
          "title": "Prevalence estimates of mental health problems in children and adolescents with intellectual disability: A systematic review and meta-analysis",
          "type": "review",
          "venue": "Australian & New Zealand Journal of Psychiatry",
          "cited_by_count": 288,
          "topics": [
            "Down syndrome and intellectual disability research",
            "Genetics and Neurodevelopmental Disorders",
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W2559812869",
          "year": 2016,
          "title": "Clinical and biological progress over 50 years in Rett syndrome",
          "type": "article",
          "venue": "Nature Reviews Neurology",
          "cited_by_count": 207,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Autism Spectrum Disorder Research",
            "Epigenetics and DNA Methylation"
          ]
        },
        {
          "openalex_id": "W4224440073",
          "year": 2022,
          "title": "CDKL5 deficiency disorder: clinical features, diagnosis, and management",
          "type": "article",
          "venue": "The Lancet Neurology",
          "cited_by_count": 149,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Genomic variations and chromosomal abnormalities",
            "Epilepsy research and treatment"
          ]
        },
        {
          "openalex_id": "W2064897206",
          "year": 2011,
          "title": "Trends in the Diagnosis of Rett Syndrome in Australia",
          "type": "article",
          "venue": "Pediatric Research",
          "cited_by_count": 147,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Family and Disability Support Research",
            "Autism Spectrum Disorder Research"
          ]
        },
        {
          "openalex_id": "W2756091964",
          "year": 2017,
          "title": "The prevalence of mental health disorders and symptoms in children and adolescents with cerebral palsy: a systematic review and meta‐analysis",
          "type": "review",
          "venue": "Developmental Medicine & Child Neurology",
          "cited_by_count": 145,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Family and Disability Support Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W2134540539",
          "year": 2014,
          "title": "Twenty years of surveillance in Rett syndrome: what does this tell us?",
          "type": "article",
          "venue": "Orphanet Journal of Rare Diseases",
          "cited_by_count": 145,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Epilepsy research and treatment",
            "Folate and B Vitamins Research"
          ]
        },
        {
          "openalex_id": "W2338814967",
          "year": 2016,
          "title": "Prevalence and onset of comorbidities in the CDKL5 disorder differ from Rett syndrome",
          "type": "article",
          "venue": "Orphanet Journal of Rare Diseases",
          "cited_by_count": 133,
          "topics": [
            "Genetics and Neurodevelopmental Disorders",
            "Epilepsy research and treatment",
            "Genomic variations and chromosomal abnormalities"
          ]
        }
      ]
    }
  },
  {
    "name": "Jeremy Dietz",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1879-EO",
        "title": "Potential applications of the EQ Health and Wellbeing Short in health technology assessment (HTA)",
        "working_group": "Education and Outreach, EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5078556304",
      "display_name": "Jeremy Dietz",
      "orcid": "",
      "reported_affiliation": "National Institute for Health and Care Excellence",
      "works_count": 6,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 2
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 1
        },
        {
          "topic": "Health Literacy and Information Accessibility",
          "works": 1
        },
        {
          "topic": "Neonatal and Maternal Infections",
          "works": 1
        },
        {
          "topic": "Preterm Birth and Chorioamnionitis",
          "works": 1
        },
        {
          "topic": "Reproductive tract infections research",
          "works": 1
        },
        {
          "topic": "Statistical Methods and Bayesian Inference",
          "works": 1
        },
        {
          "topic": "Innovation Policy and R&D",
          "works": 1
        },
        {
          "topic": "Healthcare innovation and challenges",
          "works": 1
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Lindsay Claxton",
          "works": 3
        },
        {
          "name": "Nicky J. Welton",
          "works": 3
        },
        {
          "name": "G Rogers",
          "works": 2
        },
        {
          "name": "Beatrice C. Downing",
          "works": 2
        },
        {
          "name": "Hannah Tebbs",
          "works": 2
        },
        {
          "name": "Wesley Hubbard",
          "works": 1
        },
        {
          "name": "Nicola Walsh",
          "works": 1
        },
        {
          "name": "Tom Hudson",
          "works": 1
        },
        {
          "name": "Andrea Heath",
          "works": 1
        },
        {
          "name": "Jane A. Plumb",
          "works": 1
        },
        {
          "name": "Philip Banfield",
          "works": 1
        },
        {
          "name": "Aung Soe",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4414168435",
          "year": 2025,
          "title": "Adult Social Care Outcomes Toolkit and ICEpop Capability Measure in Decision Making: A Review of NICE Social Care and Public Health Guidelines",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare innovation and challenges",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4311211702",
          "year": 2022,
          "title": "Development and validation of paired MEDLINE and Embase search filters for cost-utility studies",
          "type": "article",
          "venue": "BMC Medical Research Methodology",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W4211234241",
          "year": 2022,
          "title": "Immediate birth for women between 34 and 37 weeks of gestation with prolonged preterm prelabour rupture of membranes and detection of vaginal or urine group B streptococcus: an economic evaluation",
          "type": "article",
          "venue": "BJOG An International Journal of Obstetrics & Gynaecology",
          "cited_by_count": 6,
          "topics": [
            "Neonatal and Maternal Infections",
            "Preterm Birth and Chorioamnionitis",
            "Reproductive tract infections research"
          ]
        },
        {
          "openalex_id": "W4311341652",
          "year": 2022,
          "title": "MSR61 Lessons Learned From Network Meta-Analysis of Survival Data With Fractional Polynomials",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Meta-analysis and systematic reviews",
            "Statistical Methods and Bayesian Inference"
          ]
        },
        {
          "openalex_id": "W4311352031",
          "year": 2022,
          "title": "MSR79 Synthesis of Survival Outcomes in Economic Evaluation: Does the Network Meta-Analysis Model Matter?",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Innovation Policy and R&D"
          ]
        },
        {
          "openalex_id": "W4311337289",
          "year": 2022,
          "title": "P41 The Added Value of Joint Modelling of Progression Free and Overall Survival in a Restricted Mean Survival Network Meta-Analysis",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Meta-analysis and systematic reviews"
          ]
        }
      ]
    }
  },
  {
    "name": "Jermaine Dambi",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "212-RA",
        "title": "An evaluation of the feasibility and acceptability of the use of the digital version of the EQ-5D 3L in routine care in a busy HIV care clinic in Harare, Zimbabwe.",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5081348197",
      "display_name": "Jermaine M. Dambi",
      "orcid": "0000-0002-2446-7903",
      "reported_affiliation": "University of Zimbabwe",
      "works_count": 81,
      "top_topics": [
        {
          "topic": "Mental Health Treatment and Access",
          "works": 12
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 11
        },
        {
          "topic": "Cerebral Palsy and Movement Disorders",
          "works": 9
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 9
        },
        {
          "topic": "Adolescent Sexual and Reproductive Health",
          "works": 9
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 8
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 7
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 6
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 6
        },
        {
          "topic": "Physical Activity and Health",
          "works": 6
        },
        {
          "topic": "Sports Performance and Training",
          "works": 5
        },
        {
          "topic": "Occupational Health and Performance",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Dixon Chibanda",
          "works": 28
        },
        {
          "name": "Matthew Chiwaridzo",
          "works": 24
        },
        {
          "name": "Webster Mavhu",
          "works": 19
        },
        {
          "name": "Cathrine Tadyanemhandu",
          "works": 16
        },
        {
          "name": "Frances M. Cowan",
          "works": 15
        },
        {
          "name": "Beatrice K Shava",
          "works": 14
        },
        {
          "name": "Sidney Muchemwa",
          "works": 11
        },
        {
          "name": "Fardawsa Ahmed",
          "works": 10
        },
        {
          "name": "Owen Nyamwanza",
          "works": 10
        },
        {
          "name": "Ruth Verhey",
          "works": 9
        },
        {
          "name": "Alice Norah Ladur",
          "works": 9
        },
        {
          "name": "Jennifer Jelsma",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166508976",
          "year": 2026,
          "title": "A randomised equivalence study of the EQ-5D-5L Shona versions: evaluation of measurement equivalence between digital and paper formats",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Literacy and Information Accessibility"
          ]
        },
        {
          "openalex_id": "W7118164830",
          "year": 2026,
          "title": "Additional file 1 of How do social norms influence the sexual and reproductive health-related attitudes and behaviours of very young adolescents in Sub-Saharan Africa? A scoping review",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W7118182758",
          "year": 2026,
          "title": "Additional file 1 of How do social norms influence the sexual and reproductive health-related attitudes and behaviours of very young adolescents in Sub-Saharan Africa? A scoping review",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W7118167533",
          "year": 2026,
          "title": "Additional file 2 of How do social norms influence the sexual and reproductive health-related attitudes and behaviours of very young adolescents in Sub-Saharan Africa? A scoping review",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W7118172354",
          "year": 2026,
          "title": "Additional file 2 of How do social norms influence the sexual and reproductive health-related attitudes and behaviours of very young adolescents in Sub-Saharan Africa? A scoping review",
          "type": "article",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W4413127587",
          "year": 2026,
          "title": "Awareness, utility and preferences of campus-based mental health services at tertiary institutions in Harare, Zimbabwe: A cross-sectional study",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 1,
          "topics": [
            "Mental Health Treatment and Access",
            "Migration, Health and Trauma"
          ]
        },
        {
          "openalex_id": "W2060953234",
          "year": 2014,
          "title": "The impact of hospital-based and community based models of cerebral palsy rehabilitation: a quasi-experimental study",
          "type": "article",
          "venue": "BMC Pediatrics",
          "cited_by_count": 62,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Family and Disability Support Research",
            "Infant Development and Preterm Care"
          ]
        },
        {
          "openalex_id": "W1723075971",
          "year": 2015,
          "title": "Caring for a child with Cerebral Palsy: The experience of Zimbabwean mothers",
          "type": "article",
          "venue": "African Journal of Disability",
          "cited_by_count": 87,
          "topics": [
            "Family and Disability Support Research",
            "Cerebral Palsy and Movement Disorders",
            "Assistive Technology in Communication and Mobility"
          ]
        },
        {
          "openalex_id": "W2225866310",
          "year": 2015,
          "title": "Recurrent Non-Specific Low Back Pain: A Cross-Sectional Survey on Prevalence, Nature of Recurrent Episodes and The Role of Physical Activity and Psychological Status in High School Adolescents in Harare, Zimbabw",
          "type": "article",
          "venue": "Annals of Paediatric Rheumatology",
          "cited_by_count": 2,
          "topics": [
            "Occupational Health and Performance",
            "School Health and Nursing Education",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2612297819",
          "year": 2015,
          "title": "THE IMPACT OF CAREGIVING A CHILD WITH HIV/AIDS: EXPERIENCES OF ZIMBABWEAN MOTHERS",
          "type": "other",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Impact and Responses",
            "Poverty, Education, and Child Welfare",
            "Family Support in Illness"
          ]
        },
        {
          "openalex_id": "W2805576752",
          "year": 2018,
          "title": "A systematic review of the psychometric properties of the cross-cultural translations and adaptations of the Multidimensional Perceived Social Support Scale (MSPSS)",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 274,
          "topics": [
            "Health disparities and outcomes",
            "Cardiac Health and Mental Health",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W4293263159",
          "year": 2018,
          "title": "Human immunodefciency virus associated pulmonary conditions leading to hospital admission and the pulmonary rehabilitation services received by patients at two central hospitals in Harare",
          "type": "article",
          "venue": "Zenodo (CERN European Organization for Nuclear Research)",
          "cited_by_count": 178,
          "topics": [
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "Hepatitis C virus research",
            "HIV/AIDS Impact and Responses"
          ]
        },
        {
          "openalex_id": "W2806947332",
          "year": 2018,
          "title": "Work-related musculoskeletal disorders among registered general nurses: a case of a large central hospital in Harare, Zimbabwe",
          "type": "article",
          "venue": "BMC Research Notes",
          "cited_by_count": 70,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational health in dentistry",
            "Occupational Health and Safety Research"
          ]
        },
        {
          "openalex_id": "W4220919072",
          "year": 2022,
          "title": "Barriers to the provision of non-communicable disease care in Zimbabwe: a qualitative study of primary health care nurses",
          "type": "article",
          "venue": "BMC Nursing",
          "cited_by_count": 57,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Global Maternal and Child Health",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2780875531",
          "year": 2017,
          "title": "A systematic review investigating measurement properties of physiological tests in rugby",
          "type": "review",
          "venue": "BMC Sports Science Medicine and Rehabilitation",
          "cited_by_count": 50,
          "topics": [
            "Sports Performance and Training",
            "Sports injuries and prevention",
            "Sport Psychology and Performance"
          ]
        },
        {
          "openalex_id": "W4290190684",
          "year": 2022,
          "title": "A Digital Mental Health Intervention (Inuka) for Common Mental Health Disorders in Zimbabwean Adults in Response to the COVID-19 Pandemic: Feasibility and Acceptability Pilot Study",
          "type": "article",
          "venue": "JMIR Mental Health",
          "cited_by_count": 39,
          "topics": [
            "Digital Mental Health Interventions",
            "Mobile Health and mHealth Applications",
            "Mental Health Treatment and Access"
          ]
        }
      ]
    }
  },
  {
    "name": "Jeshika Singh",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2015390",
        "title": "Can social care needs and well-being be explained by EQ-5D? Analysis of the Health Survey for England dataset.",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5036902866",
      "display_name": "Jeshika Singh",
      "orcid": "0000-0003-3321-5481",
      "reported_affiliation": "Daiichi Sankyo (United States)",
      "works_count": 28,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 8
        },
        {
          "topic": "Liver Disease and Transplantation",
          "works": 5
        },
        {
          "topic": "Hemodynamic Monitoring and Therapy",
          "works": 4
        },
        {
          "topic": "Organ Transplantation Techniques and Outcomes",
          "works": 4
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Cardiac and Coronary Surgery Techniques",
          "works": 2
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 2
        },
        {
          "topic": "Cardiac Valve Diseases and Treatments",
          "works": 2
        },
        {
          "topic": "Trauma, Hemostasis, Coagulopathy, Resuscitation",
          "works": 2
        },
        {
          "topic": "Racial and Ethnic Identity Research",
          "works": 2
        },
        {
          "topic": "Child and Adolescent Psychosocial and Emotional Development",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Louise Longworth",
          "works": 18
        },
        {
          "name": "Farid Froghi",
          "works": 5
        },
        {
          "name": "Kurinchi Selvan Gurusamy",
          "works": 5
        },
        {
          "name": "Daniel Martín",
          "works": 5
        },
        {
          "name": "Christine Eastgate",
          "works": 5
        },
        {
          "name": "Margaret McNeil",
          "works": 5
        },
        {
          "name": "Helder Filipe",
          "works": 5
        },
        {
          "name": "Brian R Davidson",
          "works": 5
        },
        {
          "name": "Subhash Pokhrel",
          "works": 4
        },
        {
          "name": "Rahul Koti",
          "works": 4
        },
        {
          "name": "Nick Schofield",
          "works": 4
        },
        {
          "name": "Douglas Thorburn",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4402566487",
          "year": 2024,
          "title": "1787P Intracranial response in patients (pts) with baseline (BL) brain metastases (BM) and extensive-stage (ES) small cell lung cancer (SCLC) treated with ifinatamab deruxtecan (I-DXd) in the IDeate-Lung01 study",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 5,
          "topics": [
            "Lung Cancer Research Studies",
            "Brain Metastases and Treatment",
            "Radiopharmaceutical Chemistry and Applications"
          ]
        },
        {
          "openalex_id": "W4225687260",
          "year": 2022,
          "title": "An Analysis of 5-Level Version of EQ-5D Adjusting for Treatment Switching: The Case of Patients With Epidermal Growth Factor Receptor T790M-Positive Nonsmall Cell Lung Cancer Treated With Osimertinib",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Lung Cancer Treatments and Mutations",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W4212815978",
          "year": 2022,
          "title": "Effect of post-operative goal-directed fluid therapy (GDFT) on organ function after orthotopic liver transplantation: Secondary outcome analysis of the COLT randomised control trial",
          "type": "article",
          "venue": "International Journal of Surgery",
          "cited_by_count": 5,
          "topics": [
            "Hemodynamic Monitoring and Therapy",
            "Liver Disease and Transplantation",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation"
          ]
        },
        {
          "openalex_id": "W2997859229",
          "year": 2019,
          "title": "The cardiac output optimisation following liver transplant (COLT) trial: a feasibility randomised controlled trial",
          "type": "article",
          "venue": "HPB",
          "cited_by_count": 12,
          "topics": [
            "Hemodynamic Monitoring and Therapy",
            "Liver Disease and Transplantation",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W2980085392",
          "year": 2019,
          "title": "Ward-based Goal-Directed Fluid Therapy (GDFT) in Acute Pancreatitis (GAP) trial: study protocol for a feasibility randomised controlled trial",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 15,
          "topics": [
            "Pancreatitis Pathology and Treatment",
            "Hemodynamic Monitoring and Therapy",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation"
          ]
        },
        {
          "openalex_id": "W2801978149",
          "year": 2018,
          "title": "Amaze: a double-blind, multicentre randomised controlled trial to investigate the clinical effectiveness and cost-effectiveness of adding an ablation device-based maze procedure as an adjunct to routine cardiac surgery for patients with pre-existing atrial fibrillation",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 22,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac and Coronary Surgery Techniques",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W1980744545",
          "year": 2012,
          "title": "Does Responsibility Affect the Public's Valuation of Health Care Interventions? A Relative Valuation Approach to Health Care Safety",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 15,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2212869791",
          "year": 2012,
          "title": "Understanding Public Preferences for Avoiding QALY Losses Caused by Lapses in Healthcare Safety and Patient Lifestyle Choices.",
          "type": "article",
          "venue": "Journal of Health Services Research & Policy",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2147437893",
          "year": 2013,
          "title": "Exploring what lies behind public preferences for avoiding health losses caused by lapses in healthcare safety and patient lifestyle choices",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2316533813",
          "year": 2014,
          "title": "An Evaluation of the Performance of Eq-5d: A Review of Reviews of Psychometric Properties",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Clinical practice guidelines implementation",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2530421404",
          "year": 2016,
          "title": "Proceedings of Patient Reported Outcome Measure’s (PROMs) Conference Sheffield 2016: advances in patient reported outcomes research",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 152,
          "topics": [
            "Primary Care and Health Outcomes",
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2120071057",
          "year": 2014,
          "title": "Does Convenience Matter in Health Care Delivery? A Systematic Review of Convenience-Based Aspects of Process Utility",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 61,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2806487688",
          "year": 2018,
          "title": "Mini-Stern Trial: A randomized trial comparing mini-sternotomy to full median sternotomy for aortic valve replacement",
          "type": "article",
          "venue": "Journal of Thoracic and Cardiovascular Surgery",
          "cited_by_count": 60,
          "topics": [
            "Cardiac and Coronary Surgery Techniques",
            "Aortic Disease and Treatment Approaches",
            "Surgical site infection prevention"
          ]
        },
        {
          "openalex_id": "W2800895946",
          "year": 2018,
          "title": "Amaze: a randomized controlled trial of adjunct surgery for atrial fibrillation†",
          "type": "article",
          "venue": "European Journal of Cardio-Thoracic Surgery",
          "cited_by_count": 20,
          "topics": [
            "Atrial Fibrillation Management and Outcomes",
            "Cardiac Arrhythmias and Treatments",
            "Cardiac Valve Diseases and Treatments"
          ]
        }
      ]
    }
  }
]
