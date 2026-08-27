---
title: SKILL
type: skill
name: amos-agent-systems-master
description: AMOS Agent Systems — agent fabrication, delegation, agency-consequence tensors, agent economy governance, agent-to-agent protocols. Use for agent design, delegation reasoning, or multi-agent govern...
parent_skill: none
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-agent-systems-master]
---

# AGENTS README

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 11 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 11 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `06_AGENTS/AGENTS_README.md`).

## When to Use

AMOS Agent Systems — agent fabrication, delegation, agency-consequence tensors, agent economy governance, agent-to-agent protocols. Use for agent design, delegation reasoning, or multi-agent govern...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **agent_systems.fabricate_agent**: Fabricate agents with proper schema: capabilities, side-effect classification, governance metadata, and content hash.
- **agent_systems.delegate_task**: Delegate tasks to subordinate agents with scope bounds, authority gates, and consequence tensor tracking.
- **agent_systems.validate_agent_composition**: Validate agent composition: MECE coverage, skill binding integrity, capability bounds, and governance metadata.
- **agent_systems.trace_agent_provenance**: Trace agent capabilities, content, and delegation chain to source skills and vault provenance.
- **agent_systems.assess_agent_claim**: Assess agent claims for epistemic class, capability scope, authority bounds, and lifecycle status.
- **agent_systems.manage_agent_lifecycle**: Manage agent lifecycle: fabricate, activate, promote, retire, and archive with provenance tracking.
- **agent_systems.detect_agent_drift**: Detect agent drift: capability creep, scope expansion, governance decay, and content hash tampering.
- **agent_systems.escalate_agent_gaps**: Escalate agent gaps: flag orphan agents, broken skill bindings, missing capabilities, trigger repair.
- **agent_systems.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agent_systems.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agent_systems.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (11)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## Vault-Sourced Domain Knowledge

> **Source**: `06_AGENTS/AGENTS_README.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# AGENTS README

## Purpose
`AGENTS README` is the package readme for the **Agents** plane segment at `06_AGENTS`.
The Agents plane governs agent specifications, capability envelopes, and delegation boundaries. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[AGENTS_AGENT_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics
Given an operation touching `AGENTS README` within the Agents plane:
1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane binding
- [[AGENT_TEMPLATE]]
