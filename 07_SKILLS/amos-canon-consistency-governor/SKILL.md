---
title: SKILL
type: skill
name: amos-canon-consistency-governor
description: Canon Consistency Governor — canon and universe capability. Use when canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-canon-consistency-governor]
---


# Canon Consistency Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-canon-universe-master`
- **Domain**: canon
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Canon and universe engine for Canon Consistency Governor

## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **canon_consistency.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **canon_consistency.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **canon_consistency.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **canon_consistency.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **canon_consistency.validate_substrate**: Validate canonical software substrate against canon requirements

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 653b78f7dec7566f) for the full vault-sourced domain knowledge (9537 chars).
- **canon_consistency.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **canon_consistency.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **canon_consistency.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/amos-general/0/00_AMOS_Full_Brain_OS_Architecture.md` (content_hash: b7acbb430dff829e) (vault canon, SOURCE_CLAIM)

### Canon Consistency Rules

**Law of Law**: No unresolved contradictions within the canon. Every contradiction must be either resolved, flagged as UNKNOWN/GAP, or explicitly tolerated with justification.

**Consistency checks**:
1. **Contradiction detection**: no two canon entries make contradictory claims within the same scope and regime
2. **Gap detection**: no canon entry references a missing dependency
3. **Orphan detection**: no canon entry has zero incoming references (except root entries)
4. **Scope consistency**: no canon entry claims beyond its declared scope
5. **Epistemic consistency**: no canon entry promotes its epistemic class without evidence
6. **Provenance consistency**: every canon entry has a traceable provenance chain

### RSCF Epistemic Substrate

Objects: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

State kinds: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

### Contradiction Resolution Protocol

1. **Detect**: identify the contradiction (automated scan)
2. **Classify**: scope conflict, regime conflict, evidence conflict, or epistemic conflict
4. **Resolve**: resolve via evidence weight, scope intersection, or steward decision
5. **Flag**: if unresolvable, flag as UNKNOWN/GAP and fail closed
6. **Record**: record the contradiction and resolution in the canon audit trail

### Epistemic Boundary

Canon consistency is a structural property. It does not prove the canon is true, only that it is internally consistent. A consistent canon can still be wrong.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyo

---
**Links:** [[07_SKILLS_MOC]]
