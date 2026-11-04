# Ocean AI — Engineering Roadmap

This checklist tracks potential improvements. Items are proposals until implemented and verified.

## Data quality and provenance

- [ ] Document the provenance and license of every ocean dataset before ingestion.

## Reliability and data handling

- [ ] Display dataset collection timestamps and timezone consistently.

- [ ] Show a visible stale-data state when a feed stops updating.

- [ ] Define a stable schema for incoming sensor observations.

- [ ] Validate latitude and longitude ranges before storing observations.

- [ ] Normalize measurement units at the API boundary.

- [ ] Keep raw sensor values separate from transformed display values.

- [ ] Document sensor calibration status and uncertainty.

- [ ] Add source attribution to map layers and data cards.

- [ ] Add filters by pollution category and severity.

- [ ] Add filters by observation date and time range.

- [ ] Allow users to inspect an observation's metadata.

- [ ] Provide CSV export for filtered, verified observations.

- [ ] Add pagination or virtualization for large detection feeds.

- [ ] Add clear loading, empty, and error states to data panels.

- [ ] Ensure color is not the only indicator of severity.

- [ ] Review contrast ratios for text and interactive controls.

- [ ] Support keyboard operation for all map controls.

- [ ] Add visible focus indicators to interactive elements.

- [ ] Respect prefers-reduced-motion in animation components.

- [ ] Add descriptive labels to canvas-based visualizations.

- [ ] Provide a text alternative for map information.

- [ ] Test layout at narrow mobile viewport widths.

- [ ] Test dashboard behavior at tablet breakpoints.

- [ ] Prevent decorative animations from blocking interaction.

- [ ] Separate UI rendering from data transformation functions.

- [ ] Use deterministic fixtures for repeatable demo scenarios.

- [ ] Label simulated values clearly in the interface.

- [ ] Do not present demo predictions as model validation.

- [ ] Document the expected image-analysis input formats.

- [ ] Validate image MIME types before previewing uploads.

- [ ] Limit image file size before processing.

- [ ] Handle image decoding errors with actionable feedback.
