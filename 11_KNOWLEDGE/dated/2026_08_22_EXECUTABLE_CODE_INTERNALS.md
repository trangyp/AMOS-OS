---
title: "2026-08-22 Executable Code Internals"
created: "2026-08-22"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-executable-code-internals, dated, dated/2026-08-22]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# 2026-08-22 Executable Code Internals

## Summary
Deep code-level inspection of the AMOS brain's three core Python files:
1. `executable_brain_model.py` — 68 layer classes, 314 state fields, 71 accessor methods
2. `AMOS_CORE_v4_8_capability_bound_governance (2).py` — 7,502 lines, 90+ classes, 12 enums, 18 rewrite functions
3. `AMOS_AUTONOMOUS_EVOLUTION_LAYER.py` — 1,871 lines, 25 classes, 10 improvement kinds, 10 validation stages
4. `AMOS_SKILL_DEPENDENCY_GRAPH.py` — 743 skills, 0 cycles, 11 graph methods

## Key Findings
- Brain model progresses through 7-phase reasoning loop across steps (verified by live test)
- Governance kernel has 10 guardrails (NO_PSYCH_LABELS, NO_MORAL_JUDGEMENT, etc.)
- 11 Omega stages: INTENT → ENVIRONMENT → GENERATE → VERIFY → WATCH → GOVERN → COMMIT → HEALTH → REPAIR → COMPLETE → QUARANTINE
- 19 NodeType logic types: ATOM, NOT, AND, OR, IMPLIES, BOTTOM, PARADOX, CONV, DIVG, PLOGIC, NLOGIC, ZLOGIC, DLOGIC, MLOGIC, METAL, SUPRAL, ANTIL, NULLL
- 4 protected layers (M0): trusted_proof_kernel, axiomatic_soundness_rules, base_structural_semantics, determinism_contract
- Skill graph has 743 skills with 0 cycles (valid DAG)

## Links
- [[00_COSMO_BRAIN_MOC]]
- executable_brain_model
- AMOS_CORE_v4_8_capability_bound_governance
- 2026-08-22 Tests Logic Bridge Registry — companion inspection of test/logic/bridge modules
- 2026-08-22 Executable Brain Model Lineage — v1→v22 lineage of the executable brain
- 2026-08-22 Brain Inventory — verified corpus counts

---
**MOC:** [[DATED_MOC]]
