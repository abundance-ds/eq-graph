# Purpose and scope

Status: version 2, to be frozen before development.

## Purpose

Build a paper-first, EuroQol-specific ontology and extraction guide.
It must help researchers find precisely relevant studies and understand:

- what each study tried to do;
- whom and what it studied;
- which exact instruments, versions, languages and roles it used;
- which study-family-specific methods, administration modes and analytic methods it used;
- what it produced and found;
- how the authors interpreted the findings;
- what the authors say the work contributes, its reported or documented use, and which gaps the authors identify.

The ontology is not a general ontology of research.
The paper is the main record.
A paper can have paper-local components when samples, phases, tasks or analyses differ.

## Granularity

Practical does not mean coarse.
A fine distinction is useful when it changes retrieval, comparison or interpretation and can be extracted consistently.

Different study families can require different depth.
For example, a valuation paper can require its valuation task, protocol, experimental design, administration and statistical model.
A psychometric paper can require the property assessed, target instrument, comparison and analytic method.
A translation paper can require source and target language, version, adaptation process and testing.

These examples are not required fields.
Apply the same evidence-based depth to every study family in the assigned papers.

Do not create detail only because a paper reports it.
The experiment must discover which distinctions need consistent labels and which are clearer in concise narrative.

## Findings and impact boundaries

Capture the principal findings, author interpretation, important limitations, reported implications and stated future work.
Do not reproduce every estimate, coefficient, confidence interval or table.
Do not build a detailed claim-evidence-finding graph.

An author-reported implication or documented use is in scope.
Do not infer scientific, policy or social impact that the available evidence does not show.
Keep an author-stated research gap separate from a gap derived later across the full corpus.

## Data layers

Bibliographic and source metadata are deterministic when the source provides them.
This includes identifiers, title, authors, affiliations, dates, journal, licence, funding and references.
JATS XML is the canonical source for these facts.

Semantic study information remains in scope even when it resembles metadata.
This includes instrument version and language, study population, respondent and referent, administration mode, protocol, method, analysis, finding and interpretation.

Projects, researchers, citations and portfolio statistics belong to linked data layers.
Counts, trends and corpus gaps are derived after paper extraction.
