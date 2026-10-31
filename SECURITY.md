# Security Policy

## Scope
Ocean AI is currently a static frontend prototype. It does not provide a trusted server-side API proxy or production model-serving backend.

## Reporting a vulnerability
Please do not disclose credentials or exploitable details in public issues. Use GitHub's private vulnerability reporting feature when available, or contact the repository maintainer privately.

## Security expectations
- Never commit API keys, tokens, passwords, or private datasets.
- Browser-stored provider keys are accessible to the browser profile and are not suitable for production secrets.
- Validate all untrusted input and avoid inserting untrusted data using `innerHTML`.
- Use HTTPS for external services.
- Review third-party scripts and dependencies before adding them.
- Treat model output as untrusted content.
- Do not upload sensitive imagery or personal data to third-party inference services without consent.
- Configure provider restrictions, quotas, and rotation for any exposed key.
- Report security findings responsibly and include reproduction steps.
