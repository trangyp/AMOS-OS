# Upstream mechanisms

All entries are `SOURCE_CLAIM`; AMOS inherits no external authority.

- `opendp/opendp@4198f76830309d4b1501441dceef393ccbaf534a`: typed privacy measurements/accounting and explicit applicability domains. Transfer: accountant-spec and validity-envelope discipline only.
- `google/differential-privacy@061df8a0fb156ae4d6eec105e4c2c9cc2ae1ac55`: explicit DP event/accounting composition objects. Transfer: cumulative accountant/event composition structure only.
- `OpenLineage/OpenLineage@5cd8884b46a3957ab07e463a959692eaed33e949`: lineage facets and event/capture-time identity. Transfer: origin lineage and freshness identity only.
- AMOS PR #25 exact head `f5023571d48c51048ac990c78e1a07bd58a4eae4`: caller-specific authorization and commit-time freshness separation. Transfer: exposure control must not mint authority and must bind authorization evidence.

`POLICY_UNIT_SUM` is an AMOS MODEL reference accountant. It is not a differential-privacy mechanism, epsilon accountant, information-theoretic leakage theorem, or empirical reconstruction-risk model.
