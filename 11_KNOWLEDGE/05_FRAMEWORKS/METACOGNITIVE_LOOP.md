---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Metacognitive Loop
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

# Metacognitive Loop & Epistemic Self-Monitoring

`METACOGNITIVE_LOOP.md` is the canonical Knowledge Plane reference artifact for the **Metacognitive Loop & Epistemic Self-Monitoring System** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It provides reflective oversight over active reasoning processes, detecting repetitive reasoning loops, epistemic drift, overconfidence, and premature convergence.

______________________________________________________________________

## 1. Metacognitive Loop Flow

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

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Mind OS Master:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_MIND_OS_FRAMEWORK|AMOS_MIND_OS_FRAMEWORK]]
- **Logic Scaffold:** [[11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK|QLS_FRAMEWORK]] and [[11_KNOWLEDGE/05_FRAMEWORKS/QCLA_MASTER|QCLA_MASTER]]
- **Executable Brain Model:** `07_SKILLS/executable-brain-model/SKILL`
- **Full Architecture:** `11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE`

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_MIND_OS_FRAMEWORK|AMOS_MIND_OS_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK|QLS_FRAMEWORK]] · `11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE`

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
