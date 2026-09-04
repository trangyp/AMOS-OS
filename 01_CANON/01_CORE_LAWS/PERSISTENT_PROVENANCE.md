---
title: PERSISTENT_PROVENANCE — Cryptographic Lineage Preservation Law
type: law
source: 01_CANON/01_CORE_LAWS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
updated: 2026-09-04
tags:
  - canon
  - core_law
  - provenance
  - lineage
  - immutability
  - law-hierarchy
  - provenance-x-confidence
  - heritage-provenance
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: CANON_LAW
  claim_class: CANONICAL_INVARIANT
  provenance: AMOS_CANON
---

# PERSISTENT_PROVENANCE — Cryptographic Lineage Preservation Law

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `CANONICAL_INVARIANT`
> **Status:** `ACTIVE_CANON_LAW`

PERSISTENT_PROVENANCE mandates that all derived claims, state transitions, and evolutionary mutations maintain an immutable, tamper-evident lineage back to independent root observations.

______________________________________________________________________

## 1. Architectural Scope

`PERSISTENT_PROVENANCE` governs the provenance subsystem of the AMOS Full OS MECE architecture. It applies to every knowledge capsule, state transition, and evolutionary mutation within the vault. The law ensures that no claim enters the corpus without a verifiable lineage chain, and that no lineage record may be deleted or modified in-place.

This law binds to [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]] and [[01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE|HERITAGE_PROVENANCE]].

______________________________________________________________________

## 2. Formal Definition

A **provenance lineage** for a knowledge capsule $K_t$ at time $t$ is a sequence:

$$\text{Lineage}(K_t) = \langle R_0, T_1, T_2, \dots, T_t \rangle$$

where $R_0$ is a root observation, each $T_i$ is a transformation step, and each step is cryptographically linked to its predecessor via a hash chain:

$$\text{Hash}(T_i) = \text{BLAKE3}(\text{Content}(T_i) \parallel \text{Hash}(T_{i-1}))$$

The lineage is **strictly verifiable** if:

1. Every $T_i$ resolves to an existing capsule in the corpus.
2. Every hash link is intact (no tampering detected).
3. The graph formed by lineage edges is acyclic (a DAG).
4. $R_0$ is an independent root observation (not itself derived).

______________________________________________________________________

## 3. Governing Invariants

$$\forall K_t, \; \text{Lineage}(K_t) = \langle R_0, T_1, T_2, \dots, T_t \rangle \; \text{is strictly verifiable}.$$

- **PP-1 Lineage Presence:** Every capsule $K_t$ with `claim_class` $\in \{$DERIVED, MODEL, DECISION$\}$ must have a declared lineage chain. Capsules with `claim_class` $=$ OBSERVATION are root nodes and are their own lineage.
- **PP-2 Immutability:** Provenance records are append-only. No record may be deleted or modified in-place. Corrections are additive (new records that supersede, with explicit supersession links).
- **PP-3 Tamper-Evidence:** Any modification to a capsule's content invalidates its hash and is detectable by all downstream consumers via hash chain verification.
- **PP-4 Acyclicity:** The provenance graph is a directed acyclic graph (DAG). No circular lineage is permitted.
- **PP-5 Root Independence:** Root observations $R_0$ must be independent — they may not reference themselves or form self-derived loops.

______________________________________________________________________

## 4. Mathematical Formulation

### 4.1 Hash Chain

$$\text{Hash}(T_i) = \text{BLAKE3}(\text{Content}(T_i) \parallel \text{Hash}(T_{i-1}))$$

### 4.2 Lineage Verifiability

$$\text{Verifiable}(K_t) \iff \forall i \in [1, t], \; \text{Hash}(T_i) = \text{BLAKE3}(\text{Content}(T_i) \parallel \text{Hash}(T_{i-1}))$$

### 4.3 Acyclicity

$$\nexists \; \text{path from } T_i \text{ to } T_i \text{ in } G = (V, E)$$

where $G$ is the provenance graph with vertices $V$ (capsules) and edges $E$ (derivation links).

### 4.4 Confidence Ceiling

$$\text{Confidence}(K_t) \le \min_{i} \text{Confidence}(T_i) \quad \text{(weakest-link bound)}$$

The confidence of a derived claim is capped by the lowest confidence in its lineage chain.

______________________________________________________________________

## 5. MECE Mapping to AMOS Full Brain OS

| Provenance Dimension | Affected AMOS Stage | Canonical Gate |
|---------------------|---------------------|----------------|
| Lineage presence | Admit / Plan | `L17_RSCF` |
| Immutability | Commit / Audit | `L0_INTEGRITY` |
| Tamper-evidence | Observe / Repair | `L6_UNCERTAINTY` |
| Acyclicity | Route / Plan | `L17_RSCF` |
| Root independence | Perceive / Admit | `L0_INTEGRITY` |
| Confidence ceiling | Evaluate / Decide | `L6_UNCERTAINTY` |

______________________________________________________________________

## 6. Safety Invariants

- `INV-PP-001` (**No orphan claims:**) A capsule with `claim_class` $\in \{$DERIVED, MODEL, DECISION$\}$ and no declared lineage is rejected as `PROVENANCE_GAP`.
- `INV-PP-002` (**No silent supersession:**) Supersession of a provenance record requires an explicit supersession link and an authority witness; silent overwrite is prohibited.
- `INV-PP-003` (**No provenance deletion:**) Provenance records are never deleted, even when superseded or reversed. Reversed operations retain a `REVERSED` marker.
- `INV-PP-004` (**Hash chain enforcement:**) Every downstream consumer must verify the hash chain before accepting a derived claim; failure triggers fail-closed.
- `INV-PP-005` (**Weakest-link confidence:**) The confidence of a derived claim cannot exceed the minimum confidence of any node in its lineage chain.

______________________________________________________________________

## 7. Navigation & Bindings

- **Master MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- **Partition Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- **Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Core Laws MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
- **Provenance × Confidence:** [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]]
- **Heritage Provenance:** [[01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE|HERITAGE_PROVENANCE]]
- **Validation Receipt:** [[01_CANON/01_CORE_LAWS/PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT|PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT]]
- **Related Laws:** [[01_CANON/01_CORE_LAWS/L0_INTEGRITY|L0_INTEGRITY]] · [[01_CANON/01_CORE_LAWS/L17_RSCF|L17_RSCF]] · [[01_CANON/01_CORE_LAWS/L6_UNCERTAINTY|L6_UNCERTAINTY]]

______________________________________________________________________

## 8. Known Gaps & Falsifiers

- `GAP-PP-001`: The hash chain assumes BLAKE3 collision resistance; while practically strong, formal collision resistance is not proven, only conjectured.
- `GAP-PP-002`: Root observation independence ($R_0$ not self-derived) is declared but not automatically verifiable; it requires external corroboration.
- `GAP-PP-003`: The weakest-link confidence bound assumes all lineage nodes have declared confidence values; capsules with missing confidence default to `UNKNOWN`, which caps derived confidence at `UNKNOWN`.
- **Falsifier:** If any derived claim is accepted into the corpus without a verifiable lineage chain, the lineage presence invariant (`PP-1`) is falsified.
- **Falsifier:** If any provenance record is modified in-place without an explicit supersession link, the immutability invariant (`PP-2`) is falsified.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]] · [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]] · [[01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE|HERITAGE_PROVENANCE]]

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: persistent_provenance
node_type: core_law
path: 01_CANON/01_CORE_LAWS/PERSISTENT_PROVENANCE.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- RELATED_TO: [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]]
- RELATED_TO: [[01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE|HERITAGE_PROVENANCE]]
