---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: L30 Authority Boundary
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
`L30 AUTHORITY BOUNDARY` defines typed artifact specification, serving the Canon plane's obligation: canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession.

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
Given an operation touching `L30 AUTHORITY BOUNDARY` within the Canon plane:
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
RSCF-NODE
node_id: l30_authority_boundary
node_type: note
path: 01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

The exact artifact is also addressable in Drive as `L30_AUTHORITY_BOUNDARY.md`. That establishes file presence/addressability only; it does not independently validate the law. 

## Derived / Proposed AMOS Formalization

Everything below is **DERIVED / PROPOSED**. It does not modify the source artifact.

A source-structure issue remains intentionally unresolved: `claim_class: AMOS_MODEL` is indented beneath the final `CHILD_OF` item in the literal RSCF block. No correction is made because the intended structural binding is not established by the source.

## 1. Epistemic and canonical state

For artifact \(L_{30}\):

$$
\operatorname{Status}(L_{30})
=
\texttt{PROPOSED\_SPECIFICATION}
$$

$$
\operatorname{EpistemicClass}(L_{30})
=
\texttt{AMOS\_MODEL}
$$

$$
\operatorname{CanonicalStatus}(L_{30})
=
\texttt{CONDITIONAL}
$$

while its frontmatter declares:

$$
\operatorname{RSCFState}(L_{30})
=
\texttt{SOURCE\_CLAIM}
$$

and

$$
\operatorname{RSCFClaimClass}(L_{30})
=
\texttt{CONDITIONAL}.
$$

These are separate typed dimensions:

$$
\boxed{
\texttt{SOURCE\_CLAIM}
\neq
\texttt{CONDITIONAL}
\neq
\texttt{AMOS\_MODEL}
\neq
\texttt{PROPOSED\_SPECIFICATION}
}
$$

unless a higher applicable canon explicitly establishes a mapping.

Therefore the strongest present classification is:

$$
\boxed{\text{SOURCE\_CLAIM / CONDITIONAL AMOS\_MODEL}}
$$

—not `VERIFIED`.

---

## 2. AB-1 — Authority as a typed envelope

The load-bearing source statement is:

$$
\boxed{
\operatorname{Consulted}(x)
\not\Rightarrow
\operatorname{Authorized}(x)
}
$$

A proposed authority envelope can be modeled as:

$$
\mathcal A_x
=
(S_x,O_x,R_x,\Sigma_x,\Gamma_x,T_x,V_x,P_x)
$$

where:

$$
S_x=\text{authorized subjects},
$$

$$
O_x=\text{authorized operations},
$$

$$
R_x=\text{authorized resources},
$$

$$
\Sigma_x=\text{scope},
$$

$$
\Gamma_x=\text{regime},
$$

$$
T_x=\text{temporal/epoch validity},
$$

$$
V_x=\text{version/state constraints},
$$

$$
P_x=\text{authority provenance}.
$$

Then an authorization claim is local to that envelope:

$$
\operatorname{Authorized}(s,o,r,\sigma,\gamma,t)
\Rightarrow
(s,o,r,\sigma,\gamma,t)\in\mathcal A_x.
$$

The exact canonical envelope schema is not supplied:

$$
\boxed{
\operatorname{CanonicalAuthorityEnvelope}
=
\texttt{UNKNOWN/GAP}
}
$$

---

## 3. Authority is not a scalar gradient

AB-1 rejects treating influence as authority.

Therefore a model such as

$$
A(x)\in[0,1]
$$

cannot by itself represent the source law if larger \(A(x)\) is interpreted as progressively greater authorization.

Instead authorization is typed:

$$
\operatorname{Auth}:
S\times O\times R\times\Sigma\times\Gamma\times T
\rightarrow
\{
\texttt{AUTHORIZED},
\texttt{UNAUTHORIZED},
\texttt{UNKNOWN/GAP}
\}.
$$

Consequently:

$$
\operatorname{Influence}(x)\uparrow
\not\Rightarrow
\operatorname{Authority}(x)\uparrow.
$$

Likewise:

$$
\operatorname{Importance}(x)
\not\Rightarrow
\operatorname{Authority}(x),
$$

