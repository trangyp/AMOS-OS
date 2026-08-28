---
title: L21 EPISTEMIC REGIME
type: epistemic
source: 01_CANON/01_CORE_LAWS
tags:
  - canon
  - core_laws
  - epistemic
  - epistemic_regime
  - declared_regime
  - regime_firewall
  - regime_bridge
  - governed_payload
  - non_portables
  - simulation
  - empirical
  - canonical
  - speculative
  - simulation_pessimism
  - branch_stability
  - worst_branch_drift
  - freshness
  - freshness_axes
  - temporal_freshness
  - environmental_freshness
  - regimeal_freshness
  - provenance_freshness
  - scope_freshness
  - model_freshness
  - source_freshness
  - applicability
  - canon/universe
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: core_laws
  canonical_status: CONDITIONAL
  specification_status: PROPOSED_SPECIFICATION
  node_id: l21_epistemic_regime
  node_type: note
---

# L21 Epistemic Regime Laws

**STATUS:** PROPOSED_SPECIFICATION  
**epistemic_class:** AMOS_MODEL  
**canonical_status:** CONDITIONAL  
**updated:** 2026-08-26

---

# 0. Status

L21 defines the proposed AMOS **Epistemic Regime Laws**.

It replaces the prior placeholder with a structured specification governing:

- explicit epistemic regime declaration,
- simulation,
- empirical evaluation,
- canonical evaluation,
- speculative evaluation,
- regime-local conclusions,
- regime boundaries,
- explicit bridge routing,
- governed cross-regime payloads,
- declaration of non-portable information,
- simulation pessimism,
- branch-sensitive simulation evaluation,
- worst-branch drift,
- all-branch stability requirements,
- applicability,
- seven-axis freshness,
- temporal freshness,
- environmental freshness,
- regimeal freshness,
- provenance freshness,
- scope freshness,
- model freshness,
- source freshness,
- regime shifts,
- conclusion invalidation,
- RSCF compatibility,
- Proof Capsule applicability,
- GMEF routing,
- provenance topology,
- causal discipline,
- adversarial validation,
- governed evolution.

L21 remains:

```text
PROPOSED_SPECIFICATION
        │
        ▼
    AMOS_MODEL
        │
        ▼
    CONDITIONAL

until authoritative epistemic-regime canon validates, modifies, supersedes, or rejects these semantics.

The four source laws are:

```text
ER-1 DECLARED REGIME
ER-2 REGIME FIREWALL
ER-3 SIMULATION PESSIMISM
ER-4 FRESHNESS AXES
```

The central invariant is:

```text
A CONCLUSION IS NOT
EPISTEMICALLY PORTABLE
MERELY BECAUSE ITS WORDING
REMAINS THE SAME.

ITS VALIDITY IS BOUND TO
REGIME + SCOPE + FRESHNESS
UNLESS AN EXPLICIT VALID BRIDGE
ESTABLISHES TRANSFER.
```

---

# 1. Governing Objective

L21 asks:

```text
UNDER WHAT EPISTEMIC REGIME
WAS THIS RESULT ESTABLISHED?
```

before asking:

```text
CAN THIS RESULT BE USED HERE?
```

The governing model is:

```text
EVALUATION
    │
    ▼
DECLARE REGIME
    │
    ▼
SIMULATION / EMPIRICAL /
CANONICAL / SPECULATIVE
    │
    ▼
EVALUATE LOCALLY
    │
    ▼
CHECK 7-AXIS FRESHNESS
    │
    ▼
SAME REGIME?
 ┌──┴──┐
 │     │
YES    NO
 │     │
 ▼     ▼
LOCAL  EXPLICIT
USE    BRIDGE ROUTING
       │
       ├─ GOVERNED PAYLOAD
       ├─ NON-PORTABLES DECLARED
       └─ TARGET VALIDITY CHECKED
              │
              ▼
         TRANSFER MAY
         BECOME VALID
```

The compact principle is:

```text
DECLARE WHERE YOU KNOW IT,
THEN PROVE WHERE IT TRAVELS.
```

---

# 2. Core Epistemic Regime Laws

```text
ER-1
DECLARED REGIME

ER-2
REGIME FIREWALL

ER-3
SIMULATION PESSIMISM

ER-4
FRESHNESS AXES
```

Unified:

```text
EVALUATION
    ↓
DECLARE REGIME
    ↓
ESTABLISH RESULT
WITHIN THAT REGIME
    ↓
CHECK APPLICABILITY
    ↓
CHECK 7 FRESHNESS AXES
    ↓
CROSS-REGIME USE?
 ┌──┴──┐
 │     │
NO    YES
 │     │
 ▼     ▼
LOCAL  EXPLICIT BRIDGE
USE       ↓
       GOVERNED PAYLOAD
          ↓
       DECLARE
       NON-PORTABLES
          ↓
       TARGET-REGIME
       VALIDATION
```

For simulation:

```text
SIMULATION
    ↓
ENUMERATE RELEVANT BRANCHES
    ↓
COUNT WORST-BRANCH DRIFT
    ↓
ALL BRANCHES STABLE?
 ┌──┴──┐
 │     │
NO    YES
 │     │
 ▼     ▼
NOT    STABLE
STABLE VERDICT
```

---

# 3. ER-1 — Declared Regime

**Law**

> every evaluation states its regime (simulation / empirical / canonical / speculative).

ER-1 establishes explicit regime declaration as a requirement of evaluation.

The four source-defined regimes are:

```text
SIMULATION
EMPIRICAL
CANONICAL
SPECULATIVE
```

Therefore:

```text
EVALUATION
⇒
DECLARED_REGIME
```

within the proposed L21 model.

---

# 4. Regime Declaration Is Part of Meaning

A conclusion without its regime can be epistemically ambiguous.

Example:

```text
"THE SYSTEM IS STABLE"
```

could mean:

```text
SIMULATION:
all modeled branches remained stable

EMPIRICAL:
observed executions remained stable

CANONICAL:
the governing corpus specifies stability

SPECULATIVE:
a model predicts stability
```

These are not interchangeable claims.

Therefore:

```text
CLAIM TEXT
+
REGIME
```

is more informative than claim text alone.

---

# 5. Simulation Regime

The source explicitly names:

```text
simulation
```

as an epistemic regime.

A conservative interpretation is:

```text
SIMULATION
=
RESULT ESTABLISHED
WITHIN A SIMULATED /
MODELED EXECUTION CONTEXT
```

The exact canonical definition of simulation is not supplied.

---

# 6. Simulation Does Not Establish Empirical Reality

Invalid:

```text
SIMULATION RESULT:
X OCCURS
        ↓
EMPIRICAL CLAIM:
X OCCURS IN REAL DEPLOYMENT
```

without a valid bridge.

Thus:

```text
SIMULATED
≠
EMPIRICALLY OBSERVED
```

---

# 7. Simulation Does Not Establish Canon

Likewise:

```text
SIMULATION SUPPORTS RULE R
```

does not imply:

```text
R IS CANON
```

Canonical status requires canonical authority under the relevant governance system.

---

# 8. Simulation Does Not Equal Speculation

Simulation and speculation are separately named regimes.

Therefore they should not be silently collapsed.

A simulation may be highly structured and deterministic while remaining simulation.

A speculative claim may be conceptual without simulated execution.

Exact boundary semantics remain unspecified.

---

# 9. Empirical Regime

The source explicitly names:

```text
empirical
```

as an epistemic regime.

A conservative interpretation is:

```text
EMPIRICAL
=
RESULT GROUNDED IN
OBSERVATION / MEASUREMENT
OF THE TARGET OR
RELEVANT REAL-WORLD SYSTEM
```

The exact measurement requirements are not supplied by L21.

---

# 10. Empirical Observation Is Scope-Bound

An empirical result established for:

```text
SYSTEM S
ENVIRONMENT E
TIME T
POPULATION P
```

does not automatically establish the same conclusion for:

```text
SYSTEM S2
ENVIRONMENT E2
TIME T2
POPULATION P2
```

This follows ER-2 and ER-4's applicability discipline.

---

# 11. Empirical Does Not Mean Universal

Invalid:

```text
OBSERVED ONCE
        ↓
UNIVERSAL LAW
```

or:

```text
OBSERVED IN SAMPLE P1
        ↓
TRUE FOR ALL POPULATIONS
```

without independent support for generalization.

---

# 12. Empirical Does Not Mean Canonical

A result can be empirically well-supported while not being canonical.

```text
EMPIRICAL VALIDITY
≠
CANONICAL AUTHORITY
```

Likewise, canon may state a rule whose empirical performance remains separately testable.

---

# 13. Canonical Regime

The source explicitly names:

```text
canonical
```

as an epistemic regime.

A conservative interpretation is:

```text
CANONICAL
=
RESULT OR RULE
ESTABLISHED BY
THE APPLICABLE
AUTHORITATIVE CANON
```

The exact authority hierarchy is governed elsewhere.

---

# 14. Canonical Is Not Automatically Empirical

A canonical specification may state:

```text
SYSTEM MUST DO X
```

without establishing:

```text
DEPLOYED SYSTEM
ACTUALLY DOES X
```

Therefore:

```text
NORMATIVE / CANONICAL RULE
≠
EMPIRICAL IMPLEMENTATION FACT
```

unless validated through an explicit bridge.

---

# 15. Canonical Is Not Automatically Simulation Truth

Likewise, a canonical rule may define expected behavior while a simulation implementation may fail to reproduce it.

Therefore:

```text
CANON SAYS X
```

does not automatically establish:

```text
SIMULATION PRODUCES X
```

The simulator itself requires validation.

---

# 16. Speculative Regime

The source explicitly names:

```text
speculative
```

as an epistemic regime.

A conservative interpretation is:

```text
SPECULATIVE
=
HYPOTHETICAL,
EXPLORATORY,
OR NOT YET
SUFFICIENTLY ESTABLISHED
IN A STRONGER REGIME
```

Exact criteria remain unspecified.

---

# 17. Speculation Is Allowed but Typed

ER-1 does not prohibit speculation.

It requires that speculative evaluation be declared as such.

Therefore:

```text
SPECULATION
+
CORRECT LABEL
```

is epistemically preferable to:

```text
SPECULATION
PRESENTED AS FACT
```

---

# 18. Speculative Does Not Mean False

A speculative claim may later be validated.

Thus:

```text
SPECULATIVE
≠
FALSE
```

It means the claim currently occupies the speculative regime.

---

# 19. Speculative Does Not Mean Empirical

Likewise:

```text
PLAUSIBLE MODEL
```

does not become:

```text
EMPIRICAL OBSERVATION
```

because it is coherent or persuasive.

---

# 20. Regime Declaration Record

A model-level representation:

```yaml
evaluation:
  evaluation_id: E1
  regime: simulation
  claim: C1
```

or:

```yaml
evaluation:
  evaluation_id: E2
  regime: empirical
  claim: C2
```

The exact schema is not source-defined.

---

# 21. Missing Regime

If an evaluation lacks a regime declaration:

```text
EVALUATION
+
NO REGIME
```

then ER-1 is not satisfied.

A conservative result is:

```text
REGIME = UNKNOWN/GAP
```

rather than inferring the regime from tone or wording.

---

# 22. Regime Inference Is Not Declaration

A reader may infer:

```text
"this sounds empirical"
```

but that does not satisfy an explicit declaration requirement.

Thus:

```text
INFERRED REGIME
≠
DECLARED REGIME
```

unless another canonical rule permits inference.

---

# 23. Mixed-Regime Evaluation

An evaluation may contain multiple epistemic components.

Example:

```text
CANONICAL PREMISE
+
EMPIRICAL OBSERVATION
+
SPECULATIVE MECHANISM
```

The source does not define a canonical mixed-regime representation.

A safe model-level approach is to type each load-bearing component separately rather than assign an unjustified single regime.

---

# 24. Regime of Derived Conclusion

If a conclusion depends on premises from multiple regimes:

```text
P1 = CANONICAL
P2 = EMPIRICAL
P3 = SPECULATIVE
```

the conclusion should not silently inherit the strongest regime label.

Its validity depends on the bridges and load-bearing premises.

---

# 25. ER-1 Compact Law

```text
EVERY EVALUATION
        ↓
