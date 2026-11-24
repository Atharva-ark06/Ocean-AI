# Ocean AI release and deployment checklist

## Static site
1. Run `python -m unittest discover -s tests -v`.
2. Run `node --check` against the inline script extracted from `index.html`.
3. Confirm `data/demo-observations.json` contains 200 valid explicitly synthetic observations.
4. Validate the GitHub Pages artifact contains `index.html`, `styles/ocean-modern.css`, and the dataset.
5. Inspect GitHub Actions Pages validation and deploy conclusions. A passing validation job does not guarantee a successful Pages deployment.
6. Visit https://atharva-ark06.github.io/Ocean-AI/ and check the demo count and banner; do not call the static feed live telemetry.
7. Keep provider test tokens short-lived; never enter production secrets into the browser experiment.

## Optional API
- Install pinned-compatible backend packages in an isolated venv.
- Run `python -m unittest discover -s backend/tests -v`.
- Confirm `GET /health` and `GET /api/v1/summary` return `data_mode: synthetic`.
- Configure CORS with exact trusted origins only; no wildcard.
- Authentication, RBAC, trusted ingestion, persistent storage, and observability are not implemented.

## Rollback
Revert/redeploy the last known-good static Pages commit, confirm its dataset is included, and document the incident.
