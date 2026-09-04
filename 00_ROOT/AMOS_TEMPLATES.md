---
artifact_id: AMOS-TEMPLATES
conclusion_class: DECISION / AMOS_MODEL
confidence: DERIVED
name: AMOS_Templates
origin_architect: Trang Phan
provenance: VAULT_INDEX
status: active
steward: Trang Phan
tags:
  - templates
  - amos-os
  - root
  - templater
  - index
  - obsidian
  - canon-group/tech-ai
  - canon/tooling
  - topic/templates
  - amos-obsidian-linking-plugins
  - amos-layer-maps
title: AMOS Templates
type: index
source: 00_ROOT
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---

# AMOS Templates

Index of Obsidian note and automation templates used by the AMOS vault.

______________________________________________________________________

## Current templates

- linked-note — Templater template for new notes that auto-links to the root, Cosmo Brain, and home MOCs
- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — plugin stack, Templater setup, and linking checklist

______________________________________________________________________

## Related MOCs

- [[00_ROOT/00_HOME|00_HOME]] — universal vault hub
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — AMOS OS master map
- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]|00 Cosmo Brain MOC — Cosmo Brain root stub
- [[00_ROOT/AMOS_LAYER_MAPS|AMOS_LAYER_MAPS]] — top-level layer map index
- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian linking plugin stack

______________________________________________________________________

## Derived / Proposed AMOS Formalization

> Everything below this boundary is **DERIVED / PROPOSED formalization** of the supplied source. It does not alter the source metadata, establish undocumented template behavior, or convert tooling descriptions into verified runtime implementation.

## 0. Epistemic Status

The supplied artifact differs materially from the preceding placeholder artifacts.

Its source declares:

\[
\\operatorname{Status}(A)=\\texttt{active}
\]

and:

## \[ \\operatorname{ConclusionClass}(A)

\\texttt{DECISION / AMOS_MODEL}.
\]

It also declares:

\[
\\operatorname{Confidence}(A)=\\texttt{DERIVED}
\]

while the embedded RSCF declares:

\[
\\operatorname{RSCFState}(A)=\\texttt{SOURCE_CLAIM}
\]

and:

\[
\\operatorname{RSCFClaimClass}(A)=\\texttt{SOURCE_CLAIM}.
\]

These fields are preserved as distinct source-declared dimensions.

Therefore:

\[
\\boxed{
\\texttt{active}
\\not\\Rightarrow
\\texttt{VERIFIED}
}
\]

and:

\[
\\boxed{
\\texttt{DERIVED confidence}
\\not\\Rightarrow
\\texttt{independently validated}.
}
\]

The source does **not** declare:

```text
canonical_status
implementation_status
validation_status
executable_binding
```

Therefore those states must not be invented.

For this artifact:

$$
\boxed{
\operatorname{CanonicalStatus}(A)
=
\texttt{UNKNOWN/GAP}
}
$$

only as a **derived assessment of missing source information**, not as a source metadata field.

Likewise:

$$
\boxed{
\operatorname{ValidationStatus}(A)
=
\texttt{UNKNOWN/GAP}
}
$$

from this source alone.

______________________________________________________________________

## 1. Purpose

The source explicitly defines the artifact as:

> Index of Obsidian note and automation templates used by the AMOS vault.

Thus the strongest source-supported functional classification is:

$$
\boxed{
A=\operatorname{Index}(\text{AMOS templates})
}
$$

with source-declared type:

$$
\operatorname{Type}(A)=\texttt{index}.
$$

The artifact indexes at least two current entries:

$$
\mathcal T_{\text{source}}
=
\{
t_1,t_2
\}
$$

where:

$$
t_1=\texttt{linked-note}
$$

and:

$$
t_2=
\texttt{AMOS\_OBSIDIAN\_LINKING\_PLUGINS}.
$$

Therefore:

$$
\boxed{
|\mathcal T_{\text{source}}|=2
}
$$

