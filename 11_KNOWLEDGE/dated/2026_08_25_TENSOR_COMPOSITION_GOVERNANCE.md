---
title: 2026-08-25 Tensor Composition Governance
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, tensors, governance, composition, dated, dated/2026-08-25]
---


# 2026-08-25 — Tensor Composition Governance Layer

## Gap found

`TENSOR_CONTRACTS.md` states the compatibility invariant — *"tensor composition is prohibited until shared axes are semantically compatible; same-name axes do not prove same meaning"* — and `amos-tensor-operations-agent` implements it for same-system compositions. But nothing governed **cross-layer composition**: after eight consolidation passes, the five QFM layers each produce tensor-shaped outputs that now meet each other, and same-name/different-meaning collisions concentrate exactly there. The known hazards were never encoded: 19-length axes from different family systems, mixed QCI claim classes, L1→L5 joins.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-tensor-composition-governance` — invariant restated as executable contract; 5-check axis table with fail examples; 4 decision rules incl. pairing-vs-merge distinction |
| Agent | `.devin/agents/amos-tensor-composition-auditor-agent.json` — 5 capabilities incl. cross-layer hazard scan and silent-composition detector |
| Workflow | `.devin/workflows/tensor-composition-governance-workflow.md` — 7-step gate procedure |
| Memory + vault note | recorded |

## Key design decisions

1. **Pairing ≠ merge**: disjoint-axis tensors may be juxtaposed but never labeled as fused information.
2. **Projection over block** when only one axis fails: compatible sub-axes compose; the incompatible axis is dropped *with a logged reason* — no all-or-nothing rigidity, but also no silent dropping.
3. **Minimum provenance class inheritance**: composed outputs take the lowest class of inputs unless demotion is explicit.
4. **19-length ≠ compatibility**: the B3 lesson (address-space kinship ≠ meaning identity) now enforced at the tensor axis level.

## Meta-note
This closes the last unowned composition surface in the QFM architecture: knowledge (L1), bridges (L2), dynamics (L3), collapse (L4), enforcement (L5) can each produce tensors, and every join between them now passes a named gate with an owning agent.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