DECLARE
SIMULATION
OR
EMPIRICAL
OR
CANONICAL
OR
SPECULATIVE
```

No regime declaration means the evaluation has an unresolved epistemic-regime gap.

---

# 26. ER-2 — Regime Firewall

**Law**

> conclusions do not cross regimes without explicit bridge routing (governed payload, non-portables declared).

ER-2 establishes:

```text
NO SILENT CROSS-REGIME
CONCLUSION TRANSFER
```

and requires:

```text
EXPLICIT BRIDGE ROUTING
```

with at least two named bridge concepts:

```text
GOVERNED PAYLOAD
NON-PORTABLES DECLARED
```

---

# 27. Regime Locality

A conclusion established in regime R1 is initially local to R1.

Conceptually:

```text
C @ R1
```

does not automatically become:

```text
C @ R2
```

Therefore:

```text
VALID_R1(C)
↛
VALID_R2(C)
```

without explicit bridge routing.

---

# 28. Regime Firewall

The firewall is:

```text
SOURCE REGIME
      │
      ▼
CONCLUSION C
      │
      ╳
NO IMPLICIT TRANSFER
      ╳
      │
      ▼
TARGET REGIME
```

Crossing requires:

```text
SOURCE REGIME
      ↓
EXPLICIT BRIDGE
      ↓
GOVERNED PAYLOAD
      ↓
NON-PORTABLES
DECLARED
      ↓
TARGET REGIME
```

---

# 29. Bridge Routing

The source uses:

```text
explicit bridge routing
```

but does not define the complete bridge protocol.

A model-level bridge answers:

```text
WHAT IS MOVING?
FROM WHICH REGIME?
TO WHICH REGIME?
UNDER WHAT AUTHORITY?
WHAT DOES NOT TRANSFER?
WHAT TARGET-SIDE VALIDATION
IS REQUIRED?
```

---

# 30. Governed Payload

The source explicitly identifies:

```text
governed payload
```

as part of bridge routing.

A conservative interpretation is:

```text
THE INFORMATION TRANSFERRED
ACROSS THE REGIME BOUNDARY
IS EXPLICITLY IDENTIFIED
AND GOVERNED
```

The exact governance mechanism is not supplied.

---

# 31. Non-Portables

The source explicitly requires:

```text
non-portables declared
```

This means some properties of a conclusion or its evidence do not survive regime transfer.

Conceptually:

```text
SOURCE RESULT
├─ PORTABLE CONTENT
└─ NON-PORTABLE CONTENT
```

The bridge must not silently transport the latter.

---

# 32. Non-Portable Examples

Possible model-level non-portables include:

* simulation-only assumptions,
* synthetic distributions,
* simulator-specific timing,
* canonical authority,
* empirical sampling context,
* speculative mechanism assumptions,
* environment-specific parameters,
* regime-local confidence.

These examples are not source-defined.

---

# 33. Canonical Authority Is Non-Portable to Empirical Fact

Example:

```text
CANONICAL:
"implementation must reject X"
```

Portable payload might include:

```text
EXPECTED REQUIREMENT:
reject X
```

But non-portable:

```text
CLAIM:
deployed implementation
actually rejects X
```

That empirical fact requires empirical validation.

---

# 34. Empirical Observation Is Non-Portable to Canonical Authority

Example:

```text
EMPIRICAL:
implementation repeatedly behaves as rule R
```

does not automatically transfer:

```text
CANONICAL:
R is governing law
```

Observed convention is not canonical authority.

---

# 35. Simulation Outcome Is Non-Portable to Empirical Observation

Example:

```text
SIMULATION:
all modeled nodes converge
```

does not transfer:

```text
EMPIRICAL:
real nodes converge
```

without bridge validation.

---

# 36. Speculative Mechanism Is Non-Portable to Empirical Cause

Example:

```text
SPECULATIVE:
mechanism M could explain O
```

does not transfer:

```text
EMPIRICAL:
M caused O
```

without appropriately typed evidence.

This also invokes the causal firewall.

---

# 37. Explicit Bridge Record

A model-level bridge representation:

```yaml
regime_bridge:

  bridge_id: RB1

  source_regime:
    simulation

  target_regime:
    empirical

  governed_payload:
    - predicted_failure_condition_F

  non_portables:
    - simulator_specific_probability
    - synthetic_workload_assumption

  target_validation:
    - empirical_test_of_F
```

Exact schema is not canonical.

---

# 38. Bridge Does Not Guarantee Transfer

The existence of a bridge object does not itself establish that the conclusion successfully transfers.

```text
BRIDGE DECLARED
≠
TARGET VALIDITY ESTABLISHED
```

The bridge must satisfy whatever target-regime validation is load-bearing.

---

# 39. Bridge Routing vs Relabeling

Invalid:

```text
SIMULATION RESULT
        ↓
CHANGE LABEL TO EMPIRICAL
```

Correct conceptual pattern:

```text
SIMULATION RESULT
        ↓
BRIDGE
        ↓
EMPIRICAL TEST
        ↓
EMPIRICAL RESULT
```

when empirical validation is required.

---

# 40. Bridge Directionality

A bridge from:

```text
SIMULATION → EMPIRICAL
```

does not automatically imply a valid bridge:

```text
EMPIRICAL → SIMULATION
```

The two directions may preserve different information.

Therefore:

```text
BRIDGE(R1,R2)
≠
BRIDGE(R2,R1)
```

unless explicitly established.

---

# 41. Bridge Composition

Suppose:

```text
R1 → R2
```

and:

```text
R2 → R3
```

are valid bridges.

It does not automatically follow that:

```text
R1 → R3
```

preserves every property.

Non-portables may accumulate.

Thus bridge composition should be explicit where load-bearing.

---

# 42. Bridge Chain

Conceptually:

```text
SIMULATION
    ↓
BRIDGE A
    ↓
EMPIRICAL
    ↓
BRIDGE B
    ↓
CANONICAL
```

A property lost at Bridge A cannot silently reappear at Bridge B.

---

# 43. Non-Portable Monotonicity

A useful model-level invariant is:

```text
ONCE A PROPERTY
IS DECLARED NON-PORTABLE
ACROSS A BRIDGE,
DOWNSTREAM CONCLUSIONS
MUST NOT CLAIM IT
WITHOUT REVALIDATION.
```

This prevents epistemic laundering.

---

# 44. Regime Laundering

Regime laundering occurs conceptually when:

```text
WEAK / DIFFERENT REGIME
        ↓
UNDECLARED TRANSFER
        ↓
STRONGER-SOUNDING LABEL
```

Examples:

```text
SPECULATION
→
"FACT"

SIMULATION
→
"OBSERVED"

EMPIRICAL PRACTICE
→
"CANON"

CANONICAL REQUIREMENT
→
"DEPLOYED BEHAVIOR"
```

ER-2 rejects such silent crossings.

---

# 45. Regime Firewall and Language

A conclusion should preserve regime-sensitive language.

Examples:

```text
SIMULATION:
"The simulation produced..."

EMPIRICAL:
"Observed measurements show..."

CANONICAL:
"The governing specification states..."

SPECULATIVE:
"A possible explanation is..."
```

This wording is model guidance, not canonical syntax.

---

# 46. Cross-Regime Confidence

A high-confidence conclusion in one regime does not automatically retain the same confidence in another.

```text
HIGH CONFIDENCE @ R1
↛
HIGH CONFIDENCE @ R2
```

unless the bridge validates the relevant dependencies.

---

# 47. Cross-Regime Provenance

Provenance should remain attached to the transferred payload.

Conceptually:

```text
SOURCE CLAIM
      ↓
BRIDGE
      ↓
TARGET CLAIM
```

should preserve:

```text
WHERE DID THIS COME FROM?
WHAT TRANSFORMATION OCCURRED?
WHAT WAS LOST?
```

where those facts are material.

---

# 48. Bridge Provenance

A model-level bridge may carry:

```yaml
provenance:
  source_claim: C1
  source_regime: simulation
  bridge: RB1
  target_claim: C2
  transformations:
    - empirical_revalidation
```

Exact fields are not source-defined.

---

# 49. Bridge and Competing Hypotheses

A bridge must not collapse multiple source-regime hypotheses merely because the target regime prefers one narrative.

Example:

```text
SIMULATION:
H1 COMPETING H2
```

must not become:

```text
EMPIRICAL:
H1 VERIFIED
```

without discriminating empirical evidence.

---

# 50. Bridge and Causality

Cross-regime transfer is especially dangerous for causal claims.

```text
SIMULATION:
intervention M produces O
```

may establish model behavior.

It does not necessarily establish:

```text
EMPIRICAL:
M causes O in reality
```

unless the empirical bridge licenses causal inference.

---

# 51. Bridge and Scope

A bridge must account for scope differences.

```text
SIMULATION:
10 nodes, network model N1
```

to:

```text
EMPIRICAL:
10,000 nodes, network N2
```

is not merely a regime change; it is also a scale/environment/scope change.

Thus ER-2 and ER-4 interact.

---

# 52. Bridge and Time

A valid historical bridge may become stale.

```text
R1 @ T1
→
R2 @ T1
```

does not automatically remain valid at:

```text
T2
```

if the target system materially changed.

---

# 53. Bridge and Model Version

A simulation-to-empirical bridge validated for:

```text
MODEL M1
```

may not transfer to:

```text
MODEL M2
```

without model-freshness validation.

---

# 54. Bridge and Source Change

If the authoritative source underlying a canonical claim changes:

```text
SOURCE S1
→
SOURCE S2
```

a prior bridge based on S1 may require revalidation.

This is captured by source freshness.

---

# 55. ER-2 Compact Law

```text
CONCLUSION @ REGIME A
        ╳
NO SILENT CROSSING
        ╳
        ↓
EXPLICIT BRIDGE
        ↓
GOVERNED PAYLOAD
        ↓
NON-PORTABLES DECLARED
        ↓
TARGET-REGIME VALIDATION
        ↓
CONCLUSION @ REGIME B
```

---

# 56. ER-3 — Simulation Pessimism

**Law**

> simulations count worst-branch drift; stable verdicts require ALL branches stable.

ER-3 establishes two explicit rules:

```text
SIMULATIONS COUNT
WORST-BRANCH DRIFT
```

and:

```text
STABLE VERDICT
REQUIRES
ALL BRANCHES STABLE
```

---

# 57. Simulation Branches

The source uses:

```text
branches
```

without defining exact branch-generation semantics.

A model-level interpretation is that a simulation may have multiple relevant execution paths, scenarios, trajectories, or modeled outcomes.

---

# 58. Branch Set

Let:

```text
B = {b1, b2, ..., bn}
```

represent the relevant simulation branches.

Each branch may have a drift measure:

```text
D(bi)
```

The exact definition of drift is not supplied by L21.

---

# 59. Worst-Branch Drift

A semantic compression is:

```text
D_worst
=
max(
  D(b1),
  D(b2),
  ...,
  D(bn)
)
```

where larger drift means worse deviation under the applicable model.

This is a model-level mathematical representation of:

```text
count worst-branch drift
```

The canonical aggregation function is not explicitly defined.

---

# 60. Stable Verdict

ER-3 explicitly requires:

```text
ALL BRANCHES STABLE
```

for a stable verdict.

Therefore:

```text
StableVerdict
⇒
∀b ∈ B : Stable(b)
```

---

# 61. One Unstable Branch

If:

```text
b1 = stable
b2 = stable
b3 = unstable
b4 = stable
```

then:

```text
ALL BRANCHES STABLE = FALSE
```

and therefore:

```text
STABLE VERDICT
NOT LICENSED
```

under ER-3.

---

# 62. Majority Stability Is Insufficient

Invalid:

```text
99 OF 100 BRANCHES STABLE
        ↓
