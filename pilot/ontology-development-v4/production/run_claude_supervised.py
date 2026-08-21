#!/usr/bin/env python3
"""Resume a Claude run after subscription usage resets."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESET_PATTERN = re.compile(r"resets\s+(\d{1,2}):(\d{2})(am|pm)", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=("extraction", "audit", "review"), required=True)
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--model", default="claude-opus-5")
    parser.add_argument("--effort", default="high")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--start-at", help="local start time: YYYY-MM-DDTHH:MM")
    parser.add_argument("--max-cycles", type=int, default=12)
    return parser.parse_args()


def sleep_until(target: datetime) -> None:
    while True:
        remaining = (target - datetime.now().astimezone()).total_seconds()
        if remaining <= 0:
            return
        time.sleep(min(60, remaining))


def reset_time(run_dir: Path) -> datetime | None:
    traces = sorted(
        (
            path
            for path in (run_dir / "traces").glob("*.json")
            if not path.name.endswith(".run.json")
        ),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    now = datetime.now().astimezone()
    for path in traces[:32]:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        match = RESET_PATTERN.search(str(value.get("result", "")))
        if not match:
            continue
        hour = int(match.group(1)) % 12
        if match.group(3).casefold() == "pm":
            hour += 12
        target = now.replace(
            hour=hour,
            minute=int(match.group(2)),
            second=0,
            microsecond=0,
        ) + timedelta(minutes=2)
        if target <= now:
            target += timedelta(days=1)
        return target
    return None


def main() -> None:
    args = parse_args()
    if args.start_at:
        start = datetime.strptime(args.start_at, "%Y-%m-%dT%H:%M").replace(
            tzinfo=datetime.now().astimezone().tzinfo
        )
        print(f"waiting_until={start.isoformat()}", flush=True)
        sleep_until(start)

    command = [
        sys.executable,
        str(HERE / "run_claude.py"),
        "--kind",
        args.kind,
        "--prepared",
        str(args.prepared),
        "--run",
        args.run,
        "--model",
        args.model,
        "--effort",
        args.effort,
        "--workers",
        str(args.workers),
    ]
    environment = os.environ.copy()
    environment.pop("ANTHROPIC_API_KEY", None)
    run_dir = HERE / args.run
    for cycle in range(1, args.max_cycles + 1):
        print(f"cycle={cycle} started={datetime.now().astimezone().isoformat()}", flush=True)
        result = subprocess.run(command, cwd=HERE.parents[2], env=environment)
        if result.returncode == 0:
            print("status=complete", flush=True)
            return
        if result.returncode == 75:
            target = reset_time(run_dir)
            if target is None:
                print("status=rate-limited reset_time=unknown", flush=True)
                raise SystemExit(75)
            print(f"status=rate-limited waiting_until={target.isoformat()}", flush=True)
            sleep_until(target)
            continue
        print(
            f"status=incomplete returncode={result.returncode} retrying_in=60s",
            flush=True,
        )
        time.sleep(60)
    raise SystemExit("Maximum Claude resume cycles reached.")


if __name__ == "__main__":
    main()
