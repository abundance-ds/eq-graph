# Independent source audit

For each assigned paper, compare the extraction record with the full article
and deterministic metadata. The article is authoritative. Do not rewrite the
record.

Check:

- inclusion, EuroQol support, publication form, and relation;
- each author-defined Study, its primary family, purposes, status, parts, and
  design axes;
- populations, sample stages, data origin, exact instruments, methods,
  protocols, models, scoring, tasks, and administration;
- principal findings, selected aggregate values, interpretations,
  limitations, products, concepts, gaps, and source conflicts; and
- important facts that are missing, invented, assigned to the wrong role, or
  linked to the wrong Study or StudyPart; and
- each supplied deterministic validation error. Include an exact correction
  for every such error in the repair instructions.

Use `PASS` when no material change is needed. Use `MINOR` for a local change
that does not change the main scientific meaning. Use `MAJOR` for a wrong
filter decision, Study unit, primary family, main method or instrument role,
principal result, or material omission.

Give exact source locations. For each non-PASS record, give complete and direct
repair instructions. Mark a true ontology gap only when the supplied record
cannot represent an important source fact. Do not propose a new controlled
value for a one-paper distinction.
