---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Task Handoff Protocol
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# Task Handoff Protocol Specification

## 1. Purpose

The Task Handoff Protocol formalizes the exact sequence, data structures, and validation rules required when an orchestrator or parent agent delegates a subtask to a specialist worker agent. This protocol ensures that delegated work maintains full provenance, respects authority boundaries, and produces verifiable execution receipts.

```text
CORE INVARIANT:
───────────────
AgentCapability != AgentAuthority
Delegation transfers CAPABILITY scope only
Authority remains with the delegating control-plane chain
```

## 2. Handoff Lifecycle & Sequence

```text
[Orchestrator]                             [Specialist Worker]
      |                                              |
      | 1. Generate Task Capsule                     |
      |    (Objective, Scope, Invariants, Budget)    |
      |--------------------------------------------->|
      |                                              | 2. Validate Preconditions &
      |                                              |    Verify Authority Token
      |                                              |
      | 3. Acknowledge & Bind Working State          |
      |<---------------------------------------------|
      |                                              | 4. Execute Bounded Routine
      |                                              |
      | 5. Return Execution Receipt & Proof Capsule  |
      |<---------------------------------------------|
      |                                              |
      | 6. Validate Receipt & Ingest Output          |
      |                                              |
```

### 2.1 Detailed Phase Descriptions

**Phase 1 — Task Capsule Generation:**
The orchestrator constructs a typed task capsule containing the objective, scope boundaries, required invariants, resource budget, and authority token. The capsule is the single source of truth for the delegated work.

**Phase 2 — Precondition Validation:**
The worker agent validates:
- Authority token authenticity and scope coverage
- Required input artifacts exist and are fresh
- Dependency closure is satisfied
- No material conflicts with concurrent work
- Budget and timeout are sufficient

**Phase 3 — Working State Binding:**
The worker acknowledges receipt and binds its local working state to the task capsule. This creates a causal link: all worker actions are now attributable to the parent task.

**Phase 4 — Bounded Execution:**
The worker executes within the declared scope, maintaining:
- Provenance chain for all intermediate conclusions
- Epistemic class preservation (no silent upgrades)
- Budget consumption tracking
- Failure mode detection

**Phase 5 — Receipt Generation:**
The worker emits a structured execution receipt containing all outputs, intermediate nodes, citations, budget consumption, and any encountered anomalies.

**Phase 6 — Receipt Validation:**
The orchestrator validates the receipt against the original task capsule, checking scope compliance, invariant preservation, and output quality.

## 3. Capsule Structure

```yaml
task_id: "TASK-2026-09-04-00129"
parent_task_id: "ORCH-TASK-8812"
delegating_agent: "amos-orchestrator-alpha"
target_agent: "amos-qfm-specialist-01"
objective: "Verify mathematical proof of Lemma 4.2 in singularity paper"
confidence_ceiling: 0.95
max_token_budget: 4000
timeout_seconds: 30
rscf_scope: "22_RESEARCH/01_MATHEMATICS"
required_invariants:
  - "M04: SOURCE_CLAIM != VERIFIED"
  - "M14: TEST_PASS != UNIVERSAL_PROOF"
input_references:
  - "[[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY]]"
authority_token: "AUTH-GR-88912-EXP-20260904"
```

### 3.1 Capsule Field Definitions

| Field | Type | Description |
| :--- | :--- | :--- |
| `task_id` | UUID | Unique identifier for this task instance |
| `parent_task_id` | UUID | Causal parent (for nested delegation chains) |
| `delegating_agent` | Agent ID | Identity of the delegating orchestrator |
| `target_agent` | Agent ID | Identity of the assigned worker |
| `objective` | String | Declarative goal statement |
| `confidence_ceiling` | Float [0,1] | Maximum confidence the worker may claim |
| `max_token_budget` | Integer | Computational resource limit |
| `timeout_seconds` | Integer | Wall-clock execution limit |
| `rscf_scope` | Path | RSCF namespace boundary for the work |
| `required_invariants` | List | Invariants the worker must preserve |
| `input_references` | List[Link] | Wikilinks to required input artifacts |
| `authority_token` | Token | Scoped, time-limited authority grant |

## 4. Execution Receipt Structure

