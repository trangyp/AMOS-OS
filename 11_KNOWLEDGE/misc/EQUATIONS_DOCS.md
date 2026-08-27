---
title: EQUATIONS DOCS
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
