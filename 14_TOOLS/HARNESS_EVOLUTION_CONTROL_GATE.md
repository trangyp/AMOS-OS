---
title: AMOS Harness Evolution Control Gate
type: tool
status: IMPLEMENTED_LOCAL_REFERENCE
epistemic_class: AMOS_MODEL
origin_architect: Trang Phan
---

# AMOS Harness Evolution Control Gate

**Tool ID:** `amos-harness-evolution-control`  
**Tier:** T1 local deterministic validation.

## Capability mask

`HARNESS_SURFACE_INVENTORY_VALIDATE | MUTATION_MANIFEST_VALIDATE | BASELINE_HASH_BIND_VALIDATE | EVALUATION_ISOLATION_AUDIT | EVALUATION_RECEIPT_BIND | EVALUATOR_RELIABILITY_BIND | HARNESS_MUTATION_VERDICT | ROLLBACK_RECEIPT_VALIDATE | RECONCILIATION_AUDIT | HARNESS_EVOLUTION_LEDGER_VERIFY`

## Executable binding

- Runtime: `07_SKILLS/amos-observability-driven-harness-evolution-rscf/scripts/harness_evolution_runtime.py`
- Receipt validator: `07_SKILLS/amos-observability-driven-harness-evolution-rscf/scripts/harness_evolution_contract_check.py`
- Regression tests: `19_TESTS/test_harness_evolution_runtime.py`

The T1 implementation stores only bounded hashes/identifiers/booleans/sets in its local SQLite reference state. It does not edit harness files, run model evaluations, write branches, merge pull requests, execute rollback, deploy code, or promote canon.

## Input evidence

- declared mutable-surface inventory;
- baseline and candidate harness versions;
- mutation evidence/root-cause hashes;
- pre-evaluation predicted fix/regression sets;
- verifier-isolation evidence;
- PR19-compatible run/comparison receipts;
- PR22-compatible held-out calibration report and reliability gate;
- post-effect reconciliation evidence when another authorized path applies/declines a recommendation.

## Output

- mutation receipt;
- isolation receipt;
- `KEEP|ROLLBACK|INCONCLUSIVE` decision receipt;
- reconciliation receipt;
- tamper-evident ledger verification.

## Firewalls

- `MUTATION_MANIFEST != FILE_WRITE`
- `KEEP_RECOMMENDATION != MERGE_AUTHORITY`
- `ROLLBACK_RECOMMENDATION != ROLLBACK_EXECUTION`
- `NEXT_ROUND_DELTA != CAUSAL_PROOF`
- `COMPARABLE_RUNS != DEPLOYMENT_VALIDITY`
- `CALIBRATION_PASS != GROUND_TRUTH`
- `RECONCILIATION_OBSERVED != ACTION_AUTHORIZED`
- `HASH_MATCH != SEMANTIC_CORRECTNESS`

Any actual repository mutation is a separate T4 effect and requires its own authority witness.
