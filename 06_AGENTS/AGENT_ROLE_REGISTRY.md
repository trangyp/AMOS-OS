---
title: AMOS Agent Role Registry
type: registry
source: 06_AGENTS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 06_AGENTS/AMOS_AGENT_SCHEMA_FULL
    - 23_OPERATING_MODEL/01_ROLES/ROLE_REGISTRY
  scope: agent_roles
tags:
  - amos-os
  - agents
  - roles
  - taxonomy
---

# AMOS Agent Role Registry

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Universal Agent Role Taxonomy (MECE Matrix)

| Role Identifier | Archetype | Primary Planes | Permitted Capabilities & Tools | Max Token Budget | Permitted RSCF State Transitions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ORCH_ROOT` | Executive Orchestrator | `00_ROOT`, `05_COGNITIVE_ORGANISM` | Full planning, subagent spawning, workflow scheduling | 128,000 | `SOURCE_CLAIM` $\to$ `DERIVED` $\to$ `DECISION` |
| `ORCH_COGNITIVE` | Cognitive Organism | `05_COGNITIVE_ORGANISM`, `25_COGNITIVE_MATRIX` | Multi-agent coordination, tensor routing | 64,000 | `MODEL` $\to$ `DERIVED` |
| `AUDIT_EPISTEMIC` | Epistemic Auditor | `01_CANON`, `20_OPERATIONS` | Read-only scan, invariant verification, linting | 32,000 | `OBSERVATION` $\to$ `DERIVED` |
| `AUDIT_LEDGER` | Ledger Verifier | `03_CONTROL_PLANE`, `20_OPERATIONS` | Audit ledger verification, CAS epoch validation | 32,000 | `OBSERVATION` $\to$ `DERIVED` |
| `AUDIT_FENCE` | Syntax Failsafe | `17_OBSERVABILITY`, `19_TESTS` | Code fence repair, YAML schema linting | 16,000 | `OBSERVATION` $\to$ `DERIVED` |
| `EXEC_SANDBOX` | Runtime Executor | `04_RUNTIME`, `07_SKILLS` | Sandboxed WASM / MicroVM execution | 32,000 | `DECISION` $\to$ `OBSERVATION` |
| `EXEC_COMPILER` | AST Compiler | `01_SOFTWARE`, `02_KERNEL` | Deterministic AST lowering, build hash verify | 64,000 | `DERIVED` |
| `EXEC_SMT` | Formal Prover | `02_KERNEL`, `22_RESEARCH` | Z3 / CVC5 SMT solver theorem proving | 64,000 | `DERIVED` $\to$ `AUTHORITATIVE_PROOF` |
| `SPEC_QUANT_FOREX` | Quantitative Trader | `21_DOMAINS/03_FOREX` | OFI / VPIN calculation, MT5 ZeroMQ bridge | 32,000 | `MODEL` $\to$ `DECISION` (bounded) |
| `SPEC_BIO_NEURO` | Biological Specialist | `21_DOMAINS/06_BIOLOGY`, `23_UBI_BEI` | Cable equation modeling, FBA flux analysis | 32,000 | `MODEL` $\to$ `DERIVED` |
| `SPEC_LEGAL_DEONTIC` | Statutory Counsel | `21_DOMAINS/08_LEGAL`, `02_KERNEL` | Deontic logic proofs, compliance auditing | 32,000 | `DERIVED` $\to$ `DECISION` |
| `SPEC_MACRO_ECON` | Economic Modeler | `21_DOMAINS/09_FINANCE`, `17_C07` | DCF valuation, input-output Leontief matrices | 32,000 | `MODEL` $\to$ `DERIVED` |
| `CURATOR_HNSW` | Semantic Indexer | `10_MEMORY`, `11_KNOWLEDGE` | Dense 1536-dim vector embedding generation | 32,000 | `OBSERVATION` $\to$ `DERIVED` |
| `CURATOR_EPISODIC` | Episodic Scribe | `10_MEMORY`, `12_STATE` | Trace serialization, salience decay scoring | 16,000 | `OBSERVATION` |
| `CURATOR_RSCF` | Knowledge Harvester | `11_KNOWLEDGE`, `16_SCHEMAS` | Multi-source RSCF ingestion and grounding | 64,000 | `SOURCE_CLAIM` $\to$ `DERIVED` |
| `SENTINEL_ED25519` | Keymaster | `18_SECURITY`, `03_CONTROL_PLANE` | Cryptographic signature verification | 16,000 | `AUTHORITATIVE` |
| `SENTINEL_MACAROON` | Authz Gatekeeper | `03_CONTROL_PLANE`, `18_SECURITY` | Macaroon caveat attenuation checking | 16,000 | `DECISION` |
| `SENTINEL_EGRESS` | Network Guard | `18_SECURITY`, `15_INTERFACES` | Outbound socket firewall rule enforcement | 16,000 | `DECISION` |
| `SRE_INCIDENT` | Incident Commander | `20_OPERATIONS`, `08_WORKFLOWS` | Automated runbook execution, failover routing | 64,000 | `OBSERVATION` $\to$ `DECISION` |
| `SRE_BACKUP` | Archival Custodian | `20_OPERATIONS`, `24_ARCHIVE` | Snapshot validation, cryptographic checksums | 32,000 | `OBSERVATION` |

---

## 2. Capability Invocation Protocol

```protobuf
syntax = "proto3";
package amos.agents.v4_4;

message AgentInvocationRequest {
  string caller_agent_id = 1;
  string target_role_id = 2;
  string session_epoch_id = 3;
  bytes capability_token = 4;
  string prompt_context = 5;
  uint32 max_token_quota = 6;
}

message AgentInvocationResponse {
  string execution_id = 1;
  bool success = 2;
  string result_payload = 3;
  uint32 tokens_consumed = 4;
  string epistemic_transition = 5;
}
```

---

## 3. Governance Invariants

```text
ORCHESTRATOR != KERNEL_AUTHORITY
SPECIALIST_MODEL != GROUND_TRUTH
EXECUTION_SUCCESS != PROVEN_INVARIANT
```
