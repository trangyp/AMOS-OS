---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skill
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Scientific Closure Governor Rscf

## Identity

Origin architect: **Trang Phan**. Domain: causal. Parent: amos-causal-reasoning-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.

## When to Use

- When validating causal abstraction across model levels
- When enforcing causal closure: every effect has a sufficient cause
- When governing causal hierarchy: direct, distributed, delayed, cascading
- When reasoning counterfactually about alternative interventions
- When the parent skill (`amos-causal-reasoning-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **scientific_closure.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **scientific_closure.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **scientific_closure.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **scientific_closure.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
- **scientific_closure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **scientific_closure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **scientific_closure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: bdd4d2cb285a670d) for the full vault-sourced domain knowledge (7917 chars).

## Operations

1. **scientific_closure.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
1. **scientific_closure.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
1. **scientific_closure.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
1. **scientific_closure.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
1. **scientific_closure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **scientific_closure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **scientific_closure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Scientific Closure

Scientific closure governs when a scientific question is sufficiently answered to be considered "closed" within the AMOS framework.

**Closure criteria**:

1. **Hypothesis tested**: the hypothesis has been tested with declared falsifiers
1. **Evidence sufficient**: evidence meets the minimum for the claim class
1. **Contradictions resolved**: no unresolved contradictions remain
1. **Provenance complete**: full provenance chain is traceable
1. **Replication**: results have been independently replicated (for VERIFIED class)
1. **Peer review**: results have been reviewed (for VERIFIED class)

**Closure levels**:

- **CLOSED_VERIFIED**: all criteria met, independently verified
- **CLOSED_SOURCE**: source claims verified, not independently replicated
- **CLOSED_MODEL**: model-based closure, not empirically verified
- **OPEN**: still under investigation
- **BLOCKED**: cannot close due to insufficient evidence

**Law**: `Closure != Truth`. A closed question is sufficiently answered within the framework, not proven true in an absolute sense.

### Epistemic Boundary

Scientific closure is an epistemic governance construct. It does not prove absolute truth, finality, or that the answer will never be revised. Closure is operational, not metaphysical.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-scientific-closure-governor-rscf/amos-scientific-closure-governor-rscf_MOC|amos-scientific-closure-governor-rscf_MOC]]

## Examples

- **Scenario**: When validating causal abstraction across model levels

  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing causal closure: every effect has a sufficient cause

  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing causal hierarchy: direct, distributed, delayed, cascading

  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

## Anti-Patterns

- **Do not use** for tasks outside the causal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-causal-reasoning-master` — routes to this skill when causal specialization is needed
- **Peers**: Other skills in the `causal` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `26_WORKFLOWS/`
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

- For generic causal analysis outside the AMOS causal framework
- To claim empirical validation of causal closure or hierarchy theories
- As a substitute for domain-specific causal or counterfactual evidence
- Outside causal reasoning domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-causal-reasoning-master` — parent skill
- \`\` — corresponding workflow
- `amos-scientific-closure-governor-rscf-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-scientific-closure-governor-rscf
node_type: skill
path: 07_SKILLS/amos-scientific-closure-governor-rscf/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
