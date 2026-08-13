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
    "name": "Guangjie Zhang",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1758-EO",
        "title": "The uniqueness and overlap of the EQ-HWB and the EQ-5D-5L in four diseases, healthy subjects, and caregivers",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1985-EO",
        "title": "Request for a travel scholarship to attend ISPOR Europe 2024 to present and disseminate findings",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5030831609",
      "display_name": "Guangjie Zhang",
      "orcid": "0000-0003-1311-8510",
      "reported_affiliation": "Murdoch University",
      "works_count": 71,
      "top_topics": [
        {
          "topic": "Composting and Vermicomposting Techniques",
          "works": 6
        },
        {
          "topic": "Phytochemistry and Biological Activities",
          "works": 6
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 6
        },
        {
          "topic": "Polysaccharides Composition and Applications",
          "works": 4
        },
        {
          "topic": "Nanocomposite Films for Food Packaging",
          "works": 4
        },
        {
          "topic": "Natural product bioactivities and synthesis",
          "works": 4
        },
        {
          "topic": "Health, psychology, and well-being",
          "works": 4
        },
        {
          "topic": "Essential Oils and Antimicrobial Activity",
          "works": 3
        },
        {
          "topic": "Pharmacological Effects of Natural Compounds",
          "works": 3
        },
        {
          "topic": "Biochemical effects in animals",
          "works": 3
        },
        {
          "topic": "Phytochemicals and Antioxidant Activities",
          "works": 3
        },
        {
          "topic": "Insect Utilization and Effects",
          "works": 3
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bin Li",
          "works": 8
        },
        {
          "name": "Min Li",
          "works": 8
        },
        {
          "name": "Tianzhu Guan",
          "works": 8
        },
        {
          "name": "Ying Tian",
          "works": 7
        },
        {
          "name": "Zhihao Yang",
          "works": 7
        },
        {
          "name": "Jie Zhang",
          "works": 6
        },
        {
          "name": "Ziming Xia",
          "works": 6
        },
        {
          "name": "Jun-Xing Dong",
          "works": 6
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 6
        },
        {
          "name": "Sifan Liu",
          "works": 6
        },
        {
          "name": "Ronghua Li",
          "works": 5
        },
        {
          "name": "Zengqiang Zhang",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7131077368",
          "year": 2026,
          "title": "Effect of Xanthoceras sorbifolia Bunge seed meal extract on polyuria in rats with kidney deficiency syndrome",
          "type": "article",
          "venue": "Phytomedicine Plus",
          "cited_by_count": 0,
          "topics": [
            "Natural Antidiabetic Agents Studies",
            "Plant Toxicity and Pharmacological Properties",
            "Hibiscus Plant Research Studies"
          ]
        },
        {
          "openalex_id": "W7160060330",
          "year": 2026,
          "title": "Enhanced nitrogen retention with a two-stage composting strategy: Synergistic effects of exogenous additives and eco-friendly insect on microbial regulation",
          "type": "article",
          "venue": "Resources Environment and Sustainability",
          "cited_by_count": 0,
          "topics": [
            "Composting and Vermicomposting Techniques",
            "Entomopathogenic Microorganisms in Pest Control",
            "Insect Utilization and Effects"
          ]
        },
        {
          "openalex_id": "W7163658802",
          "year": 2026,
          "title": "OV16 Improves Radiation-Induced Intestinal Injury by Targeting Transglutaminase 2",
          "type": "article",
          "venue": "Molecules",
          "cited_by_count": 0,
          "topics": [
            "Effects of Radiation Exposure",
            "Blood properties and coagulation",
            "Hemophilia Treatment and Research"
          ]
        },
        {
          "openalex_id": "W7137841369",
          "year": 2026,
          "title": "Preparation of xanthan gum/quinoa protein/cinnamon essential oil composite coating: Application in blueberry preservation and its antioxidant mechanism via network pharmacology",
          "type": "article",
          "venue": "Journal of Food Measurement & Characterization",
          "cited_by_count": 0,
          "topics": [
            "Polysaccharides Composition and Applications",
            "Nanocomposite Films for Food Packaging",
            "Phytochemicals and Antioxidant Activities"
          ]
        },
        {
          "openalex_id": "W7138833896",
          "year": 2026,
          "title": "Simultaneous Controlled N, P and K Release Amplifies Economic Viability and Environmental Stewardship in Rice",
          "type": "article",
          "venue": "Agronomy",
          "cited_by_count": 0,
          "topics": [
            "Sustainability and Ecological Systems Analysis",
            "Soil Carbon and Nitrogen Dynamics",
            "Rice Cultivation and Yield Improvement"
          ]
        },
        {
          "openalex_id": "W4407656747",
          "year": 2025,
          "title": "Comparing the Measurement Properties of the Preliminary Version of the EuroQol Health and Well-Being and EQ-5D-5L in Patients, Healthy General Public, and Caregivers",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4234648690",
          "year": 2004,
          "title": "A Produciton Benefit Evaluation Program",
          "type": "conference-paper",
          "venue": "Proceedings of SPE Asia Pacific Conference on Integrated Modelling for Asset Management",
          "cited_by_count": 0,
          "topics": [
            "Reservoir Engineering and Simulation Methods",
            "Oil and Gas Production Techniques",
            "Hydraulic Fracturing and Reservoir Analysis"
          ]
        },
        {
          "openalex_id": "W2386562171",
          "year": 2011,
          "title": "Study on isolation and extraction of A-and B-type starch granules in wheat",
          "type": "article",
          "venue": "Cereals & Oils",
          "cited_by_count": 0,
          "topics": [
            "Food composition and properties"
          ]
        },
        {
          "openalex_id": "W2347420809",
          "year": 2012,
          "title": "Investigation of heavy metal ions adsorption ability by thiol-modified corn stalk powder",
          "type": "article",
          "venue": "Journal of Northwest A&F University",
          "cited_by_count": 1,
          "topics": [
            "Adsorption and biosorption for pollutant removal"
          ]
        },
        {
          "openalex_id": "W424760344",
          "year": 2012,
          "title": "Nutrient transformation during swine manure co-composting with flyash under aerobic conditions.",
          "type": "article",
          "venue": "Transactions of the Chinese Society of Agricultural Machinery",
          "cited_by_count": 2,
          "topics": [
            "Composting and Vermicomposting Techniques"
          ]
        },
        {
          "openalex_id": "W2091614528",
          "year": 2012,
          "title": "Nutrient transformations during composting of pig manure with bentonite",
          "type": "article",
          "venue": "Bioresource Technology",
          "cited_by_count": 378,
          "topics": [
            "Composting and Vermicomposting Techniques",
            "Waste Management and Recycling",
            "Constructed Wetlands for Wastewater Treatment"
          ]
        },
        {
          "openalex_id": "W2019186454",
          "year": 2014,
          "title": "Nutrient transformation during aerobic composting of pig manure with biochar prepared at different temperatures",
          "type": "article",
          "venue": "Environmental Technology",
          "cited_by_count": 189,
          "topics": [
            "Composting and Vermicomposting Techniques",
            "Waste Management and Recycling"
          ]
        },
        {
          "openalex_id": "W2346465505",
          "year": 2016,
          "title": "Influence of cyclodextrins on texture behavior and freeze-thaw stability of kappa-carrageenan gel",
          "type": "article",
          "venue": "Food Chemistry",
          "cited_by_count": 94,
          "topics": [
            "Seaweed-derived Bioactive Compounds",
            "Microbial Metabolites in Food Biotechnology",
            "Polysaccharides Composition and Applications"
          ]
        },
        {
          "openalex_id": "W2801677087",
          "year": 2018,
          "title": "Effect of Selective Encapsulation of Hydroxypropyl-β-cyclodextrin on Components and Antibacterial Properties of Star Anise Essential Oil",
          "type": "article",
          "venue": "Molecules",
          "cited_by_count": 62,
          "topics": [
            "Essential Oils and Antimicrobial Activity",
            "Drug Solubulity and Delivery Systems",
            "Pharmacological Effects of Natural Compounds"
          ]
        },
        {
          "openalex_id": "W4213313350",
          "year": 2022,
          "title": "Synergism of ellagic acid in combination with radiotherapy and chemotherapy for cancer treatment",
          "type": "article",
          "venue": "Phytomedicine",
          "cited_by_count": 57,
          "topics": [
            "Pomegranate: compositions and health benefits",
            "Chemotherapy-induced organ toxicity mitigation",
            "Chemotherapy-induced cardiotoxicity and mitigation"
          ]
        },
        {
          "openalex_id": "W3176998857",
          "year": 2021,
          "title": "Advances in Supercritical Carbon Dioxide Extraction of Bioactive Substances from Different Parts of Ginkgo biloba L.",
          "type": "article",
          "venue": "Molecules",
          "cited_by_count": 56,
          "topics": [
            "Ginkgo biloba and Cashew Applications",
            "Neurological Disease Mechanisms and Treatments",
            "Tea Polyphenols and Effects"
          ]
        },
        {
          "openalex_id": "W4200503762",
          "year": 2021,
          "title": "Characterization and evaluation of sodium alginate-based edible films by incorporation of star anise ethanol extract/hydroxypropyl-β-cyclodextrin inclusion complex",
          "type": "article",
          "venue": "Food Packaging and Shelf Life",
          "cited_by_count": 30,
          "topics": [
            "Nanocomposite Films for Food Packaging",
            "Nanoparticles: synthesis and applications",
            "Polysaccharides Composition and Applications"
          ]
        },
        {
          "openalex_id": "W4283312951",
          "year": 2022,
          "title": "A randomized, placebo‐controlled clinical trial of hydrogen/oxygen inhalation for non‐alcoholic fatty liver disease",
          "type": "article",
          "venue": "Journal of Cellular and Molecular Medicine",
          "cited_by_count": 29,
          "topics": [
            "Hydrogen's biological and therapeutic effects",
            "Dietary Effects on Health",
            "Biochemical effects in animals"
          ]
        }
      ]
    }
  },
  {
    "name": "Hannah Hussain",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1967-RA",
        "title": "Assessing bolt-ons in cognition (ABC): a secondary analysis",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5015275165",
      "display_name": "Hannah Hussain",
      "orcid": "0009-0002-5645-184X",
      "reported_affiliation": "Office Of Health Economics",
      "works_count": 12,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 6
        },
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 6
        },
        {
          "topic": "Mental Health and Patient Involvement",
          "works": 3
        },
        {
          "topic": "Hearing Loss and Rehabilitation",
          "works": 2
        },
        {
          "topic": "Hearing Impairment and Communication",
          "works": 2
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Hearing, Cochlea, Tinnitus, Genetics",
          "works": 1
        },
        {
          "topic": "Schizophrenia research and treatment",
          "works": 1
        },
        {
          "topic": "Family Caregiving in Mental Illness",
          "works": 1
        },
        {
          "topic": "Breastfeeding Practices and Influences",
          "works": 1
        },
        {
          "topic": "Infant Development and Preterm Care",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Elizabeth Camacho",
          "works": 4
        },
        {
          "name": "Rachel Elliott",
          "works": 4
        },
        {
          "name": "Anju Keetharuth",
          "works": 4
        },
        {
          "name": "Donna Rowen",
          "works": 4
        },
        {
          "name": "Allan Wailoo",
          "works": 4
        },
        {
          "name": "Iracema Leroi",
          "works": 3
        },
        {
          "name": "Fofi Constantinidou",
          "works": 3
        },
        {
          "name": "Piers Dawes",
          "works": 3
        },
        {
          "name": "Éric Frison",
          "works": 3
        },
        {
          "name": "Mark Hann",
          "works": 3
        },
        {
          "name": "Chryssoula Thodi",
          "works": 3
        },
        {
          "name": "Zoë Simkin",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7148449495",
          "year": 2026,
          "title": "Economic Evaluation of the Health Impacts of Climate Action (or inaction): A Deep Dive into Social Cost of Carbon, Value of a Statistical Life, Equity, Macroeconomic Modelling, and Discounting",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Climate Change and Health Impacts",
            "Climate Change Policy and Economics"
          ]
        },
        {
          "openalex_id": "W7164348563",
          "year": 2026,
          "title": "Patient Preferences for Treatment in Relapsed/Refractory Acute Leukemia: A Multinational Discrete Choice Experiment",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 0,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4417002264",
          "year": 2025,
          "title": "A multinational study to explore patient preferences for chronic myeloid leukaemia treatments",
          "type": "conference-abstract",
          "venue": "Blood",
          "cited_by_count": 0,
          "topics": [
            "Chronic Myeloid Leukemia Treatments",
            "Medication Adherence and Compliance",
            "Acute Myeloid Leukemia Research"
          ]
        },
        {
          "openalex_id": "W4408343264",
          "year": 2025,
          "title": "Enhancing HRQoL assessment for economic evaluation in dementia populations",
          "type": "article",
          "venue": "Alzheimer s & Dementia Translational Research & Clinical Interventions",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W4411049790",
          "year": 2025,
          "title": "Mapping EQ-5D-5L Utilities in Dementia: Integrating Self and Proxy Reports",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4412648253",
          "year": 2025,
          "title": "The Cost‐Effectiveness of an Intervention to Preserve Independence in People With Dementia (Vs. No Intervention): A Decision‐Analytic (Markov) Model Analysis",
          "type": "article",
          "venue": "International Journal of Geriatric Psychiatry",
          "cited_by_count": 0,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Dementia and Cognitive Impairment Research",
            "Healthcare innovation and challenges"
          ]
        },
        {
          "openalex_id": "W2943065981",
          "year": 2019,
          "title": "Feasibility of an Intervention to Support Hearing and Vision in Dementia: The SENSE‐Cog Field Trial",
          "type": "article",
          "venue": "Journal of the American Geriatrics Society",
          "cited_by_count": 28,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Dementia and Cognitive Impairment Research",
            "Hearing Impairment and Communication"
          ]
        },
        {
          "openalex_id": "W2983680719",
          "year": 2019,
          "title": "Impact of an intervention to support hearing and vision in dementia: The SENSE‐Cog Field Trial",
          "type": "article",
          "venue": "International Journal of Geriatric Psychiatry",
          "cited_by_count": 77,
          "topics": [
            "Hearing Loss and Rehabilitation",
            "Hearing Impairment and Communication",
            "Hearing, Cochlea, Tinnitus, Genetics"
          ]
        },
        {
          "openalex_id": "W3109666226",
          "year": 2020,
          "title": "Cost-effectiveness evidence for strategies to promote or support breastfeeding: a systematic search and narrative literature review",
          "type": "article",
          "venue": "BMC Pregnancy and Childbirth",
          "cited_by_count": 27,
          "topics": [
            "Breastfeeding Practices and Influences",
            "Infant Development and Preterm Care",
            "Infant Nutrition and Health"
          ]
        },
        {
          "openalex_id": "W3035551207",
          "year": 2020,
          "title": "Impact of receiving recorded mental health recovery narratives on quality of life in people experiencing psychosis, people experiencing other mental health problems and for informal carers: Narrative Experiences Online (NEON) study protocol for three randomised controlled trials",
          "type": "article",
          "venue": "Trials",
          "cited_by_count": 41,
          "topics": [
            "Mental Health and Patient Involvement",
            "Schizophrenia research and treatment",
            "Family Caregiving in Mental Illness"
          ]
        },
        {
          "openalex_id": "W4297497435",
          "year": 2022,
          "title": "Assessing the psychometric performance of EQ-5D-5L in dementia: a systematic review",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 56,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Mental Health and Patient Involvement"
          ]
        },
        {
          "openalex_id": "W4309561473",
          "year": 2022,
          "title": "Convergent validity of EQ-5D with core outcomes in dementia: a systematic review",
          "type": "review",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 9,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Mental Health and Patient Involvement"
          ]
        }
      ]
    }
  },
  {
    "name": "Hannah Penton",
    "member_affiliation": "",
    "is_member": true,
    "projects": [
      {
        "project_id": "1453-RA",
        "title": "Exploring the use of multi-dimensional Item Response Theory to analyse EuroQol Instruments",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1493-RA",
        "title": "An investigation into the psychometric performance of the EQ-PSO in patients with atopic dermatitis in the UK and Germany",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1494-RA",
        "title": "An investigation of differential item functioning related to age, gender and education in the EQ-5D-5L using ordinal logistic regression",
        "working_group": "Descriptive Systems, Populations and Health Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5056335393",
      "display_name": "Hannah Penton",
      "orcid": "0000-0001-9492-7875",
      "reported_affiliation": "Patient-Centered Outcomes Research Institute",
      "works_count": 26,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 12
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        },
        {
          "topic": "Parkinson's Disease Mechanisms and Treatments",
          "works": 4
        },
        {
          "topic": "Sleep and related disorders",
          "works": 3
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 2
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 2
        },
        {
          "topic": "Medication Adherence and Compliance",
          "works": 2
        },
        {
          "topic": "Dermatology and Skin Diseases",
          "works": 2
        },
        {
          "topic": "Psoriasis: Treatment and Pathogenesis",
          "works": 2
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 2
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 2
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Marieke Heisen",
          "works": 10
        },
        {
          "name": "Marco Boeri",
          "works": 9
        },
        {
          "name": "Rajesh Pahwa",
          "works": 8
        },
        {
          "name": "Irene A. Malaty",
          "works": 8
        },
        {
          "name": "Josefa Domingos",
          "works": 7
        },
        {
          "name": "Pablo Arija",
          "works": 6
        },
        {
          "name": "Connie H. Yan",
          "works": 6
        },
        {
          "name": "K Ray Chaudhuri",
          "works": 5
        },
        {
          "name": "Anjana Lalla",
          "works": 5
        },
        {
          "name": "Zachary Baldwin",
          "works": 5
        },
        {
          "name": "Divya Mohan",
          "works": 5
        },
        {
          "name": "Sayeli Jayade",
          "works": 4
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
          "openalex_id": "W7154370202",
          "year": 2026,
          "title": "Burden and disutility of sleep disturbance and early morning OFF symptoms in people with advancing Parkinson’s disease: a vignette-based approach using the EQ-5D-5L",
          "type": "article",
          "venue": "Journal of Patient-Reported Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Sleep and related disorders",
            "Parkinson's Disease Mechanisms and Treatments",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W7162396037",
          "year": 2026,
          "title": "Burden and disutility of sleep disturbance and early morning OFF symptoms in people with advancing Parkinson’s disease: a vignette-based approach using the EQ-5D-5L",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7162422235",
          "year": 2026,
          "title": "Burden and disutility of sleep disturbance and early morning OFF symptoms in people with advancing Parkinson’s disease: a vignette-based approach using the EQ-5D-5L",
          "type": "other",
          "venue": "Figshare",
          "cited_by_count": 0,
          "topics": []
        },
        {
          "openalex_id": "W7147214482",
          "year": 2026,
          "title": "Exploring Preferences and Priorities in Advanced Parkinson’s Disease: A Discrete Choice Experiment",
          "type": "article",
          "venue": "Neurology and Therapy",
          "cited_by_count": 0,
          "topics": [
            "Parkinson's Disease Mechanisms and Treatments",
            "Economic and Environmental Valuation",
            "Assistive Technology in Communication and Mobility"
          ]
        },
        {
          "openalex_id": "W2346806743",
          "year": 2016,
          "title": "Potential cost-effectiveness for using patient decision aids to guide osteoporosis treatment",
          "type": "article",
          "venue": "Osteoporosis International",
          "cited_by_count": 7,
          "topics": [
            "Patient-Provider Communication in Healthcare",
            "Bone health and osteoporosis research",
            "Ethics and Legal Issues in Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W2906636693",
          "year": 2018,
          "title": "PIH52 - AN INVESTIGATION INTO THE CONTENT VALIDITY AND FEASIBILITY OF THE EQ-5D-5L, SF-12, WEMWBS AND ONS-4 IN MEASURING THE QUALITY OF LIFE AND WELLBEING OF OLDER ADULTS.",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2971111900",
          "year": 2019,
          "title": "An investigation into the psychometric performance of existing measures of health, quality of life and wellbeing in older adults",
          "type": "dissertation",
          "venue": "White Rose eTheses Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W3096894459",
          "year": 2020,
          "title": "Avatrombopag and lusutrombopag for thrombocytopenia in people with chronic liver disease needing an elective procedure: a systematic review and cost-effectiveness analysis",
          "type": "review",
          "venue": "Health Technology Assessment",
          "cited_by_count": 18,
          "topics": [
            "Platelet Disorders and Treatments",
            "Trauma, Hemostasis, Coagulopathy, Resuscitation",
            "Blood transfusion and management"
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
          "openalex_id": "W3137428760",
          "year": 2021,
          "title": "10 Years of End-of-Life Criteria in the United Kingdom",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 50,
          "topics": [
            "Palliative Care and End-of-Life Issues",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Decision-Making and Restraints"
          ]
        },
        {
          "openalex_id": "W3183300375",
          "year": 2021,
          "title": "Regulatory and HTA early dialogues in medical devices",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 22,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Biomedical Ethics and Regulation",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4224921319",
          "year": 2022,
          "title": "An Investigation of Age-Related Differential Item Functioning in the EQ-5D-5L Using Item Response Theory and Logistic Regression",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 19,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W4283455937",
          "year": 2022,
          "title": "A Qualitative Investigation of Older Adults’ Conceptualization of Quality of Life and a Think-Aloud Content Validation of the EQ-5D-5L, SF-12v2, Warwick Edinburgh Mental Well-Being Scale, and Office of National Statistics-4.",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 17,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Frailty in Older Adults"
          ]
        },
        {
          "openalex_id": "W4405417317",
          "year": 2024,
          "title": "Impact of recurrence on employment, finances, and productivity for early-stage cancer patients and caregivers: US survey",
          "type": "article",
          "venue": "Future Oncology",
          "cited_by_count": 10,
          "topics": [
            "Economic and Financial Impacts of Cancer",
            "Cancer survivorship and care",
            "Medication Adherence and Compliance"
          ]
        },
        {
          "openalex_id": "W4387002573",
          "year": 2023,
          "title": "Assessing Response in Atopic Dermatitis: A Systematic Review of the Psychometric Performance of Measures Used in HTAs and Clinical Trials",
          "type": "review",
          "venue": "Dermatology and Therapy",
          "cited_by_count": 9,
          "topics": [
            "Dermatology and Skin Diseases",
            "Allergic Rhinitis and Sensitization",
            "Psoriasis: Treatment and Pathogenesis"
          ]
        }
      ]
    }
  },
  {
    "name": "Haode Wang",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "1963-RA",
        "title": "A comprehensive feasibility, acceptability and validity assessment of using EQ-HWB in elerdly rehabilitation care in China",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2107-TVG",
        "title": "Travel Grant to support EQ PhD network member to present EQ-HWB research on iHEA meeting and to visit National University of Singapore for learning and exploring research collaborations.",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5073060343",
      "display_name": "Haode Wang",
      "orcid": "0000-0002-0759-7087",
      "reported_affiliation": "Shanghai Medical Information Center",
      "works_count": 6,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 2
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 2
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 1
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 1
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 1
        },
        {
          "topic": "Platelet Disorders and Treatments",
          "works": 1
        },
        {
          "topic": "Blood groups and transfusion",
          "works": 1
        },
        {
          "topic": "Chronic Lymphocytic Leukemia Research",
          "works": 1
        },
        {
          "topic": "Autism Spectrum Disorder Research",
          "works": 1
        },
        {
          "topic": "Psychology of Moral and Emotional Judgment",
          "works": 1
        },
        {
          "topic": "Clinical Nutrition and Gastroenterology",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Haiyin Wang",
          "works": 4
        },
        {
          "name": "Yashuang Luo",
          "works": 3
        },
        {
          "name": "Yiting Huang",
          "works": 2
        },
        {
          "name": "Shuaixin Feng",
          "works": 2
        },
        {
          "name": "Yuyan Zhao",
          "works": 2
        },
        {
          "name": "Hongbo Jiang",
          "works": 2
        },
        {
          "name": "Yuyan Fu",
          "works": 2
        },
        {
          "name": "Hui Sun",
          "works": 1
        },
        {
          "name": "Chunlin Jin",
          "works": 1
        },
        {
          "name": "Meifeng Wang",
          "works": 1
        },
        {
          "name": "Wenqian Song",
          "works": 1
        },
        {
          "name": "Donna Rowen",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413095180",
          "year": 2025,
          "title": "Assessment of structured triglyceride emulsion in parenteral nutrition for abdominal surgery patients: A systematic review and network meta-analysis",
          "type": "review",
          "venue": "Healthcare and Rehabilitation",
          "cited_by_count": 0,
          "topics": [
            "Clinical Nutrition and Gastroenterology",
            "Nutrition and Health in Aging",
            "Abdominal Surgery and Complications"
          ]
        },
        {
          "openalex_id": "W4412750883",
          "year": 2025,
          "title": "Valuing health and wellbeing using discrete choice experiment: exploring feasibility, design effect and international preference similarity",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4401111814",
          "year": 2024,
          "title": "Cost-utility analysis of romiplostim for the treatment of chronic primary immune thrombocytopenia in China",
          "type": "article",
          "venue": "Intractable & Rare Diseases Research",
          "cited_by_count": 2,
          "topics": [
            "Platelet Disorders and Treatments",
            "Blood groups and transfusion",
            "Chronic Lymphocytic Leukemia Research"
          ]
        },
        {
          "openalex_id": "W4401079045",
          "year": 2024,
          "title": "Preferences for COVID-19 Vaccines: Systematic Literature Review of Discrete Choice Experiments",
          "type": "review",
          "venue": "JMIR Public Health and Surveillance",
          "cited_by_count": 12,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4401079426",
          "year": 2024,
          "title": "Preferences for COVID-19 Vaccines: Systematic Literature Review of Discrete Choice Experiments (Preprint)",
          "type": "preprint",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "Autism Spectrum Disorder Research",
            "Psychology of Moral and Emotional Judgment"
          ]
        },
        {
          "openalex_id": "W4290975305",
          "year": 2022,
          "title": "Preference to Family Doctor Contracted Service of Patients with Chronic Disease in Urban China: A Discrete Choice Experiment",
          "type": "article",
          "venue": "Patient Preference and Adherence",
          "cited_by_count": 12,
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
    "name": "Harri Sintonen",
    "member_affiliation": "University of Helsinki/Department of Public Health",
    "is_member": true,
    "projects": [],
    "chosen_profile": {
      "openalex_id": "A5032927955",
      "display_name": "Harri Sintonen",
      "orcid": "0000-0003-1252-0946",
      "reported_affiliation": "University of Helsinki",
      "works_count": 488,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 76
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 33
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 27
        },
        {
          "topic": "Research in Social Sciences",
          "works": 25
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 22
        },
        {
          "topic": "Chronic Obstructive Pulmonary Disease (COPD) Research",
          "works": 15
        },
        {
          "topic": "Cardiac Health and Mental Health",
          "works": 15
        },
        {
          "topic": "Bariatric Surgery and Outcomes",
          "works": 14
        },
        {
          "topic": "Global Health Care Issues",
          "works": 13
        },
        {
          "topic": "Musculoskeletal pain and rehabilitation",
          "works": 13
        },
        {
          "topic": "Orthopaedic implants and arthroplasty",
          "works": 13
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 12
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Risto P. Roine",
          "works": 120
        },
        {
          "name": "Pirjo Räsänen",
          "works": 50
        },
        {
          "name": "Pekka Rissanen",
          "works": 23
        },
        {
          "name": "Miika Linna",
          "works": 21
        },
        {
          "name": "Pekka Paavolainen",
          "works": 20
        },
        {
          "name": "Marja Blom",
          "works": 20
        },
        {
          "name": "Pasi Aronen",
          "works": 19
        },
        {
          "name": "Kimmo Taari",
          "works": 18
        },
        {
          "name": "Antti Malmivaara",
          "works": 17
        },
        {
          "name": "Tiina Saarto",
          "works": 17
        },
        {
          "name": "Ulla Tuominen",
          "works": 16
        },
        {
          "name": "Johanna Hirvonen",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7140517363",
          "year": 2026,
          "title": "2195 Long-Term Patient-Reported Outcomes After Cerebellopontine Angle Epidermoid Cyst Surgery",
          "type": "conference-abstract",
          "venue": "Neurosurgery",
          "cited_by_count": 0,
          "topics": [
            "Teratomas and Epidermoid Cysts",
            "Facial Nerve Paralysis Treatment and Research",
            "Trigeminal Neuralgia and Treatments"
          ]
        },
        {
          "openalex_id": "W7124872711",
          "year": 2026,
          "title": "The Effect of Age on Improvement in Health‐Related Quality of Life After Percutaneous Coronary Intervention",
          "type": "article",
          "venue": "Clinical Cardiology",
          "cited_by_count": 0,
          "topics": [
            "Coronary Interventions and Diagnostics",
            "Cardiac Health and Mental Health",
            "Cardiac Valve Diseases and Treatments"
          ]
        },
        {
          "openalex_id": "W4407224312",
          "year": 2025,
          "title": "Generic Health‐Related Quality of Life of Children With Severe Peanut or Tree Nut Allergy",
          "type": "article",
          "venue": "Acta Paediatrica",
          "cited_by_count": 2,
          "topics": [
            "Food Allergy and Anaphylaxis Research",
            "Eosinophilic Esophagitis",
            "Respiratory and Cough-Related Research"
          ]
        },
        {
          "openalex_id": "W4410100669",
          "year": 2025,
          "title": "Health‐related quality of life in adult‐type ovarian granulosa cell tumor survivors",
          "type": "article",
          "venue": "Acta Obstetricia Et Gynecologica Scandinavica",
          "cited_by_count": 1,
          "topics": [
            "Ovarian cancer diagnosis and treatment",
            "Cancer survivorship and care",
            "PARP inhibition in cancer therapy"
          ]
        },
        {
          "openalex_id": "W4412034995",
          "year": 2025,
          "title": "Resilience and health-related quality of life in patients with pulmonary diseases receiving ambulatory oxygen therapy − 24-month follow-up results",
          "type": "article",
          "venue": "BMC Pulmonary Medicine",
          "cited_by_count": 0,
          "topics": [
            "Chronic Obstructive Pulmonary Disease (COPD) Research",
            "Interstitial Lung Diseases and Idiopathic Pulmonary Fibrosis",
            "Respiratory Support and Mechanisms"
          ]
        },
        {
          "openalex_id": "W4414142288",
          "year": 2025,
          "title": "Swallowing Guidance with FEES May Alleviate Symptoms in Functional Dysphagia",
          "type": "article",
          "venue": "Dysphagia",
          "cited_by_count": 1,
          "topics": [
            "Dysphagia Assessment and Management",
            "Child Nutrition and Feeding Issues",
            "Voice and Speech Disorders"
          ]
        },
        {
          "openalex_id": "W561553940",
          "year": 1973,
          "title": "Vanhusten huoltomuodon valinnasta = Alternatives in the care of old people",
          "type": "book",
          "venue": "Medical Entomology and Zoology",
          "cited_by_count": 2,
          "topics": [
            "Research in Social Sciences"
          ]
        },
        {
          "openalex_id": "W2093075457",
          "year": 1981,
          "title": "An approach to measuring and valuing health states",
          "type": "article",
          "venue": "Social Science & Medicine Part C Medical Economics",
          "cited_by_count": 106,
          "topics": [
            "Global Health Care Issues",
            "Health disparities and outcomes",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1125161323",
          "year": 1984,
          "title": "Julkisten ja yksityisten hammaslääkärien tuottavuus.",
          "type": "other",
          "venue": "STM:n Hallinnonalan avoin julkaisuarkisto (Julkari)",
          "cited_by_count": 1,
          "topics": [
            "Hermeneutics and Narrative Identity",
            "Aging, Elder Care, and Social Issues",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W2026549382",
          "year": 1984,
          "title": "Normative and subjective need and utilization of complete denture services",
          "type": "article",
          "venue": "Community Dentistry And Oral Epidemiology",
          "cited_by_count": 6,
          "topics": [
            "Dental Health and Care Utilization",
            "Dental Education, Practice, Research",
            "Orthodontics and Dentofacial Orthopedics"
          ]
        },
        {
          "openalex_id": "W2168973485",
          "year": 2001,
          "title": "The 15D instrument of health-related quality of life: properties and applications",
          "type": "article",
          "venue": "Annals of Medicine",
          "cited_by_count": 1239,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2154795762",
          "year": 2003,
          "title": "A single European currency for EQ-5D health states",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 465,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2026164114",
          "year": 2006,
          "title": "The Impact of 29 Chronic Conditions on Health-related Quality of Life: A General Population Survey in Finland Using 15D and EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 418,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Musculoskeletal pain and rehabilitation"
          ]
        },
        {
          "openalex_id": "W2069518397",
          "year": 2007,
          "title": "Effectiveness of hip or knee replacement surgery in terms of quality-adjusted life years and costs",
          "type": "article",
          "venue": "Acta Orthopaedica",
          "cited_by_count": 380,
          "topics": [
            "Total Knee Arthroplasty Outcomes",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Orthopaedic implants and arthroplasty"
          ]
        },
        {
          "openalex_id": "W2138305051",
          "year": 2007,
          "title": "Impact of psychiatric disorders on health-related quality of life: general population survey",
          "type": "article",
          "venue": "The British Journal of Psychiatry",
          "cited_by_count": 377,
          "topics": [
            "Mental Health Treatment and Access",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Treatment of Major Depression"
          ]
        },
        {
          "openalex_id": "W1988025689",
          "year": 2009,
          "title": "Nocturia Frequency, Bother, and Quality of Life: How Often Is Too Often? A Population-Based Study in Finland",
          "type": "article",
          "venue": "European Urology",
          "cited_by_count": 348,
          "topics": [
            "Urinary Bladder and Prostate Research",
            "Sleep and related disorders",
            "Sleep and Wakefulness Research"
          ]
        },
        {
          "openalex_id": "W2118996267",
          "year": 2006,
          "title": "Use of quality-adjusted life years for the estimation of effectiveness of health care: A systematic literature review",
          "type": "review",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 300,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Patient Satisfaction in Healthcare"
          ]
        },
        {
          "openalex_id": "W2023078845",
          "year": 2014,
          "title": "Estimating the minimum important change in the 15D scores",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 231,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Frailty in Older Adults"
          ]
        }
      ]
    }
  }
]
