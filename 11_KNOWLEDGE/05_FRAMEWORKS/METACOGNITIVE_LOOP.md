---
title: Metacognitive Loop
type: cognition
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: METACOGNITIVE_LOOP.md
artifact_id: amos_11_knowledge_05_frameworks_metacognitive_loop
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: FRAMEWORK
path: 11_KNOWLEDGE/05_FRAMEWORKS/METACOGNITIVE_LOOP.md
tags:
- amos-os
- knowledge
- vault
- 11_knowledge
- 05_frameworks
- metacognitive_loop
- metacognition
- loop_detection
- self_reflection
- epistemic_monitoring
- rscf
- canon_candidate
- canon/knowledge
- amos-mind-os-framework
- qls-framework
- qcla-master
- 00-home
- knowledge-moc
- 05-frameworks-moc
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
  - BOOK_THE_99_PCT_MIND_FROM_BRAIN_MYTHS_TO_META_INTEL
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_FRAMEWORKS
  - METACOGNITION
  - SOURCE_DEFINED_MODEL
framework_binding:
  mind_os:
    artifact:
    - - AMOS_MIND_OS_FRAMEWORK
  logic_scaffold:
    artifact:
    - - QLS_FRAMEWORK
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  metacognitive_rules: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# Metacognitive Loop & Epistemic Self-Monitoring

`METACOGNITIVE_LOOP.md` is the canonical Knowledge Plane reference artifact for the **Metacognitive Loop & Epistemic Self-Monitoring System** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It provides reflective oversight over active reasoning processes, detecting repetitive reasoning loops, epistemic drift, overconfidence, and premature convergence.

---

# 1. Metacognitive Loop Flow

```text
PRIMARY INFERENCE / REASONING CHAIN
                 │
                 ▼
METACOGNITIVE REFLECTIVE MONITOR
├── Loop Detection: Flags circular argumentation & repetitive prompt echo
├── Calibration Check: Enforces confidence ceilings (Confidence <= min(Premises))
├── Competing Hypothesis Audit: Prevents premature branch pruning (QLS Pillar II)
└── Epistemic Boundary Enforcer: Validates MODEL != OBSERVATION
                 │
                 ▼
CORRECTIVE STEERING / SAFE STATE COMMIT
```

---

# 2. Inter-Plane & Vault Connections

- **Mind OS Master:** [[AMOS_MIND_OS_FRAMEWORK]]
- **Logic Scaffold:** [[QLS_FRAMEWORK]] and [[QCLA_MASTER]]
- **Executable Brain Model:** `07_SKILLS/executable-brain-model/SKILL`
- **Full Architecture:** `11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE`

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_metacognitive_loop
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "Metacognitive Loop"
    role: "Reflective oversight, loop detection, and epistemic calibration for inference engines"
  M:
    capabilities: [loop_detection, calibration_check, competing_hypothesis_audit, boundary_enforcement]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[05_FRAMEWORKS_MOC]] · [[AMOS_MIND_OS_FRAMEWORK]] · [[QLS_FRAMEWORK]] · `11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE`

---
**MOC:** [[05_FRAMEWORKS_MOC]]
