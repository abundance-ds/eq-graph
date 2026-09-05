# Release aggregate-validity test

Test the assigned questions against the current public database at
`web/server/data/serving.sqlite`. Use the private database at
`scale/protocol-2.0/fulltext-release-v1/research.sqlite` only when a question
needs audit, provenance, or reference evidence that the public release omits.

- Judge whether the scientific answer is coherent, not only whether SQL runs.
- Use `PASS`, `PARTIAL`, `FAIL`, or `NOT TESTABLE`.
- Classify each limitation as `NONE`, `QUERY`, `DATA`, `STRUCTURE`,
  `MISSING_INPUT`, or `UNSAFE`.
- Do not treat missing data as evidence of absence.
- Keep research family, design, purpose, method, and publication form separate.
- Do not fit the ontology to a question. Reject graph debt.
- A safe bounded or unavailable answer is acceptable.
- Use `sqlite3 -readonly`. Do not change files.

For each question, give one short result and one short cause. Base each verdict
on current database evidence.
