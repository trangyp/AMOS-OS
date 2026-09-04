---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: 03 Control Plane MOC
type: moc
source: 03_CONTROL_PLANE
tags:
  - 03-control-plane
  - canon/control-plane
  - amos-home
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 03 Control Plane — Map of Content

**Path:** `03_CONTROL_PLANE`
**Top-level files:** 4 | **Subdirectories:** 13
**Total notes:** 788

The Control Plane is the governance and coordination layer between canonical/kernel reasoning and runtime execution. It gates every consequential effect through task contracts, capability admission, policy, authority, provenance, commit, and rollback.

## Top-level contracts & resolver

- [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|COGNITIVE VAULT RESOLVER]] — **Path:** `03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER.md`
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane Control Plane Contract]] — > **Origin Architect / Steward:** Trang Phan
- [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL PLANE README]] — `CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE`.
- [[03_CONTROL_PLANE/PATH_REFERENCE_POLICY|PATH REFERENCE POLICY]] — `PATH_REFERENCE_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE`.

## Orientation & Index

- [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL PLANE MAP]] (3 notes) — `CONTROL_PLANE_MAP.md` defines the structural map of the AMOS OS control plane.
  - [[03_CONTROL_PLANE/00_INDEX/INDEX_CONTROL_PLANE_CONTROL_PLANE_CONTRACT|INDEX CONTROL PLANE CONTROL PLANE CONTRACT]] — - See also — [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL_PLANE_MAP]]
  - [[03_CONTROL_PLANE/00_INDEX/INDEX_CONTROL_PLANE_README|INDEX CONTROL PLANE README]] — artifact_id: AMOS-OS-CONTROL-PLANE-README

## Task & Capability Admission

- [[03_CONTROL_PLANE/01_TASK_CONTRACT/01_TASK_CONTRACT_MOC|01 Task Contract Moc]] (7 notes) — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT|TASK CONTRACT]] — > **Layer:** `03_CONTROL_PLANE/01_TASK_CONTRACT`
  - [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT_CONTROL_PLANE_README|TASK CONTRACT CONTROL PLANE README]] — `TASK CONTRACT CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/01_TASK_CONTRACT`.
  - [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_RESOLVER|TASK RESOLVER]] — > **Layer:** `03_CONTROL_PLANE/01_TASK_CONTRACT`
- [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02 Capability MOC]] (9 notes) — **Path:** `03_CONTROL_PLANE/02_CAPABILITY`
  - [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTRACT|CAPABILITY CONTRACT]] — `CAPABILITY_CONTRACT.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/02_CAPABILITY`.
  - [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTROL_PLANE_README|CAPABILITY CONTROL PLANE README]] — `CAPABILITY CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/02_CAPABILITY`.
  - [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY MANIFEST]] — This document defines the AMOS OS manifest structure for discovering, indexing, resolving, validating, governing, versioning, and auditing c
  - [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER|CAPABILITY RESOLVER]] — So the following is a **substantive candidate replacement**, not recovered pre-existing content.
  - [[03_CONTROL_PLANE/02_CAPABILITY/CONTROL_PLANE_CAPABILITY_CONTRACT|CONTROL PLANE CAPABILITY CONTRACT]] — This document defines the governed contract by which a capability may be represented, discovered, selected, invoked, supervised, validated, 

## Policy, Authority & Provenance

