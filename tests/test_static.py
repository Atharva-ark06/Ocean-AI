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
        self.assertIn('branches: ["main"]', workflow)

    def test_deploy_workflow_has_minimal_permissions(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("contents: read", workflow)
        self.assertIn("pages: write", workflow)
        self.assertIn("id-token: write", workflow)

    def test_deploy_workflow_uses_pages_artifact(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("actions/upload-pages-artifact@", workflow)
        self.assertIn("actions/deploy-pages@", workflow)

    def test_deploy_workflow_serializes_deployments(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("group: pages", workflow)
        self.assertIn("cancel-in-progress: false", workflow)

if __name__ == "__main__":
    unittest.main()
