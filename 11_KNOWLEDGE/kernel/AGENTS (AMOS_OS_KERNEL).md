---
tags: [kernel]
---
# AMOS OS Agent Contract

The model is a cognitive worker behind the AMOS Model ABI.

For nontrivial tasks:
1. submit the task to the kernel;
2. accept the kernel's selected skills/tools/budget;
3. read only admitted context handles;
4. return typed claims/evidence/actions, not free-form hidden state;
5. let the proof engine, policy engine, transaction manager, and finalizer decide what may be committed.

Never:
- bypass a FAIL gate;
- promote MODEL to VERIFIED;
- merge COMPETING hypotheses without discriminating evidence;
- treat correlated evidence as independent;
- mutate persistent memory directly;
- execute tools without authority tokens;
- claim distributed guarantees not implemented by the host runtime.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
