#!/usr/bin/env python3
"""Build the public serving database from the typed research database."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
from pathlib import Path

from build_serving_database import COUNTRY_PATTERNS, SCHEMA, countries_from


TYPED_SCHEMA = """
CREATE TABLE registry_entities (
    registry_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    canonical_label TEXT NOT NULL,
    parent_registry_id TEXT,
    applies_to_registry_id TEXT,
    variant_kind TEXT,
    language_code TEXT,
    jurisdiction TEXT,
    version TEXT,
    respondent_form TEXT,
    source_identifier TEXT,
    scope TEXT NOT NULL
) STRICT;

CREATE TABLE study_parts (
    part_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    label TEXT NOT NULL
) STRICT;

CREATE TABLE design_axes (
    design_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    axis TEXT NOT NULL,
    value TEXT NOT NULL
) STRICT;

CREATE TABLE scientific_uses (
    use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    use_type TEXT NOT NULL,
    source_label TEXT NOT NULL,
    canonical_label TEXT,
    registry_id TEXT REFERENCES registry_entities(registry_id),
    context TEXT NOT NULL,
    function TEXT NOT NULL,
    analytic_role TEXT,
    details_json TEXT NOT NULL CHECK (json_valid(details_json))
) STRICT;

CREATE TABLE scoring_uses (
    scoring_use_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    source_label TEXT NOT NULL,
    registry_id TEXT,
    context TEXT NOT NULL,
    instrument_use_id TEXT NOT NULL REFERENCES scientific_uses(use_id),
    product_id TEXT,
    details_json TEXT NOT NULL CHECK (json_valid(details_json))
) STRICT;

