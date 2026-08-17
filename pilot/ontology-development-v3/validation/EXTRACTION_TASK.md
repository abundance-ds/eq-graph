# Holdout extraction task

## Purpose

Test whether the proposed ontology produces useful, natural EuroQol research records on unseen papers.

This is an extraction test. Do not redesign the ontology.

## Allowed inputs

- `pilot/ontology-development-v3/review/FINAL_PROPOSAL.md`
- `pilot/ontology-development-v3/validation/EXTRACTION_TASK.md`
- your assigned rows in `pilot/ontology-development-v3/validation/holdout.tsv`
- the article files in those assigned rows
- repository `AGENTS.md`, if the environment supplies it

Do not read other ontology files, summaries, proposals, records, skills, standards, Git history, or external sources.

Before extraction, verify each article SHA-256 value and byte count against the manifest.

## Output

Write one Markdown file for each assigned paper under `pilot/ontology-development-v3/validation/records/`.

Use these headings:

1. Identity and study type
2. Population and samples
3. Concepts and themes
4. Instruments and administration
5. Methods, protocol, and task design
6. Analysis and statistical models
7. Products
8. Outcomes or measurement properties
9. Principal findings and interpretation
10. Limitations and source issues
11. High-value exact terms
12. Extraction fit

The headings guide extraction. Omit inapplicable details or state `not reported`. Do not invent facts.

## Rules

- Use exact source names for instruments, methods, protocols, models, products, outcomes, and properties.
- Also give a short preferred label when the source uses a long name or abbreviation.
- Extract source-grounded concepts and themes that help users connect this study to other EuroQol research. Keep these flexible. Do not use them instead of exact fields such as study type, population, instrument, method, model, product, or finding.
- Use one or more specific study-type labels. Do not use only `empirical study`, `research article`, or another generic label.
- Separate the target population, recruitment source, completed sample, analytic sample, and subgroups when the paper reports them.
- Separate instrument version, form, language, use role, respondent, perspective, interaction, channel, setting, recall period, and time point.
- Separate the research method from the statistical model.
- Treat `hybrid` as a model or analysis unless the source clearly gives it another role.
- Give each model its role, such as candidate, preferred, final, sensitivity, or comparator.
- Identify research products and their status. Do not confuse a planned product with a produced product.
- Extract the study-level findings needed to explain the study's contribution. Do not use a fixed finding count.
- Include the main results for the stated objectives, author-emphasized secondary, null, or conflicting results, material subgroup or comparison results, interpretations, and implications when relevant.
- For a valuation study, normally include the utility range or anchors, lowest and highest states when relevant, dimension order or relative importance, selected model and selection reason, and other notable findings that the authors emphasize.
- Add key aggregate estimates when they are important for interpretation.
- Do not extract participant-level values or reproduce complete result tables.
- Keep authors' interpretations separate from direct results.
- Capture reported limitations, data-quality caveats, scope limits, research gaps, and source conflicts. Do not invent limitations.
- Give a source section, table, figure, or paragraph locator for each substantive section.
- Preserve missing facts, caveats, and source conflicts.
- In `Extraction fit`, list facts that did not fit naturally, distinctions that were unclear, and fields that felt unnecessary.
- Use compact prose and bullets. Do not write JSON.

## Publication metadata

Official publication metadata is a required input to the final system. It must be parsed from JATS XML or another structured source before semantic AI extraction. This includes available identifiers, title, abstract, authors and order, ORCID, affiliations, correspondence, journal, publisher, article type, language, date roles, volume, issue, pages or article number, URLs, licence, keywords, funding fields, references, and source provenance.

Use supplied metadata as context. Do not ask the AI to reconstruct it from the article. Report a conflict or missing field when the semantic source disagrees with the structured record.

If a paper reports no EQ instrument, do not infer that EuroQol funded it from its folder, authors, or topic. The separate portfolio review must verify direct article evidence or an authoritative project-output record.

## Final check

- All ontology corner pieces that the paper reports are visible and searchable.
- A researcher can understand what the study did and found without reading the article.
- The record does not overstate the source.
- The file has no unsupported fact, placeholder, or unresolved drafting note.
- Report all files read outside the allowlist. Do not commit.
