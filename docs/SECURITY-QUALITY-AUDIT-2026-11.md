# Ocean AI — Static Frontend Security and Quality Review
Date: 2026-11-22
Scope: GitHub Pages HTML/CSS/JavaScript frontend. No backend repository was provided.

## Findings addressed
| Area | Existing behavior | Change | Verification |
|---|---|---|---|
| Browser token handling | API keys persisted in localStorage | In-memory provider map; delete legacy saved keys | Static regression check |
| Untrusted chat rendering | User and provider text interpolated into innerHTML | DOM textContent output | Static regression check |
| Uploaded filename rendering | Filename interpolated into innerHTML | Plain textContent | Static regression check |
| Image upload | Trusted MIME prefix only | Max 5 MiB plus PNG/JPEG/GIF/WebP file-signature validation | Static regression check |
| Dashboard provenance | Random feed and impact values appeared live | Bundled 200-record synthetic JSON, visible demo labeling, offline fallback | Dataset/scenario parity tests |
| Control handlers | Map and chatbot globals shadowed within initialization function | Shared references used by inline callbacks | Node inline-script syntax check |
| API integration | Uninitialized default API endpoint and old model labels | Initialize endpoint, use demonstrative model identifiers, document CORS/backend needs | Node syntax check, manual live provider testing pending |
| GitHub Pages | Two competing deployment workflows and incomplete artifact path | Single workflow publishes site root, validates Python tests + JS syntax | PR Actions |
| Theme/accessibility | No top-right theme switch or reduced-motion style | Theme toggle, focus-visible, responsive layout, hover, reduced-motion | Manual browser testing recommended |

## Non-goals and ongoing risk
- Static GitHub Pages cannot safely implement server-side authentication, API secret custody, authorization, or real telemetry ingestion. These remain **not implemented**.
- Browser-side provider keys remain unsuitable for production even without persistence. Use restricted ephemeral keys for experimentation only, and move provider calls behind an authenticated backend before any production use.
- Synthetic image analysis, detections, coordinates, confidence, drones and impact counts are illustrative. None is a measured or operational claim.
- Source-based checks and CodeQL are not a substitute for comprehensive penetration testing or a live production deployment smoke test.
- This repository has no npm/Python third-party dependency manifest; dependency vulnerability scans must be added if a package manager is introduced.

## Verification
Run `python -m unittest discover -s tests -v` to validate fixture parity, demo data bounds, token persistence guard and Pages configuration. The Pages validation GitHub Action also runs `node --check` on extracted inline dashboard JavaScript. CodeQL is maintained in `.github/workflows/security.yml`.

## Production follow-up
Introduce a real backend with authenticated sessions, scoped server secrets, input schemas, request timeouts, provider allowlists, security headers, rate limiting, API observability and trusted ocean data sources. Only then connect authoritative telemetry to dashboard cards, preserve timestamps/provenance, and test against the deployed environment.
