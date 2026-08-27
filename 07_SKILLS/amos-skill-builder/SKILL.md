---
title: SKILL
type: skill
name: amos-skill-builder
description: Build, update, audit, and package advanced AMOS/COSMO/Trang ChatGPT Skills from capability gaps, source canon, existing Skills, engine/runtime specifications, repositories, or research evidence. Use when creating a new AMOS-aligned Skill, strengthening a thin or vault-dump Skill, converting an AMOS engine/spec into an operational Skill, checking routing and parent integration, separating SOURCE_CANON/SOURCE_CLAIM from AMOS_MODEL and empirical claims, adding RSCF/HML/provenance/governance controls, validating progressive loading and anti-overreach, or preparing a complete installable Skill bundle. This is the AMOS-specialized Skill factory; do not use it as a generic replacement for ordinary non-AMOS Skill creation.
parent_skill: none
domain: skill
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-skill-builder]
---


# AMOS Skill Builder

## Identity

Origin architect and steward: **Trang Phan**.

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
2. declared pa

---
**Links:** [[07_SKILLS_MOC]]
