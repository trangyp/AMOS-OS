---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Agent Tool Interaction Protocol
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# Agent-Tool Interaction Protocol Specification

> [!ABSTRACT] Protocol Specification
> Formalizes the exact sequence, validation rules, and safety constraints for agent-to-tool invocation in AMOS. Enforces the invariant `M10: TOOL_ACCESS != TOOL_PERMISSION` at every invocation boundary.

---

## 1. Purpose

Every agent interaction with an external tool must pass through a structured protocol that separates capability (knowing how to use a tool) from authority (being permitted to use it). This protocol ensures:

- No agent can invoke a tool it lacks authority for
- All tool invocations are auditable
- Tool outputs are classified before entering the reasoning pipeline
- Resource consumption is tracked and bounded

---

## 2. Tool Invocation Lifecycle

```text
AGENT REQUIRES TOOL
        │
        ▼
┌─────────────────────────────┐
│ 1. TOOL REQUEST GENERATION  │
│    (Agent emits structured   │
│     tool call with params)   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 2. CAPABILITY CHECK         │
│    (Is tool in agent's       │
│     capability manifest?)    │
│    FAIL → REJECT + LOG      │
└────────────┬────────────────┘
             │ PASS
             ▼
┌─────────────────────────────┐
│ 3. AUTHORITY CHECK          │
│    (Does agent have valid    │
│     authority token for      │
│     this tool + scope?)      │
│    FAIL → REJECT + ESCALATE │
└────────────┬────────────────┘
             │ PASS
             ▼
┌─────────────────────────────┐
│ 4. RESOURCE BUDGET CHECK    │
│    (Token/memory/time budget │
│     sufficient?)             │
│    FAIL → THROTTLE / REJECT │
└────────────┬────────────────┘
             │ PASS
             ▼
┌─────────────────────────────┐
│ 5. SANDBOX EXECUTION        │
│    (Tool executes within     │
│     bounded environment)     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 6. OUTPUT CLASSIFICATION    │
│    (Tool output classified   │
│     by epistemic class)      │
│    OBSERVATION / DERIVED /   │
│    SOURCE_CLAIM              │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 7. OUTPUT INGESTION         │
│    (Classified output enters │
│     agent reasoning pipeline)│
└─────────────────────────────┘
```

---

## 3. Request Structure

```yaml
tool_invocation_request:
  request_id: "TIR-2026-09-04-001"
  agent_id: "amos-qfm-specialist-01"
  tool_id: "obsidian-read-tool"
  tool_version: "2.1.0"
  parameters:
    file_path: "22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY.md"
  authority_token: "AUTH-GR-88912-EXP-20260904"
  resource_budget:
    max_tokens: 4000
    max_time_ms: 5000
    max_memory_mb: 256
  expected_output_class: "OBSERVATION"
  provenance_context:
    parent_task: "TASK-2026-09-04-00129"
    causal_epoch: 4402
```

---

## 4. Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-AT-01` | `TOOL_ACCESS != TOOL_PERMISSION` (M10) | Capability and authority checked separately |
| `INV-AT-02` | Tool output is always classified before reasoning ingestion | Epistemic classifier runs on every tool output |
| `INV-AT-03` | Tool execution is sandboxed | No tool may access resources outside its declared scope |
| `INV-AT-04` | Tool invocation is auditable | Every invocation logged with request, result, and resource usage |
| `INV-AT-05` | Authority tokens are single-use per invocation | Prevents authority reuse across invocations |
| `INV-AT-06` | Tool outputs never directly modify authority state | Authority changes require control-plane action |

---

## 5. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Capability mismatch** | Step 2 check fails | Reject; log unauthorized capability request |
| **Authority expired** | Step 3 token validation fails | Reject; escalate to control plane for re-authorization |
| **Budget exceeded** | Step 4 resource check fails | Throttle or reject; return partial results if available |
| **Tool crash** | Step 5 execution error | Emit `UNKNOWN/GAP`; log tool failure; agent retries or escalates |
| **Output hallucination** | Step 6 classification detects inconsistency | Block output; flag for review; agent must re-invoke or use alternative |

