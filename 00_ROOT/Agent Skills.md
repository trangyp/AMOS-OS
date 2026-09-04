---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Agent Skills
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Agent Skills

## 0. Status

**AMOS knowledge-integration artifact.**

**DERIVED · source-backed index · implementation UNKNOWN/GAP.**

`Agent Skills` indexes SOTA agent-skill specifications, registries, workflow references, and canonical integration material captured for AMOS.

The supplied note establishes the existence of the listed AMOS knowledge references. It does **not**, by itself, establish that every referenced specification:

- uses the same definition of a skill;
- implements the same execution model;
- is mutually compatible;
- is currently authoritative;
- is implemented inside AMOS;
- has been independently validated;
- represents one universal agent-skill standard.

Therefore:

\[
\\boxed{
\\operatorname{IndexedSourcesExist}
\\not\\Rightarrow
\\operatorname{StandardsEquivalent}
}
\]

and:

\[
\\boxed{
\\operatorname{CapturedSpecification}
\\not\\Rightarrow
\\operatorname{ImplementedCapability}
}
\]

______________________________________________________________________

## 1. Purpose

`Agent Skills` provides an AMOS-level knowledge entry point for captured agent-skill specifications and related integration material.

Its source-declared role is:

> SOTA agent-skill specifications, registries, and canonical integrations captured for AMOS.

Define the indexed source set:

## \[ \\boxed{ \\mathcal S\_{\\mathrm{skill}}

{S_1,S_2,\\ldots,S_6}
}
\]

where the supplied note identifies six raw captures/specifications.

The artifact functions conceptually as:

\[
\\boxed{
\\mathcal I\_{\\mathrm{AgentSkills}}
:
\\mathcal S\_{\\mathrm{skill}}
\\rightarrow
\\mathrm{AMOS\\ Knowledge\\ References}
}
\]

This is an indexing/integration representation, not a claim that the referenced specifications have already been normalized into one executable standard.

______________________________________________________________________

## 2. Raw Captures and Specifications

## 2.1 Addy Osmani Agent Skills

[[11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30|ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]

Classification from the supplied note:

```yaml
source_role: raw_capture
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 2.2 AgentSkills Specification

[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_SPECIFICATION_2026_08_29|AGENTSKILLS_SPECIFICATION_2026_08_29]]

```yaml
source_role: specification_reference
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 2.3 AgentSkills.io Specification

[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_IO_SPECIFICATION_2026_08_30|AGENTSKILLS_IO_SPECIFICATION_2026_08_30]]

```yaml
source_role: specification_reference
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 2.4 Agent Skills for Context Engineering

[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30|AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]]

```yaml
source_role: raw_capture
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 2.5 Agent Skills Standard

[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|AGENT_SKILLS_STANDARD_README_2026_08_30]]

