# Upstream mechanisms

All external material is `SOURCE_CLAIM`. AMOS does not inherit deployment or policy authority from these projects.

- Cedar `cedar-policy/cedar@2f4019fd645cc8d4a4c0c1f8bd0280c77d754e28`: explicit principal/action/resource authorization request, permit/forbid effects, deny-oriented decision semantics.
- OpenFGA `openfga/openfga@73591ef16ce508623920d5b706286ffcdfb6841b`: relationship-based Check request, explicit authorization-model identity, request context/contextual tuples included in check identity.
- OPA `open-policy-agent/opa@c9acbf66d24210aef939f93f3660352c4840caa7`: external policy/data decision separation and bundle manifest revision concepts.
- SPIRE `spiffe/spire@963e8338c6b14ed9512dd42c14530f0486929c8e`: workload identity/SVID and delegated identity mechanisms, reinforcing that authenticated identity is distinct from action authorization.

AMOS additions are local model constraints: issuer-authored portable objects, only-tightening delegation, cumulative chain budgets, revocation/policy epochs, object hashes, external-signature evidence states, and atomic commit-time revalidation.
