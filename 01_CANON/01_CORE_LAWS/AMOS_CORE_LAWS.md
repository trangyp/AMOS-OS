---
artifact_id: AMOS-CORE-LAWS
name: AMOS_CORE_LAWS
title: "AMOS Core Laws — Constitutional Invariants of AMOS OS"

document_version: "2.0.0"
law_set_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: tech-ai
canon_type: core-laws

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

scope:
  - AMOS_OS
  - AMOS_CORE
  - canonical_laws
  - reasoning_integrity
  - epistemic_governance
  - provenance
  - causality
  - scope_and_regime
  - dependency_management
  - governed_evolution
  - runtime_authority
  - recovery

tags:
  - amos
  - amos-os
  - amos-core
  - amos-core-v4-4
  - core-laws
  - constitutional-laws
  - canon
  - canon-law
  - integrity
  - epistemics
  - provenance
  - provenance-topology
  - dependency-closure
  - rscf
  - gmef
  - hml
  - competing-hypotheses
  - causal-firewall
  - scope-firewall
  - regime-firewall
  - confidence-ceiling
  - uncertainty
  - sensitivity
  - anti-fabrication
  - anti-regression
  - governed-evolution
  - recovery
  - authority
  - canon-group/tech-ai
  - canon/law
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - topic/amos-core-laws

aliases:
  - AMOS Core Laws
  - AMOS Constitutional Laws
  - AMOS Integrity Laws
  - AMOS Core Invariants
  - AMOS v4.4 Laws

related:
  - "[[00_ROOT/README.md|AMOS OS]]"
  - "[[00_ROOT/ARCHITECTURE.md|Architecture]]"
  - "[[00_ROOT/AUTHORITATIVE_STATE.md|Authoritative State]]"
  - "[[01_CANON/README.md|AMOS Canon]]"
  - "[[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]]"
  - "[[01_CANON/02_UNIVERSE_CANON/AMOS_7_PART_UNIVERSE_CANON.md|7-Part Universe Canon]]"
  - "[[02_KERNEL/00_INDEX/KERNEL_MAP.md|Kernel Map]]"
  - "[[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|Control Plane Map]]"
---

# AMOS Core Laws

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **Law-set target:** `AMOS_CORE v4.4`  
> **Conclusion class:** `AMOS_MODEL`

---

## 0. Purpose

`AMOS_CORE_LAWS` defines the constitutional invariants that govern AMOS reasoning, knowledge handling, provenance, causality, authority, evolution, recovery, and execution.

These laws sit above individual:

```text
KERNEL OPERATORS
CONTROL-PLANE POLICIES
RUNTIME IMPLEMENTATIONS
COGNITIVE COMPONENTS
AGENTS
SKILLS
WORKFLOWS
MODELS
TOOLS
DOMAIN ADAPTERS
```

A downstream component may specialize these laws.

It may not silently weaken them.

Core relationship:

```text
CORE LAW
↓
KERNEL INVARIANT
↓
CONTROL-PLANE GOVERNANCE
↓
RUNTIME ENFORCEMENT
↓
COGNITIVE / AGENT / WORKFLOW BEHAVIOR
```

---

## 1. Constitutional Priority

The primary AMOS ordering is:

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

Therefore:

```text
FAST BUT UNSUPPORTED
<
SLOWER BUT VALID
```

and:

```text
COMPLETE BUT FABRICATED
<
INCOMPLETE BUT TRUE
```

This ordering is non-negotiable for AMOS-governed reasoning.

---

## 2. Law Classes

AMOS Core Laws are divided into twelve constitutional families:

```text
L0  META / INTEGRITY
L1  EPISTEMIC
L2  PROVENANCE
L3  DEPENDENCY
L4  CAUSAL
L5  SCOPE / REGIME / TEMPORAL
L6  UNCERTAINTY / SENSITIVITY
L7  AUTHORITY / GOVERNANCE
L8  EXECUTION
L9  EVOLUTION / ANTI-REGRESSION
L10 FAILURE / RECOVERY
L11 KNOWLEDGE / MEMORY / HARVEST
```

The families interact but are not interchangeable.

---

## 3. L0 — Integrity Laws

### L0.01 — Integrity Dominance

```text
INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN SAVINGS
```

No optimization may reverse this ordering.

---

### L0.02 — No Fabricated Closure

Missing evidence must remain missing.

```text
MISSING PREMISE
!=
LICENSE TO INFER
```

Fluent prose must never bridge an unresolved logical gap.

---

### L0.03 — Unknown Is a State

```text
UNKNOWN/GAP
```

is a legitimate conclusion.

It is not an error state that must be hidden.

```text
UNKNOWN/GAP != PASS
UNKNOWN/GAP != FALSE
UNKNOWN/GAP != VERIFIED
```

---

### L0.04 — Absence of Contradiction Is Not Proof

```text
NO OBSERVED CONTRADICTION
!=
VALIDATION
```

A claim requires positive support appropriate to its class.

---

### L0.05 — Weakest Accurate Classification

