---
title: SKILL
type: skill
name: amos-workflow-builder
description: Build, update, audit, and package advanced AMOS/COSMO/Trang ChatGPT Workflows from capability gaps, existing skills, agent bindings, engine/runtime specifications, or operational sequences. Use when creating a new AMOS-aligned Workflow, strengthening a thin workflow, converting an AMOS engine/spec into an operational workflow, checking agent-skill-workflow routing, separating operational steps from validation gates, adding RSCF/HML/provenance/governance controls, validating step ordering and gate enforcement, or preparing a complete installable workflow bundle. This is the AMOS-specialized Workflow factory; do not use it as a generic replacement for ordinary non-AMOS workflow creation.
parent_skill: none
domain: workflow
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-workflow-builder]
---


# AMOS Workflow Builder

## Identity

Origin architect and steward: **Trang Phan**.

## When to Use

Use this skill when creating, updating, auditing, or packaging AMOS-aligned Workflows. Covers workflow step sequencing, validation gate enforcement (G1-G10), failure path specification, 1:1:1 binding (workflow→agent→skill), RSCF/HML/provenance/governance controls, trigger definition, and provenance recording. Use when converting engine specs into operational workflows or strengthening thin workflows.

Operate as the AMOS-specialized factory for creating, upgrading, auditing, and packaging Workflows belonging to the AMOS / COSMO / Trang architecture family.

Treat this Skill as a build-and-governance layer, not as proof that source frameworks are empirically true.

Use the weakest accurate epistemic class:

`SOURCE_CANON | SOURCE_CLAIM | OBSERVATION | DERIVED | AMOS_MODEL | DOMAIN_EMPIRICAL | VERIFIED | CONDITIONAL | COMPETING | UNKNOWN/GAP`
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **workflow.design**: Design a governed workflow graph from objective, steps, contracts, dependencies, gates, authority, retries, compensation, and rollback.
- **workflow.validate_topology**: Validate workflow topology, gates, contracts, authority boundaries, and cycles
- **workflow.analyze**: Analyze workflow topology, critical path, fan-out, fan-in, risk concentration, authority surface, failure propagation, and repair targets.
- **workflow.manage_lifecycle**: Manage workflow lifecycle: plan execution frontier, stage step execution under authority, checkpoint, recover from valid checkpoints, compensate completed durable steps after partial failure, and package validated workflow definitions.
- **workflow.detect_drift**: Detect workflow scope, dependency, authority, schema, environment, provenance, and confidence drift.
- **workflow.trace_workflow_provenance**: Trace workflow provenance to skills, agents, and vault sources
- **workflow.assess_workflow_claim**: Assess workflow claims: gate enforcement, step ordering, and promotion readiness
- **workflow.escalate_gaps**: Classify workflow gaps and escalate blocking unknowns.
 Core Objective

Create Workflows that are:

- triggerable
- source-faithful
- operational rather than descriptive
- compact at the entrypoint
- progressively loadable
- provenance-preserving
- scope/regime bounded
- contradiction-visible
- composable with parent/child AMOS Workflows
- explicit about AMOS_MODEL versus empirical claims
- testable and package-ready
- agent-bound (every workflow binds to exactly one agent)
- skill-bound (every workflow binds to exactly one skill)
- gate-enforced (every step has a validation gate)

Never convert a large vault dump directly into a workflow unless every step is required at runtime.
- **workflow.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Runtime

Apply:

`ORIENT -> GAP -> SOURCE -> ARCHITECT -> BUILD -> INTEGRATE -> CHALLENGE -> VALIDATE -> PACKAGE`

Load:

- `references/workflows.md` (content_hash: 96d94a2d2c10f977) for creation/update workflows
- `references/validation.md` (content_hash: f2ff778a23622064) for hard gates
- `references/integration.md` (content_hash: b0910ef0e01ce315) for AMOS routing, agent/skill binding, RSCF, H/M/L, and provenance contracts

Use the smallest sufficient proof and build scope.

## ORIENT

Resolve:

- requested Workflow name or capability
- CREATE, UPDATE, AUDIT, REPAIR, or PACKAGE
- intended parent Workflow
- domain
- bound agent (1:1)
- bound skill (1:1)
- expected trigger
- expected inputs
- expected outputs
- required validation gates
- authoritative source corpus
- whether empirical validation is part of the Workflow's purpose
- whether scripts/resources/assets materially improve reliability

Do not ask again for information already available from the request, source bundle, repository,