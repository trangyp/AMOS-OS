---
tags: [misc]
---
# Kernel Equations

These are operational AMOS control equations unless otherwise noted.

`H_(t+1) = Repair(Observe(Execute(Plan(H_t))))`

`Admit(x) = AND_i I_i(x)`

`Conf(C) <= min Conf(load-bearing premises)`

`Invalid(p) => invalidate(load-bearing descendants of p)`

`ExecSufficient = Runs ∧ TestsPass ∧ RequiredOutputsPresent ∧ NoCriticalRegression`

`SemanticSufficient = ExecSufficient ∧ SpecificationMatched ∧ AssumptionsValid`

`LocalSafe = DependencyClosure ∧ ProvenanceSufficient ∧ ScopeFit ∧ RegimeFit ∧ FreshnessFit ∧ NonConflict ∧ BoundedConsequence`

`MayAct = Capability ∧ Authority ∧ ScopeFit ∧ EvidenceGate ∧ ConstraintPass`

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
