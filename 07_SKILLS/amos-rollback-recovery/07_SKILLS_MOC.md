---
name: amos-rollback-recovery
description: Executes atomic MVCC checkpoint rollbacks to restore last known consistent state during verification failures.
origin_architect: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SKILL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
tags:
  - skill
  - governance
  - amos
---

# Rollback & Recovery Skill (`amos-rollback-recovery`)

## 1. Purpose & Invariants
Executes atomic MVCC checkpoint rollbacks to restore last known consistent state during verification failures.

## 2. Execution Contract
- **Preconditions**: Verified epoch token, valid parent MOC link, established RSCF provenance.
- **Invariants**: Fail closed upon identity failure; zero side effects without transaction receipt.
- **Postconditions**: Write immutable execution receipt to `[[20_OPERATIONS/20_OPERATIONS_MOC]]`.

## 3. Workflow Integration
- Handled via `[[08_WORKFLOWS/amos-rollback-recovery-workflow]]`.
- Monitored via `[[17_OBSERVABILITY/17_OBSERVABILITY_MOC]]`.

## Usage

Activate `amos-rollback-recovery` when the runtime or control plane routes a task to its declared domain. Typical invocation flow:

1. The `07_SKILLS/07_SKILLS_MOC` or `amos-agent-orchestrator` selects this skill based on the task's domain tags.
2. The skill receives a `SKILL.md` invocation envelope containing the request, context, and authority scope.
3. The skill executes its specialized reasoning and returns a structured output with RSCF metadata.
4. The caller plane validates the output against the skill's epistemic boundary and invariants before admitting it.

Do not invoke this skill for generic tasks outside its declared domain.

## Inputs / Outputs

| Input | Type | Description |
|-------|------|-------------|
| request | string | Task or question routed to this skill |
| context | object | Relevant prior state, memory, and provenance |
| authority | object | Capability-bound authority envelope |

| Output | Type | Description |
|--------|------|-------------|
| result | any | Skill-specific structured output |
| rscf | object | `state`, `claim_class`, `provenance`, `scope` |
| receipt | string | Cryptographic receipt for audit |

All outputs are classified as `SOURCE_CLAIM` or `DERIVED` unless independently validated.

## Dependencies

- **Skill parent / router:** `07_SKILLS/07_SKILLS_MOC`
- **Agent orchestrator:** `amos-agent-orchestrator`
- **RSCF framework:** `11_KNOWLEDGE/03_RSCF/03_RSCF_MOC`
- **Authority plane:** `02_KERNEL/07_AUTHORITY/07_AUTHORITY_MOC`
- **Related skills:** see `07_SKILLS/amos-rollback-recovery/references/references_MOC`

This skill may depend on other `amos-*` skills listed in its `SKILL.md` `depends_on_skills` block.

## Invariants

| ID | Invariant |
|----|-----------|
| AMOS_ROLLBACK_RECOVERY_INV_01 | Outputs are scoped to the skill's declared domain. |
| AMOS_ROLLBACK_RECOVERY_INV_02 | Authority is checked before any state-altering effect. |
| AMOS_ROLLBACK_RECOVERY_INV_03 | RSCF metadata is attached to every output. |
| AMOS_ROLLBACK_RECOVERY_INV_04 | No claim is promoted to `01_CANON` without governed successor evidence. |

## Examples

| Scenario | Input | Output |
|----------|-------|--------|
| Typical use | A task matching the skill's domain | Structured, scoped result with provenance |
| Out-of-scope request | A task outside the skill's domain | Refusal or escalation to `07_SKILLS/07_SKILLS_MOC` |
| Missing authority | A task requiring authority the caller lacks | Fail-closed response with `ENFORCEMENT_TRUST_CONTRACT` alert |

Examples are illustrative templates, not executed test cases.

## Related Skills

- `amos-knowledge-research-master` — routes research and vault integration tasks
- `amos-os-runtime-master` — routes runtime and OS tasks
- `amos-canon-universe-master` — routes canon and universe-level reasoning
- `amos-rscf-epistemic-master` — routes claim classification and evidence validation

See the full skill tree in `07_SKILLS/07_SKILLS_MOC`.
