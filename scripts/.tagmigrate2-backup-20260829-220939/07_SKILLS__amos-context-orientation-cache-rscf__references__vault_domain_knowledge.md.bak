---
title: Vault Domain Knowledge — Amos Context Orientation Cache Rscf
type: reference
source: 07_SKILLS/amos-context-orientation-cache-rscf/references
tags:
- reference
- amos-context-orientation-cache-rscf
- type/skill
- cosmo-brain-moc
- 2026-08-22-amos-all-249-gaps-closed
- references-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
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
> Extracted from skill: `amos-context-orientation-cache-rscf`

## Vault-Sourced Content

### Source 1: Web Cache Posioning

> Path: `misc/W/Web_Cache_Posioning.md` | Size: 1897 chars | Match score: 7 | content_hash: a9c911c31485e63f

# Web Cache Posioning
Good Caching Settings

When Testing

What is it?

Impact

Prevention

---

---

### Source 2: AMOS Token and Context Governor

> Path: `misc/TO/TOKEN.md` | Size: 1147 chars | Match score: 7 | content_hash: 1b42a1453132a3d6

# AMOS Token and Context Governor

## Objective
Maximize decision-relevant information per token without deleting load-bearing structure.

## Priority score
Retain context in this order:
1. objective and hard constraints
2. decision-changing evidence
3. unresolved contradictions
4. load-bearing premises
5. provenance/freshness/scope
6. active hypotheses
7. required implementation details
8. reusable summaries
9. examples/background
10. redundant narrative

## Progressive disclosure
Do not load raw evidence by default.
Use:
`capsule -> relevant H -> relevant M -> relevant L -> raw`

## Drop rule
Drop an item only if removing it cannot reasonably change:
- answer
- decision
- confidence
- safety
- falsifier
- implementation correctness

## Context pressure
When context is near capacity:
- preserve constraints over prose,
- preserve dependency edges over explanations,
- preserve unresolved conflict over resolved history,
- snapshot before major compression.

---

---

### Source 3: AMOS Core Module Test Coverage

> Path: `dated/2026-08-22/2026-08-22 AMOS Core Module Test Coverage.md` | Size: 3326 chars | Match score: 6 | content_hash: 4a7ee77070a0c3ff

# AMOS Core Module Test Coverage

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — all 23 previously untested core modules now have dedicated test files.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Added dedicated test files for 23 core modules that previously had no test files.
These modules were tested indirectly through `test_kernel.py` but lacked focused
unit tests for their individual logic.

## New test files

| Test file | Module | Tests | Coverage |
|-----------|--------|-------|----------|
| `test_abi_registries.py` | `amos/abi/` (model, skill, tool) | 11 | Registry discover, ModelWorker |
| `test_graph_modules.py` | `amos/graph/` (causal, dependency, provenance) | 26 | Edges, ancestors, descendants, components, sybil score |
| `test_memory_modules.py` | `amos/memory/` (manager, context, immune, orientation) | 26 | Admit, quarantine, expire, budget packing, immune flags, cache |
| `test_proof_modules.py` | `amos/proof/` (checker, hypotheses, rscf) | 22 | Claim gates, confidence ceiling, dominance, selective invalidation |
| `test_runtime_modules.py` | `amos/runtime/` (planner, router, selector, audit, finalize) | 17 | Closure, topo, tensor, complexity, budget, select, audit, finalize |
| `test_adapters_builtin.py` | `amos/adapters/builtin.py` | 18 | All 12 builtin skills + edge cases |
| `test_replay_modules.py` | `amos/replay/` (events, ledger) | 11 | EventBus subscribe/emit, ledger record/hash |


## Test count progression

| Milestone | Python tests | TypeScript tests | Total |
|-----------|-------------|-----------------|-------|
| Gaps 91-320 closed | 1505 | 1142 | 2647 |
| Cognitive matrix 321-339 | 1533 | 1142 | 2675 |
| Core module test coverage | *1934* | *1195* | *3129* |

## Key lessons

1. **Claim dataclass**: Uses `text` (not `hypothesis`) and requires `epistemic` as a required positional arg.
2. **KernelState**: The state type is `KernelState`, not `TaskState`.
3. **QueryTensor**: Has `consequence_radius` (not `urgency`).
4. **Uncertainty defaults**: Non-zero (max=0.5 for evidence) — complexity C0 requires explicitly setting low uncertainty in task context.
5. **selective_invalidate**: Does NOT add the failed_id itself to the invalid set — only invalidates dependents.
6. **Evidence dataclass**: Requires `source_id`, `source_family`, `content` (not `kind`, `source`, `payload`).
7. **ProvenanceGraph.components**: Returns root sets, not all member IDs. Connected items share the same root set.
8. **ModelManifest/SkillManifest/ToolManifest**: Check `__dataclass_fields__` before constructing test fixtures — field names differ from what you might expect.

## Anti-fabrication

- `python3 -m pytest tests/ -q` run 2026-08-22 → 1678 passed, 0 failed.
- All 7 new test files pass individually and as part of the full suite.

## Links

- [[COSMO_BRAIN_MOC]]
- 2026_08_22_AMOS_ALL_249_GAPS_CLOSED

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-context-orientation-cache-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-context-orientation-cache-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
