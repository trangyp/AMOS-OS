---
schema_version: 1.0
title: SKILL — Amos Rscf Epistemic Master
type: skill
source: 07_SKILLS/amos-rscf-epistemic-master
name: amos-rscf-epistemic-master
description: AMOS RSCF Epistemic — claim/class/premises/evidence/provenance/scope/regime/freshness/falsifiers/confidence ceiling. 6 state kinds. Use when epistemic classification, claim assessment, or evidence validation. Do not use for generic tasks outside rscf domain.
parent_skill: none
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/rscf-epistemic
- rscf/source_claim
- hml/h
- epistemic/source_canon
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
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
- L19
license: MIT
steward: Trang Phan
---

# L11 Knowledge & Memory Laws

## Identity

Origin architect: **Trang Phan**. Domain: rscf. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: H.
## When to Use

AMOS RSCF Epistemic — claim/class/premises/evidence/provenance/scope/regime/freshness/dependencies/competing hypotheses/falsifiers/confidence ceiling. 6 state kinds: OBSERVATION, SOURCE_CLAIM, DERI...
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **rscf_episte.classify_claim**: Classify claims using AMOS RSCF Epistemic RSCF state kinds: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.
- **rscf_episte.validate_epistemic**: Validate AMOS RSCF Epistemic outputs against epistemic class labels, claim ceiling, falsifier availability, and scope regime.
- **rscf_episte.analyze_evidence**: Analyze AMOS RSCF Epistemic evidence: source independence, contradiction status, freshness, and dependency chain.
- **rscf_episte.trace_provenance**: Trace AMOS RSCF Epistemic claims to source evidence, derivation chain, epistemic class, and RSCF proof capsule.
- **rscf_episte.assess_claim**: Assess AMOS RSCF Epistemic claims for epistemic class, confidence ceiling, competing hypotheses, and falsifier strength.
- **rscf_episte.manage_lifecycle**: Manage AMOS RSCF Epistemic RSCF lifecycle: classify, validate, trace, assess, label, and finalize with proof capsule.
- **rscf_episte.detect_drift**: Detect epistemic drift: class inflation, ceiling erosion, falsifier neglect, and provenance decay.
- **rscf_episte.escalate_gaps**: Escalate AMOS RSCF Epistemic RSCF gaps: flag UNKNOWN/GAP class, downgrade confidence, trigger evidence gathering.
- **rscf_episte.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (61)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 41 more sub-skills.*

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Master

From C01 Meta Logic: 5 meta-laws, RSCF epistemic substrate. From Cognitive Organism OS: ProofChecker, HypothesisField, RSCF functions.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**5 Meta-laws**:
1. **Law of Law**: no unresolved contradictions within the system
2. **Rule of 2**: at least 2 independent supports for any claim
3. **Rule of 4**: check 4 dimensions: scope, regime, evidence, falsifier
4. **Signal Fidelity Preservation**: no loss of signal fidelity through processing
5. **Structural Integrity**: system structure must be maintained under stress

**RSCF functions**: `compile_claim`, `confidence_ceiling`, `selective_invalidate`

**ProofChecker validation**:
- Scope check: claim is within declared scope
- Regime check: claim is valid under declared conditions
- Confidence ceiling: claim confidence does not exceed evidence support
- Causal level: claim causal level is supported by evidence
- Falsifier check: claim has declared falsifiers

**RSCF laws**:
- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier

### Epistemic Boundary

RSCF epistemic master is an epistemic governance framework. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **KM-1 Typed Storage**: knowledge entries carry type, provenance, confidence, epoch — no untyped dumps as authority.
- **KM-2 Provenance Preservation**: source ancestry survives every transformation; repeated descendants do not increase independence.
- **KM-3 Staleness Visibility**: stale entries are marked, not sile
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-rscf-epistemic-master_MOC]]

## Examples

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the rscf domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when rscf specialization is needed
- **Peers**: Other skills in the `rscf` domain may be composed in sequence
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

- For generic epistemic analysis outside the RSCF framework
- To claim empirical validation of epistemic classification theories
- As a substitute for domain-specific evidence or provenance validation
- Outside RSCF epistemic domain reasoning

## References

- `references/conjecture_discipline.md` — loaded on demand
- `references/ethical_intelligence.md` — loaded on demand
- `references/meta_epistemology_kernel.md` — loaded on demand
- `references/optimization_claim_governance.md` — loaded on demand
- `references/qci_claim_class_governance.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/relation_topology.md` — loaded on demand
- `references/rscf_contract.md` — loaded on demand
- `references/rscf_proof_capsule.md` — loaded on demand
- `references/rscf_state_architecture.md` — loaded on demand
- `references/validate_rscf.md` — loaded on demand
- `` — skill Map of Content
- `none` — parent skill
- `` — corresponding workflow
- `amos-rscf-epistemic-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-rscf-epistemic-master
node_type: skill
path: 07_SKILLS/amos-rscf-epistemic-master/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
