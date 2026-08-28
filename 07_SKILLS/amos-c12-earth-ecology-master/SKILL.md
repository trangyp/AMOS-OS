---
title: SKILL — Amos C12 Earth Ecology Master
type: skill
source: 07_SKILLS/amos-c12-earth-ecology-master
name: amos-c12-earth-ecology-master
description: AMOS C12 Earth & Ecology — climate, environment, hydro energy, EV infrastructure, electrical
  power, hydrogen, battery systems, solar, wind, green tech. Use for environmental analysis, energy system...
parent_skill: none
domain: c12
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/earth-ecology
- rscf/source_claim
- hml/m
- epistemic/source_canon
- amos_os
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
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
---








# AMOS C12 — Earth & Ecology Master Knowledge

## Identity

Origin architect: **Trang Phan**. Domain: c12. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.
## When to Use

AMOS C12 Earth & Ecology — climate, environment, hydro energy, EV infrastructure, electrical power, hydrogen, battery systems, solar, wind, green tech. Use for environmental analysis, energy system...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c12_earth_ecology.execute_engineering**: Execute AMOS C12 Earth & Ecology engineering design: software architecture, system implementation with fractal principles.
- **c12_earth_ecology.validate_architecture**: Validate AMOS C12 Earth & Ecology technical architecture for integrity, scalability, maintainability, and invariants.
- **c12_earth_ecology.analyze_code**: Analyze AMOS C12 Earth & Ecology code quality: design patterns, implementation correctness, and provenance requirements.
- **c12_earth_ecology.trace_tech_provenance**: Trace AMOS C12 Earth & Ecology technical outputs to design specs, code sources, and engineering standards.
- **c12_earth_ecology.assess_tech_claim**: Assess AMOS C12 Earth & Ecology technical claims for architecture validity, test coverage, and compliance.
- **c12_earth_ecology.manage_tech_lifecycle**: Manage AMOS C12 Earth & Ecology engineering lifecycle: design, implement, test, deploy, and maintain.
- **c12_earth_ecology.detect_tech_drift**: Detect technical drift: architecture decay, code degradation, test erosion, and dependency rot.
- **c12_earth_ecology.escalate_tech_gaps**: Escalate AMOS C12 Earth & Ecology technical gaps: flag architecture violations, require refactoring, trigger repair.
- **c12_earth_ecology.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **c12_earth_ecology.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **c12_earth_ecology.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (29)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 9 more sub-skills.*

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE.md` (content_hash: 5230c3adc3f51a91) (vault canon, SOURCE_CLAIM)

### 10-Source Family Mapping

The C12 Earth & Ecology domain is organized into 10 source families:

| Family | Focus |
|--------|-------|
| F01 | System mapping — Earth as coupled system |
| F02 | Climate dynamics — energy balance, carbon cycle, greenhouse effect |
| F03 | Ecology and biodiversity — species interactions, disturbance ecology |
| F04 | Food, water, health — food-system structure, soil, freshwater |
| F05 | Land and ocean use — land cover, ocean systems, cryosphere |
| F06 | Risk and tipping points — thresholds, compound events, cascades |
| F07 | Scenarios and policy — emissions scenarios, adaptation, mitigation |
| F08 | Monitoring and data — observation systems, indicators, uncertainty |
| F09 | Infrastructure and design — energy systems, EV, hydrogen, solar, wind |
| F10 | Meta-ecology governance — planetary boundaries, earth system governance |

### Major Knowledge Modules

- **M1: Earth as Coupled System** — subsystems, stocks/flows, conservation, feedback
- **M2: Planetary Energy Balance** — radiation, radiative forcing, climate sensitivity
- **M3: Carbon Cycle** — reservoirs, fluxes, anthropogenic perturbation
- **M4: Water Cycle** — atmosphere, oceans, cryosphere, sea-level change
- **M5: Nutrient Cycles** — nitrogen, phosphorus, biogeochemical cycles
- **Ecological Organization** — populations, communities, ecosystems, biodiversity
- **Disturbance Ecology** — fire, invasive species, regime shifts
- **Food-System Structure** — production, distribution, sustainability
- **Risk and Tipping Points** — thresholds, cascading failures, compound events

### Epistemic Classification

- **Conclusion class**: MIXED (established scienc
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-c12-earth-ecology-master_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect
  - **Input**: A query matching this skill's domain (c12)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration
  - **Input**: A query matching this skill's domain (c12)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (c12)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c12 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when c12 specialization is needed
- **Peers**: Other skills in the `c12` domain may be composed in sequence
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


## References

- `references/c12_earth_ecology_super_full.md` — loaded on demand
- `references/civilization_fails_energy_transition.md` — loaded on demand
- `references/domain_config.md` — loaded on demand
- `references/drive_quantum_restoration.md` — loaded on demand
- `references/electrical_power_engine_cognitive.md` — loaded on demand
- `references/electrical_power_engine_layer.md` — loaded on demand
- `references/electrical_power_model.md` — loaded on demand
- `references/energy_architecture.md` — loaded on demand
- `references/energy_eroi_carbon_scoring.md` — loaded on demand
- `references/energy_integrity_law.md` — loaded on demand
- `references/energy_justice_cannot_be_priced.md` — loaded on demand
- `references/energy_os.md` — loaded on demand
- `references/energy_pricing_moral_accounting.md` — loaded on demand
- `references/energy_reader.md` — loaded on demand
- `references/ev_kernel_layer.md` — loaded on demand
- `references/ev_super_engine.md` — loaded on demand
- `references/hydro_production_system.md` — loaded on demand
- `references/hydrogen_governance_test.md` — loaded on demand
- `references/hydrogen_offshore_energy_safety.md` — loaded on demand
- `references/hydrogen_powerful_energy_vector.md` — loaded on demand
- `references/hydrogen_vs_batteries_safety_math.md` — loaded on demand
- `references/integrity_bounded_energy_standard.md` — loaded on demand
- `references/nui_cam_planetary_energy_node.md` — loaded on demand
- `references/qls_abi_longevity.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `references/vn_driver_charging_engine.md` — loaded on demand
- `references/vn_ev_baojun_collaboration.md` — loaded on demand
- `references/vn_ev_china_market_analysis.md` — loaded on demand
- `references/vn_ev_china_trend_strategy.md` — loaded on demand
- `references/vn_ev_unitax_100_vehicles.md` — loaded on demand
- `[[amos-c12-earth-ecology-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-c12-earth-ecology-master-workflow]]` — corresponding workflow
- `amos-c12-earth-ecology-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c12-earth-ecology-master
node_type: skill
path: 07_SKILLS/amos-c12-earth-ecology-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
