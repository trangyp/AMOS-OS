---
title: "AMOS Core Infrastructure Modules"
created: "2026-08-22"
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/system
- rscf/claim
- rscf/state/observation
- topic/implementation
- topic/core-infrastructure
- dated
- dated/2026-08-22
- canon/knowledge
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Core Infrastructure Modules

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — 8 new module directories (22 modules) implemented, exported, and tested.

## What was implemented

The user created 8 new core infrastructure module directories under `amos/`:

| Directory | Modules | Purpose |
|-----------|---------|---------|
| `amos/abi/` | 3 | Agent-Brain Interface: Model, Skill, Tool registries |
| `amos/adapters/` | 1 | BuiltinSkillExecutor — executes skills |
| `amos/graph/` | 3 | Causal, Dependency, Provenance graphs |
| `amos/memory/` | 4 | Context, Immune, Manager, Orientation |
| `amos/proof/` | 3 | ProofChecker, HypothesisField, RSCF functions |
| `amos/replay/` | 2 | EventBus, Ledger |
| `amos/runtime/` | 6 | Audit, Finalize, Planner, Router, Scheduler, Selector |
| `amos/server/` | 1 | HTTP server |

**Total**: 22 modules, 131 tests

## Module Details

### abi/ (Agent-Brain Interface)
- `ModelRegistry` + `ModelWorker` — model registration and execution
- `SkillRegistry` — skill discovery and registration
- `ToolRegistry` — tool registration

### adapters/
- `BuiltinSkillExecutor` — executes skills via the builtin adapter

### graph/
- `CausalGraph` — causal evidence tracking with levels
- `DependencyGraph` — dependency tracking
- `ProvenanceGraph` — provenance tracking with sybil score detection

### memory/
- `ContextBudgetGovernor` — context/token budget management
- `MemoryImmuneSystem` — memory immune system
- `MemoryManager` — memory management
- `OrientationCache` — orientation caching

### proof/
- `ProofChecker` — checks claims (scope/regime, confidence ceiling, causal level, falsifiers)
- `HypothesisField` — hypothesis management
- `RSCF` functions: `compile_claim`, `confidence_ceiling`, `selective_invalidate`

### replay/
- `EventBus` — event publishing
- `ledger` — replay ledger with `record()` function

### runtime/
- `SelfAudit` — self-audit gate
- `finalize` — state finalization
- `planner` — plan building (`build()`, `closure()`, `topo()`)
- `router` — task routing (`tensor()`, `complexity()`, `budget()`)
- `Scheduler` — plan execution scheduler
- `selector` — skill selection

### server/
- `serve()` — HTTP server for AMOS kernel

## Kernel Integration

All modules are wired into `AmosKernel`:
- `self.skills`, `self.tools`, `self.models` — registries (discovered at init)
- `self.events`, `self.memory` — event bus and memory manager
- `self.proof_checker` — ProofChecker instance
- `self.provenance` — ProvenanceGraph instance
- `select()`, `build()`, `Scheduler.run()` — runtime pipeline
- `SelfAudit().run(state)` — self-audit gate
- `finalize(state)` — state finalization
- Proof checking post-execution gate (added)

## Exports

All new classes and functions are exported from `amos/__init__.py`:
- Classes: ModelRegistry, ModelWorker, SkillRegistry, ToolRegistry, BuiltinSkillExecutor, CausalGraph, DependencyGraph, ProvenanceGraph, ContextBudgetGovernor, MemoryImmuneSystem, MemoryManager, OrientationCache, ProofChecker, HypothesisField, EventBus, SelfAudit, Scheduler
- Functions: compile_claim, confidence_ceiling, selective_invalidate, replay_record, finalize, plan_build, tensor, complexity, budget, select, serve

## Test Coverage

| Test File | Tests | Status |
|-----------|-------|--------|
| test_abi_registries.py | 11 | Pass |
| test_adapters_builtin.py | 18 | Pass |
| test_graph_modules.py | 26 | Pass |
| test_memory_modules.py | 26 | Pass |
| test_proof_modules.py | 22 | Pass |
| test_replay_modules.py | 11 | Pass |
| test_runtime_modules.py | 17 | Pass |
| **Total** | **131** | **All pass** |

## Verification

```bash
cd cosmo-brain/AMOS_OS_KERNEL
python3 -m pytest tests/ -q -p no:randomly
# 1934 passed, 0 failures
```

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS Completion Graph All 249 Gaps Closed
- 2026-08-22 AMOS Structural Gap Promotion 340-347

---
**MOC:** [[DATED_MOC]]
