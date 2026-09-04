---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Authority Gmef Gate Integration
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Authority and GMEF Gate Integration

> Source: `_00_Cosmo brain/dated/2026-08-23/2026-08-23 AMOS Authority and GMEF Gate Integration.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## title: AMOS Authority and GMEF Gate Integration created: "2026-08-23" origin: "Hermes ↔ Cosmo Brain" origin_architect: "Trang Phan" type: "note" tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/authority, topic/gmef, topic/governance, dated, dated/2026-08-23] status: "verified" provenance: "OBSERVATION" confidence: "VERIFIED"

## AMOS Authority and GMEF Gate Integration

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
1. **Expiry** — token must not be expired
1. **Scope** — token scope must be `*` or match required scope
1. **Consequence limit** — task consequence must not exceed token's max_consequence
1. **Reversibility** — if token is reversible_only, task must be reversible

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
1. `test_gmef_wired` — kernel has GMEF instance
1. `test_authority_gate_valid_token` — valid token passes authority gate
1. `test_authority_gate_expired_token` — expired token fails authority gate
1. `test_authority_gate_capability_mismatch` — capability mismatch fails
1. `test_authority_gate_no_tokens` — no tokens = no authority gates
1. `test_gmef_gate_no_mutation` — no pending mutation = no GMEF gate
1. `test_gmef_gate_block_m0` — M0 mutation is blocked (constitutional)
1. `test_gmef_gate_sandbox_m3` — M3 mutation goes to SANDBOX
1. `test_gmef_gate_missing_fields` — missing fields causes BLOCK

## Gate Order (Updated)

The kernel's `run()` method now has this gate order:

1. Objective gate
1. AgentOps pre-execution gate
1. Autonomy pre-execution gate
1. AIBOM gate
1. Semantic flow pre-execution gate
1. Principal/delegation gate
1. **Authority token validation gate** (NEW)
1. **GMEF mutation assessment gate** (NEW)
1. Skill selection + plan building + scheduler execution
1. Autonomy post-execution gate
1. Semantic flow post-execution gate
1. AgentOps post-execution gate
1. Evaluation post-execution gate
1. Scientific post-execution gate
1. Ontology post-execution gate
1. ... (remaining advisory gates)
1. Proof checking post-execution gate
1. SelfAudit gate
1. Finalize

## Cross-Runtime Status

| Runtime                  | Tests                  | Status |
| ------------------------ | ---------------------- | ------ |
| Python (AMOS OS Kernel)  | 1934 passed            | Green  |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green  |
| **Total**                |                        |        |

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: gmef-governance-authority-gmef-gate-integration
node_type: reference
path: 07_SKILLS/gmef-governance/references/authority_gmef_gate_integration.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
