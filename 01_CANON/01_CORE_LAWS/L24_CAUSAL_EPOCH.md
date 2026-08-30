---
title: L24 — Causal Epoch Law
type: law
source: 01_CANON/01_CORE_LAWS
tags:
- canon
- core_law
- causal_epoch
- causal_time
- monotonicity
- epoch_boundary
- causal_lineage
- causal_lineage_closure
- verdict_immutability
- explicit_supersession
- witness_receipts
- fail_closed
- replayability
- provenance
- time
- canon/universe
- law/L8-execution
- law/L22-replayability
rscf:
  state: CANON_LAW
  claim_class: CANONICAL_INVARIANT
  provenance: AMOS_CANON
  scope: core_laws
  node_id: l24_causal_epoch
  node_type: core_law
---

# L24 — Causal Epoch Law

**VERSION:** 2.0.0\
**STATUS:** CANON_LAW\
**claim_class:** CANONICAL_INVARIANT\
**provenance:** AMOS_CANON

---

# 0. Canonical Status

L24 establishes the canonical AMOS law governing:

- strict monotonicity of causal epochs,
- prohibition of silent historical verdict rewriting,
- explicit epoch-based supersession,
- causal lineage closure,
- cross-epoch witness requirements,
- and fail-closed handling of unlinked consequences.

The source establishes three invariant equations and two enforcement requirements.

Canonical compression:

```text
CAUSAL TIME
MOVES FORWARD.

VERDICTS ARE NOT
SILENTLY REWRITTEN.

SUPERSESSION REQUIRES
AN EXPLICIT LATER EPOCH.

CONSEQUENCES REQUIRE
CAUSAL ANCESTRY.

CROSS-EPOCH CHAINS
REQUIRE WITNESS RECEIPTS.

UNLINKED CONSEQUENCES
FAIL CLOSED.
```

---

# 1. Governing Objective

L24 asks:

```text
WHAT EPOCH
DOES THIS STATE,
CLAIM, VERDICT,
CAUSE, OR CONSEQUENCE
BELONG TO?

IS THE NEXT EPOCH
STRICTLY LATER?

IS AN EARLIER VERDICT
BEING SILENTLY CHANGED?

IF IT IS SUPERSEDED,
IS THERE AN EXPLICIT
LATER EPOCH?

DOES EACH CONSEQUENCE
HAVE A CAUSAL PREDECESSOR?

IF THE CAUSAL CHAIN
CROSSES AN EPOCH
BOUNDARY, IS THE
REQUIRED SIGNED
WITNESS RECEIPT PRESENT?

IF CAUSAL LINEAGE
IS MISSING,
HAS EXECUTION
FAILED CLOSED?
```

---

# 2. Canonical Invariants

The supplied source establishes three canonical invariants.

## CE-1 — Strict Monotonicity

$$
e_{k+1} > e_k
\qquad
\forall k \in \mathbb{N}
$$

Meaning:

```text
NEXT CAUSAL EPOCH
MUST BE
STRICTLY GREATER
THAN THE PRIOR EPOCH.
```

---

## CE-2 — No Time Travel

$$
\operatorname{Verdicts}(e_k)
\text{ cannot be silently rewritten.}
$$

Supersession requires an explicit transition:

$$
e_k \rightarrow e_{k+1}
$$

with:

$$
e_{k+1} > e_k
$$

Meaning:

```text
OLD VERDICT
      │
      ▼
CANNOT BE
SILENTLY MUTATED
      │
      ▼
NEW EVIDENCE /
NEW VERDICT
      │
      ▼
EXPLICIT LATER
EPOCH REQUIRED
```

---

## CE-3 — Causal Lineage Closure

For every consequence \(C\):

$$
\forall C,\;
\exists A:
\operatorname{Cause}(A)
\land
\operatorname{Epoch}(A)
\le
\operatorname{Epoch}(C)
$$

Canonical meaning:

```text
CONSEQUENCE C
      │
      ▼
MUST HAVE
CAUSAL ANCESTRY A
      │
      ▼
Epoch(A)
≤
Epoch(C)
```

A consequence cannot be causally grounded in a later epoch.

---

# 3. Strict Monotonicity Law

The first invariant establishes an ordered causal progression:

```text
e0 < e1 < e2 < e3 < ... < en
```

A valid epoch transition therefore has the form:

```text
e_k
 │
 ▼
e_{k+1}

WHERE:

e_{k+1} > e_k
```

Invalid:

```text
e5 → e5
```

and:

```text
e5 → e4
```

as transitions to the next causal epoch.

---

# 4. Strict Means Strict

The source uses:

$$
>
$$

rather than:

$$
\ge
$$

Therefore:

```text
NEXT EPOCH
≠
CURRENT EPOCH
```

and:

```text
NEXT EPOCH
CANNOT BE EARLIER
THAN CURRENT EPOCH.
```

---

# 5. Epoch Identity

The source establishes ordered epochs \(e_k\), but does not specify their physical representation.

It does **not** establish whether an epoch identifier is:

- an integer,
- logical clock,
- timestamp,
- Lamport clock,
- vector-clock component,
- transaction identifier,
- cryptographic sequence,
- consensus round,
- causal generation,
- or another encoding.

Therefore:

```text
ORDERING SEMANTICS
=
CANONICAL

PHYSICAL ENCODING
=
UNKNOWN / IMPLEMENTATION-DEPENDENT
```

---

# 6. Causal Time ≠ Wall-Clock Time

L24 establishes:

```text
CAUSAL EPOCH ORDER
```

It does not establish equivalence with:

```text
WALL-CLOCK TIME
```

Therefore:

```text
CAUSAL TIME
≠
PHYSICAL CLOCK TIME
```

unless another canonical source explicitly binds them.

---

# 7. Epoch Order ≠ Timestamp Order

Do not infer:

```text
TIMESTAMP(A)
<
TIMESTAMP(B)
      ↓
Epoch(A)
<
Epoch(B)
```

from L24 alone.

The canonical law concerns causal epochs, not a specified timestamp implementation.

---

# 8. Monotonicity ≠ Fixed Increment

The equation requires:

$$
e_{k+1} > e_k
$$

It does not require:

$$
e_{k+1} = e_k + 1
$$

Therefore:

```text
STRICTLY INCREASING
≠
UNIT INCREMENT
```

---

# 9. Monotonicity ≠ Continuity

Nothing in the supplied source requires every mathematically possible epoch value to exist.

Thus:

```text
e1 → e5
```

is not ruled out solely by the strict monotonicity equation if the epoch representation permits it.

Whether skipped epochs are valid is unspecified.

---

# 10. Monotonicity ≠ Total Physical Serialization

L24 establishes strict ordering of the epoch sequence.

It does not by itself prove that every physical operation across every AMOS implementation must be globally serialized through one clock.

Therefore:

```text
CAUSAL EPOCH MONOTONICITY
≠
PROOF OF A SINGLE
GLOBAL PHYSICAL CLOCK
```

---

# 11. Epoch Boundary

An epoch boundary exists between:

```text
e_k
 │
 │ BOUNDARY
 ▼
e_{k+1}
```

where:

$$
e_{k+1} > e_k
$$

Crossing this boundary becomes especially important for:

- supersession,
- causal lineage,
- and witness enforcement.

---

# 12. Epoch Transition

Canonical transition:

```text
STATE / VERDICT @ e_k
        │
        ▼
EXPLICIT TRANSITION
        │
        ▼
STATE / VERDICT @ e_{k+1}
```

with:

```text
e_{k+1} > e_k
```

---

# 13. No Time Travel Law

The second canonical invariant states that verdicts at \(e_k\):

```text
cannot be silently rewritten
```

This protects historical epistemic state.

If AMOS reached:

```text
VERDICT V1 @ e7
```

