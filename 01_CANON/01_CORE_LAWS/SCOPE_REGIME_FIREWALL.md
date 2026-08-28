---
title: SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law
type: core_law
source: 01_CANON/01_CORE_LAWS
tags:
- canon
- core_law
- firewall
- epistemic_boundary
- l0-integrity
- 01-core-laws-moc
- provenance-x-confidence
- l5-scope-regime
- l21-epistemic-regime
- epistemic-regimes
- l30-authority-boundary
- persistent-provenance
- fail-closed-governance
- scope-regime-validation-receipt
- 00-index-moc
- 00-home
rscf:
  state: CANON_LAW
  claim_class: CANONICAL_INVARIANT
  provenance: AMOS_CANON
---

# SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law

The SCOPE_REGIME_FIREWALL strictly prohibits reasoning principles, heuristics, or confidence ratings valid in one regime (e.g. theoretical modeling) from leaking un-gated into distinct operational regimes (e.g. safety-critical execution).

## Invariant
$$\text{RegimeTransfer}(C, \text{Regime}_A, \text{Regime}_B) \le \text{Gate}(\text{BoundaryWitness})$$

## Related
- [[L0_INTEGRITY]] · [[01_CORE_LAWS_MOC]] · [[PROVENANCE_X_CONFIDENCE]] · [[L5_SCOPE_REGIME]] · [[L21_EPISTEMIC_REGIME]] · [[EPISTEMIC_REGIMES]] · [[L30_AUTHORITY_BOUNDARY]] · [[PERSISTENT_PROVENANCE]] · [[FAIL_CLOSED_GOVERNANCE]] · [[SCOPE_REGIME_VALIDATION_RECEIPT]]

---

**MOC:** [[00_INDEX_MOC]] · [[00_HOME]]
