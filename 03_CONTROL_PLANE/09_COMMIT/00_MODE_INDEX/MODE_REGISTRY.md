---
artifact_id: AMOS-OS-MODE-MODE_REGISTRY
title: AMOS OS Mode Registry
canonical_name: MODE_REGISTRY

artifact_class: GOVERNED_MODE_MASTER_REGISTRY
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
# AMOS OS — Mode Registry

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan
>
> **Artifact:** `MODE_REGISTRY.md`

---

# 0. PURPOSE

`MODE_REGISTRY` is the governed AMOS OS artifact whose purpose is to serve as the authoritative addressable inventory of all admitted, proposed, deprecated, and superseded modes.

It answers the question:

> What modes exist, what are their identities, versions, statuses, scopes, and provenance?

It does **not** assert that every described mechanism is currently implemented or empirically validated.

It does **not** grant authority.

It does **not** silently conflate specification with executable runtime.

---

# 1. CORE LAW

```text
THE REGISTRY DOES NOT DECIDE ADMISSION; IT RECORDS ADMISSION DECISIONS.
```

---

# 2. FUNDAMENTAL DISTINCTIONS

```text
REGISTERED != ADMITTED

ADMITTED != ACTIVE

ACTIVE != CURRENT

DEPRECATED != DELETED

SUPERSEDED != INVALID
```

---

# 3. WHY THIS ARTIFACT EXISTS

Without `MODE_REGISTRY`, AMOS mode governance would be forced to infer mode identity, version, and status from implicit conventions, file names, or model-generated interpretations.

This artifact makes the governing structure explicit and auditable.

---

# 4. 3. Registry Object

mode_id, version, content_hash, status, scope, provenance.

---

# 5. 4. Status Values

DRAFT, PROPOSED, ADMITTED, ACTIVE, DEPRECATED, SUPERSEDED, REVOKED.

---

# 6. 5. Discovery

Registry provides the authoritative addressing surface.

---

# 9. TESTS AND FALSIFIERS

`MODE_REGISTRY` is falsified if any of the following occur:

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

# END — MODE_REGISTRY

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
