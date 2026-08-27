---
title: C01 GOVERNANCE CONTROL PLANES COGNITIVE MATRIX FAILURE MODES
type: note
tags: [note, c01-governance]
---

# C01 — Failure Modes

**Package:** `C01_GOVERNANCE`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers law-stack enforcement (Law of Law, Rule of 2/4), authority envelopes, enforcement-root attestation, and fail-closed defaults.

## Failure modes

- `FM-C01-01`: Transitive bypass of one-hop gating. → detection: full-path gate audit
- `FM-C01-02`: Mutable enforcement root. → detection: root attestation epoch check
- `FM-C01-03`: Silent authority expansion. → detection: envelope diffing

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

---

[[COGNITIVE_MATRIX_MOC]] · 00_ROOT_MOC|AMOS MOC

---
RSCF-NODE
node_id: c01_planes_failure_modes
node_type: note
path: 03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_CONTROL_PLANES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_CONTROL_PLANES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[C01_GOVERNANCE_MOC]]