for the entries explicitly listed under `Current templates`.

This does **not** prove that the complete AMOS vault contains exactly two templates.

Hence:

$$
\boxed{
|\mathcal T_{\text{source}}|=2
\not\Rightarrow
|\mathcal T_{\text{vault}}|=2.
}
$$

______________________________________________________________________

## 2. Index Boundary

An index entry establishes addressability or reference, not necessarily implementation validity.

For indexed object (x):

$$
\operatorname{Indexed}(x,A)
$$

does not by itself imply:

$$
\operatorname{ExistsAtRuntime}(x)
$$

or:

$$
\operatorname{Validated}(x)
$$

or:

$$
\operatorname{Authorized}(x).
$$

Therefore:

$$
\boxed{
\operatorname{Indexed}(x)
\not\Rightarrow
\operatorname{Validated}(x).
}
$$

Likewise:

$$
\boxed{
\operatorname{DocumentedTemplate}(x)
\not\Rightarrow
\operatorname{ExecutableTemplate}(x).
}
$$

The source says the templates are “used by the AMOS vault,” but it does not provide an execution receipt, installation state, plugin version, or runtime test.

That statement therefore remains source-grounded rather than independently verified.

______________________________________________________________________

## 3. Template Set Model

Let:

$$
\mathcal T
=
\{t_1,t_2,\ldots,t_n\}
$$

represent the AMOS template set indexed by this artifact.

A minimal template representation can be modeled as:

$$
t_i=
(
id_i,
type_i,
purpose_i,
location_i,
dependencies_i,
outputs_i
).
$$

This tuple is **DERIVED / PROPOSED**.

The supplied source does not define a canonical template schema.

For the currently listed entries:

### (t_1) — linked-note

Source-declared semantics:

$$
\operatorname{Name}(t_1)=\texttt{linked-note}
$$

$$
\operatorname{Mechanism}(t_1)=\texttt{Templater template}
$$

with stated purpose:

$$
\operatorname{Purpose}(t_1)
=
\text{new-note auto-linking}.
$$

The source specifically identifies automatic links to:

$$
\{
\text{root},
\text{Cosmo Brain},
\text{home MOCs}
\}.
$$

### (t_2) — AMOS Obsidian Linking Plugins

The source describes this linked artifact as containing:

$$
\{
\text{plugin stack},
\text{Templater setup},
\text{linking checklist}
\}.
$$

Whether (t_2) is itself literally a template, a supporting tooling artifact, or an indexed dependency/support document is not explicitly typed in this source.

Therefore:

$$
\boxed{
\operatorname{ExactTemplateRole}(t_2)
=
\texttt{UNKNOWN/GAP}.
}
$$

______________________________________________________________________

## 4. linked-note Semantic Model

The source states that `linked-note` auto-links new notes to three MOC classes.

A minimal source-faithful model is:

$$
\operatorname{linked\_note}(n)
\rightarrow
\{
L_R(n),
L_C(n),
L_H(n)
\}
$$

where:

- (L_R) = root link;
- (L_C) = Cosmo Brain link;
- (L_H) = home-MOC link.

This formalizes the supplied description only.

The exact generated Markdown, path-resolution algorithm, frontmatter fields, Templater JavaScript, filename rules, and insertion behavior are not supplied.

Therefore:

$$
\boxed{
\operatorname{TemplateBody}(\texttt{linked-note})
=
\texttt{UNKNOWN/GAP}.
}
$$

And:

$$
\boxed{
\operatorname{ExecutionCode}(\texttt{linked-note})
=
\texttt{UNKNOWN/GAP}.
}
$$

______________________________________________________________________

## 5. Auto-Linking Model

For newly created note (n), define its target-link set:

$$
L(n)=
\{
\ell_{\text{root}},
\ell_{\text{cosmo}},
\ell_{\text{home}}
\}.
$$

The source supports the intended relation:

