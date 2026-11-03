# Ocean Visualization Guide

## Choose a view

- **Map:** spatial distribution at a fixed depth or time.
- **Time series:** temporal variability at a station or region.
- **Depth profile:** vertical structure at a location.
- **Hovmöller diagram:** evolution over time and one spatial axis.
- **Vector field:** direction and magnitude of currents or winds.

## Design principles

1. Label every variable with its unit.
2. Use sequential palettes for quantities that progress from low to high.
3. Use diverging palettes when values have a meaningful center or anomaly baseline.
4. Keep missing data visually distinct from zero.
5. Show the selected depth and timestamp in the title or caption.
6. Keep geographic projections consistent in comparisons.
7. Add source and processing details to figure captions.

## Interpretation cautions

- A color contrast may reflect a different scale rather than a stronger signal.
- Daily averages can hide short-lived events.
- Spatial smoothing can remove fronts and eddies.
- Correlation alone does not establish causal mechanisms.