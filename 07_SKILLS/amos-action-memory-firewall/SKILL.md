---
schema_version: 1.0
title: SKILL — Amos Action Memory Firewall
type: skill
source: 07_SKILLS/amos-action-memory-firewall
name: amos-action-memory-firewall
description: Action Memory Firewall — memory systems capability. Use when memory management, context continuity, or memory conflict resolution. Use when amos-memory-systems-master routes to this specialized capability. Do not use for generic tasks outside memory domain.
parent_skill: amos-memory-systems-master
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/memory-systems
- rscf/source_claim
- hml/m
- epistemic/source_claim
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

# Action Memory Firewall

## Identity

Origin architect: **Trang Phan**. Domain: memory. Parent: amos-memory-systems-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-action-memory-firewall_MOC]]

## Examples

- **Scenario**: When managing memory: storage, retrieval, decay, consolidation
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When resolving memory conflicts: contradictions, staleness, priority
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing memory firewall: preventing unauthorized access
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the memory domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-memory-systems-master` — routes to this skill when memory specialization is needed
- **Peers**: Other skills in the `memory` domain may be composed in sequence
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

- For generic memory analysis outside the AMOS memory framework
- To claim empirical validation of memory consolidation theories
- As a substitute for domain-specific memory or context evidence
- Outside memory systems domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-memory-systems-master` — parent skill
- `` — corresponding workflow
- `amos-action-memory-firewall-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-action-memory-firewall
node_type: skill
path: 07_SKILLS/amos-action-memory-firewall/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
