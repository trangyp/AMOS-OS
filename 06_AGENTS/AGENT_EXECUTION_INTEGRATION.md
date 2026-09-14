---
title: Agent Execution Integration
source: 06_AGENTS
type: architecture_contract
artifact: AGENT_EXECUTION_INTEGRATION.md
artifact_id: amos_06_agents_agent_execution_integration
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 06_AGENTS
artifact_kind: AMOS_MODEL
path: 06_AGENTS/AGENT_EXECUTION_INTEGRATION.md
canon_target: v4.4
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: PARTIAL_BOUNDED_REFERENCE
validation_status: LOCAL_BOUNDED_TESTED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance:
    - AMOS_corpus
    - 06_AGENTS/AMOS_AGENT_SCHEMA_FULL
    - 03_CONTROL_PLANE/04_AUTHORITY/AUTHORITY_WITNESS
    - 03_CONTROL_PLANE/09_COMMIT/governed_mutation_gate.py
    - 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/executor_preflight_runtime.py
  scope:
    - AGENTS
    - EXECUTION
    - RUNTIME
    - ORCHESTRATION
---

# Agent Execution Integration

> **Epistemic status:** `AMOS_MODEL` / `DERIVED`. This contract describes how agents defined by the `06_AGENTS` schema are prepared for governed execution across the AMOS runtime/control stack. A bounded preflight reference implementation now exists. This does **not** establish a deployed multi-agent runtime or a live external-effect executor.

## Role

The agent execution integration layer maps an `AMOS_AGENT_SCHEMA_FULL` contract toward concrete runtime execution: capability resolution, task routing, delegation, preflight preparation, substrate selection, telemetry, control-plane finalization, and receipt handling.

The executable boundary added by the current reference implementation is deliberately narrower:

```text
ACTION PROPOSAL
    -> STRUCTURAL PREFLIGHT
    -> EFFECT / TRANSACTION / IDEMPOTENCY BINDING
    -> PREPARED_FOR_CONTROL_PLANE
```

never:

```text
PREPARED_FOR_CONTROL_PLANE
    -> SELF-AUTHORIZED COMMIT
```

## Current Executable Reference

Reference runtime:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/executor_preflight_runtime.py`

Reference tests:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_executor_preflight_runtime.py`

The bounded runtime implements:

- typed `ActionProposal`, `ExecutionRequest`, `AuthorityBinding`, `PolicyBinding`, `ObservedRead`, and `IntendedWrite` objects;
- deterministic SHA-256 effect, declared-read-set, and write-set digests over canonicalized records;
- proposal/request temporal freshness checks;
- exact principal binding;
- exact effect-digest binding;
- exact action-type and target scope checks;
- policy identity/epoch and policy-scope checks;
- duplicate read/write coordinate rejection;
- stable idempotency-key requirement for durable effects;
- durable-effect authority binding to transaction ID and idempotency key;
- an immutable `PreparedExecution` capsule whose `commit_authorized` field is always `false`.

The runtime does **not**:

- authenticate a principal;
- cryptographically verify an authority witness;
- create or delegate authority;
- own the infrastructure-observed authoritative read set;
- validate the full semantic transaction;
- validate observability-envelope coverage;
- own effect-release ledger state;
- dispatch an external effect;
- return `COMMITTABLE` or `COMMITTED`;
- generate receiver-attested completion receipts.

Hard distinction:

```text
request.observed_read_set
    = caller-declared preflight input

PreparedExecution.declared_read_set_hash
    = deterministic digest of that declared input

infrastructure authoritative read set
    = harness-observed control-plane state
```

Therefore:

```text
DECLARED_READ_SET != AUTHORITATIVE_READ_SET
PREPARED_FOR_CONTROL_PLANE != COMMITTABLE
COMMITTABLE != COMMITTED
```

## Local Validation Evidence

The exact reference source passed **22/22** local tests.

The suite includes:

- deterministic example tests for freshness, effect identity, authority/policy scope, transaction binding, idempotency binding, duplicate read/write rejection, and `commit_authorized = false`;
- 2,000 seeded randomized effect-digest permutation/value-sensitivity cases;
- 5,000 seeded randomized authority/policy/freshness/idempotency gate combinations checked against an explicit conjunction oracle.

This is bounded local evidence only:

```text
LOCAL TEST PASS != FORMAL PROOF
LOCAL TEST PASS != DEPLOYED EFFECT EXECUTION
LOCAL TEST PASS != CANON PROMOTION
```

