# Ocean AI Security & Quality Review

## Scope
Ocean AI is currently a static, browser-based interface. No backend, secrets, authentication, or live marine-data integration is assumed by this review.

## Security priorities
- Keep API credentials out of browser-delivered JavaScript and HTML.
- Treat all external model responses and user prompts as untrusted data.
- Avoid inserting untrusted strings with `innerHTML`; prefer `textContent` and DOM APIs.
- Validate file type and size before any future image upload; enforce limits server-side too.
- Apply rate limits and abuse monitoring at any future API gateway.
- Use HTTPS for production deployment and review Content Security Policy before enabling integrations.
- Minimize personal data collected by chat, analytics, and upload features.
- Review third-party scripts and pin dependencies where feasible.

## Frontend quality gates
- Preserve keyboard access and visible focus.
- Respect `prefers-reduced-motion`.
- Check color contrast and responsive layouts.
- Keep graceful empty, loading, and error states.
- Validate HTML and run existing static tests before release.

## GitHub Actions
- Prefer least-privilege workflow permissions.
- Pin third-party actions to immutable commit SHAs.
- Do not print secrets in logs.
- Keep deployment workflows restricted to trusted branches and reviewed changes.

## Threat model
| Asset | Threat | Mitigation |
|---|---|---|
| User prompt | Prompt injection / abuse | Treat prompt as data; constrain tools and backend permissions |
| AI response | HTML/JS injection | Render as text or sanitize with a maintained sanitizer |
| API credentials | Browser exposure | Store server-side; use short-lived scoped tokens if required |
| Uploaded media | Malformed or oversized files | Type/size checks, isolated processing, safe storage |
| Deployment pipeline | Supply-chain compromise | Pinned actions, minimal permissions, protected environments |

## Release checklist
- [ ] No secrets committed or exposed in client bundles
- [ ] Static checks and tests pass
- [ ] Keyboard navigation and reduced-motion behavior checked
- [ ] External integrations reviewed for privacy and abuse controls
- [ ] Deployment workflow permissions reviewed
- [ ] Security contact and disclosure instructions are current

This document is guidance for the current frontend prototype, not a claim that backend controls already exist.
