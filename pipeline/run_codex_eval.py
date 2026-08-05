#!/usr/bin/env python3
"""Run one saved, schema-constrained Codex evaluation and retain its audit trail."""

import argparse
import datetime as dt
import json
import pathlib
import shlex
import subprocess


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
MODEL = "gpt-5.6-terra"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", choices=["profile-verification", "pubmed-v2-profile-verification", "broad-filter", "project-assessment"])
    args = parser.parse_args()
    prompt = PILOT / "ai" / "inputs" / f"{args.name}.txt"
    schema_name = "profile-verification" if args.name == "pubmed-v2-profile-verification" else args.name
    schema = PILOT / "ai" / "schemas" / f"{schema_name}.schema.json"
    output = PILOT / "ai" / "outputs" / f"{args.name}.json"
    trace_dir = PILOT / "ai" / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    trace = trace_dir / f"{args.name}.jsonl"
    stderr = trace_dir / f"{args.name}.stderr.txt"
    metadata = trace_dir / f"{args.name}.run.json"
    version = subprocess.run(["codex", "--version"], capture_output=True, text=True, check=True).stdout.strip()
    command = [
        "codex", "exec", "--ephemeral", "--sandbox", "read-only",
        "--skip-git-repo-check", "--json", "-c", 'web_search="disabled"', "-m", MODEL,
        "--output-schema", str(schema), "-o", str(output), "-",
    ]
    started = dt.datetime.now(dt.timezone.utc)
    with open(prompt) as stdin, open(trace, "w") as stdout, open(stderr, "w") as err:
        result = subprocess.run(command, cwd=ROOT, stdin=stdin, stdout=stdout, stderr=err, text=True)
    ended = dt.datetime.now(dt.timezone.utc)
    metadata.write_text(json.dumps({
        "name": args.name, "model": MODEL, "codex_version": version,
        "command": shlex.join(command), "prompt": str(prompt.relative_to(ROOT)),
        "schema": str(schema.relative_to(ROOT)), "output": str(output.relative_to(ROOT)),
        "trace": str(trace.relative_to(ROOT)), "started_utc": started.isoformat(),
        "ended_utc": ended.isoformat(), "return_code": result.returncode,
    }, indent=2))
    if result.returncode:
        raise SystemExit(f"Codex failed ({result.returncode}); see {stderr}")
    json.loads(output.read_text())
    print(output)


if __name__ == "__main__":
    main()
