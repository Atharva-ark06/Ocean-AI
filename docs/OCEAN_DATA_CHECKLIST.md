# Ocean Data Quality Checklist

Use this checklist before plotting, comparing, or sharing an ocean dataset.

## Provenance
- [ ] Record provider, dataset name, and version.
- [ ] Capture source URL and retrieval date.
- [ ] Check license and attribution requirements.

## Dimensions and coordinates
- [ ] Confirm array dimensions and coordinate names.
- [ ] Check latitude and longitude ranges.
- [ ] Verify longitude wrapping and coordinate order.
- [ ] Confirm depth sign convention and units.
- [ ] Verify time zone and sampling frequency.

## Values
- [ ] Identify fill values, NaNs, and masked cells.
- [ ] Check expected physical ranges for the variable.
- [ ] Inspect min, max, mean, and quantiles.
- [ ] Avoid mixing units or incompatible reference periods.

## Comparison and visualization
- [ ] Align time, depth, and spatial grids before comparing.
- [ ] Document interpolation or resampling methods.
- [ ] Include units and color-bar labels.
- [ ] Avoid implying precision beyond the source resolution.
- [ ] Describe uncertainty and missing coverage.

## Sharing
- [ ] Keep credentials and private endpoints out of commits.
- [ ] Cite upstream datasets and documentation.
- [ ] Include reproducible steps where practical.