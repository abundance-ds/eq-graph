# Comparison of the three ontology proposals

## Result

The three proposals converge on the same useful research facts. They differ mainly in how much structure they put around those facts.

The final proposal will use the shared domain core, but it will not use a universal assertion graph. Exact EuroQol terms will be first-class controlled values. Provenance will attach to each extracted record.

## Comparison

| Issue | Proposal A | Proposal B | Proposal C | Decision |
|---|---|---|---|---|
| Domain detail | Strongest detail for valuation methods, task designs, scales, models, and products | Strongest compact lists of exact instruments, methods, models, properties, and product types | Strongest separation of research content from project and corpus management | Combine these strengths |
| Instrument representation | Exact family, version, language, form, dimension, and use role | Best practical `Instrument use` record | Strong independent administration axes | Use an `Instrument use` record with the exact version and independent context fields |
| Methods | Rich method hierarchy and model roles | Clear exact method and model value families | Strong protocol, task-design, and quality-control detail | Keep exact methods, protocols, task design, and model roles; do not use a vague general methods tag |
| Findings | Very detailed result and assertion structure | Useful controlled finding types plus plain text | Strong links between findings and their study context | Store a small set of principal findings, optional aggregate results, interpretation, and limitations |
| Research administration | Complete, but secondary to the scientific model | Compact | Clearest project, output, person, organization, and corpus separation | Use this as a separate portfolio module |
| Provenance | Universal assertion layer | Universal evidence-assertion layer | Universal source-assertion layer | Reject as the central design. Use record-level source fields and a conflict record only when needed |
| Question support | Good, with explicit external-data limits | Good and concise | Best explanation of source facts versus derived analytics | Keep the source/extracted/derived separation and a complete dependency map |
| Implementation | Rich but heavy | Most practical minimum | Rich and careful, but heavy | Start with a relational implementation of the compact core |

## Accepted choices

- Separate `Project`, `Publication`, and `Study`.
- Make exact domain values searchable. Examples are `valuation study`, `EQ-5D-5L`, `cTTO`, `DCE`, and `heteroscedastic censored hybrid model`.
- Represent an instrument as an exact version. Represent its use in a study separately.
- Separate valuation method, protocol, task design, analysis, and statistical model.
- Treat study type as a multi-value classification. A study can be both a valuation study and a method-comparison study.
- Separate target population, recruited sample, and analytic sample.
- Separate administration mode, respondent, perspective, language, and setting.
- Separate a native value set, crosswalk, mapping function, scoring algorithm, translation, and population norms.
- Keep principal findings and interpretations. Do not copy all reported results into the ontology.
- Keep source facts separate from calculated counts, ranks, trends, networks, and similarity scores.
- Preserve exact source terms and map them to canonical terms. Do not erase aliases.
- Use evidence-bearing project-output links. A shared author or topic is not enough to make a link accepted.

## Rejected choices

- A generic `Component` concept. It hides the facts that users want.
- A generic `Paper` concept. Use `Publication`, and link it to the study or studies that it reports.
- A broad `Method` tag without an exact method value and role.
- `Hybrid` as a valuation method. It is normally a model or an analysis that combines data sources.
- One assertion node for every fact. This adds a claim-evidence graph that the project does not need.
- Participant-level outcomes or a full copy of every result table.
- One forced study type.
- One maturity ladder for all products. Development, validation, publication, recommendation, and use are different states.
- Country without a role. Study country, sample residence, value-set jurisdiction, language community, and author country are different facts.
- Calculated analytics as if they were claims from a paper.
- A graph-database structure as the conceptual starting point.

## Main trade-off

The model must be detailed where EuroQol studies differ, but sparse where detail does not improve search or synthesis.

The recommended rule is:

> Add a structured field when it answers a competency question, distinguishes studies that users would otherwise confuse, or supports a reliable filter. Keep other detail in the summary and source text.

This rule supports fine detail for instruments, valuation methods, administration, statistical models, and research products. It prevents a large schema for low-value details such as every coefficient, task pair, or protocol sentence.
