# Independent production-record audit

Read the assigned article, its deterministic metadata, the extraction JSON,
`ONTOLOGY.md`, and `VOCABULARY.tsv`. Do not change the extraction record.

For each paper, check:

1. inclusion, EuroQol support scope, publication form, and any publication
   relation;
2. Study-versus-Publication unit, primary family, purpose order, and status;
3. study parts, design axes, populations, samples, and data origin;
4. exact instruments, methods, protocols, models, scoring products, their
   context and function, and material administration details;
5. principal findings, selected aggregate values, author interpretations,
   source-reported limitations, concepts, and source conflicts; and
6. important source facts that the record missed or facts that it invented.

Use `PASS` when no material change is needed, `MINOR` for a local correction
that does not change the main scientific meaning, and `MAJOR` for a wrong
filter decision, Study unit, family, major method or instrument role, result,
or material omission. A registry warning alone is not an extraction error if
the exact source label is correct and `registry_id` is null.

Write one compact table with: record ID, verdict, checked source locations,
material corrections, and missing important facts. Then give total counts and
list any recurring failure pattern. Do not propose a new ontology value unless
the supplied values force an invalid mapping.
