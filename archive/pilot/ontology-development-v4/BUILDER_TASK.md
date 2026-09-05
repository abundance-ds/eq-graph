# Independent typed-ontology task

## Objective

Propose a typed EuroQol research ontology and apply it to all 15 supplied
papers. The output is Markdown. Do not design database tables, Cypher, or a
large JSON schema.

## Inputs

Read only these research inputs:

- `PROTOCOL.md`
- `round-01.tsv`
- `../ontology-development-v3/ONTOLOGY_V1.md`
- `../ontology-development-v3/questions.tsv`
- `../ontology-development-v3/aggregate-validity/SYNTHESIS.md`
- the 15 article files in the manifest

Repository-level `AGENTS.md` files are operational instructions. Do not read
Neo4j skills, other ontology proposals, graph records, prior extraction
records, or other research files.

## Required work

1. Define the smallest stable set of records and relationships needed to
   represent the papers.
2. For each important key, specify its owner, meaning, cardinality, value type,
   evidence requirement, and whether it is controlled.
3. Define the initial controlled values with short inclusion and exclusion
   rules. Keep distinct scientific dimensions on separate axes.
4. Treat instruments, methods, protocols, models, languages, places, people,
   and organizations as canonical registries with retained source labels.
5. Apply the proposal to every paper. Show the canonical research-purpose,
   design, data-origin, status, instrument-use, method-use, model-use, product,
   outcome, finding, limitation, and concept information that is present.
6. Record `UNMAPPED_VALUE`, `UNMODELED_ASPECT`, `UNCERTAIN_MAPPING`, and
   `NOT_REPORTED` cases. Do not force a mapping.
7. Use the user questions only as a coverage audit. Do not create a field for
   each question.

## Output

Write one concise Markdown file with:

- proposed records and relationships;
- key dictionary;
- controlled vocabulary;
- 15-paper application matrix;
- gap and ambiguity log;
- rejected distinctions;
- short assessment of stability and next-round risks;
- exact input and source-verification note.
