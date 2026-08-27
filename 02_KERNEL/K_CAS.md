---
title: "K_CAS — Compare-And-Swap State Transition Kernel"
type: kernel
source: 02_KERNEL
tags: [kernel, cas, state_transition, atomicity, rscf]
rscf:
  state: CANON_SPEC
  claim_class: AMOS_SYSTEM_CORE
  provenance: AMOS_KERNEL
---

# K_CAS — Compare-And-Swap State Transition Kernel

 enforces atomic state updates: a proposed transition  	o S_{t+1}$ succeeds if and only if the current state exactly matches the expected preimage $.

## Invariant
3689	ext{CAS}(S_t, S_{	ext{expected}}, S_{	ext{proposed}}) = egin{cases} S_{	ext{proposed}} & 	ext{if } S_t = S_{	ext{expected}} \ 	ext{REJECT}(	ext{StateConflict}) & 	ext{otherwise} \end{cases}3689

## Related
- [[K_MVCC]] · [[MVCC_CAS]] · [[02_KERNEL_MOC]]
