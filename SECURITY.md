# Security Policy

## Scope
Ocean AI is currently a static frontend prototype. It does not provide a trusted server-side API proxy or production model-serving backend.

## Reporting a vulnerability
Please do not disclose credentials or exploitable details in public issues. Use GitHub's private vulnerability reporting feature when available, or contact the repository maintainer privately.

## Implemented protections (static prototype)

- Chat messages (including external model responses) and uploaded filenames are rendered via `textContent` rather than interpolated into HTML.
- Uploaded images must be 5 MiB or smaller and match supported PNG/JPEG/GIF/WebP magic bytes.
- Demonstration data and predictions are explicitly marked synthetic; UI actions do not trigger real drone dispatch or satellite tracking.
- The single Pages workflow runs regression tests and Node syntax checks before publishing, while CodeQL separately analyzes JavaScript.
- Theme preference may be stored in localStorage; provider credentials are never written there by this release.

## Known limitations / residual risks

- No real user authentication, authorization, session management, rate limiting, or backend secrets handling exists. The static UI must **not** be used to protect private marine data or perform real operational actions.
- The optional direct browser-to-provider API experiment is not a secure production architecture and may encounter provider CORS restrictions. Use an authenticated backend proxy with tightly scoped secrets, request validation, rate limits, logging controls, and server-side authorization before production use.
- The image prediction and cleanup estimates are mock results, not validated ML inference. Do not rely on them for decisions.
- CSP, complete accessibility testing, penetration testing, dependency/SBOM automation, and production integration tests remain future work. CodeQL does not prove the absence of vulnerabilities.

## Security expectations
- Never commit API keys, tokens, passwords, or private datasets.
- Provider API keys are held in **volatile tab memory only**. Older localStorage provider entries are deleted on page load. This does **not** make browser-to-provider requests safe for production: network requests, browser extensions, and developer tools can still expose keys.
- Validate all untrusted input and avoid inserting untrusted data using `innerHTML`.
- Use HTTPS for external services.
- Review third-party scripts and dependencies before adding them.
- Treat model output as untrusted content.
- Do not upload sensitive imagery or personal data to third-party inference services without consent.
- Configure provider restrictions, quotas, and rotation for any exposed key.
- Report security findings responsibly and include reproduction steps.