STABLE
```

if the remaining relevant branch is unstable.

ER-3 requires:

```text
100% OF RELEVANT BRANCHES
STABLE
```

for the stable verdict.

---

# 63. Average Drift Is Insufficient

Invalid if used to hide an unstable worst branch:

```text
AVERAGE DRIFT = LOW
        ↓
STABLE
```

while:

```text
ONE BRANCH
HAS HIGH DRIFT
```

ER-3 explicitly directs attention to the worst branch.

---

# 64. Best-Case Selection Is Invalid

Invalid:

```text
SELECT MOST STABLE BRANCH
        ↓
REPORT SIMULATION STABLE
```

ER-3 requires all relevant branches to satisfy stability.

---

# 65. Median Stability Is Insufficient

Likewise:

```text
MEDIAN BRANCH STABLE
```

does not satisfy:

```text
ALL BRANCHES STABLE
```

unless every branch is stable.

---

# 66. Worst-Branch Pessimism

The law encodes a conservative simulation posture:

```text
SIMULATION VERDICT
IS LIMITED BY
THE LEAST STABLE
RELEVANT BRANCH
```

This resembles a weakest-branch ceiling.

---

# 67. Drift

The source does not define:

```text
drift
```

Canonical gaps include:

* what quantity drifts,
* reference baseline,
* metric,
* threshold,
* directionality,
* normalization,
* aggregation,
* time horizon.

Therefore no exact drift formula should be invented as canon.

---

# 68. Stability

Likewise, the source does not define the exact canonical stability predicate.

Conceptually:

```text
Stable(b)
```

is evaluated under whatever applicable simulation canon defines stability.

L21 only establishes the all-branch requirement.

---

# 69. Branch Relevance

ER-3 says:

```text
ALL branches stable
```

but the supplied note does not define whether `all` means:

* all generated branches,
* all reachable branches,
* all admissible branches,
* all threat-relevant branches,
* all branches above some probability,
* all branches in a bounded simulation tree.

This is a DECISION-RELEVANT gap.

---

# 70. Impossible Branches

A branch that is provably impossible under the simulation's declared regime may or may not belong to the relevant branch set.

L21 does not define this boundary.

Therefore:

```text
BRANCH MEMBERSHIP
=
CANONICAL GAP
```

---

# 71. Low-Probability Branches

ER-3 does not state:

```text
IGNORE LOW-PROBABILITY
UNSTABLE BRANCHES
```

Therefore probability alone cannot be assumed to exempt a branch.

If probability-based exclusion exists, it must come from authoritative simulation canon.

---

# 72. Zero-Probability Branches

Likewise, exact treatment of zero-probability but structurally represented branches is unspecified.

Do not silently decide their relevance without a governing branch rule.

---

# 73. Worst-Branch Drift Record

A model-level representation:

```yaml
simulation_result:

  branches:
    - id: b1
      stable: true
      drift: 0.02

    - id: b2
      stable: true
      drift: 0.04

    - id: b3
      stable: false
      drift: 0.31

  worst_branch:
    id: b3
    drift: 0.31

  stable_verdict:
    false
```

The schema and numeric metric are illustrative only.

---

# 74. Simulation Verdict Algorithm

```python
def simulation_stable(branches):

    for branch in branches:
        if not branch.stable:
            return False

    return True
```

This directly represents the all-branch requirement.

---

# 75. Worst-Branch Algorithm

A model-level representation:

```python
def worst_branch_drift(branches):

    return max(
        branch.drift
        for branch in branches
    )
```

This assumes scalar comparable drift, which L21 itself does not establish.

---

# 76. Vector Drift

If drift is multidimensional, a single maximum may be insufficient.

Example:

```text
DRIFT =
[
  safety,
  consistency,
  latency,
  epistemic divergence
]
```

The source does not specify scalar versus vector drift.

Therefore exact worst-branch ordering remains UNKNOWN/GAP.

---

# 77. Incomparable Branches

Two branches may be worse on different dimensions.

```text
b1:
high safety drift,
low consistency drift

b2:
low safety drift,
high consistency drift
```

Without a canonical ordering rule, they may remain incomparable rather than forcing one scalar ranking.

---

# 78. Simulation Pessimism Does Not Mean Fabricating Bad Branches

ER-3 requires pessimistic treatment of simulation branches.

It does not license inventing unsupported branches merely to produce a negative verdict.

Thus:

```text
PESSIMISM
≠
FABRICATION
```

The branch set still requires legitimate generation under the simulation model.

---

# 79. Simulation Pessimism Does Not Equal Universal Failure

An unstable branch establishes:

```text
SIMULATION NOT STABLE
UNDER ER-3
```

It does not automatically establish:

```text
REAL SYSTEM WILL FAIL
```

That would cross simulation → empirical regime without a bridge.

---

# 80. Stable Simulation Does Not Equal Empirical Stability

Likewise:

```text
ALL SIMULATION BRANCHES STABLE
```

licenses a stable verdict within the simulation regime.

It does not automatically establish empirical stability.

---

# 81. Stable Simulation Does Not Equal Canonical Compliance

A simulation may be stable yet violate canonical rules.

Therefore:

```text
SIMULATION STABILITY
≠
CANONICAL VALIDITY
```

unless the canonical requirement is specifically part of the simulation evaluation and bridge.

---

# 82. Simulation Pessimism and Adversarial Validation

L20 may generate adversarial branches or cases.

L21 ER-3 then provides a regime-specific rule for simulation stability:

```text
ADVERSARIAL SIMULATION
        ↓
MULTIPLE BRANCHES
        ↓
ANY UNSTABLE?
   ┌────┴────┐
   │         │
  YES       NO
   │         │
   ▼         ▼
NO STABLE   STABLE
VERDICT     MAY BE
            LICENSED
```

This integration is model-level unless cross-referenced by authoritative canon.

---

# 83. Simulation and Competing Hypotheses

Different branches may correspond to different hypotheses.

ER-3 does not require collapsing them into an average.

```text
H1 → stable branch
H2 → unstable branch
```

If both are legitimate branches, the stable verdict is not licensed.

---

# 84. Branch Provenance

Each branch may depend on different assumptions.

A useful model-level record includes:

```yaml
branch:
  id: b1
  assumptions:
    - A1
    - A2
  provenance:
    - model_component_M1
```

This helps determine whether branches are truly distinct or duplicated descendants of the same assumptions.

---

# 85. Correlated Branches

Ten branches derived from one identical underlying assumption are not necessarily ten independent confirmations.

ER-3's all-branch rule concerns stability, not independence counting.

Provenance topology remains separately relevant.

---

# 86. Branch Explosion

A simulation may contain enormous or unbounded branch spaces.

L21 does not define:

* exhaustive enumeration,
* pruning,
* abstraction,
* symbolic exploration,
* sampling,
* branch bounding.

Therefore claiming:

```text
ALL BRANCHES STABLE
```

requires clarity about what branch universe was actually covered.

---

# 87. Sampled Branches

If only sampled branches were evaluated:

```text
ALL SAMPLED BRANCHES STABLE
```

is weaker than:

```text
ALL RELEVANT BRANCHES STABLE
```

unless the sampling method independently licenses that inference.

---

# 88. Branch Coverage Receipt

A model-level simulation receipt may include:

```yaml
branch_coverage:
  universe_definition: U1
  explored: 1000
  exhaustive: false
```

Then the conclusion should not claim exhaustive all-branch stability.

---

# 89. Exhaustive Simulation

If all relevant branches are formally enumerated and all stable:

```text
∀b ∈ B_relevant:
Stable(b)
```

then ER-3's all-branch condition is satisfied within that simulation regime.

This still does not cross regimes automatically.

---

# 90. ER-3 Compact Law

```text
SIMULATION
    ↓
RELEVANT BRANCH SET
    ↓
MEASURE / EVALUATE DRIFT
    ↓
TAKE WORST-BRANCH CONDITION
    ↓
ANY BRANCH UNSTABLE?
 ┌──┴──┐
 │     │
YES    NO
 │     │
 ▼     ▼
NO     STABLE
STABLE VERDICT
VERDICT MAY BE
       LICENSED
```

---

# 91. ER-4 — Freshness Axes

**Law**

> applicability carries 7-axis freshness (temporal, environmental, regimeal, provenance, scope, model, source).

ER-4 explicitly establishes seven freshness axes:

```text
1. TEMPORAL
2. ENVIRONMENTAL
3. REGIMEAL
4. PROVENANCE
5. SCOPE
6. MODEL
7. SOURCE
```

Applicability therefore carries a multidimensional freshness state.

---

# 92. Freshness Is Not One Timestamp

A conclusion can be temporally recent yet stale in another dimension.

Example:

```text
TEMPORAL:
fresh

MODEL:
stale
```

because the conclusion was evaluated today using an obsolete model.

Thus:

```text
RECENT
≠
FRESH ON ALL AXES
```

---

# 93. Seven-Axis Freshness Vector

A model-level representation:

```text
F(C) =
[
  F_temporal,
  F_environmental,
  F_regimeal,
  F_provenance,
  F_scope,
  F_model,
  F_source
]
```

The source establishes the axes but not their numeric encoding.

---

# 94. Temporal Freshness

Temporal freshness concerns whether the conclusion remains valid relative to time.

Conceptually:

```text
VALID @ T1
```

may become stale at:

```text
T2
```

because the world or target system changed.

---

# 95. Temporal Freshness Is Claim-Specific

Different claims decay at different rates.

```text
MATHEMATICAL IDENTITY
```

may have effectively long temporal validity.

```text
CURRENT SYSTEM CONFIGURATION
```

may decay quickly.

L21 does not define universal freshness durations.

---

# 96. Environmental Freshness

Environmental freshness concerns whether the environment in which a result was established still matches the environment in which it is applied.

Examples of environment may include:

* hardware,
* network,
* deployment topology,
* runtime,
* dependency versions,
* operating conditions.

These examples are model-level.

---

# 97. Environmental Shift

```text
RESULT @ ENVIRONMENT E1
```

does not automatically apply to:

```text
ENVIRONMENT E2
```

when the changed environment is load-bearing.

Thus:

```text
E1 ≠ E2
→
ENVIRONMENTAL FRESHNESS CHECK
```

---

# 98. Regimeal Freshness

The source uses the term:

```text
regimeal
```

as one of the seven axes.

A conservative interpretation is freshness relative to the epistemic or operational regime under which the conclusion remains valid.

This axis is distinct from ER-1's regime declaration but closely related.

---

# 99. Regimeal Shift

A conclusion established under:

```text
REGIME R1
```

may become stale when applied under:

```text
REGIME R2
```

even if its timestamp is recent.

This reinforces ER-2.

---

# 100. Provenance Freshness

Provenance freshness concerns whether the evidence lineage supporting a conclusion remains valid and trustworthy for current use.

Potential failure modes include:

* source invalidated,
* ancestry corrected,
* duplicated evidence discovered,
* Sybil-like multiplicity exposed,
* provenance chain broken,
* source identity changed.

These are model-level interpretations.

---

# 101. Provenance Freshness Is Not Source Freshness

L21 lists both:

```text
provenance
```

and:

```text
source
```

as separate axes.

Therefore they must not be silently collapsed.

A useful distinction is:

```text
PROVENANCE FRESHNESS:
is the lineage/ancestry relationship still valid?

