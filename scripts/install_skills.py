#!/usr/bin/env python3
"""Safely copy canonical portable skills into a selected project host directory.

No user-home installation, overwrite, network access, or code execution.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
SKILL_IDS = (
    "android-compose-engineering",
    "minecraft-bedrock-addon",
    "threejs-game-engineering",
    "superpowers-engineering-workflow",
    "supabase-engineering",
)
HOST_DIRECTORIES = {
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "gemini": ".gemini/skills",
    "copilot": ".github/skills",
    "grok": ".grok/skills",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path,
                        help="Explicit project directory; user-home installation is not supported.")
    parser.add_argument("--host", choices=(*HOST_DIRECTORIES, "all"), default="all",
                        help="Target host adapter (default: all five hosts).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show planned copies without creating directories or files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    if target == Path.home().resolve() or target == Path(target.anchor):
        print("Refusing a home-directory or filesystem-root target; choose a project directory.", file=sys.stderr)
        return 2
    hosts = tuple(HOST_DIRECTORIES) if args.host == "all" else (args.host,)

    missing = [skill_id for skill_id in SKILL_IDS
               if not (SKILLS_ROOT / skill_id / "SKILL.md").is_file()]
    if missing:
        print("Missing canonical skill files: " + ", ".join(missing), file=sys.stderr)
        return 2

    plan: list[tuple[Path, Path]] = []
    conflicts: list[Path] = []
    for host in hosts:
        destination_root = target / HOST_DIRECTORIES[host]
        for skill_id in SKILL_IDS:
            source = SKILLS_ROOT / skill_id
            destination = destination_root / skill_id
            plan.append((source, destination))
            if destination.exists() or destination.is_symlink():
                conflicts.append(destination)

    if conflicts:
        print("Refusing to overwrite existing skill directories:", file=sys.stderr)
        for path in conflicts:
            print(f"  - {path}", file=sys.stderr)
        print("No files were copied. Review and merge manually.", file=sys.stderr)
        return 3

    for source, destination in plan:
        print(f"{'Would copy' if args.dry_run else 'Copying'} {source} -> {destination}")

    if args.dry_run:
        return 0

    try:
        for source, destination in plan:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
    except OSError as error:
        print(f"Copy failed: {error}", file=sys.stderr)
        print("Review the target for partially copied folders; no existing files were overwritten.", file=sys.stderr)
        return 4

    print(f"Prepared {len(plan)} skill folders for {len(hosts)} host(s).")
    print("No host CLI was invoked and no skill scripts were executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
