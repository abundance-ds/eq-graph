# Broad-filter calibration

- Corpus: 2,311 source records.
- Seed: `20260801`.
- Authors: 10.
- Audit: 80 records.
- Input limitation: title + year + DOI; abstract/type absent in comparison file.

## Refinements

1. Keep explicit EQ terms.
2. Keep value sets; tariffs; health states.
3. Keep valuation methods without named EQ instrument.
4. Keep DCE; preference studies.
5. Keep generic QoL; instrument development.
6. Keep PROM; psychometrics; validation.
7. Keep protocols.
8. Keep reviews; meta-analyses.
9. Keep technical valuation methods.
10. Separate document junk from topic.
11. Exclude paratext even when EQ-linked.
12. Route authorship noise to profile verification.

## Frozen rule

- Objective junk: exclude.
- Plausible EQ/measurement/valuation relation: keep.
- Uncertain: keep for full-text review.
- Clearly outside: exclude.
- Profile noise: flag upstream.

## Risks

- False exclusion: clinical/economic/generic-QoL paper with hidden utility evidence.
- False inclusion: wrong-author record.
- Control: full text + AI; profile verification; audit samples.
