---
title: L31 Amos Plane — Plane Governance Specification
type: specification
source: 01_CANON
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
canonical_status: CONDITIONAL
updated: 2026-09-04
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 00_ROOT/00_ROOT_MOC
    - 01_CANON/01_CORE_LAWS/LAW_HIERARCHY
    - 01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME
  scope: plane_governance
tags:
  - amos-os
  - 01-canon
  - specification
  - l31-amos-plane
---

# L31 Amos Plane — Plane Governance Specification

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Conclusion Class:** `AMOS_MODEL`
> **Status:** `PROPOSED_SPECIFICATION` · **Canonical Status:** `CONDITIONAL`

---

## 1. Architectural Scope

`L31_AMOS_PLANE` defines the typed contracts, invariants, and operational procedures that govern the **physical/operational plane structure** of the AMOS Full OS. A *plane* is a numbered namespace (`01_CANON` … `25_COGNITIVE_MATRIX`) that owns a MECE responsibility partition. This law specifies how planes are defined, how they relate to each other, how dependencies are expressed as typed edges (not implicit dual ownership), and how the partition invariant is maintained.

The law operationalizes the MECE partition from `FULL_BRAIN_OS_MECE_ARCHITECTURE` §2: every numbered plane belongs to exactly one responsibility domain (A–F), and the intersection of all domains is empty. `00_ROOT` is the navigation/authority-pointer meta-plane and is outside the numbered partition.

---

## 2. Governing Invariants

- **AP-1 MECE Partition:** Every numbered plane `{01..25}` is assigned to exactly one responsibility domain `A ∪ B ∪ C ∪ D ∪ E ∪ F`. No plane belongs to two domains. No domain is empty.
- **AP-2 One Primary Owner:** Each Full Brain functional field has exactly one primary physical owner. Cross-plane relationships are typed dependencies, not implicit dual ownership.
- **AP-3 Dependency-as-Edge:** Inter-plane relationships are explicit, typed edges (e.g., `DEPENDS_ON`, `READS_FROM`, `VALIDATED_BY`) rather than implicit ownership. Dependencies do not create authority.
- **AP-4 No Silent Scope Expansion:** A plane's responsibility scope cannot be silently expanded to include operations owned by another plane. Scope changes require governed canon admission.
- **AP-5 Plane Contract Required:** Every plane must expose a typed plane contract specifying its responsibility domain, primary fields, dependencies, authority class, and failure semantics.
- **AP-6 Axiom Adherence:** Plane governance is strictly bound by M01–M20 core laws and the `LAW_HIERARCHY` precedence order.

---

## 3. Plane Responsibility Partition

```text
A — NORMATIVE & GOVERNANCE DEFINITION
  01_CANON, 23_OPERATING_MODEL
  → Owns: admitted laws, definitions, lineage, supersession, roles, decision rights

B — EXECUTION CORE & EFFECT GOVERNANCE
  02_KERNEL, 03_CONTROL_PLANE, 04_RUNTIME
  → Owns: deterministic primitives, authorization, commit/finality, bounded execution

C — COGNITIVE CAPABILITY & ORCHESTRATION
  05_COGNITIVE_ORGANISM, 06_AGENTS, 07_SKILLS, 08_WORKFLOWS, 21_DOMAINS, 25_COGNITIVE_MATRIX
  → Owns: cognitive loop, bounded workers, versioned capabilities, orchestration, domain routing

D — INFORMATION, MEMORY, STATE & MODEL SUBSTRATE
  10_MEMORY, 11_KNOWLEDGE, 12_STATE, 13_MODELS, 16_SCHEMAS
  → Owns: temporal memory, source/evidence, state identity/epochs, models/simulations, typed contracts

E — INTERACTION, SECURITY & EFFECT ADAPTERS
  09_PROTOCOLS, 14_TOOLS, 15_INTERFACES, 18_SECURITY
  → Owns: handoff contracts, host/tool capabilities, system boundaries, security/trust enforcement

F — ASSURANCE, LEARNING & LIFECYCLE EVIDENCE
  17_OBSERVABILITY, 19_TESTS, 20_OPERATIONS, 22_RESEARCH, 24_ARCHIVE
  → Owns: traces/telemetry, executable checks, runbooks/audit, research, retained history
```

**Partition invariant:**

```text
{01..25} = A ∪ B ∪ C ∪ D ∪ E ∪ F
A ∩ B ∩ C ∩ D ∩ E ∩ F = ∅
```

---

## 4. Full Brain Functional Field Ownership

| Full Brain Field | Primary Owner | Typed Dependencies |
|-----------------|---------------|---------------------|
| Representation / Expression | `05_COGNITIVE_ORGANISM` | `15_INTERFACES`, `11_KNOWLEDGE`, `13_MODELS` |
| Cognitive Coordination | `05_COGNITIVE_ORGANISM` | `25_COGNITIVE_MATRIX`, `02_KERNEL` |
| Capability / Specialist Reasoning | `21_DOMAINS` | `07_SKILLS`, `13_MODELS`, `11_KNOWLEDGE` |
| World / System Representation | `13_MODELS` | `11_KNOWLEDGE`, `21_DOMAINS` |
| Runtime Continuity | `04_RUNTIME` | `09_PROTOCOLS`, `10_MEMORY`, `12_STATE`, `16_SCHEMAS` |
| Effect Governance | `03_CONTROL_PLANE` | `02_KERNEL`, `18_SECURITY`, `23_OPERATING_MODEL` |
| Deployment / Effect Adaptation | `14_TOOLS` | `06_AGENTS`, `08_WORKFLOWS`, `15_INTERFACES` |

