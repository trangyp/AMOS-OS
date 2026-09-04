---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 14 Tools Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# 14 Tools — Map of Content

> [!ABSTRACT] Tools Plane Executive Summary
> The **Tools Plane** (`14_TOOLS`) governs all deterministic and external capabilities in the AMOS Full Brain OS — filesystem, database, browser, search, compiler, calculator, API, connector, and runtime executor.
> It enforces the **Tool Authority Firewall**:
> $$\text{TOOL\_AVAILABLE} \neq \text{TOOL\_AUTHORIZED}$$
> $$\text{TOOL\_CAPABILITY} \neq \text{TOOL\_PERMISSION}$$

---

## 0. Status
Tools-plane artifact. AMOS_MODEL · CONDITIONAL · implementation PARTIAL.

---

## 1. Tool Taxonomy

### 1.1 By Function Category

| Category | Description | Examples |
| :--- | :--- | :--- |
| **Storage** | Filesystem, database, vault operations | Obsidian read/write, SQL query, blob storage |
| **Retrieval** | Search, query, lookup operations | Vector search, BM25, graph traversal |
| **Computation** | Mathematical, logical, computational operations | Calculator, SMT solver, type checker |
| **Communication** | Network, API, inter-agent messaging | HTTP client, message queue, pub/sub |
| **Transformation** | Data conversion, parsing, serialization | JSON parser, markdown renderer, codec |
| **Verification** | Validation, testing, linting operations | Schema validator, linter, test runner |
| **Integration** | External system connectors | BCI adapter, calendar, email, calendar |

### 1.2 By Authority Level

| Level | Description | Delegation | Examples |
| :--- | :--- | :--- | :--- |
| **L0 — Kernel** | Inherent in kernel logic | No | Type checking, deterministic evaluation |
| **L1 — Canon** | Core law enforcement | No | Invariant verification, epistemic classification |
| **L2 — Control Plane** | Governance tools | Scoped delegation | Authority management, capability registration |
| **L3 — Agent-Local** | Agent-scoped tools | Within capability bounds | File read/write, search, calculation |
| **L4 — External** | Third-party tools | Per-session grants | API connectors, external services |

### 1.3 By Epistemic Output Class

| Class | Tool Output Type | Examples |
| :--- | :--- | :--- |
| `OBSERVATION` | Raw data from environment | File read, API response, search result |
| `DERIVED` | Computed from premises | Calculation result, inference output |
| `MODEL` | Design artifact | Schema definition, template generation |
| `UNKNOWN/GAP` | Acknowledged failure | Error message, timeout, crash report |

---

## 2. Capability Model

### 2.1 Capability Declaration

Every tool must declare its capabilities:

```yaml
tool_capability_declaration:
  tool_id: string
  version: string
  artifact_type: "tool"
  capabilities:
    - name: string
      input_types: list[string]
      output_types: list[string]
      side_effects: boolean
      authority_required: list[string]
      epistemic_output: enum[OBSERVATION, DERIVED, MODEL, UNKNOWN/GAP]
```

### 2.2 Capability vs. Authority

| Concept | Definition | Source | Transferable |
| :--- | :--- | :--- | :--- |
| **Capability** | How to use a tool | Tool declaration | Via tool registry |
| **Authority** | Permission to use a tool | Control plane grant | Scoped delegation only |

The fundamental invariant: **Capability alone never authorizes**. An agent must have both capability (knows how) and authority (permitted to) before invoking a tool.

### 2.3 Capability Registry

```yaml
capability_registry:
  registry_id: "TOOL-CAP-REGISTRY-001"
  version: "1.0.0"
  entries:
    - tool_id: "obsidian-read-tool"
      capabilities: ["read_file", "read_directory", "read_metadata"]
      authority_requirements: ["file:read:$RSCF_SCOPE"]
      status: "ACTIVE"
    - tool_id: "obsidian-write-tool"
      capabilities: ["write_file", "create_file", "delete_file"]
      authority_requirements: ["file:write:$RSCF_SCOPE", "commit:write"]
      status: "ACTIVE"
    - tool_id: "web-search-tool"
      capabilities: ["search_web", "fetch_url"]
      authority_requirements: ["network:read"]
      status: "ACTIVE"
```

---

## 3. Tool Lifecycle

### 3.1 Lifecycle States

