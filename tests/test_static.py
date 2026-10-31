import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class StaticSiteTests(unittest.TestCase):
    def test_pages_entry_exists(self):
        self.assertTrue((ROOT / "index.html").is_file())

    def test_entry_is_nonempty_html(self):
        content = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", content)
        self.assertIn("</html>", content.lower())

    def test_security_policy_documented(self):
        self.assertTrue((ROOT / "SECURITY.md").is_file())

    def test_deploy_workflow_targets_main(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("branches: [main]", workflow)

if __name__ == "__main__":
    unittest.main()
