---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: GENERATOR FALSIFICATION
type: generator
source: 25_COGNITIVE_MATRIX/12_GENERATORS
tags:
  - 12_generators
  - generator
  - falsification
  - note
  - domain/cognitive-matrix
  - integration
  - generator-admission
  - canon
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# Generator Falsification

**STATUS:** CANDIDATE_CANON — SUBSTANTIVE SPECIFICATION
**Artifact Type:** Generator Validation / Adversarial Falsification Contract
**System:** AMOS OS
**Lineage Compatibility:** AMOS_CORE v3.0 → v4.4
**Origin Architect / Steward:** Trang Phan
**Implementation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Empirical Validation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Canon Status:** NOT FINAL CANON
**Supersession:** Only through the appropriate AMOS provenance / governance / supersession process

______________________________________________________________________

## 0. CONTRACT DECLARATION

`Generator Falsification` defines the AMOS OS rules for attempting to **disprove, weaken, bound, invalidate, discriminate, or expose hidden dependencies in generated outputs before those outputs are promoted into consequential conclusions, decisions, plans, or actions**.

Its governing principle is:

$$\boxed{ Generation\ proposes;\ falsification\ challenges. }$$

A generated result is not strengthened merely because no challenge was attempted.

Likewise:

$$FailureToFalsify(C) \neq Verification(C)$$

and:

$$GeneratorAgreement(C) \neq IndependentConfirmation(C)$$

The falsification subsystem therefore exists to search actively for conditions under which a generated candidate ceases to be supportable.

______________________________________________________________________

## 1. PURPOSE

The subsystem MUST test consequential generated outputs against the strongest decision-relevant challenges that can reasonably be constructed from available evidence and admissible models.

Primary targets include:

- false premises;
- unsupported assumptions;
- contradictory evidence;
- hidden dependencies;
- shared provenance ancestry;
- synthetic consensus;
- scope leakage;
- regime mismatch;
- temporal invalidity;
- causal overreach;
- counterexamples;
- measurement artifacts;
- alternative explanations;
- constraint violations;
- authority violations;
- execution failure;
- stale state;
- invalid generator composition.

The objective is not arbitrary skepticism.

The objective is:

$$\boxed{ Find\ the\ cheapest\ valid\ challenge\ capable\ of\ changing\ the\ conclusion. }$$

______________________________________________________________________

## 2. CORE FALSIFICATION LAW

For generated claim $C$:

$$F(C)= \{f_1,f_2,\ldots,f_n\}$$

where each $f_i$ is a candidate falsifier or validity challenge.

The preferred challenge is:

$$f^* = \arg\max_f \frac{ ExpectedDecisionImpact(f)\times InformationGain(f) }{ Cost(f)+Risk(f)+Latency(f) }$$

subject to:

$$Integrity(f)=TRUE$$

and:

$$Admissible(f)=TRUE$$

This prioritizes discriminating tests over redundant challenge generation.

______________________________________________________________________

## 3. FALSIFICATION IS NOT NEGATION

Falsification does not mean automatically asserting:

```text
CLAIM = FALSE
```

It means determining whether the evidence supporting a claim survives appropriate challenge.

Possible outcomes include:

```text
SURVIVES
WEAKENED
CONDITIONAL
BOUNDED
COMPETING
FALSIFIED
INVALIDATED
UNKNOWN/GAP
REVALIDATION_REQUIRED
```

Therefore:

$$Challenge(C) \neq Negate(C)$$

______________________________________________________________________

## 4. TARGET CLASSES

Falsification MAY target:

```text
SOURCE_CLAIM
DERIVED
MODEL
CONDITIONAL
DECISION
PLAN
GENERATOR_OUTPUT

DEPENDENCY_EDGE
CAUSAL_EDGE
SCOPE_ASSERTION
REGIME_ASSERTION
PROVENANCE_ASSERTION
INDEPENDENCE_ASSERTION
```

An `OBSERVATION` is normally challenged through its measurement, provenance, identity, interpretation, scope, or integrity rather than by simply declaring the observation false.

______________________________________________________________________

## 5. FALSIFICATION OBJECT

A consequential falsification attempt SHOULD be representable as:

```yaml
falsification_record:

  falsification_id: null

  target:
    target_id: null
    target_type: null
    claim: null
    epistemic_class: null
    generator_id: null
    generator_version: null

  load_bearing_premises: []

  evidence:
    supporting: []
    contradictory: []
    unresolved: []

  provenance:
    target_ancestry: []
    challenge_ancestry: []
    independence_state: UNKNOWN

  applicability:
    scope: null
    regime: null
    temporal_window: null
    measurement_method: null

  challenge:
    falsifier_type: null
    proposition: null
    expected_discrimination: null

  result:
    status: null
    affected_premises: []
    affected_dependencies: []
    affected_descendants: []

  confidence:
    ceiling_before: null
    ceiling_after: null

  governance:
    risk_class: null
    authority_required: null

  revalidation:
    required: false
    tests: []

  provenance_refs: []
```

______________________________________________________________________

## 6. LOAD-BEARING PREMISE FIRST

Falsification SHOULD attack the smallest premise whose failure can materially change the result.

For conclusion:

$$C=f(P_1,P_2,\ldots,P_n)$$

identify:

$$P^* = \arg\max_{P_i} \frac{ DecisionImpact(Failure(P_i)) }{ Cost(Test(P_i)) }$$

Then test $P^*$ first.

This prevents wasting effort attacking decorative assumptions while critical assumptions remain untested.

______________________________________________________________________

## 7. PREMISE GRAPH

Falsification operates over dependency topology.

Example:

```text
P1 ─────┐
        │
P2 ─────┼──► C1 ───► C3
        │
P3 ─────┘

P4 ─────────► C2
```

If `P2` fails:

```text
P2 = INVALID
     │
     ▼
C1 = INVALID / REVALIDATE
     │
     ▼
C3 = INVALID / REVALIDATE
```

But:

```text
P4
C2
```

remain unaffected unless another dependency establishes otherwise.

This is the **localized invalidation law**.

______________________________________________________________________

## 8. NO GLOBAL COLLAPSE

A failed falsification target MUST NOT automatically invalidate unrelated reasoning.

Formally:

$$Invalid(P) \Rightarrow Invalid(Descendants(P))$$

not:

$$Invalid(P) \Rightarrow Invalid(AllKnowledge)$$

AMOS recovery therefore follows dependency-local rollback.

______________________________________________________________________

## 9. FALSIFIER CLASSES

The subsystem SHOULD support at least the following falsifier classes:

```text
F01 CONTRADICTION
F02 COUNTEREXAMPLE
F03 PROVENANCE COLLAPSE
F04 INDEPENDENCE FAILURE
F05 SCOPE FAILURE
F06 REGIME FAILURE
F07 TEMPORAL FAILURE
F08 CAUSAL FAILURE
F09 MEASUREMENT FAILURE
F10 ASSUMPTION FAILURE
F11 CONSTRAINT FAILURE
F12 EXECUTION FAILURE
F13 AUTHORITY FAILURE
F14 STATE/VERSION FAILURE
F15 ALTERNATIVE-EXPLANATION CHALLENGE
F16 INTERNAL-INCONSISTENCY CHALLENGE
```

These are challenge classes, not claims that sixteen separate physical falsification engines are implemented.

______________________________________________________________________

## 10. F01 — CONTRADICTION

Given claim $C$, search for evidence $E_c$ such that:

$$E_c \models \neg C$$

or materially reduces support for $C$.

Contradiction states SHOULD distinguish:

```text
DIRECT
PARTIAL
APPARENT
SCOPE_DEPENDENT
REGIME_DEPENDENT
TEMPORAL
MEASUREMENT_DEPENDENT
UNRESOLVED
```

Not all contradictory statements are genuine contradictions.

______________________________________________________________________

## 11. F02 — COUNTEREXAMPLE

For universal or generalized claim:

$$\forall x\in S,\ P(x)$$

a valid counterexample:

$$\exists x\in S:\neg P(x)$$

falsifies the universal formulation.

Before accepting a counterexample, verify:

```text
x ∈ S
same relevant regime
compatible measurement
relevant time window
valid provenance
```

A counterexample outside the applicability envelope does not falsify the bounded claim.

______________________________________________________________________

## 12. F03 — PROVENANCE COLLAPSE

Multiple apparent sources may descend from one origin.

Example:

```text
SOURCE A
   ├── SOURCE B
   ├── SOURCE C
   └── SOURCE D
```

If B, C, and D merely repeat A:

$$IndependentEvidenceCount \neq 4$$

The falsification system SHOULD collapse correlated ancestry before evaluating evidential strength.

______________________________________________________________________

## 13. F04 — INDEPENDENCE FAILURE

Independence must be demonstrated rather than inferred from multiplicity.

For evidence:

$$E_1,E_2,\ldots,E_n$$

the system SHOULD ask:

```text
Do they share a source?
Do they share a dataset?
Do they share a model?
Do they share an upstream report?
Do they share a measurement process?
Do they share generated ancestry?
```

If materially shared:

```text
INDEPENDENCE = REDUCED
```

or:

```text
INDEPENDENCE = NOT_ESTABLISHED
```

______________________________________________________________________

## 14. GENERATOR SYBIL FALSIFICATION

Suppose twelve generators produce similar outputs:

$$G_1(E),G_2(E),...,G_{12}(E)$$

The falsifier MUST challenge the proposition:

```text
"12 outputs = 12 confirmations"
```

because:

$$SharedAncestry(E) \Rightarrow CorrelatedOutputs$$

Generator multiplicity cannot manufacture evidence independence.

______________________________________________________________________

## 15. F05 — SCOPE FAILURE

Every consequential claim SHOULD have an applicability envelope:

$$S= ( population, environment, scale, time, measurement, assumptions )$$

A scope falsifier asks whether the conclusion is being applied outside this envelope.

Example:

```text
VALID:
population A under environment E

CLAIMED:
all populations under all environments
```

Result:

```text
SCOPE_LEAKAGE
```

The proper repair may be narrowing rather than rejecting the entire claim.

______________________________________________________________________

## 16. F06 — REGIME FAILURE