then later information cannot make the canonical history pretend that:

```text
V2 @ e7
```

was always the verdict.

Instead:

```text
V1 @ e7
   │
   ▼
EXPLICIT SUPERSESSION
   │
   ▼
V2 @ e8
```

is required.

---

# 14. Historical Verdict Preservation

Canonical pattern:

```text
e7:
VERDICT = V1

e8:
NEW EVIDENCE
    │
    ▼
VERDICT = V2
SUPERSEDES V1
```

History preserves both states.

Incorrect pattern:

```text
e7:
VERDICT = V2
```

with V1 silently erased.

---

# 15. Supersession

The source explicitly establishes:

```text
supersession requires
explicit epoch transition
e_{k+1}
```

Therefore supersession has at least two canonical properties:

```text
EXPLICIT
```

and:

```text
LATER EPOCH
```

---

# 16. Supersession ≠ Deletion

The source says an earlier verdict cannot be silently rewritten.

Therefore the safest canonical interpretation is:

```text
OLD VERDICT
REMAINS HISTORICALLY
IDENTIFIABLE
```

while:

```text
NEW VERDICT
BECOMES THE LATER
SUPERSEDING STATE
```

The exact storage mechanism is not specified.

---

# 17. Supersession ≠ Contradiction Erasure

Suppose:

```text
V1 @ e5

V2 @ e6
```

and V2 contradicts V1.

L24 does not authorize rewriting e5 to remove the contradiction.

Instead:

```text
V1 @ e5
   │
   ▼
SUPERSEDED BY
   │
   ▼
V2 @ e6
```

preserves lineage.

---

# 18. New Evidence Does Not Rewrite Old Epistemic State

A later observation can change what AMOS concludes now.

It cannot silently change what AMOS concluded then.

Thus:

```text
LATER EVIDENCE
CAN CHANGE
CURRENT VERDICT
```

but:

```text
LATER EVIDENCE
CANNOT SILENTLY CHANGE
HISTORICAL VERDICT
```

---

# 19. Correction vs Rewrite

A correction is compatible with L24 when represented as:

```text
V1 @ e_k
      │
      ▼
CORRECTION EVENT
      │
      ▼
V2 @ e_{k+1}
```

A silent rewrite:

```text
V1 @ e_k
      ↓
replace in place
      ↓
V2 @ e_k
```

violates the stated no-time-travel invariant.

---

# 20. Explicit Transition Requirement

The source does not define the exact representation of an explicit transition.

Potential implementations might include:

- transition records,
- provenance edges,
- version records,
- signed receipts,
- event logs,
- RSCF lineage,
- or other structures.

Only the requirement for explicit epoch transition is canonical here.

---

# 21. Historical Immutability Boundary

L24 establishes a semantic immutability property:

```text
HISTORICAL VERDICT
CANNOT BE
SILENTLY REWRITTEN
```

This does not necessarily mean underlying storage bytes are physically immutable.

Therefore:

```text
SEMANTIC IMMUTABILITY
≠
PHYSICAL WRITE-ONCE STORAGE
```

---

# 22. No Time Travel ≠ No Revision

L24 does not prohibit revision.

It governs **how** revision occurs.

Correct:

```text
REVISE
BY SUPERSESSION
IN A LATER EPOCH
```

Incorrect:

```text
REVISE
BY SILENTLY ALTERING
THE EARLIER EPOCH
```

---

# 23. Causal Lineage Closure

The third canonical invariant requires every consequence to possess causal ancestry.

Source equation:

$$
\forall \operatorname{Consequence}(C),
\;
\exists \operatorname{Cause}(A)
\land
\operatorname{Epoch}(A)
\le
\operatorname{Epoch}(C)
$$

This establishes:

```text
NO CONSEQUENCE
WITHOUT A CAUSAL LINK
```

within the canonical model.

---

# 24. Cause Cannot Come From the Future

Because:

$$
Epoch(A) \le Epoch(C)
$$

the cause can occur:

```text
IN THE SAME EPOCH
```

or:

```text
IN AN EARLIER EPOCH
```

but not:

```text
IN A LATER EPOCH
```

relative to its consequence.

---

# 25. Same-Epoch Causation

The equation uses:

$$
\le
$$

rather than:

$$
<
$$

Therefore L24 permits, at the equation level:

```text
Epoch(A)
=
Epoch(C)
```

for a cause and consequence.

This is distinct from epoch-transition monotonicity.

---

# 26. Epoch Transition vs Cause Ordering

Two separate relations must not be collapsed.

For consecutive epochs:

$$
e_{k+1} > e_k
$$

For a cause and consequence:

$$
Epoch(A) \le Epoch(C)
$$

Thus:

```text
NEXT EPOCH
MUST BE STRICTLY LATER
```

while:

```text
CAUSE
MAY OCCUR IN
THE SAME EPOCH
AS ITS CONSEQUENCE
```

according to the supplied equations.

---

# 27. Causal Lineage

Minimal canonical form:

```text
CAUSE A
   │
   ▼
CONSEQUENCE C
```

with:

```text
Epoch(A)
≤
Epoch(C)
```

---

# 28. Multi-Step Causal Lineage

Conceptually:

```text
A @ e1
 │
 ▼
B @ e2
 │
 ▼
C @ e3
```

Each consequence requires an admissible causal predecessor.

---

# 29. Causal Lineage Closure ≠ Unique Cause

The equation states:

$$
\exists Cause(A)
$$

It does not state:

$$
\exists! Cause(A)
$$

Therefore:

```text
A CONSEQUENCE
MAY HAVE
MULTIPLE CAUSES
```

unless another canonical law imposes uniqueness.

---

# 30. Causal Lineage Closure ≠ Sufficient Cause

The existence of a causal predecessor does not establish that the predecessor is:

- sufficient,
- necessary,
- exclusive,
- dominant,
- or the sole mechanism.

L24 establishes lineage existence and temporal admissibility, not the full causal type.

---

# 31. Causal Firewall

L24 must not be used to infer causation merely because:

```text
A OCCURRED
BEFORE C
```

Temporal admissibility is necessary for the lineage relation expressed here, but temporal order alone does not prove causal effect.

Therefore:

```text
EARLIER
≠
CAUSE
```

and:

```text
SAME / EARLIER EPOCH
≠
PROOF OF CAUSATION
```

---

# 32. Structural Lineage ≠ Empirical Causation

An AMOS causal-lineage edge can represent a model or execution dependency.

It does not automatically prove a real-world causal relationship.

Thus:

```text
AMOS CAUSAL LINEAGE
≠
EMPIRICALLY VERIFIED
CAUSAL EFFECT
```

unless independently validated.

---

# 33. Cross-Epoch Causal Chain

Example:

```text
A @ e4
 │
 │ epoch boundary
 ▼
B @ e5
```

This is a causal chain crossing an epoch boundary.

The source explicitly requires such chains to carry:

```text
SIGNED WITNESS RECEIPTS
```

---

# 34. Signed Witness Receipt Requirement

Canonical enforcement:

> Causal chains crossing epoch boundaries require signed witness receipts.

Thus:

```text
CAUSE @ e_k
     │
     ▼
EPOCH BOUNDARY
     │
     ▼
CONSEQUENCE @ e_{k+1}
```

requires:

```text
SIGNED
WITNESS RECEIPT
```

---

# 35. Witness Receipt Scope

The source establishes the existence requirement.

It does **not** specify:

- receipt schema,
- signer identity,
- signature algorithm,
- key management,
- trust root,
- threshold signatures,
- quorum requirements,
- receipt expiry,
- verification protocol,
- storage format,
- or revocation.

Those remain unspecified.

---

# 36. Signed ≠ Trusted Automatically

A signature can establish some form of binding to a signing identity under an appropriate cryptographic system.

But L24 does not define that system.

Therefore:

