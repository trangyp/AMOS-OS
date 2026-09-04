---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: AMOS Global Contract for AI Coding Agents
type: note
source: 00_ROOT
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: .github/copilot-instructions.md
  scope: AMOS_general
tags:
  - contract
  - agent-agreement
  - ai-coding
---

# AMOS Global Contract for AI Coding Agents

## 0. Status

**DERIVED · AMOS_general · canonical vault entry point · authoritative contract content external to this note.**

This note is the canonical vault entry point for the global AMOS coding-agent contract.

The source declares:

```text
authoritative source: copilot-instructions.md
project location: project root
```

The note itself is therefore an index/binding artifact rather than the complete authoritative contract.

Formally, let:

$$
N=\texttt{AMOS Global Contract for AI Coding Agents}
$$

and:

$$
C=\texttt{copilot-instructions.md}
$$

Then the source-declared relationship is:

$$
\boxed{
N \xrightarrow{\mathrm{ENTRY\_POINT\_TO}} C
}
$$

not:

$$
N=C
$$

unless the contents are explicitly synchronized and validated.

______________________________________________________________________

## 1. Purpose

`AMOS Global Contract for AI Coding Agents` provides the canonical AMOS vault entry point for the global coding-agent contract.

Its primary functions are:

$$
\boxed{
\mathrm{DISCOVER}
\rightarrow
\mathrm{RESOLVE}
\rightarrow
\mathrm{AUTHORITATIVE\ SOURCE}
}
$$

The note establishes where an AMOS consumer should look for the governing contract while preserving the distinction between:

- the vault entry point;
- the agent-contract representation;
- the authoritative source file;
- any implementation that consumes that contract;
- executed validation of compliance.

Therefore:

$$
\boxed{
\mathrm{ENTRY\ POINT}
\neq
\mathrm{AUTHORITATIVE\ SOURCE}
\neq
\mathrm{IMPLEMENTATION}
\neq
\mathrm{VALIDATION}
}
$$

______________________________________________________________________

## 2. Authoritative Source

The supplied source states:

> The authoritative source lives at `copilot-instructions.md` in the project root.

The frontmatter separately records provenance as:

```yaml
provenance: .github/copilot-instructions.md
```

These are two distinct source-declared path expressions:

$$
P_1=\texttt{copilot-instructions.md}
$$

$$
P_2=\texttt{.github/copilot-instructions.md}
$$

The supplied artifact does not establish that:

$$
P_1=P_2
$$

Therefore the path relationship must remain unresolved rather than silently normalized:

$$
\boxed{
\operatorname{CanonicalPath}(C)
=
\texttt{UNKNOWN/GAP}
}
$$

until the repository binding confirms which path is authoritative or establishes that both expressions resolve to the same artifact.

This preserves both source statements without inventing reconciliation.

______________________________________________________________________

## 3. Contract Authority Boundary

The note calls the referenced file the **authoritative source**.

Therefore, within the scope declared by this artifact:

$$
\boxed{
\operatorname{ContractContentAuthority}(N)
\rightarrow C
}
$$

The vault note should not silently override contract semantics contained in (C).

If:

$$
\operatorname{Content}(N)\neq\operatorname{Content}(C)
$$

the note's descriptive or derived material does not automatically supersede (C).

A safe authority condition is:

$$
\boxed{
\operatorname{ContractClaim}(x)
\Rightarrow
\operatorname{TraceableTo}(x,C)
}
$$

for claims represented as authoritative contract requirements.

Derived AMOS analysis may exist around those requirements, but must remain typed as `DERIVED` rather than being silently promoted into contract authority.

______________________________________________________________________

## 4. Epistemic Classification

The supplied RSCF declaration is:

$$
\boxed{
\operatorname{State}(N)=\texttt{DERIVED}
}
$$

and:

$$
\boxed{
\operatorname{ClaimClass}(N)=\texttt{DERIVED}
}
$$

with scope:

$$
\boxed{
\operatorname{Scope}(N)=\texttt{AMOS\_general}
}
$$

and declared provenance:

$$
\boxed{
\pi(N)=\texttt{.github/copilot-instructions.md}
}
$$

