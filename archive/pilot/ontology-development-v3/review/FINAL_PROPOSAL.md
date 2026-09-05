# Final proposal: a practical EuroQol research ontology

## Decision

Build the ontology around the facts that EuroQol researchers search for. Do not build it around generic paper parts or generic evidence statements.

The central facts are:

1. study type;
2. population and sample;
3. instrument and exact version;
4. instrument use;
5. research concepts and themes;
6. research or valuation method;
7. protocol and task design;
8. analysis and exact statistical model;
9. measured outcome or measurement property;
10. research product;
11. principal finding, interpretation, and limitation.

Project, publication, author, funding, and citation data form a linked portfolio module. Counts, ranks, trends, networks, and similarity scores form a derived analytics layer.

This is a domain ontology for EuroQol research. It is not a general ontology for all research.

## 1. Human model

```text
Funded project ──supports──> Study ──reported in──> Publication
                              │
                              ├── has study type: valuation study
                              ├── studies: Moroccan adults
                              ├── uses instrument: EQ-5D-5L
                              ├── uses valuation method: cTTO
                              ├── uses valuation method: DCE
                              ├── concerns theme: states worse than dead
                              ├── follows protocol: EQ-VT 2.6.1
                              ├── uses model: hybrid heteroskedastic Tobit model
                              ├── produces: Moroccan EQ-5D-5L value set
                              └── reports: principal findings and limitations
```

The labels on the right are stored values. They are not hidden in free text. A user can search for `valuation study`, `EQ-5D-5L`, `cTTO`, or `hybrid heteroskedastic Tobit model` directly.

## 2. Three parts of the system

### 2.1 EuroQol research content

This is the ontology core. It describes what a study did and found.

### 2.2 Research portfolio context

This links studies and publications to funded projects, people, organizations, awards, working groups, and the corpus. It supports funding and portfolio questions.

### 2.3 Derived analytics

This contains calculated answers. Examples are counts, medians, trends, rankings, networks, and similarity scores. Each result states its data snapshot, filters, and rule.

The system must not treat a calculated result as a finding reported by a study.

## 3. Core concepts

| Concept | Plain meaning | Example |
|---|---|---|
| `Publication` | A published or unpublished research output | Moroccan value-set article, DOI `10.1007/s11136-025-03930-1` |
| `Study` | One research investigation reported by one or more publications | Moroccan national valuation study |
| `Study type` | One or more controlled labels for the purpose of the study | `value-set development`; `valuation study` |
| `Research concept or theme` | A source-grounded topic that helps users connect the study to related EuroQol research | states worse than dead; digital health; child and adolescent health |
| `Population` | The people to whom the research question applies | Moroccan adults |
| `Sample` | The people or records that supplied data | 1,048 interviewed; 976 analyzed |
| `Instrument` | An exact measure, version, or form | EQ-5D-5L; EQ-5D-Y-3L proxy version 1 |
| `Instrument use` | How an instrument was used in this study | valued; administered; scored with; psychometrically evaluated |
| `Administration` | How, where, by whom, and in which language data were collected | computer-assisted face-to-face interview in Moroccan Arabic or French |
| `Research method` | The exact procedure that generated research data | cTTO; DCE; cognitive interview; systematic review |
| `Protocol or task design` | A named protocol and important implementation detail | EQ-VT 2.6.1; ten cTTO tasks and seven DCE pairs |
| `Analysis` | A defined analysis of study data | combined cTTO and DCE analysis |
| `Statistical model` | The exact model used in an analysis | hybrid heteroskedastic Tobit model |
| `Measured outcome or property` | What was measured or evaluated | utility; test-retest reliability; content validity |
| `Research product` | A reusable output made or assessed by the study | Moroccan EQ-5D-5L value set |
| `Finding` | A principal source-grounded result in plain language | Pain/discomfort had the largest effect on utility |
| `Interpretation or impact` | What the authors think the finding means or enables | Use in Moroccan HTA and economic evaluation |
| `Limitation` | A reported constraint on interpretation | Under-representation of rural and low-literacy participants |

