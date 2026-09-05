# Version 0.3 regression task

Apply the current `ONTOLOGY.md` independently to all 45 papers in
`round-01.tsv`, `round-02.tsv`, and `round-03.tsv`.

Read only repository `AGENTS.md` files, `PROTOCOL.md`, `ONTOLOGY.md`,
`VOCABULARY.tsv`, `EXTRACTION_TASK.md`, the three manifests, and their 45
article files.
Do not read prior applications, reviews, decisions, regressions, old ontology
versions, graph records, prior extractions, or Neo4j guidance.

For each paper:

1. Verify its byte count and SHA-256.
2. Assign exactly one primary family or a gap.
3. Give the first-ranked purpose.
4. Apply part-level approach, allocation, time, comparison, and data axes.
5. Apply the version-0.3 additions only when the source supports them.
6. Record source conflicts and every new gap without changing the ontology.

Return one concise Markdown file with a 45-row family table, complete
partition, focused checks of the version-0.3 changes, material disagreements,
new gaps, stability verdict, and exact input verification.

Do not redesign the ontology. Do not edit another file. Do not commit.
