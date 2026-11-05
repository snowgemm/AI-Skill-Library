from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_skills


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "skills"
        self.root.mkdir()
        self.skill = self.root / "demo-skill"
        self.skill.mkdir()
        self.path = self.skill / "SKILL.md"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, frontmatter: str, body: str = "# Demo\n\nInstructions.") -> None:
        self.path.write_text(f"---\n{frontmatter}\n---\n\n{body}\n", encoding="utf-8")

    def test_valid_skill_passes(self) -> None:
        self.write('name: demo-skill\ndescription: A useful demo skill\nmetadata:\n  author: Example\n  version: "1.0"')
        self.assertEqual(validate_skills.validate_root(self.root), [])

    def test_duplicate_yaml_key_fails(self) -> None:
        self.write('name: demo-skill\nname: other-skill\ndescription: Demo')
        self.assertTrue(any("duplicate-key YAML" in item for item in validate_skills.validate_root(self.root)))

    def test_name_directory_mismatch_fails(self) -> None:
        self.write('name: another-skill\ndescription: Demo')
        self.assertTrue(any("must match skill directory" in x for x in validate_skills.validate_root(self.root)))

    def test_name_format_fails(self) -> None:
        self.write('name: Demo--Skill\ndescription: Demo')
        self.assertTrue(any("lowercase letters" in x for x in validate_skills.validate_root(self.root)))

    def test_description_limit_fails(self) -> None:
        self.write('name: demo-skill\ndescription: "' + ("x" * 1025) + '"')
        self.assertTrue(any("description exceeds" in x for x in validate_skills.validate_root(self.root)))

    def test_metadata_values_must_be_strings(self) -> None:
        self.write('name: demo-skill\ndescription: Demo\nmetadata:\n  version: 1')
        self.assertTrue(any("string keys and string values" in x for x in validate_skills.validate_root(self.root)))

    def test_missing_frontmatter_delimiter_fails(self) -> None:
        self.path.write_text("---\nname: demo-skill\ndescription: Demo\n", encoding="utf-8")
        self.assertTrue(any("closing ---" in x for x in validate_skills.validate_root(self.root)))

    def test_symlink_is_rejected(self) -> None:
        self.write('name: demo-skill\ndescription: Demo')
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        self.path.unlink()
        self.path.symlink_to(outside)
        self.assertTrue(any("symlink" in x for x in validate_skills.validate_root(self.root)))


if __name__ == "__main__":
    unittest.main()