```yaml
receipt_id: "RCP-2026-09-04-00129"
task_id: "TASK-2026-09-04-00129"
worker_agent: "amos-qfm-specialist-01"
status: "COMPLETED"
execution_time_ms: 1247
tokens_consumed: 3842
outputs:
  - artifact: "[[22_RESEARCH/01_MATHEMATICS/LEMMA_4_2_VERIFICATION]]"
    conclusion_class: "DERIVED"
    confidence: 0.91
intermediate_nodes:
  - node_id: "INT-001"
    source: "arXiv:2503.00016"
    claim: "Time-irreversible quantum-classical dynamics"
    epistemic_class: "SOURCE_CLAIM"
invariants_preserved:
  - "M04: SOURCE_CLAIM != VERIFIED ✓"
  - "M14: TEST_PASS != UNIVERSAL_PROOF ✓"
budget_consumption:
  tokens: 3842
  percentage: 96.05
anomalies: []
```

## 5. Invariants

- **Non-Escalation**: The target agent cannot grant itself additional scopes or tools. Authority flows downward only.
- **Strict Provenance**: The returning receipt must include all intermediate nodes and citations used during execution.
- **Fail-Closed**: If the target agent encounters an unresolvable contradiction, it must emit a structured `UNKNOWN/GAP` record rather than hallucinating a resolution.
- **Budget Enforcement**: If the worker exceeds `max_token_budget`, execution is terminated and a partial receipt is returned.
- **Timeout Enforcement**: If execution exceeds `timeout_seconds`, the worker is terminated and the orchestrator receives a timeout receipt.
- **Scope Containment**: All worker actions must remain within the declared `rscf_scope`. Out-of-scope writes are rejected.

## 6. Failure Modes & Recovery

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| Worker unreachable | Timeout on Phase 3 acknowledgment | Reassign to backup worker, or escalate |
| Authority token expired | Phase 2 validation failure | Reject task, request fresh token from control plane |
| Budget exceeded | Runtime budget monitor | Terminate, return partial receipt |
| Invariant violation | Receipt validation Phase 6 | Reject receipt, quarantine worker, escalate |
| Worker crash | Missing Phase 5 receipt within timeout | Terminate, reassign, log failure |
| Scope creep detected | Post-execution audit | Reject out-of-scope artifacts, quarantine |

## 7. Nested Delegation

Workers may further delegate subtasks, creating a delegation tree:

```text
ORCH-TASK-8812 (Orchestrator)
├── TASK-001 (QFM Specialist)
│   ├── TASK-001a (Sub-worker A)
│   └── TASK-001b (Sub-worker B)
├── TASK-002 (Literature Agent)
└── TASK-003 (Verification Agent)
```

**Constraint:** The delegation depth is bounded by `MAX_DELEGATION_DEPTH` (default: 3). Beyond this, escalation to human oversight is required.

---

## 8. Failure Recovery & Rollback

### 8.1 Failure Classification

```yaml
failure_classification:
  recoverable_failures:
    - type: "TIMEOUT"
      detection: "Worker does not acknowledge within timeout_seconds"
      recovery: "Retry with fresh worker; preserve task capsule"
      rollback: "None — task not yet started"
    
    - type: "PARTIAL_COMPLETION"
      detection: "Worker returns receipt with status=PARTIAL"
      recovery: "Orchestrator re-delegates remaining work"
      rollback: "None — partial results preserved"
    
    - type: "BUDGET_OVERFLOW"
      detection: "Worker exceeds max_token_budget"
      recovery: "Terminate worker; return partial receipt"
      rollback: "Rollback worker's local state to pre-task snapshot"
  
  unrecoverable_failures:
    - type: "INVARIANT_VIOLATION"
      detection: "Receipt validation Phase 6 detects invariant breach"
      recovery: "Reject receipt; quarantine worker; escalate to control plane"
      rollback: "Rollback all artifacts modified by worker to pre-task state"
    
    - type: "SCOPE_CREEP"
      detection: "Post-execution audit finds out-of-scope writes"
      recovery: "Reject out-of-scope artifacts; quarantine worker"
      rollback: "Rollback all out-of-scope writes"
    
    - type: "PROVENANCE_TAMPERING"
      detection: "Receipt contains modified provenance chains"
      recovery: "Reject receipt; quarantine worker; escalate to security"
      rollback: "Rollback all artifacts; preserve tampering evidence"
```

