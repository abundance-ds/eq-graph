// eq-graph schema — constraints and indexes.
//
// Apply to an empty database BEFORE any import; every statement is idempotent.
//   cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USERNAME" -p "$NEO4J_PASSWORD" -f graph/schema.cypher
//
// Design rationale: docs/graph-model.md
// Layer A = bibliographic spine, B = extracted study content, C = emergent vocabulary.
//
// Sections 1-4 are Enterprise/Aura only: `IS NODE KEY`, existence constraints and property
// type constraints are all Enterprise features. On Community, substitute `IS UNIQUE` for
// every `IS NODE KEY` and skip section 4 entirely — uniqueness ignores nulls, so a key
// property can go missing without the constraint noticing.
// Sections 5-7 (indexes) run everywhere.
// Section 7 (vector indexes) uses dimension 1024; it MUST match the embedding model in use.

// ---------------------------------------------------------------------------
// 1. Uniqueness / key constraints — layer A, bibliographic spine
// ---------------------------------------------------------------------------

CREATE CONSTRAINT project_id_key IF NOT EXISTS
  FOR (n:Project) REQUIRE n.projectId IS NODE KEY;

CREATE CONSTRAINT working_group_name_key IF NOT EXISTS
  FOR (n:WorkingGroup) REQUIRE n.name IS NODE KEY;

CREATE CONSTRAINT grant_type_code_key IF NOT EXISTS
  FOR (n:GrantType) REQUIRE n.code IS NODE KEY;

CREATE CONSTRAINT grant_category_name_key IF NOT EXISTS
  FOR (n:GrantCategory) REQUIRE n.name IS NODE KEY;

// workId is "doi:<doi>", falling back to "pmid:<pmid>" / "pmcid:<pmcid>".
// Some works have no DOI at all — see the 169-RA book case in CLAUDE.md.
CREATE CONSTRAINT work_id_key IF NOT EXISTS
  FOR (n:Work) REQUIRE n.workId IS NODE KEY;

CREATE CONSTRAINT work_doi_unique IF NOT EXISTS
  FOR (n:Work) REQUIRE n.doi IS UNIQUE;

CREATE CONSTRAINT work_pmid_unique IF NOT EXISTS
  FOR (n:Work) REQUIRE n.pmid IS UNIQUE;

CREATE CONSTRAINT work_pmcid_unique IF NOT EXISTS
  FOR (n:Work) REQUIRE n.pmcid IS UNIQUE;

CREATE CONSTRAINT journal_name_key IF NOT EXISTS
  FOR (n:Journal) REQUIRE n.name IS NODE KEY;

// personId is the ORCID where present, else a normalised-name key; `resolved` says which.
CREATE CONSTRAINT person_id_key IF NOT EXISTS
  FOR (n:Person) REQUIRE n.personId IS NODE KEY;

CREATE CONSTRAINT person_orcid_unique IF NOT EXISTS
  FOR (n:Person) REQUIRE n.orcid IS UNIQUE;

CREATE CONSTRAINT authorship_id_key IF NOT EXISTS
  FOR (n:Authorship) REQUIRE n.authorshipId IS NODE KEY;

CREATE CONSTRAINT organization_ror_key IF NOT EXISTS
  FOR (n:Organization) REQUIRE n.rorId IS NODE KEY;

CREATE CONSTRAINT country_iso2_key IF NOT EXISTS
  FOR (n:Country) REQUIRE n.iso2 IS NODE KEY;

// The reified project -> work link. Never collapse this into a relationship:
// 5148 of 5475 rows rest on ack_pi_year alone and must not read as fact.
CREATE CONSTRAINT attribution_id_key IF NOT EXISTS
  FOR (n:Attribution) REQUIRE n.attributionId IS NODE KEY;

CREATE CONSTRAINT evidence_id_key IF NOT EXISTS
  FOR (n:Evidence) REQUIRE n.evidenceId IS NODE KEY;