There is no generic `Component` concept. There is no generic `Paper` concept. Use `Publication`, `Study`, and the exact domain concepts above.

## 4. The controlled “corner pieces”

The ontology needs controlled values and aliases. It does not need one fixed list for all time. New source terms can enter a review queue.

Each controlled term has:

- a preferred label;
- exact source labels and abbreviations;
- a short definition;
- broader and narrower terms when useful;
- the source records that support its use;
- review status.

For example, `composite time trade-off`, `composite TTO`, `c-TTO`, and `cTTO` can map to the preferred label `cTTO`. The exact source label remains available.

### 4.1 Study type

Use multiple labels when the study has multiple purposes.

- value-set development;
- valuation study;
- valuation-method or task-design study;
- mapping or crosswalk study;
- instrument or descriptive-system development;
- bolt-on development or evaluation;
- translation or cultural adaptation;
- measurement-property or psychometric study;
- content-validity study;
- population norms or population-health study;
- clinical or longitudinal outcome study;
- implementation or routine-measurement study;
- qualitative or stakeholder study;
- systematic review or evidence synthesis;
- economic evaluation or utility application;
- survey, interviewer, or data-quality study;
- protocol or methodological paper.

`Valuation study` applies only when the research elicits preferences for states, dimensions, or levels. A clinical study that applies an existing value set is not a valuation study.

### 4.2 Research concepts and themes

Use a multi-value `Concepts and themes` field for source-grounded topics that help users find related EuroQol research. This layer is deliberately flexible during extraction. It is not another study-type classification and it does not replace exact structured facts.

For example:

| Exact structured facts | Concepts and themes |
|---|---|
| Population: children aged 8–15; instrument: EQ-5D-Y-3L | child and adolescent health; self-report in children |
| Method: cTTO; outcome: health-state utility | states worse than dead; health-state anchoring |
| Channel: web; product: clinical decision aid | digital health; clinical decision support |

Ten example concepts or themes are:

1. states worse than dead;
2. child and adolescent health;
3. proxy reporting and proxy perspective;
4. digital health and remote measurement;
5. respondent engagement;
6. attribute non-attendance;
7. health inequality;
8. cultural adaptation and cross-cultural comparability;
9. caregiver spillover;
10. routine PROM implementation and clinical decision support.

An extraction agent can retain an exact source term, such as `children`, and add a preferred term, such as `child and adolescent health`, when the mapping is clear. Later review can add aliases and broader or narrower links. Do not force a theme when the source does not support it. A theme can overlap a structured field when that overlap improves discovery.

### 4.3 Instrument and instrument use

Store the exact family, version, form, language, and status when the source reports them.

Example instrument values include:

- EQ-5D-3L;
- EQ-5D-5L;
- EQ-5D-Y-3L;
- EQ-5D-Y-5L;
- EQ-HWB;
- EQ-HWB-S;
- EQ-TIPS V2.0;
- EQ VAS;
- condition-specific instruments and comparator measures.

An `Instrument use` record states the role of that instrument in the study:

- developed;
- translated or adapted;
- administered as an outcome measure;
- used to describe the sample;
- valued;
- psychometrically evaluated;
- used as a comparator;
- used as a mapping source;
- used as a mapping target;
- scored with a named value set;
- implemented in routine practice.

The same instrument can have more than one role.

### 4.4 Population and sample

Keep these facts separate:

- target population;
- recruitment population or frame;
- recruited count;
- completed count;
- analytic count;
- subgroup or arm;
- age range or life stage;
- condition;
- country or region and its role;
- inclusion and exclusion criteria;
- respondent role;
- sampling method;
- representativeness and important exclusions.

Do not use one ambiguous sample-size field.

### 4.5 Administration

Use independent fields. Do not combine them into one label.

- interaction: self-completed, interviewer-assisted, or interviewer-administered;
- channel: paper, web, app, telephone, video, or in person;
- respondent: patient, general public, child, caregiver, clinician, or expert;
- perspective: self, proxy-person, proxy-proxy, adult perspective for a child, or social perspective;
- setting: home, clinic, hospital, school, community, or remote;
- instrument language and version;
- interview language;
- recall period;
- time point or repeated-measure schedule.

