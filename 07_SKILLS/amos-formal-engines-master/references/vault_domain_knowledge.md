---
title: Vault Domain Knowledge — Amos Formal Engines Master
type: reference
source: 07_SKILLS/amos-formal-engines-master/references
tags:
- reference
- amos-formal-engines-master
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# amos-formal-engines-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `02_KERNEL/01_META_LOGIC/K_META_LOGIC.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# L02_ATTENTION — Purpose

**Class:** `COGNITIVE_PRIMITIVE_PURPOSE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `PURPOSE.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** available source material identifies `L02_ATTENTION` as the primitive concerned with **attention allocation and budgeting scarce reasoning/observation resources**. The expanded architectural purpose, AI application model, interfaces, operators, governance rules, H/M/L mapping, and runtime behavior below are `AMOS_MODEL` unless independently supported by direct canon or executable evidence.

---

# 0. Purpose Statement

`L02_ATTENTION` exists to govern **what receives finite cognitive processing resources, when, at what depth, for how long, and under which constraints**.

Its function is not merely to notice information.

Its function is to transform an oversized field of possible observations, claims, tasks, risks, contradictions, hypotheses, memories, dependencies, and actions into a bounded set of currently attended objects.

Conceptually:

$$Candidate\ Space \rightarrow Attention\ Selection \rightarrow Resource\ Allocation \rightarrow Focused\ Processing$$

subject to:

```text
finite resources
governing objectives
hard constraints
scope
regime
freshness
dependency structure
provenance
uncertainty
risk
H/M/L context
authority boundaries
```

The central purpose is therefore:

> **Allocate scarce reasoning and observation capacity toward the smallest set of targets whose processing can materially improve epistemic integrity, decision quality, safety, recovery, or task completion.**

---

# 1. Source / Canon Basis

## 1.1 Source-supported semantic core

Recovered L02 meaning:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This supports three minimum propositions:

```text
1. L02 concerns attention.

2. Attention involves allocation.

3. The relevant reasoning/observation resources are scarce.
```

These propositions justify an allocation architecture.

They do not by themselves establish:

```text
canonical scoring equations
canonical operator names
canonical thresholds
canonical agents
canonical workflow
canonical neural mechanism
canonical AI implementation
```

---

# 2. Definition

Within this AMOS model:

[
Attention
=========

GovernedAllocation(
ProcessingResources,
CandidateTargets,
Context
)
]

where `Context` includes, where material:

```text
objective
constraint state
uncertainty
dependency structure
consequence
time sensitivity
scope
regime
freshness
provenance
H/M/L level
authority
```

Attention determines:

```text
what enters active processing
what receives more processing
what receives less processing
what is deferred
what is escalated
what is revalidated
what is ignored for now
when focus should stop
```

---

# 3. What L02 Is Not

L02 must remain distinct from adjacent epistemic and governance functions.

```text
ATTENTION != SENSING

ATTENTION != OBSERVATION

ATTENTION != PERCEPTION

ATTENTION != MEMORY

ATTENTION != TRUTH

ATTENTION != EVIDENCE

ATTENTION != CONFIDENCE

ATTENTION != CAUSATION

ATTENTION != DECISION AUTHORITY

ATTENTION != COMMIT AUTHORITY
```

Examples:

```text
A claim receiving high attention
does not make it true.

A source receiving repeated attention
does not make it independent evidence.

A risk receiving attention
does not prove the risk exists.

An action receiving high priority
does not authorize the action.
```

---

# 4. Primary System Role

L02 sits conceptually between a broad field of available information and deeper cognitive processing.

Minimal structural model:

```text
L00_REALITY_ENVIRONMENT
        ↓
L01_SENSING_OBSERVATION
        ↓
candidate observations
        ↓
L02_ATTENTION
        ↓
selected / prioritized processing
        ↓
downstream cognition
```

The exact canonical downstream primitive remains `UNKNOWN/GAP` unless independently recovered.

The source-supported neighboring relationship should therefore be treated conservatively.

---

# 5. Why L02 Exists

A cognitive system cannot process every potentially available object with maximum depth.

If candidate set size is:

[
|X| \gg Capacity
]

then some selection function is unavoidable.

Without governed attention, a system risks:

```text
resource exhaustion
irrelevant reasoning
salience capture
goal drift
repeated processing
failure to inspect critical evidence
failure to notice contradiction
failure to revisit stale assumptions
context overload
tool overuse
premature closure
endless exploration
```

L02 provides the architecture for controlling this bottleneck.

---

# 6. Core Objectives

The purpose of L02 can be decomposed into the following objectives.

## 6.1 Preserve finite resources

[
\sum_i Allocation_i
\le
AvailableBudget
]

for compatible resource units.

Resources may include:

```text
tokens
context capacity
reasoning depth
wall-clock time
tool calls
retrieval operations
compute
agent calls
human-review capacity
```

---

## 6.2 Protect load-bearing reasoning

Attention should preserve enough capacity for:

```text
critical premises
hard constraints
contradictions
decision-changing uncertainty
dependency failures
authority checks
provenance checks
critical gaps
repair
```

---

## 6.3 Reduce decision-relevant uncertainty

Not all uncertainty deserves equal attention.

L02 should preferentially process uncertainty capable of materially changing:

```text
claim status
decision
action
risk state
repair path
confidence ceiling
```

---

## 6.4 Prevent salience capture

Salience is allowed to influence attention.

It cannot dominate automatically.

```text
SALIENCE
!=
TRUTH

SALIENCE
!=
IMPORTANCE

SALIENCE
!=
PRIORITY
```

---

## 6.5 Preserve competing hypotheses

When materially incompatible explanations remain viable:

```text
COMPETING
```

must remain visible.

Attention should seek discriminating evidence rather than forcing premature convergence.

---

## 6.6 Enable adaptive depth

L02 should support movement between:

```text
C0 Direct
C1 Compact
C2 Structured
C3 Deep
C4 Maximum
```

according to decision-relevant uncertainty, stakes, contradiction, novelty, provenance weakness, and irreversibility.

---

## 6.7 Stop when sufficient

Attention is not intended to maximize reasoning indefinitely.

It should stop when relevant sufficiency conditions are met.

Conceptually:

[
Stop
====

ClaimSufficiency
\land
DecisionSufficiency
\land
ActionSufficiency
]

where non-applicable components are excluded.

---

# 7. Application to AI

`L02_ATTENTION` can be applied to AI systems as a governed **reasoning-resource allocation layer**.

It is not equivalent to transformer self-attention.

The term `attention` here refers to system-level cognitive/resource allocation.

```text
AMOS L02 ATTENTION
!=
TRANSFORMER ATTENTION MATRIX
```

Transformer attention is an internal model computation.

AMOS L02 attention is a higher-level architecture for deciding what an AI system should process, retrieve, inspect, verify, revisit, escalate, or ignore.

---

# 8. AI Use Cases

For AI agents, L02 may govern:

```text
which user requirement is currently load-bearing

which retrieved documents deserve deep reading

which repository files deserve inspection

which contradiction should be investigated first

which tool call has highest expected value

which unresolved gap blocks completion

which memory should be recalled

which premise must be revalidated

which hypothesis should receive more evidence

when to stop web research

when to escalate reasoning depth

when to reduce context usage

when to preserve a branch instead of merging it

when to ask another specialist skill

when a task should be blocked because authority is absent
```

---

# 9. AI Attention Candidate Space

For an AI system:

[
X_t =
{
user\ requirements,
observations,
retrieved\ evidence,
memory,
hypotheses,
constraints,
tools,
files,
tasks,
risks,
gaps
}
]

L02 then proposes allocation:

[
A_t
===

Allocate(X_t,B_t,C_t)
]

where:

```text
B_t = available resource budget
C_t = governing context
```

---

# 10. AI-Specific Resource Dimensions

AI attention resources may include:

```yaml
AIResourceBudget:

  context_tokens:
    type: integer

  reasoning_budget:
    type: bounded_resource

  retrieval_calls:
    type: integer

  web_queries:
    type: integer

  tool_calls:
    type: integer

  agent_calls:
    type: integer

  execution_time:
    type: duration

  human_review:
    type: bounded_resource
```

These resource dimensions must remain typed.

They cannot be blindly summed.

---

# 11. AI Attention Priority Factors

A candidate AI attention model may consider:

```text
goal relevance
decision consequence
uncertainty
dependency criticality
contradiction
freshness
information gain
time sensitivity
risk
irreversibility
provenance weakness
repair value
resource cost
```

Generic model:

[
Priority_i
==========

F(
Goal_i,
Consequence_i,
Uncertainty_i,
Dependency_i,
Contradiction_i,
Freshness_i,
InformationValue_i,
Cost_i
)
]

This is `AMOS_MODEL`.

No canonical coefficient set is claimed.

---

# 12. Typed Inputs

```yaml
AttentionPurposeInput:

  candidate_space:
    type: AttentionCandidate[]

  observations:
    type: ObservationRef[]

  active_objective:
    type: GoalState

  constraints:
    type: ConstraintSet

  resource_budget:
    type: ResourceBudget

  uncertainty:
    type: UncertaintyVector

  dependencies:
    type: DependencyGraph

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  hml:
    type: HMLContext

  authority:
    type: AuthorityContext
```

---

# 13. Typed Outputs

```yaml
AttentionPurposeOutput:

  admitted_candidates:
    type: CandidateRef[]

  prioritized_candidates:
    type: PriorityState[]

  allocation_proposal:
    type: AttentionAllocationProposal

  deferred_candidates:
    type: CandidateRef[]

  quarantined_candidates:
    type: CandidateRef[]

  escalation_requests:
    type: EscalationRequest[]

  unresolved_gaps:
    type: GapRef[]

  attention_state:
    type: AttentionState

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - VALID
      - PARTIAL
      - BLOCKED
      - ESCALATED
      - UNKNOWN_GAP
```

---

# 14. State Variables

```text
X_t       = candidate attention space
E_t       = admitted candidate set
A_t       = active allocation
B_t       = available resource budget
G_t       = governing objective
C_t       = constraints
U_t       = uncertainty state
D_t       = dependency graph
P_t       = provenance state
F_t       = freshness state
S_t       = scope
R_t       = regime
HML_t     = active reasoning scale
Q_t       = quarantined candidates
Def_t     = deferred candidates
Comp_t    = competing hypotheses
Contr_t   = contradictions
Gap_t     = unresolved gaps
Auth_t    = authority context
```

---

# 15. Operators

Purpose-level L02 capabilities may include:

```text
INGEST()
NORMALIZE()
ADMIT()
QUARANTINE()

ASSESS_RELEVANCE()
ASSESS_UNCERTAINTY()
ASSESS_CONSEQUENCE()
ASSESS_DEPENDENCY_CRITICALITY()
ASSESS_INFORMATION_VALUE()
ASSESS_COST()

RANK()
COMPARE()
SELECT()

ALLOCATE()
RESERVE()
FOCUS()
SUSTAIN()
SHIFT()
RELEASE()

DEFER()
RESUME()

ESCALATE()
DEESCALATE()

CHECK_FRESHNESS()
REVALIDATE()

INVALIDATE()
REALLOCATE()

RECALL()
REPAIR()
ROLLBACK_PROPOSE()

EMIT_PROPOSAL()
```

These operator names remain `AMOS_MODEL`.

---

# 16. Core Invariants

```text
L02-PURPOSE-INV-001
Attention resources are finite for a bounded execution context.

L02-PURPOSE-INV-002
Allocation cannot exceed the governing resource envelope.

L02-PURPOSE-INV-003
Priority does not establish truth.

L02-PURPOSE-INV-004
Priority does not establish confidence.

L02-PURPOSE-INV-005
Priority does not establish causation.

L02-PURPOSE-INV-006
Priority does not create authority.

L02-PURPOSE-INV-007
Salience cannot automatically dominate decision relevance.

L02-PURPOSE-INV-008
Novelty cannot automatically dominate evidence quality.

L02-PURPOSE-INV-009
Repeated exposure cannot create independent evidence.

L02-PURPOSE-INV-010
Hard constraints are non-compensatory.

L02-PURPOSE-INV-011
Critical contradictions remain visible.

L02-PURPOSE-INV-012
COMPETING hypotheses remain separate until discriminated.

L02-PURPOSE-INV-013
Scope survives attention processing.

L02-PURPOSE-INV-014
Regime survives attention processing.

L02-PURPOSE-INV-015
Freshness-sensitive premises require revalidation.

L02-PURPOSE-INV-016
Provenance must remain recoverable where material.

L02-PURPOSE-INV-017
Confidence cannot exceed weakest load-bearing premise.

L02-PURPOSE-INV-018
Invalidation propagates selectively through actual dependencies.

L02-PURPOSE-INV-019
H/M/L identity survives cross-scale attention.

L02-PURPOSE-INV-020
UNKNOWN/GAP cannot become PASS through prioritization.

L02-PURPOSE-INV-021
Resource exhaustion does not imply epistemic completion.

L02-PURPOSE-INV-022
Proposal cannot silently become commit.
```

