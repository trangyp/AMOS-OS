---
title: Portable Agent Authorization Source Registry
type: knowledge
origin_architect: Trang Phan
epistemic_class: DERIVED
---

# Portable Agent Authorization Sources

All upstream mechanisms remain `SOURCE_CLAIM`. AMOS does not inherit external policy, identity, deployment, or enforcement authority.

- `cedar-policy/cedar@2f4019fd645cc8d4a4c0c1f8bd0280c77d754e28`
  - Transfer: explicit principal/action/resource request; permit/forbid decision structure; deny-oriented authorization semantics.
  - Boundary: Cedar policy semantics are not copied wholesale and do not define AMOS authority.
- `openfga/openfga@73591ef16ce508623920d5b706286ffcdfb6841b`
  - Transfer: explicit authorization-model identity plus request context/contextual relationship state for a check.
  - Boundary: relationship-model success is not AMOS commit authority.
- `open-policy-agent/opa@c9acbf66d24210aef939f93f3660352c4840caa7`
  - Transfer: externalized policy/data decision separation and revisioned policy-bundle concepts.
  - Boundary: an OPA decision is evidence from a policy engine, not proof an effect was enforced or committed.
- `spiffe/spire@963e8338c6b14ed9512dd42c14530f0486929c8e`
  - Transfer: workload identity/SVID and delegated identity separation.
  - Boundary: authenticated workload identity does not authorize a particular action.

AMOS-local additions (`AMOS_MODEL`): issuer-authored portable authorization objects, only-tightening delegation, recipient/consequence constraints, cumulative chain budgets, policy/revocation epochs, object hashes, external-signature evidence states, and atomic local commit-time revalidation.

## Non-compensatory boundaries

`IDENTITY != AUTHORIZATION`

`CAPABILITY != AUTHORITY`

`DELEGATION != AUTHORITY_CREATION`

`PREFLIGHT_ALLOW != COMMIT_TIME_ALLOW`

`AUTHORIZATION_DECISION != ENFORCEMENT`

`POLICY_ALLOW != EFFECT_COMMITTED`
