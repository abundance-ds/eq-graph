#!/usr/bin/env python3
"""Run full-text assessment batches and aggregate validated submissions."""

import argparse
import concurrent.futures
import csv
import datetime as dt
import json
import pathlib
import shlex
import subprocess


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
MODEL = "gpt-5.6-terra"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v1-sample")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def run_batch(screen, batch_id, resume):
    folder = screen / batch_id
    manifest = json.loads((folder / "batch.json").read_text())
    expected = {item["record_id"] for item in manifest["records"]}
    output = folder / "assessments.jsonl"
    if output.exists():
        values = [json.loads(line) for line in output.read_text().splitlines() if line.strip()]
        received = {item["record_id"] for item in values}
        if resume and len(values) == len(expected) and received == expected:
            return batch_id, manifest, values
        raise RuntimeError(f"{batch_id} has existing incomplete or non-resumable output")
    command = [
        "codex", "exec", "--ephemeral", "--sandbox", "workspace-write",
        "--skip-git-repo-check", "--json", "-c", 'web_search="disabled"',
        "-m", MODEL, "-o", str(folder / "final.txt"), "-",
    ]
    version = subprocess.run(["codex", "--version"], capture_output=True, text=True, check=True).stdout.strip()
    started = dt.datetime.now(dt.timezone.utc)
    with (
        (folder / "input.md").open() as stdin,
        (folder / "trace.jsonl").open("w") as stdout,
        (folder / "stderr.txt").open("w") as stderr,
    ):
        result = subprocess.run(command, cwd=folder, stdin=stdin, stdout=stdout, stderr=stderr, text=True)
    ended = dt.datetime.now(dt.timezone.utc)
    (folder / "run.json").write_text(json.dumps({
        "batch_id": batch_id,
        "model": MODEL,
        "codex_version": version,
        "command": shlex.join(command),
        "started_utc": started.isoformat(),
        "ended_utc": ended.isoformat(),
        "return_code": result.returncode,
    }, indent=2) + "\n")
    if result.returncode:
        raise RuntimeError(f"{batch_id} Codex return code {result.returncode}")
    values = [json.loads(line) for line in output.read_text().splitlines() if line.strip()]
    received = {item["record_id"] for item in values}
    if len(values) != len(expected) or received != expected:
        raise RuntimeError(f"{batch_id} invalid submissions: {len(values)}")
    return batch_id, manifest, values


def main():
    args = parse_args()
    screen = PILOT / f"fulltext-assessment-{args.version}"
    selection = json.loads((screen / "selection.json").read_text())
    batch_ids = [batch["batch_id"] for batch in selection["batches"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        completed = list(pool.map(lambda batch_id: run_batch(screen, batch_id, args.resume), batch_ids))
    rows = []
    for batch_id, manifest, values in completed:
        titles = {item["record_id"]: item["title"] for item in manifest["records"]}
        for value in values:
            rows.append({"batch_id": batch_id, "title": titles[value["record_id"]], **value})
    fields = [
        "batch_id", "record_id", "connection", "funding", "project_link", "confidence",
        "project_ids", "connection_evidence", "funding_evidence", "project_evidence", "title",
    ]
    with (screen / "results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            item = dict(row)
            item["project_ids"] = ";".join(item["project_ids"])
            writer.writerow({field: item[field] for field in fields})
    summary = {
        "records": len(rows),
        "model": MODEL,
        "prompt_sha256": selection["prompt_sha256"],
        "connection": {value: sum(row["connection"] == value for row in rows) for value in sorted({row["connection"] for row in rows})},
        "funding": {value: sum(row["funding"] == value for row in rows) for value in sorted({row["funding"] for row in rows})},
        "project_link": {value: sum(row["project_link"] == value for row in rows) for value in sorted({row["project_link"] for row in rows})},
        "submission_validated": True,
    }
    (screen / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
