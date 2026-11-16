from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_skill_evaluations


def valid_data():
    return {
        "schema_version": "1.0.0",
        "status": "seed_cases_only_not_runtime_tested",
        "description": "Routing seed fixtures, not runtime evidence.",
        "requirements": {"positive_cases_per_skill": 5, "negative_cases_per_skill": 5},
        "skills": [{
            "skill_id": "demo-skill",
            "positive_cases": [
                {"id": f"positive-{i}", "prompt": f"Positive prompt {i}", "expected_activation": True, "rationale": "Should activate."}
                for i in range(5)
            ],
            "negative_cases": [
                {"id": f"negative-{i}", "prompt": f"Negative prompt {i}", "expected_activation": False, "rationale": "Should not activate."}
                for i in range(5)
            ],
        }],
    }


class SkillEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.expected = {"demo-skill"}
        self.data = valid_data()

    def test_valid_seed_cases_pass(self):
        self.assertEqual(validate_skill_evaluations.validate_data(self.data, self.expected), [])

    def test_seed_status_cannot_claim_runtime_tested(self):
        self.data["status"] = "runtime_tested"
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("seeds, not runtime tests" in item for item in errors), errors)

    def test_missing_skill_is_reported(self):
        errors = validate_skill_evaluations.validate_data(self.data, {"demo-skill", "other-skill"})
        self.assertTrue(any("missing skills" in item for item in errors), errors)

    def test_unexpected_skill_is_reported(self):
        errors = validate_skill_evaluations.validate_data(self.data, {"other-skill"})
        self.assertTrue(any("unknown skills" in item for item in errors), errors)

    def test_duplicate_case_id_is_rejected(self):
        self.data["skills"][0]["negative_cases"][0]["id"] = self.data["skills"][0]["positive_cases"][0]["id"]
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("duplicate case id" in item for item in errors), errors)

    def test_negative_case_cannot_expect_activation(self):
        self.data["skills"][0]["negative_cases"][0]["expected_activation"] = True
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("expected_activation must be false" in item for item in errors), errors)

    def test_positive_case_cannot_expect_no_activation(self):
        self.data["skills"][0]["positive_cases"][0]["expected_activation"] = False
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("expected_activation must be true" in item for item in errors), errors)

    def test_case_count_is_exact(self):
        self.data["skills"][0]["positive_cases"].pop()
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("positive_cases must contain exactly 5" in item for item in errors), errors)

    def test_prompt_and_rationale_are_required(self):
        self.data["skills"][0]["positive_cases"][0]["prompt"] = " "
        self.data["skills"][0]["positive_cases"][1]["rationale"] = ""
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("prompt must be a non-empty string" in item for item in errors), errors)
        self.assertTrue(any("rationale must be a non-empty string" in item for item in errors), errors)

    def test_duplicate_skill_id_is_rejected(self):
        duplicate = copy.deepcopy(self.data["skills"][0])
        self.data["skills"].append(duplicate)
        errors = validate_skill_evaluations.validate_data(self.data, self.expected)
        self.assertTrue(any("duplicate skill_id" in item for item in errors), errors)


if __name__ == "__main__":
    unittest.main()
