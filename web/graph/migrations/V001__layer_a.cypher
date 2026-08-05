// Layer A — the bibliographic spine.
//
// This file is the Community Edition form of Kazik's graph/schema.cypher.
// Two changes:
//   1. IS UNIQUE replaces IS NODE KEY. Community Edition has no node keys.
//   2. Section 4 is absent. Community Edition has no existence constraints and
//      no property type constraints. The loader validates instead.
//
// The constraint names match Kazik's names, because a test can assert a name.

// --- Uniqueness -------------------------------------------------------------

CREATE CONSTRAINT project_id_key IF NOT EXISTS
FOR (n:Project) REQUIRE n.projectId IS UNIQUE;

CREATE CONSTRAINT working_group_name_key IF NOT EXISTS
FOR (n:WorkingGroup) REQUIRE n.name IS UNIQUE;

CREATE CONSTRAINT grant_type_code_key IF NOT EXISTS
FOR (n:GrantType) REQUIRE n.code IS UNIQUE;

CREATE CONSTRAINT grant_category_name_key IF NOT EXISTS
FOR (n:GrantCategory) REQUIRE n.name IS UNIQUE;

CREATE CONSTRAINT work_id_key IF NOT EXISTS
FOR (n:Work) REQUIRE n.workId IS UNIQUE;

CREATE CONSTRAINT work_doi_unique IF NOT EXISTS
FOR (n:Work) REQUIRE n.doi IS UNIQUE;

CREATE CONSTRAINT journal_name_key IF NOT EXISTS
FOR (n:Journal) REQUIRE n.name IS UNIQUE;

CREATE CONSTRAINT person_id_key IF NOT EXISTS
FOR (n:Person) REQUIRE n.personId IS UNIQUE;

CREATE CONSTRAINT person_orcid_unique IF NOT EXISTS
FOR (n:Person) REQUIRE n.orcid IS UNIQUE;

CREATE CONSTRAINT authorship_id_key IF NOT EXISTS
FOR (n:Authorship) REQUIRE n.authorshipId IS UNIQUE;

CREATE CONSTRAINT organization_ror_key IF NOT EXISTS
FOR (n:Organization) REQUIRE n.rorId IS UNIQUE;

CREATE CONSTRAINT country_iso2_key IF NOT EXISTS
FOR (n:Country) REQUIRE n.iso2 IS UNIQUE;

CREATE CONSTRAINT attribution_id_key IF NOT EXISTS
FOR (n:Attribution) REQUIRE n.attributionId IS UNIQUE;

CREATE CONSTRAINT evidence_id_key IF NOT EXISTS
FOR (n:Evidence) REQUIRE n.evidenceId IS UNIQUE;

CREATE CONSTRAINT instrument_id_key IF NOT EXISTS
FOR (n:Instrument) REQUIRE n.instrumentId IS UNIQUE;

CREATE CONSTRAINT study_id_key IF NOT EXISTS
FOR (n:Study) REQUIRE n.studyId IS UNIQUE;

CREATE CONSTRAINT value_set_id_key IF NOT EXISTS
FOR (n:ValueSet) REQUIRE n.valueSetId IS UNIQUE;

// --- Range indexes ----------------------------------------------------------

CREATE INDEX project_status_idx IF NOT EXISTS FOR (n:Project) ON (n.status);
CREATE INDEX project_start_year_idx IF NOT EXISTS FOR (n:Project) ON (n.startYear);
CREATE INDEX work_year_idx IF NOT EXISTS FOR (n:Work) ON (n.year);
CREATE INDEX person_last_name_idx IF NOT EXISTS FOR (n:Person) ON (n.lastName);
CREATE INDEX attribution_confidence_idx IF NOT EXISTS FOR (n:Attribution) ON (n.confidence);
CREATE INDEX evidence_kind_idx IF NOT EXISTS FOR (n:Evidence) ON (n.kind);
CREATE INDEX instrument_family_idx IF NOT EXISTS FOR (n:Instrument) ON (n.family);
CREATE INDEX value_set_technique_idx IF NOT EXISTS FOR (n:ValueSet) ON (n.technique);

// --- Full-text indexes ------------------------------------------------------
// The search_graph tool uses these. Without them the agent guesses exact
// strings in a WHERE clause and finds nothing.

CREATE FULLTEXT INDEX project_text_ft IF NOT EXISTS
FOR (n:Project) ON EACH [n.title, n.abstract];

CREATE FULLTEXT INDEX work_text_ft IF NOT EXISTS
FOR (n:Work) ON EACH [n.title, n.abstract, n.journalName];

CREATE FULLTEXT INDEX person_name_ft IF NOT EXISTS
FOR (n:Person) ON EACH [n.fullName];

CREATE FULLTEXT INDEX instrument_name_ft IF NOT EXISTS
FOR (n:Instrument) ON EACH [n.name, n.family];
