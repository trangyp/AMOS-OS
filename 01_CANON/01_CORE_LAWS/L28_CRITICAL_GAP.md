---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: L28 Critical Gap
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# Source-preserved artifact

## 0. Status
Canon-plane artifact. AMOS_MODEL · CONDITIONAL · implementation PARTIAL.

## 1. Purpose
`L28 CRITICAL GAP` defines typed artifact specification, serving the Canon plane's obligation: canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession.

## 2. Semantics
- Every load-bearing field is typed; unknown values are recorded as `UNKNOWN/GAP`, never invented.
- Scope and regime are declared on every claim; cross-regime transfer requires an explicit bridge.
- Confidence ceiling 0.95; conclusion confidence ≤ weakest load-bearing premise.

## 3. Failure modes guarded
STALE_READ · SCOPE_LEAK · REGIME_DRIFT · CONFIDENCE_INFLATION · AUTHORITY_ESCALATION · PROVENANCE_LOSS · SILENT_PARTIAL_COMMIT · UNKNOWN_AS_VALID.

## 4. Validation
No artifact-specific executor yet; executed OS validators exist as pattern ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]). Required tests before promotion: identity, type-contract, negative-case (missing/malformed/stale input), authority boundary, rollback.

## 5. Gaps
Implementation binding, empirical validation, and cross-artifact consistency checks remain OPEN (UNKNOWN/GAP).

## 6. Falsifiers
F1: canonical source contradicts declared semantics. F2: executed test violates a stated invariant. F3: artifact promotes UNKNOWN to PASS.
## Worked semantics
Given an operation touching `L28 CRITICAL GAP` within the Canon plane:
1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane bindings
- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]
---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/L27_GAP|L27_GAP]] · [[01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY|L10_FAILURE_RECOVERY]] · [[01_CANON/01_CORE_LAWS/L8_EXECUTION|L8_EXECUTION]] · [[01_CANON/01_CORE_LAWS/FAIL_CLOSED_GOVERNANCE|FAIL_CLOSED_GOVERNANCE]] · [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]]

---

RSCF-NODE

node_id: l28_critical_gap

node_type: note

path: 01_CANON/01_CORE_LAWS/L28_CRITICAL_GAP.md

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

  - CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

claim_class: AMOS_MODEL

---

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

---

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

## Derived / Proposed AMOS Formalization

Everything below is **DERIVED / PROPOSED**. It does not mutate the source law, source metadata, RSCF block, conditional canonical status, or source-declared falsifier.

The supplied artifact is materially stronger than a placeholder: its source status is `PROPOSED_SPECIFICATION`, epistemic class `AMOS_MODEL`, and canonical status `CONDITIONAL`. Its four operative rules define a fail-closed governance policy for gaps that block safety, integrity, or authority.

A Drive search for the exact title did **not** return an exact `L28 CRITICAL GAP` artifact in its first results. It did return an AMOS gap-closure workflow, but that is related corpus material, not evidence that this L28 specification has been canonically implemented or validated.

## 1. Exact source state

Let

$$
L_{28}
$$

denote this artifact.

The source establishes:

$$
\operatorname{Status}(L_{28})
=
\texttt{PROPOSED\_SPECIFICATION},
$$

$$
\operatorname{EpistemicClass}(L_{28})
=
\texttt{AMOS\_MODEL},
$$

$$
\operatorname{CanonicalStatus}(L_{28})
=
\texttt{CONDITIONAL}.
$$

Its RSCF metadata separately establishes:

$$
\operatorname{RSCFState}(L_{28})
=
\texttt{SOURCE\_CLAIM},
$$

$$
\operatorname{RSCFClaimClass}(L_{28})
=
\texttt{CONDITIONAL}.
$$

The trailing RSCF node declares:

$$
\operatorname{NodeClaimClass}(L_{28})
=
\texttt{AMOS\_MODEL}.
$$

These are distinct classification dimensions and should not be collapsed:

$$
\boxed{
\texttt{SOURCE\_CLAIM}
\neq
\texttt{CONDITIONAL}
\neq
\texttt{AMOS\_MODEL}
\neq
\texttt{PROPOSED\_SPECIFICATION}.
}
$$

______________________________________________________________________

## 2. Critical-gap predicate

The source gives three load-bearing criticality domains:

$$
\mathcal B
=
\{
\text{SAFETY},
\text{INTEGRITY},
\text{AUTHORITY}
\}.
$$

For gap (g), a direct formalization of CG-1 is:

$$
\boxed{
\left(
\operatorname{Gap}(g)
\land
\operatorname{Blocks}(g,b)
\land
b\in\mathcal B
\right)
\Rightarrow
\operatorname{Class}(g)=\texttt{CRITICAL}.
}
$$

And:

$$
\boxed{
\operatorname{Class}(g)=\texttt{CRITICAL}
\Rightarrow
\operatorname{FailClosed}(g).
}
$$

This preserves the source's necessary direction without inventing a biconditional.

The source does **not** establish that safety, integrity, and authority are the only possible reasons a gap can be CRITICAL. Therefore:

$$
\operatorname{Critical}(g)
\Leftrightarrow
\operatorname{BlocksSafetyIntegrityAuthority}(g)
$$

would be too strong.

______________________________________________________________________

## 3. CG-1 — Critical Classification

Define:

$$
B_S(g)=
\operatorname{BlocksSafety}(g),
$$

$$
B_I(g)=
\operatorname{BlocksIntegrity}(g),
$$

$$
B_A(g)=
\operatorname{BlocksAuthority}(g).
$$

Then:

$$
\boxed{
B_S(g)\lor B_I(g)\lor B_A(g)
\Rightarrow
\operatorname{Critical}(g).
}
$$

The immediate governance consequence is:

$$
\boxed{
\operatorname{Critical}(g)
\Rightarrow
\operatorname{FailClosedImmediately}(g).
}
$$

Importantly:

$$
\operatorname{FailClosed}(g)
\neq
\operatorname{GapResolved}(g).
$$

Fail-closed is a containment/governance response, not evidence that the underlying uncertainty has been removed.

______________________________________________________________________

## 4. CG-2 — No Consequential Path Through Critical Gap

Let:

$$
o
$$

be an operation and:

$$
D^{*}(o)
$$

its smallest result-changing dependency closure.

If:

$$
g\in D^{*}(o)
$$

and:

$$
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g),
$$

then the source requires:

$$
\boxed{
\operatorname{Consequential}(o)
\Rightarrow
\operatorname{DENY}(o).
}
$$

More fully:

$$
\boxed{
\operatorname{Consequential}(o)
\land
\exists g\in D^{*}(o):
\left[
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g)
\right]
\Rightarrow
\operatorname{Decision}(o)=\texttt{DENY}.
}
$$

Not merely:

$$
\operatorname{Decision}(o)=\texttt{WARN}.
$$

Hence:

$$
\boxed{
\texttt{CRITICAL + UNRESOLVED + CONSEQUENTIAL PATH}
\Rightarrow
\texttt{DENY}.
}
$$

______________________________________________________________________

## 5. Consequential-path semantics

A critical gap elsewhere in the system does not automatically prove every unrelated operation must halt.

The source says operations **routing through** unresolved critical gaps are denied.

Therefore the load-bearing relation is dependency/path membership:

$$
\operatorname{RoutesThrough}(o,g).
$$

Thus:

$$
\operatorname{Critical}(g)
\land
\neg\operatorname{RoutesThrough}(o,g)
$$

does not, from L28 alone, imply:

$$
\operatorname{DENY}(o).
$$

This is important for local failure containment.

A proposed operational predicate is:

$$
\operatorname{BlockedByCriticalGap}(o)
:=
\exists g\,
[
\operatorname{RoutesThrough}(o,g)
\land
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g)
].
$$

Then:

$$
\boxed{
\operatorname{Consequential}(o)
\land
\operatorname{BlockedByCriticalGap}(o)
\Rightarrow
\operatorname{DENY}(o).
}
$$

