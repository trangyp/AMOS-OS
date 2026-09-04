---
schema_version: 1.0
title: SKILL — Amos Skill Builder
type: skill
source: 07_SKILLS/amos-skill-builder
name: amos-skill-builder
description: Build, update, audit, and package advanced AMOS/COSMO/Trang ChatGPT Skills from capability gaps, source canon, existing Skills, engine/runtime specifications, repositories, or research evidence. Use when creating a new AMOS-aligned Skill, strengthening a thin or vault-dump Skill, converting an AMOS engine/spec into an operational Skill, checking routing and parent integration, separating SOURCE_CANON/SOURCE_CLAIM from AMOS_MODEL and empirical claims, adding RSCF/HML/provenance/governance controls, validating progressive loading and anti-overreach, or preparing a complete installable Skill bundle. This is the AMOS-specialized Skill factory; do not use it as a generic replacement for ordinary non-AMOS Skill creation.
parent_skill: none
domain: skill
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
  - type/skill
  - type/skill
  - domain/skill-systems
  - epistemic/source_claim
  - hml/m
  - epistemic/source_canon
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
license: MIT
steward: Trang Phan
---

# AMOS Skill Builder

## Identity

Origin architect: **Trang Phan**. Domain: skill. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.

## When to Use

Use this skill when creating, upgrading, auditing, or packaging AMOS/COSMO/Trang Skills. Covers skill frontmatter validation, epistemic firewall enforcement, H/M/L integrity levels, RSCF integration, parent/child routing, capability naming, content hash verification, and 1:1:1 binding (skill→agent→workflow). Use when filling placeholder skills, merging skills, or validating skill corpus integrity.

Operate as the AMOS-specialized factory for creating, upgrading, auditing, and packaging Skills belonging to the AMOS / COSMO / Trang architecture family.

Treat this Skill as a build-and-governance layer, not as proof that source frameworks are empirically true.

Use the weakest accurate epistemic class:

`SOURCE_CANON | SOURCE_CLAIM | OBSERVATION | DERIVED | AMOS_MODEL | DOMAIN_EMPIRICAL | VERIFIED | CONDITIONAL | COMPETING | UNKNOWN/GAP`

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **skill_builder.execute_runtime**: Execute the Skill Builder runtime function: manage typed state, pipeline stages, and infrastructure control plane operations.
- **skill_builder.validate_runtime**: Validate Skill Builder outputs against authority gates, capability bounds, scope regime, and runtime invariants.
- **skill_builder.analyze_runtime**: Analyze Skill Builder pipeline structure, dependency graph, state transitions, and execution trace for completeness.
- **skill_builder.trace_skill_provenance**: Trace skill provenance to vault sources, parent skills, and origin architect decisions
- **skill_builder.assess_skill_claim**: Assess skill claims: epistemic class, evidence strength, and scope validity
- **skill_builder.manage_lifecycle**: Manage Skill Builder lifecycle: initialize, execute pipeline, checkpoint state, recover from failure, finalize.
- **skill_builder.detect_drift**: Detect runtime drift: state staleness, authority decay, scope creep, and pipeline degradation over time.
- **skill_builder.escalate_gaps**: Escalate Skill Builder runtime gaps: flag UNKNOWN/GAP states, downgrade confidence, trigger bounded repair.
  Core Objective

Create Skills that are:

- triggerable
- source-faithful
- operational rather than descriptive
- compact at the entrypoint
- progressively loadable
- provenance-preserving
- scope/regime bounded
- contradiction-visible
- composable with parent/child AMOS Skills
- explicit about AMOS_MODEL versus empirical claims
- testable and package-ready

Never convert a large vault dump directly into `SKILL.md` unless every section is required at runtime.

- **skill_builder.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **skill_builder.execute_runtime**: Execute the Skill Builder runtime function: manage typed state, pipeline stages, and infrastructure control plane operations.
1. **skill_builder.validate_runtime**: Validate Skill Builder outputs against authority gates, capability bounds, scope regime, and runtime invariants.
1. **skill_builder.analyze_runtime**: Analyze Skill Builder pipeline structure, dependency graph, state transitions, and execution trace for completeness.
1. **skill_builder.trace_skill_provenance**: Trace skill provenance to vault sources, parent skills, and origin architect decisions
1. **skill_builder.assess_skill_claim**: Assess skill claims: epistemic class, evidence strength, and scope validity
1. **skill_builder.manage_lifecycle**: Manage Skill Builder lifecycle: initialize, execute pipeline, checkpoint state, recover from failure, finalize.
1. **skill_builder.detect_drift**: Detect runtime drift: state staleness, authority decay, scope creep, and pipeline degradation over time.
1. **skill_builder.escalate_gaps**: Escalate Skill Builder runtime gaps: flag UNKNOWN/GAP states, downgrade confidence, trigger bounded repair. Core Objective
1. triggerable
1. source-faithful
1. operational rather than descriptive
1. compact at the entrypoint
1. progressively loadable
1. provenance-preserving
1. scope/regime bounded
1. contradiction-visible
1. composable with parent/child AMOS Skills
1. explicit about AMOS_MODEL versus empirical claims
1. testable and package-ready
1. **skill_builder.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Runtime

Apply:

`ORIENT -> GAP -> SOURCE -> ARCHITECT -> BUILD -> INTEGRATE -> CHALLENGE -> VALIDATE -> PACKAGE`

Load:

- `references/workflows.md` (content_hash: 1d4e6b352bf42ccb) for creation/update workflows
- `references/validation.md` (content_hash: c26579b18828d39e) for hard gates
- `references/integration.md` (content_hash: 5ef98902570687a9) for AMOS routing, parent/child, RSCF, H/M/L, and provenance contracts

Use the smallest sufficient proof and build scope.

## ORIENT

Resolve:

- requested Skill name or capability
- CREATE, UPDATE, AUDIT, REPAIR, or PACKAGE
- intended parent Skill
- domain
- expected inputs
- expected outputs
- required connectors/tools
- authoritative source corpus
- whether empirical validation is part of the Skill's purpose
- whether scripts/resources/assets materially improve reliability

Do not ask again for information already available from the request, source bundle, repository, or existing Skill.

If intended usage is already clear, proceed.

## GAP

Before creating a new AMOS Skill, determine whether the capability already exists.

Check when available:

1. installed Skill registry
1. declared pa

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-skill-builder/amos-skill-builder_MOC|amos-skill-builder_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect

  - **Input**: A query matching this skill's domain (skill)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration

  - **Input**: A query matching this skill's domain (skill)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class

  - **Input**: A query matching this skill's domain (skill)
  - **Output**: Structured result with epistemic labels and provenance

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the skill domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `none` — routes to this skill when skill specialization is needed
- **Peers**: Other skills in the `skill` domain may be composed in sequence
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

- For generic analysis outside the skill framework
- To claim empirical validation without domain-specific evidence
- As a substitute for domain-specific evidence
- Outside skill domain reasoning

## References

- `references/canon.md` — loaded on demand
- `references/integration.md` — loaded on demand
- `references/output-patterns.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/validation.md` — loaded on demand
- `references/workflows.md` — loaded on demand
- \`\` — skill Map of Content
- `none` — parent skill
- \`\` — corresponding workflow
- `amos-skill-builder-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-skill-builder
node_type: skill
path: 07_SKILLS/amos-skill-builder/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
