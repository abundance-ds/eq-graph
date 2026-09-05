# SQL-native single-agent pilot

## Result

- Model: `gpt-5.6-sol`, high reasoning effort
- Papers: 5 from the prior Opus pilot; 3 included and 2 excluded
- Saved and valid records: 5 of 5
- Eligibility decisions: 5 of 5 matched Opus
- Primary research families: 3 of 3 matched Opus
- Exact project links: 2 of 3 included papers matched Opus
- Included records: 237 typed items
- Proposed registry changes: 16; proposed enum changes: 0

Sol linked `P9c72daab39ca` to project `2013320`; Opus did not. The paper uses the
exact 2014 project data as external-validation data, so the link is defensible,
but the project did not produce the paper's main data. This is a project-link
policy edge case, not an extraction-interface failure. Under the current
direct-origin rule, do not retain this link in production.

## Assessment

The SQL interface passed the pilot. Sol captured the main instruments, methods,
models, products, findings, interpretations, limitations, and recurring concepts.
Known names resolved to canonical registry identities. For example, `EQ VAS`
resolved to `instrument:eq-vas`, and repeated uses of `EQ-5D-5L` resolved to one
instrument identity.

The three included papers took 212 to 262 seconds and 35 to 53 tool calls. Each
needed one or two correction responses. All corrections concerned SQL order,
relationships, controlled values, or semantic rules. There were no nested-JSON
shape failures. The two excluded papers each needed one tool call and finished in
15 to 17 seconds.

For the three included papers, Sol used 9,048 to 10,758 output tokens. The prior
Opus runs used 36,040 to 54,037 output tokens and took 353 to 547 seconds. Token
accounting differs between the two systems, but the large reduction in generated
output and elapsed time is clear.

The authoritative Sol run is `fulltext-sql-pilot-v1/sol-run-02`. It used the
final tool and runner code. `sol-run-01` was the pre-hardening check.

## Opus comparison

The same final interface was tested with `claude-opus-5` at high effort. All
five records saved without permission, tool, or schema failures. Opus matched
the prior Opus eligibility decisions, project links, and primary research
families exactly. It did not create Sol's questionable link between
`P9c72daab39ca` and project `2013320`.

Opus saved 262 typed items, compared with Sol's 237. It proposed 24 registry
changes, compared with Sol's 16. Some additional content was useful. Some was
too detailed for the graph. In the German methods paper, for example, Opus
added the Declaration of Helsinki as a protocol and two gaps about unreported
study details. Opus also requested some registry entries that already had a
usable canonical identity, such as the Canadian EQ-5D-5L value set.

The three included Opus runs took 138 to 239 seconds in total per paper. This
was about 19% less elapsed time in total than Sol. Opus produced 11,794 to
20,615 output tokens per included paper, about 70% more in total than Sol. The
authoritative Opus run is `fulltext-sql-pilot-v1/opus-run-01`. It used the
Claude subscription session; the runner removed `ANTHROPIC_API_KEY`.

Both models can use the SQL interface. Opus was better on the high-risk project
link, but Sol was more restrained and more disciplined with the registry. Use
Opus for the next small tranche because false project links are the more serious
error. Review item and registry growth before a large run.

## Decision

Use this interface for the next extraction tranche:

1. Give each agent the unchanged research instructions, the flat SQL schema, the
   controlled vocabulary, candidate projects, metadata, and paper text.
2. Give it only `sql`, `submit`, and `reject`.
3. Keep one isolated SQLite workspace per paper.
4. Let the same agent correct validation errors until the record saves.

The saved JSON record is an internal compatibility artifact for the current
ingestion pipeline. The agent does not create or inspect it.
