# PR 9 Ocean AI: security and frontend audit

## Baseline findings (2026-11-24)
- Public site is static GitHub Pages. It has **no authentication, authorization, OAuth, or protected operational APIs**; never equate provider key entry with user authentication.
- The optional FastAPI API is local-only and read-only. Responses are synthetic, not telemetry.
- Existing provider UI sends a user-supplied credential directly from the browser. Do not use privileged or production keys.
- Existing demo loader falls back silently on invalid/unavailable dataset; it should disclose fallback clearly.
- Existing stat cards have misleading initial hardcoded values and "live" style animations until JSON loads.
- The latest main Pages workflow has passing validation but its publish job failed before steps were reported (run 45038257461); root cause not identifiable from the available logs. Keep deployment guarded by validation and preserve no-deploy-on-PR.
- Backend currently parses the complete JSON file per request; strict schema validation and bounds are the defense in depth priorities.
- Python dependencies use major-version bounds, not reproducible lock files. There is no npm manifest; npm audit is inapplicable.
- Prior test suites validate static data and the API response contract but have limited malformed-record coverage.

## PR acceptance
- Retain explicit synthetic labeling and 200-record feed.
- Add dataset fallback status, stricter record contract and fetch timeout.
- No new public API keys; no fake OAuth claims.
- Harden response schema and add independently reproducible negative/error cases.
- Preserve accessible theme toggle, add explicit color contrast and restrained hover effects.
- Run static and API tests and JavaScript syntax validation on PR.
- Check Actions after head push. User performs final merge.
