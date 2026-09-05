#!/usr/bin/env python3
"""Expose full-text ingestion as two native Claude Code tools."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from fulltext_ingest_tool import build_submit_schema, reject, submit


def response(request_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    }


def tools() -> list[dict[str, Any]]:
    return [
        {
            "name": "submit",
            "description": (
                "Validate and save an eligible paper record. Correct and resubmit "
                "when the result names validation errors."
            ),
            "inputSchema": build_submit_schema(),
        },
        {
            "name": "reject",
            "description": "Save the paper as ineligible with a short reason.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "reason": {"type": "string", "minLength": 1},
                },
                "required": ["reason"],
                "additionalProperties": False,
            },
        },
    ]


def call_tool(
    context_path: Path,
    name: str,
    arguments: dict[str, Any],
) -> dict[str, Any]:
    if name == "submit":
        success, message = submit(context_path, arguments)
    elif name == "reject":
        reason = arguments.get("reason")
        if not isinstance(reason, str):
            success, message = False, "reason must be a string"
        else:
            success, message = reject(context_path, reason)
    else:
        return {
            "content": [{"type": "text", "text": f"Unknown tool: {name}"}],
            "isError": True,
        }
    return {
        "content": [{"type": "text", "text": message}],
        "isError": not success,
    }


def handle(context_path: Path, message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    request_id = message.get("id")
    if method == "initialize":
        params = message.get("params", {})
        return response(
            request_id,
            {
                "protocolVersion": params.get("protocolVersion", "2025-06-18"),
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "eq-fulltext-ingest",
                    "version": "1.0.0",
                },
            },
        )
    if method in {
        "notifications/initialized",
        "notifications/cancelled",
        "notifications/roots/list_changed",
    }:
        return None
    if method == "ping":
        return response(request_id, {})
    if method == "tools/list":
        return response(request_id, {"tools": tools()})
    if method == "tools/call":
        params = message.get("params", {})
        name = params.get("name")
        arguments = params.get("arguments", {})
        if not isinstance(name, str) or not isinstance(arguments, dict):
            return error(request_id, -32602, "Invalid tool arguments")
        return response(request_id, call_tool(context_path, name, arguments))
    if request_id is None:
        return None
    return error(request_id, -32601, f"Method not found: {method}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", type=Path, required=True)
    args = parser.parse_args()
    if not args.context.is_file():
        raise FileNotFoundError(args.context)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
            result = handle(args.context, message)
        except Exception as exception:  # Keep the server alive for the next request.
            request_id = message.get("id") if isinstance(message, dict) else None
            result = error(request_id, -32603, str(exception))
        if result is not None:
            print(json.dumps(result, ensure_ascii=False, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
