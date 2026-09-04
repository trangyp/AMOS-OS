---
title: copilot-instructions
type: control_surface
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE
conclusion_class: GOVERNANCE
rscf:
  state: ACTIVE_CONTROL_SURFACE
  provenance: amos_os_copilot_instructions
  scope: active__AMOS_OS
---

# AMOS OS Copilot & Agent Operational Instructions

> **Origin Architect & Steward:** Trang Phan
> **Target Version Lineage:** v3.0 → v4.4 (Governed Canonical Core)
> **Status:** ACTIVE_CONTROL_SURFACE

## 1. Prime Invariants for Autonomous Agents & Copilots

All autonomous agents, copilots, subagents, and automated refactoring pipelines operating within the `_AMOS_OS` vault MUST unconditionally follow the governing axioms established in [[AGENTS|AGENTS]]:

```
LATEST != AUTHORITATIVE
DOCUMENTED != IMPLEMENTED
MODEL != DEPLOYED_RUNTIME
TEST_SPECIFIED != TEST_EXECUTED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
```

## 2. Epistemic Classification Protocol

Every assertion, specification, or knowledge node created or modified must explicitly declare its epistemic state in YAML frontmatter:
- `SOURCE_CLAIM`: Direct assertion from an external entity, paper, or dataset.
- `OBSERVATION`: Empirically verified metric, log output, or test run.
- `DERIVED`: Deductive logical conclusion or mathematically proven formula.
- `MODEL`: Theoretical framework, simulation hypothesis, or surrogate representation.
- `DECISION`: Explicit architectural choice or policy commitment approved by the steward.
- `COMPETING`: Multiple rival hypotheses held simultaneously under active investigation.
- `UNKNOWN/GAP`: Acknowledged boundary of missing information, unverified code, or open question.

## 3. Standard 9-Part Specification Architecture

All architectural planes, contracts, and domain specifications must adhere to the 9-part contract structure:
1. `ROLE`: Primary functional purpose within the AMOS ecosystem.
2. `INTERFACES`: Programmatic and epistemic input/output surfaces.
3. `DEPENDENCIES`: Upstream prerequisites and downstream consumers.
4. `INVARIANTS`: Non-negotiable mathematical, logical, and operational invariants.
5. `AUTHORITY`: Architectural steward (`Trang Phan`) and governance policy.
6. `PROVENANCE`: Cryptographic hash, source repository, and historical lineage.
7. `TESTS`: Deterministic verification routines and automated test suites.
8. `FAILURE`: Observable failure states, blast radius boundaries, and tripwires.
9. `RECOVERY`: Self-healing procedures, rollback recipes, and state reconciliation.

## 4. Operational Safety & Editing Rules

1. **Large File Boundary**: Do not perform monolithic full-file edits on files exceeding 4 MB (such as `00_ROOT/00_HOME.md`). Use modular subplane notes and aliases instead.
2. **Backlink Integrity**: Never create broken wikilinks. Always verify link targets using `python3 scripts/master_vault_validator_2026.py`.
3. **Archive First**: Destructive changes or obsolete notes must be migrated to `24_ARCHIVE/` with full provenance preserved rather than deleted.
4. **Receipt Generation**: Consequential operational changes must generate a BLAKE3 or SHA-256 audit receipt recorded in `20_OPERATIONS/`.

## 5. Related Governance Surfaces

- Master Agent Contract: [[AGENTS|AGENTS]]
- Cognitive Vault Resolver: [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|Cognitive Vault Resolver]]
- Root Navigation: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- Operations Audit Ledger: [[20_OPERATIONS/AMOS_OS_MASTER_HEALTH_AUDIT_2026-09-04|Master Health Audit 2026-09-04]]
