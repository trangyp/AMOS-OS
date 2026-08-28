---
title: "SKILL — Amos C06 Society Culture Master"
type: skill
source: 07_SKILLS/amos-c06-society-culture-master
name: amos-c06-society-culture-master
description: "AMOS C06 Society & Culture — social dynamics, cultural analysis, Vietnamese language/regional analysis, linguistic patterns, anthropology. Use for social analysis, cultural reasoning, or Vietnamese..."
parent_skill: none
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-c06-society-culture-master, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# AMOS C06 — Society & Culture Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 17 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 17 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (content_hash: 6277c28f48ab4433)).

## When to Use

- When analyzing social dynamics, power structures, or collective action patterns
- When performing cultural analysis, linguistic pattern analysis, or anthropological reasoning
- When analyzing Vietnamese language/regional patterns and heritage
- When mapping institutional incentives and cultural codes in conflicts
- When a child skill routes a social, cultural, or anthropological task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c06_society_culture.analyze_social**: Analyze AMOS C06 Society & Culture social dynamics: power structures, collective action, institutional governance, cultural patterns.
- **c06_society_culture.validate_social**: Validate AMOS C06 Society & Culture social claims for epistemic class, cultural specificity vs universal, and scope regime.
- **c06_society_culture.analyze_cultural**: Analyze AMOS C06 Society & Culture cultural patterns: linguistic structures, regional systems, and anthropological models.
- **c06_society_culture.trace_social_provenance**: Trace AMOS C06 Society & Culture social findings to vault sources, cultural analysis, and regional evidence.
- **c06_society_culture.assess_social_claim**: Assess AMOS C06 Society & Culture social claims for cultural specificity, evidence strength, and overclaim risk.
- **c06_society_culture.manage_social_lifecycle**: Manage AMOS C06 Society & Culture social lifecycle: observe, analyze, model, validate, and finalize.
- **c06_society_culture.detect_social_drift**: Detect social drift: cultural shift, regime change, institutional evolution, and evidence decay.
- **c06_society_culture.escalate_social_gaps**: Escalate AMOS C06 Society & Culture social gaps: flag cultural overclaim, require regional evidence, trigger repair.
- **c06_society_culture.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **c06_society_culture.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **c06_society_culture.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (content_hash: 6277c28f48ab4433) (vault canon, SOURCE_CLAIM)

### Source Family Mapping

The domain is organized into source families:

- **F01**: Political dynamics and power
- **F02**: Institutions and governance
- **F03**: Social networks and collective action
- **F04**: Culture, ritual, and transmission
- **F05**: Conflict, cooperation, and change
- **F06**: Ethics, fairness, and consent
- **F07**: Vietnam regional systems
- **F08**: Monitoring and social data
- **F09**: Scenarios, policy, and intervention
- **F10**: Meta-society research bridge

### Major Knowledge Modules

- H1: Political Dynamics, Power & Conflict — political dynamics kernel, power, conflict/cooperation
- H2: Institutions & Governance — state capacity, common-pool resources
- H3: Social Networks & Collective Action — network structure, diffusion, collective action
- H4: Culture, Ritual & Transmission — Vietnamese cultural ritual energy (gia hệ) [MODEL]
- H5: Social Change, Stability & Regime Dynamics — change and stability

### Epistemic Classification

- **Conclusion class**: MIXED (established science + model projections + AMOS synthesis)
- **Evidence policy**: typed_per_node (each claim carries its own evidence type)
- **Canon status**: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
- **Architecture**: HML_fractal_single_file (H/M/L cross-scale reasoning)

### Epistemic Boundary

Social analysis is always context-, population-, institution-, and timescale-dependent. Contested sociological claims are COMPETING-tagged. Political analysis must remain descriptive unless prescription is explicitly framed. Alternative interpretations REQUIR
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-c06-society-culture-master_MOC]]

## Examples

- **Scenario**: When analyzing social dynamics, power structures, or collective action patterns
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When performing cultural analysis, linguistic pattern analysis, or anthropological reasoning
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing Vietnamese language/regional patterns and heritage
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c06 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when c06 specialization is needed
- **Peers**: Other skills in the `c06` domain may be composed in sequence
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

- `references/cci_official_manual.md` — loaded on demand
- `references/china_engines_model.md` — loaded on demand
- `references/cultural_bifurcation_emotion_logic.md` — loaded on demand
- `references/dignity.md` — loaded on demand
- `references/domain_config.md` — loaded on demand
- `references/humanity_ice_age_to_present.md` — loaded on demand
- `references/marketing_gtm_kernel.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/society_culture_engine_cognitive.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `references/vietnam_engine_layer.md` — loaded on demand
- `references/vietnam_engines_model.md` — loaded on demand
- `references/vietnam_environment_report.md` — loaded on demand
- `references/vietnamese_fractal_logic_analysis.md` — loaded on demand
- `references/vietnamese_writing_engine.md` — loaded on demand
- `references/vietnamese_writing_model.md` — loaded on demand
- `references/vn_absolute_architecture.md` — loaded on demand
- `references/vn_governance_politics_pack.md` — loaded on demand
- `references/vn_labor_shortage_report.md` — loaded on demand
- `references/vn_marketing_strategy.md` — loaded on demand
- `references/vn_omnistructure_clean_engine.md` — loaded on demand
- `references/vn_omnistructure_engine.md` — loaded on demand
- `references/vn_omnistructure_model.md` — loaded on demand
- `references/vn_trust_marketplace_strategy.md` — loaded on demand
- `references/when_humanity_began.md` — loaded on demand
- `[[amos-c06-society-culture-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-c06-society-culture-master-workflow]]` — corresponding workflow
- `amos-c06-society-culture-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c06-society-culture-master
node_type: skill
path: 07_SKILLS/amos-c06-society-culture-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