---

# 17. Dependencies

Source-bounded dependency model:

```text
L00_REALITY_ENVIRONMENT
        ↓
L01_SENSING_OBSERVATION
        ↓
L02_ATTENTION
```

L02 additionally depends, in the governed AMOS model, on access to:

```text
objective state
resource state
constraint state
dependency state
scope
regime
freshness
provenance
uncertainty
H/M/L context
authority context
```

Candidate local contract dependencies:

```yaml
dependencies:

  upstream:
    - L01_SENSING_OBSERVATION

  local:
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_PROTOCOLS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_CONTROL_PLANES

  governance:
    - constraints
    - provenance
    - authority
    - freshness
    - scope
    - regime
```

The exact canonical downstream dependency graph remains unresolved.

---

# 18. H/M/L Applicability

## H — Governing Attention

Purpose:

> Decide which classes of issue deserve system-level attention.

Examples:

```text
critical system objective
safety failure
authority conflict
critical gap
regime change
major contradiction
```

Question:

```text
What is important enough to shape the whole reasoning process?
```

---

## M — Allocation Attention

Purpose:

> Allocate finite resources among competing tasks, hypotheses, evidence paths, agents, tools, or workstreams.

Examples:

```text
research branch allocation
tool selection
file inspection priority
hypothesis comparison
subsystem debugging
```

Question:

```text
Which reasoning path should receive resources next?
```

---

## L — Local Attention


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_Infrastructure_Cross_Skill_Proof_Composition_Report.md` (13769 bytes in vault)

### 2. Architecture Boundary

AMOS Full Brain is treated as a structural orchestration layer, not as proof of literal biological cognition, consciousness, or autonomous external authority.

The AMOS Infrastructure Control Plane sits above domain/specialist Skills:

```text
Environment
→ Domain / Specialist Skills
→ Typed Evidence / Proof ABI
→ AMOS Infrastructure Control Plane
→ Commit / Action
```

Domain and specialist Skills may:

- produce bounded evidence;
- perform domain-specific analysis;
- emit typed proofs;
- identify risks;
- propose actions.

They may not own:

- root authoritative state;
- final authority;
- cross-Skill freshness truth;
- durable effect finality;
- commit/release authority.

---

### Weak Architecture

```text
semantic-flow Skill → PASS
exposure Skill      → PASS
authorization Skill → PASS
observability Skill → PASS

therefore → COMMIT
```

This is unsafe if those proofs were produced against different:

- policy epochs;
- authority epochs;
- environment epochs;
- semantic-transaction identities;
- effect digests;
- capability-contract versions.

### 4. Failure 2 — Missing Proof Treated As Optional

A second weak design validates whichever proofs happened to arrive.

Suppose the capability contract requires:

```text
semantic flow
+ information exposure
+ authorization
+ observability
```

but the exposure proof is absent.

A “validate what arrived” implementation can incorrectly continue.

### 5.1 Required_Proof_Closure

```text
REQUIRED_PROOF_CLOSURE[
    capability_contract_hash,
    required_skill_ids[],
    required_proof_types[],
    optional_skill_ids[],
    closure_hash,
    capability_epoch
]
```

Rule:

```text
MissingRequiredProof
→ REVALIDATE_MISSING_PROOF
```

The closure is capability-derived and must not be inferred from observed messages or available workers.

---

### 5.2 Multi_Skill_Proof_Join

```text
MULTI_SKILL_PROOF_JOIN[
    join_id,
    effect_digest,
    semantic_transaction_hash,
    capability_contract_hash,
    policy_hash,
    constraint_hash,
    authority_id,
    authority_epoch,
    environment_epoch,
    required_proof_closure_hash,
    member_proof_ids[],
    member_proof_hashes[],
    join_epoch,
    join_hash
]
```

Every load-bearing proof must bind to one compatible join identity.

---

### 6. Joint Proof Gate

Proposed infrastructure rule:

```text
JointProofReady =
    RequiredProofClosureComplete
    AND MemberProofsValid
    AND CompositionEpochCompatible
    AND NoCrossSkillConflict
