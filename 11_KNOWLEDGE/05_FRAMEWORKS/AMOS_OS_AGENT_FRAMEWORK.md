---
title: "AMOS OS Agent Framework"
type: architecture
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: "AMOS_OS_AGENT_FRAMEWORK.md"
artifact_id: "amos_11_knowledge_05_frameworks_amos_os_agent_framework"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "11_KNOWLEDGE"
segment: "11_KNOWLEDGE/05_FRAMEWORKS"
artifact_kind: "FRAMEWORK"
path: "11_KNOWLEDGE/05_FRAMEWORKS/AMOS_OS_AGENT_FRAMEWORK.md"

tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 05_frameworks
  - agent_framework
  - multi_agent_systems
  - agent_contract
  - agent_schema
  - rscf
  - canon_candidate
  - canon/knowledge

version: "1.0.0"
updated: "2026-08-27"

status: "ACTIVE_REFERENCE"
epistemic_class: "AMOS_MODEL"
canonical_status: "SOURCE_GROUNDED_CANON_CANDIDATE"
implementation_status: "CONCEPTUAL_SOURCE_DEFINED"
validation_status: "NOT_INDEPENDENTLY_ESTABLISHED"
executable_binding: "NOT_ESTABLISHED"

ingestion_action: "NATIVE_CANON_INGESTION"
raw_source_policy: "DO_NOT_LOAD_UNLESS_REQUIRED"

rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
    - AGENT_SCHEMA
    - AGENT_TEMPLATES
    - AGENT_ONBOARDING_GUIDE
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_FRAMEWORKS
    - AGENT_ARCHITECTURE
    - SOURCE_DEFINED_MODEL

framework_binding:
  agent_contract:
    artifact: "[[AGENTS]]"
  agent_schema:
    artifact: "`11_KNOWLEDGE/AGENT_SCHEMA`"
  agent_templates:
    artifact: "`11_KNOWLEDGE/AGENT_TEMPLATES`"

epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  agent_model: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# AMOS OS Agent Framework

`AMOS_OS_AGENT_FRAMEWORK.md` is the canonical Knowledge Plane reference artifact for the **AMOS OS Multi-Agent Architecture** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It establishes the structural schema, capability boundaries, and coordination protocols governing the **678+ canonical JSON agents** operating across the system.

---

# 1. Agent Architecture & Governance Invariants

```text
               ┌────────────────────────────────────────────────────────┐
               │                AMOS OS AGENT FRAMEWORK                 │
               └───────────────────────────┬────────────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
STRICT JSON SCHEMA BINDING         AUTHORITY SEPARATION              WORKFLOW RECIPROCITY
• name, type, domain, caps         • Capability != Authority         • Executes verified workflows
• Exactly 8 verified caps each     • Epistemic class compliance       in .devin/workflows/
• Validated in .devin/agents/      • Strict fail-closed defaults     • Cryptographic receipts
```

---

# 2. Inter-Plane & Vault Connections

- **Agent Contract:** [[AGENTS]]
- **Agent Schema:** `11_KNOWLEDGE/AGENT_SCHEMA` and `11_KNOWLEDGE/AGENT_TEMPLATES`
- **Onboarding Guide:** `11_KNOWLEDGE/AGENT_ONBOARDING_GUIDE`
- **Agent Registry:** [[.devin/agents/amos-agent-registry-index]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_amos_os_agent_framework
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_GROUNDED
  H:
    identity: "AMOS OS Agent Framework"
    role: "Multi-agent structural schema, capability boundaries, and execution protocols"
  M:
    primitives: [json_schema_binding, authority_separation, workflow_reciprocity]
    agent_count: 678
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[05_FRAMEWORKS_MOC]] · [[AGENTS]] · `11_KNOWLEDGE/AGENT_SCHEMA` · `11_KNOWLEDGE/AGENT_ONBOARDING_GUIDE`

---
**MOC:** [[05_FRAMEWORKS_MOC]]
