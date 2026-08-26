---
tags: ['canon', 'core_laws', 'note']
---

# L6 Uncertainty Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: LOGIC_EXECUTABLE_IN_PART
updated: 2026-08-26

## 0. Status
Proposed specification. AMOS_MODEL.

## 1. Purpose
Make uncertainty explicit, typed, and non-collapsible.

## 2. Laws
- **U-1 Typed Uncertainty**: uncertainty is classified (SOURCE / DERIVED / MODEL / UNKNOWN) before use.
- **U-2 Confidence Ceiling**: no claim exceeds its evidence-derived ceiling; hard ceiling 0.95 absent stronger proof.
- **U-3 Ambiguity Preservation**: incomparable alternatives remain COMPETING — averaging is prohibited.
- **U-4 Unknown Propagation**: operations on unknown inputs yield unknown or fail closed; never plausible fabrication.

## 3. Enforcement
Confidence ceilings in validators; competing-hypothesis sets preserved verbatim; UNKNOWN/GAP labels propagate through dependency chains.

## 4. Falsifiers
F1: authoritative epistemics canon defines different ceiling semantics.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l6_uncertainty
node_type: note
path: 01_CANON/01_CORE_LAWS/L6_UNCERTAINTY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL
