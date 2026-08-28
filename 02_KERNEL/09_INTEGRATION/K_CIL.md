---
title: K_CIL — Canon Integration Layer (CIL) Kernel
type: kernel
source: 02_KERNEL/09_INTEGRATION
artifact_id: AMOS-OS-K-CIL
canonical_name: K_CIL
artifact_type: kernel_integration_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
segment: 02_KERNEL/09_INTEGRATION
kernel_family: INTEGRATION
domain: canon-integration
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- integration
- cil
- canon-integration-layer
- add-only-ingestion
- deduplication-protocol
- rscf/claim
- rscf/state/model
- 09-integration-moc
- 02-kernel-moc
- 00-home
- 00-root-moc
aliases:
- Canon Integration Layer Kernel
- CIL Kernel
- K_CIL
- AMOS Canon Ingestion Engine
---

# K_CIL — Canon Integration Layer (CIL) Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL/09_INTEGRATION`  
> **Status:** `AMOS_MODEL`  
> **Ingestion Protocol:** `ADD_ONLY` $\times$ Single Canonical Node Invariant $\times$ Complete Provenance Lineage

---

## 1. Purpose and Canonical Integrity

`K_CIL` serves as the authoritative boundary filter for all new knowledge, research papers, external code, and user propositions entering the AMOS second-brain repository. It enforces the **`AMOS_CANON_INGESTION_RULE`**, ensuring that native canon is never overwritten, duplicated, or corrupted by unverified external claims.

```
+-------------------------------------------------------------------------+
|                  CANON INTEGRATION LAYER (CIL) PIPELINE                 |
|                                                                         |
|  [ Inbound Framework / Document / Claim ]                               |
|                     |                                                   |
|                     v                                                   |
|  ( Step 1: Duplicate Check & Lineage Hash Comparison )                  |
|                     |                                                   |
|      +--------------+--------------+                                    |
|      |                             |                                    |
|  [ Existing Framework ]    [ New Candidate Framework ]                  |
|      |                             |                                    |
|      v                             v                                    |
|  ( Link Provenance Edges;  ( Assign Typed RSCF Node Schema & Tags;      |
|    Do NOT Duplicate Node )   Determine Plane Placement )                |
|      |                             |                                    |
|      +--------------+--------------+                                    |
|                     |                                                   |
|                     v                                                   |
|  ( Step 2: Epistemic Bounds & Confidence Ceiling Declaration )          |
|                     |                                                   |
|                     v                                                   |
|  [ Atomic ADD_ONLY Commit to Vault with Bidirectional Wikilinks ]       |
+-------------------------------------------------------------------------+
```

---

## 2. The 6 Rules of Canon Ingestion

1. **Rule 1 (Preserve Existing Files):** Never overwrite existing canonical notes; normalize new contributions into distinct RSCF nodes.
2. **Rule 2 (Single Canonical Node):** If a concept appears across multiple source files, merge references into one canonical hub note and link source provenances.
3. **Rule 3 (Historical Heritage Preservation):** Legacy and historical drafts are preserved in archive planes with lineage edges to current canon.
4. **Rule 4 (External Research Containment):** External academic preprints (arXiv/PubMed) are tagged as `EVIDENCE` and kept strictly separated from native AMOS canon.
5. **Rule 5 (Fail-Closed on Uncertainty):** Unverified claims or ambiguous terms are explicitly marked as `UNKNOWN/GAP` and assigned confidence $\le 0.50$.
6. **Rule 6 (No Hallucinated Citations):** Every empirical or mathematical reference must be verifiable against active local repository files or real external DOIs.

---

## 3. Ingestion State Mutation Logic

$$\text{CIL}(\mathcal{A}_{\text{new}}) = \begin{cases} 
\text{LINK\_PROVENANCE}(\mathcal{A}_{\text{existing}}, \mathcal{A}_{\text{new}}) & \text{if } \text{Similarity}(\mathcal{A}_{\text{new}}, \mathcal{A}_{\text{existing}}) \ge 0.90 \\
\text{CREATE\_TYPED\_NODE}(\mathcal{A}_{\text{new}}) & \text{if } \text{ValidSchema}(\mathcal{A}_{\text{new}}) \land \text{Novel}(\mathcal{A}_{\text{new}}) \\
\text{REJECT\_FAIL\_CLOSED}(\mathcal{A}_{\text{new}}) & \text{otherwise}
\end{cases}$$

---

## 4. Cross-Plane Bindings

- **Canon & Governance:** [[K_CANON]] · [[K_GOVERNANCE]] · [[LAW_HIERARCHY]]
- **Integration Frameworks:** [[K_BINDING]] · [[K_HERITAGE_BINDING]] · [[K_RSCF]]
- **Anti-Autopoisoning:** [[K_ANTI_AUTOPOISONING]] · [[K_FAIL_CLOSED]]
- **Navigation:** [[00_HOME]] · [[02_KERNEL_MOC]] · [[09_INTEGRATION_MOC]] · [[00_ROOT_MOC]]