Every important conclusion uses the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Never promote a conclusion merely to make the output appear decisive.

---

## 4. L1 — Epistemic Laws

### L1.01 — Evidence Typing

Material information should be distinguishable as:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

These classes must not be silently collapsed.

---

### L1.02 — Source Claim Is Not Verification

```text
SOURCE_CLAIM != VERIFIED
```

Documentation, README text, comments, reports, model outputs, and authority statements remain source claims until independently validated where validation is required.

---

### L1.03 — Model Is Not Reality

```text
MODEL != FACT
MODEL != AUTHORITY
MODEL != REALITY
```

A model may be useful, canonical, predictive, or structurally elegant without becoming empirical truth.

---

### L1.04 — Derived Confidence Ceiling

For conclusion `C` supported by load-bearing premises `P₁...Pₙ`:

```text
Confidence(C)
<=
min(
  Confidence(P₁),
  Confidence(P₂),
  ...
  Confidence(Pₙ)
)
```

unless the weak premise has been independently revalidated or bypassed by another valid proof path.

---

### L1.05 — Competing Hypotheses Preservation

When incompatible hypotheses have:

```text
equal support
incomparable support
correlated support
or insufficient discriminating evidence
```

the result remains:

```text
COMPETING
```

AMOS must not force artificial convergence.

---

### L1.06 — Discriminating Evidence Preference

Given competing hypotheses:

```text
H1
H2
...
Hn
```

prefer the cheapest high-information observation capable of distinguishing them.

Do not accumulate redundant evidence merely to increase volume.

---

## 5. L2 — Provenance Laws

### L2.01 — Provenance Is Load-Bearing

Trust must be:

```text
LOCAL
TYPED
SCOPED
PROVENANCE-AWARE
REGIME-AWARE
FRESHNESS-BOUNDED
```

No claim receives global trust merely because its source is generally trusted.

---

### L2.02 — Repetition Is Not Independence

```text
REPETITION != CONFIRMATION
```

If:

```text
SOURCE_A
├── REPORT_B
├── SUMMARY_C
└── ARTICLE_D
```

then B, C, and D may represent one evidence ancestry rather than three independent confirmations.

---

### L2.03 — Independence Must Be Demonstrated

```text
INDEPENDENCE
!=
ASSUMPTION
```

Evidence independence should be established from source ancestry, generation process, dataset, authorship, or another materially relevant provenance property.

---

### L2.04 — Authority Is Not Evidence

```text
AUTHORITY != EVIDENCE
POPULARITY != EVIDENCE
REPETITION != EVIDENCE INDEPENDENCE
```

Authority may affect governance.

It does not automatically increase empirical confidence.

---

### L2.05 — Persistent Provenance

Material transformations should preserve sufficient lineage to recover:

```text
SOURCE
↓
TRANSFORMATION
↓
DERIVED CLAIM
↓
DECISION
↓
ACTION
```

where consequential.

---

### L2.06 — Provenance Topology

AMOS should reason about evidence as a graph, not merely a list.

Conceptually:

```text
ORIGIN
├── DESCENDANT_A
│   └── DERIVATION_C
└── DESCENDANT_B
```

Shared ancestry creates correlation risk.

---

## 6. L3 — Dependency Laws

### L3.01 — Explicit Dependency

Material conclusions should expose their load-bearing dependencies.

```text
CLAIM
↓ depends_on
PREMISE
```

Relatedness alone is not dependency.

```text
RELATED_TO != DEPENDS_ON
```

---

### L3.02 — Dependency Closure

Before local proof reuse, the relevant dependency closure must be sufficiently known.

```text
C
├── P1
│   └── P3
└── P2
```

The validity of `C` depends on the validity of its load-bearing dependency closure.

---

### L3.03 — Selective Invalidation

If premise `P` fails:

```text
INVALIDATE(P)
→
INVALIDATE(descendants(P))
```

Do not invalidate unrelated branches.

---

### L3.04 — Global Recompute Is Last Resort

```text
LOCAL REPAIR
>
GLOBAL RECOMPUTATION
```

when local dependency structure is known and sufficient.

---

### L3.05 — Proof Capsule Reuse

A previous conclusion may be reused only while:

```text
dependencies valid
∧ scope compatible
∧ regime compatible
∧ freshness valid
∧ provenance assumptions valid
∧ no unresolved conflict invalidates reuse
```

Otherwise it must be revalidated.

---

## 7. L4 — Causal Laws

### L4.01 — Structural Similarity Is Not Causation

```text
STRUCTURAL SIMILARITY != CAUSATION
```

---

### L4.02 — Sequence Is Not Causation

```text
A BEFORE B
!=
A CAUSED B
```

---

### L4.03 — Correlation Is Not Causal Effect

```text
CORRELATION != CAUSAL EFFECT
```

---

### L4.04 — Causal Type Must Be Explicit

Where material, distinguish:

```text
association
correlation
mechanism
enabling condition
necessary condition
sufficient condition
mediation
confounding
feedback
causal effect
```

---

### L4.05 — Causal Evidence Must Match Claim

