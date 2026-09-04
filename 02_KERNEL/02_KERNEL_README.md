---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Kernel Readme
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# 02 Kernel — README

## Role

The Kernel layer owns constrained computational primitives — the fundamental operations that execute AMOS reasoning. The kernel provides deterministic, auditable, fail-closed computation.

## Scope

### In Scope

- Deterministic logic kernel (DLK) — axiom enforcement, proof trails
- Meta-logic — inference rule catalog, non-monotonic consequence management
- Causality — causal ordering, epoch management
- State — state transition primitives
- Memory — computational memory operations
- Risk-repair — failure detection and recovery primitives
- Authority — permission validation
- Provenance — source tracking primitives
- Integration — cross-layer composition

### Out of Scope

- Runtime execution state (04_RUNTIME) — Kernel defines primitives, Runtime executes them
- Agent definitions (06_AGENTS) — Agents use Kernel primitives
- Knowledge claims (11_KNOWLEDGE) — Kernel validates knowledge, doesn't contain it

## Structure

```
02_KERNEL/
├── 00_INDEX/                  ← Navigation indices
├── 01_META_LOGIC/             ← Inference rules and non-monotonic management
├── 02_COGNITION/              ← Cognitive computation primitives
├── 03_CAUSAL/                 ← Causal ordering and epoch management
├── 04_STATE/                  ← State transition primitives
├── 05_MEMORY/                 ← Computational memory operations
├── 06_RISK_REPAIR/            ← Failure detection and recovery
├── 07_AUTHORITY/              ← Permission validation
├── 08_PROVENANCE/             ← Source tracking primitives
├── 09_INTEGRATION/            ← Cross-layer composition
├── K_CAS.md                   ← Compare-And-Swap atomic primitive
├── K_MVCC.md                  ← Multiversion concurrency control
├── MVCC_CAS.md                ← MVCC/CAS transaction integration
├── K_FAILURE_RECOVERY.md      ← Failure recovery and rollback
├── DETERMINISTIC_LOGIC_KERNEL.md ← Logic kernel specification
└── [additional kernel files]
```

## Key Kernels

| Kernel | Function | Critical? |
|--------|----------|-----------|
| DETERMINISTIC_LOGIC_KERNEL | Axiom enforcement, proof trails | Yes |
| K_CAS | Atomic state transitions | Yes |
| K_MVCC | Snapshot-based concurrency | Yes |
| K_FAILURE_RECOVERY | Failure detection and recovery | Yes |
| K_AUTHORITY | Permission validation | Yes |
| K_CANON | Canon compliance verification | Yes |

## Inter-Plane Connections

- **Canon:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] — Kernel validates Canon compliance
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane orchestrates Kernel
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Runtime executes Kernel primitives

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