CREATE CONSTRAINT fulltext_sha256_key IF NOT EXISTS
  FOR (n:FullText) REQUIRE n.sha256 IS NODE KEY;

CREATE CONSTRAINT chunk_id_key IF NOT EXISTS
  FOR (n:Chunk) REQUIRE n.chunkId IS NODE KEY;

// ---------------------------------------------------------------------------
// 2. Uniqueness / key constraints — layer B, extracted study content
// ---------------------------------------------------------------------------

CREATE CONSTRAINT study_id_key IF NOT EXISTS
  FOR (n:Study) REQUIRE n.studyId IS NODE KEY;

CREATE CONSTRAINT sample_id_key IF NOT EXISTS
  FOR (n:Sample) REQUIRE n.sampleId IS NODE KEY;

CREATE CONSTRAINT instrument_id_key IF NOT EXISTS
  FOR (n:Instrument) REQUIRE n.instrumentId IS NODE KEY;

CREATE CONSTRAINT instrument_use_id_key IF NOT EXISTS
  FOR (n:InstrumentUse) REQUIRE n.instrumentUseId IS NODE KEY;

CREATE CONSTRAINT method_id_key IF NOT EXISTS
  FOR (n:Method) REQUIRE n.methodId IS NODE KEY;

// COSMIN measurement property.
CREATE CONSTRAINT property_code_key IF NOT EXISTS
  FOR (n:Property) REQUIRE n.code IS NODE KEY;

// MeSH descriptor id.
CREATE CONSTRAINT condition_code_key IF NOT EXISTS
  FOR (n:Condition) REQUIRE n.code IS NODE KEY;

CREATE CONSTRAINT value_set_id_key IF NOT EXISTS
  FOR (n:ValueSet) REQUIRE n.valueSetId IS NODE KEY;

CREATE CONSTRAINT coefficient_id_key IF NOT EXISTS
  FOR (n:Coefficient) REQUIRE n.coefficientId IS NODE KEY;

CREATE CONSTRAINT finding_id_key IF NOT EXISTS
  FOR (n:Finding) REQUIRE n.findingId IS NODE KEY;

// prov:Activity — one node per extraction run. Every layer-B node points at the run
// that produced it, so a bad prompt version is traceable to exactly its own output.
CREATE CONSTRAINT extraction_id_key IF NOT EXISTS
  FOR (n:Extraction) REQUIRE n.extractionId IS NODE KEY;

// ---------------------------------------------------------------------------
// 3. Uniqueness / key constraints — layer C and the meta catalog
// ---------------------------------------------------------------------------

CREATE CONSTRAINT concept_id_key IF NOT EXISTS
  FOR (n:Concept) REQUIRE n.conceptId IS NODE KEY;

CREATE CONSTRAINT term_normalized_key IF NOT EXISTS
  FOR (n:Term) REQUIRE n.normalized IS NODE KEY;

// `_`-prefixed labels are the agent's self-description, filtered out of the domain schema.
CREATE CONSTRAINT meta_node_type_key IF NOT EXISTS
  FOR (n:_NodeType) REQUIRE n.name IS NODE KEY;

CREATE CONSTRAINT meta_rel_type_key IF NOT EXISTS
  FOR (n:_RelType) REQUIRE n.name IS NODE KEY;

CREATE CONSTRAINT meta_property_def_key IF NOT EXISTS
  FOR (n:_PropertyDef) REQUIRE n.qualifiedName IS NODE KEY;

CREATE CONSTRAINT meta_query_template_key IF NOT EXISTS
  FOR (n:_QueryTemplate) REQUIRE n.name IS NODE KEY;

