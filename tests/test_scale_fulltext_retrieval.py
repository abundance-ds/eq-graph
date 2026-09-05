import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))

from run_scale_fulltext_retrieval import (  # noqa: E402
    jats_identity,
    title_is_ordered_in_text,
)
from scale_publication_metadata import load_publications  # noqa: E402


class CanonicalMetadataTest(unittest.TestCase):
    def test_canonical_identity_replaces_stale_identity_and_keeps_enrichment(self):
        with tempfile.TemporaryDirectory() as value:
            folder = Path(value)
            corpus = folder / "corpus.jsonl"
            canonical = folder / "canonical.jsonl"
            corpus.write_text(
                json.dumps(
                    {
                        "record_id": "P1",
                        "title": "Wrong paper",
                        "year": 1980,
                        "doi": "10.1/right",
                        "pmid": "123",
                        "abstract": "Exact DOI abstract enrichment.",
                        "abstract_source": "europe_pmc",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            canonical.write_text(
                json.dumps(
                    {
                        "record_id": "P1",
                        "title": "Right paper",
                        "year": 2022,
                        "doi": "10.1/right",
                        "pmid": "",
                        "document_gate": "candidate_article",
                        "openalex_ids": ["W1"],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            paper = load_publications(corpus, canonical)["P1"]
            self.assertEqual(paper["title"], "Right paper")
            self.assertEqual(paper["year"], 2022)
            self.assertEqual(paper["pmid"], "123")
            self.assertEqual(paper["abstract"], "Exact DOI abstract enrichment.")
            self.assertEqual(paper["openalex_ids"], ["W1"])

    def test_current_canonical_metadata_has_no_known_openalex_collisions(self):
        corpus = ROOT / "scale/protocol-2.0/article-corpus.jsonl"
        canonical = ROOT / "scale/protocol-2.0/source-union.jsonl"
        if not all(path.is_file() for path in (corpus, canonical)):
            self.skipTest("Local publication data are not present.")
        papers = load_publications(corpus, canonical)
        expected = {
            "P831dfd0001ed": (
                "Measurement Properties of the EQ-5D-Y: A Systematic Review",
                {"W4283312536"},
            ),
            "P252f13cf8d71": (
                "Predictors of self-reported health-related quality of life according "
                "to the EQ-5D-Y in chronically ill children and adolescents with "
                "asthma, diabetes, and juvenile arthritis: longitudinal results",
                {"W2775004541"},
            ),
            "Pf8a24eb7c34f": (
                "Developing the EQ-5D-5L Value Set for Uganda Using the ‘Lite’ Protocol",
                {"W3217092198"},
            ),
        }
        for record_id, (title, openalex_ids) in expected.items():
            self.assertEqual(papers[record_id]["title"], title)
            self.assertEqual(set(papers[record_id]["openalex_ids"]), openalex_ids)


class JatsIdentityTest(unittest.TestCase):
    def test_exact_doi_matches(self):
        data = b"""<article><front><article-meta>
        <article-id pub-id-type="doi">10.1/example</article-id>
        <title-group><article-title>Expected title</article-title></title-group>
        </article-meta></front></article>"""
        decision, reason, title = jats_identity(
            data,
            {"doi": "10.1/example", "pmid": "", "title": "Expected title"},
        )
        self.assertEqual(decision, "MATCH")
        self.assertIn("DOI", reason)
        self.assertEqual(title, "Expected title")


class PdfTitleTest(unittest.TestCase):
    def test_title_can_span_lines_with_interleaved_column_text(self):
        title = "A Long Expected Study Title About Health and Quality of Life"
        text = """A Long Expected Study unrelated right column
Title About Health and more right column
Quality of Life"""
        self.assertTrue(title_is_ordered_in_text(title, text))


if __name__ == "__main__":
    unittest.main()
