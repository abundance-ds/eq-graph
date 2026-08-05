#!/usr/bin/env python3
"""Run and summarize the current Protocol 2.0 pilot validators."""

import hashlib
import json
import pathlib
import platform
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "pilot" / "protocol-2.0"

VALIDATORS = [
    ("screening_corpus", "validate_screening_corpus.py", "screening-corpus-validation.json"),
    ("screening_results", "validate_screening_results.py", "screening-final/validation.json"),
    ("fulltext_assessment", "validate_fulltext_assessment.py", "fulltext-assessment-validation.json"),
    ("project_candidate_audit", "evaluate_project_candidate_audit.py", "project-assessment-v3/evaluation.json"),
]


def main():
    checks = []
    for label, script, output in VALIDATORS:
        run = subprocess.run(
            [sys.executable, str(ROOT / "pipeline" / script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        output_path = PILOT / output
        result = json.loads(output_path.read_text()) if output_path.exists() else {}
        checks.append({
            "check": label,
            "ok": run.returncode == 0 and result.get("ok") is True,
            "validator": f"pipeline/{script}",
            "result": f"pilot/protocol-2.0/{output}",
            "return_code": run.returncode,
            "stderr": run.stderr.strip(),
        })

    manifest_files = [
        ROOT / "protocol-2.0.md",
        ROOT / "docs" / "METHOD_SIMPLE.md",
        ROOT / "docs" / "PROVENANCE.md",
        ROOT / "pipeline" / "validate_pilot_2_0.py",
        PILOT / "screening-v3" / "SYSTEM.md",
        PILOT / "screening-final" / "selection.json",
        PILOT / "fulltext-assessment-v1" / "SYSTEM.md",
        PILOT / "project-assessment-v3" / "SYSTEM.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in manifest_files if not path.exists()]
    checks.append({"check": "governing_files_present", "ok": not missing, "missing": missing})
    manifest = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in manifest_files if path.exists()
    }
    result = {
        "ok": all(check["ok"] for check in checks),
        "scope": "Current Protocol 2.0 pilot validation suite",
        "checks": checks,
        "environment": {
            "python": platform.python_version(),
            "codex": subprocess.run(
                ["codex", "--version"], text=True, capture_output=True, check=True
            ).stdout.strip(),
        },
        "sha256": manifest,
    }
    (PILOT / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
