---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rscf Node Index
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

# Source-preserved artifact

```markdown
---
type: index
source: 00_ROOT
aliases:
- RSCF Node Index
- AMOS RSCF Nodes Index
- RSCF_NODES
canon_group: tech-ai
canon_type: navigation
document_version: 1.0.0
origin_architect: Trang Phan
rscf_state: derived
status: ACTIVE_MOC
tags:
- amos-os
- root
- rscf
- index
- navigation
- canon/root
title: RSCF Node Index
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---

# RSCF Node Index

Brain-level index of RSCF-typed notes in the AMOS OS vault.

---

## Related

- [[00_ROOT/00_HOME|00_HOME]]
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---

RSCF-NODE

node_id: rscf_node_index

node_type: note

path: 00_ROOT/RSCF_NODE_INDEX.md

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

claim_class: AMOS_MODEL

---

**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
```

## Derived / Proposed AMOS Formalization

Everything below is **DERIVED / PROPOSED**. It does not mutate the source metadata, aliases, status, RSCF node, source relations, or declared document version.

A Drive lookup confirms that an `RSCF_NODE_INDEX.md` artifact exists and that its visible content matches the core identity, aliases, version, state, node ID, and path used here. The Root Map and Root MOC also reference the index.

## 1. Artifact role

Let

$$
I_R
$$

denote the RSCF Node Index.

The source states:

$$
\operatorname{Type}(I_R)=\texttt{index},
$$

$$
\operatorname{CanonType}(I_R)=\texttt{navigation},
$$

and describes it as a:

> Brain-level index of RSCF-typed notes in the AMOS OS vault.

Therefore the strongest structural interpretation is:

$$
\boxed{
\operatorname{Role}(I_R)=\operatorname{RSCFNavigationIndex}
}
$$

rather than treating it as the underlying RSCF corpus itself.

Thus:

$$
\boxed{
\operatorname{Index}(I_R)
\neq
\operatorname{IndexedCorpus}(I_R)
}
$$

and:

$$
\operatorname{IndexedBy}(x,I_R)
\not\Rightarrow
x=I_R.
$$

______________________________________________________________________

## 2. Epistemic-layer separation

The source contains:

$$
\operatorname{rscf\_state}(I_R)=\texttt{derived},
$$

while nested RSCF declares:

$$
\operatorname{rscf.state}(I_R)=\texttt{SOURCE\_CLAIM},
$$

$$
\operatorname{rscf.claim\_class}(I_R)=\texttt{SOURCE\_CLAIM}.
$$

The trailing RSCF node also declares:

$$
\operatorname{NodeClaimClass}(I_R)=\texttt{AMOS\_MODEL}.
$$

These are distinct metadata fields:

$$
\boxed{
\texttt{derived}
\neq
\texttt{SOURCE\_CLAIM}
\neq
\texttt{AMOS\_MODEL}.
}
$$

No precedence rule is supplied here.

Therefore:

$$
\operatorname{UnifiedEpistemicPrecedence}(I_R)
=
\texttt{UNKNOWN/GAP}.
$$

This does not necessarily indicate inconsistency; the fields may represent different layers such as document lifecycle state, source provenance state, and node-level claim class.

______________________________________________________________________

## 3. Identity and version

The source establishes:

$$
\operatorname{NodeID}(I_R)
=
\texttt{rscf\_node\_index},
$$

$$
\operatorname{Path}(I_R)
=
\texttt{00\_ROOT/RSCF\_NODE\_INDEX.md},
$$

and:

$$
\operatorname{DocumentVersion}(I_R)=1.0.0.
$$

Thus a derived address tuple is:

$$
\boxed{
\operatorname{Addr}(I_R)
=
(
\texttt{rscf\_node\_index},
1.0.0,
\texttt{00\_ROOT/RSCF\_NODE\_INDEX.md}
)
}
$$

where version is taken from `document_version`, not invented as a separate artifact version.

The source does not explicitly state that `document_version` is the same version field used by all AMOS runtime identity resolution.

Therefore:

$$
\operatorname{RuntimeVersionBinding}
=
\texttt{UNKNOWN/GAP}
$$

unless governed by a separate versioning contract.

