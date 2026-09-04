---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Persistent Provenance
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

# PERSISTENT_PROVENANCE — Cryptographic Lineage Preservation Law

PERSISTENT_PROVENANCE mandates that all derived claims, state transitions, and evolutionary mutations maintain an immutable, tamper-evident lineage back to independent root observations.

________________________________________________________________________

## 1. Definition

Every material claim $C_t$ in AMOS carries a **provenance chain** — an ordered record of its ancestry from root observations through every transformation:

$$\forall K_t, \; \text{Lineage}(K_t) = \langle R_0, T_1, T_2, \dots, T_t \rangle \; \text{is strictly verifiable}.$$

Where:
- $R_0$ = root observation or independent source evidence
- $T_i$ = transformation step $i$ (derivation, repair, evolution, consolidation)
- $K_t$ = the knowledge artifact at state $t$

A provenance chain must be:
- **Complete** — no unexplained gaps between $T_i$ and $T_{i+1}$
- **Tamper-evident** — any modification to a link is detectable
- **Persistent** — survives transformation, repair, restart, and archival
- **Typed** — each link records what operation occurred and under what authority

________________________________________________________________________

## 2. Purpose

Provenance is load-bearing infrastructure for AMOS trust. Without persistent provenance:

- Confidence ratings become groundless
- Scope and regime applicability become unverifiable
- Recovery cannot distinguish valid from corrupted state
- Authority delegation loses accountability

Failure modes prevented:

```text
CL-F006 PROVENANCE_LOSS
CL-F021 PROVENANCE_LINEAGE_ERASED
CL-F001 FABRICATED_PREMISE
CL-F007 CORRELATED_EVIDENCE_AS_INDEPENDENT
CL-F022 VERSION_IDENTITY_COLLAPSE
```

________________________________________________________________________

## 3. Formal Provenance Record

Each provenance link $T_i$ is a tuple:

$$T_i = \langle \text{op}_i, \text{authority}_i, \text{timestamp}_i, \text{scope}_i, \text{regime}_i, \text{hash}_i \rangle$$

| Field | Meaning |
|-------|---------|
| $\text{op}_i$ | transformation type: DERIVATION, REPAIR, EVOLUTION, CONSOLIDATION, REPAIR_ROLLBACK |
| $\text{authority}_i$ | who or what authorized the transformation |
| $\text{timestamp}_i$ | logical or physical time of the operation |
| $\text{scope}_i$ | applicability envelope at the time of transformation |
| $\text{regime}_i$ | epistemic regime at the time of transformation |
| $\text{hash}_i$ | tamper-evident digest of the transformation contents |

The chain verification function:

$$\text{Verify}(\langle R_0, T_1, \dots, T_t \rangle) = \bigwedge_{i=1}^{t} \text{LinkValid}(T_{i-1}, T_i)$$

Where $\text{LinkValid}(T_{i-1}, T_i)$ checks that $T_i$'s inputs are consistent with $T_{i-1}$'s outputs.

________________________________________________________________________

## 4. Transformation Persistence

Provenance must survive all of the following operations:

| Operation | Provenance Requirement |
|-----------|----------------------|
| Derivation | Append new link $T_{i+1}$; preserve full chain |
| Repair | Record repair operation; original chain becomes historical branch |
| Restart | Rehydrate provenance from persisted state; verify chain integrity |
| Archival | Preserve chain in archival format; mark as historical but recoverable |
| Consolidation | Record consolidation provenance; preserve individual source chains |
| Scope transfer | Record scope bridge; new link inherits parent chain |
| Regime transfer | Record regime bridge; new link inherits parent chain |

________________________________________________________________________

## 5. Provenance Loss — Fail Closed

If provenance is lost or corrupted:

$$\text{ProvenanceLost}(C) \Rightarrow \text{fail\_closed}(C)$$

Specifically:
1. The claim $C$ is demoted to `UNKNOWN/GAP` provenance class
2. All descendants of $C$ are flagged for revalidation
3. The loss event is recorded in the [[01_CANON/01_CORE_LAWS/ROLLBACK_AND_RECOVERY_BASINS|recovery basin]]
4. Recovery requires re-establishing provenance from independent root evidence

Failure closed is non-negotiable. Provenance loss never results in silent continuation.

________________________________________________________________________

## 6. Lineage and Supersession Tracking

When a claim $C_1$ is superseded by $C_2$:

$$C_1 \xrightarrow{\text{SUPERSEDED\_BY}} C_2$$

The supersession must record:
- The reason for supersession (evolution, correction, scope expansion)
- The provenance of $C_2$ (which includes $C_1$'s chain as ancestor)
- The validation state of $C_2$ at supersession time

Hard rule:

```text
SUPERSEDED ≠ DELETED
```

Historical states must remain recoverable. The original chain of $C_1$ is preserved even after $C_2$ supersedes it.

Lineage depth limit: AMOS tracks full lineage without artificial depth truncation. If chain depth exceeds practical verification limits, the claim must be revalidated from root evidence rather than relying on deep chain traversal.

________________________________________________________________________

## 7. Invariants

| Invariant | Statement |
|-----------|-----------|
| Provenance completeness | $\forall C_t : \text{Lineage}(C_t) \text{ contains no unexplained gaps}$ |
| Provenance persistence | $\forall \text{op} \in \{\text{derive, repair, restart, archive}\} : \text{Lineage}(C) \text{ survives op}$ |
| Fail closed on loss | $\text{ProvenanceLost}(C) \Rightarrow \text{demote}(C, \text{UNKNOWN/GAP})$ |
| Supersession preservation | $\text{SUPERSEDED}(C_1) \Rightarrow \text{recoverable}(C_1)$ |
| Chain integrity | $\text{Verify}(\text{Lineage}(C_t)) = \text{TRUE} \text{ at all material checkpoints}$ |

________________________________________________________________________

## 8. Gates

Provenance persistence is checked at:

- **Commit gate**: Before any material claim enters the canonical knowledge base
- **Recovery gate**: During rollback or repair — provenance chain integrity verified before state restoration
- **Transfer gate**: When claims cross scope or regime boundaries — provenance bridge recorded
- **Evolution gate**: During GMEF mutation — lineage of pre- and post-mutation states preserved
- **Promotion gate**: When source claims are promoted to validated knowledge

________________________________________________________________________

## 9. Falsifiers

| Falsifier | Description |
|-----------|-------------|
| Chain gap | A provenance chain with an unexplained discontinuity |
| Tampered link | A hash mismatch at any transformation step |
| Silent provenance loss | A claim operating without recoverable lineage |
| Synthetic independence | Multiple claims from one source counted as independent |
| Deep chain without revalidation | Claims relying on chain traversal beyond practical verification without revalidation |

________________________________________________________________________

## 10. Integration

- **RSCF**: Every material RSCF node must carry provenance fields.
- **Scope-regime firewall**: Provenance bridges are recorded when claims cross boundaries.
- **Rollback**: Recovery basins preserve provenance chains through rollback operations.
- **Receipt**: Successful provenance validation emits [[01_CANON/01_CORE_LAWS/PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT|PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT]].
- **Control-plane**: Provenance completeness is a mandatory admission check.

________________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]] · [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]] · [[01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE|HERITAGE_PROVENANCE]]

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

________________________________________________________________________

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
- ENFORCED_BY: [[01_CANON/01_CORE_LAWS/PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT|PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/ROLLBACK_AND_RECOVERY_BASINS|ROLLBACK_AND_RECOVERY_BASINS]]
