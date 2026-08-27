---
tags: [rscf]
---
# RSCF Contract

Use **RSCF — Recursive Structured Claim Framework** for every load-bearing conclusion.

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

## RSCF invariants
1. Confidence cannot exceed the weakest load-bearing premise without independent revalidation.
2. Descendants of one source are correlated provenance, not independent confirmation.
3. Scope, regime, and freshness propagate to dependent claims.
4. Structural similarity never proves causation.
5. Equal/incomparable support remains COMPETING.
6. Failed premises invalidate only dependent descendants.
7. Framework equations remain MODEL unless independently validated.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
