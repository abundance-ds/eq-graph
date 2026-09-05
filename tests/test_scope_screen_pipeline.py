import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))

from run_codex_abstract_screen import project_is_in_window  # noqa: E402


class FullTextPackageTest(unittest.TestCase):
    def test_package_keeps_screen_result_and_only_named_projects(self):
        work = ROOT / "work"
        work.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=work) as value:
            folder = Path(value)
            text = folder / "paper.md"
            text.write_text("# Paper\n\nFull text.\n", encoding="utf-8")
            corpus = folder / "corpus.jsonl"
            corpus.write_text(
                json.dumps(
                    {
                        "record_id": "P1",
                        "doi": "10.1/example",
                        "title": "Example",
                        "year": 2020,
                        "abstract": "A usable abstract.",
                        "abstract_source": "test",
                        "document_gate": "candidate_article",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            canonical = folder / "canonical.jsonl"
            canonical.write_text(corpus.read_text(encoding="utf-8"), encoding="utf-8")
            screen = folder / "screen.jsonl"
            screen.write_text(
                json.dumps(
                    {
                        "record_id": "P1",
                        "decision": "RETRIEVE_FULL_TEXT",
                        "project_ids": ["EQ-1"],
                        "reason": "A specific project match needs full-text confirmation.",
                        "model": "gpt-5.6-terra",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            projects = folder / "projects.csv"
            fields = [
                "Project Id",
                "Title",
                "Abstract",
                "Project PI / Applicant Name",
                "Working Group",
                "Start Year",
                "End Year",
                "Status",
            ]
            with projects.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow(
                    {
                        "Project Id": "EQ-1",
                        "Title": "Candidate",
                        "Abstract": "Candidate project",
                        "Project PI / Applicant Name": "Person One",
                        "Working Group": "Group",
                        "Start Year": "2019",
                        "End Year": "2021",
                        "Status": "Complete",
                    }
                )
                writer.writerow(
                    {
                        "Project Id": "EQ-2",
                        "Title": "Not selected",
                        "Abstract": "Another project",
                        "Project PI / Applicant Name": "Person Two",
                        "Working Group": "Group",
                        "Start Year": "2018",
                        "End Year": "2020",
                        "Status": "Complete",
                    }
                )
            manifest = folder / "fulltext.tsv"
            with manifest.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["record_id", "text_path", "source_format"],
                    delimiter="\t",
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "record_id": "P1",
                        "text_path": str(text.relative_to(ROOT)),
                        "source_format": "markdown",
                    }
                )
            output = folder / "output"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "pipeline/build_fulltext_paper_packages.py"),
                    "--screen",
                    str(screen),
                    "--corpus",
                    str(corpus),
                    "--canonical-metadata",
                    str(canonical),
                    "--projects",
                    str(projects),
                    "--fulltext-manifest",
                    str(manifest),
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            package = json.loads((output / "packages/P1.json").read_text(encoding="utf-8"))
            self.assertEqual(
                package["abstract_screen"]["decision"],
                "RETRIEVE_FULL_TEXT",
            )
            self.assertEqual(package["abstract_screen"]["project_ids"], ["EQ-1"])
            self.assertEqual(
                [project["project_id"] for project in package["candidate_projects"]],
                ["EQ-1"],
            )
            self.assertEqual(
                package["deterministic_metadata"]["publication"]["record_id"],
                "P1",
            )
            summary = json.loads((output / "SUMMARY.json").read_text(encoding="utf-8"))
            self.assertEqual(summary["packages"], 1)
            self.assertEqual(summary["packages_with_candidate_projects"], 1)


class ProjectWindowTest(unittest.TestCase):
    def test_optional_lookback_keeps_only_recent_past_projects(self):
        recent = {"start_year": 2018, "not_before_year": None}
        old = {"start_year": 2009, "not_before_year": None}
        future = {"start_year": 2021, "not_before_year": None}

        self.assertTrue(project_is_in_window(recent, 2020, 10))
        self.assertFalse(project_is_in_window(old, 2020, 10))
        self.assertFalse(project_is_in_window(future, 2020, 10))
        self.assertTrue(project_is_in_window(old, 2020, None))


if __name__ == "__main__":
    unittest.main()
