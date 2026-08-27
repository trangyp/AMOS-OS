---
tags: ['cognitive_matrix', 'index', 'note']
---

# AMOS Cognitive Matrix Architecture

The matrix is the cognitive coordinate system of AMOS OS.

```text
CognitiveCell(P,O,C,S)
    ↓
resolve primitive semantics
    ↓
resolve lifecycle operation
    ↓
apply control-plane requirements
    ↓
translate H/M/L scale
    ↓
bind candidate kernels/agents/skills/workflows
    ↓
validate evidence/provenance/dependencies
    ↓
authorize effect class
    ↓
execute / observe / learn
```

It does not replace `01_CANON`, `02_KERNEL`, `03_CONTROL_PLANE`, `04_RUNTIME`,
`06_AGENTS`, `07_SKILLS`, or `08_WORKFLOWS`. It provides the coordinate layer that
allows those systems to be composed without confusing role, capability, lifecycle,
authority, or scale.

---

[[00_ROOT_MOC|AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: cognitive_matrix_architecture
node_type: note
path: 25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_ARCHITECTURE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
