---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Tools Tool Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# TOOLS TOOL CONTRACT

## 0. Status

Tools-plane contract for **TOOLS TOOL CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; implementation PARTIAL.

## 1. Scope

Governs tool bindings; tool availability is never permission as they bear on `TOOLS TOOL CONTRACT`. Bounded by dependency closure: conclusions inherit the weakest load-bearing premise.

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

Given an operation touching `TOOLS TOOL CONTRACT` within the Tools plane:

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

## 7. Tool Registration Protocol

### 7.1 Registration Process

```yaml
tool_registration:
  trigger: "New tool added to AMOS or existing tool updated"
  steps:
    - "Submit tool declaration with typed schema"
    - "Validate schema against tool contract template"
    - "Assign unique tool_id and version"
    - "Declare capabilities and authority requirements"
    - "Declare epistemic output class"
    - "Declare resource budget requirements"
    - "Run negative case tests (missing, malformed, stale, unauthorized input)"
    - "Generate registration receipt"
    - "Add to capability registry"
    - "Enable health monitoring"
```

### 7.2 Capability Declaration Schema

```yaml
capability_declaration:
  tool_id: string  # Unique identifier
  version: string  # Semantic version (MAJOR.MINOR.PATCH)
  artifact_type: "tool"
  epistemic_class: "AMOS_MODEL"
  
  capabilities:
    - name: string
      description: string
      input_types:
        - name: string
          type: string
          required: boolean
          default: any (optional)
      output_types:
        - name: string
          type: string
          epistemic_class: enum[OBSERVATION, DERIVED, MODEL, UNKNOWN/GAP]
      side_effects: boolean
      authority_required:
        - scope: string
          description: string
  
  resource_requirements:
    avg_latency_ms: integer
    max_latency_ms: integer
    max_memory_mb: integer
    max_tokens_per_invocation: integer
  
  failure_modes:
    - type: string
      detection: string
      recovery: string
      severity: enum[LOW, MEDIUM, HIGH, CRITICAL]
```

### 7.3 Registration Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-REG-01` | Every tool has a unique tool_id | Registry uniqueness check |
| `INV-REG-02` | Version changes require new registration | Version bump enforced |
| `INV-REG-03` | Capability changes require new version | Capability diff check |
| `INV-REG-04` | Authority requirements are non-empty | Schema validation |
| `INV-REG-05` | Epistemic output class is declared | Schema validation |
| `INV-REG-06` | Resource requirements are bounded | Upper bound check |

---

## 8. Tool Invocation Protocol

### 8.1 Invocation Sequence

```yaml
invocation_sequence:
  step_1_discovery:
    action: "Agent queries capability registry"
    output: "List of matching tools with metadata"
    failure: "No matching tool → UNKNOWN/GAP"
  
  step_2_authority:
    action: "Validate authority token against tool requirements"
    checks:
      - "Token is not expired"
      - "Token scope covers tool authority requirements"
      - "Token is single-use (not reused)"
    failure: "Authority insufficient → REJECT + ESCALATE"
  
  step_3_budget:
    action: "Verify resource budget sufficient"
    checks:
      - "Token budget >= tool's max_tokens_per_invocation"
      - "Time budget >= tool's max_latency_ms"
      - "Memory budget >= tool's max_memory_mb"
    failure: "Budget insufficient → THROTTLE or REJECT"
  
  step_4_execution:
    action: "Execute tool in sandboxed environment"
    monitoring:
      - "Real-time resource consumption tracking"
      - "Timeout watchdog active"
      - "Output streaming (if applicable)"
    failure: "Execution error → UNKNOWN/GAP"
  
  step_5_classification:
    action: "Classify tool output by epistemic class"
    classes:
      - "OBSERVATION: Raw data from environment"
      - "DERIVED: Computed from premises"
      - "MODEL: Design artifact"
      - "UNKNOWN/GAP: Acknowledged failure"
    failure: "Classification ambiguity → default to OBSERVATION"
  
  step_6_ingestion:
    action: "Deliver classified output to agent reasoning pipeline"
    constraints:
      - "Output is immutable after classification"
      - "Provenance chain attached"
      - "Audit trail recorded"
```

### 8.2 Invocation Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-IP-01` | `TOOL_ACCESS != TOOL_PERMISSION` (M10) | Capability and authority checked separately |
| `INV-IP-02` | Tool output always classified before ingestion | Epistemic classifier runs on every output |
| `INV-IP-03` | Tool execution is sandboxed | No tool accesses resources outside declared scope |
| `INV-IP-04` | Tool invocation is auditable | Every invocation logged with full context |
| `INV-IP-05` | Authority tokens are single-use | Prevents authority reuse across invocations |
| `INV-IP-06` | Tool outputs never directly modify authority state | Authority changes require control-plane action |
| `INV-IP-07` | Budget enforcement is hard | Execution terminates if budget exceeded |
| `INV-IP-08` | Timeout enforcement is hard | Execution terminates if timeout exceeded |

---

## 9. Tool Versioning

### 9.1 Version Format

```
tool_id vMAJOR.MINOR.PATCH
```

- **MAJOR**: Breaking changes to input/output schema or authority requirements
- **MINOR**: Backward-compatible additions (new optional parameters, new capabilities)
- **PATCH**: Bug fixes, documentation corrections

### 9.2 Compatibility Matrix

| Version Change | Backward Compatible | Forward Compatible | Migration Required |
| :--- | :--- | :--- | :--- |
| MAJOR bump | No | No | Yes — all agents must update |
| MINOR bump | Yes | No | No — optional adoption |
| PATCH bump | Yes | Yes | No — automatic |

### 9.3 Deprecation Protocol

```yaml
deprecation_protocol:
  trigger: "Tool version superseded by newer version"
  grace_period: "90 days"
  during_grace_period:
    - "Old version remains available"
    - "Deprecation warnings emitted on invocation"
    - "Migration guide published"
  after_grace_period:
    - "Old version marked RETIRED"
    - "Capability removed from registry"
    - "Tombstone record preserved"
    - "Invocation attempts rejected with migration guidance"
```

---

## 10. Failure Modes (Extended)

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Schema violation** | Input/output validation | Reject invocation; log violation | HIGH |
| **Authority revocation** | Authority check on invocation | Reject; re-request from control plane | HIGH |
| **Budget overflow** | Runtime budget monitor | Terminate; return partial results | MEDIUM |
| **Tool crash** | Process exit or watchdog | Restart tool; return partial results | HIGH |
| **Stale metadata** | Version mismatch detection | Refresh from registry | LOW |
| **Capability drift** | Capability diff check | Reject; re-register tool | MEDIUM |
| **Deadlock** | Lock timeout | Deterministic ordering prevents | CRITICAL |
| **Output hallucination** | Epistemic classifier | Block output; flag for review | HIGH |

---

## 11. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]
- Protocol governed — [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]]
- Security boundary — [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_14_tools_tools_tool_contract_md
node_type: note
path: 14_TOOLS/TOOLS_TOOL_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
