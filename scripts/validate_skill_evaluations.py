#!/usr/bin/env python3
"""Validate deterministic positive/negative routing seed cases for every portable skill."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog/portable-skills-phase-1.json"
CASES = ROOT / "evaluations/skill-routing-cases.json"
SKILL_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_data(data: Any, expected_skill_ids: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["evaluation root must be an object"]
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if data.get("status") != "seed_cases_only_not_runtime_tested":
        errors.append("status must explicitly state that routing cases are seeds, not runtime tests")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        errors.append("description must be a non-empty string")

    requirements = data.get("requirements")
    if not isinstance(requirements, dict):
        errors.append("requirements must be an object")
        requirements = {}
    positive_required = requirements.get("positive_cases_per_skill")
    negative_required = requirements.get("negative_cases_per_skill")
    if positive_required != 5:
        errors.append("positive_cases_per_skill must be exactly 5")
    if negative_required != 5:
        errors.append("negative_cases_per_skill must be exactly 5")

    skills = data.get("skills")
    if not isinstance(skills, list):
        return errors + ["skills must be an array"]
    seen_skills: set[str] = set()
    seen_case_ids: set[str] = set()
    for index, skill in enumerate(skills):
        label = f"skills[{index}]"
        if not isinstance(skill, dict):
            errors.append(f"{label} must be an object")
            continue
        skill_id = skill.get("skill_id")
        if not isinstance(skill_id, str) or not SKILL_ID_RE.fullmatch(skill_id):
            errors.append(f"{label}.skill_id must be a valid kebab-case skill ID")
            continue
        if skill_id in seen_skills:
            errors.append(f"duplicate skill_id: {skill_id}")
        seen_skills.add(skill_id)
        for field, expected in (("positive_cases", positive_required), ("negative_cases", negative_required)):
            cases = skill.get(field)
            if not isinstance(cases, list):
                errors.append(f"{skill_id}.{field} must be an array")
                continue
            if isinstance(expected, int) and len(cases) != expected:
                errors.append(f"{skill_id}.{field} must contain exactly {expected} cases")
            expected_activation = field == "positive_cases"
            for case_index, case in enumerate(cases):
                case_label = f"{skill_id}.{field}[{case_index}]"
                if not isinstance(case, dict):
                    errors.append(f"{case_label} must be an object")
                    continue
                case_id = case.get("id")
                if not isinstance(case_id, str) or not case_id.strip():
                    errors.append(f"{case_label}.id must be a non-empty string")
                elif case_id in seen_case_ids:
                    errors.append(f"duplicate case id: {case_id}")
                else:
                    seen_case_ids.add(case_id)
                prompt = case.get("prompt")
                if not isinstance(prompt, str) or not prompt.strip():
                    errors.append(f"{case_label}.prompt must be a non-empty string")
                rationale = case.get("rationale")
                if not isinstance(rationale, str) or not rationale.strip():
                    errors.append(f"{case_label}.rationale must be a non-empty string")
                if case.get("expected_activation") is not expected_activation:
                    errors.append(f"{case_label}.expected_activation must be {str(expected_activation).lower()}")

    missing = sorted(expected_skill_ids - seen_skills)
    unexpected = sorted(seen_skills - expected_skill_ids)
    if missing:
        errors.append("missing skills from portable catalogue: " + ", ".join(missing))
    if unexpected:
        errors.append("unknown skills not in portable catalogue: " + ", ".join(unexpected))
    if len(seen_skills) != len(skills):
        errors.append("skill IDs must be unique")
    return errors


def main() -> int:
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        data = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Cannot read evaluation catalogue or cases: {exc}", file=sys.stderr)
        return 2
    items = catalog.get("skills") if isinstance(catalog, dict) else None
    if not isinstance(items, list):
        print("Portable skill catalogue must contain a skills array.", file=sys.stderr)
        return 2
    expected = {item.get("id") for item in items if isinstance(item, dict) and isinstance(item.get("id"), str)}
    errors = validate_data(data, expected)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Skill routing data validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    count = sum(len(item["positive_cases"]) + len(item["negative_cases"]) for item in data["skills"])
    print(f"Validated {count} skill-routing seed cases across {len(data['skills'])} skills.")
    print("This validates the test-data structure only; no AI host/runtime behavior was tested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