- [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03 Policy MOC]] (13 notes) — **Path:** `03_CONTROL_PLANE/03_POLICY`
  - [[03_CONTROL_PLANE/03_POLICY/BIO_LOGICAL_GOVERNANCE_POLICY|Bio-Logical Governance Policy]] — `BIO_LOGICAL_GOVERNANCE_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
  - [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|Canon Policy]] — `CANON_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
  - [[03_CONTROL_PLANE/03_POLICY/HERITAGE_POLICY|Heritage Policy]] — `HERITAGE_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
  - [[03_CONTROL_PLANE/03_POLICY/NEUROSYNCAI_GOVERNANCE_POLICY|NeuroSyncAI Governance Policy]] — `NEUROSYNCAI_GOVERNANCE_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
  - [[03_CONTROL_PLANE/03_POLICY/POLICY_CONTROL_PLANE_README|POLICY CONTROL PLANE README]] — `POLICY CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
  - [[03_CONTROL_PLANE/03_POLICY/POLICY_DECISION|POLICY DECISION]] — `POLICY_DECISION.md` defines the AMOS OS contract for representing, evaluating, composing, validating, recording, invalidating, and consumin
  - [[03_CONTROL_PLANE/03_POLICY/POLICY_ENGINE|POLICY ENGINE]] — `POLICY_ENGINE.md` defines the AMOS OS architecture for discovering, resolving, evaluating, composing, revalidating, and auditing policies t
  - [[03_CONTROL_PLANE/03_POLICY/POLICY_REGISTRY|POLICY REGISTRY]] — `POLICY_REGISTRY.md` defines the AMOS OS contract for registering, identifying, versioning, discovering, scoping, superseding, revoking, qua
  - [[03_CONTROL_PLANE/03_POLICY/UBI_INTEGRITY_POLICY|UBI Integrity Policy]] — `UBI_INTEGRITY_POLICY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/03_POLICY`.
- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04 Authority MOC]] (139 notes) — **Path:** `03_CONTROL_PLANE/04_AUTHORITY`
- [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05 Provenance MOC]] (9 notes) — **Path:** `03_CONTROL_PLANE/05_PROVENANCE`
  - [[03_CONTROL_PLANE/05_PROVENANCE/CONTROL_PLANE_PROVENANCE_CONTRACT|Control Plane Provenance Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/05_PROVENANCE/OBSERVED_READ_SET|Observed Read Set]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_CONTROL_PLANE_README|PROVENANCE CONTROL PLANE README]] — `PROVENANCE CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/05_PROVENANCE`.
  - [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_LEDGER|PROVENANCE LEDGER]] — Control Plane-plane artifact. AMOS_MODEL · CONDITIONAL · implementation PARTIAL.
  - [[03_CONTROL_PLANE/05_PROVENANCE/READ_SET_VALIDATOR|Read Set Validator]] — > **Origin Architect / Steward:** Trang Phan

## Semantic Transactions, Effects & Commit

- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/06_SEMANTIC_TRANSACTION_MOC|06 Semantic Transaction MOC]] (12 notes) — **Path:** `03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION`
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CANON_SEMANTIC_TRANSACTION|Canon Semantic Transaction]] — `CANON_SEMANTIC_TRANSACTION.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/06_SEMANTIC_TRAN
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CONTROL_PLANE_SEMANTIC_TRANSACTION_CONTRACT|Control Plane Semantic Transaction Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CROSS_FRAMEWORK_TRANSACTION|Cross-Framework Transaction]] — `CROSS_FRAMEWORK_TRANSACTION.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/06_SEMANTIC_TRA
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/LINEAGE_GRAPH|Lineage Graph]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/MULTI_RSCF_TRANSACTION|Multi-RSCF Transaction]] — `MULTI_RSCF_TRANSACTION.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/06_SEMANTIC_TRANSACT
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/PARAMETER_PROVENANCE|Parameter Provenance]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/SEMANTIC_TRANSACTION|Semantic Transaction]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/SEMANTIC_TRANSACTION_CONTROL_PLANE_README|SEMANTIC TRANSACTION CONTROL PLANE README]] — `SEMANTIC TRANSACTION CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/06_SEMANTIC_T
- [[03_CONTROL_PLANE/08_EFFECTS/08_EFFECTS_MOC|08 Effects MOC]] (9 notes) — **Path:** `03_CONTROL_PLANE/08_EFFECTS`
  - [[03_CONTROL_PLANE/08_EFFECTS/CONTROL_PLANE_EFFECTS_CONTRACT|Control Plane Effects Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/08_EFFECTS/EFFECTS_CONTROL_PLANE_README|EFFECTS CONTROL PLANE README]] — `EFFECTS CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/08_EFFECTS`.
  - [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_INTENT|Effect Intent]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_MANIFEST|Effect Manifest]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_STATE|Effect Release State]] — > **Origin Architect / Steward:** Trang Phan
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09 Commit MOC]] (553 notes) — **Path:** `03_CONTROL_PLANE/09_COMMIT`
  - [[03_CONTROL_PLANE/09_COMMIT/CAUSAL_EPOCH_FINALITY|Causal Epoch Finality]] — `CAUSAL_EPOCH_FINALITY.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/09_COMMIT`.
  - [[03_CONTROL_PLANE/09_COMMIT/COMMIT_CONTROL_PLANE_README|COMMIT CONTROL PLANE README]] — `COMMIT CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/09_COMMIT`.
  - [[03_CONTROL_PLANE/09_COMMIT/CONTROL_PLANE_COMMIT_CONTRACT|Control Plane Commit Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/09_COMMIT/PROOF_BASED_COORDINATION_AVOIDANCE|Proof-Based Coordination Avoidance]] — `PROOF_BASED_COORDINATION_AVOIDANCE.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/09_COMMI
  - [[03_CONTROL_PLANE/09_COMMIT/SHARD_LOCAL_FINALIZATION|Shard-Local Finalization]] — `SHARD_LOCAL_FINALIZATION.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/09_COMMIT`.