______________________________________________________________________

## 6. UNKNOWN/GAP interaction

L28 must not silently equate every:

$$
\texttt{UNKNOWN/GAP}
$$

with:

$$
\texttt{CRITICAL}.
$$

Instead:

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\texttt{CRITICAL}
}
$$

unless the gap satisfies a critical-classification condition.

Likewise:

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\texttt{PASS}.
}
$$

A useful typed distinction is:

$$
\operatorname{GapState}(g)
\in
\{
\texttt{OPEN},
\texttt{RESOLVED},
\texttt{UNKNOWN/GAP}
\},
$$

while:

$$
\operatorname{GapSeverity}(g)
\in
\{
\texttt{CRITICAL},
\texttt{DECISION\_RELEVANT},
\texttt{EXPLANATORY},
\texttt{COSMETIC}
\}.
$$

That four-level severity taxonomy is AMOS-derived formalization; only `CRITICAL` is explicitly defined by this source artifact.

______________________________________________________________________

## 7. Critical does not mean false

For proposition (p) blocked by gap (g):

$$
\operatorname{Critical}(g)
\not\Rightarrow
\neg p.
$$

Nor:

$$
\operatorname{Critical}(g)
\not\Rightarrow
p.
$$

Instead:

$$
\boxed{
\operatorname{Critical}(g)
\Rightarrow
\text{insufficient basis for the consequential path that depends on }g.
}
$$

Thus L28 is fundamentally an **execution-governance law under unresolved uncertainty**, not a truth-value operator.

______________________________________________________________________

## 8. CG-3 — Visible Escalation

Let:

$$
S
$$

be a status artifact and (g) an unresolved critical gap relevant to (S).

The source requires:

$$
\boxed{
\operatorname{Critical}(g)
\land
\operatorname{RelevantTo}(g,S)
\Rightarrow
\operatorname{SurfaceAtTop}(g,S).
}
$$

And prohibits:

$$
\operatorname{Buried}(g,S).
$$

A proposed visibility invariant is:

$$
\operatorname{Critical}(g)
\land
\operatorname{Open}(g)
\Rightarrow
\operatorname{Priority}(g)=\operatorname{HighestVisibleClass}.
$$

The exact UI ordering algorithm is not supplied by the source, so that remains:

$$
\texttt{UNKNOWN/GAP}.
$$

______________________________________________________________________

## 9. Visibility is not authority

CG-3 creates an observability requirement, not an authority grant.

Therefore:

$$
\operatorname{Visible}(g)
\not\Rightarrow
\operatorname{Authorized}(g).
$$

Likewise:

$$
\operatorname{StatusArtifactReports}(g)
\not\Rightarrow
\operatorname{StatusArtifactMayResolve}(g).
$$

This is consistent with the AMOS boundary:

$$
\boxed{
\text{observability}
\neq
\text{authority}.
}
$$

______________________________________________________________________

## 10. CG-4 — Owner Required

For every critical gap (g):

$$
\boxed{
\operatorname{Critical}(g)
\Rightarrow
\exists o:
\operatorname{Owns}(o,g).
}
$$

The source explicitly permits either:

$$
o=\text{owner}
$$

or:

$$
o=\text{owning process}.
$$

Therefore human ownership is not required by the text:

$$
\operatorname{Owner}(g)
\in
\{
\text{named owner},
\text{owning process}
\}.
$$

But:

$$
\operatorname{Owner}(g)
\neq
\varnothing.
$$

______________________________________________________________________

## 11. Ownership is not authority

A named gap owner does not automatically gain authority to bypass the gap.

$$
\boxed{
\operatorname{Owns}(o,g)
\not\Rightarrow
\operatorname{AuthorizedToOverride}(o,g).
}
$$

Nor:

$$
\operatorname{Owns}(o,g)
\not\Rightarrow
\operatorname{AuthorizedToCommit}(o).
$$

Ownership should be interpreted as responsibility for routing, resolution, escalation, or stewardship unless a separate authority binding says otherwise.

