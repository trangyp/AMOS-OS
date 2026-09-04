---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 09 Protocols Moc
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

# 09 Protocols — Map of Content

> [!ABSTRACT] Protocols Plane Executive Summary
> The **Protocols Plane** (`09_PROTOCOLS`) owns cross-component interaction semantics, inter-agent handoff contracts, event bus protocols, and proof-based coordination avoidance in the AMOS Full Brain OS.
> It enforces the separation:
> $$\text{COMMUNICATION PROTOCOL} \neq \text{WORKFLOW ORCHESTRATION} \quad\land\quad \text{MESSAGE} \neq \text{AUTHORIZED MUTATION}$$

---

## 1. Core Subsystem Protocols & Contracts

* [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|Coordination Avoidance Protocol]] — Mathematical rules enabling shard-local finalization without distributed locks when proofs establish commutativity ($\text{HasProof}(op) \land \text{NoConflict}(op)$).
* [[09_PROTOCOLS/TASK_HANDOFF_PROTOCOL|Task Handoff Protocol]] — Formal specification for passing task leases, epistemic context budgets, and rollback tokens between Supervisor, Planner, and Worker agents.
* [[09_PROTOCOLS/PROTOCOLS_PROTOCOL_CONTRACT|PROTOCOLS_PROTOCOL_CONTRACT]] — Wire format schemas, serialization invariants, and non-repudiation cryptographic contracts.
* [[09_PROTOCOLS/PROTOCOLS_README|PROTOCOLS_README]] — Structural overview of the Protocols plane.

---

## 2. Inbound & Outbound Interfaces

* **Agent Communication:** Binds agent messaging in [[06_AGENTS/06_AGENTS_MOC|06_AGENTS]].
* **Runtime Handshake:** Binds execution state transitions in [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]].
* **Authority Verification:** Governed by [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]].

---
[[00_ROOT/00_ROOT_MOC|Root MOC]] · [[AMOS_HOME|AMOS Home]]
