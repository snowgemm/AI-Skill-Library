#!/usr/bin/env python3
"""Safely prepare portable skills in an explicitly selected project directory.

The installer is offline, project-scoped, no-overwrite, and does not execute skill code.
It stages all files before installation and rolls back newly created paths on failure.
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
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
                        help="Existing project directory; user-home installation is not supported.")
    parser.add_argument("--host", required=True, choices=(*HOST_DIRECTORIES, "all"),
                        help="Required target host. Use all only when you intentionally want every host folder.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show planned copies without creating directories or files.")
    return parser.parse_args()


def _path_has_symlink(path: Path, stop: Path) -> bool:
    current = path
    while current != stop and current != current.parent:
        if current.is_symlink():
            return True
        current = current.parent
    return False


def _move_entry(source: Path, destination: Path) -> None:
    """Move a staged file/directory into a newly created, empty skill folder."""
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"destination appeared during installation: {destination}")
    shutil.move(str(source), str(destination))


def _ensure_directory(path: Path, target: Path, created: list[Path]) -> None:
    missing: list[Path] = []
    current = path
    while current != target and not current.exists():
        if current.is_symlink():
            raise OSError(f"refusing symlinked destination parent: {current}")
        missing.append(current)
        current = current.parent
    if current != target and (not current.is_dir() or current.is_symlink()):
        raise OSError(f"destination parent is not a normal directory: {current}")
    for directory in reversed(missing):
        directory.mkdir()
        created.append(directory)


def _rollback(skill_directories: list[Path], parent_directories: list[Path]) -> None:
    for path in reversed(skill_directories):
        try:
            if path.is_symlink() or path.is_file():
                path.unlink(missing_ok=True)
            elif path.exists():
                shutil.rmtree(path)
        except OSError:
            pass
    for path in reversed(parent_directories):
        try:
            path.rmdir()
        except OSError:
            pass


def main() -> int:
    args = parse_args()
    requested_target = args.target.expanduser().absolute()
    if not requested_target.exists() or not requested_target.is_dir():
        print("Target must be an existing project directory.", file=sys.stderr)
        return 2
    if any(ancestor.is_symlink() for ancestor in (requested_target, *requested_target.parents)):
        print("Refusing a project target reached through a symlinked path.", file=sys.stderr)
        return 2
    target = requested_target.resolve(strict=True)
    if target in {Path.home().resolve(), Path(target.anchor)} or target == REPOSITORY_ROOT.resolve() or REPOSITORY_ROOT.resolve() in target.parents:
        print("Refusing a home-directory, filesystem-root, or installer-repository target.", file=sys.stderr)
        return 2

    hosts = tuple(HOST_DIRECTORIES) if args.host == "all" else (args.host,)
    if args.host == "all":
        print(
            "Warning: some hosts also discover compatible folders used by other hosts. "
            "Review host precedence and runtime behavior before using this shared project.",
            file=sys.stderr,
        )
    missing = [skill_id for skill_id in SKILL_IDS
               if not (SKILLS_ROOT / skill_id / "SKILL.md").is_file()]
    if missing:
        print("Missing canonical skill files: " + ", ".join(missing), file=sys.stderr)
        return 2

    plan: list[tuple[Path, Path]] = []
    conflicts: list[Path] = []
    for host in hosts:
        destination_root = target / HOST_DIRECTORIES[host]
        if _path_has_symlink(destination_root, target):
            conflicts.append(destination_root)
        for skill_id in SKILL_IDS:
            source = SKILLS_ROOT / skill_id
            if source.is_symlink() or any(child.is_symlink() for child in source.rglob("*")):
                conflicts.append(source)
            destination = destination_root / skill_id
            plan.append((source, destination))
            if destination.exists() or destination.is_symlink():
                conflicts.append(destination)

    if conflicts:
        print("Refusing existing skill paths or symlinked source/destination paths:", file=sys.stderr)
        for path in sorted(set(conflicts)):
            print(f"  - {path}", file=sys.stderr)
        print("No files were copied. Review and merge manually.", file=sys.stderr)
        return 3

    for source, destination in plan:
        print(f"{'Would prepare' if args.dry_run else 'Preparing'} {source} -> {destination}")
    if args.dry_run:
        return 0

    created_parents: list[Path] = []
    created_skill_directories: list[Path] = []
    try:
        # Stage the entire payload under the target's filesystem before committing any destination.
        with tempfile.TemporaryDirectory(prefix=".ai-skill-install-", dir=target) as temporary:
            stage_root = Path(temporary)
            staged: list[tuple[Path, Path]] = []
            for index, (source, destination) in enumerate(plan):
                staged_skill = stage_root / str(index)
                shutil.copytree(source, staged_skill, symlinks=False)
                staged.append((staged_skill, destination))

            for staged_skill, destination in staged:
                _ensure_directory(destination.parent, target, created_parents)
                destination.mkdir()  # exclusive creation: never replace an existing skill directory
                created_skill_directories.append(destination)
                for entry in list(staged_skill.iterdir()):
                    _move_entry(entry, destination / entry.name)
    except Exception as error:  # rollback paths created by this invocation only
        _rollback(created_skill_directories, created_parents)
        print(f"Installation failed and rollback was attempted: {error}", file=sys.stderr)
        print("Check the target for any path that could not be removed during rollback.", file=sys.stderr)
        return 4

    print(f"Prepared {len(plan)} skill folders for {len(hosts)} host(s).")
    print("No host CLI was invoked, no account settings were changed, and no skill code was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
