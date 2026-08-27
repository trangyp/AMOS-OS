---
title: MD 2026 08 23 COSMO BRAIN CORE ARCHITECTURE
type: architecture
origin_architect: Trang Phan
provenance: direct file inspection of cosmo-brain/core/ on 2026-08-23
confidence: 0.95
epistemic_class: OBSERVATION
conclusion_class: VERIFIED
tags: [cosmo-brain, core, architecture, typescript, epistemics, reasoning, memory, orchestration, identity, constraints, validation, design-synthesis, amos-core, brain]
---



# Cosmo Brain Core Architecture

> **Source**: `/Users/mac/Downloads/stitch_project_cosmo/cosmo-brain/core/` — 39 files, ~6,365 lines of TypeScript + 14 AMOS_CORE Python spec files (v3.1→v4.4).
> **Architect**: Trang Phan. **System**: Cosmo (AMOS-derived deterministic intelligence for vocal resonance scanning).

## Directory Structure (8 modules + 14 spec files)

```
core/
├── type-guards.ts              — Runtime type narrowing + coercion helpers (100 lines)
├── constraints/index.ts        — Audio/session/feature invariant engine (180 lines)
├── validation/index.ts         — Pipeline input + audio buffer validation (157 lines)
├── identity/
│   ├── core.ts                 — System identity, IP rules, architect attribution (83 lines)
│   └── index.ts                — User identity kernel, consent state, privacy prefs
├── memory/
│   ├── session.ts              — Per-session data with retention + soft-delete (160 lines)
│   ├── timeline.ts             — Append-only chronological event store
│   ├── user-preferences.ts     — Goals, preferences, personalisation signals
│   └── index.ts                — Barrel export
├── reasoning/
│   ├── meta-logic.ts           — 12 logic modes + 4 core laws + operational modes (407 lines)
│   ├── safety-filter.ts        — Output safety: blocks medical/emotional/spiritual claims (205 lines)
│   └── index.ts                — Reasoning engine with provenance chains
├── epistemics/                 — AMOS epistemics layer (9 files, largest module)
│   ├── claims.ts               — 6 evidence classes, 6 conclusion classes, confidence ceiling (326 lines)
│   ├── rscf.ts                 — RSCF proof capsules, 10 causal levels, freshness, selective invalidation (340 lines)
│   ├── competing-hypotheses.ts — Competing hypothesis field with dominance reasons
│   ├── provenance.ts           — Provenance graph + Sybil hardening
│   ├── falsifiers.ts           — Sensitivity targets + 7 falsifier types
│   ├── adversarial-validation.ts — 9-step adversarial challenge pipeline
│   ├── regime-freshness.ts     — Applicability envelope + freshness tensor
│   ├── error-recovery.ts       — 7-step error recovery, selective revalidation
│   └── index.ts                — Barrel export (95 lines)
├── orchestration/
│   ├── index.ts                — 16-stage Resonance Scan pipeline types (371 lines)
│   ├── pipeline.ts             — Full pipeline runner (audio→features→artwork→recommendation)
│   ├── routing.ts              — Deterministic action→algorithm routing
│   └── consent.ts              — Consent gate (6 consent actions)
├── design-synthesis/
│   └── index.ts                — Requirement doc→design spec synthesiser with TF-IDF screen mapping (476+ lines)
└── AMOS_CORE v3.1—v4.4 .txt    — 14 Python spec files tracing kernel evolution
```

## Key Architectural Invariants

### 1. Epistemic Hierarchy (claims.ts)
- **Evidence classes** (strongest→weakest): `OBSERVATION(5) > DERIVED(4) > DECISION(3) > SOURCE_CLAIM(2) > MODEL(1) > UNKNOWN_GAP(0)`
- **Conclusion classes**: `VERIFIED(5) > DERIVED(4) > CONDITIONAL(3) > COMPETING(2) > MODEL(1) > UNKNOWN_GAP(0)`
- **Core invariant**: Claim strength must NOT exceed evidence strength. `confidenceCeiling = min(unresolved premise confidences)`.
- `VERIFIED` requires at least one `OBSERVATION` or `DERIVED` evidence.

### 2. RSCF Proof Capsules (rscf.ts)
- Bundles ALL epistemic metadata: claim, premises, evidence, provenance, scope, regime, freshness, dependencies, causal level, competing hypotheses, falsifiers, sensitivity.
- **10 causal levels**: `ASSOCIATION(1) → CORRELATION(2) → ENABLING_CONDITION(3) → MEDIATOR/CONFOUNDER(4) → FEEDBACK(5) → NECESSARY_CONDITION(6) → SUFFICIENT_CONDITION(7) → MECHANISM(8) → INTERVENTION_EFFECT(9)`
- **Selective invalidation**: when a premise fails, only descendant claims are invalidated (cascade via dependency graph). Unrelated work is preserved.
- **Reuse gate**: regime match + not stale + dependencies valid.

