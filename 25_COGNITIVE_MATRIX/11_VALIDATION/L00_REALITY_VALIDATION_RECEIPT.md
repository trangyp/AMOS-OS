---
tags: ['amos_os', 'validation_receipt', 'l00_reality_environment']
---

# L00_REALITY_ENVIRONMENT Validation Receipt

STATUS: EXECUTED_VALIDATION_RECEIPT
epistemic_class: AMOS_DERIVED
canonical_status: CONDITIONAL
updated: 2026-08-26

## What was executed

`[[l00_reality_validator]]` at `25_COGNITIVE_MATRIX/11_VALIDATION/l00_reality_validator.py`
executes the test table declared by the spec itself —
Section 71 of `L00_REALITY_ENVIRONMENT — Definition` (L00-T01 … L00-T30),
plus the 18 invariants (Sec 42) and 20 failure modes (Sec 66) they encode.

## Result

```text
Self-test: 91/91 PASS, exit 0  (2026-08-26)

Breakdown:
- 30 positive-path checks        (one per declared test ID)
- 30 adversarial probes          (each encodes one declared failure mode:
                                  FM-02..FM-16, INV-06/07/08/10/11/12/13/14/16/17)
- 30 UNKNOWN-propagation probes  (empty input -> UNKNOWN, never PASS: fail-closed)
- 1 malformed-input probe        (T18 with wrong type -> FAIL, never crash-open)
```

## Engine design (fail-closed by construction)

- Every check operates on typed records mirroring the spec's own tensors
  (`Observation`, `StateRecord`, `Evidence` — Secs 7/26/27).
- Missing required fields → `UNKNOWN`, never `PASS` (INV-11).
- Verdict vocabulary is the spec's own: PASS / FAIL / CONDITIONAL / UNKNOWN.
- Freshness requires an explicitly declared claim-dependent horizon τ_c;
  no universal threshold is invented.
- Causal promotion admits only INTERVENTION_EFFECT or mechanism-with-typed-evidence
  (INV-12); association/temporal-sequence/similarity are hard FAIL.

## Scope boundary (honest limits)

| Layer | Status |
|---|---|
| Test-table logic (T01–T30 semantics) | EXECUTED-VALIDATED |
| Runtime enforcement on live observation channels | UNKNOWN/GAP |
| Empirical universality of RC(r) metric | UNVERIFIED (spec's own boundary) |
| Coverage of L01–L29 primitives | UNKNOWN/GAP (this receipt covers L00 only) |

The validator validates *callers' typed inputs*; it does not itself wire into a
live observation pipeline. Wiring it to real observation streams remains open work.

## Effect on subsystem placeholders

This receipt satisfies the "executable binding" condition for the
`25_COGNITIVE_MATRIX/01_PRIMITIVES/L00_REALITY_ENVIRONMENT` package leaf.
The generic "PARTIAL unless an executed validation receipt exists" gap note in
the Cognitive Matrix contract family may now cite this receipt for L00.

---

**Related:** [[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]] · [[PROMOTION_GATES]] · [[BINDING_RULES]] · [[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: l00_reality_validation_receipt
node_type: note
path: 25_COGNITIVE_MATRIX/11_VALIDATION/L00_REALITY_VALIDATION_RECEIPT.md
claim_class: AMOS_DERIVED
