---
title: RSCF REFERENCES
tags:
- rscf
- epistemic
- claim
- canon/knowledge
type: document
source: 11_KNOWLEDGE/rscf
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: epistemic_framework
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[rscf_MOC]]
