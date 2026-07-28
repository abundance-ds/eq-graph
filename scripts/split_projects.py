#!/usr/bin/env python3
"""Split the EuroQol funded-projects CSV into one directory per project.

Regenerable and idempotent: rerunning overwrites the generated files in place.
Only the CSV is read; no network access.

Output layout (see input/projects/README.md):

    input/projects/index.json
    input/projects/<Project Id>/project.json
    input/projects/<Project Id>/abstract.txt   # omitted when the CSV cell is empty
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CSV_PATH = REPO / "input" / "Funded projects – Table for Download - EuroQol.csv"
OUT_DIR = REPO / "input" / "projects"

SOURCE_URL = (
    "https://euroqol.org/research-at-euroqol/our-research-portfolio/"
    "funded-projects-download/"
)

# Working Group is a multi-value field joined with ", " — but "Dissemination, OA fee"
# is a single group whose own name contains a comma, so a naive split is wrong.
# Longest-first matching against the closed vocabulary keeps it intact.
WORKING_GROUPS = sorted(
    [
        "Dissemination, OA fee",
        "Populations and Health Systems",
        "Education and Outreach",
        "Descriptive Systems",
        "Valuation",
        "EQ-HWB",
        "Youth",
        "Others",
    ],
    key=len,
    reverse=True,
)

# Grant type suffix, per Appendix 3 of the EuroQol Call for Proposals.
# Absent for the older year-prefixed id scheme (projects starting 2012-2022).
GRANT_TYPES = {
    "RA": "1.1 Regular research project",
    "VS": "1.2 Valuation study",
    "SG": "1.3 Seed grants",
    "BT": "1.4 Bolt-on Toolbox validation",
    "PHD": "2.1 PhD grant",
    "PD": "2.2 Postdoctoral grant",
    "TVG": "2.3 Travel grant",
    "EO": "3.1 Education and outreach project",
    "EOI": "3.3 Expression of interest form for regional events",
    "TR": "4.1 Tools and resources",
    "PCG": "4.2 Program coordination grants",
}

# "1489-RA", "215-2020RA" (call year embedded), "20190670", "20180340R1" (revision).
ID_SUFFIX_RE = re.compile(r"^(?P<seq>\d+)-(?P<year>\d{4})?(?P<code>[A-Z]+)$")
ID_PLAIN_RE = re.compile(r"^(?P<base>\d+)(?:R(?P<rev>\d+))?$")


def parse_working_groups(raw: str) -> list[str]:
    """Split the multi-value Working Group cell into its constituent groups."""
    rest = raw.strip()
    found: list[str] = []
    while rest:
        for group in WORKING_GROUPS:
            if rest == group or rest.startswith(group + ", "):
                found.append(group)
                rest = rest[len(group) :].removeprefix(", ")
                break
        else:
            raise ValueError(f"unrecognised Working Group value: {raw!r} (at {rest!r})")
    return found


def parse_project_id(project_id: str) -> dict:
    """Derive the id scheme, grant type and revision marker from a Project Id."""
    if m := ID_SUFFIX_RE.match(project_id):
        code = m.group("code")
        if code not in GRANT_TYPES:
            raise ValueError(f"unknown grant type suffix in {project_id!r}: {code!r}")
        return {
            "id_scheme": "sequence-suffix",
            "sequence_number": int(m.group("seq")),
            "call_year": int(m.group("year")) if m.group("year") else None,
            "grant_type_code": code,
            "grant_type": GRANT_TYPES[code],
            "revision": None,
        }
    if m := ID_PLAIN_RE.match(project_id):
        return {
            "id_scheme": "year-number",
            "sequence_number": None,
            "call_year": None,
            "grant_type_code": None,
            "grant_type": None,
            "revision": int(m.group("rev")) if m.group("rev") else None,
        }
    raise ValueError(f"unparseable Project Id: {project_id!r}")


def as_int(value: str, field: str, project_id: str) -> int | None:
    value = value.strip()
    if not value:
        return None
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{field} not an integer in {project_id!r}: {value!r}") from exc


def build_record(row: dict[str, str], row_number: int) -> dict:
    project_id = row["Project Id"].strip()
    abstract = row["Abstract"].strip()
    record = {
        "project_id": project_id,
        **parse_project_id(project_id),
        "title": row["Title"].strip(),
        "pi_name_raw": row["Project PI / Applicant Name"].strip(),
        "working_groups": parse_working_groups(row["Working Group"]),
        "approved_budget_eur": as_int(
            row["Approved Budget (EUR)"], "Approved Budget (EUR)", project_id
        ),
        "status": row["Status"].strip(),
        "start_year": as_int(row["Start Year"], "Start Year", project_id),
        "end_year": as_int(row["End Year"], "End Year", project_id),
        "has_abstract": bool(abstract),
        "source": {
            "file": CSV_PATH.name,
            "row": row_number,
            "url": SOURCE_URL,
        },
    }
    return record, abstract


def write_if_changed(path: Path, content: str) -> bool:
    """Write only when content differs, so reruns leave mtimes and git alone."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    index: list[dict] = []
    seen: set[str] = set()
    written = 0

    for offset, row in enumerate(rows):
        record, abstract = build_record(row, row_number=offset + 2)  # +2: header is line 1
        project_id = record["project_id"]
        if project_id in seen:
            raise ValueError(f"duplicate Project Id: {project_id!r}")
        seen.add(project_id)

        project_dir = OUT_DIR / project_id
        project_dir.mkdir(exist_ok=True)

        written += write_if_changed(
            project_dir / "project.json",
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
        )

        abstract_path = project_dir / "abstract.txt"
        if abstract:
            written += write_if_changed(abstract_path, abstract + "\n")
        elif abstract_path.exists():
            abstract_path.unlink()

        index.append(
            {
                key: record[key]
                for key in (
                    "project_id",
                    "title",
                    "pi_name_raw",
                    "working_groups",
                    "grant_type_code",
                    "status",
                    "start_year",
                    "end_year",
                    "approved_budget_eur",
                    "has_abstract",
                )
            }
        )

    write_if_changed(
        OUT_DIR / "index.json",
        json.dumps(
            {
                "source": {"file": CSV_PATH.name, "url": SOURCE_URL},
                "count": len(index),
                "projects": index,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
    )

    stale = {p.name for p in OUT_DIR.iterdir() if p.is_dir()} - seen
    if stale:
        print(f"warning: {len(stale)} directories not in the CSV: {sorted(stale)}",
              file=sys.stderr)

    print(f"{len(index)} projects in {OUT_DIR}, {written} files written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