$$
\operatorname{Expertise}(x)
\not\Rightarrow
\operatorname{Authority}(x),
$$

$$
\operatorname{Consulted}(x)
\not\Rightarrow
\operatorname{Authority}(x).
$$

---

## 4. Authority locality

Authorization for one operation does not silently transfer to another:

$$
\operatorname{Authorized}(x,o_1,r_1,\sigma_1,\gamma_1)
\not\Rightarrow
\operatorname{Authorized}(x,o_2,r_2,\sigma_2,\gamma_2).
$$

Therefore authority is modeled as:

$$
\boxed{
\text{local}
+
\text{typed}
+
\text{scoped}
+
\text{regime-bound}
+
\text{freshness-bounded}
}
$$

rather than as a global property of an identity.

---

## 5. AB-2 — Root Attestation

The source requires enforcement roots to be:

$$
\operatorname{AgentImmutable}(r),
$$

$$
\operatorname{Attested}(r),
$$

$$
\operatorname{Fresh}(r).
$$

A conservative formalization is the necessary implication:

$$
\boxed{
\operatorname{UsableEnforcementRoot}(r)
\Rightarrow
\operatorname{AgentImmutable}(r)
\land
\operatorname{Attested}(r)
\land
\operatorname{Fresh}(r)
}
$$

rather than the stronger unsupported biconditional.

Critically:

$$
\operatorname{AgentImmutable}(r)
\not\Rightarrow
\operatorname{UniversallyImmutable}(r).
$$

The source says **agent-immutable**, not absolutely immutable.

---

## 6. ERA remains unresolved

The artifact says:

> fresh (ERA discipline)

but does not define `ERA`.

Therefore:

$$
\boxed{
\operatorname{Definition}(\texttt{ERA})
=
\texttt{UNKNOWN/GAP}
}
$$

from L30 alone.

No acronym expansion, epoch mechanism, cryptographic protocol, or freshness duration should be invented.

Likewise:

$$
\operatorname{AttestationProtocol}
=
\texttt{UNKNOWN/GAP},
$$

$$
\operatorname{FreshnessThreshold}
=
\texttt{UNKNOWN/GAP}.
$$

---

## 7. Freshness formalization

A proposed generic freshness predicate is:

$$
\operatorname{Fresh}(r,t)
\iff
t-t_a\leq\Delta_r,
$$

where \(t_a\) is the last valid attestation time.

But the source does not provide \(\Delta_r\).

Thus:

$$
\Delta_r=\texttt{UNKNOWN/GAP}.
$$

The equation defines a possible formal shape, not a canonical AMOS duration.

---

## 8. AB-3 — Boundary Checks First

Let:

$$
B_f(x)
$$

be the field-specific boundary check applicable to field \(f\), and let:

$$
G(x)
$$

be a catch-all contract.

The source establishes ordering:

$$
\boxed{
B_f(x)\prec G(x)
}
$$

where \(\prec\) means “must be evaluated before.”

Therefore:

$$
x
\rightarrow
B_f
\rightarrow
G
\rightarrow
\operatorname{CandidateDecision}.
$$

Not:

$$
x
\rightarrow
G
\rightarrow
\text{assume }B_f\text{ passed}.
$$

A generic contract cannot launder a failed specific check:

$$
B_f(x)=\texttt{FAIL}
\land
G(x)=\texttt{PASS}
\not\Rightarrow
B_f(x)=\texttt{PASS}.
$$

And:

$$
B_f(x)=\texttt{UNKNOWN/GAP}
\not\Rightarrow
B_f(x)=\texttt{PASS}.
$$

---

## 9. AB-4 — Exact separability

Define:

$$
\mathcal D_A
=
\{
C,R,I,A,D,O,E,F,K
\}
$$

with:

$$
C=\text{Capability},
\quad
R=\text{Reachability},
\quad
I=\text{Identity},
$$

$$
A=\text{Authorization},
\quad
D=\text{Delegation},
\quad
O=\text{Observability},
$$

$$
E=\text{Enforcement},
\quad
F=\text{Finality},
\quad
K=\text{Consequence}.
$$

The source asserts their conceptual non-identity:

$$
\boxed{
C\neq R\neq I\neq A\neq D\neq O\neq E\neq F\neq K
}
$$

This does **not** establish statistical or causal independence.

In particular:

$$
x\neq y
\not\Rightarrow
x\perp y.
$$

AB-4 separates types; it does not prove they never interact.

---

## 10. Capability firewall

$$
\boxed{
\operatorname{Capable}(x,o)
\not\Rightarrow
\operatorname{Authorized}(x,o)
}
$$

A system may possess the technical ability to perform an operation while lacking permission to perform it.

Thus:

$$
\boxed{\text{CAPABILITY}\neq\text{AUTHORITY}}
$$

---

## 11. Reachability firewall

$$
\boxed{
\operatorname{Reachable}(x,r)
\not\Rightarrow
\operatorname{Authorized}(x,r)
}
$$

Connectivity or accessibility establishes neither permission nor delegation.

Therefore:

$$
\boxed{
\text{can reach}
\neq
\text{may act}
}
$$

---

## 12. Identity firewall

$$
\operatorname{IdentityResolved}(x)
\not\Rightarrow
\operatorname{Authorized}(x,o).
$$

Identity establishes who or what is acting.

Authorization establishes whether that identity may perform operation \(o\) under the relevant envelope.

Hence:

$$
\boxed{I\neq A}
$$

---

## 13. Delegation firewall

Authorization does not automatically confer delegation power:

$$
\boxed{
\operatorname{Authorized}(x,o)
\not\Rightarrow
\operatorname{CanDelegate}(x,o,y)
}
$$

A proposed delegation relation is:

$$
D(g,d,o,\sigma,\gamma,\tau,p)
$$

where:

* \(g\) = grantor;
* \(d\) = delegate;
* \(o\) = operation;
* \(\sigma\) = scope;
* \(\gamma\) = regime;
* \(\tau\) = temporal envelope;
* \(p\) = provenance.

The canonical delegation schema remains:

$$
\texttt{UNKNOWN/GAP}.
$$

---

## 14. Observability firewall

$$
\boxed{
\operatorname{CanObserve}(x,s)
\not\Rightarrow
\operatorname{CanControl}(x,s)
}
$$

and:

$$
\operatorname{Logged}(a)
\not\Rightarrow
\operatorname{Approved}(a).
$$

Observability may provide evidence about an authority decision without itself becoming authority.

---

## 15. Enforcement firewall

$$
\operatorname{Authorized}(a)
\not\Rightarrow
\operatorname{Enforced}(a)
$$

and:

$$
\operatorname{Enforced}(a)
\not\Rightarrow
\operatorname{Authorized}(a).
$$

This yields two independent failure classes:

$$
\text{authorized but not enforced},
$$

and

$$
\text{enforced without valid authorization}.
$$

---

## 16. Finality firewall

$$
\operatorname{Enforced}(a)
\not\Rightarrow
\operatorname{Final}(a).
$$

Likewise:

$$
\operatorname{Final}(a)
\not\Rightarrow
\operatorname{Authorized}(a).
$$

Finality cannot retroactively manufacture authority.

The source provides no finality protocol:

$$
\operatorname{CanonicalFinalityProtocol}
=
\texttt{UNKNOWN/GAP}.
$$

---

## 17. Consequence firewall

$$
\operatorname{ProducedConsequence}(a)
\not\Rightarrow
\operatorname{Authorized}(a).
$$

Nor does finality imply complete knowledge of consequences:

$$
\operatorname{Final}(a)
\not\Rightarrow
\operatorname{AllConsequencesKnown}(a).
$$

Thus actual effects prove occurrence, not legitimate authority.

---

## 18. Authority vector

A useful derived non-scalar representation is:

$$
\mathbf A(x)
=
(C,R,I,A,D,O,E,F,K).
$$

Each component is evaluated independently enough to preserve its type.

For example:

$$
C=\texttt{AVAILABLE}
$$

does not determine:

$$
A.
$$

Therefore:

$$
\boxed{
\mathbf A(x)
\not\equiv
a_x\in\mathbb R
}
$$

for authority resolution.

---

## 19. Scope/regime authority firewall