CREATE TABLE administrations (
    administration_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
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

CREATE TABLE administration_targets (
    administration_id TEXT NOT NULL REFERENCES administrations(administration_id),
    target_use_id TEXT NOT NULL,
    PRIMARY KEY (administration_id, target_use_id)
) STRICT;

CREATE TABLE task_designs (
    task_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    label TEXT NOT NULL,
    duration TEXT,
    alternatives TEXT,
    task_count TEXT,
    block TEXT,
    task_order TEXT,
    randomization_unit TEXT,
    stopping_rule TEXT,
    profiles_json TEXT NOT NULL CHECK (json_valid(profiles_json)),
    attributes_json TEXT NOT NULL CHECK (json_valid(attributes_json)),
    levels_json TEXT NOT NULL CHECK (json_valid(levels_json)),
    targets_json TEXT NOT NULL CHECK (json_valid(targets_json))
) STRICT;

CREATE TABLE study_factors (
    factor_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    label TEXT NOT NULL,
    role TEXT NOT NULL,
    levels_json TEXT NOT NULL CHECK (json_valid(levels_json))
) STRICT;

CREATE TABLE stakeholder_involvements (
    involvement_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    part_id TEXT REFERENCES study_parts(part_id),
    stakeholder_group TEXT NOT NULL,
    activity TEXT NOT NULL,
    stage TEXT,
    role TEXT,
    influence TEXT NOT NULL
) STRICT;

CREATE TABLE outcome_details (
    outcome_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL,
    family TEXT NOT NULL,
    label TEXT NOT NULL,
    instrument_use_ids_json TEXT NOT NULL CHECK (json_valid(instrument_use_ids_json)),
    FOREIGN KEY (study_id, outcome_id) REFERENCES outcomes(study_id, outcome_id)
) STRICT;

CREATE TABLE finding_values (
    finding_id TEXT NOT NULL REFERENCES findings(finding_id),
    ordinal INTEGER NOT NULL,
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

CREATE TABLE interpretations (
    interpretation_id TEXT PRIMARY KEY,
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    publication_id TEXT NOT NULL REFERENCES publications(publication_id),
    statement TEXT NOT NULL,
    finding_ids_json TEXT NOT NULL CHECK (json_valid(finding_ids_json))
) STRICT;

CREATE TABLE product_uses (
    product_use_id TEXT PRIMARY KEY REFERENCES scientific_uses(use_id),
    study_id TEXT NOT NULL REFERENCES studies(study_id),
    product TEXT NOT NULL,
    context TEXT NOT NULL,
    function TEXT NOT NULL,
    analytic_role TEXT
) STRICT;

CREATE TABLE product_states (
    state_id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL REFERENCES research_products(product_id),
    axis TEXT NOT NULL,
    exact_state TEXT NOT NULL,
    assertion_date TEXT,
    asserted_by TEXT
) STRICT;

CREATE TABLE extraction_gaps (
    gap_id TEXT PRIMARY KEY,
    study_id TEXT REFERENCES studies(study_id),
    state TEXT NOT NULL,
    affected_type TEXT NOT NULL,
    affected_key TEXT NOT NULL,
    importance TEXT NOT NULL,
    proposed_resolution TEXT NOT NULL
) STRICT;

CREATE INDEX design_axes_study_axis_index ON design_axes(study_id, axis, value);
CREATE INDEX scientific_uses_type_function_index
    ON scientific_uses(use_type, context, function);
CREATE INDEX scientific_uses_registry_index ON scientific_uses(registry_id);
CREATE INDEX registry_entities_type_scope_index
    ON registry_entities(entity_type, scope, canonical_label);
CREATE INDEX administrations_study_index ON administrations(study_id);
CREATE INDEX task_designs_study_index ON task_designs(study_id);
CREATE INDEX finding_values_finding_index ON finding_values(finding_id);
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def json_array(connection: sqlite3.Connection, sql: str, parameters: tuple[str, ...]) -> str:
    return json.dumps(
        [row[0] for row in connection.execute(sql, parameters)],
        ensure_ascii=False,
        separators=(",", ":"),
    )


def build(source: Path, output: Path) -> dict[str, int]:
    if not source.is_file():
        raise SystemExit(f"Source database does not exist: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent
    )
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        connection = sqlite3.connect(temporary)
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(SCHEMA)
        connection.executescript(TYPED_SCHEMA)
        connection.execute("ATTACH DATABASE ? AS src", (str(source.resolve()),))
        connection.execute("BEGIN")

        publication_count = connection.execute(
            "SELECT COUNT(*) FROM src.publication"
        ).fetchone()[0]
        study_count = connection.execute("SELECT COUNT(*) FROM src.study").fetchone()[0]
        project_count = connection.execute("SELECT COUNT(*) FROM src.project").fetchone()[0]
        connection.executemany(
            "INSERT INTO metadata(key,value) VALUES (?,?)",
            (
                ("dataset", "EQ-Graph typed public research serving database"),
                ("scope", f"{project_count} projects and {publication_count} publications"),
                ("source_database_sha256", sha256(source)),
                ("ontology_version", "0.13"),
                ("project_link_policy", "accepted links only"),
                ("citation_policy", "OpenAlex citation snapshots are included; reference lists remain private"),
                ("full_text_policy", "full text remains outside the serving database"),
            ),
        )

        connection.execute(
            """
            INSERT INTO projects
            SELECT project_id, title, abstract, principal_investigator,
                   working_group, start_year, end_year, status, approved_budget_eur
            FROM src.project
            """
        )
        connection.execute(
            """
            INSERT INTO publications
            SELECT
                p.publication_id, p.title, p.doi, p.pmid, p.pmcid,
                p.publication_year,
                (SELECT d.date_value FROM src.publication_date AS d
                 WHERE d.publication_id=p.publication_id
                 ORDER BY CASE d.date_type
                    WHEN 'ppub' THEN 1 WHEN 'epub' THEN 2 WHEN 'published' THEN 3
                    WHEN 'accepted' THEN 4 ELSE 5 END, d.date_value LIMIT 1),
                p.journal, p.publisher, p.volume, p.issue, p.article_number,
                p.jats_article_type, p.language,
                (SELECT group_concat(k.keyword, ' | ') FROM src.publication_keyword AS k
                 WHERE k.publication_id=p.publication_id),
                (SELECT group_concat(COALESCE(f.source_text, f.funder), ' | ')
                 FROM src.publication_funding AS f
                 WHERE f.publication_id=p.publication_id),
                p.abstract, p.canonical_url, p.licence_url, p.open_access,
                p.assessment_disposition, p.euroqol_connection, p.euroqol_support,
                p.support_scope,
                CASE sr.source_format
                    WHEN 'JATS_XML' THEN 'JATS'
                    ELSE sr.source_format
                END
            FROM src.publication AS p
            JOIN src.source_record AS sr USING (record_id)
            """
        )
        connection.execute(
            """
            INSERT INTO studies
            SELECT s.study_id, s.publication_id, s.label,
                   ROW_NUMBER() OVER (
                     PARTITION BY s.publication_id ORDER BY s.study_id
                   ),
                   s.execution_state, s.result_state
            FROM src.study AS s
            """
        )
        connection.execute(
            """
            INSERT INTO project_publications
            SELECT project_id, publication_id, project_output, support_target, support_scope
            FROM src.project_publication
            """
        )
        connection.execute(
            """
            INSERT INTO people
            SELECT person_id, display_name, family_name, given_names, orcid,
                   openalex_id, entity_kind, identity_status
            FROM src.person
            """
        )
        connection.execute(
            """
            INSERT INTO person_names
            SELECT DISTINCT person_id, name, name_type FROM src.person_name
            """
        )
        connection.execute(
            """
            INSERT INTO person_identifiers
            SELECT person_id, scheme, value FROM src.person_identifier
            """
        )
        connection.execute(
            """
            INSERT INTO euroqol_memberships
            SELECT person_id, member_id, affiliation, profile_url,
                   observed_date, status
            FROM src.euroqol_membership
            """
        )
        connection.execute(
            """
            INSERT INTO project_people
            SELECT project_id, person_id, role FROM src.project_person
            """
        )
        connection.execute(
            """
            INSERT INTO publication_authors
            SELECT pa.publication_id, pa.person_id, pa.display_name,
                   pa.author_order, pa.corresponding, p.orcid,
                   pa.resolution_method, pa.resolution_status
            FROM src.publication_author AS pa
            JOIN src.person AS p USING (person_id)
            """
        )
        connection.execute(
            """
            INSERT INTO author_affiliations
            SELECT aa.publication_id, aa.person_id, a.name
            FROM src.author_affiliation AS aa
            JOIN src.affiliation AS a USING (affiliation_id)
            """
        )
        connection.execute(
            """
            INSERT INTO publication_citations
            SELECT publication_id, 'OPENALEX', openalex_id, cited_by_count,
                   retrieved_at, source_updated_at, match_status
            FROM src.publication_openalex
            """
        )
        connection.execute(
            """
            INSERT INTO publication_citation_years
            SELECT publication_id, 'OPENALEX', year, cited_by_count
            FROM src.publication_openalex_year
            """
        )
        connection.execute(
            """
            INSERT INTO study_types
            SELECT study_id, primary_research_family, execution_state FROM src.study
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO research_purposes
            SELECT p.study_id, p.value
            FROM src.purpose AS p
            ORDER BY p.study_id, p.rank
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO study_designs
            SELECT d.study_id, d.axis || ':' || d.value
            FROM src.design AS d
            """
        )

        connection.execute(
            """
            INSERT INTO registry_entities
            SELECT registry_id, entity_type, canonical_label,
                   parent_registry_id, applies_to_registry_id, variant_kind,
                   language_code, jurisdiction, version, respondent_form,
                   source_identifier, scope
            FROM src.registry_identity
            """
        )

        connection.execute(
            """
            INSERT INTO study_parts
            SELECT p.item_id, p.study_id, p.label FROM src.study_part AS p
            """
        )
        connection.execute(
            """
            INSERT INTO design_axes
            SELECT d.item_id, d.study_id, d.part_item_id, d.axis, d.value
            FROM src.design AS d
            """
        )

        population_rows = connection.execute(
            """
            SELECT i.item_id, i.study_id, p.label, p.role,
                   p.age_description, p.inclusion_description
            FROM src.population AS p JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        ).fetchall()
        for item_id, study_id, label, role, age, inclusion in population_rows:
            geographies = [
                row[0]
                for row in connection.execute(
                    """
                    SELECT value FROM src.item_text_value
                    WHERE item_id=? AND value_type='POPULATION_GEOGRAPHY'
                    ORDER BY ordinal
                    """,
                    (item_id,),
                )
            ]
            conditions = [
                row[0]
                for row in connection.execute(
                    """
                    SELECT value FROM src.item_text_value
                    WHERE item_id=? AND value_type='POPULATION_CONDITION'
                    ORDER BY ordinal
                    """,
                    (item_id,),
                )
            ]
            details = json.dumps(
                {
                    "population_id": item_id,
                    "age": age,
                    "inclusion": inclusion,
                    "conditions": conditions,
                    "geographies": geographies,
                },
                ensure_ascii=False,
                separators=(",", ":"),
            )
            connection.execute(
                "INSERT OR IGNORE INTO populations VALUES (?,?,?,?,?,?)",
                (study_id, label, role, " | ".join(geographies) or None, None, details),
            )
            for country in sorted(countries_from(*geographies)):
                connection.execute(
                    "INSERT OR IGNORE INTO study_countries VALUES (?,?)",
                    (study_id, country),
                )

        connection.execute(
            """
            INSERT INTO samples
            SELECT s.item_id, i.study_id,
                   COALESCE(s.description, s.stage), s.size, s.stage,
                   (SELECT group_concat(t.value, ' | ')
                    FROM src.item_text_value AS t
                    WHERE t.item_id=s.population_item_id
                      AND t.value_type='POPULATION_GEOGRAPHY'),
                   json_object(
                     'stage', s.stage, 'size_text', s.size_text,
                     'unit', s.unit, 'description', s.description,
                     'population_id', s.population_item_id,
                     'part_id', i.part_item_id
                   )
            FROM src.sample AS s JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )

        connection.execute(
            """
            INSERT INTO scientific_uses
            SELECT u.item_id, i.study_id, i.part_item_id, u.use_type,
                   u.source_label, r.canonical_label, u.registry_id,
                   u.context, u.function, u.analytic_role,
                   json_object(
                     'parent_registry_id', r.parent_registry_id,
                     'variant_kind', r.variant_kind,
                     'language', r.language_code,
                     'jurisdiction', r.jurisdiction,
                     'version', r.version,
                     'respondent_form', r.respondent_form,
                     'scope', r.scope
                   )
            FROM src.registry_use AS u
            JOIN src.item AS i USING (item_id)
            LEFT JOIN src.registry_identity AS r USING (registry_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO administrations
            SELECT a.item_id, i.study_id, i.part_item_id, a.respondent,
                   a.perspective, a.completion, a.assistance, a.channel,
                   a.setting, a.instrument_language, a.interview_language,
                   a.recall_period, a.time_point
            FROM src.administration AS a JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO administration_targets
            SELECT r.source_item_id, r.target_item_id
            FROM src.item_relation AS r
            JOIN src.item AS source ON source.item_id=r.source_item_id
            WHERE source.type='Administration' AND r.predicate='APPLIES_TO'
              AND (
                r.target_item_id IN (SELECT use_id FROM scientific_uses)
                OR r.target_item_id IN (SELECT item_id FROM src.task_design)
              )
            """
        )

        use_rows = connection.execute(
            """
            SELECT u.use_id, u.study_id, u.use_type,
                   u.canonical_label, u.source_label,
                   u.context, u.function, u.analytic_role, u.registry_id,
                   u.details_json
            FROM scientific_uses AS u
            JOIN registry_entities AS r USING (registry_id)
            WHERE r.scope='GLOBAL'
            ORDER BY use_id
            """
        ).fetchall()
        for (
            use_id,
            study_id,
            use_type,
            label,
            source_label,
            context,
            function,
            analytic_role,
            registry_id,
            registry_details,
        ) in use_rows:
            administrations = connection.execute(
                """
                SELECT a.respondent, a.perspective, a.completion, a.assistance,
                       a.channel, a.setting, a.instrument_language,
                       a.interview_language, a.recall_period, a.time_point
                FROM administration_targets AS t
                JOIN administrations AS a USING (administration_id)
                WHERE t.target_use_id=? ORDER BY a.administration_id
                """,
                (use_id,),
            ).fetchall()
            administration = administrations[0] if administrations else (None,) * 10
            details = json.dumps(
                {
                    "source_label": source_label,
                    "registry_id": registry_id,
                    "context": context,
                    "function": function,
                    "analytic_role": analytic_role,
                    "registry": json.loads(registry_details),
                    "administration_ids": [
                        row[0]
                        for row in connection.execute(
                            "SELECT administration_id FROM administration_targets WHERE target_use_id=? ORDER BY administration_id",
                            (use_id,),
                        )
                    ],
                },
                ensure_ascii=False,
                separators=(",", ":"),
            )
            registry = json.loads(registry_details)
            if use_type == "Instrument":
                connection.execute(
                    "INSERT INTO instrument_uses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        use_id,
                        study_id,
                        label,
                        function,
                        administration[6] or registry.get("language"),
                        registry.get("version"),
                        administration[2],
                        administration[0],
                        administration[1],
                        administration[8],
                        administration[4],
                        administration[5],
                        details,
                    ),
                )
            elif use_type == "Method":
                connection.execute(
                    "INSERT INTO method_uses VALUES (?,?,?,?,?,?,?,?,?)",
                    (
                        use_id,
                        study_id,
                        label,
                        function,
                        analytic_role,
                        None,
                        administration[4],
                        None,
                        details,
                    ),
                )
            elif use_type == "Model":
                connection.execute(
                    "INSERT INTO model_uses VALUES (?,?,?,?,?,?,?,?)",
                    (
                        use_id,
                        study_id,
                        label,
                        function,
                        analytic_role,
                        None,
                        None,
                        details,
                    ),
                )
            elif use_type == "Protocol":
                connection.execute(
                    "INSERT INTO protocols VALUES (?,?,?,?)",
                    (use_id, study_id, label, details),
                )

        connection.execute(
            """
            INSERT INTO scoring_uses
            SELECT s.item_id, i.study_id, i.part_item_id, s.source_label,
                   s.registry_id, s.context, s.instrument_use_item_id,
                   s.product_item_id,
                   json_object('registry_id', s.registry_id, 'context', s.context)
            FROM src.scoring_use AS s JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )

        task_rows = connection.execute(
            """
            SELECT t.item_id, i.study_id, i.part_item_id, t.label, t.duration,
                   t.alternatives, t.task_count, t.block, t.task_order,
                   t.randomization_unit, t.stopping_rule
            FROM src.task_design AS t JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY t.item_id
            """
        ).fetchall()
        for row in task_rows:
            task_id = row[0]
            values = {}
            for key, value_type in (
                ("profiles", "TASK_PROFILE"),
                ("attributes", "TASK_ATTRIBUTE"),
                ("levels", "TASK_LEVEL"),
            ):
                values[key] = json_array(
                    connection,
                    "SELECT value FROM src.item_text_value WHERE item_id=? AND value_type=? ORDER BY ordinal",
                    (task_id, value_type),
                )
            targets = json_array(
                connection,
                "SELECT target_item_id FROM src.item_relation WHERE source_item_id=? AND predicate='APPLIES_TO' ORDER BY ordinal",
                (task_id,),
            )
            connection.execute(
                "INSERT INTO task_designs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (*row, values["profiles"], values["attributes"], values["levels"], targets),
            )

        factor_rows = connection.execute(
            """
            SELECT f.item_id, i.study_id, i.part_item_id, f.label, f.role
            FROM src.study_factor AS f JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY f.item_id
            """
        ).fetchall()
        for row in factor_rows:
            levels = json_array(
                connection,
                "SELECT value FROM src.item_text_value WHERE item_id=? AND value_type='FACTOR_LEVEL' ORDER BY ordinal",
                (row[0],),
            )
            connection.execute("INSERT INTO study_factors VALUES (?,?,?,?,?,?)", (*row, levels))

        connection.execute(
            """
            INSERT INTO stakeholder_involvements
            SELECT s.item_id, i.study_id, i.part_item_id, s.stakeholder_group,
                   s.activity, s.stage, s.role, s.influence
            FROM src.stakeholder_involvement AS s JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO outcomes
            SELECT o.item_id, i.study_id, o.label
            FROM src.outcome AS o JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        outcome_rows = connection.execute(
            """
            SELECT o.item_id, i.study_id, o.family, o.label
            FROM src.outcome AS o JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY o.item_id
            """
        ).fetchall()
        for outcome_id, study_id, family, label in outcome_rows:
            instruments = json_array(
                connection,
                "SELECT target_item_id FROM src.item_relation WHERE source_item_id=? AND predicate='MEASURED_WITH' ORDER BY ordinal",
                (outcome_id,),
            )
            connection.execute(
                "INSERT INTO outcome_details VALUES (?,?,?,?,?)",
                (outcome_id, study_id, family, label, instruments),
            )

        finding_rows = connection.execute(
            """
            SELECT f.item_id, i.study_id, i.publication_id, f.statement
            FROM src.finding AS f JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY f.item_id
            """
        ).fetchall()
        for finding_id, study_id, publication_id, statement in finding_rows:
            about = [
                row[0]
                for row in connection.execute(
                    "SELECT target_item_id FROM src.item_relation WHERE source_item_id=? AND predicate='ABOUT' ORDER BY ordinal",
                    (finding_id,),
                )
            ]
            outcome = connection.execute(
                """
                SELECT o.label FROM src.item_relation AS r
                JOIN src.outcome AS o ON o.item_id=r.target_item_id
                WHERE r.source_item_id=? AND r.predicate='ABOUT'
                ORDER BY r.ordinal LIMIT 1
                """,
                (finding_id,),
            ).fetchone()
            details = json.dumps(
                {"about": about}, ensure_ascii=False, separators=(",", ":")
            )
            connection.execute(
                "INSERT INTO findings VALUES (?,?,?,?,?,?)",
                (
                    finding_id,
                    study_id,
                    publication_id,
                    statement,
                    outcome[0] if outcome else None,
                    details,
                ),
            )
        connection.execute(
            """
            INSERT INTO finding_values
            SELECT finding_item_id, ordinal, reported_value, unit, denominator,
                   time, subgroup, comparator, direction, uncertainty
            FROM src.finding_value
            WHERE finding_item_id IN (SELECT finding_id FROM findings)
            """
        )

        interpretation_rows = connection.execute(
            """
            SELECT x.item_id, i.study_id, i.publication_id, x.statement
            FROM src.interpretation AS x JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY x.item_id
            """
        ).fetchall()
        for interpretation_id, study_id, publication_id, statement in interpretation_rows:
            finding_ids = json_array(
                connection,
                "SELECT target_item_id FROM src.item_relation WHERE source_item_id=? AND predicate='INTERPRETS' ORDER BY ordinal",
                (interpretation_id,),
            )
            connection.execute(
                "INSERT INTO interpretations VALUES (?,?,?,?,?)",
                (interpretation_id, study_id, publication_id, statement, finding_ids),
            )

        limitation_rows = connection.execute(
            """
            SELECT l.item_id, i.study_id, i.publication_id, l.statement
            FROM src.limitation AS l JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL ORDER BY l.item_id
            """
        ).fetchall()
        for limitation_id, study_id, publication_id, statement in limitation_rows:
            about = json_array(
                connection,
                "SELECT target_item_id FROM src.item_relation WHERE source_item_id=? AND predicate='ABOUT' ORDER BY ordinal",
                (limitation_id,),
            )
            connection.execute(
                "INSERT INTO limitations VALUES (?,?,?,?,?,?,?)",
                (
                    limitation_id,
                    study_id,
                    publication_id,
                    statement,
                    None,
                    None,
                    json.dumps({"about": json.loads(about)}, separators=(",", ":")),
                ),
            )

        connection.execute(
            """
            INSERT INTO research_products
            SELECT p.item_id, i.study_id, p.label, p.product_type,
                   (SELECT group_concat(s.axis || ':' || s.exact_state, ' | ')
                    FROM src.product_state_assertion AS s
                    WHERE s.product_item_id=p.item_id),
                   json_object('part_id', i.part_item_id)
            FROM src.product AS p JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO product_states
            SELECT s.item_id, s.product_item_id, s.axis, s.exact_state,
                   s.assertion_date, s.asserted_by
            FROM src.product_state_assertion AS s
            WHERE s.product_item_id IN (SELECT product_id FROM research_products)
            """
        )
        connection.execute(
            """
            INSERT INTO product_uses
            SELECT u.use_id, u.study_id, u.canonical_label,
                   u.context, u.function, u.analytic_role
            FROM scientific_uses AS u
            JOIN registry_entities AS r USING (registry_id)
            WHERE u.use_type='Product' AND r.scope='GLOBAL'
            """
        )
        connection.execute(
            """
            INSERT INTO dataset_uses
            SELECT d.item_id, i.study_id, d.source_label, d.origin,
                   json_object('level', d.level, 'purpose', d.purpose,
                               'part_id', i.part_item_id)
            FROM src.data_use AS d JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO concepts
            SELECT i.study_id, c.label
            FROM src.concept AS c JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO source_conflicts
            SELECT c.item_id, i.study_id,
                   COALESCE((SELECT group_concat(s.statement, ' | ')
                             FROM src.source_conflict_statement AS s
                             WHERE s.conflict_item_id=c.item_id), c.scope),
                   json_object('scope', c.scope)
            FROM src.source_conflict AS c JOIN src.item AS i USING (item_id)
            WHERE i.study_id IS NOT NULL
            """
        )
        connection.execute(
            """
            INSERT INTO extraction_gaps
            SELECT g.item_id, i.study_id, g.state, g.affected_type,
                   g.affected_key, g.importance, g.proposed_resolution
            FROM src.gap AS g JOIN src.item AS i USING (item_id)
            """
        )

        connection.execute("COMMIT")
        errors = connection.execute("PRAGMA foreign_key_check").fetchall()
        if errors:
            raise ValueError(f"foreign-key errors: {errors[:5]}")
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise ValueError(f"integrity check failed: {integrity}")
        counts = {
            table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in (
                "projects",
                "publications",
                "studies",
                "project_publications",
                "people",
                "project_people",
                "euroqol_memberships",
                "publication_authors",
                "publication_citations",
                "scientific_uses",
                "registry_entities",
                "findings",
                "limitations",
                "research_products",
            )
        }
        if counts["publications"] != publication_count or counts["studies"] != study_count:
            raise ValueError("serving database lost a publication or study")
        connection.execute("DETACH DATABASE src")
        connection.close()
        os.replace(temporary, output)
        return counts
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def main() -> None:
    args = parse_args()
    counts = build(args.source.resolve(), args.output.resolve())
    print(json.dumps({"output": str(args.output), "sha256": sha256(args.output), **counts}, indent=2))


if __name__ == "__main__":
    main()
