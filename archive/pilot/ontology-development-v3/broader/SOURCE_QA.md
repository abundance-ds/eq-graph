# Broader-batch source QA

## Method

The primary reviewer extracted each record from the full article and then
checked its identity, study design, population, instrument roles, methods,
models, products, main findings, limitations, and funding against the cited
article sections. JATS was checked for metadata that the Markdown conversion
lost. This is a source check by the same reviewer, not an independent human
replication.

All article and JATS files match the frozen manifest. `validate_batch.py`
checks hashes, DOI values, prior-set overlap, record structure, and unresolved
placeholders.

## Results

| Record | Status | Material source issue or correction |
|---|---|---|
| B01 | Pass | Support is a travel grant; the paper reports no EQ instrument. |
| B02 | Pass with boundary note | EuroQol support is an author-level grant statement. The PedsQL study does not use an EQ instrument in its main analysis. |
| B03 | Pass | Proxy type, proxy perspective, seven-day recall, and response process remain separate. |
| B04 | Pass | Review-publication count, pooled evidence, and review findings remain separate. |
| B05 | Pass with boundary note | The article reports no EuroQol funding. Folder placement cannot prove a project link. |
| B06 | Pass | Video and face-to-face are administration channels for cTTO, not separate valuation methods. |
| B07 | Pass | Direct assessment time and the earlier health state that a participant recalled remain separate. |
| B08 | Pass | The work gives co-design input. It does not report an implemented routine workflow. |
| B09 | Pass with conflict | The abstract says differences were not significant but gives `p < .05`; the Results section reports a mother-father difference of `p = .023`. The conflict remains explicit. |
| B10 | Pass after metadata recovery | JATS reports EuroQol project `348-PHD`; the Markdown conversion omits this funding record. All study activities and products are planned. |
| B11 | Pass after metadata recovery | JATS reports EuroQol project `1787-RA`; the Markdown article does not show this project statement. EQ-5D is a prediction input, not a study outcome. |
| B12 | Pass | EuroQol support paid for data collection. EQ measures were administered but were not analyzed for the reported FACIT-COST results. |
| B13 | Pass | This is a conceptual methods paper with no participant sample or administered instrument. |
| B14 | Pass | OPUF task stages and their cognitive-validity problems remain distinct. |
| B15 | Pass with conversion note | Markdown repeats headings and paragraphs. JATS controls structure. CREATE is a reporting checklist, not a health instrument. |
| B16 | Pass with safety warning | The article is retracted. Local sources give no retraction notice, reason, or date. Its value set cannot be treated as current. |
| B17 | Pass | This is a correction notice that amends a parent publication. It is not a second study. |
| B18 | Pass with boundary note | The article and JATS report no EuroQol funding. EQ-5D was shown for qualitative content evaluation, not administered as an outcome. |
| B19 | Pass | Baseline and follow-up are report times. EQ VAS is used as an experience-based valuation, and values are not anchored at dead. |
| B20 | Pass | Historical EQ-5D data are displayed in a decision aid. EQ-5D was not administered during this usability study. |

## Decision

The 20 records are fit for ontology and query testing. The source checks expose
six required safeguards:

1. record publication lifecycle and publication-to-publication corrections;
2. keep funding evidence, support scope, and project linkage explicit;
3. control instrument-use roles instead of inferring them from instrument
   names;
4. separate completed, planned, prototype, implemented, and retracted states;
5. distinguish report time, recall reference time, and valuation duration;
6. keep source conflicts and conversion defects visible.