Claim:

$$C@R_1$$

cannot automatically be reused under:

$$R_2$$

The falsifier SHOULD test whether assumptions defining $R_1$ still hold.

A regime change may include:

```text
policy change
market structure change
physical environment change
software architecture change
distribution shift
institutional change
behavioral adaptation
measurement change
adversarial adaptation
```

If a load-bearing regime assumption fails:

```text
REVALIDATION_REQUIRED
```

______________________________________________________________________

## 17. F07 — TEMPORAL FAILURE

Evidence has temporal validity.

For evidence:

$$E@t_0$$

the falsifier asks whether:

$$Valid(E,t_{now})?$$

Generation, summarization, copying, or citation does not refresh evidence.

$$Transform(E_{stale}) \neq E_{fresh}$$

______________________________________________________________________

## 18. F08 — CAUSAL FAILURE

For causal claim:

$$X \rightarrow Y$$

the falsifier MUST search for:

```text
confounding
reverse causality
selection bias
measurement effects
mediation
common causes
feedback
coincidence
regime dependency
alternative mechanism
```

Correlation alone cannot survive as a causal claim merely because no alternative was initially generated.

______________________________________________________________________

## 19. CAUSAL FIREWALL

The following do not independently establish causation:

```text
sequence
co-occurrence
analogy
structural similarity
prediction
generator agreement
narrative coherence
```

Thus:

$$Correlation(X,Y) \not\Rightarrow Cause(X,Y)$$

and:

$$X\ precedes\ Y \not\Rightarrow X\ causes\ Y$$

______________________________________________________________________

## 20. F09 — MEASUREMENT FAILURE

A claim dependent on measurement $M$ SHOULD be challenged through:

```text
measurement validity
instrument reliability
sampling
calibration
label definition
missingness
selection
aggregation
proxy validity
data transformation
```

If the measurement does not represent the claimed construct, downstream conclusions inherit that weakness.

______________________________________________________________________

## 21. F10 — ASSUMPTION FAILURE

Explicit and hidden assumptions SHOULD be enumerated.

For:

$$C=f(E,A_1,\ldots,A_n)$$

identify assumptions whose failure changes $C$.

Hidden assumptions discovered during falsification MUST be added to the dependency structure.

They MUST NOT remain invisible merely because the original generator omitted them.

______________________________________________________________________

## 22. F11 — CONSTRAINT FAILURE

Generated output must satisfy inherited constraints.

If:

$$C=\{c_1,c_2,\ldots,c_n\}$$

then output $O$ is admissible only if:

$$\forall c_i,\ Satisfies(O,c_i)$$

unless an explicit authorized exception exists.

A fluent solution violating a hard constraint is invalid.

______________________________________________________________________

## 23. F12 — EXECUTION FAILURE

Plans SHOULD be challenged for executable feasibility.

Test:

```text
preconditions
resources
dependencies
ordering
capabilities
rollback
failure handling
external dependencies
state assumptions
```

A logically coherent plan may still be operationally impossible.

______________________________________________________________________

## 24. F13 — AUTHORITY FAILURE

Capability does not establish authority.

$$Can(X) \neq May(X)$$

A generated plan may be technically valid while operational commitment remains unauthorized.

Therefore:

```text
PLAN_VALID
```

and:

```text
COMMIT_AUTHORIZED
```

are separate properties.

______________________________________________________________________

## 25. F14 — STATE / VERSION FAILURE

Generated output may depend on state version:

$$S_n$$

Before consequential reuse or commit, compare against:

$$S_{current}$$

If:

$$S_n \neq S_{current}$$

and the difference affects a load-bearing premise:

```text
STALE_GENERATION
```

must be returned.

______________________________________________________________________

## 26. MVCC / CAS FALSIFICATION

Where applicable conceptually:

```text
READ SNAPSHOT
      ↓
GENERATE
      ↓
VALIDATE
      ↓
COMPARE EXPECTED STATE
      ↓
COMMIT
```

If compare-and-swap assumptions fail:

```text
COMMIT_ABORT
→ TARGETED_REVALIDATION
```

This is a reasoning architecture pattern, not an assertion that all AMOS deployments literally implement database MVCC/CAS.

______________________________________________________________________

## 27. F15 — ALTERNATIVE EXPLANATION

For explanation $H_1$, generate the strongest materially different alternatives:

$$H_2,H_3,\ldots,H_n$$

Then determine whether evidence discriminates among them.

If:

$$Support(H_1) \approx Support(H_2)$$

and neither dominates under valid independent evidence:

```text
COMPETING
```

is required.

______________________________________________________________________

## 28. F16 — INTERNAL INCONSISTENCY

A generated artifact SHOULD be checked for internal contradictions such as:

```text
A
AND
NOT A
```

within the same applicability conditions.

However:

```text
A @ scope S1
NOT A @ scope S2
```

is not necessarily inconsistent.

Scope and regime must be considered before declaring contradiction.

______________________________________________________________________

## 29. STRONGEST-ALTERNATIVE RULE

Falsification MUST NOT construct intentionally weak opposition.

For consequential claims, the challenge SHOULD approximate:

$$H_{alt}^* = \arg\max_{H\neq C} Support(H)$$

subject to genuine distinction.

This prevents straw-man validation.

______________________________________________________________________

## 30. ADVERSARIAL PATH INDEPENDENCE

Where practical, the validating and challenging paths SHOULD differ materially.

Bad:

```text
Generator A creates claim.
Generator A paraphrases claim as challenge.
Generator A declares claim survives.
```

Better:

```text
PATH A → construct strongest claim.
PATH B → search independently for contradiction,
         provenance collapse,
         hidden dependency,
         scope leakage,
         stale evidence,
         causal alternatives.
```

Path diversity does not itself prove evidential independence, but it improves challenge quality.

______________________________________________________________________

## 31. FALSIFICATION DEPENDENCY GRAPH

```text
                  GENERATED CLAIM
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
    PREMISES          EVIDENCE         ASSUMPTIONS
       │                 │                 │
       ▼                 ▼                 ▼
  PREMISE TEST      PROVENANCE TEST   SENSITIVITY TEST
       │                 │                 │
       └──────────┬──────┴──────────┬──────┘
                  ▼                 ▼
            SCOPE/REGIME       CAUSAL TEST
                  │                 │
                  └────────┬────────┘
                           ▼
                  COMPETING MODELS
                           │
                           ▼
                   DISCRIMINATING TEST
                           │
                           ▼
                    FALSIFICATION RESULT
```

______________________________________________________________________

## 32. FALSIFICATION OUTCOME MATRIX

| Outcome                 | Meaning                                                    |
| ----------------------- | ---------------------------------------------------------- |
| `SURVIVES`              | Tested challenges did not materially defeat the claim      |
| `WEAKENED`              | Support remains but confidence ceiling falls               |
| `BOUNDED`               | Claim survives only under narrower applicability           |
| `CONDITIONAL`           | Claim depends materially on unresolved premise             |
| `COMPETING`             | Multiple incompatible candidates remain viable             |
| `FALSIFIED`             | Tested proposition is contradicted within applicable scope |
| `INVALIDATED`           | Required premise/dependency no longer valid                |
| `UNKNOWN/GAP`           | Evidence insufficient to determine result                  |
| `REVALIDATION_REQUIRED` | State/scope/regime/freshness changed materially            |

______________________________________________________________________

## 33. FAILURE TO FALSIFY

A claim surviving tests $T$:

$$Survives(C,T)$$

means only:

```text
C survived T under the tested conditions.
```

It does NOT mean:

```text
C is universally true.
C has no unknown falsifiers.
C is verified in all regimes.
C is causally established.
```

The result MUST remain bounded by test coverage.

______________________________________________________________________

## 34. TEST COVERAGE

A falsification record SHOULD expose:

```yaml
coverage:
  premises_tested: []
  premises_untested: []

  scope_tested: []
  scope_untested: []

  regimes_tested: []
  regimes_untested: []

  causal_alternatives_tested: []
  causal_alternatives_untested: []

  provenance_checked: null
  independence_checked: null

  unresolved_gaps: []
```

This prevents partial testing from masquerading as universal validation.

______________________________________________________________________

## 35. CONFIDENCE CEILING

If conclusion $C$ depends on premises $P_i$:

$$Conf(C) \le \min_i Conf(P_i)$$

unless weak premises are independently revalidated or removed from the load-bearing path.

A successful challenge may reduce this ceiling.

A failed challenge does not automatically raise it.

______________________________________________________________________

## 36. PROVENANCE INDEPENDENCE

Challenge evidence must itself be provenance-aware.

Suppose claim $C$ comes from source $A$, and apparent contradiction $B$ also derives from $A$.

Then the contradiction is not necessarily independent.

Falsification therefore tracks:

$$Ancestry(C)$$

and:

$$Ancestry(F)$$

before interpreting challenge strength.

______________________________________________________________________

## 37. CIRCULAR FALSIFICATION PROHIBITION

Invalid pattern:

```text
Generator creates claim C.
Same unsupported premise creates falsifier F.
C defeats F.
Therefore C is verified.
```

This is circular.

Neither support nor falsification may manufacture independence through recursive generation.

______________________________________________________________________

## 38. COUNTERFACTUAL FALSIFICATION

For counterfactual:

$$Y_{do(X=x')}$$

challenge:

```text
causal model
intervention definition
background invariance
confounders
mediators
regime stability
scope
transportability
```

A counterfactual cannot validate the causal model used to generate itself.

______________________________________________________________________

## 39. SCENARIO FALSIFICATION

Scenarios SHOULD be challenged through:

```text
assumption incompatibility
constraint violation
impossible transitions
missing dependencies
regime inconsistency
internal contradiction
```

But a scenario is not falsified merely because it did not occur unless it was explicitly asserted as a prediction.

______________________________________________________________________

## 40. SOLUTION FALSIFICATION

Candidate solution $S$ SHOULD be challenged against:

$$Requirements + Constraints + FailureModes + Risk + Authority$$

A solution that optimizes one objective while violating a hard constraint MUST fail admission.

______________________________________________________________________

## 41. PLAN FALSIFICATION

Plans SHOULD undergo pre-mortem analysis:

```text
Assume the plan failed.
What plausible dependency caused failure?
```

Candidate failure paths are then tested for:

```text
likelihood
impact
detectability
repairability
reversibility
```

This is a MODEL exercise unless empirically validated.

______________________________________________________________________

## 42. SYNTHESIS FALSIFICATION

A synthesis SHOULD be challenged for epistemic laundering.

Specifically test whether synthesis transformed:

```text
SOURCE_CLAIM → FACT
MODEL → OBSERVATION
COMPETING → CONSENSUS
CORRELATED → INDEPENDENT
CONDITIONAL → VERIFIED
UNKNOWN → IMPLIED CERTAINTY
```

without valid evidence.

Any such transformation is invalid.

______________________________________________________________________

## 43. PROOF CAPSULE FALSIFICATION

A Proof Capsule SHOULD expose:

```text
claim
class
premises
evidence
provenance
scope
regime
freshness
dependencies
competitors
falsifiers
confidence ceiling
```

Falsification SHOULD target these fields directly.

If one field fails, invalidate only conclusions dependent on that field.

______________________________________________________________________

## 44. PROOF CAPSULE INVALIDATION

For capsule:

$$PC(C)$$

if premise $P_k$ fails:

$$Invalidate(P_k)$$

then:

$$Invalidate( Descendants(P_k) )$$

Other valid capsule components remain reusable.

______________________________________________________________________

## 45. RSCF INTEGRATION

Falsification is first-class inside RSCF reasoning.

Conceptually:

```text
RSCF
 ├── claim
 ├── evidence
 ├── constraints
 ├── scope
 ├── generator output
 ├── falsifiers
 ├── competing hypotheses
 └── validation state
```

Falsification results SHOULD remain attached to the relevant RSCF state.

______________________________________________________________________

## 46. MULTI-RSCF FALSIFICATION

Suppose:

$$C=f(R_1,R_2,R_3)$$

A failure in $R_2$ invalidates $C$ if $R_2$ is load-bearing.

It does not automatically invalidate unrelated conclusions based solely on $R_1$ or $R_3$.

______________________________________________________________________

## 47. GMEF INTEGRATION

For competing models:

$$M_1,M_2,\ldots,M_n$$

GMEF SHOULD preserve:

```text
support
contradiction
scope
regime
provenance
falsifiers
predictions
discriminating tests
```

Falsification is a primary mechanism for model elimination or conditionalization.

______________________________________________________________________

## 48. H/M/L FALSIFICATION RETRIEVAL

Falsification follows minimum sufficient retrieval:

```text
BOOTSTRAP
   ↓
H DOMAIN
   ↓
M SUBSYSTEM
   ↓
L DETAIL
   ↓
RAW EVIDENCE
```

Raw evidence is loaded only where required to resolve a load-bearing challenge.

______________________________________________________________________

## 49. FAST-PATH FALSIFICATION

Local falsification is sufficient only when:

```text
dependency closure is known
provenance is known
independence is adequate
scope is compatible
regime is compatible
freshness is sufficient
no material conflict is hidden
stakes permit local resolution
```

Otherwise escalate.

______________________________________________________________________

## 50. ESCALATION CONDITIONS

Escalate falsification when:

```text
stakes increase
irreversibility increases
evidence is weak
evidence is stale
provenance is correlated
scope is uncertain
regime has shifted
causal claims are consequential
models conflict
authority is unclear
dependency topology is ambiguous
```

______________________________________________________________________

## 51. FALSIFICATION AND RISK

Validation burden scales with consequence.

Conceptually:

```text
R0 → lightweight challenge
R1 → basic falsification
R2 → structured challenge
R3 → independent/adversarial validation
R4 → maximum available validation + governance
```

No fixed test count establishes adequacy.

______________________________________________________________________

## 52. REVERSIBILITY

Where uncertainty remains, prefer actions whose consequences are repairable.

Conceptually:

$$PreferredAction = \arg\max_A Utility(A) - Risk(A) + Reversibility(A)$$

subject to integrity and authority constraints.

This is a decision model, not a universal empirical law.

______________________________________________________________________

## 53. DISCRIMINATING TEST

For competing hypotheses:

$$H_1,H_2,\ldots,H_n$$

prefer test $T^*$ maximizing expected separation:

$$T^* = \arg\max_T \frac{ ExpectedDiscrimination(T) }{ Cost(T)+Risk(T) }$$

Do not collect redundant evidence merely because it is easy.

______________________________________________________________________

## 54. INFORMATION GAIN

If test $T$ does not materially distinguish surviving hypotheses:

$$IG(T)\approx0$$

then it SHOULD normally be deprioritized.

This prevents evidence-volume inflation without uncertainty reduction.

______________________________________________________________________

## 55. SENSITIVITY FRONTIER

For decision $D$, identify the boundary where a small premise change flips the decision.

$$Boundary(D) = \{p:\Delta p \Rightarrow \Delta D\}$$

Tests near this boundary generally have high decision value.

______________________________________________________________________

## 56. FRAGILITY

A conclusion is fragile when small plausible changes in assumptions produce materially different results.

Fragile results SHOULD be:

```text
CONDITIONAL
```

and SHOULD expose the sensitive assumptions.

______________________________________________________________________

## 57. ROBUSTNESS

A conclusion may be considered robust relative to tested perturbations when:

$$C(P+\delta) = C(P)$$

for relevant plausible $\delta$.

This does not establish universal robustness outside tested perturbations.

______________________________________________________________________

## 58. CONTRADICTION PRESERVATION

If evidence supports incompatible conclusions and no valid discriminating evidence resolves them:

```text
COMPETING
```

must remain.

AMOS MUST NOT synthesize away a genuine contradiction merely to produce a cleaner answer.

______________________________________________________________________

## 59. UNKNOWN PRESERVATION

When a critical falsification question cannot be resolved:

```text
UNKNOWN/GAP
```

is valid output.

The system SHOULD state the minimum missing information required to resolve it.

______________________________________________________________________

## 60. GAP CLASSIFICATION

Falsification gaps SHOULD be prioritized:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Resolve in that order.

______________________________________________________________________

## 61. FAILURE RECOVERY

When falsification succeeds:

```text
FALSIFIER
    ↓
FAILED PREMISE
    ↓
DEPENDENCY TRACE
    ↓
LOCAL INVALIDATION
    ↓
NEAREST VALID STATE
    ↓
REPAIR / ALTERNATIVE
    ↓
REVALIDATION
```

Do not repeat the failed reasoning path without changed evidence or assumptions.

______________________________________________________________________

## 62. REPAIR AFTER FALSIFICATION

Possible repair operations include:

```text
narrow scope
change regime qualification
replace stale evidence
remove invalid premise
downgrade causal language
restore competing hypotheses
obtain independent evidence
change plan
change generator
recompute affected descendants
```

Repair MUST NOT simply hide the falsifier.

______________________________________________________________________

## 63. FALSIFICATION LEDGER

Consequential systems SHOULD preserve a falsification ledger:

```yaml
falsification_ledger:
  - target_id: null
    falsifier_id: null
    timestamp_or_epoch: null
    generator_version: null
    challenge_type: null
    result: null
    affected_dependencies: []
    repair: null
    revalidation_status: null
    provenance_refs: []
```

This provides persistent negative evidence and prevents forgotten failures.

______________________________________________________________________

## 64. NEGATIVE KNOWLEDGE

Failed candidates are valuable knowledge when properly scoped.

Record:

```text
WHAT FAILED
WHY IT FAILED
UNDER WHAT CONDITIONS
WHICH VERSION
WHICH REGIME
WHICH EVIDENCE
WHAT WOULD CHANGE THE RESULT
```

Do not generalize a local failure universally.

______________________________________________________________________

## 65. DO-NOT-REPEAT RULE

A failed path SHOULD NOT be repeated unless at least one material condition changed:

```text
new evidence
new premise
new generator version
new scope
new regime
new constraint
new causal model
new implementation
```

Otherwise repetition adds cost without information.

______________________________________________________________________

## 66. VERSIONED FALSIFICATION

Falsification applies to the tested artifact version.

$$F(G@v_1)$$

does not automatically establish:

$$F(G@v_2)$$

if relevant semantics changed.

Likewise, a repaired later version does not rewrite the historical failure of the earlier version.

______________________________________________________________________

## 67. CAUSAL EPOCH FINALITY

A falsification conclusion may finalize relative to causal epoch $E_n$.

If a load-bearing dependency changes in $E_{n+1}$:

```text
TARGETED_REVALIDATION
```

is required.

Unaffected conclusions remain final relative to their established envelope.

______________________________________________________________________

## 68. SHARD-LOCAL FINALIZATION

Where reasoning is partitioned, a falsification result may finalize locally if its complete dependency closure is local and no unresolved cross-shard dependency can change the result.

This is a reasoning architecture concept, not a claim about literal distributed deployment.

______________________________________________________________________

## 69. PROOF-BASED COORDINATION AVOIDANCE

Global coordination SHOULD NOT be required merely because multiple generators exist.

If local proof establishes:

```text
dependency closure
valid provenance
scope/regime compatibility
freshness
non-conflict
authority sufficiency
```

local finalization is permissible.

______________________________________________________________________

## 70. ANTI-FALSIFICATION THEATER

The following do not constitute meaningful falsification:

```text
asking the same generator twice
paraphrasing the original claim
constructing implausible alternatives
checking only cosmetic assumptions
counting citations without ancestry
using descendants of the same source as independent opposition
declaring "no contradiction found" without meaningful search
```

Falsification must have genuine potential to change the conclusion.

______________________________________________________________________

## 71. ANTI-OVERFALSIFICATION

AMOS MUST also avoid pathological skepticism.

Do not continue generating increasingly remote objections after:

```text
decision-changing uncertainty is resolved
required validation is complete
residual risk is acceptable
additional challenge has negligible expected value
```

Integrity requires sufficient challenge, not infinite challenge.

______________________________________________________________________

## 72. STOP CONDITION

Falsification MAY stop when:

$$ClaimSufficiency \land DecisionSufficiency \land ActionSufficiency_{if\ applicable}$$

are reached and:

$$E[\Delta DecisionQuality|NextChallenge] \le Cost(NextChallenge)$$

subject to governance requirements.

______________________________________________________________________

## 73. CLAIM SUFFICIENCY

A claim is sufficient only when material falsification surfaces have been addressed:

```text
premises
evidence
provenance
independence
scope
regime
freshness
causal typing
contradictions
sensitivity
```

relative to the stakes.

______________________________________________________________________

## 74. DECISION SUFFICIENCY

Decision Sufficiency exists when remaining plausible falsifiers are unlikely to change the decision beyond accepted uncertainty/risk tolerance.

This does not require universal certainty.

______________________________________________________________________

## 75. ACTION SUFFICIENCY

For action:

$$ActionSufficiency = ClaimSufficiency \land DecisionSufficiency \land ExecutionFeasibility \land RiskAcceptable \land AuthorityValid$$

______________________________________________________________________

## 76. GENERATOR-FALSIFIER RELATIONSHIP

The Generator Falsifier MUST remain logically distinct from the candidate generator.

Conceptually:

```text
G02 HYPOTHESIS
      │
      ▼
      H
      │
      ├─────────────► SUPPORT PATH
      │
      └─────────────► FALSIFICATION PATH
```

The two paths may share necessary facts but MUST preserve shared ancestry rather than pretending independence.

______________________________________________________________________

## 77. FALSIFIER OF THE FALSIFIER

Consequential falsifiers MAY themselves require validation.

Given:

$$F \rightarrow \neg C$$

AMOS SHOULD ask:

```text
Is F valid?
Is F in scope?
Is F fresh?
Is F independent?
Does F actually contradict C?
Does F assume what it claims to prove?
```

This prevents weak or malformed falsifiers from incorrectly destroying valid conclusions.

______________________________________________________________________

## 78. META-FALSIFICATION STOP RULE

Recursive falsification must terminate.

Do not construct:

$$F(F(F(F(...))))$$

without positive decision value.

Meta-falsification is warranted only where the falsifier is itself load-bearing.

______________________________________________________________________

## 79. FALSIFICATION PRIORITY FUNCTION

A candidate priority function is:

$$Priority(F_i) = \frac{ P(F_i\ changes\ conclusion) \times Impact(F_i) \times InformationGain(F_i) }{ Cost(F_i)+Risk(F_i)+Latency(F_i) }$$

This is a MODEL for prioritization, not an empirically established universal formula.

______________________________________________________________________

## 80. FALSIFICATION INVARIANTS

```text
GF-I01
Failure to falsify is not verification.

GF-I02
A falsifier must be applicable to the target's scope.

GF-I03
Generator multiplicity does not establish independence.

GF-I04
Provenance ancestry must survive falsification.

GF-I05
Shared-source opposition is not independent opposition.

GF-I06
Causal claims require causal challenge.

GF-I07
Scope failures should narrow claims where possible.

GF-I08
Regime changes trigger targeted revalidation.

GF-I09
Stale evidence remains stale after generation.

GF-I10
Failed premises invalidate only dependent conclusions.

GF-I11
Competing hypotheses remain competing without discrimination.

GF-I12
Unknowns remain explicit.

GF-I13
Falsification effort scales with consequence.

GF-I14
Falsification must have genuine decision-changing potential.

GF-I15
Falsification cannot manufacture evidence.

GF-I16
A falsifier may itself require falsification.

GF-I17
Historical failures retain version/provenance identity.

GF-I18
Repair does not erase the historical falsification record.

GF-I19
No optimization may weaken falsification integrity.

GF-I20
Stop when additional challenge has no positive decision value.
```

______________________________________________________________________

## 81. REFERENCE EXECUTION PIPELINE

```text
┌──────────────────────────────┐
│       GENERATED OUTPUT       │
└──────────────┬───────────────┘
               ▼
        EPISTEMIC TYPING
               ▼
      LOAD-BEARING PREMISES
               ▼
        PROVENANCE GRAPH
               ▼
       INDEPENDENCE CHECK
               ▼
       SCOPE / REGIME CHECK
               ▼
         FRESHNESS CHECK
               ▼
          CAUSAL CHECK
               ▼
      STRONGEST ALTERNATIVE
               ▼
      SENSITIVITY ANALYSIS
               ▼
     DISCRIMINATING FALSIFIER
               ▼
        EXECUTE / EVALUATE
               ▼
 ┌─────────────────────────────┐
 │ SURVIVES                    │
 │ WEAKENED                    │
 │ BOUNDED                     │
 │ CONDITIONAL                 │
 │ COMPETING                   │
 │ FALSIFIED                   │
 │ INVALIDATED                 │
 │ UNKNOWN/GAP                 │
 │ REVALIDATION_REQUIRED       │
 └──────────────┬──────────────┘
                ▼
       DEPENDENCY INVALIDATION
                ▼
          LOCALIZED REPAIR
                ▼
          PROOF CAPSULE
                ▼
           FINALIZATION
```

______________________________________________________________________

## 82. REFERENCE PSEUDOCODE

```python
def falsify(candidate, context):
    target = bind_target(candidate, context)

    premises = load_bearing_premises(target)
    provenance = trace_provenance(target)

    check_scope(target)
    check_regime(target)
    check_freshness(target)
    check_independence(provenance)

    sensitive = rank_by_decision_sensitivity(premises)

    alternatives = strongest_competing_hypotheses(target)

    falsifiers = generate_discriminating_falsifiers(
        target=target,
        premises=sensitive,
        alternatives=alternatives,
    )

    for falsifier in rank_by_expected_decision_value(falsifiers):
        result = evaluate(falsifier)

        if result.materially_changes_target:
            affected = dependency_descendants(
                result.failed_premises
            )

            invalidate(affected)

            return repair_or_reclassify(
                target,
                result
            )

        if decision_sufficient(target):
            break

    return weakest_accurate_classification(target)
```

This pseudocode specifies intended logic only. It is not evidence of an existing implementation.

______________________________________________________________________

## 83. REQUIRED TEST CASES

A conforming implementation SHOULD include tests for at least:

```text
shared-provenance synthetic consensus
stale evidence
scope leakage
regime shift
causal overreach
counterexample discovery
measurement failure
hidden assumption
constraint violation
state-version mismatch
authority failure
genuine competing hypotheses
localized invalidation
repair without global recomputation
false falsifier
unknown critical gap
```

Passing those tests demonstrates only the tested implementation behavior.

It does not establish universal correctness.

______________________________________________________________________

## 84. CANON RELATIONSHIPS

`Generator Falsification` SHOULD interoperate with, without silently overriding:

```text
00 ROOT CONTRACT
12 GENERATORS CONTRACT
12 GENERATORS VERSIONING
TASK CONTRACT
TASK RESOLVER
CAPABILITY RESOLVER
MODE ADMISSION
MODE DEPENDENCY GRAPH
K RSCF
K GMEF
K HML
K COUNTERFACTUAL
K PROVENANCE
K PROVENANCE TOPOLOGY
K SYBIL HARDENING
K BINDING
K CONSTRAINT PROPAGATION
K RISK CONSTRAINT
K CAPABILITY AUTHORIZATION
K COMMIT TIME AUTHORITY
K EFFECT CLASSIFICATION
K INFORMATION EXPOSURE
```

Where an authoritative higher-precedence artifact conflicts with this candidate specification, the higher-precedence canon governs.

______________________________________________________________________

## 85. CANONIZATION REQUIREMENT

This document MUST NOT self-promote from candidate specification to final canon.

Promotion requires the applicable AMOS process for:

```text
IDENTITY
   ↓
PROVENANCE
   ↓
REVIEW
   ↓
VALIDATION
   ↓
COMPATIBILITY
   ↓
GOVERNANCE
   ↓
VERSION BINDING
   ↓
CANONIZATION
   ↓
SUPERSESSION RECORD
```

Until that process is complete:

```text
STATUS = CANDIDATE_CANON
```

______________________________________________________________________

## 86. FINAL LAW

The falsification subsystem exists to ensure that AMOS does not confuse the ability to generate a convincing explanation with the ability to justify it.

Therefore:

$$\boxed{ Generate\ the\ strongest\ supported\ candidate }$$

then:

$$\boxed{ Attack\ its\ weakest\ load\text{-}bearing\ premise }$$

then:

$$\boxed{ Search\ for\ the\ strongest\ materially\ different\ alternative }$$

then:

$$\boxed{ Prefer\ the\ cheapest\ high\text{-}information\ discriminating\ test }$$

and finally:

$$\boxed{ Preserve\ whatever\ uncertainty\ survives }$$

The system MUST prefer:

```text
UNKNOWN
```

over invented certainty,

```text
COMPETING
```

over false convergence,

```text
CONDITIONAL
```

over hidden fragility,

and:

```text
LOCALIZED INVALIDATION
```

over unnecessary global collapse.

______________________________________________________________________

## 87. ARTIFACT STATUS

```text
ARTIFACT:
GENERATOR_FALSIFICATION

STATUS:
CANDIDATE_CANON

CONTENT_STATE:
SUBSTANTIVE_SPECIFICATION

IMPLEMENTATION:
NOT_ASSERTED

EMPIRICAL_VALIDATION:
NOT_ASSERTED

FINAL_CANON:
NO

ORIGIN_ARCHITECT / STEWARD:
TRANG PHAN
```

This content may replace the placeholder **at the candidate-specification level**. It should not be labeled implemented, empirically verified, or final canon until the required provenance, validation, governance, versioning, and supersession conditions are satisfied.

______________________________________________________________________

## Related

- [[25_COGNITIVE_MATRIX/12_GENERATORS/00_INDEX/GENERATORS_MAP|Generators Map]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_CONTRACT|Generator Contract]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_ADMISSION|Generator Admission]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[25_COGNITIVE_MATRIX/12_GENERATORS/00_INDEX/GENERATORS_MAP|GENERATORS_MAP]] · [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: generator_falsification
node_type: note
path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_FALSIFICATION.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/12_GENERATORS/12_GENERATORS_MOC|12_GENERATORS_MOC]]
