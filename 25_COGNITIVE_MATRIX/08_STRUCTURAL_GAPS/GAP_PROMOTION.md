---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Promotion
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# GAP_PROMOTION — Receipt-Gated Coverage Promotion

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Promotion operates only on the active structural stage chain:

`CONTRACT_ONLY -> IMPLEMENTED_BOUNDED -> VALIDATED_BOUNDED -> GOVERNED_BOUNDED`.

## Gates

A candidate stage must satisfy its cumulative receipts:
- `IMPLEMENTED_BOUNDED`: implementation receipt;
- `VALIDATED_BOUNDED`: implementation + validation receipts;
- `GOVERNED_BOUNDED`: implementation + validation + governance receipts.

Promotion may not decrease stage.

## Exception-state firewall

`STALE`, `COMPETING`, `FALSIFIED`, and `QUARANTINED` are not erased by calling promotion. Recovery requires a newly evidenced record through the appropriate repair/governance path.

```text
STALE + NEW_TIMESTAMP != VALIDATED
COMPETING + PREFERRED_SOURCE != RESOLVED
FALSIFIED + RETRY != TRUE
QUARANTINED + LOCAL_PASS != ADMITTED
```

## Authority boundary

The reference promotion function validates structural receipts only. It does not grant canon authority or durable-effect authority. Production promotion must bind exact receipt identity, freshness, provenance, policy/authority epoch, and commit-time control-plane gates.

[[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_THRESHOLDS|COVERAGE_THRESHOLDS]] · [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]]
