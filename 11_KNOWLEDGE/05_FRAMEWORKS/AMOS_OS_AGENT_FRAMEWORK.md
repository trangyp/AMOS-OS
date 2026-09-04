---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Os Agent Framework
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

# AMOS OS Agent Framework

`AMOS_OS_AGENT_FRAMEWORK.md` is the canonical Knowledge Plane reference artifact for the **AMOS OS Multi-Agent Architecture** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It establishes the structural schema, capability boundaries, and coordination protocols governing the **678+ canonical JSON agents** operating across the system.

______________________________________________________________________

## 1. Agent Architecture & Governance Invariants

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

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Agent Contract:** [[AGENTS|AGENTS]]
- **Agent Schema:** `11_KNOWLEDGE/AGENT_SCHEMA` and `11_KNOWLEDGE/AGENT_TEMPLATES`
- **Onboarding Guide:** `11_KNOWLEDGE/AGENT_ONBOARDING_GUIDE`
- **Agent Registry:** .devin/agents/amos-agent-registry-index

______________________________________________________________________

## 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_amos_os_agent_framework
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[AGENTS|AGENTS]] · `11_KNOWLEDGE/AGENT_SCHEMA` · `11_KNOWLEDGE/AGENT_ONBOARDING_GUIDE`

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
