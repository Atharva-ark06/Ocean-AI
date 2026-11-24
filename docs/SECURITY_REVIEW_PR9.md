# PR 9 security decision log

## Trust boundary
GitHub Pages runs untrusted client code in each visitor's browser. All data published with the site is public. Do not put privileged credentials, secrets, personal data or operational authorization logic in static JS.

## Browser-side provider flow
Provider credentials remain in memory and can be inspected by browser tooling and network intermediaries at endpoints. Never represent this as OAuth, Auth0, SSO, account login or session security. Production integration requires a server-side provider proxy with authentication, limits, and secret storage.

## Risk register
| Risk | Mitigation | Residual risk |
|---|---|---|
| Misleading synthetic data | Explicit banner, feed status, deterministic fixtures | Users may mistake mock predictions for observations |
| Cross-site scripting | Render user/model text as `textContent`; escape feed labels | Audit any future `innerHTML` path |
| Arbitrary API endpoint | Enforce HTTPS and disallow insecure custom URLs | Browser network and CORS still apply |
| Excessive requests | Client request timeout, server pagination limit | Backend lacks rate limiting and auth |
| Data corruption | Schema checks, reject invalid records | Static dataset is not signed |
| Workflow supply chain | Least-privilege permissions, CI tests | Third-party GitHub Actions still require monitoring |

Do not claim a full penetration test or CVE-free security state on the basis of static review.
