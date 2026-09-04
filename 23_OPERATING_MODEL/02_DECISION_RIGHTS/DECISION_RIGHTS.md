---
title: "23_OPERATING_MODEL — Decision Rights & RACI Matrix"
type: governance_specification
plane: 23_OPERATING_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# Decision Rights & Autonomous RACI Matrix

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Architectural Scope

This specification defines the decision authority boundaries for all autonomous agents, cognitive subsystems, and human stewards operating within the AMOS Full Brain OS. It establishes a five-tier decision hierarchy (D0-D4) with explicit RACI (Responsible, Accountable, Consulted, Informed) matrices for each class of operational decision.

The decision rights framework enforces the non-negotiable separation between capability and authority: an agent may possess the technical capability to perform an action without possessing the authority to commit that action without escalation.

```text
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
AGENT_RECOMMENDATION != ARCHITECT_RATIFICATION
DOCUMENTED != IMPLEMENTED
```

---

## 2. Decision Tier Classification (D0-D4)

Autonomous agents and cognitive subsystems operate under strict decision authority boundaries:

| Tier | Name | Scope of Decision | Permitted Entity | Required Quorum / Receipts |
| :--- | :--- | :--- | :--- | :--- |
| **D0** | `INFORM` | Telemetry logging, vector index updates, working trace append | All Agents (`06_AGENTS`) | Local trace hash |
| **D1** | `RECOMMEND` | Hypothesis generation, skill parameter proposal, draft research synthesis | Specialist Agents (`QFM_RESEARCHER`, `SPEC_*`) | Peer review receipt |
| **D2** | `PEER_CONSENSUS` | Shard-local CvRDT state merges, workflow step completion | Agent Clusters (`08_WORKFLOWS`) | $2/3$ BFT consensus |
| **D3** | `ORCHESTRATOR_EXEC` | Multi-agent task execution, capability token issuance, microVM sandbox spawn | `ORCH_ROOT`, `ORCH_COGNITIVE` | Signed Ed25519 token |
| **D4** | `ARCHITECT_SOLE` | Canonical law modification (`01_CANON`), kernel mutation (`02_KERNEL`), post-v4.4 version promotion | **Trang Phan (Origin Architect)** | Explicit Human Signature |

---

## 3. RACI Matrix by Decision Class

### 3.1 Canonical Law & Kernel Modifications

| Activity | Responsible | Accountable | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| Core law amendment | Origin Architect | Origin Architect | Security Council, ARB | All Agents |
| Kernel version promotion | Origin Architect | Origin Architect | ARB, Canon Stewardship | All Planes |
| Post-v4.4 lineage promotion | Origin Architect | Origin Architect | Full Governance Forum | All Agents |

### 3.2 Operational Execution Decisions

| Activity | Responsible | Accountable | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| Multi-agent task dispatch | ORCH_ROOT | ORCH_COGNITIVE | Workflow Engine | Affected Agents |
| Capability token issuance | ORCH_ROOT | ORCH_COGNITIVE | Security Plane | Token Holder |
| State epoch commit | State Engine | ORCH_COGNITIVE | Validation Pipeline | All Consumers |
| Sandbox microVM spawn | Runtime Engine | ORCH_ROOT | Security Plane | Observability |

### 3.3 Research & Knowledge Decisions

| Activity | Responsible | Accountable | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| Hypothesis generation | Specialist Agents | Peer Cluster | Domain MOC | Knowledge Plane |
| Paper synthesis draft | QFM_RESEARCHER | Peer Cluster | Math Registry | Research MOC |
| ArXiv corpus indexing | Indexing Engine | Knowledge Plane | Research Plane | All Consumers |

---

## 4. Escalation Pathway

When a decision exceeds the authority tier of the current entity, escalation follows a deterministic ladder:

```text
D0 (Agent) --> D1 (Specialist Cluster) --> D2 (Peer Consensus) --> D3 (Orchestrator) --> D4 (Architect)
```

Each escalation step must produce:
1. **Escalation Receipt:** Cryptographic hash binding the decision context, requesting entity, and escalation reason.
2. **Evidence Package:** All supporting data, analysis, and prior-tier deliberation traces.
3. **Timeout Bound:** Maximum deliberation time before automatic escalation to the next tier.

---

## 5. Safety Invariants

- `INV-DEC-001` (**Capability-Authority Separation**): No entity may commit a decision above its assigned tier, regardless of technical capability.
- `INV-DEC-002` (**Architect Sole Authority**): D4 decisions require explicit human signature from the Origin Architect. No autonomous path to D4 exists.
- `INV-DEC-003` (**Quorum Enforcement**): D2 decisions require $2f+1$ BFT consensus; partial quorum results in fail-closed deferral.
- `INV-DEC-004` (**Escalation Non-Circumvention**): Escalation pathways may not be bypassed. Any attempt to skip tiers triggers security alert and automatic rollback.
- `INV-DEC-005` (**Receipt Completeness**): Every committed decision must have a verifiable cryptographic receipt. Decisions without receipts are treated as `UNKNOWN/GAP` and reverted.

---

## 6. MECE Mapping

| AMOS Plane | Decision Rights Interaction |
| :--- | :--- |
| `01_CANON` | D4 sole authority for law modifications |
| `02_KERNEL` | D4 sole authority for kernel mutations |
| `03_CONTROL_PLANE` | D3 orchestrator exec for capability tokens |
| `06_AGENTS` | D0-D1 agent-level decisions |
| `08_WORKFLOWS` | D2 peer consensus for workflow completion |
| `09_PROTOCOLS` | D2 BFT quorum enforcement |
| `18_SECURITY` | D3-D4 security-critical decisions |
| `23_OPERATING_MODEL` | This specification (decision rights host) |

---

## 7. Navigation & Bindings

- **Operating Model README:** [[23_OPERATING_MODEL/OPERATING_MODEL_README|OPERATING_MODEL_README]]
- **Roles Registry:** [[23_OPERATING_MODEL/01_ROLES/ROLE_REGISTRY|ROLE_REGISTRY]]
- **Governance Forums:** [[23_OPERATING_MODEL/03_GOVERNANCE_FORUMS/GOVERNANCE_FORUMS|GOVERNANCE_FORUMS]]
- **Escalation Paths:** [[23_OPERATING_MODEL/04_ESCALATION/ESCALATION_PATHS|ESCALATION_PATHS]]
- **Service Levels:** [[23_OPERATING_MODEL/05_SERVICE_LEVELS/SERVICE_LEVELS|SERVICE_LEVELS]]
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Root Map:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

---

## 8. Known Gaps

- **Automated Escalation Triggers:** The escalation pathway is specified but automatic trigger conditions (e.g., timeout-based escalation) are not yet implemented in the runtime.
- **Multi-Stakeholder D4:** The current framework assigns D4 solely to the Origin Architect. Future governance models may require multi-signature D4 authority for organizational succession.
- **Cross-Domain Decision Conflicts:** When two domains have conflicting D2 consensus outcomes, the resolution mechanism is specified but not formally proven.
- **Epistemic Boundary:** `DOCUMENTED != IMPLEMENTED` — this RACI matrix is a governance specification. Enforcement in the runtime requires integration with the control plane capability token system.
