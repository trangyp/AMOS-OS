---
title: L02 ATTENTION PRIMITIVES COGNITIVE MATRIX SKILLS
type: skill
tags: [cognitive_matrix, primitives, l02_attention, note]
---



# L02_ATTENTION — Skills

**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Origin architect / steward:** Trang Phan  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed normalization pass · **Date:** `2026-08-26`

## Purpose

Define the AMOS contract for `L02_ATTENTION` / `SKILLS.md`.

This artifact specifies how **Skills may support attention allocation** without confusing an available capability with evidence, authority, execution, validation, or durable state change.

> **Core contract:** L02 may select, rank, invoke, defer, or recommend a Skill because it is relevant to an attended objective. Skill availability does not prove correctness, grant authority, or authorize effects.

## Source / canon references

Current L02 source material identifies the primitive as **attention allocation / budgeting scarce reasoning-observation resources** and requires explicit treatment of RSCF/GMEF links, provenance, repair/rollback, tests/falsifiers, governance/authority, freshness, and lineage before promotion. 

The AMOS RSCF contract further requires typed knowledge nodes, explicit dependencies, applicability envelopes, provenance ancestry, competing hypotheses, falsifiers, gap classification, and weakest-premise confidence ceilings.  

No direct canonical `L02_ATTENTION/SKILLS.md` implementation has been recovered in the available source evidence. Therefore, the detailed Skill architecture below remains `AMOS_MODEL`.

## Definition and scope

A Skill is an addressable capability package that may perform or guide a bounded operation relevant to an attention target.

For L02:

[
SkillCandidate_i =
T[id,\ capability,\ inputs,\ outputs,\ constraints,\ evidence,\ authority]
]

L02's relationship to Skills is modeled as:

[
AttentionState
\rightarrow
SkillSelectionProposal
\rightarrow
GovernanceCheck
\rightarrow
Invocation
\rightarrow
ObservedResult
\rightarrow
RSCFUpdate
]

not:

[
AttentionState \rightarrow AutomaticExecution
]

The Skill layer covers capability discovery, relevance assessment, candidate ranking, invocation proposals, result admission, failure handling, and provenance preservation.

It does **not** independently establish truth, authorization, successful execution, validation, or commit permission.

## Typed inputs / outputs

```yaml
SkillSelectionInput:
  objective: GoalRef
  attention_target: AttentionTarget
  candidate_skills: SkillDescriptor[]
  rscf_context: RSCFRef | null
  hml_context: HMLContext
  constraints: ConstraintSet
  resource_budget: ResourceBudget
  authority_context: AuthorityContext
  freshness_requirements: FreshnessPolicy
  risk_context: RiskState

SkillSelectionOutput:
  selected_skill: SkillRef | null
  alternatives: SkillRef[]
  rationale_refs: ClaimRef[]
  required_inputs: InputRequirement[]
  expected_output_type: TypeRef | null
  authority_required: AuthorityRequirement[]
  validation_required: ValidatorRef[]
  provenance_requirements: ProvenanceRequirement[]
  confidence_ceiling: ConfidenceBound
  disposition:
    - INVOKE
    - PROPOSE
    - DEFER
    - ESCALATE
    - REJECT
    - UNKNOWN
```

## State variables

```text
SK_t       = known Skill registry/view
Cand_t     = candidate Skills
Elig_t     = eligible Skills
Sel_t      = selected Skill
Cap_t      = declared capability
Auth_t     = available authority
Budget_t   = attention/execution budget
Risk_t     = consequence/risk state
Prov_t     = provenance state
Fresh_t    = Skill/version freshness
Exec_t     = execution state
Val_t      = validation state
Fail_t     = Skill failures
RSCF_t     = governing claim context
```

## Operators

Candidate operators remain `AMOS_MODEL`:

```text
DISCOVER_SKILLS()
MATCH_SKILL()
FILTER_INELIGIBLE()
CHECK_CAPABILITY()
CHECK_INPUT_CONTRACT()
CHECK_OUTPUT_CONTRACT()
CHECK_VERSION()
CHECK_FRESHNESS()
CHECK_PROVENANCE()
CHECK_AUTHORITY()
CHECK_RESOURCE_BUDGET()
CHECK_RISK()
RANK_SKILLS()
SELECT_SKILL()
PROPOSE_INVOCATION()
INVOKE_SKILL()
CAPTURE_RESULT()
VALIDATE_RESULT()
ADMIT_EVIDENCE()
QUARANTINE_RESULT()
FALLBACK_SKILL()
ESCALATE()
ROLLBACK()
```

