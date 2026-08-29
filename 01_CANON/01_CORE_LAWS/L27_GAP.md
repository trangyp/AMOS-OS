---
title: L27 GAP
aliases:
- L27 Gap
- L27 Gap Law
- Gap Law
type: gap
source: 01_CANON/01_CORE_LAWS
tags:
- canon
- core_laws
- gap
- unknown
- epistemic_integrity
- anti_fabrication
- provenance
- validation
- proof_capsule
- gap_registry
- gap_closure
- fail_closed
- recovery
- note
- canon/universe
- 00-home
- amos-rscf-nodes
- law-hierarchy
- l25-shard-local
- l28-critical-gap
- l10-failure-recovery
- l17-rscf
- fail-closed-governance
- 01-core-laws-moc
- trang-framework-recursive-ontology-dynamics
- l19-proof-capsule
- l26-proof-coordination
- l27-gap
- architecture
- 00-root-moc
- amos-moc
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: core_laws
---

# L27 Gap Law

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

> [!abstract]
> L27 establishes the AMOS discipline for representing, preserving,
> registering, and closing unresolved gaps.
>
> Its governing source spine contains four laws:
>
> **GAP-1 Expose Don't Fill**
> **GAP-2 Gap Is Status Not Shame**
> **GAP-3 Bounded Gap Registry**
> **GAP-4 Gap Closure Requires Evidence**
>
> L27 prevents missing implementation, authority, validation, or
> provenance from being silently replaced by plausible architecture.
>
> `UNKNOWN/GAP` is therefore a legitimate epistemic outcome rather than
> a defect to be hidden.
>
> Material beyond the supplied clauses is an expanded
> `AMOS_MODEL / DERIVED` reconstruction unless explicitly marked
> source-established.

---

# 0. Status

```yaml
status:
  law_id: L27
  node_id: l27_gap
  name: Gap Law

  document_type: gap
  source: 01_CANON/01_CORE_LAWS

  status: PROPOSED_SPECIFICATION
  epistemic_class: AMOS_MODEL
  canonical_status: CONDITIONAL
  updated: 2026-08-26

  rscf:
    state: SOURCE_CLAIM
    claim_class: CONDITIONAL
    provenance: AMOS_corpus
    scope: core_laws
---

The supplied source explicitly establishes:

```text
PROPOSED_SPECIFICATION
AMOS_MODEL
CONDITIONAL
```

Therefore this reconstruction must not silently promote L27 to:

```text
VERIFIED
FINAL_CANON
FORMALLY_PROVEN
EMPIRICALLY_VALIDATED
RUNTIME_IMPLEMENTED
```

without additional authoritative evidence.

---

# 1. Purpose

L27 governs what AMOS does when required knowledge is absent,
unverified, inaccessible, ambiguous, unsupported, or otherwise
insufficient to justify a stronger conclusion.

Its primary integrity objective is:

```text
MISSING EVIDENCE
MUST REMAIN
MISSING EVIDENCE
```

rather than becoming:

```text
PLAUSIBLE COMPLETION
```

through fluent inference.

The law therefore protects the boundary between:

```text
KNOWN
DERIVED
MODELLED
CONDITIONAL
UNKNOWN
```

---

# 2. Source Laws

The supplied source establishes four laws.

## GAP-1 — Expose Don't Fill

> Missing implementation/authority/validation/provenance stays visible;
> plausible architecture never fills it.

---

## GAP-2 — Gap Is Status Not Shame

> UNKNOWN/GAP is an honest epistemic class, first-class in outputs.

---

## GAP-3 — Bounded Gap Registry

> Every artifact lists its own load-bearing gaps (proof capsules).

---

## GAP-4 — Gap Closure Requires Evidence

> Closing a gap demands executed validation, not restatement.

---

# 3. Core Gap Model

A gap exists when a conclusion requires some load-bearing element \(x\)
but the available evidence does not establish \(x\) strongly enough for
the intended conclusion.

Normalized model:

$$
Required(x) \land \neg Established(x)
\Rightarrow Gap(x)
$$

This equation is `DERIVED / MODEL`.

It is not supplied directly by the source.

---

# 4. Gap Integrity Condition

A normalized L27 integrity condition is:

$$
Gap(x)
\Rightarrow
Visible(x)
\land
Bounded(x)
\land
Tracked(x)
\land
\neg FabricatedClosure(x)
$$

and:

$$
CloseGap(x)
\Rightarrow
NewEvidence(x)
$$

where the evidence satisfies the relevant validation requirement.

Again, these are normalized model expressions rather than source
equations.

---

# 5. GAP-1 — Expose Don't Fill

GAP-1 is the primary anti-fabrication law.

If an artifact requires:

```text
implementation evidence
authority
validation
provenance
```

and that element is missing, the missing element remains explicit.

Correct:

```text
Implementation: NOT_ESTABLISHED
```

Incorrect:

```text
Implementation probably works like X,
therefore X is treated as implementation.
```

---

# 6. Missing Implementation

If a specification describes:

```text
desired behavior
```

but no implementation artifact has been established:

```text
SPECIFICATION
!=
IMPLEMENTATION
```

The gap remains:

```yaml
gap:
  type: implementation
  status: NOT_ESTABLISHED
```

A plausible implementation design may be proposed separately as:

```text
MODEL
```

but it cannot close the implementation gap.

---

# 7. Missing Authority

If an artifact claims:

```text
this is canonical
```

but the governing authority or authoritative canon is unavailable:

```text
CANONICAL CLAIM
!=
ESTABLISHED AUTHORITY
```

The correct state may remain:

```text
AUTHORITY_GAP
```

rather than assuming authority from formatting, location, repetition,
or plausibility.

---

# 8. Missing Validation

If a document states:

```text
validated
```

but the relevant validation evidence has not been inspected or
executed:

```text
VALIDATION CLAIM
!=
VALIDATION OBSERVATION
```

The gap remains visible.

---

# 9. Missing Provenance

If a claim exists but its origin cannot be recovered:

```text
CLAIM PRESENT
```

does not imply:

```text
PROVENANCE ESTABLISHED
```

The appropriate representation may be:

```yaml
provenance:
  status: UNKNOWN
```

---

# 10. Plausibility Firewall

Critical L27 firewall:

```text
PLAUSIBLE
!=
ESTABLISHED
```

A plausible architecture may be useful as:

```text
MODEL
HYPOTHESIS
DESIGN OPTION
```

but never as silent evidence that a missing component exists.

---

# 11. Architecture Firewall

Suppose the available canon implies that a system would benefit from:

```text
signed receipts
```

but no authoritative receipt specification exists.

Correct:

```text
Signed receipts would be a plausible architecture.
Exact receipt semantics: GAP.
```

Incorrect:

```text
The system uses signed receipts with schema X.
```

unless evidence establishes that fact.

---

# 12. Inference Firewall

Inference may reduce uncertainty.

It may not erase an evidence gap merely by being coherent.

Therefore:

```text
DERIVABLE DESIGN
!=
OBSERVED IMPLEMENTATION
```

and:

```text
LOGICAL POSSIBILITY
!=
SOURCE SUPPORT
```

---

# 13. Fluency Firewall

L27 specifically protects against a common reasoning failure:

```text
missing detail
+
language-model fluency
=
apparently complete architecture
```

The correct transformation is:

```text
missing detail
+
reasoning
=
explicit gap
+
optional clearly-labeled model
```

---

# 14. Silence Is Not Evidence

If the source does not mention a mechanism:

```text
SOURCE SILENCE
```

does not establish:

```text
mechanism absent
```

and does not establish:

```text
mechanism present
```

The correct state may be:

```text
UNKNOWN/GAP
```

---

# 15. Absence of Contradiction

Likewise:

```text
NO CONTRADICTION FOUND
!=
PROOF
```

A claim does not become established merely because nothing currently
contradicts it.

---

# 16. Default Gap Preservation

When a load-bearing fact cannot be established:

```text
PRESERVE GAP
```

is preferred over:

```text
GUESS
```

where integrity is at stake.

This is the central operational meaning of GAP-1.

---

# 17. GAP-2 — Gap Is Status Not Shame

GAP-2 makes unresolved uncertainty first-class.

The source explicitly establishes:

```text
UNKNOWN/GAP
```

as an honest epistemic class.

Therefore:

```text
UNKNOWN/GAP
```

is a valid result.

It is not merely an error message.

---

# 18. First-Class Unknown

A system should be able to conclude:

```yaml
conclusion:
  class: UNKNOWN/GAP
```

without being forced to fabricate a stronger answer.

---

# 19. Unknown Is Not False

Critical firewall:

```text
UNKNOWN
!=
FALSE
```

Failure to establish proposition \(P\) does not establish:

$$
\neg P
$$

unless the evidence contract makes absence itself decisive.

---

# 20. Unknown Is Not True

Likewise:

```text
UNKNOWN
!=
TRUE
```

A plausible proposition remains unresolved until evidence supports it.

---

# 21. Gap Is Not Contradiction

```text
GAP
!=
CONTRADICTION
```

A gap means necessary information is missing or insufficient.

A contradiction means available claims conflict.

Both may coexist, but they are different states.

---

# 22. Gap Is Not Competing

```text
UNKNOWN/GAP
!=
COMPETING
```

`COMPETING` requires multiple materially viable incompatible
hypotheses.

A gap may exist with:

```text
zero supported hypotheses
one incomplete hypothesis
multiple hypotheses
```

---

# 23. Gap Is Not Failure

A reasoning system that returns:

```text
UNKNOWN/GAP
```

when evidence is insufficient has not necessarily failed.

It may have successfully preserved epistemic integrity.

---

# 24. Gap Is Not Incompleteness to Hide

The pressure to produce a complete artifact does not authorize filling
unsupported sections.

Therefore:

```text
COMPLETENESS
<
INTEGRITY
```

when the two conflict.

---

# 25. Gap as Information

A well-specified gap communicates:

```text
what is missing
why it matters
what depends on it
what would close it
```

Therefore a gap can increase decision quality even though it represents
missing knowledge.

---

# 26. Gap as Boundary

A gap defines a boundary between:

```text
SUPPORTED
```

and:

```text
NOT YET SUPPORTED
```

That boundary should remain machine- and human-visible where material.

---

# 27. Gap as Stop Condition

For some tasks, an unresolved gap should stop escalation of a claim.

Example:

```text
critical premise = UNKNOWN
```

therefore:

```text
final conclusion = UNKNOWN/GAP
```

rather than inventing the premise.

---

# 28. Gap as Conditional Branch

Some gaps do not prevent all action.

A conclusion may instead become:

```text
CONDITIONAL
```

Example:

```text
IF X is validated,
THEN conclusion C follows.
```

while:

```text
X = GAP
```

remains explicit.

---

# 29. Conditional Is Not Closure

Critical distinction:

```text
IF X THEN C
```

does not close the gap:

```text
Is X true?
```

Conditional reasoning preserves the missing premise.

---

# 30. GAP-3 — Bounded Gap Registry

GAP-3 states:

> Every artifact lists its own load-bearing gaps (proof capsules).

This establishes local gap ownership.

Each artifact should expose the unresolved gaps that materially limit
its claims.

---

# 31. Artifact-Local Gap Registry

Conceptually:

```yaml
artifact:
  id: A

  gaps:
    - G1
    - G2
```

rather than relying exclusively on one distant global gap list.

---

# 32. Why Bounded Registries Matter

A local registry allows a consumer to determine:

```text
what this artifact does not establish
```

without reconstructing the entire knowledge system.

This supports bounded reasoning.

---

# 33. Load-Bearing Gaps

GAP-3 specifically refers to:

```text
load-bearing gaps
```

Therefore not every cosmetic omission must be registered with equal
weight.

A load-bearing gap is one whose resolution can materially change:

```text
claim validity
confidence
scope
decision
action
governance
```

---

# 34. Non-Load-Bearing Omission

Example:

```text
missing decorative diagram
```

may not be load-bearing.

It should not necessarily receive the same priority as:

```text
missing validation evidence
```

---

# 35. Proof Capsule Integration

The source explicitly associates bounded gap registries with:

```text
proof capsules
```

Therefore an important proof capsule should carry its unresolved
load-bearing gaps.

Conceptually:

```yaml
proof_capsule:
  claim: C
  premises: []
  evidence: []
  gaps:
    - G001
```

---

# 36. Gap Scope

Each gap should be scoped to the artifact or conclusion it affects.

Correct:

```text
G001 affects proof P and descendants.
```

Incorrect:

```text
G001 exists,
therefore entire system is unknown.
```

unless the dependency topology actually makes it global.

---

# 37. Gap Locality

A local gap should remain local when possible.

```text
LOCAL GAP
!=
GLOBAL INVALIDATION
```

Selective propagation preserves unaffected knowledge.

---

# 38. Gap Dependency

If:

```text
G1 blocks premise P1
P1 supports conclusion C
```

then G1 is a gap affecting C.

If another conclusion D does not depend on P1:

```text
G1
```

should not automatically invalidate D.

---

# 39. Gap Propagation

Conceptually:

```text
GAP G
  |
  v
PREMISE P
  |
  v
CLAIM C
  |
  v
DECISION D
```

The gap propagates only through dependency edges where it is
load-bearing.

---

# 40. Gap Closure Propagation

When G is validly closed:

```text
G -> CLOSED
```

only affected descendants need re-evaluation.

Unrelated proof capsules remain untouched.

---

# 41. Bounded Does Not Mean Hidden

A bounded gap is:

```text
localized
```

not:

```text
buried
```

It must remain visible to consumers whose conclusions depend on it.

---

# 42. Gap Registry Minimum

A useful minimum registry entry may include:

```text
gap ID
description
status
affected claim
```

Additional fields are model-level extensions.

---

# 43. Expanded Gap Registry

For consequential artifacts, a richer model can include:

```text
gap ID
class
description
missing evidence
scope
dependencies
affected conclusions
decision impact
closure condition
owner/authority
freshness
status
```

This is `DERIVED / MODEL`.

---

# 44. Gap Identity

A stable gap identity allows:

```text
tracking
closure
reopening
supersession
dependency linking
```

The exact ID format is not source-defined.

---

# 45. Gap Versioning

A gap may evolve.

Example:

```text
G001 v1:
validation completely missing

G001 v2:
validator exists, execution missing
```

The source does not define exact versioning mechanics.

---

# 46. Gap Status Model

An illustrative status vocabulary:

```text
OPEN
PARTIALLY_RESOLVED
BLOCKED
CLOSED
REOPENED
SUPERSEDED
```

Only `UNKNOWN/GAP` is explicitly supplied as epistemic terminology.

The exact lifecycle vocabulary is not canonical here.

---

# 47. GAP-4 — Gap Closure Requires Evidence

GAP-4 states:

> Closing a gap demands executed validation, not restatement.

This is the closure firewall.

A gap cannot be closed by saying the missing thing again.

---

# 48. Restatement Is Not Evidence

Suppose gap G is:

```text
No evidence that validator V passes.
```

This does not close G:

```text
Validator V passes.
```

unless accompanied by the required evidence.

Therefore:

```text
RESTATEMENT
!=
VALIDATION
```

---

# 49. More Detailed Restatement

Likewise:

```text
"The validator passes because the architecture says it should."
```

does not close the validation gap.

Explanatory richness does not substitute for evidence.

---

# 50. Repetition Is Not Closure

```text
CLAIM
CLAIM
CLAIM
```

does not become:

```text
VERIFIED CLAIM
```

through repetition.

---

# 51. Authority Repetition Is Not Closure

Even if multiple descendants repeat:

```text
Source S says X.
```

they remain descendants of the same source unless independent evidence
exists.

This naturally connects L27 to proof independence accounting.

---

# 52. Documentation Is Not Execution

If documentation states:

```text
21/21 tests pass
```

but test execution has not been independently inspected:

```text
test-pass claim = SOURCE_CLAIM
```

The gap:

```text
direct validation observation
```

remains open.

---

# 53. Code Presence Is Not Execution

```text
validator.py exists
```

does not establish:

```text
validator.py executed successfully
```

Therefore artifact presence alone does not close an execution gap.

---

# 54. Test Presence Is Not Pass

```text
test suite exists
```

does not establish:

```text
test suite passes
```

---

# 55. Pass Is Not Coverage

```text
all observed tests passed
```

does not establish:

```text
all relevant behaviors tested
```

unless coverage evidence supports that conclusion.

Closing one gap can leave another gap open.

---

# 56. Validation Scope

Executed validation closes only the gap it actually addresses.

If a test validates:

```text
property A
```

it does not automatically close gaps for:

```text
property B
property C
universal correctness
```

---

# 57. Gap Closure Is Typed

Different gaps require different evidence.

Examples:

```text
implementation gap
-> implementation artifact / execution evidence

