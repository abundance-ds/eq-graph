# Production source audit

## Scope

- Checked all 15 records initially classified outside `direct_eq` plus all
  direct-EQ records with no stated EuroQol support.
- Scanned every direct-EQ study type and title for outcome-only studies.
- Compared ten varied records with their article abstracts, methods, results,
  limitations, and funding statements: valuation, psychometrics, model
  development, implementation, conceptual work, systematic review, protocol,
  supported application, and exclusion.
- Used JATS funding metadata when the Markdown conversion omitted the funding
  statement.

## Result

- Corpus disposition: no audit correction. The final set has 128 included
  studies and one unsupported application-only exclusion.
- Factual extraction: no sampled substantive fact required correction.
- Connection label: five corrections. P040, P118, and P126 became
  `application_only` after the clarified task. P013 and P127 required human
  adjudication to the same class.
- P002 and P106 remain `direct_eq` because they study routine EQ measurement as
  an implementation process. P046 remains `direct_eq` because it assesses EQ
  response distribution, floor and ceiling effects, and usefulness across
  pregnancy stages, not only population health outcomes.
- Source locators: 99.9% automatic recognition across substantive bullets.
- JATS value: P128 confirms why structured XML metadata is required. Its JATS
  funding group states that EuroQol grant 460-RA funded data collection, but
  the Markdown body has no funding heading.

## Rule confirmed by the audit

An EQ instrument as the main or only outcome does not make a paper direct EQ
research. A direct paper studies an EQ instrument, measurement process,
valuation, value set, mapping, reference norms, or measurement implementation.
A paper that uses EQ to study health, treatment, risk factors, inequalities, or
a service is `application_only`. Explicit EuroQol support still includes such a
paper in the corpus.

No ontology structure changed. The audit made one connection boundary more
precise and applied it to the final records.

## Final calibration confirmation

The final task was also rerun on the 30-paper source-checked calibration set.
After two targeted repairs, all 30 expected dispositions, all 30 structural
checks, and all 22 critical safety checks passed. The repaired records preserve
an article's internal significance conflict and the relation from a correction
notice to the corrected article. The combined 209-paper database includes
these final records.