## Observability, Exposure, Replay, Rollback

- [[03_CONTROL_PLANE/07_OBSERVABILITY/07_OBSERVABILITY_MOC|07 Observability MOC]] (9 notes) — **Path:** `03_CONTROL_PLANE/07_OBSERVABILITY`
  - [[03_CONTROL_PLANE/07_OBSERVABILITY/BLIND_SPOT_REGISTRY|BLIND SPOT REGISTRY]] — Registry for **BLIND SPOT REGISTRY** within the Control Plane plane (governance surfaces that gate effects: task contracts, capability, poli
  - [[03_CONTROL_PLANE/07_OBSERVABILITY/CONTROL_PLANE_OBSERVABILITY_CONTRACT|Control Plane Observability Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/07_OBSERVABILITY/MONITOR_REGISTRY|MONITOR REGISTRY]] — Registry for **MONITOR REGISTRY** within the Control Plane plane (governance surfaces that gate effects: task contracts, capability, policy,
  - [[03_CONTROL_PLANE/07_OBSERVABILITY/OBSERVABILITY_CONTROL_PLANE_README|OBSERVABILITY CONTROL PLANE README]] — `OBSERVABILITY CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/07_OBSERVABILITY`.
  - [[03_CONTROL_PLANE/07_OBSERVABILITY/OBSERVABILITY_ENVELOPE|Observability Envelope]] — > **Origin Architect / Steward:** Trang Phan
- [[03_CONTROL_PLANE/10_EXPOSURE/10_EXPOSURE_MOC|10 Exposure Moc]] (6 notes) — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/10_EXPOSURE/CONTROL_PLANE_EXPOSURE_CONTRACT|Control Plane Exposure Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/10_EXPOSURE/EXPOSURE_CONTROL_PLANE_README|EXPOSURE CONTROL PLANE README]] — `EXPOSURE CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/10_EXPOSURE`.
- [[03_CONTROL_PLANE/11_REPLAY/11_REPLAY_MOC|11 Replay Moc]] (6 notes) — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/11_REPLAY/CONTROL_PLANE_REPLAY_CONTRACT|Control Plane Replay Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/11_REPLAY/REPLAY_CONTROL_PLANE_README|REPLAY CONTROL PLANE README]] — `REPLAY CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/11_REPLAY`.
- [[03_CONTROL_PLANE/12_ROLLBACK/12_ROLLBACK_MOC|12 Rollback Moc]] (8 notes) — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/12_ROLLBACK/CANON_LOCAL_INVALIDATION|Canon Local Invalidation]] — `CANON_LOCAL_INVALIDATION.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/12_ROLLBACK`.
  - [[03_CONTROL_PLANE/12_ROLLBACK/CONTROL_PLANE_ROLLBACK_CONTRACT|Control Plane Rollback Contract]] — > **Origin Architect / Steward:** Trang Phan
  - [[03_CONTROL_PLANE/12_ROLLBACK/FRAMEWORK_LINEAGE_ROLLBACK|Framework Lineage Rollback]] — `FRAMEWORK_LINEAGE_ROLLBACK.md` is an **ADD-ONLY placeholder** for the **Control Plane** plane segment at `03_CONTROL_PLANE/12_ROLLBACK`.
  - [[03_CONTROL_PLANE/12_ROLLBACK/ROLLBACK_CONTROL_PLANE_README|ROLLBACK CONTROL PLANE README]] — `ROLLBACK CONTROL PLANE README` is the package readme for the **Control Plane** plane segment at `03_CONTROL_PLANE/12_ROLLBACK`.

______________________________________________________________________

|**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/00_HOME|00_HOME]]