## Invariants

```text
L02-SKILL-INV-001
SKILL_AVAILABLE != SKILL_RELEVANT

L02-SKILL-INV-002
SKILL_RELEVANT != SKILL_SELECTED

L02-SKILL-INV-003
SKILL_SELECTED != SKILL_INVOKED

L02-SKILL-INV-004
SKILL_INVOKED != SKILL_SUCCEEDED

L02-SKILL-INV-005
SKILL_SUCCEEDED != RESULT_VALIDATED

L02-SKILL-INV-006
CAPABILITY != AUTHORITY

L02-SKILL-INV-007
PROPOSAL != COMMIT

L02-SKILL-INV-008
A Skill's description is a capability claim, not proof of execution.

L02-SKILL-INV-009
A Skill result inherits its evidence and provenance limitations.

L02-SKILL-INV-010
Multiple Skills sharing the same evidence ancestry do not create independent confirmation.

L02-SKILL-INV-011
Skill invocation cannot raise an RSCF confidence ceiling without new admissible evidence.

L02-SKILL-INV-012
Skill selection cannot erase COMPETING hypotheses.

L02-SKILL-INV-013
Skill failure cannot silently become success through fallback.

L02-SKILL-INV-014
Irreversible effects require control-plane authorization.

L02-SKILL-INV-015
UNKNOWN/GAP != PASS.
```

## Dependencies

Primary modeled dependency chain:

```text
L01_SENSING_OBSERVATION
        ↓
L02_ATTENTION
        ↓
attention target
        ↓
Skill matching
        ↓
governance / authority validation
        ↓
Skill invocation
        ↓
result/evidence
        ↓
RSCF update
```

Relevant L02 sibling contracts include `PURPOSE`, `DEFINITION`, `VARIABLES`, `STATE`, `OPERATORS`, `INVARIANTS`, `DEPENDENCIES`, `HML`, `CONTROL_PLANES`, `AGENTS`, `WORKFLOWS`, `PROTOCOLS`, `PROVENANCE`, `FAILURE_MODES`, `REPAIR`, `TESTS`, and `RSCF`.

## H/M/L applicability

**H — capability architecture:** Which capability families are relevant to the governing objective, constraints, and consequence envelope?

**M — Skill routing:** Which specialist Skill or Skill composition best resolves a subsystem-level uncertainty or operation?

**L — invocation:** Which concrete Skill call, input contract, evidence read, validation, or local transformation should execute next?

Cross-scale invariant:

```text
H relevance
!=
M eligibility
!=
L invocation permission
```

## Control-plane requirements

L02 may determine that a Skill deserves attention. It must not manufacture authority to invoke consequential effects.

The control plane should govern, when material:

```text
identity
capability registration
Skill/version identity
input admissibility
authority
resource limits
privacy/exposure
external effects
mutable state
freshness
commit eligibility
rollback/recovery
audit provenance
```

High-consequence Skill use should be staged:

```text
SELECT
→ PROPOSE
→ AUTHORIZE
→ EXECUTE
→ VALIDATE
→ COMMIT
```

where the domain permits these stages.

## Agents

Candidate architectural roles:

```text
L02_SKILL_ROUTER
L02_CAPABILITY_MATCHER
L02_SKILL_ELIGIBILITY_AUDITOR
L02_SKILL_PROVENANCE_AUDITOR
L02_SKILL_RESULT_VALIDATOR
L02_SKILL_FALLBACK_COORDINATOR
```

These are roles, not claims of implemented autonomous agents.

## Skills

Candidate AMOS capability mappings include:

```text
AMOS Attention Allocation Governor
RSCF Modeler
AMOS Claim Verifier
AMOS Infrastructure Control Plane
AMOS Constraint Propagation RSCF Engine
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Context Budget Governor RSCF
AMOS Risk Constraint Governor
AMOS Repair Harm Auditor
AMOS Managed Autonomy Escalation RSCF
```

Specialist domain Skills should be loaded only when the attended target falls within their declared scope.

A domain Skill should own domain reasoning; L02 should own attention/routing concerns; infrastructure should retain governance/commit responsibilities.

## Workflows