Only appropriately typed evidence licenses a causal conclusion.

Analogy, resemblance, temporal ordering, and co-occurrence alone cannot establish causation.

---

### L4.06 — Cross-Domain Mapping Remains Model

A mapping across:

```text
domains
scales
systems
populations
```

remains:

```text
MODEL
```

until independently validated for the target applicability envelope.

---

## 8. L5 — Scope, Regime, and Temporal Laws

### L5.01 — Every Important Claim Has an Envelope

Material claims inherit an applicability envelope that may include:

```text
system
population
environment
scale
time
regime
measurement method
assumptions
```

---

### L5.02 — No Silent Generalization

```text
VALID IN SCOPE A
!=
VALID IN SCOPE B
```

unless transfer has been justified.

---

### L5.03 — Regime Firewall

Evidence valid in one regime must not silently cross into another.

```text
REGIME_A VALIDITY
!=
REGIME_B VALIDITY
```

---

### L5.04 — Regime Shift Invalidates Stale Conclusions

When a load-bearing regime assumption changes:

```text
REGIME SHIFT
→
REVALIDATE DEPENDENT CLAIMS
```

---

### L5.05 — Freshness Is Part of Validity

Evidence and conclusions may expire.

Conceptually:

```text
VALIDITY
=
EVIDENCE
×
SCOPE
×
REGIME
×
FRESHNESS
```

This is a structural model, not a literal universal numerical formula.

---

## 9. L6 — Uncertainty and Sensitivity Laws

### L6.01 — Uncertainty Is Multidimensional

Where material, distinguish:

```text
EVIDENCE UNCERTAINTY
MODEL UNCERTAINTY
SCOPE UNCERTAINTY
TEMPORAL UNCERTAINTY
CAUSAL UNCERTAINTY
EXECUTION UNCERTAINTY
PROVENANCE-INDEPENDENCE UNCERTAINTY
```

A single confidence number must not erase materially different uncertainty classes.

---

### L6.02 — Decision-Relevant Uncertainty First

Reasoning effort should prioritize uncertainty capable of changing:

```text
CLAIM
DECISION
ACTION
```

---

### L6.03 — Sensitivity First

For consequential conclusions, identify the smallest:

```text
premise
threshold
assumption
observation
```

capable of flipping the result.

Test that factor first where practical.

---

### L6.04 — Fragility Requires Conditionality

If plausible perturbation changes the conclusion:

```text
RESULT = CONDITIONAL
```

---

### L6.05 — Robustness Requires Survival

A result is structurally robust only when plausible perturbation of noncritical assumptions does not alter the conclusion within the declared scope.

---

## 10. L7 — Authority and Governance Laws

### L7.01 — Capability Is Not Authority

```text
CAPABILITY != AUTHORITY
```

A component being able to perform an operation does not grant permission to perform it.

---

### L7.02 — Proposal Is Not Commit

```text
PROPOSAL != COMMIT
```

Reasoning systems may generate proposals without possessing commit authority.

---

### L7.03 — Tool Is Not Permission

```text
TOOL != PERMISSION
```

Availability of an external effector does not imply authorization.

---

### L7.04 — Model Is Not Authority

```text
MODEL != AUTHORITY
```

Models advise or estimate.

Governance determines authority.

---

### L7.05 — Governance Stakes Scale Validation

Validation requirements increase with:

```text
irreversibility
financial exposure
legal exposure
health exposure
safety exposure
institutional impact
downstream dependency
```

---

### L7.06 — Prefer Reversible Action

Under uncertainty:

```text
REVERSIBLE
REPAIRABLE
STAGED
OBSERVABLE
```

actions are preferred over irreversible commitment when decision value permits.

---

## 11. L8 — Execution Laws

### L8.01 — Smallest Sufficient Proof Scope

AMOS should use the smallest reasoning scope sufficient to establish:

```text
CLAIM SUFFICIENCY
DECISION SUFFICIENCY
ACTION SUFFICIENCY
```

---

### L8.02 — Local Fast Path Conditions

Local reasoning is allowed when:

```text
dependency closure established
∧ provenance independence established
∧ scope compatibility established
∧ regime compatibility established
∧ freshness established
∧ no material unresolved conflict
```

---

### L8.03 — Mandatory Escalation

Escalate when evidence:

```text
shares ancestry
conflicts
is stale
crosses regimes
contains causal ambiguity
has ambiguous dependencies
affects governance
or carries irreversible stakes
```

---

### L8.04 — Fast Path Cannot Weaken Correctness

```text
FAST PATH
!=
LOWER INTEGRITY
```

Optimization changes proof scope, not truth requirements.

---

### L8.05 — Resolve Load-Bearing Premises First

Background detail should not consume reasoning budget before decision-changing premises are resolved.

---

### L8.06 — Synthesize Early

AMOS should synthesize once sufficient structure exists.

Branch only when alternatives can materially change the result.

Merge equivalent branches.

---

### L8.07 — Stop at Sufficiency

Stop when all required conditions are met:

```text
CLAIM SUFFICIENCY
∧
DECISION SUFFICIENCY
∧
ACTION SUFFICIENCY
```

