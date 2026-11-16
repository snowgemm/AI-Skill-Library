from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_workflow_security


def documents():
    quality = {
        "on": {
            "pull_request": {},
            "push": {"branches": ["main"]},
            "workflow_dispatch": {},
        },
        "permissions": {"contents": "read"},
        "jobs": {
            "validate": {"permissions": {"contents": "read"}},
            "workflow-security": {
                "permissions": {"contents": "read"},
                "steps": [{
                    "uses": "zizmorcore/zizmor-action@45d7276c9ca790aabd705e31ca99c6185c3e76dd",
                    "with": {
                        "advanced-security": False,
                        "version": "v1.32.0",
                        "min-severity": "low",
                        "min-confidence": "low",
                    },
                }],
            },
        },
    }
    upstream = {
        "on": {"schedule": [], "workflow_dispatch": {}},
        "permissions": {"contents": "read"},
        "jobs": {
            "scan": {
                "if": "github.ref == 'refs/heads/main'",
                "permissions": {"contents": "read"},
                "steps": [{
                    "run": (
                        "catalog/external-sources.json portable_skill_path listCommits "
                        "latest.sha !== pinned failures.length core.setFailed has_drift"
                    )
                }],
            },
            "notify": {
                "needs": "scan",
                "if": "needs.scan.outputs.has_drift == 'true'",
                "permissions": {"issues": "write"},
                "steps": [{
                    "run": "issues.listForRepo issues.create issues.update DRIFT_JSON"
                }],
            },
        },
    }
    return quality, upstream


class WorkflowSecurityTests(unittest.TestCase):
    def test_valid_read_only_scan_and_issue_only_notification(self):
        self.assertEqual(validate_workflow_security.validate_documents(*documents()), [])

    def test_quality_workflow_requires_dispatch(self):
        quality, upstream = documents()
        quality["on"].pop("workflow_dispatch")
        self.assertTrue(any("workflow_dispatch" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_quality_push_must_target_main_only(self):
        quality, upstream = documents()
        quality["on"]["push"]["branches"] = ["main", "feat/**"]
        self.assertTrue(any("target main only" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_quality_jobs_cannot_write(self):
        quality, upstream = documents()
        quality["jobs"]["validate"]["permissions"] = {"contents": "write"}
        self.assertTrue(any("must have contents: read only" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_upstream_scan_must_be_read_only(self):
        quality, upstream = documents()
        upstream["jobs"]["scan"]["permissions"] = {"contents": "write"}
        self.assertTrue(any("scan job must be read-only" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_upstream_notify_may_only_write_issues(self):
        quality, upstream = documents()
        upstream["jobs"]["notify"]["permissions"] = {"issues": "write", "contents": "write"}
        self.assertTrue(any("issues: write only" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_scan_must_fail_closed_when_any_source_cannot_be_checked(self):
        quality, upstream = documents()
        upstream["jobs"]["scan"]["steps"][0]["run"] = "listCommits has_drift"
        errors = validate_workflow_security.validate_documents(quality, upstream)
        self.assertTrue(any("fail-closed safeguard" in item for item in errors), errors)

    def test_scan_compares_to_pinned_source_not_previous_scan_head(self):
        quality, upstream = documents()
        upstream["jobs"]["scan"]["steps"][0]["run"] = (
            "catalog/external-sources.json portable_skill_path listCommits "
            "latest.sha !== previousHead failures.length core.setFailed has_drift"
        )
        errors = validate_workflow_security.validate_documents(quality, upstream)
        self.assertTrue(any("latest.sha !== pinned" in item for item in errors), errors)

    def test_notify_requires_idempotent_issue_update_and_creation(self):
        quality, upstream = documents()
        upstream["jobs"]["notify"]["steps"][0]["run"] = "issues.create DRIFT_JSON"
        errors = validate_workflow_security.validate_documents(quality, upstream)
        self.assertTrue(any("issues.listForRepo" in item for item in errors), errors)
        self.assertTrue(any("issues.update" in item for item in errors), errors)

    def test_raw_upstream_workflow_rejects_branch_and_pr_mutations(self):
        source = (
            "permissions:\n  contents: read\njobs:\n"
            "  propose:\n    permissions:\n      pull-requests: write\n"
            "    steps:\n      - run: github.rest.git.createRef()\n"
        )
        errors = validate_workflow_security.validate_raw_workflow_text(
            "upstream-registry.yml", source
        )
        self.assertTrue(any("pull-requests: write" in item for item in errors), errors)
        self.assertTrue(any("createRef" in item for item in errors), errors)

    def test_raw_quality_workflow_accepts_unescaped_expressions(self):
        expression = "$" + "{{"
        source = (
            "group: quality-" + expression + " github.workflow }}-" + expression + " github.ref }}\n"
            "name: Validate (Python " + expression + " matrix.python-version }})\n"
            "python-version: " + expression + " matrix.python-version }}\n"
        )
        self.assertEqual(
            validate_workflow_security.validate_raw_workflow_text("quality.yml", source), []
        )

    def test_raw_quality_workflow_rejects_escaped_expression(self):
        expression = "$" + "{{"
        source = "python-version: \\" + expression + " matrix.python-version }}\n"
        errors = validate_workflow_security.validate_raw_workflow_text("quality.yml", source)
        self.assertTrue(any("escaped GitHub Actions expression" in item for item in errors), errors)

    def test_raw_quality_workflow_requires_matrix_python_expression(self):
        expression = "$" + "{{"
        source = (
            "group: quality-" + expression + " github.workflow }}-" + expression + " github.ref }}\n"
            "name: Validate (Python " + expression + " matrix.python-version })\n"
            "python-version: 3.13\n"
        )
        errors = validate_workflow_security.validate_raw_workflow_text("quality.yml", source)
        self.assertTrue(any("matrix Python version expression is missing" in item for item in errors), errors)


if __name__ == "__main__":
    unittest.main()