This means the vault note should not independently elevate itself to `SOURCE_CLAIM` or `VERIFIED`.

The authoritative contract and this derived navigation artifact remain separate epistemic objects.

______________________________________________________________________

## 5. Contract Resolution

Let:

$$
R(N)
$$

denote resolution from the vault entry point to the authoritative contract.

A successful resolution requires an identifiable source:

$$
\boxed{
\operatorname{Resolved}(N,C)
\Rightarrow
\operatorname{Exists}(C)
\land
\operatorname{IdentityBound}(C)
}
$$

If the source cannot be resolved:

$$
\boxed{
\neg\operatorname{Resolved}(N,C)
\Rightarrow
\operatorname{State}(\operatorname{ContractResolution})
=
\texttt{UNKNOWN/GAP}
}
$$

The missing source must not be replaced by reconstructed or remembered contract text.

______________________________________________________________________

## 6. Contract ≠ Capability

A coding agent may technically possess capability (K) without the contract authorizing its use.

Therefore:

$$
\boxed{
\operatorname{Capable}(A,K)
\not\Rightarrow
\operatorname{Authorized}(A,K)
}
$$

Similarly, discovering the contract does not prove compliance:

$$
\boxed{
\operatorname{Read}(A,C)
\not\Rightarrow
\operatorname{Compliant}(A,C)
}
$$

and implementation does not prove validation:

$$
\boxed{
\operatorname{Implemented}(r)
\not\Rightarrow
\operatorname{Validated}(r)
}
$$

where (r) is a contract requirement.

______________________________________________________________________

## 7. Contract Requirement Model

The supplied note does **not** contain the individual requirements of `copilot-instructions.md`.

Therefore the following is a **DERIVED representation**, not reconstructed contract canon.

For a contract requirement (r_i):

$$
\boxed{
r_i=
(
id_i,
statement_i,
scope_i,
authority_i,
preconditions_i,
obligations_i,
prohibitions_i,
validation_i
)
}
$$

with contract:

$$
\boxed{
C=\{r_1,r_2,\ldots,r_n\}
}
$$

The actual value of (n), requirement identifiers, rules, precedence relations, and validation conditions remain:

$$
\boxed{
\texttt{UNKNOWN/GAP}
}
$$

until the authoritative source is loaded.

______________________________________________________________________

## 8. Applicability

A requirement must not silently escape its declared applicability envelope.

For agent (A), operation (O), environment (E), and requirement (r):

$$
\boxed{
\operatorname{Applies}(r,A,O,E)
}
$$

must be established before treating (r) as governing that operation.

Conversely:

$$
\boxed{
\neg\operatorname{EstablishedApplicability}(r,A,O,E)
\not\Rightarrow
\neg\operatorname{Applies}(r,A,O,E)
}
$$

Lack of resolution is uncertainty, not automatic exemption.

______________________________________________________________________

## 9. Compliance Model

A minimal derived representation of compliance is:

$$
\boxed{
\operatorname{Compliant}(A,C,O)
\Rightarrow
\bigwedge_{r_i\in R_O}
\operatorname{Satisfied}(A,r_i,O)
}
$$

where:

$$
R_O=
\{
r_i\in C:
\operatorname{Applies}(r_i,A,O,E)
\}
$$

This is a **necessary-condition formalization**.

It does not assert that checking a finite list of reconstructed requirements is sufficient for contract compliance.

If any load-bearing applicable requirement fails:

$$
\boxed{
\exists r_i\in R_O:
\neg\operatorname{Satisfied}(A,r_i,O)
\Rightarrow
\neg\operatorname{ClaimCompliant}(A,C,O)
}
$$

______________________________________________________________________

## 10. Unknown Contract State

Because the actual authoritative contract text is not included in the supplied note, unspecified contract semantics remain unknown.

Thus:

$$
\boxed{
\operatorname{MissingContractRequirement}
\Rightarrow
\operatorname{State}
=
\texttt{UNKNOWN/GAP}
}
$$

not:

$$
\operatorname{MissingContractRequirement}
\Rightarrow
\mathrm{PERMITTED}
$$

and not:

$$
\operatorname{MissingContractRequirement}
\Rightarrow
\mathrm{PROHIBITED}
$$

