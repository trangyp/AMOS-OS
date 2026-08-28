---
title: Canon Health Observability Schema
type: schema
source: 16_SCHEMAS/11_OBSERVABILITY
artifact_id: AMOS-SCHEMA-CANON-HEALTH
canonical_name: CANON_HEALTH_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/11_OBSERVABILITY
schema_family: OBSERVABILITY
domain: canon-health
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- observability
- canon-health
- broken-link-detection
- drift-auditing
- health-metrics
- rscf/claim
- rscf/state/canonical
- 11-observability-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Canon Health Schema
- Vault Observability Health Contract
- canon_health.schema
- AMOS Canon Health Telemetry
---

# Canon Health Observability Schema

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/11_OBSERVABILITY`  
> **Status:** `CANONICAL`  
> **Observability Boundary:** Read-Only Audit Telemetry $\times$ Non-Authoritative $\times$ Continuous Link/Invariant Verification

---

## 1. Schema Purpose

`CANON_HEALTH_SCHEMA` specifies the reporting telemetry for automated health checks (such as `scripts/obsidian-health-check.sh`, Vitest test runners, and link scrapers). It aggregates metrics regarding broken wikilinks, unindexed files, invalid frontmatter, confidence anomalies, and canonical drift.

```
+-------------------------------------------------------------------------+
|                    CANON HEALTH OBSERVABILITY REPORT                    |
|                                                                         |
|  [ Periodic Scanner / Health Check Suite ]                              |
|                         |                                               |
|                         v                                               |
|  ( Step 1: Scan 18 Planes for Broken Wikilinks & Frontmatter Schema )   |
|                         |                                               |
|                         v                                               |
|  ( Step 2: Compute Structural Health Score H_canon in [0.0 .. 1.0] )    |
|                         |                                               |
|                         v                                               |
|  [ Emit Typed Health Receipt: NO Execution Authority / Audit Only ]     |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/observability/canon_health.schema.json",
  "title": "AMOS_Canon_Health_Report",
  "type": "object",
  "required": [
    "report_id",
    "timestamp",
    "total_nodes",
    "broken_links_count",
    "invalid_frontmatter_count",
    "unindexed_nodes",
    "overall_health_score",
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
    "total_nodes": {
      "type": "integer",
      "minimum": 1
    },
    "broken_links_count": {
      "type": "integer",
      "minimum": 0
    },
    "invalid_frontmatter_count": {
      "type": "integer",
      "minimum": 0
    },
    "unindexed_nodes": {
      "type": "array",
      "items": { "type": "string" }
    },
    "overall_health_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "status": {
      "type": "string",
      "enum": ["HEALTHY", "DEGRADED", "CRITICAL_GAPS"]
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Non-Authority Law:** Health telemetry is purely descriptive (`OBSERVED != AUTHORIZED`) and cannot execute writes or mutations directly.
2. **Degraded Threshold:** If $\text{broken\_links\_count} > 0 \lor \text{invalid\_frontmatter\_count} > 0$, $\text{status} \ne \text{"HEALTHY"}$.
3. **Health Score Calculation:** $\text{overall\_health\_score} = 1.0 - \frac{\text{broken\_links} + \text{invalid\_frontmatter}}{\text{total\_nodes}}$.

---

## 4. Cross-Plane Bindings

- **Health Check Scripts:** `scripts/obsidian-health-check.sh` · [[K_ANTI_AUTOPOISONING]] · [[LAW_HIERARCHY]]
- **Related Schemas:** [[PROVENANCE_HEALTH_SCHEMA]] · [[FRAMEWORK_NODE_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[11_OBSERVABILITY_MOC]] · [[00_ROOT_MOC]]

