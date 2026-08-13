#!/usr/bin/env python3
"""Run and aggregate the focused EuroQol funding-scope audit."""

import concurrent.futures
import csv
import json
import pathlib
import subprocess


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"
OUT = PILOT / "funding-audit-v1"
MODEL = "gpt-5.6-terra"


def run_batch(batch_id):
    folder = OUT / batch_id
    expected = {item["record_id"] for item in json.loads((folder / "batch.json").read_text())["records"]}
    output = folder / "funding.jsonl"
    if output.exists():
        values = [json.loads(line) for line in output.read_text().splitlines() if line.strip()]
        if len(values) == len(expected) and {item["record_id"] for item in values} == expected:
            return values
        raise RuntimeError(f"{batch_id} has incomplete existing output")
    command = [
        "codex", "exec", "--ephemeral", "--sandbox", "workspace-write",
        "--skip-git-repo-check", "--json", "-c", 'web_search="disabled"',
        "-m", MODEL, "-o", str(folder / "final.txt"), "-",
    ]
    with (folder / "input.md").open() as stdin, (folder / "trace.jsonl").open("w") as stdout, (folder / "stderr.txt").open("w") as stderr:
        result = subprocess.run(command, cwd=folder, stdin=stdin, stdout=stdout, stderr=stderr, text=True)
    if result.returncode:
        raise RuntimeError(f"{batch_id} failed")
    values = [json.loads(line) for line in output.read_text().splitlines() if line.strip()]
    if len(values) != len(expected) or {item["record_id"] for item in values} != expected:
        raise RuntimeError(f"{batch_id} invalid output")
    return values


def main():
    selection = json.loads((OUT / "selection.json").read_text())
    batch_ids = [batch["batch_id"] for batch in selection["batches"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        groups = list(pool.map(run_batch, batch_ids))
    rows = [item for group in groups for item in group]
    with (OUT / "results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["record_id", "funding_scope", "funding_scope_evidence"])
        writer.writeheader()
        writer.writerows(rows)
    counts = {scope: sum(row["funding_scope"] == scope for row in rows) for scope in sorted({row["funding_scope"] for row in rows})}
    summary = {"records": len(rows), "prompt_sha256": selection["prompt_sha256"], "counts": counts}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
