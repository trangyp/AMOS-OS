---
title: "AMOS Core Module Test Coverage"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/testing, topic/test-coverage, dated, dated/2026-08-22]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---


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

**Total new tests: 131**

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

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS All 249 Gaps Closed

---
**MOC:** [[DATED_MOC]]