// Class-level alignment to published vocabularies (schema.org, PROV-O, SKOS, ...).
// Design-time and static, so it lives in the catalog rather than on the domain nodes.
// Instance-level alignment is a different thing entirely: EXACT_MATCH / CLOSE_MATCH
// edges between :Concept nodes, which are data and grow with the corpus.
CREATE CONSTRAINT meta_vocabulary_prefix_key IF NOT EXISTS
  FOR (n:_Vocabulary) REQUIRE n.prefix IS NODE KEY;

CREATE CONSTRAINT meta_vocabulary_term_curie_key IF NOT EXISTS
  FOR (n:_VocabularyTerm) REQUIRE n.curie IS NODE KEY;

// ---------------------------------------------------------------------------
// 4. Property type and existence constraints — Enterprise / Aura only
//    Skip this section on Community Edition.
// ---------------------------------------------------------------------------

CREATE CONSTRAINT project_title_exists IF NOT EXISTS
  FOR (n:Project) REQUIRE n.title IS NOT NULL;

CREATE CONSTRAINT project_start_year_integer IF NOT EXISTS
  FOR (n:Project) REQUIRE n.startYear IS :: INTEGER;

CREATE CONSTRAINT project_budget_integer IF NOT EXISTS
  FOR (n:Project) REQUIRE n.approvedBudgetEur IS :: INTEGER;

CREATE CONSTRAINT work_title_exists IF NOT EXISTS
  FOR (n:Work) REQUIRE n.title IS NOT NULL;

CREATE CONSTRAINT work_year_integer IF NOT EXISTS
  FOR (n:Work) REQUIRE n.year IS :: INTEGER;

// One of: accepted | review | weak. Enforced as a value set by the loader.
CREATE CONSTRAINT attribution_confidence_exists IF NOT EXISTS
  FOR (n:Attribution) REQUIRE n.confidence IS NOT NULL;

CREATE CONSTRAINT attribution_score_float IF NOT EXISTS
  FOR (n:Attribution) REQUIRE n.score IS :: FLOAT;

// One of: grant_id_structured | grant_id_acknowledged | grant_id_fulltext
//       | title_exact | title_strong | title_fuzzy | ack_pi_year
CREATE CONSTRAINT evidence_kind_exists IF NOT EXISTS
  FOR (n:Evidence) REQUIRE n.kind IS NOT NULL;

CREATE CONSTRAINT chunk_text_exists IF NOT EXISTS
  FOR (n:Chunk) REQUIRE n.text IS NOT NULL;

// candidate | promoted | merged
CREATE CONSTRAINT concept_status_exists IF NOT EXISTS
  FOR (n:Concept) REQUIRE n.status IS NOT NULL;

CREATE CONSTRAINT concept_pref_label_exists IF NOT EXISTS
  FOR (n:Concept) REQUIRE n.prefLabel IS NOT NULL;

// ---------------------------------------------------------------------------
// 5. Range and text indexes
// ---------------------------------------------------------------------------

CREATE INDEX project_status_idx IF NOT EXISTS
  FOR (n:Project) ON (n.status);

CREATE INDEX project_start_year_idx IF NOT EXISTS
  FOR (n:Project) ON (n.startYear);

CREATE INDEX work_year_idx IF NOT EXISTS
  FOR (n:Work) ON (n.year);

// The hot filter: almost every agent query starts by restricting to accepted.
CREATE INDEX attribution_confidence_idx IF NOT EXISTS
  FOR (n:Attribution) ON (n.confidence);

CREATE INDEX evidence_kind_idx IF NOT EXISTS
  FOR (n:Evidence) ON (n.kind);

CREATE INDEX person_last_name_idx IF NOT EXISTS
  FOR (n:Person) ON (n.lastName);

CREATE INDEX chunk_section_type_idx IF NOT EXISTS
  FOR (n:Chunk) ON (n.sectionType);

CREATE INDEX instrument_family_idx IF NOT EXISTS
  FOR (n:Instrument) ON (n.family);

CREATE INDEX value_set_technique_idx IF NOT EXISTS
  FOR (n:ValueSet) ON (n.technique);

