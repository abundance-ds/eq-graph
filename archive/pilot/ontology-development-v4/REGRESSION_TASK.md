# Version 0.2 regression task

Apply the current `ONTOLOGY.md` independently to all 30 papers in
`round-01.tsv` and `round-02.tsv`.

Read only:

- repository `AGENTS.md` files;
- `PROTOCOL.md`, `ONTOLOGY.md`, and `EXTRACTION_TASK.md`;
- the two manifests and their 30 article files.

Do not read the round applications, candidates, reviews, decisions, old
ontology versions, graph records, prior extractions, Neo4j guidance, or other
research files.

For each paper:

1. Verify its byte count and SHA-256.
2. Assign exactly one primary research family or a gap.
3. Give the first-ranked research purpose.
4. Apply the design and data axes at the necessary part level.
5. Apply `TaskDesign`, `StudyFactor`, `StakeholderInvolvement`,
   `PARTICIPATORY_DESIGN`, and product-state `asserted_by` only when the source
   supports them.
6. Record a new gap instead of adding or forcing a key or value.

Return one concise Markdown file with:

- a 30-row primary-family table;
- a complete family partition;
- a short table for each new version-0.2 structure, with applicable papers and
  non-applicable boundary cases;
- material design, data, use-context, or source conflicts;
- all new gaps;
- a stability verdict;
- exact inputs and verification results.

Do not redesign the ontology. Do not edit another file. Do not commit.
