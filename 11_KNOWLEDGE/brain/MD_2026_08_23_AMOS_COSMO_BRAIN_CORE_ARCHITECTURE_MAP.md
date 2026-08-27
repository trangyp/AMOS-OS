---
title: "AMOS Cosmo Brain Core — TypeScript Architecture Map"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/typescript, topic/architecture, topic/core-modules, brain]
status: "complete"
provenance: "OBSERVATION"
confidence: "HIGH"
---

# AMOS Cosmo Brain Core — TypeScript Architecture Map

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — Complete architecture map of `cosmo-brain/core/`.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview

The `cosmo-brain/core/` directory contains the TypeScript implementation of
the AMOS Cosmo Brain's core modules. It has **26 TypeScript files** across
**8 subdirectories**, totaling **6,365 lines** of code. All modules are
created by Trang Phan and implement brain specs from the `_00_Cosmo brain/`
vault directory.

## Directory Structure

```
core/
├── type-guards.ts              (100 lines) — Runtime type narrowing
├── constraints/index.ts        (180 lines) — Constraint engine
├── validation/index.ts         (157 lines) — Input validation
├── design-synthesis/index.ts   (614 lines) — Design spec synthesis
├── identity/
│   ├── core.ts                 (83 lines)  — System identity + IP rules
│   └── index.ts                (107 lines) — User identity + consent state
├── memory/
│   ├── index.ts                (116 lines) — Memory architecture types
│   ├── session.ts              (160 lines) — Per-session memory
│   ├── timeline.ts             (202 lines) — Append-only event store
│   └── user-preferences.ts     (178 lines) — User goals + preferences
├── reasoning/
│   ├── index.ts                (107 lines) — Reasoning chains + provenance
│   ├── meta-logic.ts           (407 lines) — 5-law meta-logic kernel
│   └── safety-filter.ts        (205 lines) — Output safety + claim filtering
├── orchestration/
│   ├── index.ts                (371 lines) — Pipeline orchestrator
│   ├── pipeline.ts             (659 lines) — Full pipeline runner
│   ├── routing.ts              (121 lines) — Algorithm routing
│   └── consent.ts              (137 lines) — Consent gate
├── epistemics/
│   ├── index.ts                (95 lines)  — Barrel export
│   ├── claims.ts               (326 lines) — Evidence + conclusion classes
│   ├── rscf.ts                 (340 lines) — RSCF proof capsules
│   ├── competing-hypotheses.ts (250 lines) — Hypothesis field
│   ├── provenance.ts           (350 lines) — Provenance graph + Sybil hardening
│   ├── falsifiers.ts           (238 lines) — Sensitivity + falsifiers
│   ├── adversarial-validation.ts (344 lines) — 9-step adversarial validation
│   ├── regime-freshness.ts     (263 lines) — Applicability envelope + freshness
│   └── error-recovery.ts       (255 lines) — Error recovery engine
└── AMOS_CORE v3.1–v4.4         (14 .txt spec files) — Version history
```

## Module Details

### 1. type-guards.ts (100 lines)
Runtime type narrowing for all modules.
- `isRecord`, `isString`, `isNumber`, `isBoolean`, `isArray`, `isNull`, `isUndefined`, `isPrimitive`
- `isFiniteNumber`, `isPositiveNumber`, `isInteger`, `isInRange`, `isOneOf`
- `assertRecord`, `assertString`, `assertNumber`, `assertBoolean`
- **Tests**: 39 tests (`type-guards.test.ts`)

### 2. constraints/index.ts (180 lines)
Constraint engine enforcing invariants, safety limits, and data boundaries.
- `Constraint` interface with `check()` function
- `ConstraintSeverity`: error | warning | info
- `ConstraintEngine` class: register, check, checkAll
- **Tests**: 25 tests (`constraints.test.ts`)

### 3. validation/index.ts (157 lines)
Input validation and sanitisation for all pipeline stages.
- `ValidationRule`, `ValidationResult`, `Validator` classes
- Audio input validation: duration, buffer length, sample rate
- String length limits, scan type validation
- **Tests**: 24 tests (`validation.test.ts`)