This supports questions about digital, paper, interview, proxy, and language differences.

### 4.6 Research and valuation method

Store exact values. Important examples include:

- conventional TTO;
- lead-time TTO;
- cTTO;
- DCE;
- DCE with duration;
- DCE with death;
- person trade-off;
- visual analogue scale;
- paired comparison;
- ranking;
- cognitive interview;
- think-aloud interview;
- focus group;
- Delphi or expert consultation;
- survey;
- psychometric assessment;
- mapping;
- systematic review;
- meta-analysis.

`Hybrid` is not a valuation method. It is normally a statistical model or analysis that combines data from methods such as cTTO and DCE.

### 4.7 Protocol and task design

Record a named protocol and version when available. Examples are `EQ-VT 2.1` and `EQ-VT 2.6.1`.

Add task details only when they distinguish the study or answer a question. Examples are:

- number of tasks per respondent;
- health-state design;
- blocking;
- duration or death anchor;
- task order;
- feedback module;
- quality-control rules;
- interviewer training or monitoring.

### 4.8 Analysis and statistical model

An analysis can use several model candidates. Store each model with its role:

- candidate;
- preferred;
- final;
- sensitivity analysis;
- comparator.

Store the exact source model label and a normalized model family. Examples include:

- random-effects generalized least squares;
- Tobit;
- heteroskedastic Tobit;
- conditional logit;
- mixed logit;
- latent-class model;
- hybrid cTTO-DCE model;
- hybrid heteroskedastic Tobit model;
- linear mapping model;
- nonlinear mapping model;
- Rasch model;
- regression model;
- random-effects meta-analysis.

Keep material qualifiers such as censoring, heteroskedasticity, random effects, data source, link function, and anchoring.

### 4.9 Outcome and measurement property

Use the source term and a controlled family. Examples include:

- utility or index score;
- EQ VAS score;
- health-state preference;
- feasibility and acceptability;
- completion and missingness;
- ceiling or floor effect;
- content validity;
- convergent validity;
- known-groups validity;
- reliability;
- agreement;
- responsiveness;
- discriminatory ability;
- model fit or predictive performance;
- implementation barrier or facilitator.

An outcome states what was measured. It does not contain all participant values.

### 4.10 Research product

Keep product types distinct:

- native value set or tariff;
- crosswalk value set;
- mapping function;
- scale-anchoring function;
- scoring algorithm;
- instrument, version, or form;
- translation or cultural adaptation;
- bolt-on dimension;
- protocol or task design;
- population norms or reference values;
- dataset or research infrastructure;
- implementation programme;
- taxonomy, guidance, or evidence synthesis.

For a value set, record its target instrument, jurisdiction, preference population, derivation basis, model, status, and source publication. Do not call a crosswalk a native value set.

## 5. Findings and reported values

### 5.1 What to store

For each study, store the study-level findings that a researcher needs to understand its contribution. The number depends on the paper. A short commentary can have one main argument. A valuation study can need several findings. Each finding has:

- a short, source-faithful statement;
- an optional finding type, such as difference, association, no clear difference, feasibility, validity, recommendation, or gap;
- links to the relevant population, instrument, method, outcome, comparator, and time point;
- an optional direction;
- key aggregate estimates when they are needed to understand the finding;
- the authors' interpretation or practical impact;
- a reported limitation or caveat;
- a source location.

### 5.2 What not to store

- No participant-level values.
- No full copy of every result table.
- No assertion record for every coefficient or p value.
- No unsupported causal statement.

The detailed numeric artifact can stay in a linked table, file, or source document. For example, a value-set product can link to its complete 3,125-state table. The ontology stores the product identity, derivation, range, anchors, and important summary facts.

For a valuation study, extraction normally covers the reported utility range or anchors, the lowest and highest states when relevant, the order or relative importance of dimensions, the selected model and why it was selected, and other notable findings that the authors emphasize. It can also include the proportion of states or observations worse than dead, consistency results, or material method comparisons when these facts are central. This is a level-of-detail instruction, not a numeric quota.

