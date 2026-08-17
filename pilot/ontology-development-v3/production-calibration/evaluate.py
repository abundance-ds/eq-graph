#!/usr/bin/env python3
"""Evaluate one-pass calibration records without another AI pass."""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CALIBRATION = Path(__file__).resolve().parent

INCLUDE_HEADINGS = [
    "### Study",
    "### Population and data",
    "### Instruments and administration",
    "### Methods and analysis",
    "### Products and concepts",
    "### Outcomes and findings",
    "### Limitations and source issues",
    "### High-value terms",
]

VALID = {
    "disposition": {"include-study", "publication-context", "exclude", "unclear"},
    "connection": {
        "direct_eq",
        "adjacent_measurement",
        "application_only",
        "unrelated",
        "unclear",
    },
    "euroqol support": {"explicit", "other-funding-only", "none-stated", "unclear"},
    "project link": {"explicit", "probable", "possible", "none", "unclear"},
}

EXPECTED_DISPOSITION = {
    **{f"H{i:02d}": "include-study" for i in range(1, 11)},
    **{f"B{i:02d}": "include-study" for i in range(1, 21)},
    "H09": "exclude",
    "B17": "publication-context",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).casefold()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(re.findall(r"[a-z0-9]+", text))


def stemmed(text: str) -> str:
    tokens = normalize(text).split()
    return " ".join(
        token[:-1]
        if len(token) > 4 and token.endswith("s") and not token.endswith(("ss", "us", "is"))
        else token
        for token in tokens
    )


def term_present(term: str, text: str) -> bool:
    variants = [term]
    for before, inside in re.findall(r"^(.*?)\s*\(([^)]+)\)", term):
        variants.extend([before, inside])
    if " / " in term:
        variants.extend(term.split(" / "))
    normalized_text = f" {normalize(text)} "
    stemmed_text = f" {stemmed(text)} "
    for variant in variants:
        normalized_variant = normalize(variant)
        if len(normalized_variant) >= 2 and f" {normalized_variant} " in normalized_text:
            return True
        stemmed_variant = stemmed(variant)
        if len(stemmed_variant) >= 2 and f" {stemmed_variant} " in stemmed_text:
            return True
    return False


SOURCE_SECTION = (
    r"abstract|introduction|background|methods?|materials?|experiment|analysis|results?|"
    r"discussion|conclusions?|funding|acknowledg(?:e)?ments?|metadata|front matter|"
    r"declarations?|disclosures?|conflicts? of interest|data availability|appendix|"
    r"supplements?|tables?|figures?|references?|candidate project"
)


