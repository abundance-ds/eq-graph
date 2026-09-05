# Scientific registry normalization result

These counts describe the 273-publication corpus before the release.
The release registry maps 13,581 public scientific uses to 3,311 canonical identities; see [docs/RESULTS.md](../../../../docs/RESULTS.md).

Seven independent reviews covered all 4,411 distinct scientific labels and
6,018 uses in the 273-publication corpus. The reviewed registry maps 4,665
uses (77.5%) to 1,241 identities through 3,109 typed exact aliases. The prior
registry mapped 2,060 uses (34.2%). No ontology field or controlled research
axis changed.

| Type | Uses | Mapped | Coverage |
| --- | ---: | ---: | ---: |
| Instrument | 1,727 | 1,541 | 89.2% |
| Method | 2,573 | 1,710 | 66.5% |
| Model | 497 | 260 | 52.3% |
| Product | 161 | 149 | 92.5% |
| Protocol | 353 | 325 | 92.1% |
| Scoring product | 171 | 160 | 93.6% |
| Software | 536 | 520 | 97.0% |

The review deliberately keeps 1,103 uses with narrow or incidental labels
unmapped. It sends 248 uses to a repair queue because the extracted item must
be split or moved to another type. These labels remain in the private evidence
record, but they cannot become aggregate categories.

The production rule is now explicit: AI keeps the exact paper wording but
does not invent a registry identity. Deterministic code assigns only a reviewed
exact alias. Aggregate views use only global canonical identities; unresolved
and paper-specific labels remain available for paper-level review.

The unresolved-label review is mandatory after each ingestion tranche. A null
identity is an extension request, not a permanent rejection.

The private and public SQLite builds pass count, relation, foreign-key, and
integrity checks. The public database now carries the stable registry and does
not put raw or paper-specific labels in its instrument and method category
tables.
