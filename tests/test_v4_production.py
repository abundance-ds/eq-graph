"""Tests for the version-4 production record contract."""

from __future__ import annotations

import copy
import sqlite3
import tempfile
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
PRODUCTION = REPO / "pilot" / "ontology-development-v4" / "production"
sys.path.insert(0, str(PRODUCTION))

from validate import resolve_record_path, validate_record, validate_registry  # noqa: E402
from normalize_registry import (  # noqa: E402
    REGISTRY_TYPE as NORMALIZE_REGISTRY_TYPE,
    normalized_label,
    registry_lookup,
)
from load_research_v2 import (  # noqa: E402
    ITEM_TYPES,
    SCHEMA,
    USE_TYPE,
    load_registry,
    load_studies_and_items,
    normalized_doi,
    publication_year,
)


def valid_record() -> dict:
    return {
        "schema_version": "eq-record-0.1",
        "record_id": "T001",
        "assessment": {
            "disposition": "include-study",
            "connection": "direct_eq",
            "euroqol_support": "none-stated",
            "support_scope": None,
            "publication_form": "ORIGINAL_RESEARCH_ARTICLE",
            "publication_relation": None,
            "reason": "The study evaluates EQ-5D-5L measurement.",
            "source": ["Abstract"],
        },
        "studies": [
            {
                "id": "s1",
                "label": "Measurement study",
                "primary_research_family": "MEASUREMENT_PROPERTY_EVALUATION",
                "execution_state": "COMPLETED",
                "result_state": "RESULTS_REPORTED",
                "family_rationale": "Measurement performance is the main result.",
                "source": ["Abstract"],
            }
        ],
        "items": [
            {
                "type": "Purpose",
                "id": "purpose1",
                "study_id": "s1",
                "part_id": None,
                "value": "MEASUREMENT_PROPERTY_EVALUATION",
                "rank": 1,
                "source": ["Abstract"],
            },
            {
                "type": "StudyPart",
                "id": "part1",
                "study_id": "s1",
                "part_id": None,
                "label": "Main empirical part",
                "source": ["Methods"],
            },
            *[
                {
                    "type": "Design",
                    "id": f"design{index}",
                    "study_id": "s1",
                    "part_id": "part1",
                    "axis": axis,
                    "value": value,
                    "source": ["Methods"],
                }
                for index, (axis, value) in enumerate(
                    (
                        ("component_approach", "QUANTITATIVE_EMPIRICAL"),
                        ("temporal_structure", "CROSS_SECTIONAL"),
                        ("comparison_structure", "NONCOMPARATIVE"),
                        ("allocation_structure", "NOT_APPLICABLE"),
                    ),
                    1,
                )
            ],
            {
                "type": "InstrumentUse",
                "id": "iu1",
                "study_id": "s1",
                "part_id": "part1",
                "source_label": "EQ-5D-5L",
                "registry_id": "instrument:eq-5d-5l",
                "context": "DIRECT_CURRENT_ACTIVITY",
                "function": "OUTCOME_MEASURE",
                "source": ["Methods"],
            },
            {
                "type": "Outcome",
                "id": "outcome1",
                "study_id": "s1",
                "part_id": "part1",
                "family": "MEASUREMENT_PROPERTY",
                "label": "Known-groups validity",
                "instrument_use_ids": ["iu1"],
                "source": ["Methods"],
            },
            {
                "type": "Finding",
                "id": "finding1",
                "study_id": "s1",
                "part_id": "part1",
                "statement": "The instrument distinguished the specified groups.",
                "about": ["outcome1", "iu1"],
                "values": [],
                "source": ["Results"],
            },
        ],
    }


def add_product_use(record: dict, registry_id: str | None) -> None:
    record["items"].append(
        {
            "type": "ProductUse",
            "id": "product_use1",
            "study_id": "s1",
            "part_id": "part1",
            "source_label": "German EQ-5D-5L value set",
            "registry_id": registry_id,
            "context": "CURRENT_STUDY_OBJECT",
            "function": "ANALYSIS_OBJECT",
            "source": ["Methods"],
        }
    )


