# Production decision

## Decision

The one-pass pipeline is approved and complete for the existing JATS corpus.

- Use `gpt-5.6-luna` for the first paper pass.
- In one pass, decide corpus inclusion and conditionally extract the full
  research record.
- Parse publication metadata from JATS before the AI pass.
- Keep the AI output as readable Markdown with a flat typed search index.
- Validate, normalize, and load into SQLite with deterministic code.
- Use a stronger model only for a record that fails a check or a manual audit.
- Do not use separate routine agents for filtering, extraction, and
  normalization.
- Do not use Neo4j for this stage. The tested questions do not justify it.

## Evidence

| Test | Result |
| --- | --- |
| Source-checked calibration | 29/30 initial decisions; the one failure produced two clear boundary rules |
| Hard-case lower-cost test | 7/7 decisions and 12/12 critical safety checks |
| Unseen production sample | 50/50 completed; no run failure |
| Targeted repair | Three formatting failures repaired; 50/50 final records clean |
| Remaining JATS set | 129/129 final records clean; stratified source audit found no sampled fact correction |
| Final calibration rerun | 30/30 expected decisions; 30/30 clean; 22/22 safety checks |
| Complete local JATS result | 209 unique papers; 206 included studies; two exclusions; one correction notice |
| Production classifications | 182 direct EQ; 16 application-only; 11 adjacent measurement |
| SQLite load | 209 publications; 3,731 terms; 5,786 record-term links; 16,471 fact bullets |
| Database checks | 9/9 pass on the combined database |

The pilot also retrieved useful flexible concepts and exact domain terms. These
include states worse than dead, cTTO, DCE, EQ-5D-5L, instrument languages,
administration modes, statistical models, findings, and limitations.

## Known limits

- The typed index still has small label variations. Deterministic aliases fix
  clear cases and retain the source form.
- The first 50 records use several source-locator styles. Combined automatic
  recognition is 96.7%; later records reach at least 99.8% with one syntax.
- PDF input has not yet had the same production calibration.
- The run used local full texts only. It did not start retrieval for the 3,148
  retained abstract records.

## Next actions

1. Convert and test the 60 local PDF-only files.
2. Compare PDF text and extraction quality with the JATS baseline.
3. Use the same one-pass process if PDF quality is adequate.
4. Start lawful full-text retrieval for the retained abstract set after the PDF
   gate passes.

No further ontology decision is required before these actions. Stop for human
review only if the audit finds a repeated semantic failure, if a new study type
does not fit, or if the inclusion policy needs a change.
