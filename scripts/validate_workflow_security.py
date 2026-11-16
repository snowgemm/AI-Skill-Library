#!/usr/bin/env python3
"""Validate GitHub Actions permissions, immutable pins, and read-only upstream monitoring."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PINNED_ACTION = re.compile(r"^\s*uses:\s*([^\s#]+)@([^\s#]+)", re.MULTILINE)
SHA = re.compile(r"^[0-9a-f]{40}$")
FORBIDDEN_UPSTREAM_OPERATIONS = (
    "createRef",
    "createWorkflowDispatch",
    "pulls.create",
    "pulls.update",
    "createOrUpdateFileContents",
    "contents: write",
    "pull-requests: write",
    "actions: write",
    "gh pr create",
)


def workflow_on(document: dict[str, Any]) -> Any:
    # PyYAML YAML 1.1 may represent the unquoted "on" key as True.
    return document.get("on", document.get(True))


def validate_raw_workflow_text(name: str, text: str) -> list[str]:
    """Catch escaped expressions and unsafe write operations in the raw workflow source."""
    errors: list[str] = []
    if re.search(r"\\\$\{\{", text):
        errors.append(f"{name}: escaped GitHub Actions expression found")
    if name == "quality.yml":
        required = {
            "concurrency group": "group: quality-" + "$" + "{{ github.workflow }}" + "-" + "$" + "{{ github.ref }}",
            "matrix job name": "name: Validate (Python " + "$" + "{{ matrix.python-version }})",
            "matrix Python version": "python-version: " + "$" + "{{ matrix.python-version }}",
        }
        for label, expected in required.items():
            if expected not in text:
                errors.append(f"{name}: required unescaped {label} expression is missing")
    if name == "upstream-registry.yml":
        for marker in FORBIDDEN_UPSTREAM_OPERATIONS:
            if marker in text:
                errors.append(f"{name}: forbidden write-capable operation found: {marker}")
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
    try:
        text = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{name}: cannot read workflow for action-pin validation: {exc}")
        return
    for action, ref in PINNED_ACTION.findall(text):
        if action.startswith("./"):
            continue
        if not SHA.fullmatch(ref):
            errors.append(f"{name}: action {action} must be pinned to a full 40-character commit SHA")


def validate_documents(quality: dict[str, Any], upstream: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    q_triggers = workflow_on(quality)
    if not isinstance(q_triggers, dict) or "workflow_dispatch" not in q_triggers:
        errors.append("quality.yml must expose workflow_dispatch")
    if not isinstance(q_triggers, dict) or "push" not in q_triggers:
        errors.append("quality.yml must run on pushes to main")
    elif q_triggers["push"].get("branches") != ["main"]:
        errors.append("quality.yml push trigger must target main only")
    if quality.get("permissions") != {"contents": "read"}:
        errors.append("quality.yml top-level permissions must be exactly contents: read")

    q_jobs = quality.get("jobs")
    if not isinstance(q_jobs, dict):
        errors.append("quality.yml must define jobs")
        q_jobs = {}
    for required in ("validate", "workflow-security"):
        if required not in q_jobs:
            errors.append(f"quality.yml is missing required job: {required}")
    for job_name, job in q_jobs.items():
        if isinstance(job, dict) and job.get("permissions") != {"contents": "read"}:
            errors.append(f"quality.yml job {job_name} must have contents: read only")

    security = q_jobs.get("workflow-security", {})
    if not isinstance(security, dict):
        errors.append("quality.yml workflow-security job must be a mapping")
        security = {}
    security_text = str(security.get("steps", []))
    for marker in ("zizmorcore/zizmor-action@", "advanced-security", "version", "min-severity", "low"):
        if marker not in security_text:
            errors.append(f"quality.yml workflow-security job is missing safeguard: {marker}")
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
    scan = u_jobs.get("scan", {})
    notify = u_jobs.get("notify", {})
    if not isinstance(scan, dict) or not isinstance(notify, dict):
        errors.append("upstream workflow must define scan and notify job mappings")
        return errors

    if scan.get("if") != "github.ref == 'refs/heads/main'":
        errors.append("upstream scan job must run only on main")
    if scan.get("permissions") != {"contents": "read"}:
        errors.append("upstream scan job must be read-only")
    if notify.get("needs") != "scan":
        errors.append("upstream notify job must depend on the complete scan")
    if notify.get("if") != "needs.scan.outputs.has_drift == 'true'":
        errors.append("upstream notify job must run only when source drift is detected")
    if notify.get("permissions") != {"issues": "write"}:
        errors.append("upstream notify job must have issues: write only")

    scan_text = str(scan.get("steps", []))
    for marker in (
        "catalog/external-sources.json",
        "portable_skill_path",
        "listCommits",
        "latest.sha !== pinned",
        "failures.length",
        "core.setFailed",
        "has_drift",
    ):
        if marker not in scan_text:
            errors.append(f"upstream scan job is missing fail-closed safeguard: {marker}")

    notify_text = str(notify.get("steps", []))
    for marker in ("issues.listForRepo", "issues.create", "issues.update", "DRIFT_JSON"):
        if marker not in notify_text:
            errors.append(f"upstream notify job is missing issue-only notification behavior: {marker}")

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
    print("Workflow permissions, immutable action pins, read-only upstream scanning, and issue-only notifications are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
