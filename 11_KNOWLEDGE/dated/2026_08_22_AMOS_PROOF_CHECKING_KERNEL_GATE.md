---
title: AMOS Proof Checking Kernel Gate
created: '2026-08-22'
origin: Hermes ↔ Cosmo Brain
origin_architect: Trang Phan
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/system
- rscf/claim
- rscf/state/observation
- topic/implementation
- topic/proof-checking
- topic/kernel-gate
- dated
- dated/2026-08-22
- canon/knowledge
status: verified
provenance: OBSERVATION
confidence: VERIFIED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Proof Checking Kernel Gate

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — ProofChecker wired into AmosKernel as post-execution gate; 4 new tests pass.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was implemented

The user added `ProofChecker` and `ProvenanceGraph` instances to `AmosKernel.__init__`,
and a post-execution proof checking gate that runs when `state.claims` is non-empty.

### Kernel Changes (`amos/kernel.py`)

```python
# In __init__:
self.proof_checker = ProofChecker()
self.provenance = ProvenanceGraph()

# In run(), after RSCF transaction gate, before SelfAudit:
if state.claims:
    proof_gates = self.proof_checker.check_state(state)
    state.gates += proof_gates
```

### Gate Behavior

- **With claims**: Adds 4 gates per claim (scope-regime, confidence, causal, falsifier)
- **Without claims**: No proof-specific gates added (SelfAudit still adds "competing" gate)
- **SelfAudit**: Always runs, also calls `ProofChecker().check_state(state)` + core invariant check

## Test Coverage (4 new tests in `test_kernel.py`)

| Test | Description |
|------|-------------|
| `test_proof_checker_wired` | `kernel.proof_checker` is a `ProofChecker` instance |
| `test_provenance_graph_wired` | `kernel.provenance` is a `ProvenanceGraph` instance |
| `test_proof_gate_with_claims` | Claim-specific gates (scope-regime, confidence, causal, falsifier) present when claims submitted |
| `test_proof_gate_no_claims` | No claim-specific gates when no claims submitted |

## Key Insight

The proof checking gate is **conditional** — it only runs when claims are present.
This avoids unnecessary gate overhead for simple tasks that don't involve epistemic
claims. The SelfAudit gate (which always runs) also calls `ProofChecker.check_state()`,
so there is some redundancy, but the explicit post-execution gate ensures proof
checking happens even if SelfAudit is modified in the future.

## Test Results

- Python: 1934 tests pass (was 1742, +160 new)
- TypeScript: 1253 tests pass (was 1191, +4 new)
- **Total: 3701 verified tests** across all runtimes

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS Core Infrastructure Modules
- 2026-08-22 AMOS Core Runtime Modules
- 2026-08-22 AMOS Remaining Module Test Coverage

---
**MOC:** [[DATED_MOC]]
