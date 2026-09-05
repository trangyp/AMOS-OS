---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 03 Policy Moc
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

# 03 Policy — Map of Content

**Path:** `03_CONTROL_PLANE/03_POLICY`
**Files:** 9 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/03_POLICY/BIO_LOGICAL_GOVERNANCE_POLICY|BIO_LOGICAL_GOVERNANCE_POLICY]]
- [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|CANON_POLICY]]
- [[03_CONTROL_PLANE/03_POLICY/HERITAGE_POLICY|HERITAGE_POLICY]]
- [[03_CONTROL_PLANE/03_POLICY/NEUROSYNCAI_GOVERNANCE_POLICY|NEUROSYNCAI_GOVERNANCE_POLICY]]
- [[03_CONTROL_PLANE/03_POLICY/POLICY_CONTROL_PLANE_README|POLICY_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/03_POLICY/POLICY_DECISION|POLICY_DECISION]]
- [[03_CONTROL_PLANE/03_POLICY/POLICY_ENGINE|POLICY_ENGINE]]
- [[03_CONTROL_PLANE/03_POLICY/POLICY_REGISTRY|POLICY_REGISTRY]]
- [[03_CONTROL_PLANE/03_POLICY/UBI_INTEGRITY_POLICY|UBI_INTEGRITY_POLICY]]

## Subdirectories

- [[03_CONTROL_PLANE/03_POLICY/00_INDEX/POLICY_MAP|POLICY_MAP]] — 00_INDEX

## Purpose

Governs the policy evaluation surface of the AMOS control plane — encoding, evaluating, and adjudicating the rules that determine whether proposed actions are permitted, denied, or deferred. Policy is the decision layer that sits between capability (what is possible) and authority (what is authorized).

## Key Artifacts

- [[03_CONTROL_PLANE/03_POLICY/POLICY_ENGINE|POLICY_ENGINE]] — Core policy evaluation engine with gate-by-gate adjudication
- [[03_CONTROL_PLANE/03_POLICY/POLICY_DECISION|POLICY_DECISION]] — Decision record format for permit/deny/defer outcomes
- [[03_CONTROL_PLANE/03_POLICY/POLICY_REGISTRY|POLICY_REGISTRY]] — Registry of all active policy artifacts with version and signer provenance
- [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|CANON_POLICY]] — Canonical policy framework governing vault-wide rule precedence

## Invariants

- Policy decisions must be deterministic given the same inputs and policy version
- Policy artifacts must be content-addressed with signer identity provenance
- Deny is the default outcome when policy evaluation is incomplete or ambiguous
- Policy version must be pinned at commit time; mid-flight policy changes require revalidation

## Cross-References

- [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02_CAPABILITY_MOC]] — Capability plane provides the surface policy evaluates over
- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]] — Authority plane enforces policy decisions with binding witnesses
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Commit plane pins policy version at commit time for replay safety

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