Also capture author-reported limitations, data-quality caveats, scope limits, source conflicts, and research gaps. Do not invent a limitation from general knowledge.

### 5.3 Source conflict

Most records only need ordinary source fields. Use a small `Reported value conflict` record only when sources report different values for the same fact. Preserve both values, their source locations, and the review decision. Do not make this mechanism the center of the ontology.

## 6. Research portfolio module

The competency questions also need these linked records:

- `Funded project` and project ID;
- `Funding award`, amount, currency, decision date, and recipient;
- `Person` and source names;
- `Organization` and country;
- project role, authorship, affiliation, membership, and working-group membership with dates;
- `Project-publication link` with status and evidence;
- corpus inclusion or exclusion decision;
- identity-resolution decision;
- citation, open-access, venue, and topic records from named sources and snapshots.

A project-publication link can be `candidate`, `accepted`, `rejected`, or `superseded`. Record the exact support relation, such as study funding, data-collection funding, researcher support, travel support, or publication support. Counts use accepted links only.

If a paper reports no EQ instrument, accept the project-publication link only when the article states that EuroQol supported the work or its data, or when an authoritative EuroQol project record lists the paper as an output. Folder placement, author overlap, topic similarity, or an author's competing-interest grant disclosure is not enough. Keep such links as candidates until they are verified.

Official publication metadata is mandatory but it is not an AI extraction task. Parse available structured records before semantic extraction. Preserve DOI, PMID, PMCID, title, abstract, authors and order, ORCID, affiliations, correspondence, journal, publisher, article type, language, dates and their roles, volume, issue, pages or article number, URLs, licence, keywords, funding fields, references, source identity, and source provenance. Give the agent this record as context and ask it not to reconstruct the same data from prose.

This module is necessary for the project, people, funding, and citation questions. It must not distort the scientific ontology.

## 7. Provenance without an assertion graph

Every extracted record has a small common header:

- source publication or source system;
- source location;
- exact source term or short excerpt when useful;
- extraction date and method;
- review status;
- optional confidence or conflict status.

Normalization adds a canonical term. It does not replace the source term.

For example:

```text
source label: "composite time trade-off"
canonical term: cTTO
term family: valuation method
source: S008, Valuation Techniques
```

This gives traceability without a subject-predicate-object claim for every field.

## 8. Agent-facing extraction description

Give an extraction agent this short instruction:

> Describe what the study did and found. Use the exact names from the source. Complete only the sections that apply. Identify the study type or types, target population, samples, concepts and themes, exact instruments and their roles, administration, exact research methods, protocol and important task details, analyses and exact models, measured outcomes or properties, products, findings, interpretations, and limitations. Extract enough findings to explain the study's contribution; do not use a fixed count. Keep project and publication facts separate from study facts. Use supplied publication metadata and do not reconstruct it. Extract no participant-level data. Do not reproduce complete result tables. Give a source location for each section. Mark missing or conflicting facts. Do not infer a fact only because it is common practice.

The output can be compact Markdown. It does not need nested JSON during ontology development.

Suggested headings are:

```text
Identity and study type
Population and samples
Concepts and themes
Instruments and administration
Methods, protocol, and task design
Analysis and statistical models
Products
Principal findings and interpretation
Limitations and source issues
High-value exact terms
```

These headings guide the agent. They do not force every study into one rigid template.

## 9. Worked examples

### 9.1 Moroccan EQ-5D-5L value set

Source: summary `S008`, DOI `10.1007/s11136-025-03930-1`.

| Field | Value |
|---|---|
| Study type | national valuation study; value-set development |
| Concepts and themes | states worse than dead; health-state anchoring; national value-set transferability |
| Population | Moroccan adults |
| Sample | 1,048 interviewed; 976 analyzed |
| Instrument | EQ-5D-5L |
| Instrument role | valued; administered to describe respondent health |
| Administration | computer-assisted face-to-face; Moroccan Arabic or French |
| Protocol | EQ-VT 2.6.1 |
| Valuation methods | cTTO; DCE |
| Candidate models | heteroskedastic censored Tobit; conditional logit; hybrid model |
| Preferred model | hybrid heteroskedastic Tobit model |
| Product | Moroccan EQ-5D-5L value set |
| Product basis | native direct valuation |
| Main finding | The preferred model was logically consistent and produced utilities from 1 for 11111 to -1.492 for 55555 |
| Interpretation | Intended for Moroccan HTA, economic evaluation, routine PROM use, and international comparison |
| Limitation | Rural, illiterate, and low-literacy participants were under-represented |