---

## 7. Tool Discovery Protocol

Before an agent can invoke a tool, it must discover available tools and their capabilities.

### 7.1 Tool Registry Query

```yaml
tool_registry_query:
  request_id: "TRQ-2026-09-04-001"
  agent_id: "amos-qfm-specialist-01"
  query_filters:
    capability_domain: "file_system"
    required_permissions: ["read", "write"]
    max_latency_ms: 5000
    epistemic_output_class: "OBSERVATION"
  response:
    - tool_id: "obsidian-read-tool"
      version: "2.1.0"
      capabilities: ["read_file", "read_directory", "read_metadata"]
      authority_requirements: ["file:read:$RSCF_SCOPE"]
      resource_profile:
        avg_latency_ms: 120
        max_memory_mb: 128
        max_tokens: 4000
      epistemic_output: "OBSERVATION"
      status: "AVAILABLE"
    - tool_id: "obsidian-write-tool"
      version: "1.8.0"
      capabilities: ["write_file", "create_file", "delete_file"]
      authority_requirements: ["file:write:$RSCF_SCOPE", "commit:write"]
      resource_profile:
        avg_latency_ms: 250
        max_memory_mb: 256
        max_tokens: 8000
      epistemic_output: "OBSERVATION"
      status: "AVAILABLE"
```

### 7.2 Tool Capability Declaration

Every tool must declare its capabilities in a typed schema:

```yaml
tool_capability_declaration:
  tool_id: "obsidian-read-tool"
  version: "2.1.0"
  artifact_type: "tool"
  epistemic_class: "OBSERVATION"
  
  capabilities:
    - name: "read_file"
      input_types:
        - "file_path: string"
        - "offset: integer (optional)"
        - "limit: integer (optional)"
      output_types:
        - "content: string"
        - "metadata: object"
      side_effects: false
      authority_required: ["file:read"]
    
    - name: "read_directory"
      input_types:
        - "directory_path: string"
      output_types:
        - "entries: list[string]"
      side_effects: false
      authority_required: ["directory:read"]
  
  invariants:
    - "INV-TOOL-01: Tool never modifies external state during read operations"
    - "INV-TOOL-02: Tool output is classified as OBSERVATION"
    - "INV-TOOL-03: Tool respects resource budget constraints"
  
  failure_modes:
    - "FILE_NOT_FOUND: Input path does not exist"
    - "PERMISSION_DENIED: Authority token insufficient"
    - "TIMEOUT: Execution exceeds resource budget"
    - "TOOL_CRASH: Unexpected internal error"
```

### 7.3 Discovery Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-TD-01` | Tool availability is never permission | Tool must be available AND authorized |
| `INV-TD-02` | Tool capabilities are immutable per version | Any capability change requires new version |
| `INV-TD-03` | Tool registry is the single source of truth | Agents must not cache tool metadata beyond session |
| `INV-TD-04` | Deprecated tools remain discoverable during grace period | Grace period metadata included in registry |

---

## 8. Invocation Error Handling

### 8.1 Error Classification