### 4. design-synthesis/index.ts (614 lines)
Turns COSMO requirement documents into structured AMOS-governed design specs.
- 5 conclusion classes: SOURCE_CLAIM, DERIVED, MODEL, CONDITIONAL, UNKNOWN_GAP
- Evidence-first reasoning with provenance back to source document
- Uncertainty/boundary preservation
- Product screen mapping
- **Tests**: 4 tests (`design-synthesis.test.ts`)

### 5. identity/ (190 lines total)
- **core.ts**: System identity, architect info, IP rules (Cosmo Identity Law)
- **index.ts**: User identity, consent state, privacy preferences
- **Tests**: 32 tests (`identity.test.ts`)

### 6. memory/ (656 lines total)
- **index.ts**: Memory architecture types (8 memory classes)
- **session.ts**: Per-session data with encryption + retention
- **timeline.ts**: Append-only chronological event store
- **user-preferences.ts**: User goals, preferences, personalisation signals
- **Tests**: 73 tests (3 files: `memory-session`, `memory-timeline`, `memory-user-preferences`)

### 7. reasoning/ (719 lines total)
- **index.ts**: Reasoning chains with provenance tracking
  - `createChain`, `addStep`, `conclude`, `explainChain`, `mergeChains`
  - Multiplicative confidence propagation
- **meta-logic.ts**: 5-law meta-logic kernel (Law of Law, Rule of 2, Rule of 4, Signal Fidelity)
  - 12 logic modes from CORE-19 Reasoning Kernel
  - Algebraic properties per mode
- **safety-filter.ts**: Output safety + claim filtering
  - Filters user-facing outputs through safety governance
  - Diagnostic language filtering
- **Tests**: 80 tests (3 files: `meta-logic`, `meta-logic-bug`, `safety-filter`)

### 8. orchestration/ (1,288 lines total)
- **index.ts**: Pipeline orchestrator routing user actions through Resonance Scan
  - 11 pipeline stages: consent_check → input_validation → audio_quality → preprocessing → feature_extraction → pitch_detection → noise_suppression → resonance_analysis → normalisation → artwork_generation → recommendation
- **pipeline.ts**: Full pipeline runner (659 lines, largest module)
  - Executes all stages end-to-end
  - Provenance chain, consent audit, algorithm execution records
- **routing.ts**: Deterministic routing of actions to algorithm modules
- **consent.ts**: Consent verification gate before any processing
- **Tests**: 59 tests (3 files: `orchestration-pipeline`, `orchestration-routing`, `orchestration-consent`)

### 9. epistemics/ (2,361 lines total — largest subdirectory)
Implements the `30_epistemics/` brain directory in TypeScript:
- **claims.ts**: Evidence + conclusion classes (6 evidence, 6 conclusion)
  - Core invariant: Claim strength ≤ evidence strength
  - Confidence ceiling: Conf(C) ≤ min_i Conf(P_i)
- **rscf.ts**: RSCF (Reasoned Source-Claimed Formal) proof capsules
  - Reuse gate: dependencies, scope, regime, freshness, provenance validity
  - Selective invalidation: only descendant claims affected
  - Causal level classification (CAUSAL/CORRELATIONAL/DESCRIPTIVE)
  - `isStale()` + `needsRevalidation()` (split as of 2026-08-23)
- **competing-hypotheses.ts**: Maintain incompatible claims as COMPETING
  - Collapse only with discriminating evidence
  - Do not collapse on: authority, source count, stylistic certainty, popularity
- **provenance.ts**: Provenance graph + Sybil hardening
  - Union-find algorithm for independent evidence groups (as of 2026-08-23)
  - Sybil resistance: source identity resolution, ancestry traversal, cycle detection
  - IndependentSupport ≤ number_of_independent_ancestry_components
- **falsifiers.ts**: Sensitivity analysis + falsifier types
  - 8 falsifier types: contradictory observation, source update, failed premise, scope mismatch, counterexample, benchmark failure, invariant violation, environment drift
  - Sensitivity: 1.0/(1.0 + premiseMargin) for above-threshold premises (as of 2026-08-23)
