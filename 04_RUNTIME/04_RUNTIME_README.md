---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 04 Runtime Readme
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

# 04 Runtime — README

## Role

The Runtime layer owns live system evolution — session, task, step, tick, epoch, active mode, current state, execution trace, commit state, failure state, and recovery state. It is where AMOS executes.

## Hard Rule

```
Design != Live Runtime
```

## Structure

```
04_RUNTIME/
├── 00_INDEX/                      ← Navigation indices
├── RUNTIME_RUNTIME_CONTRACT.md    ← Runtime plane contract
├── CAUSAL_CONCURRENCY_MVCC.md     ← Causal ordering and MVCC
└── [additional runtime files]
```

## Inter-Plane Connections

- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] — Runtime executes Kernel primitives
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane gates Runtime operations
- **State:** [[12_STATE/12_STATE_MOC|12_STATE_MOC]] — Runtime produces state updates

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
