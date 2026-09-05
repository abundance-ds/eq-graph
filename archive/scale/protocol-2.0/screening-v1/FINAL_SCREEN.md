# Scale title-and-abstract screen v1

The frozen screen is complete.

**Pause state:** no scale full text has been downloaded. Independent human screening
validation and the held identity queue remain before scale full-text retrieval.

- Input records: 18,348.
- Complete batches: 918/918.
- Retained: 3,148.
- Excluded: 15,200.
- Retention rate: 17.16%.
- Prompt SHA-256: `f08214947079d7ed660fc3ac69aafb3f53d96d1a80acfaf123c216fd695acefd`.
- Collector failures: 0.

Decision-code counts:

- R1: 1,226.
- R2: 1,914.
- RU: 8.
- E1: 2,286.
- E2: 1,548.
- E3: 621.
- E4: 9,810.
- E5: 935.

## Quality checks

- Prompt validation: 86 records, zero outcome errors against operator labels.
- Initial production check: 60 records, zero operator outcome disagreements.
- Blinded exclusion audit v1: 100 records, no confirmed false exclusion after six
  adjudications.
- Blinded exclusion audit v2: 100 different records, no confirmed false exclusion
  after two adjudications.
- Every record ID, decision code, and outcome-code pair validates.

The two exclusion audits used separate AI reviewers. They were not independent human
validation. An independent human sample check remains required before scale full-text
processing. No scale full texts were downloaded during screening.