### 3. Meta-Logic Reasoning (meta-logic.ts)
- **12 logic modes** from CORE-19 kernel: `positive, negative, zero, dual, multi, meta` (primary) + `supra, anti, null` (extended) + `convergence, divergence, paradox` (patterns).
- Each mode has algebraic properties: idempotence, involution, monotonicity, collapses-to-false.
- **4 core laws**: Law of Law (contradiction check), Rule of 2 (duality/structural opposite), Rule of 4 (quadrant: biological/experiential/logical/systemic), Signal Fidelity (blocks simulated emotion + unsupported clinical claims).
- **3 operational modes**: `SAFE_INTROSPECTION_ONLY` (risk ≤0.3, no writes), `EXTERNAL_WRITE_LOW_RISK` (risk ≤0.6), `EXPERIMENTAL_BUILD` (risk ≤0.9).

### 4. Safety Filter (safety-filter.ts)
- Blocks 5 claim categories in user-facing output: `emotional_diagnosis`, `medical_claim`, `energy_spiritual_claim`, `consciousness_claim`, `trauma_claim`.
- Risk levels: `low → medium → high → critical`. Medical/trauma → critical (requires human review).
- `replaceDiagnosticLanguage()` converts emotional/medical terms to neutral acoustic terminology (e.g. "emotional state" → "vocal pattern", "anxiety" → "vocal variability").

### 5. Identity & IP (identity/core.ts)
- System: **Cosmo**, architect: **Trang Phan**.
- IP rules: no overwrite, no reattribution, no agent claim of authorship. IP class: "Private Structural IP".
- Non-operational modes: physical control, financial execution, medical treatment, legal representation, political campaigning.

### 6. Pipeline (orchestration/index.ts)
- **16-stage Resonance Scan pipeline**: `consent_check → input_validation → audio_quality → noise_suppression → feature_extraction → feature_normalisation → resonance_representation → safety_claim_filter → artwork_parameter_generation → artwork_generation → recommendation_ranking → user_explanation → timeline_event → feedback_capture → auditable_storage → provenance_tracking`.
- Actions: `resonance_scan, rescan, compare, gift, reflection`.
- V2 features include Meyda spectral features + YIN pitch detection.

### 7. Design Synthesis (design-synthesis/index.ts)
- Parses COSMO requirement docs → structured `DesignSpec` with provenance.
- v1.3: TF-IDF phrase-aware screen matching with BM25-style saturated TF. Stop words filtered. Coverage requirements strict for multi-token screens.
- Extracts: objectives, functional requirements, entities, key claims (verbatim with triggers), brain modules, governance flags.
- Conclusion class = `DERIVED` (synthesis output never exceeds `SOURCE_CLAIM` evidence from founder canon).

### 8. AMOS_CORE Evolution (v3.1 → v4.4)
14 Python spec files tracing the kernel's evolution:
- v3.1: Logic Fixed → v3.2.1: RSCF HML Recursive → v3.3: Governed Meta-Evolution → v3.4.1: Distributed Causal Evolution → v3.5: Epistemic Regime Lineage → v3.7/3.7.1: Provenance Topology (Hardened) → v3.8: Iterative Provenance → v3.9: Persistent Incremental → v4.0: MVCC Causal Concurrency → v4.1: Transactional Multi-RSCF → v4.2: Deterministic Causal Epoch → v4.3: Hardened Adaptive Epoch → v4.4: Coordination Avoidance.

## Cross-References
- [[00_COSMO_BRAIN_MOC]] — Master Map of Content
- AMOS Core Reasoning — AMOS reasoning contract skill
- AMOS RSCF Claims — Proof capsule skill
- AMOS Competing Hypotheses — Hypothesis preservation skill
- AMOS Provenance Trust — Source ancestry and independence
- AMOS Kafka Brain Buffer — Stream-log brain architecture (open file: AMOS_Kafka_Brain_Buffer_v1.0.ts)

## Notes
- The TypeScript modules are the **executable runtime** for the Cosmo app (vocal resonance scanning + generative artwork).
- The AMOS_CORE .txt files are the **Python specification lineage** — the reasoning kernel that the TypeScript modules implement.
- All modules credit **Trang Phan** as origin architect. IP rules enforce no agent authorship claims.
- The `design-synthesis` module is the bridge between founder canon documents and implementable design specs — it preserves epistemic provenance from source to derived spec.

---
**MOC:** [[BRAIN_MOC]]
