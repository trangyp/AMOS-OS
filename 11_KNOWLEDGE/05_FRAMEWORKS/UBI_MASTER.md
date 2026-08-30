---
title: UBI Master
type: biology
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: UBI_MASTER.md
artifact_id: amos_11_knowledge_05_frameworks_ubi_master
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: MASTER
path: 11_KNOWLEDGE/05_FRAMEWORKS/UBI_MASTER.md
tags:
- amos-os
- knowledge
- vault
- 05_frameworks
- ubi_master
- biological_master
- four_domains
- governance
- rscf
- canon_candidate
- canon/knowledge
- ubi-framework
- amos-ubi-super-engine
- ubi-score-framework
- unified-biological-intelligence
- ubi-wearable-framework
version: 1.0.0
updated: '2026-08-27'
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: NOT_INDEPENDENTLY_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_INGESTION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
  - UBI_OFFICIAL_MANUAL
  - UNIFIED_BIOLOGICAL_INTELLIGENCE
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_FRAMEWORKS
  - BIOLOGICAL_MASTER
  - SOURCE_DEFINED_MODEL
framework_binding:
  framework:
    artifact:
    - - UBI_FRAMEWORK
  super_engine:
    artifact:
    - - AMOS_UBI_SUPER_ENGINE
  score_framework:
    artifact:
    - - UBI_SCORE_FRAMEWORK
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  master_rules: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# UBI Master Specification

`UBI_MASTER.md` is the canonical Knowledge Plane reference artifact for the **UBI Master System** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It coordinates biological intelligence across diagnostic scoring, real-time wearable telemetry, multi-species functional modes, and AMOS OS control-plane governors.

---

# 1. Master Control Grid

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

---

# 2. Inter-Plane & Vault Connections

- **Framework:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]] and [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]
- **Diagnostic Scoring:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]]
- **Wearable Telemetry:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_WEARABLE_FRAMEWORK|UBI_WEARABLE_FRAMEWORK]]

---

# 3. RSCF Contract

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

---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

---
**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