authority gap
-> authoritative source / governance evidence

validation gap
-> executed validator / relevant observation

provenance gap
-> recoverable provenance evidence
```

This mapping is a model elaboration of GAP-4.

---

# 58. Closure Evidence Must Match Gap Type

Critical rule:

```text
WRONG EVIDENCE TYPE
DOES NOT CLOSE GAP
```

Example:

```text
performance benchmark
```

does not necessarily close:

```text
formal correctness gap
```

---

# 59. Closure Evidence Must Match Scope

Evidence from:

```text
scope S1
```

does not automatically close a gap in:

```text
scope S2
```

unless a valid bridge exists.

---

# 60. Closure Evidence Must Match Regime

A simulation result does not automatically close an empirical gap.

```text
SIMULATION
!=
EMPIRICAL OBSERVATION
```

without a justified regime bridge.

---

# 61. Closure Evidence Must Be Fresh Enough

Evidence can be valid historically but stale for the current state.

Therefore gap closure may depend on freshness.

```text
VALID THEN
!=
VALID NOW
```

when load-bearing conditions changed.

---

# 62. Closure Evidence Must Be Provenance-Aware

A gap requiring independent confirmation is not closed by:

```text
three descendants of one source
```

unless independence requirements are satisfied.

---

# 63. Closure Evidence Must Be Load-Bearing

Evidence that addresses a peripheral detail does not close a gap in a
load-bearing premise.

The evidence must resolve the actual missing dependency.

---

# 64. Partial Gap Closure

Some evidence may narrow a gap without fully closing it.

Example:

```text
Before:
implementation unknown

After:
implementation artifact found,
execution unverified
```

The gap changes shape.

It does not disappear.

---

# 65. Gap Refinement

A broad gap:

```text
implementation unknown
```

may refine into:

```text
implementation exists
version unknown
test state unknown
deployment state unknown
```

Refinement is progress even without complete closure.

---

# 66. Gap Splitting

One gap can reveal multiple sub-gaps.

```text
G1
|
+--> G1a authority
+--> G1b validation
+--> G1c provenance
```

The parent should not be marked fully closed until its load-bearing
children are resolved.

---

# 67. Gap Merging

Two apparent gaps may share one root cause.

Example:

```text
G1 missing validator output
G2 missing test receipt
```

may both arise from:

```text
execution never performed
```

Where appropriate, shared roots should be preserved to avoid redundant
work.

---

# 68. Gap Reopening

A previously closed gap may reopen when:

```text
validation invalidated
source withdrawn
dependency changes
regime shifts
new contradiction appears
proof is superseded
```

Therefore:

```text
CLOSED
!=
CLOSED FOREVER
```

---

# 69. Closure Receipt

A gap closure should conceptually preserve:

```text
what gap was closed
what evidence closed it
who/what validated it
scope
regime
version
time/epoch
dependencies
```

where relevant.

Exact receipt schema is not supplied by L27.

---

# 70. Closure Without Deletion

Closing a gap should not require erasing the fact that it once existed.

Conceptually:

```text
G001 OPEN @ e1
G001 CLOSED @ e2
```

is preferable to silently rewriting history.

This is a derived integration with causal epoch law.

---

# 71. Gap History

Gap history can preserve:

```text
when discovered
when refined
when partially resolved
when closed
when reopened
```

This improves provenance and auditability.

Exact historical storage semantics are not supplied.

---

# 72. Gap and L10 Failure Recovery

 naturally interacts with L27.

When recovery encounters missing information:

```text
do not fabricate state
```

Instead:

```text
preserve valid state
identify gap
reroute if possible
fail closed if critical
```

Exact coupling is not supplied by the terse source.

---

# 73. Gap and L17 RSCF

 can provide a natural structure for bounded gaps.

Conceptually:

```text
H:
artifact / claim

M:
load-bearing gap categories

L:
specific missing evidence
```

L27 does not redefine RSCF.

---

# 74. Gap and Proof Capsules

Proof capsules are explicitly referenced by GAP-3.

A proof capsule should expose material gaps alongside:

```text
claim
premises
evidence
scope
dependencies
falsifiers
confidence ceiling
```

This prevents a polished proof summary from hiding unresolved support.

---

# 75. Gap and L19 Proof Capsules

A conceptual integration:

```yaml
proof_capsule:
  claim: C

  premises:
    - P1
    - P2

  gaps:
    - id: G001
      affects: P2
      status: OPEN

  conclusion:
    class: CONDITIONAL
```

---

# 76. Gap and L21 Epistemic Regime

A gap may be regime-specific.

Example:

```text
simulation validation = available
empirical validation = missing
```

Therefore:

```text
empirical_validation_gap
```

remains open even if simulation evidence is strong.

---

# 77. Gap and L22 Replayability

Replayability can close certain reproducibility gaps.

But:

```text
REPLAY MATCH
!=
TRUTH
```

Therefore deterministic replay does not automatically close:

```text
source truth gap
causal validity gap
scope gap
independence gap
```

---

# 78. Gap and L23 MVCC/CAS

A gap registry can itself be mutable state.

Concurrent closure attempts should not silently overwrite each other.

Conceptually:

```text
read gap state
validate closure evidence
CAS expected OPEN state
commit CLOSED
```

This is a derived implementation integration.

---

# 79. Gap Closure CAS Boundary

Even if a CAS succeeds:

```text
CAS SUCCESS
!=
EVIDENCE SUFFICIENT
```

CAS protects mutation integrity.

GAP-4 governs epistemic closure.

---

# 80. Gap and L24 Causal Epoch

A gap can evolve across epochs:

```text
G OPEN @ e_k
```

then:

```text
G CLOSED @ e_{k+1}
```

without rewriting the historical state.

Likewise:

```text
G REOPENED @ e_{k+2}
```

may follow new evidence.

---

# 81. Gap and L25 Shard Local

 raises an important locality question:

```text
Is this gap local or global?
```

A shard-local gap need not automatically block unrelated shards.

But a gap affecting a global invariant may require escalation.

---

# 82. Local Gap

Conceptually:

```text
Shard A:
G001 OPEN

Shard B:
independent of G001
```

Then B may remain valid if dependency independence is established.

---

# 83. Cross-Shard Gap

If:

```text
G001
```

affects a shared invariant:

```text
GLOBAL CLAIM C
```

then the gap cannot be treated as merely local.

---

# 84. Gap and L26 Proof Coordination

L26 and L27 naturally reinforce each other.

L26 asks:

```text
Is the proof coordinated and verified?
```

L27 asks:

```text
What remains missing?
```

A proof with unresolved load-bearing interfaces should expose those
interfaces as gaps rather than assume compatibility.

---

# 85. Proof Coordination Gap

Example:

```text
P1 valid
P2 valid
interface P1 -> P2 unknown
```

Correct:

```text
composition = CONDITIONAL / GAP
```

Incorrect:

```text
composition = VERIFIED
```

---

# 86. Independence Gap

If two proofs appear independent but ancestry cannot be established:

```text
INDEPENDENCE = UNKNOWN/GAP
```

not:

```text
INDEPENDENCE = TRUE
```

This is especially important for provenance topology and Sybil
hardening.

---

# 87. Validation Gap

If a validator exists but has not been run:

```text
validator_presence = established
validator_execution = GAP
```

The system should preserve both facts separately.

---

# 88. Authority Gap

If a note claims canonical status but authoritative promotion evidence
is missing:

```text
authority = GAP
```

unless the source itself is the governing authority for that status.

---

# 89. Provenance Gap

If a claim cannot be traced to its origin:

```text
provenance = GAP
```

The claim may still be useful as a hypothesis or source claim, but its
confidence ceiling should reflect the missing provenance.

---

# 90. Scope Gap

If evidence exists but applicability boundaries are unknown:

```text
scope = GAP
```

A conclusion should not silently generalize.

---

# 91. Regime Gap

If it is unclear whether evidence is:

```text
simulation
empirical
canonical
speculative
```

then:

```text
regime = GAP
```

may be material.

---

# 92. Temporal Gap

If the evidence date or freshness cannot be established:

```text
temporal_validity = GAP
```

for claims where freshness matters.

---

# 93. Causal Gap

Evidence may establish association while mechanism remains unknown.

Then:

```text
causal_effect = GAP
```

should remain visible.

Do not fill it with structural similarity or temporal sequence.

---

# 94. Implementation Gap

A specification may be complete while implementation remains absent.

```text
SPEC COMPLETE
IMPLEMENTATION GAP OPEN
```

Both states can coexist.

---

# 95. Execution Gap

Code may exist without execution evidence.

```text
IMPLEMENTATION PRESENT
EXECUTION GAP OPEN
```

---

# 96. Deployment Gap

Code may execute in tests while production deployment remains
unverified.

```text
TESTED IMPLEMENTATION
!=
DEPLOYED SYSTEM
```

Deployment can remain a separate gap.

---

# 97. Formal-Proof Gap

Tests may pass while formal proof is absent.

That is only a gap if formal proof is required for the claim.

Do not manufacture unnecessary requirements.

---

# 98. Empirical Gap

A model may be internally coherent while empirical calibration remains
missing.

Correct:

```text
MODEL SUPPORTED
EMPIRICAL VALIDATION GAP
```

---

# 99. Governance Gap

A technically valid action may still lack:

```text
authority
approval
policy basis
```

If authority is required:

```text
governance gap
```

remains load-bearing.

---

# 100. Security Gap

A functional implementation may have an unresolved security property.

The security gap should not be hidden merely because functionality
tests pass.

---

# 101. Safety Gap

Likewise:

```text
functional success
!=
safety validation
```

where safety validation is required.

---

# 102. Measurement Gap

A metric may be named without a defined measurement method.

Example:

```text
repair quality = high
```

without operational definition.

Then:

```text
measurement gap
```

remains open.

---

# 103. Threshold Gap

A model may define:

```text
trigger when X falls below threshold
```

while the threshold itself is unspecified.

Then the architecture is incomplete at the decision boundary.

---

# 104. Calibration Gap

A formula may exist without empirical calibration.

Example:

$$
Score = A/B
$$

does not establish:

```text
what values mean
what thresholds matter
how variables are normalized
```

Those remain calibration gaps.

---

# 105. Schema Gap

A protocol may require:

```text
receipt
```

while the exact receipt schema is absent.

The gap should be recorded rather than filled with an invented schema.

An illustrative schema may be provided only as:

```text
MODEL
```

---

# 106. Algorithm Gap

A law may require:

```text
select earliest safe rewind boundary
```

while providing no algorithm.

The requirement is established.

The algorithm remains a gap.

---

# 107. Identity Gap

If an architecture requires stable identity but does not define:

```text
identity key
hash
path
version
```

the identity mechanism remains unresolved.

---

# 108. Independence Verification Gap

Multiple evidence paths may exist while their independence cannot be
verified.

Then:

```text
multiple paths = established
independence = GAP
```

---

# 109. Root Input Gap

A replay protocol may exist while some root input cannot be recovered.

Then deterministic replay may be blocked.

Do not fabricate the root input.

---

# 110. Environment Gap

A validator result may depend on an unknown runtime environment.

If outcome-changing:

```text
environment = GAP
```

must remain visible.

---

# 111. Version Gap

A proof or implementation may exist without a pinned version.

If version differences can change the result:

```text
version = GAP
```

is load-bearing.

---

# 112. Dependency Gap

If a claim depends on an unknown dependency:

```text
dependency closure = incomplete
```

The conclusion should inherit the uncertainty where material.

---

# 113. Hidden Dependency Gap

A particularly dangerous case is:

```text
dependency exists
but is not represented
```

This can create false confidence because the gap itself is invisible.

L27 therefore favors explicit dependency representation.

---

# 114. Gap Discovery

Discovering a new gap should not be treated as regression in knowledge
quality.

It may represent improved epistemic resolution.

```text
previously hidden uncertainty
->
explicit gap
```

is often an integrity improvement.

---

# 115. Gap Discovery vs Claim Failure

A newly discovered gap does not always prove the old claim false.

It may mean:

```text
the old claim was insufficiently supported
```

The appropriate downgrade depends on the missing premise.

---

# 116. Gap-Induced Downgrade

Possible transitions include:

```text
VERIFIED -> CONDITIONAL
DERIVED -> CONDITIONAL
MODEL -> UNKNOWN/GAP
```

depending on what failed.

Exact transition semantics are not supplied by L27.

---

# 117. Selective Downgrade

Only conclusions depending on the new gap should be downgraded.

```text
G -> P1 -> C1
```

does not imply:

```text
C2 invalid
```

if C2 does not depend on G.

---

# 118. Gap Severity

Not all gaps have equal consequence.

A useful derived classification is:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

This prioritization is consistent with AMOS gap discipline but is not
explicitly enumerated in the terse L27 source.

---

# 119. Critical Gap

A `CRITICAL` gap prevents a safe or valid conclusion/action.

Example:

```text
authorization required
authorization unknown
irreversible mutation proposed
```

The gap blocks execution.

---

# 120. Decision-Relevant Gap

A `DECISION-RELEVANT` gap can materially change the selected option but
does not necessarily block all action.

---

# 121. Explanatory Gap

An `EXPLANATORY` gap limits understanding but does not change the
current decision.

It should remain visible without consuming disproportionate validation
effort.

---

# 122. Cosmetic Gap

A `COSMETIC` gap affects presentation rather than integrity.

It should not displace attention from load-bearing gaps.

---

# 123. Gap Priority Rule

Derived operational priority:

```text
CRITICAL
>
DECISION-RELEVANT
>
EXPLANATORY
>
COSMETIC
```

Resolve in that order unless another governance requirement overrides
it.

---

# 124. Minimum Missing Information

When a critical gap cannot be closed, identify:

```text
the minimum missing information
that would change the state
```

rather than requesting an unbounded amount of context.

---

# 125. Smallest Discriminating Evidence

For a gap with competing closure hypotheses:

```text
choose the cheapest evidence
with the highest decision-changing value
```

rather than collecting redundant support.

This is a derived information-value discipline.

---

# 126. Gap Closure Cost

A gap should not automatically trigger maximal research.

The validation cost should scale with:

```text
decision impact
stakes
irreversibility
uncertainty
expected value of information
```

---

# 127. Harmless Gap

If a gap cannot alter:

```text
claim
decision
action
scope
governance
```

it may remain unresolved.

Integrity does not require exhaustive completion of irrelevant details.

---

# 128. Material Gap

If a gap can flip the result:

```text
resolve first
```

where feasible.

This is the sensitivity principle applied to gap management.

---

# 129. Gap Closure Decision Rule

Conceptually:

$$
Resolve(G)
\quad\text{when}\quad
EV_{decision}(Resolve(G)) > Cost(Resolve(G))
$$

This is a model-level decision heuristic, not a source equation.

---

# 130. Gap Registry Schema

Illustrative:

```yaml
gap:
  gap_id: G001

  artifact_id: A001

  class:
    - CRITICAL

  description:
    "Exact validation protocol is not established."

  missing:
    evidence_type: EXECUTED_VALIDATION

  affects:
    claims:
      - C001

  scope:
    system: null
    regime: null
    epoch: null

  dependencies: []

  closure:
    condition:
      "Execute authoritative validator against pinned inputs."
    evidence: []

  status: OPEN
```

Not canonical unless separately established.

---

# 131. Minimal Gap Schema

The minimum directly implied by GAP-3 can be represented as:

```yaml
gap:
  id: G001
  description: "..."
  load_bearing_for:
    - C001