For authority envelope:

$$
\mathcal E_1=(S_1,\Gamma_1,T_1,\ldots)
$$

and another envelope:

$$
\mathcal E_2=(S_2,\Gamma_2,T_2,\ldots),
$$

authorization under the first does not silently transfer:

$$
\operatorname{Authorized}(x,\mathcal E_1)
\not\Rightarrow
\operatorname{Authorized}(x,\mathcal E_2).
$$

Cross-envelope transfer requires an explicit applicable bridge.

Therefore:

$$
\boxed{
\text{authority cannot silently leak across scope or regime}.
}
$$

---

## 20. Epistemic/authority separation

A claim can be epistemically strong without conferring execution authority:

$$
\operatorname{Verified}(c)
\not\Rightarrow
\operatorname{AuthorizedToCommit}(x,c).
$$

Conversely:

$$
\operatorname{AuthorizedToCommit}(x,c)
\not\Rightarrow
\operatorname{Verified}(c).
$$

Therefore:

$$
\boxed{
\text{epistemic validity}
\neq
\text{authority validity}
}
$$

This is the cleanest L1/L30 boundary.

---

## 21. L29 decision-value boundary

Decision value cannot override authority:

$$
\operatorname{HighDecisionValue}(a)
\not\Rightarrow
\operatorname{Authorized}(a).
$$

Even if:

$$
V(a)>V(b),
$$

that comparison does not create permission to execute \(a\).

For a consequential action:

$$
\neg\operatorname{Authorized}(a)
\Rightarrow
\neg\operatorname{COMMIT}(a).
$$

Thus:

$$
\boxed{
\text{best available action}
\neq
\text{authorized action}
}
$$

---

## 22. L28 critical-gap boundary

Where authority is load-bearing:

$$
\operatorname{Authority}(a)
=
\texttt{UNKNOWN/GAP}
$$

cannot be silently interpreted as authorization.

A derived fail-closed condition is:

$$
\operatorname{Consequential}(a)
\land
\operatorname{AuthorityCritical}(a)
\land
\operatorname{Authority}(a)=\texttt{UNKNOWN/GAP}
\Rightarrow
\operatorname{HOLD}(a).
$$

This preserves:

$$
\boxed{\texttt{UNKNOWN/GAP}\neq\texttt{PASS}}
$$

---

## 23. Competing authority claims

Suppose:

$$
H_1:
\operatorname{Authorized}(x,a)
$$

and

$$
H_2:
\neg\operatorname{Authorized}(x,a).
$$

If both claims apply to compatible subject, operation, scope, regime, version, and epoch, but precedence cannot be established:

$$
\operatorname{AuthorityState}(x,a)
=
\texttt{COMPETING}.
$$

Then:

$$
\boxed{
\texttt{COMPETING}
\not\Rightarrow
\texttt{AUTHORIZED}
}
$$

No fluent reconciliation should erase the conflict.

---

## 24. Freshness and epoch validity

An authority determination valid at \(t_0\) is not automatically valid at \(t_1\):

$$
A_{t_0}
\not\Rightarrow
A_{t_1}.
$$

If:

$$
t_1\notin T_A,
$$

where \(T_A\) is the valid temporal envelope, then revalidation is required.

Therefore:

$$
\boxed{
\text{previously authorized}
\neq
\text{currently authorized}
}
$$

---

## 25. Provenance topology

A proposed authority proof should preserve ancestry.

If:

$$
A_1\leftarrow P
$$

and

$$
A_2\leftarrow P,
$$

then \(A_1\) and \(A_2\) are not independent confirmations merely because they appear as two records.

Thus:

$$
\operatorname{Count}(A_i)>1
\not\Rightarrow
\operatorname{IndependentConfirmation}>1.
$$

Authority repetition is not authority independence.

---

## 26. Delegation lineage

For:

$$
x_0
\xrightarrow{D_1}
x_1
\xrightarrow{D_2}
\cdots
\xrightarrow{D_n}
x_n,
$$

a conservative validity condition is:

$$
\operatorname{ValidDelegatedAuthority}(D_n)
\Rightarrow
\bigwedge_{i=1}^{n}
\operatorname{Valid}(D_i).
$$

