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
    "name": "Rachel Tan",
    "member_affiliation": "IQVIA",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5047279366",
      "display_name": "Rachel Lee-Yin Tan",
      "orcid": "0000-0002-4610-1195",
      "reported_affiliation": "",
      "works_count": 37,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 20
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 3
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 3
        },
        {
          "topic": "Immune Cell Function and Interaction",
          "works": 3
        },
        {
          "topic": "Immune cells in cancer",
          "works": 3
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Asthma and respiratory diseases",
          "works": 3
        },
        {
          "topic": "Consumer Retail Behavior Studies",
          "works": 2
        },
        {
          "topic": "Consumer Behavior in Brand Consumption and Identification",
          "works": 2
        },
        {
          "topic": "Customer Service Quality and Loyalty",
          "works": 2
        },
        {
          "topic": "Healthcare Quality and Management",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Nan Luo",
          "works": 20
        },
        {
          "name": "Michael Herdman",
          "works": 9
        },
        {
          "name": "Weidong Huang",
          "works": 5
        },
        {
          "name": "Le Ann Chen",
          "works": 4
        },
        {
          "name": "Bo Liu",
          "works": 3
        },
        {
          "name": "Juan Xu",
          "works": 3
        },
        {
          "name": "Mihir Gandhi",
          "works": 3
        },
        {
          "name": "Sherry Thornton",
          "works": 3
        },
        {
          "name": "Thuy Do",
          "works": 3
        },
        {
          "name": "Alexei A. Grom",
          "works": 3
        },
        {
          "name": "Grant S. Schulert",
          "works": 3
        },
        {
          "name": "Jian Yi Soh",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7154425299",
          "year": 2026,
          "title": "Real World Evidence on Perceived Effectiveness, Quality of Life Impact, and Public Attitudes Toward a Common Cold and Flu Medication: A Cross-Sectional Study",
          "type": "preprint",
          "venue": "Preprints.org",
          "cited_by_count": 0,
          "topics": [
            "Respiratory and Cough-Related Research",
            "Antibiotic Use and Resistance",
            "Asthma and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W4409280353",
          "year": 2025,
          "title": "308. Personalized Transcranial Magnetic Stimulation Treatment for Depression – An Open Label Clinical Trial",
          "type": "article",
          "venue": "Biological Psychiatry",
          "cited_by_count": 0,
          "topics": [
            "Transcranial Magnetic Stimulation Studies",
            "Pain Management and Treatment"
          ]
        },
        {
          "openalex_id": "W4413001612",
          "year": 2025,
          "title": "A Head-to-Head Comparison of the Psychometric Properties of the EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Children Aged 8 to 18 Years With Eczema",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1,
          "topics": [
            "Dermatology and Skin Diseases",
            "Psoriasis: Treatment and Pathogenesis",
            "Body Image and Dysmorphia Studies"
          ]
        },
        {
          "openalex_id": "W4414090964",
          "year": 2025,
          "title": "A Head-to-Head Comparison of the Psychometric Properties of the EQ-5D-Y-3L, EQ-5D-Y-5L, and CHU9D in Children With Asthma",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Asthma and respiratory diseases",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4406877736",
          "year": 2025,
          "title": "A Real-World Study on the Quality of Life of Consumers with Dentine Hypersensitivity and the Benefits of Hypersensitivity Toothpaste Use",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 4,
          "topics": [
            "Dental Erosion and Treatment"
          ]
        },
        {
          "openalex_id": "W4412555489",
          "year": 2025,
          "title": "Assessing the Health-Related Quality of Life of Children With Asthma or Eczema by a Proxy: Does Assessment Perspective Matter?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Dermatology and Skin Diseases",
            "Asthma and respiratory diseases",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2156770791",
          "year": 2000,
          "title": "The moderating role of target-arousal on the impact of affect on satisfaction—an examination in the context of service experiences",
          "type": "article",
          "venue": "Journal of Retailing",
          "cited_by_count": 315,
          "topics": [
            "Consumer Retail Behavior Studies",
            "Consumer Behavior in Brand Consumption and Identification",
            "Customer Service Quality and Loyalty"
          ]
        },
        {
          "openalex_id": "W2061703741",
          "year": 2007,
          "title": "The role of arousal congruency in influencing consumers' satisfaction evaluations and in‐store behaviors",
          "type": "article",
          "venue": "International Journal of Service Industry Management",
          "cited_by_count": 94,
          "topics": [
            "Consumer Retail Behavior Studies",
            "Customer Service Quality and Loyalty",
            "Consumer Behavior in Brand Consumption and Identification"
          ]
        },
        {
          "openalex_id": "W2345937383",
          "year": 2011,
          "title": "Sharing plates : cooking and coping with cancer.",
          "type": "report",
          "venue": "DR-NTU (Nanyang Technological University)",
          "cited_by_count": 0,
          "topics": [
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2553845950",
          "year": 2016,
          "title": "OP0012 Microrna Associated with Active Systemic Juvenile Idiopathic Arthritis Regulate CD163 Expression in Polarized Macrophages through Two Distinct Mechanisms",
          "type": "conference-abstract",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 0,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Immune cells in cancer",
            "Immune Cell Function and Interaction"
          ]
        },
        {
          "openalex_id": "W3158966385",
          "year": 2021,
          "title": "Measurement Properties of the EQ VAS Around the Globe: A Systematic Review and Meta-Regression Analysis",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 107,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Reliability and Agreement in Measurement"
          ]
        },
        {
          "openalex_id": "W3096773086",
          "year": 2020,
          "title": "Measurement Properties of the EQ-5D-5L and EQ-5D-3L in Six Commonly Diagnosed Cancers",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer Treatment and Pharmacology",
            "Cancer survivorship and care"
          ]
        },
        {
          "openalex_id": "W2997211912",
          "year": 2020,
          "title": "A vision ‘bolt-on’ increases the responsiveness of EQ-5D: preliminary evidence from a study of cataract surgery",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 37,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ocular Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W2991311329",
          "year": 2019,
          "title": "Measurement Properties of Commonly Used Generic Preference-Based Measures in East and South-East Asia: A Systematic Review",
          "type": "review",
          "venue": "PharmacoEconomics",
          "cited_by_count": 35,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W3087183392",
          "year": 2020,
          "title": "How Do Respondents Interpret and View the EQ-VAS? A Qualitative Study of Three Asian Populations",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 33,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Behavioral Health and Interventions"
          ]
        },
        {
          "openalex_id": "W2911304279",
          "year": 2019,
          "title": "A Multiparameter Flow Cytometry Analysis Panel to Assess CD163 mRNA and Protein in Monocyte and Macrophage Populations in Hyperinflammatory Diseases",
          "type": "article",
          "venue": "The Journal of Immunology",
          "cited_by_count": 27,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Immune Cell Function and Interaction",
            "Immune cells in cancer"
          ]
        }
      ]
    }
  },
  {
    "name": "Rainer Reile",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1960-RA",
        "title": "EQ-5D and population disability profiles in Estonia: patterns of inequality and its implications for disability-free life expectancy",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "1987-SG",
        "title": "Health-related quality of life among Ukrainian war refugees in Estonia: A comparative analysis with the general population using EQ-5D-3L",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2569-RA",
        "title": "Reporting heterogeneity in EQ-5D-5L: Sociodemographic and cognitive drivers and their impact for population health measurement",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2621-VS",
        "title": "Development of an Estonian EQ-5D-5L Value Set Using Discrete Choice Experiment with Duration ",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5036883637",
      "display_name": "Rainer Reile",
      "orcid": "0000-0001-9488-887X",
      "reported_affiliation": "National Institute for Health Development",
      "works_count": 59,
      "top_topics": [
        {
          "topic": "Health disparities and outcomes",
          "works": 18
        },
        {
          "topic": "Substance Abuse Treatment and Outcomes",
          "works": 14
        },
        {
          "topic": "Alcohol Consumption and Health Effects",
          "works": 13
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 9
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 8
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 6
        },
        {
          "topic": "Obesity, Physical Activity, Diet",
          "works": 6
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 5
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 4
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 4
        },
        {
          "topic": "Physical Activity and Health",
          "works": 3
        },
        {
          "topic": "Global Health Care Issues",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Mall Leinsalu",
          "works": 17
        },
        {
          "name": "Jürgen Rehm",
          "works": 12
        },
        {
          "name": "Huan Jiang",
          "works": 10
        },
        {
          "name": "Mindaugas Štelemėkas",
          "works": 10
        },
        {
          "name": "Shannon Lange",
          "works": 9
        },
        {
          "name": "Alexander Tran",
          "works": 9
        },
        {
          "name": "Inese Gobiņa",
          "works": 8
        },
        {
          "name": "Janina Petkevičienė",
          "works": 8
        },
        {
          "name": "Laura Miščikienė",
          "works": 7
        },
        {
          "name": "Relika Stoppel",
          "works": 7
        },
        {
          "name": "Kinga Janik‐Koncewicz",
          "works": 6
        },
        {
          "name": "Ričardas Radišauskas",
          "works": 6
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7168122963",
          "year": 2026,
          "title": "Economic cost of excess body weight among adults in Estonia",
          "type": "article",
          "venue": "Central European Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Obesity, Physical Activity, Diet",
            "Obesity and Health Practices",
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W7169785586",
          "year": 2026,
          "title": "Global, regional, and national burden of road injuries 1990–2023: a systematic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "The Lancet Public Health",
          "cited_by_count": 0,
          "topics": [
            "Traffic and Road Safety",
            "Trauma and Emergency Care Studies",
            "Injury Epidemiology and Prevention"
          ]
        },
        {
          "openalex_id": "W7128071457",
          "year": 2026,
          "title": "Health-Related Quality of Life Among Ukrainian War Refugees Compared to the General Population in Estonia",
          "type": "article",
          "venue": "International Journal of Public Health",
          "cited_by_count": 1,
          "topics": [
            "Migration, Health and Trauma",
            "Posttraumatic Stress Disorder Research",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W7161954143",
          "year": 2026,
          "title": "Updated trends in the global prevalence and burden of mental disorders, 1990–2023: a systematic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 12,
          "topics": [
            "Mental Health Treatment and Access",
            "Bipolar Disorder and Treatment",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W7120120859",
          "year": 2026,
          "title": "Using a return on investment analysis to estimate the economic impact of potential changes to alcohol control policies in Estonia",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 1,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W4414695919",
          "year": 2025,
          "title": "Age verification in alcohol online sales and delivery: results from a mystery shopping study in Estonia",
          "type": "article",
          "venue": "Public Health in Practice",
          "cited_by_count": 0,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Consumer Market Behavior and Pricing",
            "Smoking Behavior and Cessation"
          ]
        },
        {
          "openalex_id": "W2034336541",
          "year": 2013,
          "title": "Differentiating positive and negative self-rated health: results from a cross-sectional study in Estonia",
          "type": "article",
          "venue": "International Journal of Public Health",
          "cited_by_count": 23,
          "topics": [
            "Psychological Well-being and Life Satisfaction",
            "Optimism, Hope, and Well-being",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W2181712290",
          "year": 2014,
          "title": "Naiste teadlikkus emakakaelavähki ennetavatest meetmetest Eestis 2011. aastal",
          "type": "article",
          "venue": "Ajakirjad. Journals by UT",
          "cited_by_count": 0,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Viral-associated cancers and disorders",
            "Herpesvirus Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W1991411303",
          "year": 2014,
          "title": "The prevalence of genital warts in the Baltic countries: findings from national cross-sectional surveys in Estonia, Latvia and Lithuania",
          "type": "article",
          "venue": "Sexually Transmitted Infections",
          "cited_by_count": 9,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Reproductive tract infections research",
            "Genital Health and Disease"
          ]
        },
        {
          "openalex_id": "W2170189795",
          "year": 2014,
          "title": "The recent economic recession and self-rated health in Estonia, Lithuania and Finland: a comparative cross-sectional study in 2004–2010",
          "type": "article",
          "venue": "Journal of Epidemiology & Community Health",
          "cited_by_count": 34,
          "topics": [
            "Employment and Welfare Studies",
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W4415092555",
          "year": 2025,
          "title": "Global burden of 292 causes of death in 204 countries and territories and 660 subnational locations, 1990–2023: a systematic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 341,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Autopsy Techniques and Outcomes",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4415092550",
          "year": 2025,
          "title": "Global age-sex-specific all-cause mortality and life expectancy estimates for 204 countries and territories and 660 subnational locations, 1950–2023: a demographic analysis for the Global Burden of Disease Study 2023",
          "type": "article",
          "venue": "The Lancet",
          "cited_by_count": 126,
          "topics": [
            "Insurance, Mortality, Demography, Risk Management",
            "Global Maternal and Child Health",
            "Maternal and Neonatal Healthcare"
          ]
        },
        {
          "openalex_id": "W4386333270",
          "year": 2023,
          "title": "Impact of the WHO \"best buys\" for alcohol policy on consumption and health in the Baltic countries and Poland 2000–2020",
          "type": "article",
          "venue": "The Lancet Regional Health - Europe",
          "cited_by_count": 50,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W4310777143",
          "year": 2022,
          "title": "Classifying alcohol control policies enacted between 2000 and 2020 in Poland and the Baltic countries to model potential impact",
          "type": "article",
          "venue": "Addiction",
          "cited_by_count": 34,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W2574979354",
          "year": 2017,
          "title": "Large variation in predictors of mortality by levels of self-rated health: Results from an 18-year follow-up study",
          "type": "article",
          "venue": "Public Health",
          "cited_by_count": 34,
          "topics": [
            "Health disparities and outcomes",
            "Employment and Welfare Studies",
            "Physical Activity and Health"
          ]
        },
        {
          "openalex_id": "W4308071894",
          "year": 2022,
          "title": "Do alcohol control policies have the predicted effects on consumption? An analysis of the Baltic countries and Poland 2000–2020",
          "type": "article",
          "venue": "Drug and Alcohol Dependence",
          "cited_by_count": 28,
          "topics": [
            "Substance Abuse Treatment and Outcomes",
            "Alcohol Consumption and Health Effects",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W4366269342",
          "year": 2023,
          "title": "Alcohol control policies reduce all-cause mortality in Baltic Countries and Poland between 2001 and 2020",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 26,
          "topics": [
            "Employment and Welfare Studies",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        }
      ]
    }
  },
  {
    "name": "Rebecca Addo",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1899-RA",
        "title": "An EQ-5D multilayered measure of HRQoL: what are the perspectives of key stakeholders?",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5005424373",
      "display_name": "Rebecca Addo",
      "orcid": "0000-0002-5970-1122",
      "reported_affiliation": "University of Technology Sydney",
      "works_count": 29,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 13
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 4
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 4
        },
        {
          "topic": "Global Health Care Issues",
          "works": 4
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 3
        },
        {
          "topic": "Family Caregiving in Mental Illness",
          "works": 2
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 2
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 2
        },
        {
          "topic": "Innovation Policy and R&D",
          "works": 2
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Justice Nonvignon",
          "works": 10
        },
        {
          "name": "Stephen Goodall",
          "works": 8
        },
        {
          "name": "Marion Haas",
          "works": 6
        },
        {
          "name": "Jane Hall",
          "works": 5
        },
        {
          "name": "Brendan Mulhern",
          "works": 4
        },
        {
          "name": "Philip Haywood",
          "works": 3
        },
        {
          "name": "Samuel Agyei Agyemang",
          "works": 2
        },
        {
          "name": "Chris Sampson",
          "works": 2
        },
        {
          "name": "Richard Norman",
          "works": 2
        },
        {
          "name": "Richmond Owusu",
          "works": 2
        },
        {
          "name": "Rosalie Viney",
          "works": 2
        },
        {
          "name": "Huihui Wang",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411380466",
          "year": 2025,
          "title": "\"It is better for me to die than to be disgraced”: Perceptions of Worse than death health states in Ghana",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health and Conflict Studies",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4413131103",
          "year": 2025,
          "title": "Herbal Medicine Use among Pregnant Women in Rural Ghana: Implications for Maternal Health and Healthcare Integration",
          "type": "article",
          "venue": "Journal of Complementary and Alternative Medical Research",
          "cited_by_count": 0,
          "topics": [
            "Complementary and Alternative Medicine Studies"
          ]
        },
        {
          "openalex_id": "W4408690389",
          "year": 2025,
          "title": "Perspectives of School Health Education Program (SHEP) Coordinators on School Absenteeism Among Adolescent Schoolgirls in the Tamale Metropolis, Ghana: A Qualitative Study",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Youth Substance Use and School Attendance"
          ]
        },
        {
          "openalex_id": "W4415730612",
          "year": 2025,
          "title": "RWD49 AN EQ-5D MULTILAYERED MEASURE OF HEALTH-RELATED QUALITY OF LIFE: IS THERE RELEVANCE AND NEED FOR IT?",
          "type": "conference-abstract",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health and Wellbeing Research"
          ]
        },
        {
          "openalex_id": "W4402232684",
          "year": 2024,
          "title": "An EQ-5D-5L Value Set for Ghana Using an Adapted EuroQol Valuation Technology Protocol",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 5,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4406147638",
          "year": 2024,
          "title": "OD04 The EQ-5D-5L Value Set For Ghana",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 0,
          "topics": [
            "Construction Project Management and Performance"
          ]
        },
        {
          "openalex_id": "W2346578708",
          "year": 2013,
          "title": "Household costs of mental health care in Ghana.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 18,
          "topics": [
            "Mental Health Treatment and Access",
            "Family Caregiving in Mental Illness",
            "Schizophrenia research and treatment"
          ]
        },
        {
          "openalex_id": "W2149828426",
          "year": 2014,
          "title": "An Exploratory Study of Financial Management Practices Among Ghanaian Households",
          "type": "article",
          "venue": "International Journal of Management and Sustainability",
          "cited_by_count": 5,
          "topics": [
            "Financial Literacy, Pension, Retirement Analysis",
            "Housing Market and Economics",
            "Microfinance and Financial Inclusion"
          ]
        },
        {
          "openalex_id": "W2259597151",
          "year": 2016,
          "title": "Do leadership styles influence productivity?",
          "type": "article",
          "venue": "British Journal of Healthcare Management",
          "cited_by_count": 12,
          "topics": [
            "Nursing education and management",
            "Global Maternal and Child Health",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2600637952",
          "year": 2017,
          "title": "Learning a practice through practise: presenting knowledge in doctoral spoken presentations",
          "type": "article",
          "venue": "Studies in Continuing Education",
          "cited_by_count": 13,
          "topics": [
            "Reflective Practices in Education",
            "Innovative Education and Learning Practices",
            "Evaluation of Teaching Practices"
          ]
        },
        {
          "openalex_id": "W2886333327",
          "year": 2018,
          "title": "Economic burden of caregiving for persons with severe mental illness in sub-Saharan Africa: A systematic review",
          "type": "review",
          "venue": "PLoS ONE",
          "cited_by_count": 138,
          "topics": [
            "Family Caregiving in Mental Illness",
            "Schizophrenia research and treatment",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W4225135404",
          "year": 2022,
          "title": "Criteria for developing, assessing and selecting candidate EQ-5D bolt-ons",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 37,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W3007523113",
          "year": 2020,
          "title": "The knowledge and attitude of Ghanaian decision-makers and researchers towards health technology assessment",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 18,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W3121048549",
          "year": 2020,
          "title": "Costs, burden and quality of life associated with informal caregiving for children with Lymphoma attending a tertiary hospital in Ghana",
          "type": "article",
          "venue": "International Journal of Care Pathways",
          "cited_by_count": 14,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Family Support in Illness",
            "Acute Lymphoblastic Leukemia research"
          ]
        },
        {
          "openalex_id": "W3088035549",
          "year": 2020,
          "title": "Assessing the capacity of Ghana to introduce health technology assessment: a systematic review of economic evaluations conducted in Ghana",
          "type": "review",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 13,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare Systems and Reforms"
          ]
        }
      ]
    }
  },
  {
    "name": "Richard Brooks",
    "member_affiliation": "Retirement Association",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5112107099",
      "display_name": "Richard Brooks",
      "orcid": "",
      "reported_affiliation": "Guiyang Medical University",
      "works_count": 66,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 18
        },
        {
          "topic": "Regional Development and Policy",
          "works": 8
        },
        {
          "topic": "Global Health Care Issues",
          "works": 5
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 4
        },
        {
          "topic": "German Economic Analysis & Policies",
          "works": 4
        },
        {
          "topic": "Global Financial Crisis and Policies",
          "works": 4
        },
        {
          "topic": "Health Promotion and Cardiovascular Prevention",
          "works": 3
        },
        {
          "topic": "European Political History Analysis",
          "works": 3
        },
        {
          "topic": "European history and politics",
          "works": 3
        },
        {
          "topic": "European and International Contract Law",
          "works": 3
        },
        {
          "topic": "Migration, Aging, and Tourism Studies",
          "works": 3
        },
        {
          "topic": "demographic modeling and climate adaptation",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jim Love",
          "works": 15
        },
        {
          "name": "Brian Ashcroft",
          "works": 15
        },
        {
          "name": "Paul Draper",
          "works": 15
        },
        {
          "name": "Stewart Dunlop",
          "works": 15
        },
        {
          "name": "Cliff Lockyer",
          "works": 15
        },
        {
          "name": "Eleanor Malloy",
          "works": 15
        },
        {
          "name": "Eric McRory",
          "works": 14
        },
        {
          "name": "Peter McGregor",
          "works": 13
        },
        {
          "name": "Jim Stevens",
          "works": 13
        },
        {
          "name": "Kim Swales",
          "works": 13
        },
        {
          "name": "Iain McNicoll",
          "works": 12
        },
        {
          "name": "Roger Perman",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W3217165750",
          "year": 2021,
          "title": "The remarkably frequent use of EQ-5D in non-economic research",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W3137074628",
          "year": 2020,
          "title": "Business Person and Movement Lawyer",
          "type": "conference-paper",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "European and International Contract Law",
            "Conflict of Laws and Jurisdiction",
            "Comparative and International Law Studies"
          ]
        },
        {
          "openalex_id": "W3038290679",
          "year": 2020,
          "title": "EQ-5D: a plea for accurate nomenclature",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 109,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2587851012",
          "year": 2017,
          "title": "EQ-5D and the EuroQol Group: Past, Present and Future",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 1223,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2181610062",
          "year": 2017,
          "title": "The Right to Associate and the Rights of Associations: Civil-Society Organizations in Prussia, 1794–1908",
          "type": "article",
          "venue": "NBER Chapters",
          "cited_by_count": 3,
          "topics": [
            "European Political History Analysis",
            "European history and politics"
          ]
        },
        {
          "openalex_id": "W3121408998",
          "year": 2017,
          "title": "The Right to Associate and the Rights of Associations: Civil-Society Organizations in Prussia, 1794–1908",
          "type": "preprint",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 2,
          "topics": [
            "European Political History Analysis",
            "European history and politics"
          ]
        },
        {
          "openalex_id": "W2081006182",
          "year": 1964,
          "title": "A Neighborhood Social-Legal Program",
          "type": "article",
          "venue": "Social Service Review",
          "cited_by_count": 0,
          "topics": [
            "Crime Patterns and Interventions",
            "Urban, Neighborhood, and Segregation Studies"
          ]
        },
        {
          "openalex_id": "W2323866389",
          "year": 1969,
          "title": "The Meaning of 'Real' in Advaita Vedanta",
          "type": "article",
          "venue": "Philosophy East and West",
          "cited_by_count": 4,
          "topics": [
            "Indian and Buddhist Studies"
          ]
        },
        {
          "openalex_id": "W2163374566",
          "year": 1971,
          "title": "Social Planning in Columbia",
          "type": "article",
          "venue": "Journal of the American Institute of Planners",
          "cited_by_count": 3,
          "topics": [
            "Community Development and Social Impact"
          ]
        },
        {
          "openalex_id": "W2140273415",
          "year": 1973,
          "title": "A Source Book of Advaita Vedanta",
          "type": "article",
          "venue": "Philosophy East and West",
          "cited_by_count": 28,
          "topics": [
            "Indian and Buddhist Studies",
            "Indian History and Philosophy"
          ]
        },
        {
          "openalex_id": "W2071686284",
          "year": 1996,
          "title": "EuroQol: the current state of play",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 5913,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W572189123",
          "year": 2003,
          "title": "The measurement and valuation of health status using EQ-5D : a European perspective : evidence from the EuroQol BIOMED Research Programme",
          "type": "article",
          "venue": "",
          "cited_by_count": 241,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Innovation Policy and R&D"
          ]
        },
        {
          "openalex_id": "W2060699469",
          "year": 1991,
          "title": "EuroQol©: health-related quality of life measurement. Results of the Swedish questionnaire exercise",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 204,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W595308902",
          "year": 1995,
          "title": "Health Status Measurement: A Perspective on Change",
          "type": "book",
          "venue": "",
          "cited_by_count": 47,
          "topics": [
            "Health Promotion and Cardiovascular Prevention"
          ]
        },
        {
          "openalex_id": "W584862694",
          "year": 2012,
          "title": "The EuroQol Group after 25 years",
          "type": "book",
          "venue": "",
          "cited_by_count": 45,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Richard Norman",
    "member_affiliation": "Curtin University",
    "is_member": true,
    "projects": [
      {
        "project_id": "1578-RA",
        "title": "Redundancy in HRQoL algorithms: conceptual and empirical challenges",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015310",
        "title": "The impact of duration on EQ‐5D‐5L value sets derived from a Discrete Choice Experiment",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016250",
        "title": "The relationship between the EQ-5D and surgical outcomes in a large Australian registry of percutaneous intervention patients",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170410",
        "title": "Comparing the EQ-5D-3L and EQ-5D-5L in a cohort of cancer patients",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20170560",
        "title": "Framing effects when valuing EQ-5D-Y health states in a latent scale DCE",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "83-VS",
        "title": "An Australian Value Set for the EQ-5D-Y",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5101841802",
      "display_name": "Richard Norman",
      "orcid": "0000-0002-3112-3893",
      "reported_affiliation": "Curtin University",
      "works_count": 466,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 164
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 101
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 39
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 29
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 18
        },
        {
          "topic": "Global Health Care Issues",
          "works": 18
        },
        {
          "topic": "Telemedicine and Telehealth Implementation",
          "works": 18
        },
        {
          "topic": "Lipoproteins and Cardiovascular Health",
          "works": 15
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 14
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 14
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 14
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 14
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Rosalie Viney",
          "works": 70
        },
        {
          "name": "Madeleine King",
          "works": 53
        },
        {
          "name": "Brendan Mulhern",
          "works": 34
        },
        {
          "name": "Suzanne Robinson",
          "works": 32
        },
        {
          "name": "Georg Kemmler",
          "works": 28
        },
        {
          "name": "John Brazier",
          "works": 25
        },
        {
          "name": "Deborah J. Street",
          "works": 24
        },
        {
          "name": "Eva‐Maria Gamper",
          "works": 21
        },
        {
          "name": "Nancy Devlin",
          "works": 20
        },
        {
          "name": "Daniel Costa",
          "works": 19
        },
        {
          "name": "A. Simon Pickard",
          "works": 19
        },
        {
          "name": "Donna Rowen",
          "works": 19
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7165804290",
          "year": 2026,
          "title": "Barriers and facilitators to sexual and reproductive health services among adolescents and young adults in Sidama region, Ethiopia: a qualitative study",
          "type": "article",
          "venue": "Reproductive Health",
          "cited_by_count": 0,
          "topics": [
            "Adolescent Sexual and Reproductive Health",
            "Global Maternal and Child Health",
            "HIV/AIDS Research and Interventions"
          ]
        },
        {
          "openalex_id": "W7133959279",
          "year": 2026,
          "title": "COVID-19 pandemic perceived impacts on the Australian general population, a national survey exploring the role of socio-demographic and psychological factors",
          "type": "article",
          "venue": "Scientific Reports",
          "cited_by_count": 0,
          "topics": [
            "COVID-19 and Mental Health",
            "COVID-19 epidemiological studies",
            "Vaccine Coverage and Hesitancy"
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
          "openalex_id": "W4408992809",
          "year": 2025,
          "title": "A comparison of health-related quality of life using the World Health Organization Quality of Life–BREF and 5-Level EuroQol-5 Dimensions in the Malaysian population",
          "type": "article",
          "venue": "Osong Public Health and Research Perspectives",
          "cited_by_count": 4,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4415746872",
          "year": 2025,
          "title": "A qualitative study to understand public views on the relative value of health gains for children and young people in Australia compared to adults",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "demographic modeling and climate adaptation"
          ]
        },
        {
          "openalex_id": "W4412856348",
          "year": 2025,
          "title": "Acceptability, feasibility, and program outcomes of an equity-focused, adapted community-based healthy lifestyle program for children, young people, and their families in Perth, Western Australia: an implementation hybrid research protocol",
          "type": "article",
          "venue": "Frontiers in Health Services",
          "cited_by_count": 2,
          "topics": [
            "Health Policy Implementation Science",
            "Community Health and Development",
            "Obesity, Physical Activity, Diet"
          ]
        },
        {
          "openalex_id": "W4243958298",
          "year": 1973,
          "title": "IX.—NEW BOOKS",
          "type": "article",
          "venue": "Mind",
          "cited_by_count": 0,
          "topics": [
            "Philosophical Ethics and Theory",
            "Philosophy and Historical Thought",
            "Globalization, Historical Perspectives, and International Relations"
          ]
        },
        {
          "openalex_id": "W4244541057",
          "year": 1977,
          "title": "BOOK REVIEWS",
          "type": "book-review",
          "venue": "Mind",
          "cited_by_count": 0,
          "topics": [
            "Free Will and Agency",
            "Philosophy and Theoretical Science",
            "Legal principles and applications"
          ]
        },
        {
          "openalex_id": "W3210876172",
          "year": 1978,
          "title": "Registration of Vona wheat",
          "type": "article",
          "venue": "Crop Science",
          "cited_by_count": 6,
          "topics": [
            "Wheat and Barley Genetics and Pathology",
            "Genetics and Plant Breeding",
            "Plant pathogens and resistance mechanisms"
          ]
        },
        {
          "openalex_id": "W2038167694",
          "year": 1978,
          "title": "Some Animals are More Equal Than Others",
          "type": "article",
          "venue": "Philosophy",
          "cited_by_count": 104,
          "topics": [
            "Environmental Philosophy and Ethics",
            "Philosophical Ethics and Theory",
            "Political Philosophy and Ethics"
          ]
        },
        {
          "openalex_id": "W2129114099",
          "year": 2009,
          "title": "Caring for Aged Dementia Care Resident Study (CADRES) of person-centred care, dementia-care mapping, and usual care in dementia: a cluster-randomised trial",
          "type": "article",
          "venue": "The Lancet Neurology",
          "cited_by_count": 535,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W1558112948",
          "year": 2009,
          "title": "How far does screening women for domestic (partner) violence in different health-care settings meet the UK National Screening Committee criteria for a screening programme? Systematic reviews of nine UK National Screening Committee criteria",
          "type": "article",
          "venue": "Health Technology Assessment",
          "cited_by_count": 334,
          "topics": [
            "Intimate Partner and Family Violence",
            "Elder Abuse and Neglect",
            "Workplace Violence and Bullying"
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
          "openalex_id": "W2025330974",
          "year": 2013,
          "title": "A Pilot Discrete Choice Experiment to Explore Preferences for EQ-5D-5L Health States",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 211,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2091799436",
          "year": 1996,
          "title": "A common major histocompatibility complex class II allele HLA-DQB1* 0301 is present in clinical variants of pemphigoid.",
          "type": "article",
          "venue": "Proceedings of the National Academy of Sciences",
          "cited_by_count": 209,
          "topics": [
            "Autoimmune Bullous Skin Diseases",
            "Urticaria and Related Conditions",
            "Coagulation, Bradykinin, Polyphosphates, and Angioedema"
          ]
        },
        {
          "openalex_id": "W2041731719",
          "year": 2009,
          "title": "International Comparisons in Valuing EQ-5D Health States: A Review and Analysis",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 176,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W4318624517",
          "year": 2023,
          "title": "The Use of a Discrete Choice Experiment Including Both Duration and Dead for the Development of an EQ-5D-5L Value Set for Australia",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 163,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W2527943338",
          "year": 2016,
          "title": "Estimating Health-State Utility for Economic Models in Clinical Studies: An ISPOR Good Research Practices Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 161,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Global Health Care Issues"
          ]
        }
      ]
    }
  }
]
