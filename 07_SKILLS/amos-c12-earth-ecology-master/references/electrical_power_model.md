---
title: electrical power model
type: reference
source: 07_SKILLS/amos-c12-earth-ecology-master/references
tags: [reference, amos-c12-earth-ecology-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Electrical Power Model

> Source: `_00_Cosmo brain/models/Electrical_Power_Model.md`
> Epistemic class: SOURCE_DERIVED

---
aliases: [Electrical Power Engine, AMOS_Electrical_Power]
tags: [canon-group/tech-ai, canon/model, rscf/claim, rscf/provenance, rscf/state/derived, topic/electrical-power-model, models]
---

# AMOS Electrical Power Engine

**Version:** vInfinity_MAX
**Source:** `AMOS_Electrical_Power_Engine_v0.json`

The **Electrical Power Engine** models physics, grids, markets, safety, and EV infrastructure systems.

## Kernel Modules
1. **Physical Foundations:** Maxwell's equations (power frequency), Ohm's law, Kirchhoff's laws, power relations (P, Q, S, pf), impedance/admittance.
2. **System Representations:** Single line diagrams (SLD), per-unit systems, phasor and sequence components.
3. **Mathematical Models:** Steady state (AC/DC load flow), dynamic/transient (short circuit, stability, harmonics), and probabilistic (SAIDI, Monte Carlo).
4. **Safety & Risk:** Electric shock, arc flash, thermal overload, cyber-physical risks.
5. **Standards & Regulation:** IEC, IEEE, CIGRE, NFPA, ISO. Never assume jurisdictional rules.

## Core Capabilities
- Designing and evaluating power system topologies (LV networks, industrial grids, microgrids).
- EV infrastructure network planning (AC/DC mixing, demand profiling, peak shaving).
- Reviewing SLDs and specifying electrical equipment constraints.
- Drafting specifications and translating technical results for executives/regulators.

## Constraints
- Never give safety-critical guidance without clear caveats.
- Always ask for missing data (especially in protection settings).
- Do not fabricate standards or regulations.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[references_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c12-earth-ecology-master-electrical-power-model
node_type: reference
path: 07_SKILLS/amos-c12-earth-ecology-master/references/electrical_power_model.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
