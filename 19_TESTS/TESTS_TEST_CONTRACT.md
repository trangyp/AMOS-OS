---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Tests Test Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# TESTS TEST CONTRACT

## 0. Status

Tests-plane contract for **TEST CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; implementation PARTIAL.

## 1. Scope

Governs test taxonomy, coverage declarations, negative coverage, and receipts as they bear on `TEST CONTRACT`. Bounded by dependency closure: conclusions inherit the weakest load-bearing premise.

## 2. Contract terms

- **Typed artifacts** — every artifact declares artifact_type, epistemic class, scope, regime.
- **Firewalls preserved** — CAPABILITY ≠ AUTHORITY · PROPOSAL ≠ COMMIT · OBSERVED ≠ CURRENT · TEST_PASS ≠ TRUTH.
- **Epochs distinct** — state_version ≠ causal_epoch ≠ policy_epoch ≠ provenance_epoch unless an explicit mapping licenses equivalence.
- **Local finality requires proof** — demonstrated dependency closure may avoid coordination; assumed independence may not.
- **Selective invalidation** — failure invalidates dependent descendants only; unrelated state is preserved.

## 3. Invariants

- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.
- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- Consequential effects emit receipts; rollback basin exists before mutation.
- Competing hypotheses remain visible when evidence does not discriminate.

## 4. Executed reference

