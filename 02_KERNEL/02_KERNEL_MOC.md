---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Kernel Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
updated: 2026-09-14
---
---
---

# 02 Kernel — Map of Content

**Path:** `02_KERNEL`  
**Role:** Deterministic primitives, axiomatic logic, concurrency ALU, and invariant verification kernels under AMOS Core v4.4.

## Active interpretation guards — 2026-09-14

Historical/source kernel files remain preserved. Governed runtime use must apply the relevant repair overlay where newer bounded evidence identifies stale or over-broad semantics.

### URK / Core-19

- [[02_KERNEL/01_META_LOGIC/URK_CORE19_REPAIR_OVERLAY_2026-09-14|URK / Core-19 Repair Overlay — 2026-09-14]]
- [[01_CANON/07_PROVENANCE/URK_CORE19_REPAIR_CANDIDATE_2026-09-14|URK / Core-19 Repair Candidate Provenance — 2026-09-14]]
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/classical_sat_firewall.py`

This guard prevents stale assumptions such as fixed cross-lineage P02, universal linear time, `1E∞` as standard tensor dimension, total 19×19 semantics, universal contradiction semantics, or bottom-up-only double-`NLOGIC` rewriting from being treated as current verified mathematics merely because an older source file contains them.

### Canon admission

- [[02_KERNEL/01_META_LOGIC/K_CANON_ADMISSION_REPAIR_OVERLAY_2026-09-14|K_CANON Admission Repair Overlay — 2026-09-14]]
- [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|CANON_POLICY]]
- `03_CONTROL_PLANE/03_POLICY/canon_admission_gate.py`

This guard rejects confidence-threshold auto-promotion. Candidate eligibility, provenance, contradiction handling, authority, and commit-time freshness are separate gates.

### Governed evolution

- [[02_KERNEL/01_META_LOGIC/K_GOVERNED_EVOLUTION_REPAIR_OVERLAY_2026-09-14|K_GOVERNED_EVOLUTION Repair Overlay — 2026-09-14]]
- `03_CONTROL_PLANE/09_COMMIT/governed_mutation_gate.py`

This guard enforces mutation permission profiles, legal lifecycle progression, non-compensatory hard gates, bounded propagation, rollback requirements, exact change binding, and fresh authority at commit. Constitutional/governance-boundary self-rewrite is escalated rather than autonomously approved.

## Files & Computational Kernels

- [[02_KERNEL/KERNEL_README|KERNEL_README]]
- [[02_KERNEL/KERNEL_KERNEL_CONTRACT|KERNEL_KERNEL_CONTRACT]]
- [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19|ABSOLUTE_LOGIC_KERNEL_19x19]] — preserved historical/source 19×19 kernel; apply the active URK/Core-19 repair overlay before governed runtime use
- [[02_KERNEL/AMOS_LEGAL_ENGINE_KERNEL|AMOS_LEGAL_ENGINE_KERNEL]] — Formal Contract, Deontic Logic & Compliance Substrate
- [[02_KERNEL/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]] — Atomic Multi-RSCF Proof Coordination
- [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — Deterministic Logic ALU
- [[02_KERNEL/K_ANTI_AUTOPOISONING|K_ANTI_AUTOPOISONING]] — Anti-Autopoisoning Base ALU
- [[02_KERNEL/K_ATOMIC_MULTI_RSCF|K_ATOMIC_MULTI_RSCF]] — Atomic Multi-Proof Transaction ALU
- [[02_KERNEL/K_AUTHORITY|K_AUTHORITY]] — Authority & Permission Validation Kernel
- [[02_KERNEL/K_CANON|K_CANON]] — preserved source kernel; active promotion semantics constrained by the K_CANON admission repair overlay
- [[02_KERNEL/K_CAS|K_CAS]] — Lock-Free Compare-And-Swap Epoch ALU
- [[02_KERNEL/K_CONTROL_PLANE|K_CONTROL_PLANE]] — Control Plane Orchestration ALU
- [[02_KERNEL/K_CORE_LAWS|K_CORE_LAWS]] — Core Law Validation Engine
- [[02_KERNEL/K_DOMAINS|K_DOMAINS]] — Multi-Domain Mapping Kernel
- [[02_KERNEL/K_FAILURE_RECOVERY|K_FAILURE_RECOVERY]] — Failure Recovery & Rollback ALU
- [[02_KERNEL/K_FAIL_CLOSED|K_FAIL_CLOSED]] — Fail-Closed Safety Gate
- [[02_KERNEL/K_GOVERNANCE|K_GOVERNANCE]] — Governance & Policy Enforcement Kernel
- [[02_KERNEL/K_GOVERNED_EVOLUTION|K_GOVERNED_EVOLUTION]] — preserved source kernel; active mutation semantics constrained by the governed-evolution repair overlay
- [[02_KERNEL/K_MVCC|K_MVCC]] — Multiversion Concurrency Snapshot Buffer
- [[02_KERNEL/K_REALITY|K_REALITY]] — Reality Grounding Substrate ALU
- [[02_KERNEL/K_UNIVERSE_STRATA|K_UNIVERSE_STRATA]] — Universe Strata Hierarchy Engine
- [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — MVCC/CAS Transaction Integration
- [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] — Neural-Symbolic Reasoning Bridge
- [[02_KERNEL/SOFT_REALTIME_SCHEDULER|SOFT_REALTIME_SCHEDULER]] — Soft Real-Time Task Execution Scheduler
- [[02_KERNEL/ULK_LOGIC_KERNEL|ULK_LOGIC_KERNEL]] — Universal Logic Kernel ALU

## Subdirectories

- [[02_KERNEL/01_META_LOGIC/01_META_LOGIC_MOC|01_META_LOGIC_MOC]] — 01_META_LOGIC
- [[02_KERNEL/02_COGNITION/02_COGNITION_MOC|02_COGNITION_MOC]] — 02_COGNITION
- [[02_KERNEL/03_CAUSAL/03_CAUSAL_MOC|03_CAUSAL_MOC]] — 03_CAUSAL
- [[02_KERNEL/04_STATE/04_STATE_MOC|04_STATE_MOC]] — 04_STATE
- [[02_KERNEL/05_MEMORY/05_MEMORY_MOC|05_MEMORY_MOC]] — 05_MEMORY
- [[02_KERNEL/06_RISK_REPAIR/06_RISK_REPAIR_MOC|06_RISK_REPAIR_MOC]] — 06_RISK_REPAIR
- [[02_KERNEL/07_AUTHORITY/07_AUTHORITY_MOC|07_AUTHORITY_MOC]] — 07_AUTHORITY
- [[02_KERNEL/08_PROVENANCE/08_PROVENANCE_MOC|08_PROVENANCE_MOC]] — 08_PROVENANCE
- [[02_KERNEL/09_INTEGRATION/09_INTEGRATION_MOC|09_INTEGRATION_MOC]] — 09_INTEGRATION

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

**Related:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] · [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] · [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS_MOC]] · [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]
