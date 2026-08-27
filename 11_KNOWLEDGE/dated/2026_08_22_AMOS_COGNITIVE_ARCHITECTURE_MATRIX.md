---
title: "AMOS Cognitive Architecture Matrix"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/completion-graph, topic/cognitive-architecture, dated, dated/2026-08-22]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Cognitive Architecture Matrix

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — the 4-axis matrix is generated, addressable, and the 19 explicit gaps are closed in the AMOS OS Kernel.

## Purpose

The Cognitive Architecture Matrix exposes the **interaction space** of AMOS cognition, not just its modules. A flat gap list hides missing *interactions*; the matrix makes them addressable.

- **13,770 addressable cells** (30 × 17 × 9 × 3)
- **1.98% existing**
- **22.96% partial**
- **7.04% explicitly missing**
- **68.02% structural gaps** (9,367 cells) — interactions not yet recognized or named
- These 9,367 structural cells collapse to **243 structural-gap unknown-unknowns** (one per primitive × plane pair) plus **3 original unknown-unknowns** = **246 total unknown-unknowns** tracked

## The four axes

| Axis | Count | Description |
|------|------:|-------------|
| P — Primitives | 30 | L0–L29 cognitive primitives (reality, sensing, attention, memory, reasoning, action, learning, etc.) |
| C — Control planes | 9 | C1–C9 governance/execution planes (sense, focus, recall, reason, affect, act, signal, self, etc.) |
| O — Lifecycle operations | 17 | Encode, bind, recall, predict, plan, act, monitor, repair, evolve, etc. |
| S — Scales | 3 | Individual (L), collective (M), planetary / high (H) |

## Status classes

- `e` — existing
- `p` — partial
- `m` — explicitly missing (with gap reference)
- `g` — structural gap

## Artifacts

| Artifact | Location | Role |
|----------|----------|------|
| Spec | `AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md` | Human-readable design |
| JSON | `AMOS_Cognitive_Architecture_Matrix.json` | 13,770 queryable cells |
| Builder | `build_amos_cognitive_matrix.py` | Reproducible generator |
| Seeder | `cosmo-brain/AMOS_OS_KERNEL/amos/governance/seed_cognitive_matrix.py` | Kernel wiring |
| Module | `cosmo-brain/AMOS_OS_KERNEL/amos/governance/cognitive_matrix.py` | `CognitiveMatrixGovernor` |

## 19 explicit missing interactions (now closed)

Gaps 321-339 map to 19 (primitive, plane) pairs that the AMOS OS Kernel closed as `GapKind.RELATION` with complete 11-layer chains. See `2026-08-22 AMOS Cognitive Architecture Matrix Governance.md` for the full table.

## Key findings

- Existing coverage clusters in **L18 Action**, **L28 Governance**, **L29 Evolution** × **C1 / C8 / C9** — consistent with the kernel treating the LLM as replaceable.
- **Representation (C5)** and **Perception (C7)** planes are 0% existing — deepest gaps.
- Scale **H** (high / hard / long-horizon) is where most structural gaps concentrate.

## Architectural invariant

```
LLM ⊂ CognitiveExecution
AMOS = Kernel + CognitiveRuntime + MemorySystem + WorldModel
      + ReasoningSystem + SimulationSystem + DecisionSystem
      + LearningSystem + AgentSystem + GovernanceSystem
AMOS ≠ LLM
```

## Next steps

1. Triage 9,367 structural gaps by (irreversibility × dependency-centrality × scale).
2. Promote high-value `g` → `m` (name them, assign gap IDs past 339).
3. Fill `m` → `p` → `e` via governed evolution, with each matrix cell as a unit of progress.
4. Re-run `build_amos_cognitive_matrix.py` as maturity / coverage scores change.

## Anti-fabrication

- Source: `AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md` and `AMOS_Cognitive_Architecture_Matrix.json`.
- 19 matrix gaps are CLOSED and tested: `python3 -m pytest tests/test_cognitive_matrix.py -q`.

## Links
- [[00_Cosmo_Brain_MOC]]
- 2026-08-22 AMOS Cognitive Architecture Matrix Governance
- 2026-08-22 AMOS All 249 Gaps Closed
