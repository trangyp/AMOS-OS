---
title: Vault Domain Knowledge — Arxiv Test Time Training Rscf
type: reference
source: 07_SKILLS/arxiv-test-time-training-rscf/references
tags:
- reference
- arxiv-test-time-training-rscf
- type/skill
- 2026-08-22-19x19-ai-cognitive-field
- 2026-08-22-tests-logic-bridge-registry
- 2026-08-22-amos-all-249-gaps-closed
- 2026-08-23-amos-abi-and-io-test-expansion
- 2026-08-22-amos-core-module-test-coverage
- 2026-08-22-amos-go-board-19x19-formal-system
- 2026-08-22-typescript-data-quality-governance
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
> Extracted from skill: `arxiv-test-time-training-rscf`

## Vault-Sourced Content

### Source 1: AMOS Runtime Test Expansion

> Path: `dated/2026-08-23/2026-08-23 AMOS Runtime Test Expansion.md` | Size: 2864 chars | Match score: 20

# AMOS Runtime Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Runtime module tests expanded from 17 to 37, IO tests fixed and expanded.

## What was done

### Runtime Modules (`tests/test_runtime_modules.py`)
- **Before**: 17 tests (basic closure, topo, build, tensor, complexity, budget, select, audit, finalize)
- **After**: 37 tests (+20 new)

New tests cover:
- Transitive dependency closure (a→b→c)
- Multiple root closure
- Self-dependency closure
- Topological sort chain ordering
- Topological sort with no dependencies
- Priority ordering (lower priority = earlier in order)
- Tensor with critical stakes, domain, irreversibility
- Complexity monotonicity (higher stakes ≥ lower stakes complexity)
- Budget monotonicity (C4 tokens > C0 tokens)
- Budget for all complexity levels (C0-C4)
- Selector with empty skills
- Selector C0 returns core skills
- Selector C4 adds all available skills
- Finalize with no claims → DERIVED (not UNKNOWN)
- Finalize with mixed VERIFIED + UNKNOWN → DERIVED (not all VERIFIED)
- Finalize with all VERIFIED → VERIFIED
- Finalize produces final dict
- Finalize preserves gates

### IO Module Fix (`amos/io.py`)
- Fixed `task_from(d)` to provide default `""` for missing `objective`
- This allows `payload({})` to create a default task instead of raising `TypeError`

## Key Behaviors Discovered

### `finalize(state)` Status Priority
1. FAIL gates → `Status.UNKNOWN`
2. Competing claims (with `competing_ids`, not INVALIDATED/QUARANTINED) → `Status.COMPETING`
3. Conditional gates or memory gaps → `Status.CONDITIONAL`
4. All claims VERIFIED → `Status.VERIFIED`
5. Else → `Status.DERIVED`

Mixed VERIFIED + UNKNOWN claims = `DERIVED` (not all VERIFIED).

### `closure(roots, skills)` Behavior
- Transitive: a→b→c closure includes all three
- Self-dependency: a→a is handled (returns {a})
- Missing skill raises `KeyError`

### `topo(roots, skills)` Behavior
- Lower priority value = earlier in order
- Dependencies always come before dependents
- No deps = sorted by priority

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3129** | **Both green** |

## Links (2)

- [[COSMO_BRAIN_MOC]]
- 2026_08_23_AMOS_ABI_AND_IO_TEST_EXPANSION
- 2026_08_22_AMOS_CORE_MODULE_TEST_COVERAGE

---

### Source 2: AMOS 19×19 Go Board — Runtime Methods (62+ Sections)

> Path: `dated/2026-08-22/2026-08-22 AMOS Go Board 19x19 Runtime Methods.md` | Size: 5500 chars | Match score: 12

# AMOS 19×19 Go Board — Runtime Methods (62+ Sections)

