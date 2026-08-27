---
title: "C401–C500: System Dynamics Constraints (Data Quality, Knowledge, Epistemics)"
created: "2026-08-22"
origin: "AMOS brain knowledge ingest"
origin_architect: "AMOS"
type: "reference"
tags: [canon-group/tech-ai, canon/metric, rscf/claim, rscf/provenance, rscf/state/observation, topic/c401-c500-system-dynamics-constraints, system]
status: "active"
provenance: "OBSERVATION"
confidence: "VERIFIED"
source: "Ingest batch 2026-08-22"
---

# C401–C500: System Dynamics Constraints

50 system dynamics constraints (C401–C500) across three groups: Data Quality & Analytics Correctness, Knowledge/Documentation/Memory, Epistemics/Dissent/Opacity.

---

## Group E1 — Data Quality & Analytics Correctness (C401–C430)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C401 | DQ_Increases_With_GC | Data quality increases with governance control |
| C402 | DQ_Increases_With_AQ | Data quality increases with audit quality |
| C403 | DQ_Increases_With_OB | Data quality increases with observability |
| C404 | DQ_Decreases_With_MP | Data quality decreases with misconfiguration pressure |
| C405 | DQ_Decreases_With_OP | Data quality decreases with operational pressure |
| C406 | DQ_Decreases_With_CF | Data quality decreases with config drift |
| C407 | LowDQ_Raises_IR | Low DQ raises incident rate |
| C408 | LowDQ_Raises_CP | Low DQ raises cost of production (misallocation) |
| C409 | LowDQ_Raises_OP | Low DQ raises operational pressure (data distrust → backchannels) |
| C410 | DQ_Amplifies_DecisionError | Higher DQ decreases decision error amplification |
| C411 | DQ_Amplifies_Bypass | Higher DQ decreases bypass slope |
| C412 | DataDrift_Regime | DataDrift regime |
| C413 | DQ_Control_Requires_OB | DQ control requires observability under churn |
| C414 | DQ_Control_Requires_GC | DQ control requires governance control |
| C415 | DQ_LoopGain | Loop gain of DQ subsystem |
| C416 | Stabilizer_GC_OB | GC + OB stabilizer |
| C417 | HighDQ_Improves_RES | High DQ improves resilience (via better CD/EB control) |
| C418 | HighDQ_Lowers_CR | High DQ lowers cost of risk |
| C419 | DQ_Threshold_CostSpiral | Below DQ threshold, CostSpiral risk rises |
| C420 | DQ_Boundedness | DQ remains bounded (not noise-driven) |
| C421 | DQ_Saturation | DQ saturation: analytics-driven errors minimal |
| C422 | MP_Shock_Lowers_DQ | Misconfiguration shock lowers DQ |
| C423 | OP_Shock_Lowers_DQ | Operational pressure shock lowers DQ |
| C424 | CF_Shock_Lowers_DQ | Config drift shock lowers DQ |
| C425 | DQ_Requires_DF | DQ requires documentation fidelity under model changes |
| C426 | DQ_Requires_VR | DQ requires version control |
| C427 | DQ_Improves_EI | DQ improves epistemic integrity |
| C428 | DQ_Reduces_Bypass_Slope | Higher DQ decreases bypass slope |
| C429 | DQ_Stability_Exit | Exit DataDrift regime |
| C430 | DataIntegrity_Global | System-level decision noise bounded |

---

## Group E2 — Knowledge, Documentation & Memory (C431–C460)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C431 | DF_Increases_With_CB | Documentation fidelity increases with change bandwidth |
| C432 | DF_Increases_With_RS | DF increases with release stability |
| C433 | DF_Increases_With_GC | DF increases with governance control |
| C434 | DF_Decreases_With_MP | DF decreases with misconfiguration |
| C435 | DF_Decreases_With_CC | DF decreases with change churn |
| C436 | DF_Decreases_With_IR | DF decreases with incident rate (firefighting) |
| C437 | LowDF_Raises_TK | Low DF raises tribal knowledge burden |
| C438 | HighTK_Raises_MTTR | High tribal knowledge raises MTTR |
| C439 | KnowledgeLockIn_Regime | KnowledgeLockIn regime |
| C440 | DF_Improves_VR | DF improves version control |
| C441 | DF_Improves_DR | DF improves deployment reliability |
| C442 | DF_Reduces_Bypass | DF reduces bypass |
| C443 | KnowledgeLoopGain | Loop gain of knowledge subsystem |
| C444 | Stabilizer_RS_GC | RS + GC stabilizer |
| C445 | DF_Threshold_Attrition | Below DF threshold, attrition rises |
| C446 | DF_Boundedness | DF remains bounded under churn |
| C447 | DF_Saturation | DF saturation (idealized limit) |
| C448 | MP_Shock_Lowers_DF | MP shock lowers DF |
| C449 | IR_Shock_Lowers_DF | IR shock lowers DF |
| C450 | DF_ExitCondition | Exit KnowledgeLockIn regime |
| C451 | TK_Raises_OP | TK raises operational pressure |
| C452 | DF_Reduces_OP | DF reduces operational pressure |
| C453 | DF_Improves_EI | DF improves epistemic integrity |
| C454 | DF_Improves_RES | DF improves resilience |
| C455 | LowDF_Raises_CR | Low DF raises cost of risk (via MTTR/IR) |
| C456 | DF_Requires_CB | DF requires change bandwidth |
| C457 | DF_Requires_RS | DF requires release stability (investment unsustained) |
| C458 | DF_Requires_GC | DF requires governance control (decays under churn) |
| C459 | DF_Reduces_CF_Indirectly | DF reduces config drift indirectly |
| C460 | KnowledgeStability_Global | System knowledge stability bounded |