If one load-bearing delegation edge becomes invalid:

$$
\neg\operatorname{Valid}(D_k)
$$

then dependent downstream authority must be re-evaluated.

Unrelated authority does not automatically fail.

---

## 27. Smallest sufficient authority closure

Let:

$$
D_A^*(a)
$$

be the smallest dependency set whose state can change the authorization result for action \(a\).

A proposed local decision is safe only if:

$$
\operatorname{ClosureKnown}(D_A^*)
$$

$$
\land
\operatorname{ScopeCompatible}(D_A^*)
$$

$$
\land
\operatorname{RegimeCompatible}(D_A^*)
$$

$$
\land
\operatorname{Fresh}(D_A^*)
$$

$$
\land
\operatorname{NonConflict}(D_A^*)
$$

$$
\land
\operatorname{ProvenanceAdequate}(D_A^*).
$$

Otherwise:

$$
\operatorname{ESCALATE/HOLD}.
$$

---

## 28. Consequential commit condition

For consequential action \(a\), a conservative necessary-condition model is:

$$
\boxed{
\operatorname{COMMIT}(a)
\Rightarrow
\operatorname{IdentityValid}(a)
\land
\operatorname{ScopeValid}(a)
\land
\operatorname{RegimeValid}(a)
\land
\operatorname{SpecificBoundaryValid}(a)
\land
\operatorname{AuthorityValid}(a)
}
$$

and where an enforcement root \(r\) is load-bearing:

$$
\operatorname{COMMIT}(a)
\Rightarrow
\operatorname{AgentImmutable}(r)
\land
\operatorname{Attested}(r)
\land
\operatorname{Fresh}(r).
$$

This is deliberately **not** written as:

$$
\operatorname{COMMIT}(a)
\iff \cdots
$$

because L30 does not establish sufficiency.

---

## 29. Atomic authority mutation

For a coupled authority update:

$$
\Delta_A=
\{\delta_1,\delta_2,\ldots,\delta_n\},
$$

a proposed integrity rule is:

$$
\operatorname{COMMIT}(\Delta_A)
\Rightarrow
\bigwedge_{i=1}^{n}
\operatorname{Valid}(\delta_i).
$$

If a load-bearing mutation fails:

$$
\exists i:
\neg\operatorname{Valid}(\delta_i),
$$

then:

$$
\operatorname{HOLD/ROLLBACK}(\Delta_A).
$$

This is an AMOS architectural formalization, not evidence that L30 itself implements atomic transactions.

---

## 30. Version-safe mutation

MVCC/CAS concepts can express a proposed authority-state guard:

$$
A^{(v)}
\xrightarrow{\Delta}
A^{(v+1)}.
$$

Commit requires the observed state still to match the expected state:

$$
v_{\mathrm{observed}}
=
v_{\mathrm{expected}}.
$$

Otherwise:

$$
\operatorname{REVALIDATE}.
$$

This prevents a stale authority decision from silently committing against changed state.

Again:

$$
\boxed{\text{MODEL}\neq\text{IMPLEMENTED RUNTIME}}
$$

---

## 31. Local invalidation

If authority premise \(p\) becomes invalid:

$$
\operatorname{Invalid}(p)
\Rightarrow
\operatorname{Invalidate}(\operatorname{Desc}(p)).
$$

But:

$$
x\notin\operatorname{Desc}(p)
$$

does not justify invalidating \(x\) solely because \(p\) failed.

Thus authority failure recovery should be dependency-local rather than automatically global.

---

## 32. Source falsifier formalization

The source declares:

> F1: authoritative authority canon merges any separated term.

Let:

$$
\mathcal D_A
=
\{
C,R,I,A,D,O,E,F,K
\}.
$$

Then:

$$
F_1
=
\exists x,y\in\mathcal D_A:
x\neq y
\land
\operatorname{AuthoritativeCanon}(x\equiv y).
$$

If a genuinely authoritative, applicable authority canon establishes such an equivalence, L30's AB-4 formulation must be re-evaluated.

This is a **source-declared falsifier**, not a derived one.

---

## Derived validation matrix