```yaml
source_role: standard_reference
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 2.6 Anthropic Skills Agent Skills Specification

[[11_KNOWLEDGE/LLM_WIKI/raw/ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30|ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30]]

```yaml
source_role: specification_reference
epistemic_state: SOURCE_REFERENCE
integration_state: UNKNOWN/GAP
```

______________________________________________________________________

## 3. Supporting References

## SOTA Agent-Skill / Workflow Repositories

[[11_KNOWLEDGE/LLM_WIKI/wiki/SOTA_AGENT_SKILL_WORKFLOW_REPOS|SOTA_AGENT_SKILL_WORKFLOW_REPOS]]

This is the supplied cross-reference for the broader repository/workflow landscape.

______________________________________________________________________

## AMOS Agent Governance

[[00_ROOT/AMOS Global Contract for AI Coding Agents|AMOS Global Contract for AI Coding Agents]]

This is the supplied AMOS canonical-integration reference.

The existence of this relationship should not be strengthened into:

$$
\mathrm{ExternalSkillSpec}
=
\mathrm{AMOSContract}
$$

Instead:

$$
\boxed{
\mathrm{ExternalSkillKnowledge}
\xrightarrow{\mathrm{integration/reference}}
\mathrm{AMOS\ Agent\ Governance}
}
$$

subject to explicit AMOS validation and governance boundaries.

______________________________________________________________________

## 4. Epistemic Separation

The artifact itself is declared:

$$
\boxed{
\operatorname{State}
=
\mathrm{DERIVED}
}
$$

and:

$$
\boxed{
\operatorname{ClaimClass}
=
\mathrm{DERIVED}
}
$$

with provenance:

$$
\boxed{
\pi
=
\texttt{11\_KNOWLEDGE/LLM\_WIKI/raw/}
}
$$

and scope:

$$
\boxed{
\sigma
=
\texttt{AMOS\_general}
}
$$

The raw captures remain evidence/source material beneath the derived integration artifact.

Conceptually:

$$
\boxed{
\mathrm{RAW\ SOURCE}
\rightarrow
\mathrm{CAPTURE}
\rightarrow
\mathrm{DERIVED\ INDEX}
}
$$

This lineage does not automatically establish independent validation.

______________________________________________________________________

## 5. Source Independence

Multiple captured documents do not necessarily constitute multiple independent confirmations.

Let:

$$
a(S_i)
$$

represent the ancestry/provenance of source (S_i).

Then:

$$
\boxed{
a(S_i)\cap a(S_j)\neq\varnothing
\Rightarrow
S_i,S_j
\text{ cannot automatically be counted as independent}
}
$$

Therefore:

$$
\boxed{
|\mathcal S_{\mathrm{skill}}|=6
\not\Rightarrow
6\ \mathrm{independent\ confirmations}
}
$$

The source ancestry between the listed captures is not established by the supplied index.

Thus:

$$
\boxed{
\operatorname{ProvenanceIndependence}
=
\texttt{UNKNOWN/GAP}
}
$$

until the raw captures are compared.

______________________________________________________________________

## 6. Skill as a Typed Capability

The supplied artifact does not provide a canonical field-level definition of an agent skill.

Therefore, the following is a **DERIVED AMOS integration model**, not a claim about every referenced external specification.

Represent a skill as:

$$
\boxed{
K=
(
id,
version,
purpose,
inputs,
outputs,
preconditions,
procedure,
dependencies,
authority,
scope,
provenance,
validation
)
}
$$

where:

- (id) = stable skill identity;
- (version) = explicit version;
- (purpose) = intended capability;
- (inputs) = accepted input contract;
- (outputs) = output contract;
- (preconditions) = required conditions;
- (procedure) = governed execution specification;
- (dependencies) = required tools/data/skills;
- (authority) = permissions required for consequential actions;
- (scope) = applicability envelope;
- (provenance) = source and transformation lineage;
- (validation) = evidence supporting correct operation.

The exact canonical skill schema remains:

$$
\boxed{
\operatorname{CanonicalSkillSchema}
=
\texttt{UNKNOWN/GAP}
}
$$

until resolved from the referenced specifications and AMOS governance.

______________________________________________________________________

## 7. Skill Specification ≠ Skill Implementation

A specification describes capability semantics.

An implementation realizes some version of those semantics.

Therefore:

$$
\boxed{
\operatorname{Specified}(K)
\not\Rightarrow
\operatorname{Implemented}(K)
}
$$

Likewise:

$$
\boxed{
\operatorname{Implemented}(K)
\not\Rightarrow
\operatorname{Validated}(K)
}
$$

and:

$$
\boxed{
\operatorname{Validated}(K)
\not\Rightarrow
\operatorname{Authorized}(K,O)
}
$$

for consequential operation (O).

The distinctions must remain typed:

$$
\boxed{
\mathrm{SPECIFIED}
\neq
\mathrm{IMPLEMENTED}
\neq
\mathrm{VALIDATED}
\neq
\mathrm{AUTHORIZED}
}
$$

______________________________________________________________________

## 8. Skill Discovery ≠ Skill Execution

A system may discover that skill (K) exists without satisfying its execution conditions.

Thus:

$$
\boxed{
\operatorname{Discover}(K)
\not\Rightarrow
\operatorname{Execute}(K)
}
$$

Likewise:

$$
\boxed{
\operatorname{Applicable}(K,O)
\not\Rightarrow
\operatorname{Authorized}(K,O)
}
$$

A derived AMOS execution boundary can therefore be represented:

$$
\boxed{
\operatorname{Execute}(K,O)
\Rightarrow
\operatorname{Resolved}(K)
\land
\operatorname{Applicable}(K,O)
\land
\operatorname{RequiredDependenciesAvailable}(K)
\land
\operatorname{RequiredAuthorityValid}(K,O)
}
$$

No reverse implication is asserted.

______________________________________________________________________

## 9. Skill Registry Model

Because the source explicitly identifies **registries** as part of the captured domain, a derived registry representation is:

$$
\boxed{
\mathcal R_K
=
\{K_1,K_2,\ldots,K_n\}
}
$$

with lookup:

$$
\boxed{
\operatorname{Lookup}_{\mathcal R_K}(id,version)
\rightarrow
K
\cup
\{\texttt{UNKNOWN/GAP}\}
}
$$

If no matching skill can be resolved:

$$
\boxed{
\neg\operatorname{Resolve}(id,version)
\Rightarrow
\operatorname{State}(K)=\texttt{UNKNOWN/GAP}
}
$$

A registry entry alone does not establish operational readiness:

$$
\boxed{
\operatorname{Registered}(K)
\not\Rightarrow
\operatorname{Executable}(K)
}
$$

______________________________________________________________________

## 10. Skill Selection

Given task (T) and available skill set:

$$
\mathcal K=\{K_1,\ldots,K_n\}
$$

define candidate skills:

$$
\boxed{
\mathcal K_T
=
\{
K_i\in\mathcal K:
\operatorname{Applicable}(K_i,T)
\}
}
$$

A selected skill:

$$
K^{*}\in\mathcal K_T
$$

must not be inferred merely from semantic similarity.

Thus:

$$
\boxed{
\operatorname{SimilarDescription}(K,T)
\not\Rightarrow
\operatorname{Applicable}(K,T)
}
$$

Applicability must respect the actual capability contract.

______________________________________________________________________

## 11. Dependency Closure

Let:

$$
D(K)
$$

represent the direct dependencies of skill (K).

Its dependency closure is:

$$
\boxed{
D^{*}(K)
=
D(K)
\cup
\bigcup_{d\in D(K)}D^{*}(d)
}
$$

where recursive traversal is finite and well-defined for the applicable dependency graph.

Execution should not assume dependency availability:

$$
\boxed{
\operatorname{Execute}(K)
\Rightarrow
\bigwedge_{d\in D_{\mathrm{required}}^{*}(K)}
\operatorname{Available}(d)
}
$$

for load-bearing required dependencies.

Optional dependencies are not included in that necessary condition unless they become load-bearing for the selected execution path.

______________________________________________________________________

## 12. Scope and Applicability

A skill's validity should be interpreted within an applicability envelope.

Derived AMOS representation:

$$
\boxed{
\mathcal E_K
=
(
task,
environment,
input\_type,
output\_type,
authority,
dependencies,
time,
regime
)
}
$$

Then:

$$
\boxed{
\operatorname{Validated}(K,\mathcal E_1)
\not\Rightarrow
\operatorname{Validated}(K,\mathcal E_2)
}
$$

when load-bearing dimensions differ without a validated bridge.

This prevents silent cross-environment or cross-regime transfer.

______________________________________________________________________

## 13. Provenance

For each captured specification (S_i), define provenance:

$$
\pi(S_i)
$$

For a derived AMOS skill model (K) constructed from sources:

$$
S_{i_1},S_{i_2},\ldots,S_{i_m}
$$

its provenance should preserve those dependencies:

$$
\boxed{
\pi(K)
\supseteq
\{
S_{i_1},
S_{i_2},
\ldots,
S_{i_m}
\}
}
$$

A derived synthesis must not erase disagreement between those sources.

Therefore:

$$
\boxed{
\operatorname{Conflict}(S_i,S_j)
\Rightarrow
\neg\operatorname{SilentMerge}(S_i,S_j)
}
$$

______________________________________________________________________

## 14. Competing Specifications

If two captured specifications make incompatible claims:

$$
C_i\neq C_j
$$

and neither has sufficient governing authority or discriminating evidence to dominate the other, then:

$$
\boxed{
C_i\parallel C_j
\Rightarrow
\operatorname{State}
=
\mathrm{COMPETING}
}
$$

rather than forcing:

$$
C_i=C_j
$$

The supplied index does not establish whether such conflicts exist.

Therefore:

$$
\boxed{
\operatorname{CrossSpecificationCompatibility}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## 15. Freshness

The captures contain dated identifiers:

- `2026_08_29`
- `2026_08_30`

Those dates identify the captured artifacts as named in the source.

They do not automatically prove:

$$
\operatorname{CurrentLatestSpecification}
$$

at every future time.

Therefore:

$$
\boxed{
\operatorname{CapturedAt}(t_c)
\not\Rightarrow
\operatorname{LatestAt}(t)
}
$$

for:

$$
t>t_c
$$

without a freshness check.

______________________________________________________________________

## 16. Validation

The supplied artifact provides references but does not provide executed validation evidence for a unified AMOS Agent Skills implementation.

Therefore:

$$
\boxed{
\operatorname{UnifiedAMOSSkillValidation}
=
\texttt{UNKNOWN/GAP}
}
$$

Required validation depends on the actual integration target.

At minimum, a consequential implementation would need to distinguish:

$$
\boxed{
\mathrm{SOURCE\ COMPATIBILITY}
}
$$

$$
\boxed{
\mathrm{SCHEMA\ VALIDITY}
}
$$

$$
\boxed{
\mathrm{DEPENDENCY\ VALIDITY}
}
$$

$$
\boxed{
\mathrm{EXECUTION\ VALIDITY}
}
$$

$$
\boxed{
\mathrm{AUTHORITY\ VALIDITY}
}
$$

$$
\boxed{
\mathrm{OUTPUT\ CONTRACT\ VALIDITY}
}
$$

______________________________________________________________________

## 17. Gaps

## G1 — Canonical Skill Schema

$$
\boxed{
\operatorname{CanonicalSkillSchema}
=
\texttt{UNKNOWN/GAP}
}
$$

The supplied index does not contain the actual field-level schemas of the referenced specifications.

______________________________________________________________________

## G2 — Cross-Specification Compatibility

$$
\boxed{
\operatorname{CrossSpecificationCompatibility}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G3 — Provenance Independence

$$
\boxed{
\operatorname{ProvenanceIndependence}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G4 — AMOS Runtime Binding

$$
\boxed{
\operatorname{AMOSRuntimeBinding}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G5 — Executed Validation

$$
\boxed{
\operatorname{ExecutedValidation}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## G6 — Canonical Authority Ordering

The supplied artifact does not specify which external source controls if specifications disagree.

$$
\boxed{
\operatorname{ExternalSpecAuthorityOrdering}
=
\texttt{UNKNOWN/GAP}
}
$$

______________________________________________________________________

## 18. Derived Validation Conditions

These conditions are **DERIVED** from the integration structure. They are not source-declared falsifiers.

## DVC1 — Specification Conflation

Invalid integration condition:

$$
\boxed{
S_i\neq S_j
\land
\operatorname{UnverifiedEquivalence}(S_i,S_j)
}
$$

Do not silently treat distinct specifications as identical.

______________________________________________________________________

## DVC2 — Registry Equals Implementation

Unsupported inference:

$$
\boxed{
\operatorname{Registered}(K)
\Rightarrow
\operatorname{Implemented}(K)
}
$$

______________________________________________________________________

## DVC3 — Implementation Equals Validation

Unsupported inference:

$$
\boxed{
\operatorname{Implemented}(K)
\Rightarrow
\operatorname{Validated}(K)
}
$$

______________________________________________________________________

## DVC4 — Capability Equals Authority

Unsupported inference:

$$
\boxed{
\operatorname{CanExecute}(K,O)
\Rightarrow
\operatorname{Authorized}(K,O)
}
$$

______________________________________________________________________

## DVC5 — Correlated Sources Counted as Independent

If:

$$
a(S_i)\cap a(S_j)\neq\varnothing
$$

then they must not automatically be counted as independent confirmation.

______________________________________________________________________

## DVC6 — Stale Capture Treated as Current Canon

Unsupported inference:

$$
\boxed{
\operatorname{Captured}(S,t_c)
\Rightarrow
\operatorname{CurrentCanonical}(S,t)
}
$$

for arbitrary (t>t_c).

______________________________________________________________________

## 19. Derived AMOS Skill Integration Flow

A minimal governed integration path is:

$$
\boxed{
\mathrm{Capture}
\rightarrow
\mathrm{Identify}
\rightarrow
\mathrm{Classify}
\rightarrow
\mathrm{Compare}
\rightarrow
\mathrm{Normalize}
\rightarrow
\mathrm{Validate}
\rightarrow
\mathrm{Govern}
\rightarrow
\mathrm{Register}
}
$$

where each transition is conditional on the relevant evidence.

More explicitly:

### 1. Capture

Preserve raw specification:

$$
S_i
$$

without rewriting its source semantics.

### 2. Identify

Bind:

$$
(id,source,date,version)
$$

where available.

### 3. Classify

Distinguish:

$$
\mathrm{SOURCE}
$$

from:

$$
\mathrm{DERIVED}
$$

and:

$$
\mathrm{MODEL}
$$

### 4. Compare

Determine whether sources:

$$
S_i,S_j
$$

are:

$$
\mathrm{COMPATIBLE},
\quad
\mathrm{PARTIALLY\ COMPATIBLE},
\quad
\mathrm{COMPETING},
\quad
\text{or}
\quad
\texttt{UNKNOWN/GAP}
$$

### 5. Normalize

Create an AMOS representation only for semantics that can be mapped without destroying load-bearing distinctions.

### 6. Validate

Test the normalized representation against the relevant source specification and implementation.

### 7. Govern

Apply AMOS authority, scope, provenance, and consequence boundaries.

### 8. Register

Only then register the governed skill state at the appropriate epistemic and implementation status.

______________________________________________________________________

## 20. Integration Invariant

The central integration invariant is:

$$
\boxed{
\operatorname{AMOSIntegration}(S)
\Rightarrow
\operatorname{PreserveLoadBearingSemantics}(S)
}
$$

If normalization loses a load-bearing distinction:

$$
\boxed{
\operatorname{SemanticLoss}(S\rightarrow K)>0
}
$$

for a decision-relevant distinction, then the mapping requires repair or explicit limitation.

A conceptual loss function is:

$$
\boxed{
L_{\mathrm{semantic}}
=
\sum_{d\in D_L}
w_d
\mathbf 1
[
d\text{ is not preserved}
]
}
$$

where:

- (D_L) = load-bearing distinctions;
- (w_d) = importance of distinction (d);
- (\\mathbf 1[\\cdot]) = indicator function.

This is a **DERIVED formal model**, not a metric declared by the supplied external sources.

______________________________________________________________________

## 21. RSCF

```yaml
RSCF:
  node_id: amos_00_root_agent_skills_md

  node_type: note

  artifact:
    title: "Agent Skills"
    type: note
    source: 00_ROOT
    plane: 00_ROOT

  state: DERIVED
  claim_class: DERIVED

  provenance:
    root: "11_KNOWLEDGE/LLM_WIKI/raw/"

    source_artifacts:
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30|ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_SPECIFICATION_2026_08_29|AGENTSKILLS_SPECIFICATION_2026_08_29]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_IO_SPECIFICATION_2026_08_30|AGENTSKILLS_IO_SPECIFICATION_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30|AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|AGENT_SKILLS_STANDARD_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30|ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30]]"

  scope:
    - AMOS_general
    - agent_skills
    - skill_specifications
    - skill_registries
    - context_engineering
    - agent_capability_integration

  H:
    role: >
      AMOS knowledge-integration index for captured SOTA
      agent-skill specifications, registries, workflow
      references, and canonical integration material.

    invariants:
      - source_capture_does_not_imply_implementation
      - specification_does_not_imply_validation
      - validation_does_not_imply_authority
      - discovery_does_not_imply_execution
      - registry_entry_does_not_imply_executability
      - source_repetition_does_not_imply_independence
      - competing_specifications_are_not_silently_merged
      - stale_capture_is_not_automatically_current_canon
      - unknown_fields_remain_unknown_gap

  M:
    source_set:
      count: 6
      independence: UNKNOWN/GAP

    derived_skill_model:
      fields:
        - id
        - version
        - purpose
        - inputs
        - outputs
        - preconditions
        - procedure
        - dependencies
        - authority
        - scope
        - provenance
        - validation

      canonical_status: DERIVED_MODEL

    integration_flow:
      - capture
      - identify
      - classify
      - compare
      - normalize
      - validate
      - govern
      - register

    compatibility_states:
      - COMPATIBLE
      - PARTIALLY_COMPATIBLE
      - COMPETING
      - UNKNOWN/GAP

    execution_boundary:
      required:
        - skill_resolution
        - applicability
        - required_dependencies
        - required_authority

  L:
    raw_sources:
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30|ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_SPECIFICATION_2026_08_29|AGENTSKILLS_SPECIFICATION_2026_08_29]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_IO_SPECIFICATION_2026_08_30|AGENTSKILLS_IO_SPECIFICATION_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30|AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|AGENT_SKILLS_STANDARD_README_2026_08_30]]"
      - "[[11_KNOWLEDGE/LLM_WIKI/raw/ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30|ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30]]"

    supporting_references:
      - "[[11_KNOWLEDGE/LLM_WIKI/wiki/SOTA_AGENT_SKILL_WORKFLOW_REPOS|SOTA_AGENT_SKILL_WORKFLOW_REPOS]]"
      - "[[00_ROOT/AMOS Global Contract for AI Coding Agents|AMOS Global Contract for AI Coding Agents]]"

  gaps:
    canonical_skill_schema: UNKNOWN/GAP
    cross_specification_compatibility: UNKNOWN/GAP
    provenance_independence: UNKNOWN/GAP
    amos_runtime_binding: UNKNOWN/GAP
    executed_validation: UNKNOWN/GAP
    external_spec_authority_ordering: UNKNOWN/GAP

  derived_validation_conditions:
    - specification_conflation
    - registry_treated_as_implementation
    - implementation_treated_as_validation
    - capability_treated_as_authority
    - correlated_sources_treated_as_independent
    - stale_capture_treated_as_current_canon

  epistemic:
    class: DERIVED
    implementation: UNKNOWN/GAP
    empirical_validation: UNKNOWN/GAP
