PRAGMA foreign_keys = ON;

-- These context tables are preloaded and read-only for the agent.
CREATE TABLE paper_context (
    record_id TEXT PRIMARY KEY,
    publication_form TEXT NOT NULL,
    source_marker TEXT NOT NULL
) STRICT;

CREATE TABLE candidate_project (
    project_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    abstract TEXT,
    principal_investigator TEXT,
    working_group TEXT,
    start_year INTEGER,
    end_year INTEGER,
    status TEXT
) STRICT;

CREATE TABLE controlled_value (
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    definition TEXT NOT NULL,
    PRIMARY KEY (key, value)
) STRICT;

CREATE TABLE registry_identity (
    entity_type TEXT NOT NULL,
    canonical_name TEXT NOT NULL,
    PRIMARY KEY (entity_type, canonical_name)
) STRICT;

CREATE TABLE registry_alias (
    entity_type TEXT NOT NULL,
    alias TEXT NOT NULL,
    canonical_name TEXT NOT NULL,
    PRIMARY KEY (entity_type, alias, canonical_name)
) STRICT;

-- Write one eligibility row for an included paper. Use reject for an excluded paper.
CREATE TABLE eligibility (
    basis TEXT PRIMARY KEY CHECK (basis IN ('EXPLICIT_SUPPORT', 'PROJECT_OUTPUT', 'BOTH')),
    reason TEXT NOT NULL,
    support_scope TEXT
) STRICT;

CREATE TABLE project_link (
    project_id TEXT PRIMARY KEY REFERENCES candidate_project(project_id)
) STRICT;

CREATE TABLE study (
    study_id TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    primary_research_family TEXT NOT NULL, -- controlled: primary_research_family
    execution_state TEXT NOT NULL,         -- controlled: execution_state
    result_state TEXT NOT NULL,            -- controlled: result_state
    family_rationale TEXT NOT NULL
) STRICT;

CREATE TABLE purpose (
    purpose_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    value TEXT NOT NULL, -- controlled: research_purpose
    rank INTEGER NOT NULL CHECK (rank > 0),
    UNIQUE (study_id, rank)
) STRICT;

CREATE TABLE study_part (
    part_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES study(study_id),
    label TEXT NOT NULL
) STRICT;

CREATE TABLE design (
    design_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    axis TEXT NOT NULL,  -- one design key from controlled_value
    value TEXT NOT NULL  -- a value for that key
) STRICT;

CREATE TABLE population (
    population_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    label TEXT NOT NULL,
    role TEXT,
    age_description TEXT,
    inclusion_description TEXT
) STRICT;

CREATE TABLE sample (
    sample_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    population_id TEXT REFERENCES population(population_id),
    stage TEXT NOT NULL, -- controlled: sample_stage
    size INTEGER CHECK (size >= 0),
    size_text TEXT,
    unit TEXT,
    description TEXT
) STRICT;

CREATE TABLE data_use (
    data_use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    origin TEXT NOT NULL, -- controlled: data_origin
    level TEXT NOT NULL,  -- controlled: data_level
    purpose TEXT
) STRICT;

CREATE TABLE instrument_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL,  -- controlled: use_context
    function TEXT NOT NULL  -- controlled: instrument_function
) STRICT;

CREATE TABLE method_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL, -- controlled: use_context
    function TEXT NOT NULL -- controlled: method_function
) STRICT;

CREATE TABLE protocol_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL, -- controlled: use_context
    function TEXT NOT NULL -- controlled: protocol_function
) STRICT;

CREATE TABLE model_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL,       -- controlled: use_context
    function TEXT NOT NULL,      -- controlled: model_function
    analytic_role TEXT NOT NULL  -- controlled: analytic_role
) STRICT;

CREATE TABLE software_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL, -- controlled: use_context
    function TEXT NOT NULL -- controlled: software_function
) STRICT;

CREATE TABLE product_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    context TEXT NOT NULL, -- controlled: use_context
    function TEXT NOT NULL -- controlled: product_function
) STRICT;

CREATE TABLE scoring_use (
    use_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    instrument_use_id TEXT NOT NULL REFERENCES instrument_use(use_id),
    product_id TEXT,
    context TEXT NOT NULL -- controlled: use_context; name resolves as Product
) STRICT;

CREATE TABLE task_design (
    task_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
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
    factor_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    label TEXT NOT NULL,
    role TEXT NOT NULL -- controlled: factor_role
) STRICT;

