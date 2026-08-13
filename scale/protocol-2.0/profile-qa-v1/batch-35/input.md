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
    "name": "Margreet Franken",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "196-RA",
        "title": "Validity of the EQ-5D-3L and EQ-5D-5L in advanced Melanoma",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5089696059",
      "display_name": "M Franken",
      "orcid": "0000-0003-4207-510X",
      "reported_affiliation": "Radboud University Nijmegen",
      "works_count": 104,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 51
        },
        {
          "topic": "Cutaneous Melanoma Detection and Management",
          "works": 26
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 25
        },
        {
          "topic": "Melanoma and MAPK Pathways",
          "works": 17
        },
        {
          "topic": "Multiple Myeloma Research and Treatments",
          "works": 15
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 15
        },
        {
          "topic": "CAR-T cell therapy research",
          "works": 11
        },
        {
          "topic": "Cancer Immunotherapy and Biomarkers",
          "works": 10
        },
        {
          "topic": "Cancer Treatment and Pharmacology",
          "works": 7
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 6
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 6
        },
        {
          "topic": "Protein Degradation and Inhibitors",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Carin A. Uyl‐de Groot",
          "works": 32
        },
        {
          "name": "B Leeneman",
          "works": 31
        },
        {
          "name": "Michel W.J.M. Wouters",
          "works": 29
        },
        {
          "name": "Djura Piersma",
          "works": 28
        },
        {
          "name": "Ellen Kapiteijn",
          "works": 27
        },
        {
          "name": "Gerard Vreugdenhil",
          "works": 27
        },
        {
          "name": "Geke A.P. Hospers",
          "works": 25
        },
        {
          "name": "Hedwig M. Blommestein",
          "works": 24
        },
        {
          "name": "Maureen J.B. Aarts",
          "works": 21
        },
        {
          "name": "Alexander C. J. van Akkooi",
          "works": 21
        },
        {
          "name": "John B.A.G. Haanen",
          "works": 18
        },
        {
          "name": "Marc Koopmanschap",
          "works": 17
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4402558723",
          "year": 2024,
          "title": "2000P Combining whole blood RNA-sequencing (WB-RNA) and circulating tumor DNA (ctDNA) for the early identification of patients (pts) without clinical benefit to immune checkpoint inhibitors (ICI) in metastatic urothelial cancer (mUC)",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 0,
          "topics": [
            "Bladder and Urothelial Cancer Treatments",
            "Cancer Genomics and Diagnostics",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W4392305222",
          "year": 2024,
          "title": "A blueprint for health technology assessment capacity building: lessons learned from Malta",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 2,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Quality and Safety in Healthcare",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4391429636",
          "year": 2024,
          "title": "Applying a cost-based pricing model for innovative cancer treatments subject to indication expansion: A case study for pembrolizumab and daratumumab",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 6,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W4403471421",
          "year": 2024,
          "title": "Cost-effectiveness of treatment sequences for BRAF-mutant advanced melanoma in the Netherlands using a health economic model",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 4,
          "topics": [
            "Melanoma and MAPK Pathways",
            "Cutaneous Melanoma Detection and Management",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4405748231",
          "year": 2024,
          "title": "EE497 Validity of EQ-5D-3L and EQ-5D-5L Using the Fact-M in Patients With Advanced Melanoma",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4402565661",
          "year": 2024,
          "title": "LBA72 Nivolumab 3mg/kg and ipilimumab 1mg/kg (nivo3/ipi1) in molecularly selected patients (pts) with metastatic castration-resistant prostate cancer (mCRPC)",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 0,
          "topics": [
            "Prostate Cancer Treatment and Research",
            "Cancer Immunotherapy and Biomarkers",
            "Radiopharmaceutical Chemistry and Applications"
          ]
        },
        {
          "openalex_id": "W2481186057",
          "year": 2003,
          "title": "Prescribing indicators as a tool to evaluate drug use in nursing homes.",
          "type": "article",
          "venue": "University of Groningen research database (University of Groningen / Centre for Information Technology)",
          "cited_by_count": 1,
          "topics": [
            "Geriatric Care and Nursing Homes",
            "Pharmaceutical Practices and Patient Outcomes"
          ]
        },
        {
          "openalex_id": "W2963682937",
          "year": 2008,
          "title": "Health System Goals: What are the relative preferences in the Netherlands",
          "type": "report",
          "venue": "Data Archiving and Networked Services (DANS)",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2132647523",
          "year": 2009,
          "title": "CN7 TREATMENT VARIATION COMPLICATES REAL-WORLD PHARMACOECONOMICS: DAILY CLINICAL PRACTICE OF BORTEZOMIB IN RELAPSED OR REFRACTORY MULTIPLE MYELOMA",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Chronic Lymphocytic Leukemia Research",
            "Cancer Treatment and Pharmacology"
          ]
        },
        {
          "openalex_id": "W2050655854",
          "year": 2009,
          "title": "PCN18 OUTCOMES RESEARCH OF BORTEZOMIB INDICATED FOR MULTIPLE MYELOMA IN THE CONTEXT OF THE DUTCH REIMBURSEMENT POLICY FOR EXPENSIVE MEDICINES: THREATS TO THE INTERNAL VALIDITY OF THE INCREMENTAL EFFECTIVENESS ESTIMATE",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 3,
          "topics": [
            "Multiple Myeloma Research and Treatments"
          ]
        },
        {
          "openalex_id": "W2592673843",
          "year": 2017,
          "title": "Systematic Literature Review and Network Meta-Analysis of Treatment Outcomes in Relapsed and/or Refractory Multiple Myeloma",
          "type": "review",
          "venue": "Journal of Clinical Oncology",
          "cited_by_count": 127,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Protein Degradation and Inhibitors",
            "Histone Deacetylase Inhibitors Research"
          ]
        },
        {
          "openalex_id": "W2561799613",
          "year": 2016,
          "title": "Dutch Melanoma Treatment Registry: Quality assurance in the care of patients with metastatic melanoma in the Netherlands",
          "type": "article",
          "venue": "European Journal of Cancer",
          "cited_by_count": 107,
          "topics": [
            "Melanoma and MAPK Pathways",
            "Cutaneous Melanoma Detection and Management",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W2038390083",
          "year": 2012,
          "title": "SIMILARITIES AND DIFFERENCES BETWEEN FIVE EUROPEAN DRUG REIMBURSEMENT SYSTEMS",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 75,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Pharmacovigilance and Adverse Drug Reactions"
          ]
        },
        {
          "openalex_id": "W3137718127",
          "year": 2021,
          "title": "Early discontinuation of PD-1 blockade upon achieving a complete or partial response in patients with advanced melanoma: the multicentre prospective Safe Stop trial",
          "type": "article",
          "venue": "BMC Cancer",
          "cited_by_count": 50,
          "topics": [
            "Cancer Immunotherapy and Biomarkers",
            "Melanoma and MAPK Pathways",
            "Cutaneous Melanoma Detection and Management"
          ]
        },
        {
          "openalex_id": "W1784508447",
          "year": 2012,
          "title": "Real-world health care costs of relapsed/refractory multiple myeloma during the era of novel cancer agents",
          "type": "article",
          "venue": "Journal of Clinical Pharmacy and Therapeutics",
          "cited_by_count": 50,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Economic and Financial Impacts of Cancer",
            "Cancer Treatment and Pharmacology"
          ]
        },
        {
          "openalex_id": "W2982112607",
          "year": 2019,
          "title": "A systematic literature review and network meta-analysis of effectiveness and safety outcomes in advanced melanoma",
          "type": "review",
          "venue": "European Journal of Cancer",
          "cited_by_count": 49,
          "topics": [
            "Cutaneous Melanoma Detection and Management",
            "Melanoma and MAPK Pathways",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W2323266321",
          "year": 2016,
          "title": "Balancing the Optimal and the Feasible: A Practical Guide for Setting Up Patient Registries for the Collection of Real-World Data for Health Care Decision Making Based on Dutch Experiences",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 45,
          "topics": [
            "Pharmacovigilance and Adverse Drug Reactions",
            "Electronic Health Records Systems",
            "Pharmaceutical industry and healthcare"
          ]
        },
        {
          "openalex_id": "W1969391254",
          "year": 2013,
          "title": "Health system goals: A discrete choice experiment to obtain societal valuations",
          "type": "article",
          "venue": "Health Policy",
          "cited_by_count": 44,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Systems and Reforms"
          ]
        }
      ]
    }
  },
  {
    "name": "Marisa Da Santos",
    "member_affiliation": "Instituto Nacional de Cardiologia",
    "is_member": true,
    "projects": [
      {
        "project_id": "1445-RA",
        "title": "Assessment of Impact of an NGO Support Program – The Dara Project",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20190630",
        "title": "EUROQOL Satellite Symposium - Applying Quality of life Measurements for Clinical and Economic Research",
        "working_group": "Education and Outreach"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5070231679",
      "display_name": "Marisa Santos",
      "orcid": "0000-0002-2174-6800",
      "reported_affiliation": "Instituto Nacional de Cardiologia",
      "works_count": 164,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 49
        },
        {
          "topic": "Public Health in Brazil",
          "works": 20
        },
        {
          "topic": "Infective Endocarditis Diagnosis and Management",
          "works": 12
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 9
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 7
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 7
        },
        {
          "topic": "Cardiac Valve Diseases and Treatments",
          "works": 6
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 6
        },
        {
          "topic": "Surgical site infection prevention",
          "works": 5
        },
        {
          "topic": "Health Education and Validation",
          "works": 5
        },
        {
          "topic": "Streptococcal Infections and Treatments",
          "works": 5
        },
        {
          "topic": "Health, Nursing, Elderly Care",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Bernardo Rangel Tura",
          "works": 29
        },
        {
          "name": "K. Senna",
          "works": 26
        },
        {
          "name": "Carlos Magliano",
          "works": 23
        },
        {
          "name": "Quenia Cristina Dias Morais",
          "works": 16
        },
        {
          "name": "Márcia Gisele Santos da Costa",
          "works": 12
        },
        {
          "name": "Cristiane da Cruz Lamas",
          "works": 11
        },
        {
          "name": "A Monteiro",
          "works": 10
        },
        {
          "name": "Marcelo Goulart Correia",
          "works": 10
        },
        {
          "name": "G. Ferraiuoli",
          "works": 9
        },
        {
          "name": "Clara Weksler",
          "works": 9
        },
        {
          "name": "B Tura",
          "works": 8
        },
        {
          "name": "W. Golebiovski",
          "works": 7
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7164857449",
          "year": 2026,
          "title": "Cuidados e manejo do potencial doador de órgãos torácicos: protocolo de revisão de escopo",
          "type": "article",
          "venue": "Global Academic Nursing Journal",
          "cited_by_count": 0,
          "topics": [
            "Organ Donation and Transplantation",
            "Transplantation: Methods and Outcomes",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W7167908602",
          "year": 2026,
          "title": "Genetic testing versus clinical screening for relatives of patients with hypertrophic cardiomyopathy in the Brazilian public health system: a cost-utility analysis",
          "type": "article",
          "venue": "The Lancet Global Health",
          "cited_by_count": 0,
          "topics": [
            "Cardiomyopathy and Myosin Studies",
            "Genomics and Rare Diseases",
            "Cardiovascular Effects of Exercise"
          ]
        },
        {
          "openalex_id": "W7167492013",
          "year": 2026,
          "title": "Health utility values in myasthenia gravis: a systematic review of health-related quality of life evidence and estimations for Brazilian economic models",
          "type": "review",
          "venue": "HTA Journal",
          "cited_by_count": 0,
          "topics": [
            "Myasthenia Gravis and Thymoma",
            "Fibromyalgia and Chronic Fatigue Syndrome Research",
            "Parkinson's Disease and Spinal Disorders"
          ]
        },
        {
          "openalex_id": "W4410916057",
          "year": 2025,
          "title": "Adjusting Health State Utility Values for Multiple Conditions: Real-World EQ-5D-3L Data Modeling in Brazil",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W4416021299",
          "year": 2025,
          "title": "Assessing the Impact of a Social Program Using EQ-HWB-9 and EQ-5D-5L: The Dara Project",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W4412785951",
          "year": 2025,
          "title": "Cost-effectiveness assessment of liquid biopsy for early detection of lung cancer in Brazil",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 2,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Lung Cancer Treatments and Mutations",
            "Cancer Immunotherapy and Biomarkers"
          ]
        },
        {
          "openalex_id": "W2289241457",
          "year": 1944,
          "title": "Endocarditis and Septicaemia due to Corynebacterium haemolyticum n. sp.",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Diphtheria, Corynebacterium, and Tetanus",
            "Mycobacterium research and diagnosis",
            "Bacterial Identification and Susceptibility Testing"
          ]
        },
        {
          "openalex_id": "W2338678260",
          "year": 1996,
          "title": "Estimulaçao cardíaca atrioventricular sincrônica através de um eletrodo flutuante único (Modo VDD)",
          "type": "article",
          "venue": "DOAJ (DOAJ: Directory of Open Access Journals)",
          "cited_by_count": 2,
          "topics": [
            "Cardiac pacing and defibrillation studies"
          ]
        },
        {
          "openalex_id": "W1979025463",
          "year": 1997,
          "title": "Proposição de técnica endocavitária para remodelamento ventricular esquerdo",
          "type": "article",
          "venue": "Brazilian Journal of Cardiovascular Surgery",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Structural Anomalies and Repair",
            "Cardiac Valve Diseases and Treatments",
            "Mechanical Circulatory Support Devices"
          ]
        },
        {
          "openalex_id": "W2117432589",
          "year": 1999,
          "title": "Emergence of mupirocin resistance in multiresistant Staphylococcus aureus clinical isolates belonging to Brazilian epidemic clone III::B:A",
          "type": "article",
          "venue": "Journal of Medical Microbiology",
          "cited_by_count": 24,
          "topics": [
            "Antimicrobial Resistance in Staphylococcus",
            "Ocular Infections and Treatments",
            "Bacterial biofilms and quorum sensing"
          ]
        },
        {
          "openalex_id": "W2173668850",
          "year": 2015,
          "title": "Brazilian Valuation of EQ-5D-3L Health States",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 139,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Global Health Care Issues"
          ]
        },
        {
          "openalex_id": "W2129921345",
          "year": 2014,
          "title": "Impact of Early Valve Surgery on Outcome of Staphylococcus aureus Prosthetic Valve Infective Endocarditis: Analysis in the International Collaboration of Endocarditis–Prospective Cohort Study",
          "type": "article",
          "venue": "Clinical Infectious Diseases",
          "cited_by_count": 113,
          "topics": [
            "Infective Endocarditis Diagnosis and Management",
            "Cardiac Valve Diseases and Treatments",
            "Surgical site infection prevention"
          ]
        },
        {
          "openalex_id": "W2970690326",
          "year": 2019,
          "title": "Systematic review of dengue vaccine efficacy",
          "type": "review",
          "venue": "BMC Infectious Diseases",
          "cited_by_count": 75,
          "topics": [
            "Mosquito-borne diseases and control",
            "Viral Infections and Outbreaks Research",
            "Indigenous Health and Education"
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
          "openalex_id": "W3166961211",
          "year": 2021,
          "title": "EQ-5D Brazilian population norms",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 49,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W3092850450",
          "year": 2020,
          "title": "Health state utility values in people living with HTLV-1 and in patients with HAM/TSP: The impact of a neglected disease on the quality of life",
          "type": "article",
          "venue": "PLoS neglected tropical diseases",
          "cited_by_count": 39,
          "topics": [
            "T-cell and Retrovirus Studies",
            "Leptospirosis research and findings",
            "Vector-Borne Animal Diseases"
          ]
        },
        {
          "openalex_id": "W1973818145",
          "year": 2012,
          "title": "Bartonella and Coxiella infective endocarditis in Brazil: molecular evidence from excised valves from a cardiac surgery referral center in Rio de Janeiro, Brazil, 1998 to 2009",
          "type": "article",
          "venue": "International Journal of Infectious Diseases",
          "cited_by_count": 38,
          "topics": [
            "Bartonella species infections research",
            "Streptococcal Infections and Treatments",
            "Rabies epidemiology and control"
          ]
        },
        {
          "openalex_id": "W1954213316",
          "year": 2014,
          "title": "Viability of human adenovirus from hospital fomites",
          "type": "article",
          "venue": "Journal of Medical Virology",
          "cited_by_count": 37,
          "topics": [
            "Viral gastroenteritis research and epidemiology",
            "Infection Control and Ventilation",
            "Virus-based gene therapy research"
          ]
        }
      ]
    }
  },
  {
    "name": "Mark Oppe",
    "member_affiliation": "EuroQol Research Foundation",
    "is_member": true,
    "projects": [
      {
        "project_id": "2013220",
        "title": "Feasibility of the use of EQ-5D in quantitative benefit-risk assessment",
        "working_group": "Others"
      },
      {
        "project_id": "2015300",
        "title": "QALY-balanced DCE designs for health state evaluations",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016140",
        "title": "Two small DCE projects",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016590",
        "title": "Extension of Variability in DCE Results Ð October 2016",
        "working_group": "Valuation"
      },
      {
        "project_id": "452-RA",
        "title": "Behavioural Groups for composite TTO data",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5023709885",
      "display_name": "Mark Oppe",
      "orcid": "0000-0003-4286-8855",
      "reported_affiliation": "Erasmus MC",
      "works_count": 109,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 72
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 38
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 11
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 11
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 10
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 7
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 6
        },
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 6
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 5
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 5
        },
        {
          "topic": "Decision-Making and Behavioral Economics",
          "works": 5
        },
        {
          "topic": "Patient Satisfaction in Healthcare",
          "works": 4
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Elly Stolk",
          "works": 19
        },
        {
          "name": "Oliver Rivero‐Arias",
          "works": 16
        },
        {
          "name": "Maureen Rutten‐van Mölken",
          "works": 15
        },
        {
          "name": "Juan Manuel Ramos-Goñi",
          "works": 14
        },
        {
          "name": "Nancy Devlin",
          "works": 13
        },
        {
          "name": "Louise Longworth",
          "works": 11
        },
        {
          "name": "Koonal Shah",
          "works": 9
        },
        {
          "name": "Stavros Petrou",
          "works": 9
        },
        {
          "name": "Helen Dakin",
          "works": 9
        },
        {
          "name": "Robert Froud",
          "works": 9
        },
        {
          "name": "Alastair Gray",
          "works": 9
        },
        {
          "name": "Leander R. Buisman",
          "works": 9
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4408482511",
          "year": 2025,
          "title": "How do Design Characteristics Affect Respondent Engagement? Assessing Attribute Non-attendance in Discrete Choice Experiments Valuing the EQ-5D-5L",
          "type": "article",
          "venue": "Patient",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4387660890",
          "year": 2023,
          "title": "ASO Visual Abstract: Characteristics Predicting Short-Term and Long-Term, Health-Related Quality of Life in Patients with Esophageal Cancer After Neoadjuvant Chemoradiotherapy and Esophagectomy",
          "type": "article",
          "venue": "Annals of Surgical Oncology",
          "cited_by_count": 0,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Esophageal and GI Pathology"
          ]
        },
        {
          "openalex_id": "W4385879130",
          "year": 2023,
          "title": "Characteristics Predicting Short-Term and Long-Term Health-Related Quality of Life in Patients with Esophageal Cancer After Neoadjuvant Chemoradiotherapy and Esophagectomy",
          "type": "article",
          "venue": "Annals of Surgical Oncology",
          "cited_by_count": 9,
          "topics": [
            "Esophageal Cancer Research and Treatment",
            "Gastric Cancer Management and Outcomes",
            "Esophageal and GI Pathology"
          ]
        },
        {
          "openalex_id": "W4312065748",
          "year": 2022,
          "title": "Budget impact of introducing subcutaneous vedolizumab as a maintenance therapy in biologic-naïve and biologic-experienced patients with ulcerative colitis in France",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 8,
          "topics": [
            "Inflammatory Bowel Disease",
            "Biosimilars and Bioanalytical Methods",
            "Clostridium difficile and Clostridium perfringens research"
          ]
        },
        {
          "openalex_id": "W4225004644",
          "year": 2022,
          "title": "Cost Effectiveness of Subcutaneous Vedolizumab for Maintenance Treatment of Ulcerative Colitis in Canada",
          "type": "article",
          "venue": "PharmacoEconomics - Open",
          "cited_by_count": 11,
          "topics": [
            "Inflammatory Bowel Disease",
            "Biosimilars and Bioanalytical Methods",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W4220830129",
          "year": 2022,
          "title": "Does Changing the Age of a Child to be Considered in 3-Level Version of EQ-5D-Y Discrete Choice Experiment–Based Valuation Studies Affect Health Preferences?",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 26,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Decision-Making and Behavioral Economics"
          ]
        },
        {
          "openalex_id": "W2076854401",
          "year": 2003,
          "title": "PRK13: DEVELOPMENT OF A QUESTIONNAIRE TO ASSESS QUALITY OF CARE IN DUTCH DIALYSIS CENTERS",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1986622725",
          "year": 2005,
          "title": "Development of a questionnaire to assess the quality of care in Dutch dialysis centers from the patient’s perspective",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 1,
          "topics": [
            "Patient Satisfaction in Healthcare",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Medical Malpractice and Liability Issues"
          ]
        },
        {
          "openalex_id": "W2085149262",
          "year": 2006,
          "title": "1110 A systematic review of the cost-effectiveness of echocardiography as a diagnostic technique for the detection of coronary artery disease",
          "type": "article",
          "venue": "European Journal of Echocardiography",
          "cited_by_count": 0,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Cardiovascular Disease and Adiposity"
          ]
        },
        {
          "openalex_id": "W178793739",
          "year": 2007,
          "title": "Comparative review of Time Trade-Off value sets",
          "type": "book-chapter",
          "venue": "",
          "cited_by_count": 25,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W1466167365",
          "year": 2007,
          "title": "EQ-5D value sets : inventory, comparative review, and user guide",
          "type": "other",
          "venue": "",
          "cited_by_count": 499,
          "topics": [
            "Product Development and Customization",
            "Manufacturing Process and Optimization"
          ]
        },
        {
          "openalex_id": "W2123969858",
          "year": 2014,
          "title": "A Program of Methodological Research to Arrive at the New International EQ-5D-5L Valuation Protocol",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 439,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Quality and Management",
            "Patient-Provider Communication in Healthcare"
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
          "openalex_id": "W3000338306",
          "year": 2020,
          "title": "A French Value Set for the EQ-5D-5L",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 164,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Economic and Financial Impacts of Cancer"
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
    "name": "Mark Sculpher",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20180710",
        "title": "Valuation of EQ-5D-5L in Uganda and exploration of a ‘lite’ protocol",
        "working_group": "Valuation"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5060049178",
      "display_name": "Mark Sculpher",
      "orcid": "0000-0003-3746-9913",
      "reported_affiliation": "University of York",
      "works_count": 640,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 285
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 78
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 71
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 55
        },
        {
          "topic": "Global Health Care Issues",
          "works": 38
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 28
        },
        {
          "topic": "HIV/AIDS Research and Interventions",
          "works": 27
        },
        {
          "topic": "Cardiac Imaging and Diagnostics",
          "works": 22
        },
        {
          "topic": "Acute Myocardial Infarction Research",
          "works": 22
        },
        {
          "topic": "Cardiac, Anesthesia and Surgical Outcomes",
          "works": 21
        },
        {
          "topic": "Coronary Interventions and Diagnostics",
          "works": 21
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 19
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Karl Claxton",
          "works": 106
        },
        {
          "name": "Simon Walker",
          "works": 59
        },
        {
          "name": "Laura Bojke",
          "works": 57
        },
        {
          "name": "Stephen Palmer",
          "works": 50
        },
        {
          "name": "Nerys Woolacott",
          "works": 50
        },
        {
          "name": "Andrew Briggs",
          "works": 47
        },
        {
          "name": "Susan Griffin",
          "works": 44
        },
        {
          "name": "Andrea Manca",
          "works": 39
        },
        {
          "name": "Keith R. Abrams",
          "works": 37
        },
        {
          "name": "Paul Revill",
          "works": 35
        },
        {
          "name": "Beth Woods",
          "works": 34
        },
        {
          "name": "Eldon Spackman",
          "works": 34
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7133048404",
          "year": 2026,
          "title": "Alternative pricing policies for multi-indication products: a quantitative analysis",
          "type": "article",
          "venue": "White Rose Research Online (University of Leeds, The University of Sheffield, University of York)",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W7124741329",
          "year": 2026,
          "title": "Reply to “On Selection and Analytical Transparency in the <scp>FRAME</scp> Framework for <scp>RWE</scp> Evaluation”",
          "type": "letter",
          "venue": "Clinical Pharmacology & Therapeutics",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Advanced Causal Inference Techniques",
            "Psychometric Methodologies and Testing"
          ]
        },
        {
          "openalex_id": "W7118406154",
          "year": 2026,
          "title": "Revised methods guide for economic evaluation studies of health technologies in Portugal",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Global Health Care Issues",
            "Healthcare Systems and Reforms"
          ]
        },
        {
          "openalex_id": "W4411177350",
          "year": 2025,
          "title": "<scp>FRAME</scp>: Framework for Real‐World Evidence Assessment to Mitigate Evidence Uncertainties for Efficacy/Effectiveness – An Evaluation of Regulatory and Health Technology Assessment Decision Making",
          "type": "article",
          "venue": "Clinical Pharmacology & Therapeutics",
          "cited_by_count": 7,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W4414521800",
          "year": 2025,
          "title": "A0075 – IP9 – ATLAS (Approaches To Long-term Active Surveillance): A randomised controlled trial of regular MRI scans versus standard care in patients with low to intermediate risk prostate cancer on active surveillance",
          "type": "conference-abstract",
          "venue": "European Urology",
          "cited_by_count": 0,
          "topics": [
            "Radiomics and Machine Learning in Medical Imaging",
            "Cardiac Imaging and Diagnostics",
            "Prostate Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W4417480788",
          "year": 2025,
          "title": "CO26 Bayesian Dynamic Borrowing to Enhance Evidence for New Therapies",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Statistical Methods in Clinical Trials",
            "Multiple Sclerosis Research Studies",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W1970726206",
          "year": 1991,
          "title": "A Relative Cost‐effectiveness Analysis of Different Methods of Screening for Diabetic Retinopathy",
          "type": "article",
          "venue": "Diabetic Medicine",
          "cited_by_count": 51,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Retinal and Optic Conditions"
          ]
        },
        {
          "openalex_id": "W2044756904",
          "year": 1991,
          "title": "Cost implications of alternative treatments for aids patients with cryptococcal meningitis. Comparison of fluconazole and amphotericin b-based therapies",
          "type": "article",
          "venue": "Journal of Infection",
          "cited_by_count": 16,
          "topics": [
            "Fungal Infections and Studies",
            "Delphi Technique in Research",
            "Antifungal resistance and susceptibility"
          ]
        },
        {
          "openalex_id": "W2167236074",
          "year": 1991,
          "title": "Do patient charge increases reduce the use of prescription medicines? An economic perspective",
          "type": "article",
          "venue": "Public Money & Management",
          "cited_by_count": 0,
          "topics": [
            "Healthcare Policy and Management",
            "Global Health Care Issues",
            "Primary Care and Health Outcomes"
          ]
        },
        {
          "openalex_id": "W2000296091",
          "year": 1991,
          "title": "Screening for Treatable Diabetic Retinopathy: a Comparison of Different Methods",
          "type": "article",
          "venue": "Diabetic Medicine",
          "cited_by_count": 166,
          "topics": [
            "Retinal Diseases and Treatments",
            "Retinal Imaging and Analysis",
            "Glaucoma and retinal disorders"
          ]
        },
        {
          "openalex_id": "W85469694",
          "year": 2006,
          "title": "Decision Modelling For Health Economic Evaluation",
          "type": "book",
          "venue": "",
          "cited_by_count": 3128,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2519603001",
          "year": 2016,
          "title": "Recommendations for Conduct, Methodological Practices, and Reporting of Cost-effectiveness Analyses",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 3052,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2106203584",
          "year": 2001,
          "title": "Representing uncertainty: the role of cost‐effectiveness acceptability curves",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 1119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Delphi Technique in Research"
          ]
        },
        {
          "openalex_id": "W2118249259",
          "year": 2004,
          "title": "Estimating mean QALYs in trial‐based cost‐effectiveness analysis: the importance of controlling for baseline utility",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 1069,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Meta-analysis and systematic reviews"
          ]
        },
        {
          "openalex_id": "W2115787220",
          "year": 1998,
          "title": "Primary total hip replacement surgery: a systematic review of outcomes and modelling of cost-effectiveness associated with different prostheses.",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 972,
          "topics": [
            "Orthopaedic implants and arthroplasty",
            "Total Knee Arthroplasty Outcomes",
            "Orthopedic Infections and Treatments"
          ]
        },
        {
          "openalex_id": "W2122664355",
          "year": 1998,
          "title": "An Introduction to Markov Modelling for Economic Evaluation",
          "type": "article",
          "venue": "PharmacoEconomics",
          "cited_by_count": 968,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2286756681",
          "year": 2016,
          "title": "Country-Level Cost-Effectiveness Thresholds: Initial Estimates and the Need for Further Research",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 935,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Global Maternal and Child Health"
          ]
        },
        {
          "openalex_id": "W2013329800",
          "year": 2012,
          "title": "Model Parameter Estimation and Uncertainty Analysis",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 893,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        }
      ]
    }
  },
  {
    "name": "Martijn Doeleman",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2101-EO",
        "title": "Towards A Continuum of Care for Juvenile Idiopathic Arthritis: Innovative Strategies regarding Monitoring and Treatment",
        "working_group": "Dissemination, OA fee"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5038383689",
      "display_name": "Martijn J. H. Doeleman",
      "orcid": "0000-0003-4786-4108",
      "reported_affiliation": "Utrecht University",
      "works_count": 13,
      "top_topics": [
        {
          "topic": "Autoimmune and Inflammatory Disorders Research",
          "works": 9
        },
        {
          "topic": "Rheumatoid Arthritis Research and Therapies",
          "works": 6
        },
        {
          "topic": "Adolescent and Pediatric Healthcare",
          "works": 5
        },
        {
          "topic": "Biosimilars and Bioanalytical Methods",
          "works": 4
        },
        {
          "topic": "Clinical Laboratory Practices and Quality Control",
          "works": 2
        },
        {
          "topic": "Family and Disability Support Research",
          "works": 2
        },
        {
          "topic": "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
          "works": 1
        },
        {
          "topic": "Systemic Lupus Erythematosus Research",
          "works": 1
        },
        {
          "topic": "Inflammatory Biomarkers in Disease Prognosis",
          "works": 1
        },
        {
          "topic": "Ocular Diseases and Behçet’s Syndrome",
          "works": 1
        },
        {
          "topic": "Spondyloarthritis Studies and Treatments",
          "works": 1
        },
        {
          "topic": "Blood groups and transfusion",
          "works": 1
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Sytze de Roock",
          "works": 10
        },
        {
          "name": "Joost F. Swart",
          "works": 9
        },
        {
          "name": "Nico Wulffraat",
          "works": 7
        },
        {
          "name": "Wouter M. Tiel Groenestege",
          "works": 3
        },
        {
          "name": "Susanne M Benseler",
          "works": 3
        },
        {
          "name": "Anouk Esseveld",
          "works": 2
        },
        {
          "name": "Erik M. van Maarseveen",
          "works": 2
        },
        {
          "name": "Nathan Buijsse",
          "works": 2
        },
        {
          "name": "Mark Klein",
          "works": 2
        },
        {
          "name": "Gouke J. Bonsel",
          "works": 2
        },
        {
          "name": "Maarten J. IJzerman",
          "works": 2
        },
        {
          "name": "Marinka Twilt",
          "works": 2
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4413506571",
          "year": 2025,
          "title": "Comparison of capillary dried blood spot and capillary microtubes with venous immunoglobulin G levels for routine diagnostics",
          "type": "article",
          "venue": "Clinical Biochemistry",
          "cited_by_count": 2,
          "topics": [
            "Biosimilars and Bioanalytical Methods",
            "Blood groups and transfusion",
            "Immunodeficiency and Autoimmune Disorders"
          ]
        },
        {
          "openalex_id": "W4409982922",
          "year": 2025,
          "title": "Towards a Continuum of Care for Juvenile Idiopathic Arthritis",
          "type": "dissertation",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Adolescent and Pediatric Healthcare",
            "Autoimmune and Inflammatory Disorders Research",
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W7149215551",
          "year": 2025,
          "title": "Towards a Continuum of Care for Juvenile Idiopathic Arthritis: Innovative strategies regarding monitoring and treatment",
          "type": "dissertation",
          "venue": "Utrecht University Repository (Utrecht University)",
          "cited_by_count": 0,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Biosimilars and Bioanalytical Methods"
          ]
        },
        {
          "openalex_id": "W4396704557",
          "year": 2024,
          "title": "Adherence to low-dose methotrexate in children with juvenile idiopathic arthritis using a sensitive methotrexate assay",
          "type": "article",
          "venue": "Pediatric Rheumatology",
          "cited_by_count": 1,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Adolescent and Pediatric Healthcare"
          ]
        },
        {
          "openalex_id": "W4392502059",
          "year": 2024,
          "title": "Adherence to low-dose methotrexate in children with juvenile idiopathic arthritis using a sensitive methotrexate assay",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Adolescent and Pediatric Healthcare",
            "Acute Lymphoblastic Leukemia research"
          ]
        },
        {
          "openalex_id": "W4404560591",
          "year": 2024,
          "title": "Comparison of capillary finger stick and venous blood sampling for 34 routine chemistry analytes: potential for in hospital and remote blood sampling",
          "type": "article",
          "venue": "Clinical Chemistry and Laboratory Medicine (CCLM)",
          "cited_by_count": 21,
          "topics": [
            "Clinical Laboratory Practices and Quality Control",
            "Biosimilars and Bioanalytical Methods",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients"
          ]
        },
        {
          "openalex_id": "W2336758010",
          "year": 2015,
          "title": "Cardiac Regeneration and microRNAs: Regulators of Pluripotency, Reprogramming, and Cardiovascular Lineage Commitment",
          "type": "book-chapter",
          "venue": "Stem cell biology and regenerative medicine",
          "cited_by_count": 0,
          "topics": [
            "Pluripotent Stem Cells Research",
            "Tissue Engineering and Regenerative Medicine",
            "MicroRNA in disease regulation"
          ]
        },
        {
          "openalex_id": "W2917936278",
          "year": 2019,
          "title": "Immunogenicity of biologic agents in juvenile idiopathic arthritis: a systematic review and meta-analysis",
          "type": "review",
          "venue": "Lara D. Veeken",
          "cited_by_count": 61,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Systemic Lupus Erythematosus Research"
          ]
        },
        {
          "openalex_id": "W2951524052",
          "year": 2019,
          "title": "SAT0494 HOME MONITORING OF INACTIVE DISEASE IN CHILDREN WITH JUVENILE IDIOPATHIC ARTHRITIS: PREDICTIVE VALUE OF EQ-5D-5L-Y",
          "type": "article",
          "venue": "Annals of the Rheumatic Diseases",
          "cited_by_count": 3,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Adolescent and Pediatric Healthcare",
            "Family and Disability Support Research"
          ]
        },
        {
          "openalex_id": "W3155426166",
          "year": 2021,
          "title": "Association of adalimumab trough concentrations and treatment response in patients with juvenile idiopathic arthritis",
          "type": "article",
          "venue": "Lara D. Veeken",
          "cited_by_count": 8,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Ocular Diseases and Behçet’s Syndrome"
          ]
        },
        {
          "openalex_id": "W4367669139",
          "year": 2023,
          "title": "Stability and comparison of complete blood count parameters between capillary and venous blood samples",
          "type": "article",
          "venue": "International Journal of Laboratory Hematology",
          "cited_by_count": 26,
          "topics": [
            "Clinical Laboratory Practices and Quality Control",
            "Inflammatory Biomarkers in Disease Prognosis",
            "Biosimilars and Bioanalytical Methods"
          ]
        },
        {
          "openalex_id": "W3138174213",
          "year": 2021,
          "title": "Monitoring patients with juvenile idiopathic arthritis using health-related quality of life",
          "type": "article",
          "venue": "Pediatric Rheumatology",
          "cited_by_count": 19,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Adolescent and Pediatric Healthcare",
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W4390058863",
          "year": 2023,
          "title": "Quantifying hospital-associated costs, and accompanying travel costs and productivity losses, before and after withdrawing TNF-α inhibitors in juvenile idiopathic arthritis",
          "type": "article",
          "venue": "Lara D. Veeken",
          "cited_by_count": 6,
          "topics": [
            "Autoimmune and Inflammatory Disorders Research",
            "Rheumatoid Arthritis Research and Therapies",
            "Spondyloarthritis Studies and Treatments"
          ]
        }
      ]
    }
  }
]
