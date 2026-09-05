from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))

from fulltext_ingest_tool import reject, submit  # noqa: E402


def valid_payload() -> dict:
    return {
        "basis": "PROJECT_OUTPUT",
        "project_ids": ["EQ-1"],
        "reason": "The methods and output match the funded project.",
        "support_scope": None,
        "record": {
            "studies": [
                {
                    "id": "s1",
                    "label": "Measurement study",
                    "primary_research_family": "MEASUREMENT_PROPERTY_EVALUATION",
                    "execution_state": "COMPLETED",
                    "result_state": "RESULTS_REPORTED",
                    "family_rationale": "Measurement performance is the main result.",
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
                },
                *[
                    {
                        "type": "Design",
                        "id": f"design{index}",
                        "study_id": "s1",
                        "part_id": None,
                        "axis": axis,
                        "value": value,
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
                    "part_id": None,
                    "name": "EQ-5D-5L",
                    "context": "DIRECT_CURRENT_ACTIVITY",
                    "function": "OUTCOME_MEASURE",
                },
                {
                    "type": "Finding",
                    "id": "finding1",
                    "study_id": "s1",
                    "part_id": None,
                    "statement": "The instrument distinguished the specified groups.",
                    "about": ["iu1"],
                    "values": [],
                },
            ],
        },
        "extensions": [],
    }


class FullTextIngestToolTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.folder = Path(self.temporary.name)
        self.context = self.folder / "context.json"
        self.context.write_text(
            json.dumps(
                {
                    "record_id": "T001",
                    "candidate_project_ids": ["EQ-1"],
                    "publication_form": "ORIGINAL_RESEARCH_ARTICLE",
                    "source_marker": "paper.md",
                    "accepted_record_path": "accepted.json",
                    "extension_log_path": "extensions.jsonl",
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_valid_submission_maps_registry_name_and_saves(self) -> None:
        success, message = submit(self.context, valid_payload())
        self.assertTrue(success, message)
        result = json.loads((self.folder / "accepted.json").read_text())
        instrument = next(
            item for item in result["record"]["items"] if item["type"] == "InstrumentUse"
        )
        self.assertEqual(instrument["registry_id"], "instrument:eq-5d-5l")
        self.assertEqual(instrument["source_label"], "EQ-5D-5L")
        self.assertNotIn("name", instrument)

    def test_unknown_enum_returns_choices_and_extension_syntax(self) -> None:
        payload = valid_payload()
        payload["record"]["items"][0]["value"] = "NEW_RESEARCH_PURPOSE"
        success, message = submit(self.context, payload)
        self.assertFalse(success)
        self.assertIn("research_purpose", message)
        self.assertIn("ADD_ENUM_VALUE", message)
        self.assertFalse((self.folder / "accepted.json").exists())

    def test_explicit_enum_extension_is_accepted_and_recorded(self) -> None:
        payload = valid_payload()
        payload["record"]["items"][0]["value"] = "NEW_RESEARCH_PURPOSE"
        payload["extensions"] = [
            {
                "action": "ADD_ENUM_VALUE",
                "key": "research_purpose",
                "value": "NEW_RESEARCH_PURPOSE",
                "definition": "A genuinely new research purpose.",
            }
        ]
        success, message = submit(self.context, payload)
        self.assertTrue(success, message)
        extensions = (self.folder / "extensions.jsonl").read_text()
        self.assertIn("NEW_RESEARCH_PURPOSE", extensions)
        self.assertIn('"record_id": "T001"', extensions)

    def test_unknown_registry_name_can_be_added_by_same_worker(self) -> None:
        payload = valid_payload()
        instrument = next(
            item for item in payload["record"]["items"] if item["type"] == "InstrumentUse"
        )
        instrument["name"] = "New Research Instrument"
        success, message = submit(self.context, payload)
        self.assertFalse(success)
        self.assertIn("ADD_REGISTRY_ENTITY", message)

        payload["extensions"] = [
            {
                "action": "ADD_REGISTRY_ENTITY",
                "entity_type": "Instrument",
                "name": "New Research Instrument",
            }
        ]
        success, message = submit(self.context, payload)
        self.assertTrue(success, message)
        result = json.loads((self.folder / "accepted.json").read_text())
        instrument = next(
            item for item in result["record"]["items"] if item["type"] == "InstrumentUse"
        )
        self.assertTrue(instrument["registry_id"].startswith("instrument:new-research-instrument"))

    def test_same_worker_can_confirm_a_new_alias(self) -> None:
        payload = valid_payload()
        instrument = next(
            item for item in payload["record"]["items"] if item["type"] == "InstrumentUse"
        )
        instrument["name"] = "Five-level EQ instrument"
        payload["extensions"] = [
            {
                "action": "ADD_REGISTRY_ALIAS",
                "entity_type": "Instrument",
                "alias": "Five-level EQ instrument",
                "canonical_name": "EQ-5D-5L",
            }
        ]
        success, message = submit(self.context, payload)
        self.assertTrue(success, message)
        result = json.loads((self.folder / "accepted.json").read_text())
        instrument = next(
            item for item in result["record"]["items"] if item["type"] == "InstrumentUse"
        )
        self.assertEqual(instrument["registry_id"], "instrument:eq-5d-5l")

    def test_concept_alias_is_saved_as_one_canonical_label(self) -> None:
        payload = valid_payload()
        payload["record"]["items"].append(
            {
                "type": "Concept",
                "id": "concept1",
                "study_id": "s1",
                "part_id": None,
                "name": "States worse than dead",
                "description": None,
                "about": ["s1"],
            }
        )
        success, message = submit(self.context, payload)
        self.assertTrue(success, message)
        result = json.loads((self.folder / "accepted.json").read_text())
        concept = next(
            item for item in result["record"]["items"] if item["type"] == "Concept"
        )
        self.assertEqual(concept["label"], "Health states worse than dead")
        self.assertNotIn("name", concept)

    def test_malformed_extension_returns_an_error(self) -> None:
        payload = valid_payload()
        payload["extensions"] = [{"action": "ADD_ENUM_VALUE"}]
        success, message = submit(self.context, payload)
        self.assertFalse(success)
        self.assertIn("invalid extension object", message)

    def test_reject_saves_no_scientific_record(self) -> None:
        success, message = reject(self.context, "No EuroQol support or project link.")
        self.assertTrue(success, message)
        result = json.loads((self.folder / "accepted.json").read_text())
        self.assertEqual(result["eligibility"]["decision"], "EXCLUDE")
        self.assertIsNone(result["record"])

    def test_submit_cli_reads_standard_input(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "pipeline" / "fulltext_ingest_tool.py"),
                "--context",
                str(self.context),
                "submit",
            ],
            input=json.dumps(valid_payload()),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "SAVED")
        self.assertTrue((self.folder / "accepted.json").is_file())


if __name__ == "__main__":
    unittest.main()