def extract_source_locator(text: str) -> str | None:
    """Return a trailing article locator in the formats used by pilot records."""
    patterns = (
        r"\*\*Source:\*\*\s*[^\n]{2,}\.?$",
        r"\[[^\]\n]{2,}\]\.?$",
        rf"\([^)]*(?:{SOURCE_SECTION})[^)]*\)\.?$",
        rf"(?:^|(?<=[.!?])\s+)((?:(?:{SOURCE_SECTION})\b[^.!?\n]{{0,180}}(?:;\s*)?)+)\.?$",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(0).strip()
    return None


def source_locator_coverage(text: str) -> tuple[int, int]:
    if "### Study" not in text:
        return (0, 0)
    body = text.split("### Study", 1)[1].split("### High-value terms", 1)[0]
    bullets: list[str] = []
    current = ""
    for raw in body.splitlines():
        if re.match(r"^\s*-\s+", raw):
            if current:
                bullets.append(current)
            current = re.sub(r"^\s*-\s+", "", raw).strip()
        elif current and raw.strip() and not raw.startswith("### "):
            current += " " + raw.strip()
    if current:
        bullets.append(current)
    located = sum(extract_source_locator(bullet) is not None for bullet in bullets)
    return located, len(bullets)


def clean_value(value: str) -> str:
    value = value.strip().strip("`*_ ")
    return value.rstrip(". ;:").casefold()


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_usage(path: Path) -> dict[str, int]:
    usage: dict[str, int] = {}
    if not path.is_file():
        return usage
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            usage = {
                key: int(value)
                for key, value in event["usage"].items()
                if isinstance(value, int)
            }
    return usage


def parse_labels(text: str) -> dict[str, str]:
    labels: dict[str, str] = {}
    assessment = text.split("### Study", 1)[0]
    for label in ("Disposition", "Connection", "EuroQol support", "Support scope", "Project link", "Publication status", "Evidence"):
        match = re.search(rf"^- {re.escape(label)}:\s*(.+)$", assessment, flags=re.MULTILINE | re.IGNORECASE)
        if match:
            labels[label.casefold()] = match.group(1).strip()
    return labels


def first_class(value: str, allowed: set[str]) -> str:
    lowered = clean_value(value)
    for item in sorted(allowed, key=len, reverse=True):
        if re.search(rf"(?<![a-z0-9_-]){re.escape(item)}(?![a-z0-9_-])", lowered):
            return item
    return ""


def reference_terms(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"^##(?:\s+\d+\.)?\s+High-value exact terms\s*$\n(.*?)(?=^##\s|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return []

    bullets: list[str] = []
    current = ""
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line:
            continue
        if re.match(r"^[-*]\s+", line):
            if current:
                bullets.append(current)
            current = re.sub(r"^[-*]\s+", "", line)
        else:
            current = f"{current} {line}".strip()
    if current:
        bullets.append(current)

    terms: list[str] = []
    for bullet in bullets:
        bullet = re.sub(r"\[[^\]]+\]\s*$", "", bullet)
        quoted = re.findall(r"[“\"]([^”\"]+)[”\"]", bullet)
        if quoted:
            terms.extend(value.strip() for value in quoted if value.strip())
            continue
        bullet = re.split(r"\s+[—–]\s+", bullet, maxsplit=1)[0]
        for term in bullet.split(";"):
            term = term.strip().strip("`*_ .")
            if term:
                terms.append(term)
    return terms


def check_contains(text: str, *patterns: str) -> bool:
    return all(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) for pattern in patterns)


def safety_checks(record_id: str, text: str, parsed: dict[str, str]) -> list[dict[str, object]]:
    support = first_class(parsed.get("euroqol support", ""), VALID["euroqol support"])
    project = first_class(parsed.get("project link", ""), VALID["project link"])
    status = parsed.get("publication status", "")
    checks: list[tuple[str, bool]] = []

    if record_id == "B01":
        checks += [
            ("travel-grant scope", check_contains(parsed.get("support scope", ""), r"travel[ -]?grant")),
            ("project 1483-TVG", "1483-tvg" in text.casefold()),
            ("support explicit", support == "explicit"),
        ]
    elif record_id == "B02":
        support_scope = parsed.get("support scope", "")
        checks += [
            (
                "author-level scope retained",
                check_contains(text, r"(?:author|Ngwira(?:['’]s)?\s+work)", r"20190200"),
            ),
            (
                "does not claim full-study funding",
                check_contains(
                    support_scope,
                    r"(?:does\s+not|not)\s+(?:state|claim).{0,80}fund(?:ed|ing).{0,40}(?:full|whole|entire)\s+study",
                )
                or not check_contains(
                    support_scope,
                    r"fund(?:ed|ing)\s+(?:the\s+)?(?:full|whole|entire)?\s*study",
                ),
            ),
        ]
    elif record_id == "B05":
        checks += [
            ("author-level support retained", support == "explicit" and check_contains(text, r"285-PHD")),
            ("scope is not full-study funding", not check_contains(parsed.get("support scope", ""), r"fund(?:ed|ing)\s+(?:this|the)\s+(?:research|study)")),
        ]
    elif record_id == "B09":
        checks.append(
            (
                "significance-reporting conflict",
                check_contains(text, r"not\s+(?:statistically\s+)?significant", r"p[ -]?values?\s*<?\s*\.?0?5|0\.023", r"conflict|inconsisten"),
            )
        )
    elif record_id == "B10":
        checks += [("JATS funding recovered", support == "explicit"), ("project 348-PHD", "348-phd" in text.casefold())]
    elif record_id == "B11":
        checks += [("JATS funding recovered", support == "explicit"), ("project 1787-RA", "1787-ra" in text.casefold())]
    elif record_id == "B12":
        checks += [
            ("data-collection scope", check_contains(parsed.get("support scope", ""), r"data[ -]?collection")),
            ("project 1644-RA", "1644-ra" in text.casefold()),
        ]
    elif record_id == "B16":
        checks += [
            ("retraction status", "retract" in status.casefold()),
            ("unsafe-use warning", check_contains(text, r"unsafe|not\s+(?:safe|approved)|must\s+not|do\s+not\s+use")),
        ]
    elif record_id == "B17":
        checks += [
            ("correction relation", check_contains(text, r"correct(?:s|ion)", r"10\.1371/journal\.pone\.0209344")),
            ("project 2016440", "2016440" in text),
        ]
    elif record_id == "B18":
        checks.append(("no false EuroQol funding", support != "explicit"))
    elif record_id == "H09":
        checks += [
            ("no false EuroQol funding", support != "explicit"),
            ("no asserted project link", project not in {"explicit", "probable"}),
            ("no false EQ instrument use", not check_contains(text, r"EQ-5D.{0,80}(?:administered|scored|measured|used as an instrument)")),
        ]

    return [{"name": name, "passed": passed} for name, passed in checks]


def evaluate(
    run_name: str,
    manifest_name: str,
    overlay_runs: list[str] | None = None,
) -> dict[str, object]:
    run_dir = CALIBRATION / run_name
    overlay_dirs = [CALIBRATION / value for value in (overlay_runs or [])]
    records_dir = run_dir / "records"
    rows: list[dict[str, object]] = []

    for item in read_manifest(CALIBRATION / manifest_name):
        record_id = item["record_id"]
        output_path = records_dir / f"{record_id}.md"
        selected_run_dir = run_dir
        for overlay_dir in overlay_dirs:
            candidate = overlay_dir / "records" / f"{record_id}.md"
            if candidate.is_file():
                output_path = candidate
                selected_run_dir = overlay_dir
        row: dict[str, object] = {
            "record_id": record_id,
            "doi": item["doi"],
            "output_path": str(output_path.relative_to(ROOT)),
        }
        if not output_path.exists():
            row.update({"exists": False, "errors": ["missing output"]})
            rows.append(row)
            continue

        text = output_path.read_text(encoding="utf-8")
        parsed = parse_labels(text)
        classes = {key: first_class(parsed.get(key, ""), allowed) for key, allowed in VALID.items()}
        errors: list[str] = []
        if not text.startswith("### Assessment\n"):
            errors.append("output does not start with Assessment")
        for label in ("disposition", "connection", "euroqol support", "support scope", "project link", "publication status", "evidence"):
            if label not in parsed:
                errors.append(f"missing label: {label}")
        for label, allowed in VALID.items():
            if label in parsed and not classes[label]:
                errors.append(f"invalid class: {label}")

        disposition = classes["disposition"]
        headings_present = [heading for heading in INCLUDE_HEADINGS if heading in text]
        if disposition == "include-study":
            for heading in INCLUDE_HEADINGS:
                if heading not in text:
                    errors.append(f"missing heading: {heading}")
        elif disposition in {"exclude", "publication-context"} and headings_present:
            errors.append("context or excluded output contains study extraction headings")
        if "TODO" in text or "TBD" in text:
            errors.append("placeholder present")
        if any(line.endswith((" ", "\t")) for line in text.splitlines()):
            errors.append("trailing whitespace")
        reference_path = ROOT / item["reference_path"]
        terms = reference_terms(reference_path) if disposition == "include-study" else []
        found_terms = [term for term in terms if term_present(term, text)]
        missed_terms = [term for term in terms if term not in found_terms]
        safety = safety_checks(record_id, text, parsed)
        expected = EXPECTED_DISPOSITION[record_id]
        located_bullets, substantive_bullets = source_locator_coverage(text)

        row.update(
            {
                "exists": True,
                "classes": classes,
                "expected_disposition": expected,
                "disposition_match": disposition == expected,
                "headings_present": len(headings_present),
                "errors": errors,
                "reference_term_count": len(terms),
                "term_hits": len(found_terms),
                "term_recall": round(len(found_terms) / len(terms), 4) if terms else None,
                "missed_terms": missed_terms,
                "located_bullets": located_bullets,
                "substantive_bullets": substantive_bullets,
                "source_locator_rate": round(located_bullets / substantive_bullets, 4)
                if substantive_bullets
                else None,
                "word_count": len(text.split()),
                "usage": read_usage(selected_run_dir / "traces" / f"{record_id}.jsonl"),
                "safety_checks": safety,
            }
        )
        rows.append(row)

    existing = [row for row in rows if row.get("exists")]
    term_total = sum(int(row.get("reference_term_count", 0)) for row in existing)
    hit_total = sum(int(row.get("term_hits", 0)) for row in existing)
    safety_total = sum(len(row.get("safety_checks", [])) for row in existing)
    safety_hits = sum(
        int(check["passed"])
        for row in existing
        for check in row.get("safety_checks", [])
    )
    located_total = sum(int(row.get("located_bullets", 0)) for row in existing)
    substantive_total = sum(int(row.get("substantive_bullets", 0)) for row in existing)
    classes = {
        key: dict(Counter(row.get("classes", {}).get(key, "missing") for row in existing))
        for key in VALID
    }
    usage_keys = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
    usage = {
        key: sum(int(row.get("usage", {}).get(key, 0)) for row in existing)
        for key in usage_keys
    }
    word_total = sum(int(row.get("word_count", 0)) for row in existing)
    summary = {
        "run": run_name,
        "records_expected": len(rows),
        "records_present": len(existing),
        "structurally_clean": sum(not row.get("errors") for row in existing),
        "disposition_matches": sum(bool(row.get("disposition_match")) for row in existing),
        "term_hits": hit_total,
        "term_total": term_total,
        "weighted_term_recall": round(hit_total / term_total, 4) if term_total else None,
        "source_locators": located_total,
        "substantive_bullets": substantive_total,
        "source_locator_rate": round(located_total / substantive_total, 4)
        if substantive_total
        else None,
        "safety_checks_passed": safety_hits,
        "safety_checks_total": safety_total,
        "output_words": word_total,
        "mean_output_words": round(word_total / len(existing), 1) if existing else None,
        "usage": usage,
        "class_counts": classes,
    }
    return {"summary": summary, "records": rows}


def write_markdown(result: dict[str, object], path: Path) -> None:
    summary = result["summary"]
    records = result["records"]
    lines = [
        "# One-pass calibration evaluation",
        "",
        "## Deterministic results",
        "",
        f"- Records present: {summary['records_present']}/{summary['records_expected']}.",
        f"- Structurally clean: {summary['structurally_clean']}/{summary['records_present']}.",
        f"- Expected dispositions: {summary['disposition_matches']}/{summary['records_present']}.",
        f"- High-value term coverage: {summary['term_hits']}/{summary['term_total']} ({summary['weighted_term_recall']:.1%}).",
        f"- Source locators on substantive bullets: {summary['source_locators']}/{summary['substantive_bullets']} ({summary['source_locator_rate']:.1%}).",
        f"- Critical safety checks: {summary['safety_checks_passed']}/{summary['safety_checks_total']}.",
        f"- Mean study record length: {summary['mean_output_words']:,.0f} words.",
        f"- Model tokens: {summary['usage']['input_tokens']:,} input and {summary['usage']['output_tokens']:,} output.",
        "",
        "Term coverage accepts exact phrases, acronyms, and singular or plural forms. It is not a correctness score.",
        "",
        "## Record results",
        "",
        "| ID | Disposition | Expected | Structure | Exact terms | Safety |",
        "|---|---|---|---:|---:|---:|",
    ]
    for row in records:
        if not row.get("exists"):
            lines.append(f"| {row['record_id']} | missing | {EXPECTED_DISPOSITION[row['record_id']]} | fail | — | — |")
            continue
        safety = row.get("safety_checks", [])
        safety_text = f"{sum(int(c['passed']) for c in safety)}/{len(safety)}" if safety else "—"
        term_text = (
            f"{row['term_hits']}/{row['reference_term_count']}"
            if row["reference_term_count"]
            else "—"
        )
        lines.append(
            f"| {row['record_id']} | {row['classes']['disposition']} | {row['expected_disposition']} | "
            f"{'pass' if not row['errors'] else 'fail'} | {term_text} | {safety_text} |"
        )

    flagged = [
        row for row in records
        if (not row.get("exists") or row.get("errors") or not row.get("disposition_match")
            or any(not check["passed"] for check in row.get("safety_checks", [])))
    ]
    lines += ["", "## Records for targeted review", ""]
    if not flagged:
        lines.append("None from deterministic checks.")
    for row in flagged:
        reasons = list(row.get("errors", []))
        if row.get("exists") and not row.get("disposition_match"):
            reasons.append(
                f"disposition {row['classes']['disposition']} instead of {row['expected_disposition']}"
            )
        reasons += [check["name"] for check in row.get("safety_checks", []) if not check["passed"]]
        lines.append(f"- {row['record_id']}: {'; '.join(reasons)}.")

    lines += ["", "## Lowest exact-term coverage", ""]
    ranked = sorted(
        (row for row in records if row.get("exists") and row.get("term_recall") is not None),
        key=lambda row: row["term_recall"],
    )[:10]
    for row in ranked:
        missed = "; ".join(row["missed_terms"][:6]) or "none"
        lines.append(
            f"- {row['record_id']}: {row['term_hits']}/{row['reference_term_count']} "
            f"({row['term_recall']:.0%}); missed examples: {missed}."
        )

    lines += [
        "",
        "## Manual review",
        "",
        "Pending source-level review of flagged records and a balanced sample of passing records.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", default="run-01")
    parser.add_argument("--manifest", default="MANIFEST.tsv")
    parser.add_argument("--overlay-run", action="append", default=[])
    args = parser.parse_args()
    if Path(args.manifest).name != args.manifest:
        raise ValueError("manifest name must not contain a path")
    result = evaluate(args.run, args.manifest, args.overlay_run)
    run_dir = CALIBRATION / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "EVALUATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, run_dir / "EVALUATION.md")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
