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
    "name": "Joshua Bonsel",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "145-RA",
        "title": "Patient Reported Outcomes in Quality of Care. A systematic review with specific attention to barriers and opportunities for EQ-5D in orthopedic surgery",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1483-TVG",
        "title": "Scientific international exchange project in the context of the EQ-sponsored PhD project (PHD-287) on inequality research with orthopedic registry data.",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "287-PHD",
        "title": "Measuring Health-Related Quality of Life in Orthopedic Clinical Practice",
        "working_group": "Populations and Health Systems, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5090783923",
      "display_name": "Joshua M. Bonsel",
      "orcid": "0000-0002-9143-5506",
      "reported_affiliation": "Erasmus MC",
      "works_count": 14,
      "top_topics": [
        {
          "topic": "Hip disorders and treatments",
          "works": 5
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 4
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 4
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 3
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Foot and Ankle Surgery",
          "works": 3
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 2
        },
        {
          "topic": "Bone and Joint Diseases",
          "works": 2
        },
        {
          "topic": "Scoliosis diagnosis and treatment",
          "works": 2
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 1
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 1
        },
        {
          "topic": "Hip and Femur Fractures",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Gouke J. Bonsel",
          "works": 7
        },
        {
          "name": "Max Reijman",
          "works": 4
        },
        {
          "name": "Jan A.N. Verhaar",
          "works": 4
        },
        {
          "name": "Liza N. van Steenbergen",
          "works": 3
        },
        {
          "name": "Ralph J. B. Sakkers",
          "works": 3
        },
        {
          "name": "Ademola Joshua Itiola",
          "works": 2
        },
        {
          "name": "Anouk S. Huberts",
          "works": 2
        },
        {
          "name": "Hannah Penton",
          "works": 2
        },
        {
          "name": "Virginie Pollet",
          "works": 2
        },
        {
          "name": "Harrie Weinans",
          "works": 2
        },
        {
          "name": "Denise Eygendaal",
          "works": 2
        },
        {
          "name": "Charles M. M. Peeters",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7125695266",
          "year": 2026,
          "title": "Causal decomposition of health outcome disparities: Assessing the contribution of healthcare",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Advanced Causal Inference Techniques",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W7163923881",
          "year": 2026,
          "title": "Socioeconomic inequalities in health-related quality of life during the COVID-19 pandemic: a six-country comparison using the EQ-5D-5 L",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health disparities and outcomes",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W4406958353",
          "year": 2025,
          "title": "A head-to-head comparison of the adult EQ-5D-5L and youth EQ-5D-Y-5L in adolescents with idiopathic scoliosis",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 1,
          "topics": [
            "Scoliosis diagnosis and treatment",
            "Hip disorders and treatments",
            "Foot and Ankle Surgery"
          ]
        },
        {
          "openalex_id": "W4410630560",
          "year": 2025,
          "title": "Socioeconomic inequalities in patient-reported outcome measures among total hip and knee arthroplasty patients: a comprehensive analysis of instruments and domains",
          "type": "article",
          "venue": "International Journal for Equity in Health",
          "cited_by_count": 6,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4410903040",
          "year": 2025,
          "title": "Ultrasound-based statistical shape modeling for prognosis in unstable hip dysplasia",
          "type": "article",
          "venue": "The Ultrasound Journal",
          "cited_by_count": 1,
          "topics": [
            "Hip disorders and treatments",
            "Orthopaedic implants and arthroplasty",
            "Bone and Joint Diseases"
          ]
        },
        {
          "openalex_id": "W4393900050",
          "year": 2024,
          "title": "Low socioeconomic status is associated with worse treatment outcomes in patients with Achilles tendinopathy",
          "type": "article",
          "venue": "British Journal of Sports Medicine",
          "cited_by_count": 5,
          "topics": [
            "Tendon Structure and Treatment",
            "Foot and Ankle Surgery",
            "Diagnosis and Treatment of Venous Diseases"
          ]
        },
        {
          "openalex_id": "W3158779778",
          "year": 2021,
          "title": "Morphological variants to predict outcome of avascular necrosis in developmental dysplasia of the hip",
          "type": "article",
          "venue": "The Bone & Joint Journal",
          "cited_by_count": 16,
          "topics": [
            "Hip disorders and treatments",
            "Orthopaedic implants and arthroplasty",
            "Bone and Joint Diseases"
          ]
        },
        {
          "openalex_id": "W4306385926",
          "year": 2022,
          "title": "Impact of the COVID-19 lockdown on patient-reported outcome measures in Dutch hip and knee arthroplasty patients",
          "type": "article",
          "venue": "Acta Orthopaedica",
          "cited_by_count": 4,
          "topics": [
            "COVID-19 and healthcare impacts",
            "Total Knee Arthroplasty Outcomes",
            "Bone fractures and treatments"
          ]
        },
        {
          "openalex_id": "W4207059854",
          "year": 2022,
          "title": "Statistical Shape Modeling of US Images to Predict Hip Dysplasia Development in Infants",
          "type": "article",
          "venue": "Radiology",
          "cited_by_count": 9,
          "topics": [
            "Hip disorders and treatments",
            "Orthopaedic implants and arthroplasty",
            "Hip and Femur Fractures"
          ]
        },
        {
          "openalex_id": "W4384945375",
          "year": 2023,
          "title": "Socioeconomic inequalities in patient-reported outcome measures of Dutch primary hip and knee arthroplasty patients for osteoarthritis",
          "type": "article",
          "venue": "Osteoarthritis and Cartilage",
          "cited_by_count": 22,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Osteoarthritis Treatment and Mechanisms",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W4404749594",
          "year": 2024,
          "title": "The use of patient-reported outcome measures to improve patient-related outcomes – a systematic review",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 96,
          "topics": [
            "Cancer survivorship and care",
            "Delphi Technique in Research",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4393057033",
          "year": 2024,
          "title": "The use of patient-reported outcome measures to improve patient-related outcomes – a systematic review",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 3,
          "topics": [
            "Cancer survivorship and care",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Childhood Cancer Survivors' Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Juan Cabasés",
    "member_affiliation": "Department of Economics, Universidad Pública de Navarra",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5039017875",
      "display_name": "Juan Manuel Cabasés Hita",
      "orcid": "0000-0003-0207-4137",
      "reported_affiliation": "Universidad de Navarra",
      "works_count": 141,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 52
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 27
        },
        {
          "topic": "Global Health Care Issues",
          "works": 21
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 8
        },
        {
          "topic": "Social Sciences and Policies",
          "works": 7
        },
        {
          "topic": "Pelvic floor disorders treatments",
          "works": 6
        },
        {
          "topic": "Public Health and Social Inequalities",
          "works": 6
        },
        {
          "topic": "Healthcare Systems and Technology",
          "works": 6
        },
        {
          "topic": "Public Health in Brazil",
          "works": 5
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 5
        },
        {
          "topic": "Primary Care and Health Outcomes",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Eduardo Sánchez",
          "works": 26
        },
        {
          "name": "María Errea Rodríguez",
          "works": 9
        },
        {
          "name": "Luis Salvador‐Carulla",
          "works": 7
        },
        {
          "name": "Mikel Berdud",
          "works": 7
        },
        {
          "name": "Ramón San Miguel",
          "works": 5
        },
        {
          "name": "Francisco José Vázquez Polo",
          "works": 5
        },
        {
          "name": "Miguel A. Negrín",
          "works": 5
        },
        {
          "name": "José Jesús Martín Martín",
          "works": 5
        },
        {
          "name": "Idoia Gaminde Inda",
          "works": 5
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 4
        },
        {
          "name": "Fernando Lera‐López",
          "works": 4
        },
        {
          "name": "Ion Agirrezabal",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4401283689",
          "year": 2024,
          "title": "Self-perceived quality of life by institutionalised adults with cerebral palsy in Spain",
          "type": "article",
          "venue": "Gaceta Sanitaria",
          "cited_by_count": 5,
          "topics": [
            "Cerebral Palsy and Movement Disorders",
            "Occupational Therapy Practice and Research",
            "Stroke Rehabilitation and Recovery"
          ]
        },
        {
          "openalex_id": "W4385620490",
          "year": 2023,
          "title": "Long‐term cost‐effectiveness analysis of sacral neuromodulation in the treatment of severe faecal incontinence",
          "type": "article",
          "venue": "Colorectal Disease",
          "cited_by_count": 5,
          "topics": [
            "Pelvic floor disorders treatments",
            "Urinary Bladder and Prostate Research",
            "Congenital gastrointestinal and neural anomalies"
          ]
        },
        {
          "openalex_id": "W4313625145",
          "year": 2023,
          "title": "Socio-demographic indicators of self-reported health based on EQ-5D-3L: A cross-country analysis of population surveys from 18 countries",
          "type": "article",
          "venue": "Frontiers in Public Health",
          "cited_by_count": 13,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, psychology, and well-being",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4220758057",
          "year": 2022,
          "title": "Changes in Inequality in Use of Maternal Health Care Services: Evidence from Skilled Birth Attendance in Mauritania for the Period 2007–2015",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 11,
          "topics": [
            "Global Maternal and Child Health",
            "Healthcare Systems and Reforms",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4229078422",
          "year": 2022,
          "title": "Economic burden of long-term treatment of severe fecal incontinence",
          "type": "article",
          "venue": "Cirugía Española (English Edition)",
          "cited_by_count": 13,
          "topics": [
            "Stoma care and complications",
            "Pelvic floor disorders treatments",
            "Pressure Ulcer Prevention and Management"
          ]
        },
        {
          "openalex_id": "W4205150269",
          "year": 2022,
          "title": "Perceived Health and Earnings: Evidence from the European Working Conditions Survey 2015",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 2,
          "topics": [
            "Employment and Welfare Studies",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W111806169",
          "year": 1981,
          "title": "La medida de la salud",
          "type": "article",
          "venue": "Información Comercial Española, ICE: Revista de economía",
          "cited_by_count": 62,
          "topics": [
            "Health and Lifestyle Studies"
          ]
        },
        {
          "openalex_id": "W167233516",
          "year": 1983,
          "title": "Economía de la salud y política económica sanitaria",
          "type": "article",
          "venue": "Boletín de Estudios Económicos",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W70254767",
          "year": 1986,
          "title": "Costes del absentismo laboral por abuso de alcohol en la Comunidad Autónoma Vasca",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 1,
          "topics": [
            "Stress and Burnout Research",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W3212731283",
          "year": 1987,
          "title": "Análisis coste-beneficio del programa de detección precoz de enfermedades metabólicas en la Comunidad Autónoma Vasca",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2803555760",
          "year": 2018,
          "title": "Validity of the EQ–5D–5L and reference norms for the Spanish population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 210,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Public Health Policies and Education"
          ]
        },
        {
          "openalex_id": "W2326661655",
          "year": 2015,
          "title": "Valuation and Modeling of EQ-5D-5L Health States Using a Hybrid Approach",
          "type": "article",
          "venue": "Medical Care",
          "cited_by_count": 154,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W2073168674",
          "year": 2005,
          "title": "Estimating the impact of hepatitis C virus therapy on future liver-related morbidity, mortality and costs related to chronic hepatitis C",
          "type": "article",
          "venue": "Journal of Hepatology",
          "cited_by_count": 109,
          "topics": [
            "Hepatitis C virus research",
            "Diabetes Management and Education",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2557436966",
          "year": 2016,
          "title": "Cost analysis and cost-benefit analysis of a medication review with follow-up service in aged polypharmacy patients",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 62,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance",
            "Public Health in Brazil"
          ]
        },
        {
          "openalex_id": "W2897619872",
          "year": 2018,
          "title": "Impact of successful treatment with direct-acting antiviral agents on health-related quality of life in chronic hepatitis C patients",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 57,
          "topics": [
            "Hepatitis C virus research",
            "Hepatitis Viruses Studies and Epidemiology",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2462471994",
          "year": 2016,
          "title": "Incentives and intrinsic motivation in healthcare",
          "type": "article",
          "venue": "Gaceta Sanitaria",
          "cited_by_count": 53,
          "topics": [
            "Accounting and Organizational Management",
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2090382983",
          "year": 1998,
          "title": "Utilisation of mental health services and costs of patients with schizophrenia in three areas of Spain",
          "type": "article",
          "venue": "The British Journal of Psychiatry",
          "cited_by_count": 53,
          "topics": [
            "Schizophrenia research and treatment",
            "Mental Health Treatment and Access",
            "Family Caregiving in Mental Illness"
          ]
        }
      ]
    }
  },
  {
    "name": "Juan M. Ramos-Goñi",
    "member_affiliation": "Maths in Health",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013320",
        "title": "Reintroduction of the ranking task in EQ-5D valuation. Improved data quality and reduced level of inconsistencies?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014210",
        "title": "Health-related quality of life and perceived burden of informal caregivers of patients with rare diseases in Europe",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016430",
        "title": "Issue panel and Workshop at ISPOR Singapore 2016",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016510",
        "title": "ISPOR Workshop: DETERMINING UTILITY OF MULTI-ATTRIBUTE HEALTH STATES: NEW MEASUREMENT AND ANALYTIC APPROACHES",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016610",
        "title": "A Randomised Controlled Trial of the effect of Short-Stretch Inelastic Compression bandages on Knee Function following total knee arthroplasty: Comparison of EQ-5D-3L and EQ-5D-5L",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170310R2",
        "title": "Interval TTO valuation approach (2nd revision)",
        "working_group": "Valuation"
      },
      {
        "project_id": "2588-TR",
        "title": "QC Tool as Web App (R/Shiny)",
        "working_group": "Valuation"
      },
      {
        "project_id": "450-RA",
        "title": "Developing tools (Stata, R and Excel) for calculating utility values, analysing and reporting data from the EQ-5D family of instruments",
        "working_group": "Descriptive Systems, Populations and Health Systems, Youth, Education and Outreach"
      },
      {
        "project_id": "74-RA",
        "title": "General public EQ-5D measurement before and during general Covid-19 quarantine in Spain",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5047957689",
      "display_name": "Juan Manuel Ramos-Goñi",
      "orcid": "0000-0002-9568-5190",
      "reported_affiliation": "SGH Warsaw School of Economics",
      "works_count": 96,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 67
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 34
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 9
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 8
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 7
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 7
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 5
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 5
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 5
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 4
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Oliver Rivero‐Arias",
          "works": 18
        },
        {
          "name": "Mark Oppe",
          "works": 14
        },
        {
          "name": "Koonal Shah",
          "works": 8
        },
        {
          "name": "Simone Kreimeier",
          "works": 8
        },
        {
          "name": "Elly Stolk",
          "works": 7
        },
        {
          "name": "Kim Rand",
          "works": 7
        },
        {
          "name": "Nancy Devlin",
          "works": 7
        },
        {
          "name": "Kristina Ludwig",
          "works": 6
        },
        {
          "name": "Mathieu F. Janssen",
          "works": 6
        },
        {
          "name": "José Luis Pinto Prades",
          "works": 6
        },
        {
          "name": "Wolfgang Greiner",
          "works": 6
        },
        {
          "name": "Cristina Valcárcel‐Nazco",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4407456299",
          "year": 2025,
          "title": "An Acquired Taste: Latent Class Analysis to Compare Adolescent and Adult Preferences for EQ-5D-Y-3L Health States",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient-Provider Communication in Healthcare"
          ]
        },
        {
          "openalex_id": "W4416297506",
          "year": 2025,
          "title": "Design and implementation of data quality controls in the EQ-DAPHNIE study: insights from the pilot phase and 15-country analysis",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 3,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Census and Population Estimation",
            "Data Quality and Management"
          ]
        },
        {
          "openalex_id": "W4413301583",
          "year": 2025,
          "title": "Eliciting and Anchoring Health State Preferences Using Discrete Choice Experiments Among Adults, Adolescents, and Children",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4410056786",
          "year": 2025,
          "title": "EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 6,
          "topics": [
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health, Environment, Cognitive Aging"
          ]
        },
        {
          "openalex_id": "W4415914601",
          "year": 2025,
          "title": "Health State Utility Values Associated with Knee Osteoarthritis: A Vignette-Based Approach",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 1,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W4413045171",
          "year": 2025,
          "title": "Health-related quality of life and QALY loss under COVID-19 lockdown: The case of Spain",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "COVID-19 and healthcare impacts",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2019692520",
          "year": 2009,
          "title": "Patient involvement in health research: A contribution to a systematic review on the effectiveness of treatments for degenerative ataxias",
          "type": "review",
          "venue": "Social Science & Medicine",
          "cited_by_count": 75,
          "topics": [
            "Mental Health and Patient Involvement",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Genetic Neurodegenerative Diseases"
          ]
        },
        {
          "openalex_id": "W2003089275",
          "year": 2011,
          "title": "Avoidable costs of physical treatments for chronic back, neck and shoulder pain within the Spanish National Health Service: a cross-sectional study",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 30,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Spine and Intervertebral Disc Pathology",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2169222192",
          "year": 2011,
          "title": "Eq5d: A command to Calculate Index Values for the EQ-5D Quality-of-life Instrument",
          "type": "article",
          "venue": "The Stata Journal Promoting communications on statistics and Stata",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Workplace Health and Well-being"
          ]
        },
        {
          "openalex_id": "W2013741355",
          "year": 2011,
          "title": "PCV91 Cost-Effectiveness of Endovascular Treatment Versus Open Surgery in Patients with Steno-Occlusive Disease of the Femoral Artery",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Peripheral Artery Disease Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2907128483",
          "year": 2019,
          "title": "Overview, Update, and Lessons Learned From the International EQ-5D-5L Valuation Work: Version 2 of the EQ-5D-5L Valuation Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 365,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2791479921",
          "year": 2018,
          "title": "Population norms for the EQ-5D-3L: a cross-country analysis of population surveys for 20 countries",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 346,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2337676734",
          "year": 2016,
          "title": "EuroQol Protocols for Time Trade-Off Valuation of Health Outcomes",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 246,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2772302443",
          "year": 2017,
          "title": "Handling Data Quality Issues to Estimate the Spanish EQ-5D-5L Value Set Using a Hybrid Interval Regression Approach",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 246,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2735686076",
          "year": 2017,
          "title": "The Indonesian EQ-5D-5L Value Set",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 205,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Systems and Reforms"
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
          "openalex_id": "W2567299962",
          "year": 2016,
          "title": "Quality Control Process for EQ-5D-5L Valuation Studies",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 178,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W3017192319",
          "year": 2020,
          "title": "International Valuation Protocol for the EQ-5D-Y-3L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 161,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Juan Pedro Alonso",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2592-RA",
        "title": "Response Scale Heterogeneity in the EQ-5D: Interpreting Response Categories Across Chronic Disease Populations in Argentina",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5109481311",
      "display_name": "María del Mar Alonso Montejo",
      "orcid": "",
      "reported_affiliation": "",
      "works_count": 15,
      "top_topics": [
        {
          "topic": "Diabetes Management and Research",
          "works": 4
        },
        {
          "topic": "Diabetes and associated disorders",
          "works": 3
        },
        {
          "topic": "Pancreatic function and diabetes",
          "works": 2
        },
        {
          "topic": "Blood Coagulation and Thrombosis Mechanisms",
          "works": 2
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 2
        },
        {
          "topic": "Bartonella species infections research",
          "works": 2
        },
        {
          "topic": "Viral Infections and Vectors",
          "works": 2
        },
        {
          "topic": "Neonatal and fetal brain pathology",
          "works": 2
        },
        {
          "topic": "Mitochondrial Function and Pathology",
          "works": 2
        },
        {
          "topic": "Neonatal Respiratory Health Research",
          "works": 2
        },
        {
          "topic": "Health and Lifestyle Studies",
          "works": 1
        },
        {
          "topic": "Nursing care and research",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "María del Carmen López Castillo",
          "works": 7
        },
        {
          "name": "Natalia Saldaña García",
          "works": 6
        },
        {
          "name": "María Álvarez Casaño",
          "works": 4
        },
        {
          "name": "Isabel Leiva‐Gea",
          "works": 4
        },
        {
          "name": "Jose Manuel Jiménez Hinojosa",
          "works": 4
        },
        {
          "name": "María Ángeles Santos Mata",
          "works": 4
        },
        {
          "name": "Francisco A. Macı́as",
          "works": 4
        },
        {
          "name": "María del Mar Romero Pérez",
          "works": 4
        },
        {
          "name": "Marta de Toro",
          "works": 4
        },
        {
          "name": "Gabriela Martínez",
          "works": 4
        },
        {
          "name": "Pilar Munguira",
          "works": 4
        },
        {
          "name": "Gustavo Vivas",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3074368178",
          "year": 2021,
          "title": "Bartonella henselae neuroretinitis: A case report",
          "type": "article",
          "venue": "Medicina Clínica (English Edition)",
          "cited_by_count": 2,
          "topics": [
            "Bartonella species infections research",
            "Viral Infections and Vectors",
            "Rabies epidemiology and control"
          ]
        },
        {
          "openalex_id": "W3121327284",
          "year": 2021,
          "title": "Study of the quality of life and adherence to treatment in patients from 2 to 16 years-old with type 1 diabetes mellitus in Andalusia, Spain",
          "type": "article",
          "venue": "Anales de Pediatría (English Edition)",
          "cited_by_count": 4,
          "topics": [
            "Diabetes Management and Research",
            "Pancreatic function and diabetes",
            "Diabetes and associated disorders"
          ]
        },
        {
          "openalex_id": "W3130197357",
          "year": 2020,
          "title": "Actualización en el tratamiento del shock hemodinámico en recién nacidos prematuros",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Mechanical Circulatory Support Devices",
            "Renal function and acid-base balance",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W3126568443",
          "year": 2020,
          "title": "Actualización en hiperamoniemia en periodo neonatal",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Neonatal Health and Biochemistry",
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W3108530291",
          "year": 2020,
          "title": "Actualización en las recomendaciones sobre transporte neonatal",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Neonatal Respiratory Health Research"
          ]
        },
        {
          "openalex_id": "W3109626375",
          "year": 2020,
          "title": "Consumo de tóxicos en la gestación y repercusión en el recién nacido",
          "type": "article",
          "venue": "Dialnet (Universidad de la Rioja)",
          "cited_by_count": 0,
          "topics": [
            "Prenatal Substance Exposure Effects",
            "Effects and risks of endocrine disrupting chemicals"
          ]
        },
        {
          "openalex_id": "W2897958778",
          "year": 2018,
          "title": "Trombosis en cuidados críticos neonatales: nuestra experiencia en 10 años",
          "type": "article",
          "venue": "Anales de Pediatría",
          "cited_by_count": 2,
          "topics": [
            "Blood Coagulation and Thrombosis Mechanisms",
            "Venous Thromboembolism Diagnosis and Management",
            "Cardiovascular Issues in Pregnancy"
          ]
        },
        {
          "openalex_id": "W2944928032",
          "year": 2019,
          "title": "Estudio de costes directos de la diabetes mellitus tipo 1 en pacientes entre 2 y 16 años en Andalucía",
          "type": "article",
          "venue": "Endocrinología Diabetes y Nutrición",
          "cited_by_count": 8,
          "topics": [
            "Diabetes Management and Research",
            "Diabetes and associated disorders",
            "Pancreatic function and diabetes"
          ]
        },
        {
          "openalex_id": "W2981806479",
          "year": 2019,
          "title": "Study of direct costs of type 1 diabetes mellitus in Andalusian patients aged 2–16 years",
          "type": "article",
          "venue": "Endocrinología Diabetes y Nutrición (English ed )",
          "cited_by_count": 5,
          "topics": [
            "Diabetes and associated disorders",
            "Diabetes Management and Research",
            "Diabetes Treatment and Management"
          ]
        },
        {
          "openalex_id": "W4242439774",
          "year": 2019,
          "title": "Thrombosis in the intensive care unit: Our experience in 10 years",
          "type": "article",
          "venue": "Anales de Pediatría (English Edition)",
          "cited_by_count": 0,
          "topics": [
            "Venous Thromboembolism Diagnosis and Management",
            "Blood Coagulation and Thrombosis Mechanisms",
            "Heparin-Induced Thrombocytopenia and Thrombosis"
          ]
        },
        {
          "openalex_id": "W3035742925",
          "year": 2020,
          "title": "Estudio de calidad de vida y adherencia al tratamiento en pacientes de 2 a 16 años con diabetes mellitus tipo 1 en Andalucía",
          "type": "article",
          "venue": "Anales de Pediatría",
          "cited_by_count": 21,
          "topics": [
            "Diabetes Management and Research",
            "Health and Lifestyle Studies",
            "Nursing care and research"
          ]
        },
        {
          "openalex_id": "W3196084403",
          "year": 2020,
          "title": "Neurorretinitis por Bartonella henselae: a propósito de un caso",
          "type": "article",
          "venue": "Medicina Clínica",
          "cited_by_count": 2,
          "topics": [
            "Bartonella species infections research",
            "Genital Health and Disease",
            "Viral Infections and Vectors"
          ]
        },
        {
          "openalex_id": "W3109951784",
          "year": 2020,
          "title": "Hipotermia en encefalopatía hipóxico-neonatal",
          "type": "article",
          "venue": "Acta Pediátrica de México",
          "cited_by_count": 1,
          "topics": [
            "Neonatal and fetal brain pathology",
            "Mitochondrial Function and Pathology",
            "Cardiac Arrhythmias and Treatments"
          ]
        }
      ]
    }
  },
  {
    "name": "Juanita Haagsma",
    "member_affiliation": "Erasmus MC",
    "is_member": true,
    "projects": [
      {
        "project_id": "141-RA",
        "title": "Test-retest reliability of the EQ-5D-5L in the general population of the UK, Italy and the Netherlands",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1498-PHD",
        "title": "Psychometric properties of EQ-5D-5L, bolt-ons and the EQ-HWB",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "151-RA",
        "title": "Does rapid fluctuation of health over time affect the actual time span that is used by trauma patients when thinking of ‘your health today’?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1604-RA",
        "title": "Population health impact of the COVID-19 pandemic (POPCORN): fourth wave",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1954-RA",
        "title": "Translation of the EQ-HWB into Dutch language",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "20180330",
        "title": "Is there a need for bolt-on itching and fatigue beyond pain and discomfort? Empirical evidence to demonstrate whether specific symptoms are contained within the broader pain/discomfort dimension and development of a standard approach to reject/confirm a b",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20180380",
        "title": "The added value of bolt on dimensions: a systematic review of studies that analyzed the performance of proposed bolt-ons for the EQ-5D",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20180630",
        "title": "’Equimetrics’ of the EQ-5D. Measuring inequalities in health in the UK, Netherlands, and Italy to assess the potential of the EQ-5D-3L and 5L as outcome measures and determinants of income inequality",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20190120",
        "title": "Prediction of injury recovery patterns: can multiple measurements of EQ-5D data be used in dynamic prediction models?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2159-RA",
        "title": "Evaluating and comparing the psychometric properties of the EQ-5D-5L, five bolt-ons and the EQ-HWB-S in injury patients",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2426-PHD",
        "title": "Understanding recall bias in health-related quality of life: the role of reference frames, response styles and life events",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "243-RA",
        "title": "The relationship between the EQ-5D-5L “anxiety/depression” dimension and anxiety and depression symptoms",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2456-BT",
        "title": "Psychometric Evaluation of EQ-5D-5L, EQ-5D-5L with Bolt-On Items in Sarcoma and Colorectal Cancer Patients",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "315-RA",
        "title": "The relation between the EQ-5D-5L and fatigue and cognition problems: does the EQ-5D-5L capture persistent symptoms of infectious disease?",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "420-RA",
        "title": "CORFU: a COVID-19 follow-up study",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "460-RA",
        "title": "Population health impact of the COVID-19 pandemic (POPCORN): third wave",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "77-RA",
        "title": "Public health impact of the COVID-19 pandemia: inequity of its effects and the role of health policies.",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5060133399",
      "display_name": "Juanita A. Haagsma",
      "orcid": "0000-0002-2055-548X",
      "reported_affiliation": "Erasmus MC",
      "works_count": 358,
      "top_topics": [
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 97
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 72
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 69
        },
        {
          "topic": "Traumatic Brain Injury and Neurovascular Disturbances",
          "works": 66
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 46
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 28
        },
        {
          "topic": "Cardiac Arrest and Resuscitation",
          "works": 21
        },
        {
          "topic": "Posttraumatic Stress Disorder Research",
          "works": 20
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 19
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 17
        },
        {
          "topic": "Global Health Care Issues",
          "works": 17
        },
        {
          "topic": "Long-Term Effects of COVID-19",
          "works": 16
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Suzanne Polinder",
          "works": 131
        },
        {
          "name": "Alexandra Bražinová",
          "works": 56
        },
        {
          "name": "Amra Čović",
          "works": 56
        },
        {
          "name": "Nada Anđelić",
          "works": 52
        },
        {
          "name": "Ari Ercole",
          "works": 52
        },
        {
          "name": "Brecht Devleesschauwer",
          "works": 52
        },
        {
          "name": "Giuseppe Citerio",
          "works": 51
        },
        {
          "name": "Endre Czeiter",
          "works": 51
        },
        {
          "name": "Ronny Beer",
          "works": 51
        },
        {
          "name": "Philippe Azouvi",
          "works": 50
        },
        {
          "name": "Bart Depreitere",
          "works": 50
        },
        {
          "name": "Valery L. Feigin",
          "works": 49
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7154701455",
          "year": 2026,
          "title": "The effect of feedback on the diagnostic process of physicians at the emergency department: a systematic review",
          "type": "review",
          "venue": "European Journal of Emergency Medicine",
          "cited_by_count": 0,
          "topics": [
            "Clinical Reasoning and Diagnostic Skills",
            "Clinical Laboratory Practices and Quality Control",
            "Radiology practices and education"
          ]
        },
        {
          "openalex_id": "W7148767027",
          "year": 2026,
          "title": "The effectiveness of decompressive craniectomy size in traumatic brain injury; an international, observational, comparative effectiveness study",
          "type": "article",
          "venue": "Brain and Spine",
          "cited_by_count": 1,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "Traumatic Brain Injury Research",
            "Trauma and Emergency Care Studies"
          ]
        },
        {
          "openalex_id": "W7154230313",
          "year": 2026,
          "title": "The impact of survivorship care on burden of disease among Hodgkin lymphoma survivors",
          "type": "article",
          "venue": "JNCI Journal of the National Cancer Institute",
          "cited_by_count": 2,
          "topics": [
            "Chemotherapy-induced cardiotoxicity and mitigation",
            "Cancer survivorship and care",
            "Cancer-related cognitive impairment studies"
          ]
        },
        {
          "openalex_id": "W4409534169",
          "year": 2025,
          "title": "A societal cost-benefit analysis of falls prevention in community-dwelling older people in the Netherlands",
          "type": "article",
          "venue": "Experimental Gerontology",
          "cited_by_count": 0,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4415900046",
          "year": 2025,
          "title": "Beyond mild, moderate, and severe traumatic brain injury: modelling severity from clinical, neuroimaging, and blood-based indicators",
          "type": "article",
          "venue": "EBioMedicine",
          "cited_by_count": 5,
          "topics": [
            "Traumatic Brain Injury and Neurovascular Disturbances",
            "S100 Proteins and Annexins",
            "Traumatic Brain Injury Research"
          ]
        },
        {
          "openalex_id": "W4412479558",
          "year": 2025,
          "title": "Clinical Practice Guideline Recommendations on Mental Health in Trauma",
          "type": "article",
          "venue": "JAMA Surgery",
          "cited_by_count": 2,
          "topics": [
            "Clinical practice guidelines implementation",
            "Trauma and Emergency Care Studies",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W2886256324",
          "year": 1967,
          "title": "Aujeszky's disease in cats",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Herpesvirus Infections and Treatments",
            "Dermatology and Skin Diseases",
            "Acne and Rosacea Treatments and Effects"
          ]
        },
        {
          "openalex_id": "W194682148",
          "year": 1970,
          "title": "Studies on the resistance of Aleutian disease agent to chemical and physical effects with special reference to the control of this disease.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Genetic Neurodegenerative Diseases"
          ]
        },
        {
          "openalex_id": "W2726593807",
          "year": 1977,
          "title": "Slow virus diseases of animals and man",
          "type": "book-review",
          "venue": "Veterinary Microbiology",
          "cited_by_count": 127,
          "topics": [
            "Animal Disease Management and Epidemiology",
            "Virology and Viral Diseases",
            "Zoonotic diseases and public health"
          ]
        },
        {
          "openalex_id": "W253211376",
          "year": 1978,
          "title": "Klinik der Katzenkrankheiten",
          "type": "book-review",
          "venue": "Veterinary Microbiology",
          "cited_by_count": 4,
          "topics": [
            "Biotin and Related Studies",
            "Neurological diseases and metabolism",
            "Virus-based gene therapy research"
          ]
        },
        {
          "openalex_id": "W2912654919",
          "year": 2018,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseases and injuries for 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 14146,
          "topics": [
            "Health disparities and outcomes",
            "Chronic Disease Management Strategies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2097950056",
          "year": 2012,
          "title": "Disability-adjusted life years (DALYs) for 291 diseases and injuries in 21 regions, 1990–2010: a systematic analysis for the Global Burden of Disease Study 2010",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 9025,
          "topics": [
            "Health disparities and outcomes",
            "Cerebral Palsy and Movement Disorders",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W2899736836",
          "year": 2018,
          "title": "Global, regional, and national age-sex-specific mortality for 282 causes of death in 195 countries and territories, 1980–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 8712,
          "topics": [
            "Global Maternal and Child Health",
            "Insurance, Mortality, Demography, Risk Management",
            "Autopsy Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W2108344016",
          "year": 2012,
          "title": "Years lived with disability (YLDs) for 1160 sequelae of 289 diseases and injuries 1990–2010: a systematic analysis for the Global Burden of Disease Study 2010",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 8424,
          "topics": [
            "Frailty in Older Adults",
            "Chronic Disease Management Strategies",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2527824850",
          "year": 2016,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 310 diseases and injuries, 1990–2015: a systematic analysis for the Global Burden of Disease Study 2015",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 7421,
          "topics": [
            "Injury Epidemiology and Prevention",
            "Global Public Health Policies and Epidemiology",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2614986146",
          "year": 2016,
          "title": "Global, regional, and national life expectancy, all-cause mortality, and cause-specific mortality for 249 causes of death, 1980–2015: a systematic analysis for the Global Burden of Disease Study 2015",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 6717,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Global Maternal and Child Health",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2098082628",
          "year": 2015,
          "title": "Global, regional, and national incidence, prevalence, and years lived with disability for 301 acute and chronic diseases and injuries in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 6527,
          "topics": [
            "Chronic Disease Management Strategies",
            "Health disparities and outcomes",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W2899773405",
          "year": 2018,
          "title": "Global, regional, and national comparative risk assessment of 84 behavioural, environmental and occupational, and metabolic risks or clusters of risks for 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 5057,
          "topics": [
            "Health, Environment, Cognitive Aging",
            "Risk Perception and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  }
]