No subsystem-local executor yet. Existing executed validators for the OS: routing-policy validator 19/19 ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]) and authz invariant engine 17/17 ([[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]) — cited as pattern, not as evidence for this artifact.

## 5. Gaps

Runtime enforcement, persistence binding, and empirical validation remain OPEN (UNKNOWN/GAP). Promotion beyond AMOS_MODEL requires the promotion-gate checklist plus an executed receipt specific to this contract.

## 6. Falsifiers

F1: canonical source defines different semantics for this surface. F2: an executed test contradicts a declared invariant. F3: this contract silently collapses a protected firewall.

## Worked semantics

Given an operation touching `TESTS · TEST CONTRACT` within the Tests plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
1. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
1. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
1. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
1. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
1. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

## 7. Test Specification Format

### 7.1 Required Sections

Every test specification must include:

```yaml
test_spec_required_sections:
  identity:
    - "test_id: string (unique)"
    - "version: string (semantic)"
    - "category: enum[UNIT, INTEGRATION, CONTRACT, PROPERTY, ADVERSARIAL, FAILURE_RECOVERY, RUNTIME, REGRESSION, INVARIANT]"
  
  purpose:
    - "description: string (what is verified)"
    - "rationale: string (why this matters)"
    - "epistemic_class: OBSERVATION"
  
  preconditions:
    - "environment: string (where test runs)"
    - "dependencies: list[string]"
    - "authority_required: list[string]"
  
  inputs_and_outputs:
    - "inputs: list[{name, type, value}]"
    - "expected_outputs: list[{name, type, value}]"
  
  assertions:
    - "assertion: string (what must hold)"
    - "type: enum[EQUALS, CONTAINS, SATISFIES, NOT, THROWS]"
  
  non_coverage:
    - "not_covered: list[string] (what is explicitly not tested)"
  
  falsifiers:
    - "falsifier: string (what would invalidate the result)"
```

### 7.2 Assertion Model

```yaml
assertion_model:
  assertion_types:
    EQUALS:
      description: "Actual value equals expected value"
      example: "result.status == 'COMPLETED'"
    CONTAINS:
      description: "Actual value contains expected value"
      example: "result.errors CONTAINS 'schema_violation'"
    SATISFIES:
      description: "Actual value satisfies predicate"
      example: "result.latency_ms SATISFIES <= 5000"
    NOT:
      description: "Actual value does not match expected"
      example: "result.epistemic_class NOT == 'VERIFIED'"
    THROWS:
      description: "Execution raises expected error"
      example: "invoke() THROWS PermissionDeniedError"
  
  assertion_failure_handling:
    on_failure:
      - "Record assertion failure with actual value"
      - "Capture stack trace"
      - "Classify result as FAILED"
      - "Generate failure receipt"
    epistemic_class: "UNKNOWN/GAP"
```

### 7.3 Negative Case Specification

```yaml
negative_case_spec:
  required_negative_cases:
    missing_input:
      description: "Required input omitted"
      expected: "Test fails gracefully"
    malformed_input:
      description: "Input has wrong structure or types"
      expected: "Test fails with validation error"
    stale_input:
      description: "Input is from outdated version"
      expected: "Test fails with version mismatch"
    unauthorized_input:
      description: "Input lacks required authority"
      expected: "Test fails with authority error"
    boundary_input:
      description: "Input at boundary of valid range"
      expected: "Test passes (boundary is valid)"
    overflow_input:
      description: "Input exceeds valid range"
      expected: "Test fails with range error"
```

---

## 8. Assertion Model (Extended)

### 8.1 Weighted Assertions

Not all assertions carry equal weight. Assertions are classified by criticality:

| Weight Class | Description | Failure Action | Examples |
| :--- | :--- | :--- | :--- |
| **W1 — Critical** | Violation indicates system failure | BLOCK promotion | Invariant violation, data corruption |
| **W2 — High** | Violation indicates component failure | BLOCK merge | Contract violation, schema mismatch |
| **W3 — Medium** | Violation indicates behavioral deviation | WARN; investigate | Performance degradation, minor deviation |
| **W4 — Low** | Violation indicates cosmetic issue | LOG; no action | Formatting, naming inconsistency |

### 8.2 Assertion Confidence

Each assertion carries a confidence level based on strength:

```yaml
assertion_confidence:
  formula: "confidence = specificity * evidence_weight"
  specificity:
    high: "1.0 — Assertion is precise and unambiguous"
    medium: "0.7 — Assertion is somewhat general"
    low: "0.4 — Assertion is vague"
  evidence_weight:
    single_pass: "0.6 — One test run"
    multiple_pass: "0.8 — Multiple consistent test runs"
    cross_environment: "0.9 — Verified in multiple environments"
    formal_proof: "1.0 — Mathematically proven"
```

---

## 9. Test Reporting

### 9.1 Result Classification

```yaml
result_classification:
  PASS:
    description: "All assertions satisfied"
    epistemic_class: "OBSERVATION"
    confidence: "Bounded by assertion confidence"
  
  FAIL:
    description: "At least one assertion violated"
    epistemic_class: "UNKNOWN/GAP"
    action: "Record failure with full context"
  
  PARTIAL:
    description: "Some assertions satisfied, some not"
    epistemic_class: "UNKNOWN/GAP"
    action: "Record partial results; classify pass/fail per assertion"
  
  SKIPPED:
    description: "Test not executed"
    epistemic_class: "SOURCE_CLAIM"
    reason: "Precondition not met, environment unavailable"
  
  TIMEOUT:
    description: "Test exceeded time limit"
    epistemic_class: "UNKNOWN/GAP"
    action: "Terminate test; record timeout receipt"
```

### 9.2 Report Structure

```yaml
test_report:
  report_id: "TR-2026-09-04-001"
  test_suite: "routing-policy-validation"
  run_id: "RUN-2026-09-04-00129"
  timestamp: "2026-09-04T10:30:00Z"
  
  summary:
    total_tests: 19
    passed: 19
    failed: 0
    skipped: 0
    pass_rate: 1.0
    execution_time_ms: 1247
  
  results:
    - test_id: "IT-2026-09-04-001"
      status: "PASS"
      assertions_passed: 5
      assertions_failed: 0
      execution_time_ms: 12
  
  coverage:
    code_coverage: 0.92
    requirement_coverage: 1.0
    invariant_coverage: 1.0
    negative_case_coverage: 0.95
  
  environment:
    runtime: "AMOS_KERNEL_v4.4"
    os: "darwin"
    resources: { ... }
```

### 9.3 Receipt Generation

Every test run generates a validation receipt:

```yaml
validation_receipt:
  receipt_id: "VR-2026-09-04-001"
  test_suite: "routing-policy-validation"
  result: "PASS"
  certificates:
    - "19/19 tests passed"
    - "Coverage targets met"
    - "No invariant violations"
  falsifiers_checked:
    - "No test promoted UNKNOWN to PASS"
    - "No test violated declared invariant"
  confidence:
    ceiling: 0.95
    achieved: 0.92
  validity_window: "until next code change or environment change"
```

---

## 10. Failure Modes (Extended)

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Flaky test** | Intermittent pass/fail | Investigate; quarantine; fix | MEDIUM |
| **Test environment mismatch** | Result differs across environments | Align environments; document drift | HIGH |
| **Test specification error** | Wrong expected output | Correct specification; re-run | HIGH |
| **Coverage gap** | Coverage below target | Add tests to close gap | MEDIUM |
| **False pass** | Test passes but system broken | Audit test adequacy; strengthen | CRITICAL |
| **Test timeout** | Exceeds configured limit | Optimize test; increase timeout | LOW |

---

## 11. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]
- Protocol validated — [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]]
- Interface validated — [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
- Tool validated — [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_19_tests_tests_test_contract_md
node_type: note
path: 19_TESTS/TESTS_TEST_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]
