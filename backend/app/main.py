"""Read-only marine observation API.

This service exposes explicitly synthetic observations until a trusted ingestion
pipeline and authenticated operational data source are configured.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field, model_validator
from math import isfinite

ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "data" / "demo-observations.json"

class Observation(BaseModel):
    id: str = Field(min_length=1, max_length=64, pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
    category: Literal["bottles", "nets", "bags", "debris"]
    severity: Literal["low", "medium", "high"]
    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)
    confidence: float = Field(ge=0, le=100)
    minutesAgo: int = Field(ge=0, le=1000000)
    source: Literal["synthetic-scenario-v1"]
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def valid_finite_coordinates(self):
        if not all(isfinite(value) for value in (self.lat, self.lng, self.confidence)):
            raise ValueError("Observation coordinates and confidence must be finite")
        return self

app = FastAPI(title="Ocean AI Demo API", version="0.1.0",
              description="Read-only, explicitly synthetic ocean observations")
origins = [item.strip() for item in os.getenv("OCEAN_ALLOWED_ORIGINS", "").split(",") if item.strip()]
if origins:
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET"],
                       allow_headers=["Accept", "Content-Type"], allow_credentials=False)

def load_observations() -> list[Observation]:
    """Validate source records before returning them to clients."""
    records = json.loads(DATASET.read_text(encoding="utf-8"))
    if not isinstance(records, list) or len(records) > 10000:
        raise ValueError("Invalid synthetic dataset size")
    validated = [Observation.model_validate(record) for record in records]
    ids = [row.id for row in validated]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate observation identifiers")
    return validated

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "data_mode": "synthetic"}

@app.get("/api/v1/observations")
def observations(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    severity: Literal["low", "medium", "high"] | None = None,
    category: Literal["bottles", "nets", "bags", "debris"] | None = None,
) -> dict:
    try:
        rows = load_observations()
    except (OSError, ValueError, TypeError) as exc:
        raise HTTPException(status_code=503, detail="Dataset unavailable") from exc
    if severity:
        rows = [row for row in rows if row.severity == severity]
    if category:
        rows = [row for row in rows if row.category == category]
    return {"data_mode": "synthetic", "total": len(rows),
            "offset": offset, "limit": limit,
            "items": [row.model_dump() for row in rows[offset:offset + limit]]}

@app.get("/api/v1/summary")
def summary() -> dict:
    try:
        rows = load_observations()
    except (OSError, ValueError) as exc:
        raise HTTPException(status_code=503, detail="Dataset unavailable") from exc
    return {"data_mode": "synthetic", "total": len(rows),
            "by_severity": {level: sum(row.severity == level for row in rows)
                            for level in ("low", "medium", "high")},
            "by_category": {kind: sum(row.category == kind for row in rows)
                            for kind in ("bottles", "nets", "bags", "debris")}}
