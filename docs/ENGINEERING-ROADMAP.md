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