```text
DECLARED
    │  Tool registered in capability registry
    │  Schema validated
    ▼
AVAILABLE
    │  Tool passes health check
    │  Resource budget allocated
    ▼
ACTIVE
    │  Tool receiving invocations
    │  Audit trail active
    ▼
THROTTLED
    │  Resource budget near limit
    │  Rate limiting active
    ▼
DEPRECATED
    │  Tool superseded by newer version
    │  Grace period for migration
    ▼
RETIRED
    │  No active invocations
    │  Capability removed from registry
    │  Tombstone preserved
```

### 3.2 Promotion Gate Checklist

- [ ] Typed schema bound to tool artifact
- [ ] Identity + versioning implemented
- [ ] Negative cases covered (missing, malformed, stale, unauthorized input)
- [ ] Authority requirements declared
- [ ] Resource budget specified
- [ ] Epistemic output class declared
- [ ] Failure modes documented
- [ ] Audit trail hooks active
- [ ] At least one validation receipt generated

---

## 4. Tool Invocation Protocol

### 4.1 Invocation Sequence

```text
AGENT REQUIRES TOOL
        │
        ▼
┌─────────────────────────────┐
│ 1. TOOL DISCOVERY           │
│    Query capability registry│
│    Find matching tool       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 2. AUTHORITY CHECK          │
│    Validate authority token │
│    Check scope coverage     │
└────────────┬────────────────┘
             │ PASS
             ▼
┌─────────────────────────────┐
│ 3. RESOURCE BUDGET CHECK    │
│    Verify budget sufficient │
└────────────┬────────────────┘
             │ PASS
             ▼
┌─────────────────────────────┐
│ 4. SANDBOX EXECUTION        │
│    Tool executes in bounded │
│    environment              │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 5. OUTPUT CLASSIFICATION    │
│    Classify output by       │
│    epistemic class          │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ 6. OUTPUT INGESTION         │
│    Classified output enters │
│    reasoning pipeline       │
└─────────────────────────────┘
```

**Detail:** [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]]

---

## 5. Tool Health Monitoring

### 5.1 Health Check Protocol

```yaml
health_check:
  tool_id: "obsidian-read-tool"
  check_interval_ms: 30000
  timeout_ms: 5000
  metrics:
    - "latency_p99_ms"
    - "error_rate_percent"
    - "resource_utilization_percent"
    - "invocation_count_per_hour"
  thresholds:
    latency_p99_ms: 10000
    error_rate_percent: 5.0
    resource_utilization_percent: 80.0
  on_failure:
    - "Mark tool as THROTTLED"
    - "Reduce resource budget"
    - "Notify observability plane"
    - "After 3 consecutive failures → RETIRED"
```

### 5.2 Resource Budget Tracking

```yaml
resource_budget:
  global_pool:
    total_tokens: 500000
    total_memory_mb: 4096
    total_concurrent_invocations: 20
  
  per_tool_limits:
    max_tokens_per_invocation: 8000
    max_time_per_invocation_ms: 10000
    max_memory_per_invocation_mb: 512
    max_concurrent_per_tool: 5
```

---

## 6. Failure Modes

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Tool crash** | Process exit or watchdog timeout | Restart tool; return partial results | HIGH |
| **Resource overflow** | Budget monitor | Terminate invocation; return partial results | MEDIUM |
| **Authority revocation** | Authority check on invocation | Reject invocation; re-request authority | HIGH |
| **Schema violation** | Input/output validation | Reject invocation; log violation | MEDIUM |
| **Stale tool metadata** | Version mismatch detection | Refresh from registry; re-negotiate version | LOW |
| **Deadlock** | Lock timeout | Deterministic ordering prevents by design | CRITICAL |

---

## 7. Cross-References

### 7.1 Internal Plane References

- [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] — Formal tool contract
- [[14_TOOLS/AMOS_LLM_WIKI_TOOL|AMOS_LLM_WIKI_TOOL]] — LLM Wiki tool bindings
- [[14_TOOLS/TOOLS_README|TOOLS_README]] — Structural overview

### 7.2 External Plane References

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane authorizes tool use
- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Agents invoke tools
- **Protocols:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]] — Tool interactions governed by protocols
- **Security:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] — Tool access is security boundary
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Tool invocations produce observability data

---

## 8. Worked Semantics

Given an operation touching `14 TOOLS MOC` within the Tools plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

---

## 9. Promotion Gate Checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

## 10. Cross-plane bindings
- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]

---

## 11. Falsifiers

F1: canonical source contradicts declared semantics. F2: executed test violates a stated invariant. F3: artifact promotes UNKNOWN to PASS.
