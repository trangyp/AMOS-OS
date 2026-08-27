---
title: SKILL
type: skill
name: amos-memory-systems-master
description: AMOS Memory Systems — 3 memory types, context compaction, memory conflict resolution, memory immune system, action-memory firewall. Use for memory management, context continuity, or memory conflict...
parent_skill: none
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-memory-systems-master]
---

# MEMORY README

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 3 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 3 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `10_MEMORY/MEMORY_README.md`).

## When to Use

AMOS Memory Systems — 3 memory types, context compaction, memory conflict resolution, memory immune system, action-memory firewall. Use for memory management, context continuity, or memory conflict...
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **memory_systems.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Memory Systems consent, provenance, and risk gates.
- **memory_systems.validate_gates**: Validate AMOS Memory Systems decisions against hard partition gates, epistemic class preservation, and consent state requirements.
- **memory_systems.analyze_state**: Analyze AMOS Memory Systems memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
- **memory_systems.trace_provenance**: Trace AMOS Memory Systems memory entries to source, encoding operation, consolidation history, and field-level lineage.
- **memory_systems.assess_claim**: Assess AMOS Memory Systems memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
- **memory_systems.manage_lifecycle**: Manage AMOS Memory Systems lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
- **memory_systems.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
- **memory_systems.escalate_gaps**: Escalate AMOS Memory Systems memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
- **memory_systems.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (3)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## Vault-Sourced Domain Knowledge

> **Source**: `10_MEMORY/MEMORY_README.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# MEMORY README

## Purpose
`MEMORY README` is the package readme for the **Memory** plane segment at `10_MEMORY`.
The Memory plane governs durable memory stores, trust classes, admission, retrieval, and conflict policy. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[MEMORY_MEMORY_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics
Given an operation touching `MEMORY · README` within the Memory plane:
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

## Cross-plane bindings
- Governed by canon — [[LAW_HIERARCHY|AMOS Core Laws]] · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — OPERATI
- [[AGENT_TEMPLATE]]
