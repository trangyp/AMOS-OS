---
title: "C201–C300: Resilience, Operational Stability, Burnout (System Dynamics Constraints)"
created: "2026-08-22"
origin: "AMOS brain knowledge ingest"
origin_architect: "AMOS"
type: "invariant-cluster"
status: "active"
provenance: "OBSERVATION"
confidence: "VERIFIED"
source: "Ingest batch 2026-08-22"
tags: [canon-group/tech-ai, canon/metric, rscf/claim, rscf/provenance, rscf/state/observation, topic/c201-c300-resilience-operational-stabili, misc]
---

# C201–C300: Resilience, Operational Stability, Burnout

100 system dynamics constraints (C201–C300) across Operational Stability & Resilience, Burnout & Sustainable Throughput, Cost Spiral, Resolution Performance, Recovery & On-Call/Toil, Engineering Bandwidth & Effective Buffer, Attrition & Social Fabric.

---

## Group C2 — Operational Stability & Resilience (C201–C230)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C201 | RES_Increases_With_DH | Resilience increases with dependency health |
| C202 | RES_Increases_With_SP | RES increases with supply posture |
| C203 | RES_Increases_With_INS | RES increases with instrumentation/observability |
| C204 | RES_Decreases_With_MP | RES decreases with misconfiguration |
| C205 | RES_Decreases_With_OP | RES decreases with operational pressure |
| C206 | RES_Decreases_With_ImmunityGap | RES decreases when immunity gap widens |
| C207 | LowRES_Raises_IR | Low RES raises incident rate |
| C208 | LowRES_Raises_OS | Low RES raises outage severity |
| C209 | LowRES_Raises_MTTR | Low RES raises MTTR (recovery time) |
| C210 | ResilienceRegime | Resilience regime (system recovery capacity dominant) |
| C211 | LowDH_Lowers_RES | Low dependency health lowers RES |
| C212 | HighOP_Erodes_RES | High operational pressure erodes RES |
| C213 | HighMP_Erodes_RES | High misconfiguration erodes RES |
| C214 | RES_Amplifies_Outcome_Later | RES is delayed benefit (not immediate) |
| C215 | RES_Bounded_Recovery | RES-driven recovery is bounded until root causes fixed |
| C216 | ResilienceLoopGain | Loop gain of resilience subsystem |
| C217 | Stabilizer_DH_SP_INS | DH + SP + INS stabilizer |
| C218 | RES_Threshold_CostSpiral | Below RES threshold, CostSpiral risk rises |
| C219 | RES_Threshold_CascadeRisk | Below RES threshold, cascade risk rises |
| C220 | RES_Boundedness | RES remains bounded (not infinite) |
| C221 | RES_Saturation | RES saturation: further investment yields diminishing returns |
| C222 | MP_Shock_Raises_OS | MP shock raises outage severity |
| C223 | OP_Shock_Raises_OS | OP shock raises outage severity |
| C224 | ResilienceRegimeExit | Exit Resilience regime (stability restored) |
| C225 | RES_Requires_Observability | RES requires observability to guide actions |
| C226 | RES_Requires_Runbooks | RES requires runbooks to execute under stress |
| C227 | RES_Improves_DH | RES improves DH (feedback loop) |
| C228 | RES_Reduces_OS_Indirect | RES reduces outage severity indirectly |
| C229 | RES_Lowers_Attrition_Indirect | RES lowers attrition indirectly |
| C230 | ResilienceStability_Global | System-wide resilience bounded |

---

## Group C3 — Burnout & Sustainable Throughput (C231–C250)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C231 | EB_Increases_With_Skill | EB increases with skill/capability |
| C232 | EB_Increases_With_Inn | EB increases with innovation |
| C233 | EB_Decreases_With_MP | EB decreases with misconfiguration |
| C234 | EB_Decreases_With_OS | EB decreases with outage severity |
| C235 | EB_Decreases_With_IR | EB decreases with incident rate |
| C236 | LowEB_Raises_OS | Low EB raises outage severity |
| C237 | LowEB_Raises_MTTR | Low EB raises MTTR |
| C238 | BurnoutRegime | Burnout regime (sustained load without recovery) |
| C239 | HighOP_Burns_EB | High OP burns EB (throughput optimization eats capacity) |
| C240 | HighIR_Burns_EB | High IR burns EB (context switching) |
| C241 | EB_Prevents_OS_Cascade | EB prevents outage cascade (if available) |
| C242 | EB_LoopGain | Loop gain of EB subsystem |
| C243 | Stabilizer_PR_Inn | PR + Inn stabilizer for EB |
| C244 | EB_Threshold_Burnout | Below EB threshold, burnout risk rises |
| C245 | EB_Boundedness | EB is bounded (finite human capacity) |
| C246 | EB_ExitCondition | Exit Burnout regime |
| C247 | MP_Shock_Reduces_EB | MP shock reduces EB |
| C248 | OP_Shock_Reduces_EB | OP shock reduces EB |
| C249 | EB_Amplifies_RES_Indirect | EB amplifies RES indirectly |
| C250 | BurnoutStability_Global | System burnout risk bounded |

---