```text
SIGNED
≠
AUTOMATICALLY TRUSTED
```

without valid signer authority and verification semantics.

---

# 37. Witness ≠ Independent Witness

The source says:

```text
signed witness receipts
```

It does not establish that witnesses must be provenance-independent.

Therefore:

```text
MULTIPLE RECEIPTS
≠
MULTIPLE INDEPENDENT
WITNESSES
```

unless provenance independence is separately demonstrated.

---

# 38. Witness Receipt ≠ Proof of Empirical Causation

A receipt can attest to a causal-chain transition under AMOS semantics.

It does not by itself prove that the modeled causal relationship is empirically true in the external world.

---

# 39. Witness Receipt Function

At minimum, the canonical enforcement role is:

```text
CROSS-EPOCH
CAUSAL LINK
      │
      ▼
WITNESS RECEIPT
REQUIRED
```

Anything beyond that is implementation detail unless established elsewhere.

---

# 40. Unlinked Consequence

An unlinked consequence is a consequence for which required causal ancestry is absent.

Conceptually:

```text
?
│
▼
CONSEQUENCE C
```

rather than:

```text
CAUSE A
│
▼
CONSEQUENCE C
```

---

# 41. Fail-Closed Enforcement

The source explicitly establishes:

> Unlinked consequences trigger fail-closed execution halts.

Therefore:

```text
CONSEQUENCE
      │
      ▼
CAUSAL LINK?
   ┌──┴──┐
   │     │
  YES    NO
   │     │
   ▼     ▼
CONTINUE FAIL-CLOSED
         EXECUTION
         HALT
```

---

# 42. Fail-Closed ≠ Best-Effort Continuation

Invalid under the explicit enforcement rule:

```text
CAUSAL LINK
MISSING
    │
    ▼
CONTINUE ANYWAY
```

Canonical:

```text
CAUSAL LINK
MISSING
    │
    ▼
HALT
```

---

# 43. Fail-Closed Scope

The source says:

```text
execution halts
```

but does not define whether the halt is:

- local to a reasoning branch,
- local to an RSCF,
- transaction-local,
- shard-local,
- workflow-wide,
- process-wide,
- or system-wide.

Therefore the **halt requirement** is canonical, while the exact halt scope remains unspecified.

---

# 44. Missing Receipt vs Missing Causal Link

The source separately states:

```text
CROSS-EPOCH CHAIN
→
SIGNED WITNESS RECEIPT REQUIRED
```

and:

```text
UNLINKED CONSEQUENCE
→
FAIL-CLOSED HALT
```

It does not explicitly state whether a causal link with a missing required witness receipt is formally classified as an “unlinked consequence.”

The safest interpretation is:

```text
CROSS-EPOCH LINK
WITHOUT REQUIRED RECEIPT
=
ENFORCEMENT FAILURE
```

but the exact error taxonomy remains unspecified.

---

# 45. Canonical Enforcement Flow

```text
CAUSE / PRIOR STATE
        │
        ▼
CONSEQUENCE PROPOSED
        │
        ▼
CAUSAL LINK EXISTS?
     ┌──┴──┐
     │     │
    NO    YES
     │     │
     ▼     ▼
FAIL-     EPOCH
CLOSED    BOUNDARY
HALT      CROSSED?
           ┌──┴──┐
           │     │
          NO    YES
           │     │
           ▼     ▼
        CONTINUE SIGNED
                 WITNESS
                 RECEIPT?
                  ┌──┴──┐
                  │     │
                 YES    NO
                  │     │
                  ▼     ▼
               CONTINUE ENFORCEMENT
                        FAILURE
```

The precise response to a missing receipt beyond non-compliance is not explicitly defined.

---

# 46. Verdict Evolution

Canonical verdict evolution:

```text
V1 @ e1
   │
   ▼
V2 @ e2
   │
   ▼
V3 @ e3
```

with:

```text
e1 < e2 < e3
```

Each later verdict can supersede an earlier verdict explicitly.

---

# 47. Verdict Lineage

Model-level representation:

```text
V1 @ e1
   │
   │ SUPERSEDED_BY
   ▼
V2 @ e2
```

The exact relation name is not source-defined.

---

# 48. Evidence Evolution

Suppose:

```text
EVIDENCE A @ e3
      │
      ▼
VERDICT V1 @ e3
```

Later:

```text
EVIDENCE B @ e4
      │
      ▼
VERDICT V2 @ e4
```

The new verdict does not rewrite V1.

Instead:

```text
V1 @ e3
   │
   ▼
SUPERSEDED
   │
   ▼
V2 @ e4
```

---

# 49. Contradiction Across Epochs

A later epoch can contradict an earlier verdict.

L24 requires the contradiction to remain historically visible through explicit transition rather than silent replacement.

Thus:

```text
V1 @ e5
CONTRADICTED BY
V2 @ e6
```

is representable without destroying V1's historical state.

---

# 50. Competing Hypotheses Across Epochs

Suppose:

```text
H1 @ e7
H2 @ e7
```

remain COMPETING.

Later discriminating evidence at e8 may support H2.

Correct:

```text
e7:
H1 vs H2
=
COMPETING

e8:
NEW EVIDENCE
→
H2 SUPPORTED
```

Incorrect:

```text
rewrite e7
as though H2
had already won
```

---

# 51. Epochs Preserve Epistemic History

L24 therefore supports a distinction between:

```text
WHAT WAS JUSTIFIED THEN
```

and:

```text
WHAT IS JUSTIFIED NOW
```

without conflating them.

---

# 52. Historical Error Remains Historical

If a verdict at e5 was later discovered to be wrong:

```text
V_wrong @ e5
```

the canonical record should not pretend it never existed.

Instead:

```text
V_wrong @ e5
      │
      ▼
CORRECTED / SUPERSEDED
      │
      ▼
V_corrected @ e6
```

This preserves causal and epistemic lineage.

---

# 53. No Retroactive Confidence Inflation

Later evidence supporting an old claim does not justify silently increasing the confidence attached to the historical verdict at its original epoch.

Instead:

```text
CONFIDENCE C1 @ e4
       │
       ▼
NEW EVIDENCE @ e5
       │
       ▼
CONFIDENCE C2 @ e5
```

as a model-level consequence of the no-silent-rewrite law.

---

# 54. No Retroactive Confidence Deflation

Likewise, later disconfirmation does not silently alter the historical confidence state.

Historical and current evaluations remain distinguishable.

---

# 55. Epoch-Scoped Proof Capsule

A model-level Proof Capsule may carry:

```yaml
proof_capsule:
  claim: C1
  epoch: e7
  premises:
    - P1
    - P2
  conclusion: V1
```

A later capsule:

```yaml
proof_capsule:
  claim: C1
  epoch: e8
  supersedes:
    - prior_capsule
  conclusion: V2
```

This representation is consistent with L24 but is not explicitly specified by the supplied source.

---

# 56. Proof Capsule Reuse Across Epochs

A Proof Capsule from an earlier epoch should not automatically be assumed valid in a later epoch.

Its dependencies may have changed.

Therefore model-level reuse requires checking:

```text
DEPENDENCIES
SCOPE
REGIME
FRESHNESS
SUPERSESSION
```

This follows broader AMOS proof-capsule discipline rather than the minimal L24 source alone.

---

# 57. RSCF Epoch Binding

An RSCF node can conceptually carry:

```yaml
rscf:
  node_id: N1
  epoch: e5
```

A later replacement can carry:

```yaml
rscf:
  node_id: N2
  epoch: e6
  supersedes:
    - N1
```

Exact serialization is model-level.

---

# 58. RSCF Historical Preservation

Under L24:

```text
RSCF@e5
```

should not be silently mutated into:

```text
RSCF@e6
```

while pretending it remained the same historical state.

Explicit lineage preserves the transition.

