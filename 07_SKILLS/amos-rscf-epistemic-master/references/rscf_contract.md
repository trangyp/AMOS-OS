---
title: rscf contract
type: reference
tags: [reference, amos-rscf-epistemic-master]
---

# RSCF Contract — Canonical Schema

> Source: `_00_Cosmo brain/rscf/rscf.md` from the AMOS_OS Obsidian vault.
> Epistemic class: SOURCE_CANON

## RSCF YAML Schema

```yaml
claim_id: stable-id
claim: concise proposition
class: VERIFIED | DERIVED | MODEL | CONDITIONAL | COMPETING | UNKNOWN/GAP
scale: H | M | L
premises: []
evidence: []
provenance:
  ancestry: []
  independence_status: demonstrated | correlated | unknown
scope:
  system_or_population: null
  environment: null
  scale: null
  time_window: null
  measurement_method: null
  assumptions: []
regime:
  id: null
  validity_conditions: []
freshness:
  observed_at: null
  revalidate_at: null
dependencies: []
competing_hypotheses: []
falsifiers: []
confidence_ceiling: 0.0
decision_relevance: low | medium | high
```

## RSCF Invariants

1. Confidence cannot exceed the weakest load-bearing premise without independent revalidation.
2. Descendants of one source are correlated provenance, not independent confirmation.
3. Scope, regime, and freshness propagate to dependent claims.
4. Structural similarity never proves causation.
5. Equal/incomparable support remains COMPETING.
6. Failed premises invalidate only dependent descendants.
7. Framework equations remain MODEL unless independently validated.

## 6 State Kinds

- **OBSERVATION**: Directly measured, empirically grounded.
- **SOURCE_CLAIM**: Sourced from a canonical reference, not independently verified.
- **DERIVED**: Logically derived from premises and evidence.
- **MODEL**: Framework assertion, not empirically validated.
- **CONDITIONAL**: Valid only under stated regime conditions.
- **COMPETING**: Equal/incomparable support, no dominant hypothesis.
- **UNKNOWN/GAP**: Insufficient evidence to classify.

---
**MOC:** [[references_MOC]]
