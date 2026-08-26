---
artifact_id: AMOS-OS-MODE-MODE_FALSIFIER_REGISTRY
title: AMOS OS Mode Falsifier Registry
canonical_name: MODE_FALSIFIER_REGISTRY

artifact_class: GOVERNED_MODE_FALSIFIER_REGISTRY
subsystem: MODE_GOVERNANCE
origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

source_state:
  existing_file: PLACEHOLDER
  recovered_substantive_implementation: false

related_artifacts:
  - MODE_ADMISSION_QUEUE.md
  - MODE_COMPOSITION_REGISTRY.md
  - MODE_CONFLICT_REGISTRY.md
  - MODE_COVERAGE_MATRIX.md
  - K_GMEF
  - K_RSCF
  - K_HML
  - K_SYSTEM_STATE
  - K_CONTEXT_STATE
  - K_PROVENANCE
  - K_COMMIT_TIME_AUTHORITY

implementation_status: SPECIFICATION
formal_verification_status: NOT_CLAIMED
empirical_validation_status: NOT_CLAIMED

promotion_required: true
updated: 2026-08-26
tags: ['control_plane', 'commit', 'mode_index', 'note']

---
# AMOS OS — Mode Falsifier Registry

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan
>
> **Artifact:** `MODE_FALSIFIER_REGISTRY.md`

---

# 0. PURPOSE

`MODE_FALSIFIER_REGISTRY` is the governed AMOS OS artifact whose purpose is to register tests, counterexamples, failure scenarios, and empirical conditions that could falsify a mode claim.

It answers the question:

> What would show that a declared mode does not actually hold, is not safe, or does not cover its claimed scope?

It does **not** assert that every described mechanism is currently implemented or empirically validated.

It does **not** grant authority.

It does **not** silently conflate specification with executable runtime.

---

# 1. CORE LAW

```text
A MODE WITHOUT A FALSIFIER IS A CLAIM WITHOUT A TEST.
```

---

# 2. FUNDAMENTAL DISTINCTIONS

```text
FALSIFIER_LISTED != FALSIFIER_EXECUTED

FALSIFIER_EXECUTED != FALSIFIER_PASSED

FALSIFIER_PASSED != PROOF

NO_KNOWN_FALSIFIER != UNFALSIFIABLE

FAILED_FALSIFIER != MODE_INVALID
```

---

# 3. WHY THIS ARTIFACT EXISTS

Without `MODE_FALSIFIER_REGISTRY`, AMOS mode governance would be forced to infer falsification conditions and counterexamples from implicit conventions, file names, or model-generated interpretations.

This artifact makes the governing structure explicit and auditable.

---

# 4. 3. Falsifier Types

Scope, composition, authority, runtime, safety.

---

# 5. 4. Registry Fields

falsifier_id, target_mode, condition, expected_outcome, evidence.

---

# 6. 5. Failure Response

Quarantine, review, supersession, revocation.

---

# 9. TESTS AND FALSIFIERS

`MODE_FALSIFIER_REGISTRY` is falsified if any of the following occur:

- The artifact permits a mode to be treated as admitted without evidence.
- It conflates a registry/schedule/graph entry with authority or execution.
- It allows a declared distinction to be silently ignored.
- It accepts a claim as proven without a corresponding evidence artifact.
- It permits cyclic, stale, or unbounded governance without detection.

---

# 10. STATUS PRESERVATION

This artifact remains `CANDIDATE_CANON / DERIVED` until:

- the exact historical source or approved new specification is bound;
- the canon/provenance process promotes it;
- formal verification and empirical validation evidence are attached;
- the relevant supersession and source registry entries are updated.

# END — MODE_FALSIFIER_REGISTRY

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: mode_falsifier_registry
node_type: note
path: 03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_FALSIFIER_REGISTRY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
