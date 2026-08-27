---
origin_architect: Trang Phan
provenance: direct file inspection of cosmo-brain/ on 2026-08-23 (README, package.json, manifest.json, 4 subagent explorations, direct reads of key files)
confidence: 0.95
epistemic_class: OBSERVATION
conclusion_class: VERIFIED
tags: [cosmo-brain, architecture, typescript, python, amos, algorithms, governance, domains, knowledge, schemas, registry, prompts, trang-agent, amos-os-kernel, amos-md-brain, amos-v1-production, brain]
---

# Cosmo Brain — Full Architecture

> **Source**: `/Users/mac/Downloads/stitch_project_cosmo/cosmo-brain/` — 1,771 files across 22 top-level directories + 104 root files.
> **Package**: `@cosmo/brain` v1.0.0 (private, ESM, Node ≥20).
> **Architect**: Trang Phan. **Status**: Production-ready, modular, typed, tested, governed.
> **Companion note**: md__2026-08-23 Cosmo Brain Core Architecture (deep dive on `core/`).

## Overview

Cosmo Brain is a bounded, testable, auditable intelligence system for the **Cosmo Wellness platform** — a vocal resonance scanning app that generates artwork and recommendations from audio features. It replaces ~1000 unorganised AMOS files with a clean modular architecture.

**Key principles:**
- Every output includes uncertainty fields and measured language — no diagnostic/medical claims
- Transparent recommendation ranking with explainable factors
- Full reproducibility records for generated artwork
- 8-class memory system with individual retention/deletion rules
- Privacy-first: highly-sensitive data requires explicit consent
- Zero `as any`, zero `@ts-ignore`, zero `eslint-disable` in TypeScript

---

## Directory Structure (22 directories)

### Production TypeScript Architecture

