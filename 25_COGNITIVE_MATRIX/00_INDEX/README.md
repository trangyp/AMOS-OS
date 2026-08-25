# AMOS Cognitive Matrix

**Origin architect / steward:** Trang Phan  
**Class:** AMOS architecture / matrix runtime specification

This package turns the AMOS Cognitive Architecture Matrix into an addressable OS coordinate system.

## Address

`CELL_<Primitive>_<Operation>_<ControlPlane>_<Scale>`

Example:

`CELL_L10_O08_C04_H`

means:

World Modeling × Prediction × Reasoning Control Plane × High scale.

## Cardinality

30 primitives × 17 lifecycle operations × 9 control planes × 3 scales = **13,770 cells**.

## Critical separation

CANON != KERNEL != PRIMITIVE != AGENT != SKILL != WORKFLOW != CONTROL_PLANE

A cell does not claim implementation merely because a candidate kernel/agent/skill/workflow can be routed to it.
Each binding is `UNVALIDATED_BINDING` until validated by tests and provenance.
