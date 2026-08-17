#!/usr/bin/env python3
"""Run retrieval and boundary tests against the ontology pilot."""

from __future__ import annotations

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "ontology-pilot.sqlite"


def rows(connection: sqlite3.Connection, query: str, parameters: tuple = ()) -> list[tuple]:
    return connection.execute(query, parameters).fetchall()


def main() -> None:
    connection = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    tests: list[tuple[str, bool, str]] = []

    value_set = rows(
        connection,
        """
        SELECT DISTINCT s.study_id, rm.preferred_label, sm.preferred_label, rp.label
        FROM study AS s
        JOIN research_method AS rm USING (study_id)
        JOIN statistical_model AS sm USING (study_id)
        JOIN research_product AS rp USING (study_id)
        WHERE rm.preferred_label IN ('cTTO', 'DCE')
          AND sm.role = 'preferred-final'
          AND rp.product_type = 'native value set'
        ORDER BY rm.preferred_label
        """,
    )
    tests.append(
        (
            "national value-set corner pieces",
            value_set
            == [
                ("H01", "DCE", "hybrid model 3b", "German EQ-5D-5L value set"),
                ("H01", "cTTO", "hybrid model 3b", "German EQ-5D-5L value set"),
            ],
            str(value_set),
        )
    )

    dce_roles = rows(
        connection,
        "SELECT study_id, role FROM research_method WHERE preferred_label = 'DCE' ORDER BY study_id",
    )
    tests.append(("DCE method roles", dce_roles == [("H01", "preference elicitation"), ("H02", "task-design experiment")], str(dce_roles)))

    concept_hits = rows(
        connection,
        """
        SELECT preferred_label, group_concat(study_id, ',')
        FROM study_concept
        WHERE preferred_label IN ('states worse than dead', 'digital health', 'child and adolescent health')
        GROUP BY preferred_label ORDER BY preferred_label
        """,
    )
    tests.append(
        (
            "concept and theme retrieval",
            concept_hits
            == [
                ("child and adolescent health", "H04,H06,H08"),
                ("digital health", "H10"),
                ("states worse than dead", "H01"),
            ],
            str(concept_hits),
        )
    )

    funded_no_eq = rows(
        connection,
        """
        SELECT s.study_id, p.doi, pp.support_type
        FROM study AS s
        JOIN publication AS p USING (publication_id)
        JOIN project_publication AS pp USING (publication_id)
        WHERE s.eq_instrument_status = 'none-reported' AND pp.link_status = 'accepted'
        """,
    )
    tests.append(("verified funded paper with no EQ instrument", funded_no_eq == [("H11", "10.1007/s11136-017-1512-x", "study funding")], str(funded_no_eq)))

    h09_boundary = rows(
        connection,
        """
        SELECT pp.project_id, pp.link_status
        FROM project_publication AS pp JOIN publication AS p USING (publication_id)
        WHERE p.doi = '10.1038/s41433-023-02860-x'
        ORDER BY pp.project_id
        """,
    )
    tests.append(("unverified H09 links excluded", h09_boundary == [("341-RA", "rejected"), ("357-RA", "rejected")], str(h09_boundary)))

    proxy = rows(
        connection,
        """
        SELECT s.study_id, i.preferred_label, a.respondent, a.perspective, a.setting
        FROM study AS s
        JOIN administration AS a USING (study_id)
        JOIN instrument AS i USING (instrument_id)
        WHERE s.study_id = 'H05'
        """,
    )
    tests.append(
        (
            "proxy role and perspective",
            proxy == [("H05", "EQ-HWB proxy version 2", "family or staff proxy", "proxy-person with observed drift", "residential aged care")],
            str(proxy),
        )
    )

    chichewa = rows(
        connection,
        """
        SELECT i.preferred_label, iu.language, iu.role
        FROM instrument_use AS iu JOIN instrument AS i USING (instrument_id)
        WHERE iu.study_id = 'H08' AND i.family = 'EQ-5D-Y'
        ORDER BY i.preferred_label
        """,
    )
    tests.append(
        (
            "exact Chichewa youth versions",
            chichewa
            == [
                ("EQ-5D-Y-3L", "Chichewa", "administered and psychometrically evaluated"),
                ("EQ-5D-Y-5L", "Chichewa", "administered and psychometrically evaluated"),
            ],
            str(chichewa),
        )
    )

    review_counts = rows(
        connection,
        """
        SELECT count(DISTINCT CASE WHEN count_status = 'review-publication' THEN sample_id END),
               max(CASE WHEN count_status = 'review-publication' THEN count_value END),
               max(CASE WHEN count_status = 'review-evidence-unit' THEN count_value END),
               (SELECT count(*) FROM review_evidence_unit WHERE study_id = 'H07')
        FROM sample WHERE study_id = 'H07'
        """,
    )
    tests.append(("review publication and evidence-unit separation", review_counts == [(1, 79, 1504, 1)], str(review_counts)))

    valuation_findings = rows(
        connection,
        "SELECT statement FROM finding WHERE study_id = 'H01' ORDER BY sequence",
    )
    findings_text = " ".join(value[0] for value in valuation_findings)
    tests.append(
        (
            "valuation finding depth",
            all(token in findings_text for token in ("-0.661", "pain/discomfort", "hybrid model 3b", "recommend")),
            findings_text,
        )
    )

    limitation_hit = rows(
        connection,
        "SELECT statement FROM limitation WHERE study_id = 'H11' AND statement LIKE '%response styles%'",
    )
    tests.append(("reported limitation retrieval", len(limitation_hit) == 1, str(limitation_hit)))

    h10_role = rows(
        connection,
        """
        SELECT iu.role, a.channel, rp.status
        FROM instrument_use AS iu
        JOIN administration AS a ON a.study_id = iu.study_id AND a.instrument_id = iu.instrument_id
        JOIN research_product AS rp ON rp.study_id = iu.study_id
        WHERE iu.study_id = 'H10'
        """,
    )
    tests.append(
        (
            "visualized data is not instrument administration",
            h10_role
            == [
                (
                    "historical data visualized in decision support",
                    "paper prototype",
                    "tested as paper prototype; online implementation planned",
                )
            ],
            str(h10_role),
        )
    )

    conflicts = rows(connection, "SELECT study_id, fact_name FROM source_conflict ORDER BY study_id")
    tests.append(("source conflicts remain visible", conflicts == [("H04", "Cronbach alpha"), ("H08", "all-participant sample")], str(conflicts)))

    metadata = rows(
        connection,
        """
        SELECT p.doi, p.pmid, p.pmcid, count(DISTINCT pa.author_id), count(DISTINCT pr.reference_id)
        FROM publication AS p
        JOIN publication_author AS pa USING (publication_id)
        LEFT JOIN publication_reference AS pr USING (publication_id)
        WHERE p.doi = '10.1007/s11136-017-1512-x'
        GROUP BY p.publication_id
        """,
    )
    tests.append(("deterministic metadata and references", metadata == [("10.1007/s11136-017-1512-x", "28185039", "PMC5420378", 3, 42)], str(metadata)))

    finding_counts = rows(
        connection,
        "SELECT count(*) FROM finding GROUP BY study_id ORDER BY study_id",
    )
    distinct_counts = {value[0] for value in finding_counts}
    tests.append(("study-dependent finding depth", len(distinct_counts) > 1 and min(distinct_counts) >= 3, str(sorted(distinct_counts))))

    search_terms = rows(
        connection,
        "SELECT term_type, term FROM study_search_term WHERE study_id = 'H01' ORDER BY term_type, term",
    )
    required_terms = {
        ("instrument", "EQ-5D-5L"),
        ("method", "cTTO"),
        ("method", "DCE"),
        ("model", "hybrid model 3b"),
        ("product", "German EQ-5D-5L value set"),
        ("research-purpose", "value-set development"),
    }
    tests.append(("corner pieces survive normalized search view", required_terms.issubset(set(search_terms)), str(search_terms)))

    connection.close()
    failures = [name for name, passed, _ in tests if not passed]
    for name, passed, detail in tests:
        print(f"{'PASS' if passed else 'FAIL'}\t{name}\t{detail}")
    print(f"SUMMARY\tpass={len(tests) - len(failures)}\tfail={len(failures)}")
    if failures:
        raise SystemExit("Query failures: " + ", ".join(failures))


if __name__ == "__main__":
    main()
