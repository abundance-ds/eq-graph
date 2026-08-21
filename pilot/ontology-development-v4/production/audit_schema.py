#!/usr/bin/env python3
"""Build the compact output schema for one source-audit batch."""

from __future__ import annotations

import json


def build_audit_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {
            "batch_id": {"type": "string", "minLength": 1},
            "audits": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "properties": {
                        "record_id": {"type": "string", "minLength": 1},
                        "verdict": {"type": "string", "enum": ["PASS", "MINOR", "MAJOR"]},
                        "source_locations": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "repair": {"type": ["string", "null"]},
                        "ontology_gap": {"type": ["string", "null"]},
                    },
                    "required": [
                        "record_id",
                        "verdict",
                        "source_locations",
                        "repair",
                        "ontology_gap",
                    ],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["batch_id", "audits"],
        "additionalProperties": False,
    }


if __name__ == "__main__":
    print(json.dumps(build_audit_schema(), ensure_ascii=False, indent=2))
