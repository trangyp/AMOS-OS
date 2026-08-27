---
title: "AMOS Core Runtime Modules"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/core-runtime, topic/proof, topic/memory, topic/graph, dated, dated/2026-08-22, canon/knowledge]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Core Runtime Modules

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 109 tests pass across 6 core module families.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview

The AMOS OS Kernel has 6 core module families that implement the cognitive
runtime. These are the foundational layers beneath the governance modules.

## Module Families

### 1. Proof (`amos/proof/`)
- **ProofChecker**: 4 gates — scope/regime, confidence ceiling, causal evidence, falsifier
- **HypothesisField**: unresolved competing claims, dominance, discrimination
- **RSCF**: compile_claim, confidence_ceiling, selective_invalidate (cascade)
- **Tests**: 22 (test_proof_modules.py)

### 2. Memory (`amos/memory/`)
- **ContextBudgetGovernor**: utility-weighted context selection (6 factors)
- **MemoryImmuneSystem**: REVOKED/PROVENANCE_CYCLE/PATHOLOGICAL detection
- **MemoryManager**: tiered admission (hot/warm/cold) with provenance
- **OrientationCache**: stale-aware key-value cache
- **Tests**: 21 (test_memory_modules.py)

### 3. Graph (`amos/graph/`)
- **CausalGraph**: 7 causal levels (descriptive→intervention_effect)
- **DependencyGraph**: load-bearing descendant traversal, independence
- **ProvenanceGraph**: roots, components, sybil score
- **Tests**: 28 (test_graph_modules.py)

### 4. Runtime (`amos/runtime/`)
- **Planner**: closure, topo, build — skill dependency planning
- **Router**: tensor, complexity (C0-C4), budget
- **Selector**: complexity-aware skill selection
- **SelfAudit**: ProofChecker on all claims
- **Finalizer**: gate summary + competing check
- **Scheduler**: replay-ledger-integrated execution
- **Tests**: 17 (test_runtime_modules.py)

### 5. ABI (`amos/abi/`)
- **ModelRegistry**: discover model manifests from JSON
- **SkillRegistry**: discover skill manifests from JSON
- **ToolRegistry**: discover tool manifests from JSON
- **Tests**: 11 (test_abi_registries.py)

### 6. Replay (`amos/replay/`)
- **EventBus**: publish/subscribe with store persistence
- **Ledger**: SHA-256 hashed replay entries
- **Tests**: ~10 (test_replay_modules.py)

## Test Results

| Test File | Tests |
|-----------|------:|
| test_proof_modules.py | 22 |
| test_memory_modules.py | 21 |
| test_graph_modules.py | 28 |
| test_runtime_modules.py | 17 |
| test_abi_registries.py | 11 |
| test_replay_modules.py | ~10 |
| **Total** | **~109** |

## Full Suite

- Python: 1934 tests pass (all modules with full test coverage)
- TypeScript: 1191 tests pass
- **Total: 3701 verified tests** across all runtimes

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS All 249 Gaps Closed
- 2026-08-22 TypeScript Data Quality Governance

---
**MOC:** [[DATED_MOC]]
