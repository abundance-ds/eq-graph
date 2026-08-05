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
    "name": "Helen Harcombe",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2015160",
        "title": "Relationship between behavioural risk factors for poor health and the EQ-5D: Prospective analyses in a New Zealand cohort",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5081829233",
      "display_name": "Helen Harcombe",
      "orcid": "0000-0002-2612-1789",
      "reported_affiliation": "University of Otago",
      "works_count": 56,
      "top_topics": [
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 26
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 20
        },
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 18
        },
        {
          "topic": "Occupational Health and Safety Research",
          "works": 12
        },
        {
          "topic": "Occupational health in dentistry",
          "works": 10
        },
        {
          "topic": "Traumatic Brain Injury Research",
          "works": 7
        },
        {
          "topic": "Occupational Health and Performance",
          "works": 5
        },
        {
          "topic": "Fibromyalgia and Chronic Fatigue Syndrome Research",
          "works": 4
        },
        {
          "topic": "Workplace Health and Well-being",
          "works": 4
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 4
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 3
        },
        {
          "topic": "Traffic and Road Safety",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sarah Derrett",
          "works": 39
        },
        {
          "name": "Emma Wyeth",
          "works": 23
        },
        {
          "name": "Gabrielle Davie",
          "works": 19
        },
        {
          "name": "David McBride",
          "works": 13
        },
        {
          "name": "Georgia Ntani",
          "works": 12
        },
        {
          "name": "Vanda Elisa Andrés Felli",
          "works": 12
        },
        {
          "name": "Eda Merisalu",
          "works": 12
        },
        {
          "name": "Rima R. Habib",
          "works": 12
        },
        {
          "name": "Farideh Sadeghian",
          "works": 12
        },
        {
          "name": "Ko Matsudaira",
          "works": 12
        },
        {
          "name": "Marianela Rojas",
          "works": 12
        },
        {
          "name": "Helen L. Kelsall",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7119496605",
          "year": 2026,
          "title": "Are We Ready? Ageing of People Living With <scp>HIV</scp> in Aotearoa New Zealand: <scp>HIV</scp> Knowledge and Attitudes Among Staff in Aged Care Facilities",
          "type": "article",
          "venue": "Australasian Journal on Ageing",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W7163824200",
          "year": 2026,
          "title": "Long-term follow-up of work participation among New Zealand workers following injury: A 12-year national cohort study",
          "type": "article",
          "venue": "Journal of Occupational and Environmental Medicine",
          "cited_by_count": 0,
          "topics": [
            "Injury Epidemiology and Prevention",
            "Musculoskeletal pain and rehabilitation",
            "Trauma and Emergency Care Studies"
          ]
        },
        {
          "openalex_id": "W7166657384",
          "year": 2026,
          "title": "PREDICTORS OF SEVERE OR MULTIPLE SUBSEQUENT INJURIES AMONG PEOPLE PRESENTING TO HEALTHCARE PROVIDERS FOLLOWING AN INJURY",
          "type": "conference-paper",
          "venue": "World Physiotherapy Congress Archive",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W4411005523",
          "year": 2025,
          "title": "BMI-z score trajectories of Indonesian children and adolescents between 1993 and 2014 and associated risk factors",
          "type": "article",
          "venue": "Public Health Nutrition",
          "cited_by_count": 1,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Child Nutrition and Water Access",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W4415917970",
          "year": 2025,
          "title": "Longitudinal study of knee pain amongst workers in the Cultural and Psychosocial Influences on Disability (CUPID) study",
          "type": "article",
          "venue": "BMC Musculoskeletal Disorders",
          "cited_by_count": 1,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Osteoarthritis Treatment and Mechanisms",
            "Occupational health in dentistry"
          ]
        },
        {
          "openalex_id": "W4402059829",
          "year": 2024,
          "title": "734 Preventing subsequent injuries: a feasibility study",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Trauma and Emergency Care Studies",
            "Injury Epidemiology and Prevention",
            "Disaster Response and Management"
          ]
        },
        {
          "openalex_id": "W2169005406",
          "year": 2009,
          "title": "Prevalence and impact of musculoskeletal disorders in New Zealand nurses, postal workers and office workers",
          "type": "article",
          "venue": "Australian and New Zealand Journal of Public Health",
          "cited_by_count": 129,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational health in dentistry",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2109664895",
          "year": 2010,
          "title": "Physical and psychosocial risk factors for musculoskeletal disorders in New Zealand nurses, postal workers and office workers",
          "type": "article",
          "venue": "Injury Prevention",
          "cited_by_count": 120,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Workplace Health and Well-being",
            "Occupational Health and Safety Research"
          ]
        },
        {
          "openalex_id": "W2104828026",
          "year": 2011,
          "title": "\"Do I really want to do this?\" Longitudinal cohort study participants' perspectives on postal survey design: a qualitative study",
          "type": "article",
          "venue": "BMC Medical Research Methodology",
          "cited_by_count": 17,
          "topics": [
            "Survey Methodology and Nonresponse",
            "Focus Groups and Qualitative Methods",
            "Ethics in Clinical Research"
          ]
        },
        {
          "openalex_id": "W2203231878",
          "year": 2012,
          "title": "A mixed methods study of musculoskeletal disorders in New Zealand nurses, postal workers and office workers",
          "type": "dissertation",
          "venue": "Otago University Research Archive (University of Otago)",
          "cited_by_count": 0,
          "topics": [
            "Occupational Health and Safety Research",
            "Musculoskeletal pain and rehabilitation",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2076483860",
          "year": 2013,
          "title": "Patterns of multisite pain and associations with risk factors",
          "type": "article",
          "venue": "Pain",
          "cited_by_count": 194,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2142382699",
          "year": 2013,
          "title": "Disabling musculoskeletal pain in working populations: Is it the job, the person, or the culture?",
          "type": "article",
          "venue": "Pain",
          "cited_by_count": 180,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Occupational Health and Performance"
          ]
        },
        {
          "openalex_id": "W2115005299",
          "year": 2012,
          "title": "The CUPID (Cultural and Psychosocial Influences on Disability) Study: Methods of Data Collection and Characteristics of Study Sample",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 178,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational Health and Safety Research",
            "Occupational health in dentistry"
          ]
        },
        {
          "openalex_id": "W2792438476",
          "year": 2018,
          "title": "Interventions to prevent and reduce the impact of musculoskeletal injuries among nurses: A systematic review",
          "type": "review",
          "venue": "International Journal of Nursing Studies",
          "cited_by_count": 127,
          "topics": [
            "Musculoskeletal pain and rehabilitation",
            "Occupational health in dentistry",
            "Nursing education and management"
          ]
        },
        {
          "openalex_id": "W2344015084",
          "year": 2016,
          "title": "Descriptive Epidemiology of Somatising Tendency: Findings from the CUPID Study",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 107,
          "topics": [
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Psychosomatic Disorders and Their Treatments",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2183320435",
          "year": 2015,
          "title": "The Incremental Effects of Manual Therapy or Booster Sessions in Addition to Exercise Therapy for Knee Osteoarthritis: A Randomized Clinical Trial",
          "type": "article",
          "venue": "Journal of Orthopaedic and Sports Physical Therapy",
          "cited_by_count": 87,
          "topics": [
            "Osteoarthritis Treatment and Mechanisms",
            "Total Knee Arthroplasty Outcomes",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        }
      ]
    }
  },
  {
    "name": "Henry Bailey",
    "member_affiliation": "The University of the West Indies",
    "is_member": true,
    "projects": [
      {
        "project_id": "1414-EO",
        "title": "The First EuroQol Latin American Academy Meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1767-RA",
        "title": "A head on comparison of EQ-VT and crosswalk based EQ-5D-5L value sets.",
        "working_group": "Valuation"
      },
      {
        "project_id": "20170390",
        "title": "Request for funding to cover expenses relating to a proposed visit of Henry Bailey to spend 1 month at the University of Leeds with Paul Kind",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20180040R1",
        "title": "NA",
        "working_group": "Valuation"
      },
      {
        "project_id": "341-RA",
        "title": "Piloting the DCE duration valuation protocol: an EQ-5D-5L valuation study for Trinidad and Tobago.",
        "working_group": "Valuation"
      },
      {
        "project_id": "357-RA",
        "title": "A comparative investigation of inequality measures for EQ-5D outcomes",
        "working_group": "Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5090969739",
      "display_name": "Henry Bailey",
      "orcid": "0000-0002-4479-9948",
      "reported_affiliation": "University of the West Indies",
      "works_count": 41,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 25
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 12
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 7
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 6
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 5
        },
        {
          "topic": "Public Health Policies and Education",
          "works": 4
        },
        {
          "topic": "Dialysis and Renal Disease Management",
          "works": 3
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 2
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 2
        },
        {
          "topic": "Evaluation and Performance Assessment",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Mathieu F. Janssen",
          "works": 12
        },
        {
          "name": "Althea La Foucade",
          "works": 10
        },
        {
          "name": "Girjanauth Boodraj",
          "works": 7
        },
        {
          "name": "Philip Castillo",
          "works": 7
        },
        {
          "name": "Bram Roudijk",
          "works": 6
        },
        {
          "name": "Paul Kind",
          "works": 6
        },
        {
          "name": "Marjorie Wharton",
          "works": 6
        },
        {
          "name": "Marcel F. Jonker",
          "works": 4
        },
        {
          "name": "Eleanor Pullenayegum",
          "works": 4
        },
        {
          "name": "Tasanee Braithwaite",
          "works": 4
        },
        {
          "name": "Alastair Gray",
          "works": 4
        },
        {
          "name": "S Ramsewak",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4408305971",
          "year": 2025,
          "title": "A Head-On Comparison of EQ-VT- and Crosswalk-Based EQ-5D-5L Value Sets",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
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
          "openalex_id": "W4406659077",
          "year": 2025,
          "title": "Quality of life in HIV patients treated at a primary care clinic: a cross-sectional study in Tobago",
          "type": "article",
          "venue": "Journal of HIV/AIDS & Social Services",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "HIV/AIDS Impact and Responses"
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
          "openalex_id": "W2123709959",
          "year": 2005,
          "title": "An economic evaluation of Laparoscopic Cholecystectomy for public hospitals in Trinidad and Tobago",
          "type": "article",
          "venue": "West Indian Medical Journal",
          "cited_by_count": 12,
          "topics": [
            "Gallbladder and Bile Duct Disorders",
            "Bariatric Surgery and Outcomes",
            "Minimally Invasive Surgical Techniques"
          ]
        },
        {
          "openalex_id": "W2012326345",
          "year": 2010,
          "title": "PR3 NATIONAL CULTURE AND EQ-5D VALUE SETS",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Cultural Differences and Values",
            "Social Science and Policy Research",
            "Complex Systems and Decision Making"
          ]
        },
        {
          "openalex_id": "W2002960311",
          "year": 2010,
          "title": "Preliminary findings of an investigation into the relationship between national culture and EQ-5D value sets",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 75,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Evaluation and Performance Assessment",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2037595734",
          "year": 2011,
          "title": "PRM30 RESULTS FROM A NEW VISUAL ANALOGUE SCALE PROTOCOL FOR EQ-5D VALUATIONS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Quality Function Deployment in Product Design"
          ]
        },
        {
          "openalex_id": "W2943646016",
          "year": 2019,
          "title": "EQ-5D-5L population norms and health inequalities for Trinidad and Tobago",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2794963362",
          "year": 2018,
          "title": "Quality-Adjusted Life-Years without Constant Proportionality",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 39,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W3142387932",
          "year": 2021,
          "title": "EQ-5D-5L Population Norms and Health Inequality in Colombia",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 31,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W2215560671",
          "year": 2015,
          "title": "Health and entrepreneurship in four Caribbean Basin countries",
          "type": "article",
          "venue": "Economics & Human Biology",
          "cited_by_count": 30,
          "topics": [
            "Entrepreneurship Studies and Influences",
            "Employment and Welfare Studies",
            "Innovation and Socioeconomic Development"
          ]
        },
        {
          "openalex_id": "W4295345833",
          "year": 2022,
          "title": "The impact of chronic disease and accompanying bio-psycho-social factors on health-related quality of life",
          "type": "article",
          "venue": "Journal of Family Medicine and Primary Care",
          "cited_by_count": 25,
          "topics": [
            "Cancer survivorship and care",
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education"
          ]
        },
        {
          "openalex_id": "W2535713570",
          "year": 2016,
          "title": "Toward Explicit Prioritization for the Caribbean: An EQ-5D Value Set for Trinidad and Tobago",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 21,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2765989435",
          "year": 2017,
          "title": "Health system dynamics analysis of eyecare services in Trinidad and Tobago and progress towards Vision 2020 Goals",
          "type": "article",
          "venue": "Health Policy and Planning",
          "cited_by_count": 19,
          "topics": [
            "Healthcare Systems and Reforms",
            "Retinal Imaging and Analysis",
            "Global Maternal and Child Health"
          ]
        }
      ]
    }
  },
  {
    "name": "Hesam Ghiasvand",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2423-BT",
        "title": "Assessing the Content Validity of EQ-5D Vision Bolt-Ons in People with Diabetic Retinopathy",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5011771775",
      "display_name": "Hesam Ghiasvand",
      "orcid": "0000-0002-3110-6954",
      "reported_affiliation": "University of Warwick",
      "works_count": 60,
      "top_topics": [
        {
          "topic": "Global Maternal and Child Health",
          "works": 14
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 13
        },
        {
          "topic": "Global Health Care Issues",
          "works": 12
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 11
        },
        {
          "topic": "HIV, Drug Use, Sexual Risk",
          "works": 10
        },
        {
          "topic": "MRI in cancer diagnosis",
          "works": 5
        },
        {
          "topic": "Radiomics and Machine Learning in Medical Imaging",
          "works": 5
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 3
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 3
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 3
        },
        {
          "topic": "Food Security and Health in Diverse Populations",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bahram Armoon",
          "works": 17
        },
        {
          "name": "Seyran Naghdi",
          "works": 15
        },
        {
          "name": "Mehdi Noroozi",
          "works": 11
        },
        {
          "name": "Ahmed Abdelalim",
          "works": 7
        },
        {
          "name": "Ibrahim Abdollahpour",
          "works": 7
        },
        {
          "name": "Victor Adekanmbi",
          "works": 7
        },
        {
          "name": "Olatunji Adetokunboh",
          "works": 7
        },
        {
          "name": "Tomi Akinyemiju",
          "works": 7
        },
        {
          "name": "Ziyad Al‐Aly",
          "works": 7
        },
        {
          "name": "Syed Mohamed Aljunid",
          "works": 7
        },
        {
          "name": "Khalid A Altirkawi",
          "works": 7
        },
        {
          "name": "Cătălina Liliana Andrei",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4410456003",
          "year": 2025,
          "title": "Software with artificial intelligence-derived algorithms for detecting and analysing lung nodules in CT scans: systematic review and economic evaluation",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 11,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Radiomics and Machine Learning in Medical Imaging",
            "AI in cancer detection"
          ]
        },
        {
          "openalex_id": "W4415880589",
          "year": 2025,
          "title": "Using a Co-Designed Digital Self-Management Program to Prepare Patients for Hip or Knee Replacement Surgery: Pragmatic Pilot Study",
          "type": "article",
          "venue": "JMIR Rehabilitation and Assistive Technologies",
          "cited_by_count": 0,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Mental Health and Patient Involvement",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4404264262",
          "year": 2024,
          "title": "Does a Digital Self-Management Programme Prepare Patients for Hip or Knee Replacement Surgery: A Pragmatic Mixed Methods Pilot Study (Preprint)",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Cardiac Health and Mental Health",
            "Musculoskeletal Disorders and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W4399073555",
          "year": 2024,
          "title": "Optimising the diagnostic accuracy of First post-contrAst SubtracTed breast MRI (FAST MRI) through interpretation-training: a multicentre e-learning study, mapping the learning curve of NHS Breast Screening Programme (NHSBSP) mammogram readers using an enriched dataset",
          "type": "article",
          "venue": "Breast Cancer Research",
          "cited_by_count": 2,
          "topics": [
            "MRI in cancer diagnosis",
            "Global Cancer Incidence and Screening",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W4402837489",
          "year": 2024,
          "title": "Software using artificial intelligence for nodule and cancer detection in CT lung cancer screening: systematic review of test accuracy studies",
          "type": "review",
          "venue": "Thorax",
          "cited_by_count": 50,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Radiomics and Machine Learning in Medical Imaging",
            "COVID-19 diagnosis using AI"
          ]
        },
        {
          "openalex_id": "W4400678757",
          "year": 2024,
          "title": "Time series analysis of COVID-19's impact on physician and dentist visits in Iran",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 1,
          "topics": [
            "COVID-19 and healthcare impacts",
            "Dental Research and COVID-19",
            "COVID-19 Clinical Research Studies"
          ]
        },
        {
          "openalex_id": "W2301032360",
          "year": 2011,
          "title": "RELATIONSHIP BETWEEN HEALTH INSURANCE AND CATASTROPHIC MEDICAL PAYMENT IN HOSPITALS AFFILIATED TO IRAN UNIVERSITY OF MEDICAL SCIENCE; 2009",
          "type": "article",
          "venue": "",
          "cited_by_count": 4,
          "topics": [
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2272526438",
          "year": 2012,
          "title": "MEASURING INEQUALITY OF DISTRIBUTION OF HEALTH RESOURCES: A CASE STUDY",
          "type": "article",
          "venue": "",
          "cited_by_count": 5,
          "topics": [
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4386042860",
          "year": 2012,
          "title": "Measuring inequality of distribution of health resources: a case study",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 5,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W2189442883",
          "year": 2013,
          "title": "The Inequity of Expenditure Ratios on Health and Food among Different Deciles of Iranian Households",
          "type": "article",
          "venue": "Iranian Journal Of Health Sciences",
          "cited_by_count": 3,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W3092849554",
          "year": 2020,
          "title": "Global burden of 369 diseases and injuries in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 19565,
          "topics": [
            "Global Maternal and Child Health",
            "Global Health and Surgery",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3092861045",
          "year": 2020,
          "title": "Global burden of 87 risk factors in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 9726,
          "topics": [
            "Health, Environment, Cognitive Aging",
            "Sodium Intake and Health",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W2899742633",
          "year": 2018,
          "title": "Global, regional, and national age-sex-specific mortality and life expectancy, 1950–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1217,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2900431425",
          "year": 2018,
          "title": "Measuring progress from 1990 to 2017 and projecting attainment to 2030 of the health-related Sustainable Development Goals for 195 countries and territories: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 558,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2899825622",
          "year": 2018,
          "title": "Population and fertility by age and sex for 195 countries and territories, 1950–2017: a systematic analysis for the Global Burden of Disease Study 2017",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 501,
          "topics": [
            "Global Maternal and Child Health",
            "Insurance, Mortality, Demography, Risk Management",
            "Demographic Trends and Gender Preferences"
          ]
        },
        {
          "openalex_id": "W3009480301",
          "year": 2020,
          "title": "Do NICU developmental care improve cognitive and motor outcomes for preterm infants? A systematic review and meta-analysis",
          "type": "review",
          "venue": "BMC Pediatrics",
          "cited_by_count": 109,
          "topics": [
            "Infant Development and Preterm Care",
            "Neonatal Respiratory Health Research",
            "Neonatal and fetal brain pathology"
          ]
        },
        {
          "openalex_id": "W3023066456",
          "year": 2020,
          "title": "Mapping local patterns of childhood overweight and wasting in low- and middle-income countries between 2000 and 2017",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 95,
          "topics": [
            "Child Nutrition and Water Access",
            "Obesity, Physical Activity, Diet",
            "Energy and Environment Impacts"
          ]
        },
        {
          "openalex_id": "W2982390637",
          "year": 2019,
          "title": "Clinical determinants associated with quality of life for people who live with HIV/AIDS: a Meta-analysis",
          "type": "review",
          "venue": "BMC Health Services Research",
          "cited_by_count": 89,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments",
            "HIV Research and Treatment"
          ]
        }
      ]
    }
  },
  {
    "name": "Hilton Lam",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20170230",
        "title": "Estimating the EQ-5D-5L Value Set for the Philippines",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5071601943",
      "display_name": "Hilton Y. Lam",
      "orcid": "0000-0003-4042-5997",
      "reported_affiliation": "University of the Philippines Manila",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Global Maternal and Child Health",
          "works": 20
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 16
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 12
        },
        {
          "topic": "Injury Epidemiology and Prevention",
          "works": 10
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 10
        },
        {
          "topic": "Disaster Response and Management",
          "works": 10
        },
        {
          "topic": "Global Health Care Issues",
          "works": 9
        },
        {
          "topic": "Disaster Management and Resilience",
          "works": 8
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 7
        },
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 7
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 6
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Adovich S. Rivera",
          "works": 21
        },
        {
          "name": "Carl Abelardo T. Antonio",
          "works": 18
        },
        {
          "name": "Nelson Alvis‐Guzmán",
          "works": 16
        },
        {
          "name": "Foad Abd-Allah",
          "works": 15
        },
        {
          "name": "Arsène Kouablan Adou",
          "works": 15
        },
        {
          "name": "Raghib Ali",
          "works": 15
        },
        {
          "name": "Ubai Alsharif",
          "works": 15
        },
        {
          "name": "Azmeraw T. Amare",
          "works": 15
        },
        {
          "name": "Walid Ammar",
          "works": 15
        },
        {
          "name": "François Alla",
          "works": 14
        },
        {
          "name": "Johan Ärnlöv",
          "works": 14
        },
        {
          "name": "Zulfiqar A Bhutta",
          "works": 13
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7138928176",
          "year": 2026,
          "title": "UP Manila DRRM-H Innovative Tools for Disaster Risk Reduction: A Descriptive Review of Technologies for Resilience and Response",
          "type": "article",
          "venue": "Philippine Journal of Health Research and Development",
          "cited_by_count": 0,
          "topics": [
            "Disaster Response and Management",
            "Disaster Management and Resilience",
            "Posttraumatic Stress Disorder Research"
          ]
        },
        {
          "openalex_id": "W4417158952",
          "year": 2025,
          "title": "Budget Impact and Investment Case for HEARTS Hypertension Control Programs in 4 Low- and Middle-Income Countries",
          "type": "article",
          "venue": "JACC Advances",
          "cited_by_count": 1,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Medication Adherence and Compliance",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4414684375",
          "year": 2025,
          "title": "Cost-Effectiveness Analysis of Oral Health Care Package of Services within a Comprehensive PhilHealth Benefit Package",
          "type": "article",
          "venue": "Acta Medica Philippina",
          "cited_by_count": 0,
          "topics": [
            "Dental Health and Care Utilization",
            "Oral microbiology and periodontitis research",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4414710037",
          "year": 2025,
          "title": "Cost-Effectiveness Analysis of Various Coronavirus Disease (COVID-19) Vaccines against Emerging Variants of Concern in the Philippines",
          "type": "article",
          "venue": "Acta Medica Philippina",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 epidemiological studies",
            "SARS-CoV-2 and COVID-19 Research",
            "Vaccine Coverage and Hesitancy"
          ]
        },
        {
          "openalex_id": "W4414684617",
          "year": 2025,
          "title": "Economic Evaluation of the WHO Elimination Strategy for Hepatitis B for the Philippines",
          "type": "article",
          "venue": "Acta Medica Philippina",
          "cited_by_count": 0,
          "topics": [
            "Hepatitis B Virus Studies",
            "Hepatitis C virus research",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W4414708793",
          "year": 2025,
          "title": "Measuring Hepatitis B-related Stigma: A Systematic Review of Questionnaire-based Studies",
          "type": "review",
          "venue": "Acta Medica Philippina",
          "cited_by_count": 1,
          "topics": [
            "Mental Health Treatment and Access",
            "Hepatitis C virus research",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W1990654283",
          "year": 2009,
          "title": "German automaker wins crucial design patent case in China",
          "type": "article",
          "venue": "Journal of Intellectual Property Law & Practice",
          "cited_by_count": 0,
          "topics": [
            "Intellectual Property and Patents"
          ]
        },
        {
          "openalex_id": "W1977323590",
          "year": 2010,
          "title": "Use of the Griffiths Mental Development Scales in an agro‐industrial province in the Philippines",
          "type": "article",
          "venue": "Child Care Health and Development",
          "cited_by_count": 20,
          "topics": [
            "Cognitive Abilities and Testing",
            "Infant Development and Preterm Care",
            "Children's Physical and Motor Development"
          ]
        },
        {
          "openalex_id": "W2732424477",
          "year": 2013,
          "title": "Current Practices of Blood Service Facilities in the Philippines",
          "type": "article",
          "venue": "Journal of Health Research",
          "cited_by_count": 0,
          "topics": [
            "Blood donation and transfusion practices",
            "Trauma and Emergency Care Studies"
          ]
        },
        {
          "openalex_id": "W1432646618",
          "year": 2014,
          "title": "Assessing the residual risk for transfusion-transmitted infections in the Philippine blood supply.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 2,
          "topics": [
            "Blood donation and transfusion practices",
            "Hepatitis C virus research",
            "HIV, Drug Use, Sexual Risk"
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
          "openalex_id": "W2889517514",
          "year": 2018,
          "title": "Alcohol use and burden for 195 countries and territories, 1990–2016: a systematic analysis for the Global Burden of Disease Study 2016",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 3600,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Alcoholism and Thiamine Deficiency"
          ]
        },
        {
          "openalex_id": "W3143437408",
          "year": 2015,
          "title": "Global, regional, and national comparative risk assessment of 79 behavioural, environmental and occupational, and metabolic risks or clusters of risks in 188 countries, 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2758,
          "topics": [
            "Health, Environment, Cognitive Aging",
            "Air Quality and Health Impacts",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4393858312",
          "year": 2024,
          "title": "Global burden of 288 causes of death and life expectancy decomposition in 204 countries and territories and 811 subnational locations, 1990–2021: a systematic analysis for the Global Burden of Disease Study 2021",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2632,
          "topics": [
            "COVID-19 and healthcare impacts",
            "COVID-19 epidemiological studies",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W2142472354",
          "year": 2015,
          "title": "Global, regional, and national disability-adjusted life years (DALYs) for 306 diseases and injuries and healthy life expectancy (HALE) for 188 countries, 1990–2013: quantifying the epidemiological transition",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 2021,
          "topics": [
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2043449557",
          "year": 2014,
          "title": "Global, regional, and national levels and causes of maternal mortality during 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 1676,
          "topics": [
            "Global Maternal and Child Health",
            "Maternal and fetal healthcare",
            "HIV/AIDS Research and Interventions"
          ]
        }
      ]
    }
  },
  {
    "name": "Hsiang-Wen Lin",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2016440",
        "title": "Taiwan valuation study for the EQ-5D-5L",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5003956817",
      "display_name": "Hsiang‐Wen Lin",
      "orcid": "0000-0002-6771-6746",
      "reported_affiliation": "China Medical University",
      "works_count": 67,
      "top_topics": [
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 17
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 11
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 10
        },
        {
          "topic": "Pharmacy and Medical Practices",
          "works": 6
        },
        {
          "topic": "Health Literacy and Information Accessibility",
          "works": 5
        },
        {
          "topic": "Complementary and Alternative Medicine Studies",
          "works": 5
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 3
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 3
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 3
        },
        {
          "topic": "Traditional Chinese Medicine Studies",
          "works": 3
        },
        {
          "topic": "Potassium and Related Disorders",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Yen‐Ming Huang",
          "works": 11
        },
        {
          "name": "Chien‐Ning Hsu",
          "works": 8
        },
        {
          "name": "Hsin-Hui Tsai",
          "works": 7
        },
        {
          "name": "A. Simon Pickard",
          "works": 6
        },
        {
          "name": "Yu‐Chieh Chen",
          "works": 5
        },
        {
          "name": "Nan Luo",
          "works": 5
        },
        {
          "name": "Daniel Hsiang‐Te Tsai",
          "works": 5
        },
        {
          "name": "Chih‐Hsueh Lin",
          "works": 4
        },
        {
          "name": "I.W. Yu",
          "works": 4
        },
        {
          "name": "Yu Ko",
          "works": 4
        },
        {
          "name": "Okti Ratna Mafruhah",
          "works": 4
        },
        {
          "name": "Po‐Chen Chu",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413449721",
          "year": 2025,
          "title": "Charting the path to better diabetes outcomes: Revealing psychosocial influences on medication adherence through the information-motivation-behavioral skills model among adults with type 2 diabetes",
          "type": "article",
          "venue": "Research in Social and Administrative Pharmacy",
          "cited_by_count": 2,
          "topics": [
            "Medication Adherence and Compliance",
            "Diabetes Management and Education",
            "Mobile Health and mHealth Applications"
          ]
        },
        {
          "openalex_id": "W4412443192",
          "year": 2025,
          "title": "EPH168 Determination of Medication Regimen Complexity Trends in Older Adult Patients With Insomnia: A Triangulation of Findings From Artificial Neural Network and Logistic Regression Analyses",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Mental Health Research Topics",
            "Sleep and related disorders"
          ]
        },
        {
          "openalex_id": "W2885413899",
          "year": 2025,
          "title": "Pharmacists' knowledge, attitudes, self-efficacy and counseling on herbs and dietary supplements.",
          "type": "dissertation",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": [
            "Hermeneutics and Narrative Identity",
            "Aging, Elder Care, and Social Issues",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W4411962102",
          "year": 2025,
          "title": "Prescription patterns of traditional Chinese medications and potential consequences in patients with new-onset cardiac or vascular-related diseases: a nationwide cohort study",
          "type": "article",
          "venue": "BMC Complementary Medicine and Therapies",
          "cited_by_count": 0,
          "topics": [
            "Traditional Chinese Medicine Studies",
            "Complementary and Alternative Medicine Studies",
            "Traditional Chinese Medicine Analysis"
          ]
        },
        {
          "openalex_id": "W4415730185",
          "year": 2025,
          "title": "RWD34 GENERATING REAL-WORLD UTILITY VALUES FOR PEDIATRIC HEALTH STATES IN TAIWAN: A NATIONWIDE EQ-5D-Y-3L VALUATION STUDY USING COMPOSITE TIME TRADE-OFF",
          "type": "conference-abstract",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W4413257249",
          "year": 2025,
          "title": "Risk prediction of QTc prolongation occurrence in cancer patients treated with commonly used oral tyrosine kinase inhibitors: machine learning modeling or conventional statistical analysis better?",
          "type": "article",
          "venue": "BMC Medical Informatics and Decision Making",
          "cited_by_count": 2,
          "topics": [
            "Chemotherapy-induced cardiotoxicity and mitigation",
            "Acute Myocardial Infarction Research",
            "Cardiac electrophysiology and arrhythmias"
          ]
        },
        {
          "openalex_id": "W2598341722",
          "year": 2002,
          "title": "Accelerating Drug Dispensing by Enhancing Physician Order Entry Systems",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Pharmaceutical studies and practices",
            "Pharmacy and Medical Practices",
            "Intravenous Infusion Technology and Safety"
          ]
        },
        {
          "openalex_id": "W2152364595",
          "year": 2002,
          "title": "Cyclosporine C2 Monitoring in Single Lung Transplantation",
          "type": "article",
          "venue": "Zhōngtáiwān yīxué kēxué zázhì",
          "cited_by_count": 0,
          "topics": [
            "Transplantation: Methods and Outcomes",
            "Polyomavirus and related diseases",
            "Renal Transplantation Outcomes and Treatments"
          ]
        },
        {
          "openalex_id": "W2128580805",
          "year": 2005,
          "title": "Effects of a National Health Education Program on the Medication Knowledge of the Public in Taiwan",
          "type": "article",
          "venue": "Annals of Pharmacotherapy",
          "cited_by_count": 20,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Antibiotic Use and Resistance",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2033147256",
          "year": 2006,
          "title": "Trends in off-label β-blocker use: A secondary data analysis",
          "type": "article",
          "venue": "Clinical Therapeutics",
          "cited_by_count": 13,
          "topics": [
            "Pharmaceutical studies and practices",
            "Healthcare cost, quality, practices",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W2101713088",
          "year": 2007,
          "title": "Health Utilities Using the EQ-5D in Studies of Cancer",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 295,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W2617799736",
          "year": 2017,
          "title": "Economic outcomes of pharmacist-physician medication therapy management for polypharmacy elderly: A prospective, randomized, controlled trial",
          "type": "article",
          "venue": "Journal of the Formosan Medical Association",
          "cited_by_count": 65,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W3087894952",
          "year": 2020,
          "title": "Effects of Non-insulin Anti-hyperglycemic Agents on Gut Microbiota: A Systematic Review on Human and Animal Studies",
          "type": "review",
          "venue": "Frontiers in Endocrinology",
          "cited_by_count": 52,
          "topics": [
            "Gut microbiota and health",
            "Clostridium difficile and Clostridium perfringens research",
            "Diet and metabolism studies"
          ]
        },
        {
          "openalex_id": "W2611087152",
          "year": 2017,
          "title": "Development and validation of a Chinese medication literacy measure",
          "type": "article",
          "venue": "Health Expectations",
          "cited_by_count": 34,
          "topics": [
            "Health Literacy and Information Accessibility",
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W2789896455",
          "year": 2018,
          "title": "EQ-5D-Y for the assessment of health-related quality of life among Taiwanese youth with mild-to-moderate chronic kidney disease",
          "type": "article",
          "venue": "International Journal for Quality in Health Care",
          "cited_by_count": 33,
          "topics": [
            "Dialysis and Renal Disease Management",
            "Adolescent and Pediatric Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2186469139",
          "year": 2015,
          "title": "Changes in medication regimen complexity and the risk for 90-day hospital readmission and/or emergency department visits in U.S. Veterans with heart failure",
          "type": "article",
          "venue": "Research in Social and Administrative Pharmacy",
          "cited_by_count": 28,
          "topics": [
            "Heart Failure Treatment and Management",
            "Pharmaceutical Practices and Patient Outcomes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4322208187",
          "year": 2023,
          "title": "Impacts of medication non-adherence to major modifiable stroke-related diseases on stroke prevention and mortality: a meta-analysis",
          "type": "review",
          "venue": "Journal of Neurology",
          "cited_by_count": 21,
          "topics": [
            "Acute Ischemic Stroke Management",
            "Medication Adherence and Compliance",
            "Atrial Fibrillation Management and Outcomes"
          ]
        }
      ]
    }
  }
]
