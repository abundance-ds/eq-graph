# Flat search index

For an included study, format `### High-value terms` as a flat typed index.
Use one bullet for each exact term:

```text
- Study type: national valuation study
- Population: German general-population adults
- Instrument: EQ-5D-5L
- Method: cTTO
- Model: hybrid model 3b
- Product: German EQ-5D-5L value set
- Concept: states worse than dead
```

Allowed types are `Study type`, `Design`, `Population`, `Dataset`, `Instrument`,
`Language`, `Administration`, `Method`, `Protocol`, `Analysis`, `Model`,
`Product`, `Outcome`, `Concept`, `Condition`, `Setting`, and `Geography`. Use
only types that apply. Use `Analysis` for statistical tests and techniques;
reserve `Model` for fitted, prediction, or valuation models. Keep qualifiers
and explanations in the main record. `Instrument` means a measurement
instrument, not a treatment, device, or clinical procedure. `Condition` means
a disease or health condition. If no precise type applies, use `Concept`; do
not force a term into another type. List a term under one best type only. For
example, a fitted regression belongs under `Model`, not also under `Analysis`.
Put thematic or content analysis under `Analysis`. Put a measurement property,
such as validity, reliability, responsiveness, or agreement, under `Outcome`,
not `Method`. An instrument can produce a score or value as an `Outcome`; do
not repeat the instrument label as the outcome.
Do not add source locators or sentences to this index.
