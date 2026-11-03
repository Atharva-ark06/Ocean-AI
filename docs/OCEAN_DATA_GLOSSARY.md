# Ocean Data Glossary

A compact reference for common terms used when exploring ocean observations and visualizations.

| Term | Meaning | Typical unit |
|---|---|---|
| SST | Sea-surface temperature | °C |
| SSS | Sea-surface salinity | PSU |
| SSH | Sea-surface height | m |
| SLA | Sea-level anomaly relative to a reference | m |
| MLD | Mixed-layer depth | m |
| Thermocline | Layer where temperature changes rapidly with depth | °C / m |
| Bathymetry | Seafloor depth and terrain | m |
| Chlorophyll-a | Pigment proxy for phytoplankton biomass | mg/m³ |
| Dissolved oxygen | Oxygen dissolved in seawater | mmol/m³ or mg/L |
| Current velocity | Flow speed and direction | m/s |
| Wave height | Vertical distance between crest and trough | m |
| Argo float | Autonomous profiling float measuring ocean conditions | — |

## Reading gridded data

- **Coordinates:** confirm longitude convention (0–360° or −180–180°).
- **Time:** note whether a timestamp is UTC, local time, or a daily composite.
- **Depth:** distinguish positive-down depth from negative elevation.
- **Missing values:** treat fill values and NaNs as missing, not as physical measurements.
- **Units:** convert units before comparing datasets.
- **Resolution:** a finer grid does not necessarily mean greater observational accuracy.

## Responsible interpretation

Visualizations are not forecasts by themselves. Check provenance, temporal coverage, uncertainty, and the product's intended use before drawing conclusions.