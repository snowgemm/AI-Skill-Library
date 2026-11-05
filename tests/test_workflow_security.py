from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_workflow_security


def documents():
    quality = {
        "on": {"pull_request": {}, "push": {}, "workflow_dispatch": {}},
        "permissions": {"contents": "read"},
        "jobs": {
            "validate": {"permissions": {"contents": "read"}},
            "workflow-security": {
                "permissions": {"contents": "read"},
                "steps": [{
                    "uses": "zizmorcore/zizmor-action@45d7276c9ca790aabd705e31ca99c6185c3e76dd",
                    "with": {"advanced-security": False, "version": "v1.32.0"},
                }],
            },
        },
    }
    upstream = {
        "on": {"schedule": [], "workflow_dispatch": {}},
        "permissions": {"contents": "read"},
        "jobs": {
            "detect": {"permissions": {"contents": "read"}},
            "propose": {
                "needs": "detect",
                "if": "needs.detect.outputs.has_updates == 'true'",
                "permissions": {
                    "actions": "write", "contents": "write", "pull-requests": "write"
                },
                "steps": [{
                    "run": (
                        "createWorkflowDispatch workflow_id: quality.yml "
                        "checksums.git-blob-sha1.txt SHA-1"
                    )
                }],
            },
        },
    }
    return quality, upstream


class WorkflowSecurityTests(unittest.TestCase):
    def test_valid_workflow_contract(self):
        self.assertEqual(validate_workflow_security.validate_documents(*documents()), [])

    def test_quality_workflow_requires_dispatch(self):
        quality, upstream = documents()
        quality["on"].pop("workflow_dispatch")
        self.assertTrue(any("workflow_dispatch" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_detect_job_cannot_write(self):
        quality, upstream = documents()
        upstream["jobs"]["detect"]["permissions"] = {"contents": "write"}
        self.assertTrue(any("detect job must be read-only" in item for item in
                            validate_workflow_security.validate_documents(quality, upstream)))

    def test_proposal_job_requires_checksum_and_dispatch(self):
        quality, upstream = documents()
        upstream["jobs"]["propose"]["steps"][0]["run"] = "create pull request"
        errors = validate_workflow_security.validate_documents(quality, upstream)
        self.assertTrue(any("createWorkflowDispatch" in item for item in errors))
        self.assertTrue(any("checksums.git-blob-sha1.txt" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