| Check             | Required relation                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Consultation      | \(\operatorname{Consulted}\not\Rightarrow\operatorname{Authorized}\)                                                       |
| Capability        | \(C\not\Rightarrow A\)                                                                                                     |
| Reachability      | \(R\not\Rightarrow A\)                                                                                                     |
| Identity          | \(I\not\Rightarrow A\)                                                                                                     |
| Delegation        | \(A\not\Rightarrow D\)                                                                                                     |
| Observability     | \(O\not\Rightarrow A\)                                                                                                     |
| Enforcement       | \(E\not\Rightarrow A\)                                                                                                     |
| Finality          | \(F\not\Rightarrow A\)                                                                                                     |
| Consequence       | \(K\not\Rightarrow A\)                                                                                                     |
| Root admission    | \(\operatorname{UsableRoot}\Rightarrow\operatorname{AgentImmutable}\land\operatorname{Attested}\land\operatorname{Fresh}\) |
| Boundary order    | \(B_f\prec G\)                                                                                                             |
| Unknown authority | \(\texttt{UNKNOWN/GAP}\neq\texttt{AUTHORIZED}\)                                                                            |

These are **DERIVED validation conditions**, except where they directly restate AB-1–AB-4.

## Full RSCF H/M/L expansion

```yaml
classification: DERIVED_FORMALIZATION

RSCF_EXPANSION:
  source_node:
    node_id: l30_authority_boundary
    node_type: note
    path: 01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY.md

  source_frontmatter:
    state: SOURCE_CLAIM
    claim_class: CONDITIONAL
    provenance: AMOS_corpus
    scope: core_laws

  source_status:
    status: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL
    updated: 2026-08-26

  H:
    role: AUTHORITY_BOUNDARY_GOVERNANCE
    concerns:
      - authority_envelopes
      - enforcement_roots
      - scope_regime_boundaries
      - typed_authority_separation

  M:
    role: AUTHORITY_RESOLUTION
    laws:
      - AB_1_ENVELOPE_NOT_GRADIENT
      - AB_2_ROOT_ATTESTATION
      - AB_3_BOUNDARY_CHECKS_FIRST
      - AB_4_SEPARABILITY

  L:
    role: OPERATION_SPECIFIC_AUTHORITY_CHECK
    proposed_dimensions:
      - capability
      - reachability
      - identity
      - authorization
      - delegation
      - observability
      - enforcement
      - finality
      - consequence
      - scope
      - regime
      - temporal_validity
      - provenance
      - root_attestation

  canonical_authority_envelope:
    state: UNKNOWN/GAP

  canonical_ERA_definition:
    state: UNKNOWN/GAP

  canonical_freshness_threshold:
    state: UNKNOWN/GAP

  canonical_delegation_schema:
    state: UNKNOWN/GAP

  executable_enforcement_binding:
    state: UNKNOWN/GAP
```

## Machine representation

```yaml
classification: DERIVED_FORMALIZATION

L30_AUTHORITY_BOUNDARY:
  source:
    status: PROPOSED_SPECIFICATION
    epistemic_class: AMOS_MODEL
    canonical_status: CONDITIONAL
    rscf_state: SOURCE_CLAIM
    rscf_claim_class: CONDITIONAL

  AB_1:
    law: ENVELOPE_NOT_GRADIENT
    consulted_vs_authorized: DISTINCT
    scalar_authority_gradient: NOT_SUPPORTED_BY_SOURCE

  AB_2:
    law: ROOT_ATTESTATION
    requirements:
      agent_immutable: REQUIRED_BY_SOURCE
      attested: REQUIRED_BY_SOURCE
      fresh: REQUIRED_BY_SOURCE
    ERA_definition: UNKNOWN/GAP
    freshness_threshold: UNKNOWN/GAP
    attestation_protocol: UNKNOWN/GAP

  AB_3:
    law: BOUNDARY_CHECKS_FIRST
    precedence:
      first: FIELD_SPECIFIC_CHECK
      then: CATCH_ALL_CONTRACT

  AB_4:
    law: SEPARABILITY
    dimensions:
      - CAPABILITY
      - REACHABILITY
      - IDENTITY
      - AUTHORIZATION
      - DELEGATION
      - OBSERVABILITY
      - ENFORCEMENT
      - FINALITY
      - CONSEQUENCE

  source_falsifier:
    F1: "authoritative authority canon merges any separated term"

  canonical_authority_schema: UNKNOWN/GAP
  executable_authority_binding: UNKNOWN/GAP
  artifact_specific_validation: UNKNOWN/GAP
```

