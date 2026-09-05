# Aggregate-validity rerun

Test the 100 user questions against `web/server/data/serving.sqlite`.

- Judge whether the scientific answer is coherent, not only whether SQL runs.
- Use `PASS`, `PARTIAL`, `FAIL`, or `NOT TESTABLE`.
- State the evidence-base boundary when it matters.
- Do not treat missing data as evidence of absence.
- Do not propose ontology fields to make a question pass.
- Do not fit the graph to the questions; reject graph debt.
- A safe `PARTIAL` or `NOT TESTABLE` result is acceptable.
- Report the current result and the main cause in one short sentence each.

The prior test is `../aggregate-validity-v2/RESULT.md`. Recheck its claims
against the current database. Person identities, project leaders, observed
EuroQol membership, exact registry mappings, and OpenAlex citation counts have
changed since that test.
