# Formal contract

Let an authorization object `A` contain:

- `Act(A)`: finite allowed action set.
- `Res(A)`: finite resource-scope prefixes.
- `Recip(A)`: finite recipient/audience set.
- `I(A)=[nb(A), exp(A)]`: validity interval.
- `U(A)`: maximum cumulative uses.
- `K(A)`: consequence ceiling on an ordered tier lattice.
- `P(A)`: optional parent authorization.
- policy/revocation epochs and external signature-evidence state.

For child `C` and parent `P`, define the AMOS attenuation predicate:

`Atten(C,P)` iff all of the following hold:

1. `Act(C) subseteq Act(P)`.
2. Every `r in Res(C)` lies within at least one `p in Res(P)` under the runtime's segment-aware prefix relation.
3. `Recip(C) subseteq Recip(P)`.
4. `nb(P) <= nb(C) <= exp(C) <= exp(P)`.
5. `U(C) <= U(P)`.
6. `K(C) <= K(P)`.
7. `issuer(C) = subject(P)`.
8. policy identity/version is unchanged and delegation depth does not exceed the parent's declared bound.

A request is eligible only when the leaf subject and requested action/resource/recipient/consequence match, every chain object is temporally valid and unrevoked, cumulative budgets remain available, identity evidence is authenticated, current policy/revocation state is known, and any required signature evidence is externally verified.

`PREFLIGHT_ALLOW` is not durable authority. Commit calls repeat the same checks inside an immediate transaction and reserve one use on every authorization object in the chain before returning `ALLOW`.

Authorization rows carry an `object_hash`; delegation and evaluation recompute the hash before trusting stored scope fields. A mismatch fails closed.

## Signature boundary

The local runtime never performs cryptographic verification. `VERIFIED_EXTERNAL` is admissible only with verifier id, verifier version and evidence reference. That evidence can satisfy a declared signature requirement, but `SIGNATURE_VERIFIED != POLICY_VALID` remains invariant.
