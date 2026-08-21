# Independent typed-ontology review

## Objective

Compare the two round-1 proposals. Recommend a single typed vocabulary, but do
not edit either proposal.

## Inputs

Read only:

- `PROTOCOL.md`
- `round-01.tsv`
- `BUILDER_TASK.md`
- `round-01/candidate-a.md`
- `round-01/candidate-b.md`
- `../ontology-development-v3/questions.tsv`
- `../ontology-development-v3/aggregate-validity/SYNTHESIS.md`
- article files from `round-01.tsv` when a disagreement needs source checking

Do not read other ontology proposals, graph records, prior extraction records,
or Neo4j guidance.

## Review questions

- Do the keys describe one clear scientific dimension each?
- Do controlled values have usable boundaries?
- Can an agent map normal paper evidence without inventing a value?
- Are registries, enums, open concepts, and free text used for the correct
  purposes?
- Do the applications expose forced mappings or silent information loss?
- Do categories support coherent aggregation without false exclusivity?
- Does either proposal add a key only to answer one user question?
- Which gaps require a new value, a new key, an existing value, or open text?

## Output

Write `round-01/review.md` with:

- agreements;
- material differences and their trade-offs;
- paper-backed decisions;
- vocabulary proposals marked `MERGE`, `ACCEPT`, `REJECT`, or `KEEP_OPEN`;
- recommended typed ontology;
- unresolved decisions;
- readiness decision for synthesis and round 2;
- exact input note.