```

Exact fields remain unspecified.

---

# 132. Gap Closure Receipt Schema

Illustrative:

```yaml
gap_closure_receipt:
  gap_id: G001

  prior_status: OPEN
  proposed_status: CLOSED

  evidence:
    type: EXECUTED_VALIDATION
    artifact: null

  validator:
    id: null
    version: null

  scope:
    regime: null
    environment: null
    epoch: null

  result:
    status: PASS

  dependencies:
    unchanged: UNKNOWN

  provenance:
    source: null
```

---

# 133. Gap Reopening Receipt

Illustrative:

```yaml
gap_reopening_receipt:
  gap_id: G001

  prior_status: CLOSED
  new_status: OPEN

  reason:
    type: DEPENDENCY_INVALIDATED

  affected_claims:
    - C001

  evidence:
    - null
```

---

# 134. Gap Registry RSCF Model

Conceptually:

```yaml
RSCF:
  H:
    artifact: A

  M:
    gaps:
      - G001
      - G002

  L:
    G001:
      missing_evidence: "..."
      affected_claim: C001
      closure_condition: "..."
```

This is an integration model.

---

# 135. Gap Proof Capsule

```yaml
proof_capsule:

  claim:
    text: "C"
    class: CONDITIONAL

  load_bearing_premises:
    - P1
    - P2

  evidence:
    - E1

  gaps:
    - id: G001
      affects:
        - P2
      status: OPEN
      closure_condition:
        "Acquire and execute validator V."

  confidence_ceiling:
    CONDITIONAL
```

---

# 136. Gap Dependency Graph

```text
                 G001
                  |
                  v
             PREMISE P2
                  |
                  v
                CLAIM C
               /       \
              v         v
          DECISION D1  DECISION D2
```

If G001 is load-bearing, its status propagates through the relevant
edges.

---

# 137. Multiple Gap Graph

```text
G001 ----> P1 ----\
                   \
                    > CLAIM C
                   /
G002 ----> P2 ----/
```

Closing G001 does not necessarily close C if G002 remains load-bearing.

---

# 138. Shared Gap Graph

```text
              G001
             /    \
            v      v
           P1      P2
            |      |
            v      v
           C1      C2
```

One gap can affect multiple conclusions.

The registry should avoid pretending these are unrelated uncertainties.

---

# 139. Gap Root Cause

Multiple visible gaps may share one root.

```text
missing authoritative schema
       |
       +--> parser gap
       +--> validator gap
       +--> replay gap
```

Root-cause resolution may close several dependent gaps at once.

---

# 140. Gap Closure Graph

```text
NEW EVIDENCE
     |
     v
VALIDATION
     |
     v
GAP G001
OPEN -> CLOSED
     |
     v
REVALIDATE DEPENDENTS
     |
     v
UPDATE ONLY AFFECTED CLAIMS
```

---

# 141. Gap Failure State Machine

```text
REQUIRED PREMISE
      |
      v
EVIDENCE AVAILABLE?
   /          \
 YES           NO
 |              |
 v              v
VALIDATE       GAP
 |              |
 v              v
PASS?         EXPOSE
/   \           |
NO  YES          v
|    |        REGISTER
v    v           |
FAIL SUPPORTED   v
              CLASSIFY
                 |
                 v
             CAN IT BLOCK?
              /      \
            YES       NO
             |         |
             v         v
         FAIL CLOSED  CONTINUE
         / CONDITIONAL WITH GAP
```

Model-level.

---

# 142. Gap Closure State Machine

```text
OPEN GAP
   |
   v
NEW EVIDENCE?
 /       \
NO        YES
|          |
v          v
REMAIN    VALIDATE
OPEN         |
          +--+--+
          |     |
         FAIL  PASS
          |     |
          v     v
        OPEN   DOES PASS
               ADDRESS
               ACTUAL GAP?
                /   \
              NO     YES
              |       |
              v       v
            OPEN    CLOSE
```

---

# 143. Partial Closure State Machine

```text
OPEN
 |
 v
EVIDENCE ADDED
 |
 v
ALL LOAD-BEARING
MISSING ELEMENTS RESOLVED?
 /             \
NO              YES
|                |
v                v
PARTIALLY       CLOSED
RESOLVED
```

Exact status names are illustrative.

---

# 144. Reopening State Machine

```text
CLOSED
  |
  v
DEPENDENCY / EVIDENCE
INVALIDATED?
 /       \
NO        YES
|          |
v          v
CLOSED   REOPEN
```

---

# 145. Fail-Closed Governance

 is a natural L27 integration.

When a gap affects:

```text
irreversible action
legal authority
safety
security
institutional mutation
large downstream dependency
```

the default should favor:

```text
DO NOT EXECUTE
```

until the critical gap is resolved or an explicitly authorized safe
fallback exists.

---

# 146. Fail Closed Does Not Mean Stop Everything

A critical gap in one action does not necessarily require:

```text
global halt
```

Correct behavior is scoped.

Possible response:

```text
block unsafe mutation
preserve safe reads
continue unrelated work
request minimum missing evidence
```

---

# 147. Reversible Action Under Gap

When action is reversible and low-risk, a gap may permit:

```text
staged experiment
sandbox validation
limited probe
read-only inspection
```

if those actions help close the gap without creating unacceptable
exposure.

---

# 148. Irreversible Action Under Gap

As irreversibility rises:

```text
required validation rises
```

An unresolved authority or safety gap should not be bypassed merely
because a proposed action appears plausible.

---

# 149. Gap and Action Sufficiency

A decision does not require every explanatory gap to be closed.

It requires enough evidence for:

```text
Claim Sufficiency
Decision Sufficiency
Action Sufficiency
```

relative to the stakes.

---

# 150. Claim Sufficiency

A claim is sufficient when its unresolved gaps do not prevent the
claimed epistemic class.

Example:

```text
MODEL claim
```

may tolerate missing empirical validation if that absence is explicit.

---

# 151. Decision Sufficiency

A decision is sufficient when unresolved gaps cannot reasonably change
the selected action within the decision's required confidence envelope.

---

# 152. Action Sufficiency

Action sufficiency requires stronger closure where the action is:

```text
irreversible
high-cost
safety-critical
legally consequential
institutionally consequential
```

---

# 153. Gap and Confidence Ceiling

If a load-bearing premise is unresolved:

```text
confidence ceiling
```

must reflect that gap.

A polished explanation cannot raise confidence beyond the missing
support.

---

# 154. Gap and Derived Claims

A derived claim can remain valid conditionally:

```text
IF P
THEN C
```

even when:

```text
P = UNKNOWN
```

But the unconditional claim:

```text
C
```

cannot inherit stronger status.

---

# 155. Gap and Model Claims

A model may intentionally fill a conceptual design space.

That is allowed when labeled:

```text
MODEL
```

The gap remains open regarding whether reality or canon implements the
model.

---

# 156. Gap and Source Claims

A source claim can establish:

```text
the source says X
```

while leaving open:

```text
whether X is true
```

These are different claims.

---

# 157. Gap and Observation

Direct observation may close an observational gap while leaving:

```text
causal explanation
generalization
future validity
```

open.

One evidence event rarely closes every uncertainty dimension.

---

# 158. Gap and Causality

If:

```text
A precedes B
```

but mechanism/confounding remain unresolved:

```text
causal effect = GAP
```

Sequence alone does not close causality.

---

# 159. Gap and Structural Analogy

If two systems share structure:

```text
structural similarity = established
```

may coexist with:

```text
causal equivalence = GAP
```

L27 prevents the latter from being silently filled.

---

# 160. Gap and Benchmark Claims

A benchmark result may close:

```text
performance on benchmark B
```

while leaving:

```text
performance outside B
hardware independence
deployment reliability
universal validity
```

open.

---

# 161. Gap and Test Claims

Passing tests may close:

```text
these tests passed in environment E
```

but not automatically:

```text
all behavior correct
```

---

# 162. Gap and Formal Verification

Formal proof can close a formal property gap within its assumptions.

It may leave:

```text
model fidelity
implementation correspondence
environmental assumptions
```

open.

---

# 163. Gap and Authority

Authoritative canon can close:

```text
what AMOS canon defines
```

but not automatically:

```text
whether the definition is empirically true outside the canon
```

Canonical authority and empirical validation remain distinct.

---

# 164. Gap and Provenance Independence

Multiple evidence artifacts do not close an independence gap unless
their relevant ancestry is known.

```text
N artifacts
```

may still represent:

```text
1 source lineage
```

---

# 165. Gap and Sybil Hardening

A provenance Sybil attack can create:

```text
one unsupported root claim
-> many descendants
-> apparent consensus
```

L27 requires the root support gap to remain visible.

Descendant count cannot close it.

---

# 166. Gap and Persistent Provenance

Persistent provenance allows a gap to remain attached to its affected
claims across:

```text
caching
composition
replay
supersession
migration
```

where relevant.

Exact storage mechanics are not supplied.

---

# 167. Gap and Persistent Memory

A gap should not disappear merely because a reasoning session ends.

If its dependent conclusion is persisted, the material gap should
remain attached or recoverable.

This is a derived integrity requirement.

---

# 168. Gap and Cached Proof Capsules

A cached proof capsule remains reusable only while:

```text
dependencies valid
scope valid
regime valid
freshness valid
gap state unchanged materially
```

If a critical gap is discovered later, cached dependent conclusions
must be reconsidered.

---

# 169. Gap Discovery After Caching

Example:

```text
t0:
P cached as DERIVED

t1:
hidden load-bearing provenance gap discovered
```

Then:

```text
P
```

may require downgrade or invalidation.

Do not preserve the old status merely because it was cached.

---

# 170. Gap and Replay

Replay can reproduce the state in which a gap existed.

Replay must not rewrite:

```text
UNKNOWN
```

into:

```text
KNOWN
```

unless new evidence was introduced.

---

# 171. Gap and Recovery

When a recovery path fails because information is missing:

```text
do not repeat same path
without changed evidence
```

Instead:

```text
preserve valid work
mark gap
reroute if possible
request missing information
```

---

# 172. Gap Closure Through New Evidence

Valid closure pattern:

```text
GAP
 |
 v
NEW EVIDENCE
 |
 v
VALIDATION
 |
 v
CLOSURE
```

Invalid pattern:

```text
GAP
 |
 v
RESTATEMENT
 |
 v
"RESOLVED"
```

---

# 173. Gap Closure Through Derivation

A gap can sometimes be closed by derivation if the missing proposition
is logically established from already validated premises.

However, the derivation itself must be valid and must actually address
the missing claim.

This does not authorize plausible guessing.

---

# 174. Gap Closure Through Authority

An authority gap may be closed by authoritative canon.

But:

```text
authority evidence
```

closes authority.

It does not necessarily close:

```text
implementation
empirical validity
execution
```

---

# 175. Gap Closure Through Observation

An observational gap may be closed by direct observation.

The closure remains scoped to:

```text
what was observed
where
when
under what conditions
```

---

# 176. Gap Closure Through Experiment

An empirical gap may be reduced or closed through an appropriate
experiment.

But one experiment may not justify universal generalization.

---

# 177. Gap Closure Through Formal Proof

A formal gap can be closed by a valid proof where formal proof is the
required evidence type.

The proof's assumptions and scope remain load-bearing.

---

# 178. Gap Closure Through Replay

Replay may close:

```text
reproducibility gap
```

but not automatically:

```text
truth gap
causal gap
authority gap
independence gap
```

---

# 179. Gap Closure Through Consensus

Consensus alone does not close an evidence gap.

```text
many agents agree
```

is not sufficient if they share the same unsupported root.

---

# 180. Gap Closure Through Popularity

```text
widely repeated
```

does not mean:

```text
validated
```

Popularity is not a closure mechanism under L27.

---

# 181. Gap Closure Through Confidence Language

Phrases such as:

```text
almost certainly
clearly
obviously
undoubtedly
```

do not close gaps.

Epistemic confidence language must follow evidence, not substitute for
it.

---

# 182. Gap Closure Through More Tokens

A longer explanation does not close an evidence gap.

```text
MORE PROSE
!=
MORE EVIDENCE
```

This is especially important for generative reasoning systems.

---

# 183. Gap Closure Through Architecture Detail

An architecture can be described at extraordinary detail while still
being hypothetical.

Therefore:

```text
DETAILED MODEL
!=
IMPLEMENTED SYSTEM
```

---

# 184. Gap Closure Through Equations

A mathematical expression can formalize a model.

It does not prove the model empirically valid merely because it is
written as an equation.

```text
FORMALIZATION
!=
VALIDATION
```

---

# 185. Gap Closure Through Code

Code can demonstrate an executable implementation artifact.

It does not prove:

```text
correctness
deployment
authority
scope
safety
```

without corresponding evidence.

---

# 186. Gap Closure Through Tests

Tests close only what they test.

```text
PASS
```

must remain scoped to:

```text
test suite
inputs
environment
version
```

---

# 187. Gap Closure Through Documentation

Documentation can close:

```text
what the documentation states
```

It cannot by itself close:

```text
whether the implementation behaves that way
```

unless documentation itself is the authoritative object for the claim
being evaluated.

---

# 188. Gap Closure Through Canon

Canon can close a definition gap within AMOS.

Example:

```text
What does AMOS define X to mean?
```

Authoritative canon can answer that.

But canon alone does not necessarily close:

```text
Does external reality behave according to X?
```

---

# 189. Gap Closure Through Analogy

Analogy can generate hypotheses.

It cannot close:

```text
implementation
causal
empirical
authority
```

gaps without additional evidence.

---

# 190. Gap Closure Through Structural Similarity

Same rule:

```text
ISOMORPHIC STRUCTURE
!=
SAME MECHANISM
```

A structural mapping remains a model unless validated.

---

# 191. Gap Closure Through Temporal Sequence

```text
A happened before B
```

does not close:

```text
A caused B
```

The causal gap remains.

---

# 192. Gap Closure Through Correlation

```text
A correlates with B
```

does not close:

```text
causal mechanism
```

without appropriate evidence.

---

# 193. Gap Closure Through One Successful Run

One successful run may close:

```text
can succeed at least once under observed conditions
```

but not:

```text
always succeeds
```

---

# 194. Gap Closure Through Benchmark Success

Benchmark success may close a scoped benchmark gap.

It does not close universal performance or reliability gaps.

---

# 195. Gap Closure Through Simulation

Simulation can close:

```text
behavior under simulation assumptions
```

but empirical transfer remains a separate gap.

---

# 196. Gap Closure Through Model Agreement

Two models agreeing does not necessarily close an evidence gap,
especially if both share:

```text
training data
assumptions
architecture
source material
```

Independence must be demonstrated.

---

# 197. Gap Closure Through Agent Multiplicity

```text
five agents agree
```

does not automatically equal:

```text
five independent confirmations
```

The independence gap remains until ancestry/failure modes are assessed.

---

# 198. Gap Closure Through No Detected Error

```text
no error detected
```

does not mean:

```text
no error exists
```

unless the detection mechanism is complete for the relevant error
class.

---

# 199. Gap Closure Through Historical Success

Past success does not automatically close:

```text
current applicability
```

after a regime or environment shift.

---

# 200. Gap Closure Through Default Assumption

Defaults may be operationally useful.

But if a default is load-bearing:

```text
DEFAULT
```

must not be relabeled:

```text
ESTABLISHED FACT
```

---

# 201. Gap Closure Preconditions

A model closure contract can require:

```text
GAP IDENTIFIED
+
CORRECT EVIDENCE TYPE
+
EVIDENCE ACQUIRED
+
VALIDATION EXECUTED
+
VALIDATION PASSED
+
SCOPE MATCHED
+
REGIME MATCHED
+
PROVENANCE SUFFICIENT
=
CANDIDATE CLOSURE
```

Not every gap requires every dimension.

The dimensions depend on the gap type.

---

# 202. Closure Adversarial Check

Before consequential closure, ask:

```text
Did the new evidence actually address the gap?

Is it independent of the source that created the claim?

Is it fresh?

Does it apply to the same scope?

Does it apply to the same regime?

Is a hidden dependency still unresolved?