This preserves the L30 authority-boundary linkage.

______________________________________________________________________

## 12. Proposed critical-gap record

A typed representation is:

$$
G=
(id,c,s,o,p,d,e,r,t,\pi),
$$

where:

- (id) = gap identity;
- (c) = criticality/severity class;
- (s) = resolution state;
- (o) = owner or owning process;
- (p) = affected consequential paths;
- (d) = dependencies;
- (e) = evidence required for closure;
- (r) = regime/scope;
- (t) = temporal/freshness state;
- (\\pi) = provenance.

```yaml
classification: DERIVED_FORMALIZATION

CRITICAL_GAP_RECORD:
  gap_id: REQUIRED

  severity:
    required_value: CRITICAL

  resolution_state:
    state: REQUIRED

  blocking_domain:
    allowed_source_supported_values:
      - SAFETY
      - INTEGRITY
      - AUTHORITY

  owner:
    requirement: REQUIRED
    type:
      - OWNER
      - OWNING_PROCESS

  affected_paths:
    state: REQUIRED_FOR_ENFORCEMENT

  dependency_refs:
    state: REQUIRED_FOR_ENFORCEMENT

  provenance:
    state: REQUIRED

  scope:
    state: REQUIRED

  regime:
    state: REQUIRED_WHEN_MATERIAL

  closure_evidence:
    state: UNKNOWN/GAP

  validation_receipt:
    state: UNKNOWN/GAP
```

The schema is **DERIVED**, not source canon.

______________________________________________________________________

## 13. Gap lifecycle

A minimal proposed lifecycle is:

$$
\texttt{DETECTED}
\rightarrow
\texttt{CLASSIFIED}
\rightarrow
\texttt{OWNED}
\rightarrow
\texttt{RESOLUTION\_PENDING}
\rightarrow
\texttt{VALIDATED\_CLOSED}.
$$

But the source does not define this state machine.

Therefore:

$$
\boxed{
\operatorname{CanonicalGapLifecycle}
=
\texttt{UNKNOWN/GAP}.
}
$$

L28 establishes requirements on critical gaps, not a complete lifecycle ontology.

______________________________________________________________________

## 14. Closure condition

A gap should not be treated as closed merely because someone marks it closed.

A proposed integrity condition is:

$$
\operatorname{Close}(g)
\Rightarrow
\operatorname{ResolutionEvidenceValid}(g)
\land
\operatorname{DependenciesRevalidated}(g).
$$

For consequential gaps:

$$
\operatorname{CloseCritical}(g)
\Rightarrow
\operatorname{ValidationReceipt}(g).
$$

This is a **DERIVED validation requirement**, not explicit L28 source text.

______________________________________________________________________

## 15. No warning-only downgrade

CG-2 gives an especially strong invariant.

For unresolved critical gap (g):

$$
\operatorname{Consequential}(o)
\land
\operatorname{RoutesThrough}(o,g)
\Rightarrow
\neg\operatorname{WarningOnly}(o,g).
$$

Therefore:

$$
\boxed{
\texttt{DENY}
\neq
\texttt{WARN\_AND\_CONTINUE}.
}
$$

An implementation that detects the critical gap but permits the consequential operation after merely emitting a warning violates the proposed specification.

______________________________________________________________________

## 16. Failure recovery coupling

The source explicitly relates L28 to `L10_FAILURE_RECOVERY`.

A safe derived interaction is:

If:

$$
o
$$

fails because of critical gap (g), then the response should target the affected dependency region rather than invalidate unrelated state.

Let:

$$
\operatorname{Desc}(g)
=
\{x\mid g\leadsto x\}.
$$

Then:

$$
\boxed{
\operatorname{CriticalFailure}(g)
\Rightarrow
\operatorname{Invalidate}
\left(
\operatorname{DependentDescendants}(g)
\right).
}
$$

Not necessarily:

$$
\operatorname{InvalidateEntireSystem}.
$$

This preserves fail-closed behavior while allowing local recovery where independence is actually demonstrated.