______________________________________________________________________

## 4. Alias semantics

The source declares three aliases:

$$
A(I_R)
=
\{
\text{RSCF Node Index},
\text{AMOS RSCF Nodes Index},
\text{RSCF\_NODES}
\}.
$$

Aliases support discovery:

$$
a\in A(I_R)
\Rightarrow
\operatorname{MayResolveTo}(a,I_R).
$$

But alias identity must not silently become canonical identity:

$$
\boxed{
\operatorname{Alias}(a,I_R)
\not\Rightarrow
a=\operatorname{NodeID}(I_R).
}
$$

Likewise, an alias matching another file name does not by itself prove artifact identity.

This matters because the source links separately to:

$$
\texttt{AMOS\_RSCF\_NODES}.
$$

Therefore:

$$
\boxed{
\texttt{RSCF\_NODE\_INDEX}
\neq
\texttt{AMOS\_RSCF\_NODES}
}
$$

unless an explicit equivalence relation establishes otherwise.

______________________________________________________________________

## 5. Index versus master RSCF node collection

The source establishes:

$$
I_R
\xrightarrow{\texttt{INDEXED\_BY}}
\texttt{AMOS\_RSCF\_NODES}.
$$

This implies that the RSCF Node Index is itself indexed by the broader AMOS RSCF node structure.

Therefore:

$$
\boxed{
I_R
\neq
\texttt{AMOS\_RSCF\_NODES}
}
$$

under the supplied topology.

A useful derived hierarchy is:

$$
\texttt{AMOS\_RSCF\_NODES}
\rightarrow
I_R
\rightarrow
\text{RSCF-typed navigation targets},
$$

but only the first relation is explicitly source-declared here.

The second arrow is a semantic interpretation of the phrase “index of RSCF-typed notes,” not a new canonical RSCF relation.

______________________________________________________________________

## 6. Set-theoretic model

Let:

$$
\mathcal N
=
\{\text{RSCF-typed notes in the AMOS OS vault}\}.
$$

Let:

$$
\mathcal I
$$

be the set of index entries represented by this artifact.

A well-formed index aims for a relation:

$$
\iota:\mathcal I\rightarrow\mathcal N.
$$

For each index record (i):

$$
\iota(i)=n
$$

should resolve to an RSCF note (n).

The source does not enumerate (\\mathcal I).

Therefore:

$$
|\mathcal I|
=
\texttt{UNKNOWN/GAP}.
$$

Likewise:

$$
|\mathcal N|
=
\texttt{UNKNOWN/GAP}
$$

from this artifact alone.

The existence of a large `AMOS_RSCF_NODES.md` file in Drive does not establish its exact canonical node count without parsing and validation.

______________________________________________________________________

## 7. Index completeness

Define coverage:

$$
\operatorname{Coverage}(I_R)
=
\frac{
|\operatorname{ResolvedIndexedNodes}(I_R)|
}{
|\mathcal N|
}.
$$

A complete index would satisfy:

$$
\operatorname{Coverage}(I_R)=1.
$$

But the source does not claim completeness.

Therefore:

$$
\boxed{
\operatorname{Complete}(I_R)=\texttt{UNKNOWN/GAP}.
}
$$

`ACTIVE_MOC` does not imply exhaustive coverage:

$$
\operatorname{Status}(I_R)=\texttt{ACTIVE\_MOC}
\not\Rightarrow
\operatorname{Complete}(I_R).
$$

______________________________________________________________________

## 8. Addressability firewall

An indexed note is addressable only to the extent that its target resolves.

For (n\\in\\mathcal N):

$$
\operatorname{Listed}(n,I_R)
\not\Rightarrow
\operatorname{Resolvable}(n).
$$

Even if resolvable:

$$
\operatorname{Resolvable}(n)
\not\Rightarrow
\operatorname{Implemented}(n).
$$

And:

$$
\operatorname{Implemented}(n)
\not\Rightarrow
\operatorname{Validated}(n).
$$

Thus the index must preserve:

$$
\boxed{
\text{INDEXED}
\neq
\text{IMPLEMENTED}
\neq
\text{VALIDATED}.
}
$$