```

______________________________________________________________________

## 22. RSCF-NODE

```yaml
RSCF-NODE:
  node_id: amos_00_root_agent_skills_md
  node_type: note
  path: 00_ROOT/Agent Skills.md
  state: DERIVED
  claim_class: DERIVED
  provenance: "11_KNOWLEDGE/LLM_WIKI/raw/"
  scope: AMOS_general
```

______________________________________________________________________

## 23. RSCF-RELATIONS

```yaml
RSCF-RELATIONS:
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30|ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_SPECIFICATION_2026_08_29|AGENTSKILLS_SPECIFICATION_2026_08_29]]
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_IO_SPECIFICATION_2026_08_30|AGENTSKILLS_IO_SPECIFICATION_2026_08_30]]
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30|AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]]
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|AGENT_SKILLS_STANDARD_README_2026_08_30]]
  - DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/raw/ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30|ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30]]

  - RELATED_TO: [[11_KNOWLEDGE/LLM_WIKI/wiki/SOTA_AGENT_SKILL_WORKFLOW_REPOS|SOTA_AGENT_SKILL_WORKFLOW_REPOS]]
  - RELATED_TO: [[00_ROOT/AMOS Global Contract for AI Coding Agents|AMOS Global Contract for AI Coding Agents]]
```

______________________________________________________________________

## 24. Related

- [[11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30|ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]
- [[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_SPECIFICATION_2026_08_29|AGENTSKILLS_SPECIFICATION_2026_08_29]]
- [[11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLS_IO_SPECIFICATION_2026_08_30|AGENTSKILLS_IO_SPECIFICATION_2026_08_30]]
- [[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30|AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]]
- [[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|AGENT_SKILLS_STANDARD_README_2026_08_30]]
- [[11_KNOWLEDGE/LLM_WIKI/raw/ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30|ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30]]
- [[11_KNOWLEDGE/LLM_WIKI/wiki/SOTA_AGENT_SKILL_WORKFLOW_REPOS|SOTA_AGENT_SKILL_WORKFLOW_REPOS]]
- [[00_ROOT/AMOS Global Contract for AI Coding Agents|AMOS Global Contract for AI Coding Agents]]
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

______________________________________________________________________

## 25. Machine Representation

```yaml
agent_skills:
  artifact:
    title: Agent Skills
    type: note
    source: 00_ROOT

  epistemic:
    state: DERIVED
    claim_class: DERIVED
    provenance: "11_KNOWLEDGE/LLM_WIKI/raw/"
    scope: AMOS_general

  source_index:
    raw_capture_count: 6

    sources:
      - ADDYOSMANI_AGENT_SKILLS_README_2026_08_30
      - AGENTSKILLS_SPECIFICATION_2026_08_29
      - AGENTSKILLS_IO_SPECIFICATION_2026_08_30
      - AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30
      - AGENT_SKILLS_STANDARD_README_2026_08_30
      - ANTHROPICS_SKILLS_AGENT_SKILLS_SPEC_2026_08_30

    provenance_independence: UNKNOWN/GAP
    cross_spec_compatibility: UNKNOWN/GAP

  derived_model:
    skill:
      fields:
        - id
        - version
        - purpose
        - inputs
        - outputs
        - preconditions
        - procedure
        - dependencies
        - authority
        - scope
        - provenance
        - validation

    canonical_schema: UNKNOWN/GAP

  integration:
    stages:
      - CAPTURE
      - IDENTIFY
      - CLASSIFY
      - COMPARE
      - NORMALIZE
      - VALIDATE
      - GOVERN
      - REGISTER

  invariants:
    specification_implies_implementation: false
    implementation_implies_validation: false
    validation_implies_authority: false
    discovery_implies_execution: false
    registry_implies_executability: false
    repeated_source_implies_independence: false

  gaps:
    canonical_skill_schema: UNKNOWN/GAP
    cross_specification_compatibility: UNKNOWN/GAP
    provenance_independence: UNKNOWN/GAP
    amos_runtime_binding: UNKNOWN/GAP
    executed_validation: UNKNOWN/GAP
    external_spec_authority_ordering: UNKNOWN/GAP
