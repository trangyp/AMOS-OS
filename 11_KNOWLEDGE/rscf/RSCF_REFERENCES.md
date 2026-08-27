---
tags: [rscf]
---
# RSCF Contract

Every load-bearing conclusion uses:

```yaml
claim:
class: VERIFIED|DERIVED|MODEL|CONDITIONAL|COMPETING|UNKNOWN/GAP
premises: []
evidence: []
provenance:
  ancestry_groups: []
dependencies: []
scope:
regime:
freshness:
falsifiers: []
competing_hypotheses: []
confidence_ceiling:
consequence:
repair_path:
```

Rules:
- `Conf(C) <= min Conf(P_i)` for unresolved load-bearing premises.
- Shared ancestry is correlated provenance.
- Scope, regime, and freshness propagate.
- Failed premises invalidate only dependent descendants.
- Equal or incomparable support remains `COMPETING`.
- `UNKNOWN/GAP` is explicit and never silently coerced to zero.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
