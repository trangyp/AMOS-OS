---
name: amos-information-exposure-auditor
description: Audit AMOS information-exposure changes for canonical-origin accounting, coalition budgets, proof-join coherence, and authority separation.
---

Audit changed exposure-control surfaces. Require:

- canonical semantic-origin resolution before charging;
- duplicate aliases aggregated before accounting;
- all load-bearing origins charged;
- exact accountant identity and validity envelope;
- no use of policy exposure units as differential-privacy epsilon;
- cross-Skill proof joins bound to one effect/policy/authority/environment/capability/proof epoch;
- atomic multi-origin reservation;
- metadata-only observability;
- `AuthorizationAllow != ExposureAllow` and `ExposureReceipt != EffectCommitted` preserved.

Fail closed on unresolved origin identity, missing proof, mixed epochs, unsupported accountant semantics, or stale policy state.