- **adversarial-validation.ts**: 9-step adversarial validation
  - For consequential conclusions: construct strongest, seek contradiction, test correlated provenance, test stale premises, test scope leakage, test hidden dependency, test causal overreach, test stronger alternative, test sensitivity
- **regime-freshness.ts**: Applicability envelope + freshness tensor
  - 7-axis applicability envelope: system/population, environment, scale, time, regime, measurement_method, assumptions
  - Regime changes selectively invalidate claims
- **error-recovery.ts**: Error recovery engine
  - 7-step recovery: mark failed, identify descendants, preserve unrelated, roll back, reroute, revalidate affected, preserve history
- **Tests**: 139 tests (7 files)

## AMOS_CORE Version History (14 spec files)

| Version | Name | Key Innovation |
|---------|------|----------------|
| v3.1 | Logic Fixed | Deterministic reasoning kernel |
| v3.2.1 | RSCF HML Recursive | RSCF proof capsules + HML recursion |
| v3.3 | Governed Meta-Evolution | Meta-evolution governance |
| v3.4.1 | Distributed Causal Evolution | Distributed causal evolution |
| v3.5 | Epistemic Regime Lineage | Epistemic regime lineage |
| v3.7 | Provenance Topology | Provenance topology |
| v3.7.1 | Provenance Topology Hardened | Hardened provenance topology |
| v3.8 | Iterative Provenance | Iterative provenance |
| v3.9 | Persistent Incremental Provenance | Persistent incremental provenance |
| v4.0 | MVCC Causal Concurrency | MVCC causal concurrency |
| v4.1 | Transactional Multi-RSCF | Transactional multi-RSCF |
| v4.2 | Deterministic Causal Epoch | Deterministic causal epoch |
| v4.3 | Hardened Adaptive Epoch | Hardened adaptive epoch |
| v4.4 | Coordination Avoidance | Coordination avoidance |

## Test Coverage Summary

| Module | Test Files | Tests |
|--------|-----------|-------|
| type-guards | 1 | 39 |
| constraints | 1 | 25 |
| validation | 1 | 24 |
| design-synthesis | 1 | 4 |
| identity | 1 | 32 |
| memory | 3 | 73 |
| reasoning | 3 | 80 |
| orchestration | 3 | 59 |
| epistemics | 7 | 139 |
| **Total** | **21** | **475** |

## Key Design Principles

1. **Evidence-first reasoning**: Every claim carries a conclusion class and provenance back to source
2. **Claim strength ≤ evidence strength**: Core invariant from `claims.ts`
3. **Confidence ceiling**: Conf(C) ≤ min_i Conf(P_i) for unresolved load-bearing premises
4. **Selective invalidation**: When a premise fails, only descendant claims are invalidated
5. **Independent confirmation must be demonstrated**: Not assumed (Sybil hardening)
6. **Regime-aware freshness**: Sources can remain historically accurate while decision-invalid
7. **Multiplicative confidence**: Reasoning chain confidence = product of step confidences
8. **Consent-gated processing**: No processing without verified consent
9. **Append-only timeline**: User journey events are never deleted
10. **AMOS governance**: All outputs filtered through safety + claim governance

## Recent Fixes (2026-08-23)

1. **`isStale()` / `needsRevalidation()` split**: `isStale()` now only checks `validUntil`;
   `needsRevalidation()` checks `revalidateAfter` but not yet stale
2. **Union-find for independent groups**: `provenance.ts` uses union-find algorithm instead
   of greedy grouping for correct independent evidence group computation
3. **Sensitivity formula**: `falsifiers.ts` uses `1.0/(1.0 + premiseMargin)` for above-threshold
   premises (was `1.0 - premiseMargin/margin` which could go negative)
4. **Claim validation bypass**: `epistemics-claims.test.ts` sets `claim.confidence = 1.5`
   directly to test the validator (factory clamps to [0,1])

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Kafka Brain Buffer Complete Fix
- 2026-08-23 AMOS Gap Discovery Engine All 6 Modes
- 2026-08-23 AMOS Unknown-Unknown Registry

---
**MOC:** [[BRAIN_MOC]]