---

# 59. Causal Dependency Graph

```text
A @ e1
│
├────→ B @ e1
│
└────→ C @ e2
          │
          ▼
        D @ e3
```

Requirements:

```text
Epoch(A) ≤ Epoch(B)
Epoch(A) ≤ Epoch(C)
Epoch(C) ≤ Epoch(D)
```

Cross-epoch causal edges require signed witness receipts.

---

# 60. Invalid Future-Cause Graph

Invalid under the lineage equation:

```text
A @ e8
   │
   ▼
C @ e7
```

if A is asserted as the cause of C.

Because:

$$
8 \nleq 7
$$

---

# 61. Unlinked Graph

Invalid execution condition:

```text
        C @ e7
```

with no required cause link.

Canonical response:

```text
FAIL CLOSED
```

---

# 62. Cross-Epoch Witness Graph

```text
A @ e4
   │
   │ SIGNED
   │ WITNESS
   │ RECEIPT
   ▼
B @ e5
```

The receipt requirement is canonical.

Its cryptographic mechanics are not specified.

---

# 63. Multiple Cross-Epoch Edges

Conceptually:

```text
A @ e1
 │
 ▼
B @ e2
 │
 ▼
C @ e3
```

Each causal chain crossing epoch boundaries falls under the witness-receipt requirement.

Whether one receipt can cover multiple edges or an entire chain is not specified.

---

# 64. Epoch Jump

Suppose:

```text
A @ e2
 │
 ▼
B @ e7
```

The source still treats this as crossing epoch boundaries.

The exact number or structure of required receipts is unspecified.

---

# 65. Witness Granularity Gap

L24 does not establish whether witness receipts bind:

- individual causal edges,
- entire chains,
- epoch transitions,
- transactions,
- verdict transitions,
- RSCF groups,
- or another unit.

This is a decision-relevant implementation gap.

---

# 66. Signed Witness Identity Gap

L24 does not define:

```text
WHO SIGNS?
```

Possible answers cannot be invented from the supplied source.

Therefore:

```text
SIGNER AUTHORITY
=
UNKNOWN/GAP
```

---

# 67. Witness Trust Gap

Likewise:

```text
WHAT MAKES A
WITNESS TRUSTED?
```

is not answered by this note.

The signature requirement alone does not define trust semantics.

---

# 68. Witness Freshness Gap

The source does not define:

- receipt lifetime,
- expiry,
- revocation,
- epoch validity,
- or replay prevention.

These require additional canon.

---

# 69. Replayability

L24 explicitly relates to:

```text

```

The supplied note does not define that law's content.

However, causal epoch history naturally provides ordering information relevant to replay.

Do not import additional L22 semantics without retrieving that canon.

---

# 70. Execution

L24 explicitly relates to:

```text

```

and directly establishes one execution rule:

```text
UNLINKED CONSEQUENCE
→
FAIL-CLOSED EXECUTION HALT
```

Additional L8 semantics require the actual L8 source.

---

# 71. Replay ≠ Rewrite

A replay of historical execution should conceptually distinguish:

```text
REPRODUCE
HISTORICAL STATE
```

from:

```text
REWRITE
HISTORICAL STATE
```

L24 prohibits the latter when it silently changes prior verdicts.

---

# 72. Replay and Epoch Identity

A replay system may need to know which epoch a historical verdict belonged to.

But exact replay mechanics are not specified by L24.

---

# 73. L24 and MVCC/CAS

The broader AMOS lineage includes MVCC/CAS concepts.

Conceptually:

```text
VERSION / EXPECTED STATE
```

and:

```text
CAUSAL EPOCH
```

are related but not identical.

Therefore:

```text
VERSION
≠
EPOCH
```

unless authoritative canon explicitly binds them.

---

# 74. Version Monotonicity ≠ Epoch Monotonicity

A storage version may increase for implementation reasons without representing a new causal epoch.

Likewise, an epoch transition may conceptually encompass multiple storage mutations.

L24 alone does not define their mapping.

---

# 75. L24 and Atomic Multi-RSCF Reasoning

Suppose a conclusion depends on:

```text
RSCF A @ e5
+
RSCF B @ e5
```

and is committed at:

```text
e6
```

the causal dependencies must not point backward from future premises.

Exact atomic commit semantics are defined elsewhere, not by L24 alone.

---

# 76. L24 and Shard Locality

Shard identity and causal epoch are separate axes:

```text
STATE
=
SHARD S
+
EPOCH e
```

conceptually.

Therefore:

```text
SAME SHARD
≠
SAME EPOCH
```

and:

```text
SAME EPOCH
≠
SAME SHARD
```

---

# 77. Cross-Shard ≠ Cross-Epoch

Example:

```text
S1 @ e5
↔
S2 @ e5
```

is cross-shard but not necessarily cross-epoch.

Example:

```text
S1 @ e5
→
S1 @ e6
```

is cross-epoch but not cross-shard.

---

# 78. Cross-Shard Cross-Epoch Chain

Both dimensions can coexist:

```text
A @ S1/e5
    │
    ▼
B @ S2/e6
```

This is both:

```text
CROSS-SHARD
```

and:

```text
CROSS-EPOCH
```

The cross-epoch witness requirement applies under L24.

Any shard coordination requirement depends on the relevant distribution canon.

---

# 79. L24 and L25

L24 governs:

```text
CAUSAL TIME
EPOCH BOUNDARIES
HISTORICAL VERDICTS
CAUSAL LINEAGE
CROSS-EPOCH WITNESSES
```

L25 governs, under its supplied proposed specification:

```text
SHARD LOCALITY
LOCAL/GLOBAL FACTS
CROSS-SHARD INVARIANTS
BOUNDARY CONTRACTS
MERGE DISCIPLINE
```

They should remain orthogonal unless a dependency requires composition.

---

# 80. Causal Epoch Finality

The broader AMOS evolution spine references:

```text
CAUSAL EPOCH FINALITY
```

The supplied L24 v2.0.0 establishes strict monotonicity and no silent rewriting, but does not explicitly define a complete finality protocol.

Therefore:

```text
L24
SUPPORTS HISTORICAL
NON-REWRITE SEMANTICS
```

but:

```text
L24 SOURCE ALONE
≠
COMPLETE FORMAL
FINALITY PROTOCOL
```

---

# 81. Finality ≠ Impossibility of Supersession

The law explicitly allows supersession through a later epoch.

Therefore:

```text
HISTORICAL FINALITY
```

must not be interpreted as:

```text
NO FUTURE VERDICT
CAN DIFFER
```

The invariant is instead against silent rewriting of the earlier verdict.

---

# 82. L24 and Persistent Provenance

Persistent provenance is naturally compatible with L24 because it can preserve:

```text
CAUSE
CONSEQUENCE
EPOCH
SUPERSESSION
WITNESS
```

But the supplied source does not prescribe a provenance storage architecture.

---

# 83. L24 and Provenance Topology

A consequence may have multiple causal ancestors:

```text
A ─┐
   ├→ C
B ─┘
```

The existence of multiple ancestors does not establish provenance independence.

Therefore:

```text
MULTIPLE CAUSAL EDGES
≠
INDEPENDENT EVIDENCE
```

---

# 84. L24 and Sybil Hardening

Multiple witness receipts derived from the same controlling origin do not automatically constitute independent validation.

This follows broader AMOS provenance discipline, not the minimal L24 source.

---

# 85. L24 and Epistemic Regimes

Epoch and epistemic regime are separate concepts.

```text
EPOCH
=
CAUSAL-TIME POSITION
```

while:

```text
REGIME
=
VALIDITY / ENVIRONMENT
CONTEXT
```

under broader AMOS terminology.

Therefore:

```text
NEW EPOCH
≠
NEW REGIME
```

and:

```text
NEW REGIME
≠
NEW EPOCH
```

unless a specific transition binds them.

---

# 86. Regime Change Across Epochs

A regime transition may coincide with:

```text
e_k → e_{k+1}
```

but L24 does not require every epoch transition to represent a regime shift.

---

# 87. L24 and Scope

A verdict at epoch e5 may be valid only within scope S1.

Moving to e6 does not automatically broaden that scope.

Therefore:

```text
LATER EPOCH
≠
BROADER APPLICABILITY
```

---

# 88. L24 and Freshness

An old verdict can remain historically valid as a record of what was concluded at e3 while being stale for present decision-making.

Thus:

```text
HISTORICALLY PRESERVED
≠
CURRENTLY ACTIONABLE
```

---

# 89. L24 and Competing Hypotheses

L24 preserves the historical state of competing hypotheses.

Example:

```text
e5:
H1 = plausible
H2 = plausible
STATUS = COMPETING

e6:
new discriminating evidence

H1 = weakened
H2 = supported
```

The e5 state remains historically intact.

---

# 90. L24 and Selective Invalidation

The broader AMOS lineage supports selective dependent invalidation.

Suppose:

```text
P1 → C1 → C2
```

and at a later epoch P1 is invalidated.

The model-level recovery pattern is:

```text
INVALIDATE
C1 AND C2
```

while preserving unrelated conclusions.

This is compatible with L24 but not explicitly specified in the supplied source.

---

# 91. Invalidation ≠ Historical Deletion

Critical distinction:

```text
INVALIDATE FOR
CURRENT USE
```

does not mean:

```text
DELETE HISTORICAL
EXISTENCE
```

A conclusion can remain part of the historical causal record while no longer being valid for current reuse.

---

# 92. L24 and Failure Recovery

If an execution path fails because a causal link is missing:

```text
UNLINKED CONSEQUENCE
→
HALT
```

A corrected path should establish the missing lineage rather than pretending the original execution was valid.

---

# 93. L24 and Knowledge Harvest

Harvested knowledge may conceptually preserve:

```text
EPOCH OF ACQUISITION
EPOCH OF VALIDATION
SUPERSESSION HISTORY
CAUSAL DEPENDENCIES
```

where material.

This is a model-level integration.

---

# 94. L24 and Adaptive Complexity

For simple same-epoch reasoning, extensive epoch machinery may not need to be surfaced.

Escalation becomes material when:

- conclusions supersede earlier verdicts,
- causal chains cross epochs,
- historical replay matters,
- lineage is disputed,
- or consequences lack clear causes.

This is operational guidance, not a new canonical law.

---

# 95. Causal Epoch State Machine

```text
┌────────────────────┐
│ STATE / VERDICT Vk │
│      @ e_k         │
└─────────┬──────────┘
          │
          ▼
   CHANGE REQUIRED?
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
    KEEP   EXPLICIT
           TRANSITION
               │
               ▼
          e_{k+1} > e_k
               │
               ▼
       NEW STATE / VERDICT
               │
               ▼
        CAUSAL LINEAGE
           COMPLETE?
          ┌────┴────┐
          │         │
         NO        YES
          │         │
          ▼         ▼
       FAIL-      CROSS-EPOCH
       CLOSED      LINK?
       HALT        ┌──┴──┐
                   │     │
                  NO    YES
                   │     │
                   ▼     ▼
                 VALID  SIGNED
                        WITNESS
                        REQUIRED
```

---

# 96. Canonical Integrity Invariants

```yaml
causal_epoch_integrity_invariants:

  CE_I1_STRICT_MONOTONICITY:
    requirement:
      next_epoch_strictly_greater_than_prior_epoch

  CE_I2_NO_SILENT_REWRITE:
    requirement:
      historical_verdicts_not_silently_rewritten

  CE_I3_EXPLICIT_SUPERSESSION:
    requirement:
      supersession_requires_explicit_later_epoch_transition

  CE_I4_CAUSAL_LINEAGE_CLOSURE:
    requirement:
      every_consequence_has_causal_ancestry

  CE_I5_NO_FUTURE_CAUSE:
    requirement:
      cause_epoch_not_greater_than_consequence_epoch

  CE_I6_CROSS_EPOCH_WITNESS:
    requirement:
      causal_chains_crossing_epoch_boundaries_have_signed_witness_receipts

  CE_I7_FAIL_CLOSED_UNLINKED:
    requirement:
      unlinked_consequences_trigger_fail_closed_execution_halt
```

---

# 97. Extended Model Invariants

```yaml
extended_causal_epoch_invariants:

  CE_E1_EPOCH_NOT_WALL_CLOCK:
    requirement:
      causal_epoch_not_silently_equated_with_wall_clock_time

  CE_E2_EPOCH_NOT_VERSION:
    requirement:
      causal_epoch_not_silently_equated_with_storage_version

  CE_E3_EPOCH_NOT_REGIME:
    requirement:
      causal_epoch_not_silently_equated_with_epistemic_regime

  CE_E4_EPOCH_NOT_SHARD:
    requirement:
      causal_epoch_not_silently_equated_with_shard_identity

  CE_E5_EARLIER_NOT_CAUSE:
    requirement:
      temporal_precedence_alone_does_not_establish_causation

  CE_E6_LINEAGE_NOT_EMPIRICAL_PROOF:
    requirement:
      AMOS_lineage_edge_does_not_by_itself_prove_external_causal_effect

  CE_E7_SIGNED_NOT_TRUSTED:
    requirement:
      signature_presence_alone_does_not_establish_witness_authority

  CE_E8_MULTIPLE_WITNESSES_NOT_INDEPENDENT:
    requirement:
      witness_independence_requires_provenance_validation

  CE_E9_INVALIDATION_NOT_DELETION:
    requirement:
      later_invalidation_preserves_historical_record

  CE_E10_NO_RUNTIME_OVERCLAIM:
    requirement:
      L24_not_presented_as_proof_of_literal_distributed_epoch_runtime
```

These are interpretive/model protections, not additional source equations.

---

# 98. Anti-Patterns

## CE-A1 — Equal Next Epoch

```text
e_k → e_k
```

Rejected by strict monotonicity.

---

## CE-A2 — Backward Epoch

```text
e5 → e4
```

Rejected.

---

## CE-A3 — Silent Verdict Rewrite

```text
V1 @ e5
   ↓
replace
   ↓
V2 @ e5
```

Rejected.

---

## CE-A4 — Retroactive Historical Correction

```text
NEW EVIDENCE @ e8
      ↓
CHANGE WHAT
VERDICT@e5
WAS RECORDED AS
```

Rejected when done silently.

---

## CE-A5 — Supersession Without New Epoch

```text
V1 @ e5
→
V2 @ e5
```

Rejected.

---

## CE-A6 — Future Cause

```text
A @ e8
↓
C @ e7
```

Rejected by:

$$
Epoch(A) \le Epoch(C)
$$

---

## CE-A7 — Consequence Without Cause

```text
C
```

with no causal ancestry.

Triggers fail-closed enforcement.

---

## CE-A8 — Cross-Epoch Chain Without Required Receipt

```text
A @ e4
↓
B @ e5
```

without the required signed witness receipt.

Non-compliant with enforcement.

---

## CE-A9 — Timestamp Equals Epoch

```text
TIMESTAMP
=
CAUSAL EPOCH
```

Not established.

---

## CE-A10 — Earlier Means Cause

```text
A BEFORE B
↓
A CAUSED B
```

Rejected by causal firewall.

---

## CE-A11 — Signed Means Trusted

```text
SIGNED RECEIPT
↓
TRUSTED RECEIPT
```

Not established without signer/trust semantics.

---

## CE-A12 — Multiple Receipts Mean Independent Witnesses

```text
3 RECEIPTS
=
3 INDEPENDENT
SOURCES
```

