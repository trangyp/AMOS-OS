---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 03 Control Plane Readme
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

# 03 Control Plane — README

## Role

The Control Plane owns authority, routing, admission, policy, permission, commit gates, risk escalation, mode governance, tool governance, and lifecycle governance. It is the governance layer that determines what operations are permitted and under what conditions.

## Key Principle

```
WORKER CAPABILITY != CONTROL-PLANE AUTHORITY
```

A worker may know how to perform an operation without being authorized to commit it.

## Structure

```
03_CONTROL_PLANE/
├── 01_TASK_CONTRACT/     ← Task authorization contracts
├── 02_CAPABILITY/        ← Capability registry
├── 03_POLICY/            ← Policy definitions
├── 04_AUTHORITY/         ← Authority grants and revocations
├── 05_COMMIT/            ← Commit authority gating
├── 06_REASONING_MODES/   ← Reasoning mode definitions
├── 07_ROUTING_MODES/     ← Routing mode definitions
├── 08_EXECUTION_MODES/   ← Execution mode definitions
├── 09_COMMIT/            ← Commit governance
├── 10_EPISTEMIC_MODES/   ← Epistemic mode definitions
├── 11_SCALE_MODES/       ← Scale mode definitions
├── 12_WORLD_MODEL_MODES/ ← World model mode definitions
├── 13_RECOVERY_DEGRADED/ ← Recovery and degraded modes
├── 14_COMPOSITE_MODES/   ← Composite mode definitions
└── 15_CUSTOM_MODES/      ← Custom mode definitions
```

## Inter-Plane Connections

- **Canon:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] — Control plane enforces Canon
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] — Control plane orchestrates Kernel
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Control plane gates Runtime operations

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