______________________________________________________________________

## 17. Execution coupling

The explicit `L8_EXECUTION` relation implies L28 constrains execution semantics, but the exact binding is not supplied here.

A derived execution gate is:

$$
\operatorname{EXECUTE}(o)
\Rightarrow
\neg\operatorname{BlockedByCriticalGap}(o).
$$

For consequential execution:

$$
\boxed{
\operatorname{EXECUTE}_{C}(o)
\Rightarrow
\forall g\in D^{*}(o):
\neg[
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g)
].
}
$$

This is a necessary condition, not a complete authorization rule.

______________________________________________________________________

## 18. Authority-boundary coupling

Suppose authority determination depends on unresolved gap (g_A):

$$
g_A
\in
D^{*}(\operatorname{AuthorityDecision}).
$$

If:

$$
\operatorname{Critical}(g_A)
\land
\operatorname{Unresolved}(g_A),
$$

then:

$$
\boxed{
\operatorname{AuthorityDecision}
=
\texttt{DENY/HOLD}
}
$$

rather than inferring authorization.

In particular:

$$
\operatorname{UnknownAuthority}
\not\Rightarrow
\operatorname{Authorized}.
$$

This is one of L28's strongest integrity consequences.

______________________________________________________________________

## 19. Fail-closed governance

The source links `FAIL_CLOSED_GOVERNANCE`.

For a critical unresolved premise (p):

$$
\operatorname{State}(p)=\texttt{UNKNOWN/GAP}
$$

and consequential operation (o) depending on (p):

$$
p\in D^{*}(o),
$$

then:

$$
\boxed{
\operatorname{COMMIT}(o)
\text{ is not licensed}.
}
$$

Fail closed means preserving uncertainty rather than converting it into positive permission.

______________________________________________________________________

## 20. Recursive ontology relationship

The source explicitly links:

`TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS`.

That establishes a declared relationship, but the source does not state its semantic type beyond the label `Trang Framework`.

Therefore:

$$
\operatorname{Related}
(L_{28},T_{\mathrm{ROD}})
$$

is source-supported, while stronger claims such as:

$$
L_{28}
=
\operatorname{DerivedFrom}(T_{\mathrm{ROD}})
$$

or:

$$
T_{\mathrm{ROD}}
\Rightarrow
L_{28}
$$

remain:

$$
\texttt{UNKNOWN/GAP}.
$$

Structural correspondence alone is insufficient to establish derivation or causation.

______________________________________________________________________

## 21. Source falsifier

The source declares exactly one falsifier:

> F1: authoritative canon permits consequential execution across critical gaps.

Formalized:

$$
F_1
=
\exists o,g:
\operatorname{AuthoritativeCanonPermits}(o)
\land
\operatorname{Consequential}(o)
\land
\operatorname{RoutesThrough}(o,g)
\land
\operatorname{Critical}(g).
$$

Because the law text repeatedly concerns **unresolved** critical gaps, the strongest internally consistent reading is that unresolved status is load-bearing. However, that qualifier is not literally repeated in F1.

Therefore the exact source falsifier should remain unchanged rather than silently rewritten.

______________________________________________________________________

## 22. Derived validation conditions

The following are not source falsifiers; they are **DERIVED validation conditions**.

$$
V_1:
\quad
\text{a safety-blocking gap is classified CRITICAL}.
$$

$$
V_2:
\quad
\text{an integrity-blocking gap is classified CRITICAL}.
$$

$$
V_3:
\quad
\text{an authority-blocking gap is classified CRITICAL}.
$$

$$
V_4:
\quad
\text{a consequential operation through an unresolved critical gap is denied}.
$$

$$
V_5:
\quad
\text{warning-only continuation is impossible for that path}.
$$

$$
V_6:
\quad
\text{the critical gap is surfaced prominently}.
$$

$$
V_7:
\quad
\text{the critical gap has an owner or owning process}.
$$

$$
V_8:
\quad
\text{unrelated operations are not automatically denied unless dependency coupling is established}.
$$

