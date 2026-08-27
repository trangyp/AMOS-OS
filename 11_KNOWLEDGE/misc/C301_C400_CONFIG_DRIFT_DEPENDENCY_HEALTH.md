---
title: "C301–C400: Config Drift & Dependency Health (System Dynamics Constraints)"
created: "2026-08-22"
origin: "AMOS brain knowledge ingest"
origin_architect: "AMOS"
type: "reference"
tags: [canon-group/biology, canon/metric, rscf/claim, rscf/provenance, rscf/state/observation, topic/c301-c400-config-drift-dependency-health, misc]
status: "active"
provenance: "OBSERVATION"
confidence: "VERIFIED"
source: "Ingest batch 2026-08-22"
---

# C301–C400: Config Drift & Dependency Health

100 system dynamics constraints (C301–C400) across Config Drift & Change Entropy, Dependency Health & Integration Fragility, Supply Chain Security & Security Posture.

---

## Group D2 — Config Drift & Change Entropy (C301–C340)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C301 | CF_Increases_With_MP | Config drift increases with misconfiguration |
| C302 | CF_Increases_With_CC | CF increases with change churn |
| C303 | CF_Increases_With_TK | CF increases with tribal knowledge burden |
| C304 | CF_Decreases_With_GC | CF decreases with governance control |
| C305 | CF_Decreases_With_AQ | CF decreases with audit quality |
| C306 | CF_Decreases_With_CD | CF decreases with change discipline |
| C307 | HighCF_Raises_IR | High CF raises incident rate |
| C308 | HighCF_Raises_MTTR | High CF raises MTTR |
| C309 | HighCF_Lowers_DQ | High CF lowers data quality |
| C310 | ConfigEntropy_Regime | ConfigEntropy regime |
| C311 | LowGC_Allows_CF_Runaway | Low GC allows CF runaway |
| C312 | CD_Is_Primary_CF_Damper | Change discipline is primary CF damper (if MP not extreme) |
| C313 | AQ_Is_Primary_CF_Damper | Audit quality is primary CF damper |
| C314 | CF_Amplifies_Bypass | CF amplifies bypass (via incidents/oncall) |
| C315 | CF_Amplifies_CC_Sensitivity | CF amplifies change churn sensitivity |
| C316 | CF_Amplifies_DependencyRisk | CF amplifies dependency risk |
| C317 | CF_Amplifies_SecurityRisk | CF amplifies security risk |
| C318 | ConfigDriftLoopGain | Loop gain of config drift subsystem |
| C319 | Stabilizer_GC_CD_AQ | GC + CD + AQ stabilizer |
| C320 | CF_Threshold_CascadeRisk | Above CF threshold, cascade risk elevated |
| C321 | CF_Threshold_CostSpiral | Above CF threshold, CostSpiral risk rises |
| C322 | CF_Boundedness | CF must be bounded (high IR saturates) |
| C323 | CF_Saturation | CF saturation: config contributes ~0 to IR |
| C324 | MP_Shock_Raises_CF | MP shock raises CF (unless CD/AQ high) |
| C325 | OP_Correlates_With_CF | OP correlates with CF (untracked changes) |
| C326 | TK_Correlates_With_CF | TK correlates with CF |
| C327 | DF_Dampens_CF_Indirectly | DF dampens CF indirectly |
| C328 | HighCF_Burns_EB | High CF burns engineering bandwidth |
| C329 | HighCF_Raises_CP | High CF raises cost of production |
| C330 | CF_Raises_MTTD_Indirectly | CF raises MTTD indirectly |
| C331 | CF_Raises_Attrition | CF raises attrition |
| C332 | CF_Reduces_Resilience | CF reduces resilience (via IR/OS/CB) |
| C333 | CF_Requires_Runbooks | CF control requires runbooks (to keep MTTR bounded) |
| C334 | CF_Control_Requires_GC | CF control requires governance control |
| C335 | CF_Control_Requires_CD | CF control requires change discipline (under MP) |
| C336 | CF_Control_Requires_AQ | CF control requires audit quality (under MP) |
| C337 | CF_Control_Requires_CB | CF control requires change bandwidth |
| C338 | CF_Perturbs_DQ | CF perturbs DQ |
| C339 | CF_Perturbs_DH | CF perturbs dependency health |
| C340 | ConfigEntropy_ExitCondition | Exit ConfigEntropy regime |

---

