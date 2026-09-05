from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pikepdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import pdf_markdown


class CMapTests(unittest.TestCase):
    def test_reads_bfchar_and_array_bfrange(self) -> None:
        source = b"""begincmap
2 beginbfchar
<01> <2212>
<02> <003C>
endbfchar
1 beginbfrange
<14> <16> [<FFFD> <0061> <0062>]
endbfrange
endcmap
"""
        with pikepdf.new() as pdf:
            font = pikepdf.Dictionary()
            font["/ToUnicode"] = pdf.make_stream(source)

            mapping = pdf_markdown.existing_mapping(font)

        self.assertEqual(mapping[0x01], "−")
        self.assertEqual(mapping[0x02], "<")
        self.assertEqual(mapping[0x14], "�")
        self.assertEqual(mapping[0x15], "a")
        self.assertEqual(mapping[0x16], "b")

    def test_builds_a_one_byte_cmap(self) -> None:
        output = pdf_markdown.build_tounicode(
            {0x02: "−", 0x24: "≥"}, "TestMap"
        ).decode("ascii")

        self.assertIn("<00> <FF>", output)
        self.assertIn("<02> <2212>", output)
        self.assertIn("<24> <2265>", output)

    def test_builds_a_two_byte_cmap(self) -> None:
        output = pdf_markdown.build_tounicode(
            {0x1234: "β"}, "WideTestMap", code_width=2
        ).decode("ascii")

        self.assertIn("<0000> <FFFF>", output)
        self.assertIn("<1234> <03B2>", output)


class RepairSelectionTests(unittest.TestCase):
    def test_uses_glyph_name_when_raw_codes_have_different_meanings(self) -> None:
        font = pikepdf.Dictionary(
            BaseFont=pikepdf.Name("/ABCDEF+AdvP4C4E74"),
            FirstChar=1,
            LastChar=4,
            Encoding=pikepdf.Dictionary(
                Differences=pikepdf.Array(
                    [1, pikepdf.Name("/C15"), pikepdf.Name("/C21")]
                )
            ),
        )

        family, repairs = pdf_markdown.repairs_for_font(font)

        self.assertEqual(family, "AdvP4C4E74")
        self.assertEqual(repairs, {1: "•", 2: "≥"})


class MarkdownAssemblyTests(unittest.TestCase):
    def test_drops_only_a_verified_leading_cover(self) -> None:
        chunks = [
            {"text": "White Rose Research Online URL for this paper"},
            {"text": "Article title\n\nAbstract"},
        ]

        kept, count = pdf_markdown.drop_cover_chunks(chunks)

        self.assertEqual(count, 1)
        self.assertEqual(kept, chunks[1:])

    def test_keeps_a_publisher_title_page(self) -> None:
        chunks = [
            {"text": "Article in Press\n\nArticle title\n\nAuthors"},
            {"text": "Methods"},
        ]

        kept, count = pdf_markdown.drop_cover_chunks(chunks)

        self.assertEqual(count, 0)
        self.assertEqual(kept, chunks)

    def test_joins_a_positioned_acute_accent(self) -> None:
        text = "Maja Kuhari<sup>\uE000</sup> c, PhD"

        self.assertEqual(
            pdf_markdown.fix_detached_accents(text), "Maja Kuharić, PhD"
        )

    def test_keeps_page_numbers_and_one_level_one_title(self) -> None:
        chunks = [
            {
                "metadata": {"page_number": 2},
                "text": "# A Long Article Title\n\n# Methods\n\nBody",
            }
        ]

        output = pdf_markdown.chunks_to_markdown(chunks, "A Long Article Title")

        self.assertIn("<!-- source-page: 2 -->", output)
        self.assertNotIn("# A Long Article Title", output)
        self.assertIn("## Methods", output)


class CorpusRegressionTests(unittest.TestCase):
    """Run source regressions when the private input PDFs are present."""

    SOURCES = {
        "1455": ROOT
        / "input/projects/1455-RA/papers/doi_10.1016_j.jval.2024.05.007.pdf",
        "442": ROOT
        / "input/projects/442-RA/papers/doi_10.1016_j.vhri.2025.101543.pdf",
        "1883": ROOT
        / "input/projects/1883-RA/papers/doi_10.1177_0272989x261446644.pdf",
        "1508": ROOT
        / "input/projects/1508-RA/papers/doi_10.12688_wellcomeopenres.21408.2.pdf",
        "actual_text": ROOT
        / "input/projects/20180080/papers/doi_10.21203_rs.3.rs-2423517_v1.pdf",
        "font_scope": ROOT
        / "input/projects/214-RA/papers/doi_10.1016_j.jval.2022.05.013.pdf",
    }

    @classmethod
    def setUpClass(cls) -> None:
        if not all(path.exists() for path in cls.SOURCES.values()):
            raise unittest.SkipTest("private PDF regression sources are not present")
        cls.outputs = {
            name: pdf_markdown.convert(path) for name, path in cls.SOURCES.items()
        }

    def test_elsevier_statistical_symbols_and_tables(self) -> None:
        body, stats = self.outputs["1455"]

        self.assertIn("rs ≥ 0.5", body)
        self.assertIn("P < .001", body)
        self.assertIn("−0.384", body)
        self.assertEqual(stats["cover_sheet_pages_dropped"], 1)
        self.assertGreaterEqual(stats["tables"], 1)
        self.assertEqual(stats["replacement_characters"], 0)

    def test_value_in_health_thresholds_and_detached_accent(self) -> None:
        body, stats = self.outputs["442"]

        self.assertIn("(<80 vs ≥80)", body)
        self.assertIn("Kuharić M", body)
        self.assertGreaterEqual(stats["tables"], 1)
        self.assertEqual(stats["replacement_characters"], 0)

    def test_sage_letters_thresholds_and_copyright(self) -> None:
        body, stats = self.outputs["1883"]

        self.assertIn("Michał Jakubczyk", body)
        self.assertIn("age ≥17", body)
        self.assertIn("|≥80|", body)
        self.assertIn("|<80|", body)
        self.assertIn("© The Author(s) 2026", body)
        self.assertEqual(stats["replacement_characters"], 0)

    def test_f1000_formula_signs(self) -> None:
        body, stats = self.outputs["1508"]

        self.assertIn("−0.384", body)
        self.assertIn("∑", body)
        self.assertEqual(stats["replacement_characters"], 0)

    def test_promotes_unambiguous_actual_text_ligatures(self) -> None:
        body, stats = self.outputs["actual_text"]

        self.assertIn("financial burden", body)
        self.assertIn("difficult", body)
        self.assertGreater(stats["font_codes_repaired"], 0)
        self.assertEqual(stats["replacement_characters"], 0)

    def test_limits_a_shared_font_repair_to_the_verified_object(self) -> None:
        body, stats = self.outputs["font_scope"]

        self.assertIn("Katarzyna Młynczak", body)
        self.assertNotIn(pdf_markdown.DETACHED_ACUTE, body)
        self.assertNotIn(pdf_markdown.INVISIBLE_GLYPH, body)
        self.assertEqual(stats["replacement_characters"], 0)


if __name__ == "__main__":
    unittest.main()
