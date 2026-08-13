"""Shared person-name normalization for Phase 1."""

import re


TITLE_SUFFIX = re.compile(r"\s*,?\s*(phd|ph\.?\s*d\.?|msc|md|dr\.?|prof\.?)\s*$", re.I)
TITLE_PREFIX = re.compile(r"^(?:(?:prof(?:essor)?|dr)\.?\s*)+", re.I)


def norm(name: str) -> str:
    n = re.sub(r"\s+", " ", name).strip()
    n = TITLE_PREFIX.sub("", n).strip()
    n = TITLE_SUFFIX.sub("", n).strip().strip(",")
    if "," in n:
        last, _, first = n.partition(",")
        n = f"{first.strip()} {last.strip()}"
    m = re.search(r"\(([^)]+)\)", n)
    if m:
        rest = re.sub(r"^[A-Z.\s]+\(", "(", n)
        n = (m.group(1) + " " + n[m.end():].strip()) if rest.startswith("(") else re.sub(r"\s*\([^)]*\)", "", n)
        n = re.sub(r"\s+", " ", n).strip()
    return n


def key(name: str) -> str:
    return norm(name).casefold()
