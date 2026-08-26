---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1510.05771
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1510.05771_Cosmological_modelling_with_Regge_calculus

> Source: 1510.05771_Cosmological_modelling_with_Regge_calculus.pdf

> Pages: 8

---


## Page 1


arXiv:1510.05771v1  [gr-qc]  14 Oct 2015
Cosmological modelling with Regge
calculus
Rex G Liu and Ruth M Williams
DAMTP, CMS, Wilberforce Rd Cambridge, CB3 0WA, UK
Email : R.G.Liu.01@cantab.net
Abstract
The late universe’s matter distribution obeys the Copernican princi-
ple at only the coarsest of scales.
The relative importance of such in-
homogeneity is still not well understood. Because of the Einstein ﬁeld
equations’ non-linear nature, some argue a non-perturbative approach is
necessary to correctly model inhomogeneities and may even obviate any
need for dark energy. We shall discuss an approach based on Regge cal-
culus, a discrete approximation to general relativity: we shall discuss the
Collins–Williams formulation of Regge calculus and its application to two
toy universes. The ﬁrst is a universe for which the continuum solution is
well-established, the Λ-FLRW universe. The second is an inhomogeneous
universe, the ‘lattice universe’ wherein matter consists solely of a lattice
of point masses with pure vacuum in between, a distribution more similar
to that of the actual universe compared to FLRW universes. We shall
discuss both regular lattices and one where one mass gets perturbed.
1
Introduction
Friedmann–Lemaˆıtre–Robertson–Walker (FLRW) models have been extremely
successful in explaining many cosmological observations, including, most no-
tably, the Hubble expansion, the cosmic microwave background (CMB), and
baryon acoustic oscillations.
Indeed, the underlying Copernican assumption
appears well-supported by precision measurements showing the CMB to be
isotropic to within one part in 105 [1]. Yet the late, matter-dominated uni-
verse obeys the Copernican principle at only the coarsest of scales: most matter
is clustered into large-scale structures with large voids in between, and the phys-
ical eﬀects of such ‘lumpiness’ are still not fully understood.
There has been intense interest recently over the possible importance of
inhomogeneities to observational cosmology. For instance, it has been proposed
that the universe’s observed acceleration is actually an apparent eﬀect, a result
of ﬁtting a homogeneous model to data from an inhomogeneous source, and
because of its non-linear structure, the inhomogeneities can only be modelled
correctly by non-perturbative methods [2, and references therein].
1


## Page 2


Regge calculus [3] oﬀers one non-perturbative approach. It is a discretisa-
tion of general relativity that can in principle approximate any space–time. This
work will focus on a form of Regge calculus ﬁrst devised by Collins and Williams
(CW) [4] and further developed by Brewin [5]. We shall examine the formal-
ism’s potential to non-perturbatively approximate inhomogeneous cosmologies.
Section 2 will present a cursory introduction to Regge calculus and the CW
formalism. To deepen our understanding of the formalism, Section 3 will apply
it to a space–time for which the continuum solution is well-known, the closed
vacuum Λ-FLRW space–time. Section 4 will adopt the formalism to model a toy
inhomogeneous universe, the closed ‘lattice universes’ where matter consists of
massive particles arranged into a regular lattice on space-like Cauchy surfaces.
Such matter content would be more representative of the actual universe’s com-
pared to that of FLRW. Section 5 will summarise and present a few directions
in which this work can be extended.
2
Regge calculus and the Collins–Williams for-
malism
In general relativity, one can obtain the Einstein ﬁeld equations by varying the
Einstein–Hilbert action
SEH =
1
16π
Z
R √−g d4x
(1)
with respect to the metric tensor gµν, where R is the Ricci scalar and g =
det(gµν). The action is evaluated over a continuous manifold.
Figure 1: Discretisation of a continu-
ous manifold into a skeleton.
θ(j)
i
θ(j)
i
ﬂatten
δi
Figure 2: Conical singularity at a 2-
dimensional hinge (vertex).
If the
hinge is ﬂattened, a gap of angle δi
opens up between two blocks.
The key idea of Regge calculus is to replace this continuous manifold with a
discrete piece-wise linear one (Fig. 1), known as a skeleton. A skeleton essentially
consists of ﬂat blocks glued together at shared faces. As the blocks are ﬂat, the
interior metric is the Minkowski metric. Curvature manifests itself as conical
singularities centred on the sub-faces of co-dimension 2, known as hinges; if
one were to ﬂatten a hinge (Fig. 2), a gap would open up between two of
the blocks, and the size of this gap, the deﬁcit angle, gives a measure of the
curvature. The Regge analogue to the metric are the block edge-lengths. Since
2


## Page 3