______________________________________________________________________

## 23. Sensitivity boundary

The smallest premise capable of flipping the execution result is often:

$$
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g)
\land
\operatorname{RoutesThrough}(o,g)
\land
\operatorname{Consequential}(o).
$$

If any of these load-bearing conditions changes, the L28 denial conclusion may need reevaluation.

Thus:

$$
\boxed{
D(o)=
C(g)\land U(g)\land R(o,g)\land Q(o)
}
$$

is a useful derived decision boundary.

This makes criticality classification itself highly consequential and therefore deserving of provenance and validation.

______________________________________________________________________

## 24. False-positive / false-negative asymmetry

Two classification failures exist.

### False negative

$$
\operatorname{ActuallyCritical}(g)
\land
\operatorname{ClassifiedNonCritical}(g).
$$

This can permit unsafe consequential execution.

### False positive

$$
\operatorname{ActuallyNonCritical}(g)
\land
\operatorname{ClassifiedCritical}(g).
$$

This can unnecessarily deny valid operations.

Because L28 is fail-closed, the specification structurally prioritizes avoiding the first failure where safety, integrity, or authority is blocked.

That is a governance interpretation, not empirical evidence about optimal system behavior.

______________________________________________________________________

## 25. Provenance requirement

A criticality decision should conceptually preserve:

$$
\Pi(g)=
(
\text{claim},
\text{classification basis},
\text{evidence},
\text{scope},
\text{regime},
\text{dependencies},
\text{owner},
\text{falsifiers},
\text{freshness}
).
$$

Without the classification basis:

$$
\operatorname{Critical}(g)
$$

becomes an untraceable governance assertion.

A proposed proof obligation is:

$$
\operatorname{Critical}(g)
\Rightarrow
\exists e:
\operatorname{SupportsCriticalClassification}(e,g).
$$

This is DERIVED.

______________________________________________________________________

## 26. Full RSCF H/M/L expansion

```yaml
classification: DERIVED_FORMALIZATION

RSCF_EXPANSION:
  source_node:
    node_id: l28_critical_gap
    node_type: note
    path: 01_CANON/01_CORE_LAWS/L28_CRITICAL_GAP.md
    claim_class: AMOS_MODEL

  source_frontmatter_rscf:
    state: SOURCE_CLAIM
    claim_class: CONDITIONAL
    provenance: AMOS_corpus
    scope: core_laws

  source_status:
    specification: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL
    updated: 2026-08-26

  H:
    role: CORE_LAW_GOVERNANCE
    concerns:
      - critical_gap_governance
      - fail_closed_execution
      - safety
      - integrity
      - authority

  M:
    role: CRITICAL_GAP_CONTROL
    source_laws:
      - CG-1_CRITICAL_CLASSIFICATION
      - CG-2_NO_CONSEQUENTIAL_PATH_THROUGH_CRITICAL_GAP
      - CG-3_VISIBLE_ESCALATION
      - CG-4_OWNER_REQUIRED

  L:
    role: INDIVIDUAL_GAP_DECISION
    decision_fields:
      - gap_identity
      - criticality
      - resolution_state
      - affected_path
      - consequentiality
      - owner
      - scope
      - regime
      - provenance

  executable_binding:
    state: UNKNOWN/GAP

  artifact_specific_validation:
    state: UNKNOWN/GAP
```

The final two fields are derived gaps because the source does not provide implementation or validation receipts.

______________________________________________________________________

## 27. Machine representation

