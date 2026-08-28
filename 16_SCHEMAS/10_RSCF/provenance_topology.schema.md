---
title: Provenance Topology Schema (RSCF)
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-PROVENANCE-TOPOLOGY
canonical_name: PROVENANCE_TOPOLOGY_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: provenance-topology
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- provenance-topology
- source-independence
- ancestry-graph
- dag-verification
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Provenance Topology Schema
- Provenance Graph Contract
- provenance_topology.schema
- AMOS Source Ancestry Specification
---

# Provenance Topology Schema (RSCF)

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Topology Standard:** Directed Acyclic Lineage Graph $\times$ Source Independence Metric $\times$ Cryptographic Ancestry

---

## 1. Schema Purpose

`PROVENANCE_TOPOLOGY_SCHEMA` specifies the graph structure representing the origin, transformation history, derivation paths, and external source dependencies of any canonical node in AMOS OS. It guarantees that multi-source syntheses compute true source independence rather than compounding redundant circular citations.

```
+-------------------------------------------------------------------------+
|                    PROVENANCE TOPOLOGY GRAPH                            |
|                                                                         |
|  [ Primary Source A (arXiv) ]       [ Primary Source B (Vault Native) ] |
|             \                                      /                    |
|              v                                    v                     |
|         ( Derivation Edge: E1 )          ( Derivation Edge: E2 )        |
|                       \                  /                              |
|                        v                v                               |
|                  [ Derived Synthesized Node N ]                         |
|                                 |                                       |
|                                 v                                       |
|       ( Source Independence Audit: Indep(A, B) >= 0.85 -> PASS )        |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/provenance_topology.schema.json",
  "title": "AMOS_Provenance_Topology",
  "type": "object",
  "required": [
    "topology_id",
    "target_node",
    "ancestor_nodes",
    "derivation_edges",
    "source_independence_score",
    "last_audited_epoch"
  ],
  "properties": {
    "topology_id": {
      "type": "string",
      "format": "uuid"
    },
    "target_node": {
      "type": "string",
      "pattern": "^\\[\\[[A-Za-z0-9_\\-\\.]+\\]\\]$"
    },
    "ancestor_nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["node_id", "source_uri", "independence_tier"],
        "properties": {
          "node_id": { "type": "string" },
          "source_uri": { "type": "string" },
          "independence_tier": { "type": "integer", "minimum": 1, "maximum": 5 }
        }
      }
    },
    "derivation_edges": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["source", "target", "transformation_type"],
        "properties": {
          "source": { "type": "string" },
          "target": { "type": "string" },
          "transformation_type": { 
            "type": "string", 
            "enum": ["DIRECT_EXTRACTION", "ALGEBRAIC_DERIVATION", "SYNTHESIS", "REFACTOR", "EMPIRICAL_FIT"] 
          }
        }
      }
    },
    "source_independence_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "last_audited_epoch": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Acyclicity Invariant:** The directed graph formed by `derivation_edges` must be strictly acyclic (no ancestor may have the target node as its ancestor).
2. **Circular Citation Floor:** Aggregated multi-source confidence is capped if `source_independence_score < 0.70`.
3. **Audit Trail Mandate:** Every topology must record the `last_audited_epoch` state hash.

---

## 4. Cross-Plane Bindings

- **Kernel Protocols:** [[K_PROVENANCE_TRACKING]] · [[K_ANTI_AUTOPOISONING]] · [[K_CIL]]
- **Schemas:** [[PROOF_CAPSULE_SCHEMA]] · [[FRAMEWORK_NODE_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]
- **Governed by:** [[LAW_HIERARCHY]]

---
**MOC:** [[10_RSCF_MOC]]
