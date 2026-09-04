---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: electrical power model
type: reference
source: 07_SKILLS/amos-c12-earth-ecology-master/references
tags:
  - reference
  - amos-c12-earth-ecology-master
  - type/skill
  - system-scan-agent
  - automation-profiles
  - amos-simulation-kernel-v0-math-foundations
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Electrical Power Model

> Source: `_00_Cosmo brain/models/Electrical_Power_Model.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## aliases: [Electrical Power Engine, AMOS_Electrical_Power] tags: [canon-group/tech-ai, canon/model, rscf/claim, rscf/provenance, rscf/state/derived, topic/electrical-power-model, models]

## AMOS Electrical Power Engine

**Version:** vInfinity_MAX
**Source:** `AMOS_Electrical_Power_Engine_v0.json`

The **Electrical Power Engine** models physics, grids, markets, safety, and EV infrastructure systems.

## Kernel Modules

1. **Physical Foundations:** Maxwell's equations (power frequency), Ohm's law, Kirchhoff's laws, power relations (P, Q, S, pf), impedance/admittance.
1. **System Representations:** Single line diagrams (SLD), per-unit systems, phasor and sequence components.
1. **Mathematical Models:** Steady state (AC/DC load flow), dynamic/transient (short circuit, stability, harmonics), and probabilistic (SAIDI, Monte Carlo).
1. **Safety & Risk:** Electric shock, arc flash, thermal overload, cyber-physical risks.
1. **Standards & Regulation:** IEC, IEEE, CIGRE, NFPA, ISO. Never assume jurisdictional rules.

## Core Capabilities

- Designing and evaluating power system topologies (LV networks, industrial grids, microgrids).
- EV infrastructure network planning (AC/DC mixing, demand profiling, peak shaving).
- Reviewing SLDs and specifying electrical equipment constraints.
- Drafting specifications and translating technical results for executives/regulators.

## Constraints

- Never give safety-critical guidance without clear caveats.
- Always ask for missing data (especially in protection settings).
- Do not fabricate standards or regulations.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-c12-earth-ecology-master-electrical-power-model
node_type: reference
path: 07_SKILLS/amos-c12-earth-ecology-master/references/electrical_power_model.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
