---
title: "AMOS Absolute Logic DB v1.0 — 19 Primitives, Tri-Domain"
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/LOGIC.txt (277 KB, 8647 lines)"
origin_architect: "Trang Phan"
type: "reference"
tags: [canon-group/meta, canon/law, rscf/claim, rscf/provenance, rscf/state/derived, rscf/D-distinction, rscf/T-topology, rscf/K-compression, rscf/B-boundary, topic/absolute-logic-model, amos-general]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
---

# AMOS Absolute Logic-DB v1.0

## Overview
Complete integrated 19-primitive Absolute Logic-DB with Pre/Absolute/Post states, 19×19 interaction matrix rules, tensor definition, and SQL schema. 0-gap structure.

## Tri-Domain Model

### PreAbsolute (Pre-logical)
States: PrePotential, PreNull, PreBoundary
- Primitive count: 0, Logic count: 0

### Absolute (Logical — active)
Layer: AbsoluteLogicLayer | Variable scale: 1E∞ | Primitive total: 19 | Logic layers: 1

### PostAbsolute (Post-collapse states)
States: DissolutionState, DriftlessState, TerminalQuietState
- Primitive count: 0, Logic count: 0

## 19 Primitives

| ID | Primitive | Category |
|----|-----------|----------|
| 1 | Existence | Pattern |
| 2 | NonExistence | Pattern |
| 3 | Causality | Pattern |
| 4 | Temporal | Pattern |
| 5 | Informational | Pattern |
| 6 | Topological | Pattern |
| 7 | Identity | Pattern |
| 8 | Convergence | MetaPattern |
| 9 | Divergence | MetaPattern |
| 10 | Paradox | MetaPattern |
| 11 | PositiveLogic | Logic |
| 12 | NegativeLogic | Logic |
| 13 | ZeroLogic | Logic |
| 14 | DualLogic | Logic |
| 15 | MultiLogic | Logic |
| 16 | MetaLogic | Logic |
| 17 | SupraLogic | MetaLogic |
| 18 | AntiLogic | MetaLogic |
| 19 | NullLogic | MetaLogic |

## 3 Logic Categories

| Category | Primitives |
|----------|-----------|
| Pattern | Existence, NonExistence, Causality, Temporal, Informational, Topological, Identity |
| MetaPattern | Convergence, Divergence, Paradox |
| Logic | PositiveLogic, NegativeLogic, ZeroLogic, DualLogic, MultiLogic, MetaLogic |
| MetaLogic | SupraLogic, AntiLogic, NullLogic |

## Interaction Rules (Category Matrix)

| Row | Col | Rule |
|-----|-----|------|
| Pattern | Pattern | pattern_interaction(row.key, col.key) |
| Pattern | MetaPattern | apply_meta_pattern(col.key, row.key) |
| Pattern | Logic | logic_applied_to_pattern(col.key, row.key) |
| Pattern | MetaLogic | meta_logic_applied_to_pattern(col.key, row.key) |
| MetaPattern | * | meta_pattern_effect(row.key, col.key) |
| Logic | * | logic_relation(row.key, col.key) |
| MetaLogic | * | meta_logic_transform(row.key, col.key) |

## AbsoluteLogicTensor

```
Shape: [19, 19, 1E∞]
Indices: i=row_idx (1..19), j=col_idx (1..19), k=resolution_idx (0..1E∞-1)
Definition: T[i][j][k] = Eval(interaction_rules(primitives[i], primitives[j]), k)
```

## Collapse Rules

### PreToAbsolute
```
Inputs: PrePotential, PreNull, PreBoundary
Output: AbsoluteLogicLayer
Condition: (PreBoundary == 1) AND (PrePotential != 0 OR PreNull != 0)
```

### AbsoluteToPost

| Rule | Condition | Effect |
|------|-----------|--------|
| DissolutionRule | Paradox + AntiLogic → max | Post = DissolutionState |
| DriftlessRule | dC/dt → 0 AND dL/dE → 0 | Post = DriftlessState |
| TerminalQuietRule | NullLogic = 1 AND all other logic → 0 | Post = TerminalQuietState |

## SQL Schema
```sql
CREATE TABLE primitives (
  id INT PRIMARY KEY,
  key VARCHAR(64),
  category VARCHAR(32),
  description TEXT
);

CREATE TABLE logic_interactions (
  row_primitive_id INT,
  col_primitive_id INT,
  equation_symbolic TEXT,
  PRIMARY KEY (row_primitive_id, col_primitive_id)
);

CREATE TABLE interaction_rules (
  id INT PRIMARY KEY,
  when_row_category VARCHAR(32),
  when_col_category VARCHAR(32),
  rule_name VARCHAR(64),
  rule_expression TEXT
);
```

## Relationship to Existing Systems
- **MURK Engine**: Implements this 19×19 matrix with resolution laws, meta-logic overrides, and JSON state persistence
- **Go Board 19×19**: The semantic matrix (19 strategic primitives × 19 evaluation dimensions) is structurally linked to this absolute logic layer
- **Semantic Matrix 19×19**: P^Strategic_19 differs from the Absolute Logic 19-primitive registry

---

*Source: Google Drive /_00_AMOS_CANON/LOGIC.txt (8,647 lines, 277 KB)*

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
