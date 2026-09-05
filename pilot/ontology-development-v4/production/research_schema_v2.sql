PRAGMA foreign_keys = ON;

CREATE TABLE build (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
) STRICT;

CREATE TABLE publication (
    publication_id TEXT PRIMARY KEY,
    record_id TEXT NOT NULL UNIQUE,
    doi TEXT UNIQUE,
    pmid TEXT,
    pmcid TEXT,
    title TEXT NOT NULL,
    abstract TEXT,
    publication_year INTEGER,
    journal TEXT,
    publisher TEXT,
    jats_article_type TEXT,
    publication_form TEXT NOT NULL,
    language TEXT,
    volume TEXT,
    issue TEXT,
    article_number TEXT,
    licence_url TEXT,
    open_access INTEGER NOT NULL CHECK (open_access IN (0, 1)),
    canonical_url TEXT,
    assessment_disposition TEXT NOT NULL,
    euroqol_connection TEXT NOT NULL,
    euroqol_support TEXT NOT NULL,
    support_scope TEXT,
    assessment_reason TEXT NOT NULL,
    schema_version TEXT NOT NULL
) STRICT;

CREATE TABLE source_record (
    record_id TEXT PRIMARY KEY REFERENCES publication(record_id),
    article_path TEXT NOT NULL,
    article_sha256 TEXT NOT NULL,
    article_bytes INTEGER NOT NULL CHECK (article_bytes > 0),
    source_format TEXT NOT NULL CHECK (source_format IN ('JATS_XML', 'PDF')),
    source_path TEXT NOT NULL,
    source_sha256 TEXT NOT NULL,
    source_bytes INTEGER NOT NULL CHECK (source_bytes > 0),
    extraction_record_path TEXT NOT NULL,
    extraction_record_sha256 TEXT NOT NULL,
    extraction_source_run TEXT NOT NULL
) STRICT;

CREATE TABLE assessment_source (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    locator TEXT NOT NULL,
    PRIMARY KEY (publication_id, ordinal)
) STRICT;

CREATE TABLE publication_date (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    date_type TEXT NOT NULL,
    date_value TEXT NOT NULL,
    PRIMARY KEY (publication_id, date_type, date_value)
) STRICT;

CREATE TABLE publication_url (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    url_type TEXT NOT NULL,
    url TEXT NOT NULL,
    PRIMARY KEY (publication_id, url_type, url)
) STRICT;

CREATE TABLE person (
    person_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    family_name TEXT,
    given_names TEXT,
    orcid TEXT,
    openalex_id TEXT,
    entity_kind TEXT NOT NULL CHECK (entity_kind IN ('PERSON', 'GROUP')),
    identity_status TEXT NOT NULL
) STRICT;

CREATE TABLE person_name (
    person_id TEXT NOT NULL REFERENCES person(person_id),
    name TEXT NOT NULL,
    name_type TEXT NOT NULL,
    source TEXT NOT NULL,
    PRIMARY KEY (person_id, name, source)
) STRICT;

CREATE TABLE person_identifier (
    person_id TEXT NOT NULL REFERENCES person(person_id),
    scheme TEXT NOT NULL CHECK (scheme IN ('ORCID', 'OPENALEX')),
    value TEXT NOT NULL,
    source TEXT NOT NULL,
    PRIMARY KEY (person_id, scheme, value),
    UNIQUE (scheme, value)
) STRICT;

CREATE TABLE euroqol_membership (
    person_id TEXT PRIMARY KEY REFERENCES person(person_id),
    member_id TEXT NOT NULL UNIQUE,
    affiliation TEXT,
    profile_url TEXT,
    observed_date TEXT NOT NULL,
    status TEXT NOT NULL
) STRICT;

CREATE TABLE publication_author (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    person_id TEXT NOT NULL REFERENCES person(person_id),
    source_author_id TEXT,
    display_name TEXT NOT NULL,
    author_order INTEGER NOT NULL CHECK (author_order > 0),
    corresponding INTEGER NOT NULL CHECK (corresponding IN (0, 1)),
    email TEXT,
    roles_json TEXT NOT NULL CHECK (json_valid(roles_json)),
    resolution_method TEXT NOT NULL,
    resolution_status TEXT NOT NULL,
    PRIMARY KEY (publication_id, author_order),
    UNIQUE (publication_id, person_id)
) STRICT;