## Agent Lifecycle

```text
[Schema Instantiation] -> [Capability Resolution] -> [Task Routing]
       |
[Delegation Witness] -> [Executor Preflight] -> [Control-Plane Validation]
       |
[Runtime Dispatch] -> [Substrate Execution] -> [Telemetry / Observation]
       |
[Receipt] -> [Causal Epoch / Finalization]
```

## Execution Stages

| Stage | Agent Concern | Runtime / Control Concern | Output |
|-------|---------------|---------------------------|--------|
| Instantiate | Load schema, identity, skills | Validate typed identity input | `agent_handle` / candidate identity |
| Resolve capability | Match task to capability | Resolve capability contract | `capability_match` |
| Route | Select candidate runtime | Route under explicit capability bounds | `dispatch_record` |
| Delegate | Carry delegation evidence | Validate attenuation upstream | `delegation_witness` |
| Preflight | Bind proposal/effect/transaction | Structural freshness + exact local bindings | `PreparedExecution` |
| Commit gate | None; agent cannot self-authorize | Revalidate authority, policy, constraints, read set, semantic transaction, observability, ledger | control-plane decision |
| Execute | Consume already-admitted effect | Effect adapter / substrate | `effect_trace` |
| Observe | Collect result/state | Telemetry + receiver evidence | `observation` |
| Finalize | Preserve lineage | Finality / receipt / replay | `effect_receipt` |

## Multi-Agent Orchestration

- **Contract Net:** `AUTONOMOUS_CONTRACT_NET_TASK_ALLOCATION_ENGINE` may govern task announcement, bid, award, and result where implemented.
- **Consensus:** `ADMM_DECENTRALIZED_CONSENSUS_LEDGER` is a candidate coordination mechanism; its existence does not grant execution authority.
- **Federation:** `FEDERATED_DIFFERENTIAL_PRIVACY_LEDGER` is a candidate privacy-preserving federation mechanism subject to implementation evidence.
- **Failure memory:** `07_SKILLS/amos-failure-memory` may preserve agent failures for lineage where the skill/runtime is active.

## Invariants

| ID | Invariant |
|----|-----------|
| AGT_EXEC_INV_01 | An agent's capability does not grant authority; authority is resolved by the control plane. |
| AGT_EXEC_INV_02 | Every durable/external effect remains subject to control-plane commit-time validation. |
| AGT_EXEC_INV_03 | Agent-to-agent delegation must respect temporal and scope attenuation. |
| AGT_EXEC_INV_04 | Telemetry is `OBSERVATION` class, not `COMMIT` class, until finalized. |
| AGT_EXEC_INV_05 | Substrate selection is a runtime capability decision, not an agent authority decision. |
| AGT_EXEC_INV_06 | `PREPARED_FOR_CONTROL_PLANE != COMMITTABLE != COMMITTED`. |
| AGT_EXEC_INV_07 | Caller-declared read state cannot substitute for the infrastructure-observed authoritative read set. |
| AGT_EXEC_INV_08 | Durable effect authority must remain bound to the exact effect, transaction and idempotency identity at the boundary where those fields are required. |

## Cross-Plane References

- **Agent schema:** [[06_AGENTS/AMOS_AGENT_SCHEMA_FULL|AMOS_AGENT_SCHEMA_FULL]]
- **Authority witness:** [[03_CONTROL_PLANE/04_AUTHORITY/AUTHORITY_WITNESS|AUTHORITY_WITNESS]]
- **Commit semantics:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- **Runtime integration:** [[04_RUNTIME/HARDWARE_AWARE_RUNTIME_INTEGRATION|HARDWARE_AWARE_RUNTIME_INTEGRATION]]
- **Kernel execution:** [[02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL|QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL]]
- **Capability-bound governance:** [[07_SKILLS/amos-capability-bound-governance/SKILL|amos-capability-bound-governance]]
- **Delegation witness:** [[03_CONTROL_PLANE/04_AUTHORITY/DELEGATION_WITNESS|DELEGATION_WITNESS]]
- **Runtime master skill:** [[07_SKILLS/amos-os-runtime-master/amos-os-runtime-master_MOC|amos-os-runtime-master_MOC]]
- **Parent MOC:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]]

## MECE Boundary

This note owns the **agent-to-runtime execution integration contract** and its bounded preflight adapter. It does not own the agent schema, authority issuance, capability-governance kernel, authoritative read-set observation, durable commit/finality, receiver receipts, or substrate physics.

---

**MOC:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
