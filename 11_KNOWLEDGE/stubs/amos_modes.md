---
title: "AMOS Modes Master Registry"
type: registry
source: 21_DOMAINS/45_MODES
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/amos_modes.json
  scope: amos_modes
tags:
  - amos-os
  - modes
  - cognitive-modes
---

# AMOS Modes Master Registry

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Operating Modes

```json
{
  "current_mode": "EXPERIMENTAL_BUILD",
  "modes": {
    "SAFE_INTROSPECTION_ONLY": {
      "allow_external_write": false,
      "allow_external_delete": false,
      "max_risk_score": 0.3,
      "description": "Internal analysis, self-repair, diagnostics only. No external side effects."
    },
    "EXTERNAL_WRITE_LOW_RISK": {
      "allow_external_write": true,
      "allow_external_delete": false,
      "max_risk_score": 0.6,
      "description": "Allows low-risk writes to whitelisted locations and outputs. No destructive actions."
    },
    "EXPERIMENTAL_BUILD": {
      "allow_external_write": true,
      "allow_external_delete": false,
      "max_risk_score": 0.9,
      "description": "Build and refactor mode with strict safety checks. No destructive actions outside sandbox."
    }
  }
}
```

## 2. Cross-Plane Bindings

- **Organism Modes:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- **Domain Mapping:** [[21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL|DOMAIN_EXTENSION_PROTOCOL]]

## Scope

`amos_modes` is part of the AMOS OS canonical corpus. Its role is defined by its containing plane and RSCF metadata.

## Invariants

| ID | Invariant |
|----|-----------|
| AMOS_MODES_INV_01 | Content preserves RSCF epistemic classification. |
| AMOS_MODES_INV_02 | Authority is checked before any state-altering claim. |
| AMOS_MODES_INV_03 | Cross-links are valid within the vault graph. |

## Cross References
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|Audit Ledger]]
