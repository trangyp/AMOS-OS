---
schema_version: 1.0
title: SKILL — Amos Economic Model
type: skill
source: 07_SKILLS/amos-economic-model
name: amos-economic-model
description: Economic Model — econ capability. Use when executing the core capability
  within this domain. Use when amos-c07-econ-finance-master routes to this specialized
  capability. Do not use for generic tasks outside econ domain.
parent_skill: amos-c07-econ-finance-master
domain: econ
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/econ-finance
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L6_uncertainty
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L6
- L16
- L17
license: MIT
steward: Trang Phan
---

# Economic Model

## Identity

Origin architect: **Trang Phan**. Domain: econ. Parent: amos-c07-econ-finance-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When governing agent economy: constitutional rules, monetary policy
- When modeling economic dynamics: supply, demand, price formation
- When assessing future debt and option value: intertemporal tradeoffs
- When the parent skill (`amos-c07-econ-finance-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **economic_model.govern_economy**: Govern agent economy: constitutional rules, monetary policy, and allocation
- **economic_model.model_economic**: Model economic dynamics: supply, demand, price formation, and equilibrium
- **economic_model.assess_debt**: Assess future debt and option value: intertemporal tradeoffs and commitments
- **economic_model.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **economic_model.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **economic_model.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d865f64cecd4214a) for the full vault-sourced domain knowledge (6420 chars).

## Operations

1. **economic_model.govern_economy**: Govern agent economy: constitutional rules, monetary policy, and allocation
2. **economic_model.model_economic**: Model economic dynamics: supply, demand, price formation, and equilibrium
3. **economic_model.assess_debt**: Assess future debt and option value: intertemporal tradeoffs and commitments
4. **economic_model.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
5. **economic_model.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
6. **economic_model.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/economy/Econ_Finance_Model.md` (content_hash: c5bb82643b0856ff) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### Economic Model

From Cosmo Brain AMOS Economics & Finance Engine (vInfinity.1.0.0): Models firm behavior, macroeconomic cycles, public finance policy, and financial market risk.

**4 Core Sub-Kernels**:
1. **Microeconomics Kernel**: models preferences, constraints, technology, and market equilibria for firms and households
2. **Macroeconomics Kernel**: models the output gap, policy rates, expectations, and exogenous shocks affecting growth and inflation
3. **Public Finance Kernel**: tracks revenue, transfers, deficits, and intergenerational burdens for taxes and welfare
4. **Financial System Kernel**: models assets, liabilities, leverage, liquidity, and default risk in banks and capital markets

**3 Applied Engines**:
- **Sector Modelling Engine**: maps demand/supply profiles and shock propagation across sectors, connecting micro to macro impacts
- **Financial Risk Scenario Engine**: generates loss distributions and stress test results, highlighting tail risks
- **Policy Tradeoff Engine**: frames policy decisions as optimizations, extracting the Pareto frontier and mapping stakeholder impact

**3 Constraints**:
1. Never provide personalized investment advice
2. Flag high uncertainty for long-horizon economic forecasts
3. Avoid recommending illegal financial behaviour or market manipulation

**Economic model laws**:
- `MODEL != REALITY`: the economic model is an approximation; it is not the real economy
- `FORECAST != PREDICTION**: a forecast is a scenario projection; a prediction is a definite claim
- `EQUILIBRIUM != STABILITY**: equilibrium is a balance of forces; stability is resistance to perturbation

### Epistemic Boundary

Economic model is an AMOS_MODEL. It does not prove economic predictions are accurate, that the 4 sub-kernels are exhaustive, or that the model captures all economic dynamics.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evid

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-economic-model/amos-economic-model_MOC|amos-economic-model_MOC]]

## Examples

- **Scenario**: When governing agent economy: constitutional rules, monetary policy
  - **Input**: A query matching this skill's domain (econ)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling economic dynamics: supply, demand, price formation
  - **Input**: A query matching this skill's domain (econ)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing future debt and option value: intertemporal tradeoffs
  - **Input**: A query matching this skill's domain (econ)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the econ domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c07-econ-finance-master` — routes to this skill when econ specialization is needed
- **Peers**: Other skills in the `econ` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic economic analysis outside the econ/finance framework
- To claim empirical validation of economic laws or market dynamics
- As a substitute for domain-specific economic or financial evidence
- Outside econ/finance domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c07-econ-finance-master` — parent skill
- `` — corresponding workflow
- `amos-economic-model-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-economic-model
node_type: skill
path: 07_SKILLS/amos-economic-model/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
