---
title: AMOS Total Framework Registry
type: registry
source: 00_ROOT
artifact: AMOS_TOTAL_FRAMEWORK_REGISTRY.md
artifact_id: 00_root_amos_total_framework_registry
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 00_ROOT
segment: 00_ROOT/AMOS_TOTAL_FRAMEWORK_REGISTRY.md
artifact_kind: REGISTRY
path: 00_ROOT/AMOS_TOTAL_FRAMEWORK_REGISTRY.md
tags:
  - amos-os
  - framework-registry
  - canon/root
  - rscf
  - hml
  - tss
  - tpe
  - ubi
  - fkn
  - frameworks
version: 1.0.0
updated: '2026-09-03'
status: POPULATED_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: AMOS_MODEL
canonical_status: AMOS_MODEL
implementation_status: SPECIFIED_DOCUMENTARY
validation_status: DERIVED_CONSISTENT
ingestion_action: EXPANDED_SYNTHESIS
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS
    - 11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC
    - 11_KNOWLEDGE/trang/TRANG_FRAMEWORK
  scope: repository_wide_framework_registry
---

# AMOS Total Framework Registry — Canonical Epistemic Frameworks

**Origin architect / steward:** Trang Phan
**Status:** `POPULATED_REGISTRY`
**Lineage target:** `AMOS Core v4.4`
**Epistemic classification:** `AMOS_MODEL`

---

## 1. Scope & Architectural Role

The **AMOS Total Framework Registry** indexes and coordinates all overarching conceptual, epistemic, and cognitive modeling frameworks across AMOS OS.

Frameworks provide **the conceptual grammar, reasoning invariants, and formal scaffolds** that bridge low-level Kernel computations (`02_KERNEL`) with high-level Agent orchestrations (`06_AGENTS` / `08_WORKFLOWS`).

```text
FRAMEWORK != KERNEL != IMPLEMENTED RUNTIME
CONCEPTUAL SCAFFOLD != DETERMINISTIC ALU != EMPIRICAL TRUTH
```

---

## 2. Master Framework Index (FW01–FW12)

| Code | Framework Title | Primary Focus | Governing Artifacts & Formal Scaffolds |
| :--- | :--- | :--- | :--- |
| **FW01** | **RSCF (Reality-Signal-Claim)** | Epistemic classification | Separates raw reality, observed signals, and verbalized claims. Enforces `SOURCE_CLAIM`, `OBSERVATION`, `DERIVED`, `AMOS_MODEL`, `UNKNOWN/GAP`. |
| **FW02** | **H/M/L Epistemic Hierarchy** | Scoped granularity | High-level (governing domain), Mid-level (subsystem contract), Low-level (concrete detail & raw evidence). Prevents context bloating. |
| **FW03** | **Trang Framework (TSS/TPE/∅)** | Recursive ontology | Trang Semantic Space (TSS), Trang Perspective Engine (TPE), and the Zero-Origin Void (∅) recursion dynamics. |
| **FW04** | **DRC (Distinction-Relation-Constraint)** | Relational algebra | Formalizes intelligence as distinction-making, relationship-binding, and constraint-satisfaction. |
| **FW05** | **UBI (Unified Biological Intelligence)** | Living systems cognition | Grounded autopoiesis, metabolic energy-budget constraint, bio-neurological coherence, organism survival imperative. |
| **FW06** | **FKN (Fractal Knowledge Network)** | Self-similar knowledge | Scale-invariant representation where local note structures mirror vault-level architectural topologies. |
| **FW07** | **Active Inference & Markov Blankets** | Predictive perception | Minimization of variational free energy across sensory, active, internal, and external states. |
| **FW08** | **Cognitive Organism OS** | Supervised full-brain loop | Coordinated cognitive organs: Perception, Memory, Reasoning, Metacognition, Executive Governance. |
| **FW09** | **Universal Coordinate System (UCS)** | Strategic field | 19×19 Go grid geometric embedding of cognitive states, strategic leverage points, and territory balance. |
| **FW10** | **Value Creation OS** | Economic intelligence | Epistemic wealth creation, non-zero-sum coordination, opportunity discovery, resource optimization. |
| **FW11** | **Constitutional Agent Governance** | Multi-agent safety | Non-delegable human stewardship, epoch-bounded capability grants, fail-closed permission gates. |
| **FW12** | **Metamorphic Verification** | Formal robustness | Property-based testing where outputs under transformed inputs must satisfy relational invariants. |

---

## 3. Framework Application Invariants

1. **Epistemic Discipline:** No framework may be used to elevate an unsubstantiated claim to empirical truth (`FRAMEWORK_APPLICATION != EMPIRICAL_VALIDATION`).
2. **Preservation of Provenance:** Any knowledge synthesized through a framework must retain its original source citations.
3. **Traceability:** Framework transitions must produce durable verification receipts registered under `20_OPERATIONS`.

---

RSCF-NODE
node_id: amos_00_root_amos_total_framework_registry
node_type: registry
path: 00_ROOT/AMOS_TOTAL_FRAMEWORK_REGISTRY.md
claim_class: AMOS_MODEL
rscf_state: active_specification
canonical_status: AMOS_MODEL
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- BINDS: [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
