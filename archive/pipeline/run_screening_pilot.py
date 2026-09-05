#!/usr/bin/env python3
"""Run and validate tool-submitted title and abstract screening batches."""

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
DEFAULT_MODEL = "gpt-5.6-terra"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v3")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--screen-dir")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--start", type=int, default=0)
    return parser.parse_args()


def run_batch(screen, batch_id, model, resume=False):
    folder = screen / batch_id
    manifest = json.loads((folder / "batch.json").read_text())
    expected = {item["record_id"] for item in manifest["records"]}
    output = folder / "decisions.jsonl"
    if output.exists():
        decisions = [
            json.loads(line) for line in output.read_text().splitlines() if line.strip()
        ]
        received = {item["record_id"] for item in decisions}
        if len(decisions) == len(expected) and received == expected and resume:
            return batch_id, manifest, decisions
        if not resume:
            raise RuntimeError(f"{output} already exists; preserved rather than overwritten")
        if not received < expected:
            raise RuntimeError(f"{batch_id} cannot resume inconsistent submissions")
    suffix = "-resume" if resume and (folder / "run.json").exists() else ""
    command = [
        "codex", "exec", "--ephemeral", "--sandbox", "workspace-write",
        "--skip-git-repo-check", "--json", "-c", 'web_search="disabled"',
        "-m", model, "-o", str(folder / f"final{suffix}.txt"), "-",
    ]
    version = subprocess.run(
        ["codex", "--version"], capture_output=True, text=True, check=True
    ).stdout.strip()
    started = dt.datetime.now(dt.timezone.utc)
    with (
        (folder / "input.md").open() as stdin,
        (folder / f"trace{suffix}.jsonl").open("w") as stdout,
        (folder / f"stderr{suffix}.txt").open("w") as stderr,
    ):
        result = subprocess.run(
            command, cwd=folder, stdin=stdin, stdout=stdout, stderr=stderr, text=True
        )
    ended = dt.datetime.now(dt.timezone.utc)
    (folder / f"run{suffix}.json").write_text(json.dumps({
        "batch_id": batch_id,
        "model": model,
        "codex_version": version,
        "command": shlex.join(command),
        "started_utc": started.isoformat(),
        "ended_utc": ended.isoformat(),
        "return_code": result.returncode,
    }, indent=2) + "\n")
    if result.returncode:
        raise RuntimeError(f"{batch_id} Codex return code {result.returncode}")
    decisions = [
        json.loads(line) for line in output.read_text().splitlines() if line.strip()
    ]
    received = {item["record_id"] for item in decisions}
    if len(decisions) != len(expected) or received != expected:
        raise RuntimeError(f"{batch_id} invalid submissions: {len(decisions)} decisions")
    return batch_id, manifest, decisions


def main():
    args = parse_args()
    screen = pathlib.Path(args.screen_dir).resolve() if args.screen_dir else PILOT / f"screening-{args.version}"
    selection = json.loads((screen / "selection.json").read_text())
    batch_ids = [batch["batch_id"] for batch in selection["batches"]]
    if args.start < 0:
        raise SystemExit("--start must be zero or greater")
    batch_ids = batch_ids[args.start:]
    if args.limit is not None:
        batch_ids = batch_ids[:args.limit]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(run_batch, screen, batch_id, args.model, args.resume)
            for batch_id in batch_ids
        ]
        completed = [future.result() for future in futures]

    rows = []
    for batch_id, manifest, decisions in completed:
        metadata = {item["record_id"]: item for item in manifest["records"]}
        for decision in decisions:
            rows.append({
                "batch_id": batch_id,
                **metadata[decision["record_id"]],
                **decision,
            })
    fields = [
        "batch_id", "record_id", "outcome", "reason", "year",
        "linked_people", "title",
    ]
    with (screen / "results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["linked_people"] = "; ".join(output["linked_people"])
            writer.writerow({field: output[field] for field in fields})
    counts = {
        batch_id: {
            outcome: sum(
                row["batch_id"] == batch_id and row["outcome"] == outcome
                for row in rows
            )
            for outcome in ["retain", "exclude"]
        }
        for batch_id in batch_ids
    }
    summary = {
        "records": len(rows),
        "model": args.model,
        "prompt_sha256": selection["prompt_sha256"],
        "counts": counts,
        "submission_validated": True,
        "accuracy_validated": False,
    }
    (screen / "results-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