These are distinctions, not necessarily exhaustive lifecycle stages.

______________________________________________________________________

## 9. Navigation is not authority

The source labels this artifact as navigation.

Therefore:

$$
\operatorname{Indexed}(n,I_R)
\not\Rightarrow
\operatorname{Authority}(I_R,n).
$$

Likewise:

$$
\operatorname{IndexRank}(n)
\not\Rightarrow
\operatorname{EpistemicPriority}(n).
$$

The index cannot promote a claim merely because it is discoverable.

Thus:

$$
\boxed{
\operatorname{Navigation}
\neq
\operatorname{Governance}.
}
$$

______________________________________________________________________

## 10. Navigation is not provenance

The source RSCF provenance is:

$$
\operatorname{Provenance}(I_R)=\texttt{AMOS\_corpus}.
$$

That provenance applies to this artifact's source declaration.

It does not automatically become the provenance of every indexed node.

For node (n):

$$
\operatorname{IndexedBy}(n,I_R)
\not\Rightarrow
\operatorname{Provenance}(n)=\operatorname{Provenance}(I_R).
$$

Each target should preserve its own provenance lineage.

______________________________________________________________________

## 11. Navigation is not epistemic inheritance

Suppose:

$$
\operatorname{ClaimClass}(I_R)=\texttt{AMOS\_MODEL}.
$$

Then for indexed node (n):

$$
\operatorname{IndexedBy}(n,I_R)
\not\Rightarrow
\operatorname{ClaimClass}(n)=\texttt{AMOS\_MODEL}.
$$

Likewise:

$$
\operatorname{State}(I_R)=\texttt{SOURCE\_CLAIM}
\not\Rightarrow
\operatorname{State}(n)=\texttt{SOURCE\_CLAIM}.
$$

The index must not overwrite target epistemic typing.

______________________________________________________________________

## 12. Related links

The source declares:

$$
I_R
\operatorname{RelatedTo}
\texttt{00\_HOME},
$$

$$
I_R
\operatorname{RelatedTo}
\texttt{AMOS\_RSCF\_NODES},
$$

and:

$$
I_R
\operatorname{RelatedTo}
\texttt{00\_ROOT\_MOC / AMOS MOC}.
$$

These `Related` links are navigational.

They do not independently establish:

$$
\operatorname{DEPENDS\_ON},
$$

$$
\operatorname{GOVERNED\_BY},
$$

$$
\operatorname{DERIVED\_FROM},
$$

or:

$$
\operatorname{CAUSES}.
$$

No stronger edge type should be invented.

______________________________________________________________________

## Full RSCF H/M/L Expansion

```yaml
classification: DERIVED_FORMALIZATION

RSCF_EXPANSION:
  source_node:
    node_id: rscf_node_index
    node_type: note
    path: 00_ROOT/RSCF_NODE_INDEX.md
    claim_class: AMOS_MODEL

  source_frontmatter:
    type: index
    source: 00_ROOT
    canon_group: tech-ai
    canon_type: navigation
    document_version: 1.0.0
    origin_architect: Trang Phan
    rscf_state: derived
    status: ACTIVE_MOC

  source_rscf:
    state: SOURCE_CLAIM
    claim_class: SOURCE_CLAIM
    provenance: AMOS_corpus
    scope: root_index

  H:
    role: RSCF_NAVIGATION_INDEX
    purpose:
      - brain_level_navigation
      - RSCF_note_discovery
      - root_level_indexing
      - MOC_connectivity

  M:
    role: INDEX_RESOLUTION_LAYER
    concerns:
      - alias_resolution
      - node_identity
      - path_resolution
      - version_binding
      - relation_integrity
      - index_coverage
      - orphan_detection
      - duplicate_detection

  L:
    role: INDIVIDUAL_INDEX_ENTRY
    proposed_fields:
      - node_id
      - node_type
      - path
      - claim_class
      - rscf_state
      - provenance_ref
      - version_ref
      - relation_refs
      - resolution_state

  unresolved:
    total_index_entries: UNKNOWN/GAP
    total_RSCF_nodes: UNKNOWN/GAP
    index_completeness: UNKNOWN/GAP
    runtime_version_binding: UNKNOWN/GAP
    alias_collision_policy: UNKNOWN/GAP
```

