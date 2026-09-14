---
canon-group: meta
canon-type: repair-overlay
rscf-state: derived
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
created: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
runtime_binding:
  - 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/logic_math_runtime.py
  - 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/logic_fragments_runtime.py
---

# Core-19 Mathematical and Topological Repair Overlay

Origin architect / steward: **Trang Phan**

## 0. Status

This overlay repairs a specific failure mode in the AMOS logic surface: prose labels, repeated router names, matrices, tensors, topology terms, or named logic fragments MUST NOT be treated as mathematics merely because they are written symbolically.

This overlay is **AMOS_MODEL**, not a canon promotion. It binds bounded executable mathematical and logic-fragment substrates to the current Core-19 repair plane while preserving the existing canon/source hierarchy.

```text
19 x 19 ADDRESS SPACE != 361 PROVEN EQUATIONS
TOPOLOGY != CAUSALITY
ADJACENCY != REACHABILITY
REACHABILITY != SHORTEST PATH
PATH != AUTHORITY
TENSOR SHAPE != SEMANTICS
ALGORITHM AVAILABILITY != ADMISSIBILITY
IMPLEMENTATION != CANON
BOUNDED FRAGMENT != COMPLETE LOGIC
TEST PASS != UNIVERSAL PROOF
```

## 1. Typed mathematical objects

Let the finite Core-19 index set be

\[
V = \{1,2,\ldots,19\}.
\]

A directed topology is represented by a Boolean adjacency matrix

\[
A \in \{0,1\}^{19\times19},
\]

where

\[
A_{ij}=1
\]

means only that the declared directed relation from coordinate \(i\) to coordinate \(j\) is present under the active relation semantics.

It does **not** imply causation, entailment, authority, truth, or temporal precedence unless the relation type separately establishes that interpretation.

The matrix has exactly

\[
|V\times V|=19^2=361
\]

addressable ordered coordinate pairs. This is a coordinate count, not a theorem count and not an equation count.

## 2. Reachability

For a Boolean adjacency matrix \(A\), define the reflexive-transitive closure \(R\) by Warshall's recurrence. Initialize

\[
R^{(0)}_{ij}=A_{ij}\lor[i=j].
\]

For \(k\in\{1,\ldots,n\}\),

\[
R^{(k)}_{ij}
=
R^{(k-1)}_{ij}
\lor
\left(R^{(k-1)}_{ik}\land R^{(k-1)}_{kj}\right).
\]

Then \(R^{(n)}_{ij}=1\) exactly when \(j\) is reachable from \(i\) in the finite directed graph under the declared edge semantics.

Runtime binding: `transitive_closure`.

## 3. Strongly connected components

For directed graph \(G=(V,E)\), vertices \(u,v\in V\) are in the same strongly connected component iff both

\[
u\leadsto v
\]

and

\[
v\leadsto u.
\]

The runtime uses Tarjan's depth-first low-link algorithm and returns a deterministic partition of the finite vertex set.

Runtime binding: `strongly_connected_components`.

Invariant:

\[
\bigcup_{C\in\mathcal{C}} C = V,
\]

and for distinct components \(C_i,C_j\),

\[
C_i\cap C_j=\varnothing.
\]

## 4. Directed acyclic dependency order

For a finite DAG \(G=(V,E)\), a topological order is a bijection

\[
\pi:V\to\{0,\ldots,|V|-1\}
\]

such that for every directed edge \((u,v)\in E\),

\[
\pi(u)<\pi(v).
\]

The runtime uses deterministic Kahn ordering. If a cycle exists, no topological order is returned; the function fails closed.

Runtime binding: `topological_order`.

This order can represent dependency precedence only where the input edge type is explicitly a dependency relation.

## 5. Non-negative weighted shortest paths

Let

\[
w:E\to\mathbb{R}_{\ge0}
\]

be non-negative edge weights. For a path \(p=(v_0,\ldots,v_m)\), define path cost

\[
L(p)=\sum_{r=0}^{m-1}w(v_r,v_{r+1}).
\]

The source-to-target shortest-path distance is

\[
d(s,t)=\min_{p:s\leadsto t}L(p),
\]

with \(d(s,t)=+\infty\) when no path exists.

The runtime uses Dijkstra's algorithm only after enforcing non-negative weights. Negative weights, non-finite weights other than explicit \(+\infty\) absence, non-square matrices, and non-zero diagonal self-distance are rejected.

Runtime binding: `WeightedTopology.shortest_distances`.

## 6. Row-stochastic transition matrices

A finite transition matrix

\[
P\in[0,1]^{n\times n}
\]

is admitted only if every row satisfies

\[
\sum_{j=1}^{n}P_{ij}=1.
\]

For a row probability vector

\[
x\in[0,1]^n,
\qquad
\sum_{i=1}^{n}x_i=1,
\]

the one-step update is

\[
y=xP.
\]