CREATE INDEX finding_metric_idx IF NOT EXISTS
  FOR (n:Finding) ON (n.metric);

// Drives the curation queue: candidates ordered by accumulated support.
CREATE INDEX concept_status_support_idx IF NOT EXISTS
  FOR (n:Concept) ON (n.status, n.support);

CREATE INDEX concept_scheme_idx IF NOT EXISTS
  FOR (n:Concept) ON (n.scheme);

// Lets the accuracy audit slice output by the run that produced it.
CREATE INDEX extraction_prompt_version_idx IF NOT EXISTS
  FOR (n:Extraction) ON (n.promptVersion);

// ---------------------------------------------------------------------------
// 6. Full-text indexes
//    Exact-identifier lookup must never go through the vector index.
// ---------------------------------------------------------------------------

CREATE FULLTEXT INDEX work_text_ft IF NOT EXISTS
  FOR (n:Work) ON EACH [n.title, n.abstract, n.journalName];

CREATE FULLTEXT INDEX project_text_ft IF NOT EXISTS
  FOR (n:Project) ON EACH [n.title, n.abstract];

CREATE FULLTEXT INDEX person_name_ft IF NOT EXISTS
  FOR (n:Person) ON EACH [n.fullName];

CREATE FULLTEXT INDEX instrument_name_ft IF NOT EXISTS
  FOR (n:Instrument) ON EACH [n.name, n.family];

CREATE FULLTEXT INDEX concept_label_ft IF NOT EXISTS
  FOR (n:Concept) ON EACH [n.prefLabel, n.definition];

CREATE FULLTEXT INDEX term_text_ft IF NOT EXISTS
  FOR (n:Term) ON EACH [n.text];

// ---------------------------------------------------------------------------
// 7. Vector indexes
//    `vector.dimensions` MUST equal the embedding model's output width.
//    1024 is a placeholder (Voyage voyage-3.5); OpenAI text-embedding-3-small is 1536.
//    Changing it means dropping and rebuilding the index and re-embedding everything.
// ---------------------------------------------------------------------------

// Passage embeddings live only here — project abstracts, work abstracts and
// section-aware full-text chunks all become :Chunk, so one index serves all three.
CREATE VECTOR INDEX chunk_embedding_idx IF NOT EXISTS
  FOR (n:Chunk) ON (n.embedding)
  OPTIONS { indexConfig: {
    `vector.dimensions`: 1024,
    `vector.similarity_function`: 'cosine',
    `vector.quantization.type`: 'SCALAR'
  } };

// On Neo4j 2026.01+ the index can carry filterable metadata, letting SEARCH ... WHERE
// filter inside the index instead of post-filtering. Replace the statement above with:
//
// CREATE VECTOR INDEX chunk_embedding_idx IF NOT EXISTS
//   FOR (n:Chunk) ON (n.embedding)
//   WITH [n.sectionType, n.source, n.year]
//   OPTIONS { indexConfig: { `vector.dimensions`: 1024, `vector.similarity_function`: 'cosine' } };

// Deliberate deviation from "embeddings only on :Chunk": the concept embedding IS the
// entity-resolution key, queried before minting a candidate, and there are only thousands.
CREATE VECTOR INDEX concept_embedding_idx IF NOT EXISTS
  FOR (n:Concept) ON (n.embedding)
  OPTIONS { indexConfig: {
    `vector.dimensions`: 1024,
    `vector.similarity_function`: 'cosine',
    `vector.quantization.type`: 'SCALAR'
  } };

// ---------------------------------------------------------------------------
// 8. Verify
// ---------------------------------------------------------------------------

// Do not import or query until every index reports ONLINE:
//   SHOW INDEXES YIELD name, type, state WHERE state <> 'ONLINE' RETURN name, type, state;
//   SHOW CONSTRAINTS YIELD name, type, labelsOrTypes, properties RETURN name, type, labelsOrTypes, properties;
