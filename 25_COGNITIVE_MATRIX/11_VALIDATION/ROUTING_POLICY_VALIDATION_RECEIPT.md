---
artifact_id: AMOS-CM-11-VALIDATION-RPOL-EXECUTOR
title: "Routing Policy Validator — Execution Receipt"
path_target: "25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT.md"
artifact_class: VALIDATION_EVIDENCE
contract_class: EXECUTED_VALIDATION_RECEIPT
subsystem: 11_VALIDATION / 10_ROUTING
origin_architect: Trang Phan
executor: Hermes agent (ox-alpha)
updated: 2026-08-26
epistemic_class: DERIVED
conclusion_class: PARTIAL
---

# Routing Policy Validator — Execution Receipt

## What was executed

`routing_policy_validator.py` — a reference executor for the **constitutional
test table T-RPOL-001..015** declared in
`25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md` §99, plus 2 adversarial
probes from §100 (scope expansion, registration-order manipulation).

## Result (executed, not asserted)

```text
19/19 constitutional tests PASS   exit=0
```

| Test group | Coverage |
|---|---|
| T-RPOL-001 | specialist beats default despite earlier registration |
| T-RPOL-002 | explicit target missing → visible DENY, no silent fallback |
| T-RPOL-003 | competing specialists → AMBIGUOUS preserved |
| T-RPOL-004 | UNKNOWN/GAP → DENY (fail closed) |
| T-RPOL-005 | wrong regime → DENY |
| T-RPOL-006/011 | stale epoch → invalidated |
| T-RPOL-007 | unvalidated mode blocked; validated passes |
| T-RPOL-008 | capability without authority → AUTHORITY_REQUIRED |
| T-RPOL-009 | shared evidence root ≠ independence gain |
| T-RPOL-010 | capability-incompatible fallback denied explicitly |
| T-RPOL-012 | security-sensitive w/o security cap → DENY |
| T-RPOL-013 | fresh route reusable across unrelated policy change |
| T-RPOL-015 | hard scope filter dominates ranking/speed |

Adversarial probes passed: wildcard-scope capture BLOCKED,
registration-order manipulation BLOCKED.

## Honest scope boundary (per Full Brain OS law)

This receipt does NOT claim:

- active runtime policy promotion (`PROMOTION_GATES.md` untouched)
- canonical precedence authority (`authority_state: NONE` preserved)
- full router implementation — this validates *policy logic*, not a live router

The source contract's own `proof_capsule.final_status`
(`PLACEHOLDER / UNVALIDATED`) is now partially upgraded:
**structural policy logic is EXECUTED-VALIDATED; runtime enforcement remains UNKNOWN/GAP.**

## Falsifier status

F1–F5 from §101 remain open. If authoritative routing canon is recovered and
defines a materially different hierarchy, supersede this validator.

## Reproduce

```bash
python3 25_COGNITIVE_MATRIX/11_VALIDATION/routing_policy_validator.py
```

---

RSCF-NODE
node_id: routing_policy_validation_receipt
node_type: note
claim_class: DERIVED
RSCF-RELATIONS:
  - VALIDATES: [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md]]
