# EuroQol research graph

## Center

```text
(Person) --AUTHORED--> (Publication) --REPORTS--> (Study)

(Publication) --CORRECTS or RETRACTS--> (Publication)

(Project) --SUPPORTED {exact scope}--> (Study, Publication, or Person)

(Study)
  +--HAS_PURPOSE------> (Research purpose)
  +--HAS_DESIGN-------> (Study design)
  +--STUDIES----------> (Population)
  +--HAS_SAMPLE-------> (Sample)
  +--USES_DATA--------> (Dataset or cohort)
  +--USES_INSTRUMENT--> (Instrument use) --OF--> (Instrument)
  +--USES_METHOD------> (Method use) -----OF--> (Method)
  +--FOLLOWS----------> (Protocol)
  +--ANALYZED_WITH----> (Statistical model)
  +--MEASURES---------> (Outcome or measurement property)
  +--PRODUCES---------> (Research product)
  +--CONCERNS---------> (Concept or theme)
  +--REPORTS----------> (Finding)
  +--HAS_LIMITATION---> (Limitation)
  +--HAS_CONFLICT-----> (Source conflict)
```

## Meaning

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
  coefficient or participant value.

## Relationship details

Some relationships carry facts:

```text
Study --USES_INSTRUMENT--> EQ-5D-5L
          role: valued
          language: Moroccan Arabic
          respondent: general-public adult
          perspective: social
          interaction: interviewer-administered
          channel: computer-assisted face-to-face
          scoring source: not applicable

Study --ANALYZED_WITH--> hybrid heteroskedastic Tobit model
          role: preferred final model
          input: cTTO and DCE
          qualifier: cTTO censoring at -1
```

Use exact source terms and a preferred label when the mapping is clear. Keep
an uncertain new term as a candidate. Do not force it into an existing term.