curvature has support on the hinges only, the integration in (1) reduces to a
discrete summation over the hinges, and the Einstein–Hilbert action reduces to
the Regge action
SRegge = 1
8π
X
i ∈{hinges}
Ai δi,
(2)
where Ai are the hinge areas and δi their corresponding deﬁcit angles. The Regge
equations are then obtained by varying SRegge with respect to the edge-lengths.
The CW formalism is essentially a Regge approximation of FLRW space–
times using a skeleton that mimics FLRW symmetries.
FLRW space–times
admit a foliation by Cauchy surfaces of constant curvature; all surfaces are
identical to each other apart from an overall scale factor. CW Cauchy surfaces
approximate their FLRW counterparts by tessellating them with a single regular
polytope. Although the formalism can be generalised to other tessellations and
background curvatures, we shall focus only on tessellations of closed universes
using identical, equilateral tetrahedra; there are only three such possible tessel-
lations, consisting of 5, 16, or 600 tetrahedra [6]. All edge-lengths in a surface
are identical to each other, and all surfaces are identical to each other apart
from an overall scaling. To complete the 4-dimensional skeleton, the surfaces
are glued together by a series of time-like struts {mi} that connect vertices in
one surface to their time-evolved images in the next.
Then the world-tubes
of the tetrahedra between pairs of consecutive surfaces form the skeleton’s 4-
blocks. The surfaces can be parametrised by a time parameter t. After we have
obtained the Regge equations though, we shall take the continuum time limit
where the time separation between surfaces goes to zero, dt →0; this generates
a series of diﬀerential equations for the Cauchy surface edge-lengths l(t). Thus,
the CW formalism is actually a continuum time formulation of Regge calculus.
Since the original FLRW Cauchy surfaces are 3-spheres, our CW Cauchy
surfaces are actually triangulations of 3-spheres and can therefore be embedded
into 3-spheres in E4. As Brewin noted [5], the embedding radius R(t) provides
a natural analogue to the FLRW scale factor a(t). We explored this idea further
in [7] and found multiple ways to deﬁne the radius – we could take, for instance,
the radius to the vertices or to the tetrahedral centres – but regardless of the
choice, the radius would always be related to the tetrahedral edge-length by
some constant scaling Z,
R(t) = Z l(t).
(3)
Brewin [5] noted that there are actually two ways to vary the Regge action.
The ﬁrst is to impose the symmetry constraints on the skeleton ﬁrst – that
is, require all tetrahedral edges in a surface to have equal length and all struts
between the same pair of surfaces to have equal length. When we vary one edge,
the constraints require that all other edges sharing the same length be varied
simultaneously. This is called global variation. The alternative approach is to
ﬁrst vary each edge individually and afterwards impose the constraints. This is
called local variation and is more analogous to how the Einstein–Hilbert action
is varied in standard general relativity; in that case, the action gets varied with
respect to an unconstrained metric ﬁrst, and the Copernican symmetries are
3


## Page 4


imposed afterwards on the resulting Einstein ﬁeld equations. To locally vary
the CW skeleton though, we need to fully triangulate the skeleton; otherwise, the
geometry of the varied skeleton would not be well-deﬁned [5, 7]. Triangulation
is done by introducing a set of diagonal edges {di} between Cauchy surfaces.
If the local and global actions are equivalent, then the global Regge equation
can be related to the local one via a chain rule [5]: if we vary globally with respect
to some edge q, we can express this variation as
∂S
∂q =
X
i
∂S
∂lℓ
i
∂lℓ
i
∂q +
X
i
∂S
∂mℓ
i
∂mℓ
i
∂q +
X
i
∂S
∂dℓ
i
∂dℓ
i
∂q ,
(4)
where the superscript ℓdenotes that the relevant edges are being varied locally.
It is immediately evident that any solution of the local Regge equations, 0 =
∂S
∂lℓ
i =
∂S
∂mℓ
i = ∂S
∂dℓ
i , would also be a solution of the global equation, 0 = ∂S
∂q , but
the converse is not necessarily true. In the models we shall consider, the local
and global actions are indeed equivalent [7, 8].
Finally, Brewin noted certain analogies between the CW and the ADM for-
malisms [5]. The tetrahedral edge-lengths {li} determined the Cauchy surface
3-geometry and were therefore analogous to the 3-metric (3)gij. The time-like
struts were analogous to the ADM lapse functions. The diagonals were anal-
ogous to the ADM shift functions.
Thus, we shall call the Regge equations
obtained from the tetrahedral edges the evolution equation, from the struts the
Hamiltonian constraints, and from the diagonals the momentum constraints.
There are, however, certain caveats to this analogy [9, and references therein].
3
CW models of closed Λ-FLRW space–times
When there is a non-zero cosmological constant Λ, both the Einstein–Hilbert
action and the Regge action acquire a volume term
1
16π
Z
(R −2 Λ) √−g d4x
→
1
8π


