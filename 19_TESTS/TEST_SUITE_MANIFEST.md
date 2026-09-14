---
title: AMOS OS Test Suite Evidence Manifest
type: test_manifest
origin_architect: Trang Phan
steward: Trang Phan
status: CONDITIONAL
epistemic_class: AMOS_MODEL
---

# AMOS OS Test Suite Evidence Manifest

This manifest is the human-readable view of `19_TESTS/EVAL_EVIDENCE_REGISTRY.json`.

The machine-readable registry is authoritative for evaluation-evidence classification. It is validated by `07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py`.

## Protected distinctions

`TEST_SPECIFIED != TEST_EXECUTED`

`TEST_EXECUTED != TEST_REPRODUCIBLE`

`TEST_PASS != TRUTH`

`MODEL_TEST != PRODUCTION_RUNTIME_TEST`

`SAMPLED_FORMULAS != COMPLETE_FORMAL_PROOF`

`RECEIPT_PRESENT != HARNESS_PRESENT`

`BENCHMARK_SCORE != DEPLOYMENT_VALIDITY`

A result may be promoted only to the narrowest conclusion licensed by its harness, receipt, environment, source identity, raw outcome, and explicit non-coverage.

## Evidence classes

Use the benchmark-forensics evidence classes:

- `CONCEPTUAL_DESIGN` — a test or architecture is specified but not executed.
- `SYNTHETIC_SCENARIO` — an illustrative/simulated scenario was run but is not evidence about a deployed runtime.
- `EXECUTED_MODEL` — executable reference/model logic was run.
- `EXECUTED_RUNTIME` — the identified runtime artifact was actually run in a bound environment.
- `UNKNOWN` — the available evidence does not establish a stronger class.

## Verdicts

- `VERIFIED_TESTED_SCOPE` — exact tested scope has executable, reproducible evidence sufficient for that bounded claim.
- `PARTIAL` — useful executed evidence exists but the evidence envelope or coverage is incomplete.
- `INVALIDATED_EVIDENCE` — the prior evidence cannot support the claimed conclusion.
- `CONCEPTUAL_ONLY` — design/specification only.
- `NON_REPRODUCIBLE` — a historical result/receipt exists but the active evidence set cannot reproduce it.
- `UNKNOWN` — unresolved.

## Current registry summary

| Suite | Evidence | Verdict | Bounded interpretation |
| --- | --- | --- | --- |
| `TS-AUTHZ-02` | `EXECUTED_MODEL` | `PARTIAL` | In-tree reference harness + receipt record 17/17 selected authorization probes; original environment/commit were not fully bound. |
| `TS-ROUTING-03` | `UNKNOWN` | `NON_REPRODUCIBLE` | Detailed 19/19 historical receipt exists, but the named validator is absent from the active repository. |
| `TS-MATH-04` | `UNKNOWN` | `NON_REPRODUCIBLE` | Verification report is preserved, but no executable harness/raw evidence is bound and the visible report does not independently establish all 137 formulas. |
| `TS-ARROW-06` | `CONCEPTUAL_DESIGN` | `CONCEPTUAL_ONLY` | Active specification contains performance/runtime claims but is not an executed benchmark receipt. |
| `TS-ZK-07` | `CONCEPTUAL_DESIGN` | `CONCEPTUAL_ONLY` | Security architecture is a design specification, not executed cryptographic/runtime validation. |

Do not replace these verdicts with `PASS` unless the machine registry can be updated with the required evidence and passes validation.

## Evaluation architecture

Evaluation should be split into independent lanes:

1. **Deterministic contract tests** — schemas, invariants, authority firewalls, state machines, validators.
2. **Trajectory/process evaluations** — tool choice, handoff quality, recoverability, wasted steps, authority/process compliance.
3. **Adversarial/red-team evaluations** — prompt/tool poisoning, privilege escalation, data exfiltration, stale state, replay, ambiguous effects.
4. **Model-dependent quality evaluations** — semantic quality, factuality, judge-based scoring; these require calibration and must not become hard truth automatically.
5. **Runtime/performance benchmarks** — latency, throughput, resource usage; require exact runtime, hardware/environment, workload and raw measurements.
6. **Production/deployment validation** — field behavior and operational validity; cannot be inferred from offline/model tests.

External tooling such as Promptfoo may be used as a test runner or red-team generator when useful, but framework output remains evidence input to AMOS rather than an authority or truth source.

## Promotion requirements

Before a suite can receive `VERIFIED_TESTED_SCOPE`, bind all of:

- exact target artifact identity;
- in-tree or immutable harness identity;
- executed receipt identity;
- exact source/artifact hashes;
- environment/runtime versions;
- inputs/seeds/workload when applicable;
- raw or recomputable result counts;
- explicit non-coverage;
- failure traces for failed cases;
- validity/invalidation conditions.

If any load-bearing item is unavailable, downgrade to the narrowest supported verdict instead of filling the gap narratively.

## Machine validation

```bash
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py \
  19_TESTS/EVAL_EVIDENCE_REGISTRY.json \
  --repo .
```

The validator also computes Git blob hashes for bound harness/receipt files and rejects stale evidence identities.

## External source pattern

The 2026 scan inspected `promptfoo/promptfoo` for reusable evaluation/red-team patterns: CLI/CI evaluation, adversarial testing, model comparison and local/private execution. AMOS imports the separation of evaluation lanes and CI-friendly test execution, not product claims or benchmark authority.

## Cross-plane bindings

- [[19_TESTS/TESTS_TEST_CONTRACT|Test Contract]]
- `19_TESTS/EVAL_EVIDENCE_REGISTRY.json`
- `07_SKILLS/amos-interactive-evaluation-design-rscf/SKILL.md`
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|Observability]]
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane]]