$$
\operatorname{Apply}(\texttt{linked-note},n)
\Rightarrow
\operatorname{TargetLinks}(n)\supseteq L(n)
$$

as a formalization of the stated template purpose.

It does **not** establish the stronger runtime claim:

$$
\operatorname{Apply}(\texttt{linked-note},n)
\Rightarrow
\operatorname{RuntimeVerified}(L(n)).
$$

No execution receipt is supplied.

______________________________________________________________________

## 6. Linking Topology

The source explicitly links the template index to several AMOS navigation structures.

Let:

$$
A=\texttt{AMOS Templates}.
$$

The source declares navigation toward:

$$
H=\texttt{00\_HOME}
$$

$$
R=\texttt{00\_ROOT\_MOC}
$$

$$
C=\texttt{00\_COSMO\_BRAIN\_MOC}
$$

$$
M=\texttt{AMOS\_LAYER\_MAPS}
$$

$$
P=\texttt{AMOS\_OBSIDIAN\_LINKING\_PLUGINS}.
$$

Thus the supplied artifact forms a navigation neighborhood:

$$
N(A)=\{H,R,C,M,P\}.
$$

This is a structural link relation only.

It does not imply:

$$
A\equiv H
$$

or:

$$
A\equiv R
$$

or canonical authority flowing automatically from those links.

______________________________________________________________________

## 7. Template Dependency Boundary

The presence of `Templater` in the source establishes a tooling relationship at the descriptive level.

A useful derived relation is:

$$
\texttt{linked-note}
\xrightarrow{\text{USES}}
\texttt{Templater}.
$$

But the source does not specify:

- Templater version;
- Obsidian version;
- plugin configuration;
- installation state;
- enabled/disabled state;
- API compatibility;
- execution permissions;
- exact template folder;
- required supporting scripts.

Therefore:

$$
\boxed{
\operatorname{RuntimeDependencyClosure}
=
\texttt{UNKNOWN/GAP}.
}
$$

The tag:

```text
templater
```

and source prose support relevance, but not a complete executable dependency specification.

______________________________________________________________________

## 8. Capability / Execution Firewall

A template being syntactically present does not establish that it executes correctly.

Formally:

$$
\boxed{
\operatorname{TemplatePresent}(t)
\not\Rightarrow
\operatorname{TemplateExecutable}(t).
}
$$

Likewise:

$$
\boxed{
\operatorname{PluginInstalled}(p)
\not\Rightarrow
\operatorname{PluginConfigured}(p).
}
$$

And:

$$
\boxed{
\operatorname{PluginConfigured}(p)
\not\Rightarrow
\operatorname{TemplateValidated}(t).
}
$$

These distinctions matter because the source provides an index and descriptive purpose, not runtime validation evidence.

______________________________________________________________________

## 9. Template Identity

The artifact itself has explicit source identity:

$$
I(A)=
(
\texttt{AMOS-TEMPLATES},
\texttt{AMOS\_Templates},
\texttt{index},
\texttt{00\_ROOT}
).
$$

The source also supplies an RSCF node identifier:

$$
\operatorname{NodeID}(A)
=
\texttt{amos\_templates}.
$$

And source path:

$$
\operatorname{Path}(A)
=
\texttt{00\_ROOT/AMOS\_Templates.md}.
$$

These identifiers should remain distinct rather than silently collapsed:

$$
\boxed{
\texttt{artifact\_id}
\neq
\texttt{node\_id}
}
$$

as identifiers of different declared fields, even if they refer to the same artifact.

______________________________________________________________________

## 10. Provenance

Two source-level provenance declarations are present:

Top-level:

$$
P_{\text{top}}
=
\texttt{VAULT\_INDEX}.
$$

Embedded RSCF:

$$
P_{\text{RSCF}}
=
\texttt{AMOS\_corpus}.
$$

These are not necessarily contradictory because they may describe different provenance layers.

A derived provenance model is:

$$
P(A)=
(
P_{\text{artifact}},
P_{\text{RSCF}}
).
$$