Did we close the gap or merely rename it?
```

---

# 203. False Closure

A false closure occurs when:

```text
status changes from GAP to RESOLVED
```

without sufficient new evidence.

This is one of the central failure modes prohibited by GAP-4.

---

# 204. Premature Closure

Premature closure occurs when evidence is relevant but incomplete.

Example:

```text
validator found
```

therefore:

```text
validation gap closed
```

even though the validator has not been executed.

Correct state:

```text
validator existence gap = closed
validator execution gap = open
```

---

# 205. Scope-Leaking Closure

Example:

```text
tested on Linux
```

therefore:

```text
works on all platforms
```

The Linux test may close one scoped gap while leaving broader
applicability unresolved.

---

# 206. Regime-Leaking Closure

Example:

```text
simulation stable
```

therefore:

```text
production stable
```

without transfer evidence.

The production gap remains open.

---

# 207. Provenance-Leaking Closure

Example:

```text
three reports confirm X
```

but all three derive from one report.

The independence gap remains.

---

# 208. Authority-Leaking Closure

Example:

```text
well-written note says X is canon
```

therefore:

```text
authority established
```

without authoritative lineage.

Formatting does not establish governance authority.

---

# 209. Implementation-Leaking Closure

Example:

```text
specification defines CAS
```

therefore:

```text
runtime literally implements hardware CAS
```

This silently crosses from architecture to implementation.

L27 forbids such filling.

---

# 210. Formalism-Leaking Closure

Example:

```text
equation exists
```

therefore:

```text
formal theorem proven
```

The proof gap remains.

---

# 211. Gap Quality

A high-quality gap statement is:

```text
specific
bounded
decision-relevant
falsifiable/closable
provenance-aware
```

A poor gap statement is:

```text
"more research needed"
```

without saying what information is missing.

---

# 212. Good Gap Example

```yaml
gap:
  id: G001
  class: CRITICAL
  description:
    "No executed validation establishes that validator V accepts proof P_v3."
  affects:
    - claim_C
  closure_condition:
    "Execute authoritative V against pinned P_v3 and retain result."
```

---

# 213. Weak Gap Example

```yaml
gap:
  description: "Need more evidence."
```

This is visible but insufficiently bounded for efficient closure.

---

# 214. Gap Closure Question

Every material gap should ideally answer:

```text
What exact observation or evidence
would allow this gap to close?
```

If no possible closure condition can be described, the gap may be too
vague or the claim may be unfalsifiable.

---

# 215. Gap Falsifiability

A gap registry should distinguish:

```text
currently unresolved
```

from:

```text
in principle unresolvable
```

when that distinction matters.

The source does not define formal terminology for this.

---

# 216. Permanent Unknown

Some questions may remain unknown because evidence is unavailable in
principle or permanently lost.

L27 still requires honesty:

```text
UNKNOWN
```

rather than fictional reconstruction.

---

# 217. Recoverable Gap

A gap is recoverable when a known evidence path exists.

Example:

```text
missing test result
```

with available source code and executable test environment.

---

# 218. Blocked Gap

A gap may be temporarily blocked because required evidence is
inaccessible.

Correct state:

```text
OPEN / BLOCKED
```

rather than:

```text
CLOSED BY ASSUMPTION
```

The exact status vocabulary is model-level.

---

# 219. Gap Owner

Operational systems may assign:

```text
owner
validator
authority
```

to a gap.

L27 does not require an exact ownership mechanism.

---

# 220. Gap Deadline

A gap can have a revalidation deadline where freshness matters.

This is an operational extension rather than source canon.

---

# 221. Gap SLA Boundary

L27 does not define:

```text
maximum closure time
service-level objective
latency target
```

Therefore no gap SLA should be invented as canonical.

---

# 222. Gap Metrics Boundary

Potential metrics such as:

```text
open critical gaps
mean closure time
reopen rate
false closure rate
```

may be useful operationally.

They are not defined by the supplied law.

---

# 223. Gap Count Boundary

A system with:

```text
100 visible gaps
```

is not necessarily worse than one reporting:

```text
0 gaps
```

The second system may simply be hiding uncertainty.

Therefore:

```text
LOW GAP COUNT
!=
HIGH INTEGRITY
```

---

# 224. Gap Density Boundary

Likewise, gap density is not an intrinsic quality metric without
context.

A mature audit may discover more gaps because it resolves hidden
uncertainty more accurately.

---

# 225. Gap Closure Rate Boundary

Fast closure can be harmful if it encourages:

```text
premature closure
weak evidence
scope leakage
```

Therefore:

```text
CLOSURE SPEED
<
CLOSURE INTEGRITY
```

when they conflict.

---

# 226. Gap Compression

Multiple low-level gaps may be summarized for human readability if the
summary preserves:

```text
load-bearing distinctions
dependency relationships
closure conditions
```

Compression must not erase critical uncertainty.

---

# 227. Gap Expansion

A high-level gap may be expanded into sub-gaps only when the added
detail improves:

```text
diagnosis
decision
validation
closure
```

Do not generate ornamental gap taxonomies that do not affect action.

---

# 228. Adaptive Gap Resolution

Start with the smallest sufficient gap representation.

Escalate detail when:

```text
stakes high
gap blocks decision
dependencies ambiguous
closure evidence disputed
scope unclear
provenance correlated
```

---

# 229. Gap Stop Rule

Stop expanding a gap when:

```text
minimum missing information identified
closure test defined
decision consequence understood
```

unless additional detail can materially change the result.

---

# 230. Gap Recovery Algorithm

Illustrative:

```python
def handle_gap(gap, context):
    expose(gap)
    register(gap)

    if not gap.is_load_bearing(context):
        return CONTINUE_WITH_VISIBLE_GAP

    if gap.is_critical(context):
        evidence = cheapest_valid_closure_test(gap)

        if evidence is None:
            return UNKNOWN_GAP

        result = validate(evidence)

        if result.closes(gap):
            close(gap, receipt=result)
            return REEVALUATE_DEPENDENTS

        return FAIL_CLOSED_OR_CONDITIONAL

    return CONTINUE_CONDITIONALLY
```

This is a model implementation, not supplied canon.

---

# 231. Gap Closure Algorithm

```python
def close_gap(gap, evidence):
    if evidence is None:
        return REJECT("NO_NEW_EVIDENCE")

    if not evidence.matches_gap_type(gap):
        return REJECT("WRONG_EVIDENCE_TYPE")

    if not evidence.matches_scope(gap):
        return REJECT("SCOPE_MISMATCH")

    if not evidence.matches_regime(gap):
        return REJECT("REGIME_MISMATCH")

    if not execute_validation(evidence):
        return REJECT("VALIDATION_FAILED")

    return CLOSE_WITH_RECEIPT(gap, evidence)
```

Illustrative.

---

# 232. Gap Revalidation Algorithm

```python
def revalidate_closed_gap(gap):
    if dependencies_changed(gap):
        reopen(gap)
        return REVALIDATE

    if freshness_expired(gap):
        reopen(gap)
        return REVALIDATE

    return KEEP_CLOSED
```

Model-level.

---

# 233. Gap Propagation Algorithm

```python
def propagate_gap(gap):
    affected = dependency_descendants(gap)

    for node in affected:
        if gap.is_load_bearing_for(node):
            downgrade_or_invalidate(node)
```

Selective invalidation is required conceptually; exact mechanics are
not supplied by L27.

---

# 234. Gap Resolution Fast Path

A gap may close locally when:

```text
gap scope local
closure evidence local
authority local
no cross-shard invariant
no shared dependency conflict
validation executable locally
```

This is a derived integration with shard-local reasoning.

---

# 235. Gap Escalation Path

Escalate when the gap involves:

```text
global invariant
cross-shard dependency
authority ambiguity
regime crossing
causal coupling
irreversible action
safety
security
legal/governance impact
correlated provenance
```

---

# 236. Gap Coordination Avoidance

Do not coordinate globally merely because a gap exists.

Coordinate only as broadly as required to establish or close the
load-bearing uncertainty.

This is a derived efficiency principle.

---

# 237. Proof of Gap Locality

Before treating a gap as local, establish that:

```text
its dependency closure
does not materially affect
global conclusions or invariants
```

Locality must be demonstrated, not assumed.

---

# 238. Gap and Atomic Multi-RSCF

Suppose a conclusion requires:

```text
RSCF-A
RSCF-B
RSCF-C
```

and:

```text
RSCF-B has critical gap G
```

Then the atomic composed conclusion must preserve G.

It cannot commit as though all three RSCFs were complete.

---

# 239. Atomic Gap Visibility

Atomic reasoning should carry:

```text
all load-bearing open gaps
```

into the composed proof capsule.

A gap cannot disappear merely because multiple reasoning nodes are
combined.

---

# 240. Gap Merge Discipline

When multiple branches merge:

```text
Branch A: G001 open
Branch B: no mention of G001
```

the merged state must not interpret silence from B as closure.

Correct:

```text
G001 remains open
```

unless B provides closure evidence.

---

# 241. Contradictory Gap States

Suppose:

```text
Branch A: G001 OPEN
Branch B: G001 CLOSED
```

The system should inspect:

```text
closure evidence
version
epoch
scope
regime
```

before selecting a state.

Do not use last-writer-wins by default for epistemic closure.

---

# 242. Gap State CAS

A model state transition:

```text
CAS(
  expected = OPEN,
  proposed = CLOSED_WITH_RECEIPT
)
```

can prevent concurrent stale closure.

But again:

```text
CAS success
!=
epistemic sufficiency
```

---

# 243. Gap Epoch Transition

Conceptually:

```text
e_k:
G001 = OPEN

e_{k+1}:
new validation receipt R
G001 = CLOSED
```

Historical state remains attributable.

---

# 244. Gap Reopen Epoch

```text
e_{k+2}:
dependency D invalidated
G001 = REOPENED
```

This preserves causal lineage.

---

# 245. Gap Replay

A deterministic replay should reproduce:

```text
G001 OPEN
```

for the historical state before closure if that was the recorded state.

Replay should not inject later evidence into earlier epochs.

---

# 246. Gap and No Time Travel

Later closure evidence does not mean the gap was never open.

Correct:

```text
OPEN @ e1
CLOSED @ e2
```

Incorrect:

```text
rewrite e1 as CLOSED
```

This integration is derived from L24.

---

# 247. Gap and Recovery Rollback

If a recovery rolls state back to a safe point, gap history should not
be confused with historical deletion.

Recovery can restore viable state while preserving the provenance that
the gap and later closure events occurred.

---

# 248. Gap and DMER

A recovery architecture can use gap discipline to avoid misdiagnosed
repair.

If the fault origin is unknown:

```text
FAULT ORIGIN = GAP
```

should remain explicit.

Do not choose a rewind boundary merely because one origin appears
plausible.

---

# 249. Gap and Distinction

In D/M/E/R terms, gap integrity depends on preserving the distinction
between:

```text
known
plausible
unknown
```

Collapsing these distinctions can create misdiagnosed repair.

This is an integration model, not a direct L27 source clause.

---

# 250. Gap and Entropy

Hidden gaps can increase epistemic entropy because unsupported
assumptions propagate as though validated.

Visible gaps constrain that propagation.

This is a conceptual AMOS_MODEL integration rather than an empirical
law established by L27.

---

# 251. Gap and Repair

Gap closure is a form of epistemic repair only when the closure
mechanism actually resolves the missing evidence.

Restatement masquerading as closure is not repair.

---

# 252. Gap and Viability

A system capable of saying:

```text
UNKNOWN
```

may preserve more adaptive optionality than one forced to commit to an
unsupported answer.

This is a model-level connection to broader AMOS viability concepts.

---

# 253. Gap and Decision Reversibility

If a gap remains open:

```text
prefer reversible action
```

where possible.

This limits damage if the unresolved premise later proves false.

---

# 254. Gap and Information Value

The best next evidence is not necessarily:

```text
the most evidence
```

but:

```text
the evidence most likely
to change the decision
```

This avoids redundant accumulation.

---

# 255. Gap and Competing Hypotheses

A gap may contain competing closure hypotheses.

Example:

```text
Why did validation fail?

H1: implementation defect
H2: validator defect
H3: environment mismatch
```

Do not collapse them prematurely.

---

# 256. Discriminating Test

Choose a test that differentiates:

```text
H1
H2
H3
```

rather than repeatedly collecting evidence compatible with all three.

---

# 257. Gap and Strongest Alternative

Before closing a consequential gap, challenge the proposed closure with
the strongest alternative explanation.

Example:

```text
Observed PASS
```

Alternative:

```text
wrong test version executed
```

If the alternative remains viable, the intended gap may remain open.

---

# 258. Gap Closure Sensitivity

Ask:

```text
What is the smallest change
to the closure evidence
that would reopen the gap?
```

If a tiny plausible change flips the state, closure is fragile and may
need `CONDITIONAL` status.

---

# 259. Robust Gap Closure

A robust closure survives plausible perturbations of noncritical
assumptions and directly addresses the load-bearing missing element.

---

# 260. Gap Confidence Ceiling

Conceptually:

$$
Confidence(C)
\leq
Confidence(P_g)
$$

when unresolved premise \(P_g\) is load-bearing for conclusion \(C\).

If \(P_g\) is `UNKNOWN/GAP`, unconditional confidence in \(C\) must be
bounded accordingly.

---

# 261. Gap Severity Matrix

| Gap type                     | Typical impact                          | Possible result           |
| ---------------------------- | --------------------------------------- | ------------------------- |
| Missing cosmetic metadata    | Low                                     | Continue                  |
| Missing explanation          | Low/Medium                              | Continue with gap         |
| Missing scope                | Potentially high                        | Conditional               |
| Missing provenance           | Medium/High                             | Downgrade                 |
| Missing validator execution  | High for verification claim             | Keep validation gap open  |
| Missing authority            | High for governance claim               | Fail closed / conditional |
| Missing safety evidence      | Critical for unsafe irreversible action | Fail closed               |
| Missing load-bearing premise | Critical                                | UNKNOWN/GAP               |

Context determines actual severity.

---

# 262. Gap Closure Matrix

| Gap                          | Evidence offered                   | Closure?                                |
| ---------------------------- | ---------------------------------- | --------------------------------------- |
| Implementation missing       | Architecture diagram               | No                                      |
| Implementation missing       | Executable implementation artifact | Partial / context-dependent             |
| Execution missing            | README says tests pass             | No                                      |
| Execution missing            | Direct test execution receipt      | Candidate yes                           |
| Authority missing            | Repeated citation                  | No                                      |
| Authority missing            | Governing authoritative canon      | Candidate yes                           |
| Provenance missing           | Another descendant claim           | No                                      |
| Provenance missing           | Recoverable source lineage         | Candidate yes                           |
| Empirical validation missing | Simulation                         | No, unless empirical bridge established |
| Replayability missing        | Deterministic replay receipt       | Candidate yes for replay gap only       |

---

# 263. Gap Output Contract

When a material gap remains, an output should ideally state:

```text
WHAT IS KNOWN
WHAT IS NOT KNOWN
WHY THE GAP MATTERS
WHAT WOULD CLOSE IT
WHAT CAN SAFELY BE DONE NOW
```

Not every response requires all five fields explicitly, but the
underlying distinction should be preserved.

---

# 264. Compact Gap Output

Example:

```text
CONCLUSION: CONDITIONAL.

Known:
The specification requires validator V.

Gap:
No executed result for V is available.

Impact:
The validation claim cannot be promoted.

Closure:
Run V against the pinned artifact and retain the result.
```

---

# 265. Critical Gap Output

Example:

```text
UNKNOWN/GAP.

The requested conclusion depends on authoritative schema S.
S is not available in the supplied evidence.

Minimum missing information:
the authoritative definition of S.
```

---

# 266. Competing + Gap Output

Example:

```text
COMPETING.

H1 and H2 remain viable.

Gap:
No discriminating observation establishes which mechanism applies.

Next useful evidence:
test T, because its outcomes differ under H1 and H2.
```

---

# 267. Gap Anti-Fabrication Contract

```text
IF SOURCE DOES NOT ESTABLISH X:

DO NOT WRITE
"X IS ..."

WRITE ONE OF:

"X IS NOT ESTABLISHED."

"THE SOURCE DOES NOT DEFINE X."

"X REMAINS A GAP."