## Derived / proposed implementation gaps

```yaml
classification: DERIVED_FORMALIZATION

IMPLEMENTATION_GAPS:
  canonical_authority_envelope_schema: UNKNOWN/GAP
  ERA_definition: UNKNOWN/GAP
  enforcement_root_attestation_protocol: UNKNOWN/GAP
  freshness_threshold: UNKNOWN/GAP
  field_specific_boundary_registry: UNKNOWN/GAP
  delegation_schema: UNKNOWN/GAP
  authority_conflict_resolution: UNKNOWN/GAP
  authority_epoch_protocol: UNKNOWN/GAP
  finality_protocol: UNKNOWN/GAP
  executable_authority_binding: UNKNOWN/GAP
  artifact_specific_validation_receipt: UNKNOWN/GAP
```

## Source RSCF — literal preservation

```text
RSCF-NODE
node_id: l30_authority_boundary
node_type: note
path: 01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  claim_class: AMOS_MODEL
```

No additional source relation is inserted, and the final indentation is not silently repaired.

## Proof capsule

```yaml
classification: DERIVED_FORMALIZATION

PROOF_CAPSULE:
  claim:
    class: CONDITIONAL
    statement: >
      L30 models authority as a typed boundary envelope, requires
      agent-immutable/attested/fresh enforcement roots, gives
      field-specific boundary checks precedence over catch-all contracts,
      and separates capability, reachability, identity, authorization,
      delegation, observability, enforcement, finality, and consequence.

  load_bearing_source:
    - AB-1
    - AB-2
    - AB-3
    - AB-4

  provenance:
    source: AMOS_corpus
    scope: core_laws

  source_falsifier:
    - authoritative authority canon merges any separated term

  unresolved:
    - canonical authority envelope schema
    - ERA definition
    - freshness threshold
    - delegation schema
    - executable enforcement binding
    - artifact-specific validation

  confidence_ceiling:
    state: SOURCE_DOES_NOT_DECLARE_NUMERIC_VALUE
```

## Canonical Compression

The source-supported authority firewall is:

$$
\boxed{
\text{Authority}
=
\text{typed envelope}
\neq
\text{influence gradient}
}
$$

with:

$$
\boxed{
\operatorname{Consulted}
\not\Rightarrow
\operatorname{Authorized}
}
$$

and:

$$
\boxed{
\operatorname{UsableEnforcementRoot}(r)
\Rightarrow
\operatorname{AgentImmutable}(r)
\land
\operatorname{Attested}(r)
\land
\operatorname{Fresh}(r)
}
$$

while:

$$
\boxed{
\text{field-specific checks}
\prec
\text{catch-all contracts}
}
$$

and:

$$
\boxed{
\text{Capability}
\neq
\text{Reachability}
\neq
\text{Identity}
\neq
\text{Authorization}
\neq
\text{Delegation}
\neq
\text{Observability}
\neq
\text{Enforcement}
\neq
\text{Finality}
\neq
\text{Consequence}
}
$$

For consequential execution, the conservative derived gate is:

$$
\boxed{
\operatorname{COMMIT}(a)
\Rightarrow
\operatorname{IdentityValid}(a)
\land
\operatorname{ScopeValid}(a)
\land
\operatorname{RegimeValid}(a)
\land
\operatorname{SpecificBoundaryValid}(a)
\land
\operatorname{AuthorityValid}(a)
}
$$

but this implication is **necessary, not sufficient**.

**Conclusion class:** `SOURCE_CLAIM / CONDITIONAL AMOS_MODEL`.

**Canonical status:** `CONDITIONAL`.

**ERA definition, canonical authority-envelope schema, freshness threshold, delegation schema, executable authority binding, and artifact-specific validation:** `UNKNOWN/GAP` from this artifact alone.
```