The implementation verifies probability-mass conservation within an explicit numerical tolerance:

\[
\left|\sum_j y_j-1\right|\le\varepsilon.
\]

Runtime binding: `RowStochasticMatrix`.

A stochastic transition is a model of state transition probabilities. It is not itself a causal model and does not license empirical probability claims without data and calibration.

## 7. Typed sparse tensors

A finite tensor is declared by a tuple of unique named axes

\[
(a_1,\ldots,a_d)
\]

and finite positive dimensions

\[
(n_1,\ldots,n_d),
\qquad n_k\in\mathbb{N}_{>0}.
\]

An admissible coordinate

\[
i=(i_1,\ldots,i_d)
\]

must satisfy

\[
0\le i_k<n_k
\]

for every axis \(k\).

The sparse representation stores only explicit finite non-zero-or-declared values; omitted coordinates evaluate to zero. Stored state is immutable after construction.

For stored real-valued entries, the squared Frobenius norm is

\[
\lVert T\rVert_F^2
=
\sum_i |T_i|^2.
\]

Runtime binding: `SparseLogicTensor`.

A tensor shape does not establish semantic compatibility. Axis names, units, provenance, scope, and regime remain separate contracts.

## 8. Bounded executable logic fragments

The canonical root ULK names eight logic-engine ALUs. This overlay does not equate a small executor with a complete ALU. It records only bounded semantics that are now executable.

### 8.1 First-order term unification

For finite first-order terms, a substitution \(\sigma\) unifies terms \(s,t\) when

\[
\sigma(s)=\sigma(t).
\]

The implementation performs Robinson-style term unification with mandatory occurs-check and returns an immutable normalized substitution when one exists.

Runtime binding: `unify` and `apply_substitution`.

Scope: term unification only. Quantifier semantics, resolution completeness, theorem proving, equality theories, and full FOL remain outside this bounded executor.

### 8.2 LTL on finite traces

The implementation evaluates an LTLf subset over an explicit finite non-empty trace. Strong next satisfies

\[
(\tau,i)\models X\varphi
\iff
i+1<|\tau|\land(\tau,i+1)\models\varphi.
\]

Eventually and always satisfy

\[
(\tau,i)\models F\varphi
\iff
\exists j\in[i,|\tau|-1]:(\tau,j)\models\varphi,
\]

\[
(\tau,i)\models G\varphi
\iff
\forall j\in[i,|\tau|-1]:(\tau,j)\models\varphi.
\]

Until satisfies

\[
(\tau,i)\models \varphi U\psi
\]

iff there exists \(j\ge i\) within the finite trace such that \(\psi\) holds at \(j\) and \(\varphi\) holds at every position from \(i\) through \(j-1\).

Runtime binding: `evaluate_ltlf`.

Scope: finite traces only; this does not establish equivalence to an infinite-trace LTL engine.

### 8.3 Finite Kripke modal semantics

A finite Kripke model is represented as

\[
M=(W,\{R_a\}_{a\in A},V),
\]

with finite worlds \(W\), agent-indexed accessibility relations \(R_a\subseteq W\times W\), and valuation \(V\).

Box semantics is

\[
M,w\models \Box_a\varphi
\iff
\forall v\,(wR_av\Rightarrow M,v\models\varphi).
\]

Diamond semantics is

\[
M,w\models \Diamond_a\varphi
\iff
\exists v\,(wR_av\land M,v\models\varphi).
\]

The runtime can separately test whether a declared agent relation is reflexive, symmetric, and transitive, i.e. an equivalence relation suitable for an S5-style interpretation. It does not silently assume S5.

Runtime binding: `KripkeModel`, `evaluate_modal`, `relation_is_s5`.

Scope: finite relational modal semantics. Calling \(\Box_a\) "knowledge" requires an explicit epistemic interpretation and relation assumptions.

### 8.4 Dung grounded argumentation

For finite argumentation framework

\[
AF=(A,R),
\]

where \(R\subseteq A\times A\) is the attack relation, the characteristic function \(F\) maps a set \(S\subseteq A\) to the arguments defended by \(S\).

The grounded extension is computed as the least fixed point

\[
G=\operatorname{lfp}(F),
\]

by monotone iteration from \(\varnothing\) over the finite framework.

Runtime binding: `ArgumentationFramework.grounded_extension`.

Scope: Dung grounded semantics only. Preferred, stable, semi-stable, stage, ranking, probabilistic, or structured argumentation are not implied.

## 9. Algorithm provenance

Current bounded runtime imports mathematical ideas from established algorithm families, while the AMOS composition remains AMOS_MODEL:

