---
title: SKILL
type: skill
name: amos-formal-engines-master
description: AMOS Formal Engines — MURK 19x19, Go Board 19x19, tensor composition, formal specifications, proof systems. 6 typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) with 5-check axis table. Use for formal re...
parent_skill: none
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-formal-engines-master]
---

# L02_ATTENTION — Purpose

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 24 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 24 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `02_KERNEL/01_META_LOGIC/K_META_LOGIC.md`).

## When to Use

- When performing formal verification, symbolic execution, proof checking, or mathematical reasoning
- When using MURK 19x19 interaction matrix for absolute logic reasoning
- When using Go Board 19x19 for compositional game-theoretic analysis
- When composing typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) with axis compatibility gates
- When building formal specifications, proof systems, or constraint propagation
- When a child skill routes a formal verification or proof task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **formal_engines.execute_formal**: Execute AMOS Formal Engines formal engines: MURK 19x19, Go Board, tensor composition, and RSCF proof systems.
- **formal_engines.validate_formal**: Validate AMOS Formal Engines proofs for completeness, soundness, tensor contract compliance, and axiom application.
- **formal_engines.analyze_tensor**: Analyze AMOS Formal Engines tensor structure: typed cells, axis compatibility, composition gates, and relation topology.
- **formal_engines.trace_formal_provenance**: Trace AMOS Formal Engines formal outputs to axioms, inference rules, tensor contracts, and proof graph.
- **formal_engines.assess_formal_claim**: Assess AMOS Formal Engines formal claims for proof status, tensor compatibility, gap registry, and invariant compliance.
- **formal_engines.manage_formal_lifecycle**: Manage AMOS Formal Engines formal lifecycle: axiomatize, derive, validate, cross-check, and finalize proof.
- **formal_engines.detect_formal_drift**: Detect formal drift: axiom erosion, tensor axis mismatch, proof graph degradation, and invariant violation.
- **formal_engines.escalate_formal_gaps**: Escalate AMOS Formal Engines formal gaps: flag unproven claims, tensor incompatibility, trigger gap registry repair.
- **formal_engines.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **formal_engines.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **formal_engines.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/amos-general/A/forex/AMOS forex__packages__murk__primitives.md` (content_hash: b289395a883dab29), `_00_Cosmo brain/amos-general/A/amos/amos-go-board-19x19.md` (content_hash: 7d5f3bb30310282b) (vault canon, SOURCE_CLAIM)

### MURK 19 Primitive Definitions

The MURK (Absolute Logic) kernel defines 19 typed primitives represented as an Enum for strict type-checking:

| # | Primitive | Class |
|---|-----------|-------|
| 1 | Existence | ontological |
| 2 | NonExistence | ontological |
| 3 | Causality | causal |
| 4 | Temporal | temporal |
| 5 | Informational | informational |
| 6 | Topological | spatial |
| 7 | Identity | identity |
| 8 | Convergence | dynamic |
| 9 | Divergence | dynamic |
| 10 | Paradox | paradox |
| 11 | PositiveLogic | logic-valence |
| 12 | NegativeLogic | logic-valence |
| 13 | ZeroLogic | logic-valence |
| 14 | DualLogic | logic-valence |
| 15 | MultiLogic | logic-valence |
| 16 | MetaLogic | meta |
| 17 | SupraLogic | meta |
| 18 | AntiLogic | meta |
| 19 | NullLogic | meta |

The 19x19 interaction matrix (361 cells) provides 100% direct coverage of all primitive interactions. 5 resolution laws govern conflict resolution. The MURK reasoning engine is implemented at `cosmo-brain/AMOS_MURK_REASONING_ENGINE.py` with 231 total tests.

### Go Board 19x19 Formal System

The Go Board 19x19 is a formal system implementing 62+ sections from a 75-section formal spec (83%+). Key components:

- **Compositional engine**: `T = T_O∘T_G∘T_L∘T_E∘T_A∘T_K∘T_Φ∘T_Ω∘T_M`
- **Dependency cone**: CR (cone reach) / CD (cone depth)
- **Liberty independence graph**: eye topology (EyeQuality/PVR/Robustness)
- **Aji system**: DAG with half-life and latent threat tracking
- **Memory system**: decay, classes, prio
- [[AGENT_TEMPLATE]]
