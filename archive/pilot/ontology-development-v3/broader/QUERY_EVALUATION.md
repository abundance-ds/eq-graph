# Broader-test query evaluation

## Result

All 23 executable competency checks pass.

The database contains:

- 21 publications: 20 test publications and one correction parent;
- 19 studies: the correction notice is not a study;
- 18 accepted and two candidate project-publication links;
- 23 instruments and 44 instrument-use records;
- 37 research methods and 28 statistical models;
- 20 research products;
- 98 principal findings and 76 limitations.

## Tested distinctions

- verified EuroQol support when no EQ instrument appears;
- a candidate project link when the article gives no support evidence;
- exact non-EQ instrument language versions;
- paper, web, video, face-to-face, and interviewer roles;
- instrument valued, administered, discussed, shown, used as a predictor, and
  displayed as historical data;
- cTTO as method and video as channel;
- report time, reference time, recall period, and valuation duration;
- completed study versus planned protocol;
- co-design input versus implemented workflow;
- experimental estimates versus an operational value set;
- retracted publication and unsafe product;
- correction notice, corrected publication, and study separation;
- source conflict retention;
- conceptual methods paper with no participant sample;
- material derivation steps that add uncertainty.

## Commands

```text
python3 pilot/ontology-development-v3/broader/validate_batch.py
python3 pilot/ontology-development-v3/broader/build_broader.py
python3 pilot/ontology-development-v3/broader/test_queries.py
```

## Interpretation

The relational model answers the tested questions without a universal
claim-evidence graph. Exact EuroQol corner pieces remain direct searchable
values. The broader test required small safety and provenance additions, but
it did not require a different ontology center or a graph database.