SOURCE FRESHNESS:
is the underlying source itself still current/applicable?
```

This distinction is model-level but preserves the source's explicit separation.

---

# 102. Scope Freshness

Scope freshness concerns whether the conclusion's original applicability envelope still matches the target scope.

Possible scope dimensions include:

* system,
* population,
* scale,
* namespace,
* object set,
* geography,
* measurement method.

These are model-level examples.

---

# 103. Scope Expansion Can Stale a Conclusion

Example:

```text
VERIFIED FOR:
100-node system
```

applied to:

```text
10,000-node system
```

may fail scope freshness.

This does not necessarily mean the original result was wrong.

It means its applicability to the expanded scope is not established.

---

# 104. Model Freshness

Model freshness concerns whether the model used to derive or evaluate the conclusion remains the applicable model.

A result from:

```text
MODEL M1
```

may become stale after:

```text
M1 → M2
```

if the change affects load-bearing assumptions.

---

# 105. Model Freshness Is Not Temporal Freshness

A result created five minutes ago can already be model-stale if it used an obsolete model version.

Conversely, an older result may remain model-fresh if the relevant model has not changed.

Thus:

```text
MODEL FRESHNESS
≠
AGE
```

---

# 106. Source Freshness

Source freshness concerns whether the source itself remains current, authoritative, or applicable.

Examples:

```text
CANON v1
→
CANON v2
```

or:

```text
DOCUMENT S
SUPERSEDED BY S2
```

may make conclusions based on S stale on the source axis.

---

# 107. Source Freshness vs Source Authority

A source may be current but non-authoritative.

Likewise, a source may be authoritative historically but superseded.

Therefore:

```text
FRESH
≠
AUTHORITATIVE
```

Freshness and authority remain separate properties.

---

# 108. Freshness Vector Record

A model-level representation:

```yaml
freshness:

  temporal:
    status: fresh

  environmental:
    status: fresh

  regimeal:
    status: fresh

  provenance:
    status: fresh

  scope:
    status: fresh

  model:
    status: fresh

  source:
    status: fresh
```

The exact statuses are not source-defined.

---

# 109. Non-Binary Freshness

L21 does not state whether freshness axes are:

```text
BOOLEAN
```

or:

```text
CONTINUOUS
```

or:

```text
ENUMERATED
```

Possible model states include:

```text
FRESH
STALE
UNKNOWN
CONDITIONAL
NOT_APPLICABLE
```

but these are not canonical.

---

# 110. Unknown Freshness

If a load-bearing freshness axis cannot be evaluated:

```text
F_scope = UNKNOWN
```

the conclusion should not silently be treated as fully applicable.

The appropriate result may be:

```text
CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

depending on the claim.

---

# 111. Weakest Freshness Axis

A useful AMOS_MODEL principle is:

```text
APPLICABILITY CEILING
≤
WEAKEST LOAD-BEARING
FRESHNESS AXIS
```

If six axes are fresh but one critical axis is stale:

```text
FULL APPLICABILITY
IS NOT ESTABLISHED
```

---

# 112. Freshness Is Dependency-Sensitive

Not every axis is equally load-bearing for every conclusion.

Example:

```text
PURE CANONICAL DEFINITION
```

may not depend strongly on environmental freshness.

An empirical latency benchmark may depend heavily on it.

Thus the seven axes should be evaluated for relevance rather than mechanically averaged.

---

# 113. No Freshness Averaging

Invalid:

```text
6 / 7 AXES FRESH
= 85.7% FRESH
```

if the stale axis is load-bearing.

Freshness is not established as an arithmetic average by L21.

---

# 114. Temporal Freshness Failure

```text
CLAIM:
service currently available

EVIDENCE:
measurement from 2 years ago
```

may fail temporal freshness even if other axes match.

---

# 115. Environmental Freshness Failure

```text
CLAIM:
latency < 10 ms

EVIDENCE:
specialized hardware E1

TARGET:
commodity hardware E2
```

may fail environmental freshness.

---

# 116. Regimeal Freshness Failure

```text
CLAIM:
stable

EVIDENCE:
simulation regime

TARGET USE:
empirical deployment
```

without bridge routing fails regimeal applicability.

---

# 117. Provenance Freshness Failure

```text
CLAIM:
independently confirmed by 5 sources
```

may become provenance-stale if later analysis shows:

```text
ALL 5
DESCEND FROM
ONE ORIGINAL SOURCE
```

The underlying observations may remain, but the independence claim is invalidated.

---

# 118. Scope Freshness Failure

```text
CLAIM:
works for population P1

TARGET:
population P2
```

without validated transfer may fail scope freshness.

---

# 119. Model Freshness Failure

```text
RESULT:
derived using model M1

CURRENT GOVERNING MODEL:
M2
```

may fail model freshness if M2 changes a load-bearing assumption.

---

# 120. Source Freshness Failure

```text
CLAIM:
canonical rule R

SOURCE:
canon version V1

CURRENT:
V2 supersedes R
```

makes the old canonical basis source-stale.

---

# 121. Multi-Axis Failure

A conclusion can be stale on multiple axes simultaneously.

Example:

```yaml
freshness:
  temporal: stale
  environmental: stale
  regimeal: fresh
  provenance: fresh
  scope: stale
  model: stale
  source: fresh
```

The remediation should target the failed axes rather than globally recompute everything without need.

---

# 122. Freshness Repair

Conceptually:

```text
STALE AXIS
    ↓
IDENTIFY DEPENDENT CLAIMS
    ↓
REVALIDATE ONLY
AFFECTED DEPENDENCIES
    ↓
UPDATE FRESHNESS
```

This aligns with AMOS local failure recovery.

---

# 123. Temporal Repair

Temporal staleness may be repaired by:

```text
NEW OBSERVATION
```

or other evidence establishing current validity.

Exact method depends on the claim.

---

# 124. Environmental Repair

Environmental staleness may require:

```text
RETEST IN TARGET ENVIRONMENT
```

or an independently validated environment bridge.

---

# 125. Regimeal Repair

Regimeal staleness requires:

```text
EXPLICIT REGIME BRIDGE
```

and whatever target-side validation is necessary.

---

# 126. Provenance Repair

Provenance staleness may require:

* lineage reconstruction,
* source re-identification,
* independence analysis,
* removal of invalid descendants.

This is broader AMOS provenance discipline.

---

# 127. Scope Repair

Scope staleness may require:

```text
VALIDATION IN EXPANDED /
CHANGED SCOPE
```

or a justified scope bridge.

---

# 128. Model Repair

Model staleness may require:

```text
RERUN / REDERIVE
USING CURRENT MODEL
```

or establish equivalence between old and new models.

---

# 129. Source Repair

Source staleness may require:

```text
RETRIEVE CURRENT SOURCE
        ↓
COMPARE
        ↓
REVALIDATE DEPENDENT CLAIMS
```

---

# 130. Freshness and Proof Capsules

An L19 Proof Capsule should conceptually inherit relevant L21 freshness information.

Example:

```yaml
proof_capsule:
  claim: C1

  freshness:
    temporal: fresh
    environmental: fresh
    regimeal: fresh
    provenance: fresh
    scope: fresh
    model: fresh
    source: fresh
```

If a load-bearing axis becomes stale, dependent conclusions may require invalidation or revalidation.

---

# 131. Proof Capsule Freshness Failure

```text
PROOF CAPSULE
    ↓
MODEL AXIS BECOMES STALE
    ↓
WHICH PREMISES
DEPEND ON OLD MODEL?
    ↓
INVALIDATE ONLY
DEPENDENT CONCLUSIONS
```

This preserves unaffected work.

---

# 132. Freshness and RSCF

RSCF can represent claims whose validity depends on freshness.

Conceptually:

```text
RSCF CLAIM
   │
   ├─ REGIME
   ├─ SCOPE
   ├─ PROVENANCE
   └─ FRESHNESS VECTOR
```

The exact serialization belongs to RSCF canon.

---

# 133. Freshness and GMEF

A governance decision should not consume a stale load-bearing premise merely because the premise was once valid.

Conceptually:

```text
DECISION PAYLOAD
      ↓
CHECK REGIME
      ↓
CHECK FRESHNESS
      ↓
GMEF
```

This integration is model-level unless specified elsewhere.

---

# 134. Freshness and L20 Adversarial Validation

Adversarial evidence also ages.

A deterministic fuzz receipt may remain reproducible but become:

```text
MODEL-STALE
ENVIRONMENT-STALE
SOURCE-STALE
```

for a new decision.

Thus:

```text
REPRODUCIBLE
≠
CURRENTLY APPLICABLE
```

---

# 135. Freshness and Provenance Topology

A provenance graph can change epistemically without changing historical timestamps.

Example:

```text
T1:
A, B, C believed independent

T2:
common ancestor S discovered
```

The evidence may remain temporally old-but-unchanged, while:

```text
PROVENANCE FRESHNESS
```

of the independence interpretation fails.

---

# 136. Freshness and Regime Shift

A regime shift can invalidate conclusions even if:

```text
TEMPORAL AGE
=
VERY SMALL
```

Therefore regimeal freshness is independently load-bearing.

---

# 137. Freshness and Causal Claims

Causal conclusions may be especially sensitive to:

* environmental,
* regimeal,
* scope,
* model,

freshness.

A mechanism established in one regime may not transfer if causal structure changes.

---

# 138. Freshness and Competing Hypotheses

A previously weak competing hypothesis may become stronger if the evidence supporting the dominant hypothesis becomes stale.

Thus freshness changes can alter relative support without generating new observations.

---

# 139. Freshness and Confidence

A conclusion's confidence should not remain unchanged when a load-bearing freshness axis fails.

Conceptually:

```text
STALE PREMISE
        ↓
CONFIDENCE CEILING
MUST BE REASSESSED
```

Exact numeric confidence semantics are outside L21.

---

# 140. Freshness and Applicability

ER-4 states:

```text
APPLICABILITY
CARRIES
7-AXIS FRESHNESS
```

Therefore freshness is not merely metadata.

It is part of deciding whether a conclusion can be applied.

---

# 141. Applicability Envelope

A model-level applicability envelope:

```yaml
applicability:

  system:
    S1

  environment:
    E1

  scale:
    N1

  time:
    T1

  regime:
    empirical

  model:
    M1

  source:
    SRC1

  freshness:
    temporal: fresh
    environmental: fresh
    regimeal: fresh
    provenance: fresh
    scope: fresh
    model: fresh
    source: fresh
```

Only the seven axes are explicitly source-established.

---

# 142. Applicability Is Not Truth in the Abstract

A claim may have been valid in its original context while no longer applicable to the current one.

Therefore:

```text
STALE
≠
HISTORICALLY FALSE
```

and:

```text
OUT OF SCOPE
≠
REFUTED
```

This distinction prevents unnecessary global invalidation.

---

# 143. ER-4 Compact Law

```text
APPLICABILITY
      ↓
CHECK
TEMPORAL
ENVIRONMENTAL
REGIMEAL
PROVENANCE
SCOPE
MODEL
SOURCE
      ↓
LOAD-BEARING AXIS STALE?
   ┌──┴──┐
   │     │
  YES    NO
   │     │
   ▼     ▼
REPAIR / CURRENT
CONDITION USE MAY
/ GAP      PROCEED
```

---

# 144. Combined ER-1–ER-4 Flow

```text
EVALUATION
    │
    ▼
ER-1
DECLARE REGIME
    │
    ├─ SIMULATION
    ├─ EMPIRICAL
    ├─ CANONICAL
    └─ SPECULATIVE
    │
    ▼
ESTABLISH CONCLUSION
WITHIN REGIME
    │
    ▼
IF SIMULATION:
ER-3
WORST-BRANCH DRIFT
    │
    ▼
ALL BRANCHES STABLE?
    │
    ▼
ER-4
CHECK 7-AXIS FRESHNESS
    │
    ▼
TARGET USE
IN SAME REGIME?
 ┌──┴──┐
 │     │
YES    NO
 │     │
 ▼     ▼
LOCAL  ER-2
USE    FIREWALL
       │
       ▼
    EXPLICIT BRIDGE
       │
       ├─ GOVERNED PAYLOAD
       ├─ NON-PORTABLES
       └─ TARGET VALIDATION
              │
              ▼
        TARGET-REGIME
        CONCLUSION
```

---

# 145. L21 and L17 RSCF

L21 strengthens epistemic typing by requiring regime context.

Conceptually:

```text
RSCF
  claim: C
  class: DERIVED
  regime: empirical
```

is more precise than:

```text
RSCF
  claim: C
  class: DERIVED
```

when regime materially affects interpretation.

Exact RSCF fields remain governed by RSCF canon.

---

# 146. Claim Class vs Regime

Claim class and epistemic regime are different dimensions.

Example:

```text
CLAIM CLASS:
DERIVED

REGIME:
SIMULATION
```

or:

```text
CLAIM CLASS:
SOURCE_CLAIM

REGIME:
CANONICAL
```

Therefore:

```text
CLAIM_CLASS
≠
REGIME
```

---

# 147. Provenance vs Regime

Likewise:

```text
PROVENANCE:
AMOS_corpus
```

does not itself establish:

```text
REGIME:
CANONICAL
```

A corpus may contain proposed, speculative, empirical, or model-level content.

---

# 148. Canonical Source vs Canonical Status

A file located in:

```text
01_CANON/
```

does not automatically make every claim inside it canonically VERIFIED.

The supplied L21 note itself demonstrates this:

```text
source:
01_CANON/01_CORE_LAWS

canonical_status:
CONDITIONAL
```

Thus location and status remain distinct.

---

# 149. L21 and L18 GMEF

A regime bridge may itself be governed.

Conceptually:

```text
SOURCE-REGIME CLAIM
       ↓
BRIDGE PAYLOAD
       ↓
GMEF
       ↓
ALLOW / DENY
       ↓
TARGET-REGIME VALIDATION
```

This is a model-level integration suggested by the phrase:

```text
governed payload
```

but the exact governance protocol is not specified by L21.

---

# 150. L21 and L19 Proof Capsules

A Proof Capsule should conceptually preserve:

```text
CLAIM
CLASS
REGIME
SCOPE
FRESHNESS
DEPENDENCIES
FALSIFIERS
```

where these are load-bearing.

Cross-regime reuse requires ER-2 bridge discipline.

---

# 151. Proof Capsule Regime Binding

```text
PROOF CAPSULE PC1
VALID @ SIMULATION
```

does not automatically become:

```text
PC1 VALID @ EMPIRICAL
```

The capsule must either:

* remain simulation-bound, or
* produce a bridged target-regime conclusion.

---

# 152. L21 and L20 Adversarial Validation

L20 adversarial validation must itself declare regime.

Examples:

```text
SIMULATED ADVERSARIAL FUZZ
```

versus:

```text
EMPIRICAL ADVERSARIAL TEST
```

Their receipts may have different applicability.

---

# 153. Simulation Adversarial Pass

```text
ALL SIMULATED ATTACK
BRANCHES PASS
```

is a simulation-regime conclusion.

It cannot silently become:

```text
DEPLOYED SYSTEM
RESISTS ALL ATTACKS
```

---

# 154. Empirical Adversarial Pass

Even an empirical adversarial pass remains bounded by:

```text
TESTED ATTACK SET
ENVIRONMENT
TIME
SCOPE
MODEL
SOURCE
```

and other freshness axes.

---

# 155. L21 and H/M/L

Regime metadata can propagate through the fractal knowledge hierarchy.

Conceptually:

```text
H DOMAIN
   ↓
M SUBSYSTEM
   ↓
L DETAIL
```

Each retrieved claim should preserve its regime where material.

A higher-level synthesis must not erase regime differences between lower-level premises.

---

# 156. Cross-Level Regime Conflict

Example:

```text
H:
CANONICAL RULE SAYS X

L:
EMPIRICAL OBSERVATION SHOWS NOT-X
```

This is not automatically a contradiction in the same epistemic sense.

It may indicate:

```text
CANON / IMPLEMENTATION
MISMATCH
```

which should remain visible.

---

# 157. Canonical vs Empirical Conflict

Example:

```text
CANONICAL:
system must reject operation O

EMPIRICAL:
deployed system accepts O
```

Correct interpretation:

```text
CANONICAL REQUIREMENT:
REJECT O

EMPIRICAL BEHAVIOR:
ACCEPT O

STATUS:
IMPLEMENTATION / CANON
MISMATCH
```

Do not average them into:

```text
system sometimes should accept O
```

unless canon says so.

---

# 158. Simulation vs Empirical Conflict

Example:

```text
SIMULATION:
stable

EMPIRICAL:
unstable
```

The conflict should remain explicit.

Possible explanations include:

* simulation model incomplete,
* environment mismatch,
* implementation difference,
* measurement error,
* regime bridge invalid.

No unique cause is established automatically.

---

# 159. Speculative vs Empirical Conflict

If:

```text
SPECULATIVE:
H predicts X
```

but:

```text
EMPIRICAL:
not-X observed
```

then H may be weakened or falsified depending on its exact prediction and scope.

Do not preserve speculation against direct falsifying evidence unless the hypothesis has legitimate escape conditions.

---

# 160. Canonical vs Speculative Conflict

A speculative alternative cannot override canonical authority merely because it appears more elegant.

It may motivate a governance proposal, but:

```text
SPECULATIVE PREFERENCE
≠
CANONICAL SUPERSESSION
```

---

# 161. L21 and Provenance Topology

Regime and provenance are orthogonal.

Two empirical reports may share one source ancestry.

Likewise, two simulation branches may derive from one model.

Therefore:

```text
SAME REGIME
≠
INDEPENDENT EVIDENCE
```

---

# 162. L21 and Sybil Hardening

Multiple claims labeled:

```text
EMPIRICAL
```

do not constitute multiple independent empirical confirmations if they share a single origin.

Regime typing does not replace provenance-independence analysis.

---

# 163. L21 and Causal Firewall

Causal inference must respect regime boundaries.

Examples:

```text
SIMULATION CAUSAL EFFECT
```

is a causal result inside the simulation model.

```text
EMPIRICAL CAUSAL EFFECT
```

requires appropriately typed empirical evidence.

```text
CANONICAL CAUSAL RULE
```

may describe a specified mechanism but does not automatically establish deployed empirical causation.

---

# 164. L21 and Structural Similarity

If a simulation structurally resembles a real system:

```text
SIMILAR STRUCTURE
```

does not establish:

```text
SAME CAUSAL BEHAVIOR
```

Cross-regime mapping remains MODEL until validated.

---

# 165. L21 and Sensitivity

A regime bridge may be fragile to one assumption.

Example:

```text
SIMULATION → EMPIRICAL
```

depends critically on:

```text
network delay distribution
matches deployment
```

If a small mismatch flips the conclusion, the bridged result should be marked CONDITIONAL.

---

# 166. L21 and Adaptive Complexity

Regime complexity should escalate when:

* multiple regimes are mixed,
* a conclusion must cross regimes,
* freshness axes conflict,
* simulation branches disagree,
* provenance is correlated,
* causal transfer is attempted,
* governance depends on the result.

Simple regime-local claims can remain compact.

---

# 167. L21 and Failure Recovery

If one freshness axis fails:

```text
MODEL = STALE
```

do not invalidate unrelated conclusions that do not depend on that model.

Instead:

```text
FAILED AXIS
    ↓
DEPENDENCY EDGES
    ↓
AFFECTED CONCLUSIONS
    ↓
LOCAL REVALIDATION
```

---

# 168. L21 and Anti-Regression

An optimization that removes regime labels to save tokens violates ER-1 if regime matters.

An optimization that silently reuses simulation conclusions empirically violates ER-2.

An optimization that reports average simulation stability while hiding one unstable branch violates ER-3.

An optimization that reduces seven freshness axes to one timestamp violates ER-4.

Therefore epistemic compression may not erase load-bearing regime information.

---

# 169. L21 and Knowledge Harvest

Knowledge harvest should preserve regime.

Conceptually:

```text
EPHEMERAL RESULT
      ↓
PERSISTENT EVIDENCE
      ↓
REGIME DECLARED
      ↓
FRESHNESS ATTACHED
      ↓
VALIDATED KNOWLEDGE
```

A result changing regimes requires bridge routing, not simple relabeling.

---

# 170. Documentation Claims

A README statement:

```text
"simulation proves production stability"
```

remains a SOURCE_CLAIM until the required bridge is validated.

ER-2 prevents accepting the regime crossing merely because documentation asserts it.

---

# 171. Benchmark Claims

A benchmark measured under:

```text
EMPIRICAL
ENVIRONMENT E1
MODEL M1
TIME T1
```

does not automatically apply to:

```text
ENVIRONMENT E2
MODEL M2
TIME T2
```

Freshness axes must be checked.

---

# 172. Reported Latency

A latency result can be:

```text
EMPIRICAL
```

while remaining environment-bound.

Therefore:

```text
LATENCY = 5 ms @ E1
```

does not establish:

```text
LATENCY = 5 ms
HARDWARE-INDEPENDENT
```

---

# 173. Formal Proof Regime

The source-defined regime list does not explicitly include:

```text
formal
```

Therefore L21 does not establish `formal` as a fifth regime.

A formal proof may need to be represented within another applicable regime or under additional canon.

Do not silently extend the four-regime set as canonical.

---

# 174. Hybrid Regime

Likewise, the source does not define:

```text
hybrid
```

as a regime.

Mixed evidence can be represented through typed components without inventing a fifth canonical regime.

---

# 175. Unknown Regime

Although ER-1 requires declaration, an evaluator may encounter legacy material whose regime is unavailable.

Then:

```text
REGIME:
UNKNOWN/GAP
```

is preferable to fabricated classification.

`UNKNOWN` is a conclusion/gap state, not necessarily a fifth L21 regime.

---

# 176. Regime Bridge Matrix

A model-level matrix:

| Source      | Target      | Silent transfer allowed? |
| ----------- | ----------- | -----------------------: |
| Simulation  | Empirical   |                       No |
| Simulation  | Canonical   |                       No |
| Simulation  | Speculative |    No automatic transfer |
| Empirical   | Simulation  |                       No |
| Empirical   | Canonical   |                       No |
| Empirical   | Speculative |    No automatic transfer |
| Canonical   | Simulation  |                       No |
| Canonical   | Empirical   |                       No |
| Canonical   | Speculative |    No automatic transfer |
| Speculative | Simulation  |                       No |
| Speculative | Empirical   |                       No |
| Speculative | Canonical   |                       No |

The source law establishes the general firewall, not this exact matrix.

---

# 177. Same-Regime Transfer

ER-2 specifically governs crossing regimes.

Same-regime reuse may still fail due to:

* stale source,
* stale model,
* environment change,
* scope mismatch,
* provenance change,
* temporal change.

Thus:

```text
SAME REGIME
≠
AUTOMATIC APPLICABILITY
```

ER-4 still applies.

---

# 178. Regime Firewall Validator

```python
def cross_regime_allowed(
    source_regime,
    target_regime,
    bridge
):

    if source_regime == target_regime:
        return True

    if bridge is None:
        return False

    if not bridge.explicit:
        return False

    if not bridge.governed_payload:
        return False

    if not bridge.non_portables_declared:
        return False

    return True
```

Semantic pseudocode only. Exact bridge semantics are unspecified.

---

# 179. Simulation Stability Validator

```python
def stable_simulation(branches):

    if not branches:
        return "GAP"

    for branch in branches:
        if not branch.stable:
            return False

    return True
```

This models ER-3 but does not define canonical branch membership.

---

# 180. Freshness Validator

```python
FRESHNESS_AXES = [
    "temporal",
    "environmental",
    "regimeal",
    "provenance",
    "scope",
    "model",
    "source",
]

def freshness_complete(applicability):

    for axis in FRESHNESS_AXES:
        if axis not in applicability.freshness:
            return False

    return True
```

This checks presence only, not validity semantics.

---

# 181. Applicability Validator

A model-level validator:

```python
def applicable(claim, target):

    if not claim.regime:
        return "GAP"

    freshness = evaluate_freshness(
        claim,
        target
    )

    if freshness.has_load_bearing_stale_axis:
        return False

    if claim.regime != target.regime:

        bridge = find_bridge(
            claim.regime,
            target.regime
        )

        if not valid_bridge(bridge):
            return False

    return True
```

Semantic pseudocode only.

---

# 182. Epistemic Regime Integrity Invariants

```yaml
epistemic_regime_integrity_invariants:

  ER_I1_DECLARATION:
    requirement:
      every_evaluation_declares_regime

  ER_I2_SIMULATION:
    requirement:
      simulation_is_source_defined_regime

  ER_I3_EMPIRICAL:
    requirement:
      empirical_is_source_defined_regime

  ER_I4_CANONICAL:
    requirement:
      canonical_is_source_defined_regime

  ER_I5_SPECULATIVE:
    requirement:
      speculative_is_source_defined_regime

  ER_I6_FIREWALL:
    requirement:
      conclusions_do_not_cross_regimes_implicitly

  ER_I7_EXPLICIT_BRIDGE:
    requirement:
      cross_regime_transfer_requires_explicit_bridge_routing

  ER_I8_GOVERNED_PAYLOAD:
    requirement:
      bridge_routing_uses_governed_payload

  ER_I9_NON_PORTABLES:
    requirement:
      non_portables_are_declared

  ER_I10_WORST_BRANCH:
    requirement:
      simulation_counts_worst_branch_drift

  ER_I11_ALL_BRANCH_STABILITY:
    requirement:
      stable_simulation_verdict_requires_all_branches_stable

  ER_I12_TEMPORAL:
    requirement:
      applicability_carries_temporal_freshness

  ER_I13_ENVIRONMENTAL:
    requirement:
      applicability_carries_environmental_freshness

  ER_I14_REGIMEAL:
    requirement:
      applicability_carries_regimeal_freshness

  ER_I15_PROVENANCE:
    requirement:
      applicability_carries_provenance_freshness

  ER_I16_SCOPE:
    requirement:
      applicability_carries_scope_freshness

  ER_I17_MODEL:
    requirement:
      applicability_carries_model_freshness

  ER_I18_SOURCE:
    requirement:
      applicability_carries_source_freshness
```

These closely restate ER-1 through ER-4.

---

# 183. Extended Epistemic Invariants

```yaml
extended_epistemic_invariants:

  ER_E1_NO_REGIME_LAUNDERING:
    requirement:
      regime_transfer_does_not_upgrade_claim_without_validation

  ER_E2_DIRECTIONAL_BRIDGES:
    requirement:
      bridge_validity_is_not_assumed_bidirectional

  ER_E3_NON_PORTABLE_PERSISTENCE:
    requirement:
      lost_properties_do_not_reappear_without_revalidation

  ER_E4_NO_FRESHNESS_AVERAGING:
    requirement:
      stale_load_bearing_axis_is_not_hidden_by_fresh_axes

  ER_E5_LOCAL_INVALIDATION:
    requirement:
      freshness_failure_invalidates_only_dependent_claims

  ER_E6_CAUSAL_FIREWALL:
    requirement:
      causal_claims_do_not_cross_regimes_without_licensed_evidence

  ER_E7_PROVENANCE_INDEPENDENCE:
    requirement:
      same_regime_does_not_imply_independent_provenance

  ER_E8_SCOPE_FIREWALL:
    requirement:
      same_regime_does_not_license_scope_expansion

  ER_E9_BRANCH_COVERAGE:
    requirement:
      all_branch_claims_expose_actual_branch_universe

  ER_E10_NO_SIMULATION_TO_REALITY_SHORTCUT:
    requirement:
      simulation_verdict_is_not_relabelled_empirical
```

These are AMOS_MODEL extensions.

---

# 184. Epistemic Anti-Patterns

## ER-A1 — Missing Regime

```text
"THE RESULT IS VALID"
```

with no regime declaration.

Fails ER-1.

---

## ER-A2 — Regime by Implication

```text
"obviously this was empirical"
```

without explicit declaration.

Does not satisfy ER-1.

---

## ER-A3 — Simulation Laundering

```text
SIMULATION PASSED
↓
PRODUCTION VERIFIED
```

Rejected by ER-2.

---

## ER-A4 — Empirical-to-Canon Laundering

```text
EVERY IMPLEMENTATION
WE OBSERVED DOES X
↓
X IS CANON
```

Rejected without canonical bridge/governance.

---

## ER-A5 — Canon-to-Empirical Laundering

```text
CANON REQUIRES X
↓
DEPLOYMENT DOES X
```

Rejected without empirical validation.

---

## ER-A6 — Speculation Laundering

```text
PLAUSIBLE HYPOTHESIS
↓
ESTABLISHED FACT
```

Rejected.

---

## ER-A7 — Undeclared Non-Portable

```text
SIMULATOR-SPECIFIC ASSUMPTION
↓
BRIDGE
↓
TARGET CLAIM
```

with the assumption silently preserved.

Rejected by ER-2's non-portable declaration discipline.

---

## ER-A8 — Majority Branch Stability

```text
99% STABLE
↓
STABLE VERDICT
```

Rejected if a relevant unstable branch remains.

---

## ER-A9 — Average Hides Worst Branch

```text
AVERAGE DRIFT LOW
↓
IGNORE CATASTROPHIC BRANCH
```

Rejected by ER-3.

---

## ER-A10 — Sampled Means All

```text
1000 SAMPLED BRANCHES STABLE
↓
ALL POSSIBLE BRANCHES STABLE
```

Rejected unless exhaustive inference is independently established.

---

## ER-A11 — Timestamp-Only Freshness

```text
UPDATED TODAY
↓
FRESH
```

while model/source/environment are stale.

Rejected by ER-4.

---

## ER-A12 — Freshness Averaging

```text
6/7 FRESH
↓
PASS
```

Rejected where the stale axis is load-bearing.

---

## ER-A13 — Same Regime Means Same Scope

```text
EMPIRICAL @ P1
↓
EMPIRICAL @ P2
```

without scope validation.

Rejected.

---

## ER-A14 — Current Source Means Valid Provenance

```text
SOURCE CURRENT
↓
PROVENANCE INDEPENDENT
```

Rejected. Source and provenance freshness are distinct.

---

## ER-A15 — Old Means False

```text
STALE
↓
FALSE
```

Rejected.

Staleness concerns applicability, not necessarily historical truth.

---

# 185. Epistemic Regime Decision Matrix

| Condition                                   | Source-grounded treatment                                |
| ------------------------------------------- | -------------------------------------------------------- |
| Evaluation begins                           | Declare simulation / empirical / canonical / speculative |
| Regime missing                              | ER-1 not satisfied                                       |
| Conclusion remains in same regime           | ER-2 bridge not triggered, but ER-4 still applies        |
| Conclusion crosses regime                   | Explicit bridge routing required                         |
| Bridge payload unspecified                  | Bridge incomplete                                        |
| Non-portables undeclared                    | Bridge incomplete                                        |
| Simulation has one unstable relevant branch | Stable verdict not licensed                              |
| All relevant simulation branches stable     | ER-3 stability condition satisfied                       |
| Applicability evaluated                     | Carry seven freshness axes                               |
| Authoritative regime canon changes axis set | F1 potentially satisfied                                 |

---

# 186. Extended Decision Matrix

| Condition                                 | Model-level treatment                        |
| ----------------------------------------- | -------------------------------------------- |
| Same regime, environment changed          | Check environmental freshness                |
| Same regime, model changed                | Check model freshness                        |
| Same regime, source superseded            | Check source freshness                       |
| Simulation → empirical                    | Bridge + empirical validation                |
| Empirical → canonical                     | Governance/canonical authority required      |
| Canonical → empirical                     | Empirical implementation validation required |
| Speculative → empirical                   | Obtain empirical evidence                    |
| Multiple regimes support different claims | Preserve typed conclusions                   |
| Freshness axis unknown and load-bearing   | CONDITIONAL or GAP                           |
| Branch universe incomplete                | Do not claim all-branch stability            |
| Provenance ancestry changes               | Reassess provenance freshness                |
| Regime shift occurs                       | Reassess regimeal freshness                  |

---

# 187. Minimal Epistemic Evaluation Record

```yaml
epistemic_evaluation:

  claim:
    C1

  regime:
    null

  applicability:

    freshness:
      temporal: null
      environmental: null
      regimeal: null
      provenance: null
      scope: null
      model: null
      source: null

  bridge:
    null
```

This is a model representation, not canonical schema.

---

# 188. Full Epistemic Evaluation Record

```yaml
epistemic_evaluation:

  evaluation_id:
    ER_EVAL_1

  claim:
    C1

  claim_class:
    DERIVED

  regime:
    empirical

  provenance:
    sources: []

  scope:
    system: null
    population: null
    scale: null
    environment: null
    measurement_method: null

  applicability:

    freshness:

      temporal:
        status: null

      environmental:
        status: null

      regimeal:
        status: null

      provenance:
        status: null

      scope:
        status: null

      model:
        status: null

      source:
        status: null

  cross_regime_use:
    target_regime: null

  bridge:
    bridge_id: null
    governed_payload: []
    non_portables: []
    target_validation: []

  status:
    CONDITIONAL
```

All serialization details beyond the four laws are AMOS_MODEL.

---

# 189. Regime Bridge Record

```yaml
regime_bridge:

  bridge_id:
    RB1

  source:
    regime: simulation
    claim: C1

  target:
    regime: empirical
    claim: C2

  governed_payload:
    - failure_condition_F

  non_portables:
    - simulator_probability
    - synthetic_environment_assumption

  target_validation:
    - empirical_test_F

  provenance:
    source_evidence: []
    bridge_evidence: []

  freshness:
    temporal: null
    environmental: null
    regimeal: null
    provenance: null
    scope: null
    model: null
    source: null
```

Model-level schema only.

---

# 190. Simulation Evaluation Record

```yaml
simulation_evaluation:

  evaluation_id:
    SIM1

  regime:
    simulation

  branch_universe:
    definition: null

  branches:
    []

  worst_branch:
    id: null
    drift: null

  all_branches_stable:
    null

  verdict:
    null

  freshness:
    temporal: null
    environmental: null
    regimeal: null
    provenance: null
    scope: null
    model: null
    source: null
```

The source does not define this serialization.

---

# 191. L21 Source-Established Content

From the supplied L21 note, the following are directly established as AMOS corpus claims:

```text
1. L21 is a proposed specification.

2. Its epistemic class is AMOS_MODEL.

3. Its canonical status is CONDITIONAL.

4. Every evaluation states its regime.

5. Simulation is an explicitly named regime.

6. Empirical is an explicitly named regime.

7. Canonical is an explicitly named regime.

8. Speculative is an explicitly named regime.

9. Conclusions do not cross regimes without explicit bridge routing.

10. Bridge routing includes a governed payload.

11. Bridge routing requires non-portables to be declared.

12. Simulations count worst-branch drift.

13. Stable simulation verdicts require all branches stable.

14. Applicability carries seven-axis freshness.

15. Temporal is an explicit freshness axis.

16. Environmental is an explicit freshness axis.

17. Regimeal is an explicit freshness axis.

18. Provenance is an explicit freshness axis.

19. Scope is an explicit freshness axis.

20. Model is an explicit freshness axis.

21. Source is an explicit freshness axis.

22. The stated falsifier is authoritative regime canon defining a different axis set.
```

These are SOURCE_CLAIM statements about the supplied AMOS corpus note.

---

# 192. L21 Not Established by Source

The supplied source does **not** establish:

* exact formal definition of epistemic regime,
* whether the four named regimes are exhaustive,
* exact definition of simulation,
* exact definition of empirical,
* exact definition of canonical,
* exact definition of speculative,
* mixed-regime representation,
* bridge schema,
* bridge authority mechanism,
* bridge validation algorithm,
* governed payload schema,
* exact definition of non-portable,
* complete non-portable taxonomy,
* whether bridges are directional,
* whether bridges compose transitively,
* exact branch-generation semantics,
* exact definition of relevant branch,
* exact definition of drift,
* scalar versus vector drift,
* exact stability threshold,
* treatment of impossible branches,
* treatment of low-probability branches,
* exhaustive branch-search requirements,
* exact freshness representation,
* freshness thresholds,
* freshness decay functions,
* freshness aggregation,
* axis weighting,
* exact meaning of `regimeal`,
* exact remediation protocol for stale axes,
* exact RSCF integration,
* exact GMEF integration,
* exact L19/L20 integration,
* literal runtime implementation.

These remain MODEL or UNKNOWN/GAP.

---

# 193. L21 Known Gaps

```yaml
gaps:

  G1:
    severity: CRITICAL
    description:
      >
        Authoritative epistemic-regime canon is not supplied.
        L21 therefore remains CONDITIONAL.

  G2:
    severity: DECISION_RELEVANT
    description:
      >
        It is not established whether simulation, empirical,
        canonical, and speculative exhaust the authoritative
        regime set.

  G3:
    severity: DECISION_RELEVANT
    description:
      >
        Exact regime definitions and mixed-regime semantics
        are unspecified.

  G4:
    severity: DECISION_RELEVANT
    description:
      >
        Explicit bridge-routing protocol and governed-payload
        schema are unspecified.

  G5:
    severity: DECISION_RELEVANT
    description:
      >
        Exact definition and representation of non-portables
        are unspecified.

  G6:
    severity: DECISION_RELEVANT
    description:
      >
        Relevant simulation branch universe is unspecified.

  G7:
    severity: DECISION_RELEVANT
    description:
      >
        Worst-branch drift metric and ordering are unspecified.

  G8:
    severity: DECISION_RELEVANT
    description:
      >
        Canonical simulation stability predicate is unspecified.

  G9:
    severity: DECISION_RELEVANT
    description:
      >
        Freshness axis status representation and thresholds
        are unspecified.

  G10:
    severity: DECISION_RELEVANT
    description:
      >
        Exact semantics of regimeal freshness are unspecified.

  G11:
    severity: DECISION_RELEVANT
    description:
      >
        Interaction among multiple stale/unknown freshness
        axes is unspecified.

  G12:
    severity: EXPLANATORY
    description:
      >
        Exact integration with RSCF, GMEF, Proof Capsules,
        adversarial validation, H/M/L, provenance topology,
        and failure recovery is not defined by this note.
```

---

# 194. L21 Claim Graph

```yaml
claim_graph:

  ER_C001:
    class: SOURCE
    claim:
      Every evaluation states its regime.

  ER_C002:
    class: SOURCE
    claim:
      Simulation is an explicitly named regime.

  ER_C003:
    class: SOURCE
    claim:
      Empirical is an explicitly named regime.

  ER_C004:
    class: SOURCE
    claim:
      Canonical is an explicitly named regime.

  ER_C005:
    class: SOURCE
    claim:
      Speculative is an explicitly named regime.

  ER_C006:
    class: SOURCE
    claim:
      Conclusions do not cross regimes without explicit bridge routing.

  ER_C007:
    class: SOURCE
    claim:
      Bridge routing includes governed payload.

  ER_C008:
    class: SOURCE
    claim:
      Non-portables are declared during bridge routing.

  ER_C009:
    class: SOURCE
    claim:
      Simulations count worst-branch drift.

  ER_C010:
    class: SOURCE
    claim:
      Stable verdicts require all simulation branches stable.

  ER_C011:
    class: SOURCE
    claim:
      Applicability carries seven-axis freshness.

  ER_C012:
    class: SOURCE
    claim:
      Temporal is a freshness axis.

  ER_C013:
    class: SOURCE
    claim:
      Environmental is a freshness axis.

  ER_C014:
    class: SOURCE
    claim:
      Regimeal is a freshness axis.

  ER_C015:
    class: SOURCE
    claim:
      Provenance is a freshness axis.

  ER_C016:
    class: SOURCE
    claim:
      Scope is a freshness axis.

  ER_C017:
    class: SOURCE
    claim:
      Model is a freshness axis.

  ER_C018:
    class: SOURCE
    claim:
      Source is a freshness axis.

  ER_C019:
    class: DERIVED
    claim:
      >
        A simulation conclusion cannot silently be relabelled
        as an empirical conclusion.

  ER_C020:
    class: DERIVED
    claim:
      >
        One unstable relevant simulation branch prevents
        an ER-3 stable verdict.

  ER_C021:
    class: DERIVED
    claim:
      >
        Temporal recency alone does not establish complete
        seven-axis freshness.

  ER_C022:
    class: MODEL
    claim:
      >
        Regime and freshness metadata can be carried through
        RSCF and Proof Capsules.

  ER_C023:
    class: MODEL
    claim:
      >
        Cross-regime bridge validation can be governed by GMEF.

  ER_C024:
    class: UNKNOWN
    claim:
      >
        Exact authoritative regime definitions, bridge protocol,
        branch semantics, drift metric, and freshness thresholds.
```

---

# 195. Dependency Graph

```yaml
dependency_graph:

  ER_1:
    depends_on:
      - evaluation_identity
      - regime_taxonomy
      - regime_declaration

  ER_2:
    depends_on:
      - source_regime
      - target_regime
      - bridge_identity
      - governed_payload
      - non_portables
      - target_validation

  ER_3:
    depends_on:
      - simulation_identity
      - branch_universe
      - branch_stability
      - drift_definition
      - worst_branch_selection

  ER_4:
    depends_on:
      - applicability_scope
      - temporal_freshness
      - environmental_freshness
      - regimeal_freshness
      - provenance_freshness
      - scope_freshness
      - model_freshness
      - source_freshness
```

---

# 196. L21 Self-Proof Capsule

```yaml
proof_capsule:

  claim:
    >
      L21 proposes an epistemic-regime discipline in which
      every evaluation declares simulation, empirical,
      canonical, or speculative regime; conclusions cannot
      cross regimes without explicit bridge routing using a
      governed payload and declared non-portables; simulations
      use worst-branch pessimism and require all branches stable
      for a stable verdict; and applicability carries temporal,
      environmental, regimeal, provenance, scope, model, and
      source freshness.

  class:
    CONDITIONAL

  established:
    - ER_1_explicitly_requires_declared_regime
    - simulation_is_explicitly_named
    - empirical_is_explicitly_named
    - canonical_is_explicitly_named
    - speculative_is_explicitly_named
    - ER_2_explicitly_prohibits_unbridged_cross_regime_transfer
    - ER_2_explicitly_names_governed_payload
    - ER_2_explicitly_requires_non_portables_declared
    - ER_3_explicitly_requires_worst_branch_drift
    - ER_3_explicitly_requires_all_branches_stable
    - ER_4_explicitly_defines_seven_freshness_axes
    - temporal_axis_explicit
    - environmental_axis_explicit
    - regimeal_axis_explicit
    - provenance_axis_explicit
    - scope_axis_explicit
    - model_axis_explicit
    - source_axis_explicit
    - source_marks_L21_as_PROPOSED_SPECIFICATION
    - source_marks_L21_as_AMOS_MODEL
    - source_marks_L21_as_CONDITIONAL

  not_established:
    - authoritative_complete_regime_canon
    - exhaustive_regime_taxonomy
    - exact_regime_definitions
    - exact_bridge_protocol
    - exact_non_portable_schema
    - exact_simulation_branch_universe
    - exact_drift_metric
    - exact_stability_threshold
    - exact_freshness_status_model
    - exact_freshness_thresholds
    - literal_runtime_implementation

  load_bearing_gaps:
    - authoritative_regime_canon_not_supplied
    - authoritative_axis_set_not_independently_validated
    - bridge_semantics_not_supplied
    - branch_universe_not_supplied
    - drift_semantics_not_supplied
    - freshness_thresholds_not_supplied

  falsifiers:
    - >
      Authoritative regime canon defines a materially
      different freshness-axis set.

  confidence_ceiling:
    CONDITIONAL
```

---

# 197. No Circular Self-Validation

Invalid:

```text
L21 DEFINES
EPISTEMIC VALIDATION
        ↓
L21 IS ANALYZED
USING ITS OWN RULES
        ↓
L21 BECOMES VERIFIED
```

Correct:

```text
L21
PROPOSED_SPECIFICATION
        ↓
SELF-PROOF CAPSULE
        ↓
STRUCTURES
SOURCE SUPPORT
        ↓
STILL CONDITIONAL
```

Self-consistency is not independent canonical validation.

---

# 198. Falsifier F1

Original falsifier:

> **authoritative regime canon defines different axis set.**

Operationally:

```text
RECOVER AUTHORITATIVE
REGIME CANON
        ↓
EXTRACT FRESHNESS AXES
        ↓
COMPARE WITH L21:
TEMPORAL
ENVIRONMENTAL
REGIMEAL
PROVENANCE
SCOPE
MODEL
SOURCE
        ↓
MATERIAL DIFFERENCE?
   ┌────┴────┐
   │         │
  NO        YES
   │         │
   ▼         ▼
PRESERVE   F1 MAY
PROPOSAL   SUCCEED
              ↓
          GOVERNED
          REVISION /
          SUPERSESSION
```

---

# 199. F1 Is Axis-Specific

The stated falsifier specifically concerns:

```text
different axis set
```

Therefore a difference in:

* YAML field names,
* ordering,
* display format,
* implementation language,

does not itself satisfy F1.

The difference must concern the authoritative freshness-axis set.

---

# 200. Axis Renaming

If authoritative canon uses a different label for an equivalent concept, this may be:

```text
TERMINOLOGICAL DIFFERENCE
```

rather than:

```text
MATERIAL AXIS-SET DIFFERENCE
```

Semantic equivalence would need to be established rather than assumed.

---

# 201. Axis Addition

Suppose authoritative canon defines:

```text
7 L21 AXES
+
AXIS 8
```

Whether this falsifies L21 depends on whether L21 claims exhaustiveness.

The source says:

```text
applicability carries 7-axis freshness
```

which strongly suggests a seven-axis set, but exact supersession treatment remains governed by authoritative canon.

---

# 202. Axis Removal

If authoritative canon defines six axes and explicitly rejects one L21 axis, that would constitute a more direct conflict with ER-4.

---

# 203. Axis Merge

If authoritative canon merges:

```text
PROVENANCE
+
SOURCE
```

into one axis, this would materially alter L21's explicit seven-axis structure unless an equivalence mapping preserves the same semantics.

---

# 204. Axis Split

If authoritative canon splits one L21 axis into multiple independent axes, L21 may become incomplete even if not wholly wrong.

The appropriate status could become:

```text
CONDITIONAL
SUPERSEDED
PARTIALLY COMPATIBLE
```

depending on governance canon.

---

# 205. Regime Architecture

```text
                     EVALUATION
                         │
                         ▼
                  DECLARE REGIME
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
  SIMULATION         EMPIRICAL         CANONICAL
       │                 │                 │
       └────────────┬────┴────────────┬────┘
                    │                 │
                    ▼                 ▼
               SPECULATIVE       REGIME-LOCAL
                                  CONCLUSION
                                      │
                                      ▼
                              CHECK FRESHNESS
                                      │
                     ┌────────────────┼───────────────┐
                     │                │               │
                  TEMPORAL      ENVIRONMENTAL     REGIMEAL
                     │                │               │
                     ├────────────┬───┴────┬──────────┤
                     │            │        │          │
                 PROVENANCE     SCOPE    MODEL      SOURCE
                     │            │        │          │
                     └────────────┴────┬───┴──────────┘
                                      │
                                      ▼
                                TARGET USE
                                      │
                              SAME REGIME?
                               ┌──────┴──────┐
                               │             │
                              YES            NO
                               │             │
                               ▼             ▼
                           LOCAL USE     REGIME FIREWALL
                                             │
                                             ▼
                                       EXPLICIT BRIDGE
                                             │
                                  ┌──────────┴──────────┐
                                  │                     │
                                  ▼                     ▼
                           GOVERNED PAYLOAD       NON-PORTABLES
                                                      DECLARED
                                  │                     │
                                  └──────────┬──────────┘
                                             │
                                             ▼
                                      TARGET VALIDATION
```