unless another governing authority establishes the result.

This preserves fail-closed reasoning without inventing contract content.

______________________________________________________________________

## 11. Version and Freshness

A global contract can change over time.

Conceptually:

$$
C_t
$$

denotes the contract state applicable at time/version (t).

A prior contract state does not automatically govern a later execution:

$$
\boxed{
C_{t_1}
\not\Rightarrow
C_{t_2}=C_{t_1}
}
$$

for:

$$
t_2>t_1
$$

without version/freshness validation.

The supplied note contains no explicit contract version, hash, commit identifier, or freshness bound.

Therefore:

$$
\boxed{
\operatorname{ContractVersion}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{ContractHash}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{FreshnessBound}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## 12. Provenance

The source-declared provenance is:

```text
.github/copilot-instructions.md
```

Conceptually:

$$
\boxed{
C
\xrightarrow{\mathrm{DERIVES}}
N
}
$$

The provenance edge should remain recoverable.

If the contract changes from:

$$
C_v\rightarrow C_{v+1}
$$

then derived artifacts depending on the changed requirements may require revalidation:

$$
\boxed{
\Delta C\neq\varnothing
\Rightarrow
\operatorname{Revalidate}
\left(
\operatorname{Dependents}(\Delta C)
\right)
}
$$

Only affected dependents need invalidation; unrelated artifacts need not automatically be discarded.

______________________________________________________________________

## 13. Contract Precedence

The supplied note establishes the contract as authoritative for its declared role, but it does not provide a complete precedence relation among:

- AMOS canon;
- the global coding-agent contract;
- repository-local instructions;
- tool-specific requirements;
- task-specific instructions;
- runtime authority;
- external platform constraints.

Therefore:

$$
\boxed{
\operatorname{CompleteAuthorityOrder}
=
\texttt{UNKNOWN/GAP}
}
$$

No complete precedence lattice should be invented from this note.

______________________________________________________________________

## 14. Agent Contract Binding

The source provides:

[[AGENTS|AMOS Agent Contract]]

This establishes an explicit relationship between the global coding-agent contract entry point and the `AGENTS` artifact.

The exact semantic relationship is not specified.

Therefore:

$$
\boxed{
N
\xleftrightarrow{\mathrm{SEE\ ALSO}}
\texttt{AGENTS}
}
$$

is supported.

But the stronger claims:

$$
N=\texttt{AGENTS}
$$

or:

$$
N\supset\texttt{AGENTS}
$$

or:

$$
N\subset\texttt{AGENTS}
$$

remain:

$$
\boxed{
\texttt{UNKNOWN/GAP}
}
$$

until their contents and authority relationship are compared.

______________________________________________________________________

## 15. AMOS Root Integration

The source also binds the note to:

[[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]

Therefore:

$$
\boxed{
N
\xrightarrow{\mathrm{INDEXED\_BY}}
\texttt{00\_COSMO\_BRAIN\_MOC}
}
$$

at the vault-navigation level.

This navigation relationship does not itself establish contract authority.

______________________________________________________________________

## 16. Derived Contract Processing Flow

The following is a **DERIVED AMOS integration model**:

$$
\boxed{
\mathrm{Resolve}
\rightarrow
\mathrm{Identify}
\rightarrow
\mathrm{Load}
\rightarrow
\mathrm{Bind\ Scope}
\rightarrow
\mathrm{Determine\ Applicability}
\rightarrow
\mathrm{Check\ Authority}
\rightarrow
\mathrm{Execute}
\rightarrow
\mathrm{Validate}
\rightarrow
\mathrm{Receipt}
}
$$

### 16.1 Resolve

Resolve the authoritative source.

$$
N\rightarrow C
$$

If unresolved:

$$
\operatorname{State}(\operatorname{Resolution})
=
\texttt{UNKNOWN/GAP}
$$

### 16.2 Identify

Bind the exact contract identity/version when available.

### 16.3 Load

Load only the requirements materially relevant to the intended operation when dependency closure is known.

### 16.4 Bind Scope

Determine which requirements apply to:

$$
(A,O,E)
$$

### 16.5 Determine Applicability

Identify:

$$
R_O\subseteq C
$$

### 16.6 Check Authority

Capability alone cannot substitute for required authority.

### 16.7 Execute

Perform only actions compatible with applicable requirements and higher governing constraints.

### 16.8 Validate

Validate the resulting state against load-bearing requirements.

### 16.9 Receipt

Preserve sufficient provenance to establish:

$$
\boxed{
\mathrm{operation}
\rightarrow
\mathrm{contract\ state}
\rightarrow
\mathrm{applicable\ requirements}
\rightarrow
\mathrm{validation}
}
$$

where the implementation supports such receipts.

______________________________________________________________________

## 17. Contract Integrity Invariants

## I1 — Authority Source Preservation

$$
\boxed{
\operatorname{AuthoritativeContractContent}
\Rightarrow
\operatorname{TraceableTo}(C)
}
$$

## I2 — No Fabricated Requirements

$$
\boxed{
\neg\operatorname{SourceSupported}(r)
\Rightarrow
\neg\operatorname{LabelAsCanonicalContractRequirement}(r)
}
$$

## I3 — Capability ≠ Authorization

$$
\boxed{
\mathrm{CAPABILITY}
\neq
\mathrm{AUTHORITY}
}
$$

## I4 — Proposal ≠ Commit

Where contract-governed operations use proposal/commit semantics:

$$
\boxed{
\mathrm{PROPOSAL}
\neq
\mathrm{COMMIT}
}
$$

## I5 — Unknown ≠ Permission

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\mathrm{AUTHORIZED}
}
$$

## I6 — Unknown ≠ Compliance

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\mathrm{COMPLIANT}
}
$$

