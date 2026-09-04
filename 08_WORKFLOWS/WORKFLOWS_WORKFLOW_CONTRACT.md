---
title: Workflows Contract
type: plane_contract
source: 08_WORKFLOWS
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SPECIFICATION
updated: 2026-09-04
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance:
    - 08_WORKFLOWS/08_WORKFLOWS_MOC
    - 08_WORKFLOWS/WORKFLOW_METADATA_NORMALIZATION_REGISTRY.json
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: 08_workflows
---

# Workflows Contract

## 0. Scope

Governs **workflow objective, control graph, typed steps, bindings, state/read-write sets, resource budgets, authority/effects, assurance, replay, recovery and evolution**.

```text
WORKFLOW != SKILL
WORKFLOW != AGENT
WORKFLOW != AUTHORITY
DOCUMENTED != EXECUTED
EXECUTED != VALIDATED
```

## 1. Hard invariants

1. Workflow identity/version resolves before execution.
2. Objective, success and stop conditions are explicit.
3. Every step/edge has typed semantics; generic `RUN` cannot hide effect class.
4. Skills/agents/tools/models are bindings, not absorbed ownership.
5. Branches and joins preserve provenance and state-version compatibility.
6. Loops are bounded by resources and stop rules.
7. Consequential effects are reauthorized at commit.
8. Retry policy distinguishes call retry from effect retry.
9. Ambiguous external effects become `IN_DOUBT`.
10. Failure invalidates dependent branches only where possible.
11. Workflow evolution preserves predecessor lineage and migration impact.
12. Metadata normalization never upgrades documentary specs to empirical/runtime truth.
13. No universal fixed confidence threshold, chain depth or one-agent/one-skill topology is assumed.

## 2. Objective contract

```yaml
objective:
  purpose:
  purpose_family:
  scope:
  regime:
  success_conditions: []
  stop_conditions: []
  unacceptable_outcomes: []
  consequence_class:
```

The latest explicit user/system objective outranks an obsolete generated workflow description.

## 3. Control topology

Choose the smallest sufficient orchestration form:
`SEQUENTIAL | DAG | HIERARCHICAL | STATE_MACHINE | BOUNDED_LOOP | MANAGER_WORKER | HUMAN_CHECKPOINT | TRANSACTIONAL_EFFECT | HYBRID`.

Topology selection is a design decision, not a performance claim.

## 4. Step contract

```yaml
step:
  id:
  type:
  preconditions: []
  inputs: []
  outputs: []
  reads: []
  writes: []
  dependencies: []
  skill_binding:
  agent_binding:
  tool_binding:
  authority_required:
  validation_required:
  idempotency:
  retry:
  on_success:
  on_failure:
  provenance:
```

Place validation at load-bearing semantic transitions rather than mechanically after every trivial step.

## 5. Branch / join contract

A branch declares its independence assumptions. A join declares:
- predecessor set;
- merge semantics;
- contradiction/conflict policy;
- missing-branch policy;
- provenance composition;
- version/CAS requirement;
- failure behavior.

If independence is not demonstrated, parallelism is only a scheduling proposal.

## 6. Resources

Workflow admission should bind finite budgets when material:

```text
[token, tool_calls, wall_time, retries, handoffs, storage, external_cost]
```

A budget overrun produces `PARTIAL`, `HOLD`, `ESCALATE` or `UNKNOWN/GAP` according to the workflow contract; it does not silently relax integrity.

## 7. Procedural knowledge / memory

Reusable procedures can be stored at different levels:
- workflow/orchestrator memory: decomposition, delegation, ordering, checkpoint patterns;
- skill/task memory: fine-grained execution procedure;
- domain knowledge: factual/model evidence, not procedure;
- runtime state: current execution state, not long-term procedure.

Do not collapse these.

## 8. Authority and effects

```text
PROPOSE
→ VALIDATE PRECONDITIONS
→ BIND CURRENT STATE / POLICY
→ AUTHORIZE
→ REVALIDATE AT COMMIT
→ COMMIT
→ OBSERVE / RECEIPT
```

No workflow step can mint authority.

## 9. Failure / recovery / replay

For failures:
1. classify clean failure vs ambiguous effect;
2. freeze unsafe descendants;
3. preserve unaffected completed work;
4. rollback or compensate when defined;
5. collect discriminating evidence;
6. reroute only with changed state/evidence/path;
7. emit replayable receipt.

Replay claims require workflow version, bound inputs/state, environment, dependencies and external-effect handling.

## 10. Evaluation

Evaluate dimensions separately:
- task success;
- step/branch correctness;
- constraint/process compliance;
- recoverability;
- safety/effect containment;
- efficiency/resource use;
- robustness under perturbation;
- transfer across task/role/model/host when claimed.

One aggregate score must not erase a hard safety/authority failure.

## 11. Evolution

Workflow changes are governed mutations. Record graph diff, binding diff, authority/exposure diff, evidence, regression tests, compatibility and rollback.

## 12. Metadata normalization

`WORKFLOW_METADATA_NORMALIZATION_REGISTRY.json` remains the authoritative classification overlay for direct generated workflow adapters when legacy frontmatter conflicts.

```text
WORKFLOW SPECIFICATION = AMOS_MODEL
EMBEDDED SOURCE CLAIMS = preserve source class
EMPIRICAL = requires independent evidence
CONFLICTING VERSION = UNKNOWN/GAP for version-sensitive execution
```

The overlay is not a substitute for repairing central generators. Builder workflows must emit clean metadata going forward.

## 13. Promotion

A workflow may be called operationally implemented only when the claimed engine/runtime, graph/version, bindings, input/output validation, negative paths, authority tests, retry/idempotency, partial-effect recovery and receipts are evidenced for the same envelope.

## 14. Falsifiers

Revise or quarantine a workflow if:
- its graph cannot satisfy declared success conditions;
- branch assumptions are false;
- bindings resolve to incompatible skills/agents/tools;
- loops can fail to terminate under admitted state;
- effect retry can duplicate irreversible operations;
- authority freshness is not rechecked;
- replay diverges in a supposedly deterministic envelope;
- metadata/version ambiguity changes execution semantics.

## Related

- [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- [[08_WORKFLOWS/00_INDEX/WORKFLOW_MAP|WORKFLOW_MAP]]
- [[07_SKILLS/07_SKILLS_MOC|SKILLS]]
- [[06_AGENTS/06_AGENTS_MOC|AGENTS]]
- [[04_RUNTIME/04_RUNTIME_MOC|RUNTIME]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|CONTROL_PLANE]]
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|OBSERVABILITY]]
- [[19_TESTS/19_TESTS_MOC|TESTS]]

---
RSCF-NODE
node_id: workflows_workflow_contract
node_type: contract
path: 08_WORKFLOWS/WORKFLOWS_WORKFLOW_CONTRACT.md
claim_class: AMOS_MODEL