```

A joined proof is still **not** commit authority.

Before release, AMOS infrastructure must independently:

1. re-read current authoritative state;
2. recompute required-proof closure from the frozen capability contract;
3. compare current effect, transaction, policy, authority and environment identity;
4. verify proof hashes;
5. verify ledger/read-set freshness where required;
6. reject authority-expanding substitutions;
7. return commit, revalidation, reconciliation, or block.

---

### 7. Agent Architecture Enhancement

The latest role architecture is:

```text
OriginResolver
ExposureAccountant
IndependentAccountantAuditor
ModelValidityAuditor
ReservationCoordinator
ControlPlaneProofAssembler
CompositionAuditor
ReleaseReconciler
```

### 8. Separation-Of-Duty Law

Logical role names alone are insufficient.

For high-consequence operations, roles should bind to:

```text
principal_id
runtime_id
service_account
control_root
provider/model family
tool authority
ledger-write authority
veto authority
binding epoch
```

Hard distinction:

```text
RoleNameSeparation != ControlRootSeparation
```

A worker should not be allowed to:

```text
propose release
+ certify independent safety
+ mutate authoritative release state
```

under one control root.

---

### 9. Information-Exposure Control Integration

The previous exposure-control architecture remains in force:

```text
SEMANTIC_ORIGIN_EQUIVALENCE_CLASS
→ SEMANTIC_ORIGIN_HYPEREDGE
→ EXPOSURE_ACCOUNTANT_SPEC
→ EXPOSURE_MODEL_VALIDITY_ENVELOPE
→ EXPOSURE_ERROR_ENVELOPE
→ ORIGIN_EXPOSURE_LEDGER
→ INFORMATION_EXPOSURE_RESERVATION
→ CONTROL_PLANE_ABI_PROOF
→ MULTI_SKILL_PROOF_JOIN
→ AMOS commit gate
```

Hard distinctions retained:

```text
DifferentObjectID != DifferentSemanticOrigin
DifferentAccount != IndependentExposureBudget
LocalDeclassificationPass != CompositionPass
AccountantOutput != AccountantApplicability
AccountantAgreement != AccountantCorrectness
SkillPassToken != CommitAuthority
AllLocalSkillPass != JointProofPass
```

---

### Open Policy Agent

OPA can provide deterministic policy decisions and versioned policy/data management.

Architectural boundary:

```text
PolicyDecision != AMOSCommitAuthority
```

AMOS must still bind the policy decision to the current:

- semantic transaction;
- effect;
- authority;
- capability contract;
- authoritative state;
- commit-time freshness.

### Code-As-Agent Harness

Code-based harnesses can externalize:

- state;
- tests;
- execution traces;
- verification steps;
- multi-agent shared artifacts.

Boundary:

```text
ExecutionPass != UniversalCorrectness
```

Results remain bound to the exact artifact, environment, test oracle and runtime.

### Formal Action Verification

Formal/proof-constrained execution can substantially strengthen high-privilege action gating when the relevant property is decidable and correctly formalized.

Boundary:

```text
FormalProofOfDeclaredProperty
!= ProofOfCompleteExternalSafety
```

Guarantees inherit:

- formalization correctness;
- verifier correctness;
- trusted computing base;
- covered action interface;
- declared assumptions.

---

### 15. Final Architecture Law

> **AMOS is not the model's reasoning style. AMOS is the governed infrastructure that decides whether bounded model/domain evidence is admissible, composable, current, authorized, observable, and safe enough to become an external effect.**

And therefore:

> **Model proposal != Skill output != proof join != authoritative commit != external consequence.**

---

AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_infrastructure_cross_skill_proof_composition_report
node_type: note
path: 11_KNOWLEDGE/AMOS_Infrastructure_Cross_Skill_Proof_Composition_Report.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** [[references_MOC]]
