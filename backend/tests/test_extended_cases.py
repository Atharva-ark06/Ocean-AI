"""Reproducible query contracts added in the PR 9 extended matrix."""
import json
import pathlib
import unittest
from fastapi.testclient import TestClient
from backend.app.main import app

ROOT=pathlib.Path(__file__).resolve().parent
CASES=ROOT / "extended_cases"
CLIENT=TestClient(app)

class ExtendedAPIMatrixTests(unittest.TestCase):
    def test_extended_cases(self):
        files=sorted(CASES.glob("case-*.json"))
        self.assertGreaterEqual(len(files), 180)
        for path in files:
            with self.subTest(path=path.name):
                case=json.loads(path.read_text(encoding="utf-8"))
                response=CLIENT.get("/api/v1/observations",params=case["params"])
                self.assertEqual(response.status_code,case["status"])
                if case["status"]==200:
                    result=response.json()
                    self.assertEqual(result["data_mode"],"synthetic")
                    self.assertEqual(result["total"],case["total"])
                    self.assertEqual(result["limit"],case["params"]["limit"])
                    self.assertEqual(result["offset"],case["params"]["offset"])
                    self.assertEqual([row["id"] for row in result["items"]],case["ids"])
                    self.assertTrue(all(row["source"]=="synthetic-scenario-v1" for row in result["items"]))

if __name__=="__main__":
    unittest.main()
