---
artifact_id: AMOS-OS-MODE-MODE_ONTOLOGY
title: AMOS OS Mode Ontology
canonical_name: MODE_ONTOLOGY

artifact_class: GOVERNED_MODE_ONTOLOGY
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
---

# AMOS OS — Mode Ontology

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan
>
> **Artifact:** `MODE_ONTOLOGY.md`

---

# 0. PURPOSE

`MODE_ONTOLOGY` is the governed AMOS OS artifact whose purpose is to define the controlled vocabulary, taxonomies, and semantic relations for AMOS operating modes.

It answers the question:

> What kinds of modes exist, how are they classified, and what relations hold among mode categories?

It does **not** assert that every described mechanism is currently implemented or empirically validated.

It does **not** grant authority.

It does **not** silently conflate specification with executable runtime.

---

# 1. CORE LAW

```text
A MODE CLASSIFICATION IS GOVERNED, NOT MERELY NAMED.
```

---

# 2. FUNDAMENTAL DISTINCTIONS

```text
LABEL != CLASS

CLASS != INSTANTIATION

SIMILAR_NAME != SAME_CLASS

ONTOLOGY_DEFINED != ONTOLOGY_CORRECT

ONTOLOGY_CORRECT != RUNTIME_APPLICABLE
```

---

# 3. WHY THIS ARTIFACT EXISTS

Without `MODE_ONTOLOGY`, AMOS mode governance would be forced to infer mode classification and semantic relations from implicit conventions, file names, or model-generated interpretations.

This artifact makes the governing structure explicit and auditable.

---

# 4. 3. Mode Classes

Operational, governance, cognitive, recovery, domain.

---

# 5. 4. Relations

subClassOf, partOf, requires, excludes, refines.

---

# 6. 5. Versioning

Ontology changes are supersession-tracked.

---

# 9. TESTS AND FALSIFIERS

`MODE_ONTOLOGY` is falsified if any of the following occur:

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

# END — MODE_ONTOLOGY

