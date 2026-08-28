---
title: SKILL — Amos Provenance Trust Firewall
type: skill
source: 07_SKILLS/amos-provenance-trust-firewall
name: amos-provenance-trust-firewall
description: Provenance Trust Firewall — security and safety capability. Use when
  security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master
  routes to this specialized capability.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/security-safety
- canon-group/tech-ai
- topic/security
- capability/trust
- capability/firewall
- rscf/epistemic
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-provenance-trust-firewall
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---



# Provenance Trust Firewall

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-security-safety-master`
- **Domain**: security
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Security and trust engine for Provenance Trust Firewall

## When to Use

- When detecting adversarial activity: attacks, probes, manipulation
- When quantifying adversarial entropy and attack surface
- When governing principal-trust relationships: delegation, revocation
- When monitoring distributed attack composition: multi-stage threats
- When the parent skill (`amos-security-safety-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **provenance_trust.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
- **provenance_trust.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
- **provenance_trust.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
- **provenance_trust.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
- **provenance_trust.replay_provenance**: Replay execution provenance: trace and verify every action for integrity
- **provenance_trust.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **provenance_trust.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **provenance_trust.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 737938b28246ae22) for the full vault-sourced domain knowledge (7602 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/dated/2026-08-22/2026-08-22 Cognitive Substrate Reality Gate.md` (content_hash: 2c93bdf31c3481c7) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Provenance Trust Firewall

From Cosmo Brain Cognitive Substrate Reality Gate: Prevents epistemic autopoisoning by requiring reality contact before any LLM-generated claim is promoted to durable memory.

**The problem**: Epistemic autopoisoning -- LLM generates X -> X stored -> X retrieved -> X treated as evidence -> X strengthened -> X stored again. Confidence rises with no new reality contact. The system becomes internally coherent and externally wrong.

**The gate**:
```
Promote(X) => RC(X) >= theta_RC AND IR(X) <= theta_IR
```
- `RC(X)` -- number/quality of independent external observations supporting X
- `IR(X)` -- fraction of support ultimately descending from AMOS-generated state
- Default thresholds: `theta_RC = 1.0`, `theta_IR = 0.5` (raise both for high-stakes claims)

**Memory I/O pipelines**:
- Write path: `Propose -> Type -> CheckEvidence -> CheckScope -> CheckProvenance -> Admit`
- Read path: `Retrieve -> Validate -> Contextualize -> Use`
- Failure at any stage quarantines the object; provenance is retained, nothing is silently deleted

**4 Key invariants**:
1. Claim strength must not exceed evidence strength (high confidence does not bypass the gate)
2. Repetition does not establish source independence (non-independent contacts are not double-counted)
3. Short internal-recursion paths raise IR and tighten the gate
4. Counterfactual repair: a quarantined object is rescued only by adding an independent external contact and re-running `promote()`

**Cognitive integrity formula**: `CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity ∧ InterfaceIntegrity ∧ RealityContact`

### Epistemic Boundary

Provenance trust firewall is a security construct. It does not prove all autopoisoning is prevented, that thresholds are always correct, or that the gate cannot be bypassed.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-provenance-trust-firewall_MOC]]

## Examples

- **Scenario**: When detecting adversarial activity: attacks, probes, manipulation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When quantifying adversarial entropy and attack surface
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing principal-trust relationships: delegation, revocation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the security domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-security-safety-master` — routes to this skill when security specialization is needed
- **Peers**: Other skills in the `security` domain may be composed in sequence
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
- `[[amos-provenance-trust-firewall_MOC]]` — skill Map of Content
- `amos-security-safety-master` — parent skill
- `[[amos-provenance-trust-firewall-workflow]]` — corresponding workflow
- `amos-provenance-trust-firewall-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-provenance-trust-firewall
node_type: skill
path: 07_SKILLS/amos-provenance-trust-firewall/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
