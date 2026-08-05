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
    "name": "Sarega Gurudas",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2139-RA",
        "title": "Testing the psychometric properties of the EQ-5D-5L vision bolt-on in a large cross-sectional sample of patients with type 2 diabetes and a control group with no diabetes (SMART India study)",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5067968462",
      "display_name": "Sarega Gurudas",
      "orcid": "0000-0002-2656-0570",
      "reported_affiliation": "Moorfields Eye Hospital NHS Foundation Trust",
      "works_count": 46,
      "top_topics": [
        {
          "topic": "Retinal Diseases and Treatments",
          "works": 41
        },
        {
          "topic": "Retinal Imaging and Analysis",
          "works": 33
        },
        {
          "topic": "Retinal and Optic Conditions",
          "works": 14
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 13
        },
        {
          "topic": "Glaucoma and retinal disorders",
          "works": 9
        },
        {
          "topic": "Ocular Diseases and Behçet’s Syndrome",
          "works": 3
        },
        {
          "topic": "Retinal Development and Disorders",
          "works": 3
        },
        {
          "topic": "Retinopathy of Prematurity Studies",
          "works": 2
        },
        {
          "topic": "Nutritional Studies and Diet",
          "works": 2
        },
        {
          "topic": "Cerebral Venous Sinus Thrombosis",
          "works": 1
        },
        {
          "topic": "Laser Applications in Dentistry and Medicine",
          "works": 1
        },
        {
          "topic": "Ocular Oncology and Treatments",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sobha Sivaprasad",
          "works": 46
        },
        {
          "name": "Shruti Chandra",
          "works": 17
        },
        {
          "name": "Sridevi Thottarath",
          "works": 14
        },
        {
          "name": "Wei-Shan Tsai",
          "works": 11
        },
        {
          "name": "Elizabeth Pearce",
          "works": 8
        },
        {
          "name": "Geeta Menon",
          "works": 8
        },
        {
          "name": "Ian Pearce",
          "works": 8
        },
        {
          "name": "Martin McKibbin",
          "works": 8
        },
        {
          "name": "Ajay Kotagiri",
          "works": 8
        },
        {
          "name": "James Talks",
          "works": 8
        },
        {
          "name": "Anna Grabowska",
          "works": 8
        },
        {
          "name": "Faruque Ghanchi",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7152623367",
          "year": 2026,
          "title": "Nonexudative Macular Neovascularization in Age-Related Macular Degeneration",
          "type": "article",
          "venue": "JAMA Ophthalmology",
          "cited_by_count": 1,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W7163574514",
          "year": 2026,
          "title": "Quantification of retinal non-perfusion in eyes with diabetic retinopathy to study the association with retinal neovascularisation: INSPIRED study report 3",
          "type": "article",
          "venue": "British Journal of Ophthalmology",
          "cited_by_count": 0,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W7167327438",
          "year": 2026,
          "title": "Retinal non-perfusion progression in severe non-proliferative and proliferative diabetic retinopathy over time: INSPIRED study report 2",
          "type": "article",
          "venue": "Eye",
          "cited_by_count": 0,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4415285502",
          "year": 2025,
          "title": "Baseline factors that are associated with change in visual acuity in intermediate AMD over two years in a multicentre cohort study in Europe- INTERCEPT-AMD Report 2",
          "type": "article",
          "venue": "Eye",
          "cited_by_count": 1,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Retinopathy of Prematurity Studies"
          ]
        },
        {
          "openalex_id": "W4415324030",
          "year": 2025,
          "title": "Baseline factors that are associated with change in visual acuity in intermediate AMD over two years in a multicentre cohort study in Europe- INTERCEPT-AMD Report 2",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4408161173",
          "year": 2025,
          "title": "Characterizing the Preferred Retinal Locus and Fixation Stability in Diabetic Macular Ischemia: A One-Year Study",
          "type": "article",
          "venue": "Vision",
          "cited_by_count": 2,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Glaucoma and retinal disorders"
          ]
        },
        {
          "openalex_id": "W2985982097",
          "year": 2019,
          "title": "IDF Diabetes Atlas: A review of studies utilising retinal photography on the global prevalence of diabetes related retinopathy between 2015 and 2018",
          "type": "article",
          "venue": "Diabetes Research and Clinical Practice",
          "cited_by_count": 386,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W3014129418",
          "year": 2020,
          "title": "A Pilot Study Evaluating the Effects of 670 nm Photobiomodulation in Healthy Ageing and Age-Related Macular Degeneration",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 29,
          "topics": [
            "Laser Applications in Dentistry and Medicine",
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W3105052401",
          "year": 2020,
          "title": "Diabetic Retinopathy Environment-Wide Association Study (EWAS) in NHANES 2005–2008",
          "type": "article",
          "venue": "Journal of Clinical Medicine",
          "cited_by_count": 17,
          "topics": [
            "Retinal Imaging and Analysis",
            "Retinal Diseases and Treatments",
            "Nutritional Studies and Diet"
          ]
        },
        {
          "openalex_id": "W3088603622",
          "year": 2020,
          "title": "Diabetic retinopathy environment-wide association study (EWAS) in NHANES 2005-8",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 0,
          "topics": [
            "Nutritional Studies and Diet",
            "Retinal Imaging and Analysis",
            "Health, Environment, Cognitive Aging"
          ]
        },
        {
          "openalex_id": "W3131125541",
          "year": 2021,
          "title": "Predictors of Visual Acuity Outcomes after Anti–Vascular Endothelial Growth Factor Treatment for Macular Edema Secondary to Central Retinal Vein Occlusion",
          "type": "article",
          "venue": "Ophthalmology Retina",
          "cited_by_count": 39,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal and Optic Conditions",
            "Ocular Diseases and Behçet’s Syndrome"
          ]
        },
        {
          "openalex_id": "W4291019187",
          "year": 2022,
          "title": "Characterization of the Structural and Functional Alteration in Eyes with Diabetic Macular Ischemia",
          "type": "article",
          "venue": "Ophthalmology Retina",
          "cited_by_count": 30,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4411635081",
          "year": 2025,
          "title": "IDF diabetes Atlas: A worldwide review of studies utilizing retinal photography to screen for diabetic retinopathy from 2017 to 2024 inclusive",
          "type": "article",
          "venue": "Diabetes Research and Clinical Practice",
          "cited_by_count": 29,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4229002462",
          "year": 2022,
          "title": "Multicenter Evaluation of Diagnostic Circulating Biomarkers to Detect Sight-Threatening Diabetic Retinopathy",
          "type": "article",
          "venue": "JAMA Ophthalmology",
          "cited_by_count": 24,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4392247718",
          "year": 2024,
          "title": "National prevalence of vision impairment and blindness and associated risk factors in adults aged 40 years and older with known or undiagnosed diabetes: results from the SMART-India cross-sectional study",
          "type": "article",
          "venue": "The Lancet Global Health",
          "cited_by_count": 24,
          "topics": [
            "Retinal Diseases and Treatments",
            "Ophthalmology and Visual Impairment Studies",
            "Retinopathy of Prematurity Studies"
          ]
        },
        {
          "openalex_id": "W4205243730",
          "year": 2022,
          "title": "Visual Outcomes Associated With Patterns of Macular Edema Resolution in Central Retinal Vein Occlusion Treated With Anti–Vascular Endothelial Growth Factor Therapy",
          "type": "article",
          "venue": "JAMA Ophthalmology",
          "cited_by_count": 24,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal and Optic Conditions",
            "Cerebral Venous Sinus Thrombosis"
          ]
        }
      ]
    }
  },
  {
    "name": "Sayem Ahmed",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2202-VS",
        "title": "Development of an EQ-5D-5L Value Set for Adult Population in Nepal",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5011474576",
      "display_name": "Sayem Ahmed",
      "orcid": "0000-0001-9499-1500",
      "reported_affiliation": "Department of Health and Social Care",
      "works_count": 227,
      "top_topics": [
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 78
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 69
        },
        {
          "topic": "Global Health and Epidemiology",
          "works": 59
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 32
        },
        {
          "topic": "Global Health Care Issues",
          "works": 24
        },
        {
          "topic": "COVID-19 epidemiological studies",
          "works": 15
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 13
        },
        {
          "topic": "Immune responses and vaccinations",
          "works": 13
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 11
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 9
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 9
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Md. Zahid Hasan",
          "works": 148
        },
        {
          "name": "Gazi Golam Mehdi",
          "works": 135
        },
        {
          "name": "Gatien De Broucker",
          "works": 126
        },
        {
          "name": "Dagna Constenla",
          "works": 126
        },
        {
          "name": "Bryan Patenaude",
          "works": 126
        },
        {
          "name": "Jorge Martin Del Campo",
          "works": 125
        },
        {
          "name": "Md. Jasim Uddin",
          "works": 125
        },
        {
          "name": "Jahangir Khan",
          "works": 43
        },
        {
          "name": "Mohammad Wahid Ahmed",
          "works": 23
        },
        {
          "name": "Marufa Sultana",
          "works": 18
        },
        {
          "name": "Abdur Razzaque Sarker",
          "works": 17
        },
        {
          "name": "Zia Ul Islam",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4409177844",
          "year": 2025,
          "title": "A systematic review of the determinants of job satisfaction in healthcare workers in health facilities in Gulf Cooperation Council countries",
          "type": "review",
          "venue": "Global Health Action",
          "cited_by_count": 19,
          "topics": [
            "Health and Well-being Studies",
            "Job Satisfaction and Organizational Behavior",
            "Occupational Health and Safety Research"
          ]
        },
        {
          "openalex_id": "W4416829930",
          "year": 2025,
          "title": "Cost-Effectiveness of Community-Based Interventions for Hypertension Prevention and Management: A Protocol",
          "type": "article",
          "venue": "Journal of Nepal Medical Association",
          "cited_by_count": 0,
          "topics": [
            "Blood Pressure and Hypertension Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W4415108374",
          "year": 2025,
          "title": "Health related quality of life among the below poverty line population in Bangladesh: A cross-sectional study",
          "type": "article",
          "venue": "PLOS Global Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Chronic Disease Management Strategies",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4406121618",
          "year": 2025,
          "title": "Multimorbidity clusters and their associations with health-related quality of life in two UK cohorts",
          "type": "article",
          "venue": "BMC Medicine",
          "cited_by_count": 26,
          "topics": [
            "Chronic Disease Management Strategies",
            "Primary Care and Health Outcomes",
            "Machine Learning in Healthcare"
          ]
        },
        {
          "openalex_id": "W4413363142",
          "year": 2025,
          "title": "Non-medical costs incurred by critically ill patients with dengue, sepsis and tetanus within a major referral hospital in Southern Vietnam: a cost of illness study",
          "type": "article",
          "venue": "BMJ Public Health",
          "cited_by_count": 0,
          "topics": [
            "Diphtheria, Corynebacterium, and Tetanus",
            "Sepsis Diagnosis and Treatment",
            "Mosquito-borne diseases and control"
          ]
        },
        {
          "openalex_id": "W4414051778",
          "year": 2025,
          "title": "Optimal Site Selection for Wind Energy Power Plant: From Economic Perspectives",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Electric Power System Optimization",
            "Wind Energy Research and Development",
            "Integrated Energy Systems Optimization"
          ]
        },
        {
          "openalex_id": "W2115558868",
          "year": 2013,
          "title": "Cost of behavior change communication channels of Manoshi -a maternal, neonatal and child health (MNCH) program in urban slums of Dhaka, Bangladesh",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 14,
          "topics": [
            "Behavioral Health and Interventions",
            "Health Policy Implementation Science",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2123603106",
          "year": 2013,
          "title": "Food Insecurity and Child Undernutrition: Evidence from BDHS 2011",
          "type": "article",
          "venue": "ENLIGHTEN (Jurnal Bimbingan dan Konseling Islam)",
          "cited_by_count": 25,
          "topics": [
            "Child Nutrition and Water Access",
            "Food Security and Health in Diverse Populations",
            "Poverty, Education, and Child Welfare"
          ]
        },
        {
          "openalex_id": "W2139007023",
          "year": 2013,
          "title": "Impact of educational intervention on willingness-to-pay for health insurance: A study of informal sector workers in urban Bangladesh",
          "type": "article",
          "venue": "Health Economics Review",
          "cited_by_count": 61,
          "topics": [
            "Healthcare Systems and Reforms",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2140721512",
          "year": 2013,
          "title": "Socio-demographic Factors Associated with Home Delivery Assisted by Untrained Traditional Birth Attendant in Rural Bangladesh",
          "type": "article",
          "venue": "American journal of public health research",
          "cited_by_count": 17,
          "topics": [
            "Global Maternal and Child Health",
            "Child Nutrition and Water Access",
            "Global Health and Epidemiology"
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
          "cited_by_count": 500,
          "topics": [
            "Global Maternal and Child Health",
            "Insurance, Mortality, Demography, Risk Management",
            "Demographic Trends and Gender Preferences"
          ]
        },
        {
          "openalex_id": "W2795707819",
          "year": 2018,
          "title": "Tackling socioeconomic inequalities and non-communicable diseases in low-income and middle-income countries under the Sustainable Development agenda",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 405,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Health disparities and outcomes",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2618177743",
          "year": 2017,
          "title": "Catastrophic healthcare expenditure and poverty related to out-of-pocket payments for healthcare in Bangladesh—an estimation of financial risk protection of universal health coverage",
          "type": "article",
          "venue": "Health Policy and Planning",
          "cited_by_count": 205,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W1706865274",
          "year": 2015,
          "title": "Soil salinity, household wealth and food insecurity in tropical deltas: evidence from south-west coast of Bangladesh",
          "type": "article",
          "venue": "Sustainability Science",
          "cited_by_count": 165,
          "topics": [
            "Child Nutrition and Water Access",
            "Food Security and Health in Diverse Populations",
            "Climate change impacts on agriculture"
          ]
        },
        {
          "openalex_id": "W2271241286",
          "year": 2016,
          "title": "Willingness-to-Pay for Community-Based Health Insurance among Informal Workers in Urban Bangladesh",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 152,
          "topics": [
            "Healthcare Systems and Reforms",
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        }
      ]
    }
  },
  {
    "name": "Seungjin Bae",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2510-VS",
        "title": "Developing a National Value Set for the EQ-5D-Y-3L Instrument in South Korea: A Discrete Choice Experiment and Composite Time Trade-Off Study",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5038405248",
      "display_name": "SeungJin Bae",
      "orcid": "0000-0002-8993-8884",
      "reported_affiliation": "Ewha Womans University",
      "works_count": 117,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 38
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 34
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 16
        },
        {
          "topic": "Animal testing and alternatives",
          "works": 14
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 11
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 8
        },
        {
          "topic": "Immunotoxicology and immune responses",
          "works": 8
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 6
        },
        {
          "topic": "Biomedical Ethics and Regulation",
          "works": 5
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 5
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 5
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kyung‐Min Lim",
          "works": 23
        },
        {
          "name": "Gyeongseon Shin",
          "works": 14
        },
        {
          "name": "Donghwan Lee",
          "works": 12
        },
        {
          "name": "Kyung‐Bok Son",
          "works": 11
        },
        {
          "name": "Hye-Young Kwon",
          "works": 10
        },
        {
          "name": "Gyeyoung Choi",
          "works": 9
        },
        {
          "name": "Dong‐Sook Kim",
          "works": 7
        },
        {
          "name": "Do Yeun Kim",
          "works": 7
        },
        {
          "name": "Won-Hee Jang",
          "works": 6
        },
        {
          "name": "Green Bae",
          "works": 6
        },
        {
          "name": "Hyerim Ha",
          "works": 6
        },
        {
          "name": "Mi-Sook Jung",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167459430",
          "year": 2026,
          "title": "Analysis of Aerospace Research Trends Using Social Network Analysis: Focusing on the Structure of the International Collaborative Research Ecosystem and Industrial Impacts",
          "type": "article",
          "venue": "Journal of Korea Research Association of International Commerce",
          "cited_by_count": 0,
          "topics": [
            "Diverse Approaches in Healthcare and Education Studies",
            "Technology and Data Analysis",
            "Educational Systems and Policies"
          ]
        },
        {
          "openalex_id": "W7122803479",
          "year": 2026,
          "title": "Analysis of predictive value of animal repeated dose toxicity study results for clinical safety of US FDA-approved anticancer drugs between 2019 and 2023",
          "type": "article",
          "venue": "Regulatory Toxicology and Pharmacology",
          "cited_by_count": 1,
          "topics": [
            "Animal testing and alternatives",
            "Immunotoxicology and immune responses",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W7143539981",
          "year": 2026,
          "title": "Artificial Intelligence as a Tool in Health Economic Evaluation: A Systematic Review of Implementation, Performance, and Reporting Quality (2016-2025)",
          "type": "review",
          "venue": "Drug Targets and Therapeutics",
          "cited_by_count": 0,
          "topics": [
            "Artificial Intelligence in Healthcare and Education",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Impact of AI and Big Data on Business and Society"
          ]
        },
        {
          "openalex_id": "W7162761778",
          "year": 2026,
          "title": "FDA first to global follow-on: alignment in expedited oncology approvals across EMA, TGA, and PMDA",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical Ethics and Regulation",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W7163065390",
          "year": 2026,
          "title": "Framework for identifying reference countries in drug safety evaluation: an application of the analytic hierarchy process",
          "type": "article",
          "venue": "Journal of Pharmaceutical Policy and Practice",
          "cited_by_count": 0,
          "topics": [
            "History and advancements in chemistry",
            "Pharmacovigilance and Adverse Drug Reactions",
            "Qualitative Comparative Analysis Research"
          ]
        },
        {
          "openalex_id": "W4412851850",
          "year": 2025,
          "title": "A New Prediction Model for Waitlist Survival in Kidney Transplant Candidates",
          "type": "article",
          "venue": "American Journal of Transplantation",
          "cited_by_count": 0,
          "topics": [
            "Renal Transplantation Outcomes and Treatments"
          ]
        },
        {
          "openalex_id": "W2137334142",
          "year": 2006,
          "title": "Cost-effectiveness of inhaled steroids in asthma: Impact of effect on bone mineral density",
          "type": "article",
          "venue": "Journal of Allergy and Clinical Immunology",
          "cited_by_count": 22,
          "topics": [
            "Asthma and respiratory diseases",
            "Vitamin D Research Studies",
            "Inhalation and Respiratory Drug Delivery"
          ]
        },
        {
          "openalex_id": "W2013610393",
          "year": 2007,
          "title": "Modeling the Potential Impact of a Prescription Drug Copayment Increase on the Adult Asthmatic Medicaid Population",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 6,
          "topics": [
            "Medication Adherence and Compliance",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1969566866",
          "year": 2007,
          "title": "Porin loss and GES-type extended-spectrum β-lactamase primarily responsible for reduced susceptibility to imipenem",
          "type": "article",
          "venue": "Diagnostic Microbiology and Infectious Disease",
          "cited_by_count": 1,
          "topics": [
            "Antibiotic Resistance in Bacteria",
            "Clostridium difficile and Clostridium perfringens research",
            "Antibiotics Pharmacokinetics and Efficacy"
          ]
        },
        {
          "openalex_id": "W2042233299",
          "year": 2008,
          "title": "Patients with Multiple Chronic Conditions Do Not Receive Lower Quality of Preventive Care",
          "type": "article",
          "venue": "Journal of General Internal Medicine",
          "cited_by_count": 37,
          "topics": [
            "Chronic Disease Management Strategies",
            "Diabetes Management and Education",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W1969685778",
          "year": 2014,
          "title": "KeraSkin™-VM: A novel reconstructed human epidermis model for skin irritation tests",
          "type": "article",
          "venue": "Toxicology in Vitro",
          "cited_by_count": 79,
          "topics": [
            "Animal testing and alternatives",
            "Advancements in Transdermal Drug Delivery"
          ]
        },
        {
          "openalex_id": "W4297477916",
          "year": 2022,
          "title": "Price and Prejudice? The Value of Chimeric Antigen Receptor (CAR) T-Cell Therapy",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 79,
          "topics": [
            "CAR-T cell therapy research",
            "Integrated Circuits and Semiconductor Failure Analysis",
            "Advancements in Semiconductor Devices and Circuit Design"
          ]
        },
        {
          "openalex_id": "W3128444525",
          "year": 2021,
          "title": "Potential approaches for the pricing of cancer medicines across Europe to enhance the sustainability of healthcare systems and the implications",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 74,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1999055527",
          "year": 2012,
          "title": "Health-Care Data Collecting, Sharing, and Using in Thailand, China Mainland, South Korea, Taiwan, Japan, and Malaysia",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 67,
          "topics": [
            "Healthcare Systems and Reforms",
            "Healthcare Policy and Management",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W1951958475",
          "year": 2011,
          "title": "Prevalence of gastroesophageal reflux disease in Korea and associated health‐care utilization: A national population‐based study",
          "type": "article",
          "venue": "Journal of Gastroenterology and Hepatology",
          "cited_by_count": 67,
          "topics": [
            "Gastroesophageal reflux and treatments",
            "Helicobacter pylori-related gastroenterology studies",
            "Gastrointestinal motility and disorders"
          ]
        },
        {
          "openalex_id": "W2036246967",
          "year": 2012,
          "title": "Incidence and Short-term Mortality From Perforated Peptic Ulcer in Korea: A Population-Based Study",
          "type": "article",
          "venue": "Journal of Epidemiology",
          "cited_by_count": 63,
          "topics": [
            "Helicobacter pylori-related gastroenterology studies",
            "Gastrointestinal Bleeding Diagnosis and Treatment",
            "Gallbladder and Bile Duct Disorders"
          ]
        },
        {
          "openalex_id": "W2146615831",
          "year": 2014,
          "title": "Relationship of ceramide–, and free fatty acid–cholesterol ratios in the stratum corneum with skin barrier function of normal, atopic dermatitis lesional and non-lesional skins",
          "type": "article",
          "venue": "Journal of Dermatological Science",
          "cited_by_count": 59,
          "topics": [
            "Dermatology and Skin Diseases",
            "Advancements in Transdermal Drug Delivery",
            "Contact Dermatitis and Allergies"
          ]
        },
        {
          "openalex_id": "W3041239362",
          "year": 2020,
          "title": "Uptake of Biosimilar Infliximab in the UK, France, Japan, and Korea: Budget Savings or Market Expansion Across Countries?",
          "type": "article",
          "venue": "Frontiers in Pharmacology",
          "cited_by_count": 56,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Pharmaceutical Economics and Policy",
            "Monoclonal and Polyclonal Antibodies Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Shankar Prinja",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20170520",
        "title": "Development of health-related quality of life (EQ-5D-5L) value set for India",
        "working_group": "Valuation"
      },
      {
        "project_id": "2033-RA",
        "title": "Comparison of ‘DCE with duration’ and ‘EQ-VT’ to inform development of EQ-5D-Y-5L value-set in India: A pilot study",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2220-VS",
        "title": "Development of EQ-5D-Y-5L value-set for India",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5071690494",
      "display_name": "Shankar Prinja",
      "orcid": "0000-0001-7719-6986",
      "reported_affiliation": "Post Graduate Institute of Medical Education and Research",
      "works_count": 324,
      "top_topics": [
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 114
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 79
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 63
        },
        {
          "topic": "Global Health Care Issues",
          "works": 30
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 26
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 25
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 20
        },
        {
          "topic": "Child Nutrition and Water Access",
          "works": 17
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 16
        },
        {
          "topic": "Global Health and Epidemiology",
          "works": 16
        },
        {
          "topic": "Social and Economic Development in India",
          "works": 14
        },
        {
          "topic": "Trauma and Emergency Care Studies",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Pankaj Bahuguna",
          "works": 63
        },
        {
          "name": "Rajesh Kumar",
          "works": 43
        },
        {
          "name": "Gaurav Jyani",
          "works": 34
        },
        {
          "name": "Nidhi Gupta",
          "works": 34
        },
        {
          "name": "Akashdeep Singh Chauhan",
          "works": 33
        },
        {
          "name": "Atul Sharma",
          "works": 30
        },
        {
          "name": "Manmeet Kaur",
          "works": 26
        },
        {
          "name": "Arun Kumar Aggarwal",
          "works": 22
        },
        {
          "name": "Ramesh Verma",
          "works": 22
        },
        {
          "name": "Yashika Chugh",
          "works": 22
        },
        {
          "name": "Aarti Goyal",
          "works": 18
        },
        {
          "name": "Kavitha Rajsekar",
          "works": 18
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7139105735",
          "year": 2026,
          "title": "Comparison of utility measures and auditory performance in children with cochlear implants and hearing aids in India: a cross-sectional study",
          "type": "article",
          "venue": "Brazilian Journal of Otorhinolaryngology",
          "cited_by_count": 0,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Hearing Impairment and Communication",
            "Hearing, Cochlea, Tinnitus, Genetics"
          ]
        },
        {
          "openalex_id": "W7164207605",
          "year": 2026,
          "title": "Factors influencing the Implementation of Eat Right Campus Policy in a Tertiary Health Care setting in Chandigarh: A Scoping Review",
          "type": "article",
          "venue": "Indian Journal of Preventive & Social Medicine",
          "cited_by_count": 0,
          "topics": [
            "Obesity and Health Practices",
            "Obesity, Physical Activity, Diet",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W7161047488",
          "year": 2026,
          "title": "Health and economic impact of universal screening and management of alcohol use disorders in India: An economic modelling study",
          "type": "article",
          "venue": "Addiction",
          "cited_by_count": 0,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Alcoholism and Thiamine Deficiency"
          ]
        },
        {
          "openalex_id": "W7166165117",
          "year": 2026,
          "title": "PCR41 ESTABLISHING VALIDITY AND DEVELOPING A PREDICTOR TOOL FOR ESTIMATION OF WILLINGNESS TO PAY BASED THRESHOLD FOR INDIA",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Scientific and Engineering Research Topics",
            "Identification and Quantification in Food",
            "Forensic and Genetic Research"
          ]
        },
        {
          "openalex_id": "W4416781122",
          "year": 2025,
          "title": "174MO A randomized trial to assess impact of teleconsultation on understanding, satisfaction and compliance of patients with lung cancer",
          "type": "article",
          "venue": "ESMO Real World Data and Digital Oncology",
          "cited_by_count": 0,
          "topics": [
            "Telemedicine and Telehealth Implementation",
            "Healthcare Systems and Technology",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W4414039282",
          "year": 2025,
          "title": "A Mixed-Methods Assessment of India’s Health Technology Assessment Ecosystem",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Quality and Safety in Healthcare"
          ]
        },
        {
          "openalex_id": "W2738916833",
          "year": 2006,
          "title": "Handbook of supply management at first-level health care facilities. 1st version for country adaptation.",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 25,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical studies and practices",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2033898248",
          "year": 2006,
          "title": "Producing quality doctors: The dilemma of internship",
          "type": "article",
          "venue": "Indian Journal of Community Medicine",
          "cited_by_count": 1,
          "topics": [
            "Innovations in Medical Education",
            "Dental Education, Practice, Research",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W1999835733",
          "year": 2007,
          "title": "Over reporting of RCH services coverage and operational problems in health management information system at the sub-center level",
          "type": "article",
          "venue": "Indian Journal of Community Medicine",
          "cited_by_count": 7,
          "topics": [
            "Global Maternal and Child Health",
            "Healthcare Systems and Reforms",
            "Child Nutrition and Water Access"
          ]
        },
        {
          "openalex_id": "W2054800271",
          "year": 2007,
          "title": "Quality of records for maternal and child health services at subcentre level in a rural block of Rohtak",
          "type": "article",
          "venue": "Indian Journal of Community Medicine",
          "cited_by_count": 1,
          "topics": [
            "Healthcare Systems and Reforms",
            "Medical Coding and Health Information"
          ]
        },
        {
          "openalex_id": "W2735211001",
          "year": 2017,
          "title": "Community health workers for non-communicable diseases prevention and control in developing countries: Evidence and implications",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 297,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Diabetes Management and Education",
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W2585592226",
          "year": 2017,
          "title": "Impact of Publicly Financed Health Insurance Schemes on Healthcare Utilization and Financial Risk Protection in India: A Systematic Review",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 258,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2921942266",
          "year": 2019,
          "title": "The Ayushman Bharat Pradhan Mantri Jan Arogya Yojana and the path to universal health coverage in India: Overcoming the challenges of stewardship and governance",
          "type": "article",
          "venue": "PLoS Medicine",
          "cited_by_count": 160,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2127368965",
          "year": 2011,
          "title": "Social and Economic Implications of Noncommunicable diseases in India",
          "type": "article",
          "venue": "Indian Journal of Community Medicine",
          "cited_by_count": 140,
          "topics": [
            "Global Public Health Policies and Epidemiology",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4205139067",
          "year": 2022,
          "title": "Development of an EQ-5D Value Set for India Using an Extended Design (DEVINE) Study: The Indian 5-Level Version EQ-5D Value Set",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 131,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W2911560900",
          "year": 2019,
          "title": "Role of insurance in determining utilization of healthcare and financial risk protection in India",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 128,
          "topics": [
            "Healthcare Systems and Reforms",
            "Agricultural risk and resilience",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2268578454",
          "year": 2015,
          "title": "Availability of medicines in public sector health facilities of two North Indian States",
          "type": "article",
          "venue": "BMC Pharmacology and Toxicology",
          "cited_by_count": 123,
          "topics": [
            "Pharmaceutical Economics and Policy",
            "Pharmaceutical Quality and Counterfeiting",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W3118599774",
          "year": 2021,
          "title": "National Healthcare Economic Evaluation Guidelines: A Cross-Country Comparison",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 115,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        }
      ]
    }
  },
  {
    "name": "Shitong Xie",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2209-RA",
        "title": "Understanding the transitions and measurement properties of the EQ-5D-Y-3L, EQ-5D-Y-5L, and EQ-5D-5L among adolescents aged 12-18 in China",
        "working_group": "Youth"
      },
      {
        "project_id": "2211-RA",
        "title": "Exploring the use of the EQ-5D-Y-5L for assessing mental health of children and adolescents aged 10-18 years in China",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5113241600",
      "display_name": "Shitong Xie",
      "orcid": "",
      "reported_affiliation": "Tianjin University of Science and Technology",
      "works_count": 61,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 30
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 12
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 6
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 4
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 4
        },
        {
          "topic": "BRCA gene mutations in cancer",
          "works": 4
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 4
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 3
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 3
        },
        {
          "topic": "Acute Ischemic Stroke Management",
          "works": 3
        },
        {
          "topic": "Acute Myeloid Leukemia Research",
          "works": 3
        },
        {
          "topic": "Hemophilia Treatment and Research",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jing Wu",
          "works": 36
        },
        {
          "name": "Feng Xie",
          "works": 14
        },
        {
          "name": "Xiaoning He",
          "works": 12
        },
        {
          "name": "Tianqi Hong",
          "works": 10
        },
        {
          "name": "Meixuan Li",
          "works": 9
        },
        {
          "name": "Chang Luo",
          "works": 9
        },
        {
          "name": "Qi Wang",
          "works": 7
        },
        {
          "name": "Gang Chen",
          "works": 6
        },
        {
          "name": "Liang Yao",
          "works": 5
        },
        {
          "name": "Kehu Yang",
          "works": 5
        },
        {
          "name": "John Brazier",
          "works": 4
        },
        {
          "name": "Dingyao Wang",
          "works": 4
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7163644005",
          "year": 2026,
          "title": "Health-related quality of life and its associated factors among patients with neuromyelitis optica spectrum disorder in China: a questionnaire survey analysis",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Multiple Sclerosis Research Studies",
            "Ophthalmology and Visual Impairment Studies",
            "Systemic Sclerosis and Related Diseases"
          ]
        },
        {
          "openalex_id": "W7166115181",
          "year": 2026,
          "title": "RWD11 FRACTURE INCIDENCE AND ECONOMIC BURDEN OF FEMALE PATIENTS WITH OSTEOPOROSIS AT VERY HIGH RISK OF FRACTURE IN CHINA",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Bone fractures and treatments",
            "Bone health and osteoporosis research",
            "Hip and Femur Fractures"
          ]
        },
        {
          "openalex_id": "W7134826507",
          "year": 2026,
          "title": "Reply to \"Cost-of-illness of myelodysplastic syndromes in Italy. A reply to Tse et al.\"",
          "type": "letter",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4415903823",
          "year": 2025,
          "title": "Are there differences in health state preferences between urban and rural respondents? a comparison using time trade-off and discrete choice experiment",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4414083854",
          "year": 2025,
          "title": "Burden of Myelodysplastic Syndromes: A Literature Review of Epidemiological and Humanistic Aspects",
          "type": "article",
          "venue": "Journal of Evidence-Based Medicine",
          "cited_by_count": 1,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Histone Deacetylase Inhibitors Research",
            "Bone and Joint Diseases"
          ]
        },
        {
          "openalex_id": "W4409729565",
          "year": 2025,
          "title": "Burden of myelodysplastic syndromes: a systematic literature review of economic burden",
          "type": "review",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W3083534711",
          "year": 2020,
          "title": "Do Discrete Choice Experiments Approaches Perform Better Than Time Trade-Off in Eliciting Health State Utilities? Evidence From SF-6Dv2 in China",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 36,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4285724657",
          "year": 2020,
          "title": "Short Form Six-Dimension--Version 2; Simplified Chinese Version",
          "type": "dataset",
          "venue": "PsycTESTS Dataset",
          "cited_by_count": 0,
          "topics": [
            "Advanced Materials and Mechanics",
            "Liquid Crystal Research Advancements",
            "Block Copolymer Self-Assembly"
          ]
        },
        {
          "openalex_id": "W2999708247",
          "year": 2020,
          "title": "The Simplified Chinese version of SF-6Dv2: translation, cross-cultural adaptation and preliminary psychometric testing",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 33,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health Literacy and Information Accessibility",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W3133186034",
          "year": 2021,
          "title": "Valuation of SF-6Dv2 Health States in China Using Time Trade-off and Discrete-Choice Experiment with a Duration Dimension",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 83,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4210844996",
          "year": 2022,
          "title": "Population Norms for SF-6Dv2 and EQ-5D-5L in China",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4282971310",
          "year": 2022,
          "title": "Comparison of the measurement properties of SF-6Dv2 and EQ-5D-5L in a Chinese population health survey",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 53,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Heart Failure Treatment and Management"
          ]
        },
        {
          "openalex_id": "W4321782440",
          "year": 2023,
          "title": "Canada population norms for the EQ-5D-5L",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 43,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "BRCA gene mutations in cancer",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4318450151",
          "year": 2023,
          "title": "Comparative performance and mapping algorithms between EQ-5D-5L and SF-6Dv2 among the Chinese general population",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 24,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Parkinson's Disease Mechanisms and Treatments"
          ]
        },
        {
          "openalex_id": "W4392466737",
          "year": 2024,
          "title": "Understanding Canadian stakeholders’ views on measuring and valuing health for children and adolescents: a qualitative study",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 23,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Ophthalmology and Visual Impairment Studies"
          ]
        }
      ]
    }
  }
]
