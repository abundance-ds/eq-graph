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
    "name": "Federico Augustovski",
    "member_affiliation": "Institute for Clinical Effectiveness and Health Policy (IECS)",
    "is_member": true,
    "projects": [
      {
        "project_id": "1605-RA",
        "title": "Back to basics: a qualitative review to disentangle the concepts of health related quality of life, quality of life and wellbeing, and how the EuroQol family of instruments as well as commonly used generic measures capture these concepts",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "1891-RA",
        "title": "Content Validity of the Experimental and Modified EQ-HWB S versions in Argentina: Moving One Step Closer to Prime Time.",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2012-RA",
        "title": "Killing two birds with one stone? Psychometric assessment of EQ-HWB-S, cognition bolt-ons and EQ-5D-5L in a large nursing home setting in Argentina.",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2013070",
        "title": "Deriving social values using the EQ-5D-5L in the general population of Uruguay.",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015-RA",
        "title": "Systematic Review on Empirical Testing of Constant Proportionality-Linear Utility Function in Preferences for Individual or Societal Health",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016360",
        "title": "Health related quality of life measurement -uses in economic evaluation and population health.",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20170170",
        "title": "Deriving Social Values for the EQ-5D 5L in Peru implementing a “Lite” protocol",
        "working_group": "Valuation"
      },
      {
        "project_id": "20170660",
        "title": "Extending the QALY. Stage 3: Testing face and content validity with patients, social-care users and carers in Argentin",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "20180580",
        "title": "EQALY International Psychometric Analysis: Argentina study",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "2119-RA",
        "title": "Translation of the EQ-TIPS experimental version (V.3.0) in Spanish for Argentina and development of the digital and paper-based version mok-ups both for 3L and 5L versions.",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5053077563",
      "display_name": "Federico Augustovski",
      "orcid": "0000-0002-2914-5022",
      "reported_affiliation": "Instituto de Efectividad Clínica y Sanitaria",
      "works_count": 341,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 162
        },
        {
          "topic": "Global Public Health Policies and Epidemiology",
          "works": 44
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 41
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 40
        },
        {
          "topic": "Healthcare cost, quality, practices",
          "works": 37
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 29
        },
        {
          "topic": "Global Health Care Issues",
          "works": 17
        },
        {
          "topic": "Smoking Behavior and Cessation",
          "works": 16
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 16
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 15
        },
        {
          "topic": "Health and Lifestyle Studies",
          "works": 13
        },
        {
          "topic": "Blood Pressure and Hypertension Studies",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Andrés Pichón-Rivière",
          "works": 149
        },
        {
          "name": "Andrea Alcaraz",
          "works": 82
        },
        {
          "name": "Ariel Bardach",
          "works": 81
        },
        {
          "name": "Sebastián García Martí",
          "works": 77
        },
        {
          "name": "Alfredo Palacios",
          "works": 55
        },
        {
          "name": "Michael Drummond",
          "works": 46
        },
        {
          "name": "Joaquín Caporale",
          "works": 37
        },
        {
          "name": "Don Husereau",
          "works": 36
        },
        {
          "name": "Josephine Mauskopf",
          "works": 35
        },
        {
          "name": "Dan Greenberg",
          "works": 34
        },
        {
          "name": "Chris Carswell",
          "works": 33
        },
        {
          "name": "Andrew Briggs",
          "works": 33
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7166149928",
          "year": 2026,
          "title": "Carga da doença, social e econômica do tabagismo no Brasil e impacto do aumento de impostos para a economia e para a redução da morbimortalidade",
          "type": "article",
          "venue": "Cadernos de Saúde Pública",
          "cited_by_count": 0,
          "topics": [
            "Smoking Behavior and Cessation",
            "Youth, Drugs, and Violence",
            "Global Public Health Policies and Epidemiology"
          ]
        },
        {
          "openalex_id": "W7167275189",
          "year": 2026,
          "title": "Content validity of the modified EQ-HWB-9 in a sample of Argentinean patients, informal caregivers, and members of the general public",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7169695289",
          "year": 2025,
          "title": "A Delphi study on valuing DNA sequencing in oncology: a European stakeholder developed framework for assessing next generation sequencing and comprehensive genomic profiling diagnostics",
          "type": "article",
          "venue": "CONICET Digital (CONICET)",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "BRCA gene mutations in cancer",
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4412094588",
          "year": 2025,
          "title": "Conceptual Mapping of Health-Related Quality of Life, Quality of Life, and Wellbeing: A Systematic Review and Assessment of Commonly Used Patient-Reported Outcomes Measures",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4412024234",
          "year": 2025,
          "title": "Disease burden from tobacco consumption in Peru and the projected effect of strengthening control measures: a modeling study",
          "type": "article",
          "venue": "Revista Peruana de Medicina Experimental y Salud Pública",
          "cited_by_count": 1,
          "topics": [
            "Smoking Behavior and Cessation",
            "Global Public Health Policies and Epidemiology",
            "Air Quality and Health Impacts"
          ]
        },
        {
          "openalex_id": "W4412443294",
          "year": 2025,
          "title": "EPH91 Conceptual Mapping of Health-Related Quality of Life, Quality of Life, and Wellbeing: A Systematic Review and Assessment of Commonly Used Patient Reported Outcomes Measures",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W1985632566",
          "year": 1994,
          "title": "Molecular characterization of HLA class II genes in celiac disease patients of Latin American caucasian origin",
          "type": "article",
          "venue": "Tissue Antigens",
          "cited_by_count": 29,
          "topics": [
            "Celiac Disease Research and Management",
            "Microscopic Colitis",
            "Galectins and Cancer Biology"
          ]
        },
        {
          "openalex_id": "W2060939949",
          "year": 1998,
          "title": "Aspirin for primary prevention of cardiovascular events",
          "type": "article",
          "venue": "Journal of General Internal Medicine",
          "cited_by_count": 45,
          "topics": [
            "Antiplatelet Therapy and Cardiovascular Diseases",
            "Inflammatory mediators and NSAID effects",
            "Cardiac, Anesthesia and Surgical Outcomes"
          ]
        },
        {
          "openalex_id": "W3160604651",
          "year": 1998,
          "title": "El tratamiento del hipertiroidismo con iodo radiactivo aumenta la incidencia de oftalmopatía",
          "type": "article",
          "venue": "Evidencia actualizacion en la práctica ambulatoria",
          "cited_by_count": 0,
          "topics": [
            "Thyroid Cancer Diagnosis and Treatment",
            "Cancer Diagnosis and Treatment"
          ]
        },
        {
          "openalex_id": "W3162129903",
          "year": 1998,
          "title": "Grupos pocos representados en los estudios científicos.",
          "type": "article",
          "venue": "Evidencia actualizacion en la práctica ambulatoria",
          "cited_by_count": 0,
          "topics": [
            "Psychology Research and Bibliometrics"
          ]
        },
        {
          "openalex_id": "W2143025931",
          "year": 2013,
          "title": "Consolidated Health Economic Evaluation Reporting Standards (CHEERS)—Explanation and Elaboration: A Report of the ISPOR Health Economic Evaluation Publication Guidelines Good Reporting Practices Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 2065,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Pharmaceutical Economics and Policy",
            "Economic and Financial Impacts of Cancer"
          ]
        },
        {
          "openalex_id": "W2128911553",
          "year": 2013,
          "title": "Consolidated Health Economic Evaluation Reporting Standards (CHEERS) statement",
          "type": "article",
          "venue": "BMJ",
          "cited_by_count": 1769,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2119679249",
          "year": 2013,
          "title": "Budget Impact Analysis—Principles of Good Practice: Report of the ISPOR 2012 Budget Impact Analysis Good Practice II Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1183,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Environmental and Social Impact Assessments",
            "Community Development and Social Impact"
          ]
        },
        {
          "openalex_id": "W4206608028",
          "year": 2022,
          "title": "Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 1038,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W4206006624",
          "year": 2022,
          "title": "Consolidated Health Economic Evaluation Reporting Standards (CHEERS) 2022 Explanation and Elaboration: A Report of the ISPOR CHEERS II Good Practices Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 859,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2139814250",
          "year": 2015,
          "title": "Cost-Effectiveness Analysis Alongside Clinical Trials II—An ISPOR Good Research Practices Task Force Report",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 846,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2914185992",
          "year": 2013,
          "title": "Consolidated Health Economic Evaluation Reporting Standards (CHEERS) Statement",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 686,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W2037823404",
          "year": 2013,
          "title": "CONSOLIDATED HEALTH ECONOMIC EVALUATION REPORTING STANDARDS (CHEERS) STATEMENT",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 585,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  },
  {
    "name": "Feng Xie",
    "member_affiliation": "McMaster University",
    "is_member": true,
    "projects": [
      {
        "project_id": "137-RA",
        "title": "Navigating antithrombotic therapies with the EQ-5D: An analysis of the COMPASS Trial",
        "working_group": "Others"
      },
      {
        "project_id": "1587-TVG",
        "title": "Learning and promoting health measurement and valuation using EQ instruments across continents",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "1704-RA",
        "title": "A convergent parallel mixed methods study to assess the feasibility of using discrete choice experiments among Canadian youth",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "1793-RA",
        "title": "Comparison of the EQ-5D-Y-5L, EQ-5D-Y-3L and PedsQL in Paediatric Patients with Congenital Heart Disease in China",
        "working_group": "Youth"
      },
      {
        "project_id": "2013050",
        "title": "Assessing test-retest reliability of the EuroQol Group Valuation Technology in valuing the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013180",
        "title": "Transforming latent utilities to health utilities: Can one function fit other countries?",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013230",
        "title": "Establishing a tool for endorsing EQ-5D valuation studies",
        "working_group": "Valuation"
      },
      {
        "project_id": "2013270",
        "title": "Understanding participant’s responses to the EQ-VT tasks; A qualitative study",
        "working_group": "Valuation"
      },
      {
        "project_id": "2015120",
        "title": "Making LIFE simple: Exploration of a hybrid of best-worst scaling and visual analogue scale in valuing EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "2016-RA",
        "title": "Exploring health system stakeholders’ preferences for visualizing routinely collected EQ-5D data in hip and knee arthroplasty in Canada",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "2016060",
        "title": "HTAi Workshop: Engaging patients and general public in health technology assessment: Measuring and valuing health preferences",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016080",
        "title": "Variation in health state preferences across local and international populations: East doesn't meet West",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2016540",
        "title": "Health utilities used in economic evaluations of cancer treatments",
        "working_group": "Populations and Health Systems"
      },
      {
        "project_id": "20170100",
        "title": "Measuring and valuing patient preferences in randomized clinical trials",
        "working_group": "Valuation"
      },
      {
        "project_id": "20180310",
        "title": "Non-parametric approach to valuing the EQ-5D-5L",
        "working_group": "Valuation"
      },
      {
        "project_id": "20191110",
        "title": "Meeting Asia Policy Makers at HTAi 2020",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2023-RA",
        "title": "Comparing DCE with duration split triplet and EQ-VT in valuing EQ-5D-Y-5L in Canada",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "2170-RA",
        "title": "Validating the EQ-5D-Y-5L and EQ-HWB-9 in Inherited Bleeding Disorders in Canada",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "2566-RA",
        "title": "The QALY under scrutiny: A systematic review and thematic synthesis of methodological, ethical, legal, and policy debates",
        "working_group": "Valuation"
      },
      {
        "project_id": "2593-RA",
        "title": "Advancing EQ-5D-5L Application Through AI-Driven Full-Course Management Service for Breast Cancer Patients",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "342-RA",
        "title": "Understanding the views of Canadians on valuing health for children and adolescents",
        "working_group": "Valuation, Youth"
      },
      {
        "project_id": "345-PHD",
        "title": "Statistical methods for handling and analyzing EQ-5D-5L data in randomized clinical trials",
        "working_group": "Others"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5102994482",
      "display_name": "Feng Xie",
      "orcid": "0000-0003-3454-6266",
      "reported_affiliation": "Qingdao University",
      "works_count": 385,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 141
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 30
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 23
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 18
        },
        {
          "topic": "Chronic Disease Management Strategies",
          "works": 12
        },
        {
          "topic": "Osteoarthritis Treatment and Mechanisms",
          "works": 12
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 12
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 12
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 11
        },
        {
          "topic": "Patient-Provider Communication in Healthcare",
          "works": 11
        },
        {
          "topic": "Total Knee Arthroplasty Outcomes",
          "works": 10
        },
        {
          "topic": "Venous Thromboembolism Diagnosis and Management",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Lehana Thabane",
          "works": 50
        },
        {
          "name": "Jean‐Éric Tarride",
          "works": 44
        },
        {
          "name": "Ron Goeree",
          "works": 38
        },
        {
          "name": "Daria O’Reilly",
          "works": 29
        },
        {
          "name": "Gordon Guyatt",
          "works": 28
        },
        {
          "name": "Eleanor Pullenayegum",
          "works": 26
        },
        {
          "name": "Gord Blackhouse",
          "works": 25
        },
        {
          "name": "Brittany Humphries",
          "works": 25
        },
        {
          "name": "Holger J. Schünemann",
          "works": 15
        },
        {
          "name": "Michael J. Zoratti",
          "works": 15
        },
        {
          "name": "Bernhard Michalowsky",
          "works": 15
        },
        {
          "name": "Robert Hopkins",
          "works": 15
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4411289528",
          "year": 2025,
          "title": "1094-P: Validation of the CHROME-G Scale for Measuring Health-Related Quality of Life in Chinese Patients with Diabetes",
          "type": "article",
          "venue": "Diabetes",
          "cited_by_count": 0,
          "topics": [
            "Health and Wellbeing Research",
            "Nutrition and Health in Aging",
            "Cardiovascular Health and Risk Factors"
          ]
        },
        {
          "openalex_id": "W4415942166",
          "year": 2025,
          "title": "1480P Neoadjuvant therapy of sequential transcatheter arterial chemoembolization, camrelizumab and apatinib for single large hepatocellular carcinoma (NEO-START): A randomized controlled trial",
          "type": "article",
          "venue": "Annals of Oncology",
          "cited_by_count": 1,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Cholangiocarcinoma and Gallbladder Cancer Studies",
            "Organ Transplantation Techniques and Outcomes"
          ]
        },
        {
          "openalex_id": "W4410966674",
          "year": 2025,
          "title": "22. Economic evaluations comparing deep brain stimulation to best medical therapy for movement disorders: a meta-analysis",
          "type": "article",
          "venue": "Neuromodulation Technology at the Neural Interface",
          "cited_by_count": 0,
          "topics": [
            "Neurological disorders and treatments"
          ]
        },
        {
          "openalex_id": "W4408365706",
          "year": 2025,
          "title": "A Retrospective Analysis of the Effectiveness and Safety of Plerixafor Combined with PEGylated rhG-CSF for Autologous Hematopoietic Stem Cell Mobilization in Chinese Patients with Multiple Myeloma",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Hematopoietic Stem Cell Transplantation",
            "Protein Degradation and Inhibitors"
          ]
        },
        {
          "openalex_id": "W4410347156",
          "year": 2025,
          "title": "A Retrospective Analysis of the Effectiveness and Safety of Plerixafor Combined with PEGylated rhG-CSF for Autologous Hematopoietic Stem Cell Mobilization in  Patients with Multiple Myeloma",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Multiple Myeloma Research and Treatments",
            "Hematopoietic Stem Cell Transplantation",
            "Acute Myeloid Leukemia Research"
          ]
        },
        {
          "openalex_id": "W4413402097",
          "year": 2025,
          "title": "Associations between clinical benefits of cancer drugs and incremental quality-adjusted life years used in reimbursement decisions in Australia, Canada, England and China: an observational study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Financial Impacts of Cancer",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2348919373",
          "year": 1983,
          "title": "ANALYSIS OF INFANT MORTALITY IN SHANGHAI COUNTY 1977-1981",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Birth, Development, and Health"
          ]
        },
        {
          "openalex_id": "W2007022384",
          "year": 1988,
          "title": "Blinded Comparison of an “Ultrasound Stethoscope” and Standard Echocardiographic Instrument",
          "type": "article",
          "venue": "CHEST Journal",
          "cited_by_count": 10,
          "topics": [
            "Ultrasound in Clinical Applications",
            "Phonocardiography and Auscultation Techniques",
            "Atrial Fibrillation Management and Outcomes"
          ]
        },
        {
          "openalex_id": "W2086122849",
          "year": 1996,
          "title": "Second harmonic transient response imaging with intravenous perfluorocarbon-exposed sonicated dextrose albumin in patients with previous myocardial infarction: Initial clinical experience",
          "type": "article",
          "venue": "Journal of the American College of Cardiology",
          "cited_by_count": 3,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Cardiac electrophysiology and arrhythmias",
            "Coronary Interventions and Diagnostics"
          ]
        },
        {
          "openalex_id": "W1981906456",
          "year": 1996,
          "title": "Transient response imaging with intravenous perfluorocarbon-exposed sonicated dextrose albumin defects the spatial extent of ischemia during dobutamine stress echocardiography",
          "type": "article",
          "venue": "Journal of the American College of Cardiology",
          "cited_by_count": 2,
          "topics": [
            "Cardiac Imaging and Diagnostics",
            "Cardiovascular Effects of Exercise",
            "Cardiac Arrhythmias and Treatments"
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
          "openalex_id": "W2568974466",
          "year": 2017,
          "title": "Instrument-Defined Estimates of the Minimally Important Difference for EQ-5D-5L Index Scores",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 351,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W3087770431",
          "year": 2020,
          "title": "GRADE Guidelines 30: the GRADE approach to assessing the certainty of modeled evidence—An overview in the context of health decision-making",
          "type": "article",
          "venue": "Journal of Clinical Epidemiology",
          "cited_by_count": 313,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Advanced Causal Inference Techniques"
          ]
        },
        {
          "openalex_id": "W3197328793",
          "year": 2021,
          "title": "Convalescent plasma for hospitalized patients with COVID-19: an open-label, randomized controlled trial",
          "type": "article",
          "venue": "Nature Medicine",
          "cited_by_count": 276,
          "topics": [
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 Clinical Research Studies",
            "Long-Term Effects of COVID-19"
          ]
        },
        {
          "openalex_id": "W2916095951",
          "year": 2019,
          "title": "Effect of Patient-Centered Transitional Care Services on Clinical Outcomes in Patients Hospitalized for Heart Failure",
          "type": "article",
          "venue": "JAMA",
          "cited_by_count": 263,
          "topics": [
            "Heart Failure Treatment and Management",
            "Sepsis Diagnosis and Treatment",
            "Chronic Disease Management Strategies"
          ]
        },
        {
          "openalex_id": "W4379114671",
          "year": 2023,
          "title": "Zanidatamab for HER2-amplified, unresectable, locally advanced or metastatic biliary tract cancer (HERIZON-BTC-01): a multicentre, single-arm, phase 2b study",
          "type": "article",
          "venue": "The Lancet Oncology",
          "cited_by_count": 259,
          "topics": [
            "Cholangiocarcinoma and Gallbladder Cancer Studies",
            "HER2/EGFR in Cancer Research",
            "Gallbladder and Bile Duct Disorders"
          ]
        },
        {
          "openalex_id": "W3009909056",
          "year": 2020,
          "title": "[Clinical analysis of 31 cases of 2019 novel coronavirus infection in children from six provinces (autonomous region) of northern China].",
          "type": "article",
          "venue": "PubMed",
          "cited_by_count": 241,
          "topics": [
            "COVID-19 Clinical Research Studies",
            "COVID-19 Impact on Reproduction",
            "Respiratory viral infections research"
          ]
        },
        {
          "openalex_id": "W2020197365",
          "year": 2010,
          "title": "Meta-analysis of radiofrequency ablation versus hepatic resection for small hepatocellular carcinoma",
          "type": "review",
          "venue": "BMC Gastroenterology",
          "cited_by_count": 218,
          "topics": [
            "Hepatocellular Carcinoma Treatment and Prognosis",
            "Liver Disease Diagnosis and Treatment",
            "Cholangiocarcinoma and Gallbladder Cancer Studies"
          ]
        }
      ]
    }
  },
  {
    "name": "Fernando Argento",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "2169-RA",
        "title": "Health Related Quality Of Life Of Children And Adolescents With Cerebral Palsy, And The Spillover Effect In Their Caregivers. Cross-Sectional And Longitudinal Analysis, And EQ-5D-Y-5L And EQ-HWB-9 Psychometric Properties In This Population In Argentina. ",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "2171-RA",
        "title": "Spillover Effects in Health-Related Quality of Life in Parents/Caregivers of Children 0 to 4 years old. Testing the Measurement Properties of the EQ-HWB-S in a multinational study in Argentina, Australia, Canada, Germany and Singapore",
        "working_group": "Youth, EQ-HWB"
      },
      {
        "project_id": "2436-RA",
        "title": "Comparative Assessment of the EQ-5D-Y-3L and EQ-5D-Y-5L Interviewer-administered versions in Children Aged 5–8 Years: Feasibility, Comprehension, and Psychometric Properties. ",
        "working_group": "Youth"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5021426515",
      "display_name": "Fernando Argento",
      "orcid": "0000-0002-2492-8933",
      "reported_affiliation": "Instituto de Efectividad Clínica y Sanitaria",
      "works_count": 45,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 18
        },
        {
          "topic": "COVID-19 Impact on Reproduction",
          "works": 10
        },
        {
          "topic": "Vaccine Coverage and Hesitancy",
          "works": 9
        },
        {
          "topic": "SARS-CoV-2 and COVID-19 Research",
          "works": 6
        },
        {
          "topic": "Quality and Safety in Healthcare",
          "works": 5
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 4
        },
        {
          "topic": "Health Policy Implementation Science",
          "works": 3
        },
        {
          "topic": "Lung Cancer Diagnosis and Treatment",
          "works": 3
        },
        {
          "topic": "Delphi Technique in Research",
          "works": 3
        },
        {
          "topic": "Cancer Genomics and Diagnostics",
          "works": 3
        },
        {
          "topic": "Maternal Mental Health During Pregnancy and Postpartum",
          "works": 2
        },
        {
          "topic": "Reproductive System and Pregnancy",
          "works": 2
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Federico Augustovski",
          "works": 23
        },
        {
          "name": "Ariel Bardach",
          "works": 18
        },
        {
          "name": "Agustín Ciapponi",
          "works": 14
        },
        {
          "name": "Federico Rodríguez Cairoli",
          "works": 13
        },
        {
          "name": "Andrea Alcaraz",
          "works": 12
        },
        {
          "name": "Jamile Ballivian",
          "works": 11
        },
        {
          "name": "Andrés Pichón-Rivière",
          "works": 11
        },
        {
          "name": "Daniel Comandé",
          "works": 10
        },
        {
          "name": "Mabel Berrueta",
          "works": 10
        },
        {
          "name": "Xu Xiong",
          "works": 10
        },
        {
          "name": "Agustina Mazzoni",
          "works": 10
        },
        {
          "name": "Pierre Buekens",
          "works": 10
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W7167275189",
          "year": 2026,
          "title": "Content validity of the modified EQ-HWB-9 in a sample of Argentinean patients, informal caregivers, and members of the general public",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Chronic Disease Management Strategies",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W4415257826",
          "year": 2025,
          "title": "A Delphi study on valuing DNA sequencing in oncology: a European stakeholder developed framework for assessing next generation sequencing and comprehensive genomic profiling diagnostics",
          "type": "article",
          "venue": "EBioMedicine",
          "cited_by_count": 0,
          "topics": [
            "Delphi Technique in Research",
            "Cancer Genomics and Diagnostics",
            "Ethics in Clinical Research"
          ]
        },
        {
          "openalex_id": "W4406891974",
          "year": 2025,
          "title": "Budget impact of low-dose computed tomography screening for lung cancer in Argentina",
          "type": "article",
          "venue": "Expert Review of Pharmacoeconomics & Outcomes Research",
          "cited_by_count": 3,
          "topics": [
            "Lung Cancer Diagnosis and Treatment",
            "Radiation Dose and Imaging",
            "Global Cancer Incidence and Screening"
          ]
        },
        {
          "openalex_id": "W4412094588",
          "year": 2025,
          "title": "Conceptual Mapping of Health-Related Quality of Life, Quality of Life, and Wellbeing: A Systematic Review and Assessment of Commonly Used Patient-Reported Outcomes Measures",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W4412517653",
          "year": 2025,
          "title": "Development and implementation of a value framework for rapid health technology assessment reports: enhancing evidence-informed decision making in resource-constrained settings",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 1,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Delphi Technique in Research",
            "Health Policy Implementation Science"
          ]
        },
        {
          "openalex_id": "W4412443294",
          "year": 2025,
          "title": "EPH91 Conceptual Mapping of Health-Related Quality of Life, Quality of Life, and Wellbeing: A Systematic Review and Assessment of Commonly Used Patient Reported Outcomes Measures",
          "type": "conference-abstract",
          "venue": "Value in Health",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life"
          ]
        },
        {
          "openalex_id": "W2996401746",
          "year": 2019,
          "title": "Factores de riesgo para la aparición y/o recurrencia de úlceras por presión en sujetos con lesión medular: revisión sistemática",
          "type": "article",
          "venue": "Revista de la Facultad de Ciencias Médicas de Córdoba",
          "cited_by_count": 4,
          "topics": [
            "Pressure Ulcer Prevention and Management",
            "Diabetic Foot Ulcer Assessment and Management",
            "Nursing care and research"
          ]
        },
        {
          "openalex_id": "W3180858540",
          "year": 2019,
          "title": "Validación del Timed Up and Go Test como Predictor de Riesgo de Caídas en Sujetos con Artritis Reumatoidea: Parte II: Validez Concurrente y Predictiva",
          "type": "article",
          "venue": "",
          "cited_by_count": 0,
          "topics": [
            "Rheumatoid Arthritis Research and Therapies"
          ]
        },
        {
          "openalex_id": "W4206347571",
          "year": 2019,
          "title": "Validation of the Timed Up and Go Test as a Predictor of Risk of Falls in Subjects with Rheumatoid Arthritis",
          "type": "article",
          "venue": "Revista Argentina de Reumatología",
          "cited_by_count": 0,
          "topics": [
            "Balance, Gait, and Falls Prevention",
            "Cerebral Palsy and Movement Disorders",
            "Diabetic Foot Ulcer Assessment and Management"
          ]
        },
        {
          "openalex_id": "W3107914288",
          "year": 2020,
          "title": "Demographic and clinical characteristics of individuals with traumatic spinal cord injury in Argentina from 2015 to 2019: a multicenter study",
          "type": "article",
          "venue": "Spinal Cord Series and Cases",
          "cited_by_count": 5,
          "topics": [
            "Spinal Cord Injury Research",
            "Traumatic Brain Injury Research",
            "Nerve Injury and Rehabilitation"
          ]
        },
        {
          "openalex_id": "W3176015388",
          "year": 2021,
          "title": "COVID-19 and pregnancy: An umbrella review of clinical presentation, vertical transmission, and maternal and perinatal outcomes",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 122,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Gestational Diabetes Research and Management"
          ]
        },
        {
          "openalex_id": "W4361011616",
          "year": 2023,
          "title": "Safety of COVID-19 vaccines during pregnancy: A systematic review and meta-analysis",
          "type": "review",
          "venue": "Vaccine",
          "cited_by_count": 86,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Vaccine Coverage and Hesitancy",
            "Reproductive System and Pregnancy"
          ]
        },
        {
          "openalex_id": "W3194662876",
          "year": 2021,
          "title": "Safety of components and platforms of COVID-19 vaccines considered for use in pregnancy: A rapid review",
          "type": "article",
          "venue": "Vaccine",
          "cited_by_count": 58,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        },
        {
          "openalex_id": "W4400645958",
          "year": 2024,
          "title": "Safety and Effectiveness of COVID-19 Vaccines During Pregnancy: A Living Systematic Review and Meta-analysis",
          "type": "review",
          "venue": "Drug Safety",
          "cited_by_count": 39,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research"
          ]
        },
        {
          "openalex_id": "W3159607009",
          "year": 2021,
          "title": "COVID-19 and pregnancy: An umbrella review of clinical presentation, vertical transmission, and maternal and perinatal outcomes",
          "type": "preprint",
          "venue": "medRxiv",
          "cited_by_count": 36,
          "topics": [
            "COVID-19 Impact on Reproduction",
            "Maternal Mental Health During Pregnancy and Postpartum",
            "Maternal and fetal healthcare"
          ]
        },
        {
          "openalex_id": "W4362506267",
          "year": 2023,
          "title": "Cost-effectiveness of COVID-19 vaccination in Latin America and the Caribbean: an analysis in Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico, and Peru",
          "type": "article",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 13,
          "topics": [
            "Vaccine Coverage and Hesitancy",
            "SARS-CoV-2 and COVID-19 Research",
            "COVID-19 and healthcare impacts"
          ]
        },
        {
          "openalex_id": "W4210831110",
          "year": 2022,
          "title": "The Development of a New International Generic Measure (EQ-HWB): Face Validity and Psychometric Stages in Argentina",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 13,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health Policy Implementation Science",
            "Health Education and Validation"
          ]
        },
        {
          "openalex_id": "W4311541913",
          "year": 2022,
          "title": "Rotavirus Vaccine Impact since Its Introduction in the National Immunization Program of Argentina",
          "type": "article",
          "venue": "Infectious Diseases and Therapy",
          "cited_by_count": 11,
          "topics": [
            "Viral gastroenteritis research and epidemiology",
            "Respiratory viral infections research",
            "Infection Control and Ventilation"
          ]
        }
      ]
    }
  },
  {
    "name": "Fredrick Purba",
    "member_affiliation": "Universitas Padjadjaran",
    "is_member": true,
    "projects": [
      {
        "project_id": "1644-RA",
        "title": "Psychometric properties of the EQ-HWB in patients with breast cancer in Indonesia",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "1910-RA",
        "title": "Qualitative study of the modified EQ-HWB in cancer patients.",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "1914-RA",
        "title": "Evaluating the psychometric properties of bolt-ons in breast cancer patients",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2016420",
        "title": "A Big Step Forwards for Health Policy in Indonesia: The Introduction of The EuroQol EQ-5D-5L Value Set and Other Recent Developments in Quality of Life Research and Cost-Effectiveness Analysis. (PI: Purba)",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20180140",
        "title": "Validity, Responsiveness and Test-Retest of EQ-5D-3L-Y and EQ-5D-5L-Y and their proxy versions in Pediatric Patients in Indonesia",
        "working_group": "Youth"
      },
      {
        "project_id": "20180430",
        "title": "EuroQol Annual meeting of Asian region: sharing and networking between EQ-5D researchers of Asian countries.",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "20190130",
        "title": "The performance of EQ-5D-5L in various disease groups with different durations",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "20190440",
        "title": "Proposal of the 2nd EuroQol Asia Academy Meeting",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2035-RA",
        "title": "Evaluating the Performance of EQ-HWB and EQ-HWB-S in Aged Care Setting: A Multicentre Study in Indonesia, China, and Hong Kong",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2113-EOI",
        "title": "3rd EuroQol Asia Academy Meeting 2026: sharing and networking among EQ-5D researchers of Asian countries",
        "working_group": "Education and Outreach"
      },
      {
        "project_id": "2177-RA",
        "title": "Quantitative testing of Experimental and Modified version of EQ-HWB-S using EQ-DAPHNIE data from Argentina and Germany",
        "working_group": "Populations and Health Systems, EQ-HWB"
      },
      {
        "project_id": "2203-RA",
        "title": "Testing the EQ-5D-5L Cognitive Bolt-on Items from the EQ-5D Bolt-on Toolbox and EQ-HWB-S in Patients With Schizophrenia: A Qualitative Study in Indonesia",
        "working_group": "Descriptive Systems, EQ-HWB"
      },
      {
        "project_id": "242-RA",
        "title": "Interviewer Administered and Self-Complete versions of EQ-5D-5L: agreement and psychometric properties",
        "working_group": "Descriptive Systems"
      },
      {
        "project_id": "2463-RA",
        "title": "Assessing the Impact of Digital Layout on EQ-HWB-9 Performance: A Comparative Analysis of Item-by-Item and Grid Formats Using EQ-DAPHNIE Data in Germany and Argentina",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "2466-RA",
        "title": "Cross-Country Qualitative Analysis of EQ-HWB Visual Analogue Scale (VAS) and Three Positively-Framed Items Responses From Indonesia, Germany, Slovenia, and Hungary",
        "working_group": "EQ-HWB"
      },
      {
        "project_id": "442-RA",
        "title": "EQ-HWB and EQ-HWB-S in Indonesia: content validity, interviewer administered version, and test-retest",
        "working_group": "EQ-HWB"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5059806422",
      "display_name": "Fredrick Dermawan Purba",
      "orcid": "0000-0002-7336-3043",
      "reported_affiliation": "Padjadjaran University",
      "works_count": 148,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 49
        },
        {
          "topic": "Economic and Environmental Valuation",
          "works": 17
        },
        {
          "topic": "Public Health and Nutrition",
          "works": 12
        },
        {
          "topic": "Educational Methods and Impacts",
          "works": 12
        },
        {
          "topic": "COVID-19 and Mental Health",
          "works": 11
        },
        {
          "topic": "COVID-19 Prevention and Impact",
          "works": 10
        },
        {
          "topic": "Child Development and Education",
          "works": 10
        },
        {
          "topic": "Efficiency Analysis Using DEA",
          "works": 6
        },
        {
          "topic": "Mental Health Treatment and Access",
          "works": 6
        },
        {
          "topic": "Healthcare Systems and Reforms",
          "works": 5
        },
        {
          "topic": "Psychological Well-being and Life Satisfaction",
          "works": 5
        },
        {
          "topic": "Student Stress and Coping",
          "works": 5
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Jan J.V. Busschbach",
          "works": 13
        },
        {
          "name": "Hari Setyowibowo",
          "works": 13
        },
        {
          "name": "Aulia Iskandarsyah",
          "works": 11
        },
        {
          "name": "Titi Sahidah Fitriana",
          "works": 11
        },
        {
          "name": "Dyah Aryani Perwitasari",
          "works": 11
        },
        {
          "name": "Bram Roudijk",
          "works": 10
        },
        {
          "name": "Langgersari Elsari Novianti",
          "works": 10
        },
        {
          "name": "Hendriati Agustiani",
          "works": 10
        },
        {
          "name": "Elly Stolk",
          "works": 9
        },
        {
          "name": "Nan Luo",
          "works": 8
        },
        {
          "name": "Zhihao Yang",
          "works": 8
        },
        {
          "name": "Devi Wulandari",
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
          "openalex_id": "W7170071918",
          "year": 2026,
          "title": "Cost-Utility Analysis of Dolutegravir Versus Efavirenz-Based Regimens for HIV Treatment in Indonesia: A Model-Based Extrapolation From Primary Healthcare Settings",
          "type": "article",
          "venue": "Value in Health Regional Issues",
          "cited_by_count": 0,
          "topics": [
            "HIV/AIDS drug development and treatment",
            "HIV/AIDS Research and Interventions",
            "HIV-related health complications and treatments"
          ]
        },
        {
          "openalex_id": "W7162025172",
          "year": 2026,
          "title": "Cultural development and validation of a group-based Somatic Experiencing® intervention for Indonesian women survivors of sexual assault with PTSD symptoms: a mixed-methods study",
          "type": "article",
          "venue": "Frontiers in Psychology",
          "cited_by_count": 0,
          "topics": [
            "Posttraumatic Stress Disorder Research",
            "Child Abuse and Trauma",
            "Sexual Assault and Victimization Studies"
          ]
        },
        {
          "openalex_id": "W7161802675",
          "year": 2026,
          "title": "EQ-5D-5L population health and cross-country comparison across 15 countries (the EQ-DAPHNIE project)",
          "type": "preprint",
          "venue": "Research Square",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "Health, psychology, and well-being"
          ]
        },
        {
          "openalex_id": "W7162664709",
          "year": 2026,
          "title": "Exploring Perceived Interactions between EQ-5D-5L and Bolt-ons Using Composite Time-Tradeoff Valuations: A Qualitative Study",
          "type": "article",
          "venue": "Medical Decision Making",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Patient-Provider Communication in Healthcare",
            "Economic and Environmental Valuation"
          ]
        },
        {
          "openalex_id": "W7164819429",
          "year": 2026,
          "title": "The EQ-5D-5L valuation study in Nigeria",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 0,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Efficiency Analysis Using DEA"
          ]
        },
        {
          "openalex_id": "W4255593815",
          "year": 2013,
          "title": "Indonesian dating couples: From similarity to satisfaction",
          "type": "dataset",
          "venue": "PsycEXTRA Dataset",
          "cited_by_count": 0,
          "topics": [
            "Gender and Women's Rights",
            "Marriage and Sexual Relationships",
            "Intergenerational Family Dynamics and Caregiving"
          ]
        },
        {
          "openalex_id": "W4210663307",
          "year": 2013,
          "title": "Love and its components: Study of Indonesian dating couples",
          "type": "dataset",
          "venue": "PsycEXTRA Dataset",
          "cited_by_count": 0,
          "topics": [
            "Marriage and Family Dynamics",
            "Gender and Women's Rights",
            "Islamic Finance and Communication"
          ]
        },
        {
          "openalex_id": "W4244151012",
          "year": 2013,
          "title": "Me and my best friend: A study of social comparison in Indonesian teenagers",
          "type": "dataset",
          "venue": "PsycEXTRA Dataset",
          "cited_by_count": 0,
          "topics": [
            "Education, Sociology, Communication Studies",
            "Bullying, Victimization, and Aggression",
            "Media Influence and Health"
          ]
        },
        {
          "openalex_id": "W4238845520",
          "year": 2013,
          "title": "Teenagers, you and I are not the same: A descriptive study about social comparison between male and female teenagers in Bandung, Indonesia",
          "type": "dataset",
          "venue": "PsycEXTRA Dataset",
          "cited_by_count": 0,
          "topics": [
            "Education, Sociology, Communication Studies"
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
          "openalex_id": "W2800059521",
          "year": 2018,
          "title": "Quality of life of the Indonesian general population: Test-retest reliability and population norms of the EQ-5D-5L and WHOQOL-BREF",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 179,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Systems and Reforms",
            "BRCA gene mutations in cancer"
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
          "openalex_id": "W2909118649",
          "year": 2019,
          "title": "Health-related quality of life in Indonesian type 2 diabetes mellitus outpatients measured with the Bahasa version of EQ-5D",
          "type": "article",
          "venue": "Quality of Life Research",
          "cited_by_count": 84,
          "topics": [
            "Diabetes Management and Education",
            "Health Systems, Economic Evaluations, Quality of Life",
            "Mental Health and Patient Involvement"
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
          "openalex_id": "W4389154382",
          "year": 2023,
          "title": "Understanding the protective effect of social support on depression symptomatology from a longitudinal network perspective",
          "type": "article",
          "venue": "BMJ Mental Health",
          "cited_by_count": 65,
          "topics": [
            "Mental Health Research Topics",
            "Health disparities and outcomes",
            "Functional Brain Connectivity Studies"
          ]
        },
        {
          "openalex_id": "W3196740340",
          "year": 2021,
          "title": "Marriage and quality of life during COVID-19 pandemic",
          "type": "article",
          "venue": "PLoS ONE",
          "cited_by_count": 63,
          "topics": [
            "COVID-19 and Mental Health",
            "COVID-19 Pandemic Impacts",
            "Psychological Well-being and Life Satisfaction"
          ]
        },
        {
          "openalex_id": "W3212036572",
          "year": 2021,
          "title": "Comparing measurement properties of EQ-5D-Y-3L and EQ-5D-Y-5L in paediatric patients",
          "type": "article",
          "venue": "Health and Quality of Life Outcomes",
          "cited_by_count": 58,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Behavioral and Psychological Studies",
            "HER2/EGFR in Cancer Research"
          ]
        }
      ]
    }
  },
  {
    "name": "Gerard De Pouvourville",
    "member_affiliation": "",
    "is_member": false,
    "projects": [
      {
        "project_id": "20170510",
        "title": "Valuation of the EQ-5D-5L in the French population",
        "working_group": "Valuation"
      },
      {
        "project_id": "20190020",
        "title": "QALY MICI (IBD QALY)",
        "working_group": "Descriptive Systems"
      }
    ],
    "chosen_profile": {
      "openalex_id": "A5085975930",
      "display_name": "Gérard de Pouvourville",
      "orcid": "0000-0002-5941-6823",
      "reported_affiliation": "École Supérieure des Sciences Économiques et Commerciales",
      "works_count": 356,
      "top_topics": [
        {
          "topic": "Health Systems, Economic Evaluations, Quality of Life",
          "works": 107
        },
        {
          "topic": "Healthcare Systems and Practices",
          "works": 53
        },
        {
          "topic": "Pharmaceutical Economics and Policy",
          "works": 43
        },
        {
          "topic": "Health, Medicine and Society",
          "works": 21
        },
        {
          "topic": "Economic and Financial Impacts of Cancer",
          "works": 19
        },
        {
          "topic": "Healthcare Policy and Management",
          "works": 18
        },
        {
          "topic": "Atrial Fibrillation Management and Outcomes",
          "works": 18
        },
        {
          "topic": "Diabetes Management and Research",
          "works": 16
        },
        {
          "topic": "Cervical Cancer and HPV Research",
          "works": 11
        },
        {
          "topic": "Pharmaceutical studies and practices",
          "works": 11
        },
        {
          "topic": "Diabetes Treatment and Management",
          "works": 10
        },
        {
          "topic": "Thyroid Cancer Diagnosis and Treatment",
          "works": 10
        }
      ],
      "frequent_coauthors": [
        {
          "name": "Manon Belhassen",
          "works": 30
        },
        {
          "name": "Isabelle Borget",
          "works": 19
        },
        {
          "name": "B. Detournay",
          "works": 18
        },
        {
          "name": "Patrick Blin",
          "works": 18
        },
        {
          "name": "Éric Van Ganse",
          "works": 17
        },
        {
          "name": "Julie Chevalier",
          "works": 15
        },
        {
          "name": "Nicholas Moore",
          "works": 14
        },
        {
          "name": "Laurent Laforest",
          "works": 14
        },
        {
          "name": "K Le Lay",
          "works": 14
        },
        {
          "name": "C. Droz‐Perroteau",
          "works": 14
        },
        {
          "name": "Martin Schlumberger",
          "works": 12
        },
        {
          "name": "C. Chouaïd",
          "works": 12
        }
      ],
      "work_examples": [
        {
          "openalex_id": "W4406844868",
          "year": 2025,
          "title": "Assessing the economic impact and healthcare resource utilization of inpatient pneumococcal disease among adults: a French national claims database study",
          "type": "article",
          "venue": "Journal of Medical Economics",
          "cited_by_count": 3,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Respiratory viral infections research",
            "Nosocomial Infections in ICU"
          ]
        },
        {
          "openalex_id": "W4416138483",
          "year": 2025,
          "title": "Change in healthcare resource use and associated costs of patients with metastatic lung cancer between 2013 and 2021: an observational study from the French national health data system",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 0,
          "topics": [
            "Lung Cancer Treatments and Mutations",
            "Economic and Financial Impacts of Cancer",
            "Lung Cancer Research Studies"
          ]
        },
        {
          "openalex_id": "W4412127145",
          "year": 2025,
          "title": "Clinical burden of pneumococcal disease among adults in France: A retrospective cohort study",
          "type": "article",
          "venue": "Human Vaccines & Immunotherapeutics",
          "cited_by_count": 3,
          "topics": [
            "Pneumonia and Respiratory Infections",
            "Pneumocystis jirovecii pneumonia detection and treatment",
            "Emergency and Acute Care Studies"
          ]
        },
        {
          "openalex_id": "W4406191782",
          "year": 2025,
          "title": "Do continuous glucose monitoring (CGM) metrics predict macrovascular and microvascular complications in diabetes? The FACULTY protocol of a retrospective real-world cohort study",
          "type": "article",
          "venue": "BMJ Open",
          "cited_by_count": 3,
          "topics": [
            "Diabetes Management and Research",
            "Diabetes, Cardiovascular Risks, and Lipoproteins",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients"
          ]
        },
        {
          "openalex_id": "W4416352010",
          "year": 2025,
          "title": "Economic analyses of freestyle libre systems for people living with diabetes: a systematic literature review",
          "type": "review",
          "venue": "Cost Effectiveness and Resource Allocation",
          "cited_by_count": 0,
          "topics": [
            "Diabetes Management and Research",
            "Diabetes Management and Education",
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients"
          ]
        },
        {
          "openalex_id": "W4413185816",
          "year": 2025,
          "title": "Epidemiology, disease evolution and economic burden of amyotrophic lateral sclerosis in France using the French national health data system",
          "type": "article",
          "venue": "Brain Communications",
          "cited_by_count": 4,
          "topics": [
            "Amyotrophic Lateral Sclerosis Research",
            "Parkinson's Disease Mechanisms and Treatments",
            "Prion Diseases and Protein Misfolding"
          ]
        },
        {
          "openalex_id": "W623163685",
          "year": 1982,
          "title": "Marchés publics et politique industrielle",
          "type": "book",
          "venue": "Economica eBooks",
          "cited_by_count": 6,
          "topics": [
            "French Urban and Social Studies"
          ]
        },
        {
          "openalex_id": "W1965952936",
          "year": 1983,
          "title": "La responsabilité juridique de l'Etat en matière d'interventions économiques et financières",
          "type": "article",
          "venue": "Politiques et management public",
          "cited_by_count": 0,
          "topics": [
            "Social Sciences and Governance",
            "Legal and Social Philosophy"
          ]
        },
        {
          "openalex_id": "W2027567993",
          "year": 1985,
          "title": "Hospital system management in France and Canada: National pluralism and provincial centralism",
          "type": "article",
          "venue": "Social Science & Medicine",
          "cited_by_count": 20,
          "topics": [
            "Healthcare Systems and Practices",
            "Social Policies and Family"
          ]
        },
        {
          "openalex_id": "W2411987683",
          "year": 1986,
          "title": "Hospital Reforms in France under a Socialist Government",
          "type": "article",
          "venue": "Milbank Quarterly",
          "cited_by_count": 4,
          "topics": [
            "Healthcare Systems and Practices",
            "Social Policies and Family",
            "Health, Medicine and Society"
          ]
        },
        {
          "openalex_id": "W1561023139",
          "year": 2004,
          "title": "Incidence of chemotherapy‐induced nausea and emesis after modern antiemetics",
          "type": "article",
          "venue": "Cancer",
          "cited_by_count": 470,
          "topics": [
            "Nausea and vomiting management",
            "Chemotherapy-related skin toxicity",
            "Enhanced Recovery After Surgery"
          ]
        },
        {
          "openalex_id": "W2163878956",
          "year": 2013,
          "title": "Performance-Based Risk-Sharing Arrangements—Good Practices for Design, Implementation, and Evaluation: Report of the ISPOR Good Practices for Performance-Based Risk-Sharing Arrangements Task Force",
          "type": "article",
          "venue": "Value in Health",
          "cited_by_count": 308,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare cost, quality, practices",
            "Pharmaceutical Economics and Policy"
          ]
        },
        {
          "openalex_id": "W2033717212",
          "year": 2011,
          "title": "Valuing EQ-5D using Time Trade-Off in France",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 204,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Economic and Environmental Valuation",
            "Healthcare Quality and Management"
          ]
        },
        {
          "openalex_id": "W3152935002",
          "year": 2021,
          "title": "Important Drop in Rate of Acute Diabetes Complications in People With Type 1 or Type 2 Diabetes After Initiation of Flash Glucose Monitoring in France: The RELIEF Study",
          "type": "article",
          "venue": "Diabetes Care",
          "cited_by_count": 171,
          "topics": [
            "Hyperglycemia and glycemic control in critically ill and hospitalized patients",
            "Diabetes Management and Research",
            "Diabetes and associated disorders"
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
          "openalex_id": "W2109592076",
          "year": 1992,
          "title": "Issues in the Cross-National Assessment of Health Technology",
          "type": "article",
          "venue": "International Journal of Technology Assessment in Health Care",
          "cited_by_count": 162,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management",
            "Healthcare cost, quality, practices"
          ]
        },
        {
          "openalex_id": "W1989182795",
          "year": 2005,
          "title": "Can economic evaluations be made more transferable?",
          "type": "article",
          "venue": "The European Journal of Health Economics",
          "cited_by_count": 121,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Healthcare Policy and Management"
          ]
        },
        {
          "openalex_id": "W2118406374",
          "year": 2010,
          "title": "The efficiency frontier approach to economic evaluation of health‐care interventions",
          "type": "article",
          "venue": "Health Economics",
          "cited_by_count": 119,
          "topics": [
            "Health Systems, Economic Evaluations, Quality of Life",
            "Health and Medical Studies",
            "Healthcare Policy and Management"
          ]
        }
      ]
    }
  }
]
