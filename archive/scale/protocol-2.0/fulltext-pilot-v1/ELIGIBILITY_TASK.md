# Full-text eligibility pilot

Assess one paper from its supplied full text. Use no external source.

## Connection

Choose one value:

- `DIRECT_EQ`: An EQ instrument, EQ value set, EQ scoring product, EQ-VT protocol,
  or another EuroQol-specific method is a main research object.
- `ADJACENT_MEASUREMENT`: Health or wellbeing measurement or health-state
  valuation is a main research object, but the paper has no direct EQ focus.
- `APPLICATION_ONLY`: An EQ instrument, utility, QALY, or HRQoL measure is only a
  tool, outcome, covariate, or model input.
- `UNRELATED`: The paper has no substantive measurement or valuation focus.
- `UNCLEAR`: The supplied text does not permit a reliable classification.

## EuroQol support

Choose one value:

- `CURRENT_WORK`: EuroQol explicitly funded or supported this study or paper.
- `DATA_OR_PRIOR_COMPONENT`: EuroQol explicitly supported data, a project, or a
  research component used in this paper.
- `AUTHOR_SUPPORT`: The paper states that EuroQol supported an author and this is
  not only a conflict-of-interest disclosure.
- `DISCLOSURE_ONLY`: EuroQol appears only as membership, affiliation, advice,
  licence, or a conflict-of-interest disclosure.
- `OTHER_FUNDER_ONLY`: A funding statement names funders, but not EuroQol.
- `NONE_STATED`: The supplied paper appears complete, but it names no funding or
  support. A missing funding heading alone does not make the result unclear.
- `UNCLEAR`: The source appears truncated, omits relevant pages, or contains wording
  whose support relation cannot be resolved.

Do not infer support from authorship, topic, instrument use, membership, or a
project title. Record the exact EuroQol statement when one exists.

## Recommendation

- `INCLUDE`: `DIRECT_EQ`, or explicit EuroQol support in `CURRENT_WORK`,
  `DATA_OR_PRIOR_COMPONENT`, or `AUTHOR_SUPPORT`.
- `EXCLUDE`: `APPLICATION_ONLY`, `ADJACENT_MEASUREMENT`, or `UNRELATED`, with no
  explicit EuroQol support.
- `HUMAN_REVIEW`: The connection or support relation is unclear, contradictory,
  or depends on an incomplete source section.

Give one short source locator and one short evidence statement for each judgment.
Do not extract methods, findings, limitations, projects, or ontology records.
