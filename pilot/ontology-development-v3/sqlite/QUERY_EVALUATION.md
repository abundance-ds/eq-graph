# Competency-query evaluation

Date: 2026-08-17

## Result

All 15 executable tests pass on the rebuilt database.

## What the tests establish

- A national value-set study returns `cTTO`, `DCE`, the selected hybrid model,
  the exact EQ-5D version, and the produced value set.
- The same method name can have a different role in a valuation study and a
  task-design experiment.
- Flexible concepts find children, digital health, and states worse than dead.
- Exact instrument language versions and proxy perspectives are queryable.
- A review publication is separate from its evidence units.
- Findings have study-dependent depth: the test set has three, four, or five
  findings per study.
- Reported limitations and source conflicts remain visible.
- Deterministic article metadata and references join to semantic records.
- A verified EuroQol-funded paper with no EQ instrument is retrievable.
- Rejected candidate funding links do not enter funded-project results.

## Interpretation

The pilot gives positive evidence for the ontology direction and for a
relational implementation. The later non-overlapping 20-paper test also passes
23 executable checks. Neither test proves production extraction accuracy for
the full research portfolio.
