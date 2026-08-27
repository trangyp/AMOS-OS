---
tags: ['canon', 'core_laws', 'note']
---

# L20 Adversarial Validation Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **ADV-1 Assume Attack**: consequential paths get adversarial probes (scope expansion, order manipulation, cache poisoning, spoofing) by default.
- **ADV-2 Transitive Reachability**: partial gating fails; enforcement roots must be attested and agent-immutable.
- **ADV-3 Deterministic Fuzz**: fuzz suites are deterministic and reproducible; results are receipts.
- **ADV-4 Escalate On Signal**: retry only after structured evidence of a real effect, never predictively.

## 4. Falsifiers
F1: authoritative adversarial canon defines different threat model.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l20_adversarial
node_type: note
path: 01_CANON/01_CORE_LAWS/L20_ADVERSARIAL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL
