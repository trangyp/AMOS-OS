---
title: Framework Node Schema (RSCF)
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-FRAMEWORK-NODE
canonical_name: FRAMEWORK_NODE_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: framework-nodes
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- framework-node
- note-schema
- frontmatter-specification
- ontology-typing
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Framework Node Schema
- Markdown Note Contract
- framework_node.schema
- AMOS Frontmatter Node Specification
---

# Framework Node Schema (RSCF)

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Standard:** YAML Frontmatter Standard $\times$ RSCF Node Block $\times$ Bidirectional Wikilink Graph

---

## 1. Schema Purpose

`FRAMEWORK_NODE_SCHEMA` defines the mandatory structure and metadata fields required for every Markdown knowledge note across all 18 planes of AMOS OS. It guarantees consistent indexing by Obsidian, Dataview, Obsidian Bases, and automated agent subroutines.

```
+-------------------------------------------------------------------------+
|                      FRAMEWORK NODE STRUCTURE                           |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | YAML FRONTMATTER (title, type, artifact_id, plane, tags, aliases) |  |
|  +-------------------------------------------------------------------+  |
|  | # TITLE & ARCHITECT METADATA                                      |  |
|  +-------------------------------------------------------------------+  |
|  | ## 1. PURPOSE & ARCHITECTURAL SUMMARY                             |  |
|  +-------------------------------------------------------------------+  |
|  | ## 2. FORMAL SPECIFICATION / INVARIANTS / EQUATIONS               |  |
|  +-------------------------------------------------------------------+  |
|  | ## 3. WORKED SEMANTICS / PIPELINES                                |  |
|  +-------------------------------------------------------------------+  |
|  | ## 4. CROSS-PLANE BINDINGS & MOC WIKILINKS                        |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON/YAML Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/framework_node.schema.json",
  "title": "AMOS_Framework_Node",
  "type": "object",
  "required": [
    "title",
    "type",
    "source",
    "artifact_id",
    "plane",
    "status",
    "conclusion_class",
    "tags"
  ],
  "properties": {
    "title": { "type": "string" },
    "type": { "type": "string", "enum": ["kernel", "schema", "note", "canon", "evidence", "mocs"] },
    "source": { "type": "string" },
    "artifact_id": { "type": "string" },
    "canonical_name": { "type": "string" },
    "plane": { "type": "string", "pattern": "^[0-9]{2}_[A-Z_]+$" },
    "status": { "type": "string", "enum": ["CANONICAL", "AMOS_MODEL", "DERIVED", "EXPERIMENTAL"] },
    "conclusion_class": { "type": "string" },
    "origin_architect": { "type": "string" },
    "steward": { "type": "string" },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 3
    },
    "aliases": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "additionalProperties": true
}
```

---

## 3. Invariant Validation Rules

1. **Tag Floor:** Every node must include at least 3 relevant domain tags (`minItems: 3`).
2. **MOC Footnote Invariant:** Every node must link back to its parent segment MOC and the root MOC (`[[00_ROOT_MOC]]` or `[[00_HOME]]`).
3. **No Dangling Artifact IDs:** `artifact_id` must be globally unique across the entire vault.

---

## 4. Cross-Plane Bindings

- **Kernel Protocols:** [[K_CIL]] · [[K_CANON]] · [[K_RSCF]]
- **Related Schemas:** [[PROOF_CAPSULE_SCHEMA]] · [[PROVENANCE_TOPOLOGY_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]

