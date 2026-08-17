# EQ-v3 paper selection

Final packet assignment uses seed `20260817`: shuffle the 100 selected rows once, assign the first 25 to `shared`, and assign the next three groups of 25 to `A`, `B`, and `C`. Each lineage receives `shared` plus its private group.

## Coverage summary

This revised set contains 100 unique papers from the 228 Markdown records in
`corpus/`. It keeps 30 core valuation, value-set, and valuation-method papers.
The other 70 papers broaden the evidence to instrument development, scoring,
translation, psychometrics, administration, implementation, population health,
inequality, clinical use, economic use, stakeholder work, and evidence synthesis.

The set covers EQ-5D-3L, EQ-5D-5L, EQ-5D-Y-3L, EQ-5D-Y-5L, EQ-TIPS, EQ-HWB,
CHU9D, PROMIS, and comparator instruments. It includes cTTO/TTO, DCE, hybrid
models, DCE with duration, OPUF, mapping, crosswalks, item response theory,
qualitative work, self and proxy reports, online and video modes, translations,
bolt-ons, reference values, inequality, routine PROM collection, and economic
evaluation use.

Approximate primary-purpose counts are shown below. They are not mutually
exclusive because many papers have more than one use case.

- Valuation, value sets, and valuation methods: 30 core papers.
- Instrument, translation, bolt-on, and conceptual development: about 18.
- Psychometric, comparative measurement, and scoring work: about 25.
- Population norms, inequality, longitudinal, and clinical outcomes: about 18.
- Administration, implementation, qualitative, and stakeholder work: about 12.
- Economic, HTA, QALY, mapping, and evidence-synthesis work: about 14.

## Selection method

I read the corpus front matter, titles, abstracts, and selected method text. I
first protected a 30-paper valuation core. I then selected papers that add
coverage for the competency questions: mapping and scoring, translation and
adaptation, instrument and bolt-on development, psychometrics, administration,
routine clinical use, population norms and inequality, qualitative and
stakeholder views, economic and HTA use, systematic review, meta-analysis, and
longitudinal outcomes. The `broad_reason` column records the main reason for
each inclusion.

## Swaps from the first draft

The initial rebalance retained 80 first-draft DOIs and swapped 20
valuation-heavy papers for 20 broader-use papers. The independent audit then
applied the ten in-place swaps listed below.

### Removed

- `10.1007/s10198-021-01377-y`
- `10.1007/s10198-022-01481-7`
- `10.1007/s10198-023-01569-8`
- `10.1007/s10198-025-01812-4`
- `10.1007/s10198-025-01857-5`
- `10.1007/s11136-021-03075-x`
- `10.1007/s11136-022-03143-w`
- `10.1007/s40271-022-00573-z`
- `10.1007/s40271-025-00735-9`
- `10.1007/s40273-018-0615-8`
- `10.1007/s40273-020-00994-4`
- `10.1007/s40273-022-01208-9`
- `10.1007/s40273-022-01216-9`
- `10.1007/s41669-022-00353-3`
- `10.1007/s41669-023-00437-8`
- `10.1016/j.jval.2018.05.002`
- `10.1016/j.jval.2021.03.019`
- `10.1016/j.jval.2023.03.003`
- `10.1136/bmjopen-2021-051727`
- `10.1177/0272989X21999607`

### Added

- `10.1002/hsr2.70308`
- `10.1007/s10198-018-0987-x`
- `10.1007/s11136-020-02718-9`
- `10.1007/s11136-024-03618-y`
- `10.1007/s11136-026-04285-x`
- `10.1007/s40271-022-00572-0`
- `10.1007/s40271-025-00729-7`
- `10.1007/s40271-025-00749-3`
- `10.1007/s40271-025-00787-x`
- `10.1007/s40273-021-01109-3`
- `10.1007/s40273-022-01222-x`
- `10.1007/s40273-025-01476-1`
- `10.1007/s40273-025-01493-0`
- `10.1017/S0266462326103602`
- `10.1186/s12889-018-5706-0`
- `10.1186/s12955-023-02207-w`
- `10.1371/journal.pone.0319227`
- `10.3389/fpubh.2021.744405`
- `10.3390/curroncol32060308`
- `10.3390/curroncol32110645`

## Independent audit swaps applied in place

The following ten swaps replace the paper at the same `selection_order`. No
other rows were changed in this audit.

- `10.1007/s40273-022-01143-9` -> `10.1186/s12955-023-02144-8`
- `10.1007/s40273-024-01404-9` -> `10.1007/s40258-022-00772-7`
- `10.1007/s40273-023-01330-2` -> `10.1371/journal.pone.0197098`
- `10.1007/s40273-024-01354-2` -> `10.1186/s12955-024-02323-1`
- `10.1007/s40273-024-01355-1` -> `10.1186/s12955-024-02305-3`
- `10.1007/s10198-025-01770-x` -> `10.1016/j.jval.2024.05.007`
- `10.1007/s10198-021-01309-w` -> `10.1007/s11136-024-03770-5`
- `10.1002/ppul.71031` -> `10.1177/0272989X20969686`
- `10.1186/s12955-020-01410-3` -> `10.1007/s41669-024-00486-7`
- `10.3390/children8100920` -> `10.1007/s11136-025-04074-y`

## Boundary cases

- Protocols, qualitative studies, systematic reviews, stakeholder studies, and
  surveys are included when they expose a method, concept, population, or use
  case needed by the competency questions.
- Some papers are not value-set papers. They are included because users need to
  query scoring, mapping, translation, proxy reporting, routine use, economic
  analysis, or population outcomes.
- Papers from shared projects are retained when their DOIs and research roles
  differ. Duplicate DOI records were not retained.
- The selection excludes the Taiwan correction notice and the retracted Egypt
  valuation record.

## Known limits

This is a coverage sample, not a systematic review sample. Abstract-level
screening can miss details in tables and supplements. Country and instrument
coverage remains uneven, and newer records may have less replication evidence.
The set is designed for ontology proposals and competency-question testing; it
is not a final evidence hierarchy.
