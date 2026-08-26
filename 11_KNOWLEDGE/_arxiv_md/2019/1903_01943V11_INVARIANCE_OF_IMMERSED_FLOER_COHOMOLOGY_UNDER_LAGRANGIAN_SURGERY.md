---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.01943v11
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1903.01943v11_Invariance_of_immersed_Floer_cohomology_under_Lagrangian_surgery

> Source: 1903.01943v11_Invariance_of_immersed_Floer_cohomology_under_Lagrangian_surgery.pdf

> Pages: 133

---


## Page 1


INVARIANCE OF IMMERSED FLOER COHOMOLOGY
UNDER LAGRANGIAN SURGERY
JOSEPH PALMER AND CHRIS WOODWARD
Abstract. We show that Floer cohomology of an immersed Lagrangian brane
is invariant under smoothing of a self-intersection point if the quantum valuation
of the weakly bounding cochain vanishes and the Lagrangian has dimension at
least two. The chain-level map replaces the two orderings of the self-intersection
point with meridional and longitudinal cells on the handle created by the surgery,
and uses a bijection between holomorphic disks developed by Fukaya-Oh-Ohta-
Ono [31, Chapter 10]. Our result generalizes invariance of potentials for certain
Lagrangian surfaces in Dimitroglou-Rizell–Ekholm–Tonkonog [24, Theorem 1.2],
and implies the invariance of Floer cohomology under mean curvature flow with
this type of surgery, as conjectured by Joyce [39].
Contents
1.
Introduction
2
2.
Lagrangian surgery
10
2.1.
The local model
10
2.2.
Surgery and its properties
13
3.
Treed holomorphic disks
16
3.1.
Treed disks
16
3.2.
Treed holomorphic disks
19
4.
Coherent perturbations
25
4.1.
Donaldson hypersurfaces
26
4.2.
Coherence
29
4.3.
Transversality and compactness
35
4.4.
Orientations
36
5.
Fukaya algebras
38
5.1.
Composition maps
40
5.2.
Gauge equivalence
47
5.3.
Divisor insertions
49
6.
Holomorphic disks and neck-stretching
55
6.1.
Broken holomorphic disks
55
This work was partially supported by NSF grant DMS 1711070. Any opinions, findings, and
conclusions or recommendations expressed in this material are those of the author(s) and do not
necessarily reflect the views of the National Science Foundation.
1
arXiv:1903.01943v11  [math.SG]  24 Dec 2025


## Page 2


2
JOSEPH PALMER AND CHRIS WOODWARD
6.2.
Fredholm theory and exponential decay
61
6.3.
Compactness for buildings
69
6.4.
Transversality for buildings
73
6.5.
Gluing with Lagrangian boundary conditions
75
6.6.
Deformation to split form
87
6.7.
Homotopy equivalences
88
7.
Holomorphic disks bounding the handle
90
7.1.
Classifying disks with a single end
90
7.2.
Ruling out disks with large angle in the unsurgered handle
94
7.3.
Ruling out disks with large angle in the surgered handle
98
7.4.
Ruling out maps intersecting the critical locus
108
7.5.
Comparing disks bounding the flattened and unflattened handles
109
8.
Fukaya algebras under surgery
111
8.1.
Morse functions on the surgered and unsurgered Lagrangian
111
8.2.
The surgered-unsurgered bijection
112
8.3.
Equivalence of potentials
115
8.4.
Equivalence of Floer cohomologies
122
8.5.
Variations of local system
124
9.
Quasi-isomorphisms
125
9.1.
Quasi-isomorphisms induced by Hamiltonian perturbation
125
9.2.
Quasi-isomorphism with the surgery
127
9.3.
Mapping cones
128
References
130
1. Introduction
A Lagrangian immersion in a compact symplectic manifold with transverse self-
intersection defines a homotopy-associative Fukaya algebra developed by Akaho-
Joyce in [4]. The framework of Fukaya-Oh-Ohta-Ono [31] associates to this algebra
a space of solutions to the projective Maurer-Cartan equation. For any solution,
there is a Lagrangian Floer cohomology group, independent up to isomorphism of
all choices. In Palmer-Woodward [49], we studied the behavior of Floer cohomology
under variation of an immersion in the direction of the Maslov (relative first Chern)
class, such as a coupled mean-curvature/Kähler-Ricci flow. The main result of [49]
was that there exists a flow on the space of projective Maurer-Cartan solutions with
the following property: The isomorphism class of the Lagrangian Floer cohomology
is invariant as long as the valuation of the Maurer-Cartan solution with respect to
the quantum parameter stays positive and the Lagrangian stays immersed.
In
particular, the Floer cohomology is invariant as the immersion passes through
a self-tangency.
Naturally a question arises whether one can continue the flow
through a “wall” created by the vanishing valuation at a self-intersection point.


## Page 3


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
3
Via the mirror symmetry conjectures, this question is expected to be related to a
question on deformation theory of vector bundles on a mirror complex manifold, or
more precisely, matrix factorizations [40]. The mirror of the mean curvature flow
is expected to be (a deformed version of) the Yang-Mills flow [38]. The isomor-
phism class of the bundle is constant under Yang-Mills flow and, in particular, the
cohomology is invariant [6]. That is, there are no real-codimension-one “walls” on
the mirror side, and so one does not expect such walls in the deformation spaces
for Lagrangian branes either. For vector bundles on projective varieties there exist
versal deformations [29] in the sense of Kuranishi; see for example [62] for coherent
sheaves. The base of these versal deformations are complex-analytic spaces. The
results of this paper can be viewed as giving a theory of versal deformations for
immersed Lagrangians, in which solutions to the projective Maurer-Cartan equa-
tion with negative q-exponents parametrize the actual deformations of an immersed
Lagrangian. As in the case of deformations of singular algebraic varieties [5, Chap-
ter XI], in order to produce the expected space of deformations one must allow
smoothings at the singularities.
A way of smoothing singularities of immersed self-transverse Lagrangians was
introduced by Lalonde-Sikorav [43] and Polterovich [51]. Let
ϕ0 : L0 →X
be a self-transverse Lagrangian immersion with compact domain L0 with an self-
intersection point x ∈ϕ0(L0). For a sufficiently small surgery parameter ϵ ∈R
Figure 1. An immersion and its surgery
denote by
ϕϵ : Lϵ →X
the surgery obtained by removing small balls around the intersection and gluing in
a cylinder. The surgery parameter ϵ is closely related to the difference A(ϵ) from
(17) in the areas of disks bounding (that is, having boundary in) ϕ0(L0) and ϕϵ(Lϵ).


## Page 4


4
JOSEPH PALMER AND CHRIS WOODWARD
A long line of papers in symplectic geometry have studied the effect of Lagrangian
surgery on Floer theory. Seidel’s long exact triangle [57] is perhaps the first exam-
ple, since a Dehn twist is a special case of a surgery. More generally, holomorphic1
disks with boundary in the surgery were described in Fukaya-Oh-Ohta-Ono [31,
Chapter 10]. Abouzaid [2], Mak-Wu [46], Tanaka [63], Chantraine-Dimitroglou-
Rizell-Ghiggini-Golovko [17, Chapter 8], Fang [27], and Hong-Kim-Lau [37, The-
orem B] proved various generalizations.
The invariance of disk potentials was
shown for certain Lagrangian surfaces by Pascaleff–Tonkonog [50, Theorem 1.2]
and Dimitroglou-Rizell–Ekholm–Tonkonog [24, Theorem 1.2]. In dimension two,
the Lagrangians related by the two different signs of surgery parameter are said
to be related by mutation. Mutation-invariance of Lagrangian Floer homology was
shown via Lagrangian cobordism techniques by Hicks [35]. The “wall-crossing”
formula for the change in the local system given by the above formulas is discussed
in Auroux [9], [10], Kontsevich-Soibelman [42], and Pascaleff-Tonkonog [50].
We construct a natural identification of solutions of the projective Maurer-Cartan
equations for the surgered and unsurgered Lagrangian branes that preserves the
disk potentials and Floer cohomology. The version of Floer cohomology used here
is the cohomology of the twisted first composition map for a Fukaya algebra which
counts treed holomorphic disks bounding the Lagrangian. Our results show that
if the quantum valuation at a self-intersection point of a family of Maurer-Cartan
solutions in a mean curvature flow of Palmer-Woodward [49] reaches zero then
(at least under the conditions in the Theorem) the solution may be continued
by Lagrangian surgery so that the Floer cohomology of the surgery is invariant.
Thus the flow may be continued after the singular time without changing the Floer
cohomology.
The assumptions necessary for invariance of Floer cohomology to hold are en-
coded in the following definitions. Let
(1)
Λ = C((qR)) :=
( ∞
X
i=0
aiqdi
 lim
i→∞di = ∞, ∀i, di ∈R, ai ∈C
)
denote the Novikov field with complex coefficients,2 equipped with q-valuation
valq : Λ −{0} →R,
∞
X
i=0
aiqdi 7→min(di, ai ̸= 0).
Let Λ0 denote the group of units in Λ with vanishing q-valuation
Λ0 = val−1
q (0) =


a0 +
X
i≥1
aiqdi ∈Λ
 a0 ∈C −{0}, ∀i, ai ∈C, di > 0


.
1To save space, we refer to pseudoholomorphic disks with respect to some almost complex
structure as holomorphic.
2The Fukaya algebras in this paper are defined with rational coefficients, but allowing complex
coefficients gives a possibly-larger Maurer-Cartan space.


## Page 5


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
5
Let ϕ0 : L0 →X be a Lagrangian immersion. A local system on ϕ0 is a flat Λ0-
line bundle y on ϕ0(L0), or equivalently, a flat line bundle on L0 together with
identifications of the fibers y(x−) →y(x+) at the self-intersection points
x = (x−, x+),
ϕ0(x−) = ϕ0(x+).
If ϕ0(L0) is connected with fundamental group π1(ϕ0(L0)) for some choice of base
point then the space of isomorphism classes of local systems is isomorphic to the
space of representations
R(ϕ0) ∼= Hom(π1(ϕ0(L0)), Λ0) ∼= Hom(H1(ϕ0(L0)), Λ0).
For disconnected Lagrangians, R(ϕ0) is defined by replacing π1(ϕ0(L0)) with the
product of the fundamental groups of the connected components of ϕ0(L0). Let
ϕ0 : L0 →X be equipped with a brane structure consisting of an orientation,
relative spin structure, and Λ0-valued local system y ∈R(ϕ0). In Sections 5 and
6 we construct for any such datum a Fukaya algebra CF(ϕ0), which is a strictly
unital A∞algebra.
The Fukaya algebra has a canonical family of deformations parametrized by odd
cochains, and the cohomology is defined for solutions to the projective Maurer-
Cartan equation. By definition, any element b ∈CF(ϕ0) is given as a sum
b =
X
x∈I(ϕ0)
b(x)x
over generators x ∈I(ϕ0) corresponding to critical points of a Morse function,
corresponding to cells in a cellular decomposition, or self-intersection points. In this
paper, we choose to index the Floer generators by cells, which we find conceptually
clearer than the indexing by Morse critical points. In particular, if b is odd then
b(x) vanishes for x of even degree. Let MC(ϕ0) denote the space of projective
Maurer-Cartan solutions, also called , weakly bounding cochains, as in (54). For
δ > 0 small let MCδ(ϕ0) denote the subspace satisfying
valq(b(x)) ∈(−δ, ∞)
at the transverse self-intersection points x of ϕ0. For sufficiently small δ, associated
to any b0 ∈MCδ(ϕ0) is a Floer cohomology group HF(ϕ0, b0), independent of all
choices up to isomorphism. Given x = (x−, x+), denote by x = (x+, x−) ∈L2
0 the
self-intersection point with the opposite ordering. The degree of x is even resp.
odd if the natural map
Tx−L ⊕Tx+L →Tϕ(x±)X
is orientation preserving resp. reversing. If dim(L) is even then x is odd if and
only if x is odd, while if dim(L) is odd then x is odd if and only if x even. By
convention b0(x) vanishes if x is even.


## Page 6


6
JOSEPH PALMER AND CHRIS WOODWARD
Definition 1.1. Let ϕ0 : L0 →X be a Lagrangian immersion and b0 ∈MCδ(ϕ0)
a Maurer-Cartan solution. An odd self-intersection point x = (x−, x+) ∈L2
0 is
admissible for b0 if and only if
(a) the q-valuation of the coefficient b0(x) is close to zero in the sense that
(2)
valq(b0(x)) ∈(−δ, 0)
and
(b) either b0(x) = 0, or dim(L0) = 2 and the q-valuation of b0(x) is sufficiently
large in the sense that 3
(3)
valq(b0(x)b0(x)) > 0.
This ends the Definition.
The invariance of Floer cohomology under surgery holds after the following
change in the weakly bounding cochain. The surgered Lagrangian Lϵ is obtained
from L0 by removing the self-intersection points x± ∈L0 and gluing in a handle
Hϵ ∼= Sn−1 × R
as in Section 2 below. We denote by
µ ∼= Sn−1 × {0},
λ ∼= {pt} × R
the meridional and longitudinal cells on the handle Hϵ, oriented so that the bijection
of Proposition 7.2 is orientation preserving.
Definition 1.2. Let x = (x−, x+) with ϕ0(x−) = ϕ0(x+). For ϵ > 0 let
CFδ(ϕ0, ϵ) ⊂CF(ϕ0)
denote the space of elements b0 ∈CF(ϕ0) whose q-valuation at the surgery point
is opposite the surgery area:
valq(b0(x)) + A(ϵ) = 0
with notation from (17) and (3). Let
MCδ(ϕ, ϵ) ⊂CFδ(ϕ, ϵ)
denote the space of Maurer-Cartan solutions b0 for which x is admissible and that
vanish on the closure of the cells containing x±:
(4)
b0(σ) = 0,
∀σ ⊂τ, τ ∋x±.
3For the sake of discussing explicit examples, we also allow dim(L0) = 1 under the following
assumptions (which do not typically hold): b0(x) = 0, every holomorphic disk u : S →X with
boundary on ϕ meeting x has a branch change at every z ∈∂S with u(z) = x, and there are no
holomorphic disks u : S →X with exactly one corner at x.


## Page 7


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
7
Define
(5)
Ψ : CFδ(ϕ0, ϵ) →CF(ϕϵ),
b0 7→b0 −b0(x)x −b0(x)x+



ln(b0(x)qA(ϵ))µ + ln(b0(x)b0(x) + 1)λ
dim(L0) = 2
ln(b0(x)qA(ϵ))µ + b0(x)b0(x)λ
dim(L0) > 2
where the logarithms are defined by formal power series expansion at the leading
order term for any choice of branch, well-defined by the assumption that b0(x)qA(ϵ)
and b0(x)b0(x) + 1 have vanishing q-valuation. This ends the Definition.
The vanishing condition (4) can always be achieved up to gauge equivalence by
Lemma 5.11. In the case dim(L0) = 2, we assume that the surgered Lagrangian
Lϵ is equipped with a local system which has holonomy −1 around the meridian;
note that this assumption constrains the topology of the surgery. The conditions
in Definition 1.2 are satisfied in our application to mean curvature flow [49].
We may now state the main result. Let MC≥0(ϕϵ) be the enlarged space of
projective Maurer-Cartan solutions in (61) for ϕϵ, in which one allows the coefficient
of λ to have vanishing q-valuation.4
Theorem 1.3. Let ϕ0 : L0 →X be an immersed Lagrangian brane of dimension
dim(L0) at least three in a compact rational symplectic manifold X. There exists
a constant δ > 0 such that for any b0 ∈MCδ(ϕ0) and any admissible transverse
self-intersection point x ∈Isi(ϕ) and small ϵ > 0 as in Definition 1.1 there exist
perturbation systems defining the Fukaya algebras CF(ϕ0) and CF(ϕϵ) so that the
following holds: The map Ψ of Definition 1.2 satisfies
(6)
Ψ(MCδ(ϕ0, ϵ)) ⊂MC≥0(ϕϵ)
preserves the disk potentials
Ψ∗Wϵ = W0,
W0 : MCδ(ϕ0) →Λ,
Wϵ : MC≥0(ϕϵ) →Λ
and lifts to an isomorphism of Floer cohomology groups
HF(ϕ0, b0) ∼= HF(ϕϵ, bϵ := Ψ(b0)), ∀b0 ∈MCδ(ϕ0, ϵ).
The same result holds for dim(L0) = 2 under the assumption described in (5.21).
In other words, immersed Floer cohomology is invariant under surgery after a
suitable change in the weakly bounding cochain. We conjecture that the assump-
tion b0(x) = 0 for dim(L0) > 2 is not necessary.
Remark 1.4. J. Hicks [36, Section 2] has given examples of Lagrangian spheres that
have surgeries that in the Fukaya category are non-isomorphic depending on the
sign of the surgery parameter ϵ; the result above does not contradict these examples
4This enlargement is only relevant in the case dim(L) = 2, and in this case we show that the
Maurer-Cartan sum still converges.


## Page 8


8
JOSEPH PALMER AND CHRIS WOODWARD
since we require the immersed Lagrangian ϕ0 : L0 →X itself to have a non-zero
weakly bounding cochain b0.
Remark 1.5. Returning to the application to mean curvature flow, Theorem 1.3
suggests the possibility of mean curvature flow for Lagrangians with preventive
surgery. Namely, similar to the set-up in the Thomas-Yau conjecture [64] suppose
one performs coupled mean curvature/Kähler-Ricci flow on a Lagrangian immer-
sion ϕt with unobstructed and non-trivial Floer theory HF(ϕt). The results of this
paper and Palmer-Woodward [49] imply that the non-triviality of the Floer homol-
ogy HF(ϕt) carries along with the flow ϕt, if a surgery before the time at which the
geometric singularity forms is performed whenever the q-valuation valq(bt) of the
Maurer-Cartan solution bt crosses zero. This type of surgery is preventive rather
than emergency in the sense that the Lagrangian immersion ϕt is not about to
cease to exist.
Non-triviality of the Floer cohomology affects the types of sin-
gularities that can occur as discussed by Joyce [39]. One naturally wonders what
kind of singularities can occur generically (meaning allowing arbitrary Hamiltonian
perturbations) in the case of non-trivial Floer cohomology.
We may upgrade the isomorphisms of Floer cohomology to a quasi-isomorphism
in the Fukaya category as follows. A full construction of a Fukaya category con-
taining all Lagrangians is beyond the techniques of this paper; we consider rather
the following simplified Fukaya category with two objects. Let ϕ′
0 : L′
0 →X be
a Hamiltonian isotopy of ϕ0 : L0 →X such that ϕ0, ϕ′
0 intersect transversally, as
in Figure 16; the shaded region represents the disks that correspond under the
bijection. We assume that ϵ is sufficiently small so that the surgered immersion
ϕϵ : Lϵ →X intersects ϕ′
0 transversally as well. After a Hamiltonian perturbation
we may assume that the Lagrangian
(7)
˜ϕ : ϕ0 ∪ϕ′
0 : L0 ∪L′
0 →X
is rational, immersed, and with transverse self-intersection, and similarly for
˜ϕϵ : ϕϵ ∪ϕ′
0 : Lϵ ∪L′
0 →X.
As such, we obtain a category Fuk ˜ϕ0(X) with two objects ϕ0, ϕ′
0 equipped with
weakly bounding cochains, and with morphisms defined by the corresponding sub-
spaces of CF(˜ϕ0). For sufficiently small surgery parameter ϵ, the intersection ϕϵ∩ϕ′
0
is still transverse and we obtain a category Fuk ˜ϕϵ(X) with objects (ϕϵ, bϵ), (ϕ′
0, b′
0)
with weakly bounding cochains.
Invariance of Lagrangian Floer theory under
Hamiltonian isotopy (specifically, the homotopy invariance of the A∞bimodule as-
sociated to a pair of Lagrangians) implies that ϕ′
0 admits a weakly bounding cochain
b′
0 and so that the objects (ϕ0, b0), (ϕ′
0, b′
0) are quasi-isomorphic in Fuk ˜ϕ0(X). That
is, there exist elements
(8)
α0 ∈CF(ϕ0, ϕ′
0),
β0 ∈CF(ϕ′
0, ϕ0),
δ0 ∈CF(ϕ0, ϕ0),
δ′
0 ∈CF(ϕ′
0, ϕ′
0)


## Page 9


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
9
so that
m
b0,b′
0
2
(α0, β0) −1ϕ0 = mb0
1 (δ0),
m
b′
0,b0
2
(β0, α0) −1ϕ′
0 = m
b′
0
1 (δ′
0).
It follows from the associativity of the composition law that
HF(ϕ0, b0) ∼= HF(ϕ′
0, b′
0).
We prove a similar theorem for the surgered immersion:
Theorem 1.6. Under the assumptions of Theorem 1.3, the objects (ϕϵ, bϵ) and
(ϕ′
0, b′
0) are quasi-isomorphic in Fuk ˜ϕϵ(X), and in particular their endomorphism
algebras have isomorphic cohomology algebras HF(ϕϵ, bϵ) ∼= HF(ϕ0, b0).
More generally, in any reasonable definition of the Fukaya category we expect
that (ϕ0, b0) and (ϕϵ, bϵ) are quasi-isomorphic. This would be the mirror statement
to invariance of the isomorphism class of the bundle under (deformed) Yang-Mills
heat flow.
Outline of proof.
The main result is an application of symplectic field theory
in the sense of Bourgeois-Eliashberg-Hofer-Wysocki-Zehnder [13]. We make use
of the neck-stretching limit for holomorphic disks along a sphere enclosing the
self-intersection point. In the limit, pseudoholomorphic maps limit to the pseudo-
holomorphic buildings. The levels of the buildings for the surgered and unsurgered
Lagrangians are the same except for those in a neighborhood of the self-intersection
point, and the main task is to analyze the holomorphic curves in the local model.
A similar argument was used in the proof of the special case by Fukaya-Oh-Ohta-
Ono, Chapter 10 of [31] describing the effect of surgery at an intersection point
of two Lagrangians in terms of a mapping cone. The setup requires substantial
groundwork. The definition and basic properties of surgery are described in Sec-
tion 2. The construction of a Fukaya algebra associated to an immersed Lagrangian
is recalled in Sections 3, 4, and 5, using a perturbation scheme which adapts that
in Cieliebak-Mohnke [22]. The details of the symplectic field theory argument are
carried out in Section 6. The holomorphic disks in the local model are classified
in Section 7. Details include showing that the standard complex structure in the
local model makes all holomorphic buildings regular, and the classification for the
standard handle applies to the “flattened handle” boundary condition which is
honestly cylindrical near infinity and for which the symplectic field theory results
apply. A key Lemma 7.19 describes the levels in the local model that can appear
with more than one strip-like end. Having identified a bijection between moduli
spaces defining the differential for the Lagrangian and its surgery, the isomorphism
of Floer cohomologies is carried out in Section 8, and in particular, Section 8.4
by identifying the complexes up to a stabilization. Section 9 proves various en-
hancements, such as the existence of a quasiisomorphism in the Fukaya category
between the objects defined by the Lagrangian and its surgery, which in particular
implies an isomorphism of Floer cohomologies as algebras. We also explain how


## Page 10


10
JOSEPH PALMER AND CHRIS WOODWARD
to obtain the result of Fukaya-Oh-Ohta-Ono’s Chapter 10 (equivalence of surgeries
with mapping cones) of [31], using the same arguments.
We thank Denis Auroux, Soham Chanda, John Man-Shun Ma, Dmitry Tonkonog,
Sushmita Venugopalan and Guangbo Xu for helpful discussions.
2. Lagrangian surgery
Lagrangian surgery was introduced by Lalonde-Sikorav [43] in dimension two
and Polterovich [51] for arbitrary dimension. Surgery smooths a self-intersection
point by removing small balls around the preimages of the self-intersection point
and gluing in a handle. Haug [34] introduced generalizations to handles of higher
index, which we do not consider here.
2.1. The local model. The local model for the surgery is obtained by parallel
transport of the vanishing cycle of the standard Lefschetz fibration along a line
parallel to the real axis, as explained in Seidel [58, Section 2e].
The standard
Lefschetz fibration is the map
(9)
π : Cn →C,
(z1, . . . , zn) 7→z2
1 + . . . + z2
n.
Equip Cn with the standard symplectic form ω ∈Ω2(Cn). The space Cn −{0} has
a natural connection given by a horizontal sub-bundle
T h
z ⊂Tz(Cn −{0}),
T h
z = (Ker Dzπ)ω
equal to the union of symplectic perpendiculars of the fibers π−1(z). For any path
γ : [0, 1] →C −{0}
there is a symplectic parallel transport map
Tγ : π−1(γ(0)) →π−1(γ(1))
by taking the endpoint of a horizontal lift of γ with any given initial condition.
Let γ : [0, 1] →C be an embedded path with endpoint γ(0) = 0 at the critical
point of the Lefschetz fibration. Each fiber of π over γ([0, 1]) has a vanishing cycle
Cz ⊂π−1(z) defined as the set of elements w ∈π−1(z) that limit to the origin
0 ∈Cn under symplectic parallel transport Cz →C0. If Sn−1 ⊂Rn ⊂Cn is the
unit sphere, then explicitly
Cz := √zSn−1,
z ∈C.
Now let γ : R →C be an embedded path (not necessarily with γ(0) = 0) so that
except for t in some compact interval [−c, c], we have
(10)
γ(t) = t + i2ϵ,
∀t /∈[−c, c].


## Page 11


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
11
For example, one could assume that the path is the affine linear path γ(t) = t+i2ϵ.
The handle Lagrangian Hγ is the union of vanishing cycles over γ:
Hγ :=
[
t∈R
Cγ(t).
As in [57, Discussion after (1.12)], Hγ may be equivalently defined as symplectic
parallel transport of Cz along γ.
More generally, as pointed out by Seidel [58, Section 2e], one may define surgery
by allowing more general paths in the base of the Lefschetz fibration. By bending
the path somewhat below the real axis one can achieve a zero-area surgery for which
holomorphic disks bounding the surgery have the same area as the corresponding
disks (as in Theorem 1.3) bounding the unsurgered Lagrangian. However, we will
only use the straight paths for the classification of disks in Section 7.
The handle has the following explicit description. Let Cn ∼= R2n be equipped
with Darboux coordinates
z = (z1, . . . , zn),
zk = qk + ipk,
k = 1, . . . , n.
For a real number ϵ with |ϵ| small define a Lagrangian submanifold Hϵ of Cn, the
handle of the surgery, by
(11)
Hϵ =
(
(q1 + ip1, . . . , qn + ipn) ∈Cn
 q ̸= 0, ∀k, pk = ϵqk
|q|2
)
.
Identify Cn = T ∨Rn in the standard way. Denote the standard symplectic form
ω0 =
n
X
k=1
dqk ∧dpk ∈Ω2(Cn).
Define
fϵ : Rn −{0} →R,
q 7→ϵ ln(|q|).
The Lagrangian Hϵ is the graph of the closed one-form dfϵ:
(12)
Hϵ = graph(dfϵ) ⊂R2n.
Also note that Hϵ ⊂Cn of (12) is invariant under the anti-symplectic involution
ι : Cn →Cn,
(p, q) 7→(q, p).
For the purposes of symplectic field theory, it is convenient to replace the above
Lagrangian with one that is cylindrical near infinity in the sense of Definition 6.7
rather than only asymptotically cylindrical. By the flattened handle we mean the
Lagrangian defined by parallel transport of a sphere along a path γ with γ(t) = t
for t outside of a compact neighbourhood of 0, and passing slightly above the
critical value 0 ∈C. An equivalent definition can be given explicitly as follows.
Define a Lagrangian submanifold ˇHϵ ⊂Cn equal to Hϵ in a compact neighborhood


## Page 12


12
JOSEPH PALMER AND CHRIS WOODWARD
of 0 and equal to Rn ∪iRn outside a larger compact neighborhood of 0. Following
Fukaya-Oh-Ohta-Ono [31, Chapter 10], let
ζ > 0,
ϵ ̸= 0
be constants. The constant ϵ is the surgery parameter describing the “size” of the
Lagrangian surgery, while the parameter ζ is a cutoff parameter describing the
size of the ball on whose complement the surgery ϕϵ agrees with the unsurgered
immersion ϕ0. These constants will be chosen later so that ζ is large and ζ|ϵ|1/2 is
small. Consider a function ρ given by a logarithm plus constant times a compactly-
supported cutoff function, namely
(13)
ρ ∈C∞(R>0),
ρ(r) =



ln(r) −|ϵ|
r ≤|ϵ|1/2ζ
ln(|ϵ|1/2ζ)
r ≥2|ϵ|1/2ζ
satisfying
∀r ∈R>0,
ρ′′(r) ≤0 ≤ρ′(r).
Define
(14)
ˇfϵ : Rn →R,
q 7→ϵρ(|q|).
Consider the graph
graph(d ˇfϵ) ⊂T ∨Rn ∼= R2n.
Let U ⊂X be a Darboux chart near x so that the self-intersection of ϕ at x has
the form (16). One realization of the flattened handle is the union of the graph of
the differential of ˇfϵ and its reflection:
(15) ˇHϵ =

graph(d ˇfϵ) ∩(Cn −B|ϵ|1/2ζ(0))

∪ι

graph(d ˇfϵ) ∩(Cn −B|ϵ|1/2ζ(0))

.
The inclusion
ˇϕϵ : ˇHϵ →U.
is then a Lagrangian embedding, with image equal to that of Rn ∪iRn outside of a
compact set.
A(ϵ)
Hϵ
ˇHϵ
H0
Figure 2. The local models


## Page 13


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
13
This explicit definition of the handle agrees with the previous one by parallel
transport. Indeed, since Hϵ projects to Im(z) = 2ϵ, the tangent space to THϵ
consists of a corank one sub-bundle T vHϵ := THϵ ∩Ker(Dπ) and the horizontal
lift of T({Im(z) = 2ϵ}). Hence Hϵ is obtained by symplectic parallel transport of
any fiber. The Lagrangian ˆHϵ defined in this way is cylindrical near infinity and
the argument of Proposition 2.2 (c) shows that after a change in surgery parameter
the two definitions are Hamiltonian isotopic.
2.2. Surgery and its properties. The surgery of an immersed self-transverse
Lagrangian is obtained by gluing in the local model of the previous section. Let X
be a compact symplectic manifold. Let ϕ0 : L0 →X be a self-transverse Lagrangian
immersion with compact, connected domain L0. Let
x = ϕ0(x+) = ϕ0(x−),
x+ ̸= x−∈L0
be an intersection point. The local model for transverse Lagrangian self-intersections
(see for example Pozniak [52, Section 3.4] for the more general case of clean inter-
section) implies that there exist Darboux coordinates in an open ball U ⊂X of
x
q1, . . . , qn, p1, . . . , pn ∈C∞(U)
such that the two branches of ϕ0 meeting at x are defined by
(16)
L−= {p1 = . . . = pn = 0},
L+ = {q1 = . . . = qn = 0}.
Let V ⊂U be a subset so that H0 agrees with ˇHϵ outside of V .
Definition 2.1.
(a) The Lagrangian surgery of ϕ0 : L0 →X is the immersion
with domain Lϵ defined by replacing a neighborhood U ∩L0 of the self-
intersection points x−, x+ ∈L0 with an open subset U∩ˇHϵ of the cylindrical-
near-infinity local model ˇHϵ:
Lϵ =

(L0 −V ) ∪(U ∩ˇHϵ)

/ ∼
where ∼is the obvious identification of H0 with ˇHϵ on the complement of
V . The surgered immersion
ϕϵ : Lϵ →X,
ϕϵ = (ϕ0|L0−V ) ∪(ˇϕϵ| ˇHϵ∩U)
is defined by patching together the immersions ˇϕϵ of ˇHϵ ∩U →X and ϕ0
on Lϵ −V ∼= L0 −V →X.
(b) The area of the surgery is the integral
(17)
A(ϵ) =
Z
S v∗ω
of the symplectic form over a small holomorphic triangle v : S →X with
boundary in ϕ0(L0) ∪ϕϵ(Lϵ), as in Figure 2 and Equation (132) below.


## Page 14


14
JOSEPH PALMER AND CHRIS WOODWARD
Equivalently, by Stokes’ theorem, A(ϵ) is the difference of actions
A(ϵ) =
Z
R γ∗
0α −γ∗
ϵ α
given by the integral of the canonical one-form α over paths γ0, γϵ from ∞
in Rn to ∞in iRn along H0 and ˇHϵ in the local model; see the proof of
Lemma 7.3.
We collect some basic properties of the surgery, most of which will be used later.
See [51], [57], and [31, Chapter 10] for more details.
Proposition 2.2. Let ϕ0 : L0 →X be an immersed Lagrangian with transverse
ordered self-intersection point (x−, x+) ∈L2
0.
(a) (Orientation) If L0 is oriented and ϵ > 0 then there exists an orientation
on Lϵ that agrees with that on L0 in a complement of the handle ˇHϵ if and
only if the self-intersection x ∈L2
0 is odd.
(b) (Relative spin structure) Assuming x is odd, any relative spin structure on
ϕ0 : L0 →X and an isomorphism Spin(TL0)x−∼= Spin(TL0)x+ defines a
relative spin structure on the surgery ϕϵ : Lϵ →X.
(c) (Independence of choices) The exact isotopy class of the surgery ϕϵ is inde-
pendent of all choices, up to a change in surgery parameter ϵ.
Proof. Item (a) follows from the fact that the gluing maps on the ends of the handle
are homotopic to (t, v) 7→etv resp. (t, v) 7→ie−tv. These maps are orientation
preserving exactly if the intersection is odd5. For item (b), suppose a relative spin
structure is given as a relative Čech cocycle as in [67, Section 3]. Such a cocycle
consists of charts Uα, α ∈A for X indexed by some set A, corresponding charts
Vα ⊂ϕ−1(Uα) for L0, and transition functions defined as follows. For α, β ∈A let
Vαβ = Vα ∩Vβ,
resp. gαβ : Vαβ →SO(n)
denote the intersections of the charts for L0 resp. transition maps for the tangent
bundle TL0. A relative spin structure is a collection of lifts ˜gαβ and signs oαβγ
given by maps
˜gαβ : Vαβ →Spin(n),
oαβγ : Uα ∩Uβ ∩Uγ →{±1}
such that the following relative cocycle condition holds:
˜gαβ˜g−1
αγ ˜gβγ = ϕ∗oαβγ,
∀α, β, γ ∈A.
5Recall that the self-intersection is odd if in the local model L0 in a neighborhood of x−
resp. x+ in L0 is identified with Rn with the standard orientation induced by the volume form
dq1 ∧. . . ∧dqn resp. iRn with the opposite orientation −dp1 ∧. . . ∧dpn. Reversing the sign of ϵ
changes the order of the branches, and so changes the parity of the self-intersection if and only if
dim(L0) is odd. Thus in the case that dim(L0) is odd, there is always some choice of sign of ϵ for
which the oriented surgery exists regardless of the parity of x = (x−, x+). On the other hand, if
dim(L0) is even then either both surgeries exist as oriented surgeries or neither.


## Page 15


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
15
To obtain the relative spin structure on the surgery Lϵ we take the cover on the
surgery with a single additional open set on the handle U0 := Hϵ with no triple
intersections. The relative spin structure is defined by transition maps near the
handle ˜g0α = ˜g0β = Id .
A more precise reformulation of the independence in item (c) is the following:
Let U 1, U 2 ⊂X and ˇH1
ϵ1, ˇH2
ϵ2 ⊂Cn be two sets of such choices and
ϕ1
ϵ1 : L1
ϵ1 →X,
ϕ2
ϵ2 : L2
ϵ2 →X
the corresponding families of surgeries for parameters ϵ1, ϵ2. We claim that for any
ϵ1 ∈R with |ϵ1| small there exists ϵ2 ∈R so that ϕ1
ϵ1 is an exact deformation of
ϕ2
ϵ2. In particular if both ϕ1
ϵ1 and ϕ2
ϵ2 are embeddings then ϕ2
ϵ2(Lϵ2) is Hamiltonian
isotopic to ϕ1
ϵ1(Lϵ1). To prove this claim, recall that any Lagrangian ϕ′
ϵ : Lϵ →X
nearby a given one is a graph of a one form ϕ′
ϵ = graph(α) for some α ∈Ω1(Lϵ) and
local model T ∨Lϵ ⊃U →X. An exact deformation is one generated by exact one-
forms, as in the terminology of Weinstein [68]. Exact deformations are equivalent
to deformation by Hamiltonian diffeomorphisms in the embedded case, but not in
general. Any two Darboux charts are isotopic after shrinking, by Moser’s argument.
The approximations ˇHϵ are also independent up to isotopy of the choice of cutoff
function. Therefore, any two choices of surgery are isotopic through Lagrangian
immersions ϕt
ϵ : Lϵ →X. In particular, the infinitesimal deformation
d
dtϕt
ϵ is given
by a closed one-form αt
ϵ ∈Ω1(Lϵ).
The deformation may be taken to be exact by varying the surgery parameter, as
follows. If n = 2 then the integral of αt
ϵ on the additional generator corresponding
to the meridian is, by Stokes’ theorem, the evaluation of the relative symplectic
class [ω] ∈H2(C2, ˇHϵ) on the generator in H2(C2, ˇHϵ). Such a generator is given
by a disk u : S →X, S = {|z| ≤1} with boundary u(∂S) on the meridian S1 ×{0}
of the handle. The disk u may be deformed to a disk u0 : S →X taking values
in R2, and so has vanishing area A(u) = A(u0) = 0. Returning to the case of
arbitrary n ≥2, the action
R
R γ∗
ϵ α along a longitude γϵ : R →ˇHϵ takes on all
positive values near 0 as ϵ varies. It follows that for any such ϕt
ϵ, t ∈[0, 1] there
exists a family ϵ(t), ϵ(0) = ϵ such that the deformation is given by an exact form.
Compare Sheridan-Smith [61, Section 2.6].
□
Remark 2.3. (Gradings) By Seidel [58], absolute gradings on Floer cohomology
groups are provided by gradings of the Lagrangians: Given a positive integer N,
an N-grading of a Lagrangian L is a lift of the natural map
L →Lag(TX),
x 7→TxL
from L to the bundle of Lagrangian subspaces Lag(TX) to an N-fold Maslov cover
LagN(TX) →Lag(TX).


## Page 16


16
JOSEPH PALMER AND CHRIS WOODWARD
If L0 is graded by a map ˜ϕ0 : L0 →LagN(X) and the self-intersection point has
degree 1 then ϕϵ : Lϵ →X is graded [58, Section 2e].
Remark 2.4. (Brane structures) A brane structure for ϕ0 consists of an orientation,
relative spin structure, and Λ0-valued local system y ∈R(ϕ0). For any holomorphic
treed disk u : C →X the holonomy of the local system around the boundary is
denoted by
y(∂u) ∈Λ0,
y : π1(ϕ(L)) →Λ0.
Any local system on ϕ0 induces a local system on ϕϵ, trivial on the handle, by
identifying the local system on the handle with the fiber of the local system over
the self-intersection point. Remark 2.3 and Proposition 2.2 imply that any brane
structure on ϕ0 induces a (Z2-graded) brane structure on ϕϵ.
3. Treed holomorphic disks
We recall the construction of a strictly unital A∞algebra from Charest-Woodward
[18, Theorem 4.1] and Palmer-Woodward [49, Theorem 6.2].
3.1. Treed disks. As usual in symplectic topology we require terminology for
stable disks and related concepts. A disk will mean a 2-manifold-with-boundary S
equipped with a complex structure so that the surface S is biholomorphic to the
closed unit disk {z ∈C | |z| ≤1}. A sphere will mean a complex one-manifold S
biholomorphic to the complex projective line P1 = {[ζ0 : ζ1] | ζ0, ζ1 ∈C}. A nodal
disk S is a union
S =
 n[
i=1
S ,i
!
∪
 n[
i=1
S ,i
! 
∼
of a finite number of disks S ,i, i = 1, . . . , n and spheres S ,i, i = 1, . . . , n identified
at pairs of distinct points called nodes w1, . . . , wm. Each node
we = (w−
e , w+
e ) ∈Si−(e) × Si+(e)
is a pair of distinct points (either both interior or both boundary points) where
Si±(e) are the (disk or sphere) components adjacent to the node; the resulting
topological space S is required to be simply-connected and the boundary ∂S is
required to be connected. The complex structures on the disks S ,i and spheres S ,i
induce a complex structure on the tangent bundle TS (which is a vector bundle
except at the nodal points) denoted j : TS →TS. A boundary resp. interior
marking of a nodal disk S is an ordered collection of non-nodal points
(18)
z = (z0, . . . , zd) ∈∂Sd+1
resp.
z′ = (z′
1, . . . , z′
c) ∈int(S)c
on the boundary resp. interior, whose ordering is compatible with the orientation
on the boundary ∂S. The combinatorial type Γ(S) is the graph whose vertices,
edges, and head and tail maps
(Vert(Γ(S)), Edge(Γ(S))), (h × t) : Edge(Γ(S)) →Vert(Γ(S)) ∪{∞}


## Page 17


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
17
are obtained by setting Vert(Γ(S)) to be the set of disk and sphere components
and Edge(Γ(S)) the set of nodes (each connected to the vertices corresponding to
the disks or spheres they connect). The graph Γ(S) is required to be a tree, which
means that Γ is connected with no cycles among the combinatorially finite edges;
each edge e ∈Edge(Γ(S)) is oriented so that it points towards the outgoing leaf
e0 ∈Edge(Γ(S)) corresponding to the marking z0. An edge e is combinatorially
finite if neither of its ends are at infinity. The set of edges Edge(Γ(S)) is equipped
with a partition into subsets Edge (Γ(S)) ∪Edge (Γ(S)) corresponding to interior
resp. boundary markings respectively. The set of boundary edges (h−1(v)∪t−1(v))∩
Edge (Γ(S)) meeting some vertex v ∈Vert(Γ(S)) is equipped with a cyclic ordering
giving Γ(S) the partial structure of a ribbon graph. Define
Edge→(Γ(S))
:=
h−1(∞) ∪t−1(∞)
Edge ,→(Γ(S))
:=
Edge (Γ(S)) ∩Edge→(Γ(S))
Edge ,→(Γ(S))
:=
Edge (Γ(S)) ∩Edge→(Γ(S))
The sets Edge ,→(Γ(S)), Edge ,→(Γ(S)) of boundary and interior semi-infinite edges
are each equipped with an ordering; these orderings will be omitted from the no-
tation to save space. A marked disk (S, z, z′) is stable if it admits no non-trivial
automorphisms φ : S →S preserving the markings z, z′. The moduli space of sta-
ble disks with fixed number d ≥3 of boundary markings and no interior markings
admits a natural structure of a cell complex which identifies the moduli space with
Stasheff’s associahedron.
Treed disks are defined by replacing nodes with broken segments as in the pearly
trajectories of Biran-Cornea [12] and Seidel [60]. A segment will mean a closed
one-manifold with boundary homeomorphic to a connected closed subset of the
real line. Given two such subsets Te,1, Te,2, one with a non-compact end at infinity
and another with a non-compact end at infinity we may form a new closed manifold
(19)
Te = Te,1 ∪{∞} ∪Te,2
by gluing along the infinite ends, which we call a singly-broken segment; the point
{∞} is called a breaking; repeating the gluing process gives a (multiply) broken
segment.
A treed disk is a topological space C obtained from a nodal disk S
by replacing each boundary node or boundary marking corresponding to an edge
e ∈Γ(S) with a (possibly broken) segment Te. Each such segment Te is naturally
equipped with a length
ℓ(e) ∈R≥0 ∪{∞}
where the semi-infinite edges e ∈Γ(S) are automatically assigned infinite length. A
treed disk C may be written as a union C = S ∪T where the one-dimensional part
T is joined to the two-dimensional part S at a finite set of points on the boundary
of S, called the nodes w ∈C of the treed disk (as they correspond to the nodes in
the underlying nodal disk.) The semi-infinite edges e in the one-dimensional part


## Page 18


18
JOSEPH PALMER AND CHRIS WOODWARD
T are oriented by requiring that the root edge e0 is outgoing while the remaining
leaves e1, . . . , ed are incoming; the outgoing leaf e0 is referred to as the root while
the other semi-infinite edges e1, . . . , ed are leaves.
In particular, we have the following gluing construction which produces treed
disks from a pair of treed disks. Given treed disks C1, C2 and and a leaf Te2 of C2
one may glue together C1 and C2 by identifying the point at infinity along the root
edge Te1 of C1 with the point at infinity for an incoming leaf of C2, creating a treed
disk
(20)
C = C1 ∪{∞} ∪C2,
Te := Te1 ∪{∞} ∪Te2
with a broken edge Te ⊂C. We say that the treed disks C1, C2 are obtained from
C by cutting along e. The combinatorial type
Γ(C) = (Vert(Γ(C)), Edge(Γ(C)))
of a treed disk C is defined similarly to that for disks with the following addition:
The set of edges Edge(Γ(C)) is equipped with a partition
Edge(Γ(C)) = Edge0(Γ(C)) ∪Edge(0,∞)(Γ(C)) ∪Edge∞(Γ(C))
indicating whether the length is zero, finite and non-zero, or infinite.
The space of isomorphism classes of treed disks satisfying a stability condition is
compact and Hausdorff with a universal curve. A treed disk C = S ∪T is stable if
the underlying nodal disk obtained by collapsing edges Te ⊂T to points is stable.
An example of a treed disk with one broken edge (indicated by a small hash through
the edge) is shown in Figure 3. In the Figure, the interior leaves e ∈Edge (Γ) are
not shown and only their attaching points we ∈S ∩T are depicted so as not to
clutter the figure. For a given combinatorial type Γ, denote by MΓ the moduli
Figure 3. A treed disk with d = 2 incoming boundary edges


## Page 19


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
19
space of treed disks whose domains have combinatorial type Γ and
Md = ∪ΓMΓ
the union over stable types Γ with d leaves. The moduli space Md is a compact
Hausdorff space which admits locally finite decomposition into smooth submani-
folds. It admits a universal curve Ud, given as the space of isomorphism classes of
pairs [C, z] where C is a holomorphic treed disk and z ∈C is any point, either in
S or T. The two cases correspond to a splitting
(21)
Ud = Sd ∪T d
of the universal treed disk into one-dimensional and two-dimensional parts T d resp.
Sd where the fibers of T d →Md resp. Sd →Md are one resp. two-dimensional.
Denote by SΓ resp. TΓ the surface resp. tree parts of the universal treed disk living
over MΓ, and similarly their closures SΓ, T Γ over MΓ. If for some types Γ′, Γ the
moduli space MΓ′ is contained in MΓ then we write Γ′ ⪯Γ.
3.2. Treed holomorphic disks. Treed holomorphic disks for immersed Lagrangians
are defined as in the embedded case, but requiring a double cover of the tree parts
to obtain the boundary lift. Recall that a Morse-Smale pair on L is a pair (f, g)
consisting of a Morse function and Riemannian metric
f : L →R,
g : TL ×L TL →R
so that the stable and unstable manifolds of (f, g) meet transversally. Any Morse-
Smale pair on L gives rise (somewhat non-canonically) to a cellular decomposition
whose cellular chain complex is equal to the Morse chain complex of L (see for
example [7, Theorem 4.9.3]). The Morse function f induces a Morse function ˜f on
the fiber product
L ×ϕ L ∼= L ∪Isi(ϕ),
by setting ˜f to equal f on L and any function on the discrete set Isi(ϕ). Let
J : TX →TX be an almost complex structure compatible with the symplectic
form ω ∈Ω2(X). We will assume that J is adapted to the local intersections of
ϕ : L →X in the following sense: For any self-intersection there is a Darboux
chart on U ⊂X as in (16) so that
L ∩U ∼= Rn ∪iRn
and J is given by the standard complex structure on U ⊂Cn.
A holomorphic treed disk consists of a map from treed disk together with a lift
of the map on the boundary to the Lagrangian. Since our Lagrangians are only
immersed, the domain of the boundary map is a one-manifold with boundary as
follows: Given a treed disk C = S ∪T, denote by
(22)
g
∂S = (∂S −((∂S) ∩T)) ∪{w<, w> ∈(∂S) ∩T}


## Page 20


20
JOSEPH PALMER AND CHRIS WOODWARD
the compact one-manifold obtained by replacing each element w of ∂S ∩T with
a pair of points w<, w> lying in the closure of the component of the boundary
∂S −(∂S)∩T which lies before resp. after the intersection point. Each component
of the boundary (∂S)i ⊂∂S −T has closure in g
∂S that is homeomorphic to a
closed interval. Let
ι : g
∂S →S
denote the canonical map that is generically 1 −1 except for the fibers over the
intersection points S ∩T which are 2 −1. Let
g
∂C = (g
∂S ∪T ∪T)/ ∼
denote the union of g
∂S with two copies of each edge, with the endpoints of the
edges identified with the two inverse images of the intersection points. Consider a
pair of maps
u : C →X,
∂u : g
∂C →L
so that
(23)
u ◦ι = ϕ ◦∂u.
We introduce the following notation for vector fields. Let Vect(X) denote the space
of vector fields on X, and let Vecth(X) ⊂Vect(X) denote the subset of Hamiltonian
vector fields. For any subset U ⊂X, let
(24)
Vecth(X, U) ⊂Vect(X)
be the space of Hamiltonian vector fields vanishing on U ⊂X. Let
H ∈Ω1(S, Vecth(X))
be a one-form with values in Hamiltonian vector fields supported in the interior of
S. Denote by
dHu = du −H ◦u ∈Ω1(S, u∗TX)
the Hamiltonian-perturbed exterior derivative.
Definition 3.1. A (J, H)-holomorphic treed disk with boundary in ϕ : L →X of
type Γ consists of a treed disk C = S ∪T of type Γ and continuous maps
u : C →X,
∂u : g
∂C →L
satisfying the matching condition (23) and
(a) the map u is smooth and (J, H)-holomorphic on S −(S ∩T), that is,
(25)
JdH(u|S) = dH(u|S)j
(b) the restriction of ∂u to eT := T ∪T ⊂eC is smooth and a gradient trajectory
for the given Morse function ˜f on L ×ϕ L, that is, a gradient trajectory for
f on the locus in T ∪T giving a map to L, and a constant map on the
self-intersection points.


## Page 21


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
21
The definition can be rephrased in terms of a matching condition at the endpoints
of the edges. For each edge Te adjacent to components Sv± with intersection points
{w+, w−} = Te ∩S, if the edge Te maps to L ⊂L ×ϕ L then the endpoints
u(w+), u(w−) are related by the gradient flow determined by the length of Te, while
if the edge Te maps to a self-intersection point then the endpoints u(w+), u(w−)
are equal. We denote a treed disk by (C, u : C →X), omitting ∂u to save space.
An isomorphism between treed disks (C, u : C →X) and (C′, u : C′ →X) is an
isomorphism of treed disks ψ : C →C′ so that u′ ◦ψ = u.
A compactified moduli space for any type is obtained after imposing a stability
condition.
Definition 3.2. A holomorphic treed disk (C, u : C →X) is stable if it has no
non-trivial automorphisms ψ : C →C, or equivalently
(a) each disk component Sv ⊂S, v ∈Vert (Γ) on which the map u is constant
(that is, a ghost disk bubble) has at least one interior node we ∈int(Sv) or
has at least three boundary nodes we ∈∂Sv;
(b) each sphere component Sv ⊂S, v ∈Vert (Γ) on which the map u is constant
(that is, a ghost sphere bubble) has at least three nodes we ∈∂Sv; and
(c) on each possibly broken edge Te with components Te,i as in (19) if Te,i has
two infinite ends then the map u|Te,i is non-constant.
The combinatorial data of a treed holomorphic disk is packaged into a labeled
graph called the combinatorial type:
Definition 3.3. For a holomorphic treed disk u : C →X the combinatorial type
Γ of u is the combinatorial type Γ of the underlying treed disk C together with
the labelling of vertices v ∈Vert(Γ) corresponding to sphere and disk components
Sv, v ∈Vert(Γ) by the (relative) homology classes
u∗[Sv] ∈H2(X) ∪H2(X, ϕ(L))
and the labelling
t(e) ∈{1, 2}
of edges e ∈Edge(Γ) by their branch type (whether they represent a branch change
of the map ∂u : g
∂S →ϕ(L) or not). The total homology class of a type Γ of positive
area is called primitive if it is not the sum of homology classes of types Γ1, Γ2 of
smaller positive area. We write Γ 7→Γ if Γ is the domain type of a map type Γ.
For any combinatorial type of map Γ denote by MΓ(ϕ) the moduli space of stable
treed holomorphic disks bounding ϕ of type Γ. Denote by
MΓ(ϕ) =
[
Γ7→Γ
MΓ(ϕ)


## Page 22


22
JOSEPH PALMER AND CHRIS WOODWARD
the union of strata of stable map type Γ with domain type Γ and
Md(ϕ) =
[
Γ
MΓ(ϕ)
the union over combinatorial types with d incoming edges. The case that C consists
of a single edge so that S = ∅and T = R is allowed; in this case MΓ(ϕ) is defined
to be the space of non-constant unparametrized gradient trajectories on L.
Each stratum is cut out by a Fredholm map of Banach spaces as explained in
Palmer-Woodward [49]. Since later we will have to generalize the discussion to
buildings, we review the construction. Let u : S →X be a map of type Γ. Let
S◦= S −{w ∈S ∩Te, t(e) = 2}
(where t(e) was the number of branches of the map u on the edge e defined in 3.3)
denote the complement of the points w ∈S ∩T representing branch changes of the
map ∂u : g
∂S →L. The surface S◦is naturally a surface with strip-like ends: For
each w ∈S ∩Te above there exists a proper embedding of manifolds with boundary
ϵw : R>0 × [0, 1] →S◦,
lim
s→∞ϵw(s, t) = w,
∀t ∈[0, 1]
such that the complex structure on S pulls back to the standard complex structure
in the coordinates s, t. For a Sobolev exponent p ≥2 and Sobolev differentiability
constant k ≥1 with kp > 2 , let
Mapk,p(S◦, X) = {u = expu0(ξ),
ξ ∈Ω0(S◦, TX)k,p}
denote the space of continuous maps u : S◦→X of the form u = expu0(ξ) where
u0 is constant in a neighborhood of infinity along the strip-like ends and ξ ∈
Ω0(S◦, TX)k,p has finite W k,p norm. In particular, ξ has k covariant derivatives
in Lp using a connection on X and a metric on S◦that is of product form on the
ends. For each branched edge e, let
w±(e) ∈∂S ∩T
denote the points at the end of each finite edge Te ⊂T (distinguished by requiring
that with the given orientation of Te, the segment Te points from w−(e) to w+(e))
Let δt : L →L be the time t gradient flow of f, for t ≥0. Let T1 resp. T2 ⊂T
be the locus on which u is unbranched resp. branched and Edge1(Γ), Edge2(Γ) the
corresponding subsets of edges. Define
(26)
BΓ
=





(C, u, ∂u, l) ∈

MΓ(ϕ) × Mapk,p(S◦, X) so
u ◦ι = ϕ ◦∂u, u(we,+) = δℓ(e)(u(we,−)), ∀e ∈Edge1(Γ),
u(we,−) = u(we,+) ∀e ∈Edge2(Γ)




.
Boundary values of W k,p maps lie in W k−1/p,p (see [44, (0.15)]). Maps close to any
given pair (u, ∂u) are exponentials expu(ξ), exp∂u(∂ξ) of sections
ξ ∈Ω0(S◦, u∗TX)k,p,
∂ξ ∈Ω0(∂S◦, (∂u)∗TL)k−1/p,p,


## Page 23


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
23
where the subscript denotes Sobolev class W k,p, satisfying
ξ ◦ι = Dϕ ◦∂ξ.
Here exponentiation means geodesic exponentiation using, for example, a metric
on X for which each branch of ϕ(L) is totally geodesic. The fiber of the bundle EΓ
over some map u is the vector space of one-forms
(27)
EΓ,u := Ω0,1(S, u∗
STX)k−1,p.
Local charts are provided by almost complex parallel transport
(28)
T ξ
u : Ω0,1(S◦, expu(ξ)∗TX)k−1,p →Ω0,1(S◦, u∗TX)k−1,p
along expu(sξ) for s ∈[0, 1]; note here that the connection used for parallel trans-
port T ξ
u need not be related to the metric used for geodesic exponentiation. In
any local trivialization of the universal curve, one can obtain Banach bundles with
arbitrarily high regularity. Let
(29)
Ui
Γ →Mi
Γ × C
be a collection of local trivializations of the universal curve. Let Bi
Γ denote the
inverse image of Mi
Γ in BΓ and Ei
Γ its preimage in EΓ. The Fredholm map cutting
out the moduli space over Mi
Γ is
(30)
Fi
Γ : Bi
Γ →Ei
Γ,
u 7→∂J,Hu
The linearization of the map (30) cutting out the moduli space is a combination of
the standard linearization of the Cauchy-Riemann operator with additional terms
arising from the variation of conformal structure. With k, p integers determining
the Sobolev class as above let
Du : Ω0(S◦, u∗TX, (∂u)∗TL)k,p →Ω0,1(S◦, u∗TX)k−1,p
ξ 7→∇0,1
H ξ −1
2(∇ξJ)J∂J,Hu
(31)
denote the linearization of the Cauchy-Riemann operator, cf. McDuff-Salamon [45,
p. 276]; here
∂J,Hu = 1
2(dHu −JdHuj).
The complex structures on the fibers induce a family
(32)
Mi
Γ →J (S),
m 7→j(m)
of complex structures on the two-dimensional locus S ⊂C, and In particular, any
tangent vector ζ ∈TMi
Γ induces a variation Dj : TS →TS of complex structure
on S: Let
Ω0(S◦, ∂S◦; u∗
STX; (∂u)∗TL)k,p ⊂Ω0(S◦; u∗
STX)k,p


## Page 24


24
JOSEPH PALMER AND CHRIS WOODWARD
denote the subspace of sections ξ whose boundary values lift to W k−1/p,p-sections
∂ξ with values in (∂u)∗TL. The tangent space to BΓ is the space of deformations
(ζS, ζT, ξ) preserving the matching conditions given by
T(C,u)BΓ =
(
(ζS, ζT, ξ)

(ξ(we,+) = Dδℓ(e)(ξ(we,−), ζT(e))
∀e ∈Edge1(Γ)
)
where δ(l, t) := δt(l) is the cellular approximation. The linearized operator for the
map u is given by the expression
(33)
˜Du : T(C,u)BΓ →Ω0,1(S◦, ∂S◦; u∗TX)k−1,p
(ζS, ζT, ξ) 7→

Duξ + 1
2JduDj(ζS)

.
A holomorphic treed disk u : C →X with stable domain C is
regular if the linearized operator ˜Du is surjective;
stratum-wise rigid if u is regular and ˜Du is surjective and the kernel of ˜Du
is generated by the infinitesimal automorphism aut(S) of S; and
rigid if u is stratum-wise rigid and the domain C lies in a top-dimensional
stratum MΓ in the moduli space of domains Md.
The moduli space of holomorphic treed disks admits a natural version of the
Gromov topology which allows bubbling off spheres, disks, and cellular boundaries.
For Hamiltonian-perturbed maps, the Hamiltonian-perturbed energy is
(34)
E(u) = 1
2
Z
S ∥dHu∥2d VolS
where d VolS is the area density on the surface S. The area of a map type Γ is
the sum of the pairings of the homology classes of the disk and sphere components
u∗[Sv] with the symplectic class [ω]. The energy E(u) is equal to the area A(u) up
to a curvature term explained in [45, Chapter 8]. Consider a sequence
uν : Cν →X,
∂uν : g
∂Cν →L,
ν ∈N
of treed holomorphic disks with boundary in ϕ with bounded energy E(uν) > 0.
Gromov compactness with Lagrangian boundary conditions as in, for example,
Frauenfelder-Zemisch [30, Theorem 1.1] implies that there exists a subsequence
with a stable limit
(C, u : C →X) := lim
ν→∞(Cν, uν : Cν →X).
Standard arguments using local distance functions as in McDuff-Salamon [45, Sec-
tion 5.5] then show that for any fixed energy bound E > 0, the subset
(35)
M
<E
d (ϕ) =
n
u ∈Md(ϕ)
 E(u) < E
o


## Page 25


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
25
satisfying the given energy bound E(u) < E is compact and Hausdorff.
The moduli space further decomposes according to the limits at infinity and the
expected dimension. For conceptual reasons, we index the generators by the cells
rather than critical points of the Morse function. That is, for any x ∈crit(f) let
σ(x) ⊂L denote the corresponding unstable manifold in the cellular decomposition
defined by f. Define
I(ϕ) = Ic(ϕ) ∪Isi(ϕ)
where
Ic(ϕ) := {σ(x), x ∈crit(f)}
is the set of cells; and
Isi(ϕ) := (L ×ϕ L) −∆L
is the set of ordered self-intersection points, where L ×ϕ L is the fiber product and
∆L ⊂L2 the diagonal. For some collection of cells σ0, σ1, . . . , σd ∈I(ϕ) denote by
M(ϕ, σ) =
n
[C, u : C →X] ∈Md(ϕ)

eve(u) ∈σe ∀e ∈Edge(Γ)
o
the locus of maps such that the limit, denoted eve(u), of u at infinity of the re-
striction of the map to the edge Te is the corresponding critical point of the Morse
function, so that a neighborhood of infinity maps to σe. We consider the case of
no disks in the configuration as a special case. Let
σ−∈Ic(ϕ),
σ+ ∈Ic,∨(ϕ),
deg(σ+) = deg(σ−) + 1.
For any integer d denote by
(36)
MΓ(ϕ, σ)d =
(
[C, u : C →X]
 Ind( ˜Du) −
d
X
i=0
|σi| = d
)
the locus with expected dimension d, where ˜Du is the operator of (33) and |σi| is the
codimension of the constraint σi for i = 0, . . . , d. An element of MΓ(ϕ, σ) is rigid
if it lies in the locus MΓ(ϕ, σ)0 of expected dimension zero and MΓ is codimension
zero in Md. A labeled type of map is the map type Γ with a labelling σ of its edges.
A labeled map type Γ is rigid if any (and so all) maps (C, u : C →X) of labeled
type Γ are rigid.
4. Coherent perturbations
Regularization of the moduli spaces is achieved through domain-dependent per-
turbations, using a Donaldson hypersurface [25] to stabilize the domains as in
Cieliebak-Mohnke [22].


## Page 26


26
JOSEPH PALMER AND CHRIS WOODWARD
4.1. Donaldson hypersurfaces.
Definition 4.1. A Donaldson hypersurface of a compact symplectic manifold X is
a codimension two symplectic submanifold D ⊂X representing a multiple k[ω], k >
0, of the symplectic class [ω] ∈H2(X). The integer k is the degree of D.
A relative Donaldson hypersurface for a Lagrangian immersion ϕ : L →X is a
codimension two symplectic submanifold D ⊂X disjoint from ϕ(L) representing a
multiple k[ω], k > 0, of the symplectic class [ω] ∈H2(ϕ).
Donaldson’s construction in [25] associates to any asymptotically holomorphic
sequence of sections sk of tensor powers ˆXk of a line bundle ˆX →X with first
Chern class c1( ˆX) = [ω] a sequence of hypersurfaces Dk = s−1
k (0); for k suffi-
ciently large the submanifold Dk is a Donaldson hypersurface. A result of Au-
roux [8] provides a homotopy between any two such choices with the same de-
gree. Results of Auroux-Gayet-Mohsen [11] show the existence of Donaldson hy-
persurfaces in the complement of an isotropic submanifold, and a result of Au-
roux included in Pascaleff–Tonkonog [50, Theorem 3.1] extends this to the case
of cleanly-intersecting Lagrangians satisfying the Bohr-Sommerfeld condition that
the pull-back bundle ϕ∗( ˆXk →X) is trivial for some k. As in [50, Corollary 3.4]
one may assume the Lagrangian to be exact in the complement by choosing the
approximately holomorphic section defining the Donaldson hypersurface to be flat
on the Lagrangian. Then Stokes’ theorem implies that k times the area A(u) of
any disk u : C →X bounding L is given by its intersection number ⟨[u], [D]⟩with
D. Equivalently, D represents [ω] in the relative cohomology group H2(ϕ).
As explained in Cieliebak-Mohnke [22], the set of intersections of a holomorphic
curve with a Donaldson hypersurface provides an additional set of marked points
that stabilize the domain.
Let D ⊂X be a Donaldson hypersurface.
We say
a compatible almost complex structure JD ∈J (X) is stabilizing if J preserves
TD, a compatible almost complex structure preserving D so that D contains no
non-constant holomorphic spheres as in Cieliebak-Mohnke [22, Section 8], and each
non-constant JD-holomorphic sphere u : P1 →X of energy at most E intersects D
in finitely many but at least three points u−1(D). 6
Lemma 4.2. [22, Section 8] Suppose D has sufficiently large degree k ≫0. Then
any generic almost complex structure JD preserving D is stabilizing, and for any
energy bound E > 0 there exist an open neighborhood J (X, JD, E) of JD consisting
of stabilizing almost complex structures.
We use the additional markings provided by the Donaldson hypersurface to define
domain-dependent perturbations. Choose an open neighborhood U of D. Recall
6In order to prove independence from all choices, [22] also consider tamed almost complex
structures.
However, in this paper we do not prove any independence results so compatible
almost complex structures suffice.


## Page 27


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
27
from (24) that Vecth(X, U) denotes the space of Hamiltonian vector fields v : X →
TX vanishing on U.
Definition 4.3. For each combinatorial type of domain Γ,
(a) a domain-dependent almost complex structure for Γ is a map
JΓ : SΓ →J (X, JD, E)
(notation from (21)) smooth as a map SΓ × TX →TX.
(b) A domain-dependent Hamiltonian perturbation for Γ is a one-form
HΓ ∈Ω1(SΓ, Vecth(X, U))
smooth as a map TSΓ × X →TX.
(c) A single-valued domain-dependent matching condition for Γ is a map
MΓ : (SΓ ∩T Γ) × L →L
such that MΓ(we, ·) is a diffeomorphism of L for each we ∈SΓ ∩T Γ.
(d) A perturbation datum is a datum
PΓ = (JΓ, HΓ, MΓ)
such that JΓ agrees with the given almost complex structure JD on the
hypersurface D and in a neighborhood of the nodes we ∈S and boundary
∂S for any fiber S ⊂SΓ, and takes values in the space of almost complex
structures without sphere bubbling J (X, JD, # Edge (Γ)/k) from Lemma
4.2. The space of PΓ of perturbation data is denoted
PΓ = {PΓ}.
To achieve certain symmetry properties of the Fukaya algebra, multi-valued per-
turbation data are required. For example, if one expects divisor insertions to con-
tribute exponentials to the disk potential then one expects the factorials to appear
as an averaging factor as in Theorem 5.13.
Definition 4.4.
(a) A multivalued domain-dependent matching condition for Γ
is a formal sum
(37)
MΓ =
k
X
i=1
ciMΓ,i
k
X
i=1
ci = 1
ci ∈[0, 1] ∀i
of single-valued matching conditions MΓ,i.
(b) Similarly, a multi-valued domain-dependent Hamiltonian is a formal sum
(38)
HΓ =
l
X
i=1
diHΓ,i
l
X
i=1
di = 1
di ∈[0, 1] ∀i
of single-valued Hamiltonian perturbations.


## Page 28


28
JOSEPH PALMER AND CHRIS WOODWARD
For much of the paper, one could assume that MΓ, HΓ are single-valued. However in
order to deal with repeated inputs one must allow formal sums, that is, multivalued
perturbations, as in Section 5.3.
Given perturbations, the perturbed moduli spaces are defined as follows.
Definition 4.5. For PΓ = (JΓ, HΓ, MΓ), a PΓ-perturbed treed holomorphic disk is
a pair (C, u : C →X) where C is of type Γ and the equation (25) is replaced with
the following conditions:
(a) The map u is perturbed holomorphic in the sense that
(39)
∂JΓ,HΓu(z) = 1
2
 
(du(z) −HΓ(u(z))
+JΓ(z, u(z))(du(z) −HΓ(u(z)))j(z))
!
= 0
on the surface S;
(b) for each unbranched interior edge e the perturbed matching condition
(40)
MΓ,i(w−(e), δℓ(e)u(w−(e))), MΓ,i(w+(e), u(w+(e)))) ∈∆
holds for some i; and for each leaf e labeled by a cell σe for some i we have
MΓ,i(we, u(we)) ∈σe;
(c) and the matching condition holds for each branched interior edge Te joining
points we,± ∈S ∩T:
u(we,−) = u(we,+).
The map is adapted if each connected component of u−1(D) contains an interior
node we ∈S, e ∈Edge (Γ) and each such we lies in u−1(D). This ends the Defini-
tion.
Remark 4.6. By Theorem 4.18 a generic adapted map u : C →X has the prop-
erty that every holomorphic disk component u|Sv meets D in finitely many points
u−1(D), and positively many points if the disk is non-constant. The definition
above, however, allows constant sphere components Sv mapping entirely to the
divisor D, which would therefore have infinitely many intersections.
The construction above naturally produces a collection of moduli spaces satisfy-
ing an energy gap condition:
Lemma 4.7. Let ϕ : L →X be a self-transverse Lagrangian immersion. There
exists an ℏ> 0 such that any treed holomorphic disk u : C →X with boundary on
ϕ containing at least one non-constant holomorphic component uv : Cv →X, duv ̸=
0, v ∈Vert(Γ) has area A(u) at least ℏ.
Proof. By Gromov compactness, for E > 0, the set of homotopy classes [u] ∈π2(ϕ)
of stable holomorphic disks u : S →X, S = {|z| ≤1} with energy bound E(u) <
E is finite. It follows that the set {A(u), du ̸= 0} of non-zero energies of disks


## Page 29


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
29
u : S →X bounding ϕ has a non-zero minimum min{A(u), du ̸= 0}, which we
may take to equal ℏ.
□
Our constructions produce Fukaya algebras over Novikov rings (with positive
valuation) rather than Novikov fields by use of the following:
Lemma 4.8. For a regular Hamiltonian perturbation HΓ that is sufficiently small
in the C∞topology, the areas A(u) of all rigid (JΓ, HΓ)-holomorphic treed disks
u : C →X are non-negative.
Proof. The areas of such configurations are topological quantities, that is, depend
only on the homotopy type of the map. The set of homotopy types [u] achieved
by holomorphic maps u : S →X is unchanged by the introduction of a pertur-
bation HΓ, by a standard argument using Gromov compactness. Any (JΓ, HΓ)-
holomorphic map may be written as a J′
Γ-holomorphic map for some almost com-
plex structure J′
Γ obtained by pulling back JΓ under a Hamiltonian flow as in [45,
Chapter 8]. Suppose that uν : Cν →X is a sequence of (JΓ, HΓ,ν)-holomorphic
treed disks with HΓ,ν converging to zero in C∞. After passing to a subsequence,
we may assume that the domain Cν converges to a limit C. By the energy-area
relation for Hamiltonian-perturbed maps, in particular the bound in [45, Remark
8.1.7], the energy of the sequence uν is bounded. By Gromov compactness (see
for example [45, Chapter 4], although a modification is necessary to adapt for the
varying domain) a subsequence of uν Gromov converges to a limiting stable JΓ-
holomorphic treed disk u : C →X with the same area. Since the Hamiltonian
perturbation HΓ,ν vanishes in the limit, the area is necessarily non-negative.
□
The combinatorial type of an adapted map is that of the map with the additional
data of a labelling i(e), e ∈Edge(Γ) of any interior node by intersection multiplicity
i(e) with the hypersurface D; let i(e) = 0 if the map u : S →X is constant with
values in the hypersurface D near we.
Denote the moduli space of D-adapted
treed holomorphic disks bounding ϕ of type domain type Γ with respect to the
perturbation PΓ by
MΓ(X, ϕ) ⊂
n
u : S →X
 ∂JΓ,HΓu = 0,
u(we) ∈D,
∀e ∈Edge (Γ)
o
.
Denote by
M(X, ϕ) = ∪ΓMΓ(X, ϕ)
the union over combinatorial types Γ. As before, we may further refine to a union
over map types
M(X, ϕ) = ∪ΓMΓ(X, ϕ).
4.2. Coherence. In order to obtain good compactness properties of the moduli
spaces of holomorphic curves, the following coherence properties of the perturba-
tions are required.


## Page 30


30
JOSEPH PALMER AND CHRIS WOODWARD
Definition 4.9. The perturbations P = (PΓ) are coherent if they satisfy the fol-
lowing axioms:
(Locality axiom) We require the following notation. Given a type Γ, for
each vertex v ∈Vert(Γ), let Γ(v) denote the subtree of Γ consisting of the
vertex v and all edges e of Γ meeting v. Let Γ denote the subgraph of Γ
whose vertices are those of open type v ∈Vert (Γ) and whose edges are
e ∈Edge (Γ). Let
π = π × πv : UΓ →MΓ × UΓ(v)
be the product of the maps where π is given by projection followed by
forgetful morphism and πv is the map S 7→Sv that collapses all components
other than Sv onto the corresponding special points of Sv.
The locality
property is the following: For each vertex v, the perturbation PΓ restricts
on Sv to the pull-back under π of some perturbation PΓ,v on MΓ × UΓ(v)
to UΓ. 7
(Cutting edges axiom) If Γ is obtained from types Γ1, Γ2 by gluing along
semi-infinite edges e of Γ1 and e′ of Γ2 as in (20) then let
π1 : MΓ →MΓ1,
π2 : MΓ →MΓ2
denote the projections obtained by mapping each curve C = C1∪e,e′C2 to C1
resp. C2. For the coherence axioms PΓ is the product of the perturbations
PΓ1, PΓ2 under the isomorphism UΓ ∼= π∗
1UΓ1 ∪π∗
2UΓ2.8
(Collapsing edges axiom) If Γ′ is obtained from Γ by setting a length equal to
zero or infinity, or collapsing an edge, then the restriction of PΓ to SΓ|MΓ′ ∼=
SΓ′ is equal to PΓ′.
Remark 4.10. (Forgetting markings on spheres) The locality axiom provides the fol-
lowing forgetful construction, which is a variation of the construction in Cieliebak-
Mohnke [22]: Suppose that C is a curve of type Γ containing a sphere component
Sv with more than one interior marking we ∈Sv. Forgetting all but one marking,
say we0 on Sv, and collapsing unstable components produces a marked curve f(C)
with type f(Γ) possibly with a component f(Sv) containing a single marking, as
in Figure 4. Define a perturbation datum f(PΓ) for f(Γ) by taking the almost
complex structure Jf(Γ) to equal the base almost complex structure JD on f(Sv),
7In other words, on each component Sv the perturbations only depend on the positions of the
special points on that component and the boundary edge lengths. This locality principle is used
later in Theorem 4.18 to rule out constant spheres with more than one marking, in the case of
zero and one-dimensional moduli spaces.
8That is, on any configuration with a broken edge, the perturbations on the components
separated by the broken edge depend only on the domains on that side of the edge, rather than
the domain on the other side. This property is necessary for the boundary description in Theorem
4.18, which in turn is used to prove the A∞axiom.


## Page 31


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
31
Type Γ
Type f(Γ)
Figure 4. The types Γ and f(Γ)
and the almost complex structures PΓ|f(C) −f(Sv) on the complement; while
the Hamiltonian perturbation HΓ and MΓ remains the same. If u : S →X is a
PΓ-holomorphic map constant on Sv, then one obtains an f(PΓ)-holomorphic map
on f(Sv) by forgetting all markings except we0 on Sv. Since each interior node
we, e ∈Edge (Γ) is required to map to the divisor D, the resulting type f(Γ) is the
same expected dimension as that of maps of type Γ.
Remark 4.11. The (Cutting edges) axiom implies the following relationship between
moduli spaces.
Suppose that the type Γ is obtained by gluing together types
Γ2 and Γ1 along a boundary edge. An element of MΓ(X, ϕ) consists of a pair
Ck = Sk ∪Tk, uk : Sk →X of treed holomorphic disks of combinatorial types
Γk for k ∈{1, 2}, glued together along some point at infinity along two of the
semi-infinite edges. Thus if i denotes the index of the incoming edge for Γ2 glued
at the outgoing edge of Γ1 and j + 1 the number of incoming edges of Γ2 the map
u 7→(u1, u2) defines a map
(41)
MΓ(X, ϕ, σ0, . . . , σd)0
→∪αMΓ1(X, ϕ, σ0, σ1, . . . , σi−1, α, σi+j+1, . . . , σd)0
× MΓ2(X, ϕ, α, σi, . . . , σi+j)0.
Obtaining strict units requires the addition of weightings to the combinatorial
types as in Ganatra [32, Section 10] and Charest-Woodward [18, Section 4]. When
the weighting of an edge is infinite, we will assume that the perturbation data
is pulled back under the forgetful map forgetting that edge and stabilizing. For
this reason, the edges where the weightings are forced to be infinite are called
forgettable.
Definition 4.12. A weighting of a treed disk C = S ∪T of type Γ is
(a) a partition of the boundary semi-infinite edges
Edgewt(Γ) ⊔Edgewt,∞(Γ) ⊔Edgewt,0(Γ) = Edge ,→(Γ)


## Page 32


32
JOSEPH PALMER AND CHRIS WOODWARD
into weighted resp. forgettable resp. unforgettable edges, and
(b) a map
ρ : Edge ,→(Γ) →[0, ∞]
satisfying the property: each of the semi-infinite e edges is assigned a weight
ρ(e) such that
ρ(e) ∈







{0}
e ∈Edgewt,0(Γ)
[0, ∞]
e ∈Edgewt(Γ)
{∞}
e ∈Edgewt,∞(Γ)
.
If the outgoing edge e0 ∈Edge→(Γ) is unweighted (forgettable or unforgettable)
then an isomorphism ψ : (C, ρ) →(C′, ρ′) of weighted treed disks is an iso-
morphism of treed disks C →C′ that preserves the types of semi-infinite edges
e ∈Edge→(Γ) ∼= Edge→(Γ′) and weightings: ρ(e) = ρ′(e′) for all corresponding
edges e ∈Edge ,→(Γ), e′ ∈Edge ,→(Γ′). This ends the Definition.
There is an additional notion of equivalence in the case that the outgoing edge
is weighted: If the outgoing edge e0 is weighted then an isomorphism of weighted
treed disks C →C′ is an isomorphism of treed disks preserving the types of semi-
infinite edges e ∈Edge ,→(Γ) and the weights ρ(e), e ∈Edge ,→(Γ) up to scalar
multiples:
(42)
∃λ ∈(0, ∞), ∀e ∈Edge ,→(Γ), e′ ∈Edge ,→(Γ′), ρ(e) = λρ′(e′).
In particular, any weighted tree T such that Vert(Γ) = ∅and a single edge
e ∈Edge ,→(Γ) that is weighted ρ(e) ∈(0, ∞) is isomorphic to any other such
configuration T ′ with a different weight ρ(e′) ∈(0, ∞), e′ ∈Edge(Γ′).
The combinatorial type of any weighted treed disk is the tree associated to the
underlying nodal disk with additional data recording which lengths resp. weights
are zero or infinite. Namely if C = S ∪T is a weighted treed disk then its combi-
natorial type is the tree Γ = Γ(C) obtained by gluing together the combinatorial
types Γ(Sv) of the disks Sv along the edges corresponding to the edges of T; and
equipped with the additional data of
(a) the subsets
Edgewt(Γ) resp. Edgewt,∞(Γ) resp. Edgewt,0(Γ) ⊂Edge ,→(Γ)
of weighted, resp. forgettable, resp. unforgettable semi-infinite edges;
(b) the subsets
Edge∞
−(Γ) resp. Edge0
−(Γ) resp. Edge(0,∞)
−
(Γ) ⊂Edge−(Γ)
of combinatorially finite edges of infinite resp. zero length resp. non-zero
finite length;
A well-behaved moduli space of weighted treed disks is obtained after imposing
a stability condition.


## Page 33


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
33
Definition 4.13. A weighted treed disk C = S ∪T of type Γ is stable if either
(a) there is at least one disk component Sv, v ∈Vert (Γ), and the following
conditions hold:
(i) each disk component Sv, v ∈Vert (Γ) has at least three edges e ∈
Edge(Γ) attached to the boundary ∂Sv or at least one edge attached
to the boundary ∂Sv and one edge to the interior int(Sv);
(ii) each sphere component Sv, v ∈Vert (Γ) has at least three edges e ∈
Edge(Γ) attached;
(iii) each combinatorially-finite edge e ∈Edge−(Γ) is broken at most once,
and each semi-infinite edge e ∈Edge→(Γ) is unbroken;
(iv) if the outgoing edge is weighted e0 ∈Edgewt(Γ) then at least one leaf
ei ∈Edge ,→(Γ), i > 0 is also weighted, that is, ei ∈Edgewt(Γ).
(b) if there are no disks, so that Vert(Γ) = ∅, there is a single weighted leaf
e1 ∈Edgewt(Γ) and an unweighted (forgettable or unforgettable) root e0 ∈
Edgewt,∞(Γ) ∪Edgewt,0(Γ).
This ends the Definition.
Because a configuration with no disks is allowed (namely an infinite interval)
the stability condition for weighted treed disks is not equivalent to the absence of
non-trivial automorphisms. The moduli space of weighted treed disks of some type
Γ is denoted Mwt
Γ . The natural map Mwt
Γ →MΓ forgetting the weightings is a
fiber bundle with each fiber the product of intervals for each leaf, so that as long
as there is one vertex,
(43)
Mwt
Γ ∼= MΓ × (0, ∞)# Edgewt(Γ)
where # Edgewt(Γ) is the number of weighted edges with weights in (0, 1); the case
of trees with no vertex is exceptional, since in this case both the incoming edge
may be weighted but the moduli space Mwt
Γ is still dimension zero, and there are
no stable strata MΓ.
A weighted treed holomorphic disk is a holomorphic treed disk with a weighting
on the underlying treed disk and the following restriction on leaf labels. Given a
non-constant pseudoholomorphic treed disk u : C →X with leaf ei for which the
weighting ρ(ei) = ∞resp. 0, we view u as obtained from gluing the pseudoholo-
morphic treed disk u′ : S →X obtained by attaching to ei a constant configuration
u′′ with weighted incoming e−
i and forgettable resp. unforgettable outgoing edge
e+
i . See Figure 5. Also, any two configurations u : S →X, u′ : S′ →X with an out-
going weighted edge e0 with the same underlying tree Γ are considered equivalent.
See Figure 6.
Remark 4.14. (Constant maps) If x1 = xh and x0 = xg resp. x0 = xs then the
moduli space M(L, x0, x1) contains a configuration with no disks and single edge
on which u is constant, corresponding to a weighted leaf e ∈Edgewt(Γ) and a root


## Page 34


34
JOSEPH PALMER AND CHRIS WOODWARD
ρ = ∞
ρ = ∞
Figure 5. Equivalent weighted treed disks
xh
xh
xs
ρ1
ρ1
xh
xh
xs
xh
ρ2
ρ2
ρ = ∞
xg
xg
xh
ρ = ∞
xg
xg
Figure 6. Equivalent weighted treed disks, ctd.
edge e0 ∈Edge(Γ) that is unforgettable resp. forgettable. These maps are pictured
in Figure 7.
The set of generators of the space of Floer cochains CF(ϕ) is enlarged by adding
two elements 1s
ϕ (with superscript s denoting strict unit) resp. 1h
ϕ (with superscript
h denoting homotopy between strict and geometric unit) of degree 0 resp.
−1
to I(ϕ).
Any edge e labeled 1s
ϕ resp.
1g
ϕ is required to have ρ(e) = ∞resp.
ρ(e) = 0 while an edge with label 1s
ϕ may have weighting ρ(e) ∈[0, ∞]. There is
no constraint for the edges e ∈Edge(Γ) labeled 1s
ϕ, while any edge with label not
equal to 1s
ϕ or 1h
ϕ must have zero weighting. The labels 1s
ϕ and 1h
ϕ are allowed on
the outgoing leaf only if the area of the treed disk is zero, the number of leaves
is one or two, and the expected dimension is zero. Thus either there are no disks
and the incoming edge is labeled 1h
ϕ and the outgoing leaf is labeled 1s
ϕ or 1g
ϕ or
there is a single disk with no interior markings, one incoming leaf labeled 1s
ϕ and
the label of the other incoming leaf and outgoing leaf are the same. The outgoing
weight ρ(e0) is required to be the product of the incoming weights Q ρ(ei) and in
the case of zero-area configurations all weightings are declared equivalent. By this


## Page 35


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
35
xh
ρ = 0
xh
xh
xg
xs
ρ = ∞
xs
xs
xs
xs
xh
xs
xg
xg
Figure 7. Unmarked treed disks
definition, in each of these cases the moduli space MΓ(X, ϕ) is a point in each of
these special configurations.
Definition 4.15. (Forgetful axiom) A perturbation datum PΓ satisfies the forgetful
axiom if for any leaf e ∈Edge(Γ) with infinite weighting ρ(e) = ∞, the perturbation
datum PΓ is pulled back from the perturbation datum Pf(Γ) for the type f(Γ)
obtained by forgetting the leaf e and stabilizing (that is, collapsing any unstable
components) under the forgetful map UΓ →Uf(Γ) of universal curves.
In particular, this axiom implies that the resulting moduli spaces admit forgetful
morphisms MΓ(X, ϕ) →MΓ′(X, ϕ) whenever there is a leaf e with weighting
ρ(e) = ∞. See [18, Section 4] for more details on the allowable weightings.
4.3. Transversality and compactness. Cieliebak-Mohnke perturbations [22] are
not sufficient for achieving transversality if there are multiple interior nodes on
ghost bubbles.
Indeed, suppose there exists a sphere component Sv ⊂S, v ∈
Vert (Γ) on which the map u|Sv is constant and maps to the divisor so that
u(Sv) ⊂D.
The domain Sv may meet any number of interior leaves Te ⊂T.
Adding an interior leaf Te′ to the tree meeting Sv increases the dimension of a
stratum dim MΓ(X, ϕ), but leaves the expected dimension Ind(Du), u ∈MΓ(X, ϕ)
unchanged. It follows that MΓ(X, ϕ) is not of expected dimension for some types
Γ that we call crowded:
Definition 4.16. A holomorphic treed disk (C, u : C →X) is crowded if each such
ghost component Sv ⊂S meets at least two interior leaves Te, so that #{e, Te∩Sv ̸=
∅} ≥2, and uncrowded otherwise.


## Page 36


36
JOSEPH PALMER AND CHRIS WOODWARD
The construction of coherent perturbations for uncrowded types proceeds induc-
tively. We summarize the properties that we wish our perturbations to satisfy in
the following definition:
Definition 4.17. A perturbation datum P = {PΓ ∈PΓ} has good properties if the
following hold for each uncrowded type of map Γ of expected dimension at most
one:
(a) (Transversality) Every element of MΓ(X, ϕ) is regular;
(b) (Compactness) the closure MΓ(X, ϕ) is a finite set, if expected dimension
zero; or a compact one-manifold, if expected dimension one, with boundary
contained in the adapted, uncrowded locus; and
(c) (Boundary description) the boundary of MΓ(X, ϕ) is a union of components
MΓ′(X, ϕ) where Γ′ is a type with an edge e of length ℓ(e) zero, an infinite
length edge e, ℓ(e) = ∞connecting two disk components, or a leaf e ∈
Edge(Γ) with eve mapping to the boundary σi(∂Bd(i)) of a cell;
Suppose that perturbations PΓ′ on the types Γ′ ≺Γ have been chosen in Defini-
tion 4.17 making the moduli space of type Γ′ regular and all moduli spaces obtained
by forgetting interior leaves in Remark 4.10 regular. Via a gluing construction the
perturbations PΓ′ induce regular perturbations in some neighborhood S+
Γ′ of SΓ′ in
SΓ. Namely any curve C of type Γ near MΓ′ is obtained from a curve C′ of type
Γ′ by some combination of removing small balls from the nodes and identifying the
complements by gluing maps given in local coordinates z →δ/z; and varying the
edge lengths. Since the perturbations by assumption vanish near the nodes, one
obtains perturbations on C from those on C′. Denote by PΓ ⊂PΓ the subset of
perturbations that agree with PΓ′ on S+
Γ′ on the types Γ′ ≺Γ. The following is
proved in a standard way, using Sard-Smale; see Palmer-Woodward [49, Section 4].
Theorem 4.18. There exists a comeager subset Preg
Γ
of the subspace PΓ making
the moduli space of type Γ regular and all moduli spaces obtained by forgetting
interior leaves from domains of type Γ in Remark 4.10 regular. Furthermore, the
perturbations chosen inductively in this way have the good properties in Definition
4.17.
4.4. Orientations. Orientations on the moduli spaces may be constructed fol-
lowing Fukaya-Oh-Ohta-Ono [31, Orientation chapter], [67], given a relative spin
structure. For this purpose, we may ignore the constraints at the interior nodes
w1, . . . , wm in int(S). The tangent spaces to these nodes and the linearized con-
straints du(wi) ∈Tu(wi)D are even dimensional and oriented by the given complex
structures. Suppose the type Γ has at least one vertex v ∈Vert(Γ). Consider a
regular element
(C, u : C →X) ∈MΓ(X, ϕ, σ)
of type Γ. The tangent space is the kernel of the linearized operator:
TuMΓ(X, ϕ) ∼= ker( ˜Du)


## Page 37


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
37
Figure 8. Bubbling off the strip-like ends
where (abusing notation) ˜Du is the restriction of the operator in (33) to the space
of sections (ζ, ξ : S →u∗TX) satisfying constraints
ξ(we) ∈Tσe, e ∈Edge ,→(Γ),
ξ(we) ∈TD, e ∈Edge ,→(Γ).
The operator ˜Du admits a homotopy
˜Dt
u, t ∈[0, 1],
˜D1
u = ˜Du,
˜D0
u = 0 ⊕Du
so that ˜D0
u is a direct sum of the zero operator and the linearized Cauchy-Riemann
operator Du. For any vector spaces V, W, the determinant line of the direct sum ad-
mits an isomorphism det(V ⊕W) ∼= det(V )⊗det(W). The deformation ˜Dt
u, t ∈[0, 1]
of operators induces a family of determinant lines det( ˜Dt
u) over the interval [0, 1],
necessarily trivial. One obtains by parallel transport of this family an identification
of determinant lines
(44)
det(TuMΓ(X, ϕ)) →det(TCMΓ) ⊗det(Du)
well-defined up to isomorphism. In the case of nodes of S mapping to self-intersection
points x ∈Isi(ϕ), the determinant line det(Du) is oriented by “bubbling off one-
pointed disks”, as in [31, Theorem 44.1] or [67, Equation (36)].
For each self-
intersection point
(x−̸= x+) ∈L2,
ϕ(x−) = ϕ(x+),
choose a path of Lagrangian subspaces
(45)
γx : [0, 1] →Lag(Tϕ(x−)=ϕ(x+)X)
γx(0) = Dx−ϕ(Tx−L)
γx(1) = Dx+ϕ(Tx+L).
Let S be the unit disk with a single boundary marking 1 ∈∂S. The path γx defines
a totally real boundary condition on S on the trivial bundle with fiber TxX. Let
det(D+
x ) denote the determinant line for the Cauchy-Riemann operator D+
x with
boundary conditions γx as in [67].
Let D−
x be the operator as in the previous
discussion but with the direction of the path γx reversed and
D+
x = det(D+
x ),
D−
x = det(D−
x ) ⊗det(TxL)
The once-marked disks with boundary conditions γx and γx glue together along
the strip like end to a disk with no-strip like end whose boundary condition is the
concatenation of γx and γx. This boundary condition is isotopic to the constant


## Page 38


38
JOSEPH PALMER AND CHRIS WOODWARD
boundary condition, and the determinant line extends over the isotopy giving a
canonical isomorphism
(46)
D−
x ⊗D+
x →R.
A choice of orientations ox ∈D±
x for the self-intersection points x are coherent if
the isomorphisms (46) are orientation preserving with respect to the standard ori-
entation on R. For each critical point choose an orientation on the corresponding
cell and let D−
σj denote the determinant line of the tangent space to the cell at
any point. Choose orientations D+
σ∨
k for the stable manifolds so that the combined
orientations for stable and unstable manifolds at the critical points give the orien-
tation on X. Given a relative spin structure for ϕ : L →X, the orientation at u is
determined by an isomorphism
(47)
det(Du) ∼= D+
σ0 ⊗D−
σ1 ⊗. . . ⊗D−
σd.
The isomorphism (47) is determined by degenerating the surface with strip-like
ends to a nodal surface as in Figure 8. Thus each end ϵe, e ∈E(Sv) of a component
Sv with a node w mapping to a self-intersection point is replaced by a disk Sv±(e)
with one end attached to the rest of the surface by a node w±
e . After combining
the orientations oe on the determinant lines on Sv±(k) with orientations oσ on the
tangent spaces to cells σ in the case of broken edges or semi-infinite edges e ∈
Edge(Γ), ℓ(e) = ∞, one obtains an orientation ou on the determinant line of the
parameterized linear operator det( ˜Du). The orientations on the determinant lines
give orientations on the regularized moduli spaces MΓ(X, ϕ, σ).
There is a similar discussion for weighted moduli spaces. The moduli space of
weighted trees Mwt
Γ is oriented via the product description (43). in the case of labels
1s
ϕ or 1g
ϕ the orientations of the moduli spaces are defined by considering the normal
bundles of the inclusions {∞} →[0, ∞] resp. {0} →[0, ∞] to be positively resp.
negatively weighted.
In particular, the components MΓ(X, ϕ, σ)≤1 of expected
dimension at most one are equipped with orientations satisfying the standard gluing
signs for inclusions of boundary components described in [47, Theorem 4.10].
In particular, for labeled map types Γ of expected dimension zero the strata
MΓ(X, ϕ) inherit orientation maps
(48)
o : MΓ(X, ϕ) →{+1, −1}
comparing the constructed orientation to the canonical orientation of a point.
5. Fukaya algebras
Fukaya algebras of immersed Lagrangians are introduced in Palmer-Woodward
[49]. The generators of the Floer complex consist of critical points, or equivalently,
cells in the associated cell decomposition; self-intersection points, and additional


## Page 39


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
39
generators for homotopy units. We denote
(49)
I(ϕ) = Ic(ϕ) ∪Isi(ϕ) ∪Ihu(ϕ)
where
Ic(ϕ) := {σ(x), x ∈crit(f)}
is the set of cells,
Isi(ϕ) := (L ×ϕ L) −∆L
is the set of ordered self-intersection points, where L ×ϕ L is the fiber product and
∆L ⊂L2 the diagonal; and
Ihu(ϕ) := {1s
ϕ, 1h
ϕ}
are two additional generators added as part of the homotopy unit construction.
The sum
1g
ϕ :=
X
codim(σi)=0
σi
is the geometric unit. Thus I(ϕ) consists of the cells in L together with two copies
of each self-intersection point, plus two extra generators.
In order to obtain graded Floer cohomology groups, a grading on the set of
generators is defined as follows. Given an orientation, there is a natural Z2-valued
map
I(ϕ) →Z2,
x 7→|x|
obtained by assigning to any cell σ ∈Ic(ϕ) the codimension mod 2 and to any
self-intersection point (x−, x+) ∈Isi(ϕ) the element |x| = 0 resp. |x| = 1 if the
self-intersection is even resp. odd. The grading degrees of the cells are determined
by the codimensions codim(σi) = dim(L) −d(i) for the cells σi. For the extra
generators 1s
ϕ, 1h
ϕ the gradings are given by.9
|1s
ϕ| = 0,
|1h
ϕ| = −1.
Denote by Ik(ϕ) the subset of σ ∈I(ϕ) with |σ| = k mod 2.
The space of Floer cochains is freely generated by the above generators over the
Novikov field. The space of Floer cochains is the Z2-graded vector space
CF(ϕ) =
M
k∈Z2
CF k(ϕ),
CF k(ϕ) =
M
x∈Ik(ϕ)
Λx.
The q-valuation on Λ extends naturally to CF(ϕ):
valq : CF(ϕ) −{0} →R,
X
x
c(x)x 7→min
x (valq(c(x)), c(x) ̸= 0).
9Here we work only with Z2 gradings, so the extra generators are simply even and odd respec-
tively; see Remark 2.3.


## Page 40


40
JOSEPH PALMER AND CHRIS WOODWARD
5.1. Composition maps. The composition maps in the Fukaya algebra are counts
of rigid holomorphic treed disks weighted by areas and holonomies. For perturba-
tions from the last section, define higher composition maps
md : CF(ϕ)⊗d →CF(ϕ)[2 −d],
d ≥0
on generators as follows. Let σ1, . . . , σd ∈I(ϕ) and let
MΓ(X, ϕ, σ)0 ⊂MΓ(X, ϕ)
denote the subset of rigid maps with constraints given by generators σ = (σ0, . . . , σd)
as defined in (36).
Definition 5.1. (Composition maps) On generators σ1, . . . , σd define
(50)
md(σ1, . . . , σd) =
X
Γ,
σ0∈I(ϕ)
u∈MΓ(X,ϕ,σ0,...,σd)
wt(u, γ)σ0
where the weight wt(u, γ) is defined by
wt(u, γ) = (−1)♡
θ(u)! y(∂u)qA(u)o(u)
with the notation
• θ(u) ∈Z>0 is the number of interior leaves e ∈Edge (Γ), corresponding to
intersections u(we) ∈D with the Donaldson hypersurface D;
• y(∂u) ∈Λ0 is the holonomy of the local system y around the boundary
u(∂S) ⊂ϕ(L) as in Remark 2.4;
• A(u) ∈R≥0 is the sum of the areas A(uv) of the disks and spheres uv : Sv →
X for v ∈Vert(Γ);
• o(u) ∈{±1} is an orientation sign defined in (48) using the relative spin
structure for ϕ : L →X;
• the exponent ♡∈Z is given by
(51)
♡=
d
X
i=1
i|σi|;
• and the sum is over all types of rigid maps Γ.
we have written tensor products as commas to save space. If a matching condition
MΓ is a formal sum (rather than a single diffeomorphism) the contributions are
weighted by the coefficients ci, dj of the perturbations MΓ,i, HΓ,j in (37), (38). This
ends the Definition.
The composition maps involving one input of type 1h
ϕ, 1s
ϕ are also defined geomet-
rically by the above sum, as in Lemma 5.4 below computing m1(1h
ϕ). In particular
(52)
m2(1s
ϕ, 1s
ϕ) = 1s
ϕ,
−m2(1h
ϕ, 1s
ϕ) = m2(1s
ϕ, 1h
ϕ) = 1h
ϕ


## Page 41


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
41
since the corresponding moduli spaces are points. Recall that 1s
ϕ is a strict unit if
and only if
(53)
m2(1s
ϕ, a) = a = (−1)|a|m2(a, 1s
ϕ),
md(. . . , 1s
ϕ, . . .) = 0, ∀d ̸= 2.
Theorem 5.2. [49, Theorem 4.1] For a perturbation system P = (PΓ) with good
properties as in Theorem 4.18 the maps (md)d≥0 satisfy the axioms of a (possibly
curved) A∞algebra CF(ϕ) with strict unit 1s
ϕ ∈CF(ϕ).
Remark 5.3. The second A∞relation gives a condition for the existence of a
coboundary operator. The element
m0(1) ∈CF(ϕ)
is the curvature of the Fukaya algebra and has positive q-valuation valq(m0(1)) > 0
by Lemma 5.5. The Fukaya algebra CF(ϕ) is flat if m0(1) vanishes, and projectively
flat if m0(1) is a multiple of the identity 1s
ϕ. The first two A∞relations are the
analogs of the Bianchi identity and definition of curvature respectively in differential
geometry:
m1(m0(1)) = 0,
m2
1(σ) = m2(m0(1), σ) −(−1)|σ|m2(σ, m0(1)),
∀σ ∈I(ϕ).
Thus if CF(ϕ) is projectively flat then m2
1 = 0 and the undeformed Floer cohomol-
ogy HF(ϕ) = ker(m1)/ im(m1) is defined.
Lemma 5.4. For the composition maps md defined using (50), m1(1h
ϕ) is equal to
1s
ϕ −1g
ϕ plus terms that are higher order in q.
Proof. By definition, m1(1h
ϕ) counts configurations with a single input and output
edge. By definition, constant configurations from a single edge Te with input 1h
ϕ
and output 1s
ϕ or 1g
ϕ are stable.
The moduli space of such configurations with
weight ρ(e) = ∞occur as the positive end of the moduli space Mwt
Γ
and by
definition is positively oriented, while the locus with ρ(e) = 0 is negatively oriented.
Configurations with no disks contribute 1s
ϕ −1g
ϕ, while configurations (C, u : C →
X) with at least one disk uv : Sv →X contribute terms with positive area A(u) > 0,
since at least one of the disks uv must be non-constant by the stability condition.
□
Lemma 5.5. For composition maps md defined using (50), the curvature m0(1)
satisfies the gap condition valq(m0(1)) ≥ℏ, where ℏ> 0 is the energy quantization
constant of Lemma 4.7.
Proof. Any configuration (C, u : C →X) with no leaves Te must have at least one
non-constant holomorphic disk uv|Sv : Sv →X, by the stability condition. Thus
the area of any configuration (C, u : C →X) contributing to m0(1) must be at
least A(uv) ≥ℏby Lemma 4.7.
□


## Page 42


42
JOSEPH PALMER AND CHRIS WOODWARD
More generally, the Fukaya algebra may admit projectively flat deformations
even if it itself is not projectively flat. Consider the sub-space of CF(ϕ) consisting
of elements with positive q-valuation
CF(ϕ)+ =
M
σ∈I(ϕ)
Λ>0σ.
where Λ>0 = {0} ∪val−1
q (0, ∞).10 Define the Maurer-Cartan map
m : CF(ϕ)+ →CF(ϕ),
b 7→m0(1) + m1(b) + m2(b, b) + . . . .
Here m0(1) is the image of 1 ∈Λ under
m0 : CF(ϕ)⊗0 ∼= Λ →CF(ϕ).
Let MC(ϕ) denote the space of (weakly) bounding cochains:
(54)
MC(ϕ) =
(
b ∈CF odd
+ (ϕ)
valq(b) > 0

m(b) ∈span(1s
ϕ)
)
.
The value W(b) of m(b) for b ∈MC(ϕ) defines the disk potential
W : MC(ϕ) →Λ,
m(b) = W(b)1s
ϕ.
For any b ∈MC(ϕ) define a projectively flat deformed Fukaya algebra CF(ϕ, b)
with the same underlying vector space but composition maps mb
d defined by
(55)
mb
d(a1, . . . , ad) =
X
i1,...,id+1
md+i1+...+id+1(b, . . . , b
|
{z
}
i1
, a1, b, . . . , b
|
{z
}
i2
, a2, b,
. . . , b, ad, b, . . . , b
|
{z
}
id+1
);
note that these maps only satisfy the A∞axiom if b has odd degree because of
additional signs that appear in the case b even. Occasionally we wish to emphasize
the dependence of MC(ϕ) on the local system y ∈R(ϕ) and we write MC(ϕ, y) for
MC(ϕ). For b ∈MC(ϕ), the maps mb
d, d ≥1 form a projectively flat A∞algebra.
The resulting cohomology is denoted
HF(ϕ, b) = ker(mb
1)/ im(mb
1)
The deformed second composition map mb
2 induces on HF(ϕ, b) with b ∈MC(ϕ)
the structure of an associative algebra. The union of HF(ϕ, b) for b ∈MC(ϕ) mod
gauge equivalence, see the following section, is a homotopy invariant of CF(ϕ) and
independent of all choices up to isomorphism of algebras and change of base point
b.
In the case of self-intersection points, the condition that the Maurer-Cartan
solutions have positive q-valuation may be relaxed using the following lemma, which
10In fact one can only require positive valuations of the coefficients of the degree-one generators,
and the self-intersection points. The requirement of positivity at the self-intersection points can
be slightly weakened, see (61) below.


## Page 43


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
43
is a sort of energy quantization for corners at self-intersections. The following is
an analog of [24, Lemma 2.6].
Lemma 5.6. Let dim(L0) > 2 and k > 2. There exists a constant δ > 0 such
that the following holds: Suppose that (C, u : C →X) is a rigid treed holomorphic
disk with k + 1 leaves. If s is the number of corners we ∈S mapping to transverse
self-intersection points σe ∈Isi(ϕ), then A(u) ≥sδ.
Proof. We convert the area into action via an application of Stokes’ theorem. Let
x ∈Isi(ϕ) be a self-intersection point. We may assume without loss of generality
that the Darboux chart X ⊃U →Cn has image that contains the radius r ball
Br(0) ⊂Cn for r ∈(0, ∞) small. Recall from Section 3.2 that the complex structure
JΓ ∈J (X) near the self-intersection point is standard so that JΓ|U = J0, where
J0z = iz for any tangent vector z ∈TxU ∼= R2n ∼= Cn. The symplectic form ω0 on
Cn is exact with
ω0 = dα0,
α0 :=
n
X
j=1
1
2(qjdpj −pjdqj) ∈Ω1(Cn).
By Stokes’ theorem,
(56)
Z
u−1(U) u∗ω0 =
Z
u−1(∂U) u∗α0.
Here we have used that the restriction of α to the Lagrangian branches Rn, iRn
vanishes.
We now take the limit as the path approaches the intersection point. On the
locus U ∗= {z ∈S, u(z) ̸= 0} where u is non-zero in the local chart the map u
descends to a map
[u] : U ∗→CP n−1,
z 7→span(u(z)).
Consider the corresponding section z 7→([u(z)], u(z)) of the pull-back [u]∗T of the
tautological bundle
T =
n
(ℓ, z) ∈CP n−1 × Cn  z ∈ℓ
o
→CP n−1.
The restriction of α0 to the boundary of the ball Br(x), viewed as the unitary frame
bundle of the tautological bundle T, is −r2 times the standard connection one-form
αT ∈Ω1(T1) on the unit circle bundle T1 in the tautological bundle T ∼= S2n−1 over
CP n−1 with projection π : T →CP n−1. Let
curv(T) ∈Ω2(CP n−1),
(π|T1)∗curv(T) = dαT
denote the curvature two-form of αT. One checks easily from, for example, a Taylor
series expansion that removal of singularities holds in this case and the map [u]
extends to a holomorphic map u−1(U) →CP n−1. Since [u] is also holomorphic,
the pull-back of minus the curvature −[u]∗curv(T) ∈Ω2(u−1(U)) is a positive two-
form. On the other hand, on the locus u ̸= 0 the map u determines a section of U


## Page 44


44
JOSEPH PALMER AND CHRIS WOODWARD
whose normalization v = u/∥u∥trivializes u∗T. The integral (56) is up to a scalar
the parallel transport in the frame defined by the section u: Let Bϵ(u−1(0)) denote
a union of ϵ-balls around the finite set u−1(0), and denote the fractional winding
number
d(u, z) := (2π)−1
Z
∂Bϵ(z)∩S v∗αT
of the phase of the section u along the path ∂Bϵ(z) ∩S; note that this integral is
well-defined even if z is a boundary point. By Stokes’ theorem
Z
u−1(∂U) u∗α0
=
−r2
Z
u−1(∂U) v∗αT
(57)
=
lim
ϵ→0 −r2
 Z
[u|U−Bϵ(u−1(0))][v]∗curv(T)
(58)
−
Z
∂Bϵ(u−1(0)) v∗αT
!
(59)
=
−r2
Z
[u|U][v]∗curv(T) + 2πr2
X
z∈u−1(0)
d(u, z).
(60)
The tautological bundle T has curvature −curv(T) that is a positive two-form,
see for example Demailly [23, Section 15.B]. It follows that the first term on the
right-hand side of (60) is non-negative. Let δ be the minimum of constants r2π/2,
as x varies over transverse self-intersection points. The angle change at any self-
intersection point is a multiple of π/2, which proves the claim.
Finally, we rule out constant disks mapping to self-intersections. Constant disks
u : S →X with image ϕ(x), x ∈Isi(ϕ) must have corners with alternating labels
σ1 = x, σ2 = x, σ3 = x, σ4 = x, . . . , σ2k = x.
The sum of the degrees of these constraints is k dim(L), while the moduli space of
2k + 1-marked disks has dimension 2k −2. The expected dimension of the moduli
space of holomorphic treed disks is therefore
dim MΓ(X, ϕ, σ)
=
(2k −2) −k(|x| + (dim(L) −|x|)
=
(k −1)(2 −dim(L)).
Thus the labeled type Γ is rigid only if dim(L0) = 2 or k = 1.
□
Corollary 5.7. Let ϕ0 : L0 →X be a self-transverse immersed Lagrangian brane
of dimension dim(L0) ≥2. The projective Maurer-Cartan equation
(61)
X
d≥0
md(b, . . . , b) ∈span 1s
ϕ
is well-defined for b of the form b = bsi + bc satisfying the condition in Definition
1.1 for the δ described in Lemma 5.6. Any such solution b has square-zero mb
1 and


## Page 45


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
45
so a Floer cohomology group
HF(ϕ, b) = ker(mb
1)
im(mb
1) .
Proof. By Lemma 5.6, the infinite sum in the Maurer-Cartan equation (61) has q-
valuations approaching infinity and is well-defined in CF(ϕ). A similar argument
shows that the deformed Fukaya maps mb
d from (55) are well-defined.
□
Denote the set of solutions in Corollary 5.7 by
MCδ(ϕ) = {b ∈CF(ϕ)|(61)}.
Remark 5.8. In the case ϕ = ϕϵ is a surgery, we allow the coefficients bϵ(µ), bϵ(λ)
of the meridian and longitude to have vanishing q-valuation. Theorem 5.13 implies
that for the perturbation systems we use, the potential W(bϵ) and Floer cohomology
HF(ϕϵ, bϵ) are still well-defined for such elements.
Remark 5.9. We briefly describe the invariance properties of Fukaya algebras. The
argument using quilted disks with diagonal seam condition, see Charest-Woodward
[18, Section 3] and Palmer-Woodward [49, Remark 6.3] extends to the cellular set-
ting to define A∞morphisms between A∞algebras defined using different choices.
Given two sets of choices Jk, Dk, P k this argument gives an A∞morphism
CF(ϕ, J0, D0, P 0) →CF(ϕ, J1, D1, P 1)
inducing in particular a morphism of Maurer-Cartan spaces
MC(ϕ, J0, D0, P 0) →MC(ϕ, J1, D1, P 1)
preserving the Floer cohomologies.
We expect that the homotopy type of the
immersed Fukaya algebra CF(ϕ) is independent of the choices of almost complex
structure, divisor, and perturbations. However, we prove no such invariance result
here.
Example 5.10. The following example of an immersion of a circle in the plane shown
in Figure 1 is an easily visualizable example of the invariance of the disk potential.
In this case, the correspondence between holomorphic curves in X bounding ϕ0
and ϕϵ is an application of the Riemann mapping theorem. The Floer cohomology
HF(ϕ0) is trivial since the circle is displaceable by a compactly-supported Hamil-
tonian flow. The disk potential W(ϕ0) is non-trivial and will be computed below.
Let ϕ0 : S1 →R2 be the immersion with three self-intersection points
x, x′, x′′ ⊂ϕ0(S1).
The complement of the image ϕ0(S1) ⊂X = R2 has five connected components as
in Figure 1.
We identify a particular weakly bounding cochain. Suppose that the area of the
central region in X −ϕ0(L) is A0 > 0 while the area of each of the lobes is A1 > 0.


## Page 46


46
JOSEPH PALMER AND CHRIS WOODWARD
For simplicity, choose a Morse function on L0 ∼= S1 so that there is a single 0-cell
σ0 on the lobe containing x, and a single 1-cell σ1; the actual cell structure used
for the proof is somewhat more complicated but the difference in cell structures is
irrelevant for the example. Consider the cochain
b0 = iq(−A0+3A1)/21h
ϕ0 + iq(A1−A0)/2(x + x′ + x′′) ∈CF(ϕ0)
with coefficient iq(A1−A0)/2 on the self-intersection points x, x′, x′′ and a multiple of
the degree −1 element iq(−A0+3A1)/21h
ϕ0.
We compute the twisted curvature mb0
0 (1) as follows.
The three outer lobes
with no inputs contribute qA1(x + x′ + x′′) to m0(1), and also to mb0
0 (1).
The
disk u : S →X whose interior int(S) maps to the central region of X −ϕ0(L0)
contribute to mb0
0 (1) with outputs on x, x′, x′′. Since for each such output there are
two inputs labeled b0, the contribution of this region is
qA0(iq(A1−A0)/2)2(x + x′ + x′′) ∈CF(ϕ0).
The holomorphic strip connecting x to the zero-dimensional cell contributes to
mb0
0 (1) as well, with a single g input and so a contribution of iq(A1−A0)/2qA1σ1.
Finally, the constant disk with input iq(−A0+3A1)/21h
ϕ0 contributes
iq(−A0+3A1)/2(1s
ϕ0 −1g
ϕ0) ∈CF(ϕ0)
to m1(b0), hence mb0
0 (1). Thus
mb0
0 (1)
=
qA1(x + x′ + x′′) + qA0(iq(A1−A0)/2)2(x + x′ + x′′)
+
(iq(A1−A0)/2)qA1σ1 + iq(−A0+3A1)/2(1s
ϕ0 −1g
ϕ0)
=
iq(−A0+3A1)/21s
ϕ0
is a multiple of the unit 1s
ϕ0. Therefore, the element b0 ∈MC(ϕ0) is a solution to
the projective Maurer-Cartan equation.
The self-intersection points of ϕ0 are admissible in the sense of Definition 1.1,
which implies that the Floer cohomology is well-defined. Any disk u : S →X with
boundary on ϕ0 and meeting one of the self intersection points x = (x−, x+) ∈S1
without a branch change must contain in its image u(S) the exterior non-compact
region in X outside the curve ϕ0(S1).
This is impossible since the image of a
compact set must be compact.
A small Lagrangian surgery produces a Lagrangian immersion of a disjoint union
of circles. Choose ϵ > 0 sufficiently small so that the surgery is defined and
(A1 −A0)/2 = −A(ϵ)
where A(ϵ) > 0 is the area from Definition 2.1.
Let σ′
1, σ′′
1 denote the top-
dimensional cells on the two components near the self-intersection point x, as in


## Page 47


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
47
Figure 1. As explained below in (178), the shift from b0 to bϵ is equivalent to a
shift in the local system. Define a local system yϵ on ϕϵ by
yϵ([σ′
1]) = yϵ([σ′′
1]) = iq(A1−A0)/2qA(ϵ) = i.
Define bϵ by removing the x-term so that
bϵ = iq(−A0+3A1)/21h
ϕ0 + iq(A1−A0)/2(x′ + x′′).
We have
mbϵ
0 (1)
=
iqA1−A(ϵ)σ′
1 + (iq(A1−A0)/2)2qA0−A(ϵ)σ′′
1
+qA1(x′ + x′′) + qA0−A(ϵ)i(iq(A1−A0)/2)(x′ + x′′)
+iq(−A0+3A1)/2(1s
ϕ0 −1g
ϕ0)
=
iq(−A0+3A1)/21s
ϕ0.
It follows that mbϵ
0 (1) is a multiple of the strict unit 1s
ϕ0 on the right-hand-side with
the same value of the potentials
W0(b0, y0) = iq(3A1−A0)/2 = Wϵ(bϵ, yϵ)
as the unsurgered immersion ϕ0. This ends the Example.
5.2. Gauge equivalence. A notion of gauge equivalence relates solutions to the
weak Maurer-Cartan equation so that cohomology is invariant under gauge equiv-
alence. Let b0, . . . , bd ∈CF(ϕ) have odd degree and let a1, . . . , ad ∈CF(ϕ). Define
(62)
mb0,b1,...,bd
d
(a1, . . . , ad) =
X
i0,...,id
md+i0+...+id(b0, . . . , b0
|
{z
}
i0
, a1, b1, . . . , b1
|
{z
}
i2
, a2, b2,
. . . , b2, . . . , ad, bd, . . . , bd
|
{z
}
id
).
Two odd elements b0, b1 ∈CF(ϕ)+ are gauge equivalent if and only if
∃h ∈CF(ϕ)+, b1 −b0 = mb0,b1
1
(h),
deg(h) even.
We then write b0 ∼h b1.
The discussion on [18, p.
75] shows that ∼h is an
equivalence relation. The linearization of the above equation is m1(h) = b1 −b0, in
which case we say that b0 and b1 are infinitesimally gauge equivalent.
For notational convenience, we define a “shifted valuation”
valδ
q(bsi) = valq(bsi) + δ
bsi ∈span(Isi(ϕ)) −{0}
valδ
q(bc) = valq(bc)
bc ∈span(Ic(ϕ)) −{0}
valδ
q(bc + bsi) = min(valδ
q(bc), valδ
q(bsi)),
bc, bsi ̸= 0.
Then MCδ(ϕ) is the space of solutions to the projective Maurer-Cartan equation
with non-negative valδ
q.


## Page 48


48
JOSEPH PALMER AND CHRIS WOODWARD
Lemma 5.11. Let ϕ : L →X be a self-transverse immersed Lagrangian brane and
b0, b1 ∈CF(ϕ).
(a) (Preservation of the Maurer-Cartan space under gauge equivalence) If b0 ∼h
b1 for some h ∈CF(ϕ)+ and b0 ∈MCδ(ϕ) then b1 ∈MCδ(ϕ) as well.
(b) (Integration of infinitesimal gauge equivalences into gauge equivalences)
Suppose that h, b0, b1 ∈CF(ϕ) and ζ > 0 are such that
(63)
mb0,b1
1
(h) = b1 −b0,
mod (valδ
q)−1((ζ, ∞)),
valδ
q(h) > ζ.
Then there exists an element b∞∈CF(ϕ), valδ
q(b∞) > 0 with
mb0,b∞
1
(h) = b∞−b0,
valδ
q(b∞−b1) > valδ
q(b1 −b0) + ζ.
Proof. For item (a), define W(b1) ∈Λ so that
(64)
mb1
0 (1) = W(b1)1s
ϕ + c,
c := (mb1
0 (1) −W(b1)1s
ϕ).
The element c ∈CF(ϕ) has coefficient of the strict unit 1s
ϕ equal to zero. We have
mb1
0 (1) −mb0
0 (1)
=
X
d,i≤d−1
md(b0, . . . , b0
|
{z
}
i
, b1 −b0, b1, . . . , b1)
=
mb0,b1
1
(mb0,b1
1
(h))
=
−mb0,b0,b1
2
(mb0
0 (1), h) + mb0,b1,b1
2
(h, mb1
0 (1))
=
W(b1)h −W(b0)h + mb0,b1,b1
2
(h, mb1
0 (1) −W(b1)1s
ϕ)
=
W(b1)h −W(b0)h + mb0,b1,b1
2
(h, c)
where the last inequality uses the definition of c in (64) and the strict unit identities
(53). Rearranging terms we have
(W(b1) −W(b0))(1s
ϕ −h)
=
((mb1
0 (1) −c) −W(b1)h) −(mb0
0 (1) −W(b0)h)
=
mb0,b1,b1
2
(h, c) −c.
(65)
Since the two terms on the right have no coefficient of 1s
ϕ by (52), we must have
W(b0) = W(b1).
We now apply an induction to show that the correction c vanishes. Suppose
that there exists ζ > 0 and k ≥1 such that c is divisible by qkζ and valδ
q(h) > ζ;
note that this holds for k = 1 and some ζ > 0 sufficiently small by the previous
paragraph. The equation (65) implies that
mb1
0 (1)
=
mb0,b1,b1
2
(h, c) + W(b1)1s
∈
W(b0)1s
ϕ + (valδ
q)−1(((k + 1)ζ, ∞)).
Since this holds for every k, the claim (a) follows.
The second item (b) follows from a filtration argument. Suppose
bk = mb0,bk
1
(h) + b0
mod (valδ
q)−1((kζ, ∞)).


## Page 49


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
49
Define a solution bk+1 to order (k + 1)ζ by defining
bk+1 = mb0,bk
1
(h) + b0.
The desired element is the limit of the elements bk.
□
The following gives a way of “gauging away” the weakly bounding cochain in a
neighborhood of the self-intersection.
Proposition 5.12. Let ϕ : L →X be a Lagrangian immersion and U ⊂L a
contractible open set in L. Then any b0 ∈MCδ(ϕ) is gauge equivalent to some
b∞∈MCδ(ϕ) that vanishes on critical points contained in U.
Proof. We solve for the adjusted weakly bounding cochain order by order, using the
fact that the leading order term in the Floer differential is the Morse differential.
Suppose that bk ∈MCδ(ϕ) vanishes on critical points contained in U modulo terms
of order kζ for some k ∈Z+. Let
bk(U) =
X
x∈I(ϕ)∩U
b(x)x
denote the part of bk lying in U. We may assume that ζ has been chosen sufficiently
small so that any non-constant holomorphic disk bounding ϕ has area at least ζ.
In the following, we work up to terms so the Morse differential of bk vanishes terms
with valuation greater than kη everywhere. The fact that mbk
0 (1) ∈span(1ϕ) mod
qkζ implies that m1(bk) = 0, hence δ(bk) = 0 where δ is the Morse differential. Since
U is contractible, the cohomology of (X, X −U) is acyclic except in top degree.
Hence bk = δ(ck) for some even cochain ck mod critical points supported outside
of U. Let bpre
k+1 = bk −δ(ck), so that bk+1(U) vanishes up to order (k + 1)ζ on U.
By Lemma 5.11 there exists bk+1 ∈MCδ(ϕ) gauge equivalent to bk such that
bk+1 −bk = mbk,bk+1
1
(ck),
valδ
q(bk+1(σ)) > (k + 1)ζ
for any critical point σ contained in U. The gauge transformation does not affect
the lower order terms in bk and so the limit
b∞:= lim
k→∞bk
exists, lies in MCδ(ϕ), is gauge equivalent to b0. Furthermore, b∞vanishes on all
critical points contained in U, as desired.
□
5.3. Divisor insertions. The divisor equation for Lagrangian Floer cohomology
is a hoped-for relation, (66) below, for the insertion of a degree one cocycle into the
composition maps. In this section, we prove a related result for the contribution
of any configuration with a codimension one cell as input up to repetition of the
input.11 The divisor equation for Fukaya algebras is similar to the familiar divisor
11The results of this section are not necessary if dim(L0) ≥3 and one uses the shift in local
system (175) and
bϵ = b0 −b0(x)x −b0(x)x + b0(x)b0(x)λ


## Page 50


50
JOSEPH PALMER AND CHRIS WOODWARD
equation in Gromov-Witten theory in Kontsevich-Manin [41, 2.2.4]. For k ≥0
write
mk =
X
β∈H2(ϕ)
mk,β : CF(ϕ)⊗k →CF(ϕ)
where mk,β is the contribution to mk arising from holomorphic disks of class β ∈
H2(ϕ). The divisor equation for a codimension one cycle c reads
(66)
k+1
X
i=1
mk+1,β(x1, . . . , xi−1, c, xi, . . . , xk) = ⟨[c], [∂β]⟩mk,β(x1, . . . , xk)
see [19, Proposition 6.3]. In particular, the divisor equation implies that for x a
degree one cycle in ϕ(L)
(67)
X
k≥0
mk(x, . . . , x) =
X
k≥0
X
β∈H2(ϕ)
⟨x, [∂β]⟩k
k!
m0,β(1).
The right hand side of (67) is the contribution of m0(1) with local system y shifted
by
exp(x) ∈Hom(H1(ϕ(L), Z), Λ0) ∼= R(ϕ).
In this sense, variations of the weakly bounding cochain b ∈MC(ϕ) should be
equivalent to variations of the local system y ∈R(ϕ). In general the truth of the
divisor equation typically depends on the existence of regularized moduli spaces of
holomorphic disks equipped with forgetful maps. The existence of such maps is
rather difficult in the Morse setting.
We prove an identity for contributions to the composition maps with repeated
inputs related to the divisor equation (66); the terminology will be explained in
the following discussion.
Theorem 5.13. Suppose P red is a reduced-regular perturbation system.
There
exists a system of perturbations PΓ satisfying the conditions in Definition 4.17
such that for each codimension one cell σi, rigid treed disk u : C →X whose
boundary meets σi transversally, and collection of positive integers d = (d(z) ≥0),
there exists a unique configuration ud obtained by repeating d(z) inputs at each
z ∈u−1(σi) in the neighborhood U red
u
with weight given by the inverse factorial
wt(ud, γ) =
Y
z,σi
(d(z)!)−1 wt(u, γ).
The terminology is explained by the following definitions.
Definition 5.14. (Inserting repeated inputs) Let u : S →X be a holomorphic
disk bounding ϕ and let z ∈∂S be a point where u(z) intersects a codimension
one cell σ transversally. Given such a disk and an integer d ≥1, let
ured
d
: Cred
d
→X
instead of shifting the weakly bounding cochain in Definition 1.2, or in dimension dim(L0) = 2
with the local system formulas (175), (178).


## Page 51


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
51
be the configuration whose domain
Cred
d
:= C ∪Te0 ∪Sv ∪Te1 ∪. . . ∪Ted
consists of an additional disk Sv on which ured
d
is constant, attached at z via an
edge Te0 of some length ℓ(e0) and d edges Te1, . . . , Ted attached to Sv mapping to
σ, as in the middle drawing in Figure 9.
z ∈u−1(σi)
Te1
Te2
Te3
Te1
Te2
Te3
u
ured
d
ud
Figure 9. Configurations corresponding to an intersection with a
codimension one cell: Left, a configuration meeting the cell transver-
sally; Middle, adding a constant disk with multiple edges to the left
configuration; Right, the center configuration after perturbation
Definition 5.15. A perturbation system P red is reduced regular for a cell σ if
(a) the matching conditions M = (MΓ) are equal to the identity map in an
open neighborhood of σ and
(b) all rigid configurations u not of the form (ured)d for some u and d are regular.
In other words, rigid maps u : C →X not obtained by repeating inputs are all
regular.
Suppose a reduced regular perturbation system P red has been chosen. Consider
a new perturbation system P obtained from P red by perturbing the matching con-
ditions for the semi-infinite edges Te, e ∈Edge→(Γ).
Lemma 5.16. For a generic perturbation system P obtained from P red as above,
each rigid treed disk u is regular and obtained from some ured
d
by removing the
ghost component and changing the positions of the edges Te1, . . . , Ted so that the
corresponding nodes map to the perturbed cell MΓ(wei, ·)−1(σ).
Proof. Transversality is a standard consequence of Sard-Smale. To see that any
rigid treed disk is of the form ured
d
for some u for a sufficiently small perturbation,
suppose that uν is a family of such maps for perturbations MΓ,ν(wei, ·) that con-
verges to the identity in the C∞topology, but uν is not obtained as above. By
Gromov compactness, there exists a subsequence of uν that converges to some ured
d .


## Page 52


52
JOSEPH PALMER AND CHRIS WOODWARD
But by transversality, there is a unique uν close to ured
d
satisfying the perturbed
matching conditions. This is a contradiction.
□
That is, perturbed configurations are clustered around the configurations ob-
tained by repeating inputs.
Example 5.17. We explain how repeating inputs appear in the product structure
on the Floer cohomology of a Lagrangian given by the circle in the two-sphere.
Let X = S2 and L = S1 a circle dividing X into two regions of areas A+ and A−.
Equip L with a Morse function so that it has standard cell decomposition into two
cells consisting of a 0-cell σ0 and a 1-cell σ1. Equip X with its standard complex
structure. Since there are two Maslov-index-two disks corresponding to the two
A+
A−
σ1,1
σ1,2
σ1,3
Figure 10. Disks with point constraints on the sphere
hemispheres, for the trivial bounding cochain we obtain
m0(1) = (qA+ + qA−)σ0
and the relation
m1(σ1) = (qA+ −qA−)σ0.
Consider the family of maps ured
d
obtained from one of the two hemispheres as
above with d by repeating incoming edges labeled by σ1. The unperturbed com-
plex structure and matching condition is reduced-regular for σ1, since every config-
uration without constant disks labeled by multiple codimension-one constraints is
regular. In particular, the map u1 obtained from u by adding an edge Te1 mapping
to σ0 is regular. A choice of perturbed matching conditions MΓ at the incoming
edges Te1, . . . , Ted amounts to a collection of perturbations σ1,1, . . . , σ1,d, that is,
points near σ1. Suppose the perturbations σ1,i are in the same order around the
boundary ∂Sv as the order given by the indices. Then there is a PΓ-perturbed map
ud obtained from u by repeating inputs. Otherwise, if the order is different, then
no such map exists. In particular, for d = 2 if the perturbations σ0,1, σ0,2 follow
the cyclic order around the disk with area A+ then we have
(68)
m2(σ1, σ1) = qA+σ0
while if the perturbations are in the opposite order then
(69)
m2(σ1, σ1) = qA−σ0.


## Page 53


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
53
If A+ = A1, then the Floer cohomology is non-trivial and we obtain the relation
on cohomology
m2([σ1], [σ1]) = qA+[σ0] = qA−[σ0]
so the product on cohomology is independent of the choice of perturbation.
The
standard complex structure J on X = S2 combined with the unperturbed matching
condition MΓ(w, l) = l, ∀l ∈L is reduced regular since the only maps of expected
dimension zero are those containing a single Maslov index two disk constrained by
degree one cells. Any such disk uv : Sv →X is necessarily one of those above with
area A+ or A−and is regular as long as there is a single incoming leaf. The only
other configurations of expected dimension are those with multiple leaves labeled
σ1, and these are not required to be regular. The contributions to md(σ1, . . . , σ1) are
clustered around the two maps arising from the two disks with areas A+, A−, and
obtained by slightly perturbing the points σ1, . . . , σ1 to points in general position
σ1,1, . . . , σ1,d.
We wish to choose perturbations so that the count of perturbed configurations
with repeated inputs is controlled by the weight of the original configuration.
Definition 5.18. The matching condition MΓ for a type Γ is permutation-invariant
on an open subset U ⊂L for σ if for any two edges e1, e2 ∈Edge(Γ) MΓ(we1, l) =
MΓ(we2, l) as multivalued perturbations for all l ∈U.
Example 5.19. We continue the two-sphere example in 5.17 and compute the second
structure map for a permutation-invariant matching condition. A permutation-
invariant multi-valued perturbation is given by matching conditions assigning the
nodes to map to perturbations of the 0-cells σ1,1, σ1,2 in clockwise order around
the boundary of the disk with coefficient 1/2, and σ1,1, σ1,2 in the counterclockwise
order also with coefficient 1/2. The resulting structure map is
m2(σ1, σ1) = 1
2(qA+ + qA−)σ0.
In the case A+ = A−, this agrees with the formulas (68), (69) obtained without
averaging, and so induces the same product on Floer cohomology.
Proof of Theorem 5.13. The statement of the Theorem follows by choosing the per-
turbations so that they are permutation-invariant near the reduced configurations.
Let P red = (P red
Γ ) be a reduced-regular perturbation system for σ1, . . . , σk. Induc-
tively construct, as in the proof of Theorem 4.18, a nearby regular perturbation
system P so that the perturbed matching conditions M = (MΓ) are permutation-
invariant in a neighborhood of each cell σi. Suppose that the reduced configura-
tions of type Γred meet the codimension one cells σi in a finite set ZΓ. It follows
from the implicit function theorem that for sufficiently small perturbations PΓ of
P red
Γ
there is a bijection between P red
Γ -perturbed configurations ured
d
with ℓ(e0) = 0
and PΓ-perturbed configurations.
After a generic perturbation M ◦
Γ of MΓ, the


## Page 54


54
JOSEPH PALMER AND CHRIS WOODWARD
points z1, . . . , zd are distinct. Since the number of permutations is finite, the set
of single-valued conditions g∗M ◦
Γ that are regular for all permutations g of the
edges Te1, . . . , Ted is comeager. The average MΓ is then regular. Assuming the
perturbations MΓ are invariant under permutations of the points on the constant
disks, of the d! possible orderings of the perturbations MΓ,i(σ) of σ induced by the
matching conditions MΓ exactly one ordering is achieved by a sequence of points
z1, . . . , zd in cyclic order around the boundary of S. It follows that the weight of
any point in the fiber is (d!)−1 times the weight of the image configuration. In the
recursive construction of the perturbation system P = (PΓ), at each stage we are
given PΓ on the boundary of UΓ and wish to extend it over the interior. Because
the space of perturbations is contractible, the inductive procedure may be carried
out as before.
□
Remark 5.20. (Divisor edges attached to constant disks) In the moduli space of
rigid treed disks there may also be configurations with boundary edges labeled
by σi so that the adjacent disk Sv is constant. Suppose that the perturbations
vanish, so that all treed disks are regular without perturbation. If the configuration
two incoming edges Te1, Te2 then there is another configuration u′ obtained by
interchanging the order of the inputs Te1, Te2 around the boundary of Sv. These
two configurations contribute with opposite signs and cancel.
We will need a similar “repeating input” type formula for disks with repeat-
ing alternating inputs at the self-intersection points in the case of Lagrangians of
dimension two. Suppose that dim(L0) = 2 and x = (x−, x+), x = (x+, x−) are
ordered self-intersection points. In this case, there are additional constant disks
u|Sv : Sv →{ϕ(x)} ⊂X of expected dimension zero with corners alternating
σ1 = x, σ2 = x, σ3 = x, σ4 = x, . . . ∈Isi(ϕ)
where σ± ∈Ic(ϕ) is the top-dimensional cell containing x+ resp. x−. Let Γ denote
the corresponding combinatorial type of domain, with 2d+1 boundary leaves and no
interior leaves. The unperturbed relevant moduli space MΓ(ϕ) is not of expected
dimension.
Indeed, any 2d + 1-marked treed disk (C, u : C →X) with disk
component mapping entirely to the self-intersection point ϕ(x) is holomorphic.
The moduli space of such maps MΓ(ϕ) is dimension 2d −2, not the expected
dimension zero.
Definition 5.21. Let ϕ : L →X be an immersed Lagrangian brane of dimension
dim(L) = 2 and x ∈Isi(ϕ) a self-intersection point flowing to a critical point σ±,0
in the branch ±. The immersed Fukaya algebra CF(ϕ) is rotation-invariant at x
if and only if for any d ≥1 we have
m2d(x, x, x, . . . , x)
∈
(−1)d−1σ+,0
d
+ val−1
q (0, ∞)
m2d(x, x, . . . , x, x)
∈
−(−1)d−1σ−,0
d
+ val−1
q (0, ∞).


## Page 55


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
55
Remark 5.22. It seems that rotation-invariant perturbations exist, essentially be-
cause perturbations for zero-energy disks are the first step in the inductive proce-
dure for constructing perturbations. We take 5.21 as an assumption in the case
dim(L) = 2 and both b0(x) and b0(x) are non-vanishing.
6. Holomorphic disks and neck-stretching
In symplectic field theory, one studies the behavior of holomorphic curves as
the almost complex structure on the target changes in a family corresponding to
neck-stretching. Following Bourgeois-Eliashberg-Hofer-Wysocki-Zehnder [13] and
Venugopalan-Woodward [65] we describe the limit of the Fukaya algebra of a La-
grangian under neck-stretching.
The limit of a sequence of holomorphic disks
with respect to such a neck-stretching is a holomorphic building in the language of
Bourgeois-Eliashberg-Hofer-Wysocki-Zehnder [13].
The situation in this paper differs from the situation in the above papers in
several ways.
First of all, the Lagrangian is allowed to pass through the neck
region, as it is in Fukaya-Oh-Ohta-Ono [31, Chapter 10]. Second, since our Fukaya
algebras are defined using treed disks, it may be that the tree part, rather than
surface part, breaks in the neck-stretching limit. Thus the levels of the buildings
in this case have not only strip-like and cylindrical ends going to infinity, but also
additional breakings of the segments. Finally, we wish to degenerate our moduli
spaces to products of treed disks in the pieces, rather than fiber products. For
this we take an additional limit which degenerates the matching conditions at the
separating hypersurface.
6.1. Broken holomorphic disks. Broken disks arise by the following neck-stretching
limit studied by Bourgeois-Eliashberg-Hofer-Wysocki-Zehnder [13] in the context
of symplectic field theory. Recall that if Z ⊂X is a coisotropic submanifold, then
the null foliation of Z is the distribution defined by
ker(ω|TZ) =
[
z∈Z
{ξ ∈TzZ|ω(ξ, ζ) = 0,
∀ζ ∈TzZ} ⊂TZ.
The null foliation ker(ω|TZ) is called fibrating if there exists a fiber bundle p :
Z →Y so that the null foliation is ker(ω|TZ) = ker(Dp). In this case, the bundle
p : Z →Y is unique up to isomorphism and called the null fibration.
Definition 6.1. (Neck-stretching for almost complex structures on symplectic
manifolds) Let Z ⊂X be a codimension one coisotropic submanifold admitting
the structure of an S1-null-fibration p : Z →Y over a symplectic manifold Y .
Thus
ker(Dp) = ker(ω|TZ) ⊂TZ
is the vertical subspace. Let
ωZ = p∗ωY ∈Ω2(Z)


## Page 56


56
JOSEPH PALMER AND CHRIS WOODWARD
denote the pullback of the symplectic form ωY to Z.
The neck-stretched manifold is obtained by cutting along the hypersurface and
inserting a cylinder. Let X◦denote the manifold with boundary obtained by cutting
open X along Z. Let Z′, Z′′ denote the resulting copies of Z. For any τ > 0 let
(70)
Xτ = X◦
[
Z′′={−τ}×Z,{τ}×Z=Z′
([−τ, τ] × Z)
be the manifold obtained by gluing together the ends Z′, Z′′ of X◦using a neck
[−τ, τ] × Z of length 2τ.
Define almost complex structures on the neck-stretched manifold as follows. The
R action by translation on R and U(1) action on Z combine to a smooth C× ∼=
R×U(1) action on R×Z making R×Z into a C×-bundle. Consider the projections
pR : R × Z →R,
pZ : R × Z →Z,
pY : R × Z →Y
onto factors R and Z resp. onto Y . An almost complex structure J on R × Z is
called cylindrical12 if J is C×-invariant, preserves the tangent spaces to the fibers
of pY : R × Z →Y and J is equal to the standard almost complex structure on
any fiber
p−1
Y (y) = R × Zy ∼= R × U(1) ∼= C×.
In particular, each orbit of C× is holomorphic. Any cylindrical almost complex
structure J on R × Z induces an almost complex structure JY on Y by projection
by the formula
DpY (Jw) = JY DpY w,
w ∈T(R × Z).
We assume that JY is compatible with the symplectic form ωY on Y . 13 There are
complementary vertical resp. horizontal rank resp. corank two sub-bundles
V
=
ker(Dp) ⊕ker(DpZ) ⊂T(R × Z)
H
=
TZ ∩J(TZ) ⊂p∗
ZTZ ⊂T(R × Z).
with the first bundle V being a a trivial bundle over R × Z. We have a splitting
into complex vector bundles
(71)
T(R × Z) ∼= H ⊕V.
Since Z is assumed to admit the structure of a principal S1-bundle, there is a
unique connection one-form compatible with the splitting
α ∈Ω1(Z)S1,
ker(α) = H
(and in particular Z is a stable hypersurface in the terminology of symplectic field
theory.)
Conversely, given such a one-form, there is a unique almost complex
structure J given by JY on H and the standard almost complex structure on V .
12These conditions are stronger than the definition in Bourgeois-Eliashberg-Hofer-Wysocki-
Zehnder [13], which deals with a more general situation.
13For many purposes, it suffices to assume that JY tames ωY , see for example [21].


## Page 57


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
57
The neck-stretched submanifolds of (70) are all diffeomorphic, and the construc-
tion provides a family of almost complex structures on the original manifold. The
neck-stretched manifold Xτ is diffeomorphic to X by a family of diffeomorphisms
given on the neck region by a map
(72)
(−τ, τ) × Z →(−τ0, τ0) × Z
equal to the identity on Z and a translation in a neighborhood of {±τ}×Z. Given
an almost complex structure J on X that is of cylindrical form on (−τ0, τ0)×Z, we
obtain an almost complex structure Jτ on Xτ by using the same cylindrical almost
complex structure on the neck region. Via the diffeomorphism Xτ →X described
in (72), we obtain an almost complex structure on X also denoted Jτ. This ends
the Definition.
Compactness results in symplectic field theory [13] describe the limit of holomor-
phic curves as the length of the neck approaches infinity. The complement of Z in
X divides X into regions X⊂and X⊃, which we consider as symplectic manifolds
with cylindrical ends. Similarly, suppose that ϕ : L →X is a possibly immersed
Lagrangian submanifold intersecting Z transversally in a submanifold LZ = Z ∩L,
so that in a neighborhood of {0}×Z in the tubular neighborhood (−ϵ, ϵ)×Z →X
L is the image of (−ϵ, ϵ) × LZ →X. We denote by
L⊂= ϕ−1(X⊂),
L⊃= ϕ−1(X⊃)
the pieces of L in X⊂and X⊃. In the neck-stretching limit, the symplectic field
theory compactness results produce a configuration of holomorphic maps with La-
grangian boundary conditions called a building.
Definition 6.2. The broken symplectic manifold arising from the triple (X⊂, X⊃, Y )
above is the topological space
X = X⊂∪Y ∪X⊃
obtained by compactifying X⊂, X⊃by adding a copy of Y and identifying the
copies. Thus X is the singular space obtained by gluing the smooth manifolds
X⊂= X⊂∪Y,
X⊃= X⊃∪Y
along Y . The space X inherits a natural topology by viewing X as the quotient of
X by the equivalence relation on Z given by the S1-fibration. Thus X is a stratified
space and the link of a point in Y in X is a disjoint union of two circles. The space
X comes equipped with an isomorphism of normal bundles
(73)
N = (TX⊂)Y
TY
∼=
 (TX⊃)Y
TY
!−1
.
The infinite neck is the product R × Z and may be compactified by adding copies
of Y at ±∞. For an integer k ≥1, define the k-broken symplectic manifold
(74)
X[k] = X⊂⊔(R × Z) ⊔. . . ⊔(R × Z) ⊔X⊃.


## Page 58


58
JOSEPH PALMER AND CHRIS WOODWARD
The k −1 copies of R × Z are called the neck pieces. Define
(75)
X[k]0 = X⊂,
X[k]1 = R × Z, . . . , X[k]k = R × Z,
X[k]k = X⊃.
For each piece we denote by X[k]i the compactified space obtained by adding one
or two copies of Y at infinity. The complex torus (C×)k−1 acts X[k] via the action
of C× on each neck piece,
C× × P(N± ⊕C) →P(N± ⊕C),
(z, [n, w]) 7→z[n, w] := [zn, w].
Similarly, define the broken Lagrangian
(76)
L = L⊂∪LY ∪L⊃
where LY = p(LZ). Let
L[k] = L⊂⊔(R × LZ) ⊔. . . ⊔(R × LZ) ⊔L⊃.
The group (R×)k−1 acts by real translations on the neck pieces.
Definition 6.3. A holomorphic building with k + 1 levels consists of
(a) a collection of surfaces Si, i = 0, . . . , k with strip-like and cylindrical ends
and
(b) holomorphic maps
ui : Si →X[k]i
called the levels of the building; satisfying the given boundary conditions
ui(Si) ⊂L[k]i
(c) a pairing of the outgoing ends of Si with the incoming ends of Si+1 so that
the limits along the ends satisfying matching conditions: For each such pair
of ends, there exists a multiplicity µ ∈R (possibly non-integer in the case of
strip-like ends) and coordinates (s, t) on the ends so that so that
(77)
lim
s→∞exp(−2πµ(s + it))ui(s, t) = lim
s→−∞exp(2πµ(s + it))ui+1(s, t).
In particular, the completions ui to ui+1 have matching value at Y = X[k]i ∩
X[k]i+1 and the same multiplicity of intersection with Y .
Automorphisms of buildings u : S →X[k] are pairs
ϕ ∈Aut(S),
ψ ∈Aut(X[k])
consisting of translations on the neck pieces so that
u ◦ϕ = ψ ◦u.
A building u : S →X is stable if it has finitely many automorphisms.
The limits of the levels in a building along the ends is a collection of Reeb chords
and orbits.


## Page 59


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
59
Definition 6.4. (Reeb orbits and chords) Loops in a fiber of constant speed
ϑ : S1 →Zy,
α
 d
dtϑ(t)
!
constant
are called Reeb orbits. Paths of constant speed beginning and ending at the La-
grangian
ϑ : [0, 1] →Zy,
α
 d
dtϑ(t)
!
constant,
ϑ(k) ∈LZ, k ∈{0, 1}
are called Reeb chords. This ends the definition.
Remark 6.5. Given a Reeb orbit or chord ϑ with α

d
dtϑ(t)

= µ the trivial strip
or trivial cylinder corresponding to ϑ is the map with domain S = R × [0, 1] resp.
S = R × S1
S 7→R × Z,
(s, t) 7→(sµ, ϑ(t)).
Equivalently, a building u is stable if and only if each component
uv : Sv →X[k]0 ∪X[k]k
in the components X[k]0, X[k]k without translation automorphisms is stable and
each level
ui : Si →X[k]i, i = 1, . . . , k −1
in the neck region is a union of stable maps and trivial cylinders or strips, and has
at least one component that is not a trivial cylinder or strip; the latter condition
prevents the existence of automorphisms arising from the translation action on the
neck pieces.
We now turn to treed holomorphic buildings. We assume that on the neck region
of the Lagrangian, the Morse function is given by the radial coordinate: For some
constant a > 0,
f(s, z) = a + s.
Thus the gradient vector field of f is grad(f)(s, z) = ∂s, independent of s, z.
Definition 6.6. A treed building is a treed disk C equipped with a decomposition
structure C = C0 ∪. . . ∪Ck so that any edge Te connecting different levels has a
single breaking separating it into components Te,i ⊂Ci and Te,i+1 ⊂Ci+1 for some
i. Each component Ci will be called a treed level; see Figure 11.
A holomorphic treed building is a treed building C = S ∪T equipped with a holo-
morphic map u : C →X[k] for some k so that the intersections T ∩S occur away
from the nodes joining levels and the collection ui := u|Si satisfies the conditions
(77) as well as the matching conditions for the edges Te connecting Te,i and Te,i+1


## Page 60


60
JOSEPH PALMER AND CHRIS WOODWARD
at a point w, the limits match in the sense that if si resp. si+1 is a coordinate on
Te,i resp. Te,i+1 then
(78)
lim
si→∞πZui(si) =
lim
si+1→−∞πZui(si+1).
Stability for treed buildings is defined in the same way as for buildings, with the
following special case: If a building C consists of a single edge Te with no disks with
an incoming label 1h
ϕ and an outgoing label 1s
ϕ or 1g
ϕ then we declare the building
stable; similarly a building consisting of a single edge with input labeled σe1 and
output labeled σe0, where σe0 appears in the boundary of σe1 is stable.
Figure 11. A treed level
We introduce the following notation for moduli spaces and evaluation maps. For
any type of treed building Γ denote by MΓ(X, ϕ) the moduli space of buildings of
type Γ. Similarly, if Γi is the type of level of Γ then MΓi(X, ϕ) denotes the moduli
space of levels of type Γi. For each treed level type Γi evaluation at the semi-infinite
edges defines a map
(79)
ev : MΓi(X, ϕ) →Lei( )
Z
× Y ei( ) × Ldi( )
assigning to each map ui : S →X the beginning points ϑe(0) ∈Z of the limiting
ei( ) Reeb chords or ei( ) orbits ϑe at infinity along each strip-like or cylindrical
end of S, as well as the evaluations at the ends of the di( ) semi-infinite edges. For
any subset
(80)
Σ ⊂Lei( )
Z
× Y ei( ) × Ldi( )
denote by
(81)
MΓi(ϕ, Σ) = ev−1(Σ)
the moduli space of maps with the given constraints.


## Page 61


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
61
We will regularize these moduli spaces by passing to maps adapted to a Donald-
son hypersurface. A broken divisor D = (D⊂, D⊃) is a pair of divisors D⊂⊂X⊂
and D⊃⊂X⊃with
D⊂∩Y = DY = D⊃∩Y
such that
ϕ : LY →Y,
ϕ⊂: L⊂→X⊂,
ϕ⊃: L⊃→X⊃
are exact in the complement of DY resp.
D⊂resp.
D⊃.
Any broken divisor
D = (D⊂, D⊃) gives rise to a family of divisors D such that ϕ : L →X is exact
in the complement of D, as in [18, Section 8.3]. As in [18], one may first choose a
Donaldson hypersurface DY for LY disjoint from the Lagrangian LY ⊂Y . One may
then extend to Donaldson hypersurfaces D⊂⊂X⊂and D⊃⊂X⊃, by choosing
extensions of the asymptotically holomorphic sequence of sections. The definition
of adapted buildings is then similar to that of adapted maps: Each component of
u−1(D) is required to contain an interior edge, and each such edge is required to
map to D.
6.2. Fredholm theory and exponential decay. In this section, we collect some
technical results on holomorphic maps asymptotic to Reeb orbits or chords. In
order to carry out the necessary classification of levels in the local model, we allow
Lagrangian boundary conditions that are asymptotically cylindrical rather than
cylindrical in a neighborhood of infinity.
Definition 6.7.
(a) An almost complex manifold X has a cylindrical end mod-
elled on Z if there exists an embedding
κX : R>0 × Z →X
such that the image of κX has compact complement.
A cylindrical end
almost complex structure is an almost complex structure J : TX →TX for
which the pull-back J|R>0×Z to R>0 × Z is of cylindrical form in the sense
of Definition 6.1, that is, the restriction of a cylindrical almost complex
structure JR×Z on R × Z.
(b) Let ϕ : L →X be a Lagrangian immersion. Call ϕ cylindrical near infinity
if there exists a smooth manifold LZ of Z and s ∈R so that LZ is cylindrical
in (s, ∞) × Z on the end: That is,
(κX)−1(ϕ(L)) ∩((s, ∞) × Z) = (s, ∞) × LZ.
Since we are considering only the circle-fibered case, our cylindrical end manifolds
have natural compactifications at infinity. Given a manifold X with cylindrical
almost complex structure J as above, the compactification of X is the almost
complex manifold X = X ∪Y obtained by gluing in a copy of Y at infinity. In
terms of charts, we have
(82)
X = X ∪R>0×Z (Z ×C× C)


## Page 62


62
JOSEPH PALMER AND CHRIS WOODWARD
where Z ×C× C is the line bundle associated to Z. The inclusion of R>0 × Z in
Z ×C× C is given by the isomorphism
R>0 × Z ∼= Z ×S1 C×.
Proposition 6.8. Suppose that ϕ : L →X is cylindrical-near-infinity. Then the
closure ϕ(L) ⊂X is contained in the image of a Lagrangian immersion ˜ϕ : ˜L →X
with (without boundary, but possibly non-compact) clean self-intersection.
Proof. The subset R>0 × Z glues into the chart Z ×C× C near infinity by the map
(s, z) 7→[z, e−s]. Let L denote the union
L = ϕ(L) ∪(R>0 × LZ) ∪LY
in X.
In a neighborhood of Y the closure L is contained in the cleanly-self-
intersecting submanifold ˜L given as the image of (R>0 × (−LZ ∪LZ)) ∪LY .
□
Definition 6.9. Let X = X ∪Y be as above equipped with a symplectic structure.
A Lagrangian submanifold L ⊂X is asymptotically cylindrical to a cylindrical-near-
infinity Lagrangian L0 if the closure L is an immersed submanifold-with-boundary
in X tangent to the closure of L0 at LY .
Example 6.10. The unflattened handle Hγ ⊂Cn is asymptotically cylindrical, by
Lemma 7.22 below.
Proposition 6.11. Let L ⊂X be an asymptotically cylindrical Lagrangian mani-
fold asymptotic to a cylindrical-near-infinity Lagrangian submanifold L0. The clo-
sure L is contained in a (possibly non-compact) cleanly-self-intersecting Lagrangian
submanifold of X.
Proof. The closure of L is LY and L is tangent to L0, which is contained in a
cleanly-self-intersecting Lagrangian by Proposition 6.8. We may write L near LY
as the graph of an exact one-form df on L0 where f : L0 →R is smooth, using
Weinstein neighborhoods of each branch of L′ in X to write nearby Lagrangians as
graphs of one-forms. By, for example, the Seeley extension theorem [55] f extends
to a function f ′ on L′. After possibly shrinking L′, there are no self-intersection
points of graph(df ′) other than LY , that is, the extensions of the branches do not
intersect, and graph(df ′) provides the desired extension.
□
Let S be a holomorphic curve with cylindrical and strip-like ends
κe, : R × S1 →S
e = 1, . . . , e( )
κe, : R × [0, 1] →S
e = 1, . . . , e( ).
Definition 6.12. (Holomorphic maps asymptotic to Reeb chords) Given a cylin-
drical or asymptotically cylindrical Lagrangian ϕ : L →X, a map from a surface
S with strip and cylindrical ends to X with boundary in ϕ is a map
u : S →X,
u(∂S) ⊂ϕ(L).


## Page 63


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
63
A map u : S →X is asymptotic to a Reeb chord ϑ on an end of S if there exist
s0 ∈R and a multiplicity µ ∈R+ such that in cylindrical coordinates (s, t) on each
end the distance in the cylindrical metric dcyl on R × Z, with coordinates given by
κe, or κe,
(83)
dcyl(u(s, t), (s0 + µs, ϑ(t))) < Ce−θs
for some constant θ > 0 and s0 ∈R. The definition of an end asymptotic to a Reeb
orbit is similar. This ends the Definition.
The exponential decay above is closely related to a finite-energy condition. Our
case is a special case of a more general definition for stable Hamiltonian structures in
[13]. For simplicity consider holomorphic maps to U = R×Z, where Z is equipped
with closed two-form ωZ ∈Ω2(Z) with fibrating null-foliation ker(ωZ) ⊂TZ and
connection form α ∈Ω1(Z). Let J : TU →TU be a cylindrical almost complex
structure. The horizontal energy of a holomorphic map
u = (ψ, v) : (S, j) →(R × Z, J)
is ([13, 5.3]) with S◦⊂S denoting the complement of the corners (points where
u|∂S has a branch change)
Eh(u) =
Z
S◦v∗ωZ.
The vertical energy is ([13, 5.3])
(84)
Ev(u) = sup
ζ
Z
S◦(ζ ◦ψ)dψ ∧v∗α
where the supremum is taken over the set of all non-negative C∞functions
ζ : R →R,
Z
R ζ(s)ds = 1
with compact support. The Hofer energy ([13, 5.3]) is the sum
E(u) = Eh(u) + Ev(u).
Let X◦be a symplectic manifold with cylindrical end modelled on R>0 × Z. The
vertical energy Ev(u) on the end is defined as before in (84). The Hofer energy
E(u) of a map u : S◦→X◦from a surface S◦with cylindrical ends to X◦is
defined by dividing X◦into a compact piece Xcom and a cylindrical end R>0 × Z,
and defining
E(u) = E(u|Xcom) + E(u|R≥0×Z)
where E(u) is the Hamiltonian-perturbed energy from (34).
Lemma 6.13. Let ϕ : L →X be an cylindrical-near-infinity Lagrangian immer-
sion. Any J-holomorphic map u : S →X with boundary on ϕ(L) and finite Hofer
energy extends to a J-holomorphic map u : S →X, and the extension defines a
bijection between maps to X and maps to X.


## Page 64


64
JOSEPH PALMER AND CHRIS WOODWARD
Proof. Exponential convergence on strips with finite Hofer energy is proved in
Cieliebak-Ekholm-Latschev [15, Proposition 3.2].
The exponential convergence
implies that u is finite area. Removal of singularities for holomorphic maps with
boundary on immersed Lagrangians with clean self-intersection Schmäshke [54] im-
plies that the map u extends to a map u : S →X with boundary on L. Conversely,
any map u : S →X restricts to a map from S to X by removing the points mapping
to X −X. The finite Hofer energy condition E(u) < ∞follows from the fact that
by the constant rank embedding theorem, the symplectic form in a neighborhood
of Y in X −X is diffeomorphic to a neighborhood of the zero section in the normal
bundle NY may be written d(ζv∗α) + π∗
Y ωY where ζ is the norm-square function.
This form is cohomologous to that one for which ζ has compact support, and the
Stokes’ formula computation in [13, Section 5.7] implies that bounded Hofer energy
is equivalent to bounded area. See [13, Remark 5.9].
□
The condition that a holomorphic map has finite Hofer energy implies asymptotic
convergence to Reeb chords at infinity for an exponential decay constant that is
related to the minimum angle of intersection between the Lagrangians.
Lemma 6.14. (Removal of singularities for cylindrical maps) Let ϕ : L →X
be an asymptotically cylindrical Lagrangian immersion. For any finite energy J-
holomorphic map u : S →X either
(a) there exist x ∈X such that u(s, t) converges to x as s →∞, uniformly in t
for cylindrical coordinates (s, t) along the end e (so that u has a removable
singularity) or
(b) there exists a Reeb chord resp. orbit ϑe such that u(s, t) converges exponen-
tially fast to ϑe(s) as s →∞, for s →∞with constant θ in the sense of
(83) depending only on ϑe.
Proof. The desired convergence for strip-like ends κe,◦is a consequence of Schmäshke
[54, Theorem 3.2]: There exist positive constants θ′, c0, c1, c2, . . . and an eigenfunc-
tion
v : [0, 1] →TxX,
∂tv = θv,
v(0) ∈TxLi−, v(1) ∈TxLi+
with eigenvalue θ so that for every integer k ≥0
(85)
u(s, t) = expx
−1
θ e−θsv(t) + w(s, t)

,
∥w∥Ck([s,∞]×[0,1]) ≤cke−(θ+θ′)s.
The eigenfunctions v of ∂t on the vertical parts of TxLk−, TxLk+ correspond to Reeb
chords (cf. Robbin-Salamon [53, Appendix E]) ϑ, and in cylindrical coordinates on
X the exponential of e−θsv(t) is equal to (θs, ϑ(t)). The second estimate in (85)
implies the desired exponential convergence.
□
We develop Fredholm theory for holomorphic treed maps to cylindrical end man-
ifolds. Given a holomorphic map u : S →X with finite Hofer energy, denote by Γ


## Page 65


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
65
the type of the domain S and MΓ(X, ϕ) the space of maps u : S →X with domain
type Γ.
Proposition 6.15. For any domain type Γ, the space MΓ(X, ϕ) of finite-energy
holomorphic maps (C, u : C →X) with domain type Γ is locally cut out by a
Fredholm map of Banach spaces.
Before beginning the proof, we remark that there are two possible approaches
to the Fredholm theory. By Lemma 6.13, the moduli space of finite-energy maps
MΓ(X, ϕ) is in bijection with the space of maps u : S →X to the compactification
bounding ϕ(L). The statement of the Proposition follows from the Fredholm theory
for holomorphic maps with boundary on a clean intersection Lagrangian [54]. The
second version of Fredholm theory treats the target as a cylindrical end manifold,
and is required to prepare for the needed gluing result later in Section 6.5. We
carry out the second approach.
Proof. We suppose for simplicity that the limits along the strip-like or cylindrical
ends are Reeb chords or orbits, so that there are no self-intersection points. Since
the intersection Lk ∩Zy with each branch Lk of L at infinity with each fiber Zy, y ∈
Y is by assumption finite, we may assume that the boundary of u on the strip-like
ends maps to branches Lk−, Lk+ of the Lagrangian on the boundary at infinity. The
two branches differ by
(86)
Lk+ ∩Zy ∼= eiθ(Lk−∩Zy)
for some angle θ ∈[0, 2π). Choose a Sobolev decay constant λ ∈(0, 2π) smaller
than the angles θ, if θ ̸= 0. Let β be a good cutoff function
(87)
β ∈C∞(R, [0, 1]),



β(s) = 0
s ≤0
β(s) = 1
s ≥1 .
Define a Sobolev weight function
(88)
ℵλ : S◦→[0, ∞),
(s, t) 7→β(s)pλs
where β(s)pλ is by definition zero on the complement of the cylindrical ends. Let
Ω0(S◦, u∗TX)′
k,p,λ =
n
ξ ∈Ω0(S◦, u∗TX)W k,p
loc
 ∥ξ∥p
k,p,λ < ∞
o
denote the weighted Sobolev space of exponent p, differentiability class k, and decay
constant λ. By definition this space consists of sections with finite norm ξ : S◦→
u∗TX with limits
lim
s→∞ξ ◦κe, (s, ·) =: ξ(e) ∈Ω0([0, 1], R × ϑ∗
eTZ)


## Page 66


66
JOSEPH PALMER AND CHRIS WOODWARD
at infinity defined by
(89)
∥ξ∥p
k,p,λ :=
X
e
∥(ξ(e))∥p +
Z
S◦

X
k>0
∥∇kξ∥p
+∥ξ −
X
e
β(|s| −| ln(δ)|/2)T u(ξ(e))∥p
!
exp(ℵλ)d VolS◦
where T u is parallel transport from ϑe(t) to u(s, t) along u(s′, t). By definition,
these Sobolev spaces have evaluation-at-infinity maps
(90)
ev∞: Ω0(S◦, u∗TX)′
k,p,λ →
M
e∈E(S◦)
T(R × Z),
ξ 7→(ξ(e))e∈E(S◦).
By a model map we mean a map u0 : S◦→X which has the form (s, t) 7→
exp(µ(s + it))z for some z ∈Z and constant µ ∈R; that is, mapping to a single
fiber of R × Z where it is identified with a one-parameter subgroup. Let
Map(S◦, X)k,p,λ = {expu0(ξ),
ξ ∈Ω0(S◦, u∗
0TX)k,p,λ}
denote the space of maps u : S◦→X equal to expu0(ξ) for some model map
u0 : S◦→X by an element of the weighted Sobolev space ξ ∈Ω0(S◦, u∗
0TX)k,p,λ.
Let
Ω0,1 (S◦, u∗TX)k−1,p,λ = {η ∈Ω0,1 (S◦, u∗TX)0,p,λ ,
∥η∥k−1,p,λ < ∞}
denote the space of (0, 1)-forms with finite (k −1, p, λ) norm, given in the case
k −1 = 0 by
∥η∥0,p,λ =
Z
S◦∥η∥p exp (ℵλ) d VolS◦
1/p
.
Using the local trivializations (32) define a Banach manifold resp. Banach vector
bundle
BΓ
=
Mi
Γ × Map (S◦, X, L)k,p,λ
EΓ
=
∪u∈BΓEi
Γ,u, Ei
Γ,u = Ω0,1 (S◦, u∗TX)k−1,p,λ .
Note that
(91)
TC,uBΓ = TMΓ ⊕Ω0 (S◦, u∗TX, (∂u)∗TL)′
k,p,λ .
As usual we obtain a Cauchy-Riemann operator
(92)
Fi
Γ : Bi
Γ →Ei
Γ,
u 7→∂J,Hu
whose zeros cut out the space of holomorphic maps from S◦to X locally. For
cylindrical ends, the linearized operator ˜Du is Fredholm by standard results on
elliptic operators on cylindrical end manifolds in Lockart-McOwen [44], and in
the case with Lagrangian boundary condition, results described in Schmäshke [54,
Section 5]; note that these results require that the almost complex structure is
compatible.
□


## Page 67


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
67
We compare the linearized operators for the map to the cylindrical-end manifold
and its compactification as follows. Given a holomorphic, finite energy map u :
S →X, let u : S →X denote its extension to the compactification described in
Lemma 6.13 above. The pull-back-bundle u∗TX gives an extension of u∗TX over
the cylindrical and strip-like ends. However, we wish to choose an extension so that
there is an isomorphism of kernels and cokernels of the linearized operator and its
compactification. For this, we introduce a twisting of the bundle, similar to the
notion of twisting by a divisor in algebraic geometry. On the cylindrical end, we
have a splitting
(93)
κ∗
XTX ∼= T vX ⊕T hX
where
T vX := ker (DpY ) ,
T hX := p∗
Y TY
into the vertical and horizontal parts. We assume that the almost complex struc-
ture respects the splitting, as in, for example, the standard complex structure on
Cn −{0}. The restriction of u∗TX to u−1 (κX (R>0 × Z)) splits into vertical and
horizontal parts as well:
u∗TX| (κX (R>0 × Z)) = (u∗TX)v ⊕(u∗TX)h.
Definition 6.16.
(a) For the horizontal bundle define an extension
(u∗TX)v
c := (u∗
Y TY )c := u∗
Y TY →S.
The Cauchy-Riemann operator DuY extends to u∗
Y TY as the operator DuY .
(b) For the vertical bundle define an extension by triviality: The bundle (u∗TX)v
is spanned in each fiber by the vector fields ∂s, ∂t, where s + it is the coor-
dinate on each fiber of R × Zy ∼= R × S1. So
(u∗TX)v ∼= u−1 (κX (R>0 × Z)) × R2
is the trivial bundle. The Cauchy-Riemann operator by assumption pre-
serves the vertical part and is trivial the frame given by ∂s, ∂t, and so extends
to the trivial operator over the compactification
(u∗TX)v
c :=

u−1 (κX (R>0 × Z)) ∪{ze, e ∈E(S)}

× R2 →S.
(c) Gluing the extensions of the horizontal and vertical bundles together with
the bundle u∗TX (via the canonical identification over u−1κX(R>0 × Z))
defines an extension
(u∗TX)c =

(u∗TX) ∪(u∗TX)v
c ⊕(uTX)h
c)

→S.
(d) Define an extension of the boundary condition (∂u)∗TL := (u|∂S)∗TL as
follows: On the horizontal component the condition TLY over ∂S∩κX(R>0×
Z) extends as uY |∂STY , and the vertical part TR ∼= R × R extends as the
trivial bundle.


## Page 68


68
JOSEPH PALMER AND CHRIS WOODWARD
(e) Denote by the Cauchy-Riemann operator on the compactified bundle (u∗TX)c
with boundary ((∂u)∗TL)c
(Du)c : Ω0(S, (u∗TX)c; (∂u∗TL)c) →Ω0,1(S, (u∗TX)c; (∂u∗TL)c)
Remark 6.17. The extended bundle is not generally isomorphic to u∗TX; For ex-
ample, in the case X is the cylinder R × S1 and u the identity map, u∗TX has
Chern number 2 while (u∗TX)c is the trivial bundle.
Proposition 6.18. Let u : S →X be a finite energy map bounding L, and u : S →
X its extension bounding ϕ(L). Suppose further that the almost complex structure
preserves the splitting into horizontal and vertical parts on the cylindrical ends.
Then the Cauchy-Riemann operator Du extends to an operator Du on (u∗TX)c
and restriction defines an isomorphism of kernels and cokernels
ker( ˜Du) ∼= ker( ˜Du),
coker( ˜Du) ∼= coker( ˜Du).
In particular these operators have the same index.
Proof. Restriction defines an isomorphism of kernels.
Any section of (u∗TX)c
bounding (u∗TL)c and in the kernel of Du restricts to a section of (u∗TX). By
Taylor’s theorem, smooth sections ξ of (u∗TX)c have a power series expansion in
local coordinate on each end and so in cylindrical or strip-like coordinates on each
end for each k ≥0 there exists a real constant ck so that
(94)
ξ(s, t) = v0 + e−πsv(t) + w(s, t),
∥w∥Ck([s,∞]×[0,1]) ≤cke−π(1+θ)s
where v0, v(t) are the leading eigenvector the tangential part of Du. Thus ξ has
exponential convergence to a constant and lies in the kernel of Du. On the other
hand, cf. Schmäshke [54, Appendix B], elements of the kernel of Du have the same
exponential convergence. Thus any ξ ∈ker(Du) extends to a continuous section ξ
which is a weak solution to (Du)cξ = 0. The section ξ is then a strong solution by
elliptic regularity, as in Harvey-Polking [33]. The reader may compare with similar
results in Abouzaid [3, (4.19)], or in the cylindrical end case in Ekholm [26, Lemma
6.4].
The identification of cokernels follows from a similar statement for the kernels
of the adjoints: First note that the cokernel of Du is identified with the subset of ele-
ments of the cokernel of the operator Du acting on the space Ω0(u∗TX, (∂u)∗TL)k,p,λ
that are also orthogonal to the sections were thrown in by hand, so to speak, as in
(89). As in Lockart-McOwen [44], one may assume, after treat Du as a perturba-
tion of a translation-invariant operator (Du)′ on the ends, by viewing a solution to
(Du)∗η = 0 as a solution to (D′
u)η = (Du)′η −(Du)η with exponentially-decaying
inhomogeneous term. In the translationally-invariant case, a one-form η in the
kernel of the adjoint has an eigenfunction expansion for the self-adjoint operator
∂t acting on functions on [0, 1] with real boundary condition on the ends:
η(s, t) =
X
ν≥0
cνe−νπ(s+it) (ds −idt)


## Page 69


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
69
for some real constants cν ∈Rn, after taking a bundle trivialization. Orthogonality
to the image of functions constant at infinity implies that the coefficient c0 vanishes:
If ρ(s) is a real-valued function equal to 0 for s small and 1 for s large then
Z
R<0×Z((∂ρ(s)), η(s, t))dsdt =
Z
R<0×Z
 d
dsρ(s)c0
!
ds = c0
which must vanish. It follows that |η(s, t)| decays at least as fast as e−πs. On the
other hand, the kernel of (Du)∗
c consists of one-forms η which by Taylor’s theorem
satisfy the decay estimate |η(s, t)| < ce−πs. Indeed, if z is a coordinate near the
point ze ∈S, the form dz is equal to
dz = z(ds −idt) = πeπ(−s+it)(ds −idt).
Thus, any such section η extends to a weak solution of the adjoint equation
(Du)∗
cη = 0, by removal of singularities again.
Thus restriction defines an iso-
morphism of cokernels as well.
□
6.3. Compactness for buildings. The relative form of the compactness theorem
in Bourgeois-Eliashberg-Hofer-Wysocki-Zehnder [13, Section 11.3] and Abbas [1] in
symplectic field theory describes the limits of subsequence of holomorphic maps
with Lagrangian boundary conditions and Morse-Bott non-degeneracy conditions
as in [13, Remark 5.9].
Compactness in symplectic field theory is also treated
in related situations by Cieliebak-Mohnke [21] without Lagrangian boundary and
Venugopalan-Woodward [65] in the case that the Lagrangian is disjoint from the
stretching hypersurface. Chanda [16] gives further details in the Lagrangian case.
We will need an extension of these results to the case of treed holomorphic curves.
The first result, Theorem 6.19 below, describes a compactness theorem in a neck-
stretching limit. The second, Theorem 6.21, describes compactness for buildings
under variation of the Lagrangian boundary condition.
Theorem 6.19. Given a sequence of adapted stable holomorphic treed disks (Cν, uν :
Cν →Xτν), τν →∞with Lagrangian boundary conditions in ϕ and bounded en-
ergy, there exists a subsequence of uν converging to an adapted stable holomorphic
treed building (C, u : C →X) with boundary mapping to the broken Lagrangian L.
Furthermore, the limit of any Gromov convergent sequence is unique.
Sketch of proof. Venugopalan-Woodward [65] prove sft compactness for the case of
Lagrangians not meeting the neck, and Chanda [16] extends this to the case of
Lagrangians passing through the neck. For completeness, we sketch the modifica-
tions of the argument in [65] necessary to handle the case in hand. We assume that
we have chosen a broken divisor D = (D⊂, D⊃), and a family Dτν of Donaldson
hypersurfaces in Xτν limiting to D in the sense that Dτν is the pull-back of DY
on the neck region, as in [65, Lemma 5.15]. We suppose furthermore that we have
a collection of almost complex structures J(X) = (JΓ(X)) for X for which every
adapted holomorphic building in X of expected dimension at most one is regular


## Page 70


70
JOSEPH PALMER AND CHRIS WOODWARD
and for which there are no non-constant holomorphic spheres contained in D. By
[65, Lemma 5.29], there exists a collection J(Xτν) = (JΓ(Xτν)) of almost complex
structures for Xτν converging to J(X) so that every adapted stable map to Xτν of
expected dimension at most one is regular and for which there are no non-constant
holomorphic spheres contained in Dτν. Let
(Cν, uν : Cν →Xτν), τν →∞
be a sequence as in the statement of the Theorem. Since Cν is stable, after passing
to a subsequence the sequence Cν Gromov-converges to a limiting treed disk C.
The argument in [65, Step 2, Proof of Theorem 8.4] shows that the derivatives
of uν are bounded on the neck regions in Cν, as otherwise one would obtain by
rescaling a component of C mapping non-trivially into X but with no intersections
with D. This is impossible since D is a Donaldson hypersurface in each component.
On the neck region [−τν, τν] × Z ⊂Xτν, the restriction of u to each T ν
e is a
gradient trajectory. Suppose that uν|T ν
e intersections [−τν, τν] × Z. After passing
to a subsequence, the restriction (uν|T ν
e )−1([−τν, τν] × Z) converges to a gradient
trajectory in the cylinder R × Z for the height function. This condition implies
(78) in the limit ν →∞.
□
We will also need various compactness results for moduli spaces of buildings
under variation of the Lagrangian boundary condition. Let X⊂be a manifold with
a cylindrical end as in Definition 6.7. Let ϕ⊂: L⊂→X⊂denote an asymptotically
cylindrical Lagrangian embedding. By Proposition 6.11, the closure L⊂is contained
in a cleanly-self-intersecting Lagrangian submanifold of X⊂.
Definition 6.20. Denote by X⊂[k] the union of X⊂with k −1 neck pieces P(N± ⊕
C). A treed holomorphic building in X⊂is a collection of levels
(Ci, ui : Si →X⊂[k]i, i = 1, . . . , k)
as in Definition 6.3, satisfying matching conditions for any collection of inter-level
edges between ui and ui+1.
Any treed building in a broken manifold may be viewed as a pair of treed build-
ings in the corresponding cylindrical end manifolds, although not in a canonical
way. Let X = (X⊂, X⊃). A building in X[k] of type Γ consists of a building u⊂in
X⊂[k⊂] and a building u⊃in X⊃[k⊃] for some k⊂, k⊃with k = k⊂+ k⊃satisfying
matching conditions at the leaves e⊂∈Edge(Γ⊂), e⊃∈Edge(Γ⊃) corresponding to
Reeb chords and orbits that are glued to form Γ.
The key point in the following Theorem, whose proof will occupy the rest of
the section, is that the Lagrangians are not required to be cylindrical-near-infinity,
but only asymptotically cylindrical. As such, the Theorem is not a consequence
of known results about compactness of buildings with Lagrangian boundary con-
ditions.


## Page 71


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
71
Theorem 6.21. Given a sequence of asymptotically cylindrical Lagrangian bound-
ary conditions ϕ⊂,ν converging to some limiting boundary condition ϕ⊂(at least
in the C2 topology on submanifolds) and a sequence of stable holomorphic treed
buildings (Cν, uν : Cν →X⊂[kν]) bounding ϕ⊂,ν, there exists a subsequence of uν
converging to a stable holomorphic treed building u : C →X⊂[k] with boundary
(∂u)(S) mapping to the broken Lagrangian L⊂[k]. Furthermore, the limit of any
Gromov convergent sequence is unique.
We will need the following generalization of Gromov compactness for Lagrangian
boundary conditions with clean self-intersection in Schmäschke [54, Section 4].
Theorem 6.22. Let X be a compact symplectic manifold and ϕ : L →X a possibly
non-compact Lagrangian immersion with clean self-intersection. Let L0 ⊂L be a
compact subset of L that is a submanifold with boundary. Suppose that Jν is a
sequence of tamed almost complex structures on X converging in C2 to a limiting
tamed almost complex structure J. Suppose that uν : Sν →X is a sequence of
Jν-holomorphic maps with bounded area A(uν) bounding L0. Then a subsequence
of uν Gromov-converges to a J-holomorphic stable map u : S →X bounding L.
Sketch of proof. With L compact, the statement is the standard Gromov compact-
ness for clean intersection, as explained in [54, Section 4].
The extension is a
kind of target-local Gromov-compactness theorem.
One constructs the compo-
nents uv : Sv →X of the limit u : S →X by composing u with a sequence of
embeddings ϕv,ν : Sv,ν →Sν, where Sv,ν is obtained from Sv by removing a sequence
of small balls Bv,ν around the nodes Zv ⊂Sv. Consider a sequence ϕν : Sv,ν →Sν
so that the maps uν ◦ϕν have bounded first derivative on compact sets of Sv −Zv.
The compositions uν ◦ϕν have boundary in L0 and so converge, after passing to
a subsequence, to a collection of components uv : Sv −Bv,ν →X bounding L0,
uniformly on compact sets. The exponential decay results on cylinders and strips
with small energy (used to show that bubbles connect) follow by considering uν as
maps bounding L and do not require compactness of L.
□
Sketch of proof of Theorem 6.21. We indicate the modifications necessary for sft
compactness as presented in, for example, Venugopalan-Woodward [65] to go through.
Consider a sequence of treed disks (Cν, uν : Cν →X⊂) with bounded energy with
boundary values in L⊂. Because L⊂has clean self-intersection, Theorem 6.22 im-
plies the existence of a subsequence converging to a limit (C, u∞: C →X⊂) where
C is a treed disk with surface component S = S
v Sv mapping into the compactifi-
cation X⊂.
By adding marked points, we may assume that the limiting stable map has stable
domain. For example, choose a Donaldson hypersurface D ⊂X⊂transverse to the
limit u∞and add leaves to Cν according to the intersections of uν with D. We
denote by S◦
v the complement of the nodes in Sv. For each edge Te meeting Sv
choose ϵe small and denote by Bv(ϵ) = ∪eBTe∩Sv(ϵe) the complement of the ϵe-balls


## Page 72


72
JOSEPH PALMER AND CHRIS WOODWARD
around the intersection Te ∩Sv. The surface Sν is obtained by gluing together the
surfaces Sv −Bv(ϵν) for suitable choices of ϵe,ν converging to 0 as ν →∞. We
denote by uν,v the restriction of uν to Sv −Bv(ϵν).
Construct the levels of the limiting building by rescaling the target locally as
follows. By assumption, an open neighborhood of Y in X⊂is isomorphic to the
normal bundle N−of Y . Identify the complement N ×
−of the zero section with
R × Z as above, and consider the action es : N ×
−→N ×
−of scalar multiplication of
es for a real number s ∈R, equivalent to translation in the R-factor by s. Suppose
uv has image in Y . Fix a point z ∈S◦
v and choose a sequence sν,v ∈R so that the
translations esν,vuν,v(z) converge to a point in N ×
−. The argument in [65, Section
10.4] shows that the derivatives of uν,v are bounded with respect to the cylindrical-
end metric on S◦
v, so that after passing to a subsequence we may assume that uν,v
converges to a level in P(N± ⊕C).
It remains to show that the matching conditions between levels are satisfied.
Suppose that uv1 and uv2 are adjacent components of the limit connected by a
boundary node; the case of an interior node is similar. Denote by uν,e the restriction
of uν to the neck region [−ζe, ζe] × S1 resp. strip [−ζe, ζe] × S1 connecting the two
components of the limit. For z lying in some such strip, choose a sequence sν
so that the maps esνuν,e(z) converge. Since the derivative of uν,e is bounded and
the Lagrangians esνL⊂,ν converge in C∞to a boundary condition R × LZ, after
passing to a subsequence the maps esνuν,e(z) converge in C∞on compact sets to
a limit ue which is contained in a fiber of P(N−⊕C), necessarily with a single
intersection with the divisors at zero and infinity corresponding to the two ends
of Se,ν. The boundary conditions on esνue,ν converge to the cylindrical boundary
condition R × LZ as ν →∞. It follows that ue,ν converges to a trivial strip of the
form ue(s, t) = (µs, ϑµ(t)) in some fiber N ×
−,y ∼= R × S1 for some µ ∈R and Reeb
chord or orbit ϑµ with total angle change µ.
The Reeb orbit appearing in the limit on the thin parts of the surface is indepen-
dent of the choice of rescaling. Indeed, suppose by way of contradiction that there
exist two rescaling sequences esνue,ν and es′
νue,ν converging to different to trivial
cylinders corresponding to different Reeb chords or orbits ϑµ, γµ′ with different an-
gle changes µ, µ′. Since the angle change of ue,ν(s, ·) is a continuous function of s
and the set of angle changes
(95)
Z
γ∗α,
γ : [0, 1] →Z resp. S1 →Z
of Reeb chords and orbits is discrete, the intermediate value theorem implies the
existence of a rescaling sequence s′′
ν for which the limit of es′
νue,ν(0, ·) has angle
change µ′′ ∈(µ, µ′) which is not the angle change of any Reeb chord or orbit. This
is a contradiction.
The limiting building is constructed as follows. Assign each component uv to
a level Si by comparing the translation sequences sv,ν necessary to construct the


## Page 73


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
73
limit. By the discussion from the previous paragraph, if two components uv−, uv+
are in different levels and are joined by an edge then for one of the components, say
uv−, the image of Sv−∩Sv+ maps to the divisor at infinity in P(N−⊕C) and the
other maps to the divisor at zero. After possibly adding trivial strip or cylinders,
we obtain a building (C, u) with the matching conditions that the Reeb chords at
either side of the node match, the projections to Y match on either side of the
node, and the matching occurs at the same copy of Y in X⊂[k]. Since the limit
in X⊂was unique and the rescaling sequences sν,v are unique up to addition of
constants, the limiting building in X⊂[k] is unique up to translation in the neck
pieces. The statement of the Theorem follows.
□
6.4. Transversality for buildings. Regularization of the moduli spaces of build-
ings may be carried out using Donaldson hypersurfaces following Charest-Woodward
[18] and Venugopalan-Woodward [65]. We modify the construction to allow bound-
ary in asymptotically-cylindrical broken Lagrangians
L = (L⊂, L⊃).
The broken analog of Theorem 4.18 gives an inductive construction of regular
perturbation data. For any type Γ we denote by MΓ(X, ϕ) the regularized moduli
space of buildings with type Γ. As in Proposition 6.15, the moduli space of buildings
MΓ(X, ϕ) is locally cut out by a Fredholm map. Let Ci ⊂C denote the subset of the
domain mapping to X[l]i(v±), and ui the restriction of u to Ci. In the construction
of the linearized operator, we will focus on the surface parts Si ⊂Ci. Using the
Sobolev norms from (89), let
BΓ ⊂MΓ × Πl
i=0 Map(S◦
i , X[l]i)k,p,λ
be the space of maps of class k, p from each S◦
i to the spaces X[l]i, lifting to a map
to L[l]i on the boundary, and satisfying the following conditions: The matching
conditions along cylindrical and strip-like ends via the evaluation maps including
(90) and the deformed matching conditions of (40). The linearized operator for
such buildings is defined as in the discussion after (92).
Definition 6.23. The linearized operator for a holomorphic building (S, u) is
˜Du : T(C,u)BΓ
→
Ω0,1(S◦, u∗TX)k−1,p,λ
(96)
(ζ, ξ)
7→
Duξ + 1
2JduDj(ζS)
(97)
where T(C,u)BΓ = {(ζ, ξ)} restricts to deformations ξ satisfying in addition to the
conditions in (33) the matching conditions at infinity
eve(ξSi) = eve(ξSi+1)
for all edges e of Γ connecting different levels Si, Si+1. A holomorphic building
u : S →X is called regular if the operator ˜Du is surjective.


## Page 74


74
JOSEPH PALMER AND CHRIS WOODWARD
Theorem 6.24. For any broken type Γ, given perturbations PΓ′ for strata MΓ′(X, ϕ)
with Γ′ ≺Γ, there exists a perturbation PΓ so that for each uncrowded map type
Γ with underlying domain type Γ and expected dimension at most one, the closure
of MΓ(X, ϕ) is contained in the uncrowded locus and is a finite set or a compact
one-manifold with boundary.
Sketch of proof. The proof of this theorem is similar to that in Charest-Woodward
[18, Theorem 4.20].
At any point (C, u : C →X, PΓ) in the universal moduli
space Muniv,i
Γ
(X, ϕ) one must show that any element in the cokernel of ˜Du vanishes.
The elements of the cokernel η = (ηv) have vanishing restriction ηv = 0 to any
component Sv on which u has non-trivial horizontal derivative. The restriction ηv
of η must satisfy D∗
uvηv = 0 and be perpendicular to domain-dependent variations
of the cylindrical almost-complex structure JΓ. The last condition in particular
implies that ηv vanishes in a neighborhood of any point at which d(p ◦u) is non-
zero. The claim follows by unique continuation.
Multiple covers of trivial cylinders, meaning maps whose image is contained in
a fiber of the projection R × Z →Y , are transversally cut out. Indeed, if u maps
to R × Zy for some y ∈Y then the Cauchy-Riemann operator Du splits
Du ∼= ∂TyY ⊕Dv
u
as the standard Cauchy-Riemann operator ∂TyY on maps to TyY with boundary
TyLY plus the linearized operator Dv
u for a map of a genus zero surface S◦
v into the
fiber C−{0} with boundary conditions (R∪iR)−{0}. Such operators are surjective
by any number of arguments; for example, by Proposition 6.18, Dv
u compactifies to
a rank one Cauchy-Riemann operator Dv
u with a non-trivial kernel
ker(Dv
u) ∼= R
given by dilation. In rank one, any Cauchy-Riemann operator cannot have both
non-trivial kernel and cokernel by Oh [48]. It follows that the cokernel of Dv
u must
vanish. Similarly, ∂TyY has non-trivial kernel and vanishing cokernel as well, so Du
is surjective. In particular, the usual problem in symplectic field theory of multiple
covers of trivial cylinders or strips lacking regularity does not occur. Thus, the
operator ˜Duv on any component uv that covers a trivial cylinder is surjective. In
particular, ηv = ˜Duvξv for some ξv possibly with non-trivial evaluations on the ends
of Sv.
An induction shows that the restriction of ˜Du to any union of components Sv
that are covers of trivial components, or on which the map is constant, is also
surjective: The kernel of Du on any disk with strip like ends consists of constant
sections and is identified with R ⊕TyY via the splitting of the symplectization. As
such, the matching conditions are cut out transversally as in the proof of Theorem
4.18. Thus there are no non-trivial elements of the cokernel. Compare also Ekholm
[26, Lemma 6.4] and especially Venugopalan-Woodward [65, Corollary 6.35] where a
similar proof is given for the context of multi-directional symplectic field theory.
□


## Page 75


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
75
6.5. Gluing with Lagrangian boundary conditions. The gluing argument
produces from any holomorphic building a limiting family of holomorphic maps.
The proof is probably standard and similar to that in Charest-Woodward [18].
First recall the gluing construction on domains and targets.
Definition 6.25. Given gluing parameters δ1, . . . , δk > 0, the glued domain Sδ1,...,δk
is obtained from S by gluing necks [−| ln(δi)|/2, | ln(δi)|/2]×S1 of length | ln(δi)| at
each node of S separating two levels. There is a similar construction of the glued
target Xδ obtained by gluing in a neck of length | ln(δ)| in X.
For simplicity we state the gluing result for the case of two levels only:
Theorem 6.26. Let X = X⊂∪Y X⊃and L = L⊂∪LY L⊃be a broken rational
symplectic manifold and rational self-transverse immersed cylindrical-near-infinity
broken Lagrangian in the sense of (76). Suppose that (C, u : C →X) is a regular
treed building with limiting eigenvalues µ1, . . . , µk of Reeb chords or orbits at the
separating hypersurface Y ⊂X with boundary in ϕϵ for some ϵ < 0. Then there
exists δ0 > 0 such that for each gluing parameter δ ∈(0, δ0) there exists a treed
building
(Cδ/µ1,...,δ/µk, uδ : Sδ/µ1,...,δ/µk →Xδ)
with the property that uδ depends smoothly on δ. Furthermore the Gromov limit
recovers the original map:
lim
δ→0 uδ = u.
We construct from any holomorphic building a holomorphic map to the man-
ifold with long neck, using Floer’s version of the Picard Lemma. Afterwards we
show that any such map for sufficiently long neck length is obtained by such a
construction. Recall Floer’s version of the Picard Lemma, [28, Proposition 24]).
Lemma 6.27. Let f : V1 →V2 be a smooth map between Banach spaces that
admits a Taylor expansion
f(v) = f(0) + df(0)v + N(v)
satisfying the following condition: There exists a constant C > 0 such that df(0) :
V1 →V2 has a right inverse G : V2 →V1 satisfying the uniform bound
∥GN(u) −GN(v)∥≤C(∥u∥+ ∥v∥)∥u −v∥,
∀u, v ∈V1.
Let Bϵ(0) denote the open ϵ-ball centered at 0 ∈V1 and assume that
∥Gf(0)∥≤1/(8C).
For ϵ < 1/(4C), the zero-set of f −1(0) ∩Bϵ(0) is a tranversally-cut-out (hence
smooth) submanifold of dimension dim(Ker(df(0))) diffeomorphic to the ϵ-ball in
Ker(df(0)).


## Page 76


76
JOSEPH PALMER AND CHRIS WOODWARD
Proof of Theorem. To simplify notation, we consider only the case that the build-
ing consists of a pair of maps joined by strip-like ends; the general case is left to
the reader. To construct the approximate solution, we begin by recalling the con-
struction of the deformation of a complex curve at a node. Let S be a broken curve
with two sublevels S+, S−. Let δ > 0 be a small gluing parameter. Variations of
the domain may be represented as variations of the conformal structure on a fixed
curve together with variations of the edge lengths. Let
u−: S−
→
X−:= X⊂
u+ : S+
→
X+ := X⊃
be maps from components S∓containing points w± ∈S± corresponding to the
ends satisfying (77) so that u = (u−, u+) form a building in X. Let Γ± denote the
combinatorial types of the domains of u± and let
(98)
Si
Γ± →Mi
Γ± × S±, , i = 1, . . . , l
be local trivializations of the universal treed disk. These local trivializations iden-
tify each nearby fiber with (S±, z, w) such that each point in the universal treed
disk is contained in one of the local trivializations (98). We may assume that Mi
Γ±
is identified with an open ball in Euclidean space so that nodal fiber containing
S−∪S+ lies over 0. Similarly, we assume we have a local trivialization of the univer-
sal bundle near the glued curve as a smooth fiber bundle. The local trivialization
gives rise to a family of complex structures
(99)
Mi
Γ →J (Sδ)
that are constant on the neck region. We consider metrics on the punctured curves
S◦
± that are cylindrical on the neck region. That is, on the images of the maps
κC,± : ±[0, ∞) × [0, 1] →S±
the metrics are the product of the standard metrics on the two factors. By as-
sumption we have cylindrical ends so that the images of
κX,± : ∓[0, ∞) × Z →X±
are isometric.
Both the glued target Xδµ and glued domain Sδ are defined by
removing the part of the end with |s| > | ln(δ)| and identifying
(s, t) ∼(s −| ln(δ)|, t)
(s, t) ∈(0, | ln(δ)|) × S1
(s, t) ∼(s −|µ ln(δ)|, t)
(s, t) ∈(0, | ln(δ)|) × Z.
The prerequisite for Floer’s version of the Picard lemma is an approximate solu-
tion to the Cauchy-Riemann equation on the glued curve. Choose a cutoff function
(100)
β ∈C∞(R, [0, 1]),



β(s) = 0
s ≤0
β(s) = 1
s ≥1 .


## Page 77


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
77
We denote by expx : TxXδ →Xδ geodesic exponentiation, using the given cylindri-
cal metric on the neck region. We write using geodesic exponentiation in cylindrical
coordinates
u±(s, t) = exp(∓µs,tµz)(ζ±(s, t)).
Define upre
δ
to be equal to u± away from the neck region, while on the neck region
of Sδ with coordinates s, t define
(101)
upre
δ (s, t) = exp(µs,tµz)(ζδ(s, t)),
ζδ(s, t) = β(−s)ζ−
 
−s + | ln(δ)|
2
, t
!
+ β(s)ζ+
 
s −| ln(δ)|
2
, t
!
.
In other words, one translates u+, u−by some amount | ln(δ)|, and then patches
them together using the cutoff function and geodesic exponentiation.
To obtain the estimates necessary for the application of the Picard lemma, we
work in Sobolev spaces with weighting functions close to those needed for the
Fredholm property on cylindrical and strip-like ends in (88). The surface part Sδ
satisfies a uniform cone condition and the metrics on Xδµ are uniformly bounded.
These uniform estimates imply uniform Sobolev embedding estimates and multi-
plication estimates. Denote by
(s, t) ∈
"
−| ln(δ)|
2
, | ln(δ)|
2
#
× S1
the coordinates on the neck region in Sδ created by the gluing. For λ > 0 small,
define a Sobolev weight function
ℵδ
λ : Sδ →[0, ∞),
(s, t) 7→β
 | ln(δ)|
2
−|s|
!
pλ
 | ln(δ)|
2
−|s|
!
.
By definition ℵδ
λ is zero on the complement of the neck region. We will also use
similar weight functions on the punctured curves
ℵ±
λ : S◦
± →[0, ∞),
(s, t) 7→β(|s|)pλ|s|.
Holomorphic maps near the pre-glued solution are cut out locally by a smooth map
of Banach spaces. Given an element m ∈Mi
Γ and a section ξ : Sδ →u∗TXδ define
as in Abouzaid [3, 5.38] a norm based on the decomposition of the section into a
part constant on the neck and the difference:
(102)
∥(m, ξ)∥p
1,p,λ := ∥m∥p + ∥ξ∥p
1,p,λ
∥ξ∥p
1,p,λ := ∥(ξ(0, 0))∥p +
Z
Sδ(∥∇ξ∥p
+ ∥ξ −β(| ln(δ)|/2 −|s|)T u(ξ(0, 0))∥p) exp(ℵδ
λ)d VolSδ


## Page 78


78
JOSEPH PALMER AND CHRIS WOODWARD
where T u is parallel transport from upre(0, t) to upre(s, t) along upre(s′, t). Pointwise
geodesic exponentiation defines a map (using Sobolev multiplication estimates)
(103)
expupre
δ
: Ω0(Sδ, (upre
δ )∗TXδµ)1,p,λ →Map1,p(Sδ, Xδµ)
and Map1,p(Sδ, Xδµ) denotes maps of class W loc
1,p from Sδ to Xδµ. In the case of
Lagrangian boundary conditions, we have a similar map assuming that the expo-
nential map sends tangent vectors to the Lagrangian to points in the Lagrangian
boundary condition; we omit the Lagrangian boundary condition from the nota-
tion. Similarly, for the punctured surfaces we have Sobolev norms
(104)
∥(m, ξ)∥1,p,λ :=

∥m∥p + ∥ξ∥p
1,p,λ
1/p ,
∥ξ∥1,p,λ :=
 ∥ξ(±∞, 0)∥p +
R
S◦
±(∥∇ξ∥p+
∥ξ −β(|s|)T uξ(±∞, 0)∥p) exp(ℵ±
λ )d VolS◦
±
!1/p
where the limits ξ(±∞, t) are assumed to exist. Geodesic exponentiation defines
maps
(105)
expupre
δ
: Ω0(S◦
±, (upre
δ )∗TX)′
1,p,λ →Map1,p,λ(S◦
±, X◦
±)
where, by definition, Map1,p,λ(S◦
±, X◦
±) is the space of W loc
1,p maps from S◦
± to X±
that differ from a Reeb chord at infinity by an element of Ω0(S◦
±, (upre
δ )∗TX◦
±)′
1,p,λ
(which may vary at infinity because of the inclusion of constant maps on the end
in the Banach space). In the case of the cylindrical end manifolds , the assumption
λ small on the Sobolev decay constant implies that the linearized operators
Du± : Ω0(S◦
±, u∗
±TX±)′
1,p,λ →Ω0,1(S◦
±, u∗
±TX±)0,p,λ
are Fredholm. The kernel contains any infinitesimal variation of the map by Lemma
6.14. By the regularity assumption, the fiber products
(106)
ker( ˜Du−) ×ev∞,−,ev∞,+ ker( ˜Du+)
are transversally cut out, where ev∞,± are the maps of (90).
The space of holomorphic maps near the pre-glued solution is cut out locally by
a smooth map of Banach spaces. For a 0, 1-form η ∈Ω0,1(Sδ, u∗TX) define
∥η∥0,p,λ =
Z
Sδ ∥η∥p exp(ℵδ
λ)d VolSδ
1/p
.
Parallel transport using an almost-complex connection defines a map
Tupre
δ (ξ) : Ω0,1(Sδ, (upre
δ )∗TX)0,p,λ →Ω0,1(Sδ, (expupre
δ (ξ))∗TX)0,p,λ.
Because we are working in the adapted setting, our curves Sδ are attached to a
collection of interior leaves Te1, . . . , Ten. We require
(107)
(expupre
δ (ξ))(Tei) ∈D,
i = 1, . . . , n.


## Page 79


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
79
By choosing local coordinates near the attaching points we = Te∩S, the constraints
(107) may be incorporated into the map Fδ to produce a map
(108)
Fδ : Mi
Γ × Ω0(Sδ, (upre
δ )∗TX, (∂upre
δ )∗TL)′
1,p,λ →Ω0,1(Sδ, (upre
δ )∗TX)0,p,λ × V
where the space V is the direct sum of additional factors enforcing the matching and
divisor conditions; namely those in (77) together with the sum
Ln
e=1 Tu(we)X/Tu(we)D
enforcing the conditions that the interior markings map to the Donaldson hyper-
surface. The first component of this map is
Fδ(m, ξ) =

Tupre
δ (ξ)−1∂JΓ,HΓ,j(m) expupre
δ (ξ), . . .

.
Zeroes of Fδ correspond to adapted holomorphic maps near the preglued map upre
δ .
The expression Fδ(0) has contributions created by the cutoff function and difference
in the maps:
∥Fδ(0)∥0,p,λ
=





∂JΓ,HΓ exp(µs,tµz)
 
β(−s)ζ−
 
−s + | ln(δ)|
2
, t
!
+β(s)ζ+
 
s −| ln(δ)|
2
, t
!!




0,p,λ
=





 
D exp(µs,tµz)
 
dβ(−s)ζ−
 
−s + | ln(δ)|
2
, t
!
+ dβ(s)ζ+
 
s −| ln(δ)|
2
, t
!!
+
 
β(−s)dζ−
 
−s + | ln(δ)|
2
, t
!
+ β(s)dζ+
 
s −| ln(δ)|
2
, t
!!!0,1





0,p,λ
.
Holomorphicity of u± implies an estimate
(109)






  
β(−s)dζ−
 
−s + | ln(δ)|
2
, t
!
+ β(s)dζ+
 
s −| ln(δ)|
2
, t
!!!0,1





0,p,λ
≤ce−| ln(δ)|(1−λ) = cδ1−λ,
cf. Abouzaid [3, 5.10]. Similarly, from the terms involving the derivatives of the
cutoff function and exponential convergence of ζ± to 0 we obtain an estimate
(110)
∥Fδ(0)∥0,p,λ < c exp(−| ln(δ)|(1 −λ)) = cδ1−λ
with c independent of δ.


## Page 80


80
JOSEPH PALMER AND CHRIS WOODWARD
To perform the iteration, we apply a uniformly bounded right inverse to the
failure of the approximate solution to solve the Cauchy-Riemann equation. Given
η ∈Ω0,1(Sδ, (upre)∗TX)0,p
one obtains elements
η = (η−, η+) ∈Ω0,1(S±, u∗
±TX±)
by multiplication with the cutoff function β and parallel transport T u± to u± along
the path
exp(µs,tµz)(ρ(ζδ(s, t) + (1 −ρ)ζ±(s, t))),
ρ ∈[0, 1].
Define
η+ = T u+β(s −1/2)η,
η−= T u−β(1/2 −s)η.
Since the fiber product (106) is transversally cut out, there exists
(ξ+, ξ−) ∈Ω0(S±, u∗TX±)1,p,λ,
Du±ξ± = η±,
ev∞(ξ+) = ev∞(ξ−)
where ev∞are the evaluation-at-infinity maps of (90). Denote
ξ∞= ev∞(ξ±) ∈R × Tev∞(u±)Z.
Define Qδη equal to (ξ−, ξ+) away from [−| ln(δ)|
2
, | ln(δ)|
2
] × Z and on the neck region
by patching the solutions (ξ−, ξ+) together using a cutoff function that vanishes
three-quarters of the way along the neck:
(111)
Qδη := β

−s + 1
4| ln(δ)|

((T u−)−1ξ−−T uξ∞)
+ β

s + 1
4| ln(δ)|

((T u+)−1ξ+ −T uξ∞)
+ T uξ∞∈Ω0,1(Sδ, (upre
δ )∗TX)1,p,λ
where T u± denotes parallel transport to u± from upre
δ
along the path
exp(µs,tµz)(ρ(ζδ(s, t) + (1 −ρ)ζ±(s, t))), ρ ∈[0, 1].
Since
η = (T u−)−1η−+ (T u+)−1η+
we have
∥DuδpreQδη −η∥1,p,λ
=
∥Dupre
δ Qδη −(T u−)−1Duδ
−ξ−−(T u+)−1Duδ
+ξ+∥1,p,λ
≤
c exp((1 −λ)| ln(δ)/4|)∥η∥0,p,λ
+c∥dβ(s −| ln(δ)|/4)Qδ
−η∥0,p,λ
+c∥dβ(−s + | ln(δ)|/4)Qδ
+η∥0,p,λ


## Page 81


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
81
where the first term arises from the difference between Dupre
δ
and (T u±)−1Du±T u±
and the second from the derivative dβ of the cutoff function β. The difference in
the exponential factors
ℵ±
λ = ℵδ
λ exp(±2sλ),
∓s ≥| ln(δ)|
2
in the definition of the Sobolev weight functions implies that possibly after changing
the constant c, we have since | ln(δ)| = −ln(δ)
∥dβ(s −| ln(δ)|/4)Qδ
±η∥1,p,λ < ce−λ | ln(δ)|
2
= cδλ/2.
Hence one obtains an estimate as in Fukaya-Oh-Ohta-Ono [31, 7.1.32], Abouzaid
[3, Lemma 5.13]: for some constant c > 0, for any δ > 0,
(112)
∥Dupre
δ Qδ −Id ∥< c min(δλ/2, δ(1−λ)/4).
It follows that for δ sufficiently large an actual inverse may be obtained from the
Taylor series formula
D−1
upre
δ
= Qδ(Dupre
δ Qδ)−1 =
X
k≥0
Qδ(I −QδDupre
δ )k.
The variation in the linearized operators can be estimated as follows.
After
redefining c > 0 we have for all ξ1, ξ sufficiently small
(113)
∥DξFδ(0, ξ1) −Dupre
δ ξ1∥≤C∥ξ1∥1,p,λ∥ξ∥1,p,λ.
To prove this we require some estimates on parallel transport. Let
T δ,x
z
(m, ξ) : Λ0,1T ∗
z Sδ ⊗TxX →Λ0,1
jδ(m)T ∗
z Sδ ⊗Texpx(ξ)X
denote pointwise parallel transport. Consider its derivative
DT δ,x
z
(m, ξ, m1, ξ1; η) = ∇t|t=0Tupre
δ (m + tm1, ξ + tξ1)η.
For a map u : S →X we denote by DTu the corresponding map on sections. By
Sobolev multiplication (for which the constants are uniform because of the uniform
cone condition on the metric on Sδ and uniform bounds on the metric on Xδµ) there
exists a constant c such that
(114)
∥DT δ,x
u (m, ξ, m1, ξ1; η)∥0,p,λ ≤c∥(m, ξ)∥1,p,λ∥(m1, ξ1)∥1,p,λ∥η∥0,p,λ.
Differentiate the equation
T δ,x
u (m, ξ)Fδ(m, ξ) = ∂JΓ,HΓ,jδ(m)(expuδpre(ξ))
with respect to (m1, ξ1) to obtain
(115)
DTuδpre(m, ξ, m1, ξ1, Fδ(m, ξ)) + T δ
u (m, ξ)(DFδ(m, ξ, m1, ξ1)) =
(D∂)jδ(m),expupre
δ
(ξ)(Djδ(m, m1), D expuδ(ξ, ξ1)).


## Page 82


82
JOSEPH PALMER AND CHRIS WOODWARD
Using the pointwise inequality
|Fδ(m, ξ)| < c|dexpupre
δ
(z)(ξ)| < c(|dupre
δ | + |∇ξ|)
for m, ξ sufficiently small, the estimate (114) yields a pointwise estimate
|Tupre
δ (ξ)−1DTuδpre(m, ξ, m1, ξ1, Fδ(m, ξ))| ≤c(|duδ
pre| + |∇ξ|) |(m, ξ)| |(ξ1, m1)|.
Hence
(116)
∥Tupre
δ (ξ)−1DTuδpre(m, ξ, m1, ξ1, Fδ(m, ξ))∥0,p,λ
≤c(1 + ∥duδ∥0,p,λ + ∥∇ξ∥0,p,λ)∥(m, ξ)∥L∞∥(ξ1, m1)∥L∞.
It follows that
(117) ∥Tupre
δ (ξ)−1DTuδpre(m, ξ, m1, ξ1, Fδ(m, ξ))∥0,p,λ ≤c∥(m, ξ)∥1,p,λ∥(m1, ξ1)∥1,p,λ
since the W 1,p norm controls the L∞norm by the uniform Sobolev estimates. As
in McDuff-Salamon [45, Chapter 10], Abouzaid [3] there exists a constant c > 0
such that for all δ sufficiently small,
(118)
∥Tuδpre(ξ)−1Dexpupre
δ
(ξ)(Dmjδ(m1), Dexpuδpre(ξ)ξ1)) −Dupre
δ (m1, ξ1)∥0,p,λ
≤c∥m, ξ∥1,p,λ∥m1, ξ1∥1,p,λ.
Combining the estimates (117) and (118) and integrating completes the proof of
claim (113). Applying the estimates (110), (112), (113) produces a unique solution
m(δ), ξ(δ) to the equation
Fδ(m(δ), ξ(δ)) = 0
for each δ, such that the maps
uδ := expupre
δ (ξ(δ))
depend smoothly on δ.
Note that the implicit function theorem by itself does
not give that the maps uδ are distinct, since each uδ is the result of applying the
contraction mapping principle in a different Sobolev space.
□
We now state the main result on the behavior of the moduli spaces under the
neck-stretching limit. Let M<E(X, ϕγ, D) denotes the locus in M(X, ϕγ, D) with
area less than E. Similarly, let M<E(X, ϕγ, D) denote the locus with area less than
E in M(X, ϕγ, D).
Theorem 6.28. Let X = X⊂∪Y X⊃be a broken rational symplectic manifold and
ϕ : L →X a broken self-transverse Lagrangian immersion in the sense of (76).
Suppose perturbations P = (PΓ) have been chosen so that every rigid labeled map
in M<E(X, ϕγ, D, σ) is regular. There exists δ0 such that for δ < δ0, the assignment
[u] 7→[uδ] from Theorem 6.26 defines a bijection between the rigid moduli spaces
M<E(X, ϕγ, D, σ)0 and M<E(Xδ, ϕγ, D, σ)0.


## Page 83


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
83
Proof. To prove injectivity of gluing, suppose that uδν = vδν for some pseudoholo-
morphic buildings u ̸= v and gluing parameters δν →0. Then the sequence uδν
has two stable Gromov limits, which is a contradiction to Theorem 6.19.
To prove surjectivity of gluing, it suffices to prove the following: Given a con-
verging family u′
δ with parameter δ converging to u, the map u′
δ is close to uδ in
the norms used in the gluing formula. Indeed, this closeness implies that u′
δ = uδ
by the uniqueness part of the implicit function theorem.
To check the necessary exponential decay, note the map on the neck region
may be decomposed into horizontal and vertical component. First consider the
horizontal part of the map pY ◦u′
δ : Sδ →Y . Denote by R(l) the rectangle
R(l) = [−l/2, l/2] × [0, 1].
Since there is no area loss in the limit δ →0, for any C > 0 there exists δ′ > δC
such that the restriction of pY ◦u′
δ to the annulus R(| ln(δ′)|/2) satisfies the energy
estimate of [30, Lemma 3.1]. Thus
(119)
pY u′
δ(s, t) = exppY upre
δ
(s,t) ξh(s, t),
∥ξh(s, t)∥≤C(eπ(−| ln(δ′)|/2−s)+eπ(−| ln(δ′)|/2+s))
s ∈[−| ln(δ′)|/2, | ln(δ′)|/2].
A similar estimate holds for the higher derivatives Dkξh(s, t) by elliptic regularity,
for any k ≥0. The necessary exponential decay result on the neck region is proved
in the case of cylinders in Venugopalan-Woodward [65, (8.13)]; the case of strips is
similar.
□
Corollary 6.29. If M<E(X, ϕγ, D)0 is regular, then there exists δ0 such that for
δ > δ0, M<E(Xδ, ϕγ, D)0 is regular.
Proof. We may assume that every (Cδ/µ1,...,δ/µk, uδ) in M<E(Xδ, ϕγ, D) for δ suf-
ficiently small is obtained by an application of Lemma 6.27 to the approximate
solution in the proof of Theorem 6.26. By the transversality statement in the Pi-
card Lemma 6.27, the nearby solution uδ produced from u0 by the implicit function
theorem also has surjective linearized operator ˜Duδ. (In fact, the operator is sur-
jective even restricting to variations of conformal structure on Cδ/µ1,...,δ/µk arising
from variations on S.)
□
We will need a similar bijection for the case of buildings in X⊂consisting of a
map u⊂: S⊂→X⊂and a neck piece u0 : S0 →P(N−⊕C), where the Lagrangian
L⊂in X⊂is only asymptotically cylindrical.
Theorem 6.30. Let Γ be a type of building in X⊂with two components as above.
Suppose perturbations P = (PΓ) have been chosen so that every rigid labeled map in
MΓ(X, ϕγ, D, σ) is regular, and let Γ′ be the type with a single level in X⊂obtained
by gluing. Then each u ∈MΓ(X, ϕγ, D, σ) is in the closure of a unique component
of MΓ′(X, ϕγ, D, σ).


## Page 84


84
JOSEPH PALMER AND CHRIS WOODWARD
Proof. The statement of the Theorem is a type of result known as “surjectivity of
gluing” in the literature (as in for example [54, Section 7.6]) in which one must
show that the sequence on the long cylinders is close to the approximate solution
in the chosen Sobolev norm. Let u be as in the statement of the Theorem. By
the gluing construction, there exists a one-parameter family uδ of buildings of type
Γ′ Gromov-converging to u in the limit δ →0. To see that uδ is the unique such
limit, it suffice to check that if u′
ν converges to u = (u⊂, u0) then u′
ν is close to the
approximate solution upre
δ
of (101).
To prove this, we examine the vertical and horizontal parts of the map. Denote
by u the map to X⊂obtained by projecting u0 to the base Y of the neck piece
P(N−⊕C). Similarly, let uν denote the map to X⊂induced by uν. Then uν Gromov
converges to u, and in particular the domain Cν of uν converges to the domain C
of u. Hence Cν is obtained from C by removing small balls around the node and
gluing in cylinders of length | ln(δν)| for some sequence of gluing parameters δν.
Let y ∈Y be the image of the node in u. We trivialize the bundle R × Z →Y in
a neighborhood Bϵ(y) of y. Denote by
e−τν : R × Z →R × Z,
(σ, z) 7→(σ −τν, z)
translation by −τν. We may pass to a subsequence so that
lim
ν→∞e−τνuν(0, 0) = (0, z)
for some point (0, z) over y. By the annulus lemma for maps to X⊂, we have on
the long strips of length | ln(δν)| connecting the components
(120)
uν(s, t) = expy ξ(s, t),
∥ξ(s, t)∥≤C(eπ(s−| ln(δν)|/2)µ0 + eπ(−| ln(δν)|/2−s)µ0)
s ∈[−| ln(δν)|/2, | ln(δν)|/2]
where the exponential decay constant µ0 is determined by the angles at the clean
intersection; see Abouzaid [3, 10.12].
To control the Sobolev norms of the vertical part of the map on the neck pieces,
we compare the given almost complex structure and boundary conditions to a
model problem in which the almost complex structure and boundary conditions
are constant. Let
y(s, t) = p(e−τνuν(s, t)) ∈Y,
s ∈[−| ln(δν)|/2, | ln(δν)|/2]
be the projection of the given map to Y . Choose local coordinates on Bϵ(y) so that
LY is linear. Denote by L±
⊂the branches of L⊂containing the images of uν(s, t) for
t = 0 resp. t = 1 and s sufficiently large and θ± ∈S1 the angles of the branches at
y. Define affine-linear model boundary conditions in R × S1 × Bϵ(y) by
Lmodel,±
ν
= R × {θ±} × LY .
Let σν be the R-coordinate of the evaluations uν(0, 0). Define T ±
ν by
u([−| ln(δν)|/2, | ln(δν)|/2] × {0}) = [T −
ν , T +
ν ].


## Page 85


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
85
Since L⊂has smooth cleanly-self-intersecting compactification L⊂in X⊂, the trans-
lations
e−τν(L±
⊂∩[T −
ν + τν, T +
ν + τν] × Z) ⊂R × S1 × Bϵ(y)
differ from Lmodel,±
ν
near u(s, t) by a map
β± : L±
⊂∩

[T −
ν + τν, T +
ν + τν] × Z

→NLmodel,±
ν
satisfying an exponential decay estimate
(121)
∥e−τνβ±(σ, z)∥≤C(e−τν−σ + dist(z, z′))
σ ∈[T −
ν , T +
ν ], z ∈Lmodel
ν
∩Z.
Choose a diffeomorphism identifying the boundary condition with its model
ψν ∈Diff(R × S1 × Bϵ),
ψν(e−τνL±
⊂) = Lmodel,±
ν
.
Because of (121), the diffeomorphism Dψν may be taken to satisfy an estimate
similar to that for the boundary conditions:
(122)
∥Dψν(σ, z′) −Id ∥≤C(e−τν−σ + dist(z, z′))
σ ∈[T −
ν , ∞).
The composition ψνe−τνuν satisfies the model boundary conditions and the Cauchy-
Riemann equation up to an error term arising from the failure of the map ψν to
be J-holomorphic: Let J0(t) denotes the almost complex structure obtained by
evaluating at ψνe−τνuν(0, t). By assumption, the R-derivative of uν(s, t) on the
neck so that if σν(s, t) denotes the R coordinate of e−τνuν(s, t) then for any ϵ > 0
we have for ν sufficiently large
∂sσν(s, t) ∈
µ
2, 3µ
2

.
This implies
|σν(s, t) −σν(0, t)| ≥µ
2|s|.
Let
umodel(s, t) = (µs, tµz)
as in (101). As in the discussion around (95), we have
pZ(ψνe−τνuν(sν, t)) →tµz
in
C∞([0, 1])
for any sequence sν with |sν|/| ln(δν)| →0. Define
ζν(s, t) = (ψνe−τνuν)(s, t) −umodel(s, t).
Then ζν satisfies linear totally-real boundary conditions and is approximately holo-
morphic: Since the difference between J and J0 depends only on the projection to
Y , after re-defining µ0 we have
∥∂J0ζν(s, t)∥
≤
∥∂Jζν(s, t)∥+ ∥(∂J −∂J0)ζν(s, t)∥
≤
C(e−τv−µ(s−| ln(δν)|/2)/2 + e(s−| ln(δν)|/2)µ0 + e(| ln(δν)|/2−s)µ0)
s ∈[−| ln(δν)|/2, | ln(δν)|/2]


## Page 86


86
JOSEPH PALMER AND CHRIS WOODWARD
where the first term arises from exponential convergence of the vertical part of the
boundary conditions, and the second from the annulus lemma for the horizontal
map. Write
ην := ∂J0ζν ∈Ω0,1([−| ln(δν)|/2, | ln(δν)|/2] × [0, 1], Cn).
Denote by
fi ∈C∞([0, 1], R2n), i ∈I
the eigenfunctions of J0∂t with boundary conditions the linear subspaces TLmodel,±
ν
and the eigenvalues λi ∈R, the operator J0∂t being self-adjoint. Consider the de-
composition of the maps ζν, ην into eigenfunctions of J∂t with boundary conditions
TLmodel,±
ν
with coefficients cν,i, dν,i ∈R:
ζν(s, t) =
X
i∈I
cν,i(s)fi(t),
ην(s, t) =
X
i∈I
dν,i(s)fi(t).
We obtain a solution for the coefficients by integration
cν,i(s)
=
cν,i(| ln(δν)|/2) exp
 
λi(s −| ln(δν)|/2) +
Z s
| ln(δν)|/2 dν,i(s′)ds′
!
(123)
=
cν,i(−| ln(δν)|/2) exp
 
λi(s + | ln(δν)|/2) +
Z s
−| ln(δν)|/2 dν,i(s′)ds′
!
.
(124)
We may assume, by redefining µ0, that the exponential decay constant µ0 is smaller
than the minimum of the non-zero eigenvalues |λi|. For any i ∈I, (123) gives
(125)
∥cν,i(s)∥≤C

∥cν,i(| ln(δν)|/2)∥e(s−| ln(δν)|/2)µ0 + ∥cν,i(−| ln(δν)|/2)∥e(−| ln(δν)|/2−s)µ0
s ∈[−| ln(δν)|/2, | ln(δν)|/2].
Using elliptic estimates, one obtains similar estimates for the derivatives of ζν. We
obtain by (125) and elliptic regularity that for any constant C, for ν sufficiently
large the estimate
(126)
∥ψνe−τνuν(s, t) −umodel(s, t)∥k,2,λ < C(1 + δµ0−λ
ν
/(µ0 −λ))
holds for any k ≥0.
Note that in the norm defined in (104), the zero modes
ci(s, t), λi = 0 have norm determined by evaluation, and are not required to have
small k, p norm on the neck. The Sobolev embedding theorem implies the same
estimate for the k, p, λ norm for any kp with kp > 1. Write
ψνe−τνuν(s, t) = expe−τν uδpre
ν
(s,t)(ξν(s, t))
with notation as around (104). The difference between geodesic exponentiation
and addition vanishes uniformly in the limit. Hence, the estimate (126) holds for
ξν by comparability of geodesic exponentiation with addition in the local model.
Away from the neck uν converges to uδpre
ν
uniformly in all derivatives. Thus the


## Page 87


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
87
k, p, λ norm of ξν tends to zero on Sδν as ν →∞. It follows that the map u′
ν is the
unique solution appearing in the implicit function theorem.
□
6.6. Deformation to split form. As in Charest-Woodward [18] we consider a
deformation of the matching conditions between levels to split form. In this limit,
the moduli spaces of treed buildings become products, rather than fiber products,
of moduli spaces of their treed levels. This deformation is similar to the theory
introduced by Bourgeois [13]. The resulting Fukaya algebra is homotopy equivalent
to the original. The deformation replaces the matching conditions at the Reeb
orbits and chords with deformed matching conditions using deformations of the
diagonal. Fix a Morse-Smale pair on Y = Z/S1 and LZ := L ∩Z with Morse
functions
hY : Y →R,
hZ : LZ →R.
In our special case considered in this paper, will have LZ = Sn−1 and the Morse
function can be taken to be projection on an axis, so that in particular h has two
critical points.
Definition 6.31. Let ℘∈[0, ∞]. A treed ℘-building C is a treed building Cpre
with levels C0, . . . Ck so that Ci is joined to Ci−1 by segments Ti of length ℘i so
that the sum
k
X
i=1
℘i = ℘
is equal to ℘.
A holomorphic treed ℘-building with k levels is a pair (C, u : S →X) where C is
a treed ℘-building and u : C →X is a collection of levels u|Ci : Ci →X[2k]2i and
gradient segments u|Ti : Ti →LZ ⊂X[2k]2i+1 of hY resp. hZ connected Reeb orbits
resp. chords satisfying the obvious matching conditions at the intersection points
Ti ∩Ci, Ti ∩Ci+1.
Figure 12. Replacing nodes with segments: A ℘-building is on the
right


## Page 88


88
JOSEPH PALMER AND CHRIS WOODWARD
That is, each node connecting levels is replaced by a gradient trajectory as in
Figure 12. See Charest-Woodward [18, Chapter 8]. We now repeat the construc-
tion of the broken Fukaya category using ℘-buildings rather than treed buildings.
The moduli space of holomorphic ℘-treed buildings is denoted M℘(X, ϕ).
The
same regularization procedure as in the previous section leads to regularized mod-
uli spaces M℘(X, ϕ, D) with good compactness properties for the components of
expected dimension at most one. Using moduli spaces of buildings, we may define
a broken analog of the Fukaya algebra. The underlying vector space CF(X, ϕ) is
defined in the same way as CF(X, ϕ), but in equation (50) the count of elements of
MΓ(X, ϕ, D) is replaced by a count of elements of MΓ(X, ϕ, D). Counts of ℘-treed
buildings lead to a family of broken Fukaya algebras CF ℘(X, ϕ).
Remark 6.32. In the case of infinite breaking parameter, each moduli space of
buildings is a product of the moduli spaces of levels in the following sense. Each
holomorphic building (C, u : S →X[k]) breaks up into a collection of pairs
(Ci, ui : Si →X[k]l−(i),l+(i))
where X[k]l−(i),l+(i) ⊂X[k] is the union of components in the decomposition (74)
between levels l−(i), l+(i). We denote in particular X⊂[k] ⊂X[k] the union of the
components except the last X⊃, and similarly for X⊃[k]. Thus, in particular an
∞-level may be a pair (C, u : S →X⊂[k]) which consists of a map to X⊂and some
collection of maps to R × Z with matching conditions. For a type of building Γ
and collection of constraints Σ the moduli space of treed buildings M∞
Γ (X, ϕ, D) of
labeled type Γ is a product of the moduli space of its labeled treed levels
M∞
Γ (X, ϕ, D) =
[
(Σi)
k
Y
i=0
MΓi(X, ϕ, D, Σi).
Here the union is over possible labellings Σi, representing the collection of con-
straints given by the (un)stable manifolds of the Morse functions chosen on Π and
Y for the inter-level edges and the cellular constraints for each boundary leaf. We
adjust our terminology and call the elements ui of MΓi(X, ϕ, D, Σi) levels. Each
ui further decomposes into sublevels ui,j with domain Si,j ⊂Si mapping into some
X[k]l(i,j).
6.7. Homotopy equivalences. We consider various kinds of homotopy equiva-
lences of A∞algebras involving broken Fukaya algebras in this section. The first
Theorem 6.33 is an A∞equivalence which arises in the limit of infinite neck length
under the neck stretching limit; this is essentially the same as considered in Charest-
Woodward [18]. For this theorem, the Lagrangian boundary condition is required
to be cylindrical on the neck. Suppose that ϕ : L →X is a Lagrangian boundary
condition that is cylindrical in a neighborhood of a hypersurface Z ⊂X. We de-
note by mτ
d the composition maps on CF(X, ϕ) associated to the neck-stretched
almost complex structure Jτ ∈J (X).


## Page 89


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
89
Theorem 6.33. The maps mτ
d have a limit m∞
d as τ →∞equal to the compo-
sition map md for the algebra CF(X, ϕ). The broken Fukaya algebra CF(X, ϕ) is
homotopy-equivalent to CF(X, ϕ). Similarly, for any breaking parameter ℘, the
broken Fukaya algebra CF(X, ϕ) is homotopy equivalent to CF ℘(X, ϕ).
The proof was given in [18, Chapter 8] for the case that the Lagrangian does
not pass through the neck; the proof is the same in the case here. We summarize
the argument for completeness, which uses counts of quilted disks. A quilted treed
disk is a treed disk a collection of disk components S′ ⊂S equipped with quiltings,
meaning circles in S′ intersecting a boundary component exactly once.
These
components are called quilted components and, in the treed context, the lengths ℓ(e)
of edges connecting these components satisfy a system of equalities, if the number
of quilted components is greater than one. The composition of these homotopy
equivalences converges to a homotopy equivalence with the broken Fukaya algebra.
For any energy bound E, the terms in the homotopy-equivalence ζτ relating the
neck-stretched alost complex structures with coefficient qA(u), A(u) < E vanish for
sufficiently large τ except for constant disks. It follows that there exist limits of
the successive compositions of the homotopy equivalences. For N, τ ∈Z>0 consider
the composition
ζN,τ := ζN+τ−1 ◦ζN+τ−2 ◦. . . ◦ζN : CF(XN, ϕ) →CF(XN+τ, ϕ).
Because of the bijection in Theorem 6.28, the limit
ζN = lim
τ→∞ζN,τ : CF(XN, ϕ) →lim
τ→∞CF(XN+τ, ϕ)
exists. Similarly, the limit
ψN = lim
τ→∞ψN,τ,
ψN,τ := ψN+τ ◦ψN+τ−1 ◦. . . ◦ψN
exists. The composition of strictly unital morphisms is strictly unital, so the com-
position ψ is strictly unital mod terms divisible by qE for any E.
The limiting morphisms are also homotopy-equivalences. Let hτ, gτ denote the
homotopies satisfying
ζτ ◦ψτ −id = m1(hτ),
ψτ ◦ζτ −id = m1(gτ),
from the homotopies relating ζτ ◦ψτ and ψτ ◦ζτ to the identities in [56, Section
1e]. In particular, hτ+1, gτ+1 differ from hτ, gτ by expressions counting twice-quilted
disks. For any E > 0 and τ sufficiently large, all terms in hτ+1 −hτ are divisible
by qE. It follows that the infinite composition
hN = lim
τ→∞hN,τ,
gN = lim
τ→∞gN,τ
exists and gives a homotopy-equivalence between ζN ◦ψN resp. ψN ◦ζN and the
identities on CF(X, ϕ) and CF(X, ϕ). The proof of homotopy equivalence with
CF ℘(X, ϕ) is similar.


## Page 90


90
JOSEPH PALMER AND CHRIS WOODWARD
7. Holomorphic disks bounding the handle
In this section, we review some results of Fukaya-Oh-Ohta-Ono [31, Chapter 10]
on the moduli spaces of holomorphic disks with boundary in the local model. The
main result is Proposition 7.2, which gives a correspondence, up to repetition of
codimension one inputs, between rigid maps in the local model with surgered and
unsurgered boundary condition (after adding a longitudinal constraint, in the case
of wrong-way corners.)
7.1. Classifying disks with a single end. We first classify disks with a single
end. Let γ(t) = t + i2ϵ be the standard path and MΓ(ϕγ) denote the space of
holomorphic maps u : S →X = Cn with boundary condition in ϕγ : Hγ →X of
some type of map Γ. The target X = Cn is naturally a cylindrical-end manifold
with end modelled on a cylinder R × Z on the unit sphere Z = S2n−1 defined using
coordinates qj + ipj, j = 1, . . . , n on Cn by
Z = {q2
1 + p2
1 + . . . + q2
n + p2
n = 1}.
The Reeb flow on Z is periodic with period 2π and the quotient Z/S1 is a complex
projective space
Y = Z/S1 ∼= CP n−1.
The handle Lagrangian Hγ defines a Lagrangian in the projective space CP n, whose
intersection with the divisor at infinity is RP n−1. The Reeb chords from Rn to iRn
(or vice-versa) through 0 ̸= (a1, . . . , an) ∈Rn are classified by half-integers m ∈Z/2
and are of the form
ϑm,a(t) = emπit/2(a1, . . . , an).
Consider the case that Γ is a type of configuration consisting of a disk S attached
to single leaf T at a node w ∈S. The following classification of curves with right-
way and wrong-way corners is a modification of Fukaya-Oh-Ohta-Ono [31, Theorem
60.26].
Definition 7.1. Let Γ be a type of domain S with a single strip-like end e ∈E(S).
Let Γ+ resp. Γ−be a type of finite-energy map given by sections of the Lefschetz
fibration π : Cn →C over a half space bounding ϕγ asymptotic to a Reeb chord of
angle change π/2 from Rn to iRn resp. iRn to Rn. We say that the map types Γ±
are minimal types and all other map types are non-minimal. Let ˆΓ± be the type
obtained from the minimal types Γ± by adding a boundary leaf e ∈Edge(ˆΓ±). Let
ev : MˆΓ−(ϕγ) →Hγ × Sn−1
denote the combined evaluation map for the leaf and end.
Proposition 7.2. For γ be the standard path t 7→t + i2ϵ, ϵ > 0 and JΓ = J0
the standard complex structure, the maps of type Γ± and ˆΓ± are regular and the
following hold:


## Page 91


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
91
(a) (Right-way corners) Evaluation at infinity (79) defines a diffeomorphism
MΓ+(ϕγ) →Sn−1,
u 7→ϑe(0).
(b) (Wrong-way corners) Evaluation at infinity (79) defines a map
(127)
MΓ−(ϕγ) →Sn−1,
u 7→ϑe(0)
giving MΓ−(ϕγ) the structure of an Sn−2 bundle over Sn−1 diffeomorphic
to the unit sphere bundle T1Sn−1 in TSn−1. For generic a, c ∈Sn−1, the
inverse image ev−1(R × {c} × {a}) is a single transverse point.
Furthermore, the homology classes of maps of type Γ± are primitive. In the dimen-
sion two case dim(H0) = 2, the orientations of the two points in any fiber of (127)
agree for the trivial relative spin structure.
Proof. We adopt a proof similar to Seidel’s computation in [57], which studied
a boundary value problem for sections of a Lefschetz fibration with Lagrangian
boundary condition obtained by parallel transport of the vanishing cycle around a
circle, rather than a line considered here.
We compare the indices of the map with its projection to the base of the standard
Lefschetz fibration. Let u : S →X = Cn be a map with boundary in Hγ. The
composition π ◦u of u with the Lefschetz fibration π : Cn →C of (9) produces a
map π ◦u from H to C with boundary condition (π ◦u)(∂S) ⊂R + i2ϵ. The map
π ◦u is an isomorphism from H to H + i2ϵ by assumption. After composing on the
right with the shift z 7→z + i2ϵ and an automorphism of H, the map u becomes a
section of the Lefschetz fibration:
π ◦u(z) = z,
∀z ∈H + i2ϵ.
Thus the components uj, j = 1, . . . , n of the map
u : (H, ∂H) →(Cn, Hγ)
satisfy equations
uj(z) ∈(z + i2ϵ)1/2R,
z ∈R.
The rank one problems in the previous paragraph are easily solvable. A change
in sign of ϵ is equivalent to an interchange of the types Γ±, so it suffices to consider
the case of maps whose image is half-plane above the line Im(z) = ϵ and consider
the cases ϵ > 0 and ϵ < 0 respectively. The components uj are solutions to a rank
one boundary value problem of index zero resp. one in the case ϵ > 0 resp. ϵ < 0.
Each component uj of u must be of the form for z ∈H
(128)
uj(z + i2ϵ) =



aj(z + i2ϵ)1/2
ϵ > 0
(ajz + bj)(z −i2ϵ)−1/2
ϵ < 0
for some aj ∈R>0 resp. aj ∈R>0, bj ∈R. One can check explicitly that each such
u is a solution to the given boundary value problem: In the first case ϵ > 0 the


## Page 92


92
JOSEPH PALMER AND CHRIS WOODWARD
map has the required boundary values by inspection while in the second case we
have for x ∈R,
uj(x + i2ϵ)(x + i2ϵ)−1/2
=
(ajx + bj)(x + i2ϵ)−1/2(x −i2ϵ)−1/2
=
(ajx + bj)(x2 + 4ϵ2)−1/2 ∈R.
The constants are fixed by requiring that the given map is a section of the
Lefschetz fibration over its projection to the base. Solving for the condition πu(z) =
z, that is, u(z) is a section of the Lefschetz fibration, we obtain
(129)



a2 = 1
ϵ > 0
a2 = 1,
a · b = 0,
b2 = ϵ2
ϵ < 0.
Indeed, if ϵ < 0 then
πu(z) = z
⇐⇒
(a(z −i2ϵ) + b)2 = (z −i4ϵ)z
(130)
⇐⇒



a2
=
1
2a · b −4a2ϵi
=
−2ϵi
−4ϵ2a2 −4ϵia · b + b2
=
0


.
(131)
The equations (131) are equivalent to the equations
a2 = 1,
a · b = 0,
b2 = 4ϵ2.
A similar computation computes the kernel of the linearization. In the first case
ϵ > 0, the kernel at a is the set of solutions a′ to a′a = 0, and so has dimension
n −1. In the second case ϵ < 0, the kernel of the linearization at (a, b) is the set of
solutions (a′, b′) to
a′ · a = 0,
a′ · b + a · b′ = 0,
b · b′ = 0
and so dimension 2n −3.
An index computation implies that the cokernel is trivial. Indeed, for ϵ > 0 the
bundle u∗(Cn →C) is a trivial symplectic fibration. It follows the vertical part
of the index is equal to the dimension of the boundary condition, that is, n −1.
On the other hand, if ϵ < 0 then the index problem is related to that obtained by
a connect sum with the index problem over the disk, which has index 2n −3 by
Seidel [57, Proof of Lemma 2.16]. Since the horizontal index is the same as the
dimension of the space of automorphisms of the domain, the total index is 2n −3
as well. Triviality of the cokernel implies that the moduli spaces are transversally
cut out by the equations (129). The equations give a sphere of dimension n −1 in
the first case, and fibration in the second case with spherical fibers of dimension
n −2.
For (b), it remains to prove the claim on the intersection with a generic line on
the handle. Given
c, a ∈Sn−1,
c ̸= a, −a


## Page 93


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
93
there exist unique x ∈R and b ∈Sn−1 with a · b = 0 such that
u(x + i2ϵ)
|u(x + i2ϵ)| =
ax + b
((ax)2 + b2)1/2 = c.
Indeed, the set of points
n
(ax + b)/∥ax + b∥,
x ∈R, b ∈span(a)⊥o
is the complement of the two poles a, −a in Sn−1. The claim follows.
To prove the claim about primitivity, we classify the possible homology classes.
The second relative homology group H2(CP n, Hγ) ∼= H2(CP n −{0}, Hγ) can be
computed by Mayer-Vietoris. Write CP n = Cn ∪CP n−1 and consider the cover
of CP n by the open sets (Cn −{0}) and (CP n −BR(0)) where BR(0) is a ball
around 0 ∈Cn of radius R. The classes corresponding to the first homology of the
intersection are generated by disks in the line C with boundary in Hγ ∩C that have
area π/2 ± A(ϵ). The remaining classes arise from the classes of disks and spheres
in CP n−1 with boundary in RP n−1, which have areas equal to multiples of π. It
follows that there are no decompositions of the classes with areas π/2 ± A(ϵ) into
classes with positive smaller areas, so that the homology classes of the maps in the
Proposition are primitive.
To prove the claim on orientations in the dimension two case, we must compare
the contributions from the two points u, u′ in each fiber of the fibration of (127).
The orientations o(u), o(u′) may be compared by deforming the Lefschetz fibration
by bubbling off a disk containing the critical value of the Lefschetz fibration as in
Seidel [57]. By the computation in [66, Proof of Corollary 4.31] the orientations of
the two different elements u, u′ in a single fiber agree.
□
The areas of the disks on the handle and on the self-transverse Lagrangian are
related by the area correction in Definition 2.1 and indicated (conceptually; the
graph does not exactly match the definition) in Figure 2. As in the Introduction
we denote by ϕϵ resp. ϕ0 the surgered resp. unsurgered immersion.
Lemma 7.3. Suppose that u0, uϵ : S →X are maps with boundary in ϕ0 resp.
ϕϵ that are equal except in a neighborhood of a self-intersection point x ∈Isi(ϕ0)
as in Figure 2; and suppose that in a neighborhood of the surgery, the map uϵ is
obtained by replacing a right-way resp. wrong-way corner in u0 by its smoothing
above. Then the areas of uϵ and u0 are related by
A(uϵ) = A(u0) −(κ −κ)A(ϵ)
where κ ∈Z≥0 resp. κ ∈Z≥0 is the number of times u0 passes through x resp. x.
Proof. We compute the difference in areas using Stokes’ theorem. The symplectic
form ω0 on Cn is exact with primitive
α0 =
n
X
j=1
1
2(qjdpj −pjdqj),
dα0 = ω0.


## Page 94


94
JOSEPH PALMER AND CHRIS WOODWARD
The restriction of α0 to the Lagrangian branches Rn, iRn vanishes. The maps u0, uϵ
agree away from the corner, and the difference of u0, uϵ in the relative homology
with respect to ϕ0 ∪ϕϵ is the class of a map
v : R × [0, 1] →Cn
bounding H0, Hϵ and constant outside a compact set [−T, T]×[0, 1] with boundary
γ0 : [−T, T] →ϕ0(H0),
γϵ : [−T, T] →ϕϵ(Hϵ).
The first path γ0 travels from the negative to positive branches of ϕ0(H0), while
the second γϵ travels along ϕϵ(Hϵ) in the same direction, as in Figure 2. By Stokes’
theorem, the area of v is
(132)
A(ϵ) =
Z
R×[0,1] v∗ω =
Z
[−T,T] γ∗
ϵ α0 −γ∗
0α0.
independent of the homotopy class of the map v.
□
7.2. Ruling out disks with large angle in the unsurgered handle. In this
section we show that the only rigid curves for the unsurgered handle are those
appearing in Proposition 7.2, that is, those curves with a single strip-like end
asymptotic to a Reeb chord of minimal length. Given a map type of punctured
surface Γ, denote by MΓ(ϕ0) the moduli space of holomorphic treed disks bounding
H0 = Rn ∪iRn of type Γ. Denote by e( ) resp. e( ) the number of Reeb orbits
resp. chords at infinity, and d( ) the number of boundary leaves in total, so that
f( ) = d( ) −e( ) represents the number of boundary leaves not corresponding to
Reeb chords. We have a natural evaluation map
ev : MΓ(ϕ0) →Hf( )
0
× (Sn−1)e( ) × CP e( )
which assigns to any configuration (C, u : C →X) the projection of the limiting
Reeb orbits and chords, and evaluates the map at the intersection of the remaining
leaves Te with S. As in (80) let
Σ ⊂Hf( )
0
× (Sn−1)e( ) × CP e( )
be a submanifold (later, Σ will be the image under the evaluation map of the
"outside pieces" in the symplectic field theory decomposition) intersecting the eval-
uation map for MΓ(ϕ0) transversally. As in (81) define
MΓ(ϕ0, Σ) = ev−1(Σ)
denote the moduli space of maps with the given constraints. We wish to know in
what conditions MΓ(ϕ0, Σ) may be rigid, that is, of expected dimension zero.
We recall the classification of holomorphic maps of disks to the complex pro-
jective line.
Let L ⊂S2 be an embedded circle.
For the case γ(t) = t + i2ϵ,


## Page 95


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
95
the Blaschke classification in [20] implies that after a change of coordinates any
holomorphic disk u bounding L is of the form
(133)
u(z) =

c−
d−
Y
i=1
z −ai,−
1 −zai,−
, c+
d+
Y
i=1
z −ai,+
1 −zai,+


for some integers d± and constants c± with
|c±| = 1,
ai,± ∈C,
d± ∈Z≥0.
Returning to the case of arbitrary paths, we introduce the following notation for
topological type. Identify H2(CP 1, RP 1) ∼= Z2. Let
d = (d−, d+) ∈Z2
denote the degree of the composition π ◦u given by the image u∗([S, ∂S]) in the
relative homology group H2(CP 1, RP 1) ∼= Z2. For each point z ∈S mapping to
infinity ∞, let m (z), m (z) denote the “multiplicity” of the corresponding Reeb
chord or orbit, indicating how many Taylor coefficients vanish at z. Thus m (z)
are the intersection numbers with the divisor at infinity Y at z, while m (z) = k if
the Reeb chord represents an angle change of kπ for some k ∈Z≥1.
Lemma 7.4. For a holomorphic map u : S →C bounding R asymptotic to Reeb
chords and orbits, the Fredholm index of the linearized operator Du is
(134) Ind(Du) = 1+2(d−+d+)−
X
z∈u−1(∞)∩∂S
(m (z)−1)−
X
z∈u−1(∞)∩int(S)
2(m (z)−1)
Proof. The Maslov index of the map u is I(u) = 2(d−+ d+). The Fredholm index
is Ind(Du) = 1 + 2(d−+ d+) by Riemann-Roch. The tangency requirements lower
the index by m (z) −1 resp. 2(m (z) −1) at each Reeb chord or orbit, as in [22,
Lemma 6.7].
□
Lemma 7.5. Let n ≥2. Assume that the standard complex structure makes every
punctured holomorphic disk or sphere u : S →Cn bounding Rn ∪iRn regular. Then
any rigid such map is an isomorphism from a disk onto a quadrant (R≥0 + iR≥0)v
in span(z) ∼= C ⊂Cn for some v ∈Rn ⊂Cn.
Proof. We use the fact that the boundary condition is invariant under dilation. The
action of λ ∈R× on Cn induces a one-parameter family of punctured curves λu
with the same evaluation at infinity. Suppose u is rigid. The dilation λu must equal
the composition u ◦ϕλ for some automorphism ϕλ : S →S. Thus, in particular
S has a non-trivial automorphism, at most two strip-like or cylindrical ends, and
image contained in a line in Cn, and we are in the one-dimensional case considered
in (134). For holomorphic spheres, the degree equals the signed count of points
in a fiber u−1(ζ) over a point ζ near ∞, so each puncture with multiplicity m(z)
contributes m(z) to the degree. Hence, for spheres u we have
Ind(Du) ≥2 + (d−+ d+).


## Page 96


96
JOSEPH PALMER AND CHRIS WOODWARD
Since the automorphism group is at most dimension four, rigidity forces (d−, d+) =
(1, 1). In this case, the map u(z) = v1z is linear with first derivative given by some
v1 ∈Cn. The map u admits a deformation ut(z) = v1z + tv0 with v0 not in the
span of v1, and so is not rigid.
Thus the domain is a disk, and we claim that the map is linear. Since the image
of the boundary is R-invariant, u(∂S) must intersect infinity and so u has at least
one strip-like end. If u has only one strip-like end (mapping either to 0 or to ∞)
then u is a disk in CP 1 ∼= span(c) ∪{∞} bounding RP 1 or iRP 1. By (134), u
cannot be rigid. Thus S has two strip-like ends, and by homogeneity one must
map to the corner {0} = Rn ∩iRn. The map u · u has real boundary conditions, so
u is of the form
u(z) =
q
a(z)v,
Im(z) ≥0
for some v ∈Rn and polynomial a(z). Such maps are rigid only if a(z) has degree
one, since otherwise the variation in the sub-leading coefficients in a(z) preserving
the condition a(0) = 0 produces a non-trivial variation of the map.
□
Lemma 7.6. Assuming the standard complex structure on Cn is regular, for any
rigid treed level (C, u : C →Cn[k]) bounding Rn ∪iRn with at least one component
in Cn, the domain S is connected with image u(S) equal to a quadrant in a one-
dimensional subspace of Cn.
Proof. The general linear group acts on the set of disks with the given boundary
condition. Let u : S →Cn be a rigid treed disk for the given constraint Σ with
components uv : Sv →Cn, v ∈Vert(Γ). Any deformation (ξv) of the maps uv by,
for example, a dilation by λ ∈R−{0} extends to a dilation of u, by translating the
remaining components uv′, v′ ̸= v by elements of GL(n, R) so that the matching
conditions hold. It follows that each component uv must be rigid separately. Each
uv is therefore an isomorphism onto a quadrant in some line span(c) ⊂Cn. The
attaching points we of the edges Te to the surface part S are necessarily invariant
under the action of R×. Each such we must be a point on the boundary ∂S with
u(we) = 0 ∈Cn. That is, the non-constant components of u must be quadrants,
with adjacent components joined by nodes mapping to 0 ∈Cn. (For example, the
domain S of u could consist of two components Sv1, Sv2, with the first component
Sv1 mapping onto the first quadrant, and the second Sv2 mapping onto onto the sec-
ond quadrant.) The edge length ℓ(e) of the edge Te connecting two such quadrants
is free to vary, so the configuration u cannot be rigid.
□
It remains to justify the regularity assumption, to which end we prove:
Lemma 7.7. The standard complex structure on Cn makes all treed levels (C, u :
C →Cn[k]) bounding the unsurgered handle R ∪iRn regular.
Proof. We use the fact that the boundary value problem for the unsurgered problem
splits into one-dimensional problems. Let u : S →Cn be a holomorphic map from


## Page 97


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
97
a connected surface S to Cn asymptotic to some collection ϑ of Reeb chords and
orbits. The pair (Cn, Rn∪iRn) splits into one-dimensional problems (C, R∪iR), each
invariant under the action of dilation. It follows that each summand has a non-
trivial element of the kernel and vanishing cokernel. Thus any such holomorphic
map u is regular.
The case of disconnected domain requires an induction. Let u : S →Cn[k] be
a treed level with surface components Sv, v ∈Vert(Γ) and line segments Te, e ∈
Edge(Γ); recall that the notation Cn[k] means that u has various components some
of which map to neck pieces Cn −{0}.
The moduli space of configurations of
type Γ with any given set of finite edge lengths ℓ(e) is transversally cut out. Let
M′
Γ(ϕ0) denote the moduli space of configurations with no matching conditions at
the nodes. It suffices to show that the evaluation map M′
Γ(ϕ0) →(Sn−1)#(T∩S)
is transverse to the matching condition. This follows from an inductive argument:
If e is the only finite edge adjacent to a vertex v and Γ(v) ⊂Γ is the subgraph
of edges containing v then one sees from the previous paragraph that the map
M′
Γ(v)(ϕ0) →L is a submersion at Te ∩Sv. Removing v and e one obtains a tree Γ1
with fewer vertices and edges, and the claim follows from the inductive assumption
of transversality for such trees.
□
Remark 7.8. Alternatively, one may prove regularity using a long exact sequence.
Let u : S →Cn be a punctured holomorphic disk or sphere avoiding 0 ∈Cn. Let
p : Cn −{0} →CP n−1
denote the projection. Consider the short exact sequence of vector bundles
u∗T vCn →u∗TCn →u∗p∗TCP n−1
where the vertical sub-bundle T vCn is the kernel of Dp. Denote by Dv
u, Dh
u the ver-
tical and horizontal parts of the linearized operator Du. The short exact sequence
of complexes induces a long exact sequence of kernels and cokernels denoted
(135)
coker(Dv
u)
coker(Du)
coker(Dh
u)
ker(Dv
u)
ker(Du)
ker(Dh
u)
-
-
-
-
X
X
X
X
X
X
X
X
X
X
X
X
X
y
.
As in Proposition 6.18, the kernel and cokernel of Dp◦u may be identified with
those of its extension Dp◦u obtained by adding in the points at infinity along the
cylindrical and strip-like ends.
It is a standard consequence of homogeneity of
CP n−1 that the cokernel of such operators vanish: Since p ◦u∗TCP n−1 is generated
by the image of o(n) in ker(Dp◦u) at any point, p ◦u∗TCP n−1 must be a sum of a
line bundles with boundary conditions with positive Maslov index as in Oh [48].
Since the cokernel of a Cauchy-Riemann operator on any one-dimensional problem
with positive Maslov index vanishes [48], the cokernel of Dp◦u vanishes. Similarly,


## Page 98


98
JOSEPH PALMER AND CHRIS WOODWARD
the vertical bundle u∗T v(Cn −{0}) has a section given by the action of R× on
Cn −{0} which preserves the boundary conditions. It follows that coker(Dv
u) also
vanishes. By the long exact sequence (135), coker(Du) vanishes as well.
We require similar results for ruling out holomorphic disks mapping to Cn −{0}
with boundary in (Rn∪iRn)−{0}. Consider a map u from S to X0 := Cn−{0} with
boundary on ϕ0 : (Rn ∪iRn) −{0} →Cn −{0} with multiple ends or non-minimal
Reeb orbits.
Lemma 7.9. Suppose (C, u : C →Cn −{0}) is a treed map bounding (Rn ∪iRn) −
{0} and Σ is a collection of constraints so that all cellular constraints in ϕ0 are
equal to σ1. Then (C, u) consists of a single component with image in a fiber of
Cn −{0} →CP n−1.
Proof. The proof is similar to that of Lemma 7.5 and uses the action of the group
R>0 on Cn −{0} by dilations preserving the boundary condition (Rn ∪iRn) −{0}
and preserving the limits at infinity. Suppose the surface part S of the domain
has components Sv connected by edges Te. Consider a component uv of u. By
dilation by a constant c ∈R>0 one obtains a new map cuv with the same boundary
condition not isomorphic to the original map. Given two strips Sv, Sv′ joined by
an edge Te joined at points z ∈Sv, z′ ∈Sv′, and given c the point u(cz), u(c′z′) are
still connected to Morse trajectory of the distance-to-zero function. It follows that
S has a single component that is a trivial strip.
□
7.3. Ruling out disks with large angle in the surgered handle. We now wish
to show a similar statement for curves bounding the surgered handle, namely that
rigidity forces strip-like ends of minimal length. We first introduce some notation.
Consider the natural projections
π : Cn →C,
(z1, . . . , zn) 7→z2
1 + . . . z2
n
and
p : Cn −{0} →CP n−1,
z 7→span(z).
The null-cone in CP n−1 is
N := p(π−1(0)) = {[z1, . . . , zn], z2
1 + . . . + z2
n = 0}.
Given a holomorphic map bounding the handle, we obtain maps by composition
with either projection. Namely let u : S →Cn be a smooth map with boundary on
the handle Hγ and avoiding 0. The composition π ◦u maps to C with boundary
in γ, while the composition p ◦u maps to CP n−1 with boundary in RP n−1. We
wish to compare the indices of the linearized operator of the map u with that of its
projections. Because the map u may limit to the null-cone along the strip-like ends,
the composition π ◦u may have finite limits along any particular end. To compare


## Page 99


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
99
indices we introduce a long exact sequence. We have a short exact sequence of
bundles over (S, ∂S)
(136)
0 →(T vCn, T vHγ) →(TCn, THγ) →(T hCn, T hHγ) →0.
The short exact sequence of bundles (136) induces a short exact sequence of com-
plexes of 0 and 0, 1-forms. We denote by Dv
u, Dh
u the vertical and horizontal parts
of the linearized operator Du, and ˜Dh
u the parametrized linear operator for the
horizontal part. Consider the map
Dπ : u∗TX →(π ◦u)∗TC.
The short exact sequence of complexes induces a long exact sequence of kernels
and cokernels given by
(137)
coker(Dv
u)
. . .
ker(Dv
u)
ker(Du)
ker(Dh
u)
-
-
-
X
X
X
X
X
X
X
X
X
X
X
y
.
The long exact sequence equally holds with the unparametrized linear operator
˜Du, Dh
u replaced with the parametrized linear operators ˜Du, ˜Dh
u whose domain does
not allow variations of the conformal structure, by the same argument.
We introduce convenient terminology corresponding to the “multiplicity” of the
map at infinity.
Definition 7.10.
(a) For each point z ∈S mapping to infinity in X, let
m (z), m (z) denote the “multiplicity” of the corresponding Reeb chord or
orbit, indicating which eigenvector appears in (85). Thus m (z) are the in-
tersection numbers with the divisor at infinity Y at z, while m (z) = k if
the Reeb chord represents an angle change of kπ for some k ∈Z≥1/2.
(b) Define
mex(z) =



2m (z) −1
if z represents a strip-like end, or
4m (z) −2
if z represents a cylindrical end.
Proposition 7.11. Let u : S◦→Cn be a finite energy holomorphic map bound-
ing Hγ whose evaluations eve(u) at cylindrical ends avoid the null-cone N. The
Fredholm index of the horizontal part Dh
u of the linearized operator Du is by (134)
Ind(Dh
u) = 1 + 2(d+ + d−) −
X
z∈u−1(Y )
mex(z)
while the index of the vertical part Dv
u is
Ind(Dv
u) = (n −1) + d−(n −2).


## Page 100


100
JOSEPH PALMER AND CHRIS WOODWARD
Proof. Denote the extensions of Proposition 6.18 by ((π ◦u)∗TC, (π ◦u)∗Tγ(R))c
over (CP 1, γ(R)). The Maslov index of the horizontal part is
I((π ◦u)∗TC, (π ◦u)∗Tγ(R))c = 2(d+ + d−) −
X
z∈u−1(Y )
mex(z)
by (134). To compute the vertical part of the index, note that the map u may
be viewed as a section of the pull-back of the Lefschetz fibration π : Cn →C
under (π ◦u). The “bubbling off singularities” computation in Seidel [56, p. 253]
implies that each bubble containing a singularity contributes the Maslov index of
the corresponding holomorphic map to the disk, computed in Seidel [57, Proof of
Lemma 2.16] to equal n −2.
□
Lemma 7.12. Let γ : R →C be an asymptotically cylindrical path and u : S →C
a level bounding ϕγ. Then the parametrized linearized operator ˜Du is surjective.
For the standard path γ, the unparametrized linear operator Du is surjective.
Proof. We first prove the last claim for the standard path. The kernel and cokernel
are identified via Proposition 6.18 with a one-dimensional real boundary value
problem. Note that (CP 1, RP 1) has a family of automorphisms ϕs preserving ∞.
The derivative
d
ds|s=0ϕs ◦u gives a non-trivial element of the kernel ker(Du). Hence
coker(Du) vanishes, since in rank one either the kernel or cokernel of any Cauchy-
Riemann operator vanishes by Oh [48].
For arbitrary paths that are asymptotically cylindrical, the statement of the
Lemma regarding the parametrized linear operator is an instance of automatic
regularity in dimension one as in Seidel [56, Lemma 13.2]. The cokernel of ˜Du may
be identified with the kernel of the adjoint operator. Necessarily, any η ∈coker( ˜Du)
is perpendicular to variations of the form (Jduα)0,1 produced by variations
TjJ (S) = {α ∈Ω0(S, End(TS)) | jα + αj = 0}
of the conformal structure on (S, z, z′), with notation from (18). By definition the
moduli space of curves is a slice for the action of the diffeomorphism group on the
space of conformal variations
TjJ (S) = TSM ⊕Vect(S, z, z′)
with
Vect(S, z, z′) := {v ∈Vect(S)|v(z) = 0, ∀z ∈z ∪z′}
where if S unstable then TSM is defined to be trivial. The image of the operator ˜Du
is unchanged if one extends the domain to allow all deformations: Let v ∈Vect(S)
vanish at the points z, z′ ∈u−1(∞). The variation of the complex structure and
map with respect to v is given by elements
α(v) ∈Ω0(S, End(TS)),
Lvu ∈Ω0(S, u∗TP1)
with
(Jduα(v))0,1 + DuLvu = 0.


## Page 101


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
101
Since u has derivatives vanishing up to order m(zj) at each zj ∈z, z′, the derivative
Lαu has derivatives vanishing up to order m(zj) −1.
Similarly, for the points
z ∈u−1(∞), if u has derivatives up to order m(z) vanishing at z then du has
derivatives up to order m −1 vanishing at z. Since v vanishes at z, the derivative
Lvu has derivatives up to order m vanishing at z as well. Hence Lvu defines an
element in the domain of Du. Thus, the term (Jduα(v))0,1 lies in the image of Du.
Since du is an isomorphism away from the finitely many critical points of u, there
are no 0, 1-forms perpendicular to such variations (Jduα)0,1 for all α. The claim
follows.
□
Lemma 7.13. For the standard complex structure on Cn and a boundary condition
given by an asymptotically cylindrical path γ : R →C, every holomorphic treed
disk u : C →Cn[k] with boundary on Hγ not meeting 0 ∈Cn is regular and the
evaluation map at any point on the boundary z ∈∂S has surjective linearization in
Tu(z)Hγ.
Proof. We will show that the vertical and horizontal parts of the linearized operator
are both surjective. First let Γ be a combinatorial type of map with a single vertex
v and strip-like and cylindrical ends S.
Consider the moduli space MΓ(ϕγ) of
holomorphic maps u : S →X with boundary in Hγ. By the long exact sequence,
to show regularity it suffices to show that the cokernels of Dv
u and ˜Dh
u vanish.
The homogeneity argument implies that the higher cohomology of the vertical
part vanishes: The action of SO(n) on Cn preserves the complex structure and
Lagrangians Hγ. Given a holomorphic disk u : S →Cn with boundary on Hγ, one
obtains an inclusion
so(n) →ker(Du∗T vCn),
ξ 7→d
dt|t=0 exp(tξ)u
by mapping each Lie algebra element ξ ∈so(n) to the corresponding infinitesimal
deformation of the map. In particular, the evaluation map
ker(Du∗T vCn) →T vHγ,
ξ 7→ξ(z)
at any point z ∈∂S◦is a submersion. By Lemma 7.12, coker( ˜Dh
u) vanishes as well.
The vertical part (u∗T vCn, (∂u)∗T vHγ) has spanning sections at any point given
by the action of SO(n). This fact implies that the linearization of the evaluation
map is surjective.
Similar arguments apply to the case of sublevels mapping to the neck piece, that
is, components uv mapping to Cn −{0} with boundary on (Rn ∪iRn) −{0}. Given
such a map, the projection π ◦uv is a map to C with boundary values on R with
corners of uv mapping to zeros of π ◦uv. Such maps have surjective linearization
by Lemma 7.7.
The previous paragraphs show that the moduli space MΓ(v)(ϕγ) is cut out
transversally for each vertex v ∈Vert(Γ), and the evaluation map at any point
on the boundary is a submersion. As in the proof of Lemma 7.7, an induction


## Page 102


102
JOSEPH PALMER AND CHRIS WOODWARD
shows that the evaluation maps at the nodes from H0(u∗TCn) are transverse to
the diagonal and so the moduli space MΓ(ϕγ) is transversally cut out.
□
The following Lemma gives the reader some idea of the relationship between
maps bounding the handle and their projections under the Lefschetz fibration map.
Denote by Mf
Γ(ϕγ) ⊂MΓ(ϕγ) the locus of levels u with π ◦u having finite limit
eve(π◦u) ̸= ∞along some cylindrical end e ∈Edge→, (Γ). Let Mn
Γ(ϕγ) ⊂MΓ(ϕγ)
denote the locus of maps u with eve(u) lying in the nullcone N at a cylindrical end
e.
Lemma 7.14. For each type Γ, the loci Mf
Γ(ϕγ), Mn
Γ(ϕγ) are transversally cut
out and codimension at least two. In particular, for rigid map types Γ the locus
Mf
Γ(ϕγ) ∪Mn
Γ(ϕγ) of maps having limit in the null-cone or with π ◦u having a
finite limit along some cylindrical end is empty.
Proof. Let u : S →Cn be a map so that π ◦u : S →C has finite evaluation at a
cylindrical end e. The locus of such maps has formal tangent space given by sections
ξ of u∗TCn in ker( ˜Du) such that Dπξ is finite at the end. For simplicity, suppose
there is a single such end with multiplicity m (z′
1). Evaluating the coefficients of
z−1, . . . , z−2m (z′
1) of any section at the end induces a long exact sequence
(138)
ker( ˜Dπ◦u) →ker( ˜Dh
u) →(Tu(z′
1)C)2m (z1) →coker( ˜Dπ◦u) →. . . .
The connecting homomorphism (Tu(z′
1)C)2m (z1) →coker( ˜Dπ◦u) maps the Taylor
coefficients (c1, . . . , c2m (z′
1)) to the image of ˜Dh
uξ in coker( ˜Dπ◦u) where ξ has the
given coefficients in the expansion at z′
1. Since ˜Dπ◦u is surjective, the long exact
sequence (138) implies that the evaluation map eve at the cylindrical end from
ker( ˜Dπ◦u) to (u∗TC)c has surjective linearization D eve. It follows that the locus of
maps u with eve(π ◦u) ̸= ∞is transversally cut out. The first claim follows. The
second claim follows from the last statement in Lemma 7.12.
□
By Lemma 7.14 rigid maps have evaluations only in the complement of the null-
cone, assuming transversality holds. To give the reader an idea of what kind of
maps with strip-like ends of non-minimal length occur, we classify such maps for
the standard path.
Proposition 7.15. For the standard path γ(t) = t + i2ϵ, any map u from the
complement S of a finite set in H whose evaluations eve(u) along the cylindrical
ends e ∈E (S) do not lie in the null-cone N is of the form
(139)
u(z) = b(z)−1/2
Y
Im(αi)<0
(z −αi)1/2
Y
Im(αi)>0
(z −αi)−1/2˜u
for some polynomial b(z) and complex numbers αi and polynomial
(140)
˜u(z) = (cd−zd−+ . . . + c1z + c0).


## Page 103


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
103
for some complex constants c0, , . . . , cd−satisfying
˜u(z) · ˜u(z) = f−(z)f ∗
−(z) =
Y
Im(αi)>0
|z −αi|2.
Proof. Suppose the domain of u is the punctured upper half-plane
S = {Im(z) ≥0} −{z1, . . . , ze( )−1} −{z′
1, . . . , z′
e( )}.
The difference (π ◦u)(z) −2iϵ is a rational function a(z)/b(z) of z by the reflection
principle. Since (π◦u)(z)−2iϵ has real boundary values, there exist real polynomials
a(z), b(z) so that
(π ◦u)(z) = a(z)
b(z) + i2ϵ.
By assumption u(z) goes to infinity as z →∞and the limit in CP n−1 is not in the
null-cone. So
deg(a) ≥deg(b),
deg((π ◦u)b) = deg(a).
The composition π ◦u admits a factorization
a(z) + i2ϵb(z) = cf+(z)f−(z)
where
f±(z) :=
d±
Y
i=1
(z −αi,±)
has d± roots αi,± in the lower resp. upper half-plane, that is, with ∓Im(αi,±) > 0.
Define
f ∗
±(z) :=
d±
Y
i=1
(z −αi,±)
and
˜u : H →Cn,
z 7→u(z)f+(z)−1/2f ∗
−(z)1/2b(z)1/2.
Since by assumption the limits of u along the punctures do not lie in the null-cone,
the poles of π ◦u are twice the order of those of u. Since these are the order of
vanishing of b(z), the map ˜u is a polynomial. The degree of ˜u is
deg(˜u)
=
1
2(deg(π ◦u) + deg(f−) −deg(f+) + deg(b))
=
1
2(deg(a) + deg(f−) −deg(f+)) = d−
and so of the claimed form. Conversely, u may be constructed from ˜u as follows.
Assume that for z real
(141)
˜u(z) · ˜u(z) = f−(z)f ∗
−(z) =
Y
Im(αi)>0
|z −αi|2.


## Page 104


104
JOSEPH PALMER AND CHRIS WOODWARD
The map
u(z)
:=
f+(z)1/2f ∗
−(z)−1/2b(z)−1/2˜u(z)
(142)
=
b(z)−1/2
Y
Im(αi)<0
(z −αi)1/2
Y
Im(αi)>0
(z −αi)−1/2
(cd−zd−+ . . . + c1z + c0)
has the required boundary values.
□
Remark 7.16. We have shown that the moduli spaces of levels in Cn are already
regular without using a domain-dependent almost complex structure. By an ar-
gument using Sard’s theorem, there exists a complex hypersurface D⊂in CP n so
that the moduli spaces MΓ(ϕγ, D⊂, Σ) are cut out transversally whenever Γ is an
uncrowded type of expected dimension at most one. Let f(Γ) be the type of map
without interior edges obtained by forgetting the interior edges of Γ. There is a
forgetful map
MΓ(Cn −{0}, ϕγ, D⊂, Σ) →Mf(Γ)(Cn −{0}, ϕγ, Σ)
forgetting the interior edges which produces a bijection between the moduli spaces
with and without the Donaldson hypersurface. For this reason, in this section we
use treed disks rather than the adapted treed disks in the earlier chapters.
We introduce further notation on the combinatorial type. Assume that Γ is a type
of map to Cn−{0} with e( ) boundary leaves representing strip-like ends asymptotic
to Reeb chords, and d( ) ≥e( ) boundary leaves in total. We assume there are no
cylindrical ends asymptotic to Reeb orbits. Denote by p(Γ) the corresponding type
of stable map bounding RP n−1 obtained by replacing the homology classes in Cn
with homology classes in CP n−1, and forgetting the intersection multiplicities at the
ends; assuming that this construction yields a stable map. For each strip-like end,
the resulting map to CP n−1 takes values in the divisor at infinity CP n−2 ⊂CP n−1.
We denote by Mp(Γ)(CP n−1, RP n−1) the corresponding moduli space of treed disks
in CP n−1 bounding RP n−1, where the map on the edges corresponding to strip-like
ends is a Morse trajectory on RP n−2.
Lemma 7.17. With assumptions from the previous paragraph, the unconstrained
moduli space MΓ(Cn, ϕγ) has dimension
(143)
dim MΓ(Cn, ϕγ) = d+ + n + (n −1)d−+ d( ) −3
where (d−, d+) is the bidegree of π ◦u. Each such map has projection to CP n−1
given by a disk of degree d −1, and the dimension of the moduli space of maps of
type p(Γ) is
(144)
dim Mp(Γ)(CP n−1, RP n−1) = (n −1) + nd−+ d( ) −e( ) −3.


## Page 105


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
105
Proof. By the index formula in Proposition 7.11,
dim MΓ(Cn, ϕγ)
=
2d+ + n(1 + d−) + d( ) −3 −
e( )
X
i=1
2m (zi)
(145)
=
2d+ + n(1 + d−) −3 + d( ) −(d−+ d+)
(146)
=
d+ + n + (n −1)d−+ d( ) −3.
(147)
Here d( ) −3 is the dimension of the moduli space of disks, and 2d+ + n(1 + d−) is
the Maslov index of the linearized boundary value problem. Given such a map u,
the composed map p ◦u hits the null-cone
Q := [p−1(0) −{0}] ⊂CP n−1
exactly d−times.
Its doubled map from CP 1 to CP n−1 meets the degree two
hypersurface Q exactly 2d−times, and so is a map of degree d−. Thus p ◦u is
a disk of degree d−. The second dimension formula (144) is standard and follows
from Riemann-Roch, taking into account the codimension one constraints at the
e( ) ends mapping to RP n−2.
□
We now investigate the map on moduli spaces induced from the map to projective
space. Denote by MΓ(Cn −{0}, ϕγ) the locus of maps disjoint from 0, that is, the
critical locus of π. If d−≥1 then composition induces a map on moduli spaces
(148)
pΓ : MΓ(Cn −{0}, ϕγ) →Mp(Γ)(CP n−1, RP n−1),
u 7→p ◦u.
Proposition 7.18. If d−> d+ resp. d−< d+ then the map DpΓ has positive
dimensional kernel resp. cokernel on each tangent space, while if d−= d+ the map
DpΓ is an isomorphism on each tangent space.
Proof. By the long exact sequence (135), the map DpΓ is an injection resp. surjec-
tion on each tangent space of the vertical part of the cohomology vanishes in degree
zero resp. one. On the other hand, the kernel ker(Dv
u) resp. cokernel coker(Dv
u)
vanishes if the Maslov index of (u∗T vCn, u∗T vHγ) is negative resp. positive, as in
Oh [48].
□
We now wish to classify which configurations in the local model may be rigid. Let
d1(Γ) denote the number of cellular constraints labeled σ1 and em(Γ) the number
of strip-like ends labeled with minimal length Reeb chords and with a non-trivial
constraint.
Lemma 7.19. Let Γ be a labeled type of treed holomorphic building (C, u : C →Cn)
bounding ϕγ with constraints Σ. Assume that either n = 2 or d1(Γ) ≤2, so that
there are at most two boundary constraints labeled by the cell σ1. If Γ is a rigid
type for the given constraints Σ then one of the following holds:
(a) The number of strip-like ends is e( ) = 1, the Reeb chord at the puncture
is minimal length and the type is one of the minimal types considered in
Section 7.1; or


## Page 106


106
JOSEPH PALMER AND CHRIS WOODWARD
(b) the number of strip-like ends is e( ) ≥2 and the numbers d1(Γ) resp. em(Γ)
of constraints labeled σ1 resp. strip-like ends asymptotic to minimal-length
Reeb chords satisfy the inequality
d1(Γ) + em(Γ) ≥3.
If n = 2 then only the first possibility (a) occurs.
Proof. We first rule out the case that the domain is a treed sphere, that is, the
domain has empty boundary. In this case, the dimension of the moduli space of
maps of any type Γ with Γ representing a top-dimensional stratum and map with
degree d to CP n is by Riemann-Roch
dim(MΓ(ϕγ))
=
2d(n + 1) + 2n −6 −
e( )
X
i=1
2(m (zi) −1)
=
(2d + 2)n −6 + 2e( )
≥
2e( )(n + 1) + 2n −6.
Here 2d(n + 1) is the contribution of the first Chern cass, 2n is the dimension of
the ambient manifold, 6 = dim(Aut(CP 1)), and the last term is the contribution
from the intersection constraints at the intersections the divisor at infinity. Each
cylindrical end has a constraint which cut down the dimension by at most 2(n−1).
It follows that for n ≥2 such types cannot be rigid.
Therefore, it suffices to consider the case that the domain has non-empty bound-
ary, that is, the domain is a treed disk. Suppose first n = 2 and there are no
cylindrical ends. The dimension of the moduli space from (143) is
d+ + 2 + d−+ d( ) −3 ≥2d( ) −1.
Since the constraints at the boundary leaves cut down the dimension by at most 1,
the constrained moduli space is expected dimension at least d( ) −1, and we must
have d( ) = 1 for rigidity to hold.
In the case of arbitrary dimension, each end e contributes some pair (d+(e), d−(e))
to the bidegree of the composition π ◦u, measured as the number of points in a
fiber of π◦u near infinity. Since the map at each end is asymptotic to a Reeb chord
whose projection is a circular arc whose angle is an integer multiple of π/2,
(149)
|d+(e) −d−(e)| ≤1.
Case 1: There is a single strip-like end.
The dimension of the unconstrained
moduli space from (143) is d+ + n + (n −1)d−−2.
Case 1a: d−≤1. The unconstrained dimension must be at most 2(n −1). Thus
either
(d−, d+) = (0, 1)
or
(d−, d+) = (1, 0);


## Page 107


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
107
in the latter case by rigidity there is a constraint at the end and a cellular constraint
labeled σ1.
Case 1b: d−≥2. By (149), d+ ≥1 and the dimension of the unconstrained moduli
space
d+ + n + (n −1)d−−2 ≥3n −3.
Since each cellular constraint lowers dimension by n −2 and the constraint at the
strip-like end lowers dimension by n −1, the constrained moduli space cannot be
made rigid by adding at most two cellular constraints.
Case 2: There are at least two strip-like ends.
We introduce notation for the
various kinds of strip-like ends. Let e′(Γ) denote the number of strip-like ends of
type (0, 1), e′′(Γ) the number of strip-like ends of type (1, 0), and e′′′(Γ) resp. e′′′′(Γ)
the number of strip-like ends with
0 < d−(e) = d+(e) −1 resp. 0 < d+(e) = d−(e) −1.
Since d+ ≤d−by Proposition 7.18 we must have
(150)
e′(Γ) + e′′′(Γ) ≤e′′(Γ) + e′′′′(Γ).
The dimension of the constrained moduli space from (143) satisfies the inequality
dim(MΓ(ϕγ, Σ))
≥
d+ + n + (n −1)d−+ d( ) −3 −e (Γ)(n −1) −d1(Γ)(n −2)
≥
(n −1) +
X
e
((n −1)d−(e) + d+(e) −(n −1)) −d1(Γ)(n −2)
≥
(n −1) −e′(Γ)(n −2)
(151)
+2e′′′(Γ) + e′′′′(Γ)(2n −1) −d1(Γ)(n −2)
(152)
where the sum is over edges e representing strip-like ends. Here the first inequality
holds since d± is the sum of contributions from d±(e) and the constraints at the ends
lower the dimension by at most n−1. We have ignored the ends with d−(e) = d+(e),
which are irrelevant for the computation. Equation (150) and vanishing of (151)
imply
e′′(Γ) + e′′′′(Γ) ≥e′(Γ) ≥e′′′′(Γ) + 2 −d1(Γ).
Hence
em(Γ)
=
e′(Γ) + e′′(Γ)
≥
e′(Γ) + 2 −d1(Γ).
(153)
Case 2a: Suppose d1(Γ) = 2.
By way of contradiction, suppose that e′(Γ) =
e′′(Γ) = 0. We must have e′′′′(Γ) ≥1 in order for d+ ≤d−. Then rigidity requires
d1(Γ) + e′(Γ) ≥3 which is a contradiction. Hence d1(Γ) + em(Γ) ≥3.
Case 2a: Suppose d1(Γ) ≤1. Rigidity requires e′(Γ) ≥1 and so by (153) we have
d1(Γ) + em(Γ) ≥3 as desired.


## Page 108


108
JOSEPH PALMER AND CHRIS WOODWARD
Case 3: There are cylindrical ends. Each cylindrical end with multiplicity m (z′
i)
contributes (2n+4)m (z′
i) to the degree terms 2d+ +nd−in the dimension formula
(143). On the other hand, any constraint at the Reeb orbit cuts down the dimension
by at most dim(CP n−1) = 2n −2. Since
(2n + 4)m (z′
i) −(2n −2) > 0,
the arguments of the previous paragraphs cases go through as before with only
improvements in the inequalities.
□
7.4. Ruling out maps intersecting the critical locus. In the previous section,
we ruled out rigid levels with more than one end or non-minimal Reeb length
assuming that the maps avoid the critical locus. To deal with the case that the
map intersects the critical locus, we introduce a blow-up which allows us to extend
the splitting of the tangent bundle into horizontal and vertical parts over the critical
locus. Let
Bl(Cn) = {(z, l) ∈Cn × CP n−1, z ∈l}
denote the blow-up of Cn at 0, and let
p : Bl(Cn) →Cn,
(z, l) 7→z
denote the natural surjection. For any path γ avoiding 0, the boundary condition
ϕγ naturally lifts to Bl(Cn) and we denote the lift with the same notation. Removal
of singularities defines a bijective correspondence between maps to the blow-up and
to its projection. For some type Γ of level, let f
MΓ(Bl(Cn), ϕγ) denote the moduli
space of tuples (C, u, ζ) of maps u : S →Bl(Cn) where (C, u) is a treed disk and
with additional markings ζ ⊂S is a finite set describing the intersection set with
the exceptional divisor in the sense that
u−1(CP n−1) = ζ.
Similarly, let f
Mp(Γ)(Cn, ϕγ) denote the moduli space of pairs (u, ζ) of maps u : S →
Cn with additional markings ζ describing the intersection set with the exceptional
divisor u−1(0) = ζ; here p(Γ) is the obvious type of level in Cn obtained by pro-
jecting the homology classes of the components. Composition with the projection
f
MΓ(Bl(Cn), ϕγ) →f
Mp(Γ)(Cn, ϕγ),
u 7→p ◦u
is a bijection, by removal of singularities.
Lemma 7.20. For the standard complex structure on Bl(Cn), every holomorphic
treed disk (C, u : C →Bl(Cn)) bounding ϕγ asymptotic to some collection of Reeb
orbits and chords at infinity is regular.
Proof. The proof is essentially the same as that of Lemma 7.13. The splitting of
u∗T Bl(Cn) into vertical and horizontal parts, corresponding to the tangent space


## Page 109


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
109
to Pn−1 and O(−1), induces a long exact sequence involving the kernels and cok-
ernels of Dv
u, Du and Dp◦u. Homogeneity implies vanishing of the vertical cokernel
coker(Dv
u), while existence of a section implies vanishing of the horizontal cokernel
Dp◦u. The claim now follows from the long exact sequence similar to (135).
□
Lemma 7.21. For generic constraints Σ, or generic paths of constraints, for any
type Γ of treed level the moduli space MΓ(ϕγ, Σ) is cut out transversally and any
rigid treed level u ∈MΓ(ϕγ, Σ) has image disjoint from 0 ∈Cn.
Proof. By Lemma 7.20, the moduli spaces
f
MΓ(ϕγ, Σ) are regular.
A standard
codimension argument shows that f
MΓ(ϕγ, Σ) has dimension 2(n−1) less than that
of MΓ(ϕγ, Σ), with the obvious identification of map types. Indeed, the relative
Chern class of Bl(Cn) →Cn is dual to (1−n)[CP n−1]. Thus, the Maslov index of u
differs from that of p◦u by 2(1−n) times the intersection number of u with CP n−1.
For ζ non-empty, if MΓ(ϕγ, Σ) is expected dimension zero then f
MΓ(ϕγ, Σ) is empty,
and the elements of MΓ(ϕγ, Σ) have images disjoint from 0 ∈Cn.
The same
argument works for paths of constraints, as a codimension 2(n −1)-codimensional
submanifold of a one-dimensional manifold is still empty.
□
7.5. Comparing disks bounding the flattened and unflattened handles.
We wish to show that the unflattened handle is asymptotically cylindrical.
Lemma 7.22. The handle Hγ ⊂Cn for the standard path γ(t) = t + 2iϵ is asymp-
totically cylindrical.
Proof. We first consider the case of dimension one targets. The image of the line
R + i2ϵ under the coordinate change z 7→1/z is a circle of diameter 1/2ϵ with
center at i/4ϵ, described in coordinates z = x + iy as the solution set to
(R + i2ϵ)−1 = {x2 + (y −(4ϵ)−1)2 = (4ϵ)−2}.
It suffices to consider the case ϵ = 1/4. The handle Hγ is the pre-image of R + i/2
under the square map
(x, y) 7→(x2 −y2, 2xy).
Thus Hγ is given in coordinates near infinity by
{(x2 −y2)2 + ((2xy) −1)2 = 1}
=
{y4 −2x2y2 + x4 + 4x2y2 −4xy + 1 = 1}
=
{y4 + 2x2y2 + x4 −4xy = 0}.
Write y = xz. The equation
xz = (x2z2 + x2)2
4x
= x3(1 + z2)2
4
has a smooth solution of z in terms of x, since z 7→z/(1 + z2)2 is a diffeomorphism
near z = 0. By symmetry, each branch is a smooth manifold with boundary at
x = y = 0.


## Page 110


110
JOSEPH PALMER AND CHRIS WOODWARD
For higher dimension, the handle is the flow-out of the dimension one handle
under the action of the special orthogonal group. Let H
n
γ ⊂CP n denote the handle
in dimension n. Consider the action of O(n) on CP n on the first n coordinates.
The locus
H
1
γ = {[z, 0, . . . , 0, 1]} ∩H
n
γ
has stabilizer groups contained in O(1)×O(n−1). Thus we have a homeomorphism
H
n
γ = O(n)H
1
γ ∼= (O(n) × H
1
γ)/(O(1) × O(n −1))
which is a diffeomorphism away from the boundary. Since each branch of H
1
γ is
a smooth submanifold with boundary, H
n
γ has a smooth structure for which the
inclusion in X is an immersion.
□
Proposition 7.23. Let Γ be a primitive type. There exists an oriented cobordism
from MΓ(ˇϕγ, Σ) to MΓ(ϕγ, Σ), where ˇϕγ : ˇHγ →Cn is the flattened embedding of
(15).
Proof. We will construct a cobordism between the two moduli spaces by viewing
them as moduli spaces of curves bounding cleanly-intersecting Lagrangians. The
closures of ˇHγ and Hγ in CP n are contained in cleanly-intersecting Lagrangians
by Proposition 6.11. Furthermore, this extension of ˇHγ is an exact deformation of
Hγ, by the description from (14). Choose a family of Lagrangians Ht
γ interpolating
between Hγ and ˇHγ, for example, by using ρt = (1−t)ρ+t(ln(r)−|ϵ|) in the defini-
tion (14). Let f
MΓ(ϕγ, Σ) denote the parametrized moduli space of J0-holomorphic
maps for the family consisting of triples (t, C, u) where t ∈[0, 1] and (C, u) is a
J0-holomorphic curve bounding H
t
γ above.
There is no bubbling in the parametrized moduli space by the primitivity assump-
tion. By definition any element (t, C, u) in
f
MΓ(ϕγ, Σ), consists of a collection of
disks or spheres meeting the interior and disks or spheres contained in the bound-
ary CP n−1 with homology class summing to the homology class of the sections
described above. Since the homology class is primitive, no bubbling is possible
and the domain of u consists of a single disk, with at least one corner mapping to
CP n−1. In particular, for every u ∈f
MΓ(ϕγ, Σ), the set of intersections u−1(CP n)
with the divisor at infinity consists only of a single corner, corresponding to a single
strip-like end asymptotic to a Reeb chord ϑe of minimal length.
□
Remark 7.24. In fact in the case of type Γ = Γ+ in Definition 7.1, the cobordism
provided by Proposition 7.23 is trivial: By Lemma 7.13, the linearized operators
˜Du are surjective and the evaluation map at the end is surjective on the kernel of
˜Du. It follows that
f
MΓ(ϕγ, Σ) is smooth and compact. Furthermore, the natural
map f
MΓ(ϕγ, Σ) →[0, 1] is a submersion (since the map is index one and the kernel
of the linearization is exactly the kernel of ˜Du) and the moduli space f
MΓ(ϕγ, Σ) is
a trivial cobordism between the moduli spaces MΓ(ϕγ, Σ) and MΓ(ˇϕγ, Σ).


## Page 111


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
111
8. Fukaya algebras under surgery
In this section, we prove the main result Theorem 1.3 by combining the homotopy
equivalences in the previous section with broken Fukaya algebras with the local
computation in Section 7. We work with the unflattened boundary condition on
the handle. By Theorem 6.33, the resulting Fukaya algebra is homotopy equivalent
to that of the surgered Lagrangian immersion ϕϵ. Theorem 8.3 globalizes the results
of the previous section to a bijection between buildings. Given this, some algebra
identifies the potentials up to the change in projective Maurer-Cartan solution in
Theorem 1.3. After this, a stabilization argument in (172) and (173), and then the
proof of Theorem 1.3, identifies the Floer cohomologies.
8.1. Morse functions on the surgered and unsurgered Lagrangian. The
isomorphism of Floer cohomologies is induced by a map of Floer cochains that
maps the ordered self-intersection points of the original Lagrangian to the longi-
tudinal and meridian cells in the surgered Lagrangian. Topologically, the surgered
Lagrangian Lϵ is obtained from the unsurgered Lagrangian L0 by attaching the
handle
Hϵ ∼= (−1, 1) × Sn−1.
The boundary ∂Hϵ ∼= {−1, +1} × Sn−1 is glued in along small spheres around the
preimages x± ∈L0 of the self-intersection point ϕ(x+) = ϕ(x−) ∈X. Choose a
Morse function on L0 with critical points of zero index at the self-intersection points,
so that the corresponding cell decomposition has small balls σn,± and spheres σn−1,±
around the self-intersection points x±. Let σ0,± be the zero cells in the boundary
of σn−1,±. A cell structure Lϵ is derived from that on L0 by removing a ball around
each x± and gluing in a single 1-cell and single n-cell
σ1 : B1 := [−1, 1] →Lϵ,
σn : Bn ∼= Bn−1 × [−1, 1] →Lϵ
along the boundary of the 0-cells resp. n −1-cells
σ0,± : {0} →Lϵ,
σn−1,± : Bn−1 →Lϵ
as shown in Figure 14.
σ1,−
σ1,−
σn−1,−
σn−1,−
σ′
1,+
σ1,+
σn−1,
σn−1,+
Figure 13. Cell structure on the unsurgered handle


## Page 112


112
JOSEPH PALMER AND CHRIS WOODWARD
σ1
σ′
n−1,−
σn−1,−
σ′
n−1,+
σn−1,+
Figure 14. Cell structure on the surgered handle
8.2. The surgered-unsurgered bijection. With the cellular structures on the
Lagrangian and its surgery defined, we now define the chain-level map which re-
places the ordered self-intersection points to be surgered with the longitude and
meridian on the handle. The neck-stretching argument in Theorem 6.28 produces
a cobordism between rigid holomorphic maps with rigid broken holomorphic maps.
Let X denote the broken manifold obtained by quotienting the spheres S2n−1 on
either side of the n −1-cells σn−1,± by the S1-action. This cell structure is shown
in Figure 13 and 14 as the collection of blue and red spheres. The pieces of X are
(154)
X = X⊂∪X0 ∪X⊃
where
(155)
X⊂∼= CP n,
X0 ∼= Bl(CP n)
X⊃= Bl(X)
is a projective space resp.
the blow-up Bl(CP n) of projective space at a point
resp.
the blow-up Bl(X) of X at the self-intersection point ϕ0(x−) = ϕ0(x+).
The handle Hγ admits the standard cellular deformation of the diagonal induced
by positive translation on σ1 ∼= [−1, 1] and the standard Morse flow on σn−1 ∼=
Sn−1. The Fukaya algebra CF(X, ϕγ) is then homotopy equivalent to the broken
Fukaya algebra CF(X, ϕγ) as in Theorem 6.33 whose structure maps have levels
with cellular constraints.
Lemma 8.1. There exists a regular perturbation datum P = (PΓ) for holomorphic
buildings in X with boundary in ϕγ such that JΓ is the standard complex structure
on X⊂= Cn and X0 = Cn −{0}
Proof. Lemma 7.7 shows that rigid holomorphic maps to X⊂= Cn are automat-
ically regular, while Lemma 7.20 shows that rigid holomorphic maps to X0 =
Cn −{0} are regular for the standard complex structure.
□
We apply the classification of rigid maps bounding the handle in the previous sec-
tion to classify rigid holomorphic buildings. Denote by ϕγ the Lagrangian boundary


## Page 113


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
113
condition in X defined using the Lagrangian Hγ using a path γ in the local model
corresponding to the surgered or unsurgered Lagrangian.
Lemma 8.2. Suppose the perturbations on X0 vanish. There are no rigid buildings
in X so that the level in X0 has non-trivial projection to CP n−1.
Proof. The proof is by a symmetry argument. The R −{0} action on Cn −{0}
preserves the boundary condition in X0. Furthermore, the gradient trajectories in
X0 are the lines R × {p} in R × Sn−1. Thus the action of R −{0} on the union
of components mapping to X0 produces a one-parameter family of configurations
satisfying the matching condition. By rigidity, translation must be equivalent to
an automorphism of the domain, so u0 must be a cylinder C× →R × Sn−1.
□
Define the map between generators as follows. Denote by
µ = σn−1,±,
λ = σ1
the meridianal and longitudinal cells; the choice of which cell σn−1,± is immaterial
as both choices give the same counts. Define a map
I(ϕ0) →I(ϕϵ),
σ0 7→σϵ
by mapping the surgered self-intersection points
x = (x−, x+) ∈Isi(ϕ0)
7→
µ ∈Ic(ϕϵ)
x = (x+, x−) ∈Isi(ϕ0)
7→
λ ∈Ic(ϕϵ)
to the meridianal resp.
longitudinal cells and leaving the remaining generators
unchanged. Given σ0 ∈I(ϕ0)d+1 define σϵ ∈I(ϕϵ)d+1 by applying this map to each
generator. We view this as a bijection up to the homology equivalences between
σn−1,+ and σn−1,−and similar which will be explained as a stabilization.
Theorem 8.3. (cf. Fukaya-Oh-Ohta-Ono [31, 55.11, Chapter 10]) For any labeled
rigid type Γ0 with positive energy, there exists a type Γϵ of building obtained by
replacing components in X⊂bounding ϕ0 with those bounding ϕϵ, possibly after
adding edges labeled σ1, so that there is a bijection between admissible rigid moduli
spaces of buildings of positive area
(156)
MΓ0(X, ϕ0) →MΓϵ(X, ϕϵ),
u0 7→uϵ
preserving orientations. If uϵ, u0 are related by this bijection then the symplectic
areas are related as in Lemma 7.3:
A(uϵ) = A(u0) + (κ −κ)A(ϵ)
where κ resp. κ is the number of corners with boundary in ϕ0 which map to x resp.
x and A(ϵ) is the area of (132).


## Page 114


114
JOSEPH PALMER AND CHRIS WOODWARD
Proof. The bijection between maps with boundary in the unsurgered handle ϕ0
and those in the surgered handle ϕϵ in the local model in Proposition 7.2 and
Lemma 7.5 produces a correspondence between rigid types with only constraints λ
on each level in the neck region (ignoring the count of configurations with pieces
in the local model with Reeb chords of large angle, which vanishes by Proposition
8.10.) The counts of broken maps are not changed by replacing the standard handle
with the flattened handle, by the cobordism in Proposition 7.23. We compare the
numerical invariants of the corresponding buildings. Lemma 7.3 then implies that
the areas differ by (κ−κ)A(ϵ). The bijection in (156) is sign-preserving if and only
if the bijection between moduli spaces on the broken piece X⊂of (155) containing
the self-intersection point x ∈ϕ(L) is orientation preserving. This can always be
achieved by changing the orientation on the determinant line D+
x .
□
Remark 8.4. We discuss constant disks on the handle region; these will be needed
later to prove the invariance of the potential. On the pre-surgered side, there are
two constant disks
u± : S →X,
u±(S) = ϕ(x−) = ϕ(x+)
in the case dim(L0) > 2. The constant disks u± have inputs x, x resp. x, x and
outgoing labels σ0,+ resp.
σ0,−.
In the case dim(L0) = 2, there are arbitrary
numbers of inputs, as in (5.21). For the surgered Lagrangian, we have two constant
configurations u± : S →X corresponding to the classical boundary σ0,+ −σ0,−of
σ1.
Remark 8.5. The bijections between moduli spaces of holomorphic treed disks
bounding the immersion and its surgery extend to repeated inputs. Suppose Γ0 is
a type of building bounding ϕ0 with label x appearing l times, and
r = (r1, . . . , rl)
is a collection of integers. Let Γr
ϵ denote the type obtained by repeating the edge
labeled σn−1,± at the i-th place ri times. Combining Theorem 8.3 with Theorem
5.13 (or rather, it’s extension to buildings, whose proof is the same) gives for
permutation-invariant matching conditions bijections between moduli spaces
MΓ0(X, ϕ0) →MΓr
ϵ(X, ϕϵ),
u0 7→uϵ.
Each disk passing once through the handle in the positive direction meets each
generic translate of the meridian σn−1,± exactly once. If dim(L0) = 2, then the
longitudinal cell σ1 is also codimension one. In this case, let
r = (r+
1 , . . . , r+
l , r−
1 , . . . , r−
s )
be a tuple of integers represented a pattern of repetitions. If σr
ϵ is obtained by
replacing the i-th occurrence x resp. x with r+
i resp. r−
i copies of σn−1,± resp σ1,
then there is a bijection as above for exactly one of the r+
i ! resp. r−
i !-factorial of


## Page 115


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
115
the perturbations of the cycles σn−1,± resp. σ1. Indeed, each curve hitting λ hits
each generic translate of σ1 exactly once. This ends the Remark.
Lemma 8.6. The rigid moduli spaces M(X, ϕϵ)0 are invariant under replacement
of a constraint σn−1,+ with constraint σn−1,−and vice-versa.
Proof. By Proposition 7.2, for each rigid building (C, u) the boundary ∂u : ∂S →L
meets each meridian σn−1,± the same number of times that ∂u passes through the
handle Hγ ⊂L (counted with sign), and the claim follows.
□
8.3. Equivalence of potentials. We may now prove the first part of Theorem 1.3
using the bijection between curves contributing to the potentials. First we relate
the curvatures of the immersion and its surgery. We work with the broken Fukaya
algebras
CF(ϕ0) = CF(X, ϕ0),
CF(ϕϵ) = CF(X, ϕϵ)
where ϕϵ is the asymptotically-cylindrical Lagrangian defined in the local model
by the standard path γ(t) = t + 2iϵ. These broken Fukaya algebras are homotopy
equivalent to the unbroken Fukaya algebras by Theorem 6.33. Define Ψ : b0 7→bϵ
as in (5). We assume that b0 vanishes in the neighborhood of the attaching spheres
in L0 by Lemma 5.11. The following is straight-forward from Definition 1.2:
Proposition 8.7. The derivative
Db0Ψ : CF(ϕ0) →CF(ϕϵ)
is given by the identity on all generators in I(ϕ0) except x, x. On these generators
we have
x
7→
(b0(x)qA(ϵ))−1µ + b0(x)λ
(157)
x
7→
b0(x)λ
(158)
for dim(L0) > 2; while
x
7→
(b0(x)qA(ϵ))−1µ + b0(x)(b0(x)b0(x) + 1)−1λ
(159)
x
7→
b0(x)(b0(x)b0(x) + 1)−1λ
(160)
for dim(L0) = 2.
We may write the higher composition maps in terms of correlators as follows.
For • = 0, ϵ define correlators
p•
d+1(σ0, . . . , σn) ∈Λ,
m•
d(σ1, . . . , σn) =
X
σ0,α
p•
d+1(σ0, . . . , σn)σ0.
Theorem 8.8. Assume that if dim(L0) = 2, then the condition in Definition 5.21
holds. Then
(161)
X
r≥0
pϵ
r+1(Db0Ψ(σ), bϵ, . . . , bϵ) =
X
r≥0
p0
r+1(σ, b0, . . . , b0)
for each generator σ ∈I(ϕ0).


## Page 116


116
JOSEPH PALMER AND CHRIS WOODWARD
We first show that the inadmissible configurations, in the sense of Definition 8.9
below, do not contribute to the sum on the left-hand-side of (161).
Definition 8.9. A component uv : Sv →X⊂of a building u : S →X is inadmissible
if it has more than one strip-like end. A building u : S →X is admissible if it has
no inadmissible components.
Lemma 7.19 classifies the possible rigid configurations with inadmissible compo-
nents.
Proposition 8.10. The weighted count of configurations (C, u : C →X) bounding
ϕϵ with inadmissible surface components uv : Sv →X⊂in (161) and (171) vanishes.
Proof. We will show that the weighted count of configurations is a multiple of a co-
efficient of a self-intersection point in the curvature of the weakly bounding cochain
for the unsurgered Lagrangian, which vanishes. First, suppose there is a single in-
admissible component Sv. Lemma 7.19 implies that rigid such configurations have
at least two strip-like ends asymptotic to minimal length Reeb chords on the piece
Sv, so that one of the minimal length Reeb chords connects to a configuration not
containing the output.
Choose such a minimal length chord ϑ leading to a component in X0 which
does not contain the output.
Splitting at ϑ divides the configuration into two
pieces, which we denote by u+ and u−as in Figure 15. Since there is a single
inadmissible component, the piece u+ has no inadmissible components. We obtain
a building bounding the unsurgered Lagrangian as follows. Let ˆu : ˆS →X denote
the configuration obtained by replacing u−with the map to a single quadrant
bounding ϕ0, and all levels in u+ mapping to X⊂with similar quadrants, as in
Figure 15. The resulting building ˆu = (ˆu−, ˆu+) has inputs labeled b0 and output
x
x
u+
ˆu+
γ
ˆu−
u−
γ
Figure 15. Eliminating levels with multiple ends
labeled x, in the component adjacent to ϑ. For each such type Γ, let ˆΓ denote the


## Page 117


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
117
type of ˆu. We consider the union of moduli spaces of type Γ where Γ contains Γ−.
For each such type Γ, the corresponding moduli space of type ˆΓ is a product of the
moduli space for Γ−and the moduli space for type ˆΓ: We have a bijection
[
Γ⊃Γ−
MΓ(ϕϵ) →MΓ−(ϕϵ) ×
[
ˆΓ
MˆΓ(ϕ0),
u 7→(u−, ˆu+).
Here ˆΓ ranges over types with an output labeled x or x, (depending on which
minimal length chord ϑ is). The weighted sum over such configurations ˆu is the
coefficient of x or x in mb0
0 (1) which by assumption vanishes.
Suppose now that the configuration has an arbitrary number of inadmissible com-
ponents. Removing the inadmissible vertices Vertin(Γ) ⊂Vert(Γ) corresponding to
inadmissible components Sv of Definition 8.9 creates a union of trees Γ1, . . . , Γk.
At least one of these trees Γ+ := Γi must be adjacent to a single inadmissible
vertex joined at a minimal-length orbit ϑ, since by Lemma 7.19 any inadmissible
component has
em(Γ) ≥3 −d1(Γ) ≥1.
That is, one starts from any inadmissible vertex and moves outwards along the tree
away from the output, choosing an edge in Γ that corresponds to a minimal length
Reeb chord at each inadmissible vertex. If there are several such graphs, we may
choose Γi to be the graph containing the last interior edge in the given ordering,
so that the decomposition of Γ into
Γ−:= Γ −Γi,
Γ+ := Γi
is unique.
We now sum over the moduli spaces corresponding to the subgraphs separately.
Let ui denote the part of u corresponding to Γi. Replacing each component of ui
with the corresponding quadrant, and adding a single quadrant at ϑ, produces a
configuration u bounding ϕ0. Let ˆΓ denote the type of ˆu. The weighted count
of configurations ˆu over types ˆΓ vanishes, being the coefficient of x or x in mb0
0 (1)
depending on whether ϑ is a minimal length chord from Rn to iRn or vice-versa.
□
Proof of Theorem 8.8. Each correlator is a sum over contributions from disks that
pass k−resp. k+ times through the neck region in the negative resp. positive
direction:
p•
d+1(σ0, . . . , σd) =
X
k−,k+
p•,k−,k+
d+1
(σ0, . . . , σd).
Each non-zero contribution to pϵ,k−,k+
d+1
has up to k+ groups of inputs labeled µ and
up to k−groups of inputs labeled µ or λ. Let
b∩= b0 −b0(x)x −b0(x)
which is the collection of terms of b0 and bϵ that both share.


## Page 118


118
JOSEPH PALMER AND CHRIS WOODWARD
We first prove the identity (161) for generators away from the neck. Choose a
generator σ ∈I(ϕ0) not equal to x, x. By definition, Db0Ψ(σ) = σ. Let rj resp. sj
be the number of repetitions of µ resp. λ in the j-th group. Set
c(µ) = ln(b0(x)qA(ϵ)),
c(λ) = ln(b0(x)b0(x) + 1).
Suppose first that dim(L0) = 2. By Remark 8.5, the j-th group of repetitions may
be removed at the cost of changing the correlator by a factorial rj!, where rj is the
length of the group, so that
X
r≥1
pϵ
r(σ, bϵ, . . . , bϵ)
=
X
r≥1,k−,k+


k+
Y
j=1
X
rj≥0
c(µ)rj(rj!)−1




k−
Y
j=1
X
rj≥0
(−c(µ))rj(rj!)−1

−1 +
X
sj≥0
c(λ)sj(sj!)−1




(162)
pϵ,k−,k+
r
(σ, b∩, . . . , b∩).
(163)
Here the terms in the sum
−1 +
X
sj≥0
c(λ)sj(sj!)−1
come from the two “wrong-way” curves in the handle, corresponding to the points
in Sn−2 = S0 = {1, −1}. We assume that the local system is chosen so that the
boundary of the holomorphic disk in the handle bounding ϕϵ not passing through
λ has parallel transport −1. The other curve crosses the longitude once, possibly
with repetitions, hence the sum over sj in the second term. Denote by
i+ resp. i−⊂{1, . . . , r + k−+ k+}
the positions of these groups of label µ resp. λ. Define
(164)
j0(i−, i+) : I(ϕ0)r−k−−k+ →I(ϕ0)r


## Page 119


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
119
the map defined by inserting k± labels x resp. x at the positions i−, i+. Continuing
we have
(163)
=
X
k−,k+
(exp(ln(b0(x)qA(ϵ))))k+−k−(−1 + exp(ln(b0(x)b0(x) + 1))k−
pϵ,k−,k+
r
(σ, b∩, . . . , b∩)
=
X
r,k−,k+
(b0(x)qA(ϵ))k+(b0(x)−1q−A(ϵ)(−1 + (b0(x)b0(x) + 1)))k−
p0,k−,k+
r
(σ, b∩, . . . , b∩)
=
X
r,k−,k+
q(k+−k−)A(ϵ)b0(x)k+b0(x)k−pϵ,k−,k+
r
(σ, b∩, . . . , b∩))
=
X
r,i−,i+
b0(x)k+b0(x)k−p0,k−,k+
r
(σ, j0(i−, i+)(b∩, . . . , b∩))
=
X
r≥1
p0
r(σ, b0, . . . , b0).
(165)
where j0 is defined in (164). For the contributions from non-constant disks, the
first equality above is an application of Remark 8.5, the second is by the power
series of the exponential function, the third and fourth equalities are algebraic
simplifications, the fifth is by Theorem 8.3 and Proposition 8.10, and the last is
the expansion b0 = b∩+ b0(x)x + b0(x)x.
The contributions of the constant disks in the above computation match by the
following argument. The contribution of the two constant disks with inputs x, x in
Remark 8.4 to m2(x, x) is
m2(x, x) = b0(x)b0(x)(σ0,+ −σ0,−) + . . . .
We also have contributions from alternating inputs x, x, . . . , x to σ0,± with coeffi-
cient (−1)d−1/d by assumption, see Definition 5.21. The sum of these contributions
is
X
d≥1
(−1)d−1
d
(b0(x)b0(x))d(σ0,+ −σ0,−) = ln(b0(x)b0(x) + 1) (σ0,+ −σ0,−).
Since the classical boundary of σ1 is σ0,+ −σ0,−, this sum matches the classical
terms in pϵ(σn,±, c(λ)λ).
It remains to deal with the cases that the constraint on the output is one of
the cells on the neck. In the case σ = µ, the contributions to pd(µ, . . .) arise from
configurations (C, u : C →X) passing either positively or negatively through the
neck region at the outgoing node. Write
δ(ρ) = ln((b0(x) + ρ)qA(ϵ))µ + ln(b0(x)b0(x) + 1)λ.
Let pr,r+,r−denote contributions to pr from disks where the first r+ + 1 labels and
last r−labels lie on the handle. The count of disks passing through the handle


## Page 120


120
JOSEPH PALMER AND CHRIS WOODWARD
(with sign depending on whether the disk passes through negatively or positively)
is
X
r≥1
pϵ
r(µ, bϵ, . . . , bϵ)
=
b0(x)
X
r≥1
pϵ
r(b0(x)−1µ, bϵ, . . . , bϵ)
=
b0(x)
X
r≥1,r±≥0
pϵ
r,r−,r+(b0(x)−1µ, δ(0), . . . , δ(0),
bϵ, bϵ, . . . , bϵ, δ(0), . . . , δ(0))
=
b0(x)
X
r≥1,r±≥0
∂
∂ρ|ρ=0pϵ
r,r−,r+(δ(ρ), . . . , δ(ρ),
bϵ, bϵ, . . . , bϵ, δ(ρ), . . . , δ(ρ))
=
b0(x)
X
r≥1
∂
∂ρ|ρ=0(b0(x) + ρ)p0
r(x, b0, . . . , b0)
+ ∂
∂ρ|ρ=0(b0(x) + ρ)−1(−1 + exp(ln(b0(x)b0(x) + 1)))
p0
r (x, b0, . . . , b0)
(166)
=
X
r≥1
p0
r(b0(x)x, b0, . . . , b0)
−
X
r≥1
p0
r
 −1 + (b0(x)b0(x) + 1)
b0(x)
x, b0, . . . , b0
!
(167)
=
X
r≥1
p0
r(b0(x)x −b0(x)x, b0, . . . , b0)
(168)
where the terms involving p0
r(x, b0, . . . , b0) in the sum arise from configurations pass-
ing through the handle positively and terms involving p0
r(x, b0, . . . , b0) arise from
configurations passing through the handle negatively. The presence of a label µ in
the first entry forces the first node to map to the handle. There are contributions
from any number r−entries δ(ρ) at the end of the string σ and r+ entries δ(ρ)
where those labels appear on the same level of the building in the configuration.
These contribute by Remark 8.5 with a factorial entry l = (1 + r−+ r+)!−1. Since
there are 1 + r−+ r+ such entries for each l (depending on where the 0-th entry
appears in the string), we obtain a contribution of (r+ +r+)!−1 after summing over
these positions. Similarly for σ = λ we have
X
d≥1
pϵ
d(λ, bϵ, . . . , bϵ)
=
X
r≥1
qA(ϵ)p0
r(b0(x)−1q−A(ϵ)(b0(x)b0(x) + 1)x, b0, . . . , b0)
=
X
r≥1
p0
r(b0(x)−1(b0(x)b0(x) + 1)x, b0, . . . , b0).
(169)


## Page 121


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
121
From this and (168) we obtain
X
r≥1
pϵ
r(Db0Ψ(x), bϵ, . . . , bϵ)
=
X
r≥1
pϵ
r
 
b0(x)−1µ +
b0(x)
(b0(x)b0(x) + 1)λ, bϵ, . . . , bϵ
!
=
X
r≥1
p0
r(b0(x)−1(b0(x)x −b0(x)x)
+b0(x)(b0(x)b0(x) + 1)
(b0(x)b0(x) + 1)b0(x)x, b0, . . . , b0)
=
X
r≥1
p0
r(x, b0, . . . , b0).
Finally
X
r≥1
pϵ
r(Db0Ψ(x), bϵ, . . . , bϵ)
=
X
r≥1
pϵ
r(b0(x)(b0(x)b0(x) + 1)−1λ, bϵ, . . . , bϵ)
=
X
r≥1
p0
r(x, b0, . . . , b0).
(170)
If σ has no x, x terms then Db0Ψ(σ) = σ. Together (165) and (170) imply the
result for dim(L0) = 2.
Now consider the case dim(L0) > 2. Let u : C →X be a rigid broken disk
bounding ϕϵ. Disk with levels mapping to Cn which have non-minimal angle, or
with more than one strip-like-end, do not contribute by Proposition 8.10. For levels
with a single strip-like end, each level passing through the handle in the positive
resp.
negative direction must have zero resp.
one λ label to be rigid, by the
dimension formula in Lemma 7.17. The computation is then the same as in the case
dim(L0) = 2, but without the repeated λ inputs and defining c(λ) = b0(x)b0(x).
□
Proof of the potential part of Theorem 1.3. By Theorem 8.8, the coefficients of cells
not on the neck in mb0
0 (1) and mbϵ
0 (1) agree. Furthermore, for β in the surgery region
(mb0
0 (1), β)
:=
X
r
p0
r(β, b0, . . . , b0)
=
X
r
pϵ
r(Db0Ψ(β), bϵ, . . . , bϵ)
=:
(mbϵ
0 (1), (Db0Ψ)β).
Since Db0Ψ preserves the identity 1ϕ0 7→1ϕϵ, the potential is preserved by surgery:
W0(b0) = Wϵ(Ψ(b0)).
□


## Page 122


122
JOSEPH PALMER AND CHRIS WOODWARD
Remark 8.11. Equation (161) also gives the equivalence of the derivatives with
respect to a cochain τ ∈I(ϕ0)
(171)
X
r≥0
pϵ
r+1(Db0Ψ(σ), bϵ, . . . , Db0Ψ(τ), bϵ, . . . , bϵ) =
X
r≥0
p0
r+1(σ, b0, . . . , b0, τ, b0, . . . b0).
8.4. Equivalence of Floer cohomologies. To prove the isomorphisms of Floer
cohomology, we introduce a quotient CF ess(ϕ0) of CF(ϕ0) that captures the co-
homology HF(ϕ0, b0), and a quotient CF ess(ϕϵ) of CF(ϕϵ) capturing the coho-
mology HF(ϕϵ, bϵ). Recall that the generators for ϕϵ are obtained by removing
two top-dimensional cells and two ordered self-intersections and gluing in cells of
codimension 0, n −1, 1, n. Let
CF loc(ϕ0) = span({σn−1,±, σn,±}) ⊂CF(ϕ0).
Lemma 8.12. CF loc(ϕ0) is a sub-complex of CF(ϕ0).
Proof. By assumption, the almost complex structure JΓ near the self-intersection
points x, x is the standard one. For index reasons, there are no rigid buildings
(C, u : C →X) with positive area A(u) having input σn: Forgetting the constraint
would produce a building in a moduli space of negative expected dimension. Thus
mb0
1 σn,± = ∂σn,± = σn−1,±.
Since b0 ∈MC(ϕ0), we have (mb0
1 )2 = 0 and so mb0
1 σn−1,± = 0 which proves the
claim.
□
A long exact sequence argument implies that the quotient complex has isomor-
phic cohomology: The quotient
CF ess(ϕ0) = CF(ϕ0)/CF loc(ϕ0)
(with induced differential denoted mb0
1 ) fits into a short exact sequence
0 →CF loc(ϕ0) →CF(ϕ0) →CF ess(ϕ0) →0
inducing a long exact sequence in cohomology. Since CF loc(ϕ0) is acyclic,
(172)
H(CF ess(ϕ0), mb0
1 ) = H(CF(ϕ0), mb0
1 ).
Similar arguments apply to the cohomology of the surgered Lagrangian. De-
fine a subspace CF loc(ϕϵ) generated by the cells σn, σn,±, σ1,± and their classical
boundaries:
CF loc(ϕϵ) = span({σn, σn−1,+ −σn−1,−}) ⊂CF(ϕϵ)
Lemma 8.13. CF loc(ϕϵ) is a sub-complex of CF(ϕϵ)


## Page 123


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
123
Proof. Since there are no rigid treed disks with positive area and a constraint σn
on the neck, there are no quantum corrections in the formula
mbϵ
1 (σn) = ∂σn = σn−1,+ −σn−1,−.
Since (mbϵ
1 )2 = 0, we have mbϵ
1 (σn−1,+ −σn−1,−) = 0.
□
The quotient complex
CF ess(ϕϵ) = CF(ϕϵ)/CF loc(ϕϵ)
(with induced differential denoted mbϵ
1 ) fits into a short exact sequence
0 →CF loc(ϕϵ) →CF(ϕϵ) →CF ess(ϕϵ) →0.
Since CF loc(ϕϵ) is acyclic,
(173)
H(CF ess(ϕϵ), mbϵ
1 ) ∼= H(CF(ϕϵ, ), mbϵ
1 ).
Lemma 8.14. The complexes CF ess(ϕϵ) and CF ess(ϕ0) have the same dimension.
Proof. The quotient CF ess(ϕϵ) has two new generators compared to CF ess(ϕ0) cor-
responding to the longitudinal cell in dimension 1 and the meridional cell in di-
mension n −1 compared to CF ess(ϕ0), but two fewer generators corresponding to
ordered self-intersection points (x+, x−), (x−, x+) ∈Isi(ϕ0).
□
Completion of the proof of Theorem 1.3. Let σn−1,± denote the image of σn,−, σn,+
in CF ess(ϕϵ). The derivative Db0Ψ induces a map on quotient complexes by Lemma
8.6, for which we use the same notation. The complex CF ess(ϕ0) is generated by
the images of
Iess(ϕ0) = I(ϕ0) −{σn−1,±, σn,±}
and similarly for Iess(ϕϵ). Equation (171) gives the identity
(174)
(mb0
1 (τ), α) = (mbϵ
1 (Db0Ψτ), (Db0Ψ)α),
∀α,
so mb0
1 = (Db0Ψ)tmbϵ
1 (Db0Ψ).
Since Db0Ψ is invertible, the kernels and cokernels are related by
(Db0Ψ) ker mb0
1 = ker mbϵ
1 ,
im mb0
1 = (Db0Ψ)t im mbϵ
1 .
Hence, as claimed
HF(ϕϵ, bϵ) ∼= HF ess(ϕϵ, bϵ) ∼= HF ess(ϕ0, b0) ∼= HF(ϕ0, b0).
□
Remark 8.15. Recall that a deformation of a complex variety X0 over a pointed
base (S, s0) is a pair
(π : X →S, ϕ : π−1(s0) →X0)
consisting of germ π of a flat map together with an identification of the central fiber
ϕ. A deformation is versal if it is complete, that is, if every deformation is obtained
by pullback by some map; note that this is the weakest notion of versality in the


## Page 124


124
JOSEPH PALMER AND CHRIS WOODWARD
literature [14]. There are natural notions of deformation of morphisms, coherent
sheaves, and so on as in Siu [62]. A naive notion of deformation of an immersed
Lagrangian brane ϕ →L is given by a family of pairs
(ϕs : L →X, bs ∈MC(ϕs))
parametrized by a point s in a space S. Depending on the structure of ϕs, bs, one
could speak of analytic, smooth, continuous deformations and so on. Clearly, this
notion is inadequate as the deformation does not include the surgered branes near
L, and one seems to have real-codimension-one walls at valq(b) = 0. The results of
this paper imply that those walls vanish by adjoining the Maurer-Cartan spaces of
the surgeries. In this somewhat vague sense, we have shown the existence of versal
deformations of Lagrangian branes including the surgered Lagrangians. It would
be interesting to know whether there is a more precise definition of deformation of
a Lagrangian brane similar to that of a coherent sheaf in algebraic geometry.
Remark 8.16. In the proof of Theorem 1.3, we assume that the Fukaya algebras
CF(ϕ0) and CF(ϕϵ) have been defined using perturbation data satisfying good in-
variance properties in Definition 5.18 and, for Lagrangian surfaces, Definition 5.21,
explained in Section 5.3. We were left feeling that we only partially understood
Definition 5.21, and future work will hopefully clarify the situation. Note that in
dimension two, one can also assume (177) and shift the local system rather than
the Maurer-Cartan solution to prove invariance which avoids the assumption in
5.21.
Remark 8.17. The almost complex structures admit an sft-style limit in Section 6,
in which the self-intersection point is isolated by a neck-stretching. For arbitrary
choices of perturbation data, the conclusion of Theorem 1.3 holds without the
explicit formula in Definition 1.2 for the change in the weakly bounding cochains
b0, bϵ.
8.5. Variations of local system. The formulas in Definition 1.2 are equivalent to
slightly different formulas using changes in the local system rather than the weakly
bounding cochain. Suppose that the parallel longitudinal transport Lϵ from one
side of the handle {−∞} × Sn−1 to the other {∞} × Sn−1 using yϵ is given by
(175)
Lϵ = b0(x)qA(ϵ) ∈Λ0.
Theorem 8.18. Given the local system Lϵ above, the conclusions of Theorem 1.3
hold for the surgered bounding cochain
(176)
bϵ
=
b0(x)x
−
b0(x)x
+



ln(b0(x)b0(x) + 1)λ
dim(L0) = 2
b0(x)b0(x)λ
dim(L0) > 2
The proof is essentially the same as that of the main result Theorem 1.3. In
the dimension two case one may sometimes replace the change in weakly bounding


## Page 125


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
125
cochain with a change in local system. Suppose that dim(L0) = 2, L0 is connected,
and the weakly bounding cochain b0 vanishes except on a single one-chain κ :
[−1, 1] →L0 connecting x+ with x−which has only classical boundary
(177)
m1(κ) = x+ −x−.
Define bϵ = 0 and set the parallel transport Mϵ around the meridian of the local
system yϵ to be
(178)
Mϵ = b0(x)b0(x) −1 ∈Λ0.
Indeed, variation of a weakly bounding cochain b by a degree one element b′ ∈
CF 1(ϕ) is equivalent to a variation of the local system y by the corresponding
representation exp(b′) by the divisor equation (66) in Section 5.3.
9. Quasi-isomorphisms
In this section we show Theorem 1.6, namely that the objects defined by the
surgered and unsurgered Lagrangian are quasi-isomorphic in a simplified version of
the Fukaya category.
9.1. Quasi-isomorphisms induced by Hamiltonian perturbation. Let ϕ′
0
be a Hamiltonian perturbation of ϕ0 as in the statement of Theorem 1.3 and
MC(ϕ′
0), MC(ϕ0) the corresponding Maurer-Cartan spaces. Symplectomorphisms
induce A∞isomorphisms, since one can use the pull-back almost complex structure
for which the holomorphic disk counts are the same. A change in almost complex
structure from the pull-back almost complex structure to the original almost com-
plex structure then produces an A∞homotopy equivalence by [18, Section 5]. For
each b0 ∈MC(ϕ0) there exists a b′
0 ∈MC(ϕ′
0) with the same value of the potential:
w(b0) = w(b′
0) ∈Λ.
Lemma 5.6 implies that this correspondence extends to the case that the element
b0 has slightly negative q-valuation at x, so that if b0 ∈MCδ(ϕ0, ϵ) then b′
0 ∈
MCδ(ϕ′
0, ϵ). Fix such b0, b′
0 and let Fuk ˜ϕ0(X) denote the A∞category with objects
(ϕ0, b0) and (ϕ′
0, b′
0) with higher compositions for d ≥1
(179)
mb0,...,bd
d
(a1, . . . , ad) =
X
k0,...,kd≥0
md+k0+...+kd(b0, . . . , b0
|
{z
}
k0
, a1, . . . ,
bd−1, . . . , bd−1
|
{z
}
kd−1
, ad, bd, . . . , bd
|
{z
}
kd
)
and define m0(1) = 0; here the notation is motivated by (7). The A∞associativity
relation for the algebra CF(˜ϕ) for the Lagrangian ˜ϕ of (7) implies that Fuk ˜ϕ0(X)
is a flat A∞category.
Lemma 9.1. (ϕ′
0, b′
0) is quasi-isomorphic to (ϕ0, b0) in Fuk ˜ϕ0(X).


## Page 126


126
JOSEPH PALMER AND CHRIS WOODWARD
ϕ0
ϕ′
0
x
ϕϵ
ϕ′
0
Figure 16. The unsurgered immersion and its perturbation; the
surgered immersion and its perturbation
Sketch of proof. The space CF(ϕ0, ϕ′
0) is naturally a (CF(ϕ0), CF(ϕ′
0))-bimodule
as explained in Charest-Woodward [18, Chapter 6]. The structure maps are defined
by a count of (J, H)-holomorphic strips bounding ϕ0, ϕ′
0, where H : [0, 1] × X →R
is the Hamiltonian whose flow defines ϕ′
0. Let
˜H ∈C∞(R × [0, 1] × X))
be a function limiting to 0 as s →−∞and H as s →+∞. A count of treed
(J, ˜H)-holomorphic strips implies that the bimodule (CF(ϕ0), CF(ϕ′
0)) is homotopy
equivalent to CF(ϕ0). The image of the unit 1ϕ0 under the homotopy equivalence
with CF(ϕ0, ϕ′
0), and the image of the unit 1ϕ0 under the homotopy equivalence
with CF(ϕ′
0, ϕ0) provide the necessary elements
(180)
α0 ∈CF(ϕ0, ϕ′
0),
β0 ∈CF(ϕ′
0, ϕ0),
δ0 ∈CF(ϕ0, ϕ0),
δ′
0 ∈CF(ϕ′
0, ϕ′
0)
as in (8). The fact that the composition of these two homotopy equivalences is
homotopic to the identity implies the necessary composition relation for m2(α0, β0)
and m2(β0, α0).
□
We also have a Fukaya category with the same two objects, but where the struc-
ture maps are defined by pseudoholomorphic buildings. As a special case of Theo-
rem 6.33 (with notation from (7)) counts of quilted disks define an A∞homotopy
equivalence
CF(X, ˜ϕ0) ∼= CF(X, ˜ϕ0).
Let Fuk ˜ϕ0(X) be the category whose objects are ϕ0 and ϕ′
0, and whose morphisms
are the sub-spaces of CF(X, ˜ϕ0) in the obvious way. The homotopy equivalence of
A∞algebras induces a homotopy equivalence of A∞categories
Fuk ˜ϕ0(X) →Fuk ˜ϕ0(X).
The existence of quasi-isomorphisms with the broken limit CF(X, ϕ0) implies that
(ϕ0, b0) and (ϕ′
0, b′
0) define quasi-isomorphic objects in Fuk ˜ϕ0(X).


## Page 127


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
127
9.2. Quasi-isomorphism with the surgery. We now use the computations
above to show that the surgered Lagrangian is quasi-isomorphic to the unsurg-
ered Lagrangian as objects in the Fukaya category. Since the intersections of ϕ0
and ϕ′
0 are disjoint from the surgery regions, we have a canonical bijection between
intersection points (ϕ0 ×ϕ′
0)−1(∆) and (ϕϵ ×ϕ′
0)−1(∆). These induce identifications
(181)
CF(ϕ0, ϕ′
0) ∼= CF(ϕϵ, ϕ′
0),
CF(ϕ′
0, ϕ0) ∼= CF(ϕ′
0, ϕϵ).
We denote by
αϵ ∈CF(ϕϵ, ϕ′
0),
βϵ ∈CF(ϕ′
0, ϕϵ)
the images of α0 and β0 under the isomorphisms (181). Furthermore, let
δϵ ∈CF(ϕϵ, ϕϵ)
the image of δ0 under the map DΨ. We claim
(182)
1ϕ0 = m
b0,b′
0,b0
2
(β0, α0) −mb0,b0
1
(δ0) = (Db0Ψ)t(m
bϵ,b′
0,bϵ
2
(βϵ, αϵ) −mbϵ,bϵ
1
(δϵ)).
The configurations contributing to the composition maps in the last expression
in (182) are broken maps whose components mapping to X⊂either have a single
strip-like end (in which case they are classified in Section 7.1) or those with more
than one strip-like end. The identity
mb0,b0
1
(δ0) = (Db0Ψ)tmbϵ,bϵ
1
(δϵ)
is a special case of (174). To prove
m
b0,b′
0,b0
2
(β0, α0) = (Db0Ψ)t(m
bϵ,b′
0,bϵ
2
(βϵ, αϵ)
note that if a component Sv0 mapping to X⊂∼= Cn has more than one strip-lie
end, then one of the components of S −Sv0 must contain the corners labeled α0, β0
and the others must contain only edges labeled b0, as in Figure 17; compare with
Figure 15 which involved a single Lagrangian.
u+
u−
γ
ϕϵ
ϕ′
0
Figure 17. Eliminating levels with multiple ends, second version


## Page 128


128
JOSEPH PALMER AND CHRIS WOODWARD
Since at least one of the other ends maps to a minimal length Reeb chord, the
contributions from such configurations vanish, as in Proposition 8.10. The corre-
spondence in Theorem 8.3 then implies the required identity. A similar identity
holds for the composition in the reverse order, showing that the composition is the
identity for ϕϵ. Hence αϵ, βϵ are quasi-isomorphisms as claimed. This completes
the proof of Theorem 1.6.
9.3. Mapping cones. In the case of a single intersection point of a pair of em-
bedded Lagrangians, the main result of this paper reproduces the identification of
the surgery with the mapping cone, which was the original intent of Fukaya-Oh-
Ohta-Ono [31, Chapter 10], see also Abouzaid [2], Mak-Wu [46], Tanaka [63], and
Chantraine-Dimitroglou-Rizell-Ghiggini-Golovko [17, Chapter 8]. The special case
that one of the Lagrangians is a Lagrangian sphere was treated earlier by Seidel
[57] in his paper on symplectic Dehn twists. Pascaleff-Tonkonog [50] have devel-
oped a generalization to clean intersections, related to higher-dimensional analogs
of Lagrangian mutation.
We put ourselves in the following simple version of the Fukaya category, gen-
erated by two branes. Suppose that the immersion ϕ0 : L0 →X is the disjoint
union of immersions ϕ± : L± →X intersecting transversally equipped with weakly
bounding cochains b± ∈MC(ϕ±). Denote the combined immersion by
ϕ0 = ϕ−⊔ϕ+ : L−⊔L+ →X.
Recall that CF(ϕ−, ϕ+) is the subspace of CF(ϕ0) generated by the intersection
points of ϕ−and ϕ+. As vector spaces
CF(ϕ0) ∼= CF(ϕ−) ⊕CF(ϕ+) ⊕CF(ϕ−, ϕ+) ⊕CF(ϕ+, ϕ−)
and CF(ϕ±) are A∞sub-algebras.
The space CF(ϕ−, ϕ+) is naturally an A∞
bimodule over the A∞algebras CF(ϕ−) and CF(ϕ+). Let
c ∈CF(ϕ−, ϕ+),
mb−,b+
1
(c) = 0
be a cocycle. Let ψ : K →X be another immersed Lagrangian brane in X meeting
ϕ+, ϕ−transversally and disjoint from ϕ(L+)∩ϕ(L−). Suppose that K is equipped
with a bounding cochain k ∈MC(ψ) with
W(k) = W(b−) = W(b+).
The complex Hom(Cone(c), K) is by definition
Hom(Cone(c), K) = CF(L−, K)[1] ⊕CF(L+, K)
with differential mb−+b++c,k
1
induced by the differentials on CF(L±, K) and com-
position with c, see for example Seidel [59, 2.10].


## Page 129


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
129
Theorem 9.2. (cf. [31, Remark 54.9, Chapter 10]) Suppose L±, K are as above
and dim(L±) > 2. Suppose that x ∈ϕ−(L−) ∩ϕ+(L+) is an odd self-intersection
point and
c = q−A(ϵ)x ∈CF(L−, L+),
mb−,b+
1
c = 0
is a cocycle. Let ϕϵ : Lϵ →X denote the ϵ-surgery at x with cochain bϵ = b+ + b−
with b± vanishing in an open neighborhood of x. Then the complex CF(ϕϵ, K) with
differential mbϵ,k
1
is homotopy equivalent to the mapping cone Hom(Cone(c), K).
Remark 9.3. The special case that one of the Lagrangians is a Lagrangian sphere
was treated earlier by Seidel [57]. In this case, say L−is a sphere, the surgery
ϕϵ : Lϵ →X is embedded and Hamiltonian isotopic to the Dehn twist τL−L+ of
L+ around L−. Here the Dehn twist τL−∈Aut(X, ω) is a symplectomorphism on
X that restricts to minus the identity on L−and is supported on a neighborhood
of L−. Surgering all self-intersections simultaneously gives an exact triangle in the
derived Fukaya category
Hom(L−, L+)L−→L+ →τL−(L+) →Hom(L−, L+)L−[1],
see Seidel [59, Proposition 9.1]. This ends the Remark.
Proof of Theorem 9.2. We apply neck stretching to obtain homotopy-equivalent
complexes defined by broken maps. Let ϕ± : L± →X be embeddings as in the
statement of the theorem and b± ∈MCδ(L±) projective Maurer-Cartan solutions.
As in Theorem 6.33, the complexes CF(ϕϵ, K), Hom(Cone(c), K) are homotopy
equivalent to those defined by curve counts in the broken limit X in which the almost
complex structure is stretched along a sphere enclosing the given intersection point
x ∈L−∩L+.
We now compare the broken limits. Any configuration (C, u0 : C →X) with
boundary on L0 ∪L1 ∪K, and a single corner at c, contributing to a structure
map of Hom(Cone(c), K) corresponds under the map in Theorem 8.3 with a curve
(C, uϵ : C →X) with boundary on Lϵ ∪K. The number of corners of u0 on x is
equal to the number of times that uϵ passes through the handle Hϵ positively. Since
dim(L0) > 2 by assumption, any rigid curve uϵ passes in the positive direction
on the handle by Theorem 8.3.
That is, there are no “wrong way” corners to
deal with in the bijection between holomorphic disks. On the surgered side, only
configurations passing through the handle in the positive direction can be rigid,
by the dimension formula in Lemma 7.17. The area of A(uϵ) is A(u0) −κA(ϵ)
as in Lemma 7.3. Counting rigid curves uϵ defines the differential on CF(ϕϵ, K)
using the bounding cochain b−+ b+. One obtains an identification of the complex
CF(ϕϵ, K) with Hom(Cone(c), K).
□
Remark 9.4. Fukaya-Oh-Ohta-Ono [31, Theorem 56.14, Chapter 10] use this iden-
tification with the mapping cone to show that there exists a Lagrangian in the


## Page 130


130
JOSEPH PALMER AND CHRIS WOODWARD
six-dimensional symplectic torus whose Fukaya algebra (defined using their foun-
dational system, presumably equivalent to ours) has no projective Maurer-Cartan
solutions.
References
[1] C. Abbas. An introduction to compactness results in symplectic field theory. Springer, Hei-
delberg, 2014.
[2] M. Abouzaid. On the Fukaya categories of higher genus surfaces. Advances in Mathematics
217: 1192–1235, 2008.
[3] M. Abouzaid. Framed bordism and Lagrangian embeddings of exotic spheres. Ann. of Math.
(2) 175:71–185, 2012.
[4] M. Akaho and D. Joyce. Immersed Lagrangian Floer Theory. J. Differential Geom. 86:381–
500, 2010.
[5] E. Arbarello, M. Cornalba, and P. A. Griffiths. Geometry of algebraic curves. Volume II,
volume 268 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of
Mathematical Sciences]. Springer, Heidelberg, 2011. With a contribution by Joseph Daniel
Harris.
[6] M. F. Atiyah and R. Bott. The Yang-Mills Equations over Riemann Surfaces. Philosophical
Transactions of the Royal Society of London. Ser. A. 308 (1505): 523–615.
[7] Michéle Audin and Mihai Damian. Morse Theory and Floer Homology. Translated from the
2010 French original by Reinie Erné. Universitext. Springer, London, 2014.
[8] D. Auroux. Asymptotically holomorphic families of symplectic submanifolds. Geom. Funct.
Anal., 7(6):971–995, 1997.
[9] D. Auroux. Mirror symmetry and T-duality in the complement of an anticanonical divisor.
J. Gokova Geom. Topol., 1:51–91, 2007.
[10] D. Auroux. Special Lagrangian fibrations, wall-crossing, and mirror symmetry. In Geometry,
analysis, and algebraic geometry, volume 13 of Surveys in Differential Geometry, pages 1–47.
Intl. Press, 2009.
[11] D. Auroux, D. Gayet, and J.-P. Mohsen. Symplectic hypersurfaces in the complement of an
isotropic submanifold. Math. Ann., 321(4):739–754, 2001.
[12] P. Biran and O. Cornea. Quantum structures for Lagrangian submanifolds. arxiv:0708.4221.
[13] F. Bourgeois, Y. Eliashberg, H. Hofer, K. Wysocki, and E. Zehnder. Compactness results in
symplectic field theory. Geom. Topol., 7:799–888 (electronic), 2003.
[14] Catanese, F. A superficial working guide to deformations and moduli. Handbook of moduli.
Vol. I, 161–215, Adv. Lect. Math. (ALM), 24, Int. Press, Somerville, MA, 2013. Retrieved
at http://www.mathe8.uni-bayreuth.de/pdf/CataneseFabrizio/128.pdf
[15] K. Cieliebak, T. Ekholm, and J. Latschev. Compactness for holomorphic curves with switch-
ing Lagrangian boundary conditions. J. Symplectic Geom. 8 (2010), no. 3, 267–298.
[16] S. Chanda. Floer Cohomology and Higher Mutations. arxiv:2301.08311.
[17] B. Chantraine, G. Dimitroglou Rizell, P. Ghiggini, R. Golovko. Geometric generation of the
wrapped Fukaya category of Weinstein manifolds and sectors. arxiv:1712.09126
[18] F. Charest and C. Woodward. Floer theory and flips. Mem. Amer. Math. Soc. 279, 2022.
[19] C.-H. Cho. Products of Floer cohomology of torus fibers in toric Fano manifolds. Comm.
Math. Phys. 260: 613–640, 2005.
[20] C.-H. Cho and Y.-G. Oh. Floer cohomology and disc instantons of Lagrangian torus fibers
in Fano toric manifolds. Asian J. Math., 10(4):773–814, 2006.


## Page 131


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
131
[21] K. Cieliebak and K. Mohnke. Compactness for punctured holomorphic curves. J. Symplectic
Geom., 3(4):589–654, 2005.
[22] K. Cieliebak and K. Mohnke. Symplectic hypersurfaces and transversality in Gromov-Witten
theory. J. Symplectic Geom., 5(3):281–356, 2007.
[23] J. P. Demailly. Complex Analytic and Differential Geometry. Université de Grenoble.
http://www-fourier.ujf-grenoble.fr/∼demailly/manuscripts/agbook.pdf
[24] G. Dimitroglou Rizell, T. Ekholm, and D. Tonkonog. Refined disk potentials for immersed
Lagrangian surfaces. J. Differential Geom. 121:459–539, 2022. arxiv:1806.03722.
[25] S. K. Donaldson. Symplectic submanifolds and almost-complex geometry. J. Differential
Geom. 44 (1996), no. 4, 666–705.
[26] Tobias Ekholm. Morse flow trees and Legendrian contact homology in 1-jet spaces. Geom.
Topol., 11:1083–1224, 2007.
[27] K.-Y. Fang. Geometric constructions of mapping cones in the Fukaya category. Ph.D. Thesis,
Berkeley, 2018.
[28] A. Floer. Monopoles on asymptotically flat manifolds. In: Hofer H., Taubes C.H., Wein-
stein A., Zehnder E. (eds) The Floer Memorial Volume. Progress in Mathematics, vol 133.
Birkhäuser Basel.
[29] O Forster and K. Knorr. Über die Deformationen von Vektorraumbündeln auf kompakten
komplexen Räumen. (German) Math. Ann. 209 (1974), 291–346.
[30] U. Frauenfelder and K. Zehmisch. Gromov compactness for holomorphic discs with totally
real boundary conditions. J. Fixed Point Theory Appl. 17 (2015), no. 3, 521–540.
[31] K. Fukaya,
Y.-G. Oh,
H. Ohta,
and K. Ono. Lagrangian intersection Floer the-
ory:
anomaly and obstruction.,
volume 46 of AMS/IP Studies in Advanced Math-
ematics. American Mathematical Society,
Providence,
RI, 2009. Orientation chapter
at https://www.math.kyoto-u.ac.jp/∼fukaya/bookchap9071113.pdf version 2007. Surgery
chapter at https://www.math.kyoto-u.ac.jp/ fukaya/Chapter10071117.pdf.
[32] S. Ganatra. Symplectic Cohomology and Duality for the Wrapped Fukaya Category. PhD
Thesis, Massachusetts Institute of Technology, 2006.
[33] R. Harvey and J. Polking. Removable singularities of solutions of linear partial differential
equations. Acta Math. 125:39–56 1970.
[34] L. Haug. Lagrangian antisurgery. Math. Res. Lett. 27:1423–1464, 2020.
[35] J. Hicks. Wall-crossing from Lagrangian Cobordisms. Algebr. Geom. Topol. 24: 3069–3138,
2024. arXiv:1911.09979.
[36] J. Hicks. Lagrangian cobordisms and Lagrangian surgery. Comment. Math. Helv. 98:509–595,
2023. arXiv:2102.10197.
[37] H. Hong, Y. Kim, and S.-C. Lau. Immersed two-spheres and SYZ for Gr(2,C4) and OG(1,C5).
arxiv:1805.11738.
[38] A. Jacob, and S.-T. Yau. A special Lagrangian type equation for holomorphic line bundles.
Math. Ann. 369 (2017), no.1– 2, 869–898.
[39] D. Joyce. Conjectures on Bridgeland stability for Fukaya categories of Calabi-Yau manifolds,
special Lagrangians, and Lagrangian mean curvature flow. EMS Surv. Math. Sci. 2 (2015).
arxiv:1401.4949.
[40] A. Kapustin and Y. Li. D-branes in Landau-Ginzburg models and algebraic geometry. Jour-
nal of High Energy Physics, 12:5, 2003. curvature flow. EMS Surv. Math. Sci. 2 (2015).
arxiv:hep-th/0210296.
[41] M. Kontsevich and Y. Manin. Gromov-Witten classes, quantum cohomology, and enumera-
tive geometry. Comm. Math. Phys. 164:525-562, 1994.


## Page 132


132
JOSEPH PALMER AND CHRIS WOODWARD
[42] M. Kontsevich and Y. Soibelman. Affine structures and non-Archimedean analytic spaces. In
The unity of Mathematics, volume 244 of Progr. Math., pages 321–385. Birkhäuser Boston,
Boston, MA, 2006.
[43] F. Lalonde and J.-C. Sikorav. Sous-variétés lagrangiennes et lagrangiennes exactes des fibrés
cotangents. Commentarii mathematici Helvetici, 66(1):18–33, 1991.
[44] R. B. Lockhart and R. C. McOwen. Elliptic differential operators on noncompact manifolds
Annali della Scuola Normale Superiore di Pisa - Classe di Scienze, Série 4, Volume 12, no.
3, p. 409–447, 1985.
[45] D. McDuff and D. Salamon. J-holomorphic curves and symplectic topology, volume 52 of
American Mathematical Society Colloquium Publications. American Mathematical Society,
Providence, RI, 2004.
[46] C. Y. Mak and W. Wu. Dehn twist exact sequences through Lagrangian cobordism. Compos.
Math. 154, no. 12, 2485–2533, 2018. arxiv:1509.08028.
[47] S. Ma’u, K. Wehrheim, and C.T. Woodward. A∞-functors for Lagrangian correspondences.
Selecta Math. 24(3), p. 1913–2002, 2018.
[48] Y. G. Oh. Riemann-Hilbert problem and application to the perturbation theory of analytic
discs. Kyungpook Math. J., 35(1):39–75, 1995.
[49] J. Palmer and C. Woodward. Immersed Lagrangian Floer theory and Maslov flow. Algebr.
Geom. Topol. 21(5): 2313–2410, 2021. arXiv:1804.06799.
[50] J. Pascaleff and D. Tonkonog. The wall-crossing formula and Lagrangian mutations. Adv.
Math. 361:106850, 2020. arxiv:1711.03209.
[51] L. Polterovich. The surgery of Lagrange submanifolds. Geom. Funct. Anal.
1: 198–210,
1991.
[52] M. Pozniak. Floer homology, Novikov rings and clean intersections. Northern California
Symplectic Geometry Seminar, 119-181, AMS Transl. Ser. 2, 196, AMS, Providence, RI,
1999.
[53] J. Robbin and D. Salamon. Asymptotic behaviour of holomorphic strips. Ann. Inst. H.
Poincaré Anal. Non Linéaire 18:573–612, 2001.
[54] F. Schmäschke. Floer homology of Lagrangians in clean intersection. arxiv:1606.05327.
[55] R. T. Seeley. Extension of C∞functions defined in a half space. Proc. Amer. Math. Soc. 15:
625–626, 1964.
[56] P. Seidel. Fukaya categories and Picard-Lefschetz theory. Zurich Lectures in Advanced Math-
ematics. European Mathematical Society (EMS), Zürich, 2008.
[57] P. Seidel. A long exact sequence for symplectic Floer cohomology. Topology, 42(5):1003–1063,
2003.
[58] P. Seidel. Graded Lagrangian submanifolds. Bull. Soc. Math. France, 128(1):103–149, 2000.
[59] P. Seidel. Homological mirror symmetry for the quartic surface. Memoirs of the American
Mathematical Society, 2015, Volume 236. arXiv:0310414
[60] P. Seidel. Homological mirror symmetry for the genus two curve. J. Algebraic Geom. 20:727–
769, 2011.
[61] N. Sheridan and I. Smith. Lagrangian cobordism and tropical curves. J. Reine Angew. Math.
774 (2021), 219–265. arXiv:1805.07924.
[62] Y.T. Siu and G. Trautmann. Deformations of coherent analytic sheaves with compact sup-
ports. Mem. Amer. Math. Soc. 29 (1981), no. 238.
[63] H. L. Tanaka. Surgery induces exact sequences in Lagrangian cobordisms. arXiv:1805.07424.
[64] R.P. Thomas and S. T. Yau. Special Lagrangians, stable bundles and mean curvature flow.
Comm. Anal. Geom. 10 (2002), no. 5, 1075–1113.


## Page 133


IMMERSED FLOER COHOMOLOGY AND LAGRANGIAN SURGERY
133
[65] S. Venugopalan and C. Woodward. Tropical Fukaya algebras. To appear in Memoirs of the
Eur. Math. Soc. arxiv:2004.14314.
[66] K. Wehrheim and C. Woodward. Exact triangle for fibered Dehn twists. Res. Math. Sciences
3:17, 2016. arxiv:1503.07614.
[67] K. Wehrheim and C.T. Woodward. Orientations for holomorphic quilts. arXiv:1503.07803.
[68] A. Weinstein. Removing intersections of Lagrangian immersions. Illinois J. Math. 27: 484–
500, 1983.
Department of Mathematics - Seeley Mudd Building, Amherst College, 31 Quad-
rangle Drive, Amherst, MA 01002, U.S.A.
Email address:
jpalmer@amherst.edu
Mathematics-Hill Center, Rutgers University, 110 Frelinghuysen Road, Piscat-
away, NJ 08854-8019, U.S.A.
Email address: woodwardc@gmail.com

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_01943v11_invariance_of_immersed_floer_cohomology_under_lagrangian_surgery
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_01943V11_INVARIANCE_OF_IMMERSED_FLOER_COHOMOLOGY_UNDER_LAGRANGIAN_SURGERY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
