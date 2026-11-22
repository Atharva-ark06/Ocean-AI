"""Contract tests for the explicitly synthetic API."""
import unittest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

class APIContractTests(unittest.TestCase):
    def test_health_discloses_mode(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data_mode"], "synthetic")

    def test_pagination(self):
        response = client.get("/api/v1/observations?limit=3&offset=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["items"]), 3)
        self.assertEqual(response.json()["total"], 200)

    def test_rejects_unbounded_limit(self):
        self.assertEqual(client.get("/api/v1/observations?limit=10000").status_code, 422)

    def test_filter(self):
        rows = client.get("/api/v1/observations?severity=high").json()["items"]
        self.assertTrue(all(row["severity"] == "high" for row in rows))

    def test_summary_consistency(self):
        result = client.get("/api/v1/summary").json()
        self.assertEqual(sum(result["by_severity"].values()), result["total"])
        self.assertEqual(sum(result["by_category"].values()), result["total"])