```

______________________________________________________________________

## 26. Canonical Compression

The supplied artifact establishes:

$$
\boxed{
\mathrm{AgentSkills}
=
\operatorname{DERIVED\ INDEX}
(
S_1,\ldots,S_6
)
}
$$

with:

$$
\boxed{
\pi(\mathrm{AgentSkills})
=
\texttt{11\_KNOWLEDGE/LLM\_WIKI/raw/}
}
$$

and:

$$
\boxed{
\sigma(\mathrm{AgentSkills})
=
\texttt{AMOS\_general}
}
$$

The strongest safe integration chain is:

$$
\boxed{
\mathrm{Raw\ Specification}
\rightarrow
\mathrm{Source\ Capture}
\rightarrow
\mathrm{Comparison}
\rightarrow
\mathrm{Derived\ AMOS\ Mapping}
\rightarrow
\mathrm{Validation}
\rightarrow
\mathrm{Governed\ Registration}
}
$$

subject to:

$$
\boxed{
\mathrm{SPECIFICATION}
\neq
\mathrm{IMPLEMENTATION}
}
$$

$$
\boxed{
\mathrm{IMPLEMENTATION}
\neq
\mathrm{VALIDATION}
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
\mathrm{DISCOVERY}
\neq
\mathrm{EXECUTION}
}
$$

and:

$$
\boxed{
\mathrm{MULTIPLE\ SOURCES}
\not\Rightarrow
\mathrm{INDEPENDENT\ CONFIRMATION}
}
$$

______________________________________________________________________

## 27. Integrity Boundary

This note is a **DERIVED AMOS integration artifact**, not an independent verification of the external specifications it indexes.

The supplied source directly establishes:

- six named raw agent-skill captures/specifications;
- one SOTA workflow/repository cross-reference;
- one AMOS Global Contract cross-reference;
- `DERIVED` RSCF state;
- `DERIVED` claim class;
- provenance rooted at `11_KNOWLEDGE/LLM_WIKI/raw/`;
- `AMOS_general` scope.

The expanded skill schema, registry model, execution boundary, dependency equations, integration flow, validation conditions, and RSCF decomposition above are **DERIVED formalizations** designed to preserve and govern the supplied structure. They are not attributed to any listed external specification unless separately established from that source.

Therefore the following remain unresolved from this artifact alone:

$$
\boxed{
\operatorname{CanonicalSkillSchema}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{CrossSpecificationCompatibility}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{ProvenanceIndependence}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{AMOSRuntimeBinding}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{ExecutedValidation}
=
\texttt{UNKNOWN/GAP}
}
$$

$$
\boxed{
\operatorname{ExternalSpecAuthorityOrdering}
=
\texttt{UNKNOWN/GAP}
}
$$

The governing boundary is therefore:

$$
\boxed{
\operatorname{Captured}(S)
\not\Rightarrow
\operatorname{Canonical}(S)
\not\Rightarrow
\operatorname{Implemented}(S)
\not\Rightarrow
\operatorname{Validated}(S)
\not\Rightarrow
\operatorname{Authorized}(S)
}
$$

Each transition requires its own evidence and governance.

______________________________________________________________________

**MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

```
```