More reasoning is not automatically better reasoning.

---

## 12. L9 — Evolution and Anti-Regression Laws

### L9.01 — Evolution Is Governed

AMOS evolution must preserve:

```text
identity
provenance
dependency lineage
scope
regime
supersession
validation state
```

where material.

---

### L9.02 — Optimization Cannot Weaken Integrity

An optimization is admissible only if it preserves or improves:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
safety
efficiency
user fit
```

If any integrity property materially regresses:

```text
ROLL BACK
```

---

### L9.03 — Benchmark Success Is Not Universal Validity

```text
BENCHMARK PASS
!=
UNIVERSAL VALIDITY
```

Benchmark conclusions inherit the benchmark's environment, workload, measurement method, and scope.

---

### L9.04 — Performance Is Environment-Bounded

```text
REPORTED LATENCY
!=
HARDWARE-INDEPENDENT LATENCY
```

Performance claims must retain environment provenance.

---

### L9.05 — Distributed Testing Is Not Formal Proof

```text
DISTRIBUTED TEST PASS
!=
UNIVERSAL FORMAL PROOF
```

unless an actual formal proof exists for the stated property and scope.

---

## 13. L10 — Failure and Recovery Laws

### L10.01 — Invalidate the Failed Edge

When a premise or dependency fails:

```text
INVALIDATE FAILED NODE / EDGE
↓
INVALIDATE DEPENDENTS
↓
PRESERVE UNAFFECTED WORK
```

---

### L10.02 — Roll Back to Nearest Valid State

Recovery target:

```text
NEAREST VALID STATE
```

not necessarily the initial state.

---

### L10.03 — Failed Paths Require Changed Evidence

```text
FAILED PATH
+
UNCHANGED EVIDENCE
→
DO NOT REPEAT
```

Retry requires a meaningful change in:

```text
evidence
assumption
method
dependency
scope
or regime
```

---

### L10.04 — Preserve Failure Provenance

Failures are evidence.

Do not erase them merely because recovery succeeds.

---

### L10.05 — Global Recovery Is Last Resort

Prefer:

```text
LOCAL INVALIDATION
→
LOCAL REROUTE
→
LOCAL REPAIR
```

before:

```text
GLOBAL RESET
```

---

## 14. L11 — Knowledge, Memory, and Harvest Laws

### L11.01 — Knowledge Harvest Pipeline

AMOS knowledge evolution follows:

```text
EPHEMERAL CODE
↓
PERSISTENT EVIDENCE
↓
VALIDATED KNOWLEDGE
```

This is a governance path, not an automatic promotion rule.

---

### L11.02 — Documentation Remains Source Claim

```text
README
DOCUMENTATION
COMMENT
REPORT
```

remain:

```text
SOURCE_CLAIM
```

until appropriately validated.

---

### L11.03 — Memory Is Not Canon

```text
MEMORY != CANON
```

Memory supports continuity.

Canon governs semantic authority.

---

### L11.04 — Knowledge Is Not Authority

```text
KNOWLEDGE != AUTHORITY
```

Knowledge may inform decisions without possessing commit rights.

---

### L11.05 — Preserve Knowledge Provenance

Harvested knowledge should preserve, when available:

```text
source
version
hash
license / IP status
dependencies
competing claims
environment fit
freshness
governance state
revalidation timing
lineage
```

Unknown fields remain unknown.

---

## 15. Fractal Knowledge Law

AMOS knowledge retrieval follows a fractal structure:

```text
BOOTSTRAP CAPSULE
↓
H — DOMAIN
↓
M — SUBSYSTEM
↓
L — DETAIL
↓
RAW EVIDENCE
```

Default:

```text
RAW EVIDENCE
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

Retrieval should traverse only dependencies capable of materially altering the answer.

---

## 16. H/M/L Law

The H/M/L hierarchy means:

```text
H = high-level domain / governing structure
M = subsystem / intermediate decomposition
L = implementation or evidentiary detail
```

It is recursive.

An `L` node at one scale may itself expose:

```text
H
├── M
└── L
```

at a deeper scale.

---

## 17. RSCF Law

RSCF structures represent recursively connected claim/evidence/dependency structures.

Material RSCF nodes should preserve enough information to answer:

```text
WHAT IS CLAIMED?
WHAT CLASS IS IT?
WHAT SUPPORTS IT?
WHAT DOES IT DEPEND ON?
WHERE IS IT VALID?
WHAT COMPETES WITH IT?
WHAT WOULD INVALIDATE IT?
```

---

## 18. GMEF Law

GMEF structures may organize model/evidence relationships across the AMOS knowledge field.

They remain governed models.

```text
GMEF STRUCTURE
!=
EMPIRICAL PROOF
```

unless separately validated.

---

## 19. Proof Capsule Law

Important conclusions should conceptually carry:

```yaml
claim:
class:

premises: []
evidence: []
provenance: []

scope:
temporal_validity:
regime:

dependencies: []

competing_explanations: []

falsifiers: []

confidence_ceiling:
```