---

## Group E3 — Epistemics, Dissent & Opacity (C461–C500)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C461 | DT_Increases_With_RS | Dissent tolerance increases with release stability |
| C462 | DT_Increases_With_GC | DT increases with governance control |
| C463 | DT_Increases_With_EI | DT increases with epistemic integrity |
| C464 | DT_Decreases_With_SRC | DT decreases with source control |
| C465 | DT_Decreases_With_OP | DT decreases with operational pressure |
| C466 | OP_Increases_With_MP | Operational pressure increases with misconfiguration |
| C467 | OP_Increases_With_SRC | OP increases with source control |
| C468 | OP_Increases_With_PA | OP increases with perceived authority asymmetry |
| C469 | OP_Decreases_With_VR | OP decreases with version control |
| C470 | OP_Decreases_With_RS | OP decreases with release stability |
| C471 | OP_Decreases_With_GC | OP decreases with governance control |
| C472 | EpistemicCollapse_Regime | EpistemicCollapse regime |
| C473 | LowDT_Raises_DI | Low dissent tolerance raises decision inertia |
| C474 | HighOP_Raises_Bypass | High OP raises bypass |
| C475 | HighOP_Lowers_VR | High OP lowers version control |
| C476 | EpistemicLoopGain | Loop gain of epistemic subsystem |
| C477 | Stabilizer_RS_GC_VR | RS + GC + VR stabilizer |
| C478 | HighDT_Improves_EI | High dissent tolerance improves epistemic integrity |
| C479 | HighDT_Improves_RES | High DT improves resilience |
| C480 | OP_Threshold_Cascade | Above OP threshold, cascade sensitivity rises |
| C481 | OP_Threshold_CostSpiral | Above OP threshold, CostSpiral risk rises |
| C482 | OP_Boundedness | OP remains bounded unless RS forces transparency |
| C483 | DT_Boundedness | DT remains bounded |
| C484 | OP_Shock_Amplifies_MP | OP shock amplifies misconfiguration (panic escalation) |
| C485 | DT_Shock_Dampens_MP | DT shock dampens misconfiguration |
| C486 | OP_Raises_CR | OP raises cost of risk (hidden risk) |
| C487 | DT_Lowers_CR | DT lowers cost of risk |
| C488 | OP_Raises_Attrition | OP raises attrition |
| C489 | DT_Reduces_Attrition | DT reduces attrition |
| C490 | OP_Raises_PA | OP raises perceived authority asymmetry |
| C491 | DF_Reduces_PA | DF reduces perceived authority asymmetry |
| C492 | EI_Requires_DT | Epistemic integrity requires dissent tolerance |
| C493 | EI_Requires_VR | EI requires version control |
| C494 | EpistemicExitCondition | Exit EpistemicCollapse regime |
| C495 | EpistemicStability_Global | Bounded high epistemic stability |
| C496 | OP_Raises_CF | OP raises config drift (shadow changes) |
| C497 | OP_Raises_SSR | OP raises supply chain risk (hidden supply risk) |
| C498 | DT_Raises_CD | DT raises change density |
| C499 | DT_Raises_VR | DT raises version control |
| C500 | EpistemicIntegrity_Global | System-level decision noise bounded |

---

## Key Regime Thresholds

| Regime | Trigger | Exit Condition |
|--------|---------|----------------|
| DataDrift (C412) | DQ below threshold | DQ stability restored (C429) |
| KnowledgeLockIn (C439) | DF below threshold | DF exit condition met (C450) |
| EpistemicCollapse (C472) | DT low + OP high | EpistemicExitCondition (C494) |

## Stabilizer Triads

| Triad | Components | Role |
|-------|-----------|------|
| GC + OB | Governance Control + Observability | DQ control under churn |
| RS + GC | Release Stability + Governance Control | DF control + knowledge stability |
| RS + GC + VR | Release Stability + GC + Version Control | Epistemic stability |

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