```text
OBJECTIVE
↓
ATTENTION TARGET
↓
IDENTIFY REQUIRED CAPABILITY
↓
DISCOVER CANDIDATE SKILLS
↓
CHECK SCOPE + VERSION + INPUT CONTRACT
↓
CHECK AUTHORITY / RISK / RESOURCE CONSTRAINTS
↓
RANK ELIGIBLE SKILLS
↓
SELECT MINIMUM SUFFICIENT CAPABILITY
↓
INVOKE OR PROPOSE
↓
CAPTURE OUTPUT + PROVENANCE
↓
VALIDATE
↓
UPDATE RSCF
↓
CONTINUE / STOP / REPAIR / ESCALATE
```

Selection should prefer the **smallest sufficient capability**, not the largest available Skill stack.

## Protocols

Candidate protocol family:

```text
SKILL_DISCOVERY_REQUEST
SKILL_CAPABILITY_QUERY
SKILL_ELIGIBILITY_CHECK
SKILL_SELECTION_PROPOSAL
SKILL_AUTHORIZATION_REQUEST
SKILL_INVOCATION
SKILL_RESULT
SKILL_VALIDATION
SKILL_FAILURE_NOTICE
SKILL_FALLBACK_REQUEST
SKILL_QUARANTINE
SKILL_REPAIR_REQUEST
SKILL_VERSION_INVALIDATION
```

Exact canonical protocol names remain `UNKNOWN/GAP`.

## Evidence / provenance

Each consequential Skill invocation should preserve:

```yaml
skill_provenance:
  skill_id: null
  skill_version: null
  origin: null
  invocation_id: null
  invoked_by: null
  objective_ref: null
  input_refs: []
  evidence_refs: []
  dependencies: []
  execution_environment: null
  timestamp: null
  output_ref: null
  validator_refs: []
  authority_ref: null
  result_state: null
```

A Skill's generated conclusion remains distinguishable from the evidence it consumed.

```text
SKILL OUTPUT != SOURCE EVIDENCE
```

unless the Skill directly performed an admissible observation/test and that observation is separately represented.

## Uncertainty and confidence ceiling

Material uncertainty dimensions:

```yaml
uncertainty:
  skill_relevance: MEDIUM
  capability_fit: MEDIUM
  version_freshness: MEDIUM
  execution: HIGH
  result_validity: HIGH
  authority: HIGH
  provenance_independence: MEDIUM
```

Current confidence ceiling for the detailed L02 Skill architecture is **MODEL-level only** because no direct canonical `SKILLS.md` or executed L02 Skill-routing implementation has been established.

## Failure modes

```text
FM-L02-SK-001 Wrong Skill Selected
FM-L02-SK-002 Missing Required Skill
FM-L02-SK-003 Capability Overclaim
FM-L02-SK-004 Scope Mismatch
FM-L02-SK-005 Stale Skill Version
FM-L02-SK-006 Invalid Input Contract
FM-L02-SK-007 Output-Type Mismatch
FM-L02-SK-008 Unauthorized Invocation
FM-L02-SK-009 Skill Result Treated as Evidence Without Validation
FM-L02-SK-010 Correlated Skill Outputs Counted Independently
FM-L02-SK-011 Failed Invocation Hidden by Fallback
FM-L02-SK-012 Excessive Skill Composition
FM-L02-SK-013 Resource Budget Overrun
FM-L02-SK-014 Provenance Loss
FM-L02-SK-015 Irreversible Effect Without Commit Gate
FM-L02-SK-016 MODEL Skill Mapping Reported as Canon
```

## Repair / recovery

```text
DETECT FAILURE
↓
FREEZE AFFECTED RESULT
↓
PRESERVE ORIGINAL INPUTS + PROVENANCE
↓
CLASSIFY FAILURE
↓
INVALIDATE DEPENDENT CLAIMS ONLY
↓
RECHECK CAPABILITY / VERSION / AUTHORITY
↓
SELECT ALTERNATIVE OR REPAIR
↓
REEXECUTE IF JUSTIFIED
↓
VALIDATE RESULT
↓
RESTORE DEPENDENT RSCF STATE
```

Do not retry the identical failed Skill path without changed evidence, configuration, inputs, version, or execution conditions.

## Tests / validators

Minimum validation suite:

