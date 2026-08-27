---
type: transition
artifact_id: AMOS-OS-MODE-MODE_TRANSITION_MATRIX
title: AMOS OS Mode Transition Matrix
canonical_name: MODE_TRANSITION_MATRIX

artifact_class: GOVERNED_MODE_TRANSITION_MATRIX
subsystem: MODE_GOVERNANCE
origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

source_state: "existing_file: PLACEHOLDER
  recovered_substantive_implementation: false..."
related_artifacts: "see body"
implementation_status: SPECIFICATION
formal_verification_status: NOT_CLAIMED
empirical_validation_status: NOT_CLAIMED

promotion_required: true
updated: 2026-08-26
tags: [control_plane, commit, mode_index, note]

---

# AMOS OS — Mode Transition Matrix

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan
>
> **Artifact:** `MODE_TRANSITION_MATRIX.md`

---

# 0. PURPOSE

`MODE_TRANSITION_MATRIX` is the governed AMOS OS artifact whose purpose is to define the governed set of allowed transitions between mode states and the conditions under which each may occur.

It answers the question:

> Given current mode state S and requested mode state S', is the transition allowed, and what conditions must hold?

It does **not** assert that every described mechanism is currently implemented or empirically validated.

It does **not** grant authority.

It does **not** silently conflate specification with executable runtime.

---

# 1. CORE LAW

```text
NOT EVERY DESIRED STATE TRANSITION IS A VALID GOVERNED TRANSITION.
```

---

# 2. FUNDAMENTAL DISTINCTIONS

```text
REACHABLE != PERMITTED

PERMITTED != SAFE

SAFE != AUTHORIZED

AUTHORIZED != EXECUTED

EXECUTED != COMMITTED

TRANSITION_POSSIBLE != TRANSITION_DESIRABLE
```

---

# 3. WHY THIS ARTIFACT EXISTS

Without `MODE_TRANSITION_MATRIX`, AMOS mode governance would be forced to infer allowed and forbidden mode state transitions from implicit conventions, file names, or model-generated interpretations.

This artifact makes the governing structure explicit and auditable.

---

# 4. 3. Transition Object

from_state, to_state, preconditions, postconditions, authority.

---

# 5. 4. Matrix Semantics

Allowed, forbidden, conditional, reversible.

---

# 6. 5. Rollback

Allowed reverse transitions and recovery.

---

# 9. TESTS AND FALSIFIERS

`MODE_TRANSITION_MATRIX` is falsified if any of the following occur:

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

# END — MODE_TRANSITION_MATRIX

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: mode_transition_matrix
node_type: note
path: 03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_TRANSITION_MATRIX.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_MODE_INDEX_MOC]]
