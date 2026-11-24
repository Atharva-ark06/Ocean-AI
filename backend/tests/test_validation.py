"""Negative test coverage for the read-only synthetic dataset boundary."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient
from pydantic import ValidationError

from backend.app import main

CLIENT = TestClient(main.app)
GOOD = {
    "id": "TEST-0001",
    "category": "bottles",
    "severity": "high",
    "lat": 9.8,
    "lng": 76.2,
    "confidence": 90,
    "minutesAgo": 3,
    "source": "synthetic-scenario-v1",
}


class ObservationValidationTests(unittest.TestCase):
    def test_rejects_unknown_fields(self):
        with self.assertRaises(ValidationError):
            main.Observation.model_validate({**GOOD, "unexpected": "danger"})

    def test_rejects_missing_provenance(self):
        with self.assertRaises(ValidationError):
            main.Observation.model_validate({k: v for k, v in GOOD.items() if k != "source"})

    def test_rejects_invalid_categories(self):
        for category in ("unknown", "", "javascript:alert(1)"):
            with self.subTest(category=category), self.assertRaises(ValidationError):
                main.Observation.model_validate({**GOOD, "category": category})

    def test_rejects_out_of_range_coordinates(self):
        for key, value in (("lat", -91), ("lat", 91), ("lng", -181), ("lng", 181)):
            with self.subTest(key=key, value=value), self.assertRaises(ValidationError):
                main.Observation.model_validate({**GOOD, key: value})

    def test_rejects_bad_confidence(self):
        for confidence in (-1, 101, float("nan"), float("inf")):
            with self.subTest(confidence=confidence), self.assertRaises(ValidationError):
                main.Observation.model_validate({**GOOD, "confidence": confidence})

    def test_rejects_duplicate_identifiers(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text(json.dumps([GOOD, GOOD]), encoding="utf-8")
            with patch.object(main, "DATASET", path), self.assertRaisesRegex(ValueError, "Duplicate"):
                main.load_observations()

    def test_returns_503_if_dataset_is_invalid(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text(json.dumps([{**GOOD, "confidence": -3}]), encoding="utf-8")
            with patch.object(main, "DATASET", path):
                for route in ("/api/v1/observations", "/api/v1/summary"):
                    with self.subTest(route=route):
                        self.assertEqual(CLIENT.get(route).status_code, 503)

    def test_rejects_non_list_dataset(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text(json.dumps({"records": [GOOD]}), encoding="utf-8")
            with patch.object(main, "DATASET", path), self.assertRaises(ValueError):
                main.load_observations()

    def test_rejects_oversized_dataset(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text(json.dumps([GOOD] * 10001), encoding="utf-8")
            with patch.object(main, "DATASET", path), self.assertRaises(ValueError):
                main.load_observations()

    def test_public_get_has_no_auth_claim(self):
        response = CLIENT.get("/health")
        self.assertEqual(response.json()["data_mode"], "synthetic")
        self.assertNotIn("auth", response.json())


if __name__ == "__main__":
    unittest.main()