This example shows the required corner pieces. `Valuation study`, `cTTO`, `DCE`, `EQ-5D-5L`, and `hybrid heteroskedastic Tobit model` are queryable values.

### 9.2 EQ-TIPS content-validity work

Source: summary `S061`, DOI `10.1007/s11136-025-04150-3`.

- Study types: instrument development; content-validity study; qualitative stakeholder study.
- Population: 33 experts from 15 countries.
- Instrument: experimental EQ-TIPS V2.0, also called EQ-TIPS-3L.
- Method: three online semi-structured focus groups.
- Analysis: mainly deductive thematic analysis with allowed inductive themes; NVivo 14.
- Product status: further instrument development; no value set or psychometric evidence produced.
- Principal findings: Experts wanted a clearer construct, observable examples, careful proxy instructions, and further study of sleep.
- Limitation: The study did not test caregivers or children directly.

### 9.3 Measurement properties in Pompe disease

Source: summary `S090`, DOI `10.1007/s10198-024-01682-2`.

- Study type: measurement-property comparison.
- Population: 117 Chinese patients with late-onset Pompe disease.
- Instruments: EQ-5D-3L, EQ-5D-5L, SF-6Dv2, and WHODAS-12.
- Administration: web survey with a one-week retest.
- Properties: ceiling and floor effects, convergent validity, known-groups validity, and test-retest reliability.
- Statistics: Gwet's agreement coefficient, ICC, Spearman correlation, ANOVA, and Bland-Altman plots.
- Principal finding: EQ-5D-5L had lower ceiling and floor effects and stronger validity and discrimination. EQ-5D-3L had better test-retest agreement.
- Limitation: Volunteer and web recruitment can cause selection bias. WHODAS-12 did not support a full pain-validity assessment.

## 10. Question coverage

The ontology core supports the scientific meaning in all questions. The complete system also needs project, people, corpus, citation, and current-registry data. It must not pretend that the paper corpus contains these external facts.

The full map is in [QUESTION_COVERAGE.md](QUESTION_COVERAGE.md). It assigns every question from Q1 to Q100 to its required ontology and data modules.

## 11. Implementation recommendation

Use a relational database first. SQLite is sufficient for the pilot. PostgreSQL is suitable when concurrent use, stronger search, or larger data volumes become necessary.

Use ordinary tables for the main records and link tables for many-to-many relations. Keep controlled terms and aliases in small vocabulary tables. Keep large value-set tables and other detailed artifacts in linked structured tables or files.

Do not let the database engine define the ontology. A graph view can be generated later if relationship browsing proves useful.

## 12. Validation plan

Before full extraction:

1. Apply this proposal to a new holdout set with broad study types.
2. Ask agents to extract compact Markdown records with the instruction above.
3. Check whether the exact corner-piece terms survive extraction.
4. Run representative questions for valuation, instruments, psychometrics, population, implementation, findings, and project links.
5. Add or split a controlled term only when evidence shows that users need the distinction.
6. Review conflicts and unknowns. Do not fill gaps by inference.
7. Freeze ontology version 1 only after the holdout review.

## 13. Decisions for human review

The final proposal makes these recommendations:

- Approve the compact domain core above.
- Approve exact controlled values and aliases as the center of the ontology.
- Approve study-level findings and the aggregate results needed to understand them. Reject participant-level values and exhaustive table extraction.
- Approve a separate portfolio module and a separate derived analytics layer.
- Approve record-level provenance. Reject a universal assertion graph.
- Approve a relational pilot implementation.

There is no default finding count. Extraction depth follows the study's contribution and the rule in section 5.
