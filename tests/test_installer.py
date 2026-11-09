from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install_skills.py"
spec = importlib.util.spec_from_file_location("install_skills", SCRIPT)
installer = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.target = self.root / "project"
        self.target.mkdir()
        installer.REPOSITORY_ROOT = self.root / "installer-repo"
        installer.SKILLS_ROOT = self.source
        installer.SKILL_IDS = ("skill-a", "skill-b")
        installer.HOST_DIRECTORIES = {"codex": ".agents/skills", "grok": ".grok/skills"}
        for skill_id in installer.SKILL_IDS:
            skill = self.source / skill_id
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                f"---\nname: {skill_id}\ndescription: Test\n---\nBody\n",
                encoding="utf-8",
            )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_cli(self, *args: str) -> tuple[int, str, str]:
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", [str(SCRIPT), *args]), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = installer.main()
        return code, stdout.getvalue(), stderr.getvalue()

    def test_dry_run_does_not_create_host_paths(self) -> None:
        code, _, _ = self.run_cli("--target", str(self.target), "--host", "all", "--dry-run")
        self.assertEqual(code, 0)
        self.assertFalse((self.target / ".agents").exists())
        self.assertFalse((self.target / ".grok").exists())

    def test_all_hosts_install_warns_and_creates_each_canonical_folder(self) -> None:
        actual_hosts = {
            "codex": ".agents/skills",
            "claude": ".claude/skills",
            "gemini": ".gemini/skills",
            "copilot": ".github/skills",
            "grok": ".grok/skills",
        }
        with patch.dict(installer.HOST_DIRECTORIES, actual_hosts, clear=True):
            code, output, warning = self.run_cli(
                "--target", str(self.target), "--host", "all"
            )
        self.assertEqual(code, 0, output + warning)
        self.assertIn("discover", warning)
        for host in actual_hosts.values():
            for skill_id in installer.SKILL_IDS:
                self.assertTrue((self.target / host / skill_id / "SKILL.md").is_file())

    def test_host_selection_is_required(self) -> None:
        with patch.object(sys, "argv", [str(SCRIPT), "--target", str(self.target)]):
            with self.assertRaises(SystemExit) as raised:
                installer.parse_args()
        self.assertEqual(raised.exception.code, 2)

    def test_existing_skill_refuses_without_overwrite(self) -> None:
        existing = self.target / ".agents/skills/skill-a"
        existing.mkdir(parents=True)
        marker = existing / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        code, _, _ = self.run_cli("--target", str(self.target), "--host", "codex")
        self.assertEqual(code, 3)
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")
        self.assertFalse((self.target / ".agents/skills/skill-b").exists())

    def test_missing_or_file_target_is_rejected(self) -> None:
        code, _, _ = self.run_cli("--target", str(self.root / "missing"), "--host", "codex")
        self.assertEqual(code, 2)
        file_target = self.root / "not-a-dir"
        file_target.write_text("x", encoding="utf-8")
        code, _, _ = self.run_cli("--target", str(file_target), "--host", "codex")
        self.assertEqual(code, 2)

    def test_symlinked_target_is_rejected(self) -> None:
        link = self.root / "project-link"
        link.symlink_to(self.target, target_is_directory=True)
        code, _, _ = self.run_cli("--target", str(link), "--host", "codex")
        self.assertEqual(code, 2)

    def test_symlinked_destination_parent_is_rejected(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.target / ".agents").symlink_to(outside, target_is_directory=True)
        code, _, _ = self.run_cli("--target", str(self.target), "--host", "codex")
        self.assertEqual(code, 3)
        self.assertEqual(list(outside.iterdir()), [])

    def test_partial_failure_rolls_back_new_paths(self) -> None:
        original_move = installer._move_entry
        calls = 0

        def fail_second(source: Path, destination: Path) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected failure")
            original_move(source, destination)

        with patch.object(installer, "_move_entry", side_effect=fail_second):
            code, _, error = self.run_cli("--target", str(self.target), "--host", "codex")
        self.assertEqual(code, 4)
        self.assertIn("rollback", error)
        self.assertFalse((self.target / ".agents").exists())
        self.assertEqual(list(self.target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