class ProductionRecordTests(unittest.TestCase):
    def test_valid_record(self) -> None:
        errors, warnings = validate_record(valid_record(), "T001")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_simple_study_does_not_require_a_study_part(self) -> None:
        record = copy.deepcopy(valid_record())
        record["items"] = [
            item for item in record["items"] if item["type"] != "StudyPart"
        ]
        for item in record["items"]:
            if item["part_id"] == "part1":
                item["part_id"] = None
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_whole_study_about_reference_is_valid(self) -> None:
        record = copy.deepcopy(valid_record())
        finding = next(item for item in record["items"] if item["type"] == "Finding")
        finding["about"] = ["s1"]
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_filter_rule(self) -> None:
        record = valid_record()
        record["assessment"]["connection"] = "unrelated"
        errors, _ = validate_record(record, "T001")
        self.assertTrue(any("filter rule" in error for error in errors))

    def test_design_value_must_match_axis(self) -> None:
        record = valid_record()
        design = next(item for item in record["items"] if item["type"] == "Design")
        design["value"] = "CROSS_SECTIONAL"
        errors, _ = validate_record(record, "T001")
        self.assertTrue(any("not valid for component_approach" in error for error in errors))

    def test_unknown_key_fails_schema(self) -> None:
        record = valid_record()
        record["studies"][0]["made_up_key"] = "value"
        errors, _ = validate_record(record, "T001")
        self.assertTrue(any("Additional properties" in error for error in errors))

    def test_unmapped_registry_identity_is_a_warning(self) -> None:
        record = copy.deepcopy(valid_record())
        instrument = next(item for item in record["items"] if item["type"] == "InstrumentUse")
        instrument["source_label"] = "New instrument"
        instrument["registry_id"] = None
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertTrue(any("unmapped Instrument" in warning for warning in warnings))

    def test_existing_product_can_be_a_typed_study_object(self) -> None:
        record = copy.deepcopy(valid_record())
        add_product_use(record, "product:eq-5d-5l-de")
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(NORMALIZE_REGISTRY_TYPE["ProductUse"], "Product")

    def test_product_use_rejects_an_instrument_identity(self) -> None:
        record = copy.deepcopy(valid_record())
        add_product_use(record, "instrument:eq-5d-5l")
        errors, _ = validate_record(record, "T001")
        self.assertTrue(any("is not a Product identity" in error for error in errors))

    def test_product_use_function_is_controlled(self) -> None:
        record = copy.deepcopy(valid_record())
        add_product_use(record, "product:eq-5d-5l-de")
        record["items"][-1]["function"] = "SCORING"
        errors, _ = validate_record(record, "T001")
        self.assertTrue(errors)

    def test_sqlite_loader_preserves_product_use(self) -> None:
        record = copy.deepcopy(valid_record())
        add_product_use(record, "product:eq-5d-5l-de")
        self.assertEqual(USE_TYPE["ProductUse"], "Product")
        self.assertIn("ProductUse", ITEM_TYPES)

        connection = sqlite3.connect(":memory:")
        try:
            connection.executescript(SCHEMA.read_text(encoding="utf-8"))
            load_registry(
                connection,
                PRODUCTION / "REGISTRY.tsv",
                PRODUCTION / "REGISTRY_ALIASES.tsv",
            )
            connection.execute(
                """
                INSERT INTO publication(
                    publication_id, record_id, title, publication_form,
                    open_access, assessment_disposition, euroqol_connection,
                    euroqol_support, assessment_reason, schema_version
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "publication:test",
                    "T001",
                    "Test publication",
                    "ORIGINAL_RESEARCH_ARTICLE",
                    0,
                    "include-study",
                    "direct_eq",
                    "none-stated",
                    "Test fixture",
                    "eq-record-0.1",
                ),
            )
            source_counts, loaded = load_studies_and_items(
                connection,
                "publication:test",
                record,
            )
            row = connection.execute(
                """
                SELECT use_type, registry_id, context, function
                FROM registry_use
                WHERE item_id = ?
                """,
                ("T001:product_use1",),
            ).fetchone()
        finally:
            connection.close()

        self.assertEqual(source_counts["ProductUse"], 1)
        self.assertEqual(loaded["ProductUse"], 1)
        self.assertEqual(
            row,
            (
                "Product",
                "product:eq-5d-5l-de",
                "CURRENT_STUDY_OBJECT",
                "ANALYSIS_OBJECT",
            ),
        )

    def test_software_use_and_task_relation_are_valid(self) -> None:
        record = copy.deepcopy(valid_record())
        record["items"].extend(
            [
                {
                    "type": "SoftwareUse",
                    "id": "software1",
                    "study_id": "s1",
                    "part_id": "part1",
                    "source_label": "EQ-VT 2.1",
                    "registry_id": None,
                    "context": "DIRECT_CURRENT_ACTIVITY",
                    "function": "VALUATION_ADMINISTRATION",
                    "source": ["Methods"],
                },
                {
                    "type": "TaskDesign",
                    "id": "task1",
                    "study_id": "s1",
                    "part_id": "part1",
                    "applies_to": ["software1"],
                    "label": "Computer-assisted valuation task",
                    "profiles": [],
                    "attributes": [],
                    "levels": [],
                    "duration": None,
                    "alternatives": None,
                    "task_count": None,
                    "block": None,
                    "order": None,
                    "randomization_unit": None,
                    "stopping_rule": None,
                    "source": ["Methods"],
                },
            ]
        )
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertTrue(any("unmapped Software" in warning for warning in warnings))

    def test_administration_can_apply_to_task(self) -> None:
        record = copy.deepcopy(valid_record())
        record["items"].extend(
            [
                {
                    "type": "TaskDesign",
                    "id": "task1",
                    "study_id": "s1",
                    "part_id": "part1",
                    "applies_to": ["iu1"],
                    "label": "Instrument task",
                    "profiles": [],
                    "attributes": [],
                    "levels": [],
                    "duration": None,
                    "alternatives": None,
                    "task_count": None,
                    "block": None,
                    "order": None,
                    "randomization_unit": None,
                    "stopping_rule": None,
                    "source": ["Methods"],
                },
                {
                    "type": "Administration",
                    "id": "admin1",
                    "study_id": "s1",
                    "part_id": "part1",
                    "applies_to": ["task1"],
                    "respondent": "Adult participant",
                    "perspective": None,
                    "completion": "Interviewer-administered",
                    "assistance": None,
                    "channel": "Face-to-face",
                    "setting": None,
                    "instrument_language": None,
                    "interview_language": None,
                    "recall_period": None,
                    "time_point": None,
                    "source": ["Methods"],
                },
            ]
        )
        errors, warnings = validate_record(record, "T001")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_primary_run_record_precedes_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            primary = root / "repair"
            fallback = root / "original"
            for run in (primary, fallback):
                (run / "records").mkdir(parents=True)
            fallback_record = fallback / "records" / "T001.json"
            fallback_record.write_text("{}\n", encoding="utf-8")
            self.assertEqual(
                resolve_record_path("T001", primary, [fallback]),
                (fallback_record, fallback),
            )
            primary_record = primary / "records" / "T001.json"
            primary_record.write_text("{}\n", encoding="utf-8")
            self.assertEqual(
                resolve_record_path("T001", primary, [fallback]),
                (primary_record, primary),
            )

    def test_registry_parent_cycle_fails(self) -> None:
        registry = {
            "instrument:a": {
                "entity_type": "Instrument",
                "parent_registry_id": "instrument:b",
                "variant_kind": "FORM_VERSION",
            },
            "instrument:b": {
                "entity_type": "Instrument",
                "parent_registry_id": "instrument:a",
                "variant_kind": "FORM_VERSION",
            },
        }
        errors = validate_registry(registry)
        self.assertTrue(any("parent cycle" in error for error in errors))

    def test_registry_subscale_parent_is_valid(self) -> None:
        registry = {
            "instrument:parent": {
                "entity_type": "Instrument",
                "parent_registry_id": "",
                "variant_kind": "",
            },
            "instrument:subscale": {
                "entity_type": "Instrument",
                "parent_registry_id": "instrument:parent",
                "variant_kind": "SUBSCALE",
            },
        }
        self.assertEqual(validate_registry(registry), [])

    def test_registry_software_version_parent_is_valid(self) -> None:
        registry = {
            "software:parent": {
                "entity_type": "Software",
                "parent_registry_id": "",
                "variant_kind": "",
            },
            "software:version": {
                "entity_type": "Software",
                "parent_registry_id": "software:parent",
                "variant_kind": "SOFTWARE_VERSION",
            },
        }
        self.assertEqual(validate_registry(registry), [])

    def test_ai_draft_registry_id_must_be_null(self) -> None:
        errors, _ = validate_record(
            valid_record(),
            "T001",
            require_null_registry=True,
        )
        self.assertTrue(any("AI draft registry_id must be null" in error for error in errors))

    def test_registry_label_normalization_is_conservative(self) -> None:
        self.assertEqual(normalized_label("EQ‐5D  5L"), "eq-5d 5l")
        self.assertNotEqual(
            normalized_label("Taiwan EQ-5D-5L"),
            normalized_label("EQ-5D-5L"),
        )

    def test_registry_alias_collision_is_preserved(self) -> None:
        rows = [
            {
                "registry_id": "method:a",
                "entity_type": "Method",
                "canonical_label": "Method A",
                "aliases": "shared",
            },
            {
                "registry_id": "method:b",
                "entity_type": "Method",
                "canonical_label": "Method B",
                "aliases": "shared",
            },
        ]
        _, lookup = registry_lookup(rows)
        self.assertEqual(lookup[("Method", "shared")], {"method:a", "method:b"})

    def test_doi_normalization_is_exact(self) -> None:
        self.assertEqual(
            normalized_doi("https://doi.org/10.1007/S11136-025-04145-0."),
            "10.1007/s11136-025-04145-0",
        )
        self.assertNotEqual(normalized_doi("10.1000/a"), normalized_doi("10.1000/b"))

    def test_publication_year_priority(self) -> None:
        dates = [
            {"type": "received", "value": "2022-01-01"},
            {"type": "epub", "value": "2024-03-02"},
            {"type": "ppub", "value": "2025"},
        ]
        self.assertEqual(publication_year(dates), 2025)


if __name__ == "__main__":
    unittest.main()
