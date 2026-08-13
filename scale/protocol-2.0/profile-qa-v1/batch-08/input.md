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
    "name": "Benedicte Lescrauwaet",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2403-BT",
        "title": "Content validity and cognitive debriefing of the EQ-5D-5L Vision bolt-on in patients with Inherited Retinal Dystrophies",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5076552397",
      "display_name": "Bénédicte Lescrauwaet",
      "orcid": "0000-0002-7976-0330",
      "reported_affiliation": "Ghent University Hospital",
      "works_count": 81,
      "top_topics": [
        {
          "topic": "Retinal and Macular Surgery",
          "works": 25
        },
        {
          "topic": "Hepatitis C virus research",
          "works": 24
        },
        {
          "topic": "Hepatitis B Virus Studies",
          "works": 23
        },
        {
          "topic": "Intraocular Surgery and Lenses",
          "works": 20
        },
        {
          "topic": "Vascular Malformations Diagnosis and Treatment",
          "works": 10
        },
        {
          "topic": "Liver Disease Diagnosis and Treatment",
          "works": 7
        },
        {
          "topic": "HIV/AIDS drug development and treatment",
          "works": 7
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 7
        },
        {
          "topic": "Hepatitis Viruses Studies and Epidemiology",
          "works": 5
        },
        {
          "topic": "Retinal Diseases and Treatments",
          "works": 5
        },
        {
          "topic": "Ophthalmology and Visual Impairment Studies",
          "works": 5
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Luc Duchateau",
          "works": 16
        },
        {
          "name": "Timothy L. Jackson",
          "works": 9
        },
        {
          "name": "Brett Hauber",
          "works": 9
        },
        {
          "name": "K Blot",
          "works": 8
        },
        {
          "name": "F. Reed Johnson",
          "works": 8
        },
        {
          "name": "Craig Bennison",
          "works": 8
        },
        {
          "name": "Thomas Verstraeten",
          "works": 8
        },
        {
          "name": "Hakan Leblebicioğlu",
          "works": 6
        },
        {
          "name": "Victoria Aramă",
          "works": 5
        },
        {
          "name": "Krzysztof Simon",
          "works": 5
        },
        {
          "name": "Isabelle Klauck",
          "works": 5
        },
        {
          "name": "Driss Kamar",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4412442562",
          "year": 2025,
          "title": "PCR107 Differential Item Functioning With the National Eye Institute Visual Function Questionnaire-25 in Patients With Vitreomacular Traction",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Ophthalmology and Visual Impairment Studies",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W4417481343",
          "year": 2025,
          "title": "PCR14 Advancing Patient-Centered Value Assessment in Inherited Retinal Diseases: Leveraging EQ-5D-5L Vision Bolt-ons to Support IRD-Specific PROMs",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Retinal Development and Disorders",
            "Ophthalmology and Visual Impairment Studies",
            "Genomics and Rare Diseases"
          ]
        },
        {
          "openalex_id": "W4402983352",
          "year": 2024,
          "title": "A Causal Inference Approach to Mediation Analysis in Vitreomacular Traction: How Much Does Traction Resolution Mediate Functional Outcomes?",
          "type": "article",
          "venue": "Journal of Market Access & Health Policy",
          "cited_by_count": 0,
          "topics": [
            "Retinal and Macular Surgery",
            "Intraocular Surgery and Lenses",
            "Botulinum Toxin and Related Neurological Disorders"
          ]
        },
        {
          "openalex_id": "W3151444347",
          "year": 2021,
          "title": "Clinical Update on Metamorphopsia: Epidemiology, Diagnosis and Imaging",
          "type": "article",
          "venue": "Current Eye Research",
          "cited_by_count": 18,
          "topics": [
            "Retinal and Macular Surgery",
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis"
          ]
        },
        {
          "openalex_id": "W3197299237",
          "year": 2021,
          "title": "Ocriplasmin for treatment of vitreomacular traction and macular hole: A systematic literature review and individual participant data meta-analysis of randomized, controlled, double-masked trials",
          "type": "review",
          "venue": "Survey of Ophthalmology",
          "cited_by_count": 15,
          "topics": [
            "Retinal and Macular Surgery",
            "Intraocular Surgery and Lenses",
            "Vascular Malformations Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W3001512931",
          "year": 2020,
          "title": "Cost–effectiveness analysis of ocriplasmin versus watchful waiting for treatment of symptomatic vitreomacular adhesion in the US",
          "type": "article",
          "venue": "Journal of Comparative Effectiveness Research",
          "cited_by_count": 1,
          "topics": [
            "Retinal and Macular Surgery",
            "Intraocular Surgery and Lenses",
            "Vascular Malformations Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W2787925934",
          "year": 1991,
          "title": "Voluntary partner notification by persons with HIV infection in a regional center for medical and psychosocial assessment",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions"
          ]
        },
        {
          "openalex_id": "W2022276186",
          "year": 1997,
          "title": "Patient classification and cost analysis of aids and HIV: the case of Belgium",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 7,
          "topics": [
            "HIV/AIDS Impact and Responses",
            "Healthcare Systems and Practices",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W2793171752",
          "year": 1998,
          "title": "Patient classification and cost analysis of aids and HIV: the case of Belgium",
          "type": "article",
          "venue": "RePEc: Research Papers in Economics",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS Research and Interventions",
            "HIV/AIDS Impact and Responses",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        },
        {
          "openalex_id": "W2059080100",
          "year": 2003,
          "title": "PMH7: A MARKOV COHORT SIMULATION ESTIMATING THE RISK OF DEVELOPING CORONARY HEART DISEASE IN PATIENTS USING ANTIPSYCHOTIC DRUGS",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Cardiovascular Disease and Adiposity"
          ]
        },
        {
          "openalex_id": "W2534506121",
          "year": 2004,
          "title": "40th EASD Annual Meeting of the European Association for the Study of Diabetes",
          "type": "article",
          "venue": "Diabetologia",
          "cited_by_count": 68,
          "topics": [
            "Diabetes and associated disorders",
            "Diet and metabolism studies",
            "Adipose Tissue and Metabolism"
          ]
        },
        {
          "openalex_id": "W2029235539",
          "year": 2009,
          "title": "Detection of Cognitive Impairment and Dementia Using the Animal Fluency Test: The DECIDE Study",
          "type": "article",
          "venue": "Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques",
          "cited_by_count": 57,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Nutritional Studies and Diet",
            "Neurological Disease Mechanisms and Treatments"
          ]
        },
        {
          "openalex_id": "W1970461557",
          "year": 2005,
          "title": "Risking Health to Avoid Injections",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 51,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Diabetes Management and Research",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W2312781017",
          "year": 2012,
          "title": "The burden of viral hepatitis C in Europe",
          "type": "article",
          "venue": "European Journal of Gastroenterology & Hepatology",
          "cited_by_count": 32,
          "topics": [
            "Hepatitis C virus research",
            "Diabetes Management and Education",
            "Alcohol Consumption and Health Effects"
          ]
        },
        {
          "openalex_id": "W2897199159",
          "year": 2018,
          "title": "Patient-reported prevalence of metamorphopsia and predictors of vision-related quality of life in vitreomacular traction: a prospective, multi-centre study",
          "type": "article",
          "venue": "Eye",
          "cited_by_count": 25,
          "topics": [
            "Retinal and Macular Surgery",
            "Intraocular Surgery and Lenses",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W1985027889",
          "year": 2014,
          "title": "Multicountry Burden of Chronic Hepatitis C Viral Infection among Those Aware of Their Diagnosis: A Patient Survey",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 24,
          "topics": [
            "Hepatitis C virus research",
            "Diabetes Management and Education",
            "Diabetes, Cardiovascular Risks, and Lipoproteins"
          ]
        },
        {
          "openalex_id": "W2023294022",
          "year": 2013,
          "title": "Chronic Hepatitis B Monitoring and Treatment Patterns in Five European Countries with Different Access and Reimbursement Policies",
          "type": "article",
          "venue": "Antiviral Therapy",
          "cited_by_count": 22,
          "topics": [
            "Hepatitis B Virus Studies",
            "Hepatitis C virus research",
            "Hepatitis Viruses Studies and Epidemiology"
          ]
        }
      ]
    }
  },
  {
    "name": "Benjamin Matthew Craig",
    "member_affiliation": "University of South Florida, Tampa, USA",
    "is_member": true,
    "projects": [
      {
        "project_id": "1769-RA",
        "title": "Valuing EQ-5D-5L and Cognition bolt-on attributes using DCE with Kaizen tasks (VECK): a feasbility study",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "1850-RA",
        "title": "Assessing TIPS Attributes using DCE with Kaizen Tasks: a feasibility study",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2013100",
        "title": "Preference Inversion in the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013130",
        "title": "The Relationship between Time, Sequencing, and Precision: Considerations for Choice Experiments",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015030",
        "title": "Order effects in the EQ-5D item responses",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015290",
        "title": "The Effect of Timing, Duration, and Lifespan on Choice",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016020",
        "title": "EQ DCE: Crowdsourcing innovation in valuation specification",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016720",
        "title": "REDCap Evaluation: Instrument Construction",
        "working_group": "Valuation"
      },
      {
        "project_id": "20170260",
        "title": "Exploring potential innovations in hybrid modeling (REVISED)",
        "working_group": "Valuation"
      },
      {
        "project_id": "2266-TVG",
        "title": "Travel Grant for IAHPR Presentation during the EuroQol Sponsored Session",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2337-RA",
        "title": "Exploring preferences on Toddler and Infant Populations: a latent-scale DCE",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2501-RA",
        "title": "Measuring the strength of preferences on bolt-ons: a DSWG/VWG collaboration",
        "working_group": "Descriptive Systems, Valuation"
      },
      {
        "project_id": "302-EO",
        "title": "Introduction to Latent Classes in Health Valuation: A Workshop Proposal",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "304-PHD",
        "title": "The sequential relief of child health problems: a preference path elicited by a kaizen task",
        "working_group": "Valuation, Education and Outreach"
      },
      {
        "project_id": "464-RA",
        "title": "Acute and Chronic Episodes (ACE) Project",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5029949490",
      "display_name": "Benjamin M. Craig",
      "orcid": "0000-0003-1121-1316",
      "reported_affiliation": "University of South Florida",
      "works_count": 118,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 60
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 40
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 15
        },
        {
          "topic": "Global Health Care Issues",
          "works": 14
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 12
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 9
        },
        {
          "topic": "Childhood Cancer Survivors' Quality of Life",
          "works": 7
        },
        {
          "topic": "Global Cancer Incidence and Screening",
          "works": 6
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 5
        },
        {
          "topic": "Acute Myeloid Leukemia Research",
          "works": 4
        },
        {
          "topic": "Cancer survivorship and care",
          "works": 4
        },
        {
          "topic": "Acute Lymphoblastic Leukemia research",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bryce B. Reeve",
          "works": 13
        },
        {
          "name": "A. Simon Pickard",
          "works": 10
        },
        {
          "name": "Gwendolyn P. Quinn",
          "works": 9
        },
        {
          "name": "Derek S. Brown",
          "works": 9
        },
        {
          "name": "Maksat Jumamyradov",
          "works": 8
        },
        {
          "name": "Oliver Rivero‐Arias",
          "works": 7
        },
        {
          "name": "David Cella",
          "works": 7
        },
        {
          "name": "Ron D. Hays",
          "works": 7
        },
        {
          "name": "Dennis A. Revicki",
          "works": 7
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 7
        },
        {
          "name": "John D. Hartman",
          "works": 6
        },
        {
          "name": "Suzana Karim",
          "works": 5
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7159926856",
          "year": 2026,
          "title": "A direct comparison of the measurement properties of the PROMIS-16 and EQ-5D-5L in the U.S. general population",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Psychometric Methodologies and Testing",
            "Ophthalmology and Visual Impairment Studies"
          ]
        },
        {
          "openalex_id": "W4412196677",
          "year": 2025,
          "title": "Assessing the experimental EuroQol toddler and infant populations (EQ-TIPS) descriptive system: a protocol integrating discrete choice experiment (DCE) surveys in instrument development",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W4407856078",
          "year": 2025,
          "title": "Health valuation protocol for dual discrete choice experiment (dual-DCE) surveys to estimate the effects of different scenarios and attributes on main effects",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 3,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Decision-Making and Behavioral Economics"
          ]
        },
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
          "openalex_id": "W4414035564",
          "year": 2025,
          "title": "The psychometric performance of the EQ-5D-5L composite and component items in the U.S. General population and by age group",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Workplace Health and Well-being"
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
          "openalex_id": "W2414667239",
          "year": 1986,
          "title": "The role of ultrasound in the diagnosis of cyclosporine toxicity in renal transplantation.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 1,
          "topics": [
            "Renal Transplantation Outcomes and Treatments",
            "Transplantation: Methods and Outcomes",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W3046767841",
          "year": 2000,
          "title": "The style and chronology of a group of Sogdian statuettes.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Eurasian Exchange Networks",
            "Ancient and Medieval Archaeology Studies",
            "Linguistics and language evolution"
          ]
        },
        {
          "openalex_id": "W2395415472",
          "year": 2000,
          "title": "Vice president Al Gore's health care agenda and the utilization of medical services: An empirical analysis.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2068269360",
          "year": 2002,
          "title": "Cost-effectiveness of gastric bypass for severe obesity",
          "type": "article",
          "venue": "The American Journal of Medicine",
          "cited_by_count": 170,
          "topics": [
            "Bariatric Surgery and Outcomes",
            "Cardiovascular Function and Risk Factors",
            "Body Contouring and Surgery"
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
          "openalex_id": "W1952332158",
          "year": 2005,
          "title": "Is complementary and alternative medicine (CAM) cost-effective? a systematic review",
          "type": "review",
          "venue": "BMC Complementary and Alternative Medicine",
          "cited_by_count": 233,
          "topics": [
            "Complementary and Alternative Medicine Studies",
            "Acupuncture Treatment Research Studies",
            "Biofield Effects and Biophysics"
          ]
        },
        {
          "openalex_id": "W2009650262",
          "year": 2011,
          "title": "Incidence of the myelodysplastic syndromes using a novel claims-based algorithm: high number of uncaptured cases by cancer registries",
          "type": "article",
          "venue": "Blood",
          "cited_by_count": 220,
          "topics": [
            "Acute Myeloid Leukemia Research",
            "Myeloproliferative Neoplasms: Diagnosis and Treatment",
            "Pneumocystis jirovecii pneumonia detection and treatment"
          ]
        },
        {
          "openalex_id": "W1492877912",
          "year": 2009,
          "title": "Practitioner empathy and the duration of the common cold.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 196,
          "topics": [
            "Empathy and Medical Education",
            "Respiratory and Cough-Related Research",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W2995066679",
          "year": 2019,
          "title": "Reporting Formative Qualitative Research to Support the Development of Quantitative Preference Study Protocols and Corresponding Survey Instruments: Guidelines for Authors and Reviewers",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 180,
          "topics": [
            "Economic and Environmental Valuation",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W2118635087",
          "year": 2014,
          "title": "US Valuation of Health Outcomes Measured Using the PROMIS-29",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 163,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2133540202",
          "year": 2011,
          "title": "Deriving a Preference-Based Measure for Cancer Using the EORTC QLQ-C30",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 159,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Cancer survivorship and care",
            "Economic and Financial Impacts of Cancer"
          ]
        }
      ]
    }
  },
  {
    "name": "Bernhard Michalowsky",
    "member_affiliation": "German Center for Neurodegenerative Diseases (DZNE), Greifswald, Germany & McMaster University, Hamilton, Canada",
    "is_member": true,
    "projects": [
      {
        "project_id": "152-RA",
        "title": "Head-to-head comparison of the EQ-5D-3L and EQ-5D-5L: Psychometric properties in Dementia",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1592-RA",
        "title": "Variability and reliability of the EQ-HWB-S and the EQ-5D-5L when health fluctuates: A mixed-methods study in dementia diseases",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1791-RA",
        "title": "Responsiveness of the EQ-5D-5L self and proxy ratings in dementia diseases (ReDem)",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2002-RA",
        "title": "A mixed-methods psychometric validation of the self and proxy rating of the global cognition bolt-on in patients with Alzheimer's Disease and related dementias in a randomized controlled clinical trial in Germany (Co-Bolt)",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "244-RA",
        "title": "The impact of recent health events and fluctuations in health status on the assessment of health today using the EQ-5D-5L: A mixed-methods study among people with dementia and their caregivers",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "349-RA",
        "title": "Psychometric properties of the EQ-5D in rare ataxia diseases (EQ-5D-ATAX)",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5088093819",
      "display_name": "Bernhard Michalowsky",
      "orcid": "0000-0002-3425-0089",
      "reported_affiliation": "",
      "works_count": 174,
      "top_topics": [
        {
          "topic": "Dementia and Cognitive Impairment Research",
          "works": 91
        },
        {
          "topic": "Geriatric Care and Nursing Homes",
          "works": 47
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 35
        },
        {
          "topic": "Palliative Care and End-of-Life Issues",
          "works": 28
        },
        {
          "topic": "Psychiatric care and mental health services",
          "works": 25
        },
        {
          "topic": "Health and Medical Studies",
          "works": 23
        },
        {
          "topic": "Social and Demographic Issues in Germany",
          "works": 18
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 14
        },
        {
          "topic": "Intergenerational Family Dynamics and Caregiving",
          "works": 10
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 10
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 9
        },
        {
          "topic": "COVID-19 and healthcare impacts",
          "works": 8
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Wolfgang Hoffmann",
          "works": 139
        },
        {
          "name": "Jochen René Thyrian",
          "works": 83
        },
        {
          "name": "Diana Wucherer",
          "works": 50
        },
        {
          "name": "Stefan Teipel",
          "works": 44
        },
        {
          "name": "Anika Rädke",
          "works": 43
        },
        {
          "name": "Moritz Platen",
          "works": 39
        },
        {
          "name": "Tilly Eichler",
          "works": 36
        },
        {
          "name": "Adina Dreier",
          "works": 32
        },
        {
          "name": "Johannes Hertel",
          "works": 31
        },
        {
          "name": "Ingo Kilimann",
          "works": 27
        },
        {
          "name": "Wiebke Mohr",
          "works": 27
        },
        {
          "name": "Ina Zwingmann",
          "works": 24
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7127121596",
          "year": 2026,
          "title": "Patient-reported, psychosocial and health economic outcomes in mild to moderate Friedreich's ataxia: baseline results of the PROFA study",
          "type": "article",
          "venue": "JuSER Publikationsportal",
          "cited_by_count": 0,
          "topics": [
            "Genetic Neurodegenerative Diseases",
            "Mitochondrial Function and Pathology",
            "Amyotrophic Lateral Sclerosis Research"
          ]
        },
        {
          "openalex_id": "W4417230836",
          "year": 2025,
          "title": "Association of cancer with neuropathological markers of Alzheimer's disease and related dementias",
          "type": "article",
          "venue": "Alzheimer s & Dementia Diagnosis Assessment & Disease Monitoring",
          "cited_by_count": 1,
          "topics": [
            "Cancer-related cognitive impairment studies",
            "Dementia and Cognitive Impairment Research",
            "Brain Metastases and Treatment"
          ]
        },
        {
          "openalex_id": "W4406035428",
          "year": 2025,
          "title": "Cost‐effectiveness of a multicomponent intervention against cognitive decline",
          "type": "article",
          "venue": "Alzheimer s & Dementia Translational Research & Clinical Interventions",
          "cited_by_count": 3,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Dementia and Cognitive Impairment Research",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4411436550",
          "year": 2025,
          "title": "Decline in incidence and prevalence of dementia: An analysis of outpatient claims data",
          "type": "article",
          "venue": "Deutsches Ärzteblatt international",
          "cited_by_count": 4,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Health and Medical Studies",
            "Psychiatric care and mental health services"
          ]
        },
        {
          "openalex_id": "W4411240413",
          "year": 2025,
          "title": "Differentiation Between Early and Severe Stages of Dementia in Claims Data Based on Diagnosis, Prescription, and Utilization Patterns",
          "type": "article",
          "venue": "Neurology and Therapy",
          "cited_by_count": 2,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W4415617509",
          "year": 2025,
          "title": "Efficacy and cost‐effectiveness of extended nursing roles in dementia care: Results of the cluster‐randomized trial InDePendent",
          "type": "article",
          "venue": "Alzheimer s & Dementia",
          "cited_by_count": 2,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2133237240",
          "year": 2013,
          "title": "Dementia care management: going new ways in ambulant dementia care within a GP-based randomized controlled intervention trial",
          "type": "article",
          "venue": "International Psychogeriatrics",
          "cited_by_count": 76,
          "topics": [
            "Psychiatric care and mental health services",
            "Health and Medical Studies",
            "Dementia and Cognitive Impairment Research"
          ]
        },
        {
          "openalex_id": "W1694285580",
          "year": 2014,
          "title": "Antipsychotic Drug Treatment in Ambulatory Dementia Care: Prevalence and Correlates",
          "type": "article",
          "venue": "Journal of Alzheimer s Disease",
          "cited_by_count": 13,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Schizophrenia research and treatment",
            "Geriatric Care and Nursing Homes"
          ]
        },
        {
          "openalex_id": "W1409992041",
          "year": 2014,
          "title": "Medication Cost of Persons with Dementia in Primary Care in Germany",
          "type": "article",
          "venue": "Journal of Alzheimer s Disease",
          "cited_by_count": 18,
          "topics": [
            "Pharmaceutical Practices and Patient Outcomes",
            "Medication Adherence and Compliance",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2331294531",
          "year": 2014,
          "title": "Neuropsychiatric symptoms in people screened positive for dementia in primary care",
          "type": "article",
          "venue": "International Psychogeriatrics",
          "cited_by_count": 47,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2738104433",
          "year": 2017,
          "title": "Effectiveness and Safety of Dementia Care Management in Primary Care",
          "type": "article",
          "venue": "JAMA Psychiatry",
          "cited_by_count": 196,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Social and Demographic Issues in Germany"
          ]
        },
        {
          "openalex_id": "W1774972570",
          "year": 2014,
          "title": "Rates of Formal Diagnosis in People Screened Positive for Dementia in Primary Care: Results of the DelpHi-Trial",
          "type": "article",
          "venue": "Journal of Alzheimer s Disease",
          "cited_by_count": 140,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Psychiatric care and mental health services",
            "Health and Medical Studies"
          ]
        },
        {
          "openalex_id": "W3101253521",
          "year": 2020,
          "title": "Effect of the COVID-19 lockdown on disease recognition and utilisation of healthcare services in the older population in Germany: a cross-sectional study",
          "type": "article",
          "venue": "Age and Ageing",
          "cited_by_count": 120,
          "topics": [
            "COVID-19 and healthcare impacts",
            "Telemedicine and Telehealth Implementation",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2967626462",
          "year": 2019,
          "title": "Cost‐effectiveness of a collaborative dementia care management—Results of a cluster‐randomized controlled trial",
          "type": "article",
          "venue": "Alzheimer s & Dementia",
          "cited_by_count": 94,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2079413080",
          "year": 2015,
          "title": "Rates of formal diagnosis of dementia in primary care: The effect of screening",
          "type": "article",
          "venue": "Alzheimer s & Dementia Diagnosis Assessment & Disease Monitoring",
          "cited_by_count": 92,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Geriatric Care and Nursing Homes",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W2597999764",
          "year": 2017,
          "title": "Dementia care management in primary care",
          "type": "article",
          "venue": "Zeitschrift für Gerontologie und Geriatrie",
          "cited_by_count": 85,
          "topics": [
            "Interprofessional Education and Collaboration",
            "Dementia and Cognitive Impairment Research",
            "Palliative Care and End-of-Life Issues"
          ]
        },
        {
          "openalex_id": "W2906233324",
          "year": 2018,
          "title": "Identifying Unmet Needs of Family Dementia Caregivers: Results of the Baseline Assessment of a Cluster-Randomized Controlled Intervention Trial",
          "type": "article",
          "venue": "Journal of Alzheimer s Disease",
          "cited_by_count": 78,
          "topics": [
            "Dementia and Cognitive Impairment Research",
            "Family Caregiving in Mental Illness",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        }
      ]
    }
  },
  {
    "name": "Bernhard Slaap",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20200050",
        "title": "Startup & support cost for the UK 5L valuation study",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5001372652",
      "display_name": "Bernhard Slaap",
      "orcid": "0000-0002-4301-4790",
      "reported_affiliation": "EuroQol Research Foundation",
      "works_count": 8,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 7
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 4
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 2
        },
        {
          "topic": "Global Health Care Issues",
          "works": 2
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 1
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 1
        },
        {
          "topic": "Pharmaceutical Practices and Patient Outcomes",
          "works": 1
        },
        {
          "topic": "Quality and Management Systems",
          "works": 1
        },
        {
          "topic": "Free Radicals and Antioxidants",
          "works": 1
        },
        {
          "topic": "Chemical and Physical Properties in Aqueous Solutions",
          "works": 1
        },
        {
          "topic": "Chemistry and Chemical Engineering",
          "works": 1
        },
        {
          "topic": "Nuclear Engineering Thermal-Hydraulics",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Kristina S. Boye",
          "works": 5
        },
        {
          "name": "Michael Herdman",
          "works": 4
        },
        {
          "name": "Tessa Kennedy‐Martin",
          "works": 4
        },
        {
          "name": "Annushiah Vasan Thakumar",
          "works": 3
        },
        {
          "name": "Xin Zhang",
          "works": 3
        },
        {
          "name": "Jan J.V. Busschbach",
          "works": 2
        },
        {
          "name": "Elly Stolk",
          "works": 2
        },
        {
          "name": "L Cheng",
          "works": 2
        },
        {
          "name": "Xun Li",
          "works": 2
        },
        {
          "name": "Matthew Kennedy-Martin",
          "works": 1
        },
        {
          "name": "Mandy van Reenen",
          "works": 1
        },
        {
          "name": "Wolfgang Greiner",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166049043",
          "year": 2026,
          "title": "EPH226 VALUE SETS FOR AQOL, EQ-5D, HUI, QWB AND SF-6D: A SYSTEMATIC REVIEW OF THEIR AVAILABILITY AND CHARACTERISTICS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Free Radicals and Antioxidants",
            "Chemical and Physical Properties in Aqueous Solutions",
            "Chemistry and Chemical Engineering"
          ]
        },
        {
          "openalex_id": "W7166188896",
          "year": 2026,
          "title": "MSR230 A METHODOLOGICAL REVIEW OF VALUATION STUDIES FOR THE EQ-5D-5L: EVOLVING PRACTICES AND LESSONS FROM THE EQ-5D-3L",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Nuclear Engineering Thermal-Hydraulics",
            "Technology Assessment and Management"
          ]
        },
        {
          "openalex_id": "W4417481651",
          "year": 2025,
          "title": "MSR122 How Far Have We Come With EQ-5D-5L Value Sets? An Updated Systematic Literature Review of 55 Valuation Studies",
          "type": "review",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Quality and Management Systems"
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
          "openalex_id": "W3033327429",
          "year": 2020,
          "title": "Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 307,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2212258744",
          "year": 2015,
          "title": "Validation And Valuation Of The Preference-Based Healthindex Using Eq-5d-5l In The Hong Kong Population",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 18,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Economic and Environmental Valuation"
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
        }
      ]
    }
  },
  {
    "name": "Birol Yetim",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2247-VS",
        "title": "Development of the Turkish Value Set for the EQ-5D-5L Quality of Life Instrument: A Nationally Representative Valuation Study Using the EQ-VT Protocol",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5048427287",
      "display_name": "Birol Yetim",
      "orcid": "0000-0002-1294-1874",
      "reported_affiliation": "Muş Alparslan University",
      "works_count": 28,
      "top_topics": [
        {
          "topic": "Global Health Care Issues",
          "works": 8
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 7
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 6
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 5
        },
        {
          "topic": "Health disparities and outcomes",
          "works": 3
        },
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 3
        },
        {
          "topic": "Suicide and Self-Harm Studies",
          "works": 2
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 2
        },
        {
          "topic": "Job Satisfaction and Organizational Behavior",
          "works": 2
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 2
        },
        {
          "topic": "Insurance, Mortality, Demography, Risk Management",
          "works": 1
        },
        {
          "topic": "Employment and Welfare Studies",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Murat Konca",
          "works": 13
        },
        {
          "name": "Gülnur İlgün",
          "works": 11
        },
        {
          "name": "Şenol Demirci",
          "works": 5
        },
        {
          "name": "Yusuf Çeli̇k",
          "works": 4
        },
        {
          "name": "Seda Sönmez",
          "works": 3
        },
        {
          "name": "Özgür Uğurluoğlu",
          "works": 3
        },
        {
          "name": "Yasin ÇİLHOROZ",
          "works": 2
        },
        {
          "name": "Bayram Şahi̇n",
          "works": 2
        },
        {
          "name": "Gülsün Erigüç",
          "works": 2
        },
        {
          "name": "Ceyhun Türkmen",
          "works": 1
        },
        {
          "name": "Seval Selvi Sarıgül",
          "works": 1
        },
        {
          "name": "İsmail Biçer",
          "works": 1
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7130575945",
          "year": 2026,
          "title": "Effect of Workload, Work Satisfaction, Change Fatigue, and Presenteeism on Quiet Quitting Among Healthcare Professionals: A Structural Equation Modeling Approach",
          "type": "preprint",
          "venue": "SSRN Electronic Journal",
          "cited_by_count": 0,
          "topics": [
            "Workplace Health and Well-being",
            "Healthcare professionals’ stress and burnout",
            "Job Satisfaction and Organizational Behavior"
          ]
        },
        {
          "openalex_id": "W7165416438",
          "year": 2026,
          "title": "Gambling Disorder in Türkiye: A Systematic Review and Meta-Analysis Study",
          "type": "review",
          "venue": "Current Addiction Reports",
          "cited_by_count": 0,
          "topics": [
            "Gambling Behavior and Treatments",
            "Substance Abuse Treatment and Outcomes",
            "Impact of Technology on Adolescents"
          ]
        },
        {
          "openalex_id": "W7161770197",
          "year": 2026,
          "title": "OECD Ülkelerinde Sağlık Sistem Performansı: Türkiye’nin Konumu Üzerine Çok Kriterli Bir İnceleme",
          "type": "article",
          "venue": "İşletme Bilimi Dergisi",
          "cited_by_count": 0,
          "topics": [
            "Global Health Care Issues",
            "Healthcare Systems and Reforms",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4411020177",
          "year": 2025,
          "title": "Addressing disparities: unmet health needs and its impact on health-related quality of life",
          "type": "article",
          "venue": "Psychology Health & Medicine",
          "cited_by_count": 2,
          "topics": [
            "Global Health Workforce Issues",
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4417151436",
          "year": 2025,
          "title": "BIBLIOMETRIC ANALYSIS OF CLINICAL LEADERSHIP STUDIES: TRENDS AND INSIGHTS FROM THE WEB OF SCIENCE",
          "type": "article",
          "venue": "Ege Akademik Bakis (Ege Academic Review)",
          "cited_by_count": 0,
          "topics": [
            "Nursing education and management",
            "Educational Leadership and Innovation",
            "Nursing Education, Practice, and Leadership"
          ]
        },
        {
          "openalex_id": "W4407924620",
          "year": 2025,
          "title": "BRICS-MT ÜLKELERİNDE KRONİK HASTALIK MORTALİTE HIZLARI: BOX-JENKİNS METODU İLE GELECEK PROJEKSİYONU",
          "type": "article",
          "venue": "Dokuz Eylül Üniversitesi Sosyal Bilimler Enstitüsü Dergisi",
          "cited_by_count": 0,
          "topics": [
            "Health Promotion and Cardiovascular Prevention",
            "Chronic Disease Management Strategies",
            "Psychosomatic Disorders and Their Treatments"
          ]
        },
        {
          "openalex_id": "W2796804118",
          "year": 2018,
          "title": "Sağlık Çalışanlarında Sessizlik İle İlgili Yapılan Çalışmalara Yönelik Bir İnceleme",
          "type": "article",
          "venue": "İş ve İnsan Dergisi",
          "cited_by_count": 4,
          "topics": [
            "Public Administration and Governance",
            "Job Satisfaction and Organizational Behavior",
            "Occupational Health and Safety Research"
          ]
        },
        {
          "openalex_id": "W2951928473",
          "year": 2018,
          "title": "Yaşam Memnuniyeti ve Yaşam Kalitesinin Belirleyicileri: Sağlık Hizmetlerinden Memnuniyet ve Sağlık Statüsünün Rolü",
          "type": "dissertation",
          "venue": "Hacettepe University Institutional Repository (hacettepe.edu.tr)",
          "cited_by_count": 2,
          "topics": [
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2978281959",
          "year": 2019,
          "title": "Effect of economic crisis on suicide cases: An ARDL bounds testing approach",
          "type": "article",
          "venue": "International Journal of Social Psychiatry",
          "cited_by_count": 29,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Employment and Welfare Studies",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W2990583932",
          "year": 2019,
          "title": "Individual and socio-demographic determinants of suicide: An examination on WHO countries",
          "type": "article",
          "venue": "International Journal of Social Psychiatry",
          "cited_by_count": 20,
          "topics": [
            "Suicide and Self-Harm Studies",
            "Grief, Bereavement, and Mental Health",
            "Mental Health Treatment and Access"
          ]
        },
        {
          "openalex_id": "W3018775119",
          "year": 2020,
          "title": "The socioeconomic determinants of health expenditure in OECD: An examination on panel data",
          "type": "article",
          "venue": "International Journal of Healthcare Management",
          "cited_by_count": 42,
          "topics": [
            "Global Health Care Issues",
            "Health disparities and outcomes",
            "Insurance, Mortality, Demography, Risk Management"
          ]
        },
        {
          "openalex_id": "W3210760237",
          "year": 2021,
          "title": "Measuring the efficiency of Turkish maternal and child health hospitals: A two-stage data envelopment analysis",
          "type": "article",
          "venue": "Evaluation and Program Planning",
          "cited_by_count": 23,
          "topics": [
            "Efficiency Analysis Using DEA",
            "Healthcare Policy and Management",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W3019888114",
          "year": 2020,
          "title": "Sağlık Hizmetlerine Erişim: Karşılanmamış İhtiyaçlar Sorunu",
          "type": "article",
          "venue": "Toplum ve sosyal hizmet(Online)/Toplum ve sosyal hizmet",
          "cited_by_count": 17,
          "topics": [
            "Healthcare Systems and Reforms",
            "Global Health Care Issues",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2950650919",
          "year": 2019,
          "title": "Sağlık Çalışanlarında Duygusal Emek ile İlgili Yapılan Çalışmalara Yönelik Bir İnceleme",
          "type": "article",
          "venue": "Anadolu Üniversitesi Sosyal Bilimler Dergisi",
          "cited_by_count": 11,
          "topics": [
            "Emotional Labor in Professions",
            "Workplace Violence and Bullying",
            "Emotions and Moral Behavior"
          ]
        },
        {
          "openalex_id": "W3123287611",
          "year": 2021,
          "title": "Socio-Economic Determinants of Infant Mortality Rate in Turkey",
          "type": "article",
          "venue": "Sosyoekonomi",
          "cited_by_count": 10,
          "topics": [
            "Global Health Care Issues",
            "Global Maternal and Child Health",
            "Health disparities and outcomes"
          ]
        },
        {
          "openalex_id": "W4385273627",
          "year": 2023,
          "title": "Benchmarking countries' technical efficiency using AHP-based weighted slack-based measurement (W-SBM): A cross-national perspective",
          "type": "article",
          "venue": "Health Policy and Technology",
          "cited_by_count": 8,
          "topics": [
            "Efficiency Analysis Using DEA",
            "Healthcare Systems and Reforms"
          ]
        }
      ]
    }
  }
]