Thus:

$$
P(A)=
(
\texttt{VAULT\_INDEX},
\texttt{AMOS\_corpus}
).
$$

No stronger equivalence should be assumed:

$$
\boxed{
\texttt{VAULT\_INDEX}
\not\equiv
\texttt{AMOS\_corpus}
}
$$

unless an explicit provenance binding establishes that equivalence.

______________________________________________________________________

## 11. Conclusion-Class Boundary

The top-level source declares:

```yaml
conclusion_class: DECISION / AMOS_MODEL
```

This should remain exactly preserved.

A useful typed interpretation is that the artifact carries both decision/model semantics as source metadata.

It should **not** be silently rewritten into:

```text
VERIFIED
```

or:

```text
EMPIRICAL
```

or:

```text
CANONICAL
```

because the source does not establish those classifications.

Therefore:

$$
\boxed{
\texttt{DECISION / AMOS\_MODEL}
\not\Rightarrow
\texttt{VERIFIED}.
}
$$

______________________________________________________________________

## 12. Confidence Boundary

The source declares:

$$
\operatorname{Confidence}(A)=\texttt{DERIVED}.
$$

No numerical confidence value is supplied.

Therefore assigning:

$$
0.8,\;0.9,\;0.95,\ldots
$$

would invent unsupported precision.

The exact preserved state is:

$$
\boxed{
\operatorname{Confidence}(A)=\texttt{DERIVED}.
}
$$

______________________________________________________________________

## 13. Template Registry vs Template Content

This artifact is an index.

Let:

$$
I_T
$$

represent the index and:

$$
C(t)
$$

represent the actual content of template (t).

Then:

$$
\boxed{
I_T(t)\neq C(t).
}
$$

Therefore knowing that `linked-note` is indexed does not expose its complete implementation.

Similarly:

$$
\operatorname{Description}(t)
\neq
\operatorname{TemplateSource}(t).
$$

The exact `linked-note` implementation remains unresolved from this artifact.

______________________________________________________________________

## 14. Template Execution Model

A generic derived execution model can be represented as:

$$
n'=\tau(n,c,e)
$$

where:

- (n) = initial note;
- (\\tau) = template transformation;
- (c) = execution context;
- (e) = environment;
- (n') = resulting note.

For `linked-note`:

$$
n'
=
\tau_{\text{linked-note}}(n,c,e).
$$

The source states an intended output property:

$$
\{
\ell_R,\ell_C,\ell_H
\}
\subseteq
\operatorname{Links}(n').
$$

But because the executable body is absent:

$$
\boxed{
\tau_{\text{linked-note}}
=
\texttt{UNKNOWN/GAP}
}
$$

at implementation-detail level.

______________________________________________________________________

## 15. Scope / Regime

The RSCF source declares:

$$
\operatorname{Scope}(A)=\texttt{root\_index}.
$$

Therefore conclusions from this artifact should remain bounded to its indexing role.

The artifact does not establish universal behavior for:

- every Obsidian vault;
- every AMOS deployment;
- every historical AMOS version;
- every Templater configuration.

Thus:

$$
\boxed{
\operatorname{Claim}(A)
\Rightarrow
\operatorname{Scope}(A)=\texttt{root\_index}
}
$$

unless another source expands applicability.

______________________________________________________________________

## 16. Freshness

Unlike the preceding placeholder artifacts, the supplied metadata contains no explicit:

```text
version
updated
```

fields.

Therefore source-level freshness cannot be inferred from a version or timestamp here.

The correct state is:

$$
\boxed{
\operatorname{Version}(A)=\texttt{UNKNOWN/GAP}
}
$$

and:

$$
\boxed{
\operatorname{UpdatedAt}(A)=\texttt{UNKNOWN/GAP}
}
$$

from this artifact alone.

The source does declare:

$$
\operatorname{Status}(A)=\texttt{active},
$$

but:

$$
\boxed{
\texttt{active}
\not\Rightarrow
\texttt{fresh}.
}
$$

______________________________________________________________________

## 17. Template Validation

For template (t), a derived validation predicate might require:

$$
V(t)=
V_{\text{syntax}}
\land
V_{\text{dependency}}
\land
V_{\text{link}}
\land
V_{\text{negative}}
\land
V_{\text{environment}}.
$$

Where:

$$
V_{\text{syntax}}
=
\text{template parses}
$$

$$
V_{\text{dependency}}
=
\text{required tooling resolves}
$$

$$
V_{\text{link}}
=
\text{generated links resolve as intended}
$$

$$
V_{\text{negative}}
=
\text{malformed/missing context handled}
$$

$$
V_{\text{environment}}
=
\text{tested environment compatible}.
$$

These are **DERIVED validation dimensions**.

The source supplies no executed validation receipt.

Therefore:

$$
\boxed{
V(\texttt{linked-note})
=
\texttt{UNKNOWN/GAP}
}
$$

from the supplied evidence.

______________________________________________________________________

## 18. Failure Modes

### F1 — Broken target link

Template generates a link whose target cannot be resolved.

### F2 — Wrong MOC binding

Generated note links to an unintended root, home, or Cosmo Brain node.

### F3 — Missing Templater dependency

Template exists but required plugin functionality is unavailable.

### F4 — Configuration drift

Template assumptions no longer match the active Obsidian/Templater configuration.

### F5 — Path drift

Target MOC moves while the template retains an obsolete path.

### F6 — Duplicate link insertion

Automation repeatedly inserts equivalent links.

### F7 — Index drift

The index lists a template that no longer exists or omits one that does.

### F8 — Template/content divergence

Description in this index no longer matches actual template implementation.

### F9 — Scope leakage

A template intended for a specific note class is applied universally.

### F10 — Provenance loss

Template or supporting automation changes without recoverable lineage.

These are **DERIVED failure modes**, not source claims that these failures currently exist.

______________________________________________________________________

## 19. High-Information Validation Checks

The cheapest checks capable of materially changing confidence would be:

$$
C_1=
\text{resolve actual linked-note template}
$$

$$
C_2=
\text{inspect current template body}
$$

$$
C_3=
\text{resolve Templater dependency/configuration}
$$

$$
C_4=
\text{execute against controlled test note}
$$

$$
C_5=
\text{verify generated links}.
$$

The validation chain can be represented as:

$$
\boxed{
\text{INDEX}
\rightarrow
\text{RESOLVE}
\rightarrow
\text{INSPECT}
\rightarrow
\text{EXECUTE}
\rightarrow
\text{VERIFY}.
}
$$

No supplied evidence establishes completion of that chain.

______________________________________________________________________

## 20. Full RSCF Expansion

```yaml
RSCF:
  artifact:
    artifact_id: AMOS-TEMPLATES
    name: AMOS_Templates
    title: AMOS Templates
    type: index
    source: 00_ROOT
    node_id: amos_templates
    path: 00_ROOT/AMOS_Templates.md

  stewardship:
    origin_architect: Trang Phan
    steward: Trang Phan

  source_epistemic_state:
    conclusion_class: DECISION / AMOS_MODEL
    confidence: DERIVED
    status: active
    provenance: VAULT_INDEX

    rscf:
      state: SOURCE_CLAIM
      claim_class: SOURCE_CLAIM
      provenance: AMOS_corpus
      scope: root_index

  H:
    domain: root_index

    purpose: >
      Index Obsidian note and automation templates used by
      the AMOS vault.

    source_supported_entries:
      - linked-note
      - AMOS_OBSIDIAN_LINKING_PLUGINS

  M:
    linked_note:
      classification: SOURCE_DESCRIBED_TEMPLATE
      mechanism: Templater
      purpose: new-note auto-linking

      declared_link_targets:
        - root
        - Cosmo Brain
        - home MOCs

      exact_template_body: UNKNOWN/GAP
      executable_code: UNKNOWN/GAP
      validation_receipt: UNKNOWN/GAP

    linking_plugins:
      path: 11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS
      source_description:
        - plugin stack
        - Templater setup
        - linking checklist
      exact_role_in_template_set: UNKNOWN/GAP

  L:
    navigation:
      home: 00_ROOT/00_HOME
      root_moc: 00_ROOT/00_ROOT_MOC
      cosmo_brain_moc: 00_ROOT/00_COSMO_BRAIN_MOC
      layer_maps: 00_ROOT/AMOS_LAYER_MAPS
      linking_plugins: 11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS

    source_relations:
      indexed_by:
        - 00_ROOT/00_HOME
        - 00_ROOT/AMOS_RSCF_NODES

    unresolved:
      template_body: UNKNOWN/GAP
      template_folder: UNKNOWN/GAP
      templater_version: UNKNOWN/GAP
      obsidian_version: UNKNOWN/GAP
      runtime_configuration: UNKNOWN/GAP
      execution_validation: UNKNOWN/GAP
      version: UNKNOWN/GAP
      freshness_timestamp: UNKNOWN/GAP
```

______________________________________________________________________

## 21. Source RSCF-NODE

```yaml
RSCF-NODE:
  node_id: amos_templates
  node_type: note
  path: 00_ROOT/AMOS_Templates.md
```

______________________________________________________________________

## 22. Source RSCF-RELATIONS

```yaml
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

claim_class: AMOS_MODEL
```

This preserves the supplied placement of:

```text
claim_class: AMOS_MODEL
```

after the relation list rather than silently relocating it into the source node.

______________________________________________________________________

## 23. Derived / Proposed Relations

The following are structural formalizations of source-described relationships and are **not additions to the source RSCF relation block**:

```yaml
PROPOSED_RELATIONS:
  - INDEXES:
      from: AMOS-TEMPLATES
      to: linked-note

  - REFERENCES:
      from: AMOS-TEMPLATES
      to: 11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS

  - NAVIGATES_TO:
      from: AMOS-TEMPLATES
      to: 00_ROOT/00_ROOT_MOC

  - NAVIGATES_TO:
      from: AMOS-TEMPLATES
      to: 00_ROOT/00_COSMO_BRAIN_MOC

  - NAVIGATES_TO:
      from: AMOS-TEMPLATES
      to: 00_ROOT/AMOS_LAYER_MAPS
```

For the source-described Templater relationship:

$$
\boxed{
\texttt{linked-note}
\xrightarrow{\text{DESCRIBED\_AS\_TEMPLATER\_TEMPLATE}}
\texttt{Templater}.
}
$$

This does not assert that `Templater` is itself a canonical AMOS node.

______________________________________________________________________

## 24. Machine Representation

```yaml
amos_templates:
  identity:
    artifact_id: AMOS-TEMPLATES
    name: AMOS_Templates
    title: AMOS Templates
    type: index
    source: 00_ROOT
    node_id: amos_templates
    path: 00_ROOT/AMOS_Templates.md

  stewardship:
    origin_architect: Trang Phan
    steward: Trang Phan

  source_classification:
    conclusion_class: DECISION / AMOS_MODEL
    confidence: DERIVED
    status: active
    provenance: VAULT_INDEX

  source_rscf:
    state: SOURCE_CLAIM
    claim_class: SOURCE_CLAIM
    provenance: AMOS_corpus
    scope: root_index

  source_purpose:
    statement: >
      Index of Obsidian note and automation templates
      used by the AMOS vault.

  current_templates:
    linked_note:
      name: linked-note
      source_description: >
        Templater template for new notes that auto-links
        to the root, Cosmo Brain, and home MOCs.
      implementation_body: UNKNOWN/GAP
      runtime_validation: UNKNOWN/GAP

    linking_plugins:
      path: 11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS
      source_description:
        - plugin stack
        - Templater setup
        - linking checklist
      exact_template_role: UNKNOWN/GAP

  related_mocs:
    - 00_ROOT/00_HOME
    - 00_ROOT/00_ROOT_MOC
    - 00_ROOT/00_COSMO_BRAIN_MOC
    - 00_ROOT/AMOS_LAYER_MAPS
    - 11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS

  source_relations:
    indexed_by:
      - 00_ROOT/00_HOME
      - 00_ROOT/AMOS_RSCF_NODES

  derived_integrity:
    indexed_implies_validated: false
    documented_implies_executable: false
    active_implies_fresh: false
    source_claim_implies_verified: false
    derived_confidence_implies_empirical_validation: false

  unresolved_from_source:
    canonical_status: UNKNOWN/GAP
    implementation_status: UNKNOWN/GAP
    validation_status: UNKNOWN/GAP
    executable_binding: UNKNOWN/GAP
    template_source_body: UNKNOWN/GAP
    templater_version: UNKNOWN/GAP
    obsidian_version: UNKNOWN/GAP
    environment_configuration: UNKNOWN/GAP
    artifact_version: UNKNOWN/GAP
    freshness_timestamp: UNKNOWN/GAP
```

______________________________________________________________________

## 25. Canonical Compression

The strongest source-supported compression is:

$$
\boxed{
\texttt{AMOS-TEMPLATES}
=
\text{active root index of AMOS Obsidian note/automation templates}.
}
$$

The source explicitly identifies:

$$
\boxed{
\mathcal T_{\text{listed}}
=
\{
\texttt{linked-note},
\texttt{AMOS\_OBSIDIAN\_LINKING\_PLUGINS}
\}.
}
$$

For `linked-note`:

$$
\boxed{
\text{Templater template}
\rightarrow
\text{new-note linking to root + Cosmo Brain + home MOCs}.
}
$$

But:

$$
\boxed{
\text{INDEXED}
\not\Rightarrow
\text{RUNTIME VERIFIED}.
}
$$

And:

$$
\boxed{
\texttt{active}
\not\Rightarrow
\texttt{fresh or validated}.
}
$$

The source provides:

$$
\boxed{
\operatorname{Confidence}
=
\texttt{DERIVED}
}
$$

and:

$$
\boxed{
\operatorname{RSCFState}
=
\texttt{SOURCE\_CLAIM}.
}
$$

These classifications remain intact.

______________________________________________________________________

## 26. Integrity Boundary

This artifact supports the conclusion that an **AMOS Templates** root index is declared active and indexes Obsidian note/automation template resources.

It explicitly supports:

$$
\boxed{
\texttt{linked-note}
}
$$

as a Templater template intended to auto-link new notes to root, Cosmo Brain, and home MOCs.

It also explicitly references:

$$
\boxed{
\texttt{AMOS\_OBSIDIAN\_LINKING\_PLUGINS}
}
$$

for the plugin stack, Templater setup, and linking checklist.

The supplied source does **not** provide:

- the actual `linked-note` template body;
- executable Templater code;
- Templater version;
- Obsidian version;
- current plugin installation state;
- current plugin configuration;
- template execution receipts;
- generated-note validation results;
- a complete claim that the listed entries exhaust all AMOS templates;
- an explicit canonical-status field;
- an explicit implementation-status field;
- an explicit validation-status field;
- an explicit executable-binding field;
- artifact version or freshness timestamp.

Therefore:

$$
\boxed{
\text{SOURCE DESCRIPTION}
\neq
\text{EXECUTABLE VALIDATION}.
}
$$

The artifact should remain an index until deeper template sources or runtime evidence are traversed.

______________________________________________________________________

## Related

Source-declared:

- [[00_ROOT/00_HOME|00_HOME]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
- [[00_ROOT/AMOS_LAYER_MAPS|AMOS_LAYER_MAPS]]
- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]]
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
