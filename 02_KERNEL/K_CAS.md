---
title: K_CAS — Compare-And-Swap State Transition Kernel
type: kernel
source: 02_KERNEL
tags:
- kernel
- cas
- state_transition
- atomicity
- rscf
- k-mvcc
- mvcc-cas
rscf:
  state: CANON_SPEC
  claim_class: AMOS_SYSTEM_CORE
  provenance: AMOS_KERNEL
---

# K_CAS — Compare-And-Swap State Transition Kernel

 enforces atomic state updates: a proposed transition $S_t \to S_{t+1}$ succeeds if and only if the current state exactly matches the expected preimage $S_{\text{expected}}$.

## Invariant
$$\text{CAS}(S_t, S_{\text{expected}}, S_{\text{proposed}}) = \begin{cases} S_{\text{proposed}} & \text{if } S_t = S_{\text{expected}} \\ \text{REJECT}(\text{StateConflict}) & \text{otherwise} \end{cases}$$

## Related
- [[K_MVCC]] · [[MVCC_CAS]] · [[02_KERNEL_MOC]]

---

**MOC:** [[03_CAUSAL_MOC]] · [[00_HOME]]