CREATE TABLE administration (
    administration_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
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
    involvement_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    stakeholder_group TEXT NOT NULL,
    activity TEXT NOT NULL,
    stage TEXT,
    role TEXT,
    influence TEXT NOT NULL
) STRICT;

CREATE TABLE outcome (
    outcome_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    family TEXT NOT NULL, -- controlled: outcome_family
    label TEXT NOT NULL
) STRICT;

CREATE TABLE finding (
    finding_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE finding_value (
    finding_id TEXT NOT NULL REFERENCES finding(finding_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    reported_value TEXT NOT NULL,
    unit TEXT,
    denominator TEXT,
    time TEXT,
    subgroup TEXT,
    comparator TEXT,
    direction TEXT,
    uncertainty TEXT,
    PRIMARY KEY (finding_id, ordinal)
) STRICT;

CREATE TABLE interpretation (
    interpretation_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE limitation (
    limitation_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    statement TEXT NOT NULL
) STRICT;

CREATE TABLE product (
    product_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    label TEXT NOT NULL,
    product_type TEXT NOT NULL -- controlled: product_type
) STRICT;

CREATE TABLE product_state (
    state_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    product_id TEXT NOT NULL REFERENCES product(product_id),
    axis TEXT NOT NULL CHECK (axis IN ('DEVELOPMENT', 'APPROVAL', 'VALIDATION', 'DEPLOYMENT', 'WITHDRAWAL')),
    exact_state TEXT NOT NULL,
    assertion_date TEXT,
    asserted_by TEXT
) STRICT;

CREATE TABLE concept (
    concept_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    name TEXT NOT NULL,
    description TEXT
) STRICT;

CREATE TABLE gap (
    gap_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    state TEXT NOT NULL, -- controlled: gap_state
    affected_item_id TEXT,
    affected_type TEXT NOT NULL,
    affected_key TEXT NOT NULL,
    evidence TEXT NOT NULL,
    importance TEXT NOT NULL,
    proposed_resolution TEXT NOT NULL
) STRICT;

CREATE TABLE source_conflict (
    conflict_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    scope TEXT NOT NULL
) STRICT;

CREATE TABLE conflict_statement (
    conflict_id TEXT NOT NULL REFERENCES source_conflict(conflict_id),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    statement TEXT NOT NULL,
    PRIMARY KEY (conflict_id, ordinal)
) STRICT;

CREATE TABLE publication_status (
    status_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES study(study_id),
    part_id TEXT REFERENCES study_part(part_id),
    status TEXT NOT NULL, -- controlled: publication_status
    exact_term TEXT NOT NULL,
    assertion_date TEXT,
    asserted_by TEXT,
    reason TEXT,
    notice_doi TEXT
) STRICT;

-- Repeated text values and graph links stay flat in these two tables.
CREATE TABLE item_term (
    item_id TEXT NOT NULL,
    field TEXT NOT NULL CHECK (field IN ('GEOGRAPHY', 'CONDITION', 'PROFILE', 'ATTRIBUTE', 'LEVEL', 'FACTOR_LEVEL')),
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    value TEXT NOT NULL,
    PRIMARY KEY (item_id, field, ordinal)
) STRICT;

CREATE TABLE item_relation (
    source_item_id TEXT NOT NULL,
    predicate TEXT NOT NULL CHECK (predicate IN ('APPLIES_TO', 'MEASURED_WITH', 'ABOUT', 'INTERPRETS', 'SCORES', 'USES_PRODUCT', 'ASSERTS_STATE_OF', 'AFFECTS')),
    target_item_id TEXT NOT NULL,
    ordinal INTEGER NOT NULL CHECK (ordinal > 0),
    PRIMARY KEY (source_item_id, predicate, target_item_id)
) STRICT;

-- Use these tables only when an existing controlled value or identity does not fit.
CREATE TABLE enum_extension (
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    definition TEXT NOT NULL,
    PRIMARY KEY (key, value)
) STRICT;

CREATE TABLE registry_extension (
    entity_type TEXT NOT NULL CHECK (entity_type IN ('Instrument', 'Method', 'Protocol', 'Model', 'Software', 'Product', 'Concept')),
    name TEXT NOT NULL,
    PRIMARY KEY (entity_type, name)
) STRICT;

CREATE TABLE registry_alias_extension (
    entity_type TEXT NOT NULL CHECK (entity_type IN ('Instrument', 'Method', 'Protocol', 'Model', 'Software', 'Product', 'Concept')),
    alias TEXT NOT NULL,
    canonical_name TEXT NOT NULL,
    PRIMARY KEY (entity_type, alias)
) STRICT;
