---
title: MVCC_CAS — Concurrency & Atomic State Transition Specification
type: kernel-spec
source: 02_KERNEL
tags:
- kernel
- concurrency
- mvcc
- cas
- atomic
- k-mvcc
- k-cas
rscf:
  state: CANON_SPEC
  claim_class: AMOS_SYSTEM_CORE
  provenance: AMOS_KERNEL
---

# MVCC_CAS — Concurrency & Atomic State Transition Specification

Unified specification combining [[02_KERNEL/K_MVCC|K_MVCC]] (multi-version snapshot isolation) and [[02_KERNEL/K_CAS|K_CAS]] (atomic compare-and-swap) to guarantee serializability and zero-drift state progression.

## Related
- [[02_KERNEL/K_MVCC|K_MVCC]] · [[02_KERNEL/K_CAS|K_CAS]] · [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]

---

**MOC:** [[02_KERNEL/03_CAUSAL/03_CAUSAL_MOC|03_CAUSAL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
