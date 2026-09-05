# Expanded-corpus aggregate-validity test

Test the assigned user questions against `web/server/data/serving.sqlite`.

- Judge whether the scientific answer is coherent, not only whether SQL runs.
- Use `PASS`, `PARTIAL`, `FAIL`, or `NOT TESTABLE`.
- State the 273-publication evidence boundary when it matters.
- Do not treat missing data as evidence of absence.
- Keep unlike classifications separate. For example, do not mix research
  family, design, purpose, method, and publication form.
- Do not propose ontology fields to improve a verdict.
- Do not fit the graph to the questions. Reject graph debt.
- A safe `PARTIAL` or `NOT TESTABLE` verdict is acceptable.
- Use `sqlite3 -readonly` for all database queries. Do not change files.

For each assigned question, return one short result and one short main cause.
Base each verdict on current database evidence.