> New executable methods added to `cosmo-brain/AMOS_GO_BOARD_19X19.py` to make the 75-section formal specification runnable. 226 self-tests + 251 integration tests pass; 0 failures. 811 grand total across all suites (including 15 Obsidian bridge tests).
>
> Source: `cosmo-brain/AMOS_GO_BOARD_19X19.py`
> See also: 2026_08_22_AMOS_GO_BOARD_19X19_FORMAL_SYSTEM · 2026_08_22_19X19_AI_COGNITIVE_FIELD · 2026_08_22_TESTS_LOGIC_BRIDGE_REGISTRY

## 1. Move transition engine (§10-11)

`Board19.move_transition(x, y, color)`

```
T = T_O ∘ T_G ∘ T_L ∘ T_E ∘ T_A ∘ T_K ∘ T_Φ ∘ T_Ω ∘ T_M
```

- `T_O` occupancy update
- `T_G` group recompute
- `T_L` liberty recompute
- `T_E` eye detection
- `T_A` aji update
- `T_K` ko detection
- `T_Φ` influence field update
- `T_Ω` option count
- `T_M` memory record

Returns legal flag, cell, color, eyes, aji, ko, influence sum, option count, memory record.

## 2. New runtime methods by section

| Section | Method | Purpose |
|---------|--------|---------|
| 11 | `move_transition(x, y, color)` | Compositional engine T_O∘T_G∘...∘T_M |
| 12 | `dependency_cone(x, y)` | Affected cells, causal reach, causal depth |
| 15 | `permeability(x, y)` | Vulnerable / total boundary channels; hostile invasion porosity |
| 17 | `liberty_independence(x, y)` | Liberty coupling, redundancy, independent count |
| 18-19 | `detect_eyes(x, y)` | Eye positions, quality, PVR, robustness, life |
| 20-23 | `update_aji(x, y)`, `aji_half_life()`, `aji_latent_threat()` | Aji status, opportunity, weakness, decay, threat |
| 24 | `sente_compression(x, y)` | Option-space constraining ratio |
| 25-26 | `gote_cost(x, y)`, `initiative_balance()` | GoteCost, I_Δ initiative balance |
| 27 | `detect_ko()` | Recurrence / forbidden-cycle detection |
| 28 | `ko_leverage(x, y)` | KoLeverage=ThreatValue/LocalCost |
| 29-32 | `compute_influence()`, `compute_territory()`, `influence_gradient()`, `phase_state()` | Influence/territory/gradient/phase fields |
| 33-34 | `territory_debt(x, y)`, `influence_value(x, y)` | TerritoryDebt, InfluenceValue=Expected-Risk |
| 35-38 | `option_space()`, `option_count()`, `option_diversity()`, `option_concentration_risk()`, `future_debt_tensor()` | Future option set, diversity, concentration, 7-component debt |
| 39-41 | `record_move_memory()`, `memory_decay()` | Memory priority, 4 classes, exponential decay |
| 43-46 | `scale_consistency()`, `scale_betrayal()`, `scale_integrity()` | SC, Betrayal, Integrity (bottleneck) |
| 48 | `region_residual()` | Region compression residual |
| 49 | `symmetry_breaking_count()` | D4 distinction entropy |
| 50 | `orbit_class(x, y)` | Orbit sizes: 1/4/8 |
| 51 | `distinction_entropy()` | Entropy of marked vs empty distribution |
| 52-54 | `lacunarity(window_size)` | Λ(r)=Var(Mass)/Mean² |
| 55 | `pressure_field()`, `group_pressure()`, `pressure_to_repair_ratio()` | Pressure and PRR |
| 56-57 | `repair_externality(x, y)` | NetRepair, OverRep

---

### Source 3: AMOS Core Runtime Modules

> Path: `dated/2026-08-22/2026-08-22 AMOS Core Runtime Modules.md` | Size: 3079 chars | Match score: 12

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
- [[COSMO_BRAIN_MOC]]
- 2026_08_22_AMOS_ALL_249_GAPS_CLOSED
- 2026_08_22_TYPESCRIPT_DATA_QUALITY_GOVERNANCE

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: arxiv-test-time-training-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/arxiv-test-time-training-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
