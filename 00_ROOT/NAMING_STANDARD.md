---
artifact_id: AMOS-OS-NAMING-STANDARD
status: PLACEHOLDER
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
updated: 2026-08-25
---

# AMOS OS Naming Standard

> **Status:** `PLACEHOLDER`

## Minimum conventions

```text
NN_SECTION
UPPER_SNAKE_CASE.md       root/framework contracts
K_*                      kernel contracts
A_*                      agent contracts
S_*                      skill directories
*_MAP.md                  topology/index maps
*_REGISTRY.md             typed registries
*_LEDGER.md               append/replay/audit state
```

## Identity firewall
Filename, artifact ID, registry name, semantic identity, and version identity are distinct fields.

Renaming a file must not silently rewrite canon identity or provenance lineage.

## Version rule
Version labels are explicit metadata. Missing version information remains `UNKNOWN/GAP`; do not infer historical version from filename alone.