```yaml
error_classification:
  category_1_validation_errors:
    description: "Input does not match tool schema"
    examples:
      - "Missing required parameter"
      - "Wrong type for parameter"
      - "Value outside allowed range"
    recovery: "Reject invocation; return structured error; agent may retry with corrected input"
    epistemic_class: "UNKNOWN/GAP"
  
  category_2_authority_errors:
    description: "Agent lacks authority for this invocation"
    examples:
      - "Authority token expired"
      - "Authority scope insufficient"
      - "Authority revoked during execution"
    recovery: "Reject invocation; escalate to control plane; agent may request fresh authority"
    epistemic_class: "UNKNOWN/GAP"
  
  category_3_resource_errors:
    description: "Resource budget insufficient"
    examples:
      - "Token budget exceeded"
      - "Memory limit exceeded"
      - "Time limit exceeded"
    recovery: "Terminate execution; return partial results if available; agent may re-budget"
    epistemic_class: "UNKNOWN/GAP"
  
  category_4_execution_errors:
    description: "Tool execution failed"
    examples:
      - "File not found"
      - "Network timeout"
      - "Internal tool crash"
    recovery: "Log failure; return error; agent may retry or escalate"
    epistemic_class: "UNKNOWN/GAP"
  
  category_5_output_errors:
    description: "Tool output violates postconditions"
    examples:
      - "Output does not match declared output schema"
      - "Output contains unexpected epistemic class"
      - "Output contradicts tool's declared capability"
    recovery: "Block output; flag for review; agent must re-invoke or use alternative"
    epistemic_class: "UNKNOWN/GAP"
```

### 8.2 Retry Policy

```yaml
retry_policy:
  max_retries: 3
  backoff_strategy: "exponential_with_jitter"
  initial_delay_ms: 100
  max_delay_ms: 5000
  jitter_range: "±20%"
  
  retryable_errors:
    - "TIMEOUT"
    - "TOOL_CRASH"
    - "RESOURCE_TEMPORARILY_UNAVAILABLE"
  
  non_retryable_errors:
    - "PERMISSION_DENIED"
    - "INVALID_INPUT"
    - "INVARIANT_VIOLATION"
    - "SCHEMA_MISMATCH"
  
  escalation_policy:
    after_max_retries: "ESCALATE_TO_CONTROL_PLANE"
    escalation_message:
      tool_id: "obsidian-read-tool"
      failure_count: 3
      last_error: "TIMEOUT"
      context: "TASK-2026-09-04-00129"
```

### 8.3 Timeout Enforcement

```yaml
timeout_enforcement:
  invocation_timeout_ms: 5000
  monitoring:
    granularity: "100ms"
    check_method: "async_watchdog"
  on_timeout:
    step_1: "Send SIGTERM to tool process"
    step_2: "Wait 500ms for graceful shutdown"
    step_3: "If still running → SIGKILL"
    step_4: "Collect partial output if available"
    step_5: "Return TIMEOUT error to agent"
    step_6: "Log timeout event with full context"
```

---

## 9. Output Classification Deep Dive

### 9.1 Classification Rules

Every tool output must be classified before entering the reasoning pipeline:

| Output Type | Classification | Rationale |
| :--- | :--- | :--- |
| File read result | `OBSERVATION` | Raw data from environment |
| API response | `OBSERVATION` | Raw data from external system |
| Tool-internal inference | `DERIVED` | Tool computed from premises |
| Cached result | `OBSERVATION` | Previously observed data, not re-verified |
| Tool error message | `UNKNOWN/GAP` | Acknowledged failure, not data |

### 9.2 Output Postconditions

```yaml
output_postconditions:
  obsidian_read_tool:
    output_class: "OBSERVATION"
    postconditions:
      - "Content is exactly as stored (no transformation)"
      - "Metadata reflects file state at read time"
      - "Timestamp is causal epoch of read operation"
  
  search_tool:
    output_class: "OBSERVATION"
    postconditions:
      - "Results are ranked by relevance score"
      - "Results include source attribution"
      - "Results are not independently verified"
  
  calculation_tool:
    output_class: "DERIVED"
    postconditions:
      - "Result follows from input premises"
      - "Calculation is deterministic given inputs"
      - "Result inherits confidence of input premises"
```

---

## 10. Resource Budget Management

### 10.1 Budget Allocation Model

