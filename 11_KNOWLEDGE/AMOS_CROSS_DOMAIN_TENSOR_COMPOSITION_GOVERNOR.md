---
title: AMOS CROSS DOMAIN TENSOR COMPOSITION GOVERNOR
canon-group: reference
rscf-state: derived
tags:
- skill
- cross-domain
- tensor
- composition
- governor
- rscf
---

# AMOS Cross-Domain Tensor Composition Governor

## Overview

A new AMOS skill that governs when and how typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) from different AMOS domains (C01-C12) can be composed. Enforces the tensor compatibility invariant, epistemic class preservation across domain boundaries, the weakest-load-bearing-edge confidence rule, and cross-domain provenance tracking.

## Gap Evidence

- Skill survey of 270+ skills found only 3 explicit cross-domain skills (~1.1%)
- _00_Cosmo brain exploration found 8 cross-domain integration gaps
- TENSOR_CONTRACTS.md states the critical invariant: "Tensor composition is prohibited until shared axes are semantically compatible. Same-name axes do not prove same meaning."
- No existing skill enforces this invariant across domain boundaries

## Capabilities (9)

1. `cross_domain.validate_axis_compatibility` — Validate shared axes are semantically compatible
2. `cross_domain.govern_composition` — Govern when tensors can be composed (PERMITTED/BLOCKED/CONDITIONAL)
3. `cross_domain.detect_epistemic_overreach` — Detect class promotion, scope expansion across boundaries
4. `cross_domain.trace_cross_domain_provenance` — Trace provenance chains across domain boundaries
5. `cross_domain.enforce_weakest_edge` — Enforce weakest-load-bearing-edge confidence rule
6. `cross_domain.classify_bridge` — Classify bridge type (ANALOGY/ISOMORPHISM/CAUSAL/INFORMATIONAL/STRUCTURAL)
7. `cross_domain.manage_lifecycle` — Manage lifecycle: classify, validate, trace, assess, detect
8. `cross_domain.detect_drift` — Detect drift in cross-domain evidence chains
9. `cross_domain.validate_outputs` — Validate outputs against domain constraints and epistemic class

## Bridge Type Classification

| Bridge Type | Confidence Ceiling | Falsifier |
|-------------|---------------------|-----------|
| ANALOGY | ≤ 0.50 | Domain-specific evidence overrides |
| ISOMORPHISM | ≤ 0.95 | Counterexample in either domain |
| CAUSAL | ≤ 0.80 | Confounder or alternative explanation |
| INFORMATIONAL | ≤ 0.60 | Independent evidence contradicts |
| STRUCTURAL | ≤ 0.55 | Pattern breaks under stress test |

## Cross-Domain Composition Law

```
Compose(T_A, T_B) = PERMITTED
  iff:
    1. All shared axes semantically compatible
    2. Epistemic classes preserved (no promotion)
    3. Confidence ≤ min(load_bearing_premises)
    4. Provenance ⊇ union of input provenance
    5. Scope ⊆ intersection of input scopes
    6. Regime ⊆ intersection of input regimes
    7. Bridge type classified and within ceiling
```

Status: AMOS_MODEL — formalization of the AMOS tensor compatibility invariant.

## 1:1:1 Binding

- **Skill**: `.devin/skills/amos-cross-domain-tensor-composition-governor/SKILL.md`
- **Agent**: `.devin/agents/amos-cross-domain-tensor-composition-governor-agent.json`
- **Workflow**: `.devin/workflows/amos-cross-domain-tensor-composition-governor-workflow.md`

## Validation Gates (10)

- G1 (Law of Law): No contradictions within or across composed domains
- G2 (Epistemic class): All claims labeled, no cross-domain class promotion
- G3 (Provenance): Source path recorded including domain of origin and bridge type
- G4 (Anti-overreach): No claim beyond declared scope
- G5 (Equation firewall): Composition law tagged as AMOS_MODEL
- G6 (Failure mode): Downgrade, flag, escalate on failure
- G7 (Axis compatibility): All shared axes verified before composition
- G8 (Weakest edge): Confidence ≤ weakest load-bearing premise
- G9 (Bridge classification): Explicit bridge type with confidence ceiling
- G10 (Scope intersection): Composed scope ⊆ input scope intersection

