---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Master
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

# UBI Master Specification

`UBI_MASTER.md` is the canonical Knowledge Plane reference artifact for the **UBI Master System** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It coordinates biological intelligence across diagnostic scoring, real-time wearable telemetry, multi-species functional modes, and AMOS OS control-plane governors.

______________________________________________________________________

## 1. Master Control Grid

```text
               ┌────────────────────────────────────────────────────────┐
               │                  UBI MASTER SYSTEM                     │
               └───────────────────────────┬────────────────────────────┘
                                           │
         ┌───────────────────┬─────────────┴─────┬───────────────────┐
         ▼                   ▼                   ▼                   ▼
DIAGNOSTIC SCORING     WEARABLE TELEMETRY   CROSS-SPECIES MODES  OS CONTROL PLANE
• • `UBI_WEARABLE_     • `UBI_CROSS_      • Paces token generation
• Evaluates 4 domains  FRAMEWORK`             SPECIES_FUNCTIONAL_ • Blocks cognitive fatigue
• Pinpoints bottlenecks• Live HRV & EMG        MODES`             • Sustains flow state
```

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Framework:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]] and [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]
- **Diagnostic Scoring:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]]
- **Wearable Telemetry:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_WEARABLE_FRAMEWORK|UBI_WEARABLE_FRAMEWORK]]

______________________________________________________________________

## 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_ubi_master
  node_type: master
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "UBI Master System"
    role: "Central coordination for biological scoring, wearable telemetry, and OS control-plane pacing"
  M:
    subsystems: [diagnostic_scoring, wearable_telemetry, cross_species_modes, os_control_plane]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
