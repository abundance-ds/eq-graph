# Publication metadata policy

Official publication metadata is mandatory. It is not part of the semantic AI task.

## Source rule

- Keep raw JATS XML as the canonical structured source when it is available.
- Parse structured metadata before AI extraction.
- Preserve each value's source and all missing values.
- Give the agent the parsed metadata with section-aware article text.
- Ask the agent to extract only facts that need interpretation.
- Record a conflict when the article text and structured metadata disagree.

## Required fields when available

- DOI, PMID, PMCID, publisher identifier, and source-file identity;
- title, abstract, keywords, article type, and language;
- authors, author order, ORCID, roles, affiliations, and correspondence;
- journal, publisher, volume, issue, pages or article number;
- received, accepted, online, and issue dates with their date roles;
- landing page, full-text URL, licence, and open-access status;
- funders, award identifiers, funding statements, and support type;
- structured references and their identifiers;
- parser version, extraction date, source hash, and quality flags.

## Current evidence

The earlier JATS audit covered 220 XML files and 209 unique DOIs. Core identifiers, titles, journals, authors, licences, and references were present in all 220 files. The current Markdown conversion loses useful structure for funding, licence URLs, date roles, author roles, correspondence, affiliation identifiers, references, and section types.

Therefore, converting XML to Markdown is useful for readable semantic text, but Markdown must not replace the XML metadata layer. See [JATS XML audit](../../ontology-development/XML_AUDIT.md).