X
i ∈{hinges}
Ai δi −
X
i ∈{4-blocks}
Λ V (4)
i

,
(5)
where {V (4)
i
} are the 4-block volumes. The Regge model was studied extensively
in [7]. From both local and global variation, the continuum-time Hamiltonian
constraint was found to be
l2 = 6 N1
N3 Λ
(2π −nθ)
tan
  1
2θ
 ,
(6)
where N1 and N3 are, respectively, the numbers of tetrahedral edges and tetrahe-
dra in a Cauchy surface, n is the number of tetrahedra meeting at a tetrahedral
edge, and θ is the dihedral angle between any 4-blocks meeting at the time-
like hinges located between Cauchy surfaces. It was shown that this equation
satisﬁes the initial value equation at the moment of time symmetry, which, for
4


## Page 5


Λ-FLRW, is the moment of minimum expansion. It was also shown that the
constraint is a ﬁrst integral of the global evolution equation, implying that it
alone is suﬃcient to determine the model’s evolution. The constraint is also
a ﬁrst integral of the local evolution equation but only if we also satisfy the
momentum constraints. Unfortunately, the momentum constraints are actually
unphysical because the diagonals break the Cauchy surface symmetries. Hence,
local variation in the CW formalism is unviable.
The three Regge models’ evolution have been plotted in Fig. 3; for com-
parison, the exact Λ-FLRW solution is also shown. All Regge models correctly
show an inﬁnitely expanding universe, but all models also diverge slowly from
the continuum solution as the universe expands; the divergence is slower though
if the number of tetrahedra is higher. This divergence arises from approximat-
ing an ever-expanding 3-sphere with just a ﬁxed number of tetrahedra: as the
3-sphere expands, the approximation’s resolution degrades, but the degradation
is slower if there are more tetrahedra.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
1
2
3
4
5
6
d(Radius)
dt
Radius(t)
Λ-FLRW
5 tetrahedra
16 tetrahedra
600 tetrahedra
60 tetrahedra
192 tetrahedra
7200 tetrahedra
Figure 3: Evolution of Cauchy surface 3-sphere radii. For continuum Λ-FLRW,
this is simply the scale factor a(t). For the Regge models, we have chosen Z in
(3) so that R(t) = a(t) when ˙R(t) = ˙a(t) = 0.
We can increase the number of tetrahedra by triangulating them into smaller
tetrahedra, but the new tetrahedra will no longer be identical nor necessarily
equilateral.
Brewin [5] has provided one subdivision algorithm that can be
repeated indeﬁnitely on each subsequent generation of child tetrahedra, but we
shall focus only on the ﬁrst-generation children. Subdividing a parent Cauchy
surface generates three diﬀerent types of tetrahedral edges, tetrahedra, vertices,
and struts. We shall simplify the model by setting all strut-lengths to be equal.
This model was also investigated extensively in [7]. The Hamiltonian con-
straint, which we do not show, also satisﬁed the initial value equation at time
symmetry. But the constraint was a ﬁrst integral of the evolution equation only
if all tetrahedra were equilateral; otherwise, it was not a ﬁrst integral in general,
5


## Page 6


and we believe this to be a consequence of constraining all strut-lengths to be
equal. Fig. 3 also shows the children models’ evolution; our earlier remarks for
the parents models apply to the children as well. We also see that the rate of
divergence depends only on the number of tetrahedra, independent of whether
the skeleton is a parent or child.
4
Lattice universes
If massive particles are present, the Einstein–Hilbert and Regge actions become
1
16π
Z
R √−g d4x −
X
i ∈{particles}
Mi
Z
dsi
→
1
8π
X
i ∈{hinges}
Ai δi −
X
i ∈{particles}
j ∈{4-simplices}
Mi sij, (7)
where {Mi} are the particle masses, si the length of particle Mi’s world line,
and sij the length of particle Mi’s world line through 4-block j.
In [8], the CW formalism was adapted to model lattice universes. For each
parent skeleton, there were diﬀerent ways of arranging particles to form lattices,
and it was found that the model’s behaviour depended on the particle’s position
in the tetrahedron. For regular lattices, we obtained the Hamiltonian constraint
l = 8πM Np
N1
tan θ
2

8v2 tan2 θ
2 −1
2 (8v2 −1)
 1
