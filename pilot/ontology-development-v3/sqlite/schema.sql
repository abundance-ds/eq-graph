PRAGMA foreign_keys = ON;

CREATE TABLE publication (
    publication_id TEXT PRIMARY KEY,
    doi TEXT NOT NULL UNIQUE,
    pmid TEXT,
    pmcid TEXT,
    title TEXT NOT NULL,
    abstract TEXT,
    journal TEXT,
    publisher TEXT,
    article_type TEXT,
    language TEXT,
    volume TEXT,
    issue TEXT,
    article_number TEXT,
    licence_url TEXT,
    open_access INTEGER NOT NULL DEFAULT 0 CHECK (open_access IN (0, 1)),
    canonical_url TEXT NOT NULL,
    source_path TEXT NOT NULL,
    source_sha256 TEXT NOT NULL,
    source_bytes INTEGER NOT NULL CHECK (source_bytes > 0),
    metadata_status TEXT NOT NULL DEFAULT 'parsed'
        CHECK (metadata_status IN ('parsed', 'partial', 'conflict')),
    lifecycle_status TEXT NOT NULL DEFAULT 'active'
        CHECK (lifecycle_status IN ('active', 'retracted', 'correction-notice', 'withdrawn'))
) STRICT;

CREATE TABLE publication_relation (
    source_publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    target_publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    relation_type TEXT NOT NULL
        CHECK (relation_type IN ('corrects', 'retracts', 'updates', 'supplements', 'reports-same-study')),
    effective_date TEXT,
    source_locator TEXT NOT NULL,
    PRIMARY KEY (source_publication_id, target_publication_id, relation_type)
) STRICT;

CREATE TABLE publication_date (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    date_type TEXT NOT NULL,
    date_value TEXT NOT NULL,
    PRIMARY KEY (publication_id, date_type, date_value)
) STRICT;

CREATE TABLE publication_url (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    url_type TEXT NOT NULL,
    url TEXT NOT NULL,
    PRIMARY KEY (publication_id, url_type, url)
) STRICT;

CREATE TABLE author (
    author_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    family_name TEXT,
    given_names TEXT,
    orcid TEXT
) STRICT;

CREATE TABLE publication_author (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    author_id TEXT NOT NULL REFERENCES author(author_id),
    author_order INTEGER NOT NULL CHECK (author_order > 0),
    corresponding INTEGER NOT NULL DEFAULT 0 CHECK (corresponding IN (0, 1)),
    email TEXT,
    roles TEXT,
    PRIMARY KEY (publication_id, author_order),
    UNIQUE (publication_id, author_id)
) STRICT;

CREATE TABLE publication_correspondence (
    correspondence_id INTEGER PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    label TEXT,
    correspondence_text TEXT NOT NULL,
    email TEXT
) STRICT;

CREATE TABLE affiliation (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    affiliation_id TEXT NOT NULL,
    name TEXT NOT NULL,
    ror TEXT,
    grid TEXT,
    isni TEXT,
    PRIMARY KEY (publication_id, affiliation_id)
) STRICT;

CREATE TABLE author_affiliation (
    publication_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    affiliation_id TEXT NOT NULL,
    PRIMARY KEY (publication_id, author_id, affiliation_id),
    FOREIGN KEY (publication_id, author_id)
        REFERENCES publication_author(publication_id, author_id) ON DELETE CASCADE,
    FOREIGN KEY (publication_id, affiliation_id)
        REFERENCES affiliation(publication_id, affiliation_id) ON DELETE CASCADE
) STRICT;

CREATE TABLE publication_keyword (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    keyword TEXT NOT NULL,
    PRIMARY KEY (publication_id, keyword)
) STRICT;

CREATE TABLE publication_category (
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    category_type TEXT NOT NULL,
    category TEXT NOT NULL,
    PRIMARY KEY (publication_id, category_type, category)
) STRICT;

CREATE TABLE publication_funding (
    funding_id INTEGER PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    funder TEXT,
    award_id TEXT,
    recipient TEXT,
    source_text TEXT,
    source_locator TEXT NOT NULL
) STRICT;

CREATE TABLE publication_reference (
    reference_id INTEGER PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id) ON DELETE CASCADE,
    source_reference_id TEXT,
    citation_text TEXT,
    doi TEXT,
    pmid TEXT
) STRICT;

CREATE TABLE project (
    project_id TEXT PRIMARY KEY,
    title TEXT
) STRICT;

