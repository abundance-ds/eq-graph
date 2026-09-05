#!/usr/bin/env python3
"""Convert the verified full-text pilot to canonical Markdown."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PILOT = ROOT / "scale" / "protocol-2.0" / "fulltext-pilot-v1"
MARKDOWN = PILOT / "markdown"
sys.path.insert(0, str(ROOT / "scripts"))

import pdf_markdown  # noqa: E402
import to_markdown  # noqa: E402


def read_manifest() -> list[dict[str, str]]:
    with (PILOT / "MANIFEST.tsv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_markdown(row: dict[str, str], template: Path, lua: Path) -> dict[str, str]:
    source = ROOT / row["raw_path"]
    source_data = source.read_bytes()
    digest = hashlib.sha256(source_data).hexdigest()
    if digest != row["sha256"] or len(source_data) != int(row["bytes"]):
        raise ValueError(f"Source verification failed for {row['record_id']}.")

    if row["format"] == "pdf":
        body, stats = pdf_markdown.convert(source, row["title"])
        text = f"# {row['title']}\n\n{body.lstrip()}"
        converter = (
            f"pdf_markdown:{pdf_markdown.PDF_CONVERTER_VERSION};"
            f"{pdf_markdown.parser_version()}"
        )
    elif row["format"] == "xml":
        root = ET.fromstring(source_data)
        body = to_markdown.convert_body(source, template, lua)
        body, has_references = to_markdown.insert_references(
            body,
            to_markdown.references(root),
            to_markdown.ref_list_titled(root),
        )
        text = body.lstrip()
        stats = {
            "headings": len(re.findall(r"^#{1,6} ", text, re.MULTILINE)),
            "references": has_references,
        }
        converter = f"jats-pandoc:{to_markdown.pandoc_version()}"
    else:
        raise ValueError(f"Unsupported format: {row['format']}")

    if len(text.strip()) < 500:
        raise ValueError(f"Markdown is too short for {row['record_id']}.")
    path = MARKDOWN / f"{row['record_id']}.md"
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    data = path.read_bytes()
    return {
        "record_id": row["record_id"],
        "source_format": row["format"],
        "source_path": row["raw_path"],
        "source_sha256": row["sha256"],
        "markdown_path": str(path.relative_to(ROOT)),
        "markdown_bytes": str(len(data)),
        "markdown_sha256": hashlib.sha256(data).hexdigest(),
        "markdown_chars": str(len(text)),
        "converter": converter,
        "stats_json": json.dumps(stats, ensure_ascii=False, separators=(",", ":")),
    }


def main() -> None:
    MARKDOWN.mkdir(parents=True, exist_ok=True)
    rows = read_manifest()
    outputs = []
    failures = []
    with tempfile.TemporaryDirectory() as temporary:
        template = Path(temporary) / "paper.md"
        template.write_text(to_markdown.TEMPLATE, encoding="utf-8")
        lua = Path(temporary) / "demote.lua"
        lua.write_text(to_markdown.LUA_FILTER, encoding="utf-8")
        for index, row in enumerate(rows, 1):
            try:
                outputs.append(write_markdown(row, template, lua))
                print(f"converted={index}/{len(rows)} {row['record_id']}", flush=True)
            except Exception as exc:
                failures.append(
                    {
                        "record_id": row["record_id"],
                        "source_path": row["raw_path"],
                        "source_sha256": row["sha256"],
                        "error": f"{type(exc).__name__}: {str(exc)[:300]}",
                    }
                )

    failure_file = PILOT / "PARSER_FAILURES.tsv"
    known_failures = {}
    if failure_file.exists():
        with failure_file.open(encoding="utf-8", newline="") as handle:
            known_failures = {
                row["record_id"]: row
                for row in csv.DictReader(handle, delimiter="\t")
            }
    known_failures.update({row["record_id"]: row for row in failures})
    failure_fields = ["record_id", "source_path", "source_sha256", "error"]
    with failure_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=failure_fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(known_failures[key] for key in sorted(known_failures))

    fields = list(outputs[0]) if outputs else ["record_id"]
    manifest = PILOT / "PREPROCESS.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(outputs)
    summary = {
        "input_documents": len(rows),
        "converted": len(outputs),
        "failed": failures,
        "formats": {
            kind: sum(row["source_format"] == kind for row in outputs)
            for kind in ("pdf", "xml")
        },
        "preprocess_manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
        "boundary": (
            "Markdown is the AI reading copy. The verified PDF or JATS file remains "
            "the source of record. References remain in this canonical copy but can "
            "be removed from an eligibility prompt."
        ),
    }
    (PILOT / "PREPROCESS_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit("One or more documents failed conversion.")


if __name__ == "__main__":
    main()
