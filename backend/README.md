# Ocean AI API (optional backend)

This is a **read-only prototype** for serving the same explicitly synthetic
observations used by GitHub Pages. It is not a deployed production service.

## Start

From the repository root:

```bash
python -m venv .venv
python -m pip install -r backend/requirements.txt httpx
python -m uvicorn backend.app.main:app --reload --port 8000
```

Browse `http://127.0.0.1:8000/docs` for OpenAPI documentation.

## Routes

| Route | Description |
| --- | --- |
| `GET /health` | Readiness and synthetic-data disclosure |
| `GET /api/v1/observations` | Validated, filtered and paginated demo observations |
| `GET /api/v1/summary` | Category/severity aggregate counts |

Set `OCEAN_ALLOWED_ORIGINS` to a comma-separated list of **exact trusted origins**
to enable browser CORS; empty means no cross-origin browser access.
Do not configure `*` or enable credentialed CORS.

## Boundaries

No authentication, ingestion, AI inference, persistent data store, background
worker, or authorization exists yet. Do not deploy sensitive datasets here.
Do not call this a live monitoring service. A production backend needs identity,
RBAC, trusted sensor ingestion, audit logging, rate limiting, and operational
monitoring before accepting protected actions.