## Derived machine-readable index contract

```yaml
classification: DERIVED_FORMALIZATION

RSCF_NODE_INDEX_CONTRACT:
  identity:
    node_id: rscf_node_index
    path: 00_ROOT/RSCF_NODE_INDEX.md
    document_version: 1.0.0

  role:
    type: INDEX
    canon_type: NAVIGATION
    status: ACTIVE_MOC

  aliases:
    - RSCF Node Index
    - AMOS RSCF Nodes Index
    - RSCF_NODES

  source_epistemic_layer:
    rscf_state_field: derived
    nested_rscf_state: SOURCE_CLAIM
    nested_claim_class: SOURCE_CLAIM
    node_claim_class: AMOS_MODEL
    precedence: UNKNOWN/GAP

  index_entry:
    required:
      - node_id
      - path

    recommended_when_available:
      - node_type
      - claim_class
      - provenance
      - version
      - status
      - relations

    unresolved_target:
      state: UNKNOWN/GAP

  integrity_rules:
    - INDEXED_DOES_NOT_IMPLY_IMPLEMENTED
    - INDEXED_DOES_NOT_IMPLY_VALIDATED
    - INDEXED_DOES_NOT_IMPLY_AUTHORIZED
    - INDEXED_DOES_NOT_OVERRIDE_PROVENANCE
    - INDEXED_DOES_NOT_OVERRIDE_CLAIM_CLASS
    - ALIAS_DOES_NOT_IMPLY_CANONICAL_IDENTITY
```

## Derived index-entry semantics

For index entry (e), define:

$$
e=(id,p,t,v,\rho,\pi,\sigma),
$$

where:

- (id) = target node identifier;
- (p) = target path;
- (t) = node type;
- (v) = version when applicable;
- (\\rho) = relation references;
- (\\pi) = provenance reference;
- (\\sigma) = resolution state.

A minimum admissible index record requires:

$$
id\neq\varnothing
$$

and:

$$
p\neq\varnothing.
$$

If either is absent:

$$
\operatorname{State}(e)=\texttt{UNKNOWN/GAP}.
$$

If identity and path disagree:

$$
\operatorname{Resolve}(id)\neq\operatorname{Resolve}(p)
\Rightarrow
\operatorname{State}(e)=\texttt{COMPETING}
$$

until discriminating evidence establishes the canonical target.

______________________________________________________________________

## 13. Duplicate detection

Let entries (e_i,e_j) satisfy:

$$
e_i.id=e_j.id
$$

but:

$$
e_i.path\neq e_j.path.
$$

This is a potential identity conflict:

$$
\operatorname{PotentialConflict}(e_i,e_j).
$$

Likewise if:

$$
e_i.path=e_j.path
$$

but:

$$
e_i.id\neq e_j.id,
$$

the index should not silently merge them.

Possible states are:

$$
\texttt{ALIAS},
\quad
\texttt{SUPERSESSION},
\quad
\texttt{DUPLICATE},
\quad
\texttt{COMPETING},
\quad
\texttt{UNKNOWN/GAP},
$$

but classification requires evidence from the governing identity/versioning rules.

______________________________________________________________________

## 14. Orphan detection

Let:

$$
\mathcal N
$$

be all RSCF nodes and:

$$
\mathcal I
$$

be all index-resolved nodes.

An orphan candidate is:

$$
\mathcal O
=
\mathcal N\setminus\mathcal I.
$$

But:

$$
n\notin\mathcal I
\not\Rightarrow
\operatorname{OrphanCanonical}(n)
$$

unless the index is proven complete and intended to index that node class.

Therefore the safe term is:

$$
\boxed{
\operatorname{OrphanCandidate}
}
$$

until coverage assumptions are validated.

______________________________________________________________________

## 15. Broken-link detection

For index entry (e), define:

$$
R(e)=
\begin{cases}
1,& \text{target resolves}\\
0,& \text{target demonstrably does not resolve}\\
?,& \text{resolution not established}.
\end{cases}
$$

Then:

$$
R(e)=?
\Rightarrow
\texttt{UNKNOWN/GAP}.
$$

