#!/usr/bin/env python3
"""Regenerate the Git blob SHA-1 inventory for tracked and non-ignored files."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "checksums.git-blob-sha1.txt"


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    paths = sorted({item.decode("utf-8") for item in result.stdout.split(b"\0") if item})
    rows: list[str] = []
    for relative in paths:
        if relative == OUTPUT.relative_to(ROOT).as_posix():
            continue
        path = ROOT / relative
        if path.is_symlink() or not path.is_file():
            print(f"Refusing non-regular tracked path: {relative}", file=sys.stderr)
            return 2
        try:
            rows.append(f"{blob_sha1(path.read_bytes())}  {relative}")
        except OSError as exc:
            print(f"Cannot read {relative}: {exc}", file=sys.stderr)
            return 2
    OUTPUT.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    print(f"Updated {OUTPUT.relative_to(ROOT)} with {len(rows)} Git blob SHA-1 entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
