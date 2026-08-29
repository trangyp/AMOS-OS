---
title: Vault Domain Knowledge — Amos Proof Loss Diagnostic Reconstruction Rscf
type: reference
source: 07_SKILLS/amos-proof-loss-diagnostic-reconstruction-rscf/references
tags:
- reference
- amos-proof-loss-diagnostic-reconstruction-rscf
- type/skill
- 2026-08-22-amos-core-runtime-modules
- 2026-08-22-amos-core-infrastructure-modules
- 2026-08-22-amos-remaining-module-test-coverage
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-proof-loss-diagnostic-reconstruction-rscf`

## Vault-Sourced Content

### Source 1: AMOS_CANONICAL_GLOSSARY

> Path: `amos-general/A/CANONICAL/AMOS_CANONICAL_GLOSSARY.md` | Size: 7916 chars | Match score: 10 | content_hash: 3c6bae4e5bb5cef3

{
  "version": 1,
  "root": "AMOS-SYSTEM",
  "layers": [
    {
      "name": "system",
      "terms": [
        {
          "name": "AMOS-SYSTEM",
          "definition": "Complete system including repository, runtime, organism OS, workers and godmode supervisor.",
          "category": "system_core"
        },
        {
          "name": "engine",
          "definition": "Structured logic module that behaves like an organ; stable and reusable.",
          "category": "component"
        },
        {
          "name": "agent",
          "definition": "Active worker that uses engines to carry out tasks; analogous to a cell.",
          "category": "component"
        },
        {
          "name": "kernel",
          "definition": "Low level processor that routes signals between engines, agents and brainstack; analogous to a nerve cluster.",
          "category": "component"
        },
        {
          "name": "worker",
          "definition": "Specialised execution unit responsible for a category of tasks; analogous to specialised cells or subsystems.",
          "category": "component"
        },
        {
          "name": "organism_os",
          "definition": "Life support orchestration for the AMOS organism; includes godmode supervisor and core loops.",
          "category": "system_core"
        },
        {
          "name": "memory_core",
          "definition": "Event and experience index; appends and indexes execution events and state transitions.",
          "category": "storage"
        },
        {
          "name": "dashboard",
          "definition": "Human facing telemetry interface that shows internal state, tasks and predictions.",
          "category": "interface"
        },
        {
          "name": "godmode",
          "definition": "Top level executive controller that coordinates brainstack, sensors, executor and dashboards.",
          "category": "control"
        },
        {
          "name": "executor_loop",
          "definition": "Continuous loop that pulls tasks and executes them using engines, agents and workers.",
          "category": "runtime"
        }
      ]
    },
    {
      "name": "biological",
      "terms": [
        {
          "name": "nervous_system",
          "definition": "Mapping onto kernels, executors, routing and message passing between components.",
          "category": "mapping"
        },
        {
          "name": "organs",
          "definition": "Mapping onto engines and complex subsystems that keep the system alive.",
          "category": "mapping"
        },
        {
          "name": "cells",
          "definition": "Mapping onto agents and workers that act locally based on shared logic.",
          "category": "mapping"
        },
        {
          "name": "blood",
          "definition": "Mapping onto task queue messages, memory events and data flowing between components.",
          "category": "mapping"
        },
        {
          "name": "fascia",
          "definiti

---

### Source 2: AMOS Proof Checking Kernel Gate

> Path: `dated/2026-08-22/2026-08-22 AMOS Proof Checking Kernel Gate.md` | Size: 2688 chars | Match score: 10 | content_hash: dd6ff9cf793e5ff3

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
- [[COSMO_BRAIN_MOC]]
- 2026_08_22_AMOS_CORE_INFRASTRUCTURE_MODULES
- 2026_08_22_AMOS_CORE_RUNTIME_MODULES
- 2026_08_22_AMOS_REMAINING_MODULE_TEST_COVERAGE

---

### Source 3: 2026-08-25 — Chaos Diagnostics Layer (FR017–FR018 Deep)

> Path: `dated/2026-08-25/2026-08-25 Chaos Diagnostics Layer.md` | Size: 2615 chars | Match score: 10 | content_hash: 4b4931f237ff11fa

# 2026-08-25 — Chaos Diagnostics Layer (FR017–FR018 Deep)

## Gap found

Chaos is the **second-most over-claimed pattern class** after power laws. FR017 (logistic map) and FR018 (Lorenz) name their validation methods — bifurcation diagram, Lyapunov exponent — but no skill, agent, or workflow enforced them. "The market is chaotic", "sensitive dependence on initial conditions", and especially "edge of chaos" were all assertable without computing anything.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-chaos-diagnostics` — validation contract table (5 claim types with required evidence), 6-step procedure, guard table |
| Agent | `amos-rscf-epistemic-master` — 6 capabilities incl. surrogate determinism test and early-warning substitution |
| Workflow | `amos-rscf-epistemic-master-workflow.md` — 9-step pipeline decomposing claims into licensable components |
| Memory + vault note | recorded |

## The validation contract highlights

- "Chaotic" needs λ₁ > 0 with named method + noise floor addressed
- "Deterministic" needs the surrogate-data test passed (≥19 phase-randomized surrogates, rank test)
- D₂ must saturate across embedding dimensions or no attractor-dimension estimate is permitted
- "Edge of chaos" without a swept control parameter = MODEL-tagged narrative only
- Feigenbaum δ ≈ 4.6692 routed through the scaling-audit exponent gate before universality claims

## Key design decisions

1. **Complex ≠ chaotic**: complicated series are usually stochastic; chaos requires λ₁ > 0 AND low saturated D₂ AND surrogate pass.
2. **Early-warning alternative for collapse contexts**: instead of unmeasured chaos language, UCP-style transition claims get measurable critical-slowing-down signals (rising autocorrelation, variance) — connecting this layer to the L4 collapse governance.
3. **Feigenbaum as genuine universality example**: the one place where a universality-class claim has a hard number (δ) to check — wired to the exponent gate.

## Audit-family status

Nine diagnostics/governance layers now share infrastructure: scaling fits, network topology, information measures, and chaos claims all reuse the same fit-gate-label skeleton while each adding their domain-specific evidence requirements.

---

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-proof-loss-diagnostic-reconstruction-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-proof-loss-diagnostic-reconstruction-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