```yaml
budget_allocation:
  agent_budget_pool:
    total_tokens: 100000
    reserved_for_reasoning: 60000
    available_for_tools: 40000
  
  per_invocation_budget:
    max_tokens: 4000
    max_time_ms: 5000
    max_memory_mb: 256
  
  budget_enforcement:
    pre_check: "Verify budget >= required before invocation"
    runtime_monitoring: "Track consumption during execution"
    post_reconciliation: "Record actual consumption in receipt"
    overage_handling: "Terminate if budget exceeded by >10%"
```

### 10.2 Budget Accounting

```yaml
budget_accounting:
  receipt_fields:
    - "tokens_requested: integer"
    - "tokens_consumed: integer"
    - "tokens_percentage: float"
    - "time_requested_ms: integer"
    - "time_consumed_ms: integer"
    - "memory_peak_mb: float"
    - "budget_violations: list"
```

---

## 11. Concurrency Control

### 11.1 Concurrent Invocation Rules

| Scenario | Rule | Rationale |
| :--- | :--- | :--- |
| Same tool, disjoint inputs | Permitted | No shared state modified |
| Same tool, overlapping inputs | Blocked | Risk of write-write conflict |
| Different tools, same resource | Blocked | Risk of inconsistent state |
| Read-only tools | Permitted concurrently | No state modification |

### 11.2 Lock Protocol

```yaml
lock_protocol:
  resource_locking:
    granularity: "file-level or namespace-level"
    lock_type: "shared_read / exclusive_write"
    timeout_ms: 1000
    deadlock_prevention: "resource ordering by namespace path"
  
  lock_states:
    - "UNLOCKED"
    - "SHARED_READ: one or more readers"
    - "EXCLUSIVE_WRITE: one writer, no readers"
  
  transition_rules:
    - "UNLOCKED → SHARED_READ: when read invoked"
    - "SHARED_READ → SHARED_READ: when another read invoked"
    - "SHARED_READ → EXCLUSIVE_WRITE: when write invoked (waits for all readers)"
    - "EXCLUSIVE_WRITE → UNLOCKED: when write completes"
```

---

## 12. Audit Trail Requirements

Every tool invocation must generate a complete audit trail:

```yaml
audit_trail:
  invocation_record:
    request_id: "TIR-2026-09-04-001"
    agent_id: "amos-qfm-specialist-01"
    tool_id: "obsidian-read-tool"
    tool_version: "2.1.0"
    parameters: { ... }
    authority_token: "AUTH-GR-88912-EXP-20260904"
    timestamp_request: "2026-09-04T10:30:00Z"
    timestamp_start: "2026-09-04T10:30:01Z"
    timestamp_end: "2026-09-04T10:30:02Z"
    status: "COMPLETED"
    output_class: "OBSERVATION"
    budget_consumed:
      tokens: 3842
      time_ms: 1247
      memory_mb: 128
    result_summary: "File read successfully"
    error: null
  
  retention_policy:
    hot_retention: "30 days"
    warm_retention: "1 year"
    cold_retention: "7 years"
    immutable: true
```

---

## 13. Cross-Vault References

- [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
- [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02_CAPABILITY_MOC]]
- [[06_AGENTS/AGENTS_AGENT_CONTRACT|AGENTS_AGENT_CONTRACT]]
- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]]
- [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]] — Tool invocations recorded as episodic traces
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Audit trail feeds observability

---

```RSCF-NODE
node_id: agent_tool_interaction_protocol
node_type: protocol_specification
domain: 09_PROTOCOLS
claim_class: AMOS_MODEL
confidence_ceiling:
  invocation_protocol: high
  authority_enforcement: high
  output_classification: high
  tool_discovery: high
  error_handling: high
  resource_budgeting: high
falsifiers:
  - An agent invokes a tool without passing authority check
  - Tool output bypasses epistemic classification
  - Authority token is reused across invocations
  - Tool registry returns stale tool metadata
  - Retry policy allows indefinite retry without escalation
  - Budget enforcement fails to terminate over-budget execution
```