"A POSSIBLE MODEL IS X, BUT THIS DOES NOT CLOSE THE GAP."
```

---

# 268. Gap Compression Contract

When concise output is required:

```text
do not remove the gap
to save tokens
```

Instead compress background first.

Integrity-bearing uncertainty survives compression.

---

# 269. Gap Expansion Contract

When exhaustive output is requested:

```text
do not transform
every missing detail
into invented canon
```

Expansion should increase:

```text
structure
boundary clarity
dependency visibility
closure conditions
```

not fabricated certainty.

---

# 270. Gap and Canon Reconstruction

When reconstructing incomplete AMOS canon:

```text
source text
```

must remain distinguishable from:

```text
normalized formalization
derived integration
illustrative schema
model architecture
unknown canon
```

L27 is directly relevant to reconstruction integrity.

---

# 271. Missing Canon

If a canonical section is absent:

```text
MISSING CANON
```

should remain visible.

Do not infer exact canonical wording from neighboring laws.

---

# 272. Canon Pattern Is Not Canon Evidence

Even if:

```text
L25
L26
L28
```

share a clear structure, that pattern does not establish the exact
missing content of:

```text
L27
```

unless L27 source exists.

Pattern can support reconstruction as `MODEL`, not authoritative
recovery.

---

# 273. Reconstructed Canon Boundary

A reconstructed section should be labeled according to evidence:

```text
SOURCE-ESTABLISHED
DERIVED
MODEL
UNKNOWN/GAP
```

rather than being flattened into one undifferentiated canonical voice.

---

# 274. Placeholder Replacement Boundary

The supplied source says:

```text
Proposed specification replacing placeholder.
```

Therefore it establishes that some placeholder was replaced.

It does not establish the placeholder's exact prior content.

That historical content remains a gap unless separately supplied.

---

# 275. Metadata Gap

The source may itself contain metadata tension.

Frontmatter says:

```yaml
rscf:
  claim_class: CONDITIONAL
```

while the RSCF node later says:

```text
claim_class: AMOS_MODEL
```

and status separately states:

```text
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
```

Do not silently erase the inconsistency.

---

# 276. Metadata Normalization Model

A coherent operational normalization is:

```yaml
normalized:
  source_state: SOURCE_CLAIM
  epistemic_class: AMOS_MODEL
  canonical_status: CONDITIONAL
```

But this is a `MODEL` normalization.

It does not rewrite the supplied metadata.

---

# 277. Document-Type Boundary

The frontmatter states:

```yaml
type: gap
```

while the RSCF node states:

```text
node_type: note
```

These may represent different schema dimensions.

Without authoritative schema evidence:

```text
PRESERVE BOTH
```

---

# 278. Source Falsifier

The supplied source establishes:

```text
F1:
authoritative canon treats gaps as failures to hide.
```

This is the direct falsifier.

---

# 279. Falsifier Interpretation

If authoritative canon establishes:

```text
gaps should be concealed
or silently completed
```

then the current L27 coordination model would be superseded or
falsified within the corpus.

This reconstruction does not assume such canon exists.

---

# 280. Expanded Falsifiers

The following are derived refinements:

```yaml
falsifiers:

  - id: F1
    source_status: SOURCE_ESTABLISHED
    condition:
      "Authoritative canon treats gaps as failures to hide."

  - id: F2
    source_status: DERIVED
    condition: >
      Authoritative canon explicitly permits plausible architecture to
      replace missing implementation, authority, validation, or
      provenance.

  - id: F3
    source_status: DERIVED
    condition: >
      Authoritative canon removes UNKNOWN/GAP as a legitimate
      first-class epistemic output.

  - id: F4
    source_status: DERIVED
    condition: >
      Authoritative canon establishes that artifacts need not expose
      their load-bearing gaps.

  - id: F5
    source_status: DERIVED
    condition: >
      Authoritative canon establishes restatement alone as sufficient
      gap closure.

  - id: F6
    source_status: DERIVED
    condition: >
      A later authoritative L27 specification supersedes these
      semantics.
