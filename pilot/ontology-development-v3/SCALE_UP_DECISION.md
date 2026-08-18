# Scale-up decision brief

> **Historical gate, completed on 2026-08-17.** The recommended 50-paper
> calibration was approved and completed, followed by the complete 209-paper
> local JATS pass and an independent full-source audit. The current decision is
> [`production-calibration/DECISION.md`](production-calibration/DECISION.md).

## Recommended decision

Approve `ONTOLOGY_V1.md` as the extraction ontology for a controlled production
pilot. Run one 50-paper calibration batch with automated JATS metadata, AI
semantic extraction, and independent sample QA. Review that evidence before a
full-corpus run.

Do not redesign the ontology before this calibration unless the 50-paper batch
shows a repeated failure.

## What is now proven

- Exact EuroQol corner pieces remain direct searchable values.
- A flexible concepts layer supports discovery without replacing exact facts.
- Study-dependent findings and explicit limitations fit varied papers.
- Verified EuroQol-supported papers can remain in scope when they use no EQ
  instrument.
- SQLite supports the tested search and synthesis questions.
- JATS can supply deterministic metadata without asking an AI to reconstruct
  it.
- The model handles protocols, corrections, retractions, source conflicts,
  remote modes, language versions, historical instrument data, and conceptual
  methods papers.
- The first pilot passed 15 queries. The broader pilot passed 23 queries.

## What is not yet proven

- Production AI extraction accuracy across the full corpus.
- The review effort per paper at scale.
- Reliable automatic normalization of new exact terms and concepts.
- Complete project-publication linkage when article funding evidence is weak.
- Whether rare study families need optional profiles.

## Proposed calibration gate

Use 50 papers that are outside all design and validation sets. Stratify them
across common and rare study families. The extraction agent receives:

1. deterministic JATS metadata;
2. clean full text;
3. `ONTOLOGY_V1.md`;
4. a concise Markdown extraction task;
5. the 100 user questions as purpose, not as a rigid output schema.

Audit at least 15 records in full, with deliberate coverage of valuation,
psychometric, implementation, qualitative, evidence-synthesis, non-EQ, and
publication-lifecycle cases.

Proceed to the full corpus only if:

- no unsupported project link enters verified funded counts;
- no retracted or planned product appears as current evidence;
- exact instruments, versions, methods, models, and administration modes are
  correct in at least 95% of audited applicable fields;
- principal findings and limitations are source-faithful in at least 90% of
  audited records;
- all material errors can be fixed by term normalization or prompt guidance,
  without a new top-level ontology concept;
- the 100 competency questions remain answerable or have an explicit data-gap
  explanation.

## Decision principles

- Prefer direct value to theoretical completeness.
- Add a distinction only when papers differ on it and a user can use it.
- Preserve exact source terms before normalization.
- Treat funding, lifecycle, and planned-versus-completed state as safety data.
- Keep extraction flexible. Keep database constraints strict where errors
  would mislead users.
- Change the ontology only for repeated structural failure, not one rare fact.

## Human decision requested

When you return, decide one point:

> Approve ontology v1 and authorize the 50-paper calibration batch, or identify
> a specific core distinction that must change first.

Recommended answer: approve the 50-paper calibration batch.