## Group C4 — Cost Spiral, Runaway & Escalation (C251–C270)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C251 | CostSpiral_Increases_With_OS | CostSpiral increases with outage severity |
| C252 | CostSpiral_Increases_With_MP | CostSpiral increases with misconfiguration |
| C253 | CostSpiral_Increases_With_CF | CostSpiral increases with config drift |
| C254 | CostSpiral_Increases_With_IR | CostSpiral increases with incident rate |
| C255 | CostSpiral_Decreases_With_DH | CostSpiral decreases with DH |
| C256 | CostSpiral_Decreases_With_SP | CostSpiral decreases with SP |
| C257 | CostSpiral_Decreases_With_RS | CostSpiral decreases with RS |
| C258 | CostSpiral_Decreases_With_INS | CostSpiral decreases with INS |
| C259 | CostSpiral_Regime | CostSpiral regime (fixing one thing creates three new problems) |
| C260 | HighCostSpiral_Lowers_DH | High CostSpiral lowers DH |
| C261 | HighCostSpiral_Lowers_SP | High CostSpiral lowers SP |
| C262 | CostSpiralLoopGain | Loop gain of CostSpiral subsystem |
| C263 | Stabilizer_DH_SEm_RS_INS | DH + SE + RS + INS stabilizer |
| C264 | CostSpiral_Threshold_Cascade | Above CostSpiral threshold, cascade risk rises |
| C265 | CostSpiral_Crosses_Burnout | CostSpiral plus burnout = escalation loop |
| C266 | CostSpiral_ExitCondition | Exit CostSpiral regime |
| C267 | CostSpiral_Improves_With_RepairFocus | CostSpiral improves when repair focus > workaround focus |
| C268 | MP_Correlates_With_CostSpiral | MP correlates with CostSpiral |
| C269 | CF_Correlates_With_CostSpiral | CF correlates with CostSpiral |
| C270 | CostSpiralStability_Global | System CostSpiral risk bounded |

---

## Group C5 — Resolution Performance & MTTR/MTTD (C271–C290)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C271 | RES_Improves_MTTR | RES improves MTTR |
| C272 | DH_Improves_MTTR | DH improves MTTR |
| C273 | SP_Improves_MTTR | SP improves MTTR |
| C274 | RES_Improves_MTTD | RES improves MTTD |
| C275 | DH_Improves_MTTD | DH improves MTTD |
| C276 | Low_INS_Raises_MTTD | Low INS raises MTTD (slower detection) |
| C277 | Low_INS_Raises_MTTR | Low INS raises MTTR (slower diagnosis) |
| C278 | High_OP_Raises_MTTR | High OP raises MTTR (cognitive overload) |
| C279 | High_CF_Raises_MTTR | High CF raises MTTR |
| C280 | MTTR_Priority_Boost | MTTR priority boost (invest more on resolution) |
| C281 | MTTD_Priority_Boost | MTTD priority boost (invest more on detection) |
| C282 | RES_LoopFor_MTTR | MTTR improvement loop bounded |
| C283 | MTTD_Improves_DetectionRegime | MTTD improves detection regime |
| C284 | MTTR_Improves_ResolutionRegime | MTTR improves resolution regime |
| C285 | MTTR_Decreases_OP_Indirect | MTTR decreases OP indirectly (less firefighting) |
| C286 | MTTD_Decreases_OS_Indirect | MTTD decreases OS indirectly |
| C287 | RES_ExitCondition_MTTR | Exit MTTR regime (resolution time bounded) |
| C288 | MTTR_Correlates_With_Outage | MTTR correlates with outage severity |
| C289 | MTTR_Correlates_With_IR | MTTR correlates with IR |
| C290 | ResolutionStability_Global | System resolution performance bounded |

---

## Group C6 — Recovery, On-Call, Toil & Fatigue (C291–C300)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C291 | OS_Raises_OnCall_Hours | OS raises on-call hours |
| C292 | OS_Raises_Toil | OS raises toil (manual work) |
| C293 | OS_Raises_Fatigue | OS raises fatigue |
| C294 | OS_Raises_RecoveryDebt | OS raises recovery debt |
| C295 | RecoveryDebt_Lowers_EB | Recovery debt lowers EB |
| C296 | RecoveryDebt_Lowers_RES | Recovery debt lowers RES |
| C297 | OnCallLoopGain | On-call fatigue loop gain |
| C298 | HighOnCall_Raises_IR_Indirect | High on-call raises IR indirectly (fatigue errors) |
| C299 | Toil_Reduced_With_Automation | Toil reduces with automation (if present) |
| C300 | RecoveryStability_Global | System recovery capacity bounded |

---

## Key Regime Thresholds

| Regime | Trigger | Exit Condition |
|--------|---------|----------------|
| Resilience (C210) | RES below threshold | C224 |
| Burnout (C238) | EB below threshold + OP high | C246 |
| CostSpiral (C259) | OS high + repairs create more problems | C266 |

## Stabilizer Triads

| Triad | Components | Role |
|-------|-----------|------|
| DH + SP + INS | Dependency Health + Supply Posture + Observability | RES control |
| PR + Inn | Productivity + Innovation | EB maintenance |
| DH + SE + RS + INS | Dependency Health + Security + Release Stability + Observability | CostSpiral prevention |

## Cascade Chain: OP → IR → OS → Toil → Burnout → RES↓

```
OP ↑ → IR ↑ → OS ↑ → Toil ↑ → RecoveryDebt ↑ → EB ↓ → RES ↓ → (more OP)
```

The loop is self-reinforcing unless broken by: reduced OP, improved DH/SP, investment in RES/EB, and automation of toil.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
