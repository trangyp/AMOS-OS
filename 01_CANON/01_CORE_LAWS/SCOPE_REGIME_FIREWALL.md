---
title: "SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law"
type: core_law
source: 01_CANON/01_CORE_LAWS
tags: [canon, core_law, firewall, epistemic_boundary]
rscf:
  state: CANON_LAW
  claim_class: CANONICAL_INVARIANT
  provenance: AMOS_CANON
---

# SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law

The  strictly prohibits reasoning principles, heuristics, or confidence ratings valid in one regime (e.g. theoretical modeling) from leaking un-gated into distinct operational regimes (e.g. safety-critical execution).

## Invariant
3689	ext{RegimeTransfer}(C, 	ext{Regime}_A, 	ext{Regime}_B) \le 	ext{Gate}(	ext{BoundaryWitness})3689

## Related
- [[L0_INTEGRITY]] · [[01_CORE_LAWS_MOC]] · [[PROVENANCE_X_CONFIDENCE]]