A resolution timeout or unavailable runtime must not be conflated with a missing artifact.

Thus:

$$
\operatorname{NotResolvedNow}
\not\Rightarrow
\operatorname{Nonexistent}.
$$

______________________________________________________________________

## 16. Version compatibility

For source index version:

$$
v_I=1.0.0.
$$

For indexed node version (v_n), if present, compatibility should be governed by explicit versioning rules.

The index source alone does not specify:

$$
\operatorname{Compatible}(v_I,v_n).
$$

Therefore version relationships are:

$$
\texttt{UNKNOWN/GAP}
$$

unless provided by a governing versioning artifact.

No semantic-version rule is invented here merely from the string `1.0.0`.

______________________________________________________________________

## 17. Status semantics

The source declares:

$$
\operatorname{Status}(I_R)=\texttt{ACTIVE\_MOC}.
$$

The strongest literal interpretation is that the artifact declares itself active as a MOC/navigation object.

It does not imply:

$$
\operatorname{RuntimeExecutorActive}(I_R),
$$

$$
\operatorname{CoverageComplete}(I_R),
$$

or:

$$
\operatorname{AllLinksValid}(I_R).
$$

Thus:

$$
\boxed{
\texttt{ACTIVE\_MOC}
\neq
\texttt{FULLY\_VALIDATED\_INDEX}.
}
$$

______________________________________________________________________

## 18. Provenance topology for an index lookup

A lookup through this index can be modeled as:

$$
q
\rightarrow
I_R
\rightarrow
e
\rightarrow
n
\rightarrow
\pi_n,
$$

where:

- (q) = query;
- (e) = index entry;
- (n) = resolved node;
- (\\pi_n) = node's own provenance.

The index is therefore an address-routing layer.

It should not terminate provenance resolution at itself:

$$
q\rightarrow I_R\rightarrow n
$$

is insufficient for a claim that depends on (n)'s underlying evidence if (\\pi_n) is not resolved.

______________________________________________________________________

## 19. Smallest-sufficient retrieval

For query (q), let candidate index entries be:

$$
E_q\subseteq\mathcal I.
$$

Let relevant resolved nodes be:

$$
N_q\subseteq\mathcal N.
$$

The smallest-sufficient retrieval objective is:

$$
N_q^*
=
\arg\min_{N_q}
|N_q|
$$

subject to:

$$
\operatorname{DecisionSufficient}(N_q,q).
$$

The index supports discovery; it does not require loading every RSCF node.

Thus:

$$
\boxed{
\operatorname{IndexAvailable}
\not\Rightarrow
\operatorname{LoadAllNodes}.
}
$$

______________________________________________________________________

## 20. Confidence firewall

For conclusion (c) reached after index traversal:

$$
c
\leftarrow
n_1,\ldots,n_k.
$$

The index adds no epistemic confidence merely because retrieval succeeded.

Thus:

$$
C(c)
\le
\min_i C(n_i)
$$

for load-bearing premises, absent independent revalidation.

And:

$$
\operatorname{SuccessfulIndexResolution}
\not\Rightarrow
\operatorname{ConfidenceIncrease}.
$$

______________________________________________________________________

## Derived validation receipt schema

```yaml
classification: DERIVED_FORMALIZATION

RSCF_NODE_INDEX_VALIDATION_RECEIPT:
  receipt_id: REQUIRED

  artifact:
    node_id: rscf_node_index
    path: 00_ROOT/RSCF_NODE_INDEX.md
    document_version: 1.0.0

  checks:
    identity_resolution: UNKNOWN/GAP
    path_resolution: UNKNOWN/GAP
    alias_uniqueness: UNKNOWN/GAP
    duplicate_detection: UNKNOWN/GAP
    orphan_detection_scope: UNKNOWN/GAP
    broken_link_scan: UNKNOWN/GAP
    version_compatibility: UNKNOWN/GAP
    relation_integrity: UNKNOWN/GAP
    provenance_preservation: UNKNOWN/GAP
    index_coverage: UNKNOWN/GAP

  metrics:
    total_entries: UNKNOWN/GAP
    resolved_entries: UNKNOWN/GAP
    unresolved_entries: UNKNOWN/GAP
    duplicate_candidates: UNKNOWN/GAP
    orphan_candidates: UNKNOWN/GAP
    broken_link_candidates: UNKNOWN/GAP

  conclusion:
    state: UNKNOWN/GAP

  falsifiers: []
  invalidation_conditions: []
```

