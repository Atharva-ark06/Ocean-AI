# 🌊 Ocean AI — Ocean Guardian Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Pages" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License" />
</p>

<h3 align="center">AI-assisted marine pollution monitoring and ocean intelligence — in a browser.</h3>

<p align="center"><b>Explore the ocean. Visualize signals. Understand pollution.</b></p>

---

## Overview

**Ocean AI** (Ocean Guardian AI) is a responsive, single-page frontend concept for exploring marine plastic pollution through an interactive dashboard. It combines animated ocean visualization, sample detection feeds, impact metrics, and an optional conversational assistant interface.

The repository currently contains a **static HTML/CSS/JavaScript prototype**. The visual dashboard is designed as an extensible interface; it does not itself provide verified live sensor telemetry, operational drone dispatch, satellite feeds, or a trained inference service.

## Interface preview

<p align="center">
  <img src="https://res.cloudinary.com/wpop4xyo/image/upload/v1787987431/Screenshot_2026-08-29_123942.png" alt="Ocean AI dashboard preview" width="100%" />
</p>

<p align="center">
  <img src="https://res.cloudinary.com/wpop4xyo/image/upload/v1787987437/Screenshot_2026-08-29_124009.png" alt="Ocean AI analysis and assistant preview" width="100%" />
</p>

## Features

- **Ocean visualization:** Animated canvas and interactive 3D-style map controls.
- **Pollution dashboard:** Illustrative metrics and detection cards for marine debris.
- **Detection feed:** Sample events with categories and severity presentation.
- **Image analysis UI:** Frontend flow for selecting an image and displaying demo predictions.
- **AI chat interface:** Provider selection and browser-side API connection flow.
- **Responsive layout:** Dashboard adapts to desktop and smaller screens.
- **Static deployment:** No package installation or build step is required to serve the current page.

## Technology

| Layer | Implementation |
|---|---|
| Markup | HTML5 |
| Styling | Embedded CSS, responsive layouts, animations |
| Interactivity | Vanilla JavaScript |
| Visualization | Canvas and CSS 3D transforms |
| Hosting | GitHub Pages |
| CI | GitHub Actions |

## Getting started

### Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Atharva-ark06/Ocean-AI.git
   cd Ocean-AI
   ```

2. Open `index.html` directly in a browser, or use VS Code **Live Server** for local development.

There is no `npm install` or compilation step in the current static version.

### GitHub Pages deployment

The Pages workflow is located at `.github/workflows/pages.yml`.

1. Open **Repository → Settings → Pages**.
2. Set **Build and deployment → Source** to **GitHub Actions**.
3. Push to `main` to validate and deploy automatically, or run the workflow manually from **Actions**.
4. Pull requests run the validation job; deployment is skipped for pull requests.

The workflow checks that `index.html` exists and contains the expected HTML document structure before publishing. It uses the official Pages configure, artifact upload, and deploy actions.

> The deployment workflow publishes the repository's static site. GitHub Pages cannot host a server-side API, model runtime, or secret environment variables.

## AI provider connection and privacy

The assistant UI is a frontend integration point. If you choose to enter a provider API key, treat it as a browser-side prototype: a key used in client-side JavaScript can be exposed to the browser session and its network tools.

- Do not use production, privileged, or long-lived API keys in a public static website.
- Prefer a backend proxy with server-side secrets, rate limits, and authentication for a production deployment.
- Review the provider's pricing, usage, and data-retention policies before connecting.
- Disconnect or revoke test keys after experimentation.

## Project structure

```text
Ocean-AI/
├── .github/
│   └── workflows/
│       └── pages.yml     # Validate and deploy GitHub Pages
├── index.html            # Single-page application
└── README.md              # Project documentation
```

## Roadmap

- [ ] Replace illustrative metrics with clearly sourced ocean datasets.
- [ ] Add a documented backend API contract for sensor ingestion.
- [ ] Connect a verified marine debris classification model.
- [ ] Add confidence calibration and model limitations to predictions.
- [ ] Add historical data visualization and export.
- [ ] Add accessible keyboard controls and reduced-motion support.
- [ ] Add automated browser-level smoke tests.
- [ ] Add secure server-side AI provider integration.
- [ ] Add deployment status and data-source freshness indicators.

## Contributing

Contributions, bug reports, accessibility improvements, and documentation updates are welcome.

1. Fork the repository.
2. Create a focused branch.
3. Test the static page locally.
4. Open a pull request describing the change and its verification.

## License

This project is distributed under the **MIT License**. See [LICENSE](LICENSE) if present in the repository.

## Author

**Atharva Kulkarni**  
Computer Science & Information Security | AI • Web Development • Cybersecurity

---

<p align="center"><b>🌊 Ocean AI — Where AI meets the ocean.</b></p>