| Directory | Files | Purpose |
|-----------|-------|---------|
| **core/** | 40 | Orchestration, memory, identity, reasoning, constraints, validation, design-synthesis, epistemics (see md__2026-08-23 Cosmo Brain Core Architecture) |
| **algorithms/** | 25 | 6 algorithm domains: audio, resonance, artwork, recommendations, timeline, perspective |
| **governance/** | 11 | 10 governance modules: claims, safety, privacy, consent, consent-tokens, provenance, ethics, audit, uncertainty, scientific-claims, data-quality |
| **domains/** | 10 | 9 domain mapping modules + barrel export |
| **knowledge/** | 5 | Approved knowledge (67+ entries), hypotheses, references, research studies |
| **schemas/** | 13 | Type re-exports by domain (artwork, audio, brain, recommendation, resonance, timeline, user-context) |
| **registry/** | 5 | Algorithm registry (13 algorithms), brain registry (9 modules), source-map, version-map |
| **prompts/** | 9 | System, recommendation, reflection, perspective, safety prompts |
| **types/** | 1 | Ambient type stub for @audio/pitch-yin |
| **workflows/** | 1 | AMOS quantum library workflow (10-step lifecycle) |
| **tests/** | 81 | 66 unit tests (1,035 tests) + 4 integration tests (51 tests) |
| **scripts/** | 2 | generate-design-specs.ts, verify-core-flow.ts |

### AMOS Python Lineage

| Directory | Files | Purpose |
|-----------|-------|---------|
| **AMOS_OS_KERNEL/** | 153 | Production OS kernel v3 — model-agnostic, 27 governance gates, 257 closed gaps (91-347), SQLite persistence |
| **AMOS_MD_BRAIN_FULL_INFRA/** | 314 | Markdown brain v1.0 — 60 brain modules across 11 layers, 92 manifest entries |
| **amos_v1_production/** | 20 | v1 production invariants — state substrate, RSCF graph, deterministic kernel, control plane, AIBOM autonomy |
| **trang_agent/** | 5 | Trang Agent framework — fractal decomposition, entropy/lacunarity, population evolution, ASEA state |

### Root-Level Files (104)

- **57 AMOS_*.py files**: Kernel runtime, MURK reasoning engine, cognitive substrate, Go board 19×19, semantic matrix, Kafka brain buffer, V5-V22 integration files
- **Key Python**: `executable_brain_model.py`, `AMOS_KernelRuntime.py`, `AMOS_MURK_REASONING_ENGINE.py`, `AMOS_COGNITIVE_SUBSTRATE.py`
- **Config**: `package.json`, `tsconfig.json`, `tsconfig.build.json`, `turbo.json`, `vitest.config.ts`, `.eslintrc.json`, `manifest.json`
- **Docs**: `README.md`, `AEL_ARCHITECTURE.md`, `AMOS_ABSOLUTE_LOGIC_MURK_CANON.md`, `AMOS_DETERMINISM_BOUNDARIES.md`, `PERFORMANCE_BENCHMARKS.md`, `TESTING_STRATEGY.md`
- **State**: `kernel_state.jsonl`, `murk_state.json`, `brain_model_schema.json`

---

## Pipeline (16-stage Resonance Scan)

```
Audio Input
  → consent_check
  → input_validation
  → audio_quality_assessment
  → noise_suppression
  → feature_extraction (FFT v1 + Meyda v2 + YIN pitch)
  → feature_normalisation (session-only / population / hybrid)
  → resonance_representation (8 dimensions)
  → safety_claim_filter
  → artwork_parameter_generation
  → artwork_generation (seeded deterministic SVG)
  → recommendation_ranking (9-factor transparent scoring)
  → user_explanation
  → timeline_event
  → feedback_capture
  → auditable_storage
  → provenance_tracking
```

Actions: `resonance_scan, rescan, compare, gift, reflection`

---

## Algorithms (6 domains, 13 registered)

### audio/ (7 modules)
- **preprocessing** — validate, trim silence, normalise sample rate, RMS/peak
- **feature-extraction** (v1.0.0) — FFT-based: pitch, energy, tempo, spectral centroid, harmonicity, ZCR, continuity, noise
- **feature-extraction-v2** (v2.0.0) — Meyda-powered: spectral rolloff/flatness/flux, chroma, MFCC, perceptual features
- **pitch-yin** (v1.0.0) — YIN algorithm with per-frame analysis and aggregation
- **noise-suppression** (v1.0.0) — RNNoise AudioWorklet (browser) + spectral subtraction fallback (offline)
- **quality-assessment** — excellent/good/fair/poor scoring with issues and confidence
- **normalisation** (v1.0.0) — session-only, population, hybrid methods to [0,1]

### resonance/ (4 modules)
- **session-analysis** (v1.0.0) — 8-dimensional resonance profile with confidence
- **comparison** (v1.0.0) — comparability checks, feature change detection, uncertainty
- **pattern-mapping** (v1.0.0) — 9-domain pattern mapping with confidence and evidence
- **baseline** (v1.0.0) — statistical baselines from multiple sessions, outlier detection

### artwork/ (4 modules)
- **parameter-mapping** (v1.0.0) — resonance → visual parameters (hue, saturation, complexity)
- **generation** (v1.0.0) — seeded deterministic SVG generation
- **reproducibility** (v1.0.0) — capture all inputs, verify regenerated outputs match
- **versioning** — version compatibility across pipeline components

### recommendations/ (4 modules)
- **practice-selection** (v1.0.0) — 8-factor transparent ranking
- **safety-filtering** — safety rules, contraindications, disclaimers
- **personalisation** (v1.0.0) — user state adjustments (new/established, stressed, time of day)
- **feedback-learning** (v1.0.0) — feedback profiles, score adjustment from completion rates

### timeline/ (3 modules)
- **event-processing** (v1.0.0) — events, milestones (first scan, 10/50), streaks
- **progress-comparison** — cross-session progress with timeline context
- **summaries** (v1.0.0) — readable summaries with session counts, streaks, highlights

### perspective/ (3 modules)
- **polarity-mapping** — 8 polarity pairs across 9 domains with tension assessment
- **reframing** — reflective reframes from polarity assessments
- **safety** — prohibited/caution terms, diagnostic language filter

---

## Domains (9 mapping modules)

Each maps resonance dimensions to domain-specific patterns with weighted scoring:

| Domain | Version | Patterns |
|--------|---------|----------|
| **cognition** | 1.0.0 | analytical, creative, focused, wandering, integrated |
| **emotion** | 1.0.0 | expressive, contained, dynamic, settled, layered |
| **somatic** | 1.0.0 | grounded, activated, flowing, contracted, expanded |
| **behaviour** | 1.0.0 | routine, exploratory, structured, adaptive, restful |
| **culture** | 1.0.0 | communal, individual, ritualistic, expressive, contemplative |
| **nature** | 1.0.0 | resonant, organic, simple, flowing, rooted |
| **sound** | 1.0.0 | bright, balanced, warm, rich, clear |
| **creativity** | 1.0.0 | exploratory, structured, focused, generative, contemplative |
| **relationships** | 1.0.0 | connected, attuned, introspective, expressive, distant |

All domains include explicit uncertainty disclaimers. Culture and relationships explicitly disclaim cultural identity / interpersonal assessment claims.

---

## Governance (11 modules)

| Module | Version | Purpose |
|--------|---------|---------|
| **claims** | — | Claim boundaries, prohibited phrases, diagnostic language blocking |
| **safety** | — | 4 safety levels (safe/caution/restricted/blocked), crisis resources |
| **privacy** | — | 4 classification levels (public/internal/sensitive/highly-sensitive), retention rules |
| **consent** | — | Versioned consent, per-purpose verification (policy-level) |
| **consent-tokens** | 1.0.0 | 11 modular per-data-category tokens (audio, artwork, biosignal, practitioner, analytics) |
| **provenance** | 1.0.0 | W3C-PROV chain, immutable records, comparability checks |
| **ethics** | — | 5 principles: non-harm, honest representation, autonomy, data minimisation, creator attribution |
| **audit** | — | Action logging with integrity hashing, exportable records |
| **uncertainty** | — | Propagation from features → domains → recommendations, severity levels |
| **scientific-claims** | — | 6 evidence levels (measured → unsupported), disclaimers per level |
| **data-quality** | — | 11 subsystems: retention, quality gates, unit registry, coordinate systems, schema evolution, missing data, sensor reliability, measurement uncertainty, construct validity, Goodhart monitoring, metric versioning |

---

## Knowledge Base

- **approved/** — 67+ fact-checked entries across 8 categories: acoustic-science, wellness-practice, safety, privacy, reasoning-engine (MURK), go-board, semantic-matrix, quantum-physics
- **hypotheses/** — 3 documented hypotheses (vocal-emotion correlation, body awareness, artwork as reflective tool) with status tracking
- **references/** — 3 source references (voice science, mindfulness research, signal processing)
- **research/** — 1 planned study (resonance pattern normative ranges) with consent requirements

---

## AMOS OS Kernel (v3)

`AMOS_OS_KERNEL/` — 153 files. Production-ready, model-agnostic OS for governed reasoning.

**Key principle**: The language model is one replaceable cognitive worker; the kernel owns state, proof, memory, provenance, causal structure, transactions, authority, execution, replay, budgets, skill/tool admission, and finalization.

**Structure**:
- `amos/kernel.py` — AmosKernel.run() main execution loop
- `amos/cli.py` — CLI entry (init, run, inspect, serve)
- `amos/core/types.py` — All dataclasses, enums, types
- `amos/state/` — SQLite-backed persistence (store, epochs, transactions)
- `amos/abi/` — Agent-Brain Interface (model, skill, tool)
- `amos/graph/` — Graph structures (causal, dependency, provenance)
- `amos/memory/` — Memory management (context, immune, manager, orientation)
- `amos/proof/` — Proof checking (checker, hypotheses, rscf)
- `amos/replay/` — Event replay (events, ledger)
- `amos/runtime/` — Runtime pipeline (audit, finalize, planner, router, scheduler, selector)
- `amos/server/` — HTTP server
- `amos/governance/` — **27 governance modules covering gaps 91-347**
- `registries/` — EQUATION_REGISTRY, INVARIANTS, RUNTIME_LINEAGE, TENSOR_REGISTRY, VARIABLE_REGISTRY
- `skills/` — 10 skill directories with SKILL.md and skill.json

**Closed gaps**: 257 (gaps 91-347). Features: SQLite persistence, event-sourced state, MVCC/CAS objects.

---

## AMOS Markdown Brain (v1.0)

`AMOS_MD_BRAIN_FULL_INFRA/` — 314 files. Human-readable brain spec.

**60 brain modules** across 11 layers:
- `00_boot/` (2) — bootstrap + router
- `10_core/` (5) — invariants, claims, ontology, consensus, evidence lineage
- `20_state/` (1) — state machine
- `30_epistemics/` (9) — provenance, evidence, competing hypotheses, Sybil hardening, falsifiers, adversarial validation, regime freshness, error recovery, RSCF
- `40_runtime/` (18) — v3.0-v4.4 runtime versions + lineage + transaction protocol
- `50_governance/` (5) — GMEF, authority, repair/rollback, evolution memory/debt
- `60_execution/` (8) — execution harness, knowledge harvest, RSCF schema, provenance, benchmarks
- `70_domain/` — stub (empty, no source content)
- `90_output/` (7) — expression translation, routing, formatting, final gate
- `95_meta/` (2) — self-review, bootstrap
- `99_archive/` (2) — changelog, README

**Entry sequence**: BRAIN.md → BOOTSTRAP.md → ROUTER.md → INVARIANTS.md → load only needed modules → FINAL_GATE.md before consequential output.

**Runtime versions**:
- v3.x (3.0→3.9): Deterministic reasoning, RSCF, governed meta-evolution, distributed causal, epistemic regime, competing hypotheses, provenance topology (hardened), iterative/persistent provenance
- v4.x (4.0→4.4): MVCC concurrency, transactional multi-RSCF, deterministic causal epoch, hardened adaptive epoch, coordination avoidance

**GMEF cycle**: Observe → Propose → Classify → Sandbox → Experiment → Evaluate → Challenge → Govern → Select → Deploy → Remember

**Mutation classes**: M0 (immutable) → M1 (human-governed) → M2 (explicit approval) → M3 (controlled evolution) → M4 (bounded autonomous) → M5 (low-risk autonomous)

---

## AMOS v1 Production

`amos_v1_production/` — 20 files. Production invariants bridging to OS Kernel v3.

**Key files**: `integration_kernel.py` (adapter), `state_substrate.py`, `rscf_graph.py`, `deterministic_kernel.py`, `control_plane.py`, `canonical_registry.py`, `aibom_autonomy.py`, `memory_os.py`, `engine_agent.py`, `metacognition_planning_tool.py`, `observability.py`, `security.py`, `deployment.py`

**ProductionKernelAdapter**: bridges AMOS OS Kernel v3 with v1 production invariants (StateSubstrate, RSCFGraph, DeterministicKernel, ControlPlane, AIBOMGovernor).

---

## Trang Agent

`trang_agent/` — 5 files. Fractal decomposition + population evolution framework.

- `trang_agent_core.py` — 17 equation groups, fractal tier decomposition (L/M/H), Shannon entropy, lacunarity, health scoring
- `trang_agent_reasoning.py` — survival validation, Tát 2 cross-validation, hallucination detection, ASEA state evolution
- `trang_agent_population.py` — mutation + natural-selection evolution (NO gradient descent, selection only)
- `trang_agent_main.py` — demo/CLI with 100 agents over 20 generations
- `trang_agent_sample_config.json` — framework constants (LAMBDA_OPTIMAL=0.2, weights W_L/W_M/W_H)

---

## Registry

- **algorithm-registry.ts** — 13 algorithms with typed I/O, safety metadata, scientific status (measured/validated/experimental/symbolic/product-metaphor), privacy levels, consent requirements, execution logging
- **brain-registry.json** — 9 orchestrator modules with constraints, claim boundaries, pipeline stages, AMOS source migration paths
- **source-map.json** — Maps every module to original AMOS source file with Trang Phan attribution
- **version-map.json** — Version history (all at 1.0.0, initial scaffold 2026-07-27)

---

## Test Suite

- **66 unit test files — 1,035 tests** (run with `npm test` / `vitest run`)
- **4 integration test files — 51 tests** (run with `npm run test:integration`)
- **Coverage**: all algorithms, governance, memory, orchestration, domains, schemas, prompts, reasoning, type-guards
- **Coverage thresholds**: enforced via `vitest.config.ts`

---

## Build & Tooling

- **TypeScript**: strict config, zero `as any`/`@ts-ignore`/`eslint-disable`
- **Build**: `tsc --project tsconfig.build.json` → `dist/`
- **Test**: `vitest run` (unit), `vitest run tests/integration/` (integration)
- **Lint**: `eslint . --ext .ts`
- **Turborepo**: `turbo.json` for task orchestration
- **Dependencies**: `@audio/pitch-yin`, `@sapphi-red/web-noise-suppressor`, `meyda`
- **Dev deps**: `@cosmo/domain`, `@supabase/supabase-js`, TypeScript 5.9.3, Vite 7.3.6, Vitest 4.1.11

---

## Type Safety Invariants

- Zero `as any` in all `.ts` files
- Zero `@ts-ignore`/`@ts-expect-error`/`@ts-nocheck`
- Zero `eslint-disable` directives
- Shared `core/type-guards.ts` provides `isRecord`, `isNumberArray`, `asString`, `asNumber`, `asUnion<T>`, `typedEntries<K,V>()`, `pickTopEntry<K>()`
- Validation sets provide runtime-validated string-to-union conversion
- Only 2 `as unknown as` casts remain (both necessary): memory generics, Meyda FFT interop

---

## Cross-References

- [[00_Cosmo_Brain_MOC]] — Master Map of Content
- md__2026-08-23 Cosmo Brain Core Architecture — Deep dive on core/ module
- AMOS Core Version Lineage — v3.1→v4.4 evolution
- AMOS Brain Engine Specs — Brain module specifications
- AMOS CIL Canon Integration Layer
- AMOS HIE Human Interaction Engine
- AMOS Drive Ingest Summary
- Invariants 701–800, Invariants 801–900, Invariants 901–1000
- C201–C300, C301–C400, C401–C500
- 19x19 Sparse Coupling Matrix
- Executive System Model G-N-D-C-B
- MICRO↔MACRO 100000 Years Civilization
- Meta-Laws Stability Equations Multi-Scale

## Notes

- The TypeScript modules are the **executable production runtime** for the Cosmo app.
- The AMOS_OS_KERNEL is the **Python OS kernel** (v3) — model-agnostic governance OS.
- The AMOS_MD_BRAIN_FULL_INFRA is the **markdown brain spec** — human-readable reasoning/governance rules.
- The amos_v1_production is the **v1 production adapter** — bridges v1 invariants to OS Kernel v3.
- The trang_agent is the **fractal evolution framework** — mathematical decomposition and population dynamics.
- The 57 root AMOS_*.py files are the **historical Python lineage** — V5-V22 integration files, MURK engine, cognitive substrate, Go board, semantic matrix, Kafka brain buffer.
- All modules credit **Trang Phan** as origin architect. IP rules enforce no agent authorship claims.
- The `design-synthesis` module bridges founder canon documents → implementable design specs with epistemic provenance.
- Benchmark boundaries are preserved: v3.1 logic (PASSED), v4.0 MVCC (PASSED single-target, FAILED multi-RSCF), v4.4 coordination avoidance (PROMOTED, no numeric benchmark after promotion).