CREATE TABLE publication_correspondence (
    correspondence_id INTEGER PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    label TEXT,
    correspondence_text TEXT NOT NULL,
    email TEXT
) STRICT;

CREATE TABLE affiliation (
    affiliation_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    source_affiliation_id TEXT NOT NULL,
    name TEXT NOT NULL,
    ror TEXT,
    grid TEXT,
    isni TEXT,
    UNIQUE (publication_id, source_affiliation_id)
) STRICT;

CREATE TABLE author_affiliation (
    publication_id TEXT NOT NULL,
    person_id TEXT NOT NULL,
    affiliation_id TEXT NOT NULL REFERENCES affiliation(affiliation_id),
    PRIMARY KEY (publication_id, person_id, affiliation_id),
    FOREIGN KEY (publication_id, person_id)
        REFERENCES publication_author(publication_id, person_id)
) STRICT;

CREATE TABLE publication_keyword (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    keyword TEXT NOT NULL,
    PRIMARY KEY (publication_id, keyword)
) STRICT;

CREATE TABLE publication_category (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    category_type TEXT NOT NULL,
    category TEXT NOT NULL,
    PRIMARY KEY (publication_id, category_type, category)
) STRICT;

CREATE TABLE publication_funding (
    funding_id INTEGER PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    funder TEXT,
    award_id TEXT,
    recipient TEXT,
    source_text TEXT,
    source_locator TEXT NOT NULL
) STRICT;

CREATE TABLE publication_relation (
    publication_id TEXT PRIMARY KEY REFERENCES publication(publication_id),
    relation_type TEXT NOT NULL CHECK (relation_type IN ('CORRECTS', 'RETRACTS')),
    target_doi TEXT NOT NULL,
    source_json TEXT NOT NULL CHECK (json_valid(source_json))
) STRICT;

CREATE TABLE citation_occurrence (
    citation_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    source_reference_id TEXT,
    citation_text TEXT,
    doi TEXT,
    pmid TEXT,
    target_publication_id TEXT REFERENCES publication(publication_id),
    resolution_status TEXT NOT NULL CHECK (
        resolution_status IN ('resolved', 'external-or-unresolved', 'identifier-conflict')
    )
) STRICT;

CREATE TABLE registry_identity (
    registry_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    canonical_label TEXT NOT NULL,
    parent_registry_id TEXT REFERENCES registry_identity(registry_id),
    applies_to_registry_id TEXT REFERENCES registry_identity(registry_id),
    variant_kind TEXT,
    language_code TEXT,
    jurisdiction TEXT,
    version TEXT,
    respondent_form TEXT,
    source_identifier TEXT,
    scope TEXT
) STRICT;

CREATE TABLE registry_alias (
    registry_id TEXT NOT NULL REFERENCES registry_identity(registry_id),
    alias TEXT NOT NULL,
    use_type TEXT NOT NULL CHECK (
        use_type IN (
            'Instrument', 'Method', 'Protocol', 'Model', 'Software',
            'Product', 'Scoring'
        )
    ),
    PRIMARY KEY (registry_id, alias, use_type)
) STRICT;

CREATE TABLE study (
    study_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    local_id TEXT NOT NULL,
    label TEXT NOT NULL,
    primary_research_family TEXT NOT NULL,
    execution_state TEXT NOT NULL,
    result_state TEXT NOT NULL,
    family_rationale TEXT NOT NULL,
    UNIQUE (publication_id, local_id)
) STRICT;

