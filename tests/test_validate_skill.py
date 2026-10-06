from pathlib import Path
import tempfile
import unittest

from scripts.validate_skill import validate_skill


class ValidateSkillTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "storytelling"
        (self.root / "references").mkdir(parents=True)
        self.entrypoint = self.root / "SKILL.md"
        self.entrypoint.write_text(
            "---\nname: storytelling\ndescription: Help write and revise stories.\n---\n"
            "# Storytelling\n\n[Methods](references/methods.md)\n",
            encoding="utf-8",
        )
        (self.root / "references" / "methods.md").write_text("# Methods\n", encoding="utf-8")

    def test_valid_package(self):
        self.assertEqual(validate_skill(self.root), [])

    def test_missing_entrypoint(self):
        self.entrypoint.unlink()
        self.assertTrue(validate_skill(self.root))

    def test_malformed_yaml(self):
        self.entrypoint.write_text("---\nname: [broken\n---\n", encoding="utf-8")
        self.assertTrue(validate_skill(self.root))

    def test_wrong_skill_identity(self):
        content = self.entrypoint.read_text(encoding="utf-8").replace(
            "name: storytelling", "name: another-skill"
        )
        self.entrypoint.write_text(content, encoding="utf-8")
        self.assertTrue(validate_skill(self.root))

    def test_missing_reference_target(self):
        (self.root / "references" / "methods.md").unlink()
        self.assertTrue(validate_skill(self.root))

    def test_local_reference_cannot_escape_package(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        with self.entrypoint.open("a", encoding="utf-8") as stream:
            stream.write("\n[Outside](../outside.md)\n")
        self.assertTrue(validate_skill(self.root))

    def test_reference_reachable_through_another_reference(self):
        (self.root / "references" / "detail.md").write_text("# Detail\n", encoding="utf-8")
        (self.root / "references" / "methods.md").write_text(
            "# Methods\n\n[Detail](detail.md)\n", encoding="utf-8"
        )
        self.assertEqual(validate_skill(self.root), [])

    def test_reference_cannot_be_discoverable_only_from_readme(self):
        (self.root / "references" / "detail.md").write_text("# Detail\n", encoding="utf-8")
        (self.root / "README.md").write_text(
            "[Detail](references/detail.md)\n", encoding="utf-8"
        )
        self.assertTrue(validate_skill(self.root))

    def test_encoded_local_filename_and_fragment(self):
        (self.root / "references" / "methods.md").write_text(
            "[Detail](detail%20notes.md#section)\n", encoding="utf-8"
        )
        (self.root / "references" / "detail notes.md").write_text(
            "# Section\n", encoding="utf-8"
        )
        self.assertEqual(validate_skill(self.root), [])

    def test_external_sources_do_not_require_network_access(self):
        (self.root / "references" / "methods.md").write_text(
            "[Source](https://example.invalid/unknown)\n", encoding="utf-8"
        )
        self.assertEqual(validate_skill(self.root), [])

    def test_invalid_agent_metadata(self):
        (self.root / "agents").mkdir()
        (self.root / "agents" / "openai.yaml").write_text(
            "interface:\n  display_name: Storytelling\n"
            "  short_description: Short\n  default_prompt: Wrong skill\n",
            encoding="utf-8",
        )
        self.assertTrue(validate_skill(self.root))


if __name__ == "__main__":
    unittest.main()