No validation field defaults to `PASS`.

______________________________________________________________________

## Derived / Proposed Falsifiers

$$
F_1:
\quad
\operatorname{node\_id}
\text{ resolves to a different artifact than declared path}.
$$

$$
F_2:
\quad
\text{two non-alias entries claim the same canonical identity}.
$$

$$
F_3:
\quad
\text{an index relation silently changes target provenance or claim class}.
$$

$$
F_4:
\quad
\text{the index is treated as proof that a target is implemented or validated}.
$$

$$
F_5:
\quad
\text{an unresolved target is promoted to valid}.
$$

$$
F_6:
\quad
\text{an alias collision is silently merged without identity evidence}.
$$

$$
F_7:
\quad
\text{coverage is claimed complete without a validated denominator}.
$$

______________________________________________________________________

## Derived gap classification

```yaml
classification: DERIVED_FORMALIZATION

GAPS:
  canonical_epistemic_precedence:
    state: UNKNOWN/GAP
    severity: EXPLANATORY

  runtime_version_binding:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  total_index_entries:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  total_RSCF_node_population:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  index_completeness:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  alias_collision_policy:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  orphan_definition_scope:
    state: UNKNOWN/GAP
    severity: EXPLANATORY

  artifact_specific_validation_receipt:
    state: NOT_ESTABLISHED
    severity: DECISION_RELEVANT
```

The severity assignments are **DERIVED / PROPOSED**, not source metadata.

______________________________________________________________________

## Source RSCF — Exact Preservation

```text
RSCF-NODE

node_id: rscf_node_index

node_type: note

path: 00_ROOT/RSCF_NODE_INDEX.md

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

claim_class: AMOS_MODEL
```

No additional relation is inserted into this source block.

______________________________________________________________________

## Canonical Compression

The strongest source-supported compression is:

$$
\boxed{
I_R
=
\text{active Root-level navigation index for RSCF-typed AMOS OS notes}
}
$$

with:

$$
\boxed{
\operatorname{NodeID}(I_R)=\texttt{rscf\_node\_index}
}
$$

$$
\boxed{
\operatorname{Path}(I_R)
=
\texttt{00\_ROOT/RSCF\_NODE\_INDEX.md}
}
$$

and:

$$
\boxed{
\operatorname{DocumentVersion}(I_R)=1.0.0.
}
$$

Its core semantic firewall is:

$$
\boxed{
\operatorname{Indexed}(n)
\not\Rightarrow
\operatorname{Implemented}(n)
}
$$

$$
\boxed{
\operatorname{Indexed}(n)
\not\Rightarrow
\operatorname{Validated}(n)
}
$$

$$
\boxed{
\operatorname{Indexed}(n)
\not\Rightarrow
\operatorname{Authorized}(n)
}
$$

$$
\boxed{
\operatorname{Indexed}(n)
\not\Rightarrow
\operatorname{ClaimClass}(n)=\operatorname{ClaimClass}(I_R)
}
$$

and:

$$
\boxed{
\operatorname{Indexed}(n)
\not\Rightarrow
\operatorname{Provenance}(n)=\operatorname{Provenance}(I_R).
}
$$

The artifact's own source states remain distinct:

$$
\boxed{
\texttt{rscf\_state: derived},
\quad
\texttt{rscf.state: SOURCE\_CLAIM},
\quad
\texttt{claim\_class: AMOS\_MODEL}
}
$$

with their precedence:

$$
\boxed{\texttt{UNKNOWN/GAP}}
$$

unless a governing metadata contract resolves it.

**Conclusion class:** supplied artifact = `SOURCE_CLAIM / AMOS_MODEL` with separate `rscf_state: derived`; appended formalization = `DERIVED / PROPOSED`. Drive confirms the artifact exists and is referenced from Root navigation, but does not by itself establish index completeness or validation.