```yaml
classification: DERIVED_FORMALIZATION

L28_CRITICAL_GAP:
  source_state:
    status: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL

  rscf:
    state: SOURCE_CLAIM
    claim_class: CONDITIONAL
    provenance: AMOS_corpus
    scope: core_laws

  laws:
    CG_1:
      name: Critical Classification
      condition:
        gap_blocks_any:
          - SAFETY
          - INTEGRITY
          - AUTHORITY
      consequence:
        classification: CRITICAL
        governance: FAIL_CLOSED_IMMEDIATELY

    CG_2:
      name: No Consequential Path Through Critical Gap
      condition:
        critical_gap: true
        unresolved: true
        operation_routes_through_gap: true
        operation_consequential: true
      consequence:
        decision: DENY
        warning_only: PROHIBITED

    CG_3:
      name: Visible Escalation
      condition:
        critical_gap: true
      consequence:
        status_visibility: TOP_LEVEL
        buried: PROHIBITED

    CG_4:
      name: Owner Required
      condition:
        critical_gap: true
      consequence:
        owner_or_owning_process: REQUIRED

  source_falsifier:
    F1: "authoritative canon permits consequential execution across critical gaps"

  canonical_gap_lifecycle:
    state: UNKNOWN/GAP

  executable_enforcement:
    state: UNKNOWN/GAP

  executed_validation:
    state: UNKNOWN/GAP
```

The booleans inside `condition` are declarative predicate values in this derived representation; they are not claims about a deployed runtime.

______________________________________________________________________

## 28. Exact source RSCF preservation

```text
RSCF-NODE

node_id: l28_critical_gap

node_type: note

path: 01_CANON/01_CORE_LAWS/L28_CRITICAL_GAP.md

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

  - CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

claim_class: AMOS_MODEL
```

No additional RSCF relation is inserted.

______________________________________________________________________

## 29. Proof capsule

```yaml
classification: DERIVED_FORMALIZATION

PROOF_CAPSULE:
  claim:
    "Unresolved critical gaps block consequential operations that route through them."

  conclusion_class: CONDITIONAL

  source_basis:
    - CG-1
    - CG-2
    - CG-3
    - CG-4

  load_bearing_premises:
    - gap is classified CRITICAL
    - gap remains unresolved
    - operation routes through the gap
    - operation is consequential

  consequence:
    operation: DENY

  non_consequences:
    - gap is not thereby proven false
    - every UNKNOWN/GAP is not thereby CRITICAL
    - unrelated operations are not thereby proven blocked
    - owner is not thereby granted override authority
    - visibility is not authority

  source_falsifier:
    - "authoritative canon permits consequential execution across critical gaps"

  implementation_state:
    state: UNKNOWN/GAP

  validation_state:
    state: UNKNOWN/GAP
```

## Canonical Compression

The strongest source-supported L28 rule is:

$$
\boxed{
\operatorname{GapBlocks}
(
\text{SAFETY}
\lor
\text{INTEGRITY}
\lor
\text{AUTHORITY}
)
\Rightarrow
\operatorname{CRITICAL}
}
$$

followed by:

$$
\boxed{
\operatorname{CRITICAL}(g)
\Rightarrow
\operatorname{FAIL\_CLOSED}(g)
}
$$

and, for consequential execution:

$$
\boxed{
\operatorname{Consequential}(o)
\land
\operatorname{RoutesThrough}(o,g)
\land
\operatorname{Critical}(g)
\land
\operatorname{Unresolved}(g)
\Rightarrow
\operatorname{DENY}(o).
}
$$

The other source obligations are:

$$
\boxed{
\operatorname{Critical}(g)
\Rightarrow
\operatorname{VisibleEscalation}(g)
}
$$

and:

$$
\boxed{
\operatorname{Critical}(g)
\Rightarrow
\exists o\,
\operatorname{Owns}(o,g).
}
$$

The crucial firewall is:

$$
\boxed{
\texttt{CRITICAL}
\neq
\texttt{FALSE}
\neq
\texttt{UNKNOWN/GAP}
}
$$

while:

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\texttt{PASS}.
}
$$

L28 therefore operates as a **conditional fail-closed governance law for consequential paths under critical unresolved uncertainty**, not as a mechanism for converting uncertainty into truth or falsity.

**Source conclusion class:** `CONDITIONAL / AMOS_MODEL / PROPOSED_SPECIFICATION`.
**Derived formalization:** `DERIVED / PROPOSED`.
**Executable enforcement and artifact-specific validation:** `UNKNOWN/GAP` from this source alone.
```
