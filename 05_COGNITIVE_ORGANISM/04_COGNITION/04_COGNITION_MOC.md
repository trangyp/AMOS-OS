---
title: 04 Cognition MOC
type: moc
source: 05_COGNITIVE_ORGANISM/04_COGNITION
tags:
  - 04-cognition
  - canon/cognitive
  - amos-cognition-engine
  - first-principles-reasoning
  - fractal-reasoning
  - human-intelligence-engine
  - nbi-engine
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 04 Cognition — Map of Content

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **MECE Domain:** C — Cognitive Capability & Orchestration
> **Plane:** `05_COGNITIVE_ORGANISM/04_COGNITION`

**Path:** `05_COGNITIVE_ORGANISM/04_COGNITION`
**Files:** 5 | **Subdirectories:** 0

## Purpose

The Cognition sub-plane defines the core reasoning engines that power the AMOS cognitive organism. These engines implement different reasoning paradigms — from first-principles deduction to fractal multi-scale analysis to human intelligence modeling — that together form the cognitive processing core of the AMOS Full Brain OS.

## MECE Scope

Within the MECE partition ([[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]), `04_COGNITION` is a sub-plane of `05_COGNITIVE_ORGANISM` (Domain C — Cognitive Capability & Orchestration). Its primary ownership is **reasoning engine definitions and their cognitive processing properties**. It does not own memory substrates (those belong to `10_MEMORY`), model calibration (those belong to `13_MODELS`), or cognitive matrix primitives (those belong to `25_COGNITIVE_MATRIX/01_PRIMITIVES`).

## Files

### AMOS_COGNITION_ENGINE
- [[11_KNOWLEDGE/engine/AMOS_COGNITION_ENGINE|AMOS_COGNITION_ENGINE]] — The master cognition engine that orchestrates all reasoning modes. Located in the knowledge engine directory as it bridges knowledge representation and cognitive processing. Implements the 6-layer cognition architecture with validation depth mapping.

### FIRST_PRINCIPLES_REASONING
- [[05_COGNITIVE_ORGANISM/04_COGNITION/FIRST_PRINCIPLES_REASONING|FIRST_PRINCIPLES_REASONING]] — First-principles reasoning engine that decomposes complex problems into fundamental axioms and rebuilds solutions from ground truth. Critical for AMOS's epistemic integrity — prevents reasoning from unverified assumptions. Enforces the `SOURCE_CLAIM != VERIFIED` boundary in reasoning chains.

### FRACTAL_REASONING
- [[05_COGNITIVE_ORGANISM/04_COGNITION/FRACTAL_REASONING|FRACTAL_REASONING]] — Fractal reasoning engine that applies the same reasoning structure at multiple cognitive scales (signal, word, concept, chunk, lesson, skill, habit, identity). Enables scale-appropriate reasoning depth and cross-scale consistency. Connects to the fractal learning and memory reduction engine in `10_MEMORY`.

### HUMAN_INTELLIGENCE_ENGINE
- [[05_COGNITIVE_ORGANISM/04_COGNITION/HUMAN_INTELLIGENCE_ENGINE|HUMAN_INTELLIGENCE_ENGINE]] — Models human-like intelligence processes including dual-system thinking (System 1 fast / System 2 slow), emotional cognition, and social reasoning. Provides the cognitive substrate for AMOS's human interaction engine and UBI framework.

### NBI_ENGINE
- [[05_COGNITIVE_ORGANISM/04_COGNITION/NBI_ENGINE|NBI_ENGINE]] — Neurobiological Intelligence (NBI) engine that implements the UBI NBI domain's cognitive processes. Models neurobiological substrates of intelligence including neural coding, synaptic plasticity, and cortical dynamics. Bridges the bio-neuro domain to the cognitive organism.

## Relationships

### Upstream
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — Parent cognitive organism plane
- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL]] — Kernel invariants constrain reasoning engine behavior
- [[01_CANON/01_CANON_MOC|01_CANON]] — Canon laws govern which reasoning modes are admissible

### Downstream
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09 Inference]] — Inference primitive uses cognition engines
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_MOC|L23 Metacognition]] — Metacognition monitors cognition engine output
- [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]] — Runtime executes cognition engine outputs
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY]] — Observability tracks cognition engine performance

### Peers
- [[05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/15_HOMEOSTASIS_MOC|15_HOMEOSTASIS]] — Homeostasis regulates cognitive resource allocation
- [[11_KNOWLEDGE/engine/ENGINE_MOC|11_KNOWLEDGE Engine]] — Knowledge engine provides the information substrate
- [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI Domain]] — Neurobiological intelligence domain

## Epistemic Boundary

Cognition engines are `AMOS_MODEL` artifacts. Their reasoning outputs are `DERIVED` from their inputs and architecture. A cognition engine's output does not become an `EMPIRICAL` observation by virtue of being computed. Reasoning quality must be validated through the test and observability planes.

`MODEL != OBSERVATION`
`REASONING_OUTPUT != VERIFIED_TRUTH`
`DOCUMENTED != IMPLEMENTED`

______________________________________________________________________

**Parent:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
**MECE Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
