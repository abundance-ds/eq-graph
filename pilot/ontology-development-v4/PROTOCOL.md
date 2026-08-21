# Typed ontology iteration protocol

## Aim

Develop a practical EuroQol research ontology that different capable agents
can apply consistently. Do not optimize the ontology for individual user
questions.

## Three information layers

1. **Stable structure:** paper, study, population, sample, dataset, instrument
   use, method use, model use, outcome, finding, limitation, product, concept,
   project, person, and organization.
2. **Controlled scientific values:** canonical values with operational
   definitions. Examples are research purpose, data origin, method role,
   instrument-use role, and product type.
3. **Open information:** source-faithful names, concepts, findings,
   interpretations, limitations, and evidence text.

An instrument, method, protocol, model, or language is a controlled registry
entry. It is not a large schema enum. Store the canonical identity and the
source term.

## Gap states

- `UNMAPPED_VALUE`: the key exists, but no controlled value fits.
- `UNMODELED_ASPECT`: an important fact has no suitable key or relationship.
- `UNCERTAIN_MAPPING`: more than one existing mapping is plausible.
- `NOT_REPORTED`: the source does not report the information.

Each gap must include the source evidence, why it matters, and a proposed
resolution. A gap is not a permanent scientific category.

## Expansion rule

A builder cannot add a canonical value while it extracts a paper. It proposes
the value in the gap log. An independent reviewer returns `MERGE`, `ACCEPT`,
`REJECT`, or `KEEP_OPEN`.

Accept a new key or value only when it:

- has a clear operational definition;
- is not a synonym or a combination of existing values;
- represents one scientific dimension;
- can be distinguished from its neighbours from normal paper reporting;
- supports comparison across papers;
- is supported by repeated evidence or by an important distinct research
  design.

Do not create a key or value only because one competency question mentions it.

## Round sequence

1. Propose the typed vocabulary.
2. Apply it to every paper in the round.
3. Record forced mappings, gaps, ambiguity, and missing information.
4. Review proposals independently and check disputed cases against the source.
5. Revise the ontology and reapply it to all earlier papers.
6. Add a larger, diverse paper batch.

Planned sizes are 15, 30 cumulative, a 45-paper confirmation point,
approximately 60 cumulative, and then the full corpus. The confirmation point
was added after round 2 accepted several structural changes. Batch size can
increase only when earlier papers still fit and a new batch causes few
structural changes.

## Acceptance checks

- Controlled fields contain only canonical values or a gap state.
- Separate axes do not mix purpose, design, time, data origin, and publication
  status.
- Method and instrument roles distinguish direct use, source-study context,
  observed object, planned use, and discussion only.
- Missing information does not become `no`, zero, or an empty category.
- Multi-value fields do not form false mutually exclusive groups.
- Every paper has a complete application record with source support.
- Treat `primary_research_family` as a high-impact analytical classification.
  A controlled code is necessary but does not prove that the mapping is
  correct. Review disagreements and close cross-family cases before aggregate
  publication.
- A later aggregate test uses the 100 questions. `NOT TESTABLE` remains valid
  when the required information is absent.