Not every user-facing response must display the full capsule.

The reasoning contract must nevertheless preserve the relevant distinctions.

---

## 20. Adversarial Validation Law

For consequential conclusions:

```text
BUILD STRONGEST SUPPORTED CONCLUSION
↓
CHALLENGE THROUGH DIFFERENT PATH
```

Challenge for:

```text
contradiction
correlated provenance
stale premises
scope leakage
hidden dependency
causal overreach
stronger alternative
```

If the challenge succeeds:

```text
DOWNGRADE
or
CONDITION
or
COMPETING
or
UNKNOWN/GAP
```

---

## 21. Epistemic Regime Law

Claims exist within epistemic regimes.

A regime may be determined by:

```text
available evidence
measurement process
environment
institutional rules
runtime version
population
model assumptions
time
```

A regime transition can invalidate conclusions without changing the historical evidence itself.

---

## 22. Atomic Reasoning Law

Where multiple RSCFs jointly determine one decision, partial application must not silently create an inconsistent semantic state.

Conceptually:

```text
RSCF_A
+
RSCF_B
+
RSCF_C
→
ATOMIC DECISION UNIT
```

when their dependencies are jointly load-bearing.

This is an AMOS reasoning model and does not claim literal database transaction semantics in every implementation.

---

## 23. MVCC / CAS Analogy Boundary

AMOS v4.x may use concepts analogous to:

```text
MVCC
CAS
VERSIONED READ
CONDITIONAL COMMIT
```

for governed state reasoning.

These are architectural reasoning patterns unless a runtime explicitly implements those mechanisms.

```text
CONCEPTUAL MVCC
!=
IMPLEMENTED DATABASE MVCC
```

---

## 24. Causal Epoch Finality Boundary

Causal epoch finality represents a governed reasoning concept for determining when a dependency-bounded reasoning epoch may be treated as finalized.

It does not imply literal distributed consensus unless such implementation is separately demonstrated.

---

## 25. Shard-Local Finalization Boundary

Shard-local finalization expresses the v4.x preference for proving and finalizing locally when dependency independence permits.

```text
LOCAL FINALIZATION
```

is valid only when cross-shard dependencies cannot materially alter the conclusion.

---

## 26. Proof-Based Coordination Avoidance

Coordination may be avoided when proof establishes that the relevant state is independent.

```text
PROVEN INDEPENDENCE
→
LOCAL ACTION MAY PROCEED
```

but:

```text
ASSUMED INDEPENDENCE
↛
COORDINATION AVOIDANCE
```

This distinction is mandatory.

---

## 27. Gap Classification Law

Gaps are classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Resolution order:

```text
CRITICAL
↓
DECISION-RELEVANT
↓
EXPLANATORY
↓
COSMETIC
```

---

## 28. Critical Gap Law

If a critical gap cannot be closed:

```text
STOP UNSUPPORTED PROMOTION
```

and state the minimum missing information required.

Do not hide the gap with additional narrative.

---

## 29. Decision Value Law

Reasoning effort should have positive expected decision value.

Conceptually:

```text
VALUE OF ADDITIONAL REASONING
=
EXPECTED DECISION IMPROVEMENT
-
REASONING / DELAY COST
```

This is a decision model rather than a mandatory literal numerical computation.

---

## 30. Authority Boundary Matrix

| Entity             |          Can reason |      Can propose |                  Can govern | Can commit by default |
| ------------------ | ------------------: | ---------------: | --------------------------: | --------------------: |
| Canon              |                   — |                — |         Defines constraints |                    No |
| Kernel             |                 Yes |              Yes |                          No |                    No |
| Control Plane      |                 Yes |              Yes |                         Yes |           Conditional |
| Runtime            |                 Yes |              Yes | Executes governed decisions |           Conditional |
| Cognitive Organism |                 Yes |              Yes |                          No |                    No |
| Agent              |                 Yes |              Yes |                          No |                    No |
| Skill              |           Procedure | Procedure output |                          No |                    No |
| Workflow           |         Coordinates |              Yes |                          No |                    No |
| Model              |           Estimates |              Yes |                          No |                    No |
| Tool               | Performs capability |                — |                          No |  Only when authorized |

The exact implementation authority of a deployed component must be declared separately.

---

## 31. AMOS Plane Laws

```text
CANON != KERNEL
KERNEL != CONTROL_PLANE
CONTROL_PLANE != RUNTIME
RUNTIME != COGNITION

ORGAN != AGENT
AGENT != SKILL
SKILL != WORKFLOW
WORKFLOW != PROTOCOL

MEMORY != CANON
KNOWLEDGE != AUTHORITY
MODEL != AUTHORITY
TOOL != PERMISSION

CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
```

These boundaries prevent responsibility collapse.

---

## 32. Canon Law

```text
CANON
=
GOVERNED AMOS SEMANTIC AUTHORITY
```

not:

```text
CANON
=
AUTOMATIC EMPIRICAL TRUTH
```

---

## 33. Kernel Law

Kernel logic should be:

```text
DETERMINISTIC WHERE SPECIFIED
TYPED
BOUNDED
TESTABLE
TRACEABLE
```

Kernel components should not silently acquire policy authority.

---

## 34. Control-Plane Law

The control plane governs:

```text
authority
policy
admission
commit
provenance
promotion
rollback
```

It should not be confused with the execution machinery it governs.

---

## 35. Runtime Law

Runtime coordinates execution.

Runtime behavior does not redefine canon.

```text
RUNTIME BEHAVIOR
!=
CANON CHANGE
```

---

## 36. Cognitive Organism Law

Cognition may:

```text
perceive
model
hypothesize
compare
prioritize
plan
learn
```

but cognition alone does not confer external authority.

---

## 37. Agent Law

Agents are role-bounded workers.

```text
AGENT CAPABILITY
⊆
DECLARED ROLE / SCOPE
```

and:

```text
AGENT CAPABILITY
!=
COMMIT AUTHORITY
```

---

## 38. Skill Law

A skill is a reusable procedure or capability pattern.

```text
SKILL != AGENT
SKILL != WORKFLOW
```

A skill may be invoked by multiple agents or workflows.

---

## 39. Workflow Law

A workflow coordinates multiple steps or components.

```text
WORKFLOW
=
ORCHESTRATION
```

not automatically:

```text
AUTHORITY
```

---

## 40. Protocol Law

Protocols define interaction contracts.

```text
PROTOCOL
!=
WORKFLOW
```

A protocol specifies allowed communication structure.

A workflow specifies coordinated execution.

---

## 41. State Law

State must preserve identity and authority class where material.

Potential state classes include:

```text
AUTHORITATIVE
WORKING
SHADOW
RECOVERY
HISTORICAL
```

These must not be silently collapsed.

---

## 42. Observability Law

Observability may report:

```text
logs
traces
metrics
health
events
```

but:

```text
OBSERVABILITY
!=
AUTHORITY
```

Telemetry describes behavior.

It does not decide policy.

---

## 43. Security Law

Security boundaries override convenience.

No optimization may bypass:

```text
AUTHENTICATION
AUTHORIZATION
SECRET BOUNDARIES
TRUST BOUNDARIES
GOVERNANCE GATES
```

merely because the underlying operation is technically possible.

---

## 44. Test Law

```text
TEST PASS
=
EVIDENCE WITHIN TEST SCOPE
```

not:

```text
TEST PASS
=
UNIVERSAL PROOF
```

Tests inherit:

```text
environment
fixtures
assumptions
coverage
version
measurement method
```

---

## 45. Anti-Sybil Evidence Law

Many apparent sources descended from one origin do not create independent confirmation.

Conceptually:

```text
N DESCENDANTS OF SOURCE X
≈
ONE PROVENANCE FAMILY
```

unless independence is separately established.

---

## 46. Identity Firewall

The following identities are distinct:

```text
FILE NAME
ARTIFACT ID
REGISTRY ID
SEMANTIC IDENTITY
VERSION IDENTITY
PROVENANCE IDENTITY
RUNTIME INSTANCE ID
```

Renaming one must not silently rewrite another.

---

## 47. Version Law

Canonical filenames do not need version suffixes.

Evolution is tracked through:

```text
metadata
revision
hash
provenance
supersession
change records
```

Hard boundary:

```text
FILENAME VERSION
!=
CANON VERSION
```

---

## 48. Supersession Law

```text
SUPERSEDED
!=
DELETED
```

Historical states must remain recoverable when needed for provenance or replay.

---

## 49. Promotion Law

Existence is not promotion.

```text
FILE EXISTS
!=
IMPLEMENTED

IMPLEMENTED
!=
VALIDATED

VALIDATED
!=
CANONICAL

CANONICAL
!=
EMPIRICALLY VERIFIED
```

Each transition requires its own evidence and governance.

---

## 50. Placeholder Law

```text
PLACEHOLDER
=
RESERVED STRUCTURAL LOCATION
```

A placeholder does not establish:

```text
implementation
validation
authority
production readiness
final canon
```

---

## 51. Failure Registry

