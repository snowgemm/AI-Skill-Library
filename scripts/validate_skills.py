#!/usr/bin/env python3
"""Validate portable Agent Skills against the shared SKILL.md contract."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PureWindowsPath
from typing import Any
from urllib.parse import unquote, urlsplit

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_DESCRIPTION = 1024
MAX_COMPATIBILITY = 500
MAX_FILE_BYTES = 1024 * 1024
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))")
REFERENCE_DEFINITION_RE = re.compile(r"(?m)^ {0,3}\[[^\]]+\]:\s*(?:<([^>\n]+)>|([^\s]+))")
HTML_LINK_RE = re.compile(r"(?i)\b(?:href|src)\s*=\s*['\"]([^'\"]+)['\"]")
FENCE_RE = re.compile(r"^ {0,3}([\x60]{3,}|~{3,})")


class UniqueKeySafeLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_unique_mapping(loader: UniqueKeySafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                "found an unhashable mapping key", key_node.start_mark,
            ) from exc
        if duplicate:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"found duplicate key {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def parse_skill(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    try:
        if path.is_symlink():
            return None, ["SKILL.md must not be a symlink"]
        raw = path.read_bytes()
    except OSError as exc:
        return None, [f"cannot read file: {exc}"]

    if len(raw) > MAX_FILE_BYTES:
        return None, [f"file exceeds {MAX_FILE_BYTES} bytes"]
    if b"\x00" in raw:
        return None, ["file contains NUL bytes"]
    try:
        content = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return None, [f"file is not valid UTF-8: {exc}"]

    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, ["YAML frontmatter must start at the first line with ---"]

    closing = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if closing is None:
        return None, ["YAML frontmatter closing --- delimiter is missing"]

    frontmatter = "\n".join(lines[1:closing])
    body = "\n".join(lines[closing + 1:]).strip()
    if not body:
        errors.append("Markdown instruction body must not be empty")

    try:
        metadata = yaml.load(frontmatter, Loader=UniqueKeySafeLoader)
    except yaml.YAMLError as exc:
        return None, errors + [f"invalid or duplicate-key YAML frontmatter: {exc}"]

    if not isinstance(metadata, dict):
        return None, errors + ["YAML frontmatter must be a mapping"]

    for field in ("name", "description"):
        if field not in metadata:
            errors.append(f"missing required field: {field}")
        elif not isinstance(metadata[field], str) or not metadata[field].strip():
            errors.append(f"{field} must be a non-empty string")

    name = metadata.get("name")
    if isinstance(name, str) and name:
        if len(name) > 64 or not NAME_RE.fullmatch(name):
            errors.append("name must be 1-64 lowercase letters, digits, and single hyphen-separated segments")
        if name != path.parent.name:
            errors.append(f"name {name!r} must match skill directory {path.parent.name!r}")

    description = metadata.get("description")
    if isinstance(description, str) and len(description) > MAX_DESCRIPTION:
        errors.append(f"description exceeds {MAX_DESCRIPTION} characters")

    compatibility = metadata.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, str) or not compatibility.strip():
            errors.append("compatibility must be a non-empty string when present")
        elif len(compatibility) > MAX_COMPATIBILITY:
            errors.append(f"compatibility exceeds {MAX_COMPATIBILITY} characters")

    license_value = metadata.get("license")
    if license_value is not None and (not isinstance(license_value, str) or not license_value.strip()):
        errors.append("license must be a non-empty string when present")

    allowed_tools = metadata.get("allowed-tools")
    if allowed_tools is not None and not isinstance(allowed_tools, str):
        errors.append("portable Agent Skills allowed-tools must be a space-separated string")

    extra_metadata = metadata.get("metadata")
    if extra_metadata is not None:
        if not isinstance(extra_metadata, dict):
            errors.append("metadata must be a mapping of string keys to string values")
        else:
            for key, value in extra_metadata.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    errors.append("metadata must contain only string keys and string values")
                    break

    return metadata, errors



def markdown_destinations(source: str) -> list[str]:
    """Extract Markdown and HTML resource links outside fenced and inline code."""
    visible_lines: list[str] = []
    fence_char: str | None = None
    fence_length = 0
    for line in source.splitlines():
        marker = FENCE_RE.match(line)
        if fence_char is None:
            if marker:
                token = marker.group(1)
                fence_char, fence_length = token[0], len(token)
                continue
            visible_lines.append(line)
        elif marker:
            token = marker.group(1)
            if token[0] == fence_char and len(token) >= fence_length:
                fence_char, fence_length = None, 0

    visible = "\n".join(visible_lines)
    visible = re.sub(r"(?<!\\)([\x60]+).*?\1", "", visible, flags=re.DOTALL)
    destinations: list[str] = []
    for pattern in (MARKDOWN_LINK_RE, REFERENCE_DEFINITION_RE):
        for match in pattern.finditer(visible):
            destination = next((group for group in match.groups() if group is not None), "")
            if destination:
                destinations.append(destination.strip())
    destinations.extend(match.group(1).strip() for match in HTML_LINK_RE.finditer(visible))
    return list(dict.fromkeys(destinations))


def validate_markdown_resources(skill_dir: Path) -> list[str]:
    """Ensure local links resolve within the packaged skill directory."""
    errors: list[str] = []
    skill_root = skill_dir.resolve()
    for document in sorted(skill_dir.rglob("*")):
        if document.is_symlink() or not document.is_file():
            continue
        if document.suffix.lower() not in {".md", ".mdx"}:
            continue
        try:
            raw = document.read_bytes()
            if len(raw) > MAX_FILE_BYTES:
                errors.append(f"{document}: Markdown resource file exceeds {MAX_FILE_BYTES} bytes")
                continue
            source = raw.decode("utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{document}: cannot read Markdown resource file: {exc}")
            continue

        for destination in markdown_destinations(source):
            try:
                parsed = urlsplit(destination)
            except ValueError:
                errors.append(f"{document}: malformed Markdown resource link: {destination}")
                continue
            if parsed.scheme and parsed.scheme.lower() != "file":
                continue
            if destination.startswith("//") or (not parsed.path and not parsed.scheme):
                continue
            if parsed.scheme == "file":
                errors.append(f"{document}: file:// links are not portable: {destination}")
                continue

            decoded_path = unquote(parsed.path)
            windows_path = PureWindowsPath(decoded_path)
            if (
                not decoded_path
                or decoded_path.startswith("/")
                or windows_path.is_absolute()
                or windows_path.drive
                or "\\" in decoded_path
            ):
                errors.append(f"{document}: non-relative or non-portable resource link: {destination}")
                continue

            try:
                resolved = (document.parent / decoded_path).resolve(strict=False)
            except (OSError, RuntimeError):
                errors.append(f"{document}: cannot safely resolve resource link: {destination}")
                continue
            if not resolved.is_relative_to(skill_root):
                errors.append(f"{document}: resource link escapes the skill directory: {destination}")
            elif not resolved.exists():
                errors.append(f"{document}: referenced resource does not exist: {destination}")

    return errors


def validate_root(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.exists() or not root.is_dir():
        return [f"skills root is not a directory: {root}"]
    if root.is_symlink():
        return [f"skills root must not be a symlink: {root}"]

    skill_dirs = sorted(p for p in root.iterdir() if p.is_dir() and not p.is_symlink())
    for entry in root.iterdir():
        if entry.is_symlink():
            errors.append(f"{entry}: symlinks are not allowed in the skills root")
        elif not entry.is_dir():
            errors.append(f"{entry}: each top-level skill entry must be a directory")

    if not skill_dirs:
        errors.append(f"{root}: no skill directories found")

    for skill_dir in skill_dirs:
        for path in skill_dir.rglob("*"):
            if path.is_symlink():
                errors.append(f"{path}: symlinks are not allowed inside a skill")
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_file}: required file is missing")
            continue
        _, skill_errors = parse_skill(skill_file)
        errors.extend(f"{skill_file}: {message}" for message in skill_errors)
        errors.extend(validate_markdown_resources(skill_dir))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "skills")
    args = parser.parse_args()
    errors = validate_root(args.root.absolute())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Validated {sum(1 for p in args.root.iterdir() if p.is_dir())} skill(s): {args.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
