# Typed ontology application task

Apply the current ontology to every new paper in the supplied round manifest.
Do not redesign the ontology while you extract.

## Inputs

Read only:

- `PROTOCOL.md`
- `ONTOLOGY.md`
- `EXTRACTION_TASK.md`
- the supplied round manifest and article files
- `round-01/applications.md` and `round-01/gaps.md` for regression context

Repository-level `AGENTS.md` files are operational instructions. Do not read
Neo4j skills, older ontology versions, old proposals, graph records, prior
extraction records, or another agent's round output.

## Work

1. Verify each article hash and byte count.
2. Apply only existing controlled keys and values.
3. Preserve exact instrument, method, protocol, and model source labels.
4. Give each paper one supported primary research family or a gap.
5. Keep purpose, design, time, data origin, status, use context, and function
   separate.
6. Record principal outcomes, findings, interpretations, limitations,
   products, and open concepts at the ontology's stated depth.
7. Record every proposed key or value as a gap. Do not add it to the ontology.
8. Check whether any proposed change would invalidate a round-1 application.

## Output

Write one concise Markdown file with:

- one application section for each new paper;
- a primary-family partition table;
- all `UNMAPPED_VALUE`, `UNMODELED_ASPECT`, `UNCERTAIN_MAPPING`, and
  `NOT_REPORTED` cases that affect controlled or required information;
- source conflicts;
- proposed changes, each marked as a proposal only;
- round-1 regression risks;
- an exact input and verification note.
