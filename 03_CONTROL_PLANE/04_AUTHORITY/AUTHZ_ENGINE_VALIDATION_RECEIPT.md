---
artifact_id: AMOS-CP-04-AUTHZ-ENGINE-RECEIPT
title: "AUTHZ Invariant Engine — Execution Receipt"
artifact_class: VALIDATION_EVIDENCE
subsystem: 03_CONTROL_PLANE/04_AUTHORITY
executor: Hermes agent (ox-alpha)
updated: 2026-08-26
epistemic_class: DERIVED
conclusion_class: PARTIAL
tags: [note, 04-authority]
---

# AUTHZ Invariant Engine — Execution Receipt

## What was executed

`authz_invariant_engine.py` — reference executor giving the 50 declared
invariants in `INV-AUTHZ-001..050.md` their first executable enforcement.
17 probes covering the invariant families:

| Family | Invariants exercised | Result |
|---|---|---|
| Separation laws (authn≠authz, authority, capability) | 001, 002, 003 | ✅ |
| Binding (principal, target, scope containment) | 007, 009, 011 | ✅ |
| Unknown handling (fail-closed) | 012, 040 | ✅ |
| Freshness (authority epoch, revocation) | 021, 022 | ✅ |
| Delegation (attenuation chain w/ human root) | 018, 038 | ✅ |
| Provenance (semantic origin, intent freshness) | 043, 048 | ✅ |
| Resource bounds (cumulative budget) | 041 | ✅ |
| Emergency boundedness (20% cap) | 050 | ✅ |

## Result

```text
17/17 AUTHZ invariant tests PASS   exit=0
```

## Defect caught during execution

Initial run failed 14/17 due to a tuple-wrapping bug in the check-dispatch
loop (`authorize()` double-wrapped `(Verdict, reason)` tuples from individual
checks). Fixed by unwrapping at dispatch. The engine's fail-closed design
surfaced the defect immediately rather than silently granting.

## Key semantic guarantees now enforced (not just declared)

- `UNKNOWN != PERMISSION` — unknown scope/origin components hard-DENY (INV-012+040)
- `AUTHENTICATION != AUTHORIZATION` (INV-001)
- `CAPABILITY != AUTHORITY` (INV-003)
- Revocation takes effect at current epoch, no grace drift (INV-022)
- Agents can never self-authorize without a delegating human root (INV-038)
- Emergency powers are bounded and cannot exceed 20% of budget cap (INV-050)

## Honest boundary

This validates **enforcement logic** for the declared families. Not yet
covered: ledger/receipt non-substitution paths (035–037), idempotency
redispatch (032–034), multi-origin composition (044–046), H/M/L mapping
(047). The INV files themselves remain PLACEHOLDER canon; this engine is a
DERIVED reference implementation pending promotion.

## Related MOCs

- [[00_HOME]] — universal vault hub
- [[00_ROOT_MOC]] — AMOS OS master map
- AUTHORITY_CONTROL_PLANE_README|AUTHORITY readme
- [[AMOS_RSCF_NODES]] — RSCF node index

## Reproduce

```bash
python3 03_CONTROL_PLANE/04_AUTHORITY/authz_invariant_engine.py
```

---
**MOC:** [[04_AUTHORITY_MOC]]