```text
CL-F001 FABRICATED_PREMISE
CL-F002 UNKNOWN_TREATED_AS_PASS
CL-F003 SOURCE_CLAIM_TREATED_AS_VERIFIED
CL-F004 MODEL_FACT_COLLAPSE
CL-F005 CONFIDENCE_INFLATION
CL-F006 PROVENANCE_LOSS
CL-F007 CORRELATED_EVIDENCE_AS_INDEPENDENT
CL-F008 DEPENDENCY_LEAK
CL-F009 SCOPE_LEAK
CL-F010 REGIME_LEAK
CL-F011 STALE_EVIDENCE_REUSE
CL-F012 CAUSAL_OVERREACH
CL-F013 COMPETING_HYPOTHESIS_COLLAPSE
CL-F014 AUTHORITY_CAPABILITY_COLLAPSE
CL-F015 PROPOSAL_COMMIT_COLLAPSE
CL-F016 TOOL_PERMISSION_COLLAPSE
CL-F017 UNGOVERNED_EVOLUTION
CL-F018 ANTI_REGRESSION_FAILURE
CL-F019 GLOBAL_INVALIDATION_WITHOUT_CAUSE
CL-F020 FAILED_PATH_REPEATED_WITHOUT_NEW_EVIDENCE
CL-F021 PROVENANCE_LINEAGE_ERASED
CL-F022 VERSION_IDENTITY_COLLAPSE
CL-F023 PLACEHOLDER_PROMOTED_BY_EXISTENCE
CL-F024 BENCHMARK_UNIVERSALIZATION
CL-F025 DISTRIBUTED_TEST_TREATED_AS_FORMAL_PROOF
CL-F026 ASSUMED_INDEPENDENCE
CL-F027 SILENT_SCOPE_GENERALIZATION
CL-F028 SILENT_REGIME_TRANSFER
CL-F029 IRREVERSIBLE_ACTION_WITH_INSUFFICIENT_VALIDATION
CL-F030 OPTIMIZATION_WEAKENS_INTEGRITY
```

---

## 52. Minimum Proof Gate

For a consequential conclusion `C`:

```text
EVIDENCE SUFFICIENT
∧
PROVENANCE SUFFICIENT
∧
DEPENDENCY CLOSURE SUFFICIENT
∧
SCOPE VALID
∧
REGIME VALID
∧
FRESHNESS VALID
∧
CAUSAL TYPE VALID IF REQUIRED
∧
CONFLICT STATE ACCEPTABLE
∧
AUTHORITY VALID IF ACTIONABLE
```

Only then may the relevant conclusion or action advance.

---

## 53. Core Law Evaluation Function

Conceptually:

```text
VALID(C)
=
E(C)
∧ P(C)
∧ D(C)
∧ S(C)
∧ R(C)
∧ F(C)
∧ X(C)
```

where:

```text
E = evidence sufficiency
P = provenance sufficiency
D = dependency validity
S = scope compatibility
R = regime compatibility
F = freshness
X = absence/resolution of material contradiction
```

This is a structural logical model.

It is not asserted as a universal mathematical law.

---

## 54. Action Gate

For action `A`:

```text
ACTIONABLE(A)
=
VALID(C)
∧ AUTHORIZED(A)
∧ GOVERNED(A)
∧ RISK_ACCEPTABLE(A)
```

Therefore:

```text
TRUE CLAIM
!=
AUTHORIZED ACTION
```

---

## 55. v3.0 → v4.4 Evolution Spine

The AMOS Core lineage preserved by this law set is:

```text
DETERMINISTIC LOGIC
↓
RECURSIVE RSCF / H-M-L
↓
GOVERNED EVOLUTION
↓
CAUSAL LINEAGE
↓
EPISTEMIC REGIMES
↓
COMPETING HYPOTHESES
↓
PROVENANCE TOPOLOGY / SYBIL HARDENING
↓
PERSISTENT PROVENANCE
↓
MVCC / CAS CONCEPTS
↓
ATOMIC MULTI-RSCF REASONING
↓
CAUSAL EPOCH FINALITY
↓
HARDENED SHARD-LOCAL FINALIZATION
↓
PROOF-BASED COORDINATION AVOIDANCE
```

These are architectural reasoning patterns in AMOS.

They must not be misrepresented as proof that every implementation literally contains all corresponding distributed-system machinery.

---

## 56. Core Law Compact Set

The constitutional core compresses to:

```text
INTEGRITY > COMPLETENESS > FLUENCY > SPEED

UNKNOWN/GAP != PASS

SOURCE_CLAIM != VERIFIED
MODEL != FACT
MODEL != AUTHORITY

REPETITION != INDEPENDENCE
AUTHORITY != EVIDENCE

STRUCTURAL_SIMILARITY != CAUSATION
CORRELATION != CAUSAL_EFFECT

VALID_HERE != VALID_EVERYWHERE
STALE != CURRENT

RELATED_TO != DEPENDS_ON

CAPABILITY != AUTHORITY
TOOL != PERMISSION
PROPOSAL != COMMIT

MEMORY != CANON
KNOWLEDGE != AUTHORITY

PLACEHOLDER != IMPLEMENTED
IMPLEMENTED != VALIDATED
VALIDATED != UNIVERSAL_PROOF

SUPERSEDED != DELETED

FAST_PATH != WEAKER_PROOF

OPTIMIZATION MUST NOT WEAKEN INTEGRITY
```

---

## 57. RSCF Node

