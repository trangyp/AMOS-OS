---
title: 04 Scales MOC
type: moc
source: 25_COGNITIVE_MATRIX/04_SCALES
tags:
  - 04-scales
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 04 Scales — Map of Content

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **MECE Domain:** C — Cognitive Capability & Orchestration
> **Plane:** `25_COGNITIVE_MATRIX/04_SCALES`

**Path:** `25_COGNITIVE_MATRIX/04_SCALES`
**Files:** 2 | **Subdirectories:** 4

## Purpose

The Scales sub-plane defines the AMOS tri-layer cognitive scale architecture: **L (Low), M (Mid), H (High)**. This is the canonical implementation of the AMOS LMH tri-layer pattern that appears throughout the architecture — from the Trang LMH Architecture to the cognitive matrix scales to the execution runtime modes. Each scale represents a different level of cognitive abstraction, processing depth, and resource allocation.

The L/M/H scale system is NOT a simple hierarchy. It is a **governed multi-resolution system** where:
- **L (Low)**: Fast, reactive, pattern-matching, low-latency responses. Analogous to System 1 thinking.
- **M (Mid)**: Deliberative, analytical, moderate-depth processing. Analogous to System 2 thinking.
- **H (High)**: Deep reasoning, meta-cognitive, full validation, long-horizon planning. Analogous to reflective thinking.

## MECE Scope

Within the MECE partition ([[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]), `04_SCALES` is a sub-plane of `25_COGNITIVE_MATRIX` (Domain C — Cognitive Capability & Orchestration). Its primary ownership is **cognitive scale definitions and their inter-scale governance rules**. It does not own individual cognitive primitives (those belong to `01_PRIMITIVES/`) or lifecycle operations (those belong to `02_LIFECYCLE_OPERATIONS/`).

## Files

- [[25_COGNITIVE_MATRIX/04_SCALES/COGNITIVE_MATRIX_SCALES_CONTRACT|COGNITIVE_MATRIX_SCALES_CONTRACT]] — Formal contract governing scale transitions, scale-appropriate resource allocation, and inter-scale consistency requirements
- [[25_COGNITIVE_MATRIX/04_SCALES/SCALES_COGNITIVE_MATRIX_README|SCALES_COGNITIVE_MATRIX_README]] — README explaining the L/M/H scale architecture and its relationship to the broader AMOS system

## Subdirectories

### L_LOW_SCALE
- [[25_COGNITIVE_MATRIX/04_SCALES/L_LOW_SCALE/L_LOW_SCALE_MOC|L_LOW_SCALE_MOC]] — Low-scale cognitive operations: fast pattern matching, reactive responses, heuristic-based decisions. Operates with minimal validation depth and lowest latency. Scale consistency must be preserved — a low-scale response must not claim high-scale authority.

### M_MID_SCALE
- [[25_COGNITIVE_MATRIX/04_SCALES/M_MID_SCALE/M_MID_SCALE_MOC|M_MID_SCALE_MOC]] — Mid-scale cognitive operations: deliberative reasoning, analytical processing, moderate validation depth. Balances speed and accuracy. Most routine cognitive operations occur at this scale.

### H_HIGH_SCALE
- [[25_COGNITIVE_MATRIX/04_SCALES/H_HIGH_SCALE/H_HIGH_SCALE_MOC|H_HIGH_SCALE_MOC]] — High-scale cognitive operations: deep reasoning, meta-cognitive reflection, full validation chains, long-horizon planning. Highest resource cost but strongest epistemic guarantees. Required for consequential decisions.

## Scale Transition Rules

1. **Escalation**: L → M → H escalation is always permitted when validation depth is insufficient
2. **De-escalation**: H → M → L de-escalation requires explicit authority grant (cognitive capability != authority)
3. **Scale consistency**: A response generated at scale S must not claim authority beyond scale S
4. **Cross-scale provenance**: Any scale transition must preserve full provenance chain
5. **Scale-appropriate validation**: Each scale has a minimum validation depth that cannot be bypassed

## Relationships

### Upstream
- [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX]] — Parent cognitive matrix plane
- [[01_CANON/01_CANON_MOC|01_CANON]] — Canon laws constrain scale definitions and transition rules

### Downstream
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/01_PRIMITIVES_MOC|01_PRIMITIVES]] — Each primitive operates at one or more scales
- [[04_RUNTIME/06_EXECUTION/06_EXECUTION_MOC|06_EXECUTION]] — Execution modes map to cognitive scales
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]] — Control plane routes tasks to appropriate scales

### Peers
- [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/03_CONTROL_PLANES_MOC|03_CONTROL_PLANES]] — Control planes govern scale transitions
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS]] — Lifecycle operations span all scales
- [[11_KNOWLEDGE/trang/trang_MOC|Trang LMH]] — The Trang LMH Architecture is the canonical reference for the tri-layer pattern

## Epistemic Boundary

The L/M/H scale system is an `AMOS_MODEL` artifact. Its cognitive correspondence to human System 1/2/3 thinking is a `SOURCE_CLAIM` from cognitive science literature, not an `EMPIRICAL` observation of the AMOS runtime. Scale transition rules are formally specified but their runtime enforcement is `NOT_ESTABLISHED`.

`MODEL != OBSERVATION`
`DOCUMENTED != IMPLEMENTED`

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]
**MECE Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
