---
title: SKILL
type: skill
name: amos-rscf-epistemic-master
description: AMOS RSCF Epistemic — claim/class/premises/evidence/provenance/scope/regime/freshness/falsifiers/confidence ceiling. 6 state kinds. Use for epistemic classification, claim assessment, or evidence validation.
parent_skill: none
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-rscf-epistemic-master]
---

# L11 Knowledge & Memory Laws

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 61 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 61 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `01_CANON/01_CORE_LAWS/L11_KNOWLEDGE_MEMORY.md`).

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
