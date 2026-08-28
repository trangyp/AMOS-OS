---
title: Provenance Health Observability Schema
type: schema
source: 16_SCHEMAS/11_OBSERVABILITY
artifact_id: AMOS-SCHEMA-PROVENANCE-HEALTH
canonical_name: PROVENANCE_HEALTH_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/11_OBSERVABILITY
schema_family: OBSERVABILITY
domain: provenance-health
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- observability
- provenance-health
- lineage-auditing
- source-independence-telemetry
- graph-integrity
- rscf/claim
- rscf/state/canonical
- 11-observability-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Provenance Health Schema
- Provenance Telemetry Contract
- provenance_health.schema
- AMOS Provenance Audit Report Specification
---

# Provenance Health Observability Schema

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/11_OBSERVABILITY`  
> **Status:** `CANONICAL`  
> **Observability Metric:** Lineage Completeness $\times$ Circular Reference Scans $\times$ Ancestry Independence Score

---

## 1. Schema Purpose

`PROVENANCE_HEALTH_SCHEMA` defines the structured report emitted by provenance auditing tools. It evaluates whether all canonical assertions across the vault maintain unbroken upstream citation graphs, detects circular reasoning loops, and computes the overall provenance independence index.

```
+-------------------------------------------------------------------------+
|                 PROVENANCE HEALTH AUDIT TELEMETRY                       |
|                                                                         |
|  [ Ingest Entire Vault Provenance Graph G = (V, E) ]                    |
|                         |                                               |
|                         v                                               |
|  ( Step 1: Detect Directed Cycles: Tarjan's SCC Algorithm )             |
|                         |                                               |
|                         v                                               |
|  ( Step 2: Verify Root Lineage Anchor for Every Canonical Node )        |
|                         |                                               |
|                         v                                               |
|  ( Step 3: Compute Vault-Wide Independence Score Indep(G) )             |
|                         |                                               |
|                         v                                               |
|  [ Emit Signed Provenance Health Telemetry Report ]                     |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/observability/provenance_health.schema.json",
  "title": "AMOS_Provenance_Health_Report",
  "type": "object",
  "required": [
    "report_id",
    "timestamp",
    "total_nodes_audited",
    "unanchored_nodes_count",
    "circular_reference_count",
    "average_independence_score",
    "isolated_clusters",
    "status"
  ],
  "properties": {
    "report_id": {
      "type": "string",
      "format": "uuid"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "total_nodes_audited": {
      "type": "integer",
      "minimum": 1
    },
    "unanchored_nodes_count": {
      "type": "integer",
      "minimum": 0
    },
    "circular_reference_count": {
      "type": "integer",
      "minimum": 0
    },
    "average_independence_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "isolated_clusters": {
      "type": "array",
      "items": { "type": "string" }
    },
    "status": {
      "type": "string",
      "enum": ["PROVENANCE_OPTIMAL", "LINEAGE_WARNING", "PROVENANCE_CORRUPTED"]
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Cycle Prohibition:** If $\text{circular\_reference\_count} > 0$, $\text{status} = \text{"PROVENANCE\_CORRUPTED"}$.
2. **Lineage Completeness Floor:** If $\text{unanchored\_nodes\_count} > 0$, system raises a warning receipt and flags unanchored nodes as `UNKNOWN/GAP`.
3. **Observability Isolation:** Reports are read-only telemetry and possess zero capability to modify provenance edges directly without control plane approval.

---

## 4. Cross-Plane Bindings

- **Kernel Protocols:** [[K_PROVENANCE_TRACKING]] · [[K_ANTI_AUTOPOISONING]] · [[K_HERITAGE_BINDING]]
- **Related Schemas:** [[PROVENANCE_TOPOLOGY_SCHEMA]] · [[CANON_HEALTH_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[11_OBSERVABILITY_MOC]] · [[00_ROOT_MOC]]

