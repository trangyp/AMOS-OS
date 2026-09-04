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

# Mckinsey: enterprise Data Transformation Rscf

## Identity

Origin architect: **Trang Phan**. Domain: mckinsey. Parent: amos-c08-strategy-game-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When mckinsey strategy framework for mckinsey: enterprise data transformation rscf is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **enterprise_data.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **enterprise_data.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **enterprise_data.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **enterprise_data.transfer_architecture**: Transfer architecture references: best practices across organizational contexts

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f258a3795dc58a14) for the full vault-sourced domain knowledge (8330 chars).

- **enterprise_data.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **enterprise_data.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **enterprise_data.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **enterprise_data.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
1. **enterprise_data.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
1. **enterprise_data.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
1. **enterprise_data.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
1. **enterprise_data.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **enterprise_data.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **enterprise_data.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Substrate

This RSCF engine operates on the AMOS RSCF (Reasoning, Scope, Claim, Falsifier) epistemic substrate.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**RSCF laws**:

- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier
- `SCOPE_BOUND`: every claim is valid only within its declared scope and regime
- `PROVENANCE_REQUIRED`: every claim must have traceable provenance

**RSCF validation gates**:

- G1 (Law of Law): no unresolved contradictions
- G2 (Epistemic class): all claims labeled, no class promotion without evidence
- G3 (Provenance): source path recorded for every derived claim
- G4 (Anti-overreach): no claim beyond declared scope
- G5 (Equation firewall): equations carry status tags
- G6 (Failure mode): on failure, downgrade, flag, escalate

### Epistemic Boundary

This RSCF engine is an epistemic governance tool. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

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
- **G6 (Failure mode)**:

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/mckinsey-enterprise-data-transformation-rscf/mckinsey-enterprise-data-transformation-rscf_MOC|mckinsey-enterprise-data-transformation-rscf_MOC]]

## Examples

- **Scenario**: When mckinsey strategy framework for mckinsey: enterprise data transformation rscf is needed within the mckinsey domain

  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability

  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires mckinsey-specific reasoning grounded in vault sources

  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance

## Anti-Patterns

- **Do not use** for tasks outside the mckinsey domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-c08-strategy-game-master` — routes to this skill when mckinsey specialization is needed
- **Peers**: Other skills in the `mckinsey` domain may be composed in sequence
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

- For generic business analysis outside the McKinsey framework
- To claim empirical validation of consulting methodologies
- As a substitute for domain-specific industry or market evidence
- Outside McKinsey/strategy domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- \`\` — corresponding workflow
- `mckinsey-enterprise-data-transformation-rscf-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: mckinsey-enterprise-data-transformation-rscf
node_type: skill
path: 07_SKILLS/mckinsey-enterprise-data-transformation-rscf/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