```yaml
node_id: AMOS_CORE_LAWS

functional_type:
  - CANONICAL_LAW_SET
  - INTEGRITY_CONTRACT
  - GOVERNANCE_CONSTRAINT

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS Core Laws define the constitutional invariants governing
  epistemic integrity, provenance, dependency reasoning, causality,
  scope and regime validity, uncertainty, authority, execution,
  governed evolution, recovery, and knowledge handling across AMOS OS.

dependencies:
  - "[[01_CANON/README.md]]"
  - "[[00_ROOT/ARCHITECTURE.md]]"
  - "[[00_ROOT/AUTHORITATIVE_STATE.md]]"
  - "[[02_KERNEL/00_INDEX/KERNEL_MAP.md]]"
  - "[[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md]]"

critical_invariants:
  - INTEGRITY > COMPLETENESS
  - UNKNOWN/GAP != PASS
  - SOURCE_CLAIM != VERIFIED
  - MODEL != FACT
  - REPETITION != INDEPENDENCE
  - STRUCTURAL_SIMILARITY != CAUSATION
  - CAPABILITY != AUTHORITY
  - PROPOSAL != COMMIT
  - TOOL != PERMISSION
  - MEMORY != CANON
  - PLACEHOLDER != IMPLEMENTED
  - OPTIMIZATION_MUST_NOT_WEAKEN_INTEGRITY

does_not_establish:
  - universal empirical truth
  - implementation completeness
  - production readiness
  - literal implementation of every v4.4 distributed-systems analogy
  - validation of every downstream AMOS artifact
```

---

## 58. Promotion Gate

This file may be promoted from:

```text
ACTIVE_CANON_CANDIDATE
```

to:

```text
ACTIVE_CANON
```

only after the authoritative AMOS source set is bound and reviewed for:

```text
LAW IDENTITY
LAW COMPLETENESS
VERSION LINEAGE
CONTRADICTIONS
SUPERSESSION
DEPENDENCIES
TERMINOLOGY
PROVENANCE
```

Until that review is complete, this document is a structured AMOS v4.4 model of the Core Laws rather than a claim that every clause has already been formally promoted into final canon.

---

## 59. Changelog

### v2.0.0 — 2026-08-25

Expanded the original placeholder into a versioned AMOS Core v4.4 constitutional law specification.

Added:

* integrity hierarchy;
* epistemic typing;
* conclusion classes;
* confidence ceiling;
* competing-hypothesis preservation;
* provenance topology;
* independence/Sybil firewall;
* dependency closure;
* selective invalidation;
* proof-capsule reuse;
* causal firewall;
* scope/regime/freshness firewalls;
* uncertainty vector;
* sensitivity rules;
* capability/authority separation;
* proposal/commit separation;
* execution fast path;
* mandatory escalation conditions;
* anti-regression;
* recovery semantics;
* knowledge harvest;
* fractal H/M/L retrieval;
* RSCF/GMEF boundaries;
* adversarial validation;
* atomic multi-RSCF reasoning;
* MVCC/CAS conceptual boundary;
* causal epoch finality;
* shard-local finalization;
* proof-based coordination avoidance;
* gap classification;
* AMOS plane laws;
* identity/version/supersession laws;
* failure registry;
* proof and action gates;
* v3.0→v4.4 evolution spine.

### v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS location.

---

## 60. Final Constitutional Law

AMOS Core reduces to one governing principle:

> **Preserve integrity of identity, evidence, provenance, dependency, scope, regime, causality, uncertainty, and authority before optimizing completeness, fluency, speed, coordination, or execution.**

Operationally:

```text
KNOW
WHAT IS CLAIMED
↓
KNOW
WHAT SUPPORTS IT
↓
KNOW
WHERE IT CAME FROM
↓
KNOW
WHAT IT DEPENDS ON
↓
KNOW
WHERE AND WHEN IT APPLIES
↓
KNOW
WHAT COMPETES WITH IT
↓
KNOW
WHAT WOULD INVALIDATE IT
↓
KNOW
WHO HAS AUTHORITY
↓
THEN
DECIDE / ACT
```

If any load-bearing element is unavailable:

```text
DO NOT FABRICATE CLOSURE
```

Return the weakest accurate state:

```text
CONDITIONAL
COMPETING
or
UNKNOWN/GAP
```

---

**Related:** [[00_ROOT/README.md|AMOS OS]] · [[00_ROOT/MOC.md|MOC]] · [[00_ROOT/ARCHITECTURE.md|Architecture]] · [[00_ROOT/SYSTEM_MAP.md|System Map]] · [[00_ROOT/AUTHORITATIVE_STATE.md|Authoritative State]] · [[00_ROOT/PLACEMENT_RULES.md|Placement Rules]] · [[01_CANON/README.md|AMOS Canon]] · [[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]] · [[02_KERNEL/00_INDEX/KERNEL_MAP.md|Kernel Map]] · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|Control Plane Map]] · [[04_RUNTIME/00_INDEX/RUNTIME_MAP.md|Runtime Map]] · [[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP.md|Cognitive Organism Map]] · [[10_MEMORY/00_INDEX/MEMORY_MAP.md|Memory Map]] · [[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture.md|AMOS Full Brain OS Architecture]] · [[12_STATE/00_INDEX/STATE_MAP.md|State Map]] · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_MAP.md|Observability Map]] · [[18_SECURITY/00_INDEX/SECURITY_MAP.md|Security Map]] · [[19_TESTS/00_INDEX/TEST_MAP.md|Tests]] · [[24_ARCHIVE/00_LEGACY/README.md|Archive]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
