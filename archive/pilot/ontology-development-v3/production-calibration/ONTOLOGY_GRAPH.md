# EuroQol research graph

## Center

```text
(Affiliation) <--AFFILIATED_WITH-- (Person) --AUTHORED--> (Publication)
(Publication) --REPORTS_STUDY--> (Study)
(Publication) --CITES {order, source text, identity status}
              +---> (Publication identified by DOI or PMID)
              +---> (paper-scoped unresolved bibliographic reference)

(Publication) --CORRECTS or RETRACTS--> (Publication)

(Project) --SUPPORTS_STUDY-------> (Study)
          --SUPPORTS_PUBLICATION-> (Publication)
          --SUPPORTS_PERSON------> (Person)
          --SUPPORTS_DATASET-----> (Dataset use)
(Project) --HAS_OUTPUT-----------> (Publication)
(Project) --IN_WORKING_GROUP-----> (Working group)
(Project) --LED_BY---------------> (Person; verified profile only)
(Project) --HAS_LINK_ASSESSMENT--> (Project-link assessment)
                                      --ASSESSES_PUBLICATION--> (Publication)
                                      --ASSESSES_STUDY--------> (Study)

(Study)
  +--HAS_PURPOSE------> (Research purpose)
  +--HAS_DESIGN-------> (Study design)
  +--STUDIES_POPULATION-> (Population)
  +--HAS_SAMPLE-------> (Sample)
  +--USES_DATA--------> (Dataset or cohort)
  +--USES_INSTRUMENT--> (Instrument use) --OF_INSTRUMENT--> (Instrument)
  +--USES_METHOD------> (Method use) -----OF_METHOD------> (Method)
  +--FOLLOWS_PROTOCOL-> (Protocol)
  +--ANALYZED_WITH----> (Model use) ------OF_MODEL-------> (Statistical model)
  +--MEASURES_OUTCOME-> (Outcome or measurement property)
  +--PRODUCES---------> (Research product)
  +--CONCERNS---------> (Concept or theme)
  +--REPORTS_FINDING--> (Finding)
  +--HAS_LIMITATION---> (Limitation)
  +--HAS_SOURCE_CONFLICT-> (Source conflict)
```

```text
(Finding)
  +--ABOUT_OUTCOME----> (Outcome)
  +--ABOUT_INSTRUMENT-> (Instrument)
  +--ABOUT_METHOD-----> (Method)
  +--ABOUT_MODEL------> (Statistical model)
  +--IN_POPULATION----> (Population)
```

## Meaning

- JATS supplies publication identifiers, dates, journal fields, authors,
  affiliations, correspondence, categories, funding statements, and
  references. Deterministic code loads these facts before semantic extraction.
- Citations are a secondary provenance layer. A normalized DOI, or a PMID that
  resolves to an existing publication, can join reference occurrences. A
  reference without either identifier stays local to the citing paper. Do not
  merge references by title, author, or journal similarity.
- Do not count cited external publications as corpus publications. The corpus
  boundary comes from `source_record`, not from the `Publication` node count.
- For PDF input, do not ask the semantic extraction agent to rebuild the
  bibliography. Keep it out of the evidence prompt and parse it later with a
  dedicated tool only if citation coverage is required.
- The project register supplies all projects, including projects without a
  linked publication. Accepted linkage evidence adds support and output edges.
- An exact ORCID can attach a verified researcher profile. Names alone do not
  merge people.
- A `Publication` is an identifiable output. A `Study` is the investigation
  that it reports. A correction notice is a publication, not another study.
- A support relationship keeps its reported target and scope. Author support,
  a travel grant, data-collection funding, and full study funding are not
  interchangeable.
- `Research purpose` says why the study was done. `Study design` says how it
  was organized.
- `Instrument use` states what the study did with an exact instrument or
  version. Examples are valued, administered, translated, evaluated, scored,
  mapped, shown for comment, used as a predictor, or displayed as historical
  data.
- `Method` is the research procedure, such as cTTO, DCE, cognitive interview,
  or systematic review. `Statistical model` is the analysis model, such as a
  conditional logit or hybrid heteroskedastic Tobit model.
- `Research product` is a reusable output, such as a value set, instrument,
  checklist, prediction model, or decision aid. Its status is part of the
  relationship: planned, developed, tested, validated, implemented,
  superseded, or retracted.
- `Concept or theme` is a flexible discovery term. Examples are states worse
  than dead, child health, proxy reporting, digital health, health inequality,
  and routine PROM implementation.
- `Finding` contains principal study-level results. It is not a copy of every
  coefficient or participant value. A finding keeps its aggregate values as
  properties and links to the outcome, instrument, method, model, or population
  that gives the result its meaning.
- A `Project-link assessment` keeps accepted and possible candidate judgments,
  evidence, counter-evidence, support scope, and output status. Only an accepted
  judgment creates a trusted support or output relationship.

## Relationship details

Some relationships carry facts:

```text
Study --USES_INSTRUMENT--> Instrument use --OF_INSTRUMENT--> EQ-5D-5L
          role: valued
          language: Moroccan Arabic
          respondent: general-public adult
          perspective: social
          interaction: interviewer-administered
          channel: computer-assisted face-to-face
          scoring source: not applicable

Study --ANALYZED_WITH--> Model use --OF_MODEL--> hybrid heteroskedastic Tobit model
          role: preferred final model
          input: cTTO and DCE
          qualifier: cTTO censoring at -1
```

Use exact source terms and a preferred label when the mapping is clear. Keep
an uncertain new term as a candidate. Do not force it into an existing term.
