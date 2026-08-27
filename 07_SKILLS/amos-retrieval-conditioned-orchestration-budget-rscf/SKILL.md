---
title: SKILL
type: skill
name: amos-retrieval-conditioned-orchestration-budget-rscf
description: Retrieval Conditioned Orchestration Budget — knowledge research capability. Use when knowledge management, research, or Obsidian vault integration. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-retrieval-conditioned-orchestration-budget-rscf]
---


# Retrieval Conditioned Orchestration Budget Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: knowledge
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Knowledge-research engine for Retrieval Conditioned Orchestration Budget Rscf

## When to Use

- When searching the corpus for relevant passages with provenance
- When managing research artifacts and linking to vault sources
- When tracing agent storage footprint and optimizing retention
- When validating knowledge epistemology and source quality
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **retrieval_conditioned.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **retrieval_conditioned.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **retrieval_conditioned.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **retrieval_conditioned.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **retrieval_conditioned.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: a2280a5f2b0a0d3a) for the full vault-sourced domain knowledge (9556 chars).
- **retrieval_conditioned.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **retrieval_conditioned.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **retrieval_conditioned.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's d

---
**Links:** [[07_SKILLS_MOC]]
