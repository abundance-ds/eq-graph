# EuroQol ontology development: version 3

Status: ontology design, holdout validation, JATS metadata audit, extraction,
strong source verification, project linkage, and graph loading for all 209
unique local JATS papers are complete. The audited result contains 207 included
studies, one excluded paper, and one correction notice. The next research input
is the 60 local PDF-only papers. Scale retrieval for the 3,148 retained records
remains behind the human-screening and identity gates.

## Purpose

- Develop an ontology for useful EuroQol research search and synthesis.
- Center the ontology on exact, queryable research facts.
- Examples include study type, instrument and version, valuation method, statistical model, population, administration mode, product, outcome, and finding.
- Use the 100 system competency questions as design requirements.
- Use prior standards only when they serve these requirements.

## Experiment

1. Select 100 papers with broad variation.
2. Use lower-cost agents to make one fixed, dense summary for each paper.
3. Create three controlled input packets.
   - 50 paper summaries per packet.
   - 25 papers shared by all packets.
   - 25 different papers per packet.
   - 50 questions per packet.
   - 25 questions shared by all packets.
   - 25 different questions per packet.
4. Give each packet to an independent Sol agent.
5. Each agent writes one Markdown ontology proposal.
6. Review the three proposals against the facts and all 100 questions.
7. Write one final proposal for human review.

## Controls

- Summary agents do not design the ontology.
- Ontology agents receive the same summary for each shared paper.
- Ontology agents do not receive earlier ontology files or other proposals.
- Prompts request useful semantic distinctions, not a fixed output schema.
- The final review must distinguish source data, extracted facts, controlled terms, and derived analytics.

## Main files

- `SUMMARY_TASK.md`: paper-summary task.
- `ONTOLOGY_TASK.md`: independent ontology-proposal task.
- `papers.tsv`: selected papers and packet assignments.
- `questions.tsv`: competency questions and packet assignments.
- `summaries/`: one fixed summary per paper.
- `packets/`: controlled lineage inputs.
- `proposals/`: three independent proposals.
- `review/`: comparison and final proposal.
- `validation/`: ten unseen-paper extraction records, source QA, question tests, and evidence-based revisions.
- `sqlite/`: deterministic JATS parser, relational pilot, and query tests.
- `broader/`: second non-overlapping 20-paper extraction, source QA, database,
  and query tests.
- `production-calibration/`: compact one-pass task, domain graph, flat index,
  production scripts, complete 209-paper JATS result, and production decision.
- `ONTOLOGY_V1.md`: current ontology for extraction and implementation.
- `SCALE_UP_DECISION.md`: evidence, risks, and the next human decision.
