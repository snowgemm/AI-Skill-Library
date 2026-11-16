from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_repository


COMMIT = "a" * 40


def valid_fixture():
    skills = [
        {"id": "licensed-guide", "status": "portable_adaptation", "license": "MIT"},
        {"id": "unlicensed-guide", "status": "original_documentation_adaptation", "license": "UNLICENSED"},
    ]
    routing = {
        "skills": [
            {"skill_id": item["id"], "positive_cases": [{}] * 5, "negative_cases": [{}] * 5}
            for item in skills
        ]
    }
    sources = [{"repository": "example/project", "commit": COMMIT}]
    adapters = {"skills": ["licensed-guide", "unlicensed-guide"]}
    manifest = {
        "counts": {
            "portable_skill_adaptations": 2,
            "custom_skill_bodies_created": 2,
            "unlicensed_independent_guides": 1,
            "license_reviewed_independent_guides": 1,
            "external_repositories_reviewed": 1,
            "external_repositories_commit_pinned": 1,
            "routing_case_seed_count": 20,
        },
        "routing_case_seed_count": 20,
        "ci_conclusion": "success",
        "ci_verified_commit": COMMIT,
        "ci_run_id": 12345,
    }
    return manifest, skills, adapters, sources, routing


class InventoryConsistencyTests(unittest.TestCase):
    def validate(self, fixture):
        return validate_repository.validate_inventory_consistency(*fixture)

    def test_consistent_inventory_passes(self):
        self.assertEqual(self.validate(valid_fixture()), [])

    def test_stale_top_level_routing_count_is_rejected(self):
        fixture = valid_fixture()
        fixture[0]["routing_case_seed_count"] = 10
        errors = self.validate(fixture)
        self.assertTrue(any("MANIFEST routing_case_seed_count" in item for item in errors), errors)

    def test_unlicensed_count_must_match_catalog(self):
        fixture = valid_fixture()
        fixture[0]["counts"]["unlicensed_independent_guides"] = 0
        errors = self.validate(fixture)
        self.assertTrue(any("unlicensed_independent_guides" in item for item in errors), errors)

    def test_duplicate_adapter_ids_are_rejected(self):
        fixture = valid_fixture()
        fixture[2]["skills"].append("licensed-guide")
        errors = self.validate(fixture)
        self.assertTrue(any("duplicate IDs" in item for item in errors), errors)

    def test_duplicate_or_unpinned_sources_are_rejected(self):
        fixture = valid_fixture()
        fixture[3].append({"repository": "example/project", "commit": "not-a-full-sha"})
        errors = self.validate(fixture)
        self.assertTrue(any("duplicate repository" in item for item in errors), errors)
        self.assertTrue(any("full 40-character commit SHA" in item for item in errors), errors)

    def test_license_state_and_status_must_agree(self):
        fixture = valid_fixture()
        fixture[1][1]["license"] = "MIT"
        errors = self.validate(fixture)
        self.assertTrue(any("must remain UNLICENSED" in item for item in errors), errors)


if __name__ == "__main__":
    unittest.main()
