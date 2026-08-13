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
    "name": "Eleanor Pullenayegum",
    "member_affiliation": "The Hospital for Sick Children",
    "is_member": true,
    "projects": [
      {
        "project_id": "109-RA",
        "title": "Improving predictive precision in valuation studies using non-parametric techniques",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015130",
        "title": "Evaluating consistency between DCE and TTO valuations using multivariate mixed models and multivariate latent class analysis",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015140",
        "title": "Valuation of the EQ-5D in countries with limited research resources: investigating the potential of shrinkage analysis",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190270",
        "title": "Modelling dependence in EQ-VT DCE data: impact on value sets",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190430",
        "title": "Efficient designs for valuation studies that use DCEs with mapping to TTO health states",
        "working_group": "Valuation"
      },
      {
        "project_id": "2340-RA",
        "title": "Parametric survival models for the analysis of cTTO data: accommodating asymmetry, heteroscedasticity, heterogeneity and censoring.",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5029465719",
      "display_name": "Eleanor Pullenayegum",
      "orcid": "0000-0003-4265-1330",
      "reported_affiliation": "University of Toronto",
      "works_count": 323,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 71
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 33
        },
        {
          "topic": "Advanced Causal Inference Techniques",
          "works": 25
        },
        {
          "topic": "Statistical Methods in Clinical Trials",
          "works": 20
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 17
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 16
        },
        {
          "topic": "Statistical Methods and Bayesian Inference",
          "works": 16
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 15
        },
        {
          "topic": "Meta-analysis and systematic reviews",
          "works": 14
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 12
        },
        {
          "topic": "Statistical Methods and Inference",
          "works": 12
        },
        {
          "topic": "Influenza Virus Research Studies",
          "works": 11
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Feng Xie",
          "works": 42
        },
        {
          "name": "Brian M. Feldman",
          "works": 31
        },
        {
          "name": "Sarah D. McDonald",
          "works": 20
        },
        {
          "name": "Ron Goeree",
          "works": 18
        },
        {
          "name": "Lehana Thabane",
          "works": 18
        },
        {
          "name": "Mark Loeb",
          "works": 16
        },
        {
          "name": "Patricia C. Parkin",
          "works": 16
        },
        {
          "name": "Catherine S. Birken",
          "works": 16
        },
        {
          "name": "Petros Pechlivanoglou",
          "works": 15
        },
        {
          "name": "Jean‐Éric Tarride",
          "works": 14
        },
        {
          "name": "Prakesh S. Shah",
          "works": 14
        },
        {
          "name": "Jonathon L. Maguire",
          "works": 13
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4416246483",
          "year": 2026,
          "title": "Inverse‐Intensity‐Weighted Generalized Estimating Equations With Irregularly Measured Longitudinal Data and Informative Dropout",
          "type": "article",
          "venue": "Statistics in Medicine",
          "cited_by_count": 0,
          "topics": [
            "Advanced Causal Inference Techniques",
            "Statistical Methods and Bayesian Inference",
            "COVID-19 epidemiological studies"
          ]
        },
        {
          "openalex_id": "W4416205149",
          "year": 2025,
          "title": "A randomised controlled trial comparing epinephrine and dexamethasone to placebo in the treatment of infants with bronchiolitis (BIPED study): a statistical analysis plan",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 0,
          "topics": [
            "Respiratory viral infections research",
            "Neonatal Respiratory Health Research",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W4406962765",
          "year": 2025,
          "title": "Abstract TMP89: Predictive Model of Ischemic Event Recurrence in Pediatric Moyamoya",
          "type": "conference-abstract",
          "venue": "Stroke",
          "cited_by_count": 0,
          "topics": [
            "Moyamoya disease diagnosis and treatment",
            "Mitochondrial Function and Pathology",
            "Connective tissue disorders research"
          ]
        },
        {
          "openalex_id": "W4414168152",
          "year": 2025,
          "title": "Abundance of <i>Bifidobacterium</i> species in the infant gut microbiota and associations with maternal-infant characteristics in Dhaka, Bangladesh",
          "type": "article",
          "venue": "mSphere",
          "cited_by_count": 2,
          "topics": [
            "Gut microbiota and health",
            "Infant Health and Development",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W4408230263",
          "year": 2025,
          "title": "Abundance of <i>Bifidobacterium</i> species in the infant gut microbiota and associations with maternal-infant characteristics in Dhaka, Bangladesh",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 1,
          "topics": [
            "Gut microbiota and health",
            "Child Nutrition and Water Access",
            "Pediatric health and respiratory diseases"
          ]
        },
        {
          "openalex_id": "W4417297824",
          "year": 2025,
          "title": "Association of systemic corticosteroids and clinical outcomes in children hospitalised with severe orbital infections",
          "type": "article",
          "venue": "BMJ Paediatrics Open",
          "cited_by_count": 2,
          "topics": [
            "Sinusitis and nasal conditions",
            "Ocular Diseases and Behçet’s Syndrome",
            "Nasolacrimal Duct Obstruction Treatments"
          ]
        },
        {
          "openalex_id": "W7132937214",
          "year": 2005,
          "title": "Semi-parametric models for cost-effectiveness analysis: Improving the efficiency of estimation from censored data",
          "type": "dissertation",
          "venue": "TSpace (University of Toronto)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials",
            "Statistical Methods and Bayesian Inference"
          ]
        },
        {
          "openalex_id": "W2084273456",
          "year": 2006,
          "title": "Economic Evaluation of Rivastigmine in Patients with Parkinson??s Disease Dementia",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 17,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Parkinson's Disease and Spinal Disorders",
            "Amyotrophic Lateral Sclerosis Research"
          ]
        },
        {
          "openalex_id": "W1976527790",
          "year": 2007,
          "title": "Long-Term DHEA Replacement in Primary Adrenal Insufficiency: A Randomized, Controlled Trial",
          "type": "article",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 188,
          "topics": [
            "Hormonal and reproductive studies",
            "Sexual Differentiation and Disorders",
            "Adrenal Hormones and Disorders"
          ]
        },
        {
          "openalex_id": "W2079566573",
          "year": 2007,
          "title": "Semi‐parametric regression models for cost‐effectiveness analysis: improving the efficiency of estimation from censored data",
          "type": "article",
          "venue": "Statistics in Medicine",
          "cited_by_count": 11,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Statistical Methods in Clinical Trials"
          ]
        },
        {
          "openalex_id": "W1974404062",
          "year": 2010,
          "title": "Higher vs Lower Positive End-Expiratory Pressure in Patients With Acute Lung Injury and Acute Respiratory Distress Syndrome",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 1472,
          "topics": [
            "Respiratory Support and Mechanisms",
            "Sepsis Diagnosis and Treatment",
            "Nosocomial Infections in ICU"
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
          "openalex_id": "W2945409099",
          "year": 2019,
          "title": "United States Valuation of EQ-5D-5L Health States Using an International Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 399,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2012117258",
          "year": 2010,
          "title": "The Effect of Oral Antidiabetic Agents on A1C Levels",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 324,
          "topics": [
            "Diabetes Treatment and Management",
            "Natural Antidiabetic Agents Studies",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2038304191",
          "year": 2010,
          "title": "Potentiating Cancer Immunotherapy Using an Oncolytic Virus",
          "type": "article",
          "venue": "Molecular Therapy",
          "cited_by_count": 176,
          "topics": [
            "Virus-based gene therapy research",
            "CAR-T cell therapy research",
            "Cancer Research and Treatments"
          ]
        },
        {
          "openalex_id": "W2109517979",
          "year": 2010,
          "title": "Analysis of Health Utility Data When Some Subjects Attain the Upper Bound of 1: Are Tobit and CLAD Models Appropriate?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 165,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2508934593",
          "year": 2016,
          "title": "Impact of including or excluding both-armed zero-event studies on using standard meta-analysis methods for rare event outcome: a simulation study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 163,
          "topics": [
            "Meta-analysis and systematic reviews",
            "Statistical Methods in Clinical Trials",
            "Statistical Methods and Bayesian Inference"
          ]
        }
      ]
    }
  },
  {
    "name": "Elena Olariu",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180030R1",
        "title": "Measuring Quality of Life in the general population in Romania: an EQ5D-5L value set and population norms for Romania (QoLRO",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5018887750",
      "display_name": "Elena Olariu",
      "orcid": "0000-0002-8718-5516",
      "reported_affiliation": "Matia Fundazioa",
      "works_count": 33,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 9
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 6
        },
        {
          "topic": "Sepsis Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
          "works": 3
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Treatment of Major Depression",
          "works": 3
        },
        {
          "topic": "Advanced Neuroimaging Techniques and Applications",
          "works": 3
        },
        {
          "topic": "Advanced MRI Techniques and Applications",
          "works": 3
        },
        {
          "topic": "Adrenal Hormones and Disorders",
          "works": 2
        },
        {
          "topic": "Psychosomatic Disorders and Their Treatments",
          "works": 2
        },
        {
          "topic": "Clinical practice guidelines implementation",
          "works": 2
        },
        {
          "topic": "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jordi Alonso",
          "works": 8
        },
        {
          "name": "Carlos G. Forero",
          "works": 7
        },
        {
          "name": "José Ignacio Castro-Rodríguez",
          "works": 7
        },
        {
          "name": "Yemi Oluboyede",
          "works": 7
        },
        {
          "name": "Ileana Gabriela Niculescu-Aron",
          "works": 6
        },
        {
          "name": "Marian Sorin Paveliu",
          "works": 6
        },
        {
          "name": "Luke Vale",
          "works": 6
        },
        {
          "name": "Raluca Căplescu",
          "works": 5
        },
        {
          "name": "Pilar Álvarez",
          "works": 4
        },
        {
          "name": "Luis Miguel Martín‐Lopez",
          "works": 4
        },
        {
          "name": "Gemma Vilagut",
          "works": 4
        },
        {
          "name": "María Jesús Blasco",
          "works": 3
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4412606559",
          "year": 2025,
          "title": "Análisis de las tendencias de mortalidad por enfermedad cerebrovascular en Colombia de 2010 a 2021",
          "type": "article",
          "venue": "Enfermería Global",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Health and Mental Health",
            "Public Health and Social Inequalities",
            "Health and Lifestyle Studies"
          ]
        },
        {
          "openalex_id": "W4403816232",
          "year": 2024,
          "title": "Youth mental health and exposome",
          "type": "article",
          "venue": "European Journal of Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health, Environment, Cognitive Aging"
          ]
        },
        {
          "openalex_id": "W4385839499",
          "year": 2023,
          "title": "Acute onset of Lambert Eaton myasthenic syndrome in prostate adenocarcinoma: a case report",
          "type": "article",
          "venue": "Medicine and Pharmacy Reports",
          "cited_by_count": 0,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Autoimmune Neurological Disorders and Treatments",
            "Peripheral Neuropathies and Disorders"
          ]
        },
        {
          "openalex_id": "W4385332025",
          "year": 2023,
          "title": "Population norms for the EQ-5D-3L and EQ-5D-5L in Romania",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 10,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Statistical Methods in Clinical Trials",
            "BRCA gene mutations in cancer"
          ]
        },
        {
          "openalex_id": "W4312190561",
          "year": 2022,
          "title": "Differences in health-related quality of life between the Roma community and the general population in Romania",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 9,
          "topics": [
            "Romani and Gypsy Studies",
            "Forensic Anthropology and Bioarchaeology Studies",
            "Genital Health and Disease"
          ]
        },
        {
          "openalex_id": "W4281712830",
          "year": 2022,
          "title": "EQ-5D-5L: a value set for Romania",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 32,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Clinical practice guidelines implementation"
          ]
        },
        {
          "openalex_id": "W4238967595",
          "year": 2003,
          "title": "Monte Carlo studies of the magnetic resonance diffusion decay",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 1,
          "topics": [
            "NMR spectroscopy and applications"
          ]
        },
        {
          "openalex_id": "W2182776794",
          "year": 2009,
          "title": "Analysis of water diffusion in white matter using a hydration layer model",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Advanced Neuroimaging Techniques and Applications",
            "NMR spectroscopy and applications",
            "Advanced MRI Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W1970921286",
          "year": 2009,
          "title": "SU‐FF‐I‐123: Clinical Value of Diffusion‐Weighted MRI in White Matter in Vivo",
          "type": "article",
          "venue": "Medical Physics",
          "cited_by_count": 0,
          "topics": [
            "Advanced Neuroimaging Techniques and Applications",
            "MRI in cancer diagnosis",
            "Advanced MRI Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2089677963",
          "year": 2009,
          "title": "Sci-Fri AM(1): Imaging-07: Biexponential Characterization of Diffusion in Brain Tumor",
          "type": "article",
          "venue": "Medical Physics",
          "cited_by_count": 1,
          "topics": [
            "Advanced Neuroimaging Techniques and Applications",
            "MRI in cancer diagnosis",
            "Advanced MRI Techniques and Applications"
          ]
        },
        {
          "openalex_id": "W2947375759",
          "year": 2019,
          "title": "Frequency and mortality of septic shock in Europe and North America: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Critical Care",
          "cited_by_count": 527,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Adrenal Hormones and Disorders",
            "Immune Response and Inflammation"
          ]
        },
        {
          "openalex_id": "W2168214213",
          "year": 2015,
          "title": "DETECTION OF ANXIETY DISORDERS IN PRIMARY CARE: A META-ANALYSIS OF ASSISTED AND UNASSISTED DIAGNOSES",
          "type": "review",
          "venue": "Depression and Anxiety",
          "cited_by_count": 80,
          "topics": [
            "Mental Health Treatment and Access",
            "Anxiety, Depression, Psychometrics, Treatment, Cognitive Processes",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W2795417993",
          "year": 2018,
          "title": "A systematic scoping review on the consequences of stress-related hyperglycaemia",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 62,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Adrenal Hormones and Disorders",
            "Sepsis Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W1784469430",
          "year": 2015,
          "title": "Testing the PROMIS ® Depression measures for monitoring depression in a clinical sample outside the US",
          "type": "article",
          "venue": "Journal of Psychiatric Research",
          "cited_by_count": 39,
          "topics": [
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Mental Health Treatment and Access",
            "Child and Adolescent Psychosocial and Emotional Development"
          ]
        },
        {
          "openalex_id": "W2753175606",
          "year": 2017,
          "title": "Current recommendations on the estimation of transition probabilities in Markov cohort models for use in health care decision-making: a targeted literature review",
          "type": "article",
          "venue": "ClinicoEconomics and Outcomes Research",
          "cited_by_count": 36,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2023998066",
          "year": 2014,
          "title": "Diagnostic accuracy and adequacy of treatment of depressive and anxiety disorders: A comparison of primary care and specialized care patients",
          "type": "article",
          "venue": "Journal of Affective Disorders",
          "cited_by_count": 29,
          "topics": [
            "Mental Health Treatment and Access",
            "Treatment of Major Depression",
            "Cardiac Health and Mental Health"
          ]
        },
        {
          "openalex_id": "W2969439539",
          "year": 2019,
          "title": "Measuring health-related quality of life in the general population and Roma communities in Romania: study protocol for two cross-sectional studies",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 24,
          "topics": [
            "Romani and Gypsy Studies",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Ethics in Clinical Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Eliza Wong",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180750",
        "title": "Developing a value set for the child-friendly EQ-5D Health-related Quality of Life instrument EQ-5D-Y in Hong Kong",
        "working_group": "Valuation, Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033480820",
      "display_name": "Eliza Lai‐Yi Wong",
      "orcid": "0000-0001-9983-6219",
      "reported_affiliation": "Department of Health",
      "works_count": 373,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 39
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 27
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 27
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 27
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 25
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 25
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 21
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 20
        },
        {
          "topic": "Heart Failure Treatment and Management",
          "works": 20
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 19
        },
        {
          "topic": "Health Literacy and Information Accessibility",
          "works": 18
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 15
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Eng‐Kiong Yeoh",
          "works": 150
        },
        {
          "name": "Annie Wai-Ling Cheung",
          "works": 69
        },
        {
          "name": "Richard Huan Xu",
          "works": 50
        },
        {
          "name": "Samuel Yeung Shan Wong",
          "works": 49
        },
        {
          "name": "Dong Dong",
          "works": 35
        },
        {
          "name": "Kailu Wang",
          "works": 30
        },
        {
          "name": "Annie Wai Ling Cheung",
          "works": 22
        },
        {
          "name": "Patsy Y. K. Chau",
          "works": 21
        },
        {
          "name": "Vincent CH Chung",
          "works": 21
        },
        {
          "name": "Benjamin Hon Kei Yip",
          "works": 21
        },
        {
          "name": "Roger Yat‐Nork Chung",
          "works": 18
        },
        {
          "name": "Crystal Ying Chan",
          "works": 18
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7162681960",
          "year": 2026,
          "title": "Beyond the Flames: Public Health Management and Policy Implications From the Wang Fuk Court Fire Disaster in Hong Kong",
          "type": "article",
          "venue": "International Journal of Health Policy and Management",
          "cited_by_count": 0,
          "topics": [
            "Disaster Response and Management",
            "Disaster Management and Resilience",
            "Nursing Education, Practice, and Leadership"
          ]
        },
        {
          "openalex_id": "W7167017727",
          "year": 2026,
          "title": "Housing precarity and mental health among shoebox house residents in Hong Kong: latent profile analysis of perceived social support and its associations with loneliness, depression, anxiety and stress",
          "type": "article",
          "venue": "BMJ Public Health",
          "cited_by_count": 0,
          "topics": [
            "Health disparities and outcomes",
            "Intergenerational Family Dynamics and Caregiving",
            "Employment and Welfare Studies"
          ]
        },
        {
          "openalex_id": "W7166508908",
          "year": 2026,
          "title": "Operationalizing Digital Health Equity in Artificial Intelligence–Enabled Patient Decision Aids for Older Adults: Mixed Methods Study",
          "type": "article",
          "venue": "Journal of Medical Internet Research",
          "cited_by_count": 0,
          "topics": [
            "Artificial Intelligence in Healthcare and Education",
            "Ethics and Social Impacts of AI",
            "Digital Mental Health Interventions"
          ]
        },
        {
          "openalex_id": "W4411995662",
          "year": 2025,
          "title": "A proactive approach to prevent non-communicable diseases through screening and educating emergency department attendees to adopt healthy lifestyles: Study protocol for a pragmatic, multicenter, randomized controlled trial",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 0,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Behavioral Health and Interventions",
            "Cardiac Health and Mental Health"
          ]
        },
        {
          "openalex_id": "W4406080411",
          "year": 2025,
          "title": "Association of ambient temperature with social isolation among the community-dwelling Chinese older adults: A cross-sectional study in Hong Kong",
          "type": "article",
          "venue": "Heliyon",
          "cited_by_count": 2,
          "topics": [
            "Climate Change and Health Impacts",
            "Health disparities and outcomes",
            "Thermal Regulation in Medicine"
          ]
        },
        {
          "openalex_id": "W4409840998",
          "year": 2025,
          "title": "Author response for \"Barriers and Facilitators to Implementing a Nurse‐Led Information System for Older Adult Patients' Post‐Discharge Self‐Care: An Exploratory Sequential Mixed‐Methods Study\"",
          "type": "peer-review",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Telemedicine and Telehealth Implementation"
          ]
        },
        {
          "openalex_id": "W2403409331",
          "year": 1987,
          "title": "Platelet activating factor in chronic plaque psoriasis.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Psoriasis: Treatment and Pathogenesis",
            "Mast cells and histamine"
          ]
        },
        {
          "openalex_id": "W2243298611",
          "year": 1998,
          "title": "A survey of chronic rhinitis in Hong Kong",
          "type": "conference-paper",
          "venue": "The HKU Scholars Hub (University of Hong Kong)",
          "cited_by_count": 0,
          "topics": [
            "Noise Effects and Management"
          ]
        },
        {
          "openalex_id": "W2034753101",
          "year": 1998,
          "title": "Effect of nimodipine on memory after cerebral infarction",
          "type": "article",
          "venue": "Acta Neurologica Scandinavica",
          "cited_by_count": 31,
          "topics": [
            "Stroke Rehabilitation and Recovery",
            "Dementia and Cognitive Impairment Research",
            "Spatial Neglect and Hemispheric Dysfunction"
          ]
        },
        {
          "openalex_id": "W2113601697",
          "year": 1999,
          "title": "Combined spinal–epidural analgesia in labour: comparison of two doses of intrathecal bupivacaine with fentanyl",
          "type": "article",
          "venue": "British Journal of Anaesthesia",
          "cited_by_count": 38,
          "topics": [
            "Anesthesia and Pain Management",
            "Nausea and vomiting management",
            "Spine and Intervertebral Disc Pathology"
          ]
        },
        {
          "openalex_id": "W3120557673",
          "year": 2021,
          "title": "Acceptance of the COVID-19 vaccine based on the health belief model: A population-based survey in Hong Kong",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 606,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Impact on Reproduction"
          ]
        },
        {
          "openalex_id": "W3086668930",
          "year": 2020,
          "title": "Intention of nurses to accept coronavirus disease 2019 vaccination and change of intention to accept seasonal influenza vaccination during the coronavirus disease 2019 pandemic: A cross-sectional survey",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 419,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Influenza Virus Research Studies",
            "COVID-19 and Mental Health"
          ]
        },
        {
          "openalex_id": "W3125098357",
          "year": 2021,
          "title": "Change of Willingness to Accept COVID-19 Vaccine and Reasons of Vaccine Hesitancy of Working People at Different Waves of Local Epidemic in Hong Kong, China: Repeated Cross-Sectional Surveys",
          "type": "article",
          "venue": "Vaccines",
          "cited_by_count": 289,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "COVID-19 epidemiological studies",
            "COVID-19 Pandemic Impacts"
          ]
        },
        {
          "openalex_id": "W1978689281",
          "year": 2001,
          "title": "Prospective evaluation of patients refused admission to an intensive care unit: triage, futility and outcome",
          "type": "article",
          "venue": "Intensive Care Medicine",
          "cited_by_count": 234,
          "topics": [
            "Sepsis Diagnosis and Treatment",
            "Emergency and Acute Care Studies",
            "Intensive Care Unit Cognitive Disorders"
          ]
        },
        {
          "openalex_id": "W2111504875",
          "year": 2005,
          "title": "Non-CF bronchiectasis: does knowing the aetiology lead to changes in management?",
          "type": "article",
          "venue": "European Respiratory Journal",
          "cited_by_count": 204,
          "topics": [
            "Cystic Fibrosis Research Advances",
            "Neonatal Respiratory Health Research",
            "Tracheal and airway disorders"
          ]
        },
        {
          "openalex_id": "W2605910070",
          "year": 2017,
          "title": "Integrated care for older populations and its implementation facilitators and barriers: A rapid scoping review",
          "type": "article",
          "venue": "International Journal for Quality in Health Care",
          "cited_by_count": 171,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Geriatric Care and Nursing Homes",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W3029688983",
          "year": 2020,
          "title": "Sociodemographic Predictors of Health Risk Perception, Attitude and Behavior Practices Associated with Health-Emergency Disaster Risk Management for Biological Hazards: The Case of COVID-19 Pandemic in Hong Kong, SAR China",
          "type": "article",
          "venue": "International Journal of Environmental Research and Public Health",
          "cited_by_count": 169,
          "topics": [
            "COVID-19 epidemiological studies",
            "Disaster Management and Resilience",
            "Viral Infections and Outbreaks Research"
          ]
        },
        {
          "openalex_id": "W3090353722",
          "year": 2020,
          "title": "Public preference for COVID‐19 vaccines in China: A discrete choice experiment",
          "type": "article",
          "venue": "Health Expectations",
          "cited_by_count": 157,
          "topics": [
            "Economic and Environmental Valuation",
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Elly Stolk",
    "member_affiliation": "EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "1721-RA",
        "title": "Extending the crosswalk dataset for EQ-5D-Y-3L and EQ-5D-Y-5L: proposal to fund multiple new inputs",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1761-EO",
        "title": "Development and Launch of a EuroQol E-Learning Program",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2013090",
        "title": "Course Title: Discrete choice for health state valuation",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2013300",
        "title": "The impact of framing effects on EQ-5D-5L valuations",
        "working_group": "Valuation"
      },
      {
        "project_id": "2014060",
        "title": "Separation of the BTD and WTD task in TTO",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015430",
        "title": "The impact of overlap and color coding on response efficiency in discrete choice experiments",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016410",
        "title": "The impact of color coding and the optimal degree of overlap in discrete choice experiments",
        "working_group": "Valuation"
      },
      {
        "project_id": "2138-TR",
        "title": "Data collection to support developing a crosswalk between EQ-TIPS and EQ-5D-Y",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2219-PCG",
        "title": "Partnership Agreement between Kemri-Wellcome Trust Research Programme and Euroqol Research Foundation",
        "working_group": "Valuation, Education and Outreach"
      },
      {
        "project_id": "2262-RA",
        "title": "Comprehensive Impact Assessment of EuroQol Research Foundation",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2644-EO",
        "title": "EUHEA preconference workshop: The Future of Health Preference Research",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5033903811",
      "display_name": "Elly Stolk",
      "orcid": "0000-0001-5968-0416",
      "reported_affiliation": "",
      "works_count": 161,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 110
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 56
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 18
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 12
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 11
        },
        {
          "topic": "Global Health Care Issues",
          "works": 10
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 9
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 9
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 8
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 8
        },
        {
          "topic": "Stuttering Research and Treatment",
          "works": 7
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jan J.V. Busschbach",
          "works": 28
        },
        {
          "name": "Mark Oppe",
          "works": 19
        },
        {
          "name": "Nancy Devlin",
          "works": 18
        },
        {
          "name": "Marcel F. Jonker",
          "works": 16
        },
        {
          "name": "Matthijs Versteegh",
          "works": 10
        },
        {
          "name": "Bas Donkers",
          "works": 10
        },
        {
          "name": "Fredrick Dermawan Purba",
          "works": 9
        },
        {
          "name": "John Brazier",
          "works": 9
        },
        {
          "name": "Zhihao Yang",
          "works": 9
        },
        {
          "name": "Ben van Hout",
          "works": 8
        },
        {
          "name": "Bram Roudijk",
          "works": 8
        },
        {
          "name": "Nan Luo",
          "works": 8
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7125150622",
          "year": 2026,
          "title": "Impact of mode of administration on agreement in health state scores and measurement properties of pediatric health related quality of life measurement instruments: a scoping review",
          "type": "preprint",
          "venue": "OSF Preprints (OSF Preprints)",
          "cited_by_count": 0,
          "topics": [
            "Childhood Cancer Survivors' Quality of Life",
            "Child and Adolescent Psychosocial and Emotional Development",
            "Pediatric Pain Management Techniques"
          ]
        },
        {
          "openalex_id": "W7116635480",
          "year": 2026,
          "title": "Valuing child and adolescent health states for use in economic evaluation: A good practices report of an ISPOR task force",
          "type": "article",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Policy and Management"
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
          "openalex_id": "W4410230033",
          "year": 2025,
          "title": "Adaptation of the Experimental Version of EQ-5D-Y-5L Into Bahasa Indonesia",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral and Psychological Studies",
            "Simulation-Based Education in Healthcare"
          ]
        },
        {
          "openalex_id": "W4412631456",
          "year": 2025,
          "title": "Measuring and Valuing Health Using EuroQol Instruments: New Developments 2025 and Beyond",
          "type": "article",
          "venue": "Applied Health Economics and Health Policy",
          "cited_by_count": 12,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Delphi Technique in Research"
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
          "openalex_id": "W1549889031",
          "year": 1999,
          "title": "The cost-utility of Viagra® in The Netherlands",
          "type": "report",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 4,
          "topics": [
            "Sexual function and dysfunction studies",
            "Sexuality, Behavior, and Technology",
            "Body Image and Dysmorphia Studies"
          ]
        },
        {
          "openalex_id": "W2046347354",
          "year": 2000,
          "title": "Cost effectiveness of sildenafil calls for political discussion",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 2,
          "topics": [
            "Sexual function and dysfunction studies",
            "Reproductive Health and Technologies",
            "Reproductive Health and Contraception"
          ]
        },
        {
          "openalex_id": "W2166357945",
          "year": 2000,
          "title": "Cost utility analysis of sildenafil compared with papaverine-phentolamine injections",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 69,
          "topics": [
            "Sexual function and dysfunction studies",
            "Pharmaceutical Quality and Counterfeiting",
            "Sexuality, Behavior, and Technology"
          ]
        },
        {
          "openalex_id": "W2008510340",
          "year": 2000,
          "title": "Cost-effectiveness of neonatal surgery: A review",
          "type": "article",
          "venue": "Journal of Pediatric Surgery",
          "cited_by_count": 13,
          "topics": [
            "Appendicitis Diagnosis and Management",
            "Intestinal Malrotation and Obstruction Disorders",
            "Congenital gastrointestinal and neural anomalies"
          ]
        },
        {
          "openalex_id": "W2334353679",
          "year": 2016,
          "title": "Dutch Tariff for the Five-Level Version of EQ-5D",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1144,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
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
          "openalex_id": "W2141266869",
          "year": 2013,
          "title": "Quality of life instruments for economic evaluations in health and social care for older people: A systematic review",
          "type": "review",
          "venue": "Social Science & Medicine",
          "cited_by_count": 196,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W1913100533",
          "year": 2015,
          "title": "Direct versus Indirect Treatment for Preschool Children who Stutter: The RESTART Randomized Trial",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 178,
          "topics": [
            "Stuttering Research and Treatment",
            "Stuttering Research and Treatment",
            "Child Nutrition and Feeding Issues"
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
          "openalex_id": "W2149352662",
          "year": 2006,
          "title": "Towards a multi‐criteria approach for priority setting: an application to Ghana",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 176,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Statistical Methods and Bayesian Inference"
          ]
        },
        {
          "openalex_id": "W2091278357",
          "year": 2013,
          "title": "Time trade-off: one methodology, different methods",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 163,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Environmental Valuation"
          ]
        }
      ]
    }
  },
  {
    "name": "Elske van den Akker-van Marle",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1447-RA",
        "title": "Investigating the dimensionality of wellbeing instruments and their added value in explaining health and wellbeing",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1792-SG",
        "title": "Applying Large Language Models to Identify EQ-5D Bolt-ons Based on Patient Text Data",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      },
      {
        "project_id": "2408-RA",
        "title": "Measurement Issues in EQ-5D Use in Older People Living with Dementia: Comparing the Dimensional Coverage of EQ-5D of Self and Proxy Reports",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2420-BT",
        "title": "Cognition in EQ-5D-5L: A Content Validity Study in Dementia and Caregiving Contexts in the Netherlands",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5032469209",
      "display_name": "M. Elske van den Akker‐van Marle",
      "orcid": "0000-0002-5269-509X",
      "reported_affiliation": "Leiden University Medical Center",
      "works_count": 209,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 31
        },
        {
          "topic": "Maternal and Perinatal Health Interventions",
          "works": 14
        },
        {
          "topic": "Spine and Intervertebral Disc Pathology",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 11
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 11
        },
        {
          "topic": "Global Maternal and Child Health",
          "works": 9
        },
        {
          "topic": "Cystic Fibrosis Research Advances",
          "works": 8
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 7
        },
        {
          "topic": "Cervical and Thoracic Myelopathy",
          "works": 7
        },
        {
          "topic": "Digital Mental Health Interventions",
          "works": 7
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 7
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 7
        }
      ],
      "frequent_coauthors": [
        {
          "name": "C.P.B. van der Ploeg",
          "works": 14
        },
        {
          "name": "Wilco C. Peul",
          "works": 11
        },
        {
          "name": "Anne M. Stiggelbout",
          "works": 11
        },
        {
          "name": "Leti van Bodegom‐Vos",
          "works": 11
        },
        {
          "name": "Perla J. Marang‐van de Mheen",
          "works": 11
        },
        {
          "name": "Wilbert B. van den Hout",
          "works": 11
        },
        {
          "name": "P.H. Verkerk",
          "works": 11
        },
        {
          "name": "Mattijs E. Numans",
          "works": 11
        },
        {
          "name": "Marlies Rijnders",
          "works": 10
        },
        {
          "name": "Albert Dahan",
          "works": 9
        },
        {
          "name": "Marjolein van Ballegooijen",
          "works": 9
        },
        {
          "name": "Rob G. H. H. Nelissen",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167071219",
          "year": 2026,
          "title": "Cost-effectiveness of the sFlt-1/PlGF ratio and telemonitoring in managing suspected pre-eclampsia: protocol for the PREPARE II randomised controlled trial",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Pregnancy and preeclampsia studies",
            "Maternal and fetal healthcare",
            "Preterm Birth and Chorioamnionitis"
          ]
        },
        {
          "openalex_id": "W4410109550",
          "year": 2025,
          "title": "Case Finding for Celiac Disease With a Point-of-Care Test",
          "type": "article",
          "venue": "PEDIATRICS",
          "cited_by_count": 2,
          "topics": [
            "Celiac Disease Research and Management",
            "Microscopic Colitis",
            "Glycosylation and Glycoproteins Research"
          ]
        },
        {
          "openalex_id": "W4409712635",
          "year": 2025,
          "title": "Choroidal melanoma patient views on the importance of treatment characteristics and outcomes, and physicians' information provision in the Netherlands",
          "type": "article",
          "venue": "Acta Ophthalmologica",
          "cited_by_count": 2,
          "topics": [
            "Ocular Oncology and Treatments",
            "Ocular Disorders and Treatments",
            "Glaucoma and retinal disorders"
          ]
        },
        {
          "openalex_id": "W4409539838",
          "year": 2025,
          "title": "Cost analysis of intrauterine balloon tamponade versus uterine artery embolization in the management of persistent postpartum hemorrhage",
          "type": "article",
          "venue": "International Journal of Gynecology & Obstetrics",
          "cited_by_count": 1,
          "topics": [
            "Maternal and fetal healthcare",
            "Uterine Myomas and Treatments",
            "Gestational Trophoblastic Disease Studies"
          ]
        },
        {
          "openalex_id": "W4413277512",
          "year": 2025,
          "title": "Costs in value-based health care dashboards: a qualitative study on stakeholder requirements",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 0,
          "topics": [
            "Primary Care and Health Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W4408305422",
          "year": 2025,
          "title": "Decision-making Factors in Surgical Techniques and Attitudes Towards Environmental Sustainability",
          "type": "article",
          "venue": "Annals of Surgery",
          "cited_by_count": 2,
          "topics": [
            "Climate Change and Health Impacts",
            "Climate Change Communication and Perception",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2073268787",
          "year": 1996,
          "title": "PP-4-21 Evaluation of the european pilot project in navarra; A high breast cancer detection rate in the first round and a low rate in the second round",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 0,
          "topics": [
            "Lung Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2079562291",
          "year": 1997,
          "title": "Breast cancer screening in Navarra: interpretation of a high detection rate at the first screening round and a low rate at the second round",
          "type": "article",
          "venue": "International Journal of Cancer",
          "cited_by_count": 26,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Colorectal Cancer Screening and Detection",
            "Cancer Risks and Factors"
          ]
        },
        {
          "openalex_id": "W4244659841",
          "year": 1997,
          "title": "Breast cancer screening in Navarra: interpretation of a high detection rate at the first screening round and a low rate at the second round",
          "type": "article",
          "venue": "International Journal of Cancer",
          "cited_by_count": 2,
          "topics": [
            "Global Cancer Incidence and Screening",
            "Colorectal Cancer Screening and Detection",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2052003032",
          "year": 1997,
          "title": "Non-progression of cervical intraepithelial neoplasia estimated from population-screening data",
          "type": "article",
          "venue": "British Journal of Cancer",
          "cited_by_count": 52,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Global Cancer Incidence and Screening",
            "Colorectal Cancer Screening and Detection"
          ]
        },
        {
          "openalex_id": "W2620360426",
          "year": 2017,
          "title": "Clinical and cost-effectiveness of home-based cardiac rehabilitation compared to conventional, centre-based cardiac rehabilitation: Results of the FIT@Home study",
          "type": "article",
          "venue": "European Journal of Preventive Cardiology",
          "cited_by_count": 256,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular and exercise physiology",
            "Heart Rate Variability and Autonomic Control"
          ]
        },
        {
          "openalex_id": "W2002724910",
          "year": 2000,
          "title": "A systematic review of the role of human papilloma virus (HPV) testing within a cervical screening programme: summary and conclusions",
          "type": "review",
          "venue": "British Journal of Cancer",
          "cited_by_count": 157,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Genital Health and Disease",
            "Reproductive tract infections research"
          ]
        },
        {
          "openalex_id": "W2982551528",
          "year": 2019,
          "title": "Surgery as a Viable Alternative First-Line Treatment for Prolactinoma Patients. A Systematic Review and Meta-Analysis",
          "type": "review",
          "venue": "The Journal of Clinical Endocrinology & Metabolism",
          "cited_by_count": 140,
          "topics": [
            "Pituitary Gland Disorders and Treatments",
            "Adrenal and Paraganglionic Tumors",
            "Neuroendocrine Tumor Research Advances"
          ]
        },
        {
          "openalex_id": "W4214762837",
          "year": 2022,
          "title": "The implementation of value-based healthcare: a scoping review",
          "type": "article",
          "venue": "BMC Health Services Research",
          "cited_by_count": 138,
          "topics": [
            "Healthcare cost, quality, practices",
            "Primary Care and Health Outcomes",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2149246244",
          "year": 2006,
          "title": "Cost-Effectiveness of Pharmacogenomics in Clinical Practice: a Case Study of Thiopurine Methyltransferase Genotyping in Acute Lymphoblastic Leukemia in Europe",
          "type": "article",
          "venue": "Pharmacogenomics",
          "cited_by_count": 133,
          "topics": [
            "Acute Lymphoblastic Leukemia research",
            "Pharmaceutical studies and practices",
            "Chronic Lymphocytic Leukemia Research"
          ]
        },
        {
          "openalex_id": "W2103858265",
          "year": 2015,
          "title": "Patient controlled analgesia with remifentanil versus epidural analgesia in labour: randomised multicentre equivalence trial",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 123,
          "topics": [
            "Anesthesia and Pain Management",
            "Maternal and Perinatal Health Interventions",
            "Nausea and vomiting management"
          ]
        },
        {
          "openalex_id": "W2102089766",
          "year": 2002,
          "title": "Cost-Effectiveness of Cervical Cancer Screening: Comparison of Screening Policies",
          "type": "article",
          "venue": "JNCI Journal of the National Cancer Institute",
          "cited_by_count": 118,
          "topics": [
            "Cervical Cancer and HPV Research",
            "Endometrial and Cervical Cancer Treatments",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W2031711175",
          "year": 2014,
          "title": "Effects of home-based training with telemonitoring guidance in low to moderate risk patients entering cardiac rehabilitation: short-term results of the FIT@Home study",
          "type": "article",
          "venue": "European Journal of Preventive Cardiology",
          "cited_by_count": 116,
          "topics": [
            "Cardiac Health and Mental Health",
            "Cardiovascular and exercise physiology",
            "Heart Rate Variability and Autonomic Control"
          ]
        }
      ]
    }
  }
]