CREATE TABLE project_publication (
    project_id TEXT NOT NULL REFERENCES project(project_id),
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    link_status TEXT NOT NULL
        CHECK (link_status IN ('accepted', 'candidate', 'rejected', 'superseded')),
    support_type TEXT,
    evidence_class TEXT NOT NULL,
    evidence_locator TEXT NOT NULL,
    note TEXT,
    PRIMARY KEY (project_id, publication_id)
) STRICT;

CREATE TABLE study (
    study_id TEXT PRIMARY KEY,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    title TEXT NOT NULL,
    eq_instrument_status TEXT NOT NULL
        CHECK (eq_instrument_status IN ('used', 'mentioned-only', 'none-reported', 'not-checked')),
    record_path TEXT NOT NULL,
    review_status TEXT NOT NULL
        CHECK (review_status IN ('source-checked', 'pilot-extracted', 'boundary-only')),
    execution_status TEXT NOT NULL DEFAULT 'completed'
        CHECK (execution_status IN ('planned', 'in-progress', 'completed', 'not-applicable'))
) STRICT;

CREATE TABLE study_publication (
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    publication_id TEXT NOT NULL REFERENCES publication(publication_id),
    relation_role TEXT NOT NULL,
    source_locator TEXT NOT NULL,
    PRIMARY KEY (study_id, publication_id, relation_role)
) STRICT;

CREATE TABLE study_classification (
    classification_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    classification_type TEXT NOT NULL
        CHECK (classification_type IN ('research-purpose', 'study-design')),
    preferred_label TEXT NOT NULL,
    source_label TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, classification_type, preferred_label)
) STRICT;

CREATE TABLE study_concept (
    concept_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    preferred_label TEXT NOT NULL,
    source_term TEXT,
    broader_label TEXT,
    review_status TEXT NOT NULL DEFAULT 'accepted'
        CHECK (review_status IN ('candidate', 'accepted', 'rejected')),
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, preferred_label)
) STRICT;

CREATE TABLE population (
    population_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    label TEXT NOT NULL,
    role TEXT NOT NULL,
    country_or_region TEXT,
    age_text TEXT,
    condition_text TEXT,
    source_locator TEXT NOT NULL
) STRICT;

CREATE TABLE sample (
    sample_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    label TEXT NOT NULL,
    count_value INTEGER,
    count_status TEXT NOT NULL,
    source_locator TEXT NOT NULL
) STRICT;

CREATE TABLE input_dataset (
    input_dataset_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    label TEXT NOT NULL,
    collection_period TEXT,
    recruitment_source TEXT,
    source_count INTEGER,
    analytic_contribution_count INTEGER,
    harmonization_rule TEXT,
    details TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, label)
) STRICT;

CREATE TABLE instrument (
    instrument_id TEXT PRIMARY KEY,
    preferred_label TEXT NOT NULL UNIQUE,
    family TEXT,
    version TEXT,
    form TEXT
) STRICT;

CREATE TABLE instrument_use (
    instrument_use_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    instrument_id TEXT NOT NULL REFERENCES instrument(instrument_id),
    role TEXT NOT NULL,
    source_label TEXT,
    language TEXT,
    scoring_source TEXT,
    details TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, instrument_id, role)
) STRICT;

CREATE TABLE administration (
    administration_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    instrument_id TEXT REFERENCES instrument(instrument_id),
    respondent TEXT,
    perspective TEXT,
    interaction TEXT,
    channel TEXT,
    setting TEXT,
    language TEXT,
    recall_period TEXT,
    timepoint TEXT,
    details TEXT,
    source_locator TEXT NOT NULL
) STRICT;

CREATE TABLE measurement_time (
    measurement_time_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    instrument_id TEXT REFERENCES instrument(instrument_id),
    time_role TEXT NOT NULL
        CHECK (time_role IN ('report-time', 'reference-time', 'valuation-duration', 'recall-period')),
    time_label TEXT NOT NULL,
    sequence INTEGER,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, instrument_id, time_role, time_label)
) STRICT;

CREATE TABLE research_method (
    method_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    preferred_label TEXT NOT NULL,
    source_label TEXT,
    method_family TEXT,
    role TEXT,
    protocol TEXT,
    task_details TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, preferred_label, role)
) STRICT;

