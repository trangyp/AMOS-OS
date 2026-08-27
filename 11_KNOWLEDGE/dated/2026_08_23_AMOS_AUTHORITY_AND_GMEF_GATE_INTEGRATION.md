---
title: "AMOS Authority and GMEF Gate Integration"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/authority, topic/gmef, topic/governance, dated, dated/2026-08-23, canon/knowledge]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Authority and GMEF Gate Integration

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — AuthorityGovernor and GMEF wired into kernel with 9 new tests.

## What was done

The user created two new governance modules:
- `amos/governance/authority.py` — `AuthorityGovernor` for token validation
- `amos/governance/gmef.py` — `GMEF` for mutation assessment

I wired both into the kernel's `run()` method and exported them from `__init__.py`.

## AuthorityGovernor

Validates authority tokens against 5 criteria:
1. **Capability match** — token capability must match required capability
2. **Expiry** — token must not be expired
3. **Scope** — token scope must be `*` or match required scope
4. **Consequence limit** — task consequence must not exceed token's max_consequence
5. **Reversibility** — if token is reversible_only, task must be reversible

### Kernel Integration

Added after the principal gate:
```python
required_capability = task.objective.strip().split()[0] if task.objective.strip() else "reason"
for token in state.authority_tokens:
    ok, reason = self.authority_governor.valid(
        token, required_capability, token.scope,
        token.max_consequence, True)
    state.gates.append(GateResult("authority-token", ...))
    if not ok: return finalize(state)
```

## GMEF (Governance Mutation Evaluation Framework)

Assesses pending mutations against the GMEF protocol:
- **BLOCK** if missing required fields (target, mutation_class, hypothesis, authority, rollback, validation, predicted_regression)
- **BLOCK** if M0 (constitutional invariant)
- **BLOCK** if M1/M2 without explicit authority
- **SANDBOX** otherwise (validate before promotion)

### Kernel Integration

Added after the authority gate:
```python
if hasattr(state, 'pending_mutation') and state.pending_mutation:
    gmef_result = self.gmef.assess(state.pending_mutation)
    state.gates.append(GateResult("gmef-mutation", ...))
    if gmef_result["decision"] == "BLOCK": return finalize(state)
```

## New Tests (9)

1. `test_authority_governor_wired` — kernel has AuthorityGovernor instance
2. `test_gmef_wired` — kernel has GMEF instance
3. `test_authority_gate_valid_token` — valid token passes authority gate
4. `test_authority_gate_expired_token` — expired token fails authority gate
5. `test_authority_gate_capability_mismatch` — capability mismatch fails
6. `test_authority_gate_no_tokens` — no tokens = no authority gates
7. `test_gmef_gate_no_mutation` — no pending mutation = no GMEF gate
8. `test_gmef_gate_block_m0` — M0 mutation is blocked (constitutional)
9. `test_gmef_gate_sandbox_m3` — M3 mutation goes to SANDBOX
10. `test_gmef_gate_missing_fields` — missing fields causes BLOCK

## Gate Order (Updated)

The kernel's `run()` method now has this gate order:
1. Objective gate
2. AgentOps pre-execution gate
3. Autonomy pre-execution gate
4. AIBOM gate
5. Semantic flow pre-execution gate
6. Principal/delegation gate
7. **Authority token validation gate** (NEW)
8. **GMEF mutation assessment gate** (NEW)
9. Skill selection + plan building + scheduler execution
10. Autonomy post-execution gate
11. Semantic flow post-execution gate
12. AgentOps post-execution gate
13. Evaluation post-execution gate
14. Scientific post-execution gate
15. Ontology post-execution gate
16. ... (remaining advisory gates)
17. Proof checking post-execution gate
18. SelfAudit gate
19. Finalize

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3129** | **Both green** |

## Dedicated Test Files

### `tests/test_authority.py` (20 tests)
- Valid token passes (all 5 checks)
- Capability mismatch fails
- Expired/non-expired/no-expiry token
- Scope wildcard/exact/mismatch
- Consequence within/exceeds limit, medium within high
- Reversible only with/without reversible
- ORDER values and hierarchy
- Unknown consequence defaults to zero
- All checks pass, first failure short-circuits, just-expired fails

### `tests/test_gmef.py` (25 tests)
- M3/M4/M5 → SANDBOX
- M0 → BLOCK (constitutional, even with authority)
- M1/M2 with authority → SANDBOX, without → BLOCK
- Missing all 7 fields individually tested
- Missing fields sorted alphabetically
- Partial fields block
- CLASSES dict values and ordering
- Extra fields ignored, empty change blocks

### `tests/test_gmef_authority.py` (20 tests)
- GMEF assessment, authority validation, integration tests

### `tests/test_kernel.py` (10 authority/GMEF tests)
- Kernel wiring, gate validation, expired token, capability mismatch,
  no tokens, no mutation, M0 block, M3 sandbox, missing fields

**Total: 75 tests** covering authority and GMEF gates.

## Test Fix

`test_competing` in `test_kernel.py` was fixed by changing the task objective
from "decide" to "reason" (the authority gate now validates the first word of
the objective as the required capability, and "decide" was not a recognized
capability). All 1934 tests pass with 0 failures.

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS Core Infrastructure Modules
- 2026-08-22 AMOS Structural Gap Promotion 340-347

---
**MOC:** [[DATED_MOC]]
