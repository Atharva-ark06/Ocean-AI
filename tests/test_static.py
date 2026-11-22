import json
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

    def test_demo_dataset_contains_200_valid_events(self):
        records = json.loads((ROOT / "data/demo-observations.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(records), 200)
        self.assertEqual(len({row["id"] for row in records}), len(records))
        for record in records:
            self.assertIn(record["category"], ("bottles", "nets", "bags", "debris"))
            self.assertIn(record["severity"], ("low", "medium", "high"))
            self.assertGreaterEqual(record["lat"], -90)
            self.assertLessEqual(record["lat"], 90)
            self.assertGreaterEqual(record["lng"], -180)
            self.assertLessEqual(record["lng"], 180)

    def test_provider_tokens_are_not_persisted(self):
        content = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("const volatileApiKeys = new Map()", content)
        self.assertNotIn("localStorage.setItem(`${provider}_api_key`", content)

    def test_chat_and_file_names_use_text_content(self):
        content = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("body.textContent = String(content)", content)
        self.assertIn("fileInfo.textContent =", content)
        self.assertIn("signatureValid", content)

    def test_dataset_is_deployed_with_the_site(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("path: .", workflow)
        self.assertFalse((ROOT / ".github/workflows/static.yml").exists())

    def test_deploy_workflow_targets_main(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn('branches: [main]', workflow)

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