2
1
2π −nθ,
(8)
where Np is the number of particles and v the ratio between the particle’s
distance from the tetrahedron’s centre and the tetrahedron’s edge-length. This
constraint was also a ﬁrst integral of the evolution equation. We see from the
constraint that evolution depends on the particle’s position, parametrised by v,
and it was shown in [8] that the model would only be stable unconditionally if
the particles were within a sphere that just touched the tetrahedral edge mid-
points; this is believed to be an artefact of the Regge approximation rather
than an actual feature of the lattice universes themselves. We shall henceforth
consider only lattices with the particles at the tetrahedral centres.
Fig. 4 shows the evolution of regular lattice universes and of a dust-ﬁlled
FLRW universe; the total mass is the same across all universes. We see that
the lattice universes are closed and stable. They also become more similar to
FLRW as the number of particles increases, and this is because their matter
content is becoming more like homogeneous and isotropic dust.
We can perturb the lattice by changing one mass from M to M + δM. The
skeletal geometry would then get perturbed, but depending on the skeleton,
there could be anywhere from ﬁve to over a hundred independent tetrahedral
edge-lengths. Thus for simplicity, we shall focus only on the ﬁve-tetrahedra
model, which involves just two independent lengths.
The dynamics for this universe was also studied in [8]. It was now assumed
the Hamiltonian constraint would be a ﬁrst integral again of the evolution equa-
tion. A global solution was this time obtained through local variation via the
6


## Page 7


0.0
1.0
2.0
3.0
4.0
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
dU/dt
U(t)
dust-ﬁlled FLRW
5 tetrahedra
16 tetrahedra
600 tetrahedra
Figure 4: Evolution of the universe’s volume U(t) for lattice and dust-ﬁlled
universes. For the Regge models, U(t) is the sum of the tetrahedra’s volumes.
chain rule (4). The perturbed skeleton had two independent struts, so locally
varying them gave two independent constraints in total; these were just enough
equations to solve for the two independent tetrahedral edge-lengths. Had we
directly varied the action globally instead, we would have obtained just one con-
straint, which would not be enough. In eﬀect, the local approach allowed us to
isolate one unique solution from the entire global solution space. However, the
two constraints were two coupled, non-linear diﬀerential equations for the two
edge-lengths; therefore to solve the equations, we linearised them by taking their
perturbative expansion in δM/M up to ﬁrst order. The resulting equations were
solved numerically, using as initial conditions the initial value equation at time
symmetry, satisﬁed order-by-order in δM/M. Fig. 5 shows the model’s evolu-
tion for several perturbations. In all cases, the evolution was stable; increasing
the perturbation only increased the universe’s maximum expansion.
Figure 5: Evolution of the universe’s volume U(t) for various lattice perturba-
tions. The ﬁrst three perturbations are so small that their graphs eﬀectively
overlap each other.
7


## Page 8


5
Conclusions
Comparison with the exact Λ-FLRW solution indicates the CW formalism yields
a reasonable approximation to cosmological space–times. In particular, it re-
liably reproduces the universe’s dynamics, and its accuracy increases with the
number of tetrahedra. It should be especially accurate for closed universes, as
these do not expand indeﬁnitely.
When applied to lattice universes, the formalism shows that both regular
and perturbed universes have closed and stable evolution. Yet we can take this
work further in several ways. Currently, our approximation of each lattice cell
geometry is very coarse-grained, as there is only one independent edge-length
characterising each cell. But by subdividing the tetrahedra, we can introduce
more edges and thereby increase the geometric detail. We can also increase
inhomogeneities by, for instance, having diﬀerent cells with diﬀerent masses or
even leaving some empty altogether. Finally, it would be especially interesting
to investigate the models’ optical properties and redshifts, as this may elucidate
whether inhomogeneities can signiﬁcantly aﬀect cosmological observables.
References
[1] G. F. Smoot et al., Structure in the COBE diﬀerential microwave radiome-
ter ﬁrst-year maps, Astrophys. J. 396 (1992) L1.
[2] G. F. R. Ellis, Inhomogeneity eﬀects in cosmology, Class. Quantum Grav.
28 (2011) 164001 [arXiv:1103.2335].
[3] T. E. Regge, General relativity without coordinates, Il Nuovo Cim. Series
10 9 (1961) 558.
[4] P. A. Collins and R. M. Williams, Dynamics of the Friedmann universe
using Regge calculus, Phys. Rev. D 7 (1973) 965.
[5] L. C. Brewin, Friedmann cosmologies via the Regge calculus, Class. Quan-
tum Grav. 4 (1987) 889.
[6] H. S. M. Coxeter, Regular Polytopes, Methuen and Company, Ltd, London
(1948).
[7] R. G. Liu and R. M. Williams, Regge calculus models of the closed vacuum
Λ-FLRW universe [arXiv:1501.07614].
[8] R. G. Liu and R. M. Williams, Regge calculus models of closed lattice uni-
verses [arXiv:1502.03000].
[9] R. G. Liu, Discrete gravitational approaches to cosmology, Ph.D. thesis,
University of Cambridge, UK (2014).
8

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]