---

# 206. Simulation Architecture

```text
SIMULATION
    │
    ▼
DECLARE BRANCH UNIVERSE
    │
    ▼
BRANCHES
 ┌──┼──┬──┐
 ▼  ▼  ▼  ▼
b1 b2 b3 ... bn
 │  │  │      │
 ▼  ▼  ▼      ▼
DRIFT / STABILITY
 │  │  │      │
 └──┴──┴──┬───┘
          │
          ▼
   WORST-BRANCH DRIFT
          │
          ▼
 ALL BRANCHES STABLE?
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
  NOT STABLE STABLE
              WITHIN
            SIMULATION
              REGIME
```

---

# 207. Seven-Axis Freshness Architecture

```text
                 APPLICABILITY
                      │
                      ▼
               FRESHNESS VECTOR
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
  TEMPORAL       ENVIRONMENTAL      REGIMEAL
      │               │               │
      ├──────────┬────┴────┬──────────┤
      │          │         │          │
      ▼          ▼         ▼          ▼
 PROVENANCE    SCOPE     MODEL      SOURCE
      │          │         │          │
      └──────────┴────┬────┴──────────┘
                      │
                      ▼
            LOAD-BEARING AXES
                 CURRENT?
                ┌───┴───┐
                │       │
               NO      YES
                │       │
                ▼       ▼
            REVALIDATE  APPLICABILITY
            / CONDITION MAY REMAIN
            / GAP       VALID
```

---

# 208. Canonical Epistemic Compression

```text
EVERY EVALUATION
=
DECLARED REGIME
```

```text
REGIME SET NAMED BY L21
=
SIMULATION
EMPIRICAL
CANONICAL
SPECULATIVE
```

```text
CROSS-REGIME CONCLUSION
=
NO SILENT TRANSFER
```

```text
VALID BRIDGE ROUTING
=
GOVERNED PAYLOAD
+
NON-PORTABLES DECLARED
```

```text
SIMULATION STABLE
⇒
ALL BRANCHES STABLE
```

```text
SIMULATION DRIFT
=
WORST-BRANCH SENSITIVE
```

```text
APPLICABILITY
=
7-AXIS FRESHNESS
```

```text
FRESHNESS AXES
=
TEMPORAL
+
ENVIRONMENTAL
+
REGIMEAL
+
PROVENANCE
+
SCOPE
+
MODEL
+
SOURCE
```

---

# 209. Canonical One-Line Law

> **AMOS epistemic evaluation declares its regime, prevents conclusions from silently crossing simulation, empirical, canonical, and speculative boundaries without governed bridge routing and declared non-portables, treats simulation stability pessimistically across all branches, and binds applicability to seven-axis freshness across time, environment, regime, provenance, scope, model, and source.**

---

# 210. Canonical Equations

ER-1:

```text
Evaluation(E)
⇒
DeclaredRegime(E)
```

with:

```text
DeclaredRegime(E)
∈
{
Simulation,
Empirical,
Canonical,
Speculative
}
```

This set is explicitly named by the source; whether it is globally exhaustive outside L21 remains conditional.

ER-2:

```text
Regime(C_source)
≠
Regime(C_target)
⇒
ExplicitBridgeRequired
```

and:

```text
Bridge
⇒
GovernedPayload
∧
DeclaredNonPortables
```

ER-3:

```text
StableSimulation
⇒
∀b ∈ B : Stable(b)
```

and conceptually:

```text
SimulationAssessment
is sensitive to
WorstBranchDrift(B)
```

ER-4:

```text
Freshness(C)
=
[
Temporal,
Environmental,
Regimeal,
Provenance,
Scope,
Model,
Source
]
```

These equations are semantic compressions, not formal proofs.

---

# 211. Operational Contract

```yaml
epistemic_regime_contract:

  ER_1_DECLARED_REGIME:
    establishes:
      - every_evaluation_states_regime
      - simulation_is_named_regime
      - empirical_is_named_regime
      - canonical_is_named_regime
      - speculative_is_named_regime

  ER_2_REGIME_FIREWALL:
    establishes:
      - conclusions_do_not_cross_regimes_implicitly
      - explicit_bridge_routing_is_required
      - bridge_uses_governed_payload
      - non_portables_are_declared

  ER_3_SIMULATION_PESSIMISM:
    establishes:
      - simulations_count_worst_branch_drift
      - stable_verdict_requires_all_branches_stable

  ER_4_FRESHNESS_AXES:
    establishes:
      - applicability_carries_temporal_freshness
      - applicability_carries_environmental_freshness
      - applicability_carries_regimeal_freshness
      - applicability_carries_provenance_freshness
      - applicability_carries_scope_freshness
      - applicability_carries_model_freshness
      - applicability_carries_source_freshness
```

---

# 212. Final Epistemic Regime Invariant

```text
EVALUATION
      ↓
DECLARE REGIME
      ↓
SIMULATION /
EMPIRICAL /
CANONICAL /
SPECULATIVE
      ↓
ESTABLISH RESULT
LOCALLY
      ↓
IF SIMULATION:
COUNT WORST-BRANCH DRIFT
      ↓
ALL BRANCHES STABLE?
      │
      ├── NO → NO STABLE VERDICT
      │
      └── YES
             ↓
CHECK APPLICABILITY
      ↓
TEMPORAL
ENVIRONMENTAL
REGIMEAL
PROVENANCE
SCOPE
MODEL
SOURCE
      ↓
TARGET REGIME
SAME AS SOURCE?
      │
      ├── YES
      │     ↓
      │  LOCAL USE
      │  SUBJECT TO
      │  FRESHNESS
      │
      └── NO
            ↓
       REGIME FIREWALL
            ↓
       EXPLICIT BRIDGE
            ↓
       GOVERNED PAYLOAD
            ↓
       DECLARE
       NON-PORTABLES
            ↓
       TARGET-REGIME
       VALIDATION
            ↓
       TARGET USE
       MAY BECOME VALID
```

The compact operational law is:

```text
DECLARE THE REGIME
→ KEEP CONCLUSIONS REGIME-LOCAL
→ BRIDGE EXPLICITLY WHEN CROSSING
→ GOVERN WHAT CROSSES
→ DECLARE WHAT CANNOT CROSS
→ IN SIMULATION, WATCH THE WORST BRANCH
→ CALL IT STABLE ONLY IF ALL BRANCHES ARE STABLE
→ CHECK ALL SEVEN FRESHNESS AXES
→ REVALIDATE ONLY WHAT BECOMES STALE
```

with the hard firewalls:

```text
CLAIM TEXT
≠
REGIME

SOURCE LOCATION
≠
CANONICAL STATUS

CLAIM CLASS
≠
REGIME

PROVENANCE
≠
REGIME

SIMULATION
≠
EMPIRICAL OBSERVATION

SIMULATION
≠
SPECULATION

SIMULATION PASS
≠
PRODUCTION VALIDATION

SIMULATION STABILITY
≠
EMPIRICAL STABILITY

SIMULATION STABILITY
≠
CANONICAL COMPLIANCE

EMPIRICAL OBSERVATION
≠
CANONICAL AUTHORITY

CANONICAL REQUIREMENT
≠
EMPIRICAL IMPLEMENTATION FACT

SPECULATION
≠
FALSE

SPECULATION
≠
FACT

SPECULATIVE MECHANISM
≠
EMPIRICAL CAUSE

SOURCE-REGIME CONFIDENCE
≠
TARGET-REGIME CONFIDENCE

BRIDGE DECLARED
≠
TRANSFER VALIDATED

BRIDGE A→B
≠
BRIDGE B→A

BRIDGE A→B + B→C
≠
AUTOMATIC A→C PORTABILITY

PROPERTY LOST AT BRIDGE
≠
PROPERTY RESTORED DOWNSTREAM

SAME REGIME
≠
SAME SCOPE

SAME REGIME
≠
SAME ENVIRONMENT

SAME REGIME
≠
AUTOMATIC APPLICABILITY

SAME REGIME
≠
INDEPENDENT PROVENANCE

MOST BRANCHES STABLE
≠
ALL BRANCHES STABLE

AVERAGE DRIFT LOW
≠
WORST BRANCH STABLE

SAMPLED BRANCHES
≠
ALL RELEVANT BRANCHES

PESSIMISTIC SIMULATION
≠
FABRICATED FAILURE

WORST SIMULATION BRANCH
≠
EMPIRICAL CERTAINTY OF FAILURE

RECENT
≠
FRESH

TEMPORALLY FRESH
≠
ENVIRONMENTALLY FRESH

SOURCE FRESHNESS
≠
PROVENANCE FRESHNESS

MODEL FRESHNESS
≠
TEMPORAL FRESHNESS

6 FRESH AXES
≠
FULL APPLICABILITY
WHEN THE 7TH IS LOAD-BEARING AND STALE

STALE
≠
HISTORICALLY FALSE

OUT OF SCOPE
≠
REFUTED

REPRODUCIBLE
≠
CURRENTLY APPLICABLE

FORMAL
≠
SOURCE-DEFINED FIFTH REGIME

UNKNOWN
≠
SOURCE-DEFINED FIFTH REGIME

SELF-CONSISTENCY
≠
CANONICAL VALIDATION
```

---

# 213. RSCF Node

```yaml
RSCF-NODE:

  node_id:
    l21_epistemic_regime

  node_type:
    note

  path:
    01_CANON/01_CORE_LAWS/L21_EPISTEMIC_REGIME.md

  epistemic_class:
    AMOS_MODEL

  claim_class:
    CONDITIONAL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION

RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - MEMBER_OF: [[01_CORE_LAWS_MOC]]

  - RELATED_TO: [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

  - RELATED_TO: [[L17_RSCF]]

  - RELATED_TO: [[L18_GMEF]]

  - RELATED_TO: [[L19_PROOF_CAPSULE]]

  - RELATED_TO: [[L20_ADVERSARIAL]]

  - RELATED_TO: [[L16_HML]]

  - RELATED_TO: [[PROVENANCE_TOPOLOGY]]

  - RELATED_TO: [[PERSISTENT_PROVENANCE]]

  - RELATED_TO: [[SCOPE_REGIME_FIREWALL]]

  - RELATED_TO: [[CAUSAL_FIREWALL]]

  - RELATED_TO: [[COMPETING_HYPOTHESES]]

  - RELATED_TO: [[CAUSAL_EPOCH_FINALITY]]

  - RELATED_TO: [[L10_FAILURE_RECOVERY]]

  - RELATED_TO: [[L11_KNOWLEDGE_MEMORY]]

  - RELATED_TO: [[L15_FRACTAL_KNOWLEDGE]]
```

---

**00_ROOT_MOC:** [[AMOS MOC]]

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

**MOC:** [[01_CORE_LAWS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

# 214. L21 Final Canon Boundary

The supplied source supports the four proposed laws and their explicit contents:

```text
ER-1
DECLARED REGIME

ER-2
REGIME FIREWALL

ER-3
SIMULATION PESSIMISM

ER-4
SEVEN-AXIS FRESHNESS
```

It does **not** establish the expanded bridge protocols, schemas, branch-generation mechanisms, drift metrics, freshness thresholds, integrations, or implementation algorithms developed above as authoritative canon.

Therefore:

```yaml
status:
  PROPOSED_SPECIFICATION

epistemic_class:
  AMOS_MODEL

canonical_status:
  CONDITIONAL

confidence_ceiling:
  CONDITIONAL
```

until authoritative epistemic-regime canon supplies discriminating validation.

**Conclusion class: CONDITIONAL / AMOS_MODEL.**

```