## Group D3 — Dependency Health & Integration Fragility (C341–C380)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C341 | DH_Increases_With_GC | DH increases with governance control |
| C342 | DH_Increases_With_AQ | DH increases with audit quality |
| C343 | DH_Increases_With_SP | DH increases with supply posture |
| C344 | DH_Decreases_With_SSR | DH decreases with supply chain risk |
| C345 | DH_Decreases_With_MP | DH decreases with misconfiguration |
| C346 | LowDH_Raises_IR | Low DH raises incident rate |
| C347 | LowDH_Raises_SSR | Low DH raises supply chain risk |
| C348 | IntegrationFragility_Regime | IntegrationFragility regime |
| C349 | HighMP_Erodes_DH | High MP erodes DH (unless GC high) |
| C350 | DH_Reduces_MTTR | DH reduces MTTR |
| C351 | DH_Reduces_CF_Indirectly | DH reduces CF indirectly |
| C352 | DH_Amplifies_CC_Effects | DH amplifies CC effects |
| C353 | DH_Amplifies_CF_Effects | DH amplifies CF effects |
| C354 | DH_Sensitivity_To_SSR | DH sensitivity to supply chain risk |
| C355 | DH_Sensitivity_To_SP | DH sensitivity to supply posture |
| C356 | DependencyLoopGain | Loop gain of dependency subsystem |
| C357 | Stabilizer_SP_GC | SP + GC stabilizer |
| C358 | DH_Threshold_SecurityCollapse | Above DH threshold, security collapse within 1–2 steps |
| C359 | DH_Threshold_CostSpiral | Above DH threshold, CostSpiral risk rises |
| C360 | DH_Boundedness | DH bounded (sensitivity to CF spikes) |
| C361 | DH_Saturation | DH saturation: dependency contribution to IR minimal |
| C362 | LowDH_Burns_EB | Low DH burns engineering bandwidth |
| C363 | LowDH_Raises_OS | Low DH raises outage severity |
| C364 | LowDH_Raises_Attrition | Low DH raises attrition |
| C365 | LowDH_Raises_OP | Low DH raises operational pressure |
| C366 | GC_Buffers_MP_On_DH | GC buffers MP on DH |
| C367 | AQ_Buffers_MP_On_DH | AQ buffers MP on DH |
| C368 | CD_Indirectly_Protects_DH | CD indirectly protects DH |
| C369 | DF_Protects_DH | DF protects DH |
| C370 | DH_Control_Requires_DF | DH control requires documentation fidelity (under churn) |
| C371 | DH_Control_Requires_VR | DH control requires version control |
| C372 | DH_Control_Requires_CD | DH control requires change discipline |
| C373 | DH_Control_Requires_SP | DH control requires supply posture |
| C374 | DH_Raises_Resilience | DH raises resilience |
| C375 | DH_Lowers_CatastrophicRisk | DH lowers catastrophic risk |
| C376 | DH_Amplifies_SSR_When_OPHigh | DH amplifies SSR when OP high |
| C377 | SupplyChain_Shock | Supply chain shock |
| C378 | DependencyStability_ExitCondition | Exit IntegrationFragility regime |
| C379 | DH_Requires_Governed_Upgrades | DH requires governed upgrades |
| C380 | DependencyRisk_Coordinates_With_CC | Dependency risk coordinates with CC (superlinear) |

---

## Group D4 — Supply Chain Security & Security Posture (C381–C400)

| ID | Name | Constraint (formal) |
|----|------|---------------------|
| C381 | SSR_Increases_With_LowDH | SSR increases with low dependency health |
| C382 | SSR_Increases_With_LowSP | SSR increases with low supply posture |
| C383 | SSR_Increases_With_MP | SSR increases with misconfiguration |
| C384 | SSR_Decreases_With_GC | SSR decreases with governance control |
| C385 | SSR_Decreases_With_AQ | SSR decreases with audit quality |
| C386 | SP_Increases_With_GC | SP increases with governance control |
| C387 | SP_Increases_With_AQ | SP increases with audit quality |
| C388 | SP_Increases_With_RS | SP increases with release stability |
| C389 | SP_Decreases_With_MP | SP decreases with misconfiguration |
| C390 | SP_Decreases_With_CP | SP decreases with cost of production |
| C391 | SP_Decreases_With_SSR | SP decreases with supply chain risk |
| C392 | SecurityCollapse_Regime | SecurityCollapse regime |
| C393 | LowSP_Raises_IR | Low SP raises IR (security incidents) |
| C394 | LowSP_Raises_CP | Low SP raises CP (breach cost) |
| C395 | SupplyChainLoopGain | Supply chain loop gain (runaway if unchecked) |
| C396 | Stabilizer_GC_AQ | GC + AQ stabilizer |
| C397 | SSR_Threshold_IRSpike | Above SSR threshold, IR spike (unless SP high) |
| C398 | MP_Shock_Raises_SSR | MP shock raises SSR |
| C399 | CP_Shock_Lowers_SP | CP shock lowers SP |
| C400 | SecurityExitCondition | Exit SecurityCollapse regime |

---

## Regime Thresholds & Stabilizers

| Regime | Trigger | Exit | Stabilizer Triad |
|--------|---------|------|-----------------|
| ConfigEntropy (C310) | CF above threshold | C340 | GC + CD + AQ (C319) |
| IntegrationFragility (C348) | DH below threshold | C378 | SP + GC (C357) |
| SecurityCollapse (C392) | SSR above threshold | C400 | GC + AQ (C396) |

## Cascade Chain: Config → Dependency → Security

```
CF ↑ → DH ↓ → SSR ↑ → IR spike → SecurityCollapse
        (unless DH stabilizers active)
```

The three subsystems are coupled: config drift degrades dependency health, which increases supply chain risk, which drives security incidents. Each regime has its own threshold and stabilizer triad.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
