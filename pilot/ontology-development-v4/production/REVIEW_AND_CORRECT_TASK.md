# Independent source review and correction

This is the second and final AI call for one paper. Compare the draft record
with the full article and deterministic metadata. The article is authoritative.
Return a review summary and the complete corrected record.

Check the filter decision, each author-defined Study, family, purposes, status,
parts, design, populations, sample flow, data, exact instruments, methods,
protocols, models, scoring, tasks, administration, principal findings,
reported aggregate values, interpretations, limitations, products, concepts,
gaps, source conflicts, roles, and relations.

Correct each supplied deterministic validation error. Remove invented facts and
derived values that the authors do not report. Add important omitted facts.
Preserve supported detail. Keep exact scientific labels and leave registry IDs
null for deterministic normalization.

Use `PASS` when the draft needs no material change, `MINOR` for local
corrections, and `MAJOR` for a wrong filter decision, Study unit, primary
family, main method or instrument role, principal result, or material omission.
List the changes and their source locations. Report an ontology gap only when
an important source fact cannot fit the supplied structure or controlled
values. Do not propose a controlled value for a one-paper distinction.