## QA Validation

All 10 software-engineering-qa gates pass:
- 1:1:1 binding verified (skill ↔ agent ↔ workflow)
- JSON syntax valid
- 9 unique capabilities, all using `<domain>.<verb>` format
- 10 validation gates in skill, 10 in workflow
- Epistemic class: SOURCE_CLAIM
- Claim ceiling: 0.95
- Failure paths defined in both skill and workflow
- Preconditions present in workflow
- Trigger: 245 chars (≥20 required)
- Status: PRODUCTION_READY

## Provenance

- **Origin architect**: Trang Phan
- **Parent skill**: `amos-rscf-epistemic-master`
- **Domain**: cross-domain
- **Vault sources**: TENSOR_CONTRACTS.md, CLAIM_TENSOR.md, EVIDENCE_TENSOR.md, RELATION_TENSOR.md, 12 domain master knowledge files (C01-C12), AMOS_Full_Brain_OS_Architecture.md, 11_KNOWLEDGE_MOC.md
- **Created**: 2026-08-27
- **Method**: skill-creator + amos-workflow-builder + software-engineering-qa validation

---
**Related:** [[KNOWLEDGE_MOC]] · [[TENSOR_CONTRACTS]] · 11_KNOWLEDGE/CLAIM_TENSOR · 11_KNOWLEDGE/EVIDENCE_TENSOR · 11_KNOWLEDGE/RELATION_TENSOR · [[AMOS_FULL_BRAIN_OS_ARCHITECTURE]]

---
RSCF-NODE
node_id: amos_cross_domain_tensor_composition_governor
node_type: note
path: 11_KNOWLEDGE/AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR.md
RSCF-RELATIONS:
  - INDEXED_BY: [[KNOWLEDGE_MOC]]
  - DEPENDS_ON: [[TENSOR_CONTRACTS]]
  - DEPENDS_ON: 11_KNOWLEDGE/CLAIM_TENSOR
  - DEPENDS_ON: 11_KNOWLEDGE/EVIDENCE_TENSOR
  - DEPENDS_ON: 11_KNOWLEDGE/RELATION_TENSOR
  - DEPENDS_ON: [[AMOS_FULL_BRAIN_OS_ARCHITECTURE]]
claim_class: SOURCE_CLAIM
## Vault Sources Enriched (2026-08-27)

### Fractal Tensor Architecture (Cosmo brain: fractal/FRACTAL.md)

The fractal tensor `T_F` is the primary cross-scale composition mechanism with 12 axes including HML_scale, recursion_depth, pattern_class, boundary, entropy_proxy, lacunarity_proxy.

### Fractal Directory (42 files)

- `FRACTAL.md` — Core fractal reasoning with H/M/L decomposition
- `FRACTAL_RUNTIME.md` — Runtime execution of fractal decomposition
- `AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime.md`
- `Fractal Semantic Intelligence Architecture (FSIA).md`
- `HERITAGE ∅ – 12 LOẠI FRACTAL.md` — 12 fractal types (Vietnamese heritage)
- `FRACTAL ECONOMY.md` — Fractal economics application

### Cognitive Domain Engines (13 engines)

13 Cognitive Stack Engines provide domain-specific reasoning including Deterministic Logic, Signal Processing, Strategy Game, Econ Finance, Physics Cosmos, Society Culture, Biology Cognition, and Design Language engines. 15 Domain Engines provide specialized reasoning across Tech, Science, Org-Risk, and Quantum subsystems.

### Anti-Overreach (from FRACTAL.md)

- repeated pattern != proven fractal dimension
- H/M/L similarity != identical mechanism
- entropy proxy != thermodynamic entropy
- cross-scale analogy != causation

---
**MOC:** [[KNOWLEDGE_MOC]]
