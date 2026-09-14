---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_binding
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: 03 Policy Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - control-plane
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# 03 Policy — Map of Content

**Path:** `03_CONTROL_PLANE/03_POLICY`

## Files

- [[03_CONTROL_PLANE/03_POLICY/BIO_LOGICAL_GOVERNANCE_POLICY|BIO_LOGICAL_GOVERNANCE_POLICY]]
- [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|CANON_POLICY]]
- `canon_admission_gate.py` — fail-closed candidate-canon prepare/commit gate
- `test_canon_admission_gate.py` — bounded adversarial/unit verification
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

Governs the policy evaluation surface of the AMOS control plane: encoding, evaluating, and adjudicating the rules that determine whether proposed actions or state promotions are permitted, denied, held, quarantined, or forced to revalidate.

Policy sits between capability and authority. Evidence quality may establish candidate eligibility; it cannot manufacture commit authority.

## Key Artifacts

- [[03_CONTROL_PLANE/03_POLICY/POLICY_ENGINE|POLICY_ENGINE]] — broader policy-evaluation specification/engine surface
- [[03_CONTROL_PLANE/03_POLICY/POLICY_DECISION|POLICY_DECISION]] — decision record surface
- [[03_CONTROL_PLANE/03_POLICY/POLICY_REGISTRY|POLICY_REGISTRY]] — policy registry surface
- [[03_CONTROL_PLANE/03_POLICY/CANON_POLICY|CANON_POLICY]] — current canon-admission policy boundary
- `canon_admission_gate.py` — bounded executable admission gate; confidence is metadata, not authority
- [[02_KERNEL/01_META_LOGIC/K_CANON_ADMISSION_REPAIR_OVERLAY_2026-09-14|K_CANON Admission Repair Overlay]] — active interpretation guard for stale confidence-based promotion rules

## Invariants

- Policy decisions must be deterministic given the same typed inputs and policy identity.
- Policy artifacts must preserve source/version/provenance identity.
- Deny, hold, competing, quarantine, or revalidation is preferred over invented permission when mandatory evidence or authority is missing.
- Policy identity must be pinned at prepare and rechecked at commit.
- `confidence >= threshold` is never sufficient canon-promotion authority.
- An unresolved same-scope contradiction cannot be erased by policy priority.
- `COMMITTABLE` is a permission result, not evidence that a durable write occurred.

## Current bounded executable evidence

`canon_admission_gate.py` is locally verified by 12 tests covering missing evidence, competing claims, contradictions, mathematical and implementation evidence, authority, and source/policy/baseline/authority freshness.

System-wide policy enforcement remains partial until durable commit/release and all policy surfaces are bound to equivalent control-plane contracts.

## Cross-References

- [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02_CAPABILITY_MOC]]
- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]]
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- [[02_KERNEL/01_META_LOGIC/K_CANON_ADMISSION_REPAIR_OVERLAY_2026-09-14|K_CANON Admission Repair Overlay]]

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
