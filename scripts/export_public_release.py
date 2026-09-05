#!/usr/bin/env python3
"""Export the public serving database as an open-data release.

Inputs: the sanitized public SQLite database, the ontology, the controlled
vocabulary, and the data licence. Outputs, under ``--output``:

  eq-graph-<release>.sqlite          the public database, byte-identical
  eq-graph-<release>-tables.zip      one CSV per table, plus the codebook,
                                     vocabulary, ontology, and licence
  analysis/*.csv                     joined, analysis-ready files
  CODEBOOK.md                        table, column, and file reference
  SHA256SUMS                         hashes of every file above

Every output is deterministic for one input database: rows are ordered by
primary key, multi-value cells are sorted, floats that hold integers print as
integers, and zip entries carry a fixed timestamp.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import sqlite3
import zipfile
from collections import defaultdict
from pathlib import Path

MULTI = " | "
ZIP_TIME = (2026, 8, 29, 0, 0, 0)
CODED = re.compile(r"^[A-Za-z0-9_:\-./+]+$")

TABLE_NOTES = {
    "administration_targets": "Links an administration to its scientific use or task design.",
    "administrations": "How an instrument, method, protocol, software, or task was administered; open text.",
    "author_affiliations": "Affiliation strings as printed in the metadata, not normalised; some JATS sources prepend labels or institution identifiers.",
    "concepts": "Search keywords per study; not a substitute for the typed entities.",
    "dataset_uses": "One row per data source a study used.",
    "design_axes": "Design values per axis, study-level (empty `part_id`) or per part. Part-level values override study-level values.",
    "euroqol_memberships": "EuroQol Group members list as read on `observed_date`.",
    "extraction_gaps": "Facts the extraction could not represent: missing required fact, unmapped controlled value, unmodelled aspect, or uncertain mapping.",
    "finding_values": "Aggregate values per finding, as reported.",
    "findings": "Principal findings per study as short source-faithful statements; not every coefficient or table cell.",
    "instrument_uses": "Instrument uses with administration details. Subset of `scientific_uses` (`use_type` = Instrument).",
    "interpretations": "Author interpretations. `finding_ids_json` lists the findings each rests on.",
    "limitations": "Author-stated limitations per study.",
    "metadata": "Release metadata, key-value.",
    "method_uses": "Method uses. Subset of `scientific_uses` (`use_type` = Method).",
    "model_uses": "Uses of statistical, choice, mapping, scoring, decision, or text models. Subset of `scientific_uses` (`use_type` = Model).",
    "outcome_details": "Outcome family and label per outcome, with the instrument uses measuring it.",
    "outcomes": "Outcome labels per study. Findings reference outcomes by label.",
    "people": "Resolved people and group authors (`entity_kind` GROUP: consortium or group authorship).",
    "person_identifiers": "External identifiers per person. A consolidated profile can hold several identifiers of one scheme.",
    "person_names": "Name variants per person, with origin.",
    "populations": "Study populations. Counts are in `samples`.",
    "product_states": "Dated assertions about a research product on independent axes. Silence does not prove a negative state.",
    "product_uses": "Uses of a pre-existing product, such as a value set, as analysis object, comparator, or synthesis target. Subset of `scientific_uses` (`use_type` = Product).",
    "project_people": "Principal investigator per project, resolved to a person.",
    "project_publications": "Project-publication links confirmed from the full text. Possible links are excluded.",
    "projects": "EuroQol funded projects from the foundation's public table, downloaded 2026-07-28.",
    "protocols": "Uses of named protocols, for example EQ-VT. Subset of `scientific_uses` (`use_type` = Protocol).",
    "publication_authors": "Author list per publication in printed order, resolved to people.",
    "publication_citation_years": "Reserved for citation counts by year.",
    "publication_citations": "Citation count per publication from one dated OpenAlex snapshot.",
    "publications": "Included works: full text confirmed EuroQol support or direct project origin.",
    "registry_entities": "Reviewed canonical identities for instruments, methods, models, software, protocols, and products. Variants link to a parent.",
    "research_products": "Reusable outputs the study created: value sets, instrument versions, reference data, software, datasets.",
    "research_purposes": "Stated purposes per study; multi-valued.",
    "samples": "Source-reported counts per flow stage, from identification to analysis, including evidence review.",
    "scientific_uses": "Every use of a registry identity in a study; one row per use, context, and function.",
    "scoring_uses": "Application of an exact value set or scoring product to instrument responses.",
    "source_conflicts": "Contradictions inside one source, for example abstract against results; both statements kept, unrepaired.",
    "stakeholder_involvements": "Reported stakeholder activities and their influence on the study. Ordinary participation is not involvement.",
    "studies": "Studies per included publication. One publication reports two studies; all others report one.",
    "study_countries": "Countries recognised in the study's population and sample geography text.",
    "study_designs": "Distinct `axis:VALUE` design values across the study and its parts. `design_axes` keeps the part attribution.",
    "study_factors": "Analysed conditions, determinants, comparators, stratifiers, modifiers, or stages, with their levels.",
    "study_parts": "Separable parts of a study: sample, data source, method, or state. A simple study has none.",
    "study_types": "Primary research family and execution state. Exactly one row per study.",
    "task_designs": "Elicitation or interview task designs.",
}

# Column notes keyed by (table, column). "*" matches any table.
COLUMN_NOTES = {
    ("*", "study_id"): "Study identifier. Joins `studies.study_id`.",
    ("*", "publication_id"): "Publication identifier. Joins `publications.publication_id`.",
    ("*", "part_id"): "Study part. Empty when the row applies to the whole study. Joins `study_parts.part_id`.",
    ("*", "person_id"): "Person identifier. Joins `people.person_id`.",
    ("*", "project_id"): "EuroQol project id. Joins `projects.project_id`.",
    ("*", "registry_id"): "Reviewed identity. Joins `registry_entities.registry_id`.",
    ("*", "details_json"): "JSON object; keys are listed below the table.",
    ("*", "statement"): "Source-faithful text.",
    ("administration_targets", "administration_id"): "Joins `administrations.administration_id`.",
    ("administration_targets", "target_use_id"): "The scientific use or task design the administration applies to.",
    ("administrations", "respondent"): "Who answered.",
    ("administrations", "perspective"): "Whose health was reported or valued.",
    ("administrations", "completion"): "Self, interviewer, or assisted completion. Assisted self-completion remains self-report.",
    ("administrations", "assistance"): "Type of assistance, when reported.",
    ("administrations", "channel"): "Mode of delivery, for example paper, web, or telephone.",
    ("administrations", "setting"): "Where the administration took place.",
    ("administrations", "instrument_language"): "Language of the administered instrument.",
    ("administrations", "interview_language"): "Language of the interview, when different or reported.",
    ("administrations", "recall_period"): "Recall period as stated.",
    ("administrations", "time_point"): "Measurement occasion as stated.",
    ("author_affiliations", "affiliation"): "Affiliation string as printed.",
    ("concepts", "concept"): "Concept label.",
    ("dataset_uses", "dataset"): "Data source as named in the paper.",
    ("dataset_uses", "role"): "Data origin. Vocabulary key `data_origin`.",
    ("design_axes", "axis"): "Design axis. Each axis is a vocabulary key.",
    ("design_axes", "value"): "Controlled value for the axis. NOT_APPLICABLE and NOT_REPORTED are explicit states.",
    ("euroqol_memberships", "member_id"): "EuroQol member number from the profile URL.",
    ("euroqol_memberships", "affiliation"): "Affiliation as shown on the members list.",
    ("euroqol_memberships", "profile_url"): "Public EuroQol member profile.",
    ("euroqol_memberships", "observed_date"): "Date the members list was read.",
    ("extraction_gaps", "state"): "Gap state. Vocabulary key `gap_state`.",
    ("extraction_gaps", "affected_type"): "Entity type the gap concerns.",
    ("extraction_gaps", "affected_key"): "Field or value the gap concerns.",
    ("extraction_gaps", "importance"): "Why the gap matters, as judged during extraction.",
    ("extraction_gaps", "proposed_resolution"): "What would close the gap.",
    ("finding_values", "ordinal"): "Position of the value within the finding.",
    ("finding_values", "reported_value"): "Value as printed, including sign and decimals.",
    ("finding_values", "unit"): "Unit or scale of the value.",
    ("finding_values", "denominator"): "Denominator or base as stated.",
    ("finding_values", "time"): "Time point of the value.",
    ("finding_values", "subgroup"): "Subgroup the value refers to.",
    ("finding_values", "comparator"): "Comparator for a difference or ratio.",
    ("finding_values", "direction"): "Direction of effect as stated.",
    ("finding_values", "uncertainty"): "Confidence interval, standard error, or p-value as stated.",
    ("findings", "outcome"): "Outcome label the finding is about. Joins `outcomes.outcome` within the study.",
    ("findings", "statement"): "Short source-faithful statement of the finding.",
    ("instrument_uses", "instrument_use_id"): "Same value as `scientific_uses.use_id`.",
    ("instrument_uses", "instrument"): "Canonical instrument label.",
    ("instrument_uses", "role"): "Instrument function. Vocabulary key `instrument_function`.",
    ("instrument_uses", "language"): "Instrument language as administered.",
    ("instrument_uses", "version"): "Instrument version or level as reported.",
    ("instrument_uses", "administration"): "Completion mode from the linked administration.",
    ("instrument_uses", "respondent"): "Respondent from the linked administration.",
    ("instrument_uses", "perspective"): "Perspective from the linked administration.",
    ("instrument_uses", "recall_period"): "Recall period from the linked administration.",
    ("instrument_uses", "channel"): "Channel from the linked administration.",
    ("instrument_uses", "setting"): "Setting from the linked administration.",
    ("interpretations", "finding_ids_json"): "JSON list of `findings.finding_id`.",
    ("limitations", "impact"): "Reserved.",
    ("limitations", "scope"): "Reserved.",
    ("metadata", "key"): "Metadata key.",
    ("metadata", "value"): "Metadata value.",
    ("method_uses", "method"): "Canonical method label.",
    ("method_uses", "role"): "Method function. Vocabulary key `method_function`.",
    ("method_uses", "purpose"): "Reserved.",
    ("method_uses", "protocol"): "Reserved.",
    ("method_uses", "administration"): "Free-text administration note when the source reports one.",
    ("method_uses", "software"): "Reserved.",
    ("model_uses", "model"): "Canonical model label.",
    ("model_uses", "role"): "Model function. Vocabulary key `model_function`.",
    ("model_uses", "outcome"): "Analytic role of the model in the reported results. Vocabulary key `analytic_role`.",
    ("model_uses", "inputs"): "Reserved.",
    ("model_uses", "software"): "Reserved.",
    ("outcome_details", "outcome_id"): "Joins `outcomes.outcome_id`.",
    ("outcome_details", "family"): "Outcome family. Vocabulary key `outcome_family`.",
    ("outcome_details", "label"): "Outcome label, same as `outcomes.outcome`.",
    ("outcome_details", "instrument_use_ids_json"): "JSON list of `scientific_uses.use_id` for the instruments measuring the outcome.",
    ("outcomes", "outcome"): "Outcome label.",
    ("people", "person_id"): "Identifier. The prefix shows the origin: `person:openalex:`, `person:eqmember:`, `person:leader:`, `person:orcid:`, `person:author:`, `group:author:`.",
    ("people", "display_name"): "Preferred display name.",
    ("people", "family_name"): "Family name.",
    ("people", "given_names"): "Given names.",
    ("people", "orcid"): "ORCID iD when known.",
    ("people", "openalex_id"): "OpenAlex author id when known.",
    ("people", "entity_kind"): "PERSON or GROUP.",
    ("people", "identity_status"): "How the identity was established. PROFILE_ACCEPTED: reviewed external profile accepted. PROFILE_NOT_ACCEPTED_FOR_DISCOVERY: candidate profile found, not accepted. NO_EXTERNAL_PROFILE: no external profile. NEW_EXTERNAL_IDENTITY: identity created from an external identifier. EXACT_CANONICAL_NAME: matched to a known person on the exact canonical name. PUBLICATION_LOCAL: known from one publication only, not resolved.",
    ("person_identifiers", "scheme"): "ORCID or OPENALEX.",
    ("person_identifiers", "value"): "Identifier value.",
    ("person_names", "name"): "Name variant.",
    ("person_names", "name_type"): "Origin of the variant.",
    ("populations", "population"): "Population description.",
    ("populations", "role"): "Role of the population in the study, as reported.",
    ("populations", "geography"): "Geography as reported.",
    ("populations", "size"): "Reserved. Counts are in `samples`.",
    ("product_states", "product_id"): "Joins `research_products.product_id`.",
    ("product_states", "axis"): "DEVELOPMENT, VALIDATION, DEPLOYMENT, or APPROVAL.",
    ("product_states", "exact_state"): "State as asserted by the source.",
    ("product_states", "assertion_date"): "Date or year of the assertion.",
    ("product_states", "asserted_by"): "Who made the assertion.",
    ("product_uses", "product_use_id"): "Same value as `scientific_uses.use_id`.",
    ("product_uses", "product"): "Canonical product label.",
    ("product_uses", "context"): "Vocabulary key `use_context`.",
    ("product_uses", "function"): "Vocabulary key `product_function`.",
    ("product_uses", "analytic_role"): "Reserved.",
    ("project_people", "role"): "PRINCIPAL_INVESTIGATOR for every row.",
    ("project_publications", "project_output"): "YES: the publication is a direct output of the project.",
    ("project_publications", "support_target"): "What the support applied to.",
    ("project_publications", "support_scope"): "Reserved. The publication-level scope is in `publications.support_scope`.",
    ("projects", "project_id"): "EuroQol project id. Two schemes: sequence number plus grant-type suffix, for example 1489-RA, or a year-prefixed number, for example 20190670.",
    ("projects", "title"): "Project title as published.",
    ("projects", "abstract"): "Project abstract as published by EuroQol. Empty for 20 projects.",
    ("projects", "principal_investigator"): "Principal investigator or applicant name as published, unparsed.",
    ("projects", "working_group"): "Working group or groups as published, comma-joined. `Dissemination, OA fee` is one group.",
    ("projects", "start_year"): "Start year as published.",
    ("projects", "end_year"): "End year as published. Empty for many completed projects.",
    ("projects", "status"): "Status as published.",
    ("projects", "approved_budget_eur"): "Approved budget in euros as published. Zero for 21 projects.",
    ("protocols", "protocol_id"): "Same value as `scientific_uses.use_id`.",
    ("protocols", "protocol"): "Canonical protocol label.",
    ("publication_authors", "author_name"): "Name as printed on the publication.",
    ("publication_authors", "author_order"): "Position in the author list, starting at 1.",
    ("publication_authors", "corresponding"): "1 when marked as corresponding author.",
    ("publication_authors", "orcid"): "ORCID printed on the publication.",
    ("publication_authors", "resolution_method"): "How the author was matched to a person.",
    ("publication_authors", "resolution_status"): "ACCEPTED or UNRESOLVED. Use ACCEPTED rows for person-level analysis.",
    ("publication_citations", "source"): "Citation source.",
    ("publication_citations", "source_work_id"): "OpenAlex work id.",
    ("publication_citations", "cited_by_count"): "Citations at retrieval. Zero for NOT_FOUND rows is not evidence of zero citations.",
    ("publication_citations", "retrieved_at"): "Snapshot date.",
    ("publication_citations", "source_updated_at"): "Reserved.",
    ("publication_citations", "match_status"): "EXACT when OpenAlex matched the publication; NOT_FOUND otherwise.",
    ("publications", "publication_id"): "`doi:<DOI>` when a DOI exists; otherwise an opaque key.",
    ("publications", "title"): "Title from the structured metadata.",
    ("publications", "doi"): "DOI without prefix.",
    ("publications", "pmid"): "PubMed id.",
    ("publications", "pmcid"): "PubMed Central id.",
    ("publications", "publication_year"): "Year of publication.",
    ("publications", "publication_date"): "Date as available; often only the year.",
    ("publications", "journal"): "Journal or venue.",
    ("publications", "publisher"): "Publisher when the metadata names one.",
    ("publications", "volume"): "Volume.",
    ("publications", "issue"): "Issue.",
    ("publications", "article_number"): "Article number or page range.",
    ("publications", "article_type"): "Article type as given by the source.",
    ("publications", "language"): "Language code when given.",
    ("publications", "keywords"): "Author keywords, joined with ` | `.",
    ("publications", "funding_statement"): "Funding statement or funder identifiers from the structured metadata.",
    ("publications", "abstract"): "Abstract from Crossref, Europe PMC, or OpenAlex. Third-party text.",
    ("publications", "canonical_url"): "DOI resolver URL or landing page.",
    ("publications", "licence_url"): "Licence URL from the metadata when given.",
    ("publications", "open_access"): "1 when an open-access copy was recorded during retrieval.",
    ("publications", "assessment_disposition"): "include-study for every row. Excluded works are not in the public database.",
    ("publications", "euroqol_connection"): "direct_eq for every row.",
    ("publications", "euroqol_support"): "explicit: the full text states EuroQol support. none-stated: no support statement; the work entered through a confirmed project link.",
    ("publications", "support_scope"): "What the stated support covered, as reported.",
    ("publications", "full_text_format"): "Format of the assessed full text.",
    ("registry_entities", "entity_type"): "Instrument, Method, Model, Software, Protocol, or Product.",
    ("registry_entities", "canonical_label"): "Reviewed canonical label.",
    ("registry_entities", "parent_registry_id"): "Parent identity for a variant.",
    ("registry_entities", "applies_to_registry_id"): "Identity the entity applies to, for example the instrument a value set scores.",
    ("registry_entities", "variant_kind"): "Kind of variant relative to the parent.",
    ("registry_entities", "language_code"): "Language edition code.",
    ("registry_entities", "jurisdiction"): "Country or region code for a jurisdiction-specific identity.",
    ("registry_entities", "version"): "Version label.",
    ("registry_entities", "respondent_form"): "Respondent form for a respondent-specific identity.",
    ("registry_entities", "source_identifier"): "DOI or other identifier that defines the identity, when known.",
    ("registry_entities", "scope"): "GLOBAL for every row.",
    ("research_products", "product"): "Product label.",
    ("research_products", "product_type"): "Vocabulary key `product_type`.",
    ("research_products", "status"): "Summary of the latest state assertion as `AXIS:state`. `product_states` holds all assertions.",
    ("research_purposes", "purpose"): "Vocabulary key `research_purpose`.",
    ("samples", "label"): "Sample description.",
    ("samples", "sample_size"): "Count as an integer when the source gives one.",
    ("samples", "role"): "Flow stage. Vocabulary key `sample_stage`.",
    ("samples", "geography"): "Geography as reported.",
    ("scientific_uses", "use_id"): "Use identifier. Type-specific tables reuse this value.",
    ("scientific_uses", "use_type"): "Instrument, Method, Model, Software, Protocol, or Product.",
    ("scientific_uses", "source_label"): "Label as printed in the paper.",
    ("scientific_uses", "canonical_label"): "Reviewed canonical label from the registry.",
    ("scientific_uses", "context"): "Vocabulary key `use_context`. Filter on this before counting uses.",
    ("scientific_uses", "function"): "Type-specific function. Vocabulary keys `instrument_function`, `method_function`, `model_function`, `software_function`, `protocol_function`, `product_function`.",
    ("scientific_uses", "analytic_role"): "Models only. Vocabulary key `analytic_role`.",
    ("scoring_uses", "source_label"): "Value set or scoring product as named in the paper.",
    ("scoring_uses", "context"): "Vocabulary key `use_context`.",
    ("scoring_uses", "instrument_use_id"): "The scored instrument use. Joins `scientific_uses.use_id`.",
    ("scoring_uses", "product_id"): "Set when the study applied its own product. Joins `research_products.product_id`.",
    ("source_conflicts", "statement"): "The conflicting statements, separated by ` | `.",
    ("stakeholder_involvements", "stakeholder_group"): "Who was involved.",
    ("stakeholder_involvements", "activity"): "What they did.",
    ("stakeholder_involvements", "stage"): "Study stage of the activity.",
    ("stakeholder_involvements", "role"): "Their role.",
    ("stakeholder_involvements", "influence"): "Reported influence on the study.",
    ("studies", "label"): "Study label.",
    ("studies", "study_ordinal"): "Order of the study within its publication.",
    ("studies", "execution_status"): "Vocabulary key `execution_state`.",
    ("studies", "source_status"): "Vocabulary key `result_state`.",
    ("study_countries", "country"): "Country name.",
    ("study_designs", "study_design"): "`axis:VALUE`.",
    ("study_factors", "label"): "Factor name as reported.",
    ("study_factors", "role"): "Vocabulary key `factor_role`.",
    ("study_factors", "levels_json"): "JSON list of levels.",
    ("study_parts", "label"): "Part label.",
    ("study_types", "study_type"): "Primary research family. Vocabulary key `primary_research_family`.",
    ("study_types", "status"): "Execution state, same as `studies.execution_status`.",
    ("task_designs", "label"): "Task label.",
    ("task_designs", "duration"): "Task duration or time horizon.",
    ("task_designs", "alternatives"): "Alternatives presented.",
    ("task_designs", "task_count"): "Number of tasks per respondent, as stated.",
    ("task_designs", "block"): "Blocking of tasks.",
    ("task_designs", "task_order"): "Order of tasks.",
    ("task_designs", "randomization_unit"): "What was randomised within the task.",
    ("task_designs", "stopping_rule"): "Stopping or indifference rule.",
    ("task_designs", "profiles_json"): "JSON list of health-state profiles.",
    ("task_designs", "attributes_json"): "JSON list of attributes.",
    ("task_designs", "levels_json"): "JSON list of levels.",
    ("task_designs", "targets_json"): "JSON list of the use ids the task targets.",
}

ANALYSIS_NOTES = {
    "projects": (
        "One row per funded project with its accepted publications.",
        {
            "n_publications": "Accepted project-publication links.",
            "publication_ids": "Linked `publication_id` values.",
            "publication_dois": "Linked DOIs.",
        },
    ),
    "publications": (
        "One row per publication: project links, study classification, countries, instruments, counts, citations.",
        {
            "project_ids": "Accepted project links.",
            "n_projects": "Number of accepted project links.",
            "study_ids": "Studies reported by the publication.",
            "primary_research_families": "Primary research family of each study.",
            "countries": "Countries from `study_countries`.",
            "eq_instruments": "EQ instruments used or examined: Instrument uses in context DIRECT_CURRENT_ACTIVITY or CURRENT_STUDY_OBJECT whose registry identity, or an ancestor, is under `instrument:eq-`.",
            "instruments": "All instruments used or examined, same context filter.",
            "n_authors": "Authorships, resolved or not.",
            "n_findings": "Findings.",
            "n_limitations": "Limitations.",
            "n_products": "Research products created.",
            "cited_by_count": "OpenAlex citations at the snapshot date.",
            "citation_match_status": "EXACT or NOT_FOUND.",
            "citation_retrieved_at": "Snapshot date.",
        },
    ),
    "project_publications": (
        "One row per accepted project-publication link, with descriptors of both.",
        {
            "project_title": "Project title.",
            "principal_investigator": "Project principal investigator as published.",
            "working_group": "Project working group.",
            "start_year": "Project start year.",
            "publication_title": "Publication title.",
        },
    ),
    "studies": (
        "One row per study: classification, purposes, countries, study-level design values, item counts.",
        {
            "primary_research_family": "Vocabulary key `primary_research_family`.",
            "purposes": "Vocabulary key `research_purpose`.",
            "countries": "Countries from `study_countries`.",
            "component_approach": "Study-level design value; empty when only parts carry the axis.",
            "temporal_structure": "Study-level design value.",
            "comparison_structure": "Study-level design value.",
            "allocation_structure": "Study-level design value.",
            "synthesis_design": "Study-level design value.",
            "mixed_method_integration": "Study-level design value.",
            "project_ids": "Accepted project links of the publication.",
            "n_parts": "Study parts.",
            "n_instrument_uses": "Instrument uses in any context.",
            "n_method_uses": "Method uses in any context.",
            "n_findings": "Findings.",
            "n_limitations": "Limitations.",
            "n_products": "Research products created.",
        },
    ),
    "scientific_uses": (
        "One row per scientific use, with the registry identity and its parent.",
        {
            "parent_registry_id": "Parent identity for a variant.",
            "parent_label": "Canonical label of the parent identity.",
            "variant_kind": "Kind of variant relative to the parent.",
            "language_code": "Language edition code of the identity.",
            "jurisdiction": "Jurisdiction code of the identity.",
            "version": "Version label of the identity.",
            "respondent_form": "Respondent form of the identity.",
        },
    ),
    "findings": (
        "One row per finding: publication, study family, outcome family, referenced items.",
        {
            "primary_research_family": "Primary research family of the study.",
            "outcome_family": "Vocabulary key `outcome_family`, joined on the outcome label.",
            "about_ids": "Item ids the finding refers to, from `details_json.about`.",
            "n_values": "Rows in `finding_values`.",
        },
    ),
    "finding_values": (
        "One row per reported value with its finding and publication.",
        {"outcome": "Outcome label of the finding."},
    ),
    "limitations": (
        "One row per limitation with publication and study family.",
        {
            "primary_research_family": "Primary research family of the study.",
            "about_ids": "Item ids the limitation concerns, from `details_json.about`.",
        },
    ),
    "research_products": (
        "One row per created product, with state assertions by axis.",
        {
            "development_state": "DEVELOPMENT assertions.",
            "validation_state": "VALIDATION assertions.",
            "deployment_state": "DEPLOYMENT assertions.",
            "approval_state": "APPROVAL assertions.",
            "n_scoring_uses": "Scoring uses that applied this product.",
        },
    ),
    "authorships": (
        "One row per authorship: resolved person, identifiers, affiliations.",
        {
            "display_name": "Resolved person display name.",
            "orcid": "Person ORCID, or the ORCID printed on the publication.",
            "openalex_id": "Person OpenAlex author id.",
            "entity_kind": "PERSON or GROUP.",
            "affiliations": "Affiliation strings for this author on this publication.",
        },
    ),
    "people": (
        "One row per resolved person: membership, project, and publication counts.",
        {
            "euroqol_member": "1 when observed on the EuroQol members list.",
            "n_projects_as_pi": "Projects where the person is principal investigator.",
            "n_publications": "Accepted authorships.",
            "first_publication_year": "Earliest accepted authorship year.",
            "last_publication_year": "Latest accepted authorship year.",
        },
    ),
    "coauthor_edges": (
        "Undirected co-authorship edges between resolved people, weighted by shared publications (the application's `coauthor_edges` view).",
        {
            "source_id": "Person id of one author.",
            "source": "Display name.",
            "target_id": "Person id of the other author.",
            "target": "Display name.",
            "weight": "Shared publications with accepted authorships.",
        },
    ),
}

COAUTHOR_SQL = """
SELECT a.person_id AS source_id,
       source_person.display_name AS source,
       b.person_id AS target_id,
       target_person.display_name AS target,
       COUNT(DISTINCT a.publication_id) AS weight