Not established.

---

## CE-A13 — New Epoch Means New Regime

```text
e_k → e_{k+1}
↓
REGIME CHANGE
```

Not established.

---

## CE-A14 — New Epoch Means New Shard

```text
e_k → e_{k+1}
↓
SHARD CHANGE
```

Not established.

---

## CE-A15 — Epoch Equals Version

```text
VERSION 8
=
EPOCH 8
```

Not established.

---

## CE-A16 — Invalidation Deletes History

```text
VERDICT INVALIDATED
↓
REMOVE HISTORICAL
VERDICT
```

Rejected as incompatible with no-silent-rewrite semantics.

---

## CE-A17 — Finality Means Never Revisable

```text
FINAL
↓
NO FUTURE
SUPERSESSION
```

Not established by this source.

---

## CE-A18 — Causal Lineage Proves Real-World Causality

```text
AMOS EDGE
A → B
↓
A EMPIRICALLY
CAUSES B
```

Rejected without independently typed causal evidence.

---

# 99. Decision Matrix

| Condition                                            | Canonical treatment               |
| ---------------------------------------------------- | --------------------------------- |
| Proposed next epoch equals current epoch             | Reject                            |
| Proposed next epoch is earlier                       | Reject                            |
| Proposed next epoch is strictly later                | Satisfies CE-1 ordering condition |
| Earlier verdict silently modified                    | Reject                            |
| Earlier verdict explicitly superseded in later epoch | Compatible with CE-2              |
| Consequence has cause in same epoch                  | Permitted by CE-3 equation        |
| Consequence has cause in earlier epoch               | Permitted by CE-3 equation        |
| Asserted cause is in later epoch                     | Reject                            |
| Cross-epoch causal chain has signed witness receipt  | Meets stated witness requirement  |
| Cross-epoch chain lacks required receipt             | Enforcement non-compliance        |
| Consequence has no causal link                       | Fail-closed execution halt        |

---

# 100. Extended Decision Matrix

| Condition                                  | Treatment                                                    |
| ------------------------------------------ | ------------------------------------------------------------ |
| Wall-clock timestamp increases             | Does not alone establish epoch transition                    |
| Storage version increases                  | Does not alone establish epoch transition                    |
| New evidence contradicts old verdict       | Create explicit later-epoch supersession                     |
| Old conclusion becomes stale               | Preserve historical conclusion; re-evaluate current validity |
| Multiple causal predecessors exist         | Allowed unless other canon restricts                         |
| Multiple witness receipts share provenance | Do not treat as independent confirmation automatically       |
| Signed receipt signer is unknown           | Trust validity remains GAP                                   |
| Epoch encoding unspecified                 | Preserve semantic ordering without inventing representation  |
| Missing witness granularity rules          | Mark implementation GAP                                      |
| Replay requested                           | Preserve historical epoch/verdict distinctions               |
| Causal edge represents model dependency    | Do not upgrade automatically to empirical causation          |
| Cross-shard and cross-epoch                | Apply L24 cross-epoch rule; distribution rules separately    |

---

# 101. Minimal Causal Epoch Record

```yaml
causal_epoch:

  epoch:
    current: null
    prior: null

  transition:
    explicit: null

  verdict:
    id: null
    supersedes: null

  lineage:
    causes: []

  witness:
    required: null
    receipt: null
```

Illustrative representation only.

---

# 102. Full Causal Epoch Record

```yaml
causal_epoch:

  epoch:
    id: null
    predecessor: null
    monotonicity_valid: null

  transition:
    from: null
    to: null
    explicit: null

  verdict:
    id: null
    state: null
    epoch: null
    supersedes: []
    superseded_by: []

  causal_lineage:
    causes: []
    consequences: []
    closure_valid: null

  cross_epoch:
    crossed: null

  witness:
    required: null
    receipts: []
    verification_status: null

  execution:
    unlinked_consequence: null
    fail_closed_halt: null

  provenance:
    source: null
    ancestry: []
```

Only the invariant and enforcement semantics are canonical from this source.

---

# 103. Causal Epoch Graph

```text
e1
│
├── V1
│
├── A
│   │
│   └────────────┐
│                │
▼                │
e2               │
│                │
├── V2            │
│   ▲             │
│   │ supersedes  │
│   V1            │
│                 │
├── B ◄───────────┘
│
▼
e3
│
└── C
```

Cross-epoch causal edges require the canonical witness condition.

---

# 104. Supersession Graph

```text
VERDICT V1
@ e_k
   │
   │ explicit
   │ supersession
   ▼
VERDICT V2
@ e_{k+1}

WHERE:

e_{k+1} > e_k
```

---

# 105. Historical Record Graph

```text
PAST                         PRESENT

V1 @ e1
 │
 ▼
V2 @ e2
 │
 ▼
V3 @ e3
 │
 ▼
V4 @ e4

HISTORY RETAINS:
V1, V2, V3, V4

CURRENT VERDICT:
V4
```

L24 does not permit the historical chain to be silently rewritten into:

```text
V4 @ e1
```

---

# 106. Causal Closure Graph

```text
CAUSE A
@ e_k
   │
   ▼
CONSEQUENCE C
@ e_j

REQUIREMENT:

e_k ≤ e_j
```

---

# 107. Cross-Epoch Enforcement Graph

```text
CAUSE A @ e5
     │
     ▼
┌────────────────────┐
│ EPOCH BOUNDARY     │
└────────────────────┘
     │
     │ SIGNED
     │ WITNESS
     │ RECEIPT
     ▼
CONSEQUENCE C @ e6
```

---

# 108. Fail-Closed Graph

```text
CONSEQUENCE C
      │
      ▼
CAUSE FOUND?
   ┌──┴──┐
   │     │
  YES    NO
   │     │
   ▼     ▼
CHECK   EXECUTION
EPOCH   HALT
RULES
```

---

# 109. L24 Canonical Compression

```text
e_{k+1} > e_k
```

```text
OLD VERDICT
≠
SILENTLY REWRITABLE
```
```text
SUPERSESSION
=
EXPLICIT LATER
EPOCH TRANSITION
```
```text
CONSEQUENCE
⇒
CAUSAL ANCESTRY
```
```text
CAUSE EPOCH
≤
CONSEQUENCE EPOCH
```
```text
CROSS-EPOCH
CAUSAL CHAIN
⇒
SIGNED WITNESS RECEIPT
```
```text
UNLINKED CONSEQUENCE
⇒
FAIL-CLOSED HALT
```
---

# 110. Canonical One-Line Law

> **AMOS causal time advances strictly forward; historical verdicts may be superseded only through explicit later-epoch transitions, every consequence requires temporally admissible causal ancestry, cross-epoch causal chains require signed witness receipts, and unlinked consequences halt execution fail-closed.**

---

# 111. Canonical Equations

## Strict Monotonicity

$$
\boxed{
e_{k+1} > e_k
\quad
\forall k \in \mathbb{N}
}
$$

## No Silent Rewrite

$$
\boxed{
Verdict(e_k)
\not\rightarrow
Rewrite(Verdict(e_k))
}
$$

For revision:

$$
\boxed{
Verdict(e_k)
\xrightarrow{\text{explicit supersession}}
Verdict(e_{k+1})
}
$$

with:

$$
\boxed{
e_{k+1} > e_k
}
$$

The symbolic rewrite notation above is a normalization of the prose invariant, not an additional source equation.

## Causal Lineage Closure

$$
\boxed{
\forall C,\;
\exists A:
Cause(A,C)
\land
Epoch(A)\le Epoch(C)
}
$$

This makes the causal relation explicit as a model-level normalization of the supplied formula.

---

# 112. Operational Contract

```yaml
causal_epoch_contract:

  CE_1_STRICT_MONOTONICITY:
    establishes:
      - next_epoch_is_strictly_later
      - equal_or_backward_epoch_transition_invalid

  CE_2_NO_TIME_TRAVEL:
    establishes:
      - historical_verdicts_not_silently_rewritten
      - supersession_requires_explicit_later_epoch

  CE_3_CAUSAL_LINEAGE_CLOSURE:
    establishes:
      - every_consequence_has_causal_ancestry
      - cause_epoch_not_later_than_consequence_epoch

  CE_4_CROSS_EPOCH_WITNESS:
    establishes:
      - cross_epoch_causal_chains_require_signed_witness_receipts

  CE_5_FAIL_CLOSED:
    establishes:
      - unlinked_consequences_halt_execution_fail_closed
```

---

# 113. Source-Established Claims

The supplied L24 note directly establishes:

```text
1. L24 is the Causal Epoch Law v2.0.0.

2. It is represented as a core law.

3. RSCF state is CANON_LAW.

4. Claim class is CANONICAL_INVARIANT.

5. Provenance is AMOS_CANON.

6. Causal epochs are strictly monotonic:
   e_{k+1} > e_k.

7. Verdicts at an earlier epoch cannot
   be silently rewritten.

8. Supersession requires an explicit
   later epoch transition.

9. Every consequence requires a cause
   whose epoch is not later than the
   consequence's epoch.

10. Causal chains crossing epoch
    boundaries require signed witness
    receipts.

11. Unlinked consequences trigger
    fail-closed execution halts.
```

These are SOURCE_CLAIM statements about the supplied AMOS canonical note; within that corpus, the note marks them as canonical invariants.

---

# 114. Not Established by This Source

The supplied L24 note does **not** establish:

- physical epoch representation,
- global clock implementation,
- wall-clock mapping,
- timestamp semantics,
- fixed epoch increment,
- distributed clock algorithm,
- Lamport-clock semantics,
- vector-clock semantics,
- epoch-allocation authority,
- epoch-transition transaction protocol,
- witness-receipt schema,
- signer identity,
- signer authorization,
- signature algorithm,
- cryptographic trust root,
- threshold requirements,
- quorum requirements,
- witness independence,
- receipt expiry,
- receipt revocation,
- receipt replay protection,
- witness granularity,
- exact failure-halt scope,
- exact classification of missing witness receipts,
- storage architecture,
- MVCC/CAS mapping,
- shard-finality semantics,
- complete causal-epoch finality protocol,
- replay algorithm,
- selective invalidation algorithm,
- proof-capsule serialization,
- RSCF epoch serialization,
- empirical causal validity of arbitrary lineage edges,
- or literal distributed runtime implementation.

These remain MODEL or UNKNOWN/GAP unless established by other canon.

---

# 115. Known Gaps

```yaml
gaps:

  G1:
    severity: DECISION_RELEVANT
    description:
      >
        The physical representation and allocation mechanism
        for causal epochs is not defined by L24.

  G2:
    severity: DECISION_RELEVANT
    description:
      >
        The exact structure and verification semantics of
        signed witness receipts are unspecified.

  G3:
    severity: DECISION_RELEVANT
    description:
      >
        Witness signer authority and trust-root semantics
        are unspecified.

  G4:
    severity: DECISION_RELEVANT
    description:
      >
        Witness receipt granularity across causal edges,
        chains, and epoch transitions is unspecified.

  G5:
    severity: DECISION_RELEVANT
    description:
      >
        The exact execution-halt scope for an unlinked
        consequence is unspecified.

  G6:
    severity: DECISION_RELEVANT
    description:
      >
        L24 does not explicitly state whether a cross-epoch
        causal link lacking its required witness receipt is
        classified as an unlinked consequence or another
        enforcement failure.

  G7:
    severity: EXPLANATORY
    description:
      >
        The mapping between causal epochs and MVCC/CAS
        versions is not defined here.

  G8:
    severity: EXPLANATORY
    description:
      >
        The relationship between L24 and complete causal
        epoch finality is not specified in this note.

  G9:
    severity: EXPLANATORY
    description:
      >
        The detailed replayability semantics referenced
        through L22 require retrieval of L22.

  G10:
    severity: EXPLANATORY
    description:
      >
        Additional execution semantics referenced through
        L8 require retrieval of L8.
```

---

# 116. Claim Graph

```yaml
claim_graph:

  CE_C001:
    class: SOURCE
    claim:
      >
        Causal epochs are strictly monotonic.

  CE_C002:
    class: SOURCE
    claim:
      >
        Verdicts at an earlier epoch cannot be silently
        rewritten.

  CE_C003:
    class: SOURCE
    claim:
      >
        Supersession requires an explicit later epoch
        transition.

  CE_C004:
    class: SOURCE
    claim:
      >
        Every consequence requires causal ancestry whose
        epoch is not later than the consequence.

  CE_C005:
    class: SOURCE
    claim:
      >
        Cross-epoch causal chains require signed witness
        receipts.

  CE_C006:
    class: SOURCE
    claim:
      >
        Unlinked consequences trigger fail-closed
        execution halts.

  CE_C007:
    class: DERIVED
    claim:
      >
        A same-epoch cause is permitted by the supplied
        causal-lineage equation because it uses <=.

  CE_C008:
    class: DERIVED
    claim:
      >
        A future-epoch cause violates the supplied
        causal-lineage equation.

  CE_C009:
    class: DERIVED
    claim:
      >
        Later evidence may change a current verdict only
        without silently rewriting the historical verdict.

  CE_C010:
    class: MODEL
    claim:
      >
        Proof Capsules and RSCF nodes may preserve epoch
        and supersession metadata.

  CE_C011:
    class: MODEL
    claim:
      >
        Selective dependent invalidation can preserve
        historical lineage while preventing stale reuse.

  CE_C012:
    class: UNKNOWN
    claim:
      >
        Exact epoch allocation, witness, cryptographic,
        finality, replay, and runtime mechanisms.
```

---

# 117. Dependency Graph

```yaml
dependency_graph:

  CE_1:
    depends_on:
      - epoch_identity
      - epoch_order_relation

  CE_2:
    depends_on:
      - verdict_identity
      - historical_epoch_identity
      - explicit_transition_identity

  CE_3:
    depends_on:
      - consequence_identity
      - cause_identity
      - causal_relation
      - epoch_assignment

  CE_4:
    depends_on:
      - cross_epoch_detection
      - witness_receipt_presence

  CE_5:
    depends_on:
      - causal_link_detection
      - execution_enforcement
```

---

# 118. Proof Capsule

```yaml
proof_capsule:

  claim:
    >
      L24 canonically requires causal epochs to advance
      strictly forward, prohibits silent rewriting of
      earlier verdicts, requires explicit later-epoch
      supersession, requires causal ancestry for every
      consequence, requires signed witness receipts for
      cross-epoch causal chains, and halts execution
      fail-closed for unlinked consequences.

  class:
    CANONICAL_INVARIANT

  provenance:
    AMOS_CANON

  premises:
    - strict_monotonicity_equation
    - no_time_travel_law
    - causal_lineage_closure_equation
    - cross_epoch_witness_enforcement
    - fail_closed_unlinked_consequence_enforcement

  scope:
    AMOS_OS_layers

  dependencies:
    - epoch_identity
    - causal_lineage
    - verdict_history
    - witness_enforcement

  confidence_ceiling:
    CANONICAL_INVARIANT
```

---

# 119. Self-Proof Capsule

```yaml
proof_capsule:

  claim:
    >
      The supplied L24 source establishes a canonical
      causal-time discipline based on strict epoch
      monotonicity, explicit supersession, causal lineage
      closure, cross-epoch witness receipts, and fail-closed
      handling of unlinked consequences.

  class:
    CANONICAL_INVARIANT

  established:
    - source_rscf_state_is_CANON_LAW
    - source_claim_class_is_CANONICAL_INVARIANT
    - source_provenance_is_AMOS_CANON
    - strict_monotonicity_is_explicit
    - no_silent_verdict_rewrite_is_explicit
    - explicit_epoch_supersession_is_explicit
    - causal_lineage_closure_is_explicit
    - cross_epoch_signed_witness_requirement_is_explicit
    - fail_closed_unlinked_consequence_rule_is_explicit

  not_established:
    - epoch_physical_representation
    - epoch_allocation_protocol
    - global_clock_implementation
    - wall_clock_mapping
    - witness_schema
    - witness_signer_authority
    - signature_algorithm
    - trust_root
    - witness_independence
    - receipt_granularity
    - receipt_expiry
    - receipt_revocation
    - exact_halt_scope
    - MVCC_epoch_mapping
    - complete_causal_epoch_finality_protocol
    - literal_runtime_implementation

  confidence_ceiling:
    CANONICAL_INVARIANT
```

---

# 120. No Temporal Overreach

L24 must not reason:

```text
A HAPPENED FIRST
      ↓
A CAUSED B
```

Correct:

```text
CAUSAL CLAIM
      ↓
REQUIRES VALID
CAUSAL RELATION
      +
TEMPORALLY
ADMISSIBLE EPOCH
```

---

# 121. No Epoch Overreach

L24 must not reason:

```text
TIMESTAMP INCREASED
      ↓
CAUSAL EPOCH
INCREASED
```

unless another governing specification defines that mapping.

---

# 122. No Witness Overreach

L24 must not reason:

```text
RECEIPT IS SIGNED
      ↓
RECEIPT IS TRUSTED
      ↓
CAUSAL CLAIM
EMPIRICALLY VERIFIED
```

Correct:

```text
SIGNED RECEIPT
      ↓
SATISFIES THE
L24 PRESENCE
REQUIREMENT
ONLY IF OTHERWISE
VALID UNDER THE
GOVERNING WITNESS
SEMANTICS
```

Those semantics are not defined here.

---

# 123. No Historical Overreach

L24 must not reason:

```text
OLD VERDICT
WAS WRONG
      ↓
DELETE IT
```

Correct:

```text
OLD VERDICT @ e_k
      ↓
EXPLICIT
SUPERSESSION
      ↓
NEW VERDICT @ e_{k+1}
```

---

# 124. No Finality Overreach

L24 must not reason:

```text
NO SILENT REWRITE
      ↓
NO FUTURE REVISION
EVER
```

Correct:

```text
NO SILENT REWRITE
      +
EXPLICIT LATER
SUPERSESSION ALLOWED
```

---

# 125. No Runtime Overclaim

The canonical law describes AMOS causal semantics.

It does not by itself prove a literal implementation of:

- cryptographic witness infrastructure,
- globally synchronized causal clocks,
- distributed epoch consensus,
- append-only storage,
- transactional supersession,
- replicated causal logs,
- or formal distributed finality.

Independent implementation evidence is required for those claims.

---

# 126. Final Causal Epoch Invariant

```text
CURRENT EPOCH e_k
        │
        ▼
NEW CAUSAL STATE?
     ┌──┴──┐
     │     │
    NO    YES
     │     │
     ▼     ▼
   KEEP   EXPLICIT
          TRANSITION
              │
              ▼
       e_{k+1} > e_k
              │
              ▼
       NEW VERDICT /
       CONSEQUENCE
              │
              ▼
       CAUSAL ANCESTRY?
          ┌───┴───┐
          │       │
         NO      YES
          │       │
          ▼       ▼
       FAIL-    CROSS-EPOCH?
       CLOSED     ┌──┴──┐
       HALT       │     │
                 NO    YES
                  │     │
                  ▼     ▼
                VALID  SIGNED
                       WITNESS
                       REQUIRED
```

Compact operational law:

```text
IDENTIFY CURRENT EPOCH
→ NEVER MOVE CAUSAL TIME BACKWARD
→ REQUIRE STRICTLY LATER EPOCHS FOR TRANSITION
→ PRESERVE HISTORICAL VERDICTS
→ SUPERSEDE EXPLICITLY RATHER THAN REWRITE
→ REQUIRE CAUSAL ANCESTRY FOR CONSEQUENCES
→ FORBID FUTURE-EPOCH CAUSES
→ REQUIRE SIGNED WITNESS RECEIPTS ACROSS EPOCH BOUNDARIES
→ FAIL CLOSED WHEN CONSEQUENCES ARE UNLINKED
```

with hard firewalls:

```text
CAUSAL EPOCH
≠
WALL-CLOCK TIME

CAUSAL EPOCH
≠
TIMESTAMP

CAUSAL EPOCH
≠
STATE VERSION

CAUSAL EPOCH
≠
SHARD

CAUSAL EPOCH
≠
EPISTEMIC REGIME

STRICT MONOTONICITY
≠
FIXED +1 INCREMENT

NO TIME TRAVEL
≠
NO REVISION

SUPERSESSION
≠
SILENT REWRITE

INVALIDATION
≠
HISTORICAL DELETION

EARLIER
≠
CAUSE

TEMPORALLY ADMISSIBLE
≠
CAUSALLY PROVEN

CAUSAL LINEAGE
≠
EMPIRICAL CAUSAL EFFECT

SIGNED
≠
TRUSTED

MULTIPLE RECEIPTS
≠
INDEPENDENT WITNESSES

CROSS-EPOCH
≠
CROSS-SHARD

NEW EPOCH
≠
NEW REGIME

HISTORICALLY PRESERVED
≠
CURRENTLY VALID

NO SILENT REWRITE
≠
COMPLETE FINALITY PROTOCOL

L24 CAUSAL EPOCH
≠
PROOF OF LITERAL
DISTRIBUTED RUNTIME
```

---

# 127. RSCF Node

```yaml
RSCF-NODE:

  node_id:
    l24_causal_epoch

  node_type:
    core_law

  path:
    01_CANON/01_CORE_LAWS/L24_CAUSAL_EPOCH.md

  state:
    CANON_LAW

  claim_class:
    CANONICAL_INVARIANT

  provenance:
    AMOS_CANON

RSCF-RELATIONS:

  - INDEXED_BY:

  - INDEXED_BY:

  - CHILD_OF:

  - MEMBER_OF:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO: EPISTEMIC_REGIME

  - RELATED_TO:

  - RELATED_TO:

  - RELATED_TO: FAILURE_RECOVERY
```

---

**Related:** [[01_CANON/01_CORE_LAWS/L8_EXECUTION|L8_EXECUTION]] · [[01_CANON/01_CORE_LAWS/L22_REPLAYABILITY|L22_REPLAYABILITY]] · [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

---

# 128. Final Canon Boundary

The supplied source canonically supports:

```text
STRICT CAUSAL-EPOCH
MONOTONICITY

NO SILENT HISTORICAL
VERDICT REWRITE

EXPLICIT LATER-EPOCH
SUPERSESSION

CAUSAL LINEAGE
CLOSURE

NO FUTURE-EPOCH
CAUSE

SIGNED WITNESS
RECEIPTS FOR
CROSS-EPOCH CHAINS

FAIL-CLOSED HALT FOR
UNLINKED CONSEQUENCES
```

It does **not** establish the physical epoch representation, global clock implementation, witness cryptography, signer authority, receipt granularity, MVCC mapping, complete finality protocol, replay algorithm, or literal distributed runtime implementation.

Therefore the canonical boundary is:

```yaml
status:
  CANON_LAW

claim_class:
  CANONICAL_INVARIANT

provenance:
  AMOS_CANON

scope:
  AMOS_OS_layers
```

**Conclusion class: CANONICAL_INVARIANT within AMOS_CANON.**

---

**MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
