# Ocean AI architecture evolution

## Today

GitHub Pages serves a static interface and versioned synthetic JSON. This
remains functional without any backend. The optional FastAPI application reads
the same dataset and exposes read-only, validated, bounded API routes.

```text
                  GitHub Pages (public, static)
                     |                |
              index.html       synthetic JSON
                     |
             optional API client
                     |
            FastAPI read-only API
                     |
           validated synthetic JSON
```

## Proposed production topology (not implemented)

```text
Sensor / satellite partners
          |
   Signed ingestion gateway -- schema / provenance checks
          |
      Durable queue -- quarantine and replay
          |
     Enrichment / inference workers
          |
     Versioned observations store
          |
  Authenticated API / audit / rate limits
          |
      Dashboard + alert review
```

### Trust boundaries

1. Browser is untrusted; no provider secrets, signing keys, or privileged
   dispatch tokens may be delivered to it.
2. Data sources require explicit provenance, timestamps, calibration, and
   quality labels; simulated data must never be merged into operational counts.
3. Uploads must be scanned and stored outside executable directories before
   asynchronous analysis.
4. API permissions must be enforced server-side per resource and role.
5. Public dashboard queries must have bounded pagination and request budgets.

### Delivery stages

- Stage 1: accessible, static, honest synthetic demo (existing PR)
- Stage 2: read-only FastAPI contract and tests (this increment)
- Stage 3: redesigned component-based frontend and API adapter
- Stage 4: database migrations, authenticated ingestion and roles
- Stage 5: observability, threat model, production deployment and SLOs

No stage is considered complete merely because a document describes it.