`ONE PRIMARY OWNER + MANY TYPED DEPENDENCIES` is the default. Dependencies are edges, not ownership transfers.

---

## 5. Plane Contract Schema

```yaml
plane_contract:
  plane_id: <NN_NAME>
  responsibility_domain: <A|B|C|D|E|F>
  primary_fields:
    - <full_brain_field>
  dependencies:
    - target_plane: <NN_NAME>
      edge_type: <DEPENDS_ON|READS_FROM|VALIDATED_BY|ENFORCED_BY|ROUTED_TO>
      authority_class: <PROPOSAL|COMMIT|EVIDENCE|REPRESENTATION|EFFECT_ADAPTER|DEFINITION>
  authority_boundary:
    granted_authority: <authority_class>
    prohibited_operations: [<op_class>, ...]
  failure_semantics:
    failure_mode: <fail_closed|fail_open|degrade_graceful>
    recovery_basin: <rollback_basin_id>
  provenance:
    origin_architect: Trang Phan
    steward: Trang Phan
    amos_core_target: v4.4
```

---

## 6. Inter-Plane Dependency Edge Types

```text
DEPENDS_ON     → Plane A requires Plane B's output to function
READS_FROM     → Plane A reads state/data from Plane B (no mutation)
VALIDATED_BY   → Plane A's outputs are validated by Plane B
ENFORCED_BY    → Plane A's invariants are enforced by Plane B
ROUTED_TO      → Plane A's proposals are routed to Plane B for commit
SUPERSEDED_BY  → Plane A's artifact is superseded by Plane B's artifact
```

**Edge invariant:** No edge creates authority. `DEPENDS_ON(B)` does not grant `A` the authority of `B`.

---

## 7. Plane Integrity Firewalls

```text
MEMORY != KNOWLEDGE
KNOWLEDGE != STATE
MODEL != OBSERVATION
SCHEMA != TRUTH
CANON != KERNEL
KERNEL != CONTROL_PLANE
CONTROL_PLANE != RUNTIME
RUNTIME != COGNITION
ORGAN != AGENT
AGENT != SKILL
SKILL != WORKFLOW
```

These structural firewalls prevent a lower-level component from erasing a higher-order separation by implementation.

---

## 8. Cognitive-Organism Functional Partition (Plane 05)

The cognitive organism plane normalizes the persistent cognitive loop into seven responsibility groups:

```text
INPUT / REPRESENTATION         → perception, attention, context, world-model access
INTERPRETATION / REASONING     → cognition, structural reasoning, competing hypotheses, causal analysis
AFFECT / DRIVE                 → emotion-model, instinct, motivation, goal
PROSPECTIVE / ACTION FORMATION → planning, decision-support, agency proposal, action interface
ADAPTATION / CONTINUITY        → memory access, learning, reflection, identity continuity
SOCIAL / EXPRESSION            → social modeling, communication, expression
REGULATION / ASSURANCE         → homeostasis, risk, safety, repair, observability
```

These groups are functionally distinct; dependencies between them are explicit edges.

---

## 9. Safety Invariants & Firewalls

- `INV-AP-001` (**Partition Completeness**): Every numbered plane must appear exactly once in the responsibility partition. Unassigned planes are `UNKNOWN/GAP`.
- `INV-AP-002` (**No Dual Ownership**): A plane may not own responsibilities in two MECE domains. Cross-domain operations require explicit delegation.
- `INV-AP-003` (**Cognition Cannot Self-Commit**): Cognitive planes (domain C) cannot authorize their own durable effects. They propose; the control plane (domain B) commits.
- `INV-AP-004` (**Control Plane Cannot Redefine Truth**): The control plane cannot redefine domain truth or evidence. It enforces canon; it does not create canon.
- `INV-AP-005` (**Archive Cannot Become Active**): `24_ARCHIVE` (domain F) cannot silently become current authority. Historical artifacts require governed promotion to become active.

---

## 10. Failure Modes & Degradation

| Failure Scenario | Trigger | Response |
|------------------|---------|----------|
| Plane scope violation | Operation outside MECE domain | Reject + audit + escalate |
| Missing plane contract | No contract exposed | Plane marked `UNKNOWN/GAP` |
| Circular dependency | Dependency cycle detected | Break cycle + flag for governance review |
| Unassigned plane | Plane not in A–F partition | Block consequential operations until assigned |
| Dual ownership attempt | Plane claims two domains | Reject + require canon admission for resolution |

---

## 11. Navigation & Bindings

- **Master MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- **Partition Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- **Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Scope Regime Law:** [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]]
- **Related Laws:** [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]] · [[01_CANON/01_CORE_LAWS/L32_CANON|L32_CANON]] · [[01_CANON/01_CORE_LAWS/L33_KERNEL|L33_KERNEL]]
- **Cognitive Organism MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]

---

## 12. Known Gaps & Falsifiers

- `GAP-AP-001`: The MECE partition is structurally defined but not yet enforced by a runtime validator across all planes.
- `GAP-AP-002`: Inter-plane dependency edges are documented but not yet machine-checked for cycles or orphaned references.
- `GAP-AP-003`: Dynamic plane creation (beyond the current 25) is not governed by this law.
- `GAP-AP-004`: `L31` is a `PROPOSED_SPECIFICATION` with `CONDITIONAL` canonical status; it does not by itself establish final AMOS canon.

**Falsifiers:**

- F1: A plane is found to own responsibilities in two MECE domains simultaneously.
- F2: A cognitive plane commits a durable effect without control-plane authorization.
- F3: The control plane redefines domain truth or evidence without canon admission.
- F4: An archived artifact becomes active authority without governed promotion.

**Parent:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
