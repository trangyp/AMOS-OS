---
title: SKILL — Amos Portable Agent Authorization Rscf
type: skill
source: 07_SKILLS/amos-portable-agent-authorization-rscf
name: amos-portable-agent-authorization-rscf
description: Portable Agent Authorization — agent systems capability. Use when agent
  design, delegation reasoning, or multi-agent governance. Use when amos-agent-systems-master
  routes to this specialized capability.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/agent-systems
- canon-group/tech-ai
- topic/multi-agent
- capability/agent-design
- capability/governance
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/S-state
- rscf/T-topology
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-portable-agent-authorization-rscf
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
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
---







# Portable Agent Authorization Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-agent-systems-master`
- **Domain**: agent
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Agent systems engine for Portable Agent Authorization Rscf

## When to Use

- When governing agency: who acts, under what authority, consequences
- When designing agent externalization: delegation and controls
- When attributing agent ownership and responsibility
- When verifying delegation witness validity: temporal, revocable, attenuation-bound
- When checking enforcement trust contracts for agent authorization chains
- When the parent skill (`amos-agent-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **portable_agent.govern_agency**: Govern agency: who acts, under what authority, with what consequences
- **portable_agent.design_externalization**: Design agent externalization: what is delegated, to whom, with what controls
- **portable_agent.attribute_ownership**: Attribute agent ownership: who is responsible for each agent action
- **portable_agent.verify_agentic**: Verify agentic skill-lie algebroid: structural consistency of agent capabilities
- **portable_agent.validate_delegation**: Validate delegation witness: temporal, revocable, attenuation-bound
- **portable_agent.detect_drift**: Detect drift in authorization chains, delegation validity, or trust contracts
- **portable_agent.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **portable_agent.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: Enforcement Trust Contract (v43) and Enforcement Root Attestation (v42) from AMOS brain production code (vault canon, SOURCE_CLAIM)

### Delegation Witness (v43)

Temporal, revocable, attenuation-bound delegation closing the zombie-agent problem:

- `ChildScope(t) ⊆ ParentScope(t)` — child scope must be subset of parent at all times
- `ChildLifetime ≤ ParentLifetime` — child cannot outlive parent
- `¬ParentEligible(t) ⇒ ChildEligible(t+Δ) = FALSE` — parent ineligibility propagates to child

### Enforcement Trust Contract (v43)

16-field contract binding authority to the entire enforcement chain:
- Control plane, policy artifact + signer + compiler, refmon, runtime/kernel
- Workload, egress guard, epochs, delegation parent + attenuation
- Independence root, agent-write exclusion, release ledger

**Hard rule**: An effect cannot become authoritative merely because AMOS approved it; AMOS must also establish the currently executing enforcement chain is the same trusted chain to which approval was issued.

### Separability Law (expanded v43)

`Capability ≠ Reachability ≠ Identity ≠ Authorization ≠ Delegation ≠ Observability ≠ Enforcement ≠ Finality ≠ Consequence`

Enforcement identity itself must be proven — not just the decision, but the mechanism enforcing it.

### MayExternalize_v43

`MayExternalize_v43 = v42 18-term ∧ EnforcementTrustContractValid ∧ DelegationWitnessValid` (20 terms total)

### Epistemic Boundary

Enforcement trust contracts are AMOS_MODEL validated through synthetic fuzz testing (300k deterministic fuzz, seed 202608232231). Synthetic fuzz proves logic correctness vs self-defined adversary, NOT universal security. "AMOS universally guarantees AI containment" = NOT ESTABLISHED. Hardware/root-of-trust compromise NOT ESTABLISHED.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-portable-agent-authorization-rscf_MOC]]

## Examples

- **Scenario**: When governing agency: who acts, under what authority, consequences
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When designing agent externalization: delegation and controls
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When attributing agent ownership and responsibility
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the agent domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-agent-systems-master` — routes to this skill when agent specialization is needed
- **Peers**: Other skills in the `agent` domain may be composed in sequence
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

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-portable-agent-authorization-rscf_MOC]]` — skill Map of Content
- `amos-agent-systems-master` — parent skill
- `[[amos-portable-agent-authorization-rscf-workflow]]` — corresponding workflow
- `amos-portable-agent-authorization-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-portable-agent-authorization-rscf
node_type: skill
path: 07_SKILLS/amos-portable-agent-authorization-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
