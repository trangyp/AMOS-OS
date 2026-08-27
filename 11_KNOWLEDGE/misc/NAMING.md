---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: naming
tags: [canon-group/tech-ai, canon/protocol, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/naming, misc]
created: 2026-08-22
---

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://unios.trang.system/schema/law-definition.json",
  "title": "Universe OS Law Definition",
  "description": "Canonical law + pattern-code definition for Universe OS",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Z]{2}-[0-9]{4}$"
    },
    "part": {
      "type": "integer",
      "minimum": 1,
      "maximum": 7
    },
    "section": {
      "type": "number",
      "minimum": 1.0,
      "maximum": 7.99
    },
    "canonical_name": {
      "type": "string",
      "minLength": 1
    },
    "pattern_code": {
      "type": "string",
      "pattern": "^(B|Q|C|S|M|I|E|T|D)[0-9]+$"
    },
    "short_display": {
      "type": "string",
      "minLength": 1
    },
    "description": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": ["DRAFT", "ACTIVE", "DEPRECATED"]
    },
    "version": {
      "type": "string",
      "pattern": "^v[0-9]+\\.[0-9]+\\.[0-9]+$"
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "uniqueItems": true
    },
    "links": {
      "type": "object",
      "properties": {
        "parent_ids": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[A-Z]{2}-[0-9]{4}$" },
          "uniqueItems": true
        },
        "child_ids": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[A-Z]{2}-[0-9]{4}$" },
          "uniqueItems": true
        },
        "depends_on_ids": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[A-Z]{2}-[0-9]{4}$" },
          "uniqueItems": true
        }
      },
      "additionalProperties": false
    },
    "equation": {
      "type": "string"
    },
    "examples": {
      "type": "array",
      "items": { "type": "string" }
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    },
    "author": {
      "type": "string"
    }
  },
  "required": ["id", "part", "canonical_name", "pattern_code", "short_display", "status", "version"],
  "additionalProperties": false
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
