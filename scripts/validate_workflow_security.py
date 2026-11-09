#!/usr/bin/env python3
"""Validate GitHub Actions workflow permissions and automation hand-off invariants."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PINNED_ACTION = re.compile(r"^\s*uses:\s*([^\s#]+)@([^\s#]+)", re.MULTILINE)
SHA = re.compile(r"^[0-9a-f]{40}$")


def workflow_on(document: dict[str, Any]) -> Any:
    # PyYAML YAML 1.1 may represent the unquoted on key as True.
    return document.get("on", document.get(True))




def validate_raw_workflow_text(name: str, text: str) -> list[str]:
    """Catch GitHub expressions escaped into literal strings before YAML parsing."""
    errors: list[str] = []
    if re.search(r"\\\$\{\{", text):
        errors.append(f"{name}: escaped GitHub Actions expression found")
    if name == "quality.yml":
        required = {
            "concurrency group": r"(?m)^\s*group:\s*quality-\$\{\{\s*github\.workflow\s*\}\}-\$\{\{\s*github\.ref\s*\}\}\s*$",
            "matrix job name": r"(?m)^\s*name:\s*Validate \(Python \${\{\s*matrix\.python-version\s*\}\}\)\s*$",
            "matrix Python version": r"(?m)^\s*python-version:\s*\$\{\{\s*matrix\.python-version\s*\}\}\s*$",
        }
        for label, pattern in required.items():
            if not re.search(pattern, text):
                errors.append(f"{name}: required unescaped {label} expression is missing")
    return errors


def parse(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        raw_text = path.read_text(encoding="utf-8")
        errors.extend(validate_raw_workflow_text(path.name, raw_text))
        data = yaml.safe_load(raw_text)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path.name}: cannot parse workflow: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{path.name}: workflow root must be a mapping")
        return {}
    return data


def check_action_pins(name: str, errors: list[str]) -> None:
    text = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
    for action, ref in PINNED_ACTION.findall(text):
        if action.startswith("./"):
            continue
        if not SHA.fullmatch(ref):
            errors.append(f"{name}: action {action} must be pinned to a full 40-character commit SHA")


def validate_documents(quality: dict[str, Any], upstream: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    q_triggers = workflow_on(quality)
    if not isinstance(q_triggers, dict) or "workflow_dispatch" not in q_triggers:
        errors.append("quality.yml must expose workflow_dispatch for GITHUB_TOKEN-driven automation")
    if quality.get("permissions") != {"contents": "read"}:
        errors.append("quality.yml top-level permissions must be exactly contents: read")
    q_jobs = quality.get("jobs")
    if not isinstance(q_jobs, dict):
        errors.append("quality.yml must define jobs")
        q_jobs = {}
    for required in ("validate", "workflow-security"):
        if required not in q_jobs:
            errors.append(f"quality.yml is missing required job: {required}")
    security = q_jobs.get("workflow-security", {})
    if not isinstance(security, dict):
        errors.append("quality.yml workflow-security job must be a mapping")
        security = {}
    if security.get("permissions") != {"contents": "read"}:
        errors.append("workflow-security job must have contents: read and no write permissions")
    security_text = str(security.get("steps", []))
    if "zizmorcore/zizmor-action@" not in security_text:
        errors.append("quality.yml must run the pinned zizmor workflow security audit")
    if "advanced-security" not in security_text or "version" not in security_text:
        errors.append("zizmor must use explicit non-Advanced-Security mode and a pinned scanner version")
    if "min-severity" not in security_text or "low" not in security_text:
        errors.append("zizmor must include low-severity findings for review")
    check_action_pins("quality.yml", errors)

    u_triggers = workflow_on(upstream)
    if not isinstance(u_triggers, dict) or "schedule" not in u_triggers or "workflow_dispatch" not in u_triggers:
        errors.append("upstream-registry.yml must support scheduled and manual scans")
    if upstream.get("permissions") != {"contents": "read"}:
        errors.append("upstream-registry.yml top-level permissions must be exactly contents: read")
    u_jobs = upstream.get("jobs")
    if not isinstance(u_jobs, dict):
        errors.append("upstream-registry.yml must define jobs")
        u_jobs = {}
    detect = u_jobs.get("detect", {})
    propose = u_jobs.get("propose", {})
    if not isinstance(detect, dict) or not isinstance(propose, dict):
        errors.append("upstream workflow must define detect and propose job mappings")
        return errors
    if detect.get("permissions") != {"contents": "read"}:
        errors.append("upstream detect job must be read-only")
    if propose.get("needs") != "detect":
        errors.append("upstream propose job must depend on the read-only detect job")
    if propose.get("permissions") != {
        "actions": "write", "contents": "write", "pull-requests": "write"
    }:
        errors.append("upstream propose job must have only actions, contents and pull-requests write permissions")
    if propose.get("if") != "needs.detect.outputs.has_updates == 'true'":
        errors.append("upstream propose job must run only when the complete scan finds an update")
    script_text = str(propose.get("steps", []))
    for marker in ("createWorkflowDispatch", "workflow_id", "quality.yml",
                   "checksums.git-blob-sha1.txt", "SHA-1"):
        if marker not in script_text:
            errors.append(f"upstream propose script is missing required safeguard: {marker}")
    check_action_pins("upstream-registry.yml", errors)
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    quality = parse(ROOT / ".github/workflows/quality.yml", errors)
    upstream = parse(ROOT / ".github/workflows/upstream-registry.yml", errors)
    errors.extend(validate_documents(quality, upstream))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Workflow security validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Workflow permissions, immutable action pins, zizmor audit and upstream CI hand-off are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
