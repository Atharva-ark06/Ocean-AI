"""Data-driven read-only API regression tests.

Each versioned case is an independent, reproducible pagination/filter contract.
"""
import json
import pathlib
import unittest

from fastapi.testclient import TestClient
from backend.app.main import app

ROOT = pathlib.Path(__file__).resolve().parents[2]
CASES = ROOT / "backend" / "tests" / "cases"
CLIENT = TestClient(app)

class QueryCaseTests(unittest.TestCase):
    def test_all_contract_cases(self):
        files = sorted(CASES.glob("*.json"))
        self.assertGreaterEqual(len(files), 1)
        for path in files:
            with self.subTest(case=path.name):
                case = json.loads(path.read_text(encoding="utf-8"))
                response = CLIENT.get("/api/v1/observations", params=case["params"])
                self.assertEqual(response.status_code, 200)
                payload = response.json()
                self.assertEqual(payload["data_mode"], "synthetic")
                self.assertEqual(payload["total"], case["expected_total"])
                self.assertEqual([item["id"] for item in payload["items"]], case["expected_ids"])
                self.assertEqual(payload["limit"], case["params"]["limit"])
                self.assertEqual(payload["offset"], case["params"]["offset"])
