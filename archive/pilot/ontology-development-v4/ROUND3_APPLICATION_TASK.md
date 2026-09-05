# Version 0.2 confirmation application

Apply ontology version 0.2 to every paper in `round-03.tsv`. Do not redesign
the ontology while you extract.

Read only:

- repository `AGENTS.md` files;
- `PROTOCOL.md`, `ONTOLOGY.md`, and `EXTRACTION_TASK.md`;
- `round-03.tsv` and its 15 article files.

Do not read earlier round applications, candidates, reviews, decisions, old
ontology versions, graph records, prior extractions, Neo4j guidance, or
another agent's output.

For each paper:

1. Verify its byte count and SHA-256.
2. Apply only current controlled keys and values.
3. Give one supported primary family or a gap.
4. Keep purpose, design, time, data origin, status, context, and function
   separate.
5. Apply the new task, factor, stakeholder, participatory-design, and product-
   state rules only when the source supports them.
6. Preserve exact instrument, method, protocol, model, factor, and concept
   labels.
7. Extract principal findings, interpretations, limitations, and products at
   the ontology's stated depth.
8. Put every proposed key or value in the gap log. Do not add it.

Write one concise Markdown file with:

- one application section per paper;
- one complete primary-family partition;
- all mapping and schema gaps;
- all source conflicts;
- proposals marked as proposals only;
- any risk to an existing rule;
- exact inputs and verification results.

Do not edit another file. Do not commit.