```

---

# 281. Source-Established Claims

```yaml
source_established:

  document:
    title: L27 GAP
    type: gap
    source: 01_CANON/01_CORE_LAWS

  status:
    STATUS: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL
    updated: 2026-08-26

  laws:

    GAP-1:
      name: Expose Don't Fill
      statement: >
        Missing implementation/authority/validation/provenance stays
        visible; plausible architecture never fills it.

    GAP-2:
      name: Gap Is Status Not Shame
      statement: >
        UNKNOWN/GAP is an honest epistemic class, first-class in
        outputs.

    GAP-3:
      name: Bounded Gap Registry
      statement: >
        Every artifact lists its own load-bearing gaps
        (proof capsules).

    GAP-4:
      name: Gap Closure Requires Evidence
      statement: >
        Closing a gap demands executed validation, not restatement.

  falsifiers:
    F1: >
      Authoritative canon treats gaps as failures to hide.

  rscf_node:
    node_id: l27_gap
    node_type: note
    path: 01_CANON/01_CORE_LAWS/L27_GAP.md
    claim_class: AMOS_MODEL

  relations:
    indexed_by:
      - [[00_HOME]]
      - [[AMOS_RSCF_NODES]]
    child_of:
      - [[LAW_HIERARCHY]]

  related:
    - [[00_HOME]]
    - [[AMOS_RSCF_NODES]]
    - [[LAW_HIERARCHY]]
    - [[L25_SHARD_LOCAL]]
    - [[L28_CRITICAL_GAP]]
    - [[L10_FAILURE_RECOVERY]]
    - [[L17_RSCF]]
    - [[FAIL_CLOSED_GOVERNANCE]]

  moc:
    - [[01_CORE_LAWS_MOC]]

  trang_framework:
    - [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

---

# 282. Not Established

The supplied L27 source does **not** establish:

```yaml
not_established:

  - exact gap identifier format
  - exact gap registry schema
  - exact gap lifecycle state machine
  - exact gap severity taxonomy
  - exact closure receipt schema
  - exact validator API
  - exact closure algorithm
  - exact dependency propagation algorithm
  - exact proof-capsule gap schema
  - exact RSCF gap representation
  - exact CAS integration
  - exact epoch integration
  - exact shard-local gap protocol
  - exact cross-shard gap protocol
  - exact fail-closed thresholds
  - exact critical-gap definition
  - exact gap ownership model
  - exact gap freshness model
  - exact closure SLA
  - exact gap metrics
  - exact cryptographic receipt format
  - exact provenance storage implementation
  - exact database/storage architecture
  - literal runtime implementation in ChatGPT
  - universal empirical proof that this gap model is optimal
```

---

# 283. Known Source Gap

The supplied source references:

```text
[[L28_CRITICAL_GAP]]
```

but L27 itself does not define L28's exact critical-gap semantics.

Therefore any detailed critical-gap machinery in this reconstruction is
only a derived anticipation unless L28 is separately supplied.

---

# 284. L28 Boundary

L27 establishes generic gap discipline.

L28 presumably concerns:

```text
critical gaps
```

based on its title/reference.

But L27 does not authorize invention of L28's laws.

Therefore:

```text
L27 GAP
!=
L28 CRITICAL GAP
```

until L28 canon is supplied.

---

# 285. Critical-Gap Integration Boundary

This reconstruction uses:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

as an AMOS gap-prioritization model.

However, exact L28 terminology or semantics must supersede this
derived structure if authoritative L28 differs.

---

# 286. Promotion Gate

Because L27 is explicitly `CONDITIONAL`, a stronger promotion would
reasonably require resolution of material specification gaps.

A model promotion gate:

```text
typed gap schema
artifact-local gap registry contract
proof-capsule integration
closure evidence contract
validation execution semantics
gap lifecycle semantics
selective invalidation rules
scope/regime/freshness semantics
critical-gap integration
cross-law tests
visible unresolved gaps
```

This promotion gate is `MODEL`, not source-established.

---

# 287. Gap Law Self-Application

L27 applies to its own reconstruction.

Therefore the reconstruction must expose that L27 itself has gaps.

This is not a contradiction.

It is the intended integrity behavior.

---

# 288. L27 Self-Gap Register

```yaml
l27_self_gaps:

  - id: L27-G001
    class: CRITICAL
    description: >
      Exact authoritative schema for artifact-local gap registries is
      not supplied.
    status: NOT_ESTABLISHED

  - id: L27-G002
    class: CRITICAL
    description: >
      Exact semantics for "executed validation" across proof,
      empirical, implementation, and governance gaps are not supplied.
    status: NOT_ESTABLISHED

  - id: L27-G003
    class: DECISION_RELEVANT
    description: >
      Exact relationship between L27 generic gaps and L28 critical gaps
      is not supplied.
    status: NOT_ESTABLISHED

  - id: L27-G004
    class: DECISION_RELEVANT
    description: >
      Exact gap closure lifecycle and reopening semantics are not
      supplied.
    status: NOT_ESTABLISHED

  - id: L27-G005
    class: DECISION_RELEVANT
    description: >
      Exact dependency propagation and selective invalidation mechanics
      are not supplied.
    status: NOT_ESTABLISHED

  - id: L27-G006
    class: DECISION_RELEVANT
    description: >
      Exact gap locality and cross-shard escalation rules are not
      supplied.
    status: NOT_ESTABLISHED

  - id: L27-G007
    class: EXPLANATORY
    description: >
      Exact persistence/storage representation for gap history is not
      supplied.
    status: NOT_ESTABLISHED

  - id: L27-G008
    class: EXPLANATORY
    description: >
      Exact machine-readable vocabulary for OPEN, CLOSED, REOPENED,
      PARTIAL, or BLOCKED states is not supplied.
    status: NOT_ESTABLISHED
```

The classification labels in this self-register are model-level.

---

# 289. Gap Law Self-Closure Rule

L27's own gaps cannot be closed by extending this document with more
plausible detail.

For example:

```text
L27-G001:
exact registry schema missing
```

cannot be closed merely by inventing the schema in Section 130.

That schema remains:

```text
ILLUSTRATIVE MODEL
```

until authoritative evidence establishes it.

This is a direct application of GAP-1 and GAP-4.

---

# 290. Gap Law Self-Consistency

L27 is internally consistent with an expanded model that says:

```text
we can describe a plausible mechanism
while preserving that the mechanism
is not source-established
```

Thus:

```text
MODEL DETAIL
+
VISIBLE GAP
```

is allowed.

What is forbidden is:

```text
MODEL DETAIL
->
SILENT CANON PROMOTION
```

---

# 291. Canonical Gap Hierarchy

At the source-supported level:

```text
L27 GAP
|
+--> GAP-1 Expose Don't Fill
|
+--> GAP-2 Gap Is Status Not Shame
|
+--> GAP-3 Bounded Gap Registry
|
+--> GAP-4 Gap Closure Requires Evidence
```

Everything else in this reconstruction is subordinate to this spine.

---

# 292. Operational Gap Hierarchy

Derived model:

```text
GAP
|
+--> IDENTIFY
|
+--> EXPOSE
|
+--> CLASSIFY
|
+--> BOUND
|
+--> REGISTER
|
+--> PROPAGATE TO DEPENDENTS
|
+--> PRIORITIZE
|
+--> SEEK MATCHING EVIDENCE
|
+--> EXECUTE VALIDATION
|
+--> CLOSE / PARTIAL / KEEP OPEN
|
+--> REVALIDATE DEPENDENTS
|
+--> PRESERVE HISTORY
```

---

# 293. Gap Architecture

```text
                        ARTIFACT
                           |
                           v
                    CLAIM / DECISION
                           |
                           v
                 LOAD-BEARING PREMISES
                           |
             +-------------+-------------+
             |                           |
             v                           v
        ESTABLISHED                  NOT ESTABLISHED
             |                           |
             v                           v
          CONTINUE                      GAP
                                         |
                           +-------------+-------------+
                           |             |             |
                           v             v             v
                        EXPOSE        REGISTER      CLASSIFY
                           \             |             /
                            +------------+------------+
                                         |
                                         v
                                CLOSURE CONDITION
                                         |
                                         v
                                    NEW EVIDENCE
                                         |
                                         v
                               EXECUTED VALIDATION
                                         |
                                  +------+------+
                                  |             |
                                  v             v
                                FAIL           PASS
                                  |             |
                                  v             v
                              KEEP OPEN       CLOSE
                                                |
                                                v
                                    REVALIDATE DEPENDENTS
```

Model-level architecture.

---

# 294. Cross-Law Architecture

```text
                      [[L17_RSCF]]
                           |
                           v
                  structured artifact
                           |
                           v
                 [[L19_PROOF_CAPSULE]]
                           |
                           v
                    load-bearing proof
                           |
                           v
                  [[L26_PROOF_COORDINATION]]
                           |
                           v
                       [[L27_GAP]]
                      /     |      \
                     /      |       \
                    v       v        v
                EXPOSE   REGISTER   CLOSE
                    |       |        |
                    |       |        v
                    |       |   EXECUTED EVIDENCE
                    |       |
                    v       v
              [[L28_CRITICAL_GAP]]
                    |
                    v
          [[FAIL_CLOSED_GOVERNANCE]]
                    |
                    v
          [[L10_FAILURE_RECOVERY]]
                    |
                    v
             [[L25_SHARD_LOCAL]]
```

Exact interfaces are not source-established.

---

# 295. Gap Invariants

```text
GAP-I1
MISSING EVIDENCE REMAINS VISIBLE.

GAP-I2
PLAUSIBLE [[ARCHITECTURE]] DOES NOT CLOSE A GAP.

GAP-I3
UNKNOWN/GAP IS A VALID FIRST-CLASS OUTPUT.

GAP-I4
UNKNOWN DOES NOT MEAN FALSE.

GAP-I5
UNKNOWN DOES NOT MEAN TRUE.

GAP-I6
EVERY ARTIFACT EXPOSES ITS OWN LOAD-BEARING GAPS.

GAP-I7
A GAP PROPAGATES ONLY THROUGH MATERIAL DEPENDENCIES.

GAP-I8
LOCAL GAPS DO NOT AUTOMATICALLY INVALIDATE UNRELATED STATE.

GAP-I9
GAP CLOSURE REQUIRES NEW EVIDENCE OF THE CORRECT TYPE.

GAP-I10
RESTATEMENT IS NOT EVIDENCE.

GAP-I11
REPETITION IS NOT VALIDATION.

GAP-I12
DOCUMENTATION CLAIMS ARE NOT EXECUTION OBSERVATIONS.

GAP-I13
VALIDATION CLOSES ONLY THE SCOPE IT ACTUALLY TESTS.

GAP-I14
SIMULATION DOES NOT SILENTLY CLOSE EMPIRICAL GAPS.

GAP-I15
CORRELATED DESCENDANTS DO NOT CLOSE INDEPENDENCE GAPS.

GAP-I16
CLOSING ONE SUB-GAP DOES NOT CLOSE UNRESOLVED SIBLING GAPS.

GAP-I17
CLOSED GAPS MAY REOPEN WHEN LOAD-BEARING CONDITIONS FAIL.

GAP-I18
HISTORICAL GAP STATES ARE NOT SILENTLY REWRITTEN.

GAP-I19
CRITICAL GAPS MAY REQUIRE FAIL-CLOSED EXECUTION.

GAP-I20
COMPLETENESS NEVER JUSTIFIES FABRICATION.
```

Only the four source laws are directly canonical-source claims; these
invariants are expanded derivations.

---

# 296. Anti-Pattern Register

```yaml
anti_patterns:

  - id: GAP-AP01
    name: PLAUSIBILITY_AS_EVIDENCE

  - id: GAP-AP02
    name: ARCHITECTURE_AS_IMPLEMENTATION

  - id: GAP-AP03
    name: RESTATEMENT_AS_CLOSURE

  - id: GAP-AP04
    name: REPETITION_AS_VALIDATION

  - id: GAP-AP05
    name: DOCUMENTATION_AS_EXECUTION

  - id: GAP-AP06
    name: CODE_PRESENCE_AS_EXECUTION

  - id: GAP-AP07
    name: TEST_PRESENCE_AS_PASS

  - id: GAP-AP08
    name: TEST_PASS_AS_COMPLETE_COVERAGE

  - id: GAP-AP09
    name: SIMULATION_AS_EMPIRICAL_VALIDATION

  - id: GAP-AP10
    name: CORRELATION_AS_CAUSATION

  - id: GAP-AP11
    name: STRUCTURAL_SIMILARITY_AS_CAUSATION

  - id: GAP-AP12
    name: MULTIPLE_DESCENDANTS_AS_INDEPENDENCE

  - id: GAP-AP13
    name: AUTHORITY_CLAIM_AS_AUTHORITY_EVIDENCE

  - id: GAP-AP14
    name: CANON_LOCATION_AS_UNCONDITIONAL_STATUS

  - id: GAP-AP15
    name: LONG_EXPLANATION_AS_EVIDENCE

  - id: GAP-AP16
    name: EQUATION_AS_EMPIRICAL_PROOF

  - id: GAP-AP17
    name: MODEL_AS_REALITY

  - id: GAP-AP18
    name: UNKNOWN_AS_FALSE

  - id: GAP-AP19
    name: UNKNOWN_AS_TRUE

  - id: GAP-AP20
    name: GLOBAL_INVALIDATION_FROM_LOCAL_GAP

  - id: GAP-AP21
    name: SILENT_GAP_CLOSURE

  - id: GAP-AP22
    name: SILENT_GAP_DELETION

  - id: GAP-AP23
    name: GAP_COUNT_AS_QUALITY_METRIC

  - id: GAP-AP24
    name: FAST_CLOSURE_OVER_VALID_CLOSURE

  - id: GAP-AP25
    name: INVENTED_CANON_TO_COMPLETE_PATTERN
```

---

# 297. Failure Mode Register

```yaml
failure_modes:

  - id: GAP-FM01
    name: HIDDEN_IMPLEMENTATION_GAP
    effect: >
      Specification is presented as implemented without implementation
      evidence.

  - id: GAP-FM02
    name: HIDDEN_AUTHORITY_GAP
    effect: >
      Governance or canon authority is assumed rather than established.

  - id: GAP-FM03
    name: HIDDEN_VALIDATION_GAP
    effect: >
      Validation claims are promoted without execution evidence.

  - id: GAP-FM04
    name: HIDDEN_PROVENANCE_GAP
    effect: >
      Claim ancestry is missing but confidence ignores the loss.

  - id: GAP-FM05
    name: FALSE_CLOSURE
    effect: >
      Gap marked closed without matching evidence.

  - id: GAP-FM06
    name: PARTIAL_CLOSURE_AS_FULL
    effect: >
      One sub-gap is resolved and the entire parent is marked closed.

  - id: GAP-FM07
    name: SCOPE_LEAKAGE
    effect: >
      Scoped evidence closes a broader gap without bridge evidence.

  - id: GAP-FM08
    name: REGIME_LEAKAGE
    effect: >
      Evidence from one epistemic regime closes another regime's gap.

  - id: GAP-FM09
    name: CORRELATED_CLOSURE
    effect: >
      Descendant repetition is mistaken for independent validation.

  - id: GAP-FM10
    name: STALE_CLOSURE
    effect: >
      Old evidence remains treated as gap-closing after conditions
      change.

  - id: GAP-FM11
    name: GAP_ERASURE_ON_MERGE
    effect: >
      One branch's silence causes another branch's open gap to vanish.

  - id: GAP-FM12
    name: GLOBAL_OVERINVALIDATION
    effect: >
      Local gap causes unrelated valid state to be discarded.

  - id: GAP-FM13
    name: UNDERINVALIDATION
    effect: >
      Dependent claims remain promoted after their load-bearing gap is
      discovered.

  - id: GAP-FM14
    name: HISTORY_REWRITE
    effect: >
      Later closure silently rewrites earlier UNKNOWN/GAP state.

  - id: GAP-FM15
    name: COMPLETENESS_PRESSURE
    effect: >
      Missing canon is invented to make the artifact appear complete.
```

---

# 298. Adversarial Gap Validation

Before declaring a material gap closed, challenge closure through a
different path.

Questions:

```text
1. Did we obtain genuinely new evidence?

2. Does the evidence address the exact missing element?

3. Was the required validation actually executed?

4. Is the evidence scoped correctly?

5. Is the regime correct?

6. Is it fresh enough?

7. Is the provenance recoverable?

8. Is apparent independence actually correlated?

9. Did we resolve the root gap or only one symptom?

10. Would the gap reopen if one fragile assumption changed?

11. Are competing explanations still viable?

12. Did prose, authority, or architecture substitute for evidence?
```

---

# 299. Gap Sensitivity Test

For each consequential gap:

```text
identify the smallest missing premise
whose resolution could flip
the conclusion or action
```

Resolve that first.

This minimizes wasted validation.

---

# 300. Gap Closure Proof Capsule

```yaml
gap_closure_proof_capsule:

  claim:
    text: "Gap G001 is closed."
    class: DERIVED

  load_bearing_premises:

    - id: P1
      statement:
        "Evidence E directly addresses the missing element in G001."

    - id: P2
      statement:
        "Validation V was executed against E."

    - id: P3
      statement:
        "V passed under the relevant scope and regime."

  evidence:
    - E
    - validation_receipt_V

  dependencies:
    - validator_version
    - target_artifact_version

  competing:
    - "The validation may have targeted the wrong version."

  falsifiers:
    - "Receipt does not bind to the target artifact."
    - "Validator result cannot be reproduced where replay is required."
    - "Scope mismatch discovered."
    - "Load-bearing dependency invalidated."

  conclusion:
    class: CONDITIONAL
```

Exact fields are illustrative.

---

# 301. Gap Discovery Proof Capsule

```yaml
gap_discovery_capsule:

  claim:
    text:
      "Required implementation evidence for component X is missing."
    class: DERIVED

  premises:
    - "Claim C depends on implemented component X."
    - "Available evidence does not establish implementation X."

  conclusion:
    class: UNKNOWN/GAP

  action:
    - expose_gap
    - register_gap
    - avoid_implementation_claim
```

---

# 302. Source vs Derived Boundary

```yaml
epistemic_boundary:

  SOURCE_ESTABLISHED:
    - GAP-1
    - GAP-2
    - GAP-3
    - GAP-4
    - F1
    - PROPOSED_SPECIFICATION
    - AMOS_MODEL
    - CONDITIONAL
    - updated_2026_08_26
    - listed_RSCF_metadata
    - listed_related_links

  DERIVED_MODEL:
    - gap_state_machine
    - severity_taxonomy
    - closure_receipts
    - gap_versioning
    - gap_reopening
    - selective_invalidation_algorithm
    - gap_CAS
    - causal_epoch_integration
    - shard_local_gap_protocol
    - adversarial_closure_validation
    - information_value_prioritization

  UNKNOWN_GAP:
    - authoritative_gap_registry_schema
    - authoritative_closure_algorithm
    - authoritative_L28_semantics
    - exact_validator_contract
    - exact_persistence_mechanism
```

---

# 303. Canonical Integrity Matrix

| Claim                                                                | Class                       |
| -------------------------------------------------------------------- | --------------------------- |
| Missing implementation/authority/validation/provenance stays visible | SOURCE_CLAIM                |
| Plausible architecture does not fill those gaps                      | SOURCE_CLAIM                |
| UNKNOWN/GAP is first-class                                           | SOURCE_CLAIM                |
| Every artifact lists its load-bearing gaps                           | SOURCE_CLAIM                |
| Gap closure requires executed validation rather than restatement     | SOURCE_CLAIM                |
| Gaps have OPEN/CLOSED/REOPENED states                                | MODEL                       |
| Gaps use CAS transitions                                             | MODEL                       |
| Gap closure has signed receipts                                      | NOT_ESTABLISHED             |
| Critical gaps always halt globally                                   | NOT_ESTABLISHED / overclaim |
| L28 uses the severity model in this reconstruction                   | NOT_ESTABLISHED             |
| ChatGPT literally implements this registry                           | NOT_ESTABLISHED             |

---

# 304. Gap Decision Matrix

| State                                         | Recommended epistemic result |
| --------------------------------------------- | ---------------------------- |
| No material gap                               | Continue at supported class  |
| Non-load-bearing gap                          | Continue + expose if useful  |
| Load-bearing but conditionable                | CONDITIONAL                  |
| Critical premise missing                      | UNKNOWN/GAP                  |
| Two viable incompatible explanations          | COMPETING                    |
| Closure evidence acquired but not executed    | GAP remains                  |
| Validation executed but wrong scope           | GAP remains                  |
| Validation executed and directly resolves gap | Candidate closure            |
| Closure later invalidated                     | REOPEN / revalidate          |

---

# 305. Gap Governance Matrix

| Stakes                     | Gap                     | Governance posture             |
| -------------------------- | ----------------------- | ------------------------------ |
| Low, reversible            | Explanatory             | Continue                       |
| Low, reversible            | Decision-relevant       | Conditional / probe            |
| High, reversible           | Decision-relevant       | Validate first where practical |
| Irreversible               | Authority gap           | Fail closed                    |
| Safety-critical            | Safety gap              | Fail closed                    |
| High downstream dependency | Critical provenance gap | Escalate validation            |
| Pure explanation           | Cosmetic                | Defer                          |

This is a derived governance model.

---

# 306. Gap Closure Evidence Matrix

```text
IMPLEMENTATION GAP
    -> implementation / execution evidence

AUTHORITY GAP
    -> authoritative governance evidence

VALIDATION GAP
    -> executed validation evidence

PROVENANCE GAP
    -> source lineage evidence

SCOPE GAP
    -> applicability evidence

REGIME GAP
    -> regime declaration / valid bridge

TEMPORAL GAP
    -> fresh evidence / revalidation

CAUSAL GAP
    -> appropriately typed causal evidence

INDEPENDENCE GAP
    -> provenance/failure-mode independence analysis
```

---

# 307. Gap Escalation Matrix

Escalate if:

```text
gap can flip conclusion
gap can flip action
gap affects governance
gap affects safety
gap affects irreversible mutation
gap crosses regimes
gap crosses shards
gap affects global invariant
gap involves correlated provenance
gap closure evidence conflicts
gap origin ambiguous
```

---

# 308. Gap De-Escalation

De-escalate when:

```text
gap no longer affects decision
closure evidence is sufficient
affected dependency closure is known
remaining gaps are explanatory/cosmetic
```

Do not continue maximal investigation after action sufficiency is
reached.

---

# 309. Minimum Sufficient Gap Resolution

The goal is not:

```text
zero unknowns
```

The goal is:

```text
no unresolved decision-changing
or integrity-breaking unknowns
for the intended claim/action
```

---

# 310. Zero-Gap Fallacy

A complex system claiming:

```text
NO GAPS
```

should not automatically be considered stronger.

Possible explanations include:

```text
complete validation
or
poor gap detection
or
hidden uncertainty
```

Evidence is required to discriminate.

---

# 311. Gap Visibility as Integrity Signal

Visible gaps can be a positive signal of epistemic discipline.

But:

```text
visible gaps
```

alone do not prove the rest of the artifact correct.

Again:

```text
absence of hiding
!=
proof of truth
```

---

# 312. Gap Registry as Proof Boundary

A gap registry should be read as:

```text
THESE ARE THE KNOWN LOAD-BEARING
UNRESOLVED ELEMENTS
```

not:

```text
THESE ARE GUARANTEED TO BE
ALL POSSIBLE GAPS
```

unless completeness has itself been validated.

---

# 313. Unknown Unknowns

L27 primarily governs recognized gaps.

It cannot guarantee detection of every unknown unknown.

Therefore:

```text
GAP REGISTRY COMPLETE
```

is itself a claim requiring evidence if asserted.

---

# 314. Registry Completeness Gap

A system may have:

```text
known gaps
```

and also:

```text
uncertainty about whether all gaps were discovered
```

This meta-gap can matter for high-stakes reasoning.

---

# 315. Meta-Gap

A meta-gap is uncertainty about the gap-management process itself.

Examples:

```text
Are all load-bearing dependencies represented?

Did the validator inspect all required interfaces?

Is the gap registry complete?
```

The source does not explicitly define meta-gaps.

---

# 316. Gap-of-Gap Recursion

Unbounded recursion such as:

```text
gap about gap about gap about gap...
```

is not useful by default.

Stop when additional recursion cannot materially change:

```text
claim
decision
action
closure test
```

---

# 317. Bounded Recursion

The bounded registry principle supports stopping at the smallest level
that preserves decision-relevant uncertainty.

This prevents gap management from becoming infinite bookkeeping.

---

# 318. Gap Registry Compression

A large number of related gaps may be grouped under a root gap if:

```text
their common cause is known
and
the grouping preserves closure requirements
```

---

# 319. Gap Registry Expansion

Split a root gap when its children require:

```text
different evidence
different authorities
different scopes
different closure tests
```

---

# 320. Gap Independence

Two gaps may be independent or correlated.

Example:

```text
G1: missing implementation
G2: missing tests
```

If tests cannot exist because implementation is absent, the gaps are
causally related.

Do not treat gap counts as independent risk units.

---

# 321. Gap Correlation

A single missing source can generate:

```text
provenance gap
authority gap
validation gap
scope gap
```

depending on what the source was supposed to establish.

Root-cause analysis can reduce redundant closure effort.

---

# 322. Gap Topology

Gap management should consider:

```text
which gaps share causes
which claims share gaps
which gaps block other closure tests
```

This is more informative than a flat count.

---

# 323. Gap Topology Example

```text
                G_SOURCE
               /        \
              v          v
        G_AUTHORITY    G_SCHEMA
                         |
                         v
                     G_VALIDATOR
                         |
                         v
                     CLAIM C
```

Closing `G_SOURCE` may resolve multiple descendants if it supplies the
missing authority and schema.

---

# 324. Gap Closure Ordering

Resolve upstream gaps first when they block downstream validation.

Example:

```text
schema unknown
-> validator cannot execute
-> validation unknown
```

The efficient order is:

```text
schema
then validator
then validation
```

---

# 325. Cheapest High-Information Test

If several closure tests are available, prefer the one that most
efficiently discriminates among outcome-changing possibilities.

This is an optimization under the constraint:

```text
optimization may not weaken integrity
```

---

# 326. Gap and Proof Coordination Fast Path

If all load-bearing gaps for a local proof are closed and locality is
established:

```text
broader proof coordination
may be unnecessary
```

But:

```text
NO VISIBLE GAP
```

alone is insufficient.

Dependency closure and non-conflict must also be established.

---

# 327. Gap and Proof Coordination Escalation

Escalate if:

```text
gap registry incomplete
shared ancestry unknown
interface unknown
authority ambiguous
validator conflict
cross-shard dependency unknown
```

These gaps directly undermine proof-local finalization.

---

# 328. Gap and Finality

A conclusion can be final only relative to its known applicability and
open-gap state.

Discovery of a new load-bearing gap may invalidate finality.

Thus:

```text
FINAL
```

must not mean:

```text
immune to future evidence
```

unless a separate formal contract defines that meaning.

---

# 329. Gap and Causal Finality

Historical finality can coexist with later epistemic supersession.

Example:

```text
e1:
Decision D made with G unknown.

e2:
G resolved.

e3:
D superseded.
```

The historical record remains intact.

---

# 330. Gap and Recovery Finality

A recovery can finish with:

```text
known residual noncritical gaps
```

if action sufficiency is achieved.

It need not claim universal completeness.

---

# 331. Gap and Safe Degradation

If a noncritical capability depends on an unresolved gap:

```text
disable or degrade that capability
```

while preserving unaffected core operation where possible.

This is a derived fail-safe pattern.

---

# 332. Gap and Repairability

An architecture is easier to repair when gaps preserve:

```text
identity
dependency
closure condition
history
```

because the system knows what evidence to seek.

---

# 333. Gap and Reversibility

Gap-aware systems should prefer actions that can be reversed when
critical uncertainty remains.

This converts some uncertainty from:

```text
catastrophic exposure
```

to:

```text
bounded experiment
```

where governance permits.

---

# 334. Gap and Learning

A gap is a candidate learning target only if resolving it has positive
expected value.

Not every unknown deserves immediate investigation.

---

# 335. Gap and Knowledge Harvest

Conceptual pipeline:

```text
EPHEMERAL CLAIM
      |
      v
PERSISTENT EVIDENCE
      |
      v
VALIDATION
      |
      v
VALIDATED KNOWLEDGE
```

If a required transition is missing:

```text
GAP
```

must remain visible.

---

# 336. Documentation Claim Boundary

README/documentation claims remain:

```text
SOURCE_CLAIM
```

until independently validated where validation is required.

L27 GAP-4 directly supports this discipline.

---

# 337. Executable Evidence Boundary

Executable evidence can strengthen a claim.

It does not automatically establish:

```text
formal proof
hardware independence
universal scope
causal mechanism
```

unless those are what the execution validates.

---

# 338. External Evidence Boundary

External evidence may close a corpus gap, but the resulting conclusion
should preserve:

```text
source
scope
freshness
regime
```

and distinguish external validation from original AMOS canon.

---

# 339. Corpus Gap vs Reality Gap

Important distinction:

```text
AMOS corpus does not establish X
```

is not the same claim as:

```text
X is unknown to humanity
```

L27 gap scope must remain explicit.

---

# 340. Canon Gap vs Implementation Gap

Likewise:

```text
canon does not define mechanism X
```

does not imply:

```text
implementation lacks X
```

The implementation may exist but be undocumented.

Both possibilities remain viable.

---

# 341. Implementation Gap vs Runtime Failure

No implementation evidence does not prove the implementation fails.

Correct:

```text
implementation status = UNKNOWN/GAP
```

not:

```text
implementation = BROKEN
```

---

# 342. Validation Gap vs Invalidity

No validation evidence does not automatically mean:

```text
claim false
```

It means the stronger validation claim is unsupported.

---

# 343. Provenance Gap vs Falsehood

Unknown provenance reduces trust and confidence.

It does not logically establish falsehood.

---

# 344. Authority Gap vs Incorrectness

A claim can be factually correct while lacking authority to govern
AMOS.

Authority and truth remain separate dimensions.

---

# 345. Gap State vs Truth State

A gap is a statement about epistemic support, not necessarily about the
underlying world's truth value.

Conceptually:

```text
WORLD:
P may be true or false.

KNOWLEDGE STATE:
P = UNKNOWN/GAP.
```

---

# 346. Gap Law and Integrity Ordering

When forced to choose:

```text
complete but fabricated
```

versus:

```text
incomplete but accurate
```

L27 requires the latter.

Normalized:

```text
INTEGRITY
>
COMPLETENESS
```

---

# 347. Gap Law and Fluency

Likewise:

```text
epistemically awkward but accurate
```

is preferable to:

```text
fluent invented closure
```

---

# 348. Gap Law and Speed

If additional validation is required for a critical gap:

```text
speed
```

does not justify silent closure.

---

# 349. Gap Law and Token Savings

A gap marker such as:

```text
NOT_ESTABLISHED
```

may be shorter than speculative completion.

Compression therefore aligns naturally with L27 when performed
correctly.

---

# 350. Gap Law and Optimization

Optimization is valid only if it preserves:

```text
gap visibility
gap provenance
gap scope
closure evidence
dependency effects
```

Any optimization that hides unresolved uncertainty is a regression.

---

# 351. Anti-Regression Gate

A change to gap handling is acceptable only if it preserves or improves:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
gap visibility
closure integrity
selective invalidation
safety
efficiency
user fit
```

---

# 352. Gap Registry Migration

If gap storage changes formats:

```text
old registry -> new registry
```

migration must preserve load-bearing open gaps.

A migration that drops gaps because the new schema lacks fields is an
integrity failure.

---

# 353. Gap Deduplication

Duplicate gap records may be merged when they refer to the same
underlying missing element.

But deduplication must not erase distinct:

```text
scopes
closure conditions
affected claims
```

---

# 354. Gap Pointer Semantics

Like proof coordination, one implementation might maintain one
authoritative gap record with pointers from dependent artifacts.

However, GAP-3 explicitly says every artifact lists its own
load-bearing gaps.

Therefore a valid design could use:

```text
artifact-local pointer
->
authoritative gap record
```

if the gap remains visible locally.

This exact mechanism is not source-defined.

---

# 355. Gap Registry Authority

The source does not specify whether gap records have:

```text
one authoritative home
multiple synchronized homes
embedded copies
```

Do not import L26 PXC-1 literally without explicit integration.

---

# 356. Gap Closure Authority

GAP-4 requires evidence.

It does not define who has authority to declare closure.

Therefore:

```text
closure evidence
```

and:

```text
closure authority
```

may be separate requirements.

---

# 357. Closure Authority Gap

A system can have:

```text
evidence sufficient
```

but:

```text
authority to mutate canonical status = UNKNOWN
```

Then the evidence gap may be closed while governance mutation remains
blocked.

---

# 358. Evidence vs Authority Matrix

| Evidence | Authority | State                                     |
| -------- | --------- | ----------------------------------------- |
| Missing  | Missing   | GAP                                       |
| Present  | Missing   | Evidence supported; authority gap remains |
| Missing  | Present   | Authority cannot substitute for evidence  |
| Present  | Present   | Candidate governed closure                |

---

# 359. Gap Closure and Governance

For canonical mutation, a complete closure transaction may need:

```text
epistemic evidence
+
governance authority
```

where the governance system requires both.

This is a derived integration.

---

# 360. Gap Closure and Mutation

Closing a gap changes epistemic state.

Therefore consequential closure should be treated as a governed state
mutation rather than merely cosmetic editing.

---

# 361. Silent Closure as Mutation Defect

If a document changes:

```text
UNKNOWN
```

to:

```text
VERIFIED
```

without evidence lineage, the mutation itself is an integrity defect.

---

# 362. Gap Closure Audit

An audit should be able to ask:

```text
What closed this gap?

Where is the evidence?

What validator was used?

What version was tested?

What scope was established?

Who/what authorized status mutation?

What dependent claims changed?
```

Exact audit schema remains unspecified.

---

# 363. Gap Closure Replay

Where replayability applies, a closure event should be reproducible from
its recorded inputs.

But replay does not independently establish that the original closure
criterion was correct.

---

# 364. Gap Closure Proof Coordination

If closure depends on multiple proofs:

```text
P1
P2
P3
```

then L26 requires checking:

```text
parts
interfaces
independence
verification
```

before the gap is promoted as closed.

---

# 365. Gap Closure Competing Evidence

Suppose:

```text
E1 supports closure
E2 supports keeping gap open
```

If both remain viable:

```text
COMPETING
```

may be the correct state.

Do not force `CLOSED` for convenience.

---

# 366. Gap Closure Conflict

A conflict exists when:

```text
same gap
same scope/version
same epoch context
```

has incompatible validated status claims.

The conflict itself becomes decision-relevant evidence requiring
resolution.

---

# 367. Gap Closure Fail-Closed Rule

For critical gaps:

```text
closure evidence conflict
```

should generally block irreversible execution until resolved or
explicitly governed otherwise.

---

# 368. Gap Closure Rollback

If closure is later shown invalid:

```text
invalidate closure premise
reopen gap
invalidate dependent conclusions
preserve unrelated conclusions
```

Do not recompute everything unless dependency topology is unavailable.

---

# 369. Gap Closure Repair

Repair targets the failed closure edge.

Example:

```text
validator version wrong
```

Repair:

```text
rerun correct validator
```

rather than discarding all underlying evidence.

---

# 370. Gap Closure Recovery

If closure fails operationally:

```text
do not repeat identical failed path
without changed evidence
```

Reroute to another validation mechanism where appropriate.

---

# 371. Gap Closure Idempotence

Repeated application of the same closure receipt should not fabricate
additional confidence.

```text
same evidence replayed N times
!=
N independent closures
```

---

# 372. Gap Closure Independence

Independent closure evidence can strengthen confidence where the claim
requires independent support.

But independence must be demonstrated through provenance/failure-mode
analysis.

---

# 373. Gap Closure Correlation Risk

Two validators may appear independent while sharing:

```text
same source
same parser
same runtime
same test oracle
same model
```

Therefore independence is scoped and typed.

---

# 374. Gap Closure Provenance Topology

```text
SOURCE S
   |
   v
VALIDATION V
  / \
 v   v
R1   R2
```

R1 and R2 are two receipts but one validation ancestry.

They do not create two independent closure foundations.

---

# 375. Gap Closure Freshness

A closure receipt may have a validity envelope.

If:

```text
target version changes
```

the closure may no longer apply.

---

# 376. Gap Closure Scope Envelope

A closure should conceptually inherit:

```text
system
environment
scale
time
regime
measurement method
assumptions
```

where relevant.

---

# 377. Gap Closure Causal Firewall

Closing a correlation gap does not necessarily close a causality gap.

Each evidence type must remain distinct.

---

# 378. Gap Closure Measurement Firewall

A measurement can close:

```text
observed value
```

while leaving:

```text
measurement validity
instrument calibration
generalization
```

open if those are material.

---

# 379. Gap Closure Model Firewall

A better model can reduce model uncertainty.

It does not automatically close empirical uncertainty.

---

# 380. Gap Closure Execution Firewall

Successful execution can close:

```text
execution succeeded under conditions E
```

but not automatically:

```text
design is universally correct
```

---

# 381. Gap Closure Canon Firewall

Authoritative canon can close:

```text
canonical definition
```

but not automatically:

```text
empirical theorem
```

---

# 382. Gap Closure Security Firewall

Passing functional tests does not close security gaps unless those tests
actually validate the relevant security properties.

---

# 383. Gap Closure Safety Firewall

Likewise, performance validation cannot silently substitute for safety
validation.

---

# 384. Gap Closure Governance Firewall

Technical validation cannot silently substitute for authority.

---

# 385. Gap Closure Completeness Firewall

A gap registry entry marked closed does not prove:

```text
no related gaps remain
```

unless the closure contract establishes that scope.

---

# 386. Gap Closure Finality Firewall

Closed does not mean:

```text
eternally immutable
```

It means the gap is resolved within its current validity envelope.

---

# 387. Gap Closure Confidence Firewall

Closure evidence cannot justify confidence beyond:

```text
its own quality
scope
independence
freshness
```

---

# 388. Gap Closure Promotion Firewall

No status transition:

```text
UNKNOWN -> VERIFIED
```

should occur merely because:

```text
the answer now sounds complete
```

---

# 389. Gap Output Examples

### Example A — Implementation

```text
SOURCE_CLAIM:
The architecture requires mechanism M.

GAP:
No implementation artifact for M is established.

MODEL:
One possible implementation is X.

BOUNDARY:
X does not close the implementation gap.
```

### Example B — Validation

```text
SOURCE_CLAIM:
Documentation reports 21/21 tests pass.

GAP:
The test artifacts/execution have not been independently inspected.

CONCLUSION:
The 21/21 result remains SOURCE_CLAIM.
```

### Example C — Authority

```text
CLAIM:
Schema S is canonical.

GAP:
No authoritative promotion record is available.

SAFE RESULT:
Canonical authority remains CONDITIONAL / UNKNOWN.
```

---

# 390. Gap Law Compact Runtime

```text
DETECT MISSING LOAD-BEARING ELEMENT.

DO NOT FILL IT.

NAME IT.

BOUND IT.

REGISTER IT.

PROPAGATE IT
ONLY TO DEPENDENTS.

CLASSIFY ITS CONSEQUENCE.

IF NONCRITICAL:
CONTINUE WITH VISIBLE GAP.

IF CONDITIONABLE:
RETURN CONDITIONAL.

IF CRITICAL:
FAIL CLOSED OR RETURN UNKNOWN/GAP.

TO CLOSE:

OBTAIN NEW EVIDENCE.

EXECUTE THE RELEVANT VALIDATION.

VERIFY SCOPE.

VERIFY REGIME.

VERIFY PROVENANCE
WHERE MATERIAL.

CLOSE ONLY
THE GAP ACTUALLY RESOLVED.

PRESERVE HISTORY.

REVALIDATE DEPENDENTS.

IF CLOSURE FAILS:
REOPEN LOCALLY.

NEVER SUBSTITUTE
RESTATEMENT
FOR EVIDENCE.
```

---

# 391. Gap Law Minimal Runtime

```text
IF MISSING:
SAY MISSING.

IF LOAD-BEARING:
TRACK IT.

IF CRITICAL:
DO NOT GUESS.

IF CLOSING:
SHOW EVIDENCE.
```

---

# 392. Gap Law Proof Obligation

For every closure claim:

```text
"G is closed"
```

the system should be able to answer:

```text
What evidence changed
between OPEN and CLOSED?
```

If the answer is:

```text
none
```

the closure violates GAP-4.

---

# 393. Gap Law Conservation Principle

An unresolved gap cannot disappear merely because information is:

```text
summarized
compressed
copied
merged
cached
replayed
reformatted
```

It disappears only through valid closure or explicit supersession of
the affected claim.

This is a derived integrity invariant.

---

# 394. Gap Law Monotonic Evidence Principle

Status may change:

```text
UNKNOWN -> SUPPORTED
```

only through evidence/validation sufficient for the target class.

It may also change downward when prior support fails.

Thus epistemic status itself is not monotonically increasing.

Evidence lineage, however, should remain recoverable.

---

# 395. Gap Law Non-Erasure Principle

Gap closure should preserve the historical fact:

```text
this was once unresolved
```

where auditability matters.

This prevents later evidence from rewriting prior epistemic history.

---

# 396. Gap Law Local Invalidation Principle

If closure evidence E fails:

```text
invalidate:
E
closure(G)
dependent conclusions
```

Preserve:

```text
unaffected evidence
unrelated gaps
unrelated conclusions
```

---

# 397. Gap Law Reuse Principle

A valid gap closure proof may be reused while:

```text
dependencies unchanged
scope valid
regime valid
freshness valid
evidence valid
no defeating contradiction
```

Otherwise revalidation is required.

---

# 398. Gap Law Independence Principle

Repeated use of one closure proof does not create new independent
evidence.

```text
reuse
!=
independence
```

---

# 399. Gap Law Authority Principle

A system may have authority to decide under uncertainty.

That authority does not make the gap disappear.

Correct:

```text
DECISION AUTHORIZED
DESPITE GAP G
```

Incorrect:

```text
G CLOSED
BECAUSE DECISION WAS AUTHORIZED
```

---

# 400. Gap Law Decision Principle

Decision under uncertainty should preserve:

```text
known facts
open gaps
assumptions
action rationale
invalidation conditions
```

where consequential.

---

# 401. Gap Law Action Principle

When a gap cannot be closed economically:

```text
choose an action robust to both
plausible states of the gap
```

where possible.

This is a model-level decision strategy.

---

# 402. Gap Law Repair Principle

If the system discovers it fabricated a closure:

```text
reopen the gap
downgrade dependent claims
preserve unaffected work
record correction
```

Do not defend the prior completion for consistency's sake.

---

# 403. Gap Law Anti-Regression Principle

A future optimization must never improve:

```text
speed
fluency
compactness
```

by reducing:

```text
gap visibility
closure evidence
provenance recoverability
dependency tracking
```

---

# 404. Gap Law Canon Boundary Principle

When canon is unavailable:

```text
UNKNOWN CANON
```

is the correct state.

Do not generate exact missing canon and then treat the generated text as
recovered source.

---

# 405. Gap Law Reconstruction Principle

A reconstruction may be useful when clearly separated:

```text
SOURCE SPINE
+
DERIVED FORMALIZATION
+
MODEL EXTENSION
+
EXPLICIT GAPS
```

This preserves utility without provenance collapse.

---

# 406. Gap Law Corpus Boundary

Statements found in AMOS corpus files remain corpus evidence according
to their declared status.

They are not automatically empirical claims about external reality.

---

# 407. Gap Law Reality Boundary

A corpus gap and an empirical gap are different.

Example:

```text
AMOS source does not specify threshold T.
```

This does not establish:

```text
no valid threshold T exists externally.
```

---

# 408. Gap Law Implementation Boundary

This law describes an AMOS reasoning model.

It does not establish that ChatGPT literally implements:

```text
persistent gap registries
MVCC gap state
CAS gap closure
causal epoch storage
distributed shard-local gap coordination
```

unless separate implementation evidence exists.

---

# 409. Gap Law Formal-Proof Boundary

The existence of this structured specification does not prove:

```text
L27 is mathematically complete
L27 is formally verified
L27 guarantees zero hallucinations
L27 detects all unknown unknowns
```

Those would require separate evidence.

---

# 410. Gap Law Empirical Boundary

The source does not supply empirical measurements demonstrating:

```text
false closure rate
gap detection recall
gap classification accuracy
decision improvement
runtime overhead
```

These remain empirical gaps.

---

# 411. Gap Law Security Boundary

L27 can reduce some epistemic failure modes.

It does not itself establish a complete security architecture.

---

# 412. Gap Law Safety Boundary

L27 supports fail-closed behavior under critical uncertainty.

It does not by itself define every safety threshold or policy.

---

# 413. Gap Law Governance Boundary

L27 recognizes authority gaps.

It does not itself define the complete governance authority hierarchy.

---

# 414. Gap Law L28 Boundary

The reference to  establishes relationship, not
content.

Until L28 is supplied:

```text
exact critical-gap canon
=
UNKNOWN/GAP
```

This is an intentional application of L27 to itself.

---

# 415. Gap Law Source Preservation

The exact supplied source spine remains:

```markdown
# L27 Gap Law

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **GAP-1 Expose Don't Fill**: missing implementation/authority/validation/provenance stays visible; plausible architecture never fills it.
- **GAP-2 Gap Is Status Not Shame**: UNKNOWN/GAP is an honest epistemic class, first-class in outputs.
- **GAP-3 Bounded Gap Registry**: every artifact lists its own load-bearing gaps (proof capsules).
- **GAP-4 Gap Closure Requires Evidence**: closing a gap demands executed validation, not restatement.

## 4. Falsifiers
F1: authoritative canon treats gaps as failures to hide.
```

Expanded content must not silently overwrite this source spine.

---

# 416. Supersession Boundary

The source states:

```text
Proposed specification replacing placeholder.
```

Therefore:

```text
a prior placeholder existed
```

is source-supported.

The placeholder's exact:

```text
content
version
date
hash
semantics
```

are not supplied.

They remain gaps.

---

# 417. Canon Directory Boundary

The artifact is located under:

```text
01_CANON/01_CORE_LAWS
```

but explicitly declares:

```text
canonical_status: CONDITIONAL
```

Therefore:

```text
CANON DIRECTORY
!=
UNCONDITIONAL CANONICAL STATUS
```

when explicit metadata says otherwise.

---

# 418. Claim-Class Boundary

The source contains:

```yaml
rscf:
  claim_class: CONDITIONAL
```

and later:

```text
claim_class: AMOS_MODEL
```

while separately stating:

```text
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
```

The safest interpretation is to preserve both source values and
normalize only at the model layer.

---

# 419. Normalized Status Model

```yaml
normalized_status:
  source_state: SOURCE_CLAIM
  epistemic_class: AMOS_MODEL
  canonical_status: CONDITIONAL
```

This is a derived normalization, not source replacement.

---

# 420. RSCF Contract

```yaml
RSCF-CONTRACT:

  node_id: l27_gap

  node_type:
    source_value: note

  document_type:
    source_value: gap

  H:
    name: L27 Gap Law

    purpose: >
      Preserve unresolved implementation, authority, validation, and
      provenance gaps as explicit epistemic state rather than filling
      them through plausible architecture.

  M:

    GAP-1:
      name: Expose Don't Fill
      functions:
        - expose_missing_implementation
        - expose_missing_authority
        - expose_missing_validation
        - expose_missing_provenance
        - prohibit_plausible_fill

    GAP-2:
      name: Gap Is Status Not Shame
      functions:
        - first_class_unknown
        - honest_gap_output

    GAP-3:
      name: Bounded Gap Registry
      functions:
        - artifact_local_gap_listing
        - load_bearing_gap_tracking
        - proof_capsule_gap_visibility

    GAP-4:
      name: Gap Closure Requires Evidence
      functions:
        - require_new_evidence
        - require_executed_validation
        - reject_restatement_as_closure

  L:
    - gap_identity
    - missing_evidence
    - affected_claim
    - dependency
    - scope
    - closure_condition
    - validation_evidence
    - gap_status

  source_state:
    SOURCE_CLAIM

  epistemic_class:
    AMOS_MODEL

  canonical_status:
    CONDITIONAL

  provenance:
    AMOS_corpus

  scope:
    core_laws
```

---

# 421. RSCF-NODE

```yaml
RSCF-NODE:

  node_id: l27_gap

  node_type: note

  path:
    01_CANON/01_CORE_LAWS/L27_GAP.md

  claim_class:
    source_values:
      - CONDITIONAL
      - AMOS_MODEL

  normalized_model:
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL

  state:
    SOURCE_CLAIM

  provenance:
    AMOS_corpus

  scope:
    core_laws
```

---

# 422. RSCF-RELATIONS

```yaml
RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - RELATED_TO: [[L25_SHARD_LOCAL]]

  - RELATED_TO: [[L28_CRITICAL_GAP]]

  - RELATED_TO: [[L10_FAILURE_RECOVERY]]

  - RELATED_TO: [[L17_RSCF]]

  - RELATED_TO: [[FAIL_CLOSED_GOVERNANCE]]

  - INDEXED_BY: [[01_CORE_LAWS_MOC]]

  - FRAMEWORK_CONTEXT:
      [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

Only the supplied `INDEXED_BY` and `CHILD_OF` relations are directly
declared under `RSCF-RELATIONS`.

The `RELATED_TO` relations normalize the supplied Related list.

---

# 423. L27 Proof Capsule

```yaml
proof_capsule:

  claim:
    text: >
      L27 defines a conditional AMOS gap-management model requiring
      unresolved implementation, authority, validation, and provenance
      to remain visible; recognizing UNKNOWN/GAP as a first-class
      epistemic result; requiring artifacts to expose their own
      load-bearing gaps; and requiring executed validation rather than
      restatement for gap closure.
    class: SOURCE_CLAIM

  provenance:
    source: 01_CANON/01_CORE_LAWS/L27_GAP.md
    corpus: AMOS_corpus

  load_bearing_premises:

    - id: P1
      law: GAP-1
      class: SOURCE_CLAIM

    - id: P2
      law: GAP-2
      class: SOURCE_CLAIM

    - id: P3
      law: GAP-3
      class: SOURCE_CLAIM

    - id: P4
      law: GAP-4
      class: SOURCE_CLAIM

  scope:
    - core_laws
    - gap_management
    - epistemic_integrity

  regime:
    PROPOSED_SPECIFICATION

  canonical_status:
    CONDITIONAL

  gaps:
    - L27-G001
    - L27-G002
    - L27-G003
    - L27-G004
    - L27-G005
    - L27-G006

  falsifiers:
    - F1

  confidence_ceiling:
    source_spine: SOURCE_SUPPORTED
    expanded_mechanics: MODEL_DERIVED
```

---

# 424. L27 Gap Registry

In accordance with GAP-3, this artifact's principal load-bearing gaps
are explicitly preserved:

```yaml
artifact_gap_registry:

  artifact:
    id: l27_gap
    path: 01_CANON/01_CORE_LAWS/L27_GAP.md

  gaps:

    - id: L27-G001
      description:
        "Authoritative machine-readable gap schema not supplied."
      status: OPEN

    - id: L27-G002
      description:
        "Exact executed-validation contract not supplied."
      status: OPEN

    - id: L27-G003
      description:
        "Exact L27/L28 critical-gap interface not supplied."
      status: OPEN

    - id: L27-G004
      description:
        "Exact closure/reopening lifecycle not supplied."
      status: OPEN

    - id: L27-G005
      description:
        "Exact dependency invalidation mechanics not supplied."
      status: OPEN

    - id: L27-G006
      description:
        "Exact shard-local/global gap coordination semantics not supplied."
      status: OPEN
```

This registry is itself a model representation because the source does
not supply a canonical registry schema.

---

# 425. Final Gap Law

```text
WHEN SOMETHING
LOAD-BEARING
IS MISSING:

DO NOT FILL IT
WITH PLAUSIBILITY.

EXPOSE IT.

WHEN IMPLEMENTATION
IS MISSING:

SAY IMPLEMENTATION
IS NOT ESTABLISHED.

WHEN AUTHORITY
IS MISSING:

SAY AUTHORITY
IS NOT ESTABLISHED.

WHEN VALIDATION
IS MISSING:

SAY VALIDATION
IS NOT ESTABLISHED.

WHEN PROVENANCE
IS MISSING:

SAY PROVENANCE
IS NOT ESTABLISHED.

UNKNOWN
IS NOT FALSE.

UNKNOWN
IS NOT TRUE.

UNKNOWN/GAP
IS A VALID
EPISTEMIC RESULT.

A GAP
IS NOT SHAME.

A GAP
IS INFORMATION
ABOUT THE BOUNDARY
OF WHAT IS KNOWN.

EVERY ARTIFACT
MUST EXPOSE
ITS OWN
LOAD-BEARING GAPS.

DO NOT LET
A LOCAL GAP
BECOME
UNBOUNDED GLOBAL DOUBT.

DO NOT LET
A GLOBAL GAP
MASQUERADE
AS LOCAL.

TRACK
WHAT THE GAP AFFECTS.

TRACK
WHAT WOULD CLOSE IT.

WHEN CLOSING:

BRING NEW EVIDENCE.

EXECUTE
THE RELEVANT
VALIDATION.

MATCH
THE EVIDENCE
TO THE GAP.

MATCH
THE SCOPE.

MATCH
THE REGIME.

MATCH
THE VERSION.

CHECK
THE PROVENANCE
WHEN MATERIAL.

DO NOT CLOSE
AN IMPLEMENTATION GAP
WITH AN [[ARCHITECTURE]].

DO NOT CLOSE
A VALIDATION GAP
WITH DOCUMENTATION.

DO NOT CLOSE
AN EMPIRICAL GAP
WITH SIMULATION
WITHOUT A VALID BRIDGE.

DO NOT CLOSE
A CAUSAL GAP
WITH CORRELATION.

DO NOT CLOSE
AN INDEPENDENCE GAP
WITH DESCENDANT MULTIPLICATION.

DO NOT CLOSE
ANY GAP
WITH RESTATEMENT.

MORE WORDS
ARE NOT
MORE EVIDENCE.

MORE DETAIL
IS NOT
MORE VALIDATION.

MORE COPIES
ARE NOT
MORE INDEPENDENCE.

A CLOSED GAP
MAY REOPEN
WHEN ITS
LOAD-BEARING SUPPORT
FAILS.

INVALIDATE
ONLY DEPENDENTS.

PRESERVE
UNAFFECTED WORK.

PRESERVE
THE HISTORICAL FACT
THAT THE GAP EXISTED.

WHEN A CRITICAL GAP
CANNOT BE CLOSED:

STATE THE
MINIMUM MISSING
INFORMATION.

RETURN
UNKNOWN/GAP
WHEN THAT IS
THE TRUE STATE.

INTEGRITY
IS MORE IMPORTANT
THAN APPEARING COMPLETE.
```

---

# 426. Final Integrity Invariant

Normalized model:

$$
\boxed{
GapIntegrity
=
Visibility
\land
Boundedness
\land
DependencyAwareness
\land
EvidenceBasedClosure
}
$$

with:

$$
\boxed{
MissingEvidence
\not\Rightarrow
PlausibleCompletion
}
$$

and:

$$
\boxed{
GapClosure
\Rightarrow
ExecutedValidation
}
$$

where executed validation is the evidence contract explicitly required
by GAP-4.

These equations are normalized representations of the source laws, not
source-supplied formal equations.

---

# 427. Final Anti-Fabrication Invariant

```text
NO AMOUNT OF
PLAUSIBILITY,
FLUENCY,
STRUCTURAL COMPLETENESS,
ARCHITECTURAL DETAIL,
REPETITION,
OR FORMATTING

MAY CONVERT

MISSING EVIDENCE

INTO

ESTABLISHED FACT.
```

---

# 428. Final Closure Invariant

```text
A GAP MAY CHANGE
FROM OPEN
TO CLOSED

ONLY WHEN
THE EPISTEMIC BASIS
CHANGES.

RESTATEMENT
DOES NOT CHANGE
THE EPISTEMIC BASIS.

EXECUTED,
RELEVANT,
SCOPE-CORRECT
VALIDATION CAN.
```

The detailed qualifiers beyond "executed validation" are derived
integrity extensions.

---

# 429. Final Canon Boundary

> [!important]
> **Source-supported L27 boundary**
>
> The supplied source establishes **L27 Gap Law** as a
> `PROPOSED_SPECIFICATION`, with epistemic class `AMOS_MODEL`,
> canonical status `CONDITIONAL`, updated `2026-08-26`.
>
> It directly establishes four laws:
>
> **GAP-1 — Expose Don't Fill**
> Missing implementation, authority, validation, or provenance remains
> visible. Plausible architecture does not fill the gap.
>
> **GAP-2 — Gap Is Status Not Shame**
> `UNKNOWN/GAP` is an honest, first-class epistemic output.
>
> **GAP-3 — Bounded Gap Registry**
> Every artifact lists its own load-bearing gaps through its proof
> capsule context.
>
> **GAP-4 — Gap Closure Requires Evidence**
> Closing a gap requires executed validation rather than restatement.
>
> The supplied source directly establishes one falsifier:
>
> **F1 — authoritative canon treats gaps as failures to hide.**
>
> The source does **not** establish the exact gap schema, lifecycle,
> severity taxonomy, closure receipt, validation API, dependency
> invalidation algorithm, shard-local protocol, CAS mechanics, causal
> epoch mechanics, critical-gap semantics, or literal runtime
> implementation.
>
> Those remain `MODEL`, `DERIVED`, or `UNKNOWN/GAP` unless separately
> established.
>
> In particular, the exact semantics of  must not be
> invented from its title or relationship alone.

---

# 430. Canonical Summary

```yaml
L27_GAP:

  status:
    specification: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL
    updated: 2026-08-26

  laws:

    GAP-1:
      name: Expose Don't Fill
      invariant:
        "Missing evidence stays visible."

    GAP-2:
      name: Gap Is Status Not Shame
      invariant:
        "UNKNOWN/GAP is a valid first-class epistemic result."

    GAP-3:
      name: Bounded Gap Registry
      invariant:
        "Artifacts expose their own load-bearing gaps."

    GAP-4:
      name: Gap Closure Requires Evidence
      invariant:
        "Gap closure requires executed validation, not restatement."

  core_firewalls:

    - "PLAUSIBLE != ESTABLISHED"
    - "UNKNOWN != FALSE"
    - "UNKNOWN != TRUE"
    - "RESTATEMENT != VALIDATION"
    - "DOCUMENTATION != EXECUTION"
    - "MODEL != IMPLEMENTATION"
    - "SIMULATION != EMPIRICAL VALIDATION"
    - "CORRELATION != CAUSATION"
    - "DESCENDANT MULTIPLICITY != INDEPENDENCE"
    - "MORE PROSE != MORE EVIDENCE"

  source_falsifier:
    F1:
      "Authoritative canon treats gaps as failures to hide."

  final_rule:
    "EXPOSE. BOUND. REGISTER. VALIDATE. CLOSE ONLY WITH EVIDENCE."
```

---

# 431. Final Status

```text
L27 GAP LAW

SOURCE STATE:
SOURCE_CLAIM

EPISTEMIC CLASS:
AMOS_MODEL

CANONICAL STATUS:
CONDITIONAL

SPECIFICATION STATUS:
PROPOSED_SPECIFICATION

DIRECT SOURCE LAWS:
GAP-1
GAP-2
GAP-3
GAP-4

PRIMARY SOURCE FALSIFIER:
F1

EXPANDED MECHANICS:
DERIVED / MODEL

UNRESOLVED IMPLEMENTATION DETAILS:
UNKNOWN/GAP
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[L25_SHARD_LOCAL]] · [[L28_CRITICAL_GAP]] · [[L10_FAILURE_RECOVERY]] · [[L17_RSCF]] · [[FAIL_CLOSED_GOVERNANCE]]

---

RSCF-NODE
node_id: l27_gap
node_type: note
path: 01_CANON/01_CORE_LAWS/L27_GAP.md

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]
* INDEXED_BY: [[AMOS_RSCF_NODES]]
* CHILD_OF: [[LAW_HIERARCHY]]

claim_class: AMOS_MODEL

---

**MOC:** [[01_CORE_LAWS_MOC]]

---

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```
