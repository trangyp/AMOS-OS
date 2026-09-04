---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Vault Resolver
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

# Cognitive Vault Resolver

**Path:** `03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER.md`
**Purpose:** Active vault identity, routing, repair, and archival resolver.

## Vault identity

The authoritative AMOS_OS vault is the Google Drive sync copy:

- **Authoritative vault:** `/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS`
- **Stale local copy:** `/Users/mac/Documents/AMOS_OS` — used by Obsidian MCP but missing 2,408 files and containing an older `AGENTS.md`
- **Resolution:** Google Drive copy takes precedence; Documents copy is a downstream mirror that requires resync.

## Routing bindings

| Surface                | Path                                                                    | Status                 |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------- |
| Structural navigation  | `00_ROOT/00_ROOT_MOC.md`                                                | exists                 |
| Control-plane contract | `03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT.md`              | exists                 |
| Runtime contract       | `04_RUNTIME/RUNTIME_RUNTIME_CONTRACT.md`                                | exists                 |
| Test contract          | `19_TESTS/TESTS_TEST_CONTRACT.md`                                       | exists                 |
| Audit ledger           | `20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03.md`                             | created by repair pass |
| Historical record      | `24_ARCHIVE/AGENTS__HISTORICAL_PRE_V4_4_AUTHORITY_REPAIR_2026-09-03.md` | created by repair pass |

## Repair and archival resolver

- Sync-conflict duplicates (`01_CANON/* (1)`) archived to `24_ARCHIVE/01_CANON_google_drive_sync_conflicts_2026-09-03/`
- Stale `AGENTS.md` preserved in `24_ARCHIVE/AGENTS__HISTORICAL_PRE_V4_4_AUTHORITY_REPAIR_2026-09-03.md`
- Empty archive notes flagged in `20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03.md`
- Remaining gaps tracked in `20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03.md`

## Active invariants

- `LATEST != AUTHORITATIVE`
- `DOCUMENTED != IMPLEMENTED`
- `MODEL != DEPLOYED_RUNTIME`
- `CAPABILITY != AUTHORITY`
- `PROPOSAL != COMMIT`

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
