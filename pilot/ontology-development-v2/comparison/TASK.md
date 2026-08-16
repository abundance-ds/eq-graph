# Anonymous granularity comparison task

## Purpose

Compare three independent paper-first EuroQol ontology records.
The comparison must show which distinctions help researchers retrieve relevant papers and understand what the papers did and found.

Do not rank the candidates, select a winner, or propose a harmonized ontology.
Do not use majority rule, ontology size, element count, nesting depth, or one combined score.

## Required inputs

Read these files in full:

- `context/PURPOSE.md`
- `context/USER_QUESTIONS.md`
- `context/PROTOCOL.md`
- `context/PROBES.md`
- `candidates/candidate-1.md`
- `candidates/candidate-2.md`
- `candidates/candidate-3.md`
- `batches/batch-01.tsv` through `batches/batch-04.tsv`

The 40 manifest article files are available under `corpus/` for focused source checks.
Use them when an application is unclear, candidates disagree about source evidence, or a probe needs verification.
Do not use the Internet, external ontology guidance, another repository file, or a database-modeling skill.

## Comparison work

1. Compare the current ontology and extraction guidance in all three records.
2. Compare their applications to all 40 papers.
3. For each focused user question, state whether each candidate can answer it precisely, can answer it only with ambiguity, or cannot answer it from its proposed structure and narrative.
4. For each frozen probe:
   - trace the paper applications that the candidate retrieves or distinguishes;
   - explain which recorded distinctions make the result possible;
   - record missed, ambiguous, and false matches;
   - state the practical effect on the user's answer.
5. Identify semantically equivalent elements with different names.
6. Identify overlapping elements with different boundaries.
7. Identify broad labels that hide a material EuroQol difference.
8. Identify fine distinctions that add no clear retrieval or interpretation value, or that the applications use inconsistently.
9. Compare how each candidate represents:
   - paper-local components and their relations;
   - populations, respondents, referents, perspectives, and intended populations;
   - instrument family, version, variant, language, and evidence role;
   - administration mode and support;
   - study-family-specific tasks, protocols, designs, and analytic methods;
   - products, derivation, state, access, and intended use;
   - principal findings, interpretation, limitations, implications, documented use, and gaps;
   - evidence reuse, source conflicts, transfer limits, and corpus-derived gaps.
10. For material differences, cite paper evidence and give one concrete retrieval or interpretation consequence.
11. State which requirements a later harmonization must preserve, which apparent differences need only a terminology crosswalk, and which alternatives remain unresolved by the 40 papers.

Do not treat every detail in an application as a proposed controlled field.
Distinguish controlled terms, structured values, explicit relations, and concise narrative when that choice changes retrieval or interpretation.

## Output

Write one self-contained file at `output/anonymous-granularity-comparison.md`.
Use candidate numbers only.
Include:

- a short executive summary;
- a semantic crosswalk and boundary differences;
- focused-user-question findings;
- one section for the frozen probes;
- candidate-specific strengths and failure modes;
- requirements and unresolved alternatives for the later harmonization step;
- source checks and limitations of this comparison;
- a short run note that lists all inputs used and any mechanical issue.

Use Markdown tables only when they make the comparison easier to understand.
Keep evidence specific and the prose concise.
