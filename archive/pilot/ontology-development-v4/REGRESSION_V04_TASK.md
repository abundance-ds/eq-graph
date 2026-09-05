# Version 0.4 regression task

Apply the current `ONTOLOGY.md` independently to all 60 papers in
`round-01.tsv` through `round-04.tsv`.

Read only repository `AGENTS.md` files, `PROTOCOL.md`, `ONTOLOGY.md`,
`VOCABULARY.tsv`, `EXTRACTION_TASK.md`, the four manifests, and their 60
article files. Do not read prior applications, reviews, decisions,
regressions, old ontology versions, graph records, prior extractions, or
Neo4j guidance.

For each paper:

1. Verify its byte count and SHA-256.
2. Assign exactly one primary family or a gap.
3. Give the first-ranked purpose.
4. Apply the main part-level design and data axes.
5. Record source conflicts and each new gap without changing the ontology.

Return one concise Markdown file with a 60-row family table, complete
partition, material close calls, new gaps, stability verdict, and exact input
verification.

Do not redesign the ontology. Do not edit another file. Do not commit.