```text
TEST-L02-SK-001
Relevant Skill unavailable.
Expected: GAP/ESCALATE, not fabricated capability.

TEST-L02-SK-002
Skill exists but lacks required authority.
Expected: no consequential invocation.

TEST-L02-SK-003
Skill output contradicts source evidence.
Expected: preserve contradiction.

TEST-L02-SK-004
Two Skills derive from identical source ancestry.
Expected: no false independence.

TEST-L02-SK-005
Skill version becomes stale.
Expected: revalidation.

TEST-L02-SK-006
Invocation fails.
Expected: failure recorded before fallback.

TEST-L02-SK-007
Skill succeeds but output is unvalidated.
Expected: success != validated conclusion.

TEST-L02-SK-008
High-priority target selects an out-of-scope Skill.
Expected: reject.

TEST-L02-SK-009
Skill proposes irreversible action.
Expected: control-plane authorization required.

TEST-L02-SK-010
No Skill satisfies the contract.
Expected: UNKNOWN/GAP, not PASS.
```

## Falsifiers

Revise this contract if direct canon establishes that:

* L02 does not perform Skill selection or capability routing.
* Skill routing belongs exclusively to another AMOS layer.
* canonical Skill ownership differs materially from this decomposition.
* L02 has a different H/M/L Skill model.
* direct source defines incompatible authority or invocation semantics.
* runtime evidence contradicts the modeled selection/validation sequence.

## Gap status

```yaml
gap_status:
  L02_attention_role:
    status: SOURCE_SUPPORTED

  scarce_resource_role:
    status: SOURCE_SUPPORTED

  requirement_for_governed_interfaces:
    status: SOURCE_SUPPORTED

  skill_selection_architecture:
    status: MODEL_DEFINED

  skill_input_output_contract:
    status: MODEL_DEFINED

  skill_provenance_contract:
    status: MODEL_DEFINED

  HML_skill_mapping:
    status: MODEL_DEFINED

  control_plane_boundary:
    status: MODEL_DEFINED

  canonical_L02_SKILLS_md:
    status: UNKNOWN_GAP

  canonical_skill_registry:
    status: UNKNOWN_GAP

  canonical_skill_selection_algorithm:
    status: UNKNOWN_GAP

  canonical_protocol_names:
    status: UNKNOWN_GAP

  canonical_agent_skill_mapping:
    status: UNKNOWN_GAP

  runtime_implementation:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP
```

## RSCF completion state

```yaml
claim_class: MODEL

evidence:
  - L02_ATTENTION/PLACEHOLDER.md
  - AMOS RSCF framework conventions

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  primitive: L02_ATTENTION
  artifact: SKILLS.md
  derivation:
    - source-bounded L02 primitive role
    - AMOS RSCF-governed capability-routing model

scope:
  system: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  primitive: L02_ATTENTION
  artifact: SKILLS

regime:
  governed finite-resource reasoning and capability routing

freshness:
  revalidate_on:
    - direct L02 SKILLS canon recovery
    - Skill registry change
    - L02 architecture change
    - control-plane change
    - runtime validation evidence

dependencies:
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION_DEFINITION
  - L02_ATTENTION_STATE
  - L02_ATTENTION_OPERATORS
  - L02_ATTENTION_INVARIANTS
  - L02_ATTENTION_CONTROL_PLANES
  - L02_ATTENTION_AGENTS
  - L02_ATTENTION_WORKFLOWS
  - L02_ATTENTION_PROTOCOLS
  - L02_ATTENTION_PROVENANCE
  - L02_ATTENTION_RSCF

competing:
  - L02 directly owns Skill routing
  - shared cognition layer owns Skill routing
  - infrastructure control plane owns routing
  - hybrid routing with L02 selection and infrastructure authorization

falsifiers:
  - incompatible direct canon
  - incompatible runtime implementation
  - executed tests falsifying modeled routing boundaries

confidence_ceiling:
  class: MODEL
  reason:
    detailed L02 Skill architecture is not directly canon-validated
```

## Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS

SKILL AVAILABLE != SKILL ELIGIBLE
SKILL SELECTED != SKILL INVOKED
SKILL INVOKED != SKILL SUCCEEDED
SKILL SUCCEEDED != RESULT VALIDATED
SKILL OUTPUT != SOURCE EVIDENCE
SKILL COMPOSITION != INDEPENDENT CONFIRMATION
ATTENTION PRIORITY != AUTHORIZATION
MODEL SKILL MAP != CANON
TEST DEFINED != TEST EXECUTED
```

**Conclusion class: `MODEL`.** The L02 attention/scarce-resource role is source-supported; the detailed Skill registry, routing operators, protocols, agent mappings, ownership model, runtime enforcement, and validation remain explicit `UNKNOWN/GAP` or modeled structure rather than recovered canon.

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_skills
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_SKILLS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
