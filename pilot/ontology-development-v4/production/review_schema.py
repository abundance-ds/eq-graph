#!/usr/bin/env python3
"""Build the output schema for source review and correction."""

from __future__ import annotations

import json

from schema import build_schema


def build_review_schema() -> dict:
    record_schema = build_schema()
    record_schema.pop("$schema", None)
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {
            "record_id": {"type": "string", "minLength": 1},
            "draft_verdict": {
                "type": "string",
                "enum": ["PASS", "MINOR", "MAJOR"],
            },
            "corrections": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
            },
            "ontology_gaps": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
            },
            "source_locations": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
            },
            "record": record_schema,
        },
        "required": [
            "record_id",
            "draft_verdict",
            "corrections",
            "ontology_gaps",
            "source_locations",
            "record",
        ],
        "additionalProperties": False,
    }


if __name__ == "__main__":
    print(json.dumps(build_review_schema(), ensure_ascii=False, indent=2))