CREATE TABLE study_source (
    study_id TEXT NOT NULL REFERENCES study(study_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    locator TEXT NOT NULL,
    PRIMARY KEY (study_id, ordinal)
) STRICT;

CREATE TABLE item (
    item_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    record_id TEXT NOT NULL REFERENCES publication(record_id),
    local_id TEXT NOT NULL,
    study_id TEXT REFERENCES study(study_id),
    part_item_id TEXT REFERENCES item(item_id),
    type TEXT NOT NULL CHECK (type IN (
        'Purpose', 'StudyPart', 'Design', 'Population', 'Sample', 'DataUse',
        'InstrumentUse', 'MethodUse', 'ProtocolUse', 'ModelUse', 'SoftwareUse',
        'ProductUse', 'ScoringUse',
        'TaskDesign', 'StudyFactor', 'Administration', 'StakeholderInvolvement',
        'Outcome', 'Finding', 'Interpretation', 'Limitation', 'Product',
        'ProductStateAssertion', 'Concept', 'Gap', 'SourceConflict',
        'PublicationStatusAssertion'
    )),
    payload_json TEXT NOT NULL CHECK (json_valid(payload_json)),
    UNIQUE (record_id, local_id)
) STRICT;

CREATE TABLE item_source (
    item_id TEXT NOT NULL REFERENCES item(item_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    locator TEXT NOT NULL,
    PRIMARY KEY (item_id, ordinal)
) STRICT;

CREATE TABLE item_relation (
    source_item_id TEXT NOT NULL REFERENCES item(item_id),
    predicate TEXT NOT NULL,
    target_item_id TEXT NOT NULL REFERENCES item(item_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    PRIMARY KEY (source_item_id, predicate, target_item_id)
) STRICT;

CREATE TABLE item_study_relation (
    source_item_id TEXT NOT NULL REFERENCES item(item_id),
    predicate TEXT NOT NULL,
    target_study_id TEXT NOT NULL REFERENCES study(study_id),
    PRIMARY KEY (source_item_id, predicate, target_study_id)
) STRICT;

CREATE TABLE relation_rule (
    source_type TEXT NOT NULL,
    predicate TEXT NOT NULL,
    target_type TEXT NOT NULL,
    PRIMARY KEY (source_type, predicate, target_type)
) STRICT;

CREATE TABLE item_text_value (
    item_id TEXT NOT NULL REFERENCES item(item_id),
    value_type TEXT NOT NULL,
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    value TEXT NOT NULL,
    PRIMARY KEY (item_id, value_type, ordinal)
) STRICT;

CREATE TABLE purpose (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    study_id TEXT NOT NULL REFERENCES study(study_id),
    value TEXT NOT NULL,
    rank INTEGER NOT NULL CHECK (rank > 0),
    UNIQUE (study_id, rank)
) STRICT;

CREATE TABLE study_part (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    study_id TEXT NOT NULL REFERENCES study(study_id),
    label TEXT NOT NULL
) STRICT;

CREATE TABLE design (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    study_id TEXT NOT NULL REFERENCES study(study_id),
    part_item_id TEXT REFERENCES study_part(item_id),
    axis TEXT NOT NULL,
    value TEXT NOT NULL
) STRICT;

CREATE TABLE population (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    label TEXT NOT NULL,
    role TEXT,
    age_description TEXT,
    inclusion_description TEXT
) STRICT;

CREATE TABLE sample (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    population_item_id TEXT REFERENCES population(item_id),
    stage TEXT NOT NULL,
    size INTEGER CHECK (size >= 0),
    size_text TEXT,
    unit TEXT,
    description TEXT
) STRICT;

CREATE TABLE data_use (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    source_label TEXT NOT NULL,
    origin TEXT NOT NULL,
    level TEXT NOT NULL,
    purpose TEXT
) STRICT;

CREATE TABLE registry_use (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    use_type TEXT NOT NULL CHECK (
        use_type IN (
            'Instrument', 'Method', 'Protocol', 'Model', 'Software', 'Product'
        )
    ),
    source_label TEXT NOT NULL,
    registry_id TEXT REFERENCES registry_identity(registry_id),
    context TEXT NOT NULL,
    function TEXT NOT NULL,
    analytic_role TEXT
) STRICT;

CREATE TABLE scoring_use (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    source_label TEXT NOT NULL,
    registry_id TEXT REFERENCES registry_identity(registry_id),
    context TEXT NOT NULL,
    instrument_use_item_id TEXT NOT NULL REFERENCES registry_use(item_id),
    product_item_id TEXT REFERENCES item(item_id)
) STRICT;

CREATE TABLE task_design (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    label TEXT NOT NULL,
    duration TEXT,
    alternatives TEXT,
    task_count TEXT,
    block TEXT,
    task_order TEXT,
    randomization_unit TEXT,
    stopping_rule TEXT
) STRICT;

CREATE TABLE study_factor (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    label TEXT NOT NULL,
    role TEXT NOT NULL
) STRICT;

CREATE TABLE administration (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    respondent TEXT,
    perspective TEXT,
    completion TEXT,
    assistance TEXT,
    channel TEXT,
    setting TEXT,
    instrument_language TEXT,
    interview_language TEXT,
    recall_period TEXT,
    time_point TEXT
) STRICT;

CREATE TABLE stakeholder_involvement (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    stakeholder_group TEXT NOT NULL,
    activity TEXT NOT NULL,
    stage TEXT,
    role TEXT,
    influence TEXT NOT NULL
) STRICT;

CREATE TABLE outcome (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    family TEXT NOT NULL,
    label TEXT NOT NULL
) STRICT;

CREATE TABLE finding (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE finding_value (
    finding_item_id TEXT NOT NULL REFERENCES finding(item_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    reported_value TEXT NOT NULL,
    unit TEXT,
    denominator TEXT,
    time TEXT,
    subgroup TEXT,
    comparator TEXT,
    direction TEXT,
    uncertainty TEXT,
    PRIMARY KEY (finding_item_id, ordinal)
) STRICT;

CREATE TABLE interpretation (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE limitation (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE product (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    label TEXT NOT NULL,
    product_type TEXT NOT NULL
) STRICT;

CREATE TABLE product_state_assertion (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    product_item_id TEXT NOT NULL REFERENCES product(item_id),
    axis TEXT NOT NULL,
    exact_state TEXT NOT NULL,
    assertion_date TEXT,
    asserted_by TEXT
) STRICT;

CREATE TABLE concept (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    label TEXT NOT NULL,
    description TEXT
) STRICT;

CREATE TABLE gap (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    state TEXT NOT NULL,
    affected_type TEXT NOT NULL,
    affected_key TEXT NOT NULL,
    evidence TEXT NOT NULL,
    importance TEXT NOT NULL,
    proposed_resolution TEXT NOT NULL
) STRICT;

CREATE TABLE source_conflict (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    scope TEXT NOT NULL
) STRICT;

CREATE TABLE source_conflict_statement (
    conflict_item_id TEXT NOT NULL REFERENCES source_conflict(item_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    statement TEXT NOT NULL,
    source_json TEXT NOT NULL CHECK (json_valid(source_json)),
    PRIMARY KEY (conflict_item_id, ordinal)
) STRICT;

CREATE TABLE publication_status_assertion (
    item_id TEXT PRIMARY KEY REFERENCES item(item_id),
    status TEXT NOT NULL,
    exact_term TEXT NOT NULL,
    assertion_date TEXT,
    asserted_by TEXT,
    reason TEXT,
    notice_doi TEXT
) STRICT;

CREATE TABLE project (
    project_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    abstract TEXT,
    principal_investigator TEXT,
    working_group TEXT,
    approved_budget_eur REAL,
    status TEXT,
    start_year INTEGER,
    end_year INTEGER
) STRICT;

CREATE TABLE project_publication (
    project_id TEXT NOT NULL REFERENCES project(project_id),
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    project_output TEXT,
    support_target TEXT,
    support_scope TEXT,
    evidence_status TEXT NOT NULL,
    PRIMARY KEY (project_id, publication_id)
) STRICT;

CREATE TABLE project_person (
    project_id TEXT NOT NULL REFERENCES project(project_id),
    person_id TEXT NOT NULL REFERENCES person(person_id),
    role TEXT NOT NULL,
    source_name TEXT NOT NULL,
    resolution_method TEXT NOT NULL,
    resolution_status TEXT NOT NULL,
    PRIMARY KEY (project_id, person_id, role)
) STRICT;

CREATE TABLE publication_openalex (
    publication_id TEXT PRIMARY KEY REFERENCES publication(publication_id),
    openalex_id TEXT UNIQUE,
    openalex_doi TEXT,
    source_title TEXT NOT NULL,
    source_year INTEGER,
    openalex_title TEXT,
    openalex_year INTEGER,
    title_similarity REAL,
    year_difference INTEGER,
    match_status TEXT NOT NULL,
    cited_by_count INTEGER CHECK (cited_by_count >= 0),
    source_updated_at TEXT,
    retrieved_at TEXT NOT NULL,
    google_scholar_url TEXT
) STRICT;

CREATE TABLE publication_openalex_year (
    publication_id TEXT NOT NULL REFERENCES publication_openalex(publication_id),
    year INTEGER NOT NULL,
    cited_by_count INTEGER NOT NULL CHECK (cited_by_count >= 0),
    PRIMARY KEY (publication_id, year)
) STRICT;

CREATE TABLE load_audit (
    record_id TEXT NOT NULL,
    item_type TEXT NOT NULL,
    source_count INTEGER NOT NULL,
    loaded_count INTEGER NOT NULL,
    PRIMARY KEY (record_id, item_type)
) STRICT;

CREATE INDEX publication_doi_index ON publication(doi);
CREATE INDEX publication_pmid_index ON publication(pmid);
CREATE INDEX study_publication_index ON study(publication_id);
CREATE INDEX study_family_index ON study(primary_research_family);
CREATE INDEX item_study_type_index ON item(study_id, type);
CREATE INDEX item_part_index ON item(part_item_id);
CREATE INDEX purpose_value_index ON purpose(value);
CREATE INDEX design_axis_value_index ON design(axis, value);
CREATE INDEX registry_use_identity_index ON registry_use(registry_id);
CREATE INDEX registry_use_type_context_function_index
    ON registry_use(use_type, context, function);
CREATE INDEX finding_study_index ON item(study_id) WHERE type = 'Finding';
CREATE INDEX citation_target_index ON citation_occurrence(target_publication_id);
CREATE INDEX project_publication_publication_index
    ON project_publication(publication_id);
CREATE INDEX person_name_normal_index ON person_name(name);
CREATE INDEX publication_author_person_index ON publication_author(person_id);
CREATE INDEX project_person_person_index ON project_person(person_id);
CREATE INDEX publication_openalex_citations_index ON publication_openalex(cited_by_count);

CREATE VIEW study_primary_family AS
SELECT study_id, publication_id, primary_research_family
FROM study;

CREATE VIEW study_registry_presence AS
SELECT DISTINCT i.study_id, u.use_type, u.registry_id
FROM registry_use AS u
JOIN item AS i USING (item_id)
WHERE u.registry_id IS NOT NULL;

CREATE VIEW study_geography AS
SELECT DISTINCT i.study_id, t.value AS geography
FROM item_text_value AS t
JOIN item AS i USING (item_id)
WHERE t.value_type = 'POPULATION_GEOGRAPHY';

CREATE VIEW study_design_effective AS
SELECT
    p.study_id,
    p.item_id AS part_item_id,
    d.axis,
    d.value,
    CASE WHEN d.part_item_id IS NULL THEN 'STUDY_DEFAULT' ELSE 'PART_VALUE' END AS source_scope
FROM study_part AS p
JOIN design AS d
  ON d.study_id = p.study_id
 AND (
      d.part_item_id = p.item_id
      OR (
          d.part_item_id IS NULL
          AND NOT EXISTS (
              SELECT 1
              FROM design AS local
              WHERE local.study_id = p.study_id
                AND local.part_item_id = p.item_id
                AND local.axis = d.axis
          )
      )
 );

CREATE VIEW citation_edge AS
SELECT DISTINCT publication_id AS source_publication_id, target_publication_id
FROM citation_occurrence
WHERE resolution_status = 'resolved' AND target_publication_id IS NOT NULL;