### 8.2 Rollback Protocol

```yaml
rollback_protocol:
  triggers:
    - "Receipt validation failure"
    - "Invariant violation detected"
    - "Scope creep detected"
    - "Provenance tampering detected"
  
  procedure:
    step_1: "Identify all artifacts modified by worker"
    step_2: "For each artifact, locate pre-task snapshot"
    step_3: "Verify snapshot integrity (hash check)"
    step_4: "Restore artifacts to pre-task state"
    step_5: "Invalidate all dependent descendants"
    step_6: "Generate rollback receipt"
    step_7: "Notify affected downstream tasks"
    step_8: "Quarantine worker pending investigation"
  
  rollback_receipt:
    rollback_id: "RB-2026-09-04-001"
    task_id: "TASK-2026-09-04-00129"
    worker_agent: "amos-qfm-specialist-01"
    artifacts_affected: 3
    artifacts_restored: 3
    descendants_invalidated: 7
    rollback_reason: "INVARIANT_VIOLATION"
    rollback_authority: "CONTROL_PLANE"
    rollback_timestamp: "2026-09-04T10:35:00Z"
```

### 8.3 Compensation Protocol

When rollback is not possible (e.g., external side effects), compensation is used:

```yaml
compensation_protocol:
  triggers:
    - "External API call cannot be undone"
    - "File already shared with external party"
    - "Network request already sent"
  
  procedure:
    step_1: "Classify side effect as compensable or non-compensable"
    step_2: "If compensable → execute compensation action"
    step_3: "If non-compensable → log as PERMANENT_SIDE_EFFECT"
    step_4: "Generate compensation receipt"
    step_5: "Escalate non-compensable effects to human oversight"
  
  compensation_types:
    - "inverse_action: Undo the original action if possible"
    - "notification: Notify affected parties of the change"
    - "rollback_external: Request external system rollback"
    - "accept_permanent: Accept and document the permanent effect"
```

---

## 9. Delegation Chain Integrity

### 9.1 Chain Properties

| Property | Description | Enforcement |
| :--- | :--- | :--- |
| **Causal Lineage** | Every task traces back to an orchestrator | parent_task_id chain |
| **Authority Monotonicity** | Authority never increases down the chain | Authority scope checked at each level |
| **Budget Conservation** | Child budgets ≤ parent budget | Budget allocation validated |
| **Scope Containment** | Child scope ⊂ parent scope | Scope validated at delegation |
| **Depth Limit** | Chain depth ≤ MAX_DELEGATION_DEPTH | Hard limit enforced |

### 9.2 Chain Validation

```yaml
chain_validation:
  validation_points:
    - "On delegation: validate child scope ⊂ parent scope"
    - "On delegation: validate child budget ≤ parent budget"
    - "On delegation: validate authority scope ≤ parent authority"
    - "On receipt: validate all invariants preserved"
    - "On receipt: validate provenance chain unbroken"
  
  chain_integrity_check:
    method: "Walk delegation chain from leaf to root"
    checks:
      - "Every task has valid parent_task_id"
      - "No circular delegation (depth limit prevents this)"
      - "Authority tokens are valid at each level"
      - "Budget allocations are consistent"
    failure_action: "Quarantine affected chain; escalate to control plane"
```

### 9.3 Chain Compression

When delegation chains become deep, intermediate results can be compressed:

```yaml
chain_compression:
  trigger: "Chain depth > 2"
  method: "Merge intermediate receipts into single composite receipt"
  constraints:
    - "All intermediate provenance preserved"
    - "All intermediate invariants validated"
    - "Compression receipt includes full chain lineage"
  benefit: "Reduces receipt size; simplifies downstream validation"
```

---

## 10. Cross-Vault References

- [[06_AGENTS/AGENTS_AGENT_CONTRACT|AGENT_CONTRACT]]
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|COORDINATION_AVOIDANCE_PROTOCOL]]
- [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]] — Task executions recorded as episodes
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Task receipts feed observability
