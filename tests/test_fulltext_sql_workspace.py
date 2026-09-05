from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))

from fulltext_sql_mcp import tools  # noqa: E402
from fulltext_sql_workspace import run_sql, submit_workspace  # noqa: E402


class FullTextSqlWorkspaceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.folder = Path(self.temporary.name)
        self.context = self.folder / "context.json"
        self.context.write_text(
            json.dumps(
                {
                    "record_id": "SQL-TEST",
                    "candidate_project_ids": ["EQ-1"],
                    "candidate_projects": [
                        {
                            "project_id": "EQ-1",
                            "title": "Test project",
                        }
                    ],
                    "publication_form": "ORIGINAL_RESEARCH_ARTICLE",
                    "source_marker": "paper.md",
                    "accepted_record_path": str(self.folder / "accepted.json"),
                    "extension_log_path": str(self.folder / "extensions.jsonl"),
                    "workspace_path": str(self.folder / "workspace.sqlite"),
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def populate_valid(self, instrument_name: str = "EQ-5D-5L") -> None:
        statements = [
            "INSERT INTO eligibility VALUES ('PROJECT_OUTPUT','Direct output',NULL)",
            "INSERT INTO project_link VALUES ('EQ-1')",
            "INSERT INTO study VALUES ('S1','Test','METHODS_RESEARCH','COMPLETED','RESULTS_REPORTED','Methods are the main subject')",
            "INSERT INTO purpose VALUES ('P1','S1',NULL,'VALUATION_METHOD_EVALUATION',1)",
            "INSERT INTO design VALUES ('D1','S1',NULL,'component_approach','QUANTITATIVE_EMPIRICAL')",
            "INSERT INTO design VALUES ('D2','S1',NULL,'temporal_structure','CROSS_SECTIONAL')",
            "INSERT INTO design VALUES ('D3','S1',NULL,'comparison_structure','BETWEEN_METHOD')",
            "INSERT INTO design VALUES ('D4','S1',NULL,'allocation_structure','RANDOMIZED')",
            f"INSERT INTO instrument_use VALUES ('I1','S1',NULL,{json.dumps(instrument_name)},'CURRENT_STUDY_OBJECT','VALUATION_TARGET')",
            "INSERT INTO finding VALUES ('F1','S1',NULL,'The method performed well.')",
            "INSERT INTO item_relation VALUES ('F1','ABOUT','I1',1)",
        ]
        for statement in statements:
            success, message = run_sql(self.context, statement)
            self.assertTrue(success, message)

    def test_tools_have_only_flat_arguments(self) -> None:
        values = tools()
        self.assertEqual([value["name"] for value in values], ["sql", "submit", "reject"])
        self.assertEqual(list(values[0]["inputSchema"]["properties"]), ["statement"])
        self.assertEqual(values[1]["inputSchema"]["properties"], {})
        self.assertEqual(list(values[2]["inputSchema"]["properties"]), ["reason"])
        self.assertNotIn("anyOf", json.dumps(values))

    def test_sql_rows_validate_and_save(self) -> None:
        self.populate_valid()
        success, message = submit_workspace(self.context)
        self.assertTrue(success, message)
        value = json.loads((self.folder / "accepted.json").read_text())
        self.assertEqual(value["eligibility"]["decision"], "INCLUDE")
        self.assertEqual(value["record"]["studies"][0]["id"], "S1")

    def test_context_tables_are_read_only(self) -> None:
        success, message = run_sql(self.context, "DELETE FROM candidate_project")
        self.assertFalse(success)
        self.assertIn("not authorized", message)

    def test_same_agent_can_add_a_new_registry_identity(self) -> None:
        self.populate_valid("New Research Instrument")
        success, message = submit_workspace(self.context)
        self.assertFalse(success)
        self.assertIn("registry_extension", message)
        self.assertNotIn('"action"', message)
        success, message = run_sql(
            self.context,
            "INSERT INTO registry_extension VALUES ('Instrument','New Research Instrument')",
        )
        self.assertTrue(success, message)
        success, message = submit_workspace(self.context)
        self.assertTrue(success, message)

    def test_schema_changes_are_not_allowed(self) -> None:
        success, message = run_sql(self.context, "CREATE TABLE bad(value TEXT)")
        self.assertFalse(success)
        self.assertIn("use SELECT", message)


if __name__ == "__main__":
    unittest.main()