- Stephen Warshall, transitive closure / Boolean matrix reachability, 1962, DOI `10.1145/321105.321107`.
- Robert Tarjan, depth-first search and strongly connected components, 1972, DOI `10.1137/0201010`.
- E. W. Dijkstra, non-negative shortest paths, 1959, DOI `10.1007/BF01386390`.
- A. B. Kahn, topological ordering of finite DAGs, 1962, DOI `10.1145/368996.369025`.
- J. A. Robinson, machine-oriented first-order unification/resolution family, 1965, DOI `10.1145/321250.321253`.
- Giuseppe De Giacomo and Moshe Y. Vardi, LTL/LDL on finite traces, IJCAI 2013, pp. 854-860.
- Phan Minh Dung, abstract argumentation semantics, 1995, DOI `10.1016/0004-3702(94)00041-X`.
- Finite relational Kripke semantics is treated as established modal-logic semantics; AMOS does not infer epistemic axioms from the name alone.

The mathematical/algorithmic source does not become AMOS canon merely by implementation.

## 10. Internet algorithm ingestion gate

The request to use algorithms available on the internet is implemented as governed progressive ingestion, not an impossible claim of exhaustive ingestion of all algorithms.

A candidate algorithm \(g\) may enter an executable AMOS subsystem only if the following gate is satisfied:

\[
Admit(g)
=
S\land D\land T\land A\land V\land P\land L,
\]

where:

- \(S\): source identity and provenance are resolved;
- \(D\): input/output domain and assumptions are explicit;
- \(T\): types, dimensions, units, and numerical domains are valid where applicable;
- \(A\): algorithm semantics match the target AMOS problem rather than only its name;
- \(V\): positive, boundary, negative, adversarial, and regression validation exists;
- \(P\): performance/complexity claims are either source-grounded or measured in the target environment;
- \(L\): licensing, redistribution, and implementation constraints are compatible with the repository.

If any load-bearing gate is unresolved, status remains `UNKNOWN/GAP`, `QUARANTINED`, or `SPECIFICATION_ONLY` as appropriate.

## 11. Current executed evidence

For `logic_math_runtime.py` and `test_logic_math_runtime.py`, local bounded reconstruction on 2026-09-14 produced:

```text
Python compile: PASS
Unit/adversarial/property tests: 14 PASS / 0 FAIL
Seeded randomized DAG-order tests: PASS
Seeded randomized reachability-transitivity tests: PASS
Cycle rejection: PASS
Negative/non-finite weight rejection: PASS
Probability-domain and mass-conservation checks: PASS
Core-19 19 x 19 shape checks: PASS
Sparse tensor bounds and immutability: PASS
```

For `logic_fragments_runtime.py` and `test_logic_fragments_runtime.py`:

```text
Python compile: PASS
Unit/boundary/adversarial tests: 14 PASS / 0 FAIL
Unification occurs-check: PASS
Cyclic external substitution rejection: PASS
LTLf terminal strong-next boundary: PASS
LTLf eventually/always/until semantics: PASS
Kripke box/diamond evaluation: PASS
S5 relation-property validation: PASS
Dung grounded fixed-point cases: PASS
```

GitHub Actions `Reference Runtime Tests` subsequently compiled the full reference implementation and ran the full discovered unittest suite successfully on the repair branch.

This receipt establishes only the tested finite implementation surface.

## 12. Remaining logic gaps

Bounded executor available, but full fragment equivalence remains unproven for:

- FOL: term unification exists; full quantified FOL/resolution/theorem-proving surface remains open.
- Temporal: LTLf finite-trace evaluation exists; infinite-trace LTL and automata/model-checking equivalence remain open.
- Epistemic/modal: finite Kripke evaluation exists; epistemic interpretation and source-specific axiom systems remain open unless explicitly bound.
- Non-monotonic: Dung grounded semantics exists; other argumentation/non-monotonic semantics remain open.

Still `SPECIFICATION_ONLY` / unresolved at this repair layer:

- dependent-type checking;
- quantum-logic executable rebind;
- categorical/topos executable semantics;
- empirical causal inference;
- global AMOS executable closure.

Each promotion requires its own typed semantics, provenance, assumptions, implementation, and executed/formal evidence.

## 13. Mutation boundary

AMOS may evolve repository state through governed code/document changes, tests, replay, and explicit promotion gates. This does not imply mutation of the host language model's neural weights.

```text
REPOSITORY SELF-REPAIR != MODEL-WEIGHT SELF-MODIFICATION
RUNTIME ADAPTATION != CANON PROMOTION
LEARNING ARTIFACT != AUTHORITY
```

## 14. Binding

- Math/topology runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/logic_math_runtime.py`
- Math/topology tests: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_logic_math_runtime.py`
- Logic-fragment runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/logic_fragments_runtime.py`
- Logic-fragment tests: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_logic_fragments_runtime.py`
- Existing bounded Core-19 runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`
- Existing exact bounded classical SAT firewall: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/classical_sat_firewall.py`
- CI: `.github/workflows/reference-runtime-tests.yml`

This overlay supersedes no canonical source. It narrows ambiguous mathematical claims by attaching explicit executable semantics and visible limits.