## I7 — Derived ≠ Canonical Source

$$
\boxed{
\mathrm{DERIVED}
\neq
\mathrm{AUTHORITATIVE\ SOURCE}
}
$$

## I8 — Provenance Preservation

$$
\boxed{
\operatorname{DerivedFrom}(N,C)
\Rightarrow
\operatorname{PreserveProvenance}(N,C)
}
$$

______________________________________________________________________

## 18. Gaps

## G1 — Authoritative Path Resolution

Source body:

```text
copilot-instructions.md
```

Frontmatter:

```text
.github/copilot-instructions.md
```

Therefore:

$$
\boxed{
\operatorname{CanonicalPath}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G2 — Contract Contents

The authoritative contract text was not supplied here.

$$
\boxed{
\operatorname{FullContractSemantics}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G3 — Version

$$
\boxed{
\operatorname{Version}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G4 — Content Hash

$$
\boxed{
\operatorname{Hash}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G5 — Freshness

$$
\boxed{
\operatorname{Freshness}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G6 — Executed Compliance Validation

$$
\boxed{
\operatorname{ExecutedComplianceValidation}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G7 — Complete Authority Hierarchy

$$
\boxed{
\operatorname{CompleteAuthorityOrder}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G8 — AGENTS Relationship

$$
\boxed{
\operatorname{SemanticRelation}(N,\texttt{AGENTS})
=
\texttt{UNKNOWN/GAP}
}
$$

beyond the source-declared `See also` relation.

______________________________________________________________________

## 19. Derived Validation Conditions

These are **DERIVED validation conditions**, not source-declared contract clauses.

### DVC1 — Wrong Authoritative Source

If the resolved file is not the canonical contract source, the binding is invalid.

### DVC2 — Silent Path Reconciliation

The two source-declared path expressions must not be silently treated as identical without repository evidence.

### DVC3 — Fabricated Contract Requirement

Any requirement represented as canonical without traceability to the authoritative contract violates the integration boundary.

### DVC4 — Stale Contract

A materially superseded contract state must not silently govern a later operation where freshness matters.

### DVC5 — Capability Escalation

$$
\operatorname{Capable}(A,O)
\not\Rightarrow
\operatorname{Authorized}(A,O)
$$

### DVC6 — Derived-to-Canonical Promotion

Derived interpretation must not silently become authoritative contract text.

### DVC7 — UNKNOWN-to-PASS

$$
\boxed{
\texttt{UNKNOWN/GAP}
\not\Rightarrow
\mathrm{PASS}
}
$$

______________________________________________________________________

## 20. RSCF

```yaml
RSCF:
  node_id: amos_00_root_amos_global_contract_for_ai_coding_agents_md
  node_type: note

  artifact:
    title: "AMOS Global Contract for AI Coding Agents"
    type: note
    source: 00_ROOT
    plane: 00_ROOT
    path: "00_ROOT/AMOS Global Contract for AI Coding Agents.md"

  state: DERIVED
  claim_class: DERIVED

  provenance:
    declared: ".github/copilot-instructions.md"
    body_authoritative_source: "copilot-instructions.md"
    path_resolution: UNKNOWN/GAP

  scope:
    - AMOS_general
    - ai_coding_agents
    - coding_agent_contract
    - agent_governance

  H:
    role: >
      Canonical vault entry point for the global AMOS
      coding-agent contract.

    authoritative_content:
      external_to_note: true
      source: copilot-instructions.md
      exact_path: UNKNOWN/GAP

    invariants:
      - authoritative_contract_content_must_be_source_traceable
      - derived_interpretation_is_not_contract_canon
      - capability_is_not_authority
      - unknown_is_not_permission
      - unknown_is_not_compliance
      - contract_resolution_failure_remains_unknown_gap
      - provenance_must_remain_recoverable

  M:
    distinctions:
      - entry_point_vs_authoritative_source
      - specification_vs_implementation
      - capability_vs_authority
      - reading_vs_compliance
      - derived_interpretation_vs_canonical_requirement
      - historical_contract_vs_current_contract

    contract_model:
      class: DERIVED_FORMALIZATION
      requirement_fields:
        - id
        - statement
        - scope
        - authority
        - preconditions
        - obligations
        - prohibitions
        - validation

    processing:
      - resolve
      - identify
      - load
      - bind_scope
      - determine_applicability
      - check_authority
      - execute
      - validate
      - receipt

  L:
    authoritative_source:
      body_reference: copilot-instructions.md
      frontmatter_provenance: .github/copilot-instructions.md
      resolved_identity: UNKNOWN/GAP
      version: UNKNOWN/GAP
      hash: UNKNOWN/GAP
      freshness: UNKNOWN/GAP

    related:
      - "[[AGENTS|AMOS Agent Contract]]"
      - "[[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]"

  gaps:
    canonical_path: UNKNOWN/GAP
    full_contract_semantics: UNKNOWN/GAP
    contract_version: UNKNOWN/GAP
    contract_hash: UNKNOWN/GAP
    freshness: UNKNOWN/GAP
    executed_compliance_validation: UNKNOWN/GAP
    complete_authority_order: UNKNOWN/GAP
    agents_semantic_relationship: UNKNOWN/GAP

  derived_validation_conditions:
    - wrong_authoritative_source
    - silent_path_reconciliation
    - fabricated_contract_requirement
    - stale_contract
    - capability_escalation
    - derived_to_canonical_promotion
    - unknown_to_pass

  epistemic:
    state: DERIVED
    claim_class: DERIVED
    implementation: UNKNOWN/GAP
    validation: UNKNOWN/GAP
```

______________________________________________________________________

## 21. RSCF-NODE

```yaml
RSCF-NODE:
  node_id: amos_00_root_amos_global_contract_for_ai_coding_agents_md
  node_type: note
  path: "00_ROOT/AMOS Global Contract for AI Coding Agents.md"
  state: DERIVED
  claim_class: DERIVED
  provenance: ".github/copilot-instructions.md"
  scope: AMOS_general
```

______________________________________________________________________

## 22. RSCF-RELATIONS

```yaml
RSCF-RELATIONS:
  - DERIVED_FROM: ".github/copilot-instructions.md"
  - AUTHORITATIVE_SOURCE: "copilot-instructions.md"
  - RELATED_TO: [[AGENTS|AMOS Agent Contract]]
  - INDEXED_BY: [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
```

> **Integrity note:** `DERIVED_FROM` and `AUTHORITATIVE_SOURCE` preserve the two path forms exactly as supplied. Their filesystem identity is not asserted.

______________________________________________________________________

## 23. Related

### Source-declared

- [[AGENTS|AMOS Agent Contract]]
- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]

### Derived AMOS navigation

- [[00_ROOT/Agent Skills|Agent Skills]]
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

The second group is navigation augmentation, not source-declared contract content.

______________________________________________________________________

## 24. Machine Representation

```yaml
amos_global_contract:
  artifact:
    title: "AMOS Global Contract for AI Coding Agents"
    type: note
    source: 00_ROOT

  epistemic:
    state: DERIVED
    claim_class: DERIVED
    scope: AMOS_general

  authority_binding:
    role: canonical_vault_entry_point

    source_declarations:
      frontmatter_provenance: ".github/copilot-instructions.md"
      body_authoritative_source: "copilot-instructions.md"

    canonical_path: UNKNOWN/GAP

  contract:
    contents_loaded: false
    version: UNKNOWN/GAP
    hash: UNKNOWN/GAP
    freshness: UNKNOWN/GAP
    executed_validation: UNKNOWN/GAP

  invariants:
    entry_point_equals_authoritative_source: false
    capability_implies_authority: false
    read_implies_compliance: false
    implementation_implies_validation: false
    unknown_implies_permission: false
    unknown_implies_compliance: false

  relations:
    source_declared:
      - target: AGENTS
        relation: SEE_ALSO

      - target: 00_COSMO_BRAIN_MOC
        relation: SEE_ALSO

  gaps:
    - canonical_path
    - full_contract_semantics
    - contract_version
    - contract_hash
    - freshness
    - executed_compliance_validation
    - complete_authority_order
    - agents_semantic_relationship
```

______________________________________________________________________

## 25. Canonical Compression

The source establishes:

$$
\boxed{
\mathrm{AMOS\ Global\ Contract\ Vault\ Entry}
\xrightarrow{\mathrm{resolves\ to}}
\mathrm{Authoritative\ Coding\ Agent\ Contract}
}
$$

with the note itself classified:

$$
\boxed{
\mathrm{DERIVED}
}
$$

and scoped to:

$$
\boxed{
\texttt{AMOS\_general}
}
$$

The critical distinctions are:

$$
\boxed{
\mathrm{ENTRY\ POINT}
\neq
\mathrm{AUTHORITATIVE\ SOURCE}
}
$$

$$
\boxed{
\mathrm{CONTRACT}
\neq
\mathrm{IMPLEMENTATION}
}
$$

$$
\boxed{
\mathrm{CAPABILITY}
\neq
\mathrm{AUTHORITY}
}
$$

$$
\boxed{
\mathrm{READ}
\neq
\mathrm{COMPLIANCE}
}
$$

$$
\boxed{
\mathrm{DERIVED}
\neq
\mathrm{CANONICAL\ CONTRACT\ REQUIREMENT}
}
$$

and:

$$
\boxed{
\texttt{UNKNOWN/GAP}
\neq
\mathrm{PASS}
}
$$

______________________________________________________________________

## 26. Integrity Boundary

This artifact does **not** contain the authoritative contract itself.

It establishes only what the supplied note supports:

1. `AMOS Global Contract for AI Coding Agents` is the canonical vault entry point.
1. The authoritative source is identified in the body as `copilot-instructions.md`.
1. Frontmatter declares provenance as `.github/copilot-instructions.md`.
1. The artifact is `DERIVED`.
1. Its claim class is `DERIVED`.
1. Its scope is `AMOS_general`.
1. It explicitly references `AGENTS` and `00_COSMO_BRAIN_MOC`.

Because the two source path expressions differ, their identity remains unresolved:

$$
\boxed{
\texttt{copilot-instructions.md}
\overset{?}{=}
\texttt{.github/copilot-instructions.md}
}
$$

No missing contract rules have been reconstructed.

The requirement model, compliance equations, processing flow, invariants, validation conditions, RSCF decomposition, and machine representation above are **DERIVED formalizations** of how this entry-point relationship can be represented within AMOS. They are not claims about the unprovided contents of `copilot-instructions.md`.

Until the authoritative source is resolved and loaded:

$$
\boxed{
\operatorname{FullContractSemantics}
=
\texttt{UNKNOWN/GAP}
}
$$

and:

$$
\boxed{
\operatorname{ExecutedComplianceValidation}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