FROM publication_authors a
JOIN publication_authors b
  ON b.publication_id = a.publication_id AND b.person_id > a.person_id
JOIN people source_person ON source_person.person_id = a.person_id
JOIN people target_person ON target_person.person_id = b.person_id
WHERE a.resolution_status = 'ACCEPTED'
  AND b.resolution_status = 'ACCEPTED'
  AND source_person.entity_kind = 'PERSON'
  AND target_person.entity_kind = 'PERSON'
GROUP BY a.person_id, source_person.display_name, b.person_id, target_person.display_name
ORDER BY a.person_id, b.person_id
"""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cell(value):
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def csv_text(header: list[str], rows) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(header)
    for row in rows:
        writer.writerow([cell(value) for value in row])
    return buffer.getvalue()


def table_names(db: sqlite3.Connection) -> list[str]:
    return [
        row[0]
        for row in db.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        )
    ]


def columns(db: sqlite3.Connection, table: str) -> list[tuple[str, str, int]]:
    return [(row[1], row[2] or "", row[5]) for row in db.execute(f"PRAGMA table_info({table})")]


def order_clause(db: sqlite3.Connection, table: str) -> str:
    cols = columns(db, table)
    keys = [name for name, _, pk in sorted((c for c in cols if c[2]), key=lambda c: c[2])]
    if not keys:
        keys = [name for name, _, _ in cols]
    return ", ".join(keys)


def multi(db: sqlite3.Connection, sql: str) -> dict[str, str]:
    values: dict[str, set] = defaultdict(set)
    for key, value in db.execute(sql):
        if value is not None and value != "":
            values[key].add(str(value))
    return {key: MULTI.join(sorted(items)) for key, items in values.items()}


def counts(db: sqlite3.Connection, sql: str) -> dict[str, int]:
    return {key: int(value) for key, value in db.execute(sql)}


def json_about(text: str) -> str:
    try:
        items = json.loads(text or "{}").get("about") or []
    except json.JSONDecodeError:
        return ""
    return MULTI.join(sorted(str(item) for item in items))


def eq_registry_ids(db: sqlite3.Connection) -> set[str]:
    parents = dict(db.execute("SELECT registry_id, parent_registry_id FROM registry_entities"))
    result = set()
    for registry_id in parents:
        seen = set()
        current = registry_id
        while current and current not in seen:
            if current.startswith("instrument:eq-"):
                result.add(registry_id)
                break
            seen.add(current)
            current = parents.get(current)
    return result


def build_analysis(db: sqlite3.Connection) -> dict[str, tuple[list[str], list[list]]]:
    files: dict[str, tuple[list[str], list[list]]] = {}

    pub_projects = multi(db, "SELECT publication_id, project_id FROM project_publications")
    pub_dois = multi(db, "SELECT l.project_id, p.doi FROM project_publications l JOIN publications p USING (publication_id)")
    project_pubs = multi(db, "SELECT project_id, publication_id FROM project_publications")
    project_n = counts(db, "SELECT project_id, COUNT(*) FROM project_publications GROUP BY 1")

    rows = []
    for row in db.execute(
        "SELECT project_id, title, principal_investigator, working_group, start_year, end_year, status, "
        "approved_budget_eur, abstract FROM projects ORDER BY project_id"
    ):
        pid = row[0]
        rows.append(list(row[:8]) + [project_n.get(pid, 0), project_pubs.get(pid, ""), pub_dois.get(pid, ""), row[8]])
    files["projects"] = (
        ["project_id", "title", "principal_investigator", "working_group", "start_year", "end_year", "status",
         "approved_budget_eur", "n_publications", "publication_ids", "publication_dois", "abstract"],
        rows,
    )

    eq_ids = eq_registry_ids(db)
    use_filter = "u.use_type = 'Instrument' AND u.context IN ('DIRECT_CURRENT_ACTIVITY', 'CURRENT_STUDY_OBJECT')"
    pub_instruments: dict[str, set] = defaultdict(set)
    pub_eq: dict[str, set] = defaultdict(set)
    for publication_id, label, registry_id in db.execute(
        f"SELECT s.publication_id, u.canonical_label, u.registry_id FROM scientific_uses u "
        f"JOIN studies s USING (study_id) WHERE {use_filter}"
    ):
        pub_instruments[publication_id].add(label)
        if registry_id in eq_ids:
            pub_eq[publication_id].add(label)
    pub_studies = multi(db, "SELECT publication_id, study_id FROM studies")
    pub_families = multi(db, "SELECT s.publication_id, t.study_type FROM studies s JOIN study_types t USING (study_id)")
    pub_countries = multi(db, "SELECT s.publication_id, c.country FROM studies s JOIN study_countries c USING (study_id)")
    pub_authors = counts(db, "SELECT publication_id, COUNT(*) FROM publication_authors GROUP BY 1")
    pub_findings = counts(db, "SELECT publication_id, COUNT(*) FROM findings GROUP BY 1")
    pub_limitations = counts(db, "SELECT publication_id, COUNT(*) FROM limitations GROUP BY 1")
    pub_products = counts(db, "SELECT s.publication_id, COUNT(*) FROM research_products r JOIN studies s USING (study_id) GROUP BY 1")

    rows = []
    for row in db.execute(
        "SELECT p.publication_id, p.doi, p.pmid, p.pmcid, p.title, p.publication_year, p.publication_date, p.journal, "
        "p.publisher, p.article_type, p.open_access, p.licence_url, p.canonical_url, p.full_text_format, "
        "p.euroqol_support, p.support_scope, c.cited_by_count, c.match_status, c.retrieved_at, p.keywords, "
        "p.funding_statement, p.abstract FROM publications p "
        "LEFT JOIN publication_citations c ON c.publication_id = p.publication_id ORDER BY p.publication_id"
    ):
        pid = row[0]
        projects = pub_projects.get(pid, "")
        rows.append(
            list(row[:16])
            + [
                projects,
                len(projects.split(MULTI)) if projects else 0,
                pub_studies.get(pid, ""),
                pub_families.get(pid, ""),
                pub_countries.get(pid, ""),
                MULTI.join(sorted(pub_eq.get(pid, ()))),
                MULTI.join(sorted(pub_instruments.get(pid, ()))),
                pub_authors.get(pid, 0),
                pub_findings.get(pid, 0),
                pub_limitations.get(pid, 0),
                pub_products.get(pid, 0),
            ]
            + list(row[16:])
        )
    files["publications"] = (
        ["publication_id", "doi", "pmid", "pmcid", "title", "publication_year", "publication_date", "journal",
         "publisher", "article_type", "open_access", "licence_url", "canonical_url", "full_text_format",
         "euroqol_support", "support_scope", "project_ids", "n_projects", "study_ids", "primary_research_families",
         "countries", "eq_instruments", "instruments", "n_authors", "n_findings", "n_limitations", "n_products",
         "cited_by_count", "citation_match_status", "citation_retrieved_at", "keywords", "funding_statement",
         "abstract"],
        rows,
    )

    files["project_publications"] = (
        ["project_id", "project_title", "principal_investigator", "working_group", "start_year", "publication_id",
         "doi", "publication_title", "publication_year", "journal"],
        [list(row) for row in db.execute(
            "SELECT l.project_id, pr.title, pr.principal_investigator, pr.working_group, pr.start_year, "
            "l.publication_id, p.doi, p.title, p.publication_year, p.journal FROM project_publications l "
            "JOIN projects pr USING (project_id) JOIN publications p USING (publication_id) "
            "ORDER BY l.project_id, l.publication_id"
        )],
    )

    study_purposes = multi(db, "SELECT study_id, purpose FROM research_purposes")
    study_countries = multi(db, "SELECT study_id, country FROM study_countries")
    axes = ["component_approach", "temporal_structure", "comparison_structure", "allocation_structure",
            "synthesis_design", "mixed_method_integration"]
    study_axes = {
        axis: multi(db, f"SELECT study_id, value FROM design_axes WHERE part_id IS NULL AND axis = '{axis}'")
        for axis in axes
    }
    study_parts = counts(db, "SELECT study_id, COUNT(*) FROM study_parts GROUP BY 1")
    study_instruments = counts(db, "SELECT study_id, COUNT(*) FROM scientific_uses WHERE use_type = 'Instrument' GROUP BY 1")
    study_methods = counts(db, "SELECT study_id, COUNT(*) FROM scientific_uses WHERE use_type = 'Method' GROUP BY 1")
    study_findings = counts(db, "SELECT study_id, COUNT(*) FROM findings GROUP BY 1")
    study_limitations = counts(db, "SELECT study_id, COUNT(*) FROM limitations GROUP BY 1")
    study_products = counts(db, "SELECT study_id, COUNT(*) FROM research_products GROUP BY 1")

    rows = []
    for row in db.execute(
        "SELECT s.study_id, s.publication_id, p.doi, p.publication_year, s.study_ordinal, s.label, t.study_type, "
        "s.execution_status, s.source_status FROM studies s JOIN publications p USING (publication_id) "
        "LEFT JOIN study_types t USING (study_id) ORDER BY s.study_id"
    ):
        sid, pid = row[0], row[1]
        rows.append(
            list(row)
            + [study_purposes.get(sid, ""), study_countries.get(sid, "")]
            + [study_axes[axis].get(sid, "") for axis in axes]
            + [pub_projects.get(pid, ""), study_parts.get(sid, 0), study_instruments.get(sid, 0),
               study_methods.get(sid, 0), study_findings.get(sid, 0), study_limitations.get(sid, 0),
               study_products.get(sid, 0)]
        )
    files["studies"] = (
        ["study_id", "publication_id", "doi", "publication_year", "study_ordinal", "label", "primary_research_family",
         "execution_status", "source_status", "purposes", "countries"] + axes
        + ["project_ids", "n_parts", "n_instrument_uses", "n_method_uses", "n_findings", "n_limitations",
           "n_products"],
        rows,
    )

    files["scientific_uses"] = (
        ["use_id", "study_id", "publication_id", "doi", "publication_year", "part_id", "use_type", "source_label",
         "canonical_label", "registry_id", "parent_registry_id", "parent_label", "variant_kind", "language_code",
         "jurisdiction", "version", "respondent_form", "context", "function", "analytic_role"],
        [list(row) for row in db.execute(
            "SELECT u.use_id, u.study_id, s.publication_id, p.doi, p.publication_year, u.part_id, u.use_type, "
            "u.source_label, u.canonical_label, u.registry_id, r.parent_registry_id, rp.canonical_label, "
            "r.variant_kind, r.language_code, r.jurisdiction, r.version, r.respondent_form, u.context, u.function, "
            "u.analytic_role FROM scientific_uses u JOIN studies s USING (study_id) "
            "JOIN publications p ON p.publication_id = s.publication_id "
            "LEFT JOIN registry_entities r ON r.registry_id = u.registry_id "
            "LEFT JOIN registry_entities rp ON rp.registry_id = r.parent_registry_id ORDER BY u.use_id"
        )],
    )

    value_counts = counts(db, "SELECT finding_id, COUNT(*) FROM finding_values GROUP BY 1")
    rows = []
    for row in db.execute(
        "SELECT f.finding_id, f.study_id, f.publication_id, p.doi, p.publication_year, t.study_type, f.outcome, "
        "od.family, f.statement, f.details_json FROM findings f JOIN publications p USING (publication_id) "
        "LEFT JOIN study_types t ON t.study_id = f.study_id "
        "LEFT JOIN (SELECT study_id, label, MIN(family) AS family FROM outcome_details GROUP BY 1, 2) od "
        "ON od.study_id = f.study_id AND od.label = f.outcome ORDER BY f.finding_id"
    ):
        rows.append(list(row[:9]) + [json_about(row[9]), value_counts.get(row[0], 0)])
    files["findings"] = (
        ["finding_id", "study_id", "publication_id", "doi", "publication_year", "primary_research_family", "outcome",
         "outcome_family", "statement", "about_ids", "n_values"],
        rows,
    )

    files["finding_values"] = (
        ["finding_id", "ordinal", "publication_id", "doi", "publication_year", "outcome", "reported_value", "unit",
         "denominator", "time", "subgroup", "comparator", "direction", "uncertainty"],
        [list(row) for row in db.execute(
            "SELECT v.finding_id, v.ordinal, f.publication_id, p.doi, p.publication_year, f.outcome, "
            "v.reported_value, v.unit, v.denominator, v.time, v.subgroup, v.comparator, v.direction, v.uncertainty "
            "FROM finding_values v JOIN findings f USING (finding_id) "
            "JOIN publications p ON p.publication_id = f.publication_id ORDER BY v.finding_id, v.ordinal"
        )],
    )

    rows = []
    for row in db.execute(
        "SELECT l.limitation_id, l.study_id, l.publication_id, p.doi, p.publication_year, t.study_type, l.statement, "
        "l.details_json FROM limitations l JOIN publications p USING (publication_id) "
        "LEFT JOIN study_types t ON t.study_id = l.study_id ORDER BY l.limitation_id"
    ):
        rows.append(list(row[:7]) + [json_about(row[7])])
    files["limitations"] = (
        ["limitation_id", "study_id", "publication_id", "doi", "publication_year", "primary_research_family",
         "statement", "about_ids"],
        rows,
    )

    states = {
        axis: multi(db, f"SELECT product_id, exact_state FROM product_states WHERE axis = '{axis}'")
        for axis in ["DEVELOPMENT", "VALIDATION", "DEPLOYMENT", "APPROVAL"]
    }
    scoring = counts(db, "SELECT product_id, COUNT(*) FROM scoring_uses WHERE product_id IS NOT NULL GROUP BY 1")
    rows = []
    for row in db.execute(
        "SELECT r.product_id, r.study_id, s.publication_id, p.doi, p.publication_year, r.product, r.product_type, "
        "r.status FROM research_products r JOIN studies s USING (study_id) "
        "JOIN publications p ON p.publication_id = s.publication_id ORDER BY r.product_id"
    ):
        pid = row[0]
        rows.append(list(row) + [states[axis].get(pid, "") for axis in states] + [scoring.get(pid, 0)])
    files["research_products"] = (
        ["product_id", "study_id", "publication_id", "doi", "publication_year", "product", "product_type", "status",
         "development_state", "validation_state", "deployment_state", "approval_state", "n_scoring_uses"],
        rows,
    )

    affiliations: dict[tuple[str, str], set] = defaultdict(set)
    for publication_id, person_id, affiliation in db.execute(
        "SELECT publication_id, person_id, affiliation FROM author_affiliations"
    ):
        affiliations[(publication_id, person_id)].add(affiliation)
    rows = []
    for row in db.execute(
        "SELECT a.publication_id, p.doi, p.publication_year, a.author_order, a.author_name, a.person_id, "
        "pe.display_name, COALESCE(NULLIF(pe.orcid, ''), a.orcid), pe.openalex_id, pe.entity_kind, a.corresponding, "
        "a.resolution_status FROM publication_authors a JOIN publications p USING (publication_id) "
        "JOIN people pe USING (person_id) ORDER BY a.publication_id, a.author_order, a.person_id"
    ):
        rows.append(list(row) + [MULTI.join(sorted(affiliations.get((row[0], row[5]), ())))])
    files["authorships"] = (
        ["publication_id", "doi", "publication_year", "author_order", "author_name", "person_id", "display_name",
         "orcid", "openalex_id", "entity_kind", "corresponding", "resolution_status", "affiliations"],
        rows,
    )

    members = {row[0] for row in db.execute("SELECT person_id FROM euroqol_memberships")}
    pi_counts = counts(db, "SELECT person_id, COUNT(*) FROM project_people GROUP BY 1")
    accepted = "SELECT a.person_id, %s FROM publication_authors a JOIN publications p USING (publication_id) WHERE a.resolution_status = 'ACCEPTED' GROUP BY 1"
    pub_counts = counts(db, accepted % "COUNT(DISTINCT a.publication_id)")
    first_year = counts(db, accepted % "MIN(p.publication_year)")
    last_year = counts(db, accepted % "MAX(p.publication_year)")
    rows = []
    for row in db.execute(
        "SELECT person_id, display_name, family_name, given_names, orcid, openalex_id, entity_kind, identity_status "
        "FROM people ORDER BY person_id"
    ):
        pid = row[0]
        rows.append(list(row) + [1 if pid in members else 0, pi_counts.get(pid, 0), pub_counts.get(pid, 0),
                                 first_year.get(pid), last_year.get(pid)])
    files["people"] = (
        ["person_id", "display_name", "family_name", "given_names", "orcid", "openalex_id", "entity_kind",
         "identity_status", "euroqol_member", "n_projects_as_pi", "n_publications", "first_publication_year",
         "last_publication_year"],
        rows,
    )

    files["coauthor_edges"] = (
        ["source_id", "source", "target_id", "target", "weight"],
        [list(row) for row in db.execute(COAUTHOR_SQL)],
    )
    return files


def column_profile(db: sqlite3.Connection, table: str, column: str, total: int) -> str:
    empty = db.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL OR {column} = ''").fetchone()[0]
    if total and empty == total:
        return "Empty in this release."
    distinct = db.execute(f"SELECT COUNT(DISTINCT {column}) FROM {table}").fetchone()[0]
    notes = []
    if empty:
        notes.append(f"{empty:,} empty")
    if distinct <= 30 and not column.endswith(("_json", "_url")):
        values = db.execute(
            f"SELECT {column}, COUNT(*) FROM {table} WHERE {column} IS NOT NULL AND {column} != '' "
            f"GROUP BY 1 ORDER BY COUNT(*) DESC, 1"
        ).fetchall()
        if values and all(CODED.match(str(value)) for value, _ in values):
            notes.append("values: " + ", ".join(f"{value} ({count:,})" for value, count in values))
    return "; ".join(notes) + ("." if notes else "")


def json_keys(db: sqlite3.Connection, table: str, column: str) -> list[str]:
    keys = set()
    for (text,) in db.execute(f"SELECT {column} FROM {table} WHERE {column} IS NOT NULL"):
        try:
            value = json.loads(text)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            keys.update(value)
    return sorted(keys)


def note_for(table: str, column: str) -> str:
    return COLUMN_NOTES.get((table, column)) or COLUMN_NOTES.get(("*", column)) or ""


def md_escape(text: str) -> str:
    return str(text).replace("|", "\\|")


def build_codebook(db: sqlite3.Connection, release: str, database_sha: str, analysis, sqlite_name: str,
                   zip_name: str) -> str:
    out: list[str] = []
    meta = dict(db.execute("SELECT key, value FROM metadata"))
    p = out.append
    p(f"# EQ-Graph codebook, release `{release}`")
    p("")
    p(f"Ontology {meta.get('ontology_version', '')}. Scope: {meta.get('scope', '')}. "
      f"Public database SHA-256 `{database_sha}`. "
      "Generated by `scripts/export_public_release.py`. Do not edit by hand.")
    p("")
    p("## Files")
    p("")
    p("| File | Contents |")
    p("|---|---|")
    p(f"| `{sqlite_name}` | The public database, {len(table_names(db))} tables. |")
    p(f"| `{zip_name}` | One CSV per table, this codebook, `VOCABULARY.tsv`, `ONTOLOGY.md`, and `LICENSE.md`. |")
    p("| `analysis/*.csv` | Joined, analysis-ready files. Each row has the publication DOI and year. |")
    p("| `SHA256SUMS` | Hashes of every released file. |")
    p("")
    p("## Open the database")
    p("")
    p("```r")
    p("library(DBI)")
    p(f'con <- dbConnect(RSQLite::SQLite(), "{sqlite_name}")')
    p("dbListTables(con)")
    p('publications <- dbGetQuery(con, "SELECT * FROM publications")')
    p("```")
    p("")
    p("```python")
    p("import sqlite3, pandas as pd")
    p(f'con = sqlite3.connect("{sqlite_name}")')
    p('publications = pd.read_sql("SELECT * FROM publications", con)')
    p("```")
    p("")
    p("Without code: open the file in DB Browser for SQLite (sqlitebrowser.org), or use the CSV files.")
    p("")
    p("## Identifiers and joins")
    p("")
    p("- `publication_id` is `doi:<DOI>` when a DOI exists, otherwise an opaque key. `publications.doi` holds the bare DOI.")
    p("- `study_id` and every item id (`finding_id`, `use_id`, `sample_id`, ...) start with the paper key: `P00088d2d4963:S1`, `P00088d2d4963:F1`. Use ids only for joins.")
    p("- `person_id` prefixes show the origin: `person:openalex:`, `person:eqmember:`, `person:leader:`, `person:orcid:`, `person:author:`, `group:author:`.")
    p("- `registry_id` is `<type>:<slug>`, for example `instrument:eq-5d-5l`. `registry_entities.parent_registry_id` links a variant to its parent.")
    p(f"- Multi-value cells in the analysis files are joined with `{MULTI.strip()}` and sorted.")
    p("- `*_json` columns hold JSON; their keys are listed under each table.")
    p("")
    p("## Counting rules")
    p("")
    p("- A project-publication link exists only when the full text confirmed it; a missing link is not evidence of no relation.")
    p("- One primary research family per study (`study_types`). Purposes, countries, instruments, and methods are multi-valued; totals exceed the study count.")
    p("- Filter `scientific_uses` on `context` before counting. `DIRECT_CURRENT_ACTIVITY` and `CURRENT_STUDY_OBJECT` mean used or examined by the study; `DISCUSSION_ONLY`, `SOURCE_STUDY_ACTIVITY`, `PLANNED_ACTIVITY`, and `INPUT_DATA_PROVENANCE` do not.")
    p("- Aggregate on `canonical_label` or `registry_id`, not `source_label`.")
    p("- `NOT_REPORTED`, `NOT_APPLICABLE`, `UNMAPPED_VALUE`, and gap rows are explicit states, not scientific categories.")
    p("- Citation counts are one OpenAlex snapshot, dated in `publication_citations.retrieved_at`. `NOT_FOUND` rows carry no count.")
    p("- A language model extracted findings and limitations under the ontology; deterministic validation checked them. They are selected, source-faithful, not verbatim, and not exhaustive.")
    p("")
    p("## Analysis files")
    p("")
    for name, (header, rows) in analysis.items():
        description, notes = ANALYSIS_NOTES[name]
        p(f"### `analysis/{name}.csv` ({len(rows):,} rows)")
        p("")
        p(description)
        p("")
        p("| Column | Description |")
        p("|---|---|")
        for column in header:
            note = notes.get(column) or note_for(name if name in TABLE_NOTES else "*", column) or fallback_note(column)
            p(f"| `{column}` | {md_escape(note)} |")
        p("")
    p("## Tables")
    p("")
    for table in table_names(db):
        total = db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        p(f"### `{table}` ({total:,} rows)")
        p("")
        p(TABLE_NOTES.get(table, ""))
        p("")
        p("| Column | Type | Description | Notes |")
        p("|---|---|---|---|")
        for name, typ, pk in columns(db, table):
            note = note_for(table, name)
            profile = column_profile(db, table, name, total) if total else ""
            key = " (key)" if pk else ""
            p(f"| `{name}`{key} | {typ or 'TEXT'} | {md_escape(note)} | {md_escape(profile)} |")
        json_columns = [name for name, _, _ in columns(db, table) if name.endswith("_json")]
        for name in json_columns:
            keys = json_keys(db, table, name)
            if keys:
                p("")
                p(f"`{name}` keys: " + ", ".join(f"`{key}`" for key in keys) + ".")
        p("")
    p("## Controlled vocabulary")
    p("")
    p("`VOCABULARY.tsv` in the tables archive defines every controlled value: `group`, `key`, `value`, `definition`. "
      "`ONTOLOGY.md` states the extraction rules. Column notes name the vocabulary key.")
    p("")
    p("## Licence and citation")
    p("")
    p("Licence: `LICENSE.md` in the tables archive, `release/LICENSE.md` in the repository. "
      "Citation: `CITATION.cff` at the repository root.")
    p("")
    return "\n".join(out)


def fallback_note(column: str) -> str:
    return {
        "doi": "DOI of the publication.",
        "publication_year": "Year of publication.",
        "title": "Title.",
        "n_publications": "Publication count.",
    }.get(column, "")


def write_zip(path: Path, entries: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, entries[name])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--database", type=Path, default=Path("web/server/data/serving.sqlite"))
    parser.add_argument("--release", required=True, help="Release name, for example beta-2026-08-29")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--vocabulary", type=Path, default=Path("pilot/ontology-development-v4/VOCABULARY.tsv"))
    parser.add_argument("--ontology", type=Path, default=Path("pilot/ontology-development-v4/ONTOLOGY.md"))
    parser.add_argument("--licence", type=Path, default=Path("release/LICENSE.md"))
    args = parser.parse_args()

    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    (output / "analysis").mkdir(exist_ok=True)

    sqlite_name = f"eq-graph-{args.release}.sqlite"
    zip_name = f"eq-graph-{args.release}-tables.zip"
    shutil.copyfile(args.database, output / sqlite_name)
    database_sha = sha256(args.database)
    if sha256(output / sqlite_name) != database_sha:
        raise SystemExit("The copied database does not match the source.")

    db = sqlite3.connect(f"file:{args.database}?mode=ro", uri=True)
    analysis = build_analysis(db)
    codebook = build_codebook(db, args.release, database_sha, analysis, sqlite_name, zip_name)

    entries: dict[str, bytes] = {}
    for table in table_names(db):
        cols = [name for name, _, _ in columns(db, table)]
        rows = db.execute(f"SELECT {', '.join(cols)} FROM {table} ORDER BY {order_clause(db, table)}")
        entries[f"tables/{table}.csv"] = csv_text(cols, rows).encode("utf-8")
    entries["CODEBOOK.md"] = codebook.encode("utf-8")
    entries["VOCABULARY.tsv"] = args.vocabulary.read_bytes()
    entries["ONTOLOGY.md"] = args.ontology.read_bytes()
    entries["LICENSE.md"] = args.licence.read_bytes()
    write_zip(output / zip_name, entries)

    for name, (header, rows) in analysis.items():
        (output / "analysis" / f"{name}.csv").write_text(csv_text(header, rows), encoding="utf-8")
    (output / "CODEBOOK.md").write_text(codebook, encoding="utf-8")

    files = sorted(
        path for path in output.rglob("*") if path.is_file() and path.name != "SHA256SUMS"
    )
    (output / "SHA256SUMS").write_text(
        "".join(f"{sha256(path)}  {path.relative_to(output).as_posix()}\n" for path in files), encoding="utf-8"
    )
    for path in files:
        print(f"{path.stat().st_size:>12,}  {path.relative_to(output).as_posix()}")


if __name__ == "__main__":
    main()
