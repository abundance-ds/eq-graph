#!/usr/bin/env python3
"""Run competency checks against the broader-test SQLite database."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


TESTS = [
    (
        "no-EQ funded travel-grant paper",
        "SELECT s.eq_instrument_status, pp.support_type FROM study AS s "
        "JOIN project_publication AS pp USING (publication_id) WHERE s.study_id = 'B01'",
        [("none-reported", "travel grant")],
    ),
    (
        "non-EQ language versions remain exact",
        "SELECT i.preferred_label, iu.role FROM instrument_use AS iu "
        "JOIN instrument AS i USING (instrument_id) WHERE iu.study_id = 'B02' ORDER BY i.preferred_label",
        [
            ("PedsQL 4.0 GCS child self-report", "translated and psychometrically evaluated"),
            ("PedsQL 4.0 GCS teen self-report", "translated and psychometrically evaluated"),
        ],
    ),
    (
        "language and paper administration",
        "SELECT i.preferred_label, iu.language, a.interaction, a.channel "
        "FROM instrument_use AS iu JOIN instrument AS i USING (instrument_id) "
        "JOIN administration AS a USING (study_id, instrument_id) "
        "WHERE iu.study_id = 'B02' ORDER BY i.preferred_label",
        [
            ("PedsQL 4.0 GCS child self-report", "Chichewa (Malawi)", "self-completed", "paper"),
            ("PedsQL 4.0 GCS teen self-report", "Chichewa (Malawi)", "self-completed", "paper"),
        ],
    ),
    (
        "proxy recall role",
        "SELECT i.preferred_label, mt.time_role, mt.time_label FROM measurement_time AS mt "
        "JOIN instrument AS i USING (instrument_id) WHERE mt.study_id = 'B03'",
        [("EQ-HWB-9 proxy version", "recall-period", "seven days")],
    ),
    (
        "review method and model",
        "SELECT rm.preferred_label, sm.preferred_label FROM research_method AS rm "
        "JOIN statistical_model AS sm USING (study_id) "
        "WHERE rm.study_id = 'B04' AND rm.preferred_label = 'meta-analysis' "
        "AND sm.preferred_label = 'DerSimonian-Laird random-effects model'",
        [("meta-analysis", "DerSimonian-Laird random-effects model")],
    ),
    (
        "unverified folder link does not become funded evidence",
        "SELECT link_status, evidence_class FROM project_publication WHERE project_id = '285-PHD'",
        [("candidate", "article gives no EuroQol funding statement")],
    ),
    (
        "video is not the valuation method",
        "SELECT rm.preferred_label, iu.role FROM research_method AS rm "
        "JOIN instrument_use AS iu USING (study_id) "
        "WHERE rm.study_id = 'B06' AND rm.preferred_label = 'cTTO'",
        [("cTTO", "valued")],
    ),
    (
        "valuation channels remain separate",
        "SELECT channel, interaction FROM administration WHERE study_id = 'B06' ORDER BY channel",
        [("face-to-face", "interviewer-administered"), ("video", "interviewer-administered")],
    ),
    (
        "report and reference time are separate",
        "SELECT time_role, count(*) FROM measurement_time WHERE study_id = 'B07' "
        "GROUP BY time_role ORDER BY time_role",
        [("reference-time", 1), ("report-time", 3)],
    ),
    (
        "co-design input is not implementation",
        "SELECT label, status FROM research_product WHERE study_id = 'B08'",
        [("P-PROM ROCK co-design requirements", "co-design input produced")],
    ),
    (
        "source conflict and experimental product status",
        "SELECT sc.fact_name, rp.status FROM source_conflict AS sc "
        "JOIN research_product AS rp USING (study_id) WHERE sc.study_id = 'B09'",
        [("statistical significance", "produced; not a QALY value set")],
    ),
    (
        "protocol facts remain planned",
        "SELECT execution_status FROM study WHERE study_id = 'B10'",
        [("planned",)],
    ),
    (
        "PROM used as prediction input",
        "SELECT i.preferred_label, iu.role FROM instrument_use AS iu "
        "JOIN instrument AS i USING (instrument_id) "
        "WHERE iu.study_id = 'B11' AND i.preferred_label = 'EQ-5D-5L'",
        [("EQ-5D-5L", "used as prediction input")],
    ),
    (
        "administered but unreported analysis",
        "SELECT iu.role FROM instrument_use AS iu JOIN instrument AS i USING (instrument_id) "
        "WHERE iu.study_id = 'B12' AND i.preferred_label = 'EQ-HWB'",
        [("administered; results reserved for another report",)],
    ),
    (
        "conceptual paper without administered instrument",
        "SELECT s.eq_instrument_status, rm.preferred_label, "
        "(SELECT count(*) FROM population WHERE study_id = 'B13') "
        "FROM study AS s JOIN research_method AS rm USING (study_id) WHERE s.study_id = 'B13'",
        [("mentioned-only", "conceptual uncertainty tracing", 0)],
    ),
    (
        "OPUF remains an exact method",
        "SELECT preferred_label FROM research_method WHERE study_id = 'B14' "
        "AND preferred_label = 'Online Personal Utility Functions'",
        [("Online Personal Utility Functions",)],
    ),
    (
        "CREATE is a reporting checklist",
        "SELECT label, product_type FROM research_product WHERE study_id = 'B15'",
        [("CREATE", "reporting checklist")],
    ),
    (
        "retracted value set is unsafe",
        "SELECT p.lifecycle_status, rp.status FROM publication AS p "
        "JOIN study AS s USING (publication_id) JOIN research_product AS rp USING (study_id) "
        "WHERE s.study_id = 'B16'",
        [("retracted", "retracted; do not use operationally")],
    ),
    (
        "correction amends parent and is not a study",
        "SELECT s.doi, r.relation_type, t.doi, "
        "(SELECT count(*) FROM study WHERE study_id = 'B17') "
        "FROM publication_relation AS r "
        "JOIN publication AS s ON s.publication_id = r.source_publication_id "
        "JOIN publication AS t ON t.publication_id = r.target_publication_id",
        [("10.1371/journal.pone.0305983", "corrects", "10.1371/journal.pone.0209344", 0)],
    ),
    (
        "shown for content evaluation is not administered",
        "SELECT i.preferred_label, iu.role, pp.link_status FROM instrument_use AS iu "
        "JOIN instrument AS i USING (instrument_id) "
        "JOIN study AS s USING (study_id) JOIN project_publication AS pp USING (publication_id) "
        "WHERE iu.study_id = 'B18' AND i.preferred_label = 'EQ-5D-5L'",
        [("EQ-5D-5L", "shown for content evaluation", "candidate")],
    ),
    (
        "experience-based valuation corner pieces",
        "SELECT i.preferred_label, iu.role, sm.preferred_label FROM instrument_use AS iu "
        "JOIN instrument AS i USING (instrument_id) "
        "JOIN statistical_model AS sm USING (study_id) "
        "WHERE iu.study_id = 'B19' AND i.preferred_label = 'EQ VAS' "
        "AND sm.preferred_label = 'ordinary least-squares regression'",
        [("EQ VAS", "administered and analyzed as experience-based valuation", "ordinary least-squares regression")],
    ),
    (
        "historical EQ data in decision support",
        "SELECT i.preferred_label, iu.role, rp.status FROM instrument_use AS iu "
        "JOIN instrument AS i USING (instrument_id) "
        "JOIN research_product AS rp USING (study_id) "
        "WHERE iu.study_id = 'B20' AND i.preferred_label = 'EQ-5D'",
        [("EQ-5D", "historical data displayed in decision support", "usability tested; routine implementation recommended")],
    ),
    (
        "material derivation chain",
        "SELECT study_id, count(*) FROM derivation_step GROUP BY study_id ORDER BY study_id",
        [("B04", 2), ("B11", 1), ("B13", 1)],
    ),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=SCRIPT_DIR / "broader-test.sqlite")
    args = parser.parse_args()
    connection = sqlite3.connect(args.db)
    failures = 0
    try:
        for name, sql, expected in TESTS:
            actual = connection.execute(sql).fetchall()
            status = "PASS" if actual == expected else "FAIL"
            failures += status == "FAIL"
            print(f"{status}\t{name}\t{actual}")
            if status == "FAIL":
                print(f"EXPECTED\t{expected}")
    finally:
        connection.close()
    print(f"SUMMARY\tpass={len(TESTS) - failures}\tfail={failures}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
