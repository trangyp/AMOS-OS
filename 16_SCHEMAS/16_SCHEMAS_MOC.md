---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 16 Schemas Moc
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

# 16 Schemas — Map of Content

> [!ABSTRACT] Schemas Plane Executive Summary
> The **Schemas Plane** (`16_SCHEMAS`) governs all typed artifact schemas, tensor signatures, and structural compatibility rules in the AMOS Full Brain OS.
> It enforces the typing invariant:
> $$\text{ARTIFACT\_TYPE} \in \text{SCHEMAS}(16) \implies \text{TYPED\_CLASSIFICATION}$$
> $$\text{TENSOR\_AXES} \in \text{SCHEMAS}(16) \implies \text{COMPATIBILITY\_RULES}$$

---

## 1. Core Subsystem Schemas

* [[16_SCHEMAS/AGENT_SCHEMA|AGENT_SCHEMA]] — Canonical agent construction schema (v3.0.0) covering identity, capabilities, operations, memory, and authority bounds.
* [[16_SCHEMAS/MEMORY_SCHEMA|MEMORY_SCHEMA]] — Typed schema for memory records (`working`, `episodic`, `case`, `long-term`, `negative`, `authority-sensitive`), retention curves, and consolidation states.
* [[16_SCHEMAS/KNOWLEDGE_SCHEMA|KNOWLEDGE_SCHEMA]] — Canonical schema for admitted knowledge nodes, claims, premises, and falsifiers.
* [[16_SCHEMAS/PROTOCOL_SCHEMA|PROTOCOL_SCHEMA]] — Wire format schemas for inter-agent messaging, task leases, and handoffs.
* [[16_SCHEMAS/SECURITY_SCHEMA|SECURITY_SCHEMA]] — Cryptographic capability tokens, access control lists (DAC/MAC/RBAC), and authorization receipts.
* [[16_SCHEMAS/TAG_VOCABULARY|TAG_VOCABULARY]] — Master semantic tag taxonomy and validation hierarchy across the vault.

---

## 2. Typed Tensor Framework

* [[16_SCHEMAS/CLAIM_TENSOR|CLAIM_TENSOR]] — Classifies claim epistemic class, scope, regime, and confidence ceilings.
* [[16_SCHEMAS/EVIDENCE_TENSOR|EVIDENCE_TENSOR]] — Governs empirical evidence independence and correlation tracking.
* [[16_SCHEMAS/RELATION_TENSOR|RELATION_TENSOR]] — Defines typed relational axes across the knowledge graph.
* [[16_SCHEMAS/TENSORS|TENSORS]] · [[16_SCHEMAS/TENSOR_CONTRACTS|TENSOR_CONTRACTS]] · [[16_SCHEMAS/TENSOR_REGISTRY|TENSOR_REGISTRY]] — Formal tensor contracts governing cross-domain tensor compositions.

---

## 3. Subdirectory Schemas

* **Runtime Schemas (`01_RUNTIME`):** [[16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC|01_RUNTIME_MOC]].
* **Agent Construction (`06_AGENTS`):** [[16_SCHEMAS/06_AGENTS/agent.schema|agent.schema]].
* **RSCF Family (`10_RSCF`):** [[16_SCHEMAS/10_RSCF/10_RSCF_MOC|10_RSCF_MOC]] (`proof_capsule.schema`, `rscf_transaction.schema`, `provenance_topology.schema`).
* **Observability (`11_OBSERVABILITY`):** [[16_SCHEMAS/11_OBSERVABILITY/11_OBSERVABILITY_MOC|11_OBSERVABILITY_MOC]] (`canon_health.schema`, `provenance_health.schema`).

---

## 4. Invariants & Epistemic Boundaries

- `INV-SCHEMA-01`: **Schema $\neq$ Truth.** A valid schema conformance check does not prove empirical validity.
- `INV-SCHEMA-02`: **Tensor Axis Typing Preserved.** Cross-domain compositions must satisfy compatibility rules in [[16_SCHEMAS/TENSOR_CONTRACTS|TENSOR_CONTRACTS]].

---
[[00_ROOT/00_ROOT_MOC|Root MOC]] · [[AMOS_HOME|AMOS Home]]
