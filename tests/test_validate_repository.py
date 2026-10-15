import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "tools"))

from validate_repository import (  # noqa: E402
    scan_secrets,
    validate_frontmatter,
    validate_markdown_links,
    validate_routes,
)


class RepositoryValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_frontmatter_accepts_required_fields_and_block_description(self):
        skill = self.root / "SKILL.md"
        skill.write_text("---\nname: example\ndescription: >-\n  A test skill.\n---\n", encoding="utf-8")
        self.assertEqual(validate_frontmatter(skill), [])

    def test_frontmatter_reports_missing_required_field(self):
        skill = self.root / "SKILL.md"
        skill.write_text("---\nname: example\n---\n", encoding="utf-8")
        self.assertTrue(any("missing frontmatter 'description'" in error for error in validate_frontmatter(skill)))

    def test_frontmatter_rejects_empty_block_description(self):
        skill = self.root / "SKILL.md"
        skill.write_text("---\nname: example\ndescription: >-\n---\n", encoding="utf-8")
        self.assertTrue(any("empty frontmatter 'description'" in error for error in validate_frontmatter(skill)))

    def test_routes_require_all_reference_files_and_existing_destinations(self):
        (self.root / "references").mkdir()
        (self.root / "subskills" / "sample").mkdir(parents=True)
        (self.root / "references" / "guide.md").write_text("guide", encoding="utf-8")
        (self.root / "subskills" / "sample" / "SKILL.md").write_text("skill", encoding="utf-8")
        router = self.root / "SKILL.md"
        router.write_text(
            "`references/guide.md` and `subskills/sample/SKILL.md`",
            encoding="utf-8",
        )
        self.assertEqual(validate_routes(self.root), [])
        router.write_text("`references/missing.md`", encoding="utf-8")
        errors = validate_routes(self.root)
        self.assertTrue(any("not routed: references/guide.md" in error for error in errors))
        self.assertTrue(any("does not exist: references/missing.md" in error for error in errors))

    def test_relative_markdown_links_check_local_targets_only(self):
        (self.root / "docs").mkdir()
        (self.root / "docs" / "target.md").write_text("target", encoding="utf-8")
        document = self.root / "docs" / "index.md"
        document.write_text(
            "[valid](target.md) [external](https://example.invalid) [broken](missing.md)\n",
            encoding="utf-8",
        )
        errors = validate_markdown_links(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("broken relative link: missing.md", errors[0])

    def test_secret_scan_flags_token_shapes_without_echoing_values(self):
        document = self.root / "sample.txt"
        synthetic_token = "ghp_" + ("A" * 36)
        document.write_text(f"token={synthetic_token}\n", encoding="utf-8")
        findings = scan_secrets(self.root)
        self.assertEqual(len(findings), 1)
        self.assertIn("possible github-token pattern", findings[0])
        self.assertNotIn(synthetic_token, findings[0])

    def test_secret_scan_ignores_nonmatching_placeholders(self):
        document = self.root / "sample.txt"
        document.write_text("token=YOUR_GITHUB_TOKEN_HERE\n", encoding="utf-8")
        self.assertEqual(scan_secrets(self.root), [])


if __name__ == "__main__":
    unittest.main()
