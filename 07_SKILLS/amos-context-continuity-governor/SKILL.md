---
title: SKILL
type: skill
name: amos-context-continuity-governor
description: Context Continuity Governor — boundary and scope capability. Use when evaluating scope boundaries, context continuity, or capability bounds. Use when amos-boundary-scope-master routes to this specialized capability.
parent_skill: amos-boundary-scope-master
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-context-continuity-governor]
---


# Context Continuity Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-boundary-scope-master`
- **Domain**: boundary
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Boundary and scope governance for Context Continuity Governor

## When to Use

- When boundary and scope governance for context continuity governor is needed within the boundary domain
- When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
- When a query requires boundary-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **context_continuity.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
- **context_continuity.check_admission**: Check admission criteria: whether a query enters this capability legitimately
- **context_continuity.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
- **context_continuity.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
- **context_continuity.audit_boundary**: Audit boundary crossings and log violations for governance review
- **context_continuity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **context_continuity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 8940d50a1c67341a) for the full vault-sourced domain knowledge (7483 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/TO/TOKEN_GOVERNOR.md` (content_hash: 61701ef736e3657a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/fractal/SKILL (fractal-state).md` (content_hash: 7ba1e6df8d84a479) (vault canon, SOURCE_CLAIM)

### Context Continuity Governor

From Cosmo Brain Token/Context Governor: 10-level retention priority and drop rule. From Fractal State Skill: H/M/L progressive disclosure for context management.

**10-level retention priority** (SOURCE_CLAIM):
1. **Objective**: the task objective (highest priority)
2. **Hard constraints**: constraints that cannot be violated
3. **Decision-changing evidence**: evidence that could change the decision
4. **Unresolved contradictions**: contradictions that need resolution
5. **Load-bearing premises**: premises that support conclusions
6. **Provenance/scope/regime/freshness**: RSCF metadata
7. **Active hypotheses**: hypotheses currently being tested
8. **Implementation details**: how things are implemented
9. **Recoverable background**: background that can be recovered if needed
10. **Redundant narrative**: narrative that can be dropped (lowest priority)

**Drop rule**: Drop only when removal cannot reasonably change: answer, decision, confidence, safety, falsifier, or implementation correctness.

**Compression**: Use IDs, hashes, schemas, equations, relation edges, and proof capsules internally. Use prose primarily at system boundaries.

**H/M/L progressive disclosure** (from Fractal State Skill):
1. Determine the appropriate scale level (H/M/L)
2. Load capsule-first summary at the chosen level
3. Expand recursively only when deeper detail is needed
4. Track information gain at each expansion
5. Stop when information gain falls below threshold

**Governor laws**:
- `CONTINUITY != PRESERVATION`: continuity maintains the thread; preservation keeps everything
- `CONTEXT != STATE**: context is the active working set; state is the full system state
- `DROP != DELETE**: dropping removes from active context; it does not delete the information

### Epistemic Boundary

Context continuity governance is an operational construct. It does not prove all context is preserved, that the priority order is always correct, or that dropping is always safe.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, f