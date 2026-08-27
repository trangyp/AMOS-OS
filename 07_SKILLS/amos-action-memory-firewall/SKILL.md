---
title: SKILL
type: skill
name: amos-action-memory-firewall
description: Action Memory Firewall — memory systems capability. Use when memory management, context continuity, or memory conflict resolution. Use when amos-memory-systems-master routes to this specialized capability.
parent_skill: amos-memory-systems-master
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-action-memory-firewall]
---


# Action Memory Firewall

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-memory-systems-master`
- **Domain**: memory
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Memory system engine for Action Memory Firewall

## When to Use

- When managing memory: storage, retrieval, decay, consolidation
- When resolving memory conflicts: contradictions, staleness, priority
- When enforcing memory firewall: preventing unauthorized access
- When tracking memory dynamics: formation, consolidation, forgetting
- When the parent skill (`amos-memory-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **memory.evaluate_influence_request**: Evaluate a memory-influence request against the 13-axis coupling tensor (action, tool, parameter, memory_id, memory_type, source_context, destination_context, personalizable, consent_state, stakes, irreversibility, provenance, uncertainty) to determine whether memory may influence a pending action.
- **memory.enforce_hard_gates**: Enforce hard partition gates: DATA_FLOW != AUTHORITY_FLOW, EVIDENCE_FLOW != EFFECT_PERMISSION, TOOL_OUTPUT != ACCEPTED_KNOWLEDGE, MODEL_PROPOSAL != COMMITTED_ACTION. Block memory influence that crosses action/authority/effect boundaries.
- **memory.preserve_epistemic_class**: Preserve epistemic class through memory operations: SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, DECISION survive storage unchanged; modality, negation, quantifiers, and correlation-vs-cause distinctions must not be dropped during consolidation.
- **memory.manage_consent_and_reversibility**: Manage consent state (EXPLICIT_CURRENT, EXPLICIT_PERSISTENT, IMPLIED, ABSENT, REVOKED) and reversibility for memory-influenced actions. Require current confirmation when stakes are high or consent is absent/revoked.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 26ff6df62d626f3c) for the full vault-sourced domain knowledge (9529 chars).
- **memory.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **memory.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **memory.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/kernel/A/AMOS_Automation_Kernel_v0_Tech_Systems7_3.md` (content_hash: 43ddb346762b4ad8, 843967 bytes) (vault canon, SOURCE_CLAIM)

### Action-Memory Firewall

The firewall separates action authority from memory authority. No action can autonomously modify memory without passing admission gates.

**Firewall laws**:
- `ACTION != MEMORY_MUTATION` -- executing an action does not authorize memory changes
- `OBSERVED != CURRENT` -- observed state is not current state without freshness validation
- `TEST_PASS != TRUTH` -- a test pass is not proof of correctness
- `CAPABILITY != AUTHORITY` -- having the capability to mutate memory does not authorize it

### Automation Kernel Safety Mechanisms

- **Self-auditing pipeline**: every automation run produces an audit trail
- **Benchmarking contract**: reliability, latency, cost, and safety metrics for every action
- **Auto-repair and retry**: graded fallbacks with bounded retry counts
- **Memory protection**: action side effects cannot silently modify canonical memory
- **Effect authorization**: every effect requires explicit authorization before commit

### Action Safety Gates

1. **Intent verification**: action intent matches declared scope
2. **Authority check**: action has valid authority reference
3. **Effect bound**: action effects are bounded and reversible
4. **Memory admission**: any memory mutation passes admission gates
5. **Provenance stamp**: action records full provenance before commit
6. **Rollback basin**: rollback target declared before action execution

### Epistemic Boundary

The action-memory firewall is an architectural safety construct. It does not prove absolute safety, impossibility of bypass, or information-theoretic security. It is defense-in-depth, not absolute prevention.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's 