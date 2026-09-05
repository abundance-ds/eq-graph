# Broader-test ontology fit

## Assessment

The ontology fits the 20-paper broader test. The core structure remained
stable. The new papers required clearer state, time, publication, and use-role
distinctions. They did not require a generic paper ontology.

## Required revisions

| Revision | Evidence | Action |
|---|---|---|
| Publication lifecycle | B16 is retracted | Add an explicit lifecycle status. Exclude retracted outputs from default operational evidence. |
| Publication relations | B17 corrects an earlier article | Link the correction to its parent. Do not create a second study. |
| Study execution state | B10 is a protocol | Mark facts and products as planned until a results paper reports completion. |
| Instrument-use roles | B08, B11, B12, B18, and B20 use instruments in different ways | Keep exact roles for shown, administered, analyzed, valued, prediction input, and historical data display. |
| Time roles | B07 and B19 contain several kinds of time | Separate report time, referenced health-state time, recall period, and valuation duration. |
| Product state | B08, B09, B11, B16, and B20 have different maturity or safety states | Store a source-grounded product status. Do not infer approval or implementation. |
| Material derivation | B04, B11, and B13 transform evidence and add uncertainty | Store only transformations that materially change meaning or uncertainty. |
| Funding scope and evidence | B01, B02, B05, B10, B11, B12, and B18 have different evidence patterns | Store support type, evidence class, locator, and accepted or candidate link status. |

## Clarification: material derivation

This means: record an important transformation when a user must know it to
interpret the result.

Example:

```text
reported medians and ranges
  -> converted to estimated means and standard deviations
  -> pooled with a random-effects model
  -> pooled COVID-19 EQ-5D estimate
```

Do not store every calculation or every cited input. Store the shortest chain
that exposes a material assumption or a new source of uncertainty.

## Decisions that remain unchanged

- Exact study types, instruments, versions, methods, models, products, and
  outcomes are the ontology corner pieces.
- Concepts and themes remain a flexible discovery layer.
- Findings are concise study-level results, with depth set by the paper.
- Limitations and source conflicts are explicit.
- Publication metadata comes from JATS before AI extraction.
- A publication is an output. A study is the investigation that it reports.
  A correction notice is a publication but not a study.
- `Component` is not an ontology concept.
- No universal assertion graph is needed.
- No fixed finding count is needed.
- SQLite remains sufficient for this phase.

## Fields not justified by this test

- A full coefficient or result-table model.
- Participant-level data.
- A generic claim-evidence-finding triplet.
- A closed concept taxonomy.
- A separate class for each administration combination.
- A graph database.

## Residual risks

- The batch is purposive, not a prevalence sample of the corpus.
- The same primary reviewer extracted and source-checked these 20 records.
- Project links for B05 and B18 still need authoritative portfolio evidence.
- The local B16 sources do not give the retraction reason or date.
- The semantic loader uses curated test data. A production extraction agent
  still needs calibration and independent sample QA.