CREATE TABLE statistical_model (
    model_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    preferred_label TEXT NOT NULL,
    source_label TEXT,
    model_family TEXT,
    role TEXT NOT NULL,
    analysis_purpose TEXT,
    qualifiers TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, preferred_label, role)
) STRICT;

CREATE TABLE research_product (
    product_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    label TEXT NOT NULL,
    product_type TEXT NOT NULL,
    status TEXT,
    target_instrument TEXT,
    jurisdiction TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, label)
) STRICT;

CREATE TABLE derivation_step (
    derivation_step_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    sequence INTEGER NOT NULL CHECK (sequence > 0),
    input_label TEXT NOT NULL,
    transformation TEXT NOT NULL,
    output_label TEXT NOT NULL,
    uncertainty_added TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, sequence)
) STRICT;

CREATE TABLE study_outcome (
    outcome_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    preferred_label TEXT NOT NULL,
    outcome_type TEXT,
    source_label TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, preferred_label)
) STRICT;

CREATE TABLE finding (
    finding_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    sequence INTEGER NOT NULL CHECK (sequence > 0),
    statement TEXT NOT NULL,
    finding_type TEXT,
    direction TEXT,
    interpretation TEXT,
    population_context TEXT,
    instrument_context TEXT,
    method_context TEXT,
    outcome_context TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, sequence)
) STRICT;

CREATE TABLE limitation (
    limitation_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    sequence INTEGER NOT NULL CHECK (sequence > 0),
    statement TEXT NOT NULL,
    applies_to TEXT,
    source_locator TEXT NOT NULL,
    UNIQUE (study_id, sequence)
) STRICT;

CREATE TABLE source_conflict (
    conflict_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    fact_name TEXT NOT NULL,
    value_a TEXT NOT NULL,
    source_a TEXT NOT NULL,
    value_b TEXT NOT NULL,
    source_b TEXT NOT NULL,
    resolution TEXT
) STRICT;

CREATE TABLE review_evidence_unit (
    review_unit_id INTEGER PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id) ON DELETE CASCADE,
    unit_type TEXT NOT NULL,
    source_publication_text TEXT,
    instrument_text TEXT,
    population_text TEXT,
    property_text TEXT,
    result_text TEXT,
    quality_rating TEXT,
    source_locator TEXT NOT NULL
) STRICT;

CREATE INDEX publication_doi_index ON publication(doi);
CREATE INDEX project_publication_status_index ON project_publication(link_status);
CREATE INDEX classification_label_index ON study_classification(preferred_label);
CREATE INDEX concept_label_index ON study_concept(preferred_label);
CREATE INDEX instrument_label_index ON instrument(preferred_label);
CREATE INDEX instrument_use_role_index ON instrument_use(role);
CREATE INDEX method_label_index ON research_method(preferred_label);
CREATE INDEX model_label_index ON statistical_model(preferred_label);
CREATE INDEX product_type_index ON research_product(product_type);
CREATE INDEX finding_type_index ON finding(finding_type);
CREATE INDEX publication_lifecycle_index ON publication(lifecycle_status);
CREATE INDEX publication_relation_type_index ON publication_relation(relation_type);
CREATE INDEX study_execution_status_index ON study(execution_status);
CREATE INDEX study_publication_role_index ON study_publication(relation_role);

CREATE VIEW accepted_funded_publication AS
SELECT
    pp.project_id,
    pp.support_type,
    p.publication_id,
    p.doi,
    p.title
FROM project_publication AS pp
JOIN publication AS p USING (publication_id)
WHERE pp.link_status = 'accepted';

CREATE VIEW study_search_term AS
SELECT study_id, 'research-purpose' AS term_type, preferred_label AS term FROM study_classification WHERE classification_type = 'research-purpose'
UNION ALL
SELECT study_id, 'study-design', preferred_label FROM study_classification WHERE classification_type = 'study-design'
UNION ALL
SELECT study_id, 'concept', preferred_label FROM study_concept WHERE review_status = 'accepted'
UNION ALL
SELECT iu.study_id, 'instrument', i.preferred_label FROM instrument_use AS iu JOIN instrument AS i USING (instrument_id)
UNION ALL
SELECT study_id, 'method', preferred_label FROM research_method
UNION ALL
SELECT study_id, 'model', preferred_label FROM statistical_model
UNION ALL
SELECT study_id, 'product', label FROM research_product
UNION ALL
SELECT study_id, 'outcome', preferred_label FROM study_outcome;
