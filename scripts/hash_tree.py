#!/usr/bin/env python3
"""Write a deterministic SHA-256 manifest for a directory tree."""

import argparse
import hashlib
import pathlib


def digest(path: pathlib.Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        while chunk := source.read(1024 * 1024):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    if not source.is_dir():
        raise SystemExit(f"not a directory: {source}")

    paths = sorted(path for path in source.rglob("*") if path.is_file())
    lines = [
        f"{digest(path)}\t{path.stat().st_size}\t{path.relative_to(source).as_posix()}\n"
        for path in paths
    ]

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text("".join(lines))
    temporary.replace(output)

    print(f"{len(paths)} files written to {output}")


if __name__ == "__main__":
    main()
