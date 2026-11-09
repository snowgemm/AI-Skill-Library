#!/usr/bin/env python3
"""Validate catalogue provenance, host adapters, workflow pins and Git blob checksums."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PureWindowsPath
from typing import Any

import yaml
import validate_skills

ROOT = Path(__file__).resolve().parents[1]
CHECKSUM_FILE = ROOT / "checksums.git-blob-sha1.txt"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SKILL_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_HOSTS = {"codex", "claude", "gemini", "copilot", "grok"}


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read valid JSON: {exc}")
        return None


def tracked_files(errors: list[str]) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"], cwd=ROOT, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"git ls-files failed: {exc}")
        return []
    return [ROOT / entry.decode("utf-8") for entry in result.stdout.split(b"\0") if entry]


def resolve_repository_path(value: Any, *, label: str, errors: list[str]) -> Path | None:
    """Resolve a catalogue path without allowing absolute, traversing, or symlinked paths."""
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: path must be a non-empty relative string")
        return None
    if "\\" in value:
        errors.append(f"{label}: backslash paths are not portable")
        return None
    relative = Path(value)
    windows_path = PureWindowsPath(value)
    if relative.is_absolute() or windows_path.is_absolute() or windows_path.drive:
        errors.append(f"{label}: absolute paths are not allowed")
        return None
    if ".." in relative.parts:
        errors.append(f"{label}: parent traversal is not allowed")
        return None
    root = ROOT.resolve()
    current = root
    for part in relative.parts:
        if part in {"", "."}:
            continue
        current = current / part
        if current.is_symlink():
            errors.append(f"{label}: symlink components are not allowed")
            return None
    try:
        resolved = (root / relative).resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        errors.append(f"{label}: cannot safely resolve path: {exc}")
        return None
    if not resolved.is_relative_to(root):
        errors.append(f"{label}: resolved path escapes the repository root")
        return None
    return resolved

def validate() -> list[str]:
    errors: list[str] = []
    manifest = read_json(ROOT / "MANIFEST.json", errors)
    catalogue = read_json(ROOT / "catalog/portable-skills-phase-1.json", errors)
    source_data = read_json(ROOT / "catalog/external-sources.json", errors)
    adapter_data = read_json(ROOT / "adapters/host-adapters.json", errors)

    skills = catalogue.get("skills") if isinstance(catalogue, dict) else None
    if not isinstance(skills, list) or not skills:
        errors.append("portable skill catalogue must contain a non-empty skills array")
        skills = []

    source_rows = source_data.get("sources") if isinstance(source_data, dict) else None
    if not isinstance(source_rows, list):
        errors.append("external source registry must contain a sources array")
        source_rows = []
    source_index = {
        row.get("repository"): row for row in source_rows
        if isinstance(row, dict) and isinstance(row.get("repository"), str)
    }

    seen: set[str] = set()
    for item in skills:
        if not isinstance(item, dict):
            errors.append("portable skill catalogue entries must be objects")
            continue
        skill_id = item.get("id")
        if not isinstance(skill_id, str) or not skill_id:
            errors.append("portable skill entry is missing a non-empty id")
            continue
        if skill_id in seen:
            errors.append(f"duplicate portable skill id: {skill_id}")
        seen.add(skill_id)
        if len(skill_id) > 64 or not SKILL_ID_RE.fullmatch(skill_id):
            errors.append(f"portable skill id is not a valid kebab-case slug: {skill_id!r}")
            continue
        relative_path = item.get("path")
        license_file = item.get("license_file")
        upstream = item.get("upstream")
        commit = item.get("upstream_commit")
        if relative_path != f"skills/{skill_id}/SKILL.md":
            errors.append(f"{skill_id}: non-canonical skill path")
        skill_path = resolve_repository_path(
            relative_path, label=f"{skill_id}: skill path", errors=errors
        )
        if skill_path is None or not skill_path.is_file():
            if skill_path is not None:
                errors.append(f"{skill_id}: missing portable skill file: {relative_path}")
            continue
        license_path = resolve_repository_path(
            license_file, label=f"{skill_id}: license path", errors=errors
        )
        if license_path is None or not license_path.is_file():
            if license_path is not None:
                errors.append(f"{skill_id}: missing preserved license notice: {license_file}")
        if not isinstance(upstream, str) or not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
            errors.append(f"{skill_id}: upstream repository or immutable 40-character pin is invalid")
        else:
            source = source_index.get(upstream)
            if not isinstance(source, dict):
                errors.append(f"{skill_id}: {upstream} missing from external source registry")
            elif source.get("commit") != commit:
                errors.append(f"{skill_id}: pin differs from external source registry")
        metadata, skill_errors = validate_skills.parse_skill(skill_path)
        errors.extend(f"{skill_id}: {message}" for message in skill_errors)
        if isinstance(metadata, dict):
            extra = metadata.get("metadata", {})
            if isinstance(extra, dict) and extra.get("upstream-commit") != commit:
                errors.append(f"{skill_id}: frontmatter upstream-commit differs from catalogue")

    if isinstance(manifest, dict):
        counts = manifest.get("counts", {})
        if not isinstance(counts, dict):
            errors.append("MANIFEST counts must be an object")
        else:
            for key in ("portable_skill_adaptations", "custom_skill_bodies_created"):
                if counts.get(key) != len(skills):
                    errors.append(f"MANIFEST {key} must equal portable catalogue count ({len(skills)})")
        if manifest.get("release_status") != "pre_release_not_approved_for_commercial_distribution":
            errors.append("MANIFEST must explicitly block commercial distribution until release gates pass")

    if isinstance(adapter_data, dict):
        hosts = adapter_data.get("hosts")
        if not isinstance(hosts, dict) or set(hosts) != EXPECTED_HOSTS:
            errors.append("host adapter map must define exactly codex, claude, gemini, copilot and grok")
        else:
            for host, config in hosts.items():
                if not isinstance(config, dict) or not isinstance(config.get("directory"), str):
                    errors.append(f"{host}: adapter must define a project discovery directory")
                elif not config["directory"].startswith(".") or ".." in Path(config["directory"]).parts:
                    errors.append(f"{host}: adapter directory must be a safe project-relative path")
                if isinstance(config, dict) and config.get("runtime_tested") is not False:
                    errors.append(f"{host}: runtime_tested must remain false until runtime evidence exists")
        expected_ids = {item.get("id") for item in skills if isinstance(item, dict)}
        if set(adapter_data.get("skills", [])) != expected_ids:
            errors.append("host adapter skill list does not match portable catalogue")
        policy = adapter_data.get("policy", {})
        if not isinstance(policy, dict) or policy.get("host_runtime_tested") is not False:
            errors.append("adapter policy must not claim unverified host runtime compatibility")

    workflow_dir = ROOT / ".github/workflows"
    if workflow_dir.is_dir():
        for workflow in sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml"))):
            try:
                text = workflow.read_text(encoding="utf-8")
                data = yaml.safe_load(text)
            except (OSError, UnicodeError, yaml.YAMLError) as exc:
                errors.append(f"{workflow.relative_to(ROOT)}: invalid workflow YAML: {exc}")
                continue
            if not isinstance(data, dict):
                errors.append(f"{workflow.relative_to(ROOT)}: workflow root must be a mapping")
                continue
            if re.search(r"(?m)^\s*uses:\s*[^@\s]+@(?![0-9a-f]{40}\b)[^\s#]+", text):
                errors.append(f"{workflow.relative_to(ROOT)}: every third-party action must use a full 40-character commit SHA")
            if re.search(r"(?m)^\s*pull_request_target\s*:", text):
                errors.append(f"{workflow.relative_to(ROOT)}: pull_request_target is not allowed in this repository workflow")
            if "contents: write" in text and workflow.name != "upstream-registry.yml":
                errors.append(f"{workflow.relative_to(ROOT)}: write permission is reserved for the gated upstream proposal job")

    files = tracked_files(errors)
    if CHECKSUM_FILE.is_file():
        entries: dict[str, str] = {}
        for line_number, line in enumerate(CHECKSUM_FILE.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            parts = line.split("  ", 1)
            if len(parts) != 2 or not SHA_RE.fullmatch(parts[0]):
                errors.append(f"checksums.git-blob-sha1.txt:{line_number}: malformed checksum entry")
                continue
            digest, relative = parts
            if relative in entries:
                errors.append(f"checksums.git-blob-sha1.txt:{line_number}: duplicate path {relative}")
            entries[relative] = digest
        tracked = {path.relative_to(ROOT).as_posix(): path for path in files}
        for relative, path in tracked.items():
            if relative == CHECKSUM_FILE.relative_to(ROOT).as_posix():
                continue
            expected = entries.get(relative)
            if expected is None:
                errors.append(f"checksum coverage missing tracked file: {relative}")
            elif path.is_symlink() or not path.is_file():
                errors.append(f"tracked path is not a regular file: {relative}")
            else:
                actual = git_blob_sha1(path.read_bytes())
                if expected != actual:
                    errors.append(f"checksum mismatch for {relative}: expected {expected}, got {actual}")
        for relative in entries:
            if relative not in tracked:
                errors.append(f"checksum entry is not a Git-tracked file: {relative}")
    else:
        errors.append("checksums.git-blob-sha1.txt is missing")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        print(f"Repository validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Repository metadata, source pins, host adapters, workflows and Git blob checksums are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
