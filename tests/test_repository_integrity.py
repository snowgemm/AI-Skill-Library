from __future__ import annotations

import hashlib
import importlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_repository


class RepositoryIntegrityTests(unittest.TestCase):
    def test_git_blob_sha1_matches_git_object_format(self) -> None:
        payload = b"portable skill\n"
        expected = hashlib.sha1(b"blob 15\0" + payload).hexdigest()
        self.assertEqual(validate_repository.git_blob_sha1(payload), expected)

    def build_fixture(self, root: Path) -> None:
        (root / "skills/demo-skill").mkdir(parents=True)
        (root / "licenses").mkdir()
        (root / ".github/workflows").mkdir(parents=True)
        (root / "skills/demo-skill/SKILL.md").write_text(
            "---\nname: demo-skill\ndescription: Demo skill\nlicense: MIT\nmetadata:\n  upstream: https://github.com/example/demo\n  upstream-commit: 0123456789abcdef0123456789abcdef01234567\n---\n\n# Instructions\n",
            encoding="utf-8",
        )
        (root / "licenses/mit.txt").write_text("MIT notice\n", encoding="utf-8")
        (root / "MANIFEST.json").write_text(json.dumps({
            "release_status": "pre_release_not_approved_for_commercial_distribution",
            "counts": {"portable_skill_adaptations": 1, "custom_skill_bodies_created": 1},
        }), encoding="utf-8")
        (root / "catalog").mkdir()
        (root / "catalog/portable-skills-phase-1.json").write_text(json.dumps({"skills": [{
            "id": "demo-skill", "path": "skills/demo-skill/SKILL.md", "license": "MIT",
            "license_file": "licenses/mit.txt", "upstream": "example/demo",
            "upstream_commit": "0123456789abcdef0123456789abcdef01234567",
        }]}), encoding="utf-8")
        (root / "catalog/external-sources.json").write_text(json.dumps({"sources": [{
            "repository": "example/demo", "commit": "0123456789abcdef0123456789abcdef01234567",
        }]}), encoding="utf-8")
        hosts = {name: {"directory": f".{name}/skills", "runtime_tested": False}
                 for name in ("codex", "claude", "gemini", "copilot", "grok")}
        (root / "adapters").mkdir()
        (root / "adapters/host-adapters.json").write_text(json.dumps({
            "hosts": hosts, "skills": ["demo-skill"], "policy": {"host_runtime_tested": False},
        }), encoding="utf-8")
        (root / ".github/workflows/quality.yml").write_text(
            "name: quality\non:\n  pull_request:\npermissions:\n  contents: read\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@0123456789abcdef0123456789abcdef01234567\n",
            encoding="utf-8",
        )
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        tracked = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True,
                                 stdout=subprocess.PIPE).stdout.split(b"\0")
        rows = []
        for raw in tracked:
            if not raw:
                continue
            relative = raw.decode("utf-8")
            payload = (root / relative).read_bytes()
            rows.append(f"{validate_repository.git_blob_sha1(payload)}  {relative}")
        (root / "checksums.git-blob-sha1.txt").write_text(
            "\n".join(sorted(rows)) + "\n", encoding="utf-8"
        )
        subprocess.run(["git", "add", "checksums.git-blob-sha1.txt"], cwd=root, check=True)

    def run_fixture(self, root: Path) -> list[str]:
        old_root, old_checksum = validate_repository.ROOT, validate_repository.CHECKSUM_FILE
        try:
            validate_repository.ROOT = root
            validate_repository.CHECKSUM_FILE = root / "checksums.git-blob-sha1.txt"
            return validate_repository.validate()
        finally:
            validate_repository.ROOT, validate_repository.CHECKSUM_FILE = old_root, old_checksum

    def test_repository_validator_accepts_consistent_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.build_fixture(root)
            self.assertEqual(self.run_fixture(root), [])

    def test_repository_validator_detects_stale_checksum(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.build_fixture(root)
            (root / "licenses/mit.txt").write_text("changed\n", encoding="utf-8")
            errors = self.run_fixture(root)
            self.assertTrue(any("checksum mismatch for licenses/mit.txt" